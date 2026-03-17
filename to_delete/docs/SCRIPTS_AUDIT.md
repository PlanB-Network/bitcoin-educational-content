# Scripts Audit Report

**Date**: 2026-03-17
**Audited by**: 4 parallel agents covering all scripts/ contents
**Purpose**: Decide keep/refactor/delete for every script, prepare sub-issues for refactor

---

## Executive Summary

- **Total items audited**: 13 top-level scripts + 19 subdirectories
- **DELETE**: 11 items (empty dirs, one-offs, obsolete)
- **KEEP**: 14 items (good or need minor polish only)
- **REFACTOR**: 8 items (need CLI interface, path fixes, or modernization)
- **Key finding**: 2 duplicate `validate.py`/`validate_all.py` (top-level are older, `validation-format/` are current)
- **Key finding**: 3 empty directories, 3 one-off scripts with hardcoded external paths
- **Key finding**: PDF tools fragmented across 4 directories

---

## DELETE (11 items)

### Empty / Orphaned Directories
| Item | Why |
|------|-----|
| `content_to_pdf/` | Empty directory, no files |
| `update_course_info/` | Empty directory, no files |
| `fix_italic_typos/` | Only contains .env and venv, no source code |
| `wikimedia-commons/` | Empty placeholder |

### One-Off Scripts (already ran, job done)
| Item | Why |
|------|-----|
| `extract-language-specific-content.py` | Hardcoded paths to external `sovereign-university-data/` and `LLM-Translator/` repos |
| `relocate_contributors_builders.py` | One-time migration of contributor metadata between files |
| `rename-translated-content.py` | One-time rename for LLM-Translator output |
| `fix-symbols/` | Ran 2025-09-15, corrected 424 files / 17,828 fixes. Job complete. |

### Obsolete / Superseded
| Item | Why |
|------|-----|
| `convert-to-webp-py/` | Author's README says "use my GUI tool instead" (links to external repo) |
| `course-update-tool/` | Ghost directory — has venv and modules but no entry point, no README. Duplicates `auto-translate/` structure |
| Top-level `validate.py` | Older version, superseded by `validation-format/validate.py` |

**Note**: Top-level `validate_all.py` generates HTML reports which `validation-format/validate_all.py` also does. Check if any unique features remain before deleting.

---

## KEEP (14 items)

### Production-Ready (no changes needed)
| Item | CLI? | Purpose |
|------|------|---------|
| `validation-format/` | argparse, --json, exit codes | Schema validation for all 14 content types |
| `quizz_to_pdfs/` | argparse, batch wrapper | Quiz YAML to PDF with multilingual fonts |
| `uuids-check/` | argparse, --dry-run, --verbose | UUID v4 validation and replacement across repo |
| `demote_headings.py` | --dry-run, --verbose | Demote markdown heading levels |
| `reports/` | N/A (output dir) | Central storage for HTML reports |
| `pdf_courses/` | N/A (artifact dir) | Storage for generated PDFs |

### Keep with Minor Polish
| Item | CLI? | Polish needed |
|------|------|---------------|
| `image_translation_overview/` | Runs standalone | Add --output arg |
| `md_translation_overview/` | Runs standalone | Add --output arg |
| `video_deployment_overview/` | Runs standalone | Add --output arg, add to requirements.txt |
| `proofreading_report/` | Runs standalone | Add --output arg |
| `course_report/` | Runs standalone | Add argparse for output path, language filter |
| `rename_image/` | Interactive menu | Fix hardcoded path at line 67 |
| `add_tuto_title_to_glossary_translation/` | Interactive | Fix hardcoded paths |
| `tutorial-related/data-creator/` | GUI (CustomTkinter) | Keep as-is; consider companion CLI later |

---

## REFACTOR (8 items)

### Need CLI Interface (argparse + --help)

#### `auto-translate/`
- **Current state**: Batch scripts with no argparse, minimal docs, .env and nohup.out remnants
- **What it does**: Orchestrates LLM-Translator for batch content translation
- **Refactor scope**: Add argparse to `translation_controller.py` and batch scripts; expand README; clean up artifacts
- **Priority**: HIGH (core workflow)

#### `proofreading-metadata/`
- **Current state**: Pure `inquirer` interactive prompts, no batch mode
- **What it does**: Manage proofreading entries, calculate rewards, bulk add contributors
- **Refactor scope**: Add `--batch` mode with argparse alongside interactive mode; add `--dry-run`
- **Priority**: HIGH (regular use)

#### `course-related/`
- **Current state**: Interactive selection menus, no argparse
- **What it does**: add_uuid.py, plan.py, quizz.py, update-all-courses-hours.py
- **Refactor scope**: Add argparse `--file`, `--course`, `--output` options to each script
- **Priority**: MEDIUM

#### `book-uniformizer.py`
- **Current state**: No CLI args, hardcoded to `../resources/books/` and `["fr", "en"]` languages
- **What it does**: Standardize book.yaml formatting
- **Refactor scope**: Add argparse for target dir, languages, --dry-run
- **Priority**: LOW

#### `course-to-pdf.py`
- **Current state**: Interactive menu, no argparse. Requires chromium/wkhtmltopdf
- **What it does**: Convert course markdown to styled PDF
- **Refactor scope**: Replace menu with `python course-to-pdf.py BTC101 [--all] [--output-dir]`
- **Priority**: MEDIUM

#### `fix_project_descriptions.py`
- **Current state**: No CLI args, hardcoded to `resources/projects/`
- **What it does**: Reformat multi-line YAML descriptions to single-line
- **Refactor scope**: Add argparse for target dir, --dry-run, --verbose
- **Priority**: LOW

#### `generate_all_reports.py`
- **Current state**: No args, runs all 3 reports unconditionally
- **What it does**: Orchestrate report generation
- **Refactor scope**: Add `--video-only`, `--image-only`, `--md-only`, `--output`
- **Priority**: LOW (works fine, just inflexible)


---

## Duplicate / Overlap Analysis

### PDF Generation (4 items → should be 1-2)
| Tool | Input | Output | CLI? | Status |
|------|-------|--------|------|--------|
| `quizz_to_pdfs/` | Quiz YAML | Quiz PDFs | YES | KEEP |
| `course-to-pdf.py` | Course MD | Course PDFs | No (menu) | REFACTOR |
| `convert-to-pdf/` | Any MD | Generic PDFs | No (inquirer) | DELETE or MERGE |
| `content_to_pdf/` | — | — | — | DELETE (empty) |

**Recommendation**: Keep `quizz_to_pdfs/` and `course-to-pdf.py` (different inputs). Delete `convert-to-pdf/` (superseded). Delete `content_to_pdf/` (empty).

### Validation (2 items → should be 1)
| Tool | Location | CLI? | Status |
|------|----------|------|--------|
| `validation-format/validate.py` | `scripts/validation-format/` | YES | KEEP (current) |
| `validate.py` | `scripts/` (top-level) | No | DELETE (older version) |

**Recommendation**: Delete top-level `validate.py` and `validate_all.py`. The `validation-format/` versions are strictly better.

### Image Conversion (2 items → should be 0-1)
| Tool | Status |
|------|--------|
| `convert-to-webp-py/` | Author says "use my GUI tool instead" |
| `webp-batch-conversion.py` | Hardcoded to single directory |

**Recommendation**: Delete both. If WebP conversion needed, add as `make convert-webp path=...` using a simple Pillow one-liner.

---

## Proposed scripts/ Directory After Cleanup

```
scripts/
  validation-format/         # KEEP - schema validation (core)
  │   validate.py
  │   validate_all.py
  │   schemas/               # 23 JSON schemas
  │   README.md
  │
  auto-translate/            # REFACTOR - batch translation
  proofreading-metadata/     # REFACTOR - proofreading management
  proofreading_report/       # KEEP - dashboard generation
  course-related/            # REFACTOR - course authoring utils
  course-report/             # KEEP - course analytics
  quizz_to_pdfs/             # KEEP - quiz PDF generation
  tutorial-related/          # KEEP - GUI data creator
  rename_image/              # KEEP - image renaming utility
  add_tuto_title_to_glossary_translation/  # KEEP - glossary tool
  uuids-check/               # KEEP - UUID validation
  image_translation_overview/ # KEEP - report generator
  md_translation_overview/    # KEEP - report generator
  video_deployment_overview/  # KEEP - report generator
  reports/                   # KEEP - report output directory
  pdf_courses/               # KEEP - PDF output directory
  │
  # Top-level scripts (kept)
  demote_headings.py
  generate_all_reports.py     # REFACTOR
  course-to-pdf.py            # REFACTOR
  book-uniformizer.py         # REFACTOR
  fix_project_descriptions.py # REFACTOR
  translation_builders.py     # REFACTOR
```

**Deleted** (11 items):
- `extract-language-specific-content.py`
- `relocate_contributors_builders.py`
- `rename-translated-content.py`
- `validate.py` (top-level, older version)
- `validate_all.py` (top-level, older version)
- `webp-batch-conversion.py`
- `get-planb-tags.py`
- `content_to_pdf/`
- `convert-to-pdf/`
- `convert-to-webp-py/`
- `course-update-tool/`
- `fix_italic_typos/`
- `fix-symbols/`
- `update_course_info/`
- `wikimedia-commons/`

---

## GitHub Sub-Issues (Scripts)

Each of these becomes a separate GitHub issue:

1. **[CLEANUP] Delete obsolete and one-off scripts** — Remove 15 items listed in DELETE section
2. **[REFACTOR] Add CLI interface to auto-translate/** — argparse, --help, batch mode
3. **[REFACTOR] Add CLI interface to proofreading-metadata/** — batch mode alongside interactive
4. **[REFACTOR] Add CLI interface to course-related/** — argparse for each script
5. **[REFACTOR] CLI-ify top-level scripts** — book-uniformizer, course-to-pdf, fix_project_descriptions, generate_all_reports, translation_builders
6. **[REFACTOR] Consolidate duplicate validation scripts** — Delete top-level validate.py/validate_all.py
7. **[REFACTOR] Consolidate PDF tools** — Delete convert-to-pdf/, keep quizz_to_pdfs + course-to-pdf
8. **[POLISH] Add --output args to report generators** — image_translation, md_translation, video_deployment, proofreading_report, course_report
9. **[POLISH] Fix hardcoded paths** — rename_image/, add_tuto_title_to_glossary_translation/
