#!/usr/bin/env python3
"""
fix_links.py — Post-process already-scraped docs/ to fix Wayback Machine links.

Run once after the initial scrape if links are broken:
    .venv/bin/python fix_links.py

Safe to re-run; idempotent.
"""

import re
import urllib.parse
from pathlib import Path

DOCS_DIR = Path("docs")

# Matches both:
#   /web/20190811021820/http://wiki.utopia-game.com/index.php?title=Race
#   https://web.archive.org/web/20190811021820/http://wiki.utopia-game.com/index.php?title=Race
# inside a Markdown link: [text](URL) or [text](URL "title")
WB_LINK_RE = re.compile(
    r'\((?:https?://web\.archive\.org)?/web/\d{14}[a-z]*/(?:https?://[^/]*)?(.*?)(?:\s+"[^"]*")?\)',
    re.IGNORECASE,
)

WIKI_PATH_RE = re.compile(
    r'(?:https?://wiki\.utopia-game\.com)?(/index\.php(?:/|\?title=)[^\s\)#"]+)',
    re.IGNORECASE,
)


def title_from_wiki_path(path: str) -> str | None:
    parsed = urllib.parse.urlparse(path)
    m = re.match(r'^/index\.php/(.+)$', parsed.path)
    if m:
        return urllib.parse.unquote_plus(m.group(1))
    qs = urllib.parse.parse_qs(parsed.query)
    if "title" in qs:
        # Skip action= links (edit, history, etc.)
        if not any(k in qs for k in ("action", "diff", "oldid", "redlink")):
            return urllib.parse.unquote_plus(qs["title"][0])
    return None


def slugify(title: str) -> str:
    title = urllib.parse.unquote(title)
    title = title.replace(" ", "_")
    title = re.sub(r'[<>:"/\\|?*]', "", title)
    return title[:200]


def build_slug_to_path() -> dict[str, str]:
    """Scan docs/ and build {slug: mkdocs_abs_path} from existing files."""
    mapping: dict[str, str] = {}
    for md_file in DOCS_DIR.rglob("*.md"):
        rel = md_file.relative_to(DOCS_DIR)
        stem = md_file.stem
        mapping[stem] = "/" + str(rel).replace("\\", "/")
        # Also map a slugified version of the display name (for case/space variants)
        mapping[slugify(stem)] = "/" + str(rel).replace("\\", "/")
    return mapping


SKIP_PREFIXES = (
    "Special:", "User:", "User_talk:", "Talk:", "File:",
    "Template:", "Template_talk:", "Help:", "MediaWiki:", "Image:",
)


def fix_file(path: Path, slug_to_path: dict[str, str]) -> int:
    text = path.read_text(encoding="utf-8")
    original = text

    def replace_wb_link(m: re.Match) -> str:
        wiki_path = m.group(1)  # e.g. /index.php?title=Race
        title = title_from_wiki_path(wiki_path)
        if not title or any(title.startswith(p) for p in SKIP_PREFIXES):
            # Drop the link href — replace (URL) with nothing, making [text] plain
            # We keep the bracket text by returning an empty href
            return "(#)"
        slug = slugify(title)
        target = slug_to_path.get(slug) or slug_to_path.get(title.replace(" ", "_"))
        if target:
            return f"({target})"
        return "(#)"

    text = WB_LINK_RE.sub(replace_wb_link, text)

    # Also catch any bare wiki URLs left in the text (not inside Markdown links)
    text = re.sub(
        r'https?://web\.archive\.org/web/\d{14}[a-z]*/(?:https?://[^/]*)?',
        "",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(r'/web/\d{14}[a-z]*/(?:https?://[^/]*)?', "", text)
    text = text.replace("https://wiki.utopia-game.com", "")
    text = text.replace("http://wiki.utopia-game.com", "")

    if text != original:
        path.write_text(text, encoding="utf-8")
        return 1
    return 0


def main() -> None:
    slug_to_path = build_slug_to_path()
    print(f"Found {len(slug_to_path)} page slugs in docs/")

    changed = 0
    for md_file in sorted(DOCS_DIR.rglob("*.md")):
        changed += fix_file(md_file, slug_to_path)

    print(f"Fixed links in {changed} files.")


if __name__ == "__main__":
    main()
