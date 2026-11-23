---
description: Process a new source in raw/ end to end
argument-hint: <filename in raw/>
---

Ingest a source from `raw/` into the wiki, following the Ingest workflow in `CLAUDE.md`.

Target: $ARGUMENTS (if not given, ask which file in `raw/` to ingest — list recent additions
to `raw/` that don't yet have a corresponding page in `wiki/` as candidates).

1. Read the source file in full.
2. Summarize key takeaways and discuss with the human — do not write anything yet. Ask what
   to emphasize if the source is dense or covers multiple topics.
3. Once aligned, write or update the source summary page in `wiki/`.
4. Update or create entity/concept pages the source touches, linking them to the new source
   page. Check `wiki/index.md` first to avoid creating duplicate pages for things that
   already exist.
5. Update `wiki/index.md` with the new/changed pages.
6. Append `## [YYYY-MM-DD] ingest | <title>` to `wiki/log.md`.
7. Report back what was created/updated.

This is one-source-at-a-time by default. Only batch-process multiple sources if the human
explicitly asks for it in this invocation.

## If this is the vault's first ingest

The wiki is empty, so there is nothing to link to and nothing to avoid duplicating. Do the
extra work that makes the mechanic visible:

- **Read `example/` first** to calibrate. Two fake sources, eight pages. Match that density
  and that voice, not the thin summary a first pass tends to produce.
- **Aim for 4–8 pages, not one.** A source page plus the people, the project, and at least
  one abstract page — a `pattern`, `decision` or `tension`. A first ingest that produces
  only a `sources/` page has taught the owner nothing about what this is for, and starts the
  vault as a source archive. If the source genuinely can't support an abstract page, say so
  rather than inventing one.
- **Narrate the taxonomy as you go.** When you create `people/ana-reyes.md`, say why it's a
  person page and not a line inside the source summary. The owner is learning the schema by
  watching you apply it.
- **Show your work at the end.** Print the tree of what you created, then answer one
  question off the new wiki unprompted — something the raw file does not state outright but
  the wiki now does. That is the whole point of the vault, demonstrated in one move.
- **Back it up.** If this folder is a Git repository, offer to commit the changes. Otherwise
  remind the owner to keep a separate secure backup of the entire brain folder.

## Checkpoint every 15 sources

On any batch run, stop every 15 sources and:

1. Rebuild the index and backlinks (`/rebuild-index`).
2. **New-page audit** — how many knowledge pages were created in the last 15? **If zero,
   you are cramming.** Go back and find what should have become a page.
3. **Quality audit** — re-read your 3 most-updated pages as whole pieces. Is it a coherent
   story or a chronological dump? Sections by theme or by date? Does it connect to other
   pages revealingly? Would a reader learn something non-obvious? Rewrite any that read
   like event logs.
4. Check whether any page now exceeds 120 lines and should be split.
