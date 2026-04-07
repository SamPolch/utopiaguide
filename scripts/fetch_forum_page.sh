#!/usr/bin/env bash

set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  scripts/fetch_forum_page.sh <url> [-o output.html] [--cookie '...'] [--referer <url>]
                             [--timeout seconds] [--retries count]
                             [--retry-delay seconds] [--dump-headers file]

Fetch a page from forums.utopia-game.com using the header set that has
worked for the historical age-post recovery work.

Notes:
- This script intentionally does not store live forum cookies in the repo.
- Provide cookies with --cookie or the UTOPIA_FORUM_COOKIE environment variable.
- Output goes to stdout unless -o is provided.
- Retries are useful because the forum often hangs or returns "server busy".

Examples:
  UTOPIA_FORUM_COOKIE='bb_sessionhash=...; userpwd=...' \
    scripts/fetch_forum_page.sh \
    'https://forums.utopia-game.com/forumdisplay.php?1585-Game-Announcements&page=1' \
    -o /tmp/game-announcements-page1.html

  scripts/fetch_forum_page.sh \
    'https://forums.utopia-game.com/showthread.php?640502-Final-Changes-Age-113' \
    --cookie 'bb_sessionhash=...; userpwd=...'

  scripts/fetch_forum_page.sh \
    'https://forums.utopia-game.com/forumdisplay.php?1585-Game-Announcements&page=1' \
    --timeout 20 \
    --retries 4 \
    --retry-delay 3 \
    --dump-headers /tmp/forum-headers.txt \
    -o /tmp/game-announcements-page1.html
EOF
}

output=""
referer="https://forums.utopia-game.com/archive/index.php/f-1585.html"
cookie="${UTOPIA_FORUM_COOKIE:-}"
timeout_seconds=30
retries=3
retry_delay=2
dump_headers=""

if [[ $# -eq 0 ]]; then
  usage
  exit 1
fi

url=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    -o|--output)
      output="${2:-}"
      shift 2
      ;;
    --cookie)
      cookie="${2:-}"
      shift 2
      ;;
    --referer)
      referer="${2:-}"
      shift 2
      ;;
    --timeout)
      timeout_seconds="${2:-}"
      shift 2
      ;;
    --retries)
      retries="${2:-}"
      shift 2
      ;;
    --retry-delay)
      retry_delay="${2:-}"
      shift 2
      ;;
    --dump-headers)
      dump_headers="${2:-}"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      if [[ -n "$url" ]]; then
        echo "error: unexpected argument: $1" >&2
        usage >&2
        exit 1
      fi
      url="$1"
      shift
      ;;
  esac
done

if [[ -z "$url" ]]; then
  echo "error: missing URL" >&2
  usage >&2
  exit 1
fi

curl_args=(
  --insecure
  --location
  --fail
  --silent
  --show-error
  --max-time "$timeout_seconds"
  "$url"
  -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  -H "Accept-Language: en-US,en;q=0.9"
  -H "Cache-Control: max-age=0"
  -H "Connection: keep-alive"
  -H "DNT: 1"
  -H "Referer: $referer"
  -H "Sec-Fetch-Dest: document"
  -H "Sec-Fetch-Mode: navigate"
  -H "Sec-Fetch-Site: same-origin"
  -H "Sec-Fetch-User: ?1"
  -H "Upgrade-Insecure-Requests: 1"
  -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
  -H 'sec-ch-ua: "Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"'
  -H "sec-ch-ua-mobile: ?0"
  -H 'sec-ch-ua-platform: "Linux"'
)

if [[ -n "$cookie" ]]; then
  curl_args+=(-b "$cookie")
fi

if [[ -n "$output" ]]; then
  curl_args+=(-o "$output")
fi

if [[ -n "$dump_headers" ]]; then
  curl_args+=(-D "$dump_headers")
fi

attempt=1
while true; do
  if curl "${curl_args[@]}"; then
    exit 0
  fi

  if [[ "$attempt" -ge "$retries" ]]; then
    echo "error: request failed after $attempt attempt(s)" >&2
    exit 1
  fi

  echo "warning: attempt $attempt failed; retrying in ${retry_delay}s" >&2
  sleep "$retry_delay"
  attempt=$((attempt + 1))
done
