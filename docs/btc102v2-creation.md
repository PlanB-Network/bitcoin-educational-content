# BTC102v2 - Your First Bitcoin Journey (Hub Course)

## Implementation Documentation

**Created**: 2026-01-20
**Status**: ✅ IMPLEMENTED
**Course Type**: Navigation/Hub Course

---

## Overview

BTC102v2 is the final course in the BTC102 split project. Unlike the other 6 courses which contain educational content, this is a **navigation hub** that helps learners find the right courses in the right order.

### Purpose

- Replace the original 14-hour BTC102 with a streamlined 1-hour orientation
- Guide users to the appropriate specialized courses based on their profile
- Provide a complete directory of all split courses with descriptions and links

### What This Course Does

- Introduces the complete Bitcoin learning journey
- Helps users identify their Bitcoin profile (Hodler, Stacker, User, Privacy-focused)
- Provides 4 recommended learning paths based on profile
- Contains a complete directory of all 6 split courses
- Links to all courses so users can start immediately

### What This Course Does NOT Do

- Does not duplicate content from the split courses
- Does not teach Bitcoin fundamentals (that's BTC101/BTC103)
- Does not provide acquisition/security tutorials (that's BTC105/BTC104)
- Does not include quizzes (navigation course only)

---

## Files Created

### Directory Structure

```
courses/btc102v2/
├── course.yml           # Course metadata
├── en.md                # English content (5 parts, 10 chapters)
├── assets/
│   └── en/
│       ├── 001.webp     # Course overview - Prerequisites
│       ├── 002.webp     # Course overview - Understanding
│       ├── 003.webp     # Course overview - Taking Action
│       └── 004.webp     # Course overview - Long-term
└── quizz/               # Empty (no quizzes for hub course)
```

### course.yml

```yaml
id: d493c2bb-c0d0-4d77-9a68-c9ee5631c8ba
topic: bitcoin
subtopic: getting-started
type: theory
level: beginner
hours: 1
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
  - getting-started
  - beginner
  - learning-path
  - hub
```

---

## Course Structure

### Part 1: Introduction
| Chapter | Title | Content Type |
|---------|-------|--------------|
| Ch 1 | Welcome to Your Bitcoin Journey | NEW |
| Ch 2 | Course Overview | ORIGINAL (adapted from BTC102 intro lines 29-72) |

### Part 2: Your Learning Path
| Chapter | Title | Content Type |
|---------|-------|--------------|
| Ch 3 | Understanding Your Profile | NEW - 4 profiles explained |
| Ch 4 | Recommended Course Sequences | NEW - 4 learning paths |

### Part 3: Course Directory
| Chapter | Title | Content Type |
|---------|-------|--------------|
| Ch 5 | Safety & Security Courses | NEW - SCU102, BTC104 descriptions |
| Ch 6 | Understanding Bitcoin Courses | NEW - BTC103, BIZ102 descriptions |
| Ch 7 | Practical Bitcoin Courses | NEW - BTC105, SOV102 descriptions |

### Part 4: Getting Started
| Chapter | Title | Content Type |
|---------|-------|--------------|
| Ch 8 | Your First Steps | NEW - action steps |
| Ch 9 | Going Further | NEW - summary table, links |

### Part 5: Conclusion
| Chapter | Title | Content Type |
|---------|-------|--------------|
| Ch 10 | Conclusion | STANDARD - isCourseConclusion tag |

**Total: 5 Parts, 10 Chapters**

---

## Asset Mapping

| BTC102 Image | BTC102v2 Image | Description | Used In |
|--------------|----------------|-------------|---------|
| 001.webp | 001.webp | Course overview - Prerequisites section | Ch 2 |
| 002.webp | 002.webp | Course overview - Understanding section | Ch 2 |
| 003.webp | 003.webp | Course overview - Taking Action section | Ch 2 |
| 004.webp | 004.webp | Course overview - Long-term section | Ch 2 |

**Source**: `courses/btc102/assets/en/`
**Destination**: `courses/btc102v2/assets/en/`

---

## Quiz Mapping

**No quizzes** - This is a navigation/hub course, not a content course. Users will take quizzes in the individual specialized courses.

---

## Content Details

### The Four User Profiles (Chapter 3)

1. **The Hodler** - Long-term investor focused on accumulating bitcoin as store of value
2. **The Stacker** - Regular buyer using DCA strategy
3. **The Active User** - Uses Bitcoin for payments and daily transactions
4. **The Privacy-Focused User** - Prioritizes privacy and minimizes data exposure

### The Four Learning Paths (Chapter 4)

1. **Path A: The Cautious Beginner** (Recommended for most)
   - SCU102 → BTC103 → BTC105 → BTC104 → SOV102

2. **Path B: The Eager Acquirer**
   - BTC105 → BTC104 → SCU102 → BTC103 → SOV102

3. **Path C: The Industry Professional**
   - BTC103 → BIZ102 → SCU102 → BTC105 → BTC104

4. **Path D: The Privacy-Focused User**
   - SCU102 → BTC103 → BTC105 → BTC104 → SOV102

### Course Directory (Chapters 5-7)

All 6 split courses are documented with:
- Duration and level
- What you'll learn (bullet points)
- Who should take this course
- Prerequisites (if any)
- Direct link to course

---

## Links Included

### Split Courses
- SCU102: `https://planb.academy/courses/scu102`
- BTC103: `https://planb.academy/courses/btc103`
- BIZ102: `https://planb.academy/courses/biz102`
- BTC105: `https://planb.academy/courses/btc105`
- BTC104: `https://planb.academy/courses/btc104`
- SOV102: `https://planb.academy/courses/sov102`

### Foundation Course
- BTC101: `https://planb.academy/courses/2b7dc507-81e3-4b70-88e6-41ed44239966`

---

## Implementation Checklist

- [x] Create `courses/btc102v2/` folder
- [x] Create `course.yml` with UUID (`d493c2bb-c0d0-4d77-9a68-c9ee5631c8ba`)
- [x] Create `assets/en/` subfolder
- [x] Create `quizz/` subfolder (empty)
- [x] Copy images 001-004 from original BTC102
- [x] Create `en.md` with proper frontmatter
- [x] Write Part 1: Introduction (2 chapters)
- [x] Write Part 2: Your Learning Path (2 chapters)
- [x] Write Part 3: Course Directory (3 chapters)
- [x] Write Part 4: Getting Started (2 chapters)
- [x] Write Part 5: Conclusion with `<isCourseConclusion>true</isCourseConclusion>`
- [x] Add all course links
- [x] Add NEW/ORIGINAL content tags
- [x] Validate markdown structure
- [x] Update master plan document

---

## Differences from Other Split Courses

| Aspect | BTC102v2 | Other 6 Courses |
|--------|----------|-----------------|
| Purpose | Navigation/Hub | Educational Content |
| Content | Mostly NEW | Mostly ORIGINAL from BTC102 |
| Quizzes | None | Yes (mapped from BTC102) |
| Duration | 1 hour | 1.5-3 hours each |
| Links | Many external course links | Few cross-references |

---

## Notes for Future Maintenance

1. **Course Links**: If course URLs change, update all links in chapters 5-7 and chapter 9
2. **New Courses**: If additional courses are added to the curriculum, update the course directory
3. **Profile Changes**: If user profiles are redefined, update chapter 3 and learning paths in chapter 4
4. **Images**: The 4 images are from the original BTC102 course overview; if those are updated, sync here

---

## Related Documents

- Master Plan: `docs/btc102-split-plan.md`
- Original BTC102: `courses/btc102/en.md`

---

*This document created as part of the BTC102 Split Project - Phase 3 Implementation*
