# Utopia Guide

A community wiki for [Utopia](https://utopia-game.com), built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and hosted on GitHub Pages.

## Seeding from the original wiki

The original wiki at `wiki.utopia-game.com` is currently inaccessible (expired SSL). The included scraper pulls archived snapshots from the Wayback Machine and converts them to Markdown.

### Requirements

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

### Run the scraper

```bash
.venv/bin/python scrape_wiki.py
```

This will:
1. Fetch the list of ~170 archived wiki pages from the [Wayback Machine CDX API](https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server)
2. Download each page at ~1 req/sec (polite rate limiting)
3. Convert MediaWiki HTML → Markdown via `markdownify`
4. Organise files into `docs/` by category
5. Regenerate `mkdocs.yml` with a full nav

Already-downloaded pages are skipped, so the scraper is safe to re-run if interrupted.

### Preview locally

```bash
.venv/bin/mkdocs serve
```

Then open <http://localhost:8000>.

## Deploying to GitHub Pages

### 1. Configure your subdomain

- In `mkdocs.yml`: set `site_url` to your subdomain (e.g. `https://wiki.yourdomain.com/`)
- In `.github/workflows/deploy.yml`: set the `cname:` field to match
- Add a DNS CNAME record pointing your subdomain to `<your-github-username>.github.io`

### 2. Enable GitHub Pages

In your repo settings → Pages → Source: **Deploy from a branch** → branch: `gh-pages` / root.

### 3. Push

```bash
git push origin main
```

The GitHub Actions workflow will build and deploy automatically on every push to `main`.

## Editing content

All content lives in `docs/`. Pages are plain Markdown — edit them directly. The wiki content is a starting point; feel free to reorganise, update, or add pages.

## Structure

```
docs/
├── index.md              # Home page
├── guides/               # Player guides
├── formulas/             # Game formulas
├── tools/                # External tools
├── misc/                 # Uncategorised pages
└── ...
scrape_wiki.py            # One-time seeding script
mkdocs.yml                # Site configuration
requirements.txt          # Python dependencies
.github/workflows/
└── deploy.yml            # Auto-deploy to GitHub Pages
```
