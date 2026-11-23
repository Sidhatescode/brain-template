# brain

A knowledge base you talk to. You drop sources into a folder. Claude reads them and compiles
a wiki — pages for the people, the projects, the decisions, and the patterns none of your
sources name out loud. It keeps the links, the index and the numbers straight so you don't
have to.

Everything is stored as plain Markdown files on your computer. Claude helps you build the
wiki, and Obsidian lets you browse it. You can still read the files without either app.

## Get started

### 1. Create a home for your brain

On a Mac, open Finder and go to Desktop or Documents. Right-click an empty space, choose
**New Folder**, and name it **My Brain**. On Windows, do the same in File Explorer.

### 2. Download the template

On this GitHub page, click the green **Code** button, then **Download ZIP**. Find the ZIP
in Downloads and double-click it to extract it (on Windows, right-click and choose **Extract
All**). Move the extracted folder into **My Brain**.

Open that extracted folder. It should contain `CLAUDE.md` and the folders `raw`, `docs`,
and `wiki`. This inner folder is your brain: select it in both Claude and Obsidian below.
Keep its contents together, including hidden files. You don't need a GitHub account to
download a public repository.

### 3. Open it in Claude

1. Download and install the [Claude desktop app](https://claude.com/download).
2. Sign in with an account that has access to Claude Code. The Code tab requires an eligible
   paid plan; usage limits apply.
3. Open the **Code** tab and choose a **local** session.
4. Use the project folder selector to open the extracted folder from step 2—the one
   containing `CLAUDE.md`.
5. In the chat, type `/setup` and press Enter. Claude will ask a few questions, customize
   your brain, and guide you through adding your first source.

If `/setup` doesn't appear, check that you selected the inner folder containing `CLAUDE.md`,
not its parent `My Brain` folder, and start a new local session. If needed, ask Claude:
“Read `CLAUDE.md` and `.claude/commands/setup.md`, then guide me through setup.”

### 4. Add something worth remembering

Choose a WhatsApp text export, meeting notes, an old project conversation, or notes about
an idea you keep returning to. Put the file in the brain's `raw` folder when Claude asks.
Claude will read it and discuss what it found before writing anything. Then ask a question,
such as “What themes keep coming up?”

Choose material you are comfortable sharing, including other people's messages. Your files
are stored locally, but content Claude reads is sent to its service for processing.

### 5. Explore it in Obsidian

Download [Obsidian](https://obsidian.md/). Open it, choose **Open folder as vault**, and
select the same extracted folder you selected in Claude. Open `wiki/index.md` to browse
your pages, follow links, or use graph view to see how they connect. Claude and Obsidian
work on the same files; there is no separate connection to set up.

For a terminal-based setup, see [START-HERE.md](START-HERE.md).

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
| `/setup` | Once, on a fresh copy | Interviews you, fits the schema to your subject, runs the first ingest. |
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

## Back up your brain

Keep a separate, secure backup of the entire brain folder, including its hidden files, and
update it regularly. A ZIP download is not a Git repository and does not provide version
history. If you use Git, commits can help you recover earlier versions, but they are not a
substitute for a separate backup. Be careful not to publish private sources to a public
repository.

## Credit

The taxonomy, the anti-cramming and anti-thinning rules, the length targets and the
`/breakdown` and `/cleanup` workflows are adapted from
[Farza's wiki-gen skill](https://gist.github.com/farzaa/c35ac0cfbeb957788650e36aabea836d).
`CLAUDE.md` lists where this diverges and why.
