#!/usr/bin/env python3
"""Validate references/pattern-library.md against its own index.

A library that drifts from its index cannot be cited reliably.

    python3 scripts/check_library.py [path]
"""
import pathlib
import re
import sys

ANCHOR = re.compile(r"^### .*\{#([a-z0-9-]+)\}\s*$", re.M)
META = re.compile(r"^`(clinical|neutral|warm) / (airy|mid|dense)` · medium: (\S+) · "
                  r"risk: (low|medium|high) · checked: (\d{4}-\d{2}-\d{2})\s*$", re.M)
ROW = re.compile(r"^\| `([a-z0-9-]+)` \| (.+?) \| (\S+) \| (clinical|neutral|warm) \| "
                 r"(airy|mid|dense) \| (low|medium|high) \|\s*$", re.M)


def main(argv):
    path = pathlib.Path(argv[1] if len(argv) > 1 else
                        "references/pattern-library.md")
    if not path.exists():
        print(f"missing: {path}", file=sys.stderr)
        return 64
    text = path.read_text()

    entries = ANCHOR.findall(text)
    rows = ROW.findall(text)
    row_slugs = [r[0] for r in rows]
    metas = META.findall(text)
    errors = []

    def check(cond, msg):
        if not cond:
            errors.append(msg)

    dupes = {s for s in entries if entries.count(s) > 1}
    check(not dupes, f"duplicate entry slugs: {sorted(dupes)}")
    dupe_rows = {s for s in row_slugs if row_slugs.count(s) > 1}
    check(not dupe_rows, f"duplicate index rows: {sorted(dupe_rows)}")

    missing_rows = sorted(set(entries) - set(row_slugs))
    orphan_rows = sorted(set(row_slugs) - set(entries))
    check(not missing_rows, f"entries with no index row: {missing_rows}")
    check(not orphan_rows, f"index rows with no entry: {orphan_rows}")
    check(len(metas) == len(entries),
          f"{len(entries)} entries but {len(metas)} metadata lines")

    for slug in entries:
        block = text.split(f"{{#{slug}}}", 1)[1].split("\n### ", 1)[0]
        check(META.search(block) is not None, f"{slug}: bad or missing metadata line")
        check("**Do not take:**" in block, f"{slug}: no do-not-take line")
        check("Transferable move" in block, f"{slug}: no transferable move")

    by_risk = {r: sum(1 for row in rows if row[5] == r) for r in ("low", "medium", "high")}
    by_medium = {}
    for row in rows:
        by_medium[row[2]] = by_medium.get(row[2], 0) + 1

    print(f"entries: {len(entries)}")
    print(f"index rows: {len(row_slugs)}")
    print(f"metadata lines: {len(metas)}")
    print(f"risk: {by_risk}")
    print(f"medium: {dict(sorted(by_medium.items()))}")

    if errors:
        print()
        for e in errors:
            print(f"FAIL  {e}")
        return 1
    print()
    print("library and index agree")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
