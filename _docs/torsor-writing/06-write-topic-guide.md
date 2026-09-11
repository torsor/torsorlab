---
title: write-topic-guide
tool: torsor-writing
slug: write-topic-guide
permalink: /tools/torsor-writing/write-topic-guide/
order: 6
summary: one explanatory guide to one idea, synthesized across several sources.
notes:
  - title: scanned sources are read, not OCR'd
    text: >-
      when a source is image-only, the relevant chapters are located and then
      vision-read. no OCR step, and no pretending the text layer is there.
  - title: the gaps list is a gate
    text: >-
      if a step on the spine is covered by no source, that has to be filled — from
      background or by reading more — before any writing starts.
---

where [write-paper-guide](../write-paper-guide/) companions **one** paper
organized by that paper's sections, this produces a guide to **one idea across
many sources**, organized by a conceptual spine you decide. it is for when no
single source carries the exposition and something has to.

four things are particular to it. **sources are pre-summarized** — each one
distilled by a dedicated subagent, in its own context, into a structured digest
under `source-notes/`, and the guide is written from those notes rather than from
the raw PDFs. **scanned and image-only PDFs are handled** by locating the relevant
chapters and vision-reading them. **you decide a concept spine** up front, map
every source onto it, and get back an honest list of what no source covers.
and it is **oriented to learning**: calibrated to one named reader, developing
missing prerequisites from scratch, and leaving the `source-notes` behind as a
durable study artifact.

the framing rules carry over from the paper guide. third person about the sources
— the authors prove, section 3 establishes. and a guide, never a contribution and
never a survey of the field.

## the shape

```
phase A   pre-summarize the sources     ->  source-notes/*.md  (kept)
phase B   reader + concept spine        ->  reader-profile.md, the spine, the gaps list
phase C   author and build              ->  the guide, four formats
```

## invoke

```
/write-topic-guide how to think about descent, from these three sources: ...
```

## produces

a guide directory in the house format — LaTeX source with PDF, HTML, EPUB and
Markdown — with `source-notes/` kept alongside as a deliverable in its own right.
