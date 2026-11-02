---
description: Audit and enrich pages that already exist
argument-hint: "[directory or page name]"
---

Health-check and improve existing wiki pages. Where `/breakdown` adds pages, `/cleanup`
makes the ones already there better.

Scope: $ARGUMENTS (if given, limit to that directory or page; otherwise audit everything,
working one directory at a time).

## Phase 1 — Build context

Run `python3 scripts/rebuild_index.py --check` to get broken links and orphans. Read
`wiki/index.md` and `wiki/_backlinks.json` so you know what links to what, and which
entities are mentioned repeatedly without having a page.

## Phase 2 — Assess each page

Re-read the page in full before judging it. For each, check:

- **Structure** — theme-driven or diary-driven? Sections named after dated events
  (`## The March Meeting`) are the most common defect. Apply the Steve Jobs test.
- **Length** — under 15 lines (stub, needs enriching or merging) or over 120 (needs
  splitting)? Compare against the length targets in `CLAUDE.md`.
- **Coherence** — does it tell one story with a point, or is it a list of things that
  happened? Would a reader learn something non-obvious?
- **Quotes** — more than 2 direct quotes, or quotes doing work the prose should do?
- **Links** — broken wikilinks; and missing links, where the page mentions something that
  *does* have a page but doesn't link to it.
- **Voice** — AI tells to strip: peacock words, editorial hedges ("interestingly", "it
  should be noted"), rhetorical questions, progressive narrative ("would go on to").
  Keep the analytical register and the `⚠️` flags — those stay.
- **Staleness** — claims superseded by a newer source, or figures that disagree with the
  vault's Canonical figures table (see `CLAUDE.md` for which page holds it). The table wins.

## Phase 3 — Report, then fix

**Report findings first and get the go-ahead before making non-trivial changes** — this is
the standing rule in `CLAUDE.md`. Group by severity: contradictions and stale figures
first, then structure, then polish.

On approval:

1. Restructure diary-driven pages into theme-driven ones. Rewrite, don't just re-order.
2. Enrich stubs from material in the sources that mention them.
3. Split anything over 120 lines, creating the new page properly (links in and out).
4. Fix broken links; add the missing ones.
5. Note any candidate pages you spotted along the way and hand them to `/breakdown` rather
   than creating them here.

Then run `/rebuild-index` and append a `## [YYYY-MM-DD] cleanup | <summary>` entry to
`wiki/log.md`.
