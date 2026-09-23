---
title: write-correspondence-guide
tool: torsor-writing
slug: write-correspondence-guide
permalink: /tools/torsor-writing/write-correspondence-guide/
order: 6
draft: true
summary: a skill to take one mathematical paper, and write a correspondence guide placing it in the literature around it.
howto_lead: >-
  new to this? open a folder holding the paper's LaTeX source or PDF in Claude Code or Codex, and say:
howto_say: >-
  use the repository at https://github.com/torsor/claude-plugins and write a correspondence guide for the paper in this folder
notes:
  - title: correspondence, never provenance
    text: >-
      an entry says what was observed between two written statements. it never
      says the paper's argument drew on its antecedent — that is not knowable
      from the artifact.
  - title: not written for someone to sign
    text: >-
      a referee is a valid reader, but the guide is not designed for one, and
      nothing in it is written to be signed.
  - title: missing a connection is the expensive error
    text: >-
      a false positive costs twenty minutes reading a paper that turns out to be
      different. a false negative means someone tells you in six months, or
      nobody does. so it defaults to reporting.
---

a Claude Code skill. point it at one mathematical paper and it maps the paper
into the literature around it: for each thing the paper asserts or constructs,
what the corresponding object in the existing literature is, how close the
correspondence runs, and where it stops.

it sits beside [write-paper-guide](../write-paper-guide/) and shares its shape.
the difference is the vantage. a reading guide explains the paper from inside;
this one places it from outside.

## who it is for

the author of a complete draft, running a final check. a reader working through
the paper. a reader curious about it from the arXiv, who wants context and may
never read it closely. someone placing a paper published years ago.

a referee is a valid reader — a particular kind, with a particular job — but is
not what this is designed for, and **nothing it produces is written for someone
to sign.**

## what it will not say

it states correspondences. it never says what the paper drew on, and never says
what it should cite. the words *should cite*, *fails to cite*, *uncredited* and
*omits* do not appear, and neither do *derives from*, *taken from* or
*influenced by*. whether a bibliography is adequate is a judgement for the
paper's readers; this is material for that judgement.

it also does not adjudicate. three disjoint entry points into the same object
is a better result than consensus on one — the object surfaces in three
literatures and a reader takes whichever they can read.

## the two gates

most of what it finds stays in the notes, and that is the design.

**standing** asks whether a record is a placement at all, or textbook
background, or an internal cross-reference. only placements reach a page.

**consequence** is the harder one: does this change what a reader of the paper
would do or know? a record can be correctly located, read in full, be exactly
the right source, and change nothing — a flawless identification of a tool the
authors invoked by name is worth nothing to the people who invoked it. roughly
one record in ten that passes standing passes consequence.

every admitted record names what changes. one that cannot is out, however good
the identification.

consequences are written as what is the case, not as an instruction — "the
restriction to $\mathbb{Q}$ in §1 is not needed: B. Author gives the same rank
computation over any field in which $n$ is invertible", rather than "drop the
restriction". the declarative form serves the author who can still edit and the
reader who cannot, and it is the same sentence.

## what comes back

annotated copies of the paper's own source, one per literature, with the notes
set at the passages they concern. generated reference views — the entries, the
unlocated, the leads. and optionally a written guide in two parts: the
neighbourhoods the paper turns out to sit in, then a thread through the paper
with the connections at each point.

everything generated comes from one ledger, `correspondences.yaml`, so the prose
cannot drift from what was found.

## it is slow, on purpose

`write-critical-guide` runs about two hours; this runs longer. it is meant to be
invoked once, on a complete draft, after months or years of writing. the
expensive part is not finding a candidate — it is establishing what the
candidate actually says, on both ends of a connection, well enough to argue it.

it runs unattended. every decision has a default, and the only thing that halts
a run is being unable to identify the paper.
