# Learning record format

Learning records live in `./learning-records/` and use sequential numbering:
`0001-slug.md`, `0002-slug.md`, … Create the directory lazily — only when the
first record is written.

They are the teaching equivalent of ADRs: they capture non-obvious lessons, key
insights, and stated prior knowledge that steer future sessions and locate the
learner's zone of proximal development (and their current **door** level).

## Template

```md
# {Short title of what was learned or established}

{1-3 sentences: what was learned (or what prior knowledge was established), and
why it matters for what to teach next.}
```

That is the whole format. A record can be a single paragraph. The value is in
recording *that* this is now known and *why* it changes the next lesson — not in
filling sections.

## Optional sections

Include only when they add genuine value:

- **Status** (`active | superseded by LR-NNNN`) — when an earlier understanding
  is replaced.
- **Evidence** — how the learner demonstrated it (quiz answered, channel opened
  on signet, node synced, prior experience cited).
- **Implications** — what this unlocks or rules out, including a change to the
  recommended Plan ₿ Academy door.

## When to write one

1. **Demonstrated genuine understanding** of something non-trivial — evidence,
   not mere exposure. Sets a new floor for what to teach next.
2. **Disclosed prior knowledge** — "I already run a node." Record it (and the
   depth claimed) so sessions don't re-teach it.
3. **A misconception was corrected** — high value; predicts future stumbling
   blocks. (e.g. "thought the seed phrase *is* the wallet".)
4. **The mission or door shifted** in response to learning — cross-link
   `MISSION.md` and update it.

### What does *not* qualify

- Material merely covered. Coverage is not learning — wait for evidence.
- Term definitions already in the glossary reference. Don't duplicate.
- Session-by-session activity logs. Records are decision-grade insights, not a
  journal.

## Numbering & supersession

- Scan `./learning-records/` for the highest number and increment by one.
- When a later record contradicts an earlier one, mark the old one
  `Status: superseded by LR-NNNN` rather than deleting it — the evolution of
  understanding is itself signal.
