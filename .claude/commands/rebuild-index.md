---
description: Regenerate the wiki index and backlinks, and report broken links and orphans
---

Run:

```bash
python3 scripts/rebuild_index.py
```

This regenerates `wiki/index.md` and `wiki/_backlinks.json`, and reports page counts by
directory, broken wikilinks, orphans, and the most-referenced pages.

Hand-written one-line summaries in `index.md` are preserved across rebuilds. Any page
without one appears as `TODO: summarize` and is listed under `NEEDS SUMMARY` — **write
those summaries before finishing.** A page's `aliases:` frontmatter surfaces in the index
as `also:`, which is what lets `/ingest` and `/breakdown` match raw text to existing pages
instead of creating near-duplicates.

Use `--check` to report without writing (exits non-zero if there are broken links or
orphans).

Run this at the **end** of a command, not mid-flight. Then report what changed: new pages,
new broken links, new orphans.
