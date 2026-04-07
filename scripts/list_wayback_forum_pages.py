#!/usr/bin/env python3

"""List Wayback coverage for a vBulletin forumdisplay page.

Given a Utopia forumdisplay URL, query the Internet Archive CDX API and
summarize how many archived captures exist for each forum page number.
This is useful for assessing whether older paginated forum indexes are
recoverable before trying to scrape individual threads.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Summarize Wayback coverage for a vBulletin forumdisplay URL."
    )
    parser.add_argument(
        "url",
        help=(
            "Forumdisplay URL, for example "
            "https://forums.utopia-game.com/forumdisplay.php?1585-Game-Announcements"
        ),
    )
    parser.add_argument(
        "--limit-examples",
        type=int,
        default=2,
        help="How many sample originals to print per page number (default: 2).",
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=Path("/tmp/utopia-wayback-cdx-cache"),
        help="Directory for cached CDX query results.",
    )
    parser.add_argument(
        "--retries",
        type=int,
        default=3,
        help="Retry count for the CDX request (default: 3).",
    )
    parser.add_argument(
        "--retry-delay",
        type=float,
        default=2.0,
        help="Initial retry delay in seconds (default: 2.0).",
    )
    return parser.parse_args()


def build_cdx_url(forum_url: str) -> str:
    parsed = urllib.parse.urlparse(forum_url)
    if "forumdisplay.php" not in parsed.path:
      raise ValueError("URL does not look like a vBulletin forumdisplay URL.")

    query = urllib.parse.parse_qs(parsed.query, keep_blank_values=True)
    if not query:
      raise ValueError("URL is missing the forumdisplay query component.")

    forum_slug = parsed.query
    wildcard_url = urllib.parse.urlunparse(
        (
            parsed.scheme or "https",
            parsed.netloc,
            parsed.path,
            "",
            f"{forum_slug}*",
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
    return f"https://web.archive.org/cdx/search/cdx?{cdx_query}"


def page_number_from_original(original: str, forum_query: str) -> int | None:
    match = re.search(re.escape(forum_query) + r"(?:/page(\d+))?", original)
    if not match:
        return None
    if match.group(1):
        return int(match.group(1))
    return 1


def fetch_rows(
    cdx_url: str,
    cache_dir: Path,
    retries: int,
    retry_delay: float,
) -> list[list[str]]:
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache_name = urllib.parse.quote_plus(cdx_url) + ".json"
    cache_path = cache_dir / cache_name

    if cache_path.exists():
        return json.loads(cache_path.read_text(encoding="utf-8"))[1:]

    delay = retry_delay
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            with urllib.request.urlopen(cdx_url, timeout=30) as response:
                data = json.load(response)
            cache_path.write_text(json.dumps(data), encoding="utf-8")
            return data[1:]
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            if attempt >= retries:
                break
            time.sleep(delay)
            delay *= 2

    raise RuntimeError(f"failed to fetch CDX results: {last_error}") from last_error


def main() -> int:
    args = parse_args()
    parsed = urllib.parse.urlparse(args.url)
    forum_query = parsed.query

    try:
        cdx_url = build_cdx_url(args.url)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    try:
        rows = fetch_rows(
            cdx_url,
            cache_dir=args.cache_dir,
            retries=args.retries,
            retry_delay=args.retry_delay,
        )
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    if not rows:
        print("No archived 200 responses found.")
        return 0

    page_counts: Counter[int] = Counter()
    examples: defaultdict[int, list[tuple[str, str]]] = defaultdict(list)

    for timestamp, original, _status in rows:
        page = page_number_from_original(original, forum_query)
        if page is None:
            continue
        page_counts[page] += 1
        if len(examples[page]) < args.limit_examples:
            examples[page].append((timestamp, original))

    if not page_counts:
        print("No paginated forumdisplay URLs matched after normalization.")
        return 0

    print(f"Forum URL: {args.url}")
    print(f"Archived 200 snapshots: {len(rows)}")
    print(f"Distinct page numbers: {len(page_counts)}")
    print(f"Page range: {min(page_counts)}-{max(page_counts)}")
    print()

    for page in sorted(page_counts):
        print(f"page {page}: {page_counts[page]} capture(s)")
        for timestamp, original in examples[page]:
            print(f"  {timestamp} {original}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
