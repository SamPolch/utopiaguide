#!/usr/bin/env -S /home/alex/src/utopiaguide/.venv/bin/python
"""
scrape_wiki.py — Scrape wiki.utopia-game.com from the Wayback Machine
and convert pages to Markdown for a MkDocs Material site.

Usage:
    pip install -r requirements.txt
    python3 scripts/scrape_wiki.py

Output:
    docs/              Markdown files organised by category
    mkdocs.yml         Auto-generated MkDocs config (overwritten each run)

Run mkdocs serve to preview, then push to GitHub and enable Pages.
"""

import json
import os
import re
import sys
import time
import unicodedata
import urllib.parse
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

WIKI_HOST = "wiki.utopia-game.com"
CDX_API = "http://web.archive.org/cdx/search/cdx"
WB_BASE = "http://web.archive.org/web"

DOCS_DIR = Path("docs")
SITE_NAME = "Utopia Guide"
# Set to your subdomain, e.g. "https://wiki.example.com/"
SITE_URL = "https://utopiaguide.example.com/"

# Namespaces to skip entirely
SKIP_PREFIXES = (
    "Special:",
    "User:",
    "User_talk:",
    "Talk:",
    "File:",
    "Template:",
    "Template_talk:",
    "Help:",
    "MediaWiki:",
    "MediaWiki_talk:",
    "Image:",
)

# Category prefix — kept but treated as section index pages
CATEGORY_PREFIX = "Category:"

# Rate limit between Wayback Machine requests (seconds)
REQUEST_DELAY = 1.0

SESSION = requests.Session()
SESSION.headers.update(
    {"User-Agent": "utopiaguide-scraper/1.0 (educational archival; contact via github)"}
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def slugify(title: str) -> str:
    """Convert a wiki page title to a safe filename slug."""
    title = urllib.parse.unquote(title)
    title = unicodedata.normalize("NFC", title)
    title = title.replace(" ", "_")
    # Remove characters that are unsafe in filenames
    title = re.sub(r'[<>:"/\\|?*]', "", title)
    return title


def category_to_dirname(cat: str) -> str:
    """Category:Foo_Bar → foo_bar"""
    name = cat.removeprefix(CATEGORY_PREFIX)
    return slugify(name).lower()


def page_title_from_url(url: str) -> str | None:
    """Extract wiki page title from a wiki URL (both /index.php/Title and ?title=Title forms)."""
    parsed = urllib.parse.urlparse(url)
    path = parsed.path

    # /index.php/Page_Title
    m = re.match(r"^/(?:index\.php/|w/index\.php/)(.+)$", path)
    if m:
        return urllib.parse.unquote_plus(m.group(1))

    # ?title=Page_Title
    qs = urllib.parse.parse_qs(parsed.query)
    if "title" in qs:
        return urllib.parse.unquote_plus(qs["title"][0])

    return None


def fetch(url: str, retries: int = 3) -> requests.Response | None:
    for attempt in range(retries):
        try:
            r = SESSION.get(url, timeout=30)
            if r.status_code == 429:
                wait = int(r.headers.get("Retry-After", 10))
                print(f"  Rate limited, waiting {wait}s…")
                time.sleep(wait)
                continue
            return r
        except requests.RequestException as e:
            print(f"  Request error ({e}), attempt {attempt + 1}/{retries}")
            time.sleep(3)
    return None


# ---------------------------------------------------------------------------
# Phase 1: Discover pages via CDX API
# ---------------------------------------------------------------------------

def discover_pages() -> dict[str, dict]:
    """
    Returns a dict keyed by page title with values:
        {"timestamp": "20260121151749", "url": "https://…"}
    Only the *most recent* snapshot per page is kept.
    """
    print("Discovering pages via CDX API…")
    params = {
        "url": f"{WIKI_HOST}/index.php/*",
        "output": "json",
        "fl": "original,timestamp",
        "filter": "statuscode:200",
        "collapse": "urlkey",
    }
    r = fetch(f"{CDX_API}?" + urllib.parse.urlencode(params))
    if not r or r.status_code != 200:
        sys.exit("Failed to fetch CDX index")

    rows = r.json()
    # Also check ?title= form
    params2 = dict(params)
    params2["url"] = f"{WIKI_HOST}/?title=*"
    r2 = fetch(f"{CDX_API}?" + urllib.parse.urlencode(params2))
    rows2 = r2.json() if r2 and r2.status_code == 200 else [["original", "timestamp"]]

    all_rows = rows[1:] + rows2[1:]  # skip header rows

    pages: dict[str, dict] = {}
    for original, timestamp in all_rows:
        title = page_title_from_url(original)
        if not title:
            continue

        # Skip unwanted namespaces
        if any(title.startswith(p) for p in SKIP_PREFIXES):
            continue

        # Keep only the most recent snapshot
        if title not in pages or timestamp > pages[title]["timestamp"]:
            pages[title] = {"timestamp": timestamp, "url": original}

    print(f"  Found {len(pages)} unique pages")
    return pages


# ---------------------------------------------------------------------------
# Phase 2: Fetch & convert a single page
# ---------------------------------------------------------------------------

def clean_content(soup: BeautifulSoup) -> BeautifulSoup:
    """Remove Wayback Machine toolbar, TOC, edit links, etc."""
    for sel in [
        "#wm-ipp-base",        # Wayback toolbar
        "#wm-ipp",
        ".wb-autocomplete-suggestion",
        "#toc",                # MediaWiki TOC (MkDocs generates its own)
        ".toc",
        ".editsection",        # [edit] links next to headings
        "#jump-to-nav",
        ".mw-jump",
        "#siteSub",
        "#contentSub",
    ]:
        for el in soup.select(sel):
            el.decompose()
    return soup


# Matches both absolute (https://web.archive.org/web/TS/...) and relative (/web/TS/...)
# Wayback Machine link rewrites, capturing whatever comes after the wiki host.
WB_HREF_RE = re.compile(
    r'^(?:https?://web\.archive\.org)?/web/\d{14}[a-z]*/(?:https?://[^/]*)?(.*)$',
    re.IGNORECASE,
)


def wiki_path_to_title(path: str) -> str | None:
    """Extract page title from a bare wiki path like /index.php?title=Race or /index.php/Race."""
    parsed = urllib.parse.urlparse(path)
    m = re.match(r'^/(?:index\.php/|w/index\.php/)(.+)$', parsed.path)
    if m:
        return urllib.parse.unquote_plus(m.group(1))
    qs = urllib.parse.parse_qs(parsed.query)
    if "title" in qs:
        title = urllib.parse.unquote_plus(qs["title"][0])
        # Strip action params — only keep clean titles
        if not any(k in qs for k in ("action", "diff", "oldid", "redlink")):
            return title
    return None


def rewrite_soup_links(content_div, page_title_to_path: dict[str, str]) -> None:
    """
    Rewrite all wiki/Wayback hrefs inside the parsed HTML to local Markdown file paths.
    We store relative-ish paths from docs root (e.g. /main/Race.md) for now and make
    them relative after the page is written.
    """
    for a in content_div.select("a[href]"):
        href = a["href"].strip()

        # Skip same-page anchors, mailto, javascript
        if href.startswith("#") or href.startswith("mailto:") or href.startswith("javascript:"):
            continue

        m = WB_HREF_RE.match(href)
        wiki_path = None
        if m:
            wiki_path = m.group(1) or "/"
        elif "wiki.utopia-game.com" in href or href.startswith("/index.php"):
            wiki_path = href

        if not wiki_path:
            continue

        title = wiki_path_to_title(wiki_path)
        if not title or any(title.startswith(p) for p in SKIP_PREFIXES):
            a["href"] = "#"
            continue

        if title in page_title_to_path:
            a["href"] = page_title_to_path[title]
        else:
            # leave a placeholder; we'll fix unresolved links later if possible
            a["href"] = "#"


def html_to_markdown(content_div: BeautifulSoup) -> str:
    """Convert cleaned content HTML to Markdown."""
    return md(
        str(content_div),
        heading_style="ATX",
        bullets="-",
        wrap=False,
    )


def rewrite_links(markdown_text: str) -> str:
    """Final pass to normalize markdown links that point to docs-root absolute paths."""
    # Remove duplicate blank lines / tidy stray spaces
    return markdown_text.replace("\r\n", "\n").replace("\r", "\n")


def pick_output_dir(title: str, categories: list[str]) -> str:
    """
    Choose the destination docs subdirectory based on known categories.
    Falls back to misc/.
    """
    priority = [
        ("Alliance", "alliances"),
        ("Kingdom", "kingdoms"),
        ("Player", "players"),
        ("Tools", "tools"),
        ("Guide", "guide"),
        ("History", "history"),
        ("Formulas", "formulas"),
        ("Mechanics", "main"),
    ]

    for cat in categories:
        bare = cat.removeprefix(CATEGORY_PREFIX)
        for needle, dirname in priority:
            if needle.lower() in bare.lower():
                return dirname

    # Heuristics by title
    t = title.lower()
    if "formula" in t:
        return "formulas"
    if "alliance" in t:
        return "alliances"
    if "kingdom" in t:
        return "kingdoms"
    if "player" in t:
        return "players"

    return "misc"


def build_title_to_path(pages: dict[str, dict]) -> dict[str, str]:
    """
    Map wiki page title -> docs-root absolute markdown path, e.g.
    'Race' -> '/main/Race.md'
    """
    mapping = {}
    for title in pages.keys():
        dirname = "misc"  # initial default; corrected again during actual fetch if categories suggest otherwise
        filename = slugify(title) + ".md"
        mapping[title] = f"/{dirname}/{filename}"
    return mapping


def fetch_and_convert_page(title: str, info: dict, page_title_to_path: dict[str, str]) -> dict | None:
    ts = info["timestamp"]
    original_url = info["url"]
    wb_url = f"{WB_BASE}/{ts}/{original_url}"

    print(f"Fetching {title!r} [{ts}]")
    r = fetch(wb_url)
    if not r or r.status_code != 200:
        print(f"  Failed: status {r.status_code if r else 'ERR'}")
        return None

    soup = BeautifulSoup(r.text, "html.parser")

    heading = soup.select_one("#firstHeading")
    page_title = heading.get_text(strip=True) if heading else title

    # Categories
    catlinks = soup.select_one("#catlinks")
    categories = []
    if catlinks:
        for a in catlinks.select("a"):
            text = a.get_text(strip=True)
            if text and text != "Categories":
                categories.append(text)

    out_dir = pick_output_dir(page_title, categories)
    filename = slugify(page_title) + ".md"
    out_path = DOCS_DIR / out_dir / filename

    # Update mapping with actual path now that we know category
    page_title_to_path[title] = f"/{out_dir}/{filename}"
    page_title_to_path[page_title] = f"/{out_dir}/{filename}"

    content_div = soup.select_one("#mw-content-text") or soup.select_one("#bodyContent")
    if not content_div:
        print("  No content found")
        return None

    clean_content(content_div)
    rewrite_soup_links(content_div, page_title_to_path)
    markdown = html_to_markdown(content_div)
    markdown = rewrite_links(markdown)

    # Ensure title heading at top
    markdown = f"# {page_title}\n\n{markdown}".strip() + "\n"

    return {
        "title": page_title,
        "categories": categories,
        "out_dir": out_dir,
        "out_path": out_path,
        "markdown": markdown,
    }


# ---------------------------------------------------------------------------
# Phase 3: Write files and generate nav
# ---------------------------------------------------------------------------

def write_page(page: dict) -> None:
    page["out_path"].parent.mkdir(parents=True, exist_ok=True)
    page["out_path"].write_text(page["markdown"], encoding="utf-8")


def nav_title_from_filename(md_path: Path) -> str:
    return md_path.stem.replace("_", " ")


def generate_nav() -> list:
    """
    Build a fairly flat nav grouped by top-level docs directories.
    """
    groups = [
        ("Main", "main"),
        ("Guide", "guide"),
        ("Formulas", "formulas"),
        ("History", "history"),
        ("Alliances", "alliances"),
        ("Kingdoms", "kingdoms"),
        ("Players", "players"),
        ("Tools", "tools"),
        ("Misc", "misc"),
    ]

    nav = []
    for label, dirname in groups:
        dir_path = DOCS_DIR / dirname
        if not dir_path.exists():
            continue
        items = []
        for md_file in sorted(dir_path.glob("*.md")):
            items.append({nav_title_from_filename(md_file): f"{dirname}/{md_file.name}"})
        if items:
            nav.append({label: items})
    return nav


def write_mkdocs_yaml(nav: list) -> None:
    """
    Keep mkdocs.yml simple; preserve site_name/site_url and replace nav.
    """
    mkdocs = {
        "site_name": SITE_NAME,
        "site_url": SITE_URL,
        "theme": {
            "name": "material",
            "features": [
                "navigation.instant",
                "navigation.sections",
                "search.highlight",
            ],
        },
        "markdown_extensions": [
            "tables",
            "admonition",
            "attr_list",
            "md_in_html",
        ],
        "nav": nav,
    }

    try:
        import yaml
    except ImportError:
        sys.exit("Please install pyyaml: pip install pyyaml")

    Path("mkdocs.yml").write_text(
        yaml.safe_dump(mkdocs, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )


def main():
    DOCS_DIR.mkdir(exist_ok=True)

    pages = discover_pages()

    # First-pass title→path map (rough)
    page_title_to_path = build_title_to_path(pages)

    converted_pages = []
    for i, (title, info) in enumerate(sorted(pages.items()), start=1):
        page = fetch_and_convert_page(title, info, page_title_to_path)
        if page:
            converted_pages.append(page)
            write_page(page)
        time.sleep(REQUEST_DELAY)

    print(f"\nConverted {len(converted_pages)} pages.")

    nav = generate_nav()
    write_mkdocs_yaml(nav)
    print("Wrote mkdocs.yml")

    # Save a simple crawl manifest for debugging
    manifest = [
        {
            "title": p["title"],
            "path": str(p["out_path"]),
            "categories": p["categories"],
        }
        for p in converted_pages
    ]
    Path("scrape_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print("Wrote scrape_manifest.json")


if __name__ == "__main__":
    main()
