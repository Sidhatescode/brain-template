---
description: Load relevant wiki context at the start of a session
---

Start of session. Load only what's relevant — don't dump the whole wiki into context.

1. Read `wiki/log.md`, focusing on the most recent entries (e.g.
   `grep "^## \[" wiki/log.md | tail -10`), to see what's happened recently.
2. Read `wiki/index.md` to see what pages exist.
3. Ask the human what they're working on this session, if not already stated.
4. Based on their answer, pull in the specific wiki pages relevant to that topic — read them,
   don't just list them.
5. Summarize back: what you loaded, what recent history looks relevant, and any open
   questions or loose ends from `wiki/log.md` that relate to today's topic.

Do not modify any files during spinup. This is a read-only context-loading step.
