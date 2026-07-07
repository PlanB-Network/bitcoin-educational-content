# Translation knowledge base

One file per language (`<lang>.md`, e.g. `fr.md`, `zh-Hans.md`). Each file
accumulates **lessons learned** by translation agents: terminology choices,
recurring ambiguities, register decisions, and structural gotchas specific to that
language.

## How it is used
- Before translating, a worker injects `knowledge/<lang>.md` (if present) into its
  prompt, so it inherits every prior decision for that language.
- After translating, a worker may append 1–5 concise lessons to a per-worker
  scratch file. The orchestrator then **consolidates** those scratch notes into
  `knowledge/<lang>.md` (append-only, deduplicated), avoiding write races between
  parallel workers of the same language.

## Format of a lesson
Plain markdown bullets. Keep them short and reusable, e.g.:

```
- "hardware wallet" → «portefeuille matériel» (not «wallet matériel»).
- Keep "seed phrase" verbatim per glossary; do not translate to «phrase de graine».
- Course intros use vouvoiement; keep the formal register throughout.
```

`model-matrix.md` (produced by the model-evaluation research) lives here too and
drives the `models` routing in `config.yml`.
