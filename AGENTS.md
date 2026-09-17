# working on this site

pointers for anyone — human or agent — writing or editing torsorlab.

## voice

**lowercase prose.** sentences, headings, titles, nav labels, and front-matter
strings all start lowercase. proper nouns keep their capitals (Claude Code,
LaTeX, Rust, Danny Krashen), and so do acronyms (AI, PDF, EPUB, HTML). the
uppercase mono labels in the design — eyebrows, status chips, table headers, the
wordmark — are typography, not prose; leave those alone.

**we, not the lab.** the work is collaborative and the writing should say so.
"we are exploring", "we have been developing", "our work". avoid third-person
descriptions of torsorlab as an entity that acts on its own ("the lab builds…",
"torsorlab is the name under which…").

**"credit" appears at most once on the whole site.** it is a heavy word and it
frames the work as a ledger. the one use lives on the about page. everywhere
else, say what we are doing and who is doing it, and let attribution follow from
that. "collaboration", "together", "with" do most of the work.

**never advertise judgements about anyone's work.** the review skills find
*potential issues*; they do not find what is wrong with a paper. write "catalog
the potential issues", not "write up everything questionable"; "suggested
changes", not "the repairs"; "potential issues", not "problems" or "defects" or
"errors". the skills themselves are careful about this — the critical guide
reaches no verdict and the repair stage proposes rather than applies — and the
site must not claim more than they do.

the exception is prose that argues *for* restraint: "a defect reported that is
not there costs the authors weeks" and "a preference is never reported as an
error" both describe what the skill refuses to do, and softening them would
weaken the point. the test is whether the sentence asserts something about a
paper, or describes the care taken before asserting anything.

**say what a thing is, not what it is not.** prefer the concrete. a tool
description should tell a reader what they can do with it.

**no hype.** no "powerful", "seamless", "revolutionary". the tools are useful;
that is the claim.

**assume the reader has never opened Claude Code.** every tool and every skill
carries `howto_lead` and `howto_say` in its front matter: what folder to open,
then the literal sentence to type at the agent. write the `say` line as
something a person can paste without editing, and use `<angle brackets>` only
where they genuinely have to substitute their own topic.

**the `say` line must name the skill it means.** an agent pointed at the
repository picks from eleven skills by matching what you asked for against their
descriptions, so the phrase has to contain the skill's own name: "write a review
and repair guide", not "review the paper and mark up the changes"; "write a pure
math paper", not "write a paper". the generic version reads better and selects
the wrong skill.

## the rest

`README.md` has the structure: where to edit what, the collection front matter,
and how the design is put together. it is the single copy — don't restate it
here, and update it there when it changes.

two things worth knowing before you write:

- run `make check` before committing. it asserts the collections are wired
  correctly.
- three doc pages are manual-backed and verbose; the other eight are drawn from
  the plugin's `SKILL.md` files and are shorter on purpose. when a fourth manual
  is written, add it to `MANUALS` in `bin/sync-manuals.py` and set
  `manual: true` on its doc page.
- the manuals are books written in the house voice, which is *not* this site's
  voice. do not lowercase them or edit them here — they are copied in from
  `guides/`, and an edit made here is lost on the next `make manuals`.
- the older note still holds for anything not yet covered: doc pages are
  deliberately minimal right now. the fuller shape (what it
  writes / who for / prerequisites / a worked invocation / marginalia) is
  supported by the layout whenever the prose arrives — you do not need to
  restructure anything to grow one.
