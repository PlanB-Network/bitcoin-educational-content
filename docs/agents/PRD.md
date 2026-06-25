## Problem Statement

The Bitcoin Educational Content repository (2,600+ content items across 14 types, 30 languages) has solid infrastructure — 23 JSON schemas, validation scripts, translation pipeline — but it is poorly discoverable for AI agents and automation. An agent entering the repo has no orientation file, no unified CLI, and must crawl scattered scripts to understand the data model. Documentation is partially stale and human-only. Scripts lack proper CLI interfaces (no argparse, hardcoded paths, interactive-only prompts). There is no machine-readable registry mapping content types to their schemas, paths, and conventions.

As agents increasingly become the primary content creators and maintainers, the repo needs to be refactored for **agent-first discoverability** without changing any content.

## Solution

Create a unified Python CLI tool (`bec` — bitcoin-education-content) that is the single entry point for all repo operations: validation, content scaffolding, atomic content operations, proofreading management, and report generation. Support this with a machine-readable content registry (`content-types.yml`), agent orientation files (`AGENTS.md`, `CLAUDE.md`), and a clean repo structure with obsolete scripts and docs removed.

The `bec` CLI is installed as a proper Python package (`pip install -e .`) and replaces all existing scattered scripts with a single, consistent interface.

## User Stories

1. As an AI agent, I want to read a single orientation file (`AGENTS.md`) so that I understand the repo structure, conventions, and available operations in under 30 seconds
2. As an AI agent, I want to run `bec --help` so that I discover all available operations without crawling the codebase
3. As an AI agent, I want to read `content-types.yml` so that I understand every content type, its path pattern, schema, and metadata file in a machine-parseable format
4. As an AI agent, I want to run `bec validate courses/btc101` so that I verify my changes are valid before committing
5. As an AI agent, I want to run `bec validate --all` so that I check the entire repo for errors in a single command
6. As an AI agent, I want to run `bec validate --all --json` so that I get machine-readable validation results I can parse and act on
7. As a contributor, I want to run `bec new course` so that a valid course skeleton is generated with correct folder structure, UUID, and metadata
8. As a contributor, I want to run `bec new tutorial --category wallet` so that I get a valid tutorial skeleton in the right directory
9. As a contributor, I want to run `bec new resource --type book` so that I get a valid resource skeleton without needing to know the schema
10. As a contributor, I want to run `bec new professor` so that a professor folder is created with a valid UUID and correct YAML structure
11. As a contributor, I want to run `bec new event` so that an event folder is created with valid metadata
12. As an AI agent, I want to run `bec add part --course btc101 --lang en --title "New Part"` so that a properly formatted part separator and heading are appended to the course markdown
13. As an AI agent, I want to run `bec add chapter --course btc101 --lang en --title "New Chapter"` so that a chapter heading with auto-generated BIP39 chapterId is added to the course
14. As an AI agent, I want to run `bec add quiz --course btc101 --chapter-id <uuid>` so that a quiz folder skeleton is created with question.yml and a language file
15. As an AI agent, I want to run `bec add language --path courses/btc101 --lang fr` so that a new language markdown file is created with the correct frontmatter structure copied from the original language
16. As a maintainer, I want to run `bec proofread update --path courses/btc101 --lang fr --contributor github-user` so that proofreading metadata is updated programmatically without interactive prompts
17. As a maintainer, I want to run `bec proofread reward --path courses/btc101` so that proofreading rewards are calculated and displayed
18. As a maintainer, I want to run `bec proofread batch-add --contributor github-user --lang fr --paths courses/btc101 courses/btc102` so that multiple content items are updated at once
19. As a maintainer, I want to run `bec report --all --output ./reports/` so that all HTML dashboards are regenerated in one command
20. As a monitoring system, I want to run `bec report translation --json` so that I get machine-readable translation coverage data for automated dashboards
21. As a maintainer, I want to run `bec report proofreading` so that a self-contained HTML dashboard is generated with matrix views, language stats, and leaderboards
22. As a maintainer, I want to run `bec report video` so that YouTube/PeerTube deployment status is analyzed across all courses
23. As a maintainer, I want to run `bec report analytics` so that course structure statistics (word counts, chapters, parts) are generated
24. As a contributor, I want to run `bec agent-setup` so that AGENTS.md and CLAUDE.md are symlinked to the repo root for my AI agent to discover
25. As a contributor, I want to run `pip install -e .` once and have all `bec` dependencies installed automatically
26. As an AI agent, I want `bec new course` to auto-generate a UUID so that I don't need to figure out UUID generation myself
27. As an AI agent, I want `bec new course` to present valid enum choices (topic, subtopic, level) so that I pick from valid values instead of guessing
28. As an AI agent, I want `bec validate` to return exit code 0 (pass), 1 (errors), or 2 (warnings) so that I can use it in automated workflows
29. As a maintainer, I want the tag list with descriptions to live inside the JSON schemas so that there is a single source of truth for valid tags
30. As an AI agent, I want `content-types.yml` to include discipline codes and course ID conventions so that I can generate valid course IDs like BTC101 without reading separate documentation

## Implementation Decisions

### `bec` CLI Architecture

- Single Python package with `pyproject.toml`, installed via `pip install -e .`
- Entry point: `bec` command registered as a console script
- Framework: `click` for subcommands, `--help`, option types, and prompts
- All commands support both interactive mode (prompts when args missing) and non-interactive mode (all values as CLI args)
- All commands that produce output support `--json` flag for machine-readable output
- All commands return proper exit codes (0 = success, 1 = error, 2 = warning)

### Package Structure

```
scripts/bec/
    pyproject.toml
    src/bec/
        __init__.py
        cli.py              # click group, entry point
        commands/
            __init__.py
            validate.py      # rewrite of validation-format/
            new.py           # content scaffolding
            add.py           # atomic operations (part, chapter, quiz, language)
            proofread.py     # rewrite of proofreading-metadata/
            report.py        # rewrite of 5 report generators
            agent_setup.py   # symlink AGENTS.md/CLAUDE.md
        lib/
            __init__.py
            schema.py        # load JSON schemas, validate data against them
            content_types.py # parse content-types.yml registry
            yaml_utils.py    # safe YAML read/write with date handling, null cleanup
            repo.py          # find repo root, resolve paths, detect content types
            markdown.py      # frontmatter parsing, heading manipulation, chapterId generation
```

### `content-types.yml`

- Lives at repo root
- Single fat file (~1,400 tokens) containing:
  - All 14 content type definitions (path patterns, metadata files, schemas, content schemas, examples)
  - Tutorial categories list
  - Course discipline codes with hierarchy
  - Course level ranges (101-499)
  - Tag names list (52 items, names only — descriptions in JSON schemas)
  - Supported languages list
- Consumed by: `bec` CLI, `AGENTS.md`, validation logic
- The `bec` CLI reads `content-types.yml` at startup to know all content types — replaces the hardcoded `CONTENT_TYPES` dict in current `validate.py`

### `schemas/` Symlink

- Symlink at repo root: `schemas/ -> scripts/validation-format/schemas/`
- Makes schemas discoverable at top level
- `content-types.yml` references schemas as `schemas/course-scheme.json`
- After `bec` absorbs validation logic, the canonical schema location becomes `scripts/bec/src/bec/schemas/` and the root symlink points there instead

### Validation Rewrite (`bec validate`)

- Absorbs logic from `scripts/validation-format/validate.py` (~900 lines) and `validate_all.py` (~240 lines)
- Core logic preserved: JSON Schema Draft 7 validation, YAML metadata, markdown frontmatter, content rules, quiz validation
- Reads content type configs from `content-types.yml` instead of hardcoded dict
- Shared utilities extracted to `lib/` (schema loading, YAML handling, repo root detection)
- Outputs: colored terminal, JSON, and HTML report
- `bec validate <path>` — single folder
- `bec validate --all` — all content
- `bec validate --all --courses-only` / `--tutorials-only` / `--type resources/books`
- `bec validate --all --json` — machine-readable output
- `bec validate --all --summary-only` — hide individual errors

### Content Scaffolding (`bec new`)

- `bec new course` — creates `courses/{id}/` with `course.yml` + `{lang}.md`
- `bec new tutorial` — creates `tutorials/{category}/{id}/` with `tutorial.yml` + `{lang}.md`
- `bec new professor` — creates `professors/{id}/` with `professor.yml`
- `bec new event` — creates `events/{id}/` with `event.yml`
- `bec new resource --type {book|podcast|...}` — creates `resources/{type}/{id}/` with `{type}.yml`
- All commands read JSON schemas for required fields and valid enum values
- All commands auto-generate UUIDs
- Non-interactive mode: `bec new course --id btc201 --topic bitcoin --level intermediate --lang en --professor-id <uuid>`
- Interactive mode: prompts for each required field with enum choices when no args provided
- Generated markdown files contain `TODO` placeholders in frontmatter (name, goal, objectives)
- Optional fields present but commented out — validation cleans up unused optional fields

### Atomic Operations (`bec add`)

- `bec add part --course <id> --lang <code> --title "Part Title"` — appends `+++\n\n# Part Title` to course markdown
- `bec add chapter --course <id> --lang <code> --title "Chapter Title"` — appends `## Chapter Title\n\n<chapterId>three-bip39-words</chapterId>` with auto-generated BIP39 chapter ID
- `bec add quiz --course <id> --chapter-id <uuid>` — creates next numbered `quizz/{nnn}/` folder with `question.yml` + `{lang}.yml` skeleton
- `bec add language --path <content-path> --lang <code>` — creates new language file by copying structure (frontmatter fields, headings, chapterIds) from original language, with `TODO` content placeholders

### Proofreading Rewrite (`bec proofread`)

- Absorbs logic from `scripts/proofreading-metadata/` (5 Python files)
- `bec proofread update --path <content-path> --lang <code> --contributor <github-user>` — adds contributor to proofreading metadata, updates date
- `bec proofread reward --path <content-path>` — calculates and displays reward amounts
- `bec proofread batch-add --contributor <name> --lang <code> --paths <path1> <path2> ...` — bulk operation
- `bec proofread status --path <content-path>` — shows proofreading status for all languages
- All commands work non-interactively (argparse) — no dependency on `inquirer`
- Interactive mode available as fallback when no args provided

### Reports Rewrite (`bec report`)

- Absorbs and rewrites 5 report generators as first-class `bec` subcommands
- `bec report --all` — generates all reports
- `bec report translation` — markdown translation coverage (replaces md_translation_overview)
- `bec report images` — image translation progress (replaces image_translation_overview)
- `bec report video` — video deployment status (replaces video_deployment_overview)
- `bec report proofreading` — proofreading dashboard (replaces proofreading_report)
- `bec report analytics` — course structure statistics (replaces course_report)
- All reports support `--output <dir>` (default: `docs/reports/`)
- All reports support `--json` for machine-readable output alongside HTML
- Designed for scheduled/automated execution (proper exit codes, no interactive prompts)

### Agent Orientation Files

- `docs/agents/AGENTS.md` — cross-agent standard, comprehensive orientation:
  - Repo purpose and context
  - Content type overview (references content-types.yml)
  - `bec` CLI command reference
  - Content conventions (course IDs, BIP39 chapter IDs, professor UIDs, image formats)
  - Formatting rules (heading hierarchy, `+++` part separators, `<chapterId>` tags)
  - Validation workflow
  - Translation/i18n patterns
  - Common pitfalls
- `docs/agents/CLAUDE.md` — Claude Code-specific:
  - Imports AGENTS.md context
  - Tool permissions
  - Slash command hints
- `bec agent-setup` creates symlinks at repo root (both gitignored)

### Tag Descriptions in Schemas

- Move the 52 tag descriptions from `docs/50-planb-tags.md` (being deleted) into the JSON schema files
- Add descriptions as comments or a description field in the schema's tags enum
- Tags validated by schema, descriptions available for agents that read schemas

### Cleanup — `to_delete/` lifecycle

The repo uses a `to_delete/` staging folder. Items are moved there during the refactor, then permanently deleted by the maintainer.

**Already in `to_delete/` (moved before PRD implementation begins):**
- `to_delete/scripts/` — 40 items: all old scripts, one-off fixes, empty directories, report generators, PDF tools, etc.
- `to_delete/docs/` — 12 items: stale README, templates, tag lists, category docs, course docs, planning artifacts (GITHUB_ISSUES.md, SCRIPTS_AUDIT.md)

**To be moved to `to_delete/` during PRD implementation:**
- `scripts/validation-format/` — after its logic is fully absorbed into `bec validate` and tests pass
- `scripts/proofreading-metadata/` — after its logic is fully absorbed into `bec proofread` and tests pass
- `scripts/auto-translate/` — NOT moved (out of scope, stays as-is until translation PRD)
- `docs/agents/REFACTOR_PLAN.md` — working document, superseded by this PRD once implemented
- `docs/how-to-translate-image.md` — evaluate if still needed or absorbed into AGENTS.md
- Old `.venv/` at repo root — replaced by `bec` package's own venv

**Final cleanup (done by maintainer after all `bec` commands verified working):**
- Delete `to_delete/` entirely
- Delete absorbed `scripts/validation-format/` and `scripts/proofreading-metadata/`
- The `schemas/` directory moves from `scripts/validation-format/schemas/` to `scripts/bec/src/bec/schemas/` (root symlink updated to point to new location)
- Data from deleted docs (tags → JSON schemas, discipline codes → content-types.yml, formatting rules → AGENTS.md) is already absorbed before deletion

## Testing Decisions

Good tests verify external behavior through the CLI interface, not internal implementation details. Tests should run `bec` subcommands and check outputs, exit codes, and generated files.

### What to test

- **`bec validate`**: Run against known-good content (should pass), known-bad content fixtures (should fail with specific errors), and edge cases (empty folders, missing files). Verify exit codes and JSON output format.
- **`bec new`**: Run each scaffolding command, verify generated folder structure, YAML validity against schema, UUID format, and that generated content passes basic validation structure (even with TODO placeholders).
- **`bec add`**: Run atomic operations on test content, verify markdown structure (correct heading levels, chapterId format, part separators), and that the modified content still has valid structure.
- **`bec proofread`**: Run against test YAML fixtures, verify proofreading metadata is correctly added/updated, dates are set, contributors are appended not overwritten.
- **`bec report`**: Run against test content fixtures, verify HTML output is generated, JSON output parses correctly, and report data matches expected values.

### Test infrastructure

- Use `pytest` as the test runner
- Test fixtures: minimal content folders in `tests/fixtures/` with known-valid and known-invalid content
- Integration tests: run `bec` commands via `click.testing.CliRunner` (in-process, no subprocess needed)
- Schema tests: verify all 23 JSON schemas are valid JSON Schema Draft 7
- `content-types.yml` test: verify all referenced schemas exist, all example paths exist in repo

## Out of Scope

- **Translation rewrite**: The `auto-translate/` pipeline (LLM-Translator integration, DeepL/OpenAI/Google providers, glossary management) is explicitly deferred to a follow-up PRD. `bec translate` is not implemented in this PRD.
- **Content changes**: No courses, tutorials, resources, events, or professor content is modified.
- **New content types**: No new content types are added.
- **CI/CD pipeline**: While `bec` supports JSON output and exit codes suitable for CI/CD, setting up GitHub Actions or similar is not part of this PRD.
- **GUI tools**: The `tutorial-related/data-creator/` GUI is not rewritten or replaced.
- **Website/API changes**: The PlanB Network application is not modified.

## Further Notes

- The existing `scripts/validation-format/schemas/` directory contains 23 well-maintained JSON Schema Draft 7 files that represent significant prior work. The `bec` rewrite preserves these schemas exactly — it changes how they are loaded and used, not the schemas themselves.
- The repo contains 2,600+ content items: 48 courses, 316 tutorials, 93 professors, 287 events, and ~1,900 resources across 11 subtypes. Any scaffolding or validation changes must be tested against this scale.
- The `content-types.yml` file is approximately 1,400 tokens and is designed to be auto-loaded by agents. This is intentionally compact to minimize context window cost.
- The `bec` package should have minimal dependencies. Core: `click`, `jsonschema`, `pyyaml`, `python-frontmatter`. Reports: `tqdm` (progress bars). No dependency on `inquirer`, `customtkinter`, or other heavy UI libraries.
- BIP39 chapter IDs (3-word identifiers like `father-loop-frog`) require a BIP39 wordlist. This should be bundled as a data file in the package, not fetched at runtime.
