# Agent-Friendliness Refactor Plan

**Date**: 2026-03-17
**Status**: Agreed — pending implementation
**Branch**: TBD (will be created from `dev`)

---

## Problem Statement

This content repo has solid infrastructure (23 JSON schemas, validation scripts, translation pipeline) but it's poorly **discoverable** for AI agents. An agent entering the repo has no orientation, no CLI entry point, and must crawl to understand the data model. Documentation is stale, scattered, and human-only.

## Goals

1. Any AI agent can orient itself in < 30 seconds
2. All operations are discoverable via `make help`
3. Content creation is guided by CLI scaffolding, not documentation
4. Schema validation is a one-command operation
5. The repo root stays clean — no AI config file pollution

## Non-Goals

- Changing any content (courses, tutorials, resources, etc.)
- Rewriting the validation engine
- Changing the translation pipeline
- Adding new content types

---

## Architecture Decisions

### ADR-1: Agent config files live in `docs/agents/`, not at root

**Decision**: `AGENTS.md` and `CLAUDE.md` are canonical in `docs/agents/`. A `make agent-setup` command symlinks them to root. Root-level symlinks are gitignored.

**Why**: Keep the repo clean. These files are tooling, not content. Contributors who don't use AI agents never see them. Agents that need them run one command.

**Structure**:
```
docs/agents/
  AGENTS.md        # Cross-agent standard (Cursor, Windsurf, Copilot, Claude, etc.)
  CLAUDE.md        # Claude Code-specific (imports AGENTS.md + Claude config)
.gitignore         # /AGENTS.md, /CLAUDE.md at root level
Makefile           # agent-setup target creates symlinks
README.md          # "AI Agent Usage" section with make agent-setup
```

### ADR-2: Makefile as universal CLI entry point

**Decision**: A `Makefile` at repo root wraps all operations. `make help` lists everything.

**Why**: Every agent, IDE, and CI system knows `make`. It's self-documenting. It replaces the need for agents to discover scattered scripts. Zero dependencies (pre-installed on Unix).

**Targets** (planned):
```makefile
help                # List all available commands
validate            # Validate all content
validate-courses    # Validate courses only
validate-tutorials  # Validate tutorials only
validate-resources  # Validate resources only
validate-one        # Validate single folder: make validate-one path=courses/btc101
lint                # Format with prettier
report              # Generate all reports
new-course          # Scaffold new course (interactive)
new-tutorial        # Scaffold new tutorial (interactive)
new-professor       # Scaffold new professor (interactive)
new-event           # Scaffold new event (interactive)
agent-setup         # Symlink AGENTS.md/CLAUDE.md to root
```

### ADR-3: `content-types.yml` as single source of truth

**Decision**: A `content-types.yml` at repo root maps every content type to its path pattern, metadata file, schema, and example.

**Why**: Currently the mapping is implicit — hardcoded in the validator Python code. Agents can't discover it without reading source. This file becomes the machine-readable registry that both agents AND scripts consume.

**Example structure**:
```yaml
content_types:
  courses:
    path_pattern: "courses/{id}"
    metadata_file: "course.yml"
    schema: "schemas/course-scheme.json"
    content_schema: "schemas/course-content-scheme.json"
    content_files: "{lang}.md"
    assets: "assets/{lang}/, assets/thumbnail.webp"
    example: "courses/btc101"

  tutorials:
    path_pattern: "tutorials/{category}/{id}"
    metadata_file: "tutorial.yml"
    schema: "schemas/tutorial-scheme.json"
    content_schema: "schemas/tutorial-content-scheme.json"
    content_files: "{lang}.md"
    assets: "assets/cover.webp, assets/{lang}/"
    example: "tutorials/wallet/sparrow-wallet"
    categories:
      - wallet
      - node
      - mining
      - exchange
      - privacy
      - business
      - computer-security
      - contribution

  # ... all 14 content types
```

### ADR-4: CLI scaffolding replaces template repo

**Decision**: Delete `docs/PBN-template-repo/`. Replace with `make new-*` commands that generate valid content folders interactively.

**Why**: The repo itself has 50+ courses and 100+ tutorials — it IS the template. A separate template repo is duplication that drifts. CLI scaffolding reads from JSON schemas to generate valid YAML, so it's always in sync.

**Implementation**: Python script(s) in `scripts/` that:
- Read `content-types.yml` for structure
- Read JSON schemas for required fields and enums
- Prompt interactively for values
- Generate folder + files
- Run validation on output

### ADR-5: `schemas/` symlink at repo root

**Decision**: Create a symlink `schemas/ -> scripts/validation-format/schemas/` at repo root.

**Why**: Schemas are referenced everywhere (content-types.yml, AGENTS.md, Makefile). Having them at top level makes them discoverable without knowing the internal script layout.

### ADR-6: Clean up `docs/` directory

**Decision**: Most of `docs/` is either data-pretending-to-be-docs or stale prose. Clean it up.

| File | Action | Destination |
|------|--------|-------------|
| `PBN-template-repo/` | DELETE | Replaced by CLI scaffolding (ADR-4) |
| `reports/` | KEEP | Generated reports, not docs |
| `README.md` | DELETE | Stale, replaced by AGENTS.md |
| `50-planb-tags.md` | TRANSFORM | Machine-readable YAML, referenced by schemas |
| `course_ID_rules.md` | TRANSFORM | Machine-readable YAML, part of content-types.yml |
| `tutorial-categories.md` | DELETE | Already in schema enum, redundant |
| `course_documentation.md` | ABSORB | Formatting rules go into AGENTS.md |
| `planb-uid.md` | ABSORB | Context section of AGENTS.md |
| `value-4-value-model.md` | ABSORB | Context section of AGENTS.md |
| `how-to-translate-image.md` | KEEP | Specific workflow, still useful |
| `tutorial-creation-guidelines.md` | DELETE | Stale, replaced by CLI scaffolding |
| `assets/` | CHECK | May contain referenced images |

### ADR-7: No breadcrumb/index files in directories

**Decision**: Don't add `.index.md` files in content directories.

**Why**: `AGENTS.md` + `content-types.yml` + `make help` cover all navigation needs. Adding index files in every directory is more maintenance surface for marginal benefit.

### ADR-8: Scripts cleanup

**Decision**: Audit all scripts. Keep useful ones, delete one-off fixes, ensure all kept scripts have CLI interface (argparse, --help, proper args).

**Criteria**:
- **KEEP**: Ongoing utility, used regularly
- **REFACTOR**: Useful but needs CLI interface, error handling
- **DELETE**: One-off fix that was run once, or superseded
- **MERGE**: Multiple scripts doing similar things (especially PDF tools)

Audit results: see [SCRIPTS_AUDIT.md](./SCRIPTS_AUDIT.md) — **completed 2026-03-17**.

Summary: 15 items to DELETE, 14 to KEEP, 8 to REFACTOR. See audit for full details.

---

## Implementation Order

1. `content-types.yml` — foundation, everything references it
2. `Makefile` — CLI entry point, wraps existing scripts first
3. `schemas/` symlink — surface schemas at top level
4. `docs/agents/AGENTS.md` + `CLAUDE.md` — agent orientation
5. Scripts cleanup — delete/refactor per audit results
6. CLI scaffolding (`make new-*`) — replaces template repo
7. `docs/` cleanup — delete stale files, transform data files
8. `.gitignore` + `README.md` update — final polish
9. GitHub issues — main issue + sub-issues for each item

---

## Open Questions

- [ ] Should `content-types.yml` also include the tag list (currently in `docs/50-planb-tags.md`)?
- [ ] Should discipline codes (BTC, BIZ, etc.) be in `content-types.yml` or separate?
- [ ] Do we need a `requirements.txt` or `pyproject.toml` for script dependencies?
- [ ] Should the Makefile auto-activate `.venv`?
