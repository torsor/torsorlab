---
title: write-paper-guide
tool: torsor-writing
slug: write-paper-guide
permalink: /tools/torsor-writing/write-paper-guide/
order: 2
manual: true
summary: a skill to take one mathematical paper, and write a reading guide to it for a particular reader.
notes:
  - title: calibration is the whole trick
    text: >-
      a guide written for a generic reader develops the prerequisite that reader
      happens not to need, and skips the one actually blocking them. the interview
      costs five minutes and is repaid on the first page.
  - title: describe familiarity, not ability
    text: >-
      "comfortable with derived categories, hasn't had reason to use perverse
      sheaves" is a calibration. "expert" and "beginner" are grades, and a grade
      tells the guide nothing it can act on.
  - title: third person, always
    text: >-
      the authors prove; section 3 establishes; theorem 4.2 states. a guide is not
      a contribution, and every sentence in it should be checkable against the
      paper.
---

a Claude Code skill. point it at one mathematical paper and it reads the paper and
writes a book-length reading guide to it, calibrated to one particular reader.

here is why the calibration matters. there is a paper you need to understand, and
reading it again is not working.
maybe the part you need is section 6, which rests on section 4, which assumes a
construction the authors call standard. maybe you are refereeing it in three
weeks. the paper is not the problem — the problem is the distance between what it
assumes and what you have, and that distance is specific to you. this is why "go
read the survey first" so often fails: a survey is written for nobody in
particular, and you are somebody in particular.

## two parts, one reader

**part I orients.** it answers six questions about the paper: what it is about,
why it is interesting, why it is plausible, why it is hard, why it is new, and
why the authors pulled it off. the grouping bends to fit the paper; what does not
bend is that all six get answered. the failure mode here is generic admiration,
and it writes itself — "a significant contribution to a central problem" answers
none of the six.

**part II walks the paper**, following its own sections and its own numbering. a
roadmap chapter first, then one chapter per major section, each saying what that
part accomplishes, restating the results that matter, explaining which lemma is
the engine and which are bookkeeping, and naming where the difficulty actually
lives. restated results carry the paper's own numbers, so you can check the guide
against the paper in ten seconds.

then an appendix collecting the paper's notation and mapping the guide's chapters
to the paper's sections — the part you search rather than read.

a guide is not a survey, not original work, and not a summary. a summary gets
shorter; a guide gets longer, because the compressed passages are exactly the
ones worth expanding.

## running it

point it at the paper, however you can identify it:

```
/write-paper-guide ~/papers/descent.pdf
/write-paper-guide arXiv:0000.00000
/write-paper-guide the paper on heights of special points that everyone cites
```

given only a citation it finds the paper and confirms it has the right one before
investing in a full read. then it reads the paper properly — not the abstract —
and will not start writing until it can state in one paragraph what the paper
proves and how. if that paragraph looks wrong, say so at once rather than waiting
to see whether it recovers. it will not.

next it asks about the reader, as a short batch of questions. two of the answers
do most of the work: **why they are reading** sets what counts as the point, and
**what they already know** decides how much of part I is setup. you can skip the
interview by pointing at notes or a profile file instead.

then it proposes a location, then an outline. the outline is the cheapest moment
in the whole process to change your mind about scope — merging two chapters there
costs a sentence; merging them after they are written costs a rewrite.

part I is written first and shown to you in full before part II begins, because
part II inherits its framing and depth. part II then arrives a chapter at a time.
the dial worth watching across those checkpoints is proof depth: say "more detail
on the proofs" or "less" and it carries forward.

### without checkpoints

pre-answer everything it would stop to ask, in one argument string — the paper,
the reader, the purpose, the depth, the length, the location:

```
/write-paper-guide The paper is at ~/papers/descent.pdf. Do not ask me
anything -- take every default and proceed. The reader is an active
researcher in an adjacent field: comfortable with the general area and its
standard machinery, but not a specialist in this corner. They are reading
in order to referee it, so go to proof depth and skip nothing. Length:
exhaustive, no budget. Location: ~/papers/descent/guide/.
```

an unattended run gives up the checkpoints, and the checkpoints are where depth
gets corrected. if the depth comes out wrong the fix is another full run, not an
edit.

## what comes back

a guide directory that is a self-contained book — you can move it, hand it to
someone, or rebuild it on a machine that has never had the plugin installed. the
tools are copied in rather than linked, so it survives a plugin update.

```
guide/
  Makefile
  check-build.py       verification, copied in
  tex2torsor/          converter, copied in
  latex/
    main.tex
    STYLE.md           the style guide in force
    reader-profile.md  the calibration
    chapters/
  html/  epub/  markdown/
```

`make pdf`, `make html`, `make epub`, `make md`, `make check`. the PDF is the
format the design is tuned for and the one to trust; the rest are conveniences.

### two things that will bite you

`latexd` exits 0 even when LaTeX has failed, so `make pdf && echo ok` can lie.
`make check` is what catches it — it verifies the PDF exists, is newer than every
source file, has a sane page count, and that the log carries no errors. a
one-page PDF where you expected forty is the usual shape of the failure.

but `latexd` compiles in a temporary directory and keeps no log, so after a
`latexd` build `make check` has nothing to read and fails on that alone. build
once with `latexmk -pdf -cd latex/main.tex`, which leaves the log where the
checker looks.

### when the math does not survive

the PDF renders everything. HTML and EPUB are weaker and they fail quietly. the
converter cannot handle over-accents, `\frac`, extensible arrows, or `array` and
`aligned` — which means commutative diagrams. add `--mathml` to the epub target;
add MathJax as a post-step to the html target; or write a renderable equivalent
in the source and note the paper's own glyph once in prose and once in the
appendix.

## editing it afterwards

it is LaTeX — edit the chapters and rebuild. leave the palette, fonts, and box
definitions alone, since those are what make the family look like a family, and
re-run `make check` afterwards. for more than an edit, hand the guide back to the
skill and say what should be different; it reads what is there and works
alongside it rather than starting over.
