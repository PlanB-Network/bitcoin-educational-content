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

## Phase 2: Create Paper Schema

### 2.1 Analyze paper structure
- [ ] Document all fields found in existing `paper.yml` files:
  - `title` (required, string)
  - `original_language` (required, string, ISO 639-1)
  - `authors` (required, array of strings)
  - `abstract` (required, string, multiline)
  - `publication_date` (optional, string, YYYY-MM-DD)
  - `paper_type` (required, enum: whitepaper, conference, academic)
  - `source` (required, string)
  - `type` (optional, enum: SCI, SCIE)
  - `category` (optional, string)
  - `topics` (required, array of strings)
  - `pdf_url` (required, string, URL format)
  - `id` (required, string, UUID format)

### 2.2 Create paper schema
- [ ] Create `scripts/validation-format/schemas/paper-scheme.json`
- [ ] Follow same JSON Schema format as other schemas (draft-07)
- [ ] Define required vs optional fields
- [ ] Add proper validation patterns (UUID, date, URL)

---

## Phase 3: Update Validator Script

### 3.1 Add paper support
- [ ] Add `resources/papers` to CONTENT_TYPES mapping
- [ ] Map to `paper.yml` and `paper-scheme.json`

### 3.2 Fix schema path resolution
- [ ] Update all schema path lookups to use `scripts/validation-format/schemas/`
- [ ] Ensure relative path resolution works from any working directory

### 3.3 Verify all content types work
- [ ] Test courses validation
- [ ] Test tutorials validation
- [ ] Test professors validation
- [ ] Test events validation
- [ ] Test resources/bet validation
- [ ] Test resources/books validation
- [ ] Test resources/channels validation
- [ ] Test resources/conferences validation
- [ ] Test resources/glossary validation
- [ ] Test resources/movies validation
- [ ] Test resources/newsletters validation
- [ ] Test resources/papers validation (new)
- [ ] Test resources/podcasts validation
- [ ] Test resources/projects validation

---

## Phase 4: Enhance Output Options

### 4.1 Add JSON output flag
- [ ] Add `--json` / `-j` flag for JSON output
- [ ] Structure JSON output with:
  - `path`: content path validated
  - `content_type`: detected type
  - `valid`: boolean
  - `errors`: array of error objects
  - `warnings`: array of warning objects

### 4.2 Add exit codes
- [ ] Exit code 0: validation passed
- [ ] Exit code 1: validation failed (errors)
- [ ] Exit code 2: validation passed with warnings

### 4.3 Keep terminal output as default
- [ ] Colored output for human readability
- [ ] Summary statistics at the end

---

## Phase 5: Create Validate-All Wrapper (Optional)

### 5.1 Create bulk validation script
- [ ] Create `scripts/validation-format/validate_all.py`
- [ ] Iterate over all content folders
- [ ] Call `validate.py` for each
- [ ] Aggregate results
- [ ] Support filtering by content type (`--courses-only`, `--tutorials-only`, `--resources-only`)

### 5.2 Generate reports
- [ ] Summary report in terminal
- [ ] Optional HTML report (`--html-report`)

---

## Phase 6: Cleanup

### 6.1 Remove old files
- [ ] Remove `docs/PBN-template-repo/scripts/schema_validator.py`
- [ ] Remove old `scripts/validate_all.py` (if exists)
- [ ] Remove schemas from `docs/PBN-template-repo/` subdirectories

### 6.2 Update documentation
- [ ] Update any references to old script locations
- [ ] Add usage documentation to `scripts/validation-format/README.md`

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

**Current Phase**: Phase 1 Complete

**Last Updated**: 2026-01-16 - Phase 1 completed (schemas centralized, validator updated)
