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
./scrape_wiki.py        # initial scrape
./rescrape_broken.py    # re-fetch pages that came out garbled
./fix_links.py          # fix internal links after scraping
```

Already-downloaded pages are skipped, so the scraper is safe to re-run if interrupted.

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

```
docs/
├── index.md              # Home page
├── main/                 # Core game reference (Race, Science, etc.)
├── guide/                # Official guides
├── category/             # Category pages
├── misc/                 # Miscellaneous pages
├── ages/                 # Age-specific content
├── formulas/             # Game formulas
└── tools/                # External tools
scrape_wiki.py            # Wayback Machine scraper
rescrape_broken.py        # Re-scrape garbled pages
fix_links.py              # Fix internal links
mkdocs.yml                # Site configuration
requirements.txt          # Python dependencies
.github/workflows/
└── deploy.yml            # Auto-deploy to GitHub Pages on push to master
```
