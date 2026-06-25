# BEC ↔ LMS Schema Alignment — 2026-06

> Supersedes the 2026-03-18 comparison: all mismatches have been resolved by
> rewriting the bec schemas. Policy: **LMS wins everywhere** (importer parsers >
> Zod > Drizzle). LMS reference: origin/dev @ 9fc35b345.

## Result

| Metric (2,677 items) | Before | After |
|---|---|---|
| Passing | 645 | 2,547 |
| With errors | 1,567 | 87 (all genuine content defects) |
| Warnings-only | 465 | 43 |
| bec tests | 405 | 444 |

## What changed

87 adversarially-verified schema edits across all 24 schemas: required
fields the importer treats as optional were relaxed, the tag vocabulary opened
(the importer lowercases and upserts any string — tags-definitions.json remains
as documentation), UUID patterns made version-generic, nullable unions added to
match nullable columns, importer-consumed fields documented (course
assignment/pricing fields, tutorial last_update_date/is_archived/test_only,
professor links/tips/contributor_id, conference id/original_language/
proofreading, event professor/course_related/exam type), and
word-content-scheme flattened to the standard layout (this alone fixed every
glossary markdown false-error).

Edit distribution: relax required 25, add field 22, remove constraint 12, type change 11, enum change 7, add required 5, allow additional properties 3, other 2.

44 confirmed CLI code findings were fixed in the same pass — most notably
chapter/part IDs are now UUIDs (the LMS uuidValidates them; the previous BIP39
scheme would have broken sync for scaffolded chapters).

The full interactive report (per-edit LMS evidence, verifier corrections,
remaining-error inventory) is generated from the audit data; see the PR
description for the hosted copy.

## Follow-ups

- Validate professor translation .yml files (traversal gap; ~2,451 files unchecked)
- Add a schema for assignment.yml (consumed by the LMS importer, unknown to bec)
- `bec lint` candidate: silent-drop link keys ('Github', 'nost', conference 'youtube')
- Fix courses/dev301 `testnet_only` → `test_only` typo (currently silently ignored)
- Content fixes for the 87 invalid items (dominated by unquoted-colon YAML in machine-translated quizzes)
