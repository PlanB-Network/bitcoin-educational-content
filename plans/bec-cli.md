# Plan: `bec` CLI — Agent-First Repo Tooling

> Source PRD: `docs/agents/PRD.md`

## Architectural Decisions

Durable decisions that apply across all phases:

- **Package location**: `scripts/bec/` with `pyproject.toml`, installed via `pip install -e .`
- **Entry point**: `bec` console script registered in pyproject.toml
- **CLI framework**: `click` — subcommand groups, `--help` auto-generation, option types, prompts
- **Content registry**: `content-types.yml` at repo root (~1,400 tokens) — single source of truth for all 14 content types, path patterns, schemas, tutorial categories, discipline codes, level ranges, tags, supported languages
- **Schemas**: JSON Schema Draft 7 files — initially at `scripts/validation-format/schemas/`, final location `scripts/bec/src/bec/schemas/` — root `schemas/` symlink throughout
- **Core dependencies**: `click`, `jsonschema`, `pyyaml`, `python-frontmatter`, `tqdm`
- **Test framework**: `pytest` with `click.testing.CliRunner` — fixtures in `scripts/bec/tests/fixtures/`
- **Output contract**: All commands support `--json` flag; exit codes: 0 (success), 1 (error), 2 (warning)
- **Dual mode**: All commands work non-interactive (all args on CLI) and interactive (prompts when args missing)
- **Agent files**: `docs/agents/AGENTS.md` + `docs/agents/CLAUDE.md`, symlinked to repo root via `bec agent-setup`

### Package Structure

```
scripts/bec/
    pyproject.toml
    src/bec/
        __init__.py
        cli.py              # click group, entry point
        commands/
            __init__.py
            validate.py
            new.py
            add.py
            proofread.py
            report.py
            agent_setup.py
        lib/
            __init__.py
            schema.py        # load JSON schemas, validate data
            content_types.py # parse content-types.yml
            yaml_utils.py    # safe YAML read/write
            repo.py          # find repo root, resolve paths
            markdown.py      # frontmatter, headings, chapterId generation
        data/
            bip39_wordlist.txt
    tests/
        conftest.py
        fixtures/            # known-good and known-bad content
        test_validate.py
        test_new.py
        test_add.py
        test_proofread.py
        test_report.py
```

---

## Phase 1: Package Skeleton & Content Registry

**User stories**: US-2 (bec --help), US-3 (content-types.yml), US-25 (pip install -e .), US-30 (discipline codes)

### What to build

Create the `bec` Python package that can be installed and invoked. Write `content-types.yml` at repo root containing all 14 content type definitions (path patterns, metadata filenames, schema references, example paths), tutorial categories, discipline codes with hierarchy, level ranges, the 52 tag names, and supported languages list. Implement `lib/repo.py` (find repo root by walking up to find `content-types.yml`), `lib/content_types.py` (parse and expose the registry), and `lib/yaml_utils.py` (safe YAML loading with date handling). Wire up `cli.py` as a click group with placeholder subcommands. Verify with `pip install -e .` and `bec --help`.

### Acceptance criteria

- [ ] `pip install -e scripts/bec` succeeds
- [ ] `bec --help` prints help text listing subcommands: validate, new, add, proofread, report, agent-setup
- [ ] `content-types.yml` exists at repo root with all 14 content types, each having: name, path_pattern, metadata_file, schema, content_schema (where applicable), example
- [ ] `content-types.yml` contains tutorial_categories, discipline_codes, level_range, tags (52 items), languages
- [ ] `lib/content_types.py` can load and query content-types.yml (e.g., get schema path for a content type)
- [ ] `lib/repo.py` correctly finds repo root from any subdirectory
- [ ] `lib/yaml_utils.py` loads YAML without converting dates to datetime objects
- [ ] Unit tests pass for lib/content_types.py, lib/repo.py, lib/yaml_utils.py
- [ ] All referenced schema paths in content-types.yml exist on disk
- [ ] All example paths in content-types.yml exist on disk

---

## Phase 2: Schema Infrastructure & Validate Single Path

**User stories**: US-4 (validate single), US-28 (exit codes)

### What to build

Implement `lib/schema.py` (load JSON Schema Draft 7 files, validate dicts against them, return structured errors). Create root `schemas/` symlink pointing to `scripts/validation-format/schemas/`. Implement `commands/validate.py` with `bec validate <path>` that: detects content type from path, loads the appropriate schema from content-types.yml, validates YAML metadata against schema, validates markdown frontmatter structure, and reports errors. Port core validation logic from `scripts/validation-format/validate.py` (the `validate_content()` function and its helpers). Return exit code 0 for pass, 1 for errors.

### Acceptance criteria

- [ ] `schemas/` symlink exists at repo root, pointing to `scripts/validation-format/schemas/`
- [ ] `bec validate courses/btc101` runs and reports validation results
- [ ] `bec validate tutorials/wallet/sparrow` runs and reports validation results
- [ ] `bec validate resources/books/grokking-bitcoin` runs and reports validation results (adapt to actual existing resource)
- [ ] Valid content returns exit code 0
- [ ] Content with deliberate errors returns exit code 1
- [ ] Validation checks: YAML metadata against JSON schema, markdown frontmatter required fields, content rules (heading hierarchy, chapterId format for courses)
- [ ] Test fixtures: at least one known-good and one known-bad content folder
- [ ] Tests pass via `pytest`

---

## Phase 3: Validate All & JSON Output

**User stories**: US-5 (validate --all), US-6 (--json), US-28 (exit codes)

### What to build

Extend `bec validate` with `--all` flag that discovers and validates all content in the repo. Add filter flags: `--courses-only`, `--tutorials-only`, `--type <content-type>`. Add `--json` flag that outputs machine-readable JSON with structured error/warning objects. Add `--summary-only` flag that hides individual errors and shows only counts. Use `tqdm` for progress bars during `--all` runs. Port the discovery logic from `scripts/validation-format/validate_all.py`. Exit code 2 for warnings-only.

### Acceptance criteria

- [ ] `bec validate --all` discovers and validates all 2,600+ content items with a progress bar
- [ ] `bec validate --all --courses-only` validates only courses
- [ ] `bec validate --all --tutorials-only` validates only tutorials
- [ ] `bec validate --all --type resources/books` validates only books
- [ ] `bec validate --all --json` outputs valid JSON to stdout with structure: `{summary: {total, passed, errors, warnings}, items: [{path, type, status, errors: [], warnings: []}]}`
- [ ] `bec validate --all --summary-only` shows only aggregate counts
- [ ] Exit code 0 when all pass, 1 when errors exist, 2 when only warnings
- [ ] Performance: full repo validation completes in under 60 seconds
- [ ] Tests cover filter flags and JSON output parsing

---

## Phase 4: Scaffold Course

**User stories**: US-7 (new course), US-26 (auto UUID), US-27 (enum choices)

### What to build

Implement `commands/new.py` with `bec new course` subcommand. In non-interactive mode: `bec new course --id btc201 --topic bitcoin --level intermediate --lang en --professor-id <uuid>`. In interactive mode: prompt for each required field, showing valid enum values (topics, levels) read from content-types.yml and JSON schemas. Auto-generate UUID for `course.yml`. Create folder `courses/{id}/` with `course.yml` (populated from schema required fields + UUID) and `{lang}.md` (with correct frontmatter structure and TODO placeholders). Generated content should pass `bec validate` structurally (even with TODO values).

### Acceptance criteria

- [ ] `bec new course --id test101 --topic bitcoin --level beginner --lang en --professor-id <uuid>` creates `courses/test101/` with `course.yml` and `en.md`
- [ ] `course.yml` contains a valid UUID, correct topic, level, and professor reference
- [ ] `en.md` contains correct frontmatter structure (name, goal, objectives as TODO placeholders)
- [ ] Interactive mode prompts with valid enum choices for topic, level, language
- [ ] Course ID format is validated (discipline code + 3-digit number, e.g., BTC101)
- [ ] UUID is auto-generated in valid format
- [ ] Generated course passes `bec validate courses/test101` (structural validity)
- [ ] `--json` flag outputs created file paths as JSON
- [ ] Tests verify folder structure, YAML validity, and markdown structure

---

## Phase 5: Scaffold Tutorial, Professor, Event, Resource

**User stories**: US-8 (new tutorial), US-9 (new resource), US-10 (new professor), US-11 (new event)

### What to build

Extend `commands/new.py` with four more subcommands: `bec new tutorial --category wallet --id my-tuto --lang en`, `bec new professor --id username`, `bec new event --id event-name-2025`, `bec new resource --type book --id book-name`. Each reads its JSON schema for required fields and enum values. All auto-generate UUIDs. All support interactive + non-interactive modes. Tutorial validates category against tutorial_categories from content-types.yml. Resource validates type against the 11 resource subtypes.

### Acceptance criteria

- [ ] `bec new tutorial --category wallet --id test-tuto --lang en` creates `tutorials/wallet/test-tuto/` with `tutorial.yml` + `en.md`
- [ ] `bec new professor --id test-prof` creates `professors/test-prof/` with `professor.yml` + language YML
- [ ] `bec new event --id test-event-2025` creates `events/test-event-2025/` with `event.yml`
- [ ] `bec new resource --type book --id test-book` creates `resources/books/test-book/` with `book.yml`
- [ ] `bec new resource --type podcast --id test-pod` creates `resources/podcasts/test-pod/` with `podcast.yml`
- [ ] Invalid tutorial category is rejected with helpful error listing valid categories
- [ ] Invalid resource type is rejected with helpful error listing valid types
- [ ] All generated content passes `bec validate` structurally
- [ ] Interactive mode works for all four content types
- [ ] Tests cover all content types, valid and invalid inputs

---

## Phase 6: Add Part & Chapter

**User stories**: US-12 (add part), US-13 (add chapter)

### What to build

Implement `commands/add.py` with `bec add part` and `bec add chapter`. `bec add part --course btc101 --lang en --title "Part Title"` appends `+++\n\n# Part Title` to the course markdown. `bec add chapter --course btc101 --lang en --title "Chapter Title"` appends `## Chapter Title\n\n<chapterId>three-bip39-words</chapterId>` with an auto-generated BIP39 3-word chapter ID. Implement `lib/markdown.py` with frontmatter parsing, heading manipulation, and BIP39 chapter ID generation. Bundle BIP39 wordlist as `data/bip39_wordlist.txt`.

### Acceptance criteria

- [ ] `bec add part --course btc101 --lang en --title "Test Part"` appends `+++\n\n# Test Part` to `courses/btc101/en.md`
- [ ] `bec add chapter --course btc101 --lang en --title "Test Chapter"` appends `## Test Chapter\n\n<chapterId>word-word-word</chapterId>` to `courses/btc101/en.md`
- [ ] BIP39 chapter IDs are 3 hyphenated BIP39 words (e.g., `father-loop-frog`)
- [ ] BIP39 wordlist is bundled in `scripts/bec/src/bec/data/bip39_wordlist.txt`
- [ ] Part separator is `+++` followed by blank line and `# heading`
- [ ] Chapter heading is `##` level (not `#` or `###`)
- [ ] Modified markdown still passes `bec validate` after additions
- [ ] `--json` flag outputs the appended content details
- [ ] Tests verify markdown structure before and after operations

---

## Phase 7: Add Quiz & Add Language

**User stories**: US-14 (add quiz), US-15 (add language)

### What to build

Extend `commands/add.py` with `bec add quiz --course btc101 --chapter-id <uuid>` that creates the next numbered `quizz/{nnn}/` folder with `question.yml` and `{lang}.yml` skeleton. Add `bec add language --path courses/btc101 --lang fr` that creates a new language file by copying structure (frontmatter fields, headings, chapterIds) from the original language, replacing content with TODO placeholders.

### Acceptance criteria

- [ ] `bec add quiz --course btc101 --chapter-id <id>` creates next numbered quiz folder (e.g., `quizz/005/`)
- [ ] Quiz folder contains `question.yml` with correct chapterId reference and `en.yml` skeleton
- [ ] Quiz numbering auto-detects existing quizzes and increments (e.g., if 004 exists, creates 005)
- [ ] `bec add language --path courses/btc101 --lang fr` creates `courses/btc101/fr.md`
- [ ] New language file preserves: frontmatter field structure, heading hierarchy, all `<chapterId>` tags, `+++` part separators
- [ ] New language file replaces: prose content with `TODO` placeholders
- [ ] `bec add language` works for tutorials and other content types too (not just courses)
- [ ] Generated quiz passes `bec validate` structurally
- [ ] Tests verify quiz numbering logic and language file structure preservation

---

## Phase 8: Proofread

**User stories**: US-16 (update), US-17 (reward), US-18 (batch-add)

### What to build

Implement `commands/proofread.py` absorbing logic from `scripts/proofreading-metadata/` (5 Python files). Four subcommands: `bec proofread update --path <content-path> --lang <code> --contributor <github-user>` (add contributor to proofreading metadata, update date), `bec proofread reward --path <content-path>` (calculate and display reward amounts), `bec proofread batch-add --contributor <github-user> --lang <code> --paths <path1> <path2> ...` (bulk operation), `bec proofread status --path <content-path>` (show status for all languages). No dependency on `inquirer` — all CLI args via click options.

### Acceptance criteria

- [ ] `bec proofread update --path courses/btc101 --lang fr --contributor test-user` updates proofreading metadata in the YAML
- [ ] Contributor is appended to the list, not overwriting existing contributors
- [ ] Date is updated to current date
- [ ] `bec proofread reward --path courses/btc101` displays reward calculation
- [ ] `bec proofread batch-add --contributor test-user --lang fr --paths courses/btc101 courses/btc102` updates multiple items
- [ ] `bec proofread status --path courses/btc101` shows proofreading status matrix for all languages
- [ ] All subcommands support `--json` output
- [ ] Interactive fallback when no args provided (prompts for required values)
- [ ] No dependency on `inquirer` library
- [ ] Tests with YAML fixtures verify metadata is correctly added/updated

---

## Phase 9: Report — Translation Coverage

**User stories**: US-19 (report --all), US-20 (translation --json)

### What to build

Implement `commands/report.py` with the report group and the first report subcommand: `bec report translation`. Absorbs logic from `scripts/md_translation_overview/generate_report.py`. Generates an HTML dashboard showing markdown translation coverage across all content types and languages. Supports `--output <dir>` (default: `docs/reports/`) and `--json` for machine-readable output. Wire up `bec report --all` to run all report subcommands (only translation for now, extended in later phases).

### Acceptance criteria

- [ ] `bec report translation` generates `docs/reports/md_translation_overview.html`
- [ ] `bec report translation --json` outputs valid JSON with per-content-type, per-language coverage percentages
- [ ] `bec report translation --output /tmp/reports/` writes to custom directory
- [ ] HTML report is self-contained (inline CSS/JS, no external dependencies)
- [ ] Report data matches actual repo state (spot-check a few known translations)
- [ ] `bec report --all` runs translation report (and future reports as they're added)
- [ ] Exit code 0 on success
- [ ] Tests verify HTML generation and JSON output structure

---

## Phase 10: Report — Image Translation

**User stories**: US-19 (report --all)

### What to build

Add `bec report images` subcommand. Absorbs logic from `scripts/image_translation_overview/generate_report.py`. Generates an HTML dashboard showing image translation progress — which content items have language-specific images vs fallback images. Supports `--output` and `--json`. Register in `bec report --all`.

### Acceptance criteria

- [ ] `bec report images` generates `docs/reports/image_translation_overview.html`
- [ ] `bec report images --json` outputs valid JSON with per-content-type image translation stats
- [ ] HTML report is self-contained
- [ ] Report correctly identifies images in `assets/{lang}/` vs `assets/no-txt/` patterns
- [ ] `bec report --all` now runs both translation and images reports
- [ ] Tests verify output generation

---

## Phase 11: Report — Video Deployment

**User stories**: US-22 (video)

### What to build

Add `bec report video` subcommand. Absorbs logic from `scripts/video_deployment_overview/generate_report.py`. Analyzes YouTube/PeerTube deployment status across all courses by checking video links in course YAML metadata. Supports `--output` and `--json`. Register in `bec report --all`.

### Acceptance criteria

- [ ] `bec report video` generates `docs/reports/video_deployment_overview.html`
- [ ] `bec report video --json` outputs valid JSON with per-course video deployment status
- [ ] Report identifies missing video links, broken references, platform coverage
- [ ] HTML report is self-contained
- [ ] `bec report --all` now runs translation, images, and video reports
- [ ] Tests verify output generation

---

## Phase 12: Report — Proofreading Dashboard

**User stories**: US-21 (proofreading dashboard)

### What to build

Add `bec report proofreading` subcommand. Absorbs logic from `scripts/proofreading_report/generate_proofreading_dashboard.py`. Generates a self-contained HTML dashboard with: matrix views (content x language), language statistics, contributor leaderboards, and progress tracking. Supports `--output` and `--json`. Register in `bec report --all`.

### Acceptance criteria

- [ ] `bec report proofreading` generates `docs/reports/proofreading_dashboard.html`
- [ ] `bec report proofreading --json` outputs valid JSON with matrix data, language stats, contributor rankings
- [ ] HTML dashboard includes: matrix view, language stats, leaderboard sections
- [ ] HTML report is self-contained (inline CSS/JS)
- [ ] `bec report --all` now runs translation, images, video, and proofreading reports
- [ ] Tests verify output generation and JSON structure

---

## Phase 13: Report — Course Analytics

**User stories**: US-23 (analytics)

### What to build

Add `bec report analytics` subcommand. Absorbs logic from `scripts/course_report/course_analytics.py`. Generates course structure statistics: word counts per course/chapter, chapter and part counts, quiz counts, language coverage per course. Supports `--output` and `--json`. Register in `bec report --all`. With this phase, `bec report --all` runs all 5 reports.

### Acceptance criteria

- [ ] `bec report analytics` generates `docs/reports/course_analytics_report.html`
- [ ] `bec report analytics --json` outputs valid JSON with per-course statistics (word counts, chapter counts, quiz counts)
- [ ] HTML report is self-contained
- [ ] Statistics match actual repo state (spot-check btc101)
- [ ] `bec report --all` now runs all 5 reports: translation, images, video, proofreading, analytics
- [ ] `bec report --all --output /tmp/reports/` writes all reports to custom directory
- [ ] Tests verify output generation and JSON structure

---

## Phase 14: Agent Orientation & Setup

**User stories**: US-1 (AGENTS.md), US-24 (agent-setup)

### What to build

Write `docs/agents/AGENTS.md` — the comprehensive agent orientation file covering: repo purpose, content type overview (referencing content-types.yml), `bec` CLI command reference with examples, content conventions (course IDs, BIP39 chapter IDs, professor UIDs, image formats), formatting rules (heading hierarchy, `+++` part separators, `<chapterId>` tags), validation workflow, translation/i18n patterns, common pitfalls. Write `docs/agents/CLAUDE.md` — Claude Code-specific instructions importing AGENTS.md context, tool permissions, slash command hints. Implement `commands/agent_setup.py` with `bec agent-setup` that symlinks both files to repo root (both gitignored).

### Acceptance criteria

- [ ] `docs/agents/AGENTS.md` exists with comprehensive orientation (<3,000 tokens for quick loading)
- [ ] AGENTS.md covers: repo purpose, content types (referencing content-types.yml), bec CLI commands, content conventions, formatting rules, validation workflow, translation patterns, common pitfalls
- [ ] `docs/agents/CLAUDE.md` exists with Claude Code-specific instructions
- [ ] CLAUDE.md imports/references AGENTS.md for shared context
- [ ] `bec agent-setup` creates `AGENTS.md` symlink at repo root pointing to `docs/agents/AGENTS.md`
- [ ] `bec agent-setup` creates `CLAUDE.md` symlink at repo root pointing to `docs/agents/CLAUDE.md`
- [ ] Both symlinks are listed in `.gitignore`
- [ ] An agent reading AGENTS.md + content-types.yml can understand the repo in <30 seconds (under 4,000 combined tokens)

---

## Phase 15: Tag Descriptions in Schemas

**User stories**: US-29 (tag descriptions in schemas)

### What to build

Migrate the 52 tag descriptions from `docs/50-planb-tags.md` (currently in `to_delete/docs/`) into the JSON schema files. Add tag descriptions as a `description` field or `x-tag-descriptions` extension in each schema that uses the tags enum. This makes JSON schemas the single source of truth for valid tags and their meanings. Agents reading schemas get both validation and semantics.

### Acceptance criteria

- [ ] All 52 tag descriptions are present in the JSON schema files that reference tags
- [ ] Tag descriptions are accessible as a structured field (e.g., `x-tag-descriptions` or individual enum descriptions)
- [ ] JSON schemas remain valid JSON Schema Draft 7 after modification
- [ ] `bec validate` still works correctly with modified schemas (no regression)
- [ ] No tag is missing a description
- [ ] Tests verify schemas are valid and tag descriptions are present

---

## Phase 16: Cleanup & Final Wiring

**No user story** — housekeeping and verification

### What to build

Move `scripts/validation-format/` to `to_delete/scripts/validation-format/` (after confirming `bec validate` fully replaces it). Move `scripts/proofreading-metadata/` to `to_delete/scripts/proofreading-metadata/`. Copy schemas from `scripts/validation-format/schemas/` to their final location at `scripts/bec/src/bec/schemas/`. Update root `schemas/` symlink to point to new location. Remove `docs/agents/REFACTOR_PLAN.md` (superseded by implemented PRD). Evaluate `docs/how-to-translate-image.md` for absorption into AGENTS.md. Run full `bec validate --all` against real repo to confirm no regressions. Run full `bec report --all` to confirm all reports generate correctly.

### Acceptance criteria

- [ ] `scripts/validation-format/` moved to `to_delete/`
- [ ] `scripts/proofreading-metadata/` moved to `to_delete/`
- [ ] Schemas live at `scripts/bec/src/bec/schemas/` (canonical location)
- [ ] Root `schemas/` symlink points to `scripts/bec/src/bec/schemas/`
- [ ] `docs/agents/REFACTOR_PLAN.md` moved to `to_delete/`
- [ ] `bec validate --all` passes on real repo content (exit code 0 or 2 for warnings only)
- [ ] `bec report --all` generates all 5 HTML reports successfully
- [ ] `bec new course` / `bec new tutorial` generate valid content that passes validation
- [ ] `bec --help` shows all subcommands with descriptions
- [ ] All pytest tests pass
- [ ] No remaining imports or references to old script paths
