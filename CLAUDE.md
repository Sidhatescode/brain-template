# brain — schema

This directory is a Claude Code working directory, and an Obsidian vault if you open it
there. It is a personal knowledge base built on the LLM-wiki pattern: raw sources get
compiled into a persistent, interlinked markdown wiki that you (the agent) own and
maintain. The human curates sources and asks questions. You do the reading, writing,
cross-referencing, and bookkeeping.

## About this vault

<!-- /setup rewrites this section. Until then, these are the defaults. -->

- **Owner:** unknown — ask, then write the answer here.
- **Subject:** general-purpose. Whatever the owner feeds it.
- **Sources look like:** unknown. Ask what they're dropping into `raw/`.
- **Main hub page:** none yet. The first `projects/` or `people/` page usually becomes it.

If this section still says "unknown", the owner hasn't run `/setup`. Offer to run it before
doing anything else — it takes two minutes and makes every later session better.

## Directory layout

- `raw/` — source documents (transcripts, clipped articles, exports, PDFs, notes).
  **Immutable.** Never edit or delete anything here. You only read from it. This is for
  *other people's* fixed artifacts and for point-in-time records of things already sent. If
  a document will keep changing, it does not belong here.
- `docs/` — the owner's own **living** working documents. **Editable** — unlike `raw/`, you
  may and should correct these in place when the owner gives you a new number or tells you
  something is wrong. Always state what you changed. See Canonical figures below.
- `wiki/` — everything you write. Organised by a **type taxonomy** (below), one directory
  per page type.
  - `wiki/index.md` — catalog of every wiki page, grouped by directory. One line per page: a
    wikilink, an `also:` alias list, and a one-line summary. Update on every write, or
    regenerate with `/rebuild-index`.
  - `wiki/log.md` — append-only chronological log. Never edit past entries, only append.
  - `wiki/_backlinks.json` — generated reverse-link index. Never hand-edit.
- `scripts/rebuild_index.py` — regenerates `index.md` and `_backlinks.json`, reports broken
  links and orphans.
- `.claude/commands/` — slash commands (`setup`, `spinup`, `ingest`, `breakdown`, `cleanup`,
  `rebuild-index`, `wrapup`).
- `example/` — a worked example: two fake sources and the eight wiki pages they compile
  into. Read it to calibrate quality before writing your first page. **Delete it** once the
  real vault has a dozen pages of its own; it is scaffolding, not knowledge.

The `raw/` vs `docs/` split is the one people get wrong. `raw/` is history and never
changes, so you can always see what a document said when it was written. `docs/` is current
and gets corrected.

## Page types and the taxonomy

You are a **writer**, not a filing clerk. The question is never "where does this fact go?"
but **"what does this mean, and how does it connect to what I already know?"**

Every page has a `type:` that **matches its directory**. Directories emerge from the data —
**do not pre-create empty ones.** Create a directory the first time a page genuinely
belongs in it.

| Directory | `type:` | What goes here |
|---|---|---|
| `sources/` | `source` | One per raw document. Key claims, why it matters, links out. Filename mirrors the source. |
| `people/` | `person` | Named individuals |
| `projects/` | `project` | Things built or run with serious commitment |
| `companies/` | `company` | External companies and organisations |
| `events/` | `event` | Specific dated occurrences |
| `eras/` | `era` | Major phases connecting multiple pages |
| `patterns/` | `pattern` | Recurring cycles: trigger, mechanism, outcome |
| `philosophies/` | `philosophy` | Articulated positions about how to work and live |
| `strategies/` | `strategy` | Named strategies and mechanics |
| `decisions/` | `decision` | Inflection points with enumerated reasoning |
| `tensions/` | `tension` | Unresolved contradictions between two values or two pieces of evidence |
| `craft/` | `craft` | Portable technique — how to do a thing well, independent of any one project |

Add new directories freely when a type genuinely doesn't fit — but only with a page to put
in it. Equally, drop the types this vault has no use for. A vault about a research field
may want `claims/` and `methods/`; one about a company may never need `eras/`.

**The `craft/` bar is high, deliberately.** Technique pages are the easiest kind to fill
with advice that is true everywhere and useful nowhere. Two tests, both of which must pass:

- **It must change how the owner works, not merely describe good work.** "The four outcome
  archetypes for a landing page" is a page; "use short sentences" is not.
- **It must survive detachment from its source.** If the only thing the page can say is
  "the course said X," that is a `sources/` summary wearing a costume.

**Source pages are not the wiki.** They are the raw material. A vault that is mostly
`sources/` is a source archive, not a knowledge base. The pages that make a vault worth
having are the pattern, philosophy, decision and tension pages — they are where it stops
being a list of documents and becomes a map of how the owner thinks and what they've
decided.

### When something earns a page

- **Named things** get a page once there is enough material — roughly >1 source, or one
  source with real depth. If you can't write 15 substantive lines, don't create it. Note it
  on the page where it appears and create it when more material arrives.
- **Patterns and themes** get a page when the same idea surfaces across multiple sources.
  These are often the most valuable pages in the vault, and the easiest to miss, because no
  single source names them.

## Frontmatter

```yaml
---
type: source | person | project | company | event | era | pattern | philosophy | strategy | decision | tension | craft
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: ["[[source-page-1]]", "[[source-page-2]]"]  # omit for source pages
related: ["[[other-page]]"]                          # optional
aliases: ["other name for this"]                     # optional, surfaces in the index
tags: [tag1, tag2]
---
```

## Naming and links

- Filenames: kebab-case, descriptive, no dates in the filename (dates live in frontmatter).
- Use Obsidian wikilinks (`[[page-name]]`) for all cross-references, not markdown links.
- Every new page must be linked from at least one existing page (no orphans) and added to
  `wiki/index.md`. If you can't find a natural link target, that's a sign the page may not
  need to exist yet, or the index needs a new section — flag it rather than filing an orphan.
- When a source contradicts an existing page, don't silently overwrite. Note the
  contradiction explicitly on the page (e.g. "as of [[source]], this is disputed: ...") and
  say so to the human.

## Writing standards

### Structure: theme-driven, not diary-driven

Organise pages by **theme**, not chronology. The Steve Jobs test — Wikipedia's article uses
"Early life" and "Career," not "The Xerox PARC Visit" and "The Lisa Project Failure."

```
Bad                        Good
## The March Meeting       ## Origins
## The April Pivot         ## The Pivot to Sponsorship
## The June Launch         ## Becoming the Product
```

A `## Timeline` table at the end is fine. A page whose *sections* are dated events is an
event log — **rewrite it.**

### Anti-cramming

The gravitational pull of big existing pages is the enemy. It is always easier to append a
paragraph than to create a page, and that produces 5 bloated pages instead of 30 focused
ones. **If you are adding a third paragraph about a sub-topic to an existing page, that
sub-topic needs its own page.**

### Anti-thinning

Creating a page is not the win — enriching it is. A stub with three vague sentences, when
four other sources also touched that topic, is a failure. **Every time you touch a page it
must get materially better.** Never just append to the bottom; integrate so the page reads
as a coherent whole. 40 stubs is as bad as 5 bloated pages.

### Length targets (lines)

| Type | Target |
|---|---|
| source | **as long as the source warrants** — 20–40 for a substantive document, 12+ for a trivial one |
| person | 20–80 (more references, longer) |
| project, company, event | 25–50 |
| philosophy, pattern, tension, strategy | 40–80 |
| decision | 40–70 |
| craft | 40–105 — runs longer because it carries three payloads: the technique, the specimens that prove it, and what it means for live work |
| era | 60–100 |
| **minimum, anything** | **15**, except trivial sources |
| **split above** | **120**, except hub pages |

**Two deliberate exceptions:**

- **Trivial sources.** A 16-line summary of a throwaway newsletter issue is correct. Padding
  it to hit 20 lines would be fabrication. Judge a source summary against its source, not
  against the table.
- **Hub pages.** The vault's main project or person page may run past 120 lines because it
  carries a reference table like Canonical figures. Splitting that table would break the
  single-source-of-truth rule that makes it useful. Reference tables justify the length;
  prose sprawl does not.

### Quote discipline

Maximum **2 direct quotes per page.** Pick the line that hits hardest. Quotes carry the
voice; the surrounding prose carries the analysis.

### Voice

Keep the **analytical register**. A vault like this is decision support, not an
encyclopedia — noticing that a number is stale, that two sources disagree, or that an
argument doesn't hold **is the value**. So:

- **Do** flag contradictions, stale claims and risks inline with `⚠️`, and state judgements
  plainly ("this is the most important open question here").
- **Do** lead with the subject, prefer short sentences, one claim per sentence, and
  attribution over assertion ("he described it as energizing", not "it was energizing").
- **Don't** use peacock words ("groundbreaking", "profound", "legendary"), editorial hedges
  ("interestingly", "it should be noted"), rhetorical questions, or progressive narrative
  ("would go on to", "embarked on this journey").

Every page must have a point. Not "here are four times X came up" but "X represented Y." A
reader should finish understanding something non-obvious.

## Workflows

### Setup (`/setup`)

Run once, on a fresh clone. Interviews the owner, rewrites the About this vault section
above, prunes the taxonomy to what they'll actually use, and walks them through their first
ingest. See `.claude/commands/setup.md`.

### Ingest (`/ingest`)

One source at a time, with discussion — this is the default. See
`.claude/commands/ingest.md` for the step-by-step and the every-15-sources checkpoint.

### Query

1. Read `wiki/index.md` first to find candidate pages — don't grep the whole vault blind.
2. Read the relevant pages (and follow wikilinks as needed) before answering.
3. Answer with citations to the specific wiki pages used.
4. If the answer is substantial (a comparison, an analysis, a new connection), offer to file
   it back into `wiki/` as a new page. If the human agrees, follow the same
   linking/index/log discipline as ingest.
5. Append a `## [YYYY-MM-DD] query | <short description>` entry to `wiki/log.md` if anything
   was filed back.

### Canonical figures (how numbers stay current)

Pick one page to be the vault's hub — usually its main project or subject — and give it a
**Canonical figures** table. It is the single source of truth for every number in the
vault. Spreadsheets, memos, decks and older wiki pages are downstream of it: when they
disagree, the table wins and the other document is stale.

**Whenever the owner states a figure in conversation** — a price, a headcount, a date, a
rate, a result — treat it as an update to that table, without being asked and without
waiting for `/ingest`:

1. Find the row. If the figure is new, add a row.
2. Overwrite the value **in place**. Never keep two live values for the same figure — the
   old one goes into a "Contradictions resolved" section with the date, or is deleted if it
   was simply wrong.
3. Update `Status` (`actual` / `assumption` / `modelled` / `contracted` / `claim`), the
   `As of` date, and `Source`. Downgrading matters as much as upgrading: if the owner says a
   number is a guess, mark it `assumption` even if it was previously stated as fact.
4. Propagate to the living documents in `docs/` that repeat the figure — edit them. Do
   **not** edit `raw/`; instead note on the wiki page that the raw artifact is superseded.
5. Say out loud what you changed and what else the change breaks. A changed input often
   invalidates a conclusion downstream — flag that, don't just edit the cell.
6. Append a `## [YYYY-MM-DD] figures | <what changed>` entry to `wiki/log.md`.

Table shape:

| Figure | Value | Status | As of | Source |
|---|---|---|---|---|

If this vault has no numbers in it — a reading log, a vault about a person — skip this
whole mechanic. It earns its keep only where figures drive decisions.

### Breakdown (`/breakdown`)

Find and create the pages that *should* exist but don't. This is the standing corrective to
cramming. Always present the candidate table and get approval before creating anything.

### Cleanup (`/cleanup`)

Audit and enrich pages that already exist — diary-driven structure, stubs, bloat, broken or
missing links, AI tells. Report first; fix on approval.

### Rebuild index (`/rebuild-index`)

Runs `scripts/rebuild_index.py`: regenerates `wiki/index.md` and `wiki/_backlinks.json`,
reports broken wikilinks and orphans. Run at the **end** of a command, never mid-flight.

### Lint

On request, health-check the wiki: contradictions between pages, stale claims superseded by
newer sources, orphan pages, concepts mentioned repeatedly but lacking their own page,
broken wikilinks, missing index entries. Report findings; only fix with the human's
go-ahead for anything non-trivial. Append a `## [YYYY-MM-DD] lint | <summary>` entry to
`wiki/log.md`.

### Session start / end

Use `/spinup` at the start of a session to load relevant context before starting work. Use
`/wrapup` at the end to write decisions, learnings and open questions back into the wiki and
log — don't let session insight evaporate into chat history.

## Tools

No MCP server, no embeddings, no search tool. Use built-in Read/Glob/Grep against
`wiki/index.md` and the wiki files directly. Revisit this only if grep/index-based retrieval
starts failing as the wiki grows — don't build search infrastructure preemptively.

## Ground rules

- `raw/` is immutable — read-only, always.
- `wiki/` is yours to write. The human rarely edits it directly; you maintain it.
- Never delete a wiki page without explicit confirmation.
- Never overwrite a page without reading it first. **Re-read any page immediately before
  editing it** — this is non-negotiable, and it's how you avoid clobbering work.
- ⚠️ **Creating a "new" page is where clobbering actually happens.** A
  `cat > wiki/.../page.md <<'EOF'` heredoc silently destroys an existing file, and unlike the
  `Write` tool it has no unread-file guard. **So: `ls` or `test -e` the path before any
  redirect that creates a page, and check `wiki/index.md` for the page name first — the index
  is the cheapest existence check in the vault.** A `[[name]]` with a written summary in the
  index means the page exists, whatever you assume.
- ⚠️ **Commit often. There is no other undo.** Anything overwritten between commits is gone.
  `git add -A && git commit -m "ingest: <source>"` at the end of every session costs nothing
  and is the only safety net this design has. If the owner hasn't committed in a while, say so.
- **A concurrent session may be editing the same files.** A "file changed on disk" notice is
  not always an echo of your own write — read it before assuming.
- Every claim should trace back to a source. Cite in frontmatter `sources:`.
- Rebuild the index and backlinks only at the very end of a command, not mid-flight.
- Keep this file (`CLAUDE.md`) updated if workflows change — it's the schema, not a snapshot.
- As the vault matures, append the owner's own hard-won operating notes here: the file
  formats that break, the tools that lie, the standing instructions they've given you. That
  accumulated local knowledge is what makes a vault yours rather than a template.

## Provenance

The taxonomy, anti-cramming/anti-thinning rules, theme-driven structure test, length
targets, quote discipline and the `/breakdown` and `/cleanup` workflows are adapted from
[Farza's wiki-gen skill](https://gist.github.com/farzaa/c35ac0cfbeb957788650e36aabea836d).

Deliberate divergences from that spec:
- **Analytical voice retained.** Farza mandates flat Wikipedia neutrality. A vault that
  serves live decisions needs to flag risk and contradiction.
- **Em dashes retained.** Farza bans them; cosmetic.
- **No subagents.** Farza's `/cleanup` and `/breakdown` spawn parallel agents; these run
  in-process unless the owner asks otherwise.
