# PlanB Network Content Validator

A modular, centralized validation system for all content types in the repository.

## Quick Start

```bash
# Activate the virtual environment (required)
source .venv/bin/activate

# Validate a single content folder
python scripts/validation-format/validate.py courses/btc101
python scripts/validation-format/validate.py tutorials/wallet/sparrow-wallet
python scripts/validation-format/validate.py resources/papers/bitcoin-a-peer-to-peer-electronic-cash-system

# Validate all content folders
python scripts/validation-format/validate_all.py

# Validate specific content types
python scripts/validation-format/validate_all.py --courses-only
python scripts/validation-format/validate_all.py --tutorials-only
python scripts/validation-format/validate_all.py --resources-only
python scripts/validation-format/validate_all.py --type resources/papers
```

## Requirements

```bash
pip install jsonschema pyyaml python-frontmatter
```

## Scripts

### validate.py

Validates a single content folder against its JSON schema.

```bash
# Basic usage
python scripts/validation-format/validate.py <content-folder>

# JSON output for CI/CD
python scripts/validation-format/validate.py courses/btc101 --json
```

**Exit codes:**
- `0` - Validation passed
- `1` - Validation failed (errors found)
- `2` - Validation passed with warnings

### validate_all.py

Validates all content folders in the repository.

```bash
# Validate everything
python scripts/validation-format/validate_all.py

# Filter by content type
python scripts/validation-format/validate_all.py --courses-only
python scripts/validation-format/validate_all.py --tutorials-only
python scripts/validation-format/validate_all.py --professors-only
python scripts/validation-format/validate_all.py --events-only
python scripts/validation-format/validate_all.py --resources-only

# Validate a specific resource type
python scripts/validation-format/validate_all.py --type resources/papers
python scripts/validation-format/validate_all.py --type resources/books

# Output options
python scripts/validation-format/validate_all.py --json          # JSON output
python scripts/validation-format/validate_all.py --summary-only  # Hide individual errors
python scripts/validation-format/validate_all.py --verbose       # Show all results
```

## Supported Content Types

| Content Type | Metadata File | Schema File |
|--------------|---------------|-------------|
| courses | `course.yml` | `course-scheme.json` |
| tutorials | `tutorial.yml` | `tutorial-scheme.json` |
| professors | `professor.yml` | `professor-scheme.json` |
| events | `event.yml` | `event-scheme.json` |
| resources/bet | `bet.yml` | `bet-scheme.json` |
| resources/books | `book.yml` | `book-scheme.json` |
| resources/channels | `channel.yml` | `channel-scheme.json` |
| resources/conferences | `conference.yml` | `conference-scheme.json` |
| resources/glossary | `word.yml` | `word-scheme.json` |
| resources/movies | `movie.yml` | `movie-scheme.json` |
| resources/newsletters | `newsletter.yml` | `newsletter-scheme.json` |
| resources/papers | `paper.yml` | `paper-scheme.json` |
| resources/podcasts | `podcast.yml` | `podcast-scheme.json` |
| resources/projects | `project.yml` | `project-scheme.json` |

## Directory Structure

```
scripts/validation-format/
├── README.md           # This file
├── TODO.md             # Implementation progress
├── validate.py         # Single folder validator
├── validate_all.py     # Bulk validator
└── schemas/            # JSON Schema definitions
    ├── course-scheme.json
    ├── course-content-scheme.json
    ├── tutorial-scheme.json
    ├── tutorial-content-scheme.json
    ├── professor-scheme.json
    ├── professor-content-scheme.json
    ├── event-scheme.json
    ├── paper-scheme.json
    └── ... (other schemas)
```

## CI/CD Integration

Both scripts support JSON output and exit codes suitable for CI/CD pipelines:

```bash
# Run validation and check exit code
python scripts/validation-format/validate_all.py --json > results.json
if [ $? -eq 0 ]; then
    echo "All validations passed"
elif [ $? -eq 1 ]; then
    echo "Validation errors found"
else
    echo "Validation passed with warnings"
fi
```
