#!/usr/bin/env python3
"""Brings this mirror up to date with FM1.Pocket's firmware list, then commits.

    python3 update.py                 # download what is new, drop old versions, rewrite README.md, commit
    python3 update.py --push          # the same, then push (GitHub Pages publishes it)
    python3 update.py --squash --push # also replace the whole history with one commit, then force-push

The list is fm1-pocket's pocket/vendor/firmwares.json (made by its pocket/update-firmwares.py, which runs this script at the
end), or the file given as an argument. Each firmware with an open licence is kept as <id>/<version>.fwsc, the address the
page asks for first; a version this mirror lacks makes the page fall back to the firmware's own link.

Every update adds its new packages to the git history for good, so the repository grows even though the folder doesn't.
GitHub wants repositories under about 1 GB, so the script warns past WARN_MB and --squash starts the history again from
the files as they are now.
Standard library and git only.
"""
import json, os, re, shutil, subprocess, sys, urllib.request

here = os.path.dirname(os.path.abspath(__file__))
args = [a for a in sys.argv[1:] if not a.startswith("--")]
LIST = args[0] if args else os.path.join(here, "..", "fm1-pocket", "pocket", "vendor", "firmwares.json")
OPEN = re.compile(r"^(GPL|LGPL|MPL|MIT|Apache|BSD)")  # licences that let us pass the package on; the rest stay at their author's
WARN_MB = 700
WHO = ["-c", "user.name=utopick", "-c", "user.email=310144039+utopick@users.noreply.github.com"]
AUTHOR = "--author=utopick <310144039+utopick@users.noreply.github.com>"


def git(*a, **k):
    return subprocess.run(["git", "-C", here, *WHO, *a], check=True, text=True, capture_output=True, **k).stdout


def path_of(f):  # also used by the page: "https://utopick.github.io/fm1-firmwares/" + id + "/" + version + ".fwsc"
    return f["id"] + "/" + (re.sub(r"[^\w.-]", "_", f.get("version") or "") or "0") + ".fwsc"


def readme(want):
    cell = lambda s: (s or "").replace("|", "/")
    rows = ["| %s | %s | %s | %s | %s |" % (path_of(f), cell(f["name"]), cell(f.get("author")), cell(f.get("license")), f.get("repo") or f["package"]) for f in sorted(want, key=lambda f: f["id"])]
    with open(os.path.join(here, "README.md"), "w", encoding="utf-8") as fh:
        fh.write("""# FM-1 firmware mirror

These are copies of the community firmwares for the M-VAVE FM-1, kept here so that
[FM1.Pocket](https://utopick.github.io/fm1-pocket/pocket/) has one steady place to download them from. When a version
isn't here yet, the app gets it from the firmware's own link instead.

Each firmware belongs to its author and keeps its own licence, which is listed below. Only firmwares with an open licence
are copied here, and each one's source code is at the link in its row. The files and this list are made by `update.py`,
from the list FM1.Pocket builds out of [the FM-1 Firmware Hub](https://thefirmwarehub.com/) and Joakim Eriksson's fm1-emu
list, so please don't edit them by hand. If you wrote one of these and want it taken down, open an issue and it will be
removed.

| File | Firmware | Author | Licence | Source |
|---|---|---|---|---|
""" + "\n".join(rows) + "\n")


def main():
    listed = json.load(open(LIST, encoding="utf-8"))
    want = [f for f in listed if f.get("package", "").startswith("https://") and OPEN.match(f.get("license") or "") and re.fullmatch(r"[\w.-]{1,40}", f["id"])]
    keep, got, failed = {path_of(f) for f in want}, 0, []
    for f in want:
        dest = os.path.join(here, path_of(f))
        if os.path.exists(dest): continue
        try:
            with urllib.request.urlopen(urllib.request.Request(f["package"], headers={"User-Agent": "fm1-firmwares-update"}), timeout=120) as r: data = r.read()
            if not 16 < len(data) <= 32 << 20: raise ValueError("size %d" % len(data))
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(dest, "wb") as fh: fh.write(data)
            got += 1
        except Exception as e:
            failed.append("%s (%s)" % (f["id"], e))  # its older version, if there is one, is dropped below: the page falls back to the link
    gone = 0
    for d in os.listdir(here):  # old versions and firmwares no longer listed (or no longer open) leave the mirror
        if d.startswith(".") or not os.path.isdir(os.path.join(here, d)): continue
        for n in os.listdir(os.path.join(here, d)):
            if d + "/" + n not in keep: os.remove(os.path.join(here, d, n)); gone += 1
        if not os.listdir(os.path.join(here, d)): os.rmdir(os.path.join(here, d))
    readme([f for f in want if os.path.exists(os.path.join(here, path_of(f)))])
    print("mirror: %d downloaded, %d removed, %d kept" % (got, gone, len(keep) - len(failed)))
    if failed: print("mirror: could not download " + ", ".join(failed))

    git("add", "-A")
    changed = subprocess.run(["git", "-C", here, "diff", "--cached", "--quiet"]).returncode != 0
    if changed: git("commit", "-q", AUTHOR, "-m", "Mirror update: %d new, %d removed" % (got, gone))
    squash = "--squash" in sys.argv
    if squash:  # one commit holding the files as they are now; the old history is dropped here and, after the force-push, on GitHub
        git("checkout", "-q", "--orphan", "squashed"); git("add", "-A")
        git("commit", "-q", AUTHOR, "-m", "The FM-1 community firmwares with an open licence, mirrored for FM1.Pocket")
        git("branch", "-D", "main"); git("branch", "-m", "main")
        git("reflog", "expire", "--expire=now", "--all"); git("gc", "-q", "--prune=now")
    size = sum(int(l.split()[1]) for l in git("count-objects", "-v").splitlines() if l.split()[0] in ("size:", "size-pack:")) >> 10
    print("repository: %d MB of history%s" % (size, " (past %d MB: run with --squash)" % WARN_MB if size > WARN_MB else ""))
    if "--push" in sys.argv:  # also pushes commits an earlier run made without --push
        subprocess.run(["git", "-C", here, "push", *(["--force"] if squash else []), "origin", "main"], check=True)


main()
