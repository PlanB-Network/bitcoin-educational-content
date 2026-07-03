# agent-translate — agent-driven translation pipeline

Replaces the legacy `scripts/auto-translate/` machine-translation stack (per-string
DeepL/Google/OpenAI + a 1,088-LOC MD/YAML↔JSON parser + a 902-token glossary hack)
with a single headless agent (`omp -p`) that translates whole files in place.

## Why
Generic MT engines can't see markdown structure and translate technical terms, so
the old pipeline built a huge scaffold to isolate text, shield 902 terms behind
`GW-<n>` tokens, and un-transliterate them per script. An LLM agent translates the
file directly: it preserves code/links/YAML, honours a glossary in context, and has
whole-document context (better cohesion than per-string MT). We keep the cheap,
correct parts (gap detection, validation, human proofreading) and delete the
plumbing.

## Pipeline
```
gap-check (deterministic)  ->  dedicated worktree + branch  ->  bounded omp worker pool (default 8)
      find_missing.py                translate.py                 worker.py (1 omp -p / file×lang)
                                                                        |
   knowledge/<lang>.md  --inject-->  worker  --lessons-->  consolidate --> knowledge/<lang>.md
                                                                        |
                                            verify.py (structural parity)  -> retry FAILs once
                                                                        |
                                       release agent (omp -p): validate, commit, push, ONE PR
                                                                     prompts/pr_agent.md
```
One batch = one PR.

## Files
| File | Role |
|------|------|
| `config.yml` | languages, content roots, exclusions, concurrency, **model routing** |
| `find_missing.py` | deterministic gap-check → work list (`(source, lang)` pairs) |
| `worker.py` | one `omp -p` translation per file×lang; course chapter-chunking |
| `verify.py` | structural parity + verbatim-id + glossary guard (the safety net) |
| `translate.py` | orchestrator: gap-check → worktree → pool → verify → retry → PR |
| `prompts/translate.md` | translation system rules (format contract, glossary, tone) |
| `prompts/pr_agent.md` | release-agent rules (validate, commit, push, PR) |
| `glossary.yml` | 902 verbatim terms (ported from legacy), injected per-file |
| `knowledge/<lang>.md` | per-language lessons, injected into workers and grown each batch |
| `knowledge/model-matrix.md` | model-selection research (drives `config.yml` routing) |

## Usage
```bash
# What is missing? (deterministic, no LLM, no network)
python3 find_missing.py                              # all gaps, summary
python3 find_missing.py --langs fr,de --content courses --json

# Translate (creates a worktree + branch, runs the pool, verifies, opens a PR)
python3 translate.py --langs fr --content courses --limit 20
python3 translate.py --langs zh-Hans --subtype quizz --concurrency 8

# Preview only
python3 translate.py --dry-run --langs fr

# Local, no worktree, no PR (dev / smoke test)
python3 translate.py --in-place --no-pr --langs fr --subtype quizz --limit 2
```

Key flags: `--langs`, `--content` (courses/tutorials/resources/professors/events),
`--subtype` (course/quizz/tutorial/resource/professor/event), `--limit`,
`--concurrency N` (default 8), `--model X` (force one model), `--retries N`,
`--base dev`, `--in-place`, `--no-pr`, `--keep-worktree`, `--max-items` / `--force`.

## Model routing
`config.yml → models`. `--model` overrides everything; per-language `overrides` beat
`default`. Patterns use omp fuzzy match — **the model must be authenticated in omp**.

- **Shipped default: `sonnet`** — the only model currently authenticated here, and the
  research matrix's safety anchor (best tool-use, best prompt-injection resistance).
- **Evidence-based target routing** lives under `models.recommended` (see
  `knowledge/model-matrix.md`): `gpt-5.1` workhorse, `gemini-3-pro` for
  low-resource/Asian/Nordic-Finnic, `glm-4.6` for Chinese. To adopt it, authenticate
  those providers in omp, then move `recommended` into `default`/`overrides`.
- **rn (Kirundi)** is unsupported by every candidate agent model — route to
  `gemini-3-pro` **and mandate human review** (or NLLB-200 pre-translate → post-edit).

## The safety net (`verify.py`)
Deterministic, does not trust the model:
- **FAIL** (excluded from the PR): missing/empty output, invalid YAML, heading or
  code-fence count mismatch, YAML key-structure mismatch, changed verbatim identifier
  (`partId`, `video_id`, `url`, …).
- **WARN** (kept, flagged for human spot-check): link/image count drift, dropped
  glossary term, high identical-line ratio (possible untranslated content).
FAILs are retried once on a fresh session; persistent FAILs are dropped by the
release agent and listed in the PR body.

## Status
- Proven end-to-end: gap-check → worker (omp) → verify → pool → retry → lessons
  consolidation, on real quizz content (FR), structural verify PASS.
- The release agent (`run_pr_agent` / `pr_agent.md`) is implemented and wired but has
  **not** been fired against a live PR (to avoid an unsolicited PR to the repo). Run a
  scoped pilot with a real `translate.py` invocation to exercise it.

## Not included on purpose
No provider SDKs, no MD/YAML↔JSON parser, no glossary tokenisation, no
transliteration regex. Those were the legacy scaffold and are intentionally gone.
