# Claude Code — Bitcoin Educational Content

> Read `docs/agents/AGENTS.md` for full repo orientation (content types, conventions, CLI reference).
> Load `content-types.yml` at repo root for machine-readable content type registry.

## Quick Start

```bash
# Activate bec CLI
source scripts/bec/.venv/bin/activate  # or: pip install -e scripts/bec

# Validate before committing
bec validate <path>           # Single item
bec validate --all --json     # Full repo, machine-readable

# Scaffold new content
bec new course --id btc201 --topic bitcoin --level intermediate --lang en --professor-id <uuid>
bec new tutorial --category wallet --id my-tuto --lang en

# Add structure to courses
bec add part --course btc101 --lang en --title "Part Title"
bec add chapter --course btc101 --lang en --title "Chapter Title"

# Reports
bec report --all --output docs/reports/
```

## Workflow

1. **Before editing**: Read the content's metadata YAML and understand its schema
2. **After editing**: Run `bec validate <path>` — exit code 0 means valid
3. **Before committing**: Run `bec validate --all` for full repo check
4. **Scaffolding**: Always use `bec new` — it generates UUIDs, correct structure, and proofreading metadata

## Rules

- All YAML metadata must conform to JSON schemas in `schemas/`
- Course IDs follow `{discipline_code}{level_number}` format (e.g., btc101)
- Images must be `.webp` format
- Do not manually create UUIDs — let `bec new` generate them
- Do not manually create chapter IDs — let `bec add chapter` generate BIP39 words
- Keep `content-types.yml` as single source of truth for valid types, categories, tags, languages
- Proofreading metadata is managed via `bec proofread` — do not edit manually

## Project Structure

```
content-types.yml          # Content type registry (load first)
schemas/                   # JSON Schema Draft 7 files (symlink)
courses/                   # Course content
tutorials/                 # Tutorial content (by category)
professors/                # Professor profiles
events/                    # Events
resources/                 # Books, podcasts, channels, etc.
scripts/bec/               # bec CLI package
docs/agents/               # Agent orientation files
docs/reports/              # Generated HTML reports
```

## Commit Convention

- `feat:` new content or features
- `fix:` corrections to existing content
- `chore:` maintenance, tooling updates
- `docs:` documentation changes
- Content commits: include content type and ID (e.g., `feat(btc101): add chapter 5`)
