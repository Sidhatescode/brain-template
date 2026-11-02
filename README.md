# brain

A knowledge base you talk to. You drop sources into a folder. Claude reads them and compiles
a wiki — pages for the people, the projects, the decisions, and the patterns none of your
sources name out loud. It keeps the links, the index and the numbers straight so you don't
have to.

Everything is plain markdown in a git repo. No database, no embeddings, no server, no
account. If you delete Claude tomorrow you still have a wiki.

## Get started

```bash
git clone <this-repo> brain && cd brain
claude
```

Then type `/setup`. It asks four questions, rewrites the schema to match your subject, and
does the first ingest with you. Fifteen minutes.

No Claude Code yet? `npm install -g @anthropic-ai/claude-code`.

## How it works

| Folder | What's in it | Can Claude edit it? |
|---|---|---|
| `raw/` | Sources. Transcripts, exports, articles, PDFs. Drop new files here. | **No. Never.** |
| `docs/` | Your own living files — a brief, a budget, a plan. | **Yes.** It fixes these when a fact changes. |
| `wiki/` | Everything Claude writes, sorted by type: `people/`, `projects/`, `patterns/`, `decisions/`, `tensions/`. | Yes. This is Claude's to maintain. |
| `example/` | A worked example. Two fake sources, eight pages. | Delete it when you're bored of it. |

The `raw/` vs `docs/` split is the one that matters. `raw/` is history and never changes, so
you can always see what a document said when it was written. `docs/` is current and gets
corrected.

`CLAUDE.md` is the schema — the page types, the writing standards, the rules. It is the
actual product here, and `/setup` tailors it to you. Edit it whenever; Claude reads it every
session.

## The commands

| Command | Use it when | What happens |
|---|---|---|
| `/setup` | Once, on a fresh clone | Interviews you, fits the schema to your subject, runs the first ingest. |
| `/spinup` | You start a session | Reads the log, asks what you're working on, loads only the pages that matter. |
| `/ingest` | You added a file to `raw/` | Reads it, tells you what's in it, waits for your OK, then writes it into the wiki. |
| `/breakdown` | It feels like a pile of documents | Finds ideas that keep coming up but have no page yet. Shows you a list before writing. |
| `/cleanup` | Pages feel messy or out of date | Checks structure, dead links, stale facts. Reports first, fixes after you agree. |
| `/rebuild-index` | After pages get added or moved | Rebuilds the index and link map. Warns about broken links and orphans. |
| `/wrapup` | You finish a session | Saves what you decided and learned so it doesn't die in chat history. |

## Two things need no command

**Just ask.** "What did Ana say about pricing?" "Which of these actually made money?" "Write
me a first draft of the intro email." Claude reads the index, opens the right pages, and
answers with citations.

**Just say the fact.** Tell it "the budget is $4,000 now" and it updates the canonical
figures table, fixes the files in `docs/` that repeat that number, flags what the change
breaks downstream, and logs it. You don't run anything. It keeps working in future sessions.

## What it's for

Anything where you accumulate sources over months and keep forgetting what you already knew.
A company. A research field. A job search. A person you're writing about. A hobby with a
literature.

It is not a note-taking app — you don't write in it, you feed it. The value shows up around
source ten, when it starts telling you things no single source said.

## A warning worth reading

Two pages of git history is not a backup. Commit after every session:

```bash
git add -A && git commit -m "ingest: today's source"
```

A wiki page overwritten between commits is gone. This design has no other undo.

## Credit

The taxonomy, the anti-cramming and anti-thinning rules, the length targets and the
`/breakdown` and `/cleanup` workflows are adapted from
[Farza's wiki-gen skill](https://gist.github.com/farzaa/c35ac0cfbeb957788650e36aabea836d).
`CLAUDE.md` lists where this diverges and why.
