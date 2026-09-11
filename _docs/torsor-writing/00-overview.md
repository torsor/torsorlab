---
title: overview
tool: torsor-writing
slug: overview
permalink: /tools/torsor-writing/overview/
order: 0
summary: what the eleven skills are, how they differ, and which one to reach for.
notes:
  - title: one format
    text: >-
      every skill produces the same house format — LaTeX source with PDF, HTML,
      EPUB, and Markdown built from it, in a directory that rebuilds on a machine
      that has never had the plugin installed.
  - title: three have full manuals
    text: >-
      paper-guide, critical-guide, and review-and-repair each have a complete
      user's manual, linked from their pages. the rest are covered here at
      working depth.
  - title: unattended
    text: >-
      the critical guide, the repairs, and the review-and-repair pipeline run to
      completion without asking anything. the others stop at checkpoints unless
      you pre-answer.
---

eleven skills. the useful distinction between them is not what they are about but
**what they are pointed at** — one paper, several sources, a corpus, a person, a
room, or nothing yet written.

## about one paper

[`write-paper-guide`](../write-paper-guide/) explains it, to one named reader.
[`write-critical-guide`](../write-critical-guide/) assesses it, and reaches no
verdict. [`write-paper-repairs`](../write-paper-repairs/) works out what would fix
what the assessment found. [`write-review-and-repair`](../write-review-and-repair/)
runs the last two end to end.

the first two are siblings, and the difference is the test for any sentence: if it
explains the paper to someone who wants to understand it, that is the reading
guide; if it weighs the paper for someone who has to judge it, that is the
critical guide.

## across several sources

[`write-topic-guide`](../write-topic-guide/) synthesizes them into one exposition —
for when no single source carries it. [`write-study-guide`](../write-study-guide/)
routes a reader through a corpus that already has the exposition, so its work is
selection and triage rather than explanation.
[`write-body-of-work-summary`](../write-body-of-work-summary/) covers one
mathematician's program across their papers.

all three pre-summarize their sources into notes first, and write from the notes.
the notes are kept as a deliverable.

## original writing

[`write-pure-math-paper`](../write-pure-math-paper/) and
[`write-technical-report`](../write-technical-report/). both audit their material
before writing a word, and in both the audit is a gate: nothing gets claimed that
the inventory or the evidence ledger cannot support.

## a project, or a room

[`write-manual`](../write-manual/) documents a project.
[`write-workshop-state-guide`](../write-workshop-state-guide/) reports where live
work stands, dated and commit-stamped, on the room's own confidence ledger.

## what they share

third person about the work, always. a guide is not a contribution, and a summary
is not a survey. each output is a self-contained directory carrying its own
`Makefile`, its own copy of the converter, and a `STYLE.md` recording the voice it
was written in — so it survives a plugin update and rebuilds anywhere.
