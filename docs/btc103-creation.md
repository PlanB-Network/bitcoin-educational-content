# BTC103 - Why Bitcoin Matters: Creation Plan

## Overview

| Field | Value |
|-------|-------|
| **Course Code** | BTC103 |
| **Course Name** | Why Bitcoin Matters |
| **Source** | BTC102 chapters 3.1 + 3.2 (lines 554-842) |
| **Duration** | ~2 hours |
| **Level** | Beginner |
| **Status** | COMPLETED |

---

## Source Content (from BTC102)

### Chapter 3.1: Bitcoin in 5 minutes (lines 554-701)

| Subsection | Lines | Images |
|------------|-------|--------|
| The Origins: Cypherpunks & post-2008 crisis | 564-604 | 030, 031, 032, 033 |
| A decentralized network to transfer value | 605-622 | 034, 035, 036 |
| The Role of Miners and Proof-of-Work | 623-636 | 037 |
| Bitcoin Monetary Properties | 637-653 | 038 |
| Openness and Transparency | 654-672 | 039 |
| Use cases | 673-695 | 040 |

### Chapter 3.2: Why is Bitcoin important? (lines 702-842)

| Subsection | Lines | Images |
|------------|-------|--------|
| A universal currency | 710-728 | 041, 042 |
| Protection against currency crises | 730-752 | 043, 044, 045, 046 |
| A response to state control and injustice | 754-776 | 047, 048 |
| A Solution to Monetary and Banking Corruption | 778-814 | 049, 050 |
| Bitcoin: A Political Movement? | 816-841 | 051, 052, 053 |

---

## Target Structure

```
# Part 1: Introduction
└── Chapter 1: Welcome to BTC103 [NEW]

# Part 2: Bitcoin in 5 Minutes
├── Chapter 2: The Origins [ORIGINAL: 564-604]
├── Chapter 3: A Decentralized Network [ORIGINAL: 605-636]
├── Chapter 4: Monetary Properties & Transparency [ORIGINAL: 637-672]
└── Chapter 5: Use Cases [ORIGINAL: 673-695]

# Part 3: Why Bitcoin Matters
├── Chapter 6: A Universal Currency [ORIGINAL: 710-728]
├── Chapter 7: Protection Against Crises [ORIGINAL: 730-776]
└── Chapter 8: Sound Money & Political Movement [ORIGINAL: 778-841]

# Part 4: Conclusion
└── Chapter 9: Conclusion [STANDARD]
```

**Total: 4 Parts, 9 Chapters**

---

## Assets to Copy

**Images**: BTC102 030-053 → BTC103 001-024

| BTC102 | BTC103 | Topic |
|--------|--------|-------|
| 030 | 001 | Cypherpunks |
| 031 | 002 | Cypherpunk manifesto |
| 032 | 003 | Genesis block |
| 033 | 004 | Times headline |
| 034 | 005 | P2P network |
| 035 | 006 | Blockchain visual |
| 036 | 007 | Ledger concept |
| 037 | 008 | Halving chart |
| 038 | 009 | Satoshis divisibility |
| 039 | 010 | Open source |
| 040 | 011 | Bitcoin future |
| 041 | 012 | Universal currency |
| 042 | 013 | Inclusion vs liberation |
| 043 | 014 | Monetary crisis |
| 044 | 015 | Hyperinflation |
| 045 | 016 | Devaluation |
| 046 | 017 | Hanke study |
| 047 | 018 | Inequality |
| 048 | 019 | Sovereignty |
| 049 | 020 | Central banks |
| 050 | 021 | Gold standard |
| 051 | 022 | Bitcoiners |
| 052 | 023 | Censorship resistance |
| 053 | 024 | Financial sovereignty |

---

## Quizzes to Copy

BTC102 quizzes with matching chapterIds:

| BTC102 Quiz | BTC103 Quiz | Question Topic |
|-------------|-------------|----------------|
| 015-019 | 000-004 | Bitcoin in 5 min (chapterId: ae122ad9) |
| 020-023 | 005-008 | Why Bitcoin matters (chapterId: d4327ac4) |

---

## Files to Create

```
courses/btc103-new/
├── course.yml
├── en.md
├── assets/
│   └── en/
│       └── 001-024.webp (copy from btc102 030-053)
└── quizz/
    └── 000-008/ (copy from btc102 015-023)
```

---

## course.yml Template

```yaml
id: [GENERATE-UUID]

topic: economy
subtopic: bitcoin-importance
type: theory
level: beginner
hours: 2
teaching_format: self_paced

professors_id:
  - 2e1b5182-567e-453a-af29-36009340ff02
contributor_names:
  - Plan B Network

original_language: en
proofreading:
  - language: en
    last_contribution_date:
    urgency: 1
    contributor_names:
    reward: 0

tags:
  - bitcoin
  - economics
  - sound-money
  - financial-freedom
```

---

## en.md Template

```markdown
---
name: Why Bitcoin Matters
goal: Understand what Bitcoin is and why it represents a revolutionary alternative to traditional monetary systems.
objectives:
  - Understand Bitcoin's origins and core technical concepts
  - Recognize Bitcoin's unique monetary properties
  - Understand why Bitcoin matters for financial freedom
  - Grasp Bitcoin's role as protection against monetary crises
---

<!-- NEW -->
# Introduction

<partId>[GENERATE-UUID]</partId>

## Welcome to BTC103

<chapterId>[GENERATE-UUID]</chapterId>

[Write intro: what you'll learn, prerequisites (BTC101), why this matters]

<!-- END NEW -->

# Bitcoin in 5 Minutes

<partId>[GENERATE-UUID]</partId>

## The Origins

<chapterId>[GENERATE-UUID]</chapterId>

<!-- ORIGINAL: btc102/en.md lines 564-604 -->
[Copy content, update image refs: 030→001, 031→002, 032→003, 033→004]
<!-- END ORIGINAL -->

## A Decentralized Network

<chapterId>[GENERATE-UUID]</chapterId>

<!-- ORIGINAL: btc102/en.md lines 605-636 -->
[Copy content, update image refs: 034→005, 035→006, 036→007, 037→008]
<!-- END ORIGINAL -->

## Monetary Properties & Transparency

<chapterId>[GENERATE-UUID]</chapterId>

<!-- ORIGINAL: btc102/en.md lines 637-672 -->
[Copy content, update image refs: 038→009, 039→010]
<!-- END ORIGINAL -->

## Use Cases

<chapterId>[GENERATE-UUID]</chapterId>

<!-- ORIGINAL: btc102/en.md lines 673-695 -->
[Copy content, update image refs: 040→011]
<!-- END ORIGINAL -->

# Why Bitcoin Matters

<partId>[GENERATE-UUID]</partId>

## A Universal Currency

<chapterId>[GENERATE-UUID]</chapterId>

<!-- ORIGINAL: btc102/en.md lines 710-728 -->
[Copy content, update image refs: 041→012, 042→013]
<!-- END ORIGINAL -->

## Protection Against Crises

<chapterId>[GENERATE-UUID]</chapterId>

<!-- ORIGINAL: btc102/en.md lines 730-776 -->
[Copy content, update image refs: 043→014, 044→015, 045→016, 046→017, 047→018, 048→019]
<!-- END ORIGINAL -->

## Sound Money & Political Movement

<chapterId>[GENERATE-UUID]</chapterId>

<!-- ORIGINAL: btc102/en.md lines 778-841 -->
[Copy content, update image refs: 049→020, 050→021, 051→022, 052→023, 053→024]
<!-- END ORIGINAL -->

# Conclusion

<partId>[GENERATE-UUID]</partId>

## Conclusion

<chapterId>[GENERATE-UUID]</chapterId>
<isCourseConclusion>true</isCourseConclusion>
```

---

## Implementation Steps

1. **Create folder**: `courses/btc103-new/`
2. **Create course.yml**: Copy template above, generate UUID
3. **Copy images**:
   ```bash
   # From btc102/assets/en/ copy files 030-053.webp
   # To btc103-new/assets/en/ as 001-024.webp
   ```
4. **Copy quizzes**:
   ```bash
   # From btc102/quizz/015-023/
   # To btc103-new/quizz/000-008/
   ```
5. **Create en.md**:
   - Copy YAML frontmatter from template
   - Write NEW intro chapter (see SCU102-new for example)
   - Copy ORIGINAL content from BTC102 lines 564-841
   - Update all image references (subtract 29 from each number)
   - Add ORIGINAL/NEW comment tags
6. **Validate**: Check markdown structure, image refs, links
7. **Update docs**: Mark BTC103 as completed in btc102-split-plan.md

---

## Checklist

- [x] Create `courses/btc103-new/` folder
- [x] Create `course.yml` with UUID
- [x] Copy images (030-053 → 001-024)
- [x] Copy quizzes (015-023 → 000-008)
- [x] Create `en.md` with frontmatter
- [x] Write NEW intro chapter
- [x] Copy Part 2 content (Bitcoin in 5 Minutes)
- [x] Copy Part 3 content (Why Bitcoin Matters)
- [x] Add conclusion chapter
- [x] Update all image references
- [x] Add ORIGINAL/NEW tags
- [x] Validate markdown
- [x] Update btc102-split-plan.md

---

*Document created: 2026-01-19*
*Reference: See `docs/scu102-creation.md` for similar implementation example*
