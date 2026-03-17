# GitHub Issues — Agent-Friendliness Refactor

This document contains the draft for the main epic issue and all sub-issues.
Each sub-issue is independently actionable and can be assigned to an agent or contributor.

---

## EPIC: Agent-Friendliness Refactor

**Title**: `[REFACTOR] Make repository agent-friendly: discoverability, CLI, schemas, documentation`

**Labels**: `refactor`, `dx`, `infrastructure`

**Body**:

### Problem

This content repo has solid infrastructure (23 JSON schemas, validation scripts, translation pipeline) but it's poorly discoverable for AI agents and automation. An agent entering the repo has no orientation file, no single CLI entry point, and must crawl scattered scripts to understand the data model. Documentation is partially stale and human-only.

### Goals

1. Any AI agent can orient itself in < 30 seconds (AGENTS.md)
2. All operations discoverable via `make help`
3. Content creation guided by CLI scaffolding, not static templates
4. Schema validation is a one-command operation
5. Repo root stays clean (no AI config pollution)
6. Scripts are CLI-friendly (argparse, --help, proper exit codes)
7. No content changes — only infrastructure and discoverability

### Architecture Decisions

See [REFACTOR_PLAN.md](docs/agents/REFACTOR_PLAN.md) for full ADRs.

Key decisions:
- Agent config files in `docs/agents/`, symlinked to root via `make agent-setup` (gitignored at root)
- `Makefile` as universal CLI entry point
- `content-types.yml` as machine-readable content registry
- CLI scaffolding replaces static template repo
- `schemas/` symlink at root for discoverability
- Scripts cleaned up: 15 deleted, 8 refactored for CLI

### Sub-Issues

Tracked below. Each is independently actionable.

### Reference Documents

- [REFACTOR_PLAN.md](docs/agents/REFACTOR_PLAN.md) — Architecture decisions
- [SCRIPTS_AUDIT.md](docs/agents/SCRIPTS_AUDIT.md) — Full scripts audit with recommendations

---

## Sub-Issues

---

### Issue 1: Create `content-types.yml`

**Title**: `[INFRA] Create content-types.yml — machine-readable content type registry`

**Labels**: `infra`, `agent-friendly`

**Body**:

Create a `content-types.yml` at repo root that maps every content type to its path pattern, metadata file, schema, content schema, and a real example.

This becomes the single source of truth that agents, the Makefile, and scaffolding scripts all consume.

**Acceptance criteria**:
- [ ] File at repo root: `content-types.yml`
- [ ] Covers all 14 content types (courses, tutorials, professors, events, 10 resource types)
- [ ] Each type has: `path_pattern`, `metadata_file`, `schema`, `content_schema` (if applicable), `content_files`, `assets`, `example`
- [ ] Tutorials section includes `categories` list
- [ ] Courses section includes `disciplines` map (BTC, BIZ, etc.) and `levels` (101-499 ranges)
- [ ] Tags list included (from current `docs/50-planb-tags.md`)
- [ ] Validated: YAML parses cleanly, all referenced schema files exist, all example paths exist

---

### Issue 2: Create `Makefile`

**Title**: `[INFRA] Create Makefile — universal CLI entry point for all operations`

**Labels**: `infra`, `agent-friendly`

**Body**:

Create a `Makefile` at repo root that wraps all repo operations. `make help` should list everything. All targets should auto-activate `.venv` if needed.

**Targets to implement**:
```
help                 — List all available commands
agent-setup          — Symlink AGENTS.md/CLAUDE.md to root
validate             — Validate all content (wraps validation-format/validate_all.py)
validate-courses     — Validate courses only
validate-tutorials   — Validate tutorials only
validate-resources   — Validate resources only
validate-one         — Validate single folder: make validate-one path=courses/btc101
lint                 — Format with prettier (wraps npm run lint)
report               — Generate all reports (wraps generate_all_reports.py)
report-proofreading  — Generate proofreading dashboard
new-course           — Scaffold new course (interactive)
new-tutorial         — Scaffold new tutorial (interactive)
new-professor        — Scaffold new professor (interactive)
new-event            — Scaffold new event (interactive)
quiz-pdf             — Generate quiz PDFs: make quiz-pdf course=btc101 lang=en
```

**Acceptance criteria**:
- [ ] `make help` prints formatted list of all targets with descriptions
- [ ] All targets that need Python auto-activate `.venv`
- [ ] Validation targets work and return proper exit codes
- [ ] `make agent-setup` creates symlinks and reports success

---

### Issue 3: Create `schemas/` symlink

**Title**: `[INFRA] Create schemas/ symlink at repo root`

**Labels**: `infra`, `agent-friendly`

**Body**:

Create a symlink `schemas/ -> scripts/validation-format/schemas/` at repo root.

Currently schemas are buried at `scripts/validation-format/schemas/`. Surfacing them at root makes them discoverable for agents and allows `content-types.yml` to reference them with short paths.

**Acceptance criteria**:
- [ ] `schemas/` symlink exists at repo root
- [ ] Points to `scripts/validation-format/schemas/`
- [ ] All 23 schema files accessible via `schemas/*.json`
- [ ] Symlink committed to git

---

### Issue 4: Create `AGENTS.md` and `CLAUDE.md`

**Title**: `[INFRA] Create AGENTS.md and CLAUDE.md in docs/agents/`

**Labels**: `infra`, `agent-friendly`, `documentation`

**Body**:

Create the agent orientation files that give any AI agent complete context to work with this repo.

`AGENTS.md` (cross-agent standard) should include:
- Repo purpose and context (PlanB Network, Bitcoin education, open-source, multilingual)
- Content type summary (reference content-types.yml for details)
- Key operations via Makefile
- Content structure conventions (course IDs, BIP39 chapter IDs, BIP39 professor UIDs)
- Formatting rules (absorbed from course_documentation.md)
- Validation workflow
- Translation/i18n patterns
- Value-for-value model context
- Common pitfalls and gotchas

`CLAUDE.md` should:
- Reference AGENTS.md for base context
- Add Claude-specific tool permissions
- Add slash command hints

**Acceptance criteria**:
- [ ] `docs/agents/AGENTS.md` exists and is comprehensive
- [ ] `docs/agents/CLAUDE.md` exists and references AGENTS.md
- [ ] `make agent-setup` symlinks both to root
- [ ] `/AGENTS.md` and `/CLAUDE.md` added to `.gitignore`

---

### Issue 5: Delete obsolete scripts and empty directories

**Title**: `[CLEANUP] Delete 15 obsolete scripts and empty directories`

**Labels**: `cleanup`, `scripts`

**Body**:

Per [SCRIPTS_AUDIT.md](docs/agents/SCRIPTS_AUDIT.md), delete the following:

**Empty / orphaned directories**:
- `scripts/content_to_pdf/`
- `scripts/update_course_info/`
- `scripts/fix_italic_typos/`
- `scripts/wikimedia-commons/`

**One-off scripts (job complete)**:
- `scripts/extract-language-specific-content.py`
- `scripts/relocate_contributors_builders.py`
- `scripts/rename-translated-content.py`
- `scripts/fix-symbols/`

**Obsolete / superseded**:
- `scripts/convert-to-webp-py/` (author recommends external GUI tool)
- `scripts/course-update-tool/` (ghost dir, no entry point)
- `scripts/convert-to-pdf/` (superseded by quizz_to_pdfs + course-to-pdf)
- `scripts/validate.py` (top-level, older version — superseded by validation-format/)
- `scripts/validate_all.py` (top-level, older version)
- `scripts/webp-batch-conversion.py` (hardcoded to single dir)
- `scripts/get-planb-tags.py` (one-off analysis, tag data moving to content-types.yml)

**Acceptance criteria**:
- [ ] All 15 items deleted
- [ ] No remaining scripts reference deleted items
- [ ] Validation still passes: `make validate`

---

### Issue 6: Refactor auto-translate/ for CLI

**Title**: `[REFACTOR] Add CLI interface to auto-translate/`

**Labels**: `refactor`, `scripts`

**Body**:

The auto-translate system works but has no proper CLI interface. Batch scripts lack argparse, documentation is minimal, and .env/nohup.out artifacts are present.

**Work**:
- Add argparse with --help to `translation_controller.py` and all batch scripts
- Expand README with examples and requirements
- Clean up .env and nohup.out artifacts
- Document LLM-Translator integration requirements
- Add to Makefile as `make translate` target

---

### Issue 7: Refactor proofreading-metadata/ for CLI

**Title**: `[REFACTOR] Add batch CLI mode to proofreading-metadata/`

**Labels**: `refactor`, `scripts`

**Body**:

Currently pure `inquirer` interactive mode. Cannot be used by agents or in CI/CD.

**Work**:
- Add `--batch` mode with argparse alongside existing interactive mode
- Add `--dry-run` flag for preview
- Support stdin/config file input
- Add to Makefile

---

### Issue 8: Refactor course-related/ for CLI

**Title**: `[REFACTOR] Add argparse to course-related/ scripts`

**Labels**: `refactor`, `scripts`

**Body**:

Scripts: `add_uuid.py`, `plan.py`, `quizz.py`, `update-all-courses-hours.py`

**Work**:
- Add argparse `--file`/`--course` options to each script
- Keep interactive mode as fallback when no args provided
- Add to Makefile as relevant targets

---

### Issue 9: CLI-ify remaining top-level scripts

**Title**: `[REFACTOR] Add CLI interfaces to remaining top-level scripts`

**Labels**: `refactor`, `scripts`

**Body**:

Scripts needing argparse:
- `book-uniformizer.py` — add target dir, languages, --dry-run
- `course-to-pdf.py` — replace interactive menu with `python course-to-pdf.py BTC101 [--all]`
- `fix_project_descriptions.py` — add target dir, --dry-run, --verbose
- `generate_all_reports.py` — add `--video-only`, `--image-only`, `--md-only`
- `translation_builders.py` — add languages/--dry-run; update deprecated OpenAI API

---

### Issue 10: Add --output args to report generators

**Title**: `[POLISH] Add --output argument to report generator scripts`

**Labels**: `polish`, `scripts`

**Body**:

These scripts work but have hardcoded output paths:
- `image_translation_overview/generate_report.py`
- `md_translation_overview/generate_report.py`
- `video_deployment_overview/generate_report.py`
- `proofreading_report/generate_proofreading_dashboard.py`
- `course_report/course_analytics.py`

Add `--output` argument to each. Keep current path as default.

---

### Issue 11: Fix hardcoded paths in kept scripts

**Title**: `[POLISH] Fix hardcoded paths in rename_image/ and glossary tool`

**Labels**: `polish`, `scripts`

**Body**:

- `rename_image/rename_images.py` line 67: hardcoded `../../courses` — should accept arg or auto-detect repo root
- `add_tuto_title_to_glossary_translation/add_tuto_to_glossary.py` lines 15-16: hardcoded paths — should use repo root detection

---

### Issue 12: Create CLI scaffolding (make new-*)

**Title**: `[FEATURE] Create CLI scaffolding for new content creation`

**Labels**: `feature`, `agent-friendly`

**Body**:

Replace `docs/PBN-template-repo/` with `make new-*` commands that generate valid content folders interactively.

**Commands**:
- `make new-course` — prompt for ID, topic, subtopic, level, professor → generate folder
- `make new-tutorial` — prompt for category, name, professor → generate folder
- `make new-professor` — prompt for name, links → generate folder
- `make new-event` — prompt for name, type, dates → generate folder

**Implementation**:
- Python script reading `content-types.yml` for structure and JSON schemas for required fields/enums
- Generate valid YAML metadata + empty markdown template
- Auto-generate UUID
- Run validation on output
- Non-interactive mode: accept all values as CLI args

**Acceptance criteria**:
- [ ] All 4 `make new-*` commands work
- [ ] Generated content passes `make validate-one`
- [ ] Interactive mode prompts for required fields with enum choices
- [ ] Non-interactive mode accepts all values as args

---

### Issue 13: Clean up docs/ directory

**Title**: `[CLEANUP] Clean up docs/ — delete stale files, transform data to YAML`

**Labels**: `cleanup`, `documentation`

**Body**:

Per REFACTOR_PLAN.md ADR-6:

**Delete** (absorbed into AGENTS.md or content-types.yml):
- `docs/README.md` (stale)
- `docs/tutorial-categories.md` (redundant with schema)
- `docs/course_documentation.md` (formatting rules → AGENTS.md)
- `docs/planb-uid.md` (→ AGENTS.md)
- `docs/value-4-value-model.md` (→ AGENTS.md)
- `docs/tutorial-creation-guidelines.md` (stale, → CLI scaffolding)
- `docs/PBN-template-repo/` (→ CLI scaffolding)

**Transform** (data files → machine-readable YAML in content-types.yml):
- `docs/50-planb-tags.md` → tags section of content-types.yml
- `docs/course_ID_rules.md` → disciplines section of content-types.yml

**Keep**:
- `docs/reports/` (generated)
- `docs/how-to-translate-image.md` (workflow)
- `docs/agents/` (new, our refactor output)

**Depends on**: Issue 1 (content-types.yml), Issue 4 (AGENTS.md), Issue 12 (scaffolding)

---

### Issue 14: Update .gitignore and README.md

**Title**: `[INFRA] Update .gitignore and README.md for agent-setup workflow`

**Labels**: `infra`

**Body**:

- Add `/AGENTS.md` and `/CLAUDE.md` to `.gitignore`
- Add "AI Agent Usage" section to `README.md` explaining `make agent-setup`
- Verify no other generated files need gitignoring

---

## Implementation Order (suggested)

```
Phase 1 — Foundation (no breaking changes):
  Issue 1:  content-types.yml
  Issue 3:  schemas/ symlink
  Issue 5:  Delete obsolete scripts
  Issue 14: .gitignore + README update

Phase 2 — CLI layer:
  Issue 2:  Makefile
  Issue 4:  AGENTS.md + CLAUDE.md

Phase 3 — Script refactoring (parallel):
  Issue 6:  auto-translate/ CLI
  Issue 7:  proofreading-metadata/ CLI
  Issue 8:  course-related/ CLI
  Issue 9:  Top-level scripts CLI
  Issue 10: Report generator polish
  Issue 11: Hardcoded path fixes

Phase 4 — Scaffolding + cleanup:
  Issue 12: CLI scaffolding (make new-*)
  Issue 13: docs/ cleanup
```
