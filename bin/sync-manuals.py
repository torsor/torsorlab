#!/usr/bin/env python3
"""Copy the built torsor-writing manuals into the site.

The manuals are authored and built elsewhere — in the guides directory beside
the plugin repo — and this copies the built HTML and PDF in so the site can
serve them at /tools/torsor-writing/<skill>/manual/.

    make manuals                    # copy what is already built
    make manuals BUILD=1            # run the guides' own make html/pdf first

It refuses to copy a manual whose LaTeX source is newer than its build output,
because a stale manual on the site is worse than a missing one. Rebuild it (or
pass BUILD=1) and run again.
"""

import argparse
import os
import pathlib
import shutil
import subprocess
import sys

# The three skills that have manuals. Add a line when a fourth is written.
MANUALS = ["write-paper-guide", "write-critical-guide", "write-review-and-repair"]

SITE = pathlib.Path(__file__).resolve().parent.parent
DEST_ROOT = SITE / "tools" / "torsor-writing"
# Where the manuals are authored. This is a local path that differs per machine,
# so it is not hard-coded here: set TORSOR_GUIDES, or pass --from / GUIDES=.
ENV_VAR = "TORSOR_GUIDES"


def newest_source(guide: pathlib.Path) -> float:
    tex = list((guide / "latex").rglob("*.tex"))
    return max((p.stat().st_mtime for p in tex), default=0.0)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="src", type=pathlib.Path,
                    default=pathlib.Path(os.environ[ENV_VAR]) if os.environ.get(ENV_VAR) else None,
                    help="the guides directory holding the built manuals "
                         f"(default: ${ENV_VAR})")
    ap.add_argument("--build", action="store_true",
                    help="run each guide's own `make html pdf` before copying")
    args = ap.parse_args()

    if args.src is None:
        print(f"set {ENV_VAR} to the guides directory, or pass --from / "
              f"`make manuals GUIDES=...`", file=sys.stderr)
        return 1
    if not args.src.is_dir():
        print(f"guides directory not found: {args.src}", file=sys.stderr)
        return 1

    errors = []
    for name in MANUALS:
        guide = args.src / name
        if not guide.is_dir():
            errors.append(f"{name}: not in {args.src}")
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
        for built in (html, pdf):
            if built.stat().st_mtime < src_mtime:
                errors.append(
                    f"{name}: {built.name} is older than the LaTeX source — "
                    f"rebuild it, or pass BUILD=1")
                break
        else:
            dest = DEST_ROOT / name / "manual"
            dest.mkdir(parents=True, exist_ok=True)
            shutil.copy2(html, dest / "index.html")
            shutil.copy2(pdf, dest / "manual.pdf")
            for css in ("tokens.css", "manual.css"):
                shutil.copy2(guide / "html" / css, dest / css)
            kb = sum(f.stat().st_size for f in dest.iterdir()) // 1024
            print(f"  {name}  ->  tools/torsor-writing/{name}/manual/  ({kb}kb)")

    for e in errors:
        print(f"  ! {e}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
