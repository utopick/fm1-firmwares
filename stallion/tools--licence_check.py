#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Eberon Limited (John Gorman)
"""Stallion's licence audit (stallion R52, R55): exit 1 on the first class of problem it lists, 0 when clean.

  licence_check.py [--list]      (from anywhere in the repo; --list also prints every file's licence)

Source files (C / H / S / LD, Python, JS / MJS, HTML, shell, PowerShell, batch, and any file with a #! line):
  - an SPDX-License-Identifier header in the first 25 lines, every id in it on SOURCE_OK;
  - a file under another licence than GPL-3.0 (third-party code kept as it came) is named in LICENSING.md.
Data files (everything under assets/, and images, fonts, audio, wavetables, preset banks, JSON data anywhere):
  - one row in assets/MANIFEST ("path | origin | licence | credit", four fields, none empty), its licence on
    DATA_OK (R11: SOURCE_OK and CC BY); and no row for a file that is not in the tree.
The files are git's (tracked and staged), else every file under the root but build/ and .git/. Python 3, no
packages: it runs in the pre-commit hook (tools/hooks/pre-commit) and in CI (.github/workflows/ci.yml)."""
import os
import re
import subprocess
import sys
from pathlib import Path

SOURCE_OK = {"GPL-3.0-only", "GPL-3.0-or-later", "Apache-2.0", "MIT", "BSD-2-Clause", "BSD-3-Clause",
             "CC0-1.0", "OFL-1.1"}
DATA_OK = SOURCE_OK | {"CC-BY-3.0", "CC-BY-4.0"}
GPL = {"GPL-3.0-only", "GPL-3.0-or-later"}
SOURCE_EXT = {".c", ".h", ".S", ".s", ".ld", ".py", ".js", ".mjs", ".cjs", ".html", ".htm", ".sh", ".ps1",
              ".bat", ".cmd"}
DATA_EXT = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp", ".ico", ".svg", ".tif", ".tiff", ".pdf",  # images
            ".ttf", ".otf", ".woff", ".woff2", ".bdf", ".pcf",                                      # fonts
            ".wav", ".aif", ".aiff", ".flac", ".mp3", ".m4a", ".ogg", ".opus",                      # samples
            ".wt", ".syx", ".fxp", ".fxb", ".bnk", ".json"}                                         # tables, banks
CONFIG = {"package.json", "package-lock.json", "tsconfig.json", "jsconfig.json"}  # project files, not data
MANIFEST = "assets/MANIFEST"
SPDX = re.compile(r"SPDX-License-Identifier:\s*(.+?)\s*(?:\*/|-->|$)")


def repo_files(root):
    try:
        out = subprocess.run(["git", "-C", str(root), "ls-files", "-z", "--cached"], capture_output=True,
                             check=True).stdout
        return sorted(p for p in out.decode("utf-8").split("\0") if p and (root / p).is_file())
    except (OSError, subprocess.CalledProcessError):
        files = []
        for d, dirs, names in os.walk(root):
            dirs[:] = [x for x in dirs if x not in (".git", "build", ".venv", "node_modules", "__pycache__")]
            files += [os.path.relpath(os.path.join(d, n), root).replace(os.sep, "/") for n in names]
        return sorted(files)


def is_source(root, p):
    if Path(p).suffix in SOURCE_EXT:
        return True
    if Path(p).suffix == "":                     # a script without an extension (tools/hooks/pre-commit)
        try:
            with open(root / p, "rb") as f:
                return f.read(2) == b"#!"
        except OSError:
            return False
    return False


def is_data(p):
    if p == MANIFEST:
        return False
    if p.startswith("assets/"):
        return True
    return Path(p).suffix.lower() in DATA_EXT and Path(p).name not in CONFIG


def spdx_of(path):
    """The licence expression of a source file's header, or None."""
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            for _, line in zip(range(25), f):
                m = SPDX.search(line)
                if m:
                    return m.group(1).strip()
    except OSError:
        pass
    return None


def ids_of(expr):
    """The licence ids of an SPDX expression ("MIT OR Apache-2.0" -> both); WITH exceptions stay as ids,
    so an exception never passes unseen."""
    return [t for t in re.split(r"[\s()]+", expr) if t and t not in ("AND", "OR")]


def check_sources(root, files, problems, listing):
    try:
        licensing = (root / "LICENSING.md").read_text(encoding="utf-8")
    except OSError:
        licensing = ""
    for p in files:
        if not is_source(root, p):
            continue
        expr = spdx_of(root / p)
        if listing is not None:
            listing.append(f"{expr or '(none)':24} {p}")
        if expr is None:
            problems.append(f"{p}: no SPDX-License-Identifier header (R52)")
            continue
        bad = [i for i in ids_of(expr) if i not in SOURCE_OK]
        if bad:
            problems.append(f"{p}: licence {expr!r} not on the allowed list ({', '.join(bad)}) (R52)")
        elif not set(ids_of(expr)) <= GPL and p not in licensing:
            problems.append(f"{p}: third-party licence {expr} but no row naming it in LICENSING.md (R52)")


def check_data(root, files, problems, listing):
    rows = {}
    try:
        text = (root / MANIFEST).read_text(encoding="utf-8")
    except OSError:
        problems.append(f"{MANIFEST}: missing (R55)")
        text = ""
    for n, line in enumerate(text.splitlines(), 1):
        if not line.strip() or line.startswith("#"):
            continue
        f = [x.strip() for x in line.split(" | ")]
        if len(f) != 4 or not all(f):
            problems.append(f"{MANIFEST}:{n}: not 'path | origin | licence | credit' (four fields, none empty)")
            continue
        if f[0] in rows:
            problems.append(f"{MANIFEST}:{n}: {f[0]} listed twice")
        rows[f[0]] = f[2]
        bad = [i for i in ids_of(f[2]) if i not in DATA_OK]
        if bad:
            problems.append(f"{MANIFEST}:{n}: {f[0]}: licence {f[2]!r} not allowed for data ({', '.join(bad)}) (R11)")
    present = set(files)
    for p in files:
        if is_data(p):
            if listing is not None:
                listing.append(f"{rows.get(p, '(none)'):24} {p}")
            if p not in rows:
                problems.append(f"{p}: data file not in {MANIFEST} (R55)")
    for p in rows:
        if p not in present:
            problems.append(f"{MANIFEST}: {p}: listed but not in the tree")


def main(argv):
    here = Path(__file__).resolve().parent.parent
    try:
        root = Path(subprocess.run(["git", "-C", str(here), "rev-parse", "--show-toplevel"], capture_output=True,
                                   check=True, text=True).stdout.strip())
    except (OSError, subprocess.CalledProcessError):
        root = here
    files = repo_files(root)
    listing = [] if "--list" in argv else None
    problems = []
    check_sources(root, files, problems, listing)
    check_data(root, files, problems, listing)
    if listing is not None:
        print("\n".join(listing))
    for p in problems:
        print("licence:", p)
    nsrc = sum(is_source(root, p) for p in files)
    ndat = sum(is_data(p) for p in files)
    print(f"licence check: {nsrc} source files, {ndat} data files: "
          + (f"{len(problems)} problem(s)" if problems else "ok"))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
