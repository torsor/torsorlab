#!/usr/bin/env python3
"""Assert the collections are wired correctly. Run via `make check`.

Reads the source files (not _site), so it catches a broken link before the
build silently produces a 404.
"""

import pathlib
import re
import sys

try:
    import yaml
except ImportError:  # pragma: no cover - yaml ships with the Jekyll toolchain box
    yaml = None

ROOT = pathlib.Path(__file__).resolve().parent.parent
FM = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def front_matter(path):
    m = FM.match(path.read_text())
    if not m:
        return None
    out = {}
    for line in m.group(1).splitlines():
        if line.startswith((" ", "-", "#")) or ":" not in line:
            continue
        k, _, v = line.partition(":")
        out[k.strip()] = v.strip().strip("\"'")
    return out


def check_front_matter(errors):
    """Every page must have front matter that actually parses.

    Jekyll does not fail the build on malformed front matter — it silently
    treats the file as having none, falls back to the default layout, and
    publishes a page with the content missing. That shipped once; this is the
    guard so it cannot ship again.

    Layouts are not required here: they come from the `defaults` in _config.yml.
    """
    pages = (
        [ROOT / n for n in ("index.md", "about.md", "tools.md", "404.md")]
        + sorted((ROOT / "_tools").glob("*.md"))
        + sorted((ROOT / "_docs").rglob("*.md"))
    )
    for p in pages:
        if not p.exists():
            errors.append(f"{p.relative_to(ROOT)}: expected page is missing")
            continue
        rel = p.relative_to(ROOT)
        m = FM.match(p.read_text())
        if not m:
            errors.append(f"{rel}: no front matter — Jekyll will not render it as a page")
            continue
        if yaml is None:
            continue
        try:
            data = yaml.safe_load(m.group(1))
        except yaml.YAMLError as e:
            first = str(e).strip().splitlines()[0]
            errors.append(f"{rel}: front matter is not valid YAML — {first}")
            continue
        if not isinstance(data, dict):
            errors.append(f"{rel}: front matter is not a mapping (check block-scalar indentation)")


def main():
    errors = []
    check_front_matter(errors)

    tools = {}
    for p in sorted((ROOT / "_tools").glob("*.md")):
        fm = front_matter(p)
        if fm is None:
            errors.append(f"{p.name}: no front matter")
            continue
        for key in ("title", "slug", "tagline", "status", "order"):
            if key not in fm:
                errors.append(f"_tools/{p.name}: missing `{key}`")
        if fm.get("status") not in ("released", "coming"):
            errors.append(f"_tools/{p.name}: status must be released|coming")
        tools[fm.get("slug")] = fm

    docs_by_tool = {}
    for p in sorted((ROOT / "_docs").rglob("*.md")):
        rel = p.relative_to(ROOT / "_docs")
        fm = front_matter(p)
        if fm is None:
            errors.append(f"_docs/{rel}: no front matter")
            continue
        for key in ("title", "tool", "slug", "permalink", "order", "summary"):
            if key not in fm:
                errors.append(f"_docs/{rel}: missing `{key}`")
                continue
        tool, slug = fm.get("tool"), fm.get("slug")
        if tool not in tools:
            errors.append(f"_docs/{rel}: tool `{tool}` has no _tools entry")
        want = f"/tools/{tool}/{slug}/"
        if fm.get("permalink") != want:
            errors.append(
                f"_docs/{rel}: permalink is {fm.get('permalink')}, expected {want}"
            )
        if rel.parent.name != tool:
            errors.append(f"_docs/{rel}: lives under {rel.parent.name}/ but tool is {tool}")
        docs_by_tool.setdefault(tool, []).append((fm.get("order"), rel))

    for tool, entries in docs_by_tool.items():
        orders = [o for o, _ in entries]
        dupes = {o for o in orders if orders.count(o) > 1}
        for o in sorted(dupes):
            errors.append(f"_docs/{tool}: duplicate order `{o}`")

    for slug, fm in tools.items():
        if fm.get("status") != "released" or docs_by_tool.get(slug):
            continue
        # A tool can go public before its documentation is written, but that
        # has to be declared rather than silently tolerated.
        if fm.get("docs_pending") != "true":
            errors.append(
                f"_tools/{slug}: released but has no docs — write some, or set "
                f"`docs_pending: true` to say they are still being written")

    # anything that advertises a manual must actually have one on disk
    for p in sorted((ROOT / "_docs").rglob("*.md")):
        fm = front_matter(p) or {}
        if fm.get("manual") != "true":
            continue
        manual = ROOT / "tools" / fm.get("tool", "") / fm.get("slug", "") / "manual" / "index.html"
        if not manual.exists():
            errors.append(
                f"_docs/{p.relative_to(ROOT / '_docs')}: manual: true but "
                f"{manual.relative_to(ROOT)} is missing — run `make manuals`")

    for p in sorted((ROOT / "_tools").glob("*.md")):
        fm = front_matter(p) or {}
        if fm.get("manual") != "true":
            continue
        manual = ROOT / "tools" / fm.get("slug", "") / "manual" / "index.html"
        if not manual.exists():
            errors.append(
                f"_tools/{p.name}: manual: true but {manual.relative_to(ROOT)} "
                f"is missing — run `make manuals`")

    if errors:
        print("check failed:")
        for e in errors:
            print(f"  - {e}")
        return 1

    n_docs = sum(len(v) for v in docs_by_tool.values())
    print(f"check passed: {len(tools)} tools, {n_docs} doc pages")
    return 0


if __name__ == "__main__":
    sys.exit(main())
