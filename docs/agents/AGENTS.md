# AGENTS.md — Agent guide for the Plan ₿ Academy content repo

> **Canonical, tracked, tool-agnostic agent config lives in this folder
> (`docs/agents/`).** `AGENTS.md` is the source of truth; `CLAUDE.md` is a
> symlink to it. The root `AGENTS.md`/`CLAUDE.md` and `.claude/skills/teach` are
> gitignored *pointers* created by [`install.sh`](./install.sh) — edit the files
> here, never the pointers.

This repository is **content, not an application**. It is the public source of
truth for [Plan ₿ Academy](https://planb.academy): courses, tutorials,
resources, professors and events, each formatted so the website/apps can parse
and render them. There is no build to run and no app to start — your job as an
agent is to add or modify **well-formed content** and keep it valid.

## Golden rules

- **Match the existing format exactly.** Every content type has a strict shape
  (see below and `docs/`). A second convention next to an existing one is a bug.
- **Never translate YAML frontmatter / metadata.** Keys *and* their values
  (`name`, `goal`, `objectives`, tags, …) stay in English across every language
  file. Only prose body text is translated.
- **Never invent IDs.** UUIDs, Plan ₿-UIDs and BIP-39 chapter IDs are load-
  bearing keys in the platform database. Generate them correctly; never reuse or
  fabricate one.
- **Images are `.webp`.** No `.png`/`.jpg` in content folders.
- **Branch from `dev`.** PRs target `PlanB-Network/...:dev`. Use descriptive
  branch names (e.g. `tuto-sparrow-wallet-loic`).
- **No agent attribution** in commits or PRs (no "Generated with …" footers).
- **Ask before destructive actions** (deleting content, mass renames, history
  rewrites).

## Repository structure

```
bitcoin-educational-content/
├── courses/          # structured multi-chapter courses (see Courses)
├── tutorials/        # how-to articles, grouped by category
├── resources/        # books, podcasts, papers, conferences, glossary, …
├── professors/       # author profiles (professor.yml + <lang>.yml)
├── events/           # Bitcoin events
├── docs/             # repo + content-format documentation (start here)
│   └── agents/       # ← tracked, tool-agnostic agent config (this folder)
│       ├── AGENTS.md #    the guide — CLAUDE.md is a symlink to it
│       ├── skills/   #    published skills (teach, …)
│       └── install.sh#    wires pointers into .claude/ and repo root
├── scripts/          # validators & automation (Python + Node)
└── .claude/          # tool-specific, gitignored: symlinks into docs/agents/
```

Full human docs live in [`docs/README.md`](../README.md). Read it before any
non-trivial content change.

## Content model

### Courses — `courses/<id>/`

- **`<id>`** = 3-letter discipline + 3-digit level. Levels follow the university
  convention: `101–199` beginner, `201–299` intermediate, `301–399` advanced,
  `401–499` developer/expert. Disciplines and rules:
  [`course_ID_rules.md`](../course_ID_rules.md). Full spec:
  [`course_documentation.md`](../course_documentation.md).
- **`course.yml`** — metadata: `level`, `hours`, `professors:`, `contributors:`.
- **`<lang>.md`** — one per language. Three parts:
  1. **Header** (`---` … `---`): `name`, `goal`, `objectives:` — **English only**.
  2. **Description**: an `#` title + short intro paragraph, then `+++`.
  3. **Content**: `#` part → `##` chapter → `###`/`####` sub-sections.
     Each chapter carries a unique ID: `<chapterId>three-bip39-words</chapterId>`
     (three words from the BIP-39 wordlist — stable across reorders).
- **`assets/`** — `.webp` images. `no-txt/` for text-free images; one folder per
  language code (`en/`, `es/`, …) for images with overlaid text, mirrored
  structure across languages. A `thumbnail.webp` is required.

### Tutorials — `tutorials/<category>/<name>/`

- Folder name = URL slug: lowercase, dashes only, no spaces/special chars.
- **`tutorial.yml`** — `id`, `builder`, `tags`, `category`, `level`,
  `credits.professor`, plus proofreading metadata (`original_language`,
  `proofreading:`). See [`tutorial-creation-guidelines.md`](../tutorial-creation-guidelines.md)
  and [`tutorial-categories.md`](../tutorial-categories.md).
- **`<lang>.md`** — content per language.
- **`assets/`** — `logo.webp` (square), `cover.webp`, plus a per-language folder
  of visuals.

### Resources — `resources/<type>/<name>/`

Types: `books`, `podcasts`, `papers`, `newsletters`, `movies`, `glossary`,
`conferences`, `channels`, `bet`, `projects`, `calendar`. Each has its own
template in [`docs/PBN-template-repo/`](../PBN-template-repo/).

### Professors — `professors/<name>/`

- **`professor.yml`** — `id` (UUID v4), `name`, `links:`, `tags:`. No
  `contributor_id` unless assigned manually.
- **`<lang>.yml`** — `bio` (3–5 sentences) and `short_bio` (≤100 chars).
- **`assets/`** — profile image(s).
- Referenced in content via `<professor>contributor-id</professor>`; identity is
  the [Plan ₿-UID](../planb-uid.md).

## Identifiers cheat-sheet

| Thing                | Format                          | How to generate            |
| -------------------- | ------------------------------- | -------------------------- |
| Content / professor  | UUID v4                         | `uuidgen`                  |
| Chapter ID           | 3 BIP-39 words, dash-joined     | `docs/how-to-generate-a-bip39-id.md` |
| Professor/contributor| Plan ₿-UID                      | `docs/planb-uid.md`        |
| Course ID            | `DDD` + `###` (e.g. `btc101`)   | `docs/course_ID_rules.md`  |

## Validation & formatting

- **Formatting:** `pnpm lint` runs Prettier across the repo. A **Husky
  pre-commit** hook runs `pnpm lint-staged` (Prettier on staged files). Bypass
  only when justified with `SKIP_PRE_COMMIT=1 git commit …`.
- **Content validation:** Python validators under `scripts/` —
  `scripts/validate.py`, `scripts/validate_all.py`, and `scripts/validation-format/`.
  Run the relevant validator after editing content and before committing.
- Toolchain: **pnpm** for the Node side; the Python scripts use their own venv
  (`uv`/`pip` per script).

## Agent tooling & skills

Agent config is **published in the repo** so anyone learning or contributing via
this repo gets the same setup, regardless of agent.

- **`docs/agents/`** — canonical, tracked source: this guide + `skills/`.
- **`docs/agents/skills/`** — published skills. First one: **`teach`** — a
  stateful Bitcoin teaching skill that generates interactive HTML lessons and
  routes the learner through the "right door" of the Plan ₿ Academy catalog
  (course / tutorial / resource) for their level and goal. See
  [`skills/teach/SKILL.md`](./skills/teach/SKILL.md).
- **`.claude/`** (gitignored, tool-specific) — Claude Code's `commands/` and
  `skills/`. `skills/teach` is a symlink to `docs/agents/skills/teach`. Other
  repo-local Claude skills: `create-professor-profile`, `export_thumbnail`,
  `fix_sync_errors`, `generate_annual_report`, `generate_monthly_report`,
  `update_app`.

### Setup (one command)

After cloning, wire the tool pointers (idempotent, safe to re-run):

```sh
sh docs/agents/install.sh
```

Then, in Claude Code: `/teach` (e.g. *"teach me how Bitcoin self-custody
works"*). Using another agent? Point its skills directory at
`docs/agents/skills/` and have it read this file.

## Working norms

- Prefer the smallest, most local change that satisfies the request.
- Reuse existing patterns and helper scripts over new ones.
- Verify before claiming done: run the matching validator / Prettier, and for
  content, eyeball the rendered shape (headings → parts/chapters, chapter IDs
  present, assets `.webp`, frontmatter untranslated).
- Value-4-value: tasks map to GitHub issues with sat rewards
  ([`value-4-value-model.md`](../value-4-value-model.md)). Don't close or alter
  reward metadata unless that is the task.
