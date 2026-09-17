---
title: write-pure-math-paper
tool: torsor-writing
slug: write-pure-math-paper
permalink: /tools/torsor-writing/write-pure-math-paper/
order: 10
summary: a skill to take theorem statements, proofs and notes, and write them into a finished mathematics paper.
howto_lead: >-
  new to this? open a folder holding your notes, theorem statements and proofs in Claude Code or Codex, and say:
howto_say: >-
  use the repository at https://github.com/torsor/claude-plugins and write a paper from the material in this folder
notes:
  - title: the audit is a truth gate
    text: >-
      unresolved mathematical issues stay visible and block any prose that would
      depend on them. a gap is flagged, never quietly filled.
  - title: proof status is preserved
    text: >-
      what is proved stays proved, what is conjectural stays conjectural, and the
      paper does not invent a repair to make a section read better.
---

a Claude Code skill. give it theorem statements, proofs, research notes,
computations, references, or an existing manuscript, and it writes them into a
finished paper or short note in pure mathematics.

it audits the mathematics before writing any prose. that audit produces a theorem
inventory, a dependency map, a record of hypotheses and notation, an attribution
ledger, and a list of open issues — and the issues gate the writing. then it fixes
a nine-sentence story and an architecture, choosing among the shapes a paper can
take: theorem and proof, construction or classification, counterexample, new
method, short note. then it authors in dependency-aware passes and runs integrity
and publication audits at the end.

the discipline that matters most: it preserves proof status and flags gaps rather
than inventing repairs.

## the shape

```
phase 0   scope the paper, freeze its sources   ->  brief + source inventory
phase A   audit the mathematics                 ->  paper-notes/*.md   (truth gate)
phase B   nine-sentence story and outline       ->  you approve the architecture
phase C   author in dependency-aware passes     ->  the paper, four formats
phase D   integrity and publication audits      ->  evidence report
```

## invoke

```
/write-pure-math-paper the splitting result, notes in ~/research/splitting/
```

## produces

a paper in the house format — LaTeX source with PDF, HTML, EPUB and Markdown —
with the audit notes kept alongside.
