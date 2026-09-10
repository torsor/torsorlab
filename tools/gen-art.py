#!/usr/bin/env python3
"""Generate the site's static artwork into assets/img/.

Ported from torsor-style/style-b/Torsor-Design-B.dc.html so the site ships no
runtime JS for artwork. Run it only when you want to retune the curves:

    python3 tools/gen-art.py

The site build never runs this; the output is committed.
"""

import math
import pathlib

OUT = pathlib.Path(__file__).resolve().parent.parent / "assets" / "img"

# Kept in sync by hand with _sass/_tokens.scss. SVG files cannot read CSS
# custom properties, so these four are the only duplicated colors in the repo.
VIOLET_LIGHT = "#c5c2ec"
VIOLET = "#8b86d6"
TEAL = "#3fa39d"
CORAL = "#df8567"
CREAM = "#faf6ec"


def blob_path(cx, cy, r, phase, n=9):
    """One irregular closed ring: N points on a wobbling circle, joined by
    quadratic segments through their midpoints."""
    pts = []
    for i in range(n):
        a = i / n * 2 * math.pi
        rr = r * (
            1
            + 0.10 * math.sin(phase + i * 1.7)
            + 0.06 * math.cos(phase * 1.3 + i * 2.3)
        )
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))

    def mid(a, b):
        return ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)

    m0 = mid(pts[-1], pts[0])
    d = f"M {m0[0]:.2f} {m0[1]:.2f} "
    for i in range(n):
        m = mid(pts[i], pts[(i + 1) % n])
        d += f"Q {pts[i][0]:.2f} {pts[i][1]:.2f} {m[0]:.2f} {m[1]:.2f} "
    return d + "Z"


def contour_field(name, w, h, rings, r0, step, phase_step=0.9, opacity0=0.5):
    """Nested contour rings — the topographic ground texture."""
    cx, cy = w / 2, h / 2
    paths = []
    for k in range(rings):
        d = blob_path(cx, cy, r0 + k * step, k * phase_step)
        o = max(0.05, opacity0 - k * 0.045)
        paths.append(
            f'  <path d="{d}" fill="none" stroke="{VIOLET_LIGHT}" '
            f'stroke-width="1" opacity="{o:.3f}"/>'
        )
    body = "\n".join(paths)
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'preserveAspectRatio="xMidYMid slice" aria-hidden="true">\n{body}\n</svg>\n'
    )
    (OUT / name).write_text(svg)


def mark():
    """The torsorlab mark: violet ring, teal half-arc, coral basepoint."""
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" aria-hidden="true">
  <circle cx="16" cy="16" r="9" fill="none" stroke="{VIOLET}" stroke-width="2"/>
  <path d="M16 7 A9 9 0 0 1 16 25" fill="none" stroke="{TEAL}" stroke-width="2"/>
  <circle cx="16" cy="7" r="2.6" fill="{CORAL}"/>
</svg>
"""
    (OUT / "mark.svg").write_text(svg)


def spine():
    """The vertebral rail used down the left of doc pages."""
    w, h, cx = 60, 560, 30
    k = [
        f'  <line x1="{cx - 5}" y1="18" x2="{cx - 5}" y2="{h - 18}" '
        f'stroke="{VIOLET_LIGHT}" stroke-width="2"/>',
        f'  <line x1="{cx + 5}" y1="18" x2="{cx + 5}" y2="{h - 18}" '
        f'stroke="{VIOLET_LIGHT}" stroke-width="2"/>',
        f'  <line x1="{cx}" y1="18" x2="{cx}" y2="{h - 18}" stroke="{VIOLET}" '
        f'stroke-width="1" stroke-dasharray="1 7" opacity="0.7"/>',
    ]
    rows, top, bot = 13, 40, h - 40
    for i in range(rows):
        y = top + (bot - top) * i / (rows - 1)
        amp = 18 * math.sin(math.pi * (i + 0.5) / rows) + 5
        k.append(
            f'  <path d="M {cx - 5} {y:.1f} Q {cx - amp:.1f} {y - 9:.1f} '
            f'{cx - amp - 3:.1f} {y + 5:.1f}" fill="none" stroke="{VIOLET}" '
            f'stroke-width="1.5" stroke-linecap="round" opacity="0.85"/>'
        )
        k.append(
            f'  <path d="M {cx + 5} {y:.1f} Q {cx + amp:.1f} {y - 9:.1f} '
            f'{cx + amp + 3:.1f} {y + 5:.1f}" fill="none" stroke="{VIOLET}" '
            f'stroke-width="1.5" stroke-linecap="round" opacity="0.85"/>'
        )
        k.append(
            f'  <circle cx="{cx}" cy="{y:.1f}" r="4" fill="{CREAM}" '
            f'stroke="{VIOLET}" stroke-width="1.5"/>'
        )
        k.append(
            f'  <circle cx="{cx - amp - 3:.1f}" cy="{y + 5:.1f}" r="1.8" '
            f'fill="{VIOLET_LIGHT}"/>'
        )
        k.append(
            f'  <circle cx="{cx + amp + 3:.1f}" cy="{y + 5:.1f}" r="1.8" '
            f'fill="{VIOLET_LIGHT}"/>'
        )
    body = "\n".join(k)
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'preserveAspectRatio="xMidYMid meet" aria-hidden="true">\n{body}\n</svg>\n'
    )
    (OUT / "spine.svg").write_text(svg)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    mark()
    spine()
    contour_field("contour-hero.svg", 780, 520, rings=9, r0=70, step=40)
    contour_field("contour-card.svg", 390, 340, rings=7, r0=52, step=27)
    for f in sorted(OUT.iterdir()):
        print(f"  {f.name}  {f.stat().st_size:>6}b")
