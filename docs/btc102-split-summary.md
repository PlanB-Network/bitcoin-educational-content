# BTC102 Split Project - Implementation Summary

**Project Status**: ✅ COMPLETE (All 7 courses implemented)
**Branch**: `split-btc102`
**Completion Date**: 2026-01-20

---

## Project Overview

The original BTC102 course ("Getting your first bitcoins" - 14 hours, 2,545 lines) has been split into 7 smaller, focused courses. This document provides a clean summary for the upcoming cleanup and PR phase.

---

## Courses Created

| # | Code | Name | Parts | Chapters | Quizzes | Images | Hours |
|---|------|------|-------|----------|---------|--------|-------|
| 1 | SCU102 | Financial Fraud, Scams & Online Security | 7 | 26 | 15 | 25 | 3 |
| 2 | BTC103 | Why Bitcoin Matters | 4 | 9 | 9 | 24 | 2 |
| 3 | BIZ102 | Bitcoin Industry Overview | 5 | 12 | 10 | 11 | 2 |
| 4 | BTC105 | How to Acquire Bitcoin | 6 | 18 | 9 | 4 | 2.5 |
| 5 | BTC104 | How to Secure Bitcoin | 5 | 14 | 3 | 3 | 2 |
| 6 | SOV102 | Bitcoin Inheritance Planning | 5 | 11 | 5 | 4 | 1.5 |
| 7 | BTC102v2 | Your First Bitcoin Journey (Hub) | 5 | 10 | 0 | 4 | 1 |

**Totals**: 37 Parts, 100 Chapters, 51 Quizzes, 75 Images, ~14 Hours

---

## Directory Structure

```
courses/
├── btc102/              # ORIGINAL - Keep intact until v2 validated
│
├── scu102-new/          # Course 1: Financial Fraud, Scams & Online Security
│   ├── course.yml
│   ├── en.md
│   ├── assets/en/       # 25 images (001-025.webp)
│   └── quizz/           # 15 quizzes (000-014)
│
├── btc103-new/          # Course 2: Why Bitcoin Matters
│   ├── course.yml
│   ├── en.md
│   ├── assets/en/       # 24 images (001-024.webp)
│   └── quizz/           # 9 quizzes (000-008)
│
├── biz102-new/          # Course 3: Bitcoin Industry Overview
│   ├── course.yml
│   ├── en.md
│   ├── assets/en/       # 11 images (001-011.webp)
│   └── quizz/           # 10 quizzes (000-009)
│
├── btc105/              # Course 4: How to Acquire Bitcoin
│   ├── course.yml
│   ├── en.md
│   ├── assets/en/       # 4 images (001-004.webp)
│   └── quizz/           # 9 quizzes (000-008)
│
├── btc104/              # Course 5: How to Secure Bitcoin
│   ├── course.yml
│   ├── en.md
│   ├── assets/en/       # 3 images (001-003.webp)
│   └── quizz/           # 3 quizzes (000-002)
│
├── sov102/              # Course 6: Bitcoin Inheritance Planning
│   ├── course.yml
│   ├── en.md
│   ├── assets/en/       # 4 images (001-004.webp)
│   └── quizz/           # 5 quizzes (000-004)
│
└── btc102v2/            # Course 7: Hub Course
    ├── course.yml
    ├── en.md
    ├── assets/en/       # 4 images (001-004.webp)
    └── quizz/           # (empty - no quizzes)
```

---

## Course UUIDs

| Course | UUID |
|--------|------|
| SCU102 | (check course.yml) |
| BTC103 | (check course.yml) |
| BIZ102 | (check course.yml) |
| BTC105 | (check course.yml) |
| BTC104 | (check course.yml) |
| SOV102 | 455676ad-2a81-48f4-b141-5257b9652c61 |
| BTC102v2 | d493c2bb-c0d0-4d77-9a68-c9ee5631c8ba |

---

## Content Origin Mapping

### Source: BTC102 en.md

| Lines | Content | Target Course |
|-------|---------|---------------|
| 23-74 | Course overview | BTC102v2 |
| 75-549 | Part 1: Scams, Security, Tips | SCU102 |
| 554-841 | Part 2a: Bitcoin in 5 min, Why Bitcoin | BTC103 |
| 844-1194 | Part 2b: Industry, Layered Architecture | BIZ102 |
| 1195-2191 | Part 3: Setting up your plan | BTC105 + BTC104 |
| 2192-2420 | Part 4: Inheritance | SOV102 |

### Quiz Distribution

| BTC102 Quizzes | Target Course |
|----------------|---------------|
| 000-014 | SCU102 |
| 015-023 | BTC103 |
| 025-034 | BIZ102 |
| 035-036, 039-042, 045-049, 050-052, 055-056 | BTC105 |
| 037, 045, 047 | BTC104 |
| 060-064 | SOV102 |

### Image Distribution

| BTC102 Images | Target Course |
|---------------|---------------|
| 001-004 | BTC102v2 |
| 005-029 | SCU102 (→ 001-025) |
| 030-053 | BTC103 (→ 001-024) |
| 054-064 | BIZ102 (→ 001-011) |
| 065-069 | BTC105 (→ 001-004) |
| 070-072 | BTC104 (→ 001-003) |
| 097-100 | SOV102 (→ 001-004) |

---

## Implementation Documentation

Individual implementation docs in `docs/`:

| Document | Course |
|----------|--------|
| scu102-creation.md | SCU102 |
| btc103-creation.md | BTC103 |
| biz102-creation.md | BIZ102 |
| btc105-creation.md | BTC105 |
| btc104-creation.md | BTC104 |
| sov102-creation.md | SOV102 |
| btc102v2-creation.md | BTC102v2 |
| btc102-split-plan.md | Master Plan |

---

## Content Tagging Convention

All content in the new courses is tagged:

```markdown
<!-- ORIGINAL: btc102/en.md lines XXX-YYY -->
[Original content here]
<!-- END ORIGINAL -->

<!-- NEW -->
[Newly written content here]
<!-- END NEW -->
```

This enables:
- Clear tracking of content origin
- Future automated translation bootstrapping
- Identifying what needs fresh translation vs reuse

---

## Standard Course Structure

Every course follows this structure:

```markdown
---
name: [Course Title]
goal: [One-sentence goal]
objectives:
  - [Objective 1]
  - [Objective 2]
---

# Part Name
<partId>[unique-part-id]</partId>

## Chapter Name
<chapterId>[unique-chapter-id]</chapterId>

[Content]

# Conclusion
<partId>conclusion-[course]</partId>

## Conclusion
<chapterId>conclusion-ch##</chapterId>
<isCourseConclusion>true</isCourseConclusion>
```

---

## Phase 4: Cleanup Checklist

### Validation Tasks
- [ ] Verify all course.yml files have required fields
- [ ] Verify all en.md files have proper frontmatter
- [ ] Verify all partId and chapterId tags are unique
- [ ] Verify all image references are correct
- [ ] Verify all quiz chapterIds match actual chapters
- [ ] Verify all courses end with `<isCourseConclusion>true</isCourseConclusion>`

### Naming Consistency
- [ ] Decide: Keep `-new` suffix or rename folders?
  - `scu102-new` → `scu102`?
  - `btc103-new` → `btc103`?
  - `biz102-new` → `biz102`?

### PR Preparation
- [ ] Review all changes in `split-btc102` branch
- [ ] Write PR description with summary
- [ ] List all new courses and their purposes
- [ ] Note that original BTC102 is preserved

### Post-Merge Tasks
- [ ] Bootstrap translations using content mappings
- [ ] Update any external references to BTC102
- [ ] Consider deprecation strategy for original BTC102

---

## Key Design Decisions

| Decision | Outcome | Rationale |
|----------|---------|-----------|
| SCU103 merged into SCU102 | Single comprehensive security course | Avoid fragmentation |
| BTC105/BTC104 separation | Acquisition vs Security as separate courses | Different user needs |
| Method-based BTC105 | Focus on acquisition methods, not profiles | More practical approach |
| Beginner-focused BTC104 | Simple wallet setup, advanced topics as placeholders | Avoid overwhelming beginners |
| Hub course (BTC102v2) | Navigation guide, not content duplication | Clear learning paths |
| No quizzes in hub | Quizzes belong in content courses | Hub is for navigation only |

---

## Notes for Cleanup Phase

1. **Original BTC102**: Keep intact until BTC102v2 is fully validated and translations are bootstrapped

2. **Folder Naming**: Some courses have `-new` suffix (scu102-new, btc103-new, biz102-new) while others don't. Decide on consistency.

3. **Translation Strategy**: Content mappings (ORIGINAL tags with line numbers) enable automated extraction of existing translations from btc102 language files.

4. **Cross-References**: BTC102v2 contains links to all other courses. If URLs change, update BTC102v2.

5. **Quiz Overlap**: Some quizzes (like 045, 047) are used in multiple courses. This is intentional - same question, different context.

---

*This summary document created for Phase 4 cleanup preparation.*
