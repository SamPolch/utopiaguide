#!/usr/bin/env python3

"""Extract the first forum post from saved Utopia forum HTML.

This is intended for vBulletin pages saved from the official Utopia forums.
It converts the first post body into plain text so the content can be merged
into local docs without repeatedly hand-cleaning HTML.
"""

from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path


POST_PATTERNS = [
    re.compile(
        r'<blockquote class="postcontent restore ">(.*?)</blockquote>',
        re.S,
    ),
    re.compile(
        r'<div id="post_message_\d+">(.*?)</div>',
        re.S,
    ),
]


def extract_first_post(raw_html: str) -> str:
    body = None
    for pattern in POST_PATTERNS:
        match = pattern.search(raw_html)
        if match:
            body = match.group(1)
            break

    if body is None:
        raise ValueError("Could not find a forum post body in the HTML input.")

    body = re.sub(r"<br\s*/?>", "\n", body, flags=re.I)
    body = re.sub(r"</(p|div|li|tr|h[1-6]|blockquote)>", "\n", body, flags=re.I)
    body = re.sub(r"<[^>]+>", "", body)
    body = html.unescape(body)
    body = body.replace("\r", "")
    body = re.sub(r"\n[ \t]+\n", "\n\n", body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body.strip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract the first forum post from saved Utopia forum HTML."
    )
    parser.add_argument("input", type=Path, help="Path to saved forum HTML file")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Output text file path. Defaults to input path with .txt suffix.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source = args.input
    target = args.output or source.with_suffix(".txt")

    raw_html = source.read_text(encoding="utf-8", errors="ignore")
    try:
        text = extract_first_post(raw_html)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    print(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
