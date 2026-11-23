---
description: One-time setup — make this vault yours, then run the first ingest together
---

First run on a fresh clone. You are turning a generic template into this person's vault, and
teaching them the mechanic by doing one real ingest with them. Be brisk and conversational.
**Ask one question at a time and wait** — do not dump a questionnaire.

If `wiki/` already holds pages other than `index.md` and `log.md`, stop and say the vault is
already set up; offer `/spinup` instead.

## Phase 1 — Interview (four questions, one at a time)

1. **"What's your name, and what do you want this vault to know about?"** One sentence is
   enough. A person, a company, a research field, a hobby, a job search.
2. **"What are you going to feed it?"** Meeting transcripts, WhatsApp exports, articles you
   clip, Wikipedia pages, PDFs, your own notes. This decides what `/ingest` will mostly see.
3. **"Are there numbers in this that matter?"** Prices, headcounts, dates, metrics. If yes,
   the Canonical figures mechanic stays and you'll ask which page should hold the table once
   one exists. If no — a reading log, a vault about a person — strip that section from
   `CLAUDE.md` and say you did.
4. **"Anything I should always do, or never do?"** Standing instructions. Tone, language,
   things they don't want written down. Record these verbatim under a new `## Standing
   instructions` heading in `CLAUDE.md`; they are the beginning of the local knowledge that
   makes the vault theirs.

## Phase 2 — Fit the taxonomy

Propose the type directories this vault will actually use. Default to `sources/`, `people/`
and whichever of `projects/` or `companies/` fits, plus **at least one abstract type** —
`patterns/`, `decisions/` or `tensions/`. Those are where a vault earns its keep, so never
cut all three.

Cut what doesn't fit and add what's missing. A vault about a research field may want
`claims/` and `methods/` instead of `strategies/` and `eras/`. Show the proposed list, get a
yes, then **do not create the directories** — they get created when the first page lands in
them, per `CLAUDE.md`.

## Phase 3 — Write it down

1. Rewrite the `## About this vault` section of `CLAUDE.md` with their real answers — owner,
   subject, what sources look like, hub page (write `none yet` if there isn't one).
2. Update the taxonomy table to the agreed types. Delete the rows they cut.
3. Add `## Standing instructions` if they gave any.
4. If they said no to numbers, delete the Canonical figures section.
5. Leave everything else alone. The writing standards are the part that works.

Show them the diff of `CLAUDE.md` in plain language — three bullets, not a patch.

## Phase 4 — First ingest, together

This is the part that teaches. Do not skip it or defer it to later.

Ask what they can put in `raw/` right now, and offer the four easiest. Give the exact steps
for whichever they pick — `START-HERE.md` has them all:

- **A WhatsApp chat export.** Open the chat → ⋮ / contact name → Export chat → **Without
  media** → save the `.txt` into `raw/`. The best first source: real people, real decisions,
  months of it.
- **A meeting transcript.** Granola, Otter, Zoom, Google Meet, Fathom all export text. Paste
  or save it into `raw/`.
- **A Wikipedia page** about someone they care about. Ctrl/Cmd-A on the article, paste into
  `raw/their-name.md`.
- **A LinkedIn profile.** On the profile: More → Save to PDF, drop the PDF into `raw/`.

Wait for the file to appear — `ls raw/` — then run `/ingest` on it and follow the **"If this
is the vault's first ingest"** section of that command. 4–8 pages, narrate the taxonomy,
show the tree, and answer one question off the new wiki. If this folder is a Git repository,
offer to commit; otherwise remind the owner to make a separate backup.

## Phase 5 — Hand over

End with exactly this, short:

- What's in `wiki/` now, as a tree.
- The four commands they'll actually use: `/ingest` when they add a file, `/spinup` to start
  a session, `/wrapup` to end one, and just asking questions in between.
- That they can say a number or a fact in plain chat and you'll file it — no command needed.
- That `example/` can be deleted whenever they like.
- That you've deleted `.claude/commands/setup.md`. Then delete it.
