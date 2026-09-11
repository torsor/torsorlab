---
title: write-body-of-work-summary
tool: torsor-writing
slug: write-body-of-work-summary
permalink: /tools/torsor-writing/write-body-of-work-summary/
order: 8
summary: a skill to take one mathematician's papers, and write an overview of their research program.
notes:
  - title: purpose sets the person
    text: >-
      who the summary is for changes the emphasis and also whether it is written in
      the first or third person. self-presentation is the one mode where "I" is the
      whole point.
  - title: no "why it is hard" sections
    text: >-
      it answers the same six framing questions a paper guide asks, but never names
      them and never sets them as headings.
---

a Claude Code skill. give it one mathematician's papers and it reads them all and
writes an overview of their research program: a two-to-three page essay on the
program, then a short paragraph on each paper.

where [write-paper-guide](../write-paper-guide/) companions one paper and
[write-topic-guide](../write-topic-guide/) explains one idea across sources, this
covers one person's work, organized by the themes running through it.

it borrows the pre-summarization phase intact: each paper is distilled by a
dedicated subagent, in its own context, into a digest under `source-notes/`, and
the summary is written from those notes. in place of a concept spine it gathers a
**themes map** — the threads running through the corpus, every paper mapped onto
them, and a decision about the throughline and how the paper paragraphs are
organized. the themes map gates the writing: no drafting until the threads and the
throughline are agreed.

it is a summary, not a contribution and not a survey of the field.

## invoke

```
/write-body-of-work-summary my research program, papers in ~/papers/
/write-body-of-work-summary summarize X's body of work for a tenure committee
```

## produces

a guide directory in the house format, with `source-notes/` and a themes-by-papers
table kept alongside.
