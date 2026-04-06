#!/usr/bin/env -S /home/alex/src/utopiaguide/.venv/bin/python
"""
rescrape_broken.py — Re-fetch pages that were saved as wikitext source views
instead of rendered HTML, by trying multiple Wayback Machine snapshots.

Usage:
    .venv/bin/python scripts/rescrape_broken.py
"""

import re
import sys
import time
import urllib.parse
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

sys.path.insert(0, str(Path(__file__).parent))
from scrape_wiki import (
    DOCS_DIR, CDX_API, WB_BASE, WIKI_HOST, REQUEST_DELAY,
    clean_content, rewrite_soup_links, html_to_markdown, rewrite_links,
    slugify, build_title_to_path,
)

SESSION = requests.Session()
SESSION.headers.update(
    {"User-Agent": "utopiaguide-scraper/1.0 (educational archival; contact via github)"}
)


def is_bad_page(soup: BeautifulSoup) -> bool:
    """Return True for source views, diff views, or other non-article pages."""
    heading = soup.select_one("#firstHeading")
    if heading:
        h = heading.get_text()
        if "View source" in h or "Difference between revisions" in h or "Revision history" in h:
            return True
    if soup.select_one("textarea#wpTextbox1"):
        return True
    # Diff tables
    if soup.select_one("table.diff"):
        return True
    return False


def get_all_timestamps(title: str) -> list[str]:
    """Fetch all Wayback Machine timestamps for a page title, newest first."""
    # Wiki uses underscores for spaces; try both encodings
    underscored = title.replace(" ", "_")
    # CDX stores underscores literally; only encode special chars like & , ( )
    encoded_us = urllib.parse.quote(underscored, safe="_")
    encoded_sp = urllib.parse.quote(title, safe=" ")  # fallback with spaces
    urls_to_try = [
        f"{WIKI_HOST}/index.php/{encoded_us}",
        f"{WIKI_HOST}/index.php?title={encoded_us}",
        f"{WIKI_HOST}/index.php/{encoded_sp}",
        f"{WIKI_HOST}/index.php?title={encoded_sp}",
    ]
    timestamps = {}
    for url_pat in urls_to_try:
        params = {
            "url": url_pat,
            "output": "json",
            "fl": "timestamp,original",
            "filter": "statuscode:200",
        }
        try:
            r = SESSION.get(f"{CDX_API}?" + urllib.parse.urlencode(params), timeout=20)
            for ts, orig in r.json()[1:]:
                timestamps[ts] = orig
        except Exception:
            pass
    return sorted(timestamps.items(), reverse=True)  # newest first


def fetch_rendered(title: str) -> tuple[BeautifulSoup, str] | None:
    """
    Try Wayback Machine snapshots newest-first until we get a rendered page
    (not a view-source page). Returns (soup, timestamp) or None.
    """
    snapshots = get_all_timestamps(title)
    if not snapshots:
        print(f"  No snapshots found for {title!r}")
        return None

    for ts, original_url in snapshots:
        wb_url = f"{WB_BASE}/{ts}/{original_url}"
        try:
            r = SESSION.get(wb_url, timeout=30)
        except requests.RequestException as e:
            print(f"  Error fetching {ts}: {e}")
            time.sleep(2)
            continue

        if r.status_code != 200:
            continue

        soup = BeautifulSoup(r.text, "html.parser")
        if is_bad_page(soup):
            print(f"  {ts}: source view, trying older…")
            time.sleep(0.5)
            continue

        content = (
            soup.select_one("#mw-content-text")
            or soup.select_one("#bodyContent")
        )
        if not content or not content.get_text(strip=True):
            continue

        print(f"  {ts}: rendered OK")
        return soup, ts

    return None


def rescrape_page(md_file: Path, page_title_to_path: dict) -> bool:
    # Derive the wiki page title from the filename / file contents
    text = md_file.read_text(encoding="utf-8")
    # First heading gives us the title
    m = re.match(r'^#\s+(.+)$', text, re.MULTILINE)
    raw_title = m.group(1).strip() if m else md_file.stem.replace("_", " ")
    # Strip MediaWiki page-variant prefixes
    raw_title = re.sub(r'^View source for\s+', '', raw_title, flags=re.IGNORECASE)
    raw_title = re.sub(r'^Difference between revisions of\s+"?', '', raw_title, flags=re.IGNORECASE)
    raw_title = re.sub(r'^Revision history of\s+"?', '', raw_title, flags=re.IGNORECASE)
    raw_title = raw_title.rstrip('"')
    title = raw_title

    print(f"Re-scraping: {title!r}")
    result = fetch_rendered(title)
    if not result:
        print(f"  FAILED — no good snapshot found")
        return False

    soup, ts = result

    heading = soup.select_one("#firstHeading")
    page_title = heading.get_text(strip=True) if heading else title

    catlinks = soup.select_one("#catlinks")
    categories = []
    if catlinks:
        for a in catlinks.select("a"):
            t = a.get_text(strip=True)
            if t and t != "Categories":
                categories.append(t)

    content_div = soup.select_one("#mw-content-text") or soup.select_one("#bodyContent")
    clean_content(content_div)
    rewrite_soup_links(content_div, page_title_to_path)
    markdown = html_to_markdown(content_div)
    markdown = rewrite_links(markdown)
    markdown = re.sub(r"\n{3,}", "\n\n", markdown).strip()

    md_file.write_text(f"# {page_title}\n\n{markdown}\n", encoding="utf-8")
    print(f"  Saved to {md_file}")
    return True


def main():
    # Find all docs with wikitext source content
    broken = [
        f for f in sorted(DOCS_DIR.rglob("*.md"))
        if re.search(
            r"View source for|You do not have permission to edit|^# Difference between revisions|^# Revision history of",
            f.read_text(),
            re.MULTILINE,
        )
    ]

    if not broken:
        print("No broken pages found.")
        return

    print(f"Found {len(broken)} pages with wikitext source content.\n")

    # Build link lookup from existing files
    pages_stub = {
        f.stem: {"timestamp": "0", "url": ""}
        for f in DOCS_DIR.rglob("*.md")
    }
    page_title_to_path = build_title_to_path(pages_stub)

    ok = 0
    for md_file in broken:
        if rescrape_page(md_file, page_title_to_path):
            ok += 1
        time.sleep(REQUEST_DELAY)

    print(f"\nDone. Successfully re-scraped {ok}/{len(broken)} pages.")
    if ok < len(broken):
        print("Run scripts/fix_links.py afterwards to clean up any new links.")


if __name__ == "__main__":
    main()
