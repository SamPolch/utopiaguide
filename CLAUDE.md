# CLAUDE.md

Project-specific guidance for editing the Utopia Guide docs.

## Markdown and MkDocs gotchas

- MkDocs uses Python-Markdown, which is stricter than GitHub-flavored
  Markdown in a few places.
- Nested list items should use 4-space indentation per level. Two-space
  indentation may render as a single flat `<ul>` instead of nested
  lists.
- If a nested list still renders poorly, prefer a flatter structure or
  real headings instead of forcing deep nesting.
- Avoid placeholder self-links like `(#)` and self-referential links to
  the current page. Convert them to real links or plain text.
- Prefer real Markdown headings over bold pseudo-headings.
- MkDocs admonitions are available and already used on the site. Use
  `!!! note "Title"`, `!!! tip "Title"`, `!!! info "Title"`, or
  `!!! example "Title"` with 4-space-indented body content for
  editorial sidebars, cautions, and callouts.
- Prefer real Markdown tables only for genuinely row/column data. If a
  table is just being used for layout, convert it to headings or lists.
- For historical age pages, avoid duplicating the same material in both
  early summary sections and later reference sections. Keep one
  canonical presentation.

## Historical age docs

- Use the more modern reference-style layout for `Races` and
  `Personalities` when feasible.
- Typical race subsections: `Bonuses`, `Penalties`, `Spell Book`,
  `Operation Access`, `Special Access`, `Units`.
- Typical personality subsections: `Bonuses`, `Spell Book`,
  `Starting Bonuses`, and other clearly named access sections where
  needed.
- Keep `Rituals` and `Dragons` near each other when both are present.
- If a `Rituals` section merely points to content elsewhere on the same
  page, remove the duplicate stub instead of keeping both.
- Use bullet summaries instead of wide one-row tables for stances,
  relations, dragons, and similar dense summaries when the table is hard
  to read on narrow screens.
- If an age page is only a placeholder forum link, prefer replacing it
  with a full local archive from the forum or Wayback rather than
  keeping a thin outbound link.
- The live forum is flaky. Prefer using the repo helpers under
  `scripts/`:
  `fetch_forum_page.sh`, `fetch_wayback_thread.py`, and
  `extract_forum_post.py`.
- If a recovered forum post is structured as `Age N` compared against
  `Age N-1`, preserve that comparison shape explicitly with `#### Age N`
  and `#### Age N-1` subsections instead of flattening the old values
  into prose.
- For recovered forum-backed age pages, keep the content materially
  intact while normalizing headings, bullets, and labels to match the
  surrounding age-doc style.
