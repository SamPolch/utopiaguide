#!/usr/bin/env python3

"""Compare archived forum age-change threads against local age docs.

This script queries Wayback for a vBulletin forumdisplay page, fetches one
archived snapshot per available forum page number, extracts thread titles from
the archived HTML, and compares discovered age/final-change threads against the
local docs/history/Age_*.md coverage.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path


DEFAULT_FORUM_URL = (
    "https://forums.utopia-game.com/forumdisplay.php?1585-Game-Announcements"
)


@dataclass(frozen=True)
class ThreadMatch:
    page: int
    age: int | None
    title: str
    url: str


class ThreadLinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[tuple[str, str]] = []
        self._href: str | None = None
        self._text_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a":
            return
        href = dict(attrs).get("href")
        if href and "showthread.php?" in href:
            self._href = href
            self._text_parts = []

    def handle_data(self, data: str) -> None:
        if self._href is not None:
            self._text_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() != "a" or self._href is None:
            return
        title = " ".join("".join(self._text_parts).split())
        if title:
            self.links.append((html.unescape(self._href), html.unescape(title)))
        self._href = None
        self._text_parts = []


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compare archived age-change threads against local age docs."
    )
    parser.add_argument(
        "url",
        nargs="?",
        default=DEFAULT_FORUM_URL,
        help=f"Forumdisplay URL (default: {DEFAULT_FORUM_URL})",
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=Path("/tmp/utopia-wayback-forum-cache"),
        help="Directory for cached archived forum pages.",
    )
    parser.add_argument(
        "--retries",
        type=int,
        default=3,
        help="Retry count for each archived page fetch (default: 3).",
    )
    parser.add_argument(
        "--retry-delay",
        type=float,
        default=2.0,
        help="Initial retry delay in seconds (default: 2.0).",
    )
    parser.add_argument(
        "--pages",
        help="Optional comma-separated page numbers to restrict the scan.",
    )
    return parser.parse_args()


def build_cdx_url(forum_url: str) -> tuple[str, str]:
    parsed = urllib.parse.urlparse(forum_url)
    if "forumdisplay.php" not in parsed.path:
        raise ValueError("URL does not look like a vBulletin forumdisplay URL.")
    if not parsed.query:
        raise ValueError("URL is missing the forumdisplay query component.")

    wildcard_url = urllib.parse.urlunparse(
        (
            parsed.scheme or "https",
            parsed.netloc,
            parsed.path,
            "",
            f"{parsed.query}*",
            "",
        )
    )
    cdx_query = urllib.parse.urlencode(
        {
            "url": wildcard_url,
            "output": "json",
            "fl": "timestamp,original,statuscode",
            "filter": "statuscode:200",
        }
    )
    return parsed.query, f"https://web.archive.org/cdx/search/cdx?{cdx_query}"


def fetch_json(url: str) -> list[list[str]]:
    with urllib.request.urlopen(url, timeout=30) as response:
        return json.load(response)


def latest_snapshot_per_page(rows: list[list[str]]) -> dict[int, tuple[str, str]]:
    page_to_snap: dict[int, tuple[str, str]] = {}
    for timestamp, original, _status in rows[1:]:
        match = re.search(r"1585-Game-Announcements(?:/page(\d+))?", original)
        page = int(match.group(1)) if match and match.group(1) else 1
        current = page_to_snap.get(page)
        if current is None or timestamp > current[0]:
            page_to_snap[page] = (timestamp, original)
    return page_to_snap


def fetch_with_cache(
    url: str,
    cache_path: Path,
    retries: int,
    retry_delay: float,
) -> str:
    if cache_path.exists():
        return cache_path.read_text(encoding="utf-8", errors="ignore")

    cache_path.parent.mkdir(parents=True, exist_ok=True)
    attempt = 1
    delay = retry_delay
    last_error: Exception | None = None

    while attempt <= retries:
        try:
            with urllib.request.urlopen(url, timeout=30) as response:
                html_text = response.read().decode("utf-8", "ignore")
            cache_path.write_text(html_text, encoding="utf-8")
            return html_text
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            if attempt >= retries:
                break
            time.sleep(delay)
            delay *= 2
            attempt += 1

    raise RuntimeError(f"failed to fetch {url}: {last_error}") from last_error


def extract_matches(page: int, html_text: str) -> list[ThreadMatch]:
    parser = ThreadLinkParser()
    parser.feed(html_text)
    patterns = [
        re.compile(r"\bAge\s*(\d+)\b", re.I),
        re.compile(r"\bAge-(\d+)\b", re.I),
    ]
    terms = (
        "final changes",
        "age changes",
        "changes for next age",
        "age change",
        "age-end changes",
        "genesis age",
    )

    results: dict[tuple[int | None, str, str], ThreadMatch] = {}
    for href, title in parser.links:
        lowered = title.lower()
        if "age" not in lowered or not any(term in lowered for term in terms):
            continue

        age = None
        for pattern in patterns:
            match = pattern.search(title)
            if match:
                age = int(match.group(1))
                break

        if href.startswith("http"):
            full_url = href.split("&", 1)[0]
        else:
            full_url = ("https://forums.utopia-game.com/" + href.lstrip("./")).split(
                "&", 1
            )[0]

        key = (age, title, full_url)
        results[key] = ThreadMatch(page=page, age=age, title=title, url=full_url)

    return sorted(results.values(), key=lambda item: ((item.age or 9999), item.title))


def existing_ages() -> set[int]:
    return {
        int(path.stem.split("_")[1])
        for path in Path("docs/history").glob("Age_*.md")
    }


def parse_page_filter(raw: str | None) -> set[int] | None:
    if not raw:
        return None
    values = set()
    for part in raw.split(","):
        part = part.strip()
        if not part:
            continue
        values.add(int(part))
    return values


def main() -> int:
    args = parse_args()
    page_filter = parse_page_filter(args.pages)

    try:
        forum_query, cdx_url = build_cdx_url(args.url)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    rows = fetch_json(cdx_url)
    page_to_snap = latest_snapshot_per_page(rows)
    local_ages = existing_ages()

    all_matches: dict[tuple[int | None, str, str], ThreadMatch] = {}

    for page in sorted(page_to_snap):
        if page_filter is not None and page not in page_filter:
            continue

        timestamp, original = page_to_snap[page]
        wb_url = f"https://web.archive.org/web/{timestamp}/{original}"
        cache_path = args.cache_dir / f"page-{page}-{timestamp}.html"
        print(f"PAGE {page} {wb_url}", file=sys.stderr)

        try:
            html_text = fetch_with_cache(
                wb_url,
                cache_path=cache_path,
                retries=args.retries,
                retry_delay=args.retry_delay,
            )
        except RuntimeError as exc:
            print(f"FETCH_FAIL\tpage={page}\t{exc}", file=sys.stderr)
            continue

        for match in extract_matches(page, html_text):
            key = (match.age, match.title, match.url)
            all_matches[key] = match

    print(f"Forum URL: {args.url}")
    print(f"Archived pages scanned: {len(page_to_snap) if page_filter is None else len(page_filter)}")
    print(f"Discovered age-change threads: {len(all_matches)}")
    print()

    missing: list[ThreadMatch] = []
    for match in sorted(
        all_matches.values(),
        key=lambda item: ((item.age is None), item.age or 9999, item.title.lower()),
    ):
        status = "HAS_DOC" if match.age in local_ages else "MISSING_DOC"
        print(
            f"{status}\tpage={match.page}\tage={match.age}\t{match.title}\t{match.url}"
        )
        if status == "MISSING_DOC":
            missing.append(match)

    print()
    print(f"MISSING_COUNT\t{len(missing)}")
    for match in missing:
        print(f"page={match.page}\tage={match.age}\t{match.title}\t{match.url}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
