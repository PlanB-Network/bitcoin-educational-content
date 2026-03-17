# Bitcoin Educational Content — Agent Orientation

> Open-source Bitcoin education platform. 14 content types, 31 languages, ~2,600 content items.
> Machine-readable registry: `content-types.yml` (at repo root). Always load it first.

## Content Types (from content-types.yml)

| Type | Path Pattern | Metadata | Has Markdown |
|------|-------------|----------|--------------|
| course | `courses/{id}/` | `course.yml` | `{lang}.md` |
| tutorial | `tutorials/{category}/{id}/` | `tutorial.yml` | `{lang}.md` |
| professor | `professors/{id}/` | `professor.yml` | — (YML content) |
| event | `events/{id}/` | `event.yml` | — |
| bet | `resources/bet/{id}/` | `bet.yml` | — (YML content) |
| book | `resources/books/{id}/` | `book.yml` | — (YML content) |
| channel | `resources/channels/{id}/` | `channel.yml` | — |
| conference | `resources/conferences/{id}/` | `conference.yml` | — |
| glossary | `resources/glossary/{id}/` | `word.yml` | `{lang}.md` |
| movie | `resources/movies/{id}/` | `movie.yml` | — |
| newsletter | `resources/newsletters/{id}/` | `newsletter.yml` | — |
| podcast | `resources/podcasts/{id}/` | `podcast.yml` | — |
| project | `resources/projects/{id}/` | `project.yml` | — (YML content) |
| paper | `resources/papers/{id}/` | `paper.yml` | — |

## bec CLI

Installed: `pip install -e scripts/bec`. All commands support `--json` output.

```
bec validate <path>              # Validate single content item
bec validate --all               # Validate entire repo (--courses-only, --tutorials-only, --type <t>)
bec validate --all --json        # Machine-readable validation output
bec new course --id btc201 ...   # Scaffold new course
bec new tutorial --category wallet --id my-tuto --lang en
bec new professor --id username
bec new event --id event-2025
bec new resource --type book --id book-name
bec add part --course btc101 --lang en --title "Part Title"
bec add chapter --course btc101 --lang en --title "Chapter Title"
bec add quiz --course btc101 --chapter-id <id>
bec add language --path courses/btc101 --lang fr
bec proofread update --path courses/btc101 --lang fr --contributor user
bec proofread reward --path courses/btc101
bec proofread status --path courses/btc101
bec report translation|images|video|proofreading|analytics
bec report --all --output docs/reports/
bec agent-setup                  # Symlink orientation files to repo root
```

Exit codes: 0 = success, 1 = error, 2 = warning-only.
Omit required args → interactive prompts with enum choices.

## Content Conventions

### Course IDs
Format: `{discipline}{number}` — 3-letter discipline code + 3-digit number.
Discipline codes: btc, biz, csv, cyp, dev, eco, ene, his, lnp, min, net, phi, pos, pro, scu, sid, soc.
Number ranges: 101–199 beginner, 200–299 intermediate, 300–399 advanced, 400–499 expert.
Example: `btc101`, `lnp201`, `min301`.

### Course Markdown Structure
```markdown
---
name: Course Name
goal: One-line goal
objectives:
  - Objective 1
---
+++

# Part Title

<partId>uuid-here</partId>

## Chapter Title

<chapterId>three-bip39-words</chapterId>

Content here...
```

- Parts: `+++` separator, then `# heading`, then `<partId>uuid</partId>`
- Chapters: `## heading`, then `<chapterId>three-bip39-words</chapterId>`
- Chapter IDs: 3 hyphenated BIP39 words (e.g., `father-loop-frog`)
- Quizzes: `courses/{id}/quizz/{nnn}/question.yml` + `{lang}.yml`

### Tutorial Categories
business, computer-security, contribution, exchange, mining, node, privacy, wallet.

### Images
- Location: `assets/` within content folder
- Translated images: `assets/{lang}/` subfolder
- Language-neutral: `assets/no-txt/` subfolder
- Format: WebP only (`.webp`)
- Thumbnails: `assets/thumbnail.webp`

### Languages
31 supported codes. See `content-types.yml → languages` for full list.
Language-specific files: `{lang}.md` (markdown) or `{lang}.yml` (YAML content).

### Proofreading
Tracked in metadata YAML under `proofreading:` key. Each language entry has:
`last_contribution_date`, `urgpiority` (0–5), `contributors_id` (list), `reward` (calculated).

## Validation

JSON Schema Draft 7 files in `schemas/` (symlink to `scripts/validation-format/schemas/`).
Always run `bec validate <path>` after modifying content. Run `bec validate --all` for full repo check.

## Common Pitfalls

- YAML dates: Must stay as strings, not Python datetime objects
- Course markdown: Frontmatter must have `name`, `goal`, `objectives`
- Tags: Must be from the 52 valid tags in `content-types.yml`
- Image format: Only `.webp` — other formats will fail validation
- Quiz numbering: Zero-padded 3-digit folders (001, 002, ...)
- Part/chapter order: Parts are `#`, chapters are `##` — never skip levels
