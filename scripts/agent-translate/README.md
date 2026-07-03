# agent-translate — agent-driven translation pipeline

Replaces the legacy `scripts/auto-translate/` machine-translation stack (per-string
DeepL/Google/OpenAI + a 1,088-LOC MD/YAML↔JSON parser + a 902-token glossary hack)
with a single headless agent (`omp -p`) that translates whole files in place.

## Why
Generic MT engines can't see markdown structure and translate technical terms, so
the old pipeline built a huge scaffold to isolate text and shield terms. An LLM agent
translates the file directly: it preserves code/links/YAML, resolves terminology
against the repo's own glossary, and has whole-document context. We keep the cheap,
correct parts (gap detection, validation, human proofreading) and delete the plumbing.

## Pipeline
```
gap-check (deterministic)  ->  dedicated worktree + branch  ->  bounded omp job pool (default 8)
      find_missing.py                translate.py               worker.py (1 omp -p per JOB)
                                                                        |
   a JOB = N files, ONE language:  long-form md = 1 file/job · small YAML batched (≈15/job)
                                                                        |
   knowledge/<lang>.md  --inject-->  worker  --lessons-->  consolidate --> knowledge/<lang>.md
                                                                        |
                                            verify.py (structural parity)  -> retry walks fallback models
                                                                        |
                                       release agent (omp -p): validate, commit, push, ONE PR
```
One batch = one PR. Knowledge updates ride in the same PR.

## Files
| File | Role |
|------|------|
| `config.yml` | languages, content roots, exclusions, concurrency, **batch_size**, **model routing** |
| `find_missing.py` | deterministic gap-check → work list; scope by `--langs`/`--content`/`--subtype`/`--path` |
| `worker.py` | one `omp -p` per JOB (1 long file, or a per-language batch of small files) |
| `verify.py` | structural parity + verbatim-id guard (FAIL/WARN); the safety net |
| `translate.py` | orchestrator: gap-check → worktree → job pool → verify → retry → PR |
| `prompts/translate.md` | translation rules (format contract, terminology policy, tone) |
| `prompts/pr_agent.md` | release-agent rules (validate, commit, push, PR) |
| `knowledge/<lang>.md` | per-language lessons; injected into workers, grown each batch, committed in the PR |
| `knowledge/model-matrix.html` | asi0's model-selection decision (drives `config.yml` routing) |

No provider SDKs, no MD/YAML↔JSON parser, no static glossary tokenisation — those were
the legacy scaffold and are intentionally gone.

## Usage
```bash
# What is missing? (deterministic, no LLM, no network)
python3 find_missing.py                                   # all gaps
python3 find_missing.py --langs fr,de --content courses
python3 find_missing.py --subtype quizz --json
python3 find_missing.py --path courses/btc101             # scope to one content subtree
python3 find_missing.py --path courses/btc101/en.md       # or one specific source file

# Translate (creates a worktree + branch, runs the pool, verifies, opens a PR)
python3 translate.py --path courses/scr403 --langs fr
python3 translate.py --langs zh-Hans --subtype quizz --concurrency 8 --batch-size 15

# Preview only (shows per-language model · thinking)
python3 translate.py --dry-run --path courses/scr403 --langs fr,ja,et

# Local, no worktree, no PR (dev / smoke test)
python3 translate.py --in-place --no-pr --langs fr --subtype quizz --limit 4 --batch-size 4
```

Scoping flags combine freely: `--langs`, `--content`, `--subtype`
(course/quizz/tutorial/resource/professor/event), `--path` (subtree or one
`en.md`/`en.yml`), `--limit`. Run flags: `--concurrency N` (default 8),
`--batch-size N` (small-file packet, default 15), `--model X` + `--thinking`,
`--retries N` (default 2, walks the fallback chain), `--base dev`, `--in-place`,
`--no-pr`, `--keep-worktree`, `--max-items`/`--force`.

## Model routing (`config.yml → models`)
asi0's decision, from `knowledge/model-matrix.html`. Each language maps to an ordered
chain `[#1, #2, #3]` of `{model, thinking}`; the retry pass walks DOWN the chain, so a
FAIL is retried on the next-ranked model. `--model` overrides the whole chain.

- `sonnet` (Claude Sonnet 5) — European naturalness, value; **present in every chain**,
  so if `opus`/`gpt-5.5` are unauthenticated the chain still lands on a working model.
- `opus` (Claude Opus 4.8) — self-verification, terminology consistency, hardest targets.
- `gpt-5.5` — raw CJK / Indic / RTL accuracy.
- thinking: `medium` (easy langs) → `high` (register/morphology) → `xhigh` (low-resource).
- **rn (Kirundi)**: routed to `opus/xhigh` but MUST get human review (no model is reliable alone).

Model patterns use omp fuzzy match and MUST be authenticated in omp.

## Terminology (no static glossary)
The agent resolves terms against the repo's own glossary: `resources/glossary/<slug>/<lang>.md`
(frontmatter `term:` = canonical rendering). On doubt it greps the glossary, checks other
same-language files, or web-searches the conventional usage — see `prompts/translate.md`.

## The safety net (`verify.py`)
Deterministic, does not trust the model:
- **FAIL** (excluded from PR): missing/empty output, invalid YAML, heading or code-fence
  count mismatch, YAML key-structure mismatch, changed verbatim identifier
  (`partId`, `video_id`, `url`, …).
- **WARN** (kept, flagged): link/image count drift, high identical-line ratio.
FAILs are retried (walking the fallback chain); persistent FAILs are dropped by the
release agent and listed in the PR body.

## Status
- Proven end-to-end (in-place): gap-check → batched worker (omp) → verify → retry →
  lessons consolidation. Real FR quizz batch: 4 files / 1 session, verify all PASS,
  knowledge/fr.md grown.
- The release agent (`run_pr_agent` / `pr_agent.md`) is implemented and wired but not yet
  fired against a live PR.
- **Prerequisite for content batches:** this pipeline must be on `dev` first, so content
  PRs contain only translations (+ knowledge), not the tooling diff.
