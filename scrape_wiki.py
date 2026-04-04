#!/usr/bin/env -S /home/alex/src/utopiaguide/.venv/bin/python
"""
scrape_wiki.py — Scrape wiki.utopia-game.com from the Wayback Machine
and convert pages to Markdown for a MkDocs Material site.

Usage:
    pip install -r requirements.txt
    python3 scrape_wiki.py

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
    Rewrite <a href> attributes in-place (before markdownify):
    - Wayback Machine links → relative .md paths if the target page was scraped
    - Unresolvable internal links → remove href (keep link text)
    - External links and anchors → leave as-is
    """
    for a in content_div.select("a[href]"):
        href = a.get("href", "")
        if not href or href.startswith("#"):
            continue  # anchor-only, fine as-is

        m = WB_HREF_RE.match(href)
        if not m:
            continue  # not a Wayback link (e.g. already-external)

        wiki_path = m.group(1)  # e.g. /index.php?title=Race
        title = wiki_path_to_title(wiki_path)

        if title and not any(title.startswith(p) for p in SKIP_PREFIXES):
            slug = slugify(title)
            path = page_title_to_path.get(slug)
            if path:
                a["href"] = path
            else:
                # Page not in our scraped set — drop the link, keep text
                a.unwrap()
        else:
            # Unresolvable (Special:, action=edit, etc.) — drop
            a.unwrap()


def rewrite_links(markdown: str) -> str:
    """Final pass: strip any remaining Wayback/wiki URL fragments in markdown text."""
    # Catch any leftover absolute Wayback URLs not cleaned by soup pass
    markdown = re.sub(
        r'https?://web\.archive\.org/web/\d{14}[a-z]*/(?:https?://[^/]*)?',
        "",
        markdown,
        flags=re.IGNORECASE,
    )
    # Catch leftover relative /web/TS/ paths
    markdown = re.sub(r'/web/\d{14}[a-z]*/(?:https?://[^/]*)?', "", markdown)
    # Bare wiki host references
    markdown = markdown.replace("https://wiki.utopia-game.com", "")
    markdown = markdown.replace("http://wiki.utopia-game.com", "")
    return markdown


def html_to_markdown(html_content: str) -> str:
    return md(
        str(html_content),
        heading_style="ATX",
        bullets="-",
        convert=["a", "b", "blockquote", "code", "em", "h1", "h2", "h3",
                 "h4", "h5", "h6", "hr", "i", "img", "li", "ol", "p",
                 "pre", "strong", "table", "td", "th", "tr", "ul"],
    )


def scrape_page(title: str, info: dict, page_title_to_path: dict[str, str]) -> dict | None:
    """
    Fetch a page from the Wayback Machine and return:
        {"title": str, "markdown": str, "categories": [str]}
    or None on failure.
    """
    wb_url = f"{WB_BASE}/{info['timestamp']}/{info['url']}"
    r = fetch(wb_url)
    if not r or r.status_code != 200:
        print(f"  SKIP {title}: HTTP {r.status_code if r else 'error'}")
        return None

    soup = BeautifulSoup(r.text, "html.parser")

    # Page title
    heading = soup.select_one("#firstHeading")
    page_title = heading.get_text(strip=True) if heading else title.replace("_", " ")

    # Categories
    catlinks = soup.select_one("#catlinks")
    categories: list[str] = []
    if catlinks:
        for a in catlinks.select("a"):
            text = a.get_text(strip=True)
            if text and text != "Categories":
                categories.append(text)

    # Main content
    content_div = soup.select_one("#mw-content-text")
    if not content_div:
        print(f"  SKIP {title}: no #mw-content-text")
        return None

    clean_content(content_div)
    rewrite_soup_links(content_div, page_title_to_path)
    markdown = html_to_markdown(content_div)
    markdown = rewrite_links(markdown)
    # Collapse excessive blank lines
    markdown = re.sub(r"\n{3,}", "\n\n", markdown).strip()

    return {"title": page_title, "markdown": markdown, "categories": categories}


# ---------------------------------------------------------------------------
# Phase 3: Organise into docs/ directory
# ---------------------------------------------------------------------------

def safe_filename(title: str) -> str:
    slug = slugify(title)
    # Truncate to 200 chars to avoid filesystem limits
    return slug[:200] + ".md"


def output_path(title: str, categories: list[str]) -> Path:
    if title.startswith(CATEGORY_PREFIX):
        cat_name = title.removeprefix(CATEGORY_PREFIX)
        dirname = category_to_dirname(title)
        return DOCS_DIR / dirname / "index.md"

    if categories:
        dirname = category_to_dirname(CATEGORY_PREFIX + categories[0])
        return DOCS_DIR / dirname / safe_filename(title)

    return DOCS_DIR / "misc" / safe_filename(title)


def write_page(title: str, data: dict) -> Path:
    path = output_path(title, data["categories"])
    path.parent.mkdir(parents=True, exist_ok=True)
    content = f"# {data['title']}\n\n{data['markdown']}\n"
    path.write_text(content, encoding="utf-8")
    return path


# ---------------------------------------------------------------------------
# Phase 4: Generate mkdocs.yml
# ---------------------------------------------------------------------------

def build_nav(docs_dir: Path) -> list:
    """Walk docs/ and build a MkDocs nav list."""
    nav = [{"Home": "index.md"}]

    for section_dir in sorted(docs_dir.iterdir()):
        if not section_dir.is_dir():
            continue
        section_name = section_dir.name.replace("_", " ").title()
        index = section_dir / "index.md"
        pages = sorted(p for p in section_dir.glob("*.md") if p != index)

        if not pages and not index.exists():
            continue

        entries = []
        if index.exists():
            entries.append({section_name: str(index.relative_to(docs_dir))})
        for page in pages:
            label = page.stem.replace("_", " ")
            entries.append({label: str(page.relative_to(docs_dir))})

        if entries:
            nav.append({section_name: entries})

    misc_dir = docs_dir / "misc"
    if misc_dir.exists():
        misc_entries = []
        for page in sorted(misc_dir.glob("*.md")):
            label = page.stem.replace("_", " ")
            misc_entries.append({label: f"misc/{page.name}"})
        if misc_entries:
            nav.append({"Miscellaneous": misc_entries})

    return nav


def write_mkdocs_yml(nav: list) -> None:
    import yaml  # optional — fall back to manual serialisation if not installed

    config = {
        "site_name": SITE_NAME,
        "site_url": SITE_URL,
        "theme": {
            "name": "material",
            "features": [
                "navigation.tabs",
                "navigation.sections",
                "navigation.top",
                "search.suggest",
                "search.highlight",
                "content.code.copy",
            ],
            "palette": [
                {
                    "scheme": "slate",
                    "primary": "deep purple",
                    "accent": "purple",
                    "toggle": {
                        "icon": "material/brightness-4",
                        "name": "Switch to light mode",
                    },
                },
                {
                    "scheme": "default",
                    "primary": "deep purple",
                    "accent": "purple",
                    "toggle": {
                        "icon": "material/brightness-7",
                        "name": "Switch to dark mode",
                    },
                },
            ],
        },
        "plugins": ["search"],
        "nav": nav,
    }

    try:
        import yaml

        with open("mkdocs.yml", "w") as f:
            yaml.dump(config, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
        print("Wrote mkdocs.yml (via PyYAML)")
    except ImportError:
        # Fallback: write a minimal hand-crafted YAML
        _write_mkdocs_yml_manual()
        print("Wrote mkdocs.yml (manual fallback — install PyYAML for full nav)")


def _write_mkdocs_yml_manual() -> None:
    content = f"""\
site_name: {SITE_NAME}
site_url: {SITE_URL}
theme:
  name: material
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.top
    - search.suggest
    - search.highlight
    - content.code.copy
  palette:
    - scheme: slate
      primary: deep purple
      accent: purple
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
    - scheme: default
      primary: deep purple
      accent: purple
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
plugins:
  - search
"""
    with open("mkdocs.yml", "w") as f:
        f.write(content)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def build_title_to_path(pages: dict[str, dict]) -> dict[str, str]:
    """
    Pre-compute a slug→MkDocs-relative-path map so link rewriting can resolve
    targets before each page is individually fetched.

    We don't know categories until we fetch each page, so we use a best-effort
    heuristic: if the file already exists on disk (from a prior run), use that
    path; otherwise assume misc/.
    """
    mapping: dict[str, str] = {}
    for title in pages:
        slug = slugify(title)
        # Check if already downloaded anywhere under docs/
        existing = list(DOCS_DIR.rglob(f"{slug[:200]}.md"))
        if title.startswith(CATEGORY_PREFIX):
            dirname = category_to_dirname(title)
            path = f"/{dirname}/"
        elif existing:
            # Use the path relative to docs/
            rel = existing[0].relative_to(DOCS_DIR)
            path = "/" + str(rel).replace("\\", "/")
        else:
            path = f"/misc/{slug[:200]}.md"
        mapping[slug] = path
    return mapping


def main() -> None:
    DOCS_DIR.mkdir(exist_ok=True)
    (DOCS_DIR / "misc").mkdir(exist_ok=True)

    pages = discover_pages()

    # Build title→path lookup for internal link rewriting
    page_title_to_path = build_title_to_path(pages)

    total = len(pages)
    ok = 0
    skipped = 0

    for i, (title, info) in enumerate(pages.items(), 1):
        # Resume support: skip if already downloaded
        slug = slugify(title)
        existing = list(DOCS_DIR.rglob(f"{slug[:200]}.md"))
        if existing:
            skipped += 1
            continue

        print(f"[{i}/{total}] {title}")
        data = scrape_page(title, info, page_title_to_path)
        if data:
            path = write_page(title, data)
            # Update mapping now that we know the real path
            rel = path.relative_to(DOCS_DIR)
            page_title_to_path[slug] = "/" + str(rel).replace("\\", "/")
            ok += 1
        time.sleep(REQUEST_DELAY)

    print(f"\nDone. Fetched {ok} pages, skipped {skipped} already present.")

    print("Building nav and writing mkdocs.yml…")
    nav = build_nav(DOCS_DIR)
    write_mkdocs_yml(nav)

    print("\nNext steps:")
    print("  pip install mkdocs-material")
    print("  mkdocs serve          # preview at http://localhost:8000")
    print("  # Push to GitHub and enable Pages from the gh-pages branch")


if __name__ == "__main__":
    main()
