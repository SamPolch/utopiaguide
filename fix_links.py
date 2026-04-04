#!/usr/bin/env -S /home/alex/src/utopiaguide/.venv/bin/python
"""
fix_links.py — Post-process already-scraped docs/ to fix Wayback Machine links.

Run once after the initial scrape if links are broken:
    .venv/bin/python fix_links.py

Safe to re-run; idempotent.
"""

import os
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


def build_slug_to_path() -> dict[str, Path]:
    """Scan docs/ and build {slug: absolute_Path} from existing files."""
    mapping: dict[str, Path] = {}
    for md_file in DOCS_DIR.rglob("*.md"):
        stem = md_file.stem
        mapping[stem] = md_file
        mapping[slugify(stem)] = md_file
    return mapping


def relative_link(from_file: Path, to_file: Path) -> str:
    """Return a relative path from from_file's directory to to_file, usable in Markdown."""
    rel = os.path.relpath(to_file, from_file.parent)
    return rel.replace("\\", "/")


SKIP_PREFIXES = (
    "Special:", "User:", "User_talk:", "Talk:", "File:",
    "Template:", "Template_talk:", "Help:", "MediaWiki:", "Image:",
)


def fix_file(path: Path, slug_to_path: dict[str, Path]) -> int:
    text = path.read_text(encoding="utf-8")
    original = text

    def replace_wb_link(m: re.Match) -> str:
        wiki_path = m.group(1)  # e.g. /index.php?title=Race
        title = title_from_wiki_path(wiki_path)
        if not title or any(title.startswith(p) for p in SKIP_PREFIXES):
            return "(#)"
        slug = slugify(title)
        target_file = slug_to_path.get(slug) or slug_to_path.get(title.replace(" ", "_"))
        if target_file:
            return f"({relative_link(path, target_file)})"
        return "(#)"

    text = WB_LINK_RE.sub(replace_wb_link, text)

    # Fix bare /index.php?title=Foo or /index.php/Foo links (no Wayback prefix)
    def fix_bare_wiki_link(m: re.Match) -> str:
        wiki_path = m.group(1)
        title = title_from_wiki_path(wiki_path)
        if not title or any(title.startswith(p) for p in SKIP_PREFIXES):
            return "(#)"
        slug = slugify(title)
        target_file = slug_to_path.get(slug) or slug_to_path.get(title.replace(" ", "_"))
        if target_file:
            return f"({relative_link(path, target_file)})"
        return "(#)"

    text = re.sub(r'\((/index\.php[^\s\)#"]*)\)', fix_bare_wiki_link, text)

    # Fix any already-rewritten absolute /dir/page.md links (from previous run)
    def fix_absolute_link(m: re.Match) -> str:
        abs_path = m.group(1)  # e.g. /misc/Race.md
        target_file = DOCS_DIR / abs_path.lstrip("/")
        if target_file.exists():
            return f"({relative_link(path, target_file)})"
        return m.group(0)  # leave unchanged

    # Match absolute /path.md with optional "title" attribute
    text = re.sub(r'\((/[^\s\)#"]+\.md)(?:\s+"[^"]*")?\)', fix_absolute_link, text)

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

    # Convert any remaining [[wikitext links]]
    text = convert_wikilinks(text, path, slug_to_path)

    if text != original:
        path.write_text(text, encoding="utf-8")
        return 1
    return 0


WIKILINK_RE = re.compile(r'\[\[([^\]|#]+)(?:#([^\]|]*))?(?:\|([^\]]*))?\]\]')


def convert_wikilinks(text: str, from_file: Path, slug_to_path: dict[str, Path]) -> str:
    """Convert remaining [[WikiLink|Display]] syntax to Markdown links."""
    def replace(m: re.Match) -> str:
        page = m.group(1).strip()
        anchor = m.group(2)  # may be None
        display = m.group(3).strip() if m.group(3) else page

        # Strip bold/italic markup from display text
        display = re.sub(r"'{2,3}", "", display).strip()

        # Category declarations → remove entirely
        if page.startswith("Category:") and not m.group(3):
            return ""

        slug = slugify(page.replace(" ", "_"))
        target_file = slug_to_path.get(slug) or slug_to_path.get(slugify(page))
        if target_file:
            rel = relative_link(from_file, target_file)
            if anchor:
                # MkDocs lowercases and slugifies anchors
                anchor_slug = re.sub(r'[^\w-]', '-', anchor.lower()).strip('-')
                rel = f"{rel}#{anchor_slug}"
            return f"[{display}]({rel})"

        # Page not found — just use display text as plain text
        return display

    return WIKILINK_RE.sub(replace, text)


def main() -> None:
    slug_to_path = build_slug_to_path()
    print(f"Found {len(slug_to_path)} page slugs in docs/")

    changed = 0
    for md_file in sorted(DOCS_DIR.rglob("*.md")):
        changed += fix_file(md_file, slug_to_path)

    print(f"Fixed links in {changed} files.")


if __name__ == "__main__":
    main()
