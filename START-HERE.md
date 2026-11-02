# Start here

Two steps. Takes about fifteen minutes, most of it Claude working.

```bash
claude
```

Then type `/setup`. It asks you four questions, makes the vault yours, and walks you through
the rest. **You can stop reading here** — the rest of this file is the detail `/setup` will
give you anyway, in case you'd rather go manually.

---

## Step 1 — get one real file into `raw/`

The vault compiles sources into a wiki. It needs a source. Pick whichever of these you can
do in the next two minutes — the first one is the best.

### A WhatsApp chat export ← start here if you can

The best first source by a distance. It's months of real decisions, real people and real
arguments, and nothing else you own is this dense.

- **iPhone:** open the chat → tap the contact or group name at the top → scroll down →
  **Export Chat** → **Without Media** → share it to Files, then move the `.txt` into `raw/`.
- **Android:** open the chat → **⋮** → **More** → **Export chat** → **Without media** →
  save to your phone, then move the `.txt` into `raw/`.

Pick a group chat about a project, or a one-on-one with someone you work with. Avoid
anything you'd be uncomfortable having written up — the wiki will write it up.

### A meeting transcript

If you record calls, you already have the ideal source. Granola, Otter, Fathom, Zoom and
Google Meet all export plain text or `.srt`. Export one substantial call — forty minutes
beats four — and save it as `raw/<who>-<what>-call.md`.

No recordings? Write out one conversation from memory. Half a page of "he said X, I pushed
back with Y" works fine. The vault does not care that it's not verbatim.

### A Wikipedia page

Zero setup, and good if you want to watch the mechanic before trusting it with your own
material. Open the article for someone you actually care about — a founder, a scientist, a
musician. Select all, copy, paste into `raw/<their-name>.md`.

Pick someone with a messy career rather than a tidy one. The vault's abstract pages —
patterns, decisions, tensions — need contradictions to chew on.

### A LinkedIn profile

On the profile page: **More** → **Save to PDF**. Drop the PDF into `raw/`. Your own profile
works, or a person you're about to meet. Thinner than the others, so expect fewer pages out
of it.

---

## Step 2 — ingest it

```
/ingest
```

Claude reads the file, tells you what's in it, and **waits for your OK before writing
anything.** Then it writes: a summary page for the source, a page for each person, a page for
the project, and — the part that matters — at least one page for a pattern, decision or
tension that the source never states outright.

When it's done, ask it something the raw file doesn't answer directly. That's the whole
point.

Then commit, every time:

```bash
git add -A && git commit -m "ingest: my first source"
```

There is no other undo. A page overwritten between commits is gone.

---

## What to do after that

| You want to | Do this |
|---|---|
| Add another source | Drop it in `raw/`, run `/ingest` |
| Start a work session | `/spinup` |
| Ask it something | Just ask. No command. |
| Correct a fact or a number | Just say it. It files the change itself. |
| End a session | `/wrapup` |
| Feel like it's a pile of documents | `/breakdown` |
| Feel like the pages are messy | `/cleanup` |

Feed it ten sources before you judge it. One source gives you a summary; ten give you a map,
and the map is the product.

Browse it in [Obsidian](https://obsidian.md) if you want the graph view — point Obsidian at
this folder, open a vault, done. Everything is plain markdown either way.
