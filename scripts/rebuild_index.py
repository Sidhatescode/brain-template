#!/usr/bin/env python3
"""Rebuild wiki/index.md and wiki/_backlinks.json from the current wiki state.

Preserves the hand-written one-line summary for every page already listed in
index.md. Pages that are new get a `TODO: summarize` placeholder for you to fill in.

Aliases come from each page's own `aliases:` frontmatter (Obsidian-native, so
[[alias]] links resolve too) and are surfaced in the index as `also:`.

Usage:
    python3 scripts/rebuild_index.py            # rewrite index.md + _backlinks.json
    python3 scripts/rebuild_index.py --check    # report only, write nothing (exit 1 on problems)
"""

import json
import os
import re
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(ROOT, "wiki")
INDEX = os.path.join(WIKI, "index.md")
BACKLINKS = os.path.join(WIKI, "_backlinks.json")

# Files that live at wiki/ root and are not wiki pages.
NON_PAGES = {"index", "log"}

# Directory display order in the index. Anything not listed is appended alphabetically.
DIR_ORDER = [
    "people", "projects", "companies", "events", "eras",
    "patterns", "philosophies", "craft", "strategies", "decisions", "tensions",
    "sources",
]

DIR_HEADINGS = {
    "people": "People",
    "projects": "Projects",
    "companies": "Companies",
    "events": "Events",
    "eras": "Eras",
    "patterns": "Patterns",
    "philosophies": "Philosophies",
    "craft": "Craft",
    "strategies": "Strategies",
    "decisions": "Decisions",
    "tensions": "Tensions",
    "sources": "Sources",
}

WIKILINK = re.compile(r"\[\[([^\]|#]+)")
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
# Index line: "- [[name]] — summary" or "- [[name]] -- summary", optional *(also: ...)*
INDEX_LINE = re.compile(
    r"^-\s*\[\[([^\]|]+)\]\]\s*(?:\*\(also:.*?\)\*)?\s*(?:—|--)?\s*(.*)$"
)


def page_files():
    """Every wiki page as (name, relpath, directory)."""
    out = []
    for dirpath, _dirnames, filenames in os.walk(WIKI):
        for fn in sorted(filenames):
            if not fn.endswith(".md"):
                continue
            name = fn[:-3]
            rel = os.path.relpath(os.path.join(dirpath, fn), WIKI)
            d = os.path.dirname(rel)
            if not d and name in NON_PAGES:
                continue
            out.append((name, rel, d or ""))
    return out


def frontmatter_field(text, field):
    m = FRONTMATTER.match(text)
    if not m:
        return None
    fm = m.group(1)
    fm_match = re.search(rf"^{field}:\s*(.*)$", fm, re.M)
    return fm_match.group(1).strip() if fm_match else None


def parse_aliases(raw):
    if not raw:
        return []
    raw = raw.strip()
    if raw.startswith("["):
        raw = raw[1:-1] if raw.endswith("]") else raw[1:]
    parts = [p.strip().strip("\"'") for p in raw.split(",")]
    return [p for p in parts if p]


def links_in(text):
    """Real wikilinks in a page body.

    Ignores anything inside HTML comments (index.md holds templates there), fenced
    code blocks, and inline code spans -- prose like `[[wikilinks]]` written as an
    example is not a link and must not be reported as broken. Attachment embeds
    (`![[image.png]]`) point at files in wiki/attachments/, not at pages, so they
    are stripped too.
    """
    body = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    body = re.sub(r"```.*?```", "", body, flags=re.S)
    body = re.sub(r"`[^`\n]*`", "", body)
    body = re.sub(r"!\[\[[^\]]+\]\]", "", body)
    return {m.strip() for m in WIKILINK.findall(body)}


def existing_summaries():
    """Recover hand-written summaries from the current index.md."""
    if not os.path.exists(INDEX):
        return {}
    out = {}
    for line in open(INDEX, encoding="utf-8"):
        m = INDEX_LINE.match(line.rstrip("\n"))
        if m:
            name, summary = m.group(1).strip(), m.group(2).strip()
            if summary:
                out[name] = summary
    return out


def main():
    check_only = "--check" in sys.argv

    pages = page_files()
    names = {n for n, _, _ in pages}
    meta = {}
    backlinks = defaultdict(list)
    broken = defaultdict(set)

    for name, rel, d in pages:
        text = open(os.path.join(WIKI, rel), encoding="utf-8").read()
        meta[name] = {
            "path": rel,
            "dir": d,
            "type": frontmatter_field(text, "type"),
            "aliases": parse_aliases(frontmatter_field(text, "aliases")),
        }
        for target in links_in(text):
            if target == name:
                continue
            if target in names:
                backlinks[target].append(name)
            else:
                broken[rel].add(target)

    # log.md links count toward backlinks but log.md is not itself a page.
    log_path = os.path.join(WIKI, "log.md")
    if os.path.exists(log_path):
        for target in links_in(open(log_path, encoding="utf-8").read()):
            if target in names:
                backlinks[target].append("log")
            else:
                broken["log.md"].add(target)

    orphans = sorted(n for n in names if not backlinks.get(n))

    print(f"pages: {len(names)}")
    by_dir = defaultdict(int)
    for n in names:
        by_dir[meta[n]["dir"] or "(root)"] += 1
    for d in sorted(by_dir, key=lambda x: (DIR_ORDER.index(x) if x in DIR_ORDER else 99, x)):
        print(f"  {d:<14} {by_dir[d]}")

    if broken:
        print(f"\nBROKEN WIKILINKS ({sum(len(v) for v in broken.values())}):")
        for f, targets in sorted(broken.items()):
            print(f"  {f} -> {', '.join(sorted(targets))}")
    else:
        print("\nno broken wikilinks")

    if orphans:
        print(f"\nORPHANS ({len(orphans)}) — no inbound links:")
        for o in orphans:
            print(f"  {meta[o]['path']}")
    else:
        print("no orphans")

    top = sorted(backlinks.items(), key=lambda kv: -len(kv[1]))[:10]
    if top:
        print("\nmost-referenced:")
        for n, srcs in top:
            print(f"  {len(srcs):4}  {n}")

    if check_only:
        sys.exit(1 if (broken or orphans) else 0)

    # ---- write _backlinks.json -------------------------------------------------
    payload = {
        n: {"count": len(sorted(set(v))), "from": sorted(set(v))}
        for n, v in sorted(backlinks.items())
    }
    with open(BACKLINKS, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
        f.write("\n")

    # ---- write index.md --------------------------------------------------------
    summaries = existing_summaries()
    missing = []
    out = [
        "# Index",
        "",
        "Catalog of every wiki page, grouped by type. Regenerate with `/rebuild-index`",
        "(`python3 scripts/rebuild_index.py`). Summaries are hand-written and preserved",
        "across rebuilds — new pages appear with `TODO: summarize`.",
        "",
    ]
    dirs = sorted({meta[n]["dir"] for n in names},
                  key=lambda x: (DIR_ORDER.index(x) if x in DIR_ORDER else 99, x))
    for d in dirs:
        heading = DIR_HEADINGS.get(d, d.replace("-", " ").title() or "Root")
        members = sorted(n for n in names if meta[n]["dir"] == d)
        out.append(f"## {heading}")
        out.append("")
        for n in members:
            summary = summaries.get(n)
            if not summary:
                summary = "TODO: summarize"
                missing.append(n)
            alias = ""
            if meta[n]["aliases"]:
                alias = f" *(also: {', '.join(meta[n]['aliases'])})*"
            out.append(f"- [[{n}]]{alias} — {summary}")
        out.append("")

    with open(INDEX, "w", encoding="utf-8") as f:
        f.write("\n".join(out))

    print(f"\nwrote {os.path.relpath(INDEX, ROOT)} and {os.path.relpath(BACKLINKS, ROOT)}")
    if missing:
        print(f"NEEDS SUMMARY ({len(missing)}):")
        for n in missing:
            print(f"  {n}")


if __name__ == "__main__":
    main()
