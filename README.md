# Utopia Guide

A community-maintained guide for [Utopia](https://utopia-game.com), built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and hosted at [utopiaguide.chaos-intel.com](https://utopiaguide.chaos-intel.com).

**Pull requests are welcome!** All content lives in `docs/` as plain Markdown — edit pages directly and open a PR.

## Contributing

1. Fork the repo and clone it
2. Install dependencies: `python3 -m venv .venv && .venv/bin/pip install -r requirements.txt`
3. Preview locally: `.venv/bin/mkdocs serve` → <http://localhost:8000>
4. Edit pages in `docs/`, then open a pull request

## Seeding from the original wiki

The original wiki at `wiki.utopia-game.com` is currently inaccessible (expired SSL). The included scraper pulls archived snapshots from the Wayback Machine and converts them to Markdown.

```bash
./scripts/scrape_wiki.py        # initial scrape
./scripts/rescrape_broken.py    # re-fetch pages that came out garbled
./scripts/fix_links.py          # fix internal links after scraping
```

Already-downloaded pages are skipped, so the scraper is safe to re-run if interrupted.

## Recovering historical forum posts

Many age pages and changelogs were recovered from the official Utopia
forums and the Wayback Machine. The repo includes helpers for both live
forum fetches and archived thread recovery.

```bash
./scripts/fetch_forum_page.sh 'https://forums.utopia-game.com/forumdisplay.php?1585-Game-Announcements&page=1' -o /tmp/forum-page1.html
python3 ./scripts/fetch_wayback_thread.py 640160
python3 ./scripts/extract_forum_post.py /tmp/utopia-wayback-thread-cache/640160-*.html
python3 ./scripts/list_wayback_forum_pages.py 'https://forums.utopia-game.com/forumdisplay.php?1585-Game-Announcements'
python3 ./scripts/compare_archived_forum_ages.py
```

Useful helpers:

- `scripts/fetch_forum_page.sh`: fetch a live forum page with the header set that works against the flaky official forum
- `scripts/fetch_wayback_thread.py`: fetch and cache the latest Wayback snapshot for a forum thread id
- `scripts/extract_forum_post.py`: extract the first forum post body from saved HTML
- `scripts/list_wayback_forum_pages.py`: list archived forumdisplay page coverage in Wayback
- `scripts/compare_archived_forum_ages.py`: compare archived age-change threads against local `docs/history/Age_*.md` coverage

## Deploying to GitHub Pages

### 1. Configure your subdomain

- In `mkdocs.yml`: set `site_url` to your subdomain
- In `.github/workflows/deploy.yml`: set the `cname:` field to match
- Add a DNS CNAME record pointing your subdomain to `<your-github-username>.github.io`

### 2. Enable GitHub Pages

In your repo settings → Pages → Source: **Deploy from a branch** → branch: `gh-pages` / root.

### 3. Push to master

The GitHub Actions workflow builds and deploys automatically on every push to `master`.

## Structure

The site navigation is defined in `mkdocs.yml`, and the published content currently lives under these sections:

```text
docs/
├── index.md              # Home page
├── main/                 # Core game reference and mechanics
├── guide/                # Guides, strategy, and player how-tos
├── history/              # Ages, Genesis, World of Legends, historical data
├── misc/                 # Mechanics, community pages, and miscellany
├── formulas/             # Formula reference pages
├── tools/                # External tool documentation
├── stylesheets/          # Custom CSS (extra.css)
└── CNAME                 # Custom domain for GitHub Pages
```

Current MkDocs nav groupings:

- `Game Reference`: mostly `docs/main/`
- `Guides` and `Player Guides`: `docs/guide/`
- `Mechanics`: content split across `docs/main/`, `docs/misc/`, and `docs/formulas/`
- `History`: mostly `docs/history/` with some historical pages in `docs/misc/`
- `Community & Tools`: content from `docs/tools/`, and `docs/misc/`
- `About`: informational pages in `docs/misc/`

Repo files of note:

```text
scripts/scrape_wiki.py    # Wayback Machine scraper
scripts/rescrape_broken.py # Re-scrape garbled pages
scripts/fix_links.py      # Fix internal links
scripts/fetch_forum_page.sh # Fetch live forum pages with browser-style headers
scripts/fetch_wayback_thread.py # Cache archived forum thread snapshots
scripts/extract_forum_post.py # Extract first forum post from saved HTML
scripts/list_wayback_forum_pages.py # Inspect forum page coverage in Wayback
scripts/compare_archived_forum_ages.py # Compare archived age threads to local docs
mkdocs.yml                # Site configuration and navigation
requirements.txt          # Python dependencies
.github/workflows/
└── deploy.yml            # Auto-deploy to GitHub Pages on push to master
```
