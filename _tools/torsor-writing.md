---
title: torsor-writing
slug: torsor-writing
tagline: Eleven LaTeX writing skills for Claude Code, packaged to run on any machine.
status: released
repo: https://github.com/torsor/claude-plugins
order: 1
---

A Claude Code plugin. Each skill writes a document in the torsor house format —
LaTeX source, with PDF, HTML, EPUB, and Markdown output — in the torsor design
and prose style.

The skills used to read the prose library, reference templates, a style preamble,
and `tex2torsor` by absolute path on one machine. Here those are vendored into the
plugin and referenced through `${CLAUDE_PLUGIN_ROOT}`, so nothing is tied to a
particular box.

## Install

```sh
claude plugin marketplace add https://github.com/torsor/claude-plugins
claude plugin install torsor-writing@torsor-plugins
claude plugin list
```

All eleven `/write-…` skills are then available on that machine.

## Build prerequisites

The skills author and reference everything themselves, but *building* a document
needs these on the box that runs `make`:

- a TeX install (with `amsmath`, `amsthm`, `mathtools` for guides)
- `pandoc`, for EPUB and for HTML via `tex2torsor`
- `latexd` and `lab-view`, the torsor lab build and preview tools — install
  separately, or build PDF and HTML by hand

`tex2torsor` is bundled with the plugin, so it is not a separate prerequisite.
