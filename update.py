#!/usr/bin/env python3
"""Brings this mirror up to date with FM1.Pocket's firmware list, then commits.

    python3 update.py                 # download what is new, drop old versions, rewrite README.md, commit
    python3 update.py --push          # the same, then push (GitHub Pages publishes it)
    python3 update.py --squash --push # also replace the whole history with one commit, then force-push
    python3 update.py --notices       # fetch the licence files of every firmware again, not only of the new ones

The list is fm1-pocket's pocket/vendor/firmwares.json (made by its pocket/update-firmwares.py, which runs this script at the
end), or the file given as an argument. Each firmware with an open licence is kept as <id>/<version>.fwsc, the address the
page asks for first; a version this mirror lacks makes the page fall back to the firmware's own link. Next to it go the
licence and notice files of its repository (LICENSE, COPYING, NOTICE, LICENSING, THIRD_PARTY..., up to three folders deep),
because most licences ask that copies keep them: firmwares built on M-VAVE's SDK, for one, may only be passed on with its
THIRD_PARTY.md. A firmware the list gives an "rfm1" (its own code built as WebAssembly, from RemoteFM1FW's release) also
gets that file, <id>/<name>.rfm1, which the page runs instead of emulating the chip; the file carries its own licence texts. The list of a repository's files comes from GitHub's API, with GITHUB_TOKEN or gh's login when there is one.

Every update adds its new packages to the git history for good, so the repository grows even though the folder doesn't.
GitHub wants repositories under about 1 GB, so the script warns past WARN_MB and --squash starts the history again from
the files as they are now.
Standard library and git only.
"""
import json, os, re, subprocess, sys, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor

here = os.path.dirname(os.path.abspath(__file__))
args = [a for a in sys.argv[1:] if not a.startswith("--")]
LIST = args[0] if args else os.path.join(here, "..", "fm1-pocket", "pocket", "vendor", "firmwares.json")
OPEN = re.compile(r"^(GPL|LGPL|MPL|MIT|Apache|BSD)")  # licences that let us pass the package on; the rest stay at their author's
WARN_MB = 700
RFM1 = "https://github.com/Quixotic7/RemoteFM1FW/releases/latest/download/"
OWN_RFM1 = os.path.join(here, "..", "fm1-rfm1", "out")  # our own builds (TP/fm1-rfm1's convert.py): copied from there, not downloaded
WHO = ["-c", "user.name=utopick", "-c", "user.email=310144039+utopick@users.noreply.github.com"]
AUTHOR = "--author=utopick <310144039+utopick@users.noreply.github.com>"


def git(*a, **k):
    return subprocess.run(["git", "-C", here, *WHO, *a], check=True, text=True, capture_output=True, **k).stdout


def path_of(f):  # also used by the page: "https://utopick.github.io/fm1-firmwares/" + id + "/" + version + ".fwsc"
    return f["id"] + "/" + (re.sub(r"[^\w.-]", "_", f.get("version") or "") or "0") + ".fwsc"


NOTICE = re.compile(r"^(LICEN[CS]E|COPYING|NOTICE|THIRD[_-]PART|LICENSING)", re.I)
ROOT_NOTICES = ["LICENSE", "LICENSE.md", "LICENSE.txt", "COPYING", "NOTICE.md", "LICENSING.md", "THIRD_PARTY.md", "THIRD_PARTY_NOTICES.md"]


def token():
    t = os.environ.get("GITHUB_TOKEN")
    if t: return t
    try: return subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, timeout=20).stdout.strip()
    except Exception: return ""


TOKEN = token()


def notices(f):
    """The licence and notice files of the firmware's GitHub repository, up to three folders deep (SDK notices such as
    M-VAVE's THIRD_PARTY.md are often in one), into <id>/ with "--" for "/". Without the file list (no token and over
    GitHub's limit) it tries the usual names at the root."""
    m = re.match(r"https://github\.com/([\w.-]+)/([\w.-]+)", f.get("repo") or "")
    if not m: return []
    head = {"User-Agent": "fm1-firmwares-update", **({"Authorization": "Bearer " + TOKEN} if TOKEN else {})}
    try:
        with urllib.request.urlopen(urllib.request.Request("https://api.github.com/repos/%s/%s/git/trees/HEAD?recursive=1" % (m[1], m[2]), headers=head), timeout=60) as r:
            paths = [t["path"] for t in json.load(r)["tree"] if t["type"] == "blob" and NOTICE.match(t["path"].rsplit("/", 1)[-1]) and t["path"].count("/") <= 3]
    except Exception:
        paths = ROOT_NOTICES
    def one(p):
        try:
            with urllib.request.urlopen(urllib.request.Request("https://raw.githubusercontent.com/%s/%s/HEAD/%s" % (m[1], m[2], urllib.parse.quote(p)), headers={"User-Agent": "fm1-firmwares-update"}), timeout=30) as r: data = r.read()
        except Exception: return None  # with the usual names, mostly 404: that one is not there
        if not 0 < len(data) <= 1 << 20: return None
        with open(os.path.join(here, f["id"], p.replace("/", "--")), "wb") as fh: fh.write(data)
        return p
    with ThreadPoolExecutor(8) as ex: return [p for p in ex.map(one, paths[:40]) if p]


def rfm1_licence(data):
    """The licence in an .rfm1's manifest (its "rfm1" custom section), or "" if the file is not an .rfm1."""
    if data[:8] != b"\0asm\1\0\0\0": return ""
    def leb(i):
        v = s = 0
        while True:
            c = data[i]; i += 1; v |= (c & 0x7f) << s; s += 7
            if not c & 0x80: return v, i
    i = 8
    while i < len(data):
        sid = data[i]; size, i = leb(i + 1); end = i + size
        if sid == 0:
            n, k = leb(i)
            if data[k:k + n] == b"rfm1":
                try: return str(json.loads(data[k + n:end]).get("license") or "")
                except Exception: return ""
        i = end
    return ""


def rfm1(f):
    """Downloads the firmware's .rfm1 when it is new (copies our own build when it changed); returns 1 if it did. One with no open licence in its manifest is not kept."""
    n = f.get("rfm1") or ""
    dest = os.path.join(here, f["id"], n)
    if not re.fullmatch(r"[\w.-]{1,80}\.rfm1", n): return 0
    if os.path.exists(os.path.join(OWN_RFM1, n)):  # (a glue fix keeps the name, so a copy that differs is replaced)
        with open(os.path.join(OWN_RFM1, n), "rb") as fh: data = fh.read()
        if os.path.exists(dest) and open(dest, "rb").read() == data: return 0
    elif os.path.exists(dest): return 0
    else:
        with urllib.request.urlopen(urllib.request.Request(RFM1 + n, headers={"User-Agent": "fm1-firmwares-update"}), timeout=180) as r: data = r.read()
    if not 16 < len(data) <= 40 << 20: raise ValueError("size %d" % len(data))
    if not OPEN.match(rfm1_licence(data)): raise ValueError("no open licence in its manifest")
    with open(dest, "wb") as fh: fh.write(data)
    return 1


def readme(want):
    cell = lambda s: (s or "").replace("|", "/")
    note = lambda f: ", ".join("[%s](%s/%s)" % (n, f["id"], n) for n in sorted(os.listdir(os.path.join(here, f["id"]))) if not n.endswith((".fwsc", ".rfm1"))) or "none found"
    fast = lambda f: "[%s](%s/%s)" % (f["rfm1"], f["id"], f["rfm1"]) if f.get("rfm1") and os.path.exists(os.path.join(here, f["id"], f["rfm1"])) else ""
    rows = ["| %s | %s | %s | %s | %s | %s | %s |" % (path_of(f), fast(f), cell(f["name"]), cell(f.get("author")), cell(f.get("license")), note(f), f.get("repo") or f["package"]) for f in sorted(want, key=lambda f: f["id"])]
    with open(os.path.join(here, "README.md"), "w", encoding="utf-8") as fh:
        fh.write("""# FM-1 firmware mirror

These are copies of the community firmwares for the M-VAVE FM-1, kept here so that
[FM1.Pocket](https://utopick.github.io/fm1-pocket/pocket/) has one steady place to download them from. When a version
isn't here yet, the app gets it from the firmware's own link instead.

Each firmware belongs to its author and keeps its own licence, which is listed below. Only firmwares with an open licence
are copied here. Each one's folder also holds the licence and notice files of its repository, and its source code is at
the link in its row. Some also have a fast build, an `.rfm1` from
[RemoteFM1FW](https://github.com/Quixotic7/RemoteFM1FW): the firmware's own code built as WebAssembly by Quixotic7's FM1VST,
with its licence texts and the exact source commit inside the file. A few were built here instead, with the same
FM1VST tools and glue of our own, for firmwares that release doesn't have yet. The files and this list are made by `update.py`,
from the list FM1.Pocket builds out of [the FM-1 Firmware Hub](https://thefirmwarehub.com/) and Joakim Eriksson's fm1-emu
list, so please don't edit them by hand. If you wrote one of these and want it taken down, open an issue and it will be
removed.

| File | Fast build | Firmware | Author | Licence | Notices | Source |
|---|---|---|---|---|---|---|
""" + "\n".join(rows) + "\n")


def main():
    listed = json.load(open(LIST, encoding="utf-8"))
    want = [f for f in listed if f.get("package", "").startswith("https://") and OPEN.match(f.get("license") or "") and re.fullmatch(r"[\w.-]{1,40}", f["id"])]
    keep, got, fast, failed = {path_of(f) for f in want} | {f["id"] + "/" + f["rfm1"] for f in want if f.get("rfm1")}, 0, 0, []
    for f in want:
        dest = os.path.join(here, path_of(f))
        if os.path.exists(dest):
            if "--notices" in sys.argv:  # fetch every firmware's notices again
                for n in os.listdir(os.path.dirname(dest)):
                    if not n.endswith((".fwsc", ".rfm1")): os.remove(os.path.join(os.path.dirname(dest), n))
                notices(f)
        else:
            try:
                with urllib.request.urlopen(urllib.request.Request(f["package"], headers={"User-Agent": "fm1-firmwares-update"}), timeout=120) as r: data = r.read()
                if not 16 < len(data) <= 32 << 20: raise ValueError("size %d" % len(data))
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                with open(dest, "wb") as fh: fh.write(data)
                for n in os.listdir(os.path.dirname(dest)):  # the old version's notices go with it
                    if not n.endswith((".fwsc", ".rfm1")): os.remove(os.path.join(os.path.dirname(dest), n))
                notices(f)
                got += 1
            except Exception as e:
                failed.append("%s (%s)" % (f["id"], e))  # its older version, if there is one, is dropped below: the page falls back to the link
                continue
        try: fast += rfm1(f)
        except Exception as e: failed.append("%s's .rfm1 (%s)" % (f["id"], e))
    gone, ids = 0, {f["id"] for f in want}
    for d in os.listdir(here):  # old versions and firmwares no longer listed (or no longer open) leave the mirror
        if d.startswith(".") or not os.path.isdir(os.path.join(here, d)): continue
        for n in os.listdir(os.path.join(here, d)):
            if d not in ids or n.endswith((".fwsc", ".rfm1")) and d + "/" + n not in keep: os.remove(os.path.join(here, d, n)); gone += 1
        if not os.listdir(os.path.join(here, d)): os.rmdir(os.path.join(here, d))
    readme([f for f in want if os.path.exists(os.path.join(here, path_of(f)))])
    print("mirror: %d downloaded, %d fast builds downloaded, %d removed, %d files kept" % (got, fast, gone, len(keep) - len(failed)))
    if failed: print("mirror: could not download " + ", ".join(failed))

    git("add", "-A")
    changed = subprocess.run(["git", "-C", here, "diff", "--cached", "--quiet"]).returncode != 0
    if changed: git("commit", "-q", AUTHOR, "-m", "Mirror update: %d new, %d fast builds, %d removed" % (got, fast, gone))
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
