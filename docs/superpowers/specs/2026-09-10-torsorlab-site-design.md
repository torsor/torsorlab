# torsorlab — site design

**Date:** 2026-09-10
**Status:** approved, ready for implementation planning

## Purpose

A Jekyll site presenting torsorlab: the name under which Danny Krashen's agentic-AI
work is done and credited. The site is a showcase *and* a documentation host — a
visitor arriving cold should be able to learn what a tool is, why it exists, and how
to use it, without leaving for a GitHub README.

At launch it covers three tools. One is public and gets full documentation; two are
announced but not yet released.

## Constraints and decisions

These were settled in brainstorming and are not open questions:

| Decision | Value |
|---|---|
| Site title | `torsorlab` |
| Generator | Jekyll, hand-rolled, no third-party theme |
| Hosting | **Local only** for now (`jekyll serve`). Nothing is pushed. |
| Eventual home | `lab.torsor.org` (domain `torsor.org` is owned) |
| Docs sourcing | **Hand-authored on the site.** No sync script. Source repos remain the source of truth for code; the site is a separate, curated telling. |
| Docs depth | One page per skill (eleven for `torsor-writing`), plus an overview page |
| Launch scope | All three tools appear; two marked `COMING` |
| Visual base | `torsor-style/style-b`, Direction A for site pages, Direction B for doc pages |

### Explicitly out of scope

- Any push, deploy, or DNS change. The Pages workflow and `CNAME` are written but inert.
- A posts/blog stream. (Considered and declined; the structure does not preclude adding
  one later.)
- Client-side search. Eleven doc pages do not need it.
- Any content drawn from the private `workshop-kit-dev` or `hive-v2` repos beyond a
  public-safe one-paragraph description. No internal hostnames, no repo URLs.

## Source material

**`torsor/claude-plugins`** (public, GitHub) — a Claude Code plugin marketplace. One
plugin, `torsor-writing`: eleven LaTeX writing skills that each produce a document in
the torsor house format (LaTeX source with PDF, HTML, EPUB, Markdown output). The
eleven, as named in the repo README:

`write-manual`, `write-paper-guide`, `write-critical-guide`, `write-paper-repairs`,
`write-review-and-repair`, `write-topic-guide`, `write-study-guide`,
`write-body-of-work-summary`, `write-workshop-state-guide`, `write-pure-math-paper`,
`write-technical-report`.

Install is `claude plugin marketplace add` then `claude plugin install
torsor-writing@torsor-plugins`. Build prerequisites (TeX, pandoc, `latexd`, `lab-view`)
belong on the tool page, not repeated on every skill page.

**`workshop-kit-dev`** (local, private) — the workshop platform: a provisioned host
running AI-aided mathematics research sessions. Public description only.

**`hive-v2`** (local, private) — a fleet console for agent sessions (Claude Code, Codex)
running in tmux on always-on boxes; a Rust rewrite of the original shell toolkit. Public
description only.

**`torsor-style/style-b`** — the design source. Two `.dc.html` canvas artboards plus
`support.js`, which carries the generative artwork: `blobPath` / `contourField` (nested
irregular contour rings), `spineRail` (a vertebral rail), and `makeMark` (the logo).

## Design system

One SCSS token file; both directions draw from it. Nothing hard-codes a hex value
outside `_tokens.scss`.

### Color

| Token | Value | Role |
|---|---|---|
| `--cream` | `#faf6ec` | topographic ground |
| `--cream-panel` | `#fbf8ef` | raised card on cream |
| `--lav` | `#eceaf7` | spinal ground |
| `--lav-panel` | `#efedf8` | marginalia column |
| `--lav-bar` | `#e6e3f4` | spinal top bar |
| `--ink` | `#2c2b4d` | headings, strong text |
| `--prose` | `#4a4868` | body text |
| `--muted` | `#6c6a92` | secondary text |
| `--faint` | `#8d8aa8` | tertiary, inactive nav |
| `--violet` | `#8b86d6` | primary accent, mark ring, micro-labels |
| `--teal` | `#3fa39d` | secondary accent, section eyebrows |
| `--coral` | `#df8567` | basepoint dot, `COMING` chips, alerts |
| `--rule-cream` | `#e6e0cf` | borders on cream |
| `--rule-lav` | `#ddd9ef` | borders on lavender |

Contrast: `--prose` on `--cream` and `--ink` on both grounds clear WCAG AA for body text.
`--faint` is for non-essential text only and must never carry meaning alone.

### Type

- **Space Grotesk** 400/500/600/700 — site headings, nav, card titles. Tight tracking
  (`-1px` at 40px, `-0.2px` at 23px).
- **Hanken Grotesk** 400/500/600 — body prose, 15.5px / 1.72.
- **Sora** 400/600 — doc-page headings and marginalia notes.
- **Space Mono** 400/700 — micro-labels (11px, 2px letter-spacing, uppercase), captions,
  code, breadcrumbs.

Loaded from Google Fonts with `preconnect`, each with a real fallback stack.

### Artwork

Three pieces, ported from `support.js` into static assets by a one-time generator script
(`tools/gen-art.py`) so the site ships no runtime JS for artwork:

1. **`mark.svg`** — viewBox 32×32: violet ring `r=9` `stroke-width=2`, teal half-arc
   `M16 7 A9 9 0 0 1 16 25`, coral dot `r=2.6` at `(16,7)`. Rotates 18s linear infinite
   via CSS, wrapped in `@media (prefers-reduced-motion: reduce)` to stop.
2. **`contour-*.svg`** — nested irregular rings from `blobPath`, emitted at a few sizes
   for hero and card backgrounds. Low-opacity violet strokes on cream.
3. **`spine.svg`** — the vertebral rail: twin verticals, dashed nerve line, thirteen
   vertebrae with paired curved ribs and terminal dots. Used as the doc-page progress rail.

The generator is committed alongside its output so the artwork can be regenerated or
retuned, but the site build never runs it.

### Two treatments

**Topographic** — home, about, tools index, tool pages. Cream ground, horizontal panels
with `1px` rules and a soft drop shadow (`0 18px 50px -24px rgba(44,43,77,.45)`), contour
field behind the hero, generous vertical rhythm. Content column max 760px for prose,
full width for card grids.

**Spinal** — doc pages. Lavender ground, a three-column frame: spine rail (96px, section
progress) / content / marginalia (308px, dashed left border, numbered notes). Sora
headings, Space Mono captions.

### Responsive

Single breakpoint at 900px. Below it: spinal collapses to one column, rail hidden,
marginalia notes inline after the section they annotate; card grids go one-up; hero
contour art shrinks and drops behind text at reduced opacity. Side gutter never below
16px. No horizontal scroll except inside `overflow-x: auto` wrappers on tables and code.

## Site structure

```
torsorlab/
  _config.yml
  Gemfile / Gemfile.lock
  Makefile                    serve, build, check
  CNAME                       lab.torsor.org — inert until deploy
  .github/workflows/pages.yml disabled (workflow_dispatch only)
  _data/nav.yml
  _tools/
    torsor-writing.md         status: released
    workshop-kit.md           status: coming
    hive.md                   status: coming
  _docs/
    torsor-writing/00-overview.md
    torsor-writing/01-write-manual.md
    …
    torsor-writing/11-write-technical-report.md
  _layouts/    base.html  home.html  page.html  tool.html  doc.html
  _includes/   head.html  nav.html  footer.html  mark.svg
               tool-card.html  doc-nav.html  marginalia.html
  _sass/       _tokens.scss _base.scss _topographic.scss _spinal.scss
  assets/css/main.scss
  assets/img/  mark.svg contour-*.svg spine.svg
  tools/gen-art.py
  index.md  tools.md  about.md
  README.md
```

### Collections

`_tools` — output `true`, permalink `/tools/:name/`. Front matter:

```yaml
title:        # torsor-writing
tagline:      # one line, used on the card
status:       # released | coming
repo:         # URL, or omitted when private
order:        # integer, controls index order
```

`_docs` — output `true`, `permalink: /tools/:path/`. Filenames carry a numeric prefix
for ordering (`01-write-manual.md`) which must not appear in the URL, so each doc
declares an explicit `permalink` in its own front matter, overriding the collection
default. Front matter:

```yaml
title:
tool:         # torsor-writing — the key joining a doc to its tool
order:        # integer within the tool, matching the filename prefix
slug:         # write-manual
permalink:    # /tools/torsor-writing/write-manual/
summary:      # one line for the overview index
```

`make check` asserts each doc's `permalink` equals `/tools/<tool>/<slug>/`, so the
redundancy between these three keys cannot silently diverge.

A tool page lists its docs by filtering `site.docs` on `doc.tool == page.slug` — the
tool's filename slug, not its display title — and sorting by `order`. Adding a tool's
docs later means dropping files into a folder; no index is edited by hand.

## Page inventory

**Home (`/`)** — hero: the mark, `torsorlab`, and a statement of what the lab is and the
collaborative-credit premise, over the contour field. Then the three tools as cards.
Then a short "how the lab works" band.

**Tools (`/tools/`)** — the three cards, released first. `COMING` cards carry a coral
chip, the public one-paragraph description, and no outbound link.

**Tool page (`/tools/torsor-writing/`)** — what it is, why it exists, install, build
prerequisites, then the eleven skills as a linked table into the docs.

**Doc pages (`/tools/torsor-writing/<skill>/`)** — one per skill, spinal layout.
**Deliberately minimal at build time** (decided 2026-09-10): each page carries the
skill's name, a one-line summary, its invocation, and its outputs — enough that the page
exists and the structure is proven. Danny writes the real prose later. The layout
supports the fuller shape (what it writes / who for / prerequisites / worked invocation /
marginalia) whenever content arrives; nothing needs restructuring to grow.

**About (`/about/`)** — what torsorlab names, how the work is done, and how to credit it:
a suggested acknowledgement line and a note on what the name covers. **This page is a
stub for Danny to rewrite** — it is the page most needing his own words.

## Verification

- `make serve` renders locally without warnings; `make build` succeeds.
- `make check` — assertions run against the built `_site`: every `_docs` entry has a
  `tool` matching an existing `_tools` slug; every `released` tool has at least one doc;
  every doc's `permalink` equals `/tools/<tool>/<slug>/`; no `_docs` order collides
  within a tool. Non-zero exit on any failure.
- Screenshots of home, the tool page, and a doc page at desktop (1280px) and phone
  (390px) width, reviewed before the work is called done.
- No network calls at build time. No content from private repos beyond the agreed
  public descriptions.

## Risks

- **Hand-authored docs drift** from the plugin as it changes. Accepted deliberately: the
  site is a curated telling, and a stale sentence is a smaller cost than sync machinery.
  Mitigation is a note in `README.md` saying which upstream files a doc page was drawn
  from.
- **Eleven doc pages is real writing.** Resolved by shipping them as minimal stubs; the
  fallback grouped-pages structure remains available since the schema supports either.

## Editability

A stated requirement, not a nicety: Danny edits this site by hand. Therefore —

- Every color and font lives in `_sass/_tokens.scss` as a CSS custom property. No hex
  value appears anywhere else in the codebase.
- Every page's content is Markdown with front matter. No HTML in content files.
- Navigation is `_data/nav.yml`. Adding a nav item is editing one YAML line.
- Layouts do one job each and stay short; anything appearing twice becomes an include.
- Each non-obvious file opens with a comment saying what it is and what to change in it.
