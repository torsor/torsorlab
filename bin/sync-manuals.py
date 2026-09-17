#!/usr/bin/env python3
"""Copy the built manuals into the site.

Manuals are authored and built elsewhere, each in its own directory with its
own Makefile. This copies the built HTML and PDF in so the site can serve them.

    make manuals                    # copy what is already built
    make manuals BUILD=1            # run each manual's own make html/pdf first
    make manuals GUIDES=/a:/b       # extra directories to search

Source directories are found by name under the search roots, which come from
$TORSOR_GUIDES (colon-separated, as a PATH). They are local paths that differ
per machine, so none is hard-coded here.

It refuses to copy a manual whose LaTeX source is newer than its build output,
because a stale manual on the site is worse than a missing one.
"""

import argparse
import os
import pathlib
import re
import shutil
import subprocess
import sys

ENV_VAR = "TORSOR_GUIDES"
SITE = pathlib.Path(__file__).resolve().parent.parent

# source directory name -> where it lands in the site, and its browser title.
# A manual can belong to a single skill (a doc page) or to a whole tool.
MANUALS = {
    "write-paper-guide": (
        "tools/torsor-writing/write-paper-guide/manual",
        "write-paper-guide: a user's manual",
    ),
    "write-critical-guide": (
        "tools/torsor-writing/write-critical-guide/manual",
        "write-critical-guide: a user's manual",
    ),
    "write-review-and-repair": (
        "tools/torsor-writing/write-review-and-repair/manual",
        "write-review-and-repair: a user's manual",
    ),
    "rr-guide": (
        "tools/research-room/manual",
        "research-room: a user's manual",
    ),
    "hive-guide": (
        "tools/hive/manual",
        "hive: a user's manual",
    ),
}


def search_roots(extra):
    roots = []
    for chunk in (extra or []) + os.environ.get(ENV_VAR, "").split(":"):
        chunk = chunk.strip()
        if chunk:
            p = pathlib.Path(chunk).expanduser()
            if p.is_dir():
                roots.append(p)
    return roots


def find_source(name, roots):
    for r in roots:
        # the manual directory may be a root itself, or sit under one
        if r.name == name and (r / "latex").is_dir():
            return r
        cand = r / name
        if (cand / "latex").is_dir():
            return cand
    return None


def newest_source(guide):
    tex = list((guide / "latex").rglob("*.tex"))
    return max((p.stat().st_mtime for p in tex), default=0.0)


def set_title(html_path, title):
    """tex2torsor emits <title>Document</title> for every manual, so tabs and
    bookmarks are all identically useless. Give each one its real name."""
    s = html_path.read_text()
    new, n = re.subn(r"<title>.*?</title>", f"<title>{title}</title>", s, count=1, flags=re.S)
    if n == 0:
        new = new.replace("</head>", f"  <title>{title}</title>\n</head>", 1)
    html_path.write_text(new)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="src", action="append", default=[],
                    help=f"a directory to search (repeatable; adds to ${ENV_VAR})")
    ap.add_argument("--build", action="store_true",
                    help="run each manual's own `make html pdf` before copying")
    args = ap.parse_args()

    roots = search_roots(args.src)
    if not roots:
        print(f"set {ENV_VAR} to the directories holding the manual sources "
              f"(colon-separated), or pass --from / `make manuals GUIDES=...`",
              file=sys.stderr)
        return 1

    errors = []
    for name, (dest_rel, title) in MANUALS.items():
        guide = find_source(name, roots)
        if guide is None:
            errors.append(f"{name}: not found under {', '.join(str(r) for r in roots)}")
            continue

        if args.build:
            r = subprocess.run(["make", "html", "pdf"], cwd=guide,
                               capture_output=True, text=True)
            if r.returncode != 0:
                errors.append(f"{name}: build failed\n{r.stderr.strip()[:400]}")
                continue

        html = guide / "html" / "manual.html"
        pdf = guide / "latex" / "main.pdf"
        missing = [str(p.relative_to(guide)) for p in (html, pdf) if not p.exists()]
        if missing:
            errors.append(f"{name}: not built — missing {', '.join(missing)}")
            continue

        src_mtime = newest_source(guide)
        stale = [b.name for b in (html, pdf) if b.stat().st_mtime < src_mtime]
        if stale:
            errors.append(f"{name}: {', '.join(stale)} older than the LaTeX source — "
                          f"rebuild, or pass BUILD=1")
            continue

        dest = SITE / dest_rel
        dest.mkdir(parents=True, exist_ok=True)
        shutil.copy2(html, dest / "index.html")
        shutil.copy2(pdf, dest / "manual.pdf")
        for css in ("tokens.css", "manual.css"):
            shutil.copy2(guide / "html" / css, dest / css)
        set_title(dest / "index.html", title)
        kb = sum(f.stat().st_size for f in dest.iterdir()) // 1024
        print(f"  {name:24} -> {dest_rel}  ({kb}kb)")

    for e in errors:
        print(f"  ! {e}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
