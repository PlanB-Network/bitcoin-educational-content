# Validation Format - Implementation Plan

## Overview

Create a modular, centralized validation system for all content types in the repository.

**Goal**: A single script that takes a content folder path (relative to repo root), auto-detects the content type, and validates it against the corresponding schema.

**Location**: `scripts/validation-format/`

---

## Phase 1: Setup & Reorganization ✓

### 1.1 Create folder structure
- [x] Create `scripts/validation-format/` directory
- [x] Create `scripts/validation-format/schemas/` directory for all JSON schemas

### 1.2 Move and consolidate schemas
- [x] Move course schemas from `docs/PBN-template-repo/courses/`
  - `course-scheme.json`
  - `course-content-scheme.json`
- [x] Move tutorial schemas from `docs/PBN-template-repo/tutorials/`
  - `tutorial-scheme.json`
  - `tutorial-content-scheme.json`
- [x] Move professor schemas from `docs/PBN-template-repo/professors/`
  - `professor-scheme.json`
  - `professor-content-scheme.json`
- [x] Move event schemas from `docs/PBN-template-repo/events/`
  - `event-scheme.json`
- [x] Move resource schemas from `docs/PBN-template-repo/resources/`
  - `bet-scheme.json`, `bet-content-scheme.json`
  - `book-scheme.json`, `book-content-scheme.json`
  - `channel-scheme.json`
  - `conference-scheme.json`
  - `movie-scheme.json`
  - `newsletter-scheme.json`
  - `podcast-scheme.json`
  - `project-scheme.json` (non-community-builder-scheme.json)
  - `word-scheme.json` (glossary)
- [x] Move quiz schemas
  - `quizz-question-scheme.json`
  - `quizz-translation-scheme.json`

### 1.3 Move validator script
- [x] Copy `docs/PBN-template-repo/scripts/schema_validator.py` to `scripts/validation-format/validate.py`
- [x] Update schema path resolution to use new `schemas/` directory
- [ ] Remove old script from `docs/PBN-template-repo/scripts/` (deferred - keep for backward compatibility)

---

## Phase 2: Create Paper Schema ✓

### 2.1 Analyze paper structure
- [x] Document all fields found in existing `paper.yml` files:
  - `title` (required, string)
  - `original_language` (required, string, ISO 639-1)
  - `authors` (required, array of strings)
  - `abstract` (required, string, multiline)
  - `publication_date` (optional, string, YYYY-MM-DD)
  - `paper_type` (required, enum: whitepaper, conference, academic, pre-print, review, PhD Thesis, book)
  - `source` (optional, string)
  - `type` (optional, enum: SCI, SCIE, SSCI)
  - `category` (optional, string)
  - `topics` (required, array of strings)
  - `pdf_url` (required, string, URL format)
  - `id` (required, string, UUID format)

### 2.2 Create paper schema
- [x] Create `scripts/validation-format/schemas/paper-scheme.json`
- [x] Follow same JSON Schema format as other schemas (draft-07)
- [x] Define required vs optional fields
- [x] Add proper validation patterns (UUID, date, URL)

---

## Phase 3: Update Validator Script ✓

### 3.1 Add paper support
- [x] Add `resources/papers` to CONTENT_TYPES mapping
- [x] Map to `paper.yml` and `paper-scheme.json`

### 3.2 Fix schema path resolution
- [x] Update all schema path lookups to use `scripts/validation-format/schemas/`
- [x] Ensure relative path resolution works from any working directory

### 3.3 Verify all content types work
- [x] Test courses validation (btc101: 0 errors)
- [x] Test tutorials validation (sparrow-wallet: runs correctly)
- [x] Test professors validation (runs correctly)
- [x] Test events validation (runs correctly)
- [x] Test resources/bet validation (runs correctly)
- [x] Test resources/books validation (runs correctly)
- [x] Test resources/channels validation (0 errors)
- [x] Test resources/conferences validation (runs correctly)
- [x] Test resources/glossary validation (runs correctly)
- [x] Test resources/movies validation (runs correctly)
- [x] Test resources/newsletters validation (runs correctly)
- [x] Test resources/papers validation (0 errors)
- [x] Test resources/podcasts validation (runs correctly)
- [x] Test resources/projects validation (runs correctly)

Note: Some content types show validation errors due to schema drift (schemas need updating to match current content structure). The validator itself works correctly for all types.

---

## Phase 4: Enhance Output Options ✓

### 4.1 Add JSON output flag
- [x] Add `--json` / `-j` flag for JSON output
- [x] Structure JSON output with:
  - `folder`: content path validated
  - `results`: array with file, valid, errors, warnings
  - `total_errors`: total error count
  - `total_warnings`: total warning count

### 4.2 Add exit codes
- [x] Exit code 0: validation passed
- [x] Exit code 1: validation failed (errors)
- [x] Exit code 2: validation passed with warnings only

### 4.3 Keep terminal output as default
- [x] Colored output for human readability (ANSI codes)
- [x] Summary statistics at the end

---

## Phase 5: Create Validate-All Wrapper ✓

### 5.1 Create bulk validation script
- [x] Create `scripts/validation-format/validate_all.py`
- [x] Iterate over all content folders
- [x] Call `validate.py` for each
- [x] Aggregate results
- [x] Support filtering by content type (`--courses-only`, `--tutorials-only`, `--resources-only`, `--type`)

### 5.2 Generate reports
- [x] Summary report in terminal (with progress bar)
- [x] JSON output (`--json`)
- [ ] Optional HTML report (`--html-report`) - deferred

---

## Phase 6: Cleanup

### 6.1 Remove old files
- [ ] Remove `docs/PBN-template-repo/scripts/schema_validator.py` - deferred (template may be standalone)
- [ ] Remove old `scripts/validate_all.py` (if exists) - deferred (has HTML report feature)
- [ ] Remove schemas from `docs/PBN-template-repo/` subdirectories - deferred (template is self-contained)

### 6.2 Update documentation
- [x] Update any references to old script locations (none found)
- [x] Add usage documentation to `scripts/validation-format/README.md`

---

## Content Types Reference

| Content Type | Metadata File | Schema File | Content Files |
|--------------|---------------|-------------|---------------|
| courses | `course.yml` | `course-scheme.json` | `{lang}.md` |
| tutorials | `tutorial.yml` | `tutorial-scheme.json` | `{lang}.md` |
| professors | `professor.yml` | `professor-scheme.json` | `{lang}.md` |
| events | `event.yml` | `event-scheme.json` | - |
| resources/bet | `bet.yml` | `bet-scheme.json` | `{lang}.yml` |
| resources/books | `book.yml` | `book-scheme.json` | `{lang}.yml` |
| resources/channels | `channel.yml` | `channel-scheme.json` | - |
| resources/conferences | `conference.yml` | `conference-scheme.json` | - |
| resources/glossary | `word.yml` | `word-scheme.json` | - |
| resources/movies | `movie.yml` | `movie-scheme.json` | - |
| resources/newsletters | `newsletter.yml` | `newsletter-scheme.json` | - |
| resources/papers | `paper.yml` | `paper-scheme.json` | - |
| resources/podcasts | `podcast.yml` | `podcast-scheme.json` | - |
| resources/projects | `project.yml` | `project-scheme.json` | `{lang}.yml` |

---

## Usage (Target)

```bash
# Validate a single content folder
python scripts/validation-format/validate.py courses/btc101
python scripts/validation-format/validate.py tutorials/wallet/bitbox02
python scripts/validation-format/validate.py resources/papers/bitcoin-a-peer-to-peer-electronic-cash-system

# JSON output for CI/CD
python scripts/validation-format/validate.py courses/btc101 --json

# Validate all content
python scripts/validation-format/validate_all.py

# Validate only specific types
python scripts/validation-format/validate_all.py --courses-only
python scripts/validation-format/validate_all.py --resources-only
```

---

## Progress Tracking

**Status Legend**:
- [ ] Not started
- [x] Completed

**Current Phase**: Phase 6.2 Complete (documentation)

**Last Updated**: 2026-01-16 - Phase 1-5 completed, Phase 6.2 documentation complete (schemas centralized, paper schema added, validator with JSON output and exit codes, bulk validation wrapper, README.md)
