---
title: torsor-writing
slug: torsor-writing
tagline: eleven writing skills for Claude Code to create reading guides, critical reviews, repairs, papers and reports, from your source material, each built as a self-contained manuscript.
status: released
repo: https://github.com/torsor/claude-plugins
howto_lead: >-
  new to this? open a folder holding your manuscript's LaTeX source in Claude Code or Codex, and say:
howto_say: >-
  use the repository at https://github.com/torsor/claude-plugins and write a critical guide for the paper in this folder
order: 1
docs_eyebrow: the skills
docs_heading: what each one does
---

## getting it

a Claude Code plugin. each skill writes a document in the torsor house format —
LaTeX source, with PDF, HTML, EPUB, and Markdown output — in the torsor design
and prose style.

### install

```sh
claude plugin marketplace add https://github.com/torsor/claude-plugins
claude plugin install torsor-writing@torsor-plugins
claude plugin list
```

all eleven `/write-…` skills are then available on that machine.

the skills used to read the prose library, reference templates, a style preamble,
and `tex2torsor` by absolute path on one machine. here those are vendored into the
plugin and referenced through `${CLAUDE_PLUGIN_ROOT}`, so nothing is tied to a
particular box.

### build prerequisites

the skills author and reference everything themselves, but *building* a document
needs these on the box that runs `make`:

- a TeX install (with `amsmath`, `amsthm`, `mathtools` for guides)
- `pandoc`, for EPUB and for HTML via `tex2torsor`
- `latexd` and `lab-view`, the torsor lab build and preview tools — install
  separately, or build PDF and HTML by hand

`tex2torsor` is bundled with the plugin, so it is not a separate prerequisite.
