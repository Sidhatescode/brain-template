---
description: Find and create the knowledge pages that should exist but don't
argument-hint: "[--reorganize] [focus area]"
---

Expand the wiki by finding concrete entities and recurring themes that deserve their own
page. This is the standing corrective to cramming — see the Writing standards in
`CLAUDE.md`.

Focus: $ARGUMENTS (if given, restrict mining to that area; otherwise survey everything).

## Phase 1 — Survey

Read `wiki/index.md` and `wiki/_backlinks.json`. Identify:

- **High-backlink targets with no page of their own** — things referenced repeatedly that
  were never written up. These are the strongest candidates.
- **Bloated pages** (>120 lines) that are carrying sub-topics which should be split out.
- **Bare directories** — a taxonomy directory with 0–1 pages usually means that whole class
  of knowledge hasn't been extracted yet.
- **Misclassified pages** — a `project` that is really a `pattern`, a `source` doing the job
  of a `strategy`.

## Phase 2 — Mine

Read pages in batches and extract candidates.

**Concrete entities** — apply the noun test, "X is a ___":
named people, companies, organisations, places, named events with dates, books/films/music
referenced, tools and platforms used significantly, named projects.

**Themes and patterns** — the same idea surfacing across multiple sources: a recurring
behavioural cycle, an articulated philosophy, a repeated strategic mechanic, a
contradiction that keeps resurfacing. **These are usually the most valuable pages in the
vault and the easiest to miss**, because no single source names them.

**Do NOT extract:** generic technologies (React, Python, Docker) unless there's a
documented learning arc; things already covered by an existing page; passing mentions with
no material behind them.

## Phase 3 — Plan (stop here)

Deduplicate against existing pages, count references for each candidate, and rank by
reference count. **Present a table and stop for approval. Do not create anything yet.**

| # | Proposed page | Dir | Refs | What it would say |
|---|---|---|---|---|

Flag any candidate you can't write 15 substantive lines for — those should wait rather than
become stubs.

## Phase 4 — Create (after approval)

For each approved candidate:

1. Grep the wiki for every mention, and read the pages that mention it.
2. Write the page, following the type's structure and length target in `CLAUDE.md`.
   Theme-driven sections, max 2 quotes, analytical voice.
3. **Add inbound wikilinks from the existing pages that mention it** — a new page with no
   inbound links is an orphan.
4. Set `sources:` frontmatter to the source pages the material came from.

Then run `/rebuild-index` and append a `## [YYYY-MM-DD] breakdown | <summary>` entry to
`wiki/log.md`.

## `--reorganize`

Also move misclassified pages to their correct directory (updating `type:` to match).
Common moves: a page stating a belief → `philosophies/`; a page with trigger-response
structure → `patterns/`; a multi-week uncertain period → `eras/`; a page with enumerated
reasons for a choice → `decisions/`. Use `git mv`. Wikilinks resolve by filename, so moves
don't break links.
