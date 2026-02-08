# BTC102 Split Phase 2: Course Review & Video Production Workflow

> **Master reference document for Phase 2 production pipeline**
>
> This workflow enables any Claude session to pick up exactly where the last one stopped.

---

## Quick Start

**To begin work on a course:**
1. Identify which course and phase you're working on
2. Copy the appropriate bootstrap prompt below
3. Follow the phase-specific tasks
4. Update the per-course review doc before ending session

---

## Course Production Progress

| Course | Phase A | Phase B | Phase C | Phase D | Review Doc |
|--------|---------|---------|---------|---------|------------|
| BTC103 | ✅ | ⬜ | ⬜ | ⬜ | [phase2-review.md](../courses/btc103-new/phase2-review.md) |
| BIZ102 | ✅ | ⬜ | ⬜ | ⬜ | [phase2-review.md](../courses/biz102-new/phase2-review.md) |
| BTC102v2 | ✅ | ⬜ | ⬜ | ⬜ | [phase2-review.md](../courses/btc102v2/phase2-review.md) |
| SOV102 | ✅ | ⬜ | ⬜ | ⬜ | [phase2-review.md](../courses/sov102/phase2-review.md) |
| BTC104 | ✅ | ⬜ | ⬜ | ⬜ | [phase2-review.md](../courses/btc104/phase2-review.md) |
| BTC105 | ✅ | ⬜ | ⬜ | ⬜ | [phase2-review.md](../courses/btc105/phase2-review.md) |
| SCU102 | ✅ | ⬜ | ⬜ | ⬜ | [phase2-review.md](../courses/scu102-new/phase2-review.md) |

**Legend:** ⬜ Not Started | 🔄 In Progress | ✅ Complete

**Last Updated:** 2026-01-21

---

## Context: Phase 1 vs Phase 2

**Phase 1 (COMPLETE):** Split original BTC102 into 7 focused courses
- Created course structures, content, quiz mappings
- Documented in `docs/btc102-split-plan.md`

**Phase 2 (THIS WORKFLOW):** Review, polish, and produce videos for all 7 courses

---

## The 7 Courses

| # | Code | Name | Parts | Ch | Quiz | Img | Hrs | Folder |
|---|------|------|-------|-----|------|-----|-----|--------|
| 1 | SCU102 | Financial Fraud, Scams & Online Security | 7 | 26 | 15 | 25 | 3 | `scu102-new/` |
| 2 | BTC103 | Why Bitcoin Matters | 4 | 9 | 9 | 24 | 2 | `btc103-new/` |
| 3 | BIZ102 | Bitcoin Industry Overview | 5 | 12 | 10 | 11 | 2 | `biz102-new/` |
| 4 | BTC105 | How to Acquire Bitcoin | 6 | 18 | 9 | 4 | 2.5 | `btc105/` |
| 5 | BTC104 | How to Secure Bitcoin | 5 | 14 | 3 | 3 | 2 | `btc104/` |
| 6 | SOV102 | Bitcoin Inheritance Planning | 5 | 11 | 5 | 4 | 1.5 | `sov102/` |
| 7 | BTC102v2 | Your First Bitcoin Journey (Hub) | 5 | 10 | 0 | 4 | 1 | `btc102v2/` |

**Recommended Order:** BTC103 → BIZ102 → BTC102v2 → SOV102 → BTC104 → BTC105 → SCU102

---

## Production Pipeline

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  PHASE A        │    │  PHASE B        │    │  PHASE C        │    │  PHASE D        │
│  Structure &    │───>│  Pre-Production │───>│  Recording      │───>│  Post-Production│
│  Content Review │    │  (Script/PPT)   │    │  (By Rogzy)     │    │  (Finalization) │
└─────────────────┘    └─────────────────┘    └─────────────────┘    └─────────────────┘
     Claude              Claude              Manual (Rogzy)           Claude
```

---

# Phase A: Structure & Content Review

## Purpose
**Audit and document what's missing** so it can be fixed later. Phase A produces a comprehensive inventory of all gaps (images, quizzes, structure issues) as a **checklist of work to be done**.

## Key Principle
Phase A is about **documenting gaps**, not fixing them. The output should clearly list:
- What exists now
- What is required
- What is missing (the gap)
- Specifications for creating missing items

## Bootstrap Prompt
```
I am doing PHASE A (Structure & Content Review) for [COURSE_CODE].
Repository: bitcoin-educational-content
Branch: split-btc102
Folder: courses/[FOLDER]/

FIRST: Read these docs for context:
- docs/phase2-review-workflow.md (this workflow - READ THE STANDARDS CAREFULLY)
- courses/[FOLDER]/phase2-review.md (if exists - may have prior progress)

TASKS:
1. Validate course.yml metadata (all required fields present)
2. Verify en.md frontmatter (name, goal, objectives)
3. Audit Part/Chapter structure against PBN standards
4. Verify Conclusion section has <isCourseConclusion>true</isCourseConclusion>
5. Count images per chapter - document EXACT gaps with specifications
6. Count quizzes per chapter - document EXACT gaps (5 per chapter + 40 for exam)
7. Generate detailed specifications for ALL missing images
8. Generate topic suggestions for ALL missing quizzes
9. List all structural fixes needed

OUTPUT: Create/update courses/[FOLDER]/phase2-review.md with Phase A report
        (Note: review doc goes IN THE COURSE FOLDER, not in docs/)
Mark Phase A status as COMPLETE when done
```

## Structure Standards

**Required course structure:**
```markdown
---
name: [Title]
goal: [One sentence]
objectives:
  - [Objective 1]
  - [Objective 2]
  - [Objective 3+]
---

[Course intro text]

+++

# Introduction                         <- First Part
<partId>intro-[course]</partId>

## Welcome to [Course]                 <- First Chapter
<chapterId>welcome-ch01</chapterId>
[Content...]

# [Content Part 2]                     <- Content Parts
<partId>[descriptive-id]</partId>

## [Chapter Title]
<chapterId>[descriptive-id]</chapterId>
[Content...]

# [Last Content Part]
<partId>[descriptive-id]</partId>

## [Last Content Chapter]
<chapterId>[descriptive-id]</chapterId>
[Content...]

## Going Further                       <- MUST be last chapter before Conclusion
<chapterId>going-further-chXX</chapterId>
[Resources, next steps, golden rules...]

# Conclusion                           <- Separate Part with ONLY conclusion
<partId>conclusion-[course]</partId>

## Conclusion
<chapterId>conclusion-chXX</chapterId>
<isCourseConclusion>true</isCourseConclusion>
```

**Rules:**
- NO text between `# Part` and first `## Chapter`
- Every Part needs `<partId>`
- Every Chapter needs `<chapterId>`
- IDs should be descriptive (BIP39 words or slugs)
- Going Further = last chapter of last content Part
- Conclusion Part contains ONLY the Conclusion chapter
- `<isCourseConclusion>true</isCourseConclusion>` is REQUIRED

## Image Targets

| Chapter Type | Target Images | Notes |
|--------------|---------------|-------|
| Introduction/Welcome | 0-1 | Minimal visuals |
| Substantive content | 4-5 | Diagrams, examples, screenshots |
| Going Further | 1-2 | Resource summary |
| Conclusion | 0 | None needed |

**Image Gap Calculation:**
```
For each chapter:
  Current images: [count from assets/en/ referenced in chapter]
  Target images: [based on chapter type above]
  Gap: Target - Current = [number of images to create]
```

## Quiz Requirements (IMPORTANT)

### Per-Chapter Quizzes (End of Chapter)
Each content chapter needs **5 quizzes minimum** for the small quiz at the end of the chapter.

| Chapter Type | Required Quizzes |
|--------------|------------------|
| Introduction/Welcome | 0 |
| Substantive content | **5 minimum** |
| Going Further | 0 |
| Conclusion | 0 |

### Final Exam Quizzes
Every course needs **40 quizzes minimum** for the final exam pool.
- These can overlap with chapter quizzes or be separate
- Should cover all major topics across the course

### Quiz Gap Calculation
```
Per-chapter requirement:
  Content chapters count: [N]
  Required chapter quizzes: N × 5 = [total]

Final exam requirement: 40 minimum

Total quizzes needed: MAX(chapter_quizzes, 40) or ideally chapter_quizzes + exam_pool

Current quizzes: [count from quizz/ folder]
Gap: Required - Current = [number of quizzes to create]
```

### Example Calculation (9-chapter course like BTC103)
```
Content chapters (excluding intro/conclusion): 7
Chapter quizzes needed: 7 × 5 = 35
Final exam pool needed: 40
Total recommended: 35 + 40 = 75 quizzes (or at minimum 40 with overlap)

If current quizzes = 9
Gap = 75 - 9 = 66 quizzes to create (or minimum 40 - 9 = 31)
```

## Phase A Report Template

**IMPORTANT:** The review document should be saved in the course folder:
`courses/[FOLDER]/phase2-review.md` (NOT in docs/)

```markdown
# [COURSE_CODE] Phase 2 Review

> This document tracks all work needed to complete [COURSE_CODE] for production.
> Location: `courses/[FOLDER]/phase2-review.md`

## Progress Tracker
| Phase | Status | Date | Session |
|-------|--------|------|---------|
| A - Structure Review | ⬜ / 🔄 / ✅ | | |
| B - Pre-Production | ⬜ | | |
| C - Recording | ⬜ | | |
| D - Post-Production | ⬜ | | |

---

## Phase A: Structure & Content Review

### A1. Metadata Validation (course.yml)
| Field | Value | Status |
|-------|-------|--------|
| id | [UUID] | ✅/❌ |
| topic | [value] | ✅/❌ |
| subtopic | [value] | ✅/❌ |
| type | [theory/practice] | ✅/❌ |
| level | [value] | ✅/❌ |
| hours | [value] | ✅/❌ |
| professors_id | [list] | ✅/❌ |

**Issues:** [list any problems]

### A2. Frontmatter Validation (en.md)
- [ ] `name` present and descriptive
- [ ] `goal` is single sentence, action-oriented
- [ ] `objectives` has 3-6 items

**Issues:** [list any problems]

### A3. Structure Validation
- [ ] First Part is Introduction
- [ ] No text between Part headings and first Chapter
- [ ] All Parts have `<partId>`
- [ ] All Chapters have `<chapterId>`
- [ ] Going Further is last chapter of last content Part
- [ ] Conclusion Part exists with only Conclusion chapter
- [ ] `<isCourseConclusion>true</isCourseConclusion>` tag present

**Issues:** [list any problems]

---

### A4. Image Inventory

**Summary:**
| Metric | Count |
|--------|-------|
| Current images | [N] |
| Target images | [N] |
| **GAP** | **[N] images to create** |

**Per-Chapter Breakdown:**

| Ch # | Chapter Title | Current | Target | Gap |
|------|---------------|---------|--------|-----|
| 1 | [Title] | 0 | 0-1 | 0 |
| 2 | [Title] | X | 4-5 | Y |
| ... | ... | ... | ... | ... |
| N | Conclusion | 0 | 0 | 0 |

### A5. Missing Images - Detailed Specifications

For each missing image, provide enough detail for an image generator:

#### Chapter [N]: [Title]

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | [descriptive-name] | [What the image should show, key elements, purpose] | [diagram/illustration/chart/screenshot] | [high/medium/low] |
| 2 | ... | ... | ... | ... |

[Repeat for each chapter with missing images]

---

### A6. Quiz Inventory

**Summary:**
| Metric | Count |
|--------|-------|
| Current quizzes | [N] |
| Required per-chapter (content chapters × 5) | [N] |
| Required for final exam | 40 |
| **Total recommended** | **[N]** |
| **GAP** | **[N] quizzes to create** |

**Per-Chapter Breakdown:**

| Ch # | Chapter Title | chapterId | Current | Required | Gap |
|------|---------------|-----------|---------|----------|-----|
| 1 | Welcome | [id] | 0 | 0 | 0 |
| 2 | [Title] | [id] | X | 5 | Y |
| ... | ... | ... | ... | ... | ... |
| N | Conclusion | [id] | 0 | 0 | 0 |

**Current Quiz Mapping:**
| Quiz # | chapterId | Linked Chapter | Topic |
|--------|-----------|----------------|-------|
| 000 | [id] | Ch X: [Title] | [topic] |
| ... | ... | ... | ... |

### A7. Missing Quizzes - Topic Suggestions

For each chapter needing quizzes, suggest topics:

#### Chapter [N]: [Title] (needs [X] quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | [Topic from chapter content] | [multiple-choice/true-false] | [easy/medium/hard] |
| 2 | ... | ... | ... |
| 3 | ... | ... | ... |
| 4 | ... | ... | ... |
| 5 | ... | ... | ... |

[Repeat for each chapter needing quizzes]

#### Final Exam Pool (needs [X] additional quizzes)

| # | Topic | Related Chapter | Difficulty |
|---|-------|-----------------|------------|
| 1 | [Cross-cutting topic] | Ch X | [medium/hard] |
| ... | ... | ... | ... |

---

### A8. Structural Fixes Required

List all structural issues that must be fixed:

| # | Issue | Location | Fix Required | Priority |
|---|-------|----------|--------------|----------|
| 1 | [e.g., Missing "Going Further" chapter] | Part X | [Description of fix] | Critical |
| 2 | ... | ... | ... | ... |

---

### A9. Work Summary for Phase B

**Before starting Phase B, complete these tasks:**

#### Critical (Must Do)
- [ ] [Task 1]
- [ ] [Task 2]

#### Images to Create ([N] total)
- [ ] Ch X: [N] images (see specs in A5)
- [ ] Ch Y: [N] images (see specs in A5)
- [ ] ...

#### Quizzes to Create ([N] total)
- [ ] Ch X: [N] quizzes (see topics in A7)
- [ ] Ch Y: [N] quizzes (see topics in A7)
- [ ] Final exam pool: [N] quizzes
- [ ] ...

---

**Phase A Status:** ⬜ NOT STARTED / 🔄 IN PROGRESS / ✅ COMPLETE
**Phase A Completed:** [YYYY-MM-DD]
**Notes:** [Any additional context for next session]
```

---

# Phase B: Pre-Production

## Purpose
Create all materials needed for video recording: transcript outlines, PowerPoint structures, recording session plan.

## Prerequisites
- Phase A COMPLETE
- All structural fixes from Phase A applied
- Images generated (or generation in progress with specs locked)

## Bootstrap Prompt
```
I am doing PHASE B (Pre-Production) for [COURSE_CODE].
Repository: bitcoin-educational-content
Folder: courses/[FOLDER]/

FIRST: Read these docs:
- docs/phase2-review-workflow.md (this workflow)
- docs/[COURSE_CODE]-phase2-review.md (MUST have Phase A complete)

VERIFY: Phase A status is COMPLETE and fixes applied

TASKS:
1. Create bullet-point transcript outline for EACH chapter
2. Design PowerPoint slide structure for EACH chapter
3. Identify any content gaps or unclear sections
4. Create recording session plan (logical chapter groupings)
5. Estimate total recording time

OUTPUT: Update docs/[COURSE_CODE]-phase2-review.md with Phase B materials
Mark Phase B status as COMPLETE when done
```

## Transcript Outline Template

```markdown
## Chapter [N]: [Title]
**Part:** [Part Name]
**Duration Target:** [X] minutes

### Key Teaching Points
1. [Main concept - what learner must understand]
2. [Secondary concept]
3. [Tertiary concept]

### Script Outline

**INTRO (30-60 sec)**
- Hook: [Opening question or compelling statement]
- Context: [Why this matters to the learner]
- Preview: [What we'll cover]

**SECTION 1: [Topic] (~X min)**
- Point: [Key information]
- Point: [Key information]
- Example/Analogy: [Make it concrete]
- Visual: [00X.webp - what it shows]

**SECTION 2: [Topic] (~X min)**
- Point: [Key information]
- Point: [Key information]
- Visual: [00Y.webp - what it shows]

**SECTION 3: [Topic] (~X min)**
- Point: [Key information]
- Visual: [00Z.webp - what it shows]

**SUMMARY (30 sec)**
- Key takeaway 1
- Key takeaway 2
- Transition: [Bridge to next chapter]

### Visuals Needed
| Timestamp | Image | Purpose |
|-----------|-------|---------|
| 1:30 | 00X.webp | Show [concept] |
| 3:00 | 00Y.webp | Illustrate [concept] |

### Quiz Cue
After covering [specific concept], reference Quiz [000] - "[quiz topic]"
```

## PowerPoint Structure Template

```markdown
## Chapter [N]: [Title] - Slide Deck

**Total Slides:** [N]
**Images Required:** [list]

| Slide | Type | Title | Content | Visual |
|-------|------|-------|---------|--------|
| 1 | Title | [Chapter Name] | Course: [CODE] • Part [N] • Chapter [N] | Course logo |
| 2 | Overview | What You'll Learn | • Point 1 • Point 2 • Point 3 | None |
| 3 | Content | [Section 1 Title] | • Key point • Key point | 00X.webp |
| 4 | Diagram | [Concept Name] | [Diagram explanation] | 00Y.webp |
| 5 | Example | [Example Title] | [Concrete example] | 00Z.webp or None |
| 6 | Content | [Section 2 Title] | • Key point • Key point | Image |
| N-1 | Summary | Key Takeaways | • Takeaway 1 • Takeaway 2 • Takeaway 3 | None |
| N | Transition | Next Up | Preview of next chapter | None |

**Design Notes:**
- Color scheme: [if specific to course]
- Diagram style needed: [technical/friendly/etc]
- Special elements: [animations, reveals, etc]
```

## Recording Session Plan Template

```markdown
## Recording Session Plan for [COURSE_CODE]

### Overview
- **Total Chapters:** [N]
- **Estimated Total Recording Time:** [X] hours
- **Recommended Sessions:** [N]

### Session Breakdown

| Session | Part | Chapters | Duration | Notes |
|---------|------|----------|----------|-------|
| 1 | Introduction | Ch 1-2 | ~20 min | Light intro, set the tone |
| 2 | Part 2 | Ch 3-5 | ~45 min | Core concepts |
| 3 | Part 3 | Ch 6-8 | ~40 min | Build on Part 2 |
| 4 | Parts 4-5 | Ch 9-11 + Going Further | ~35 min | Wrap up |

### Recommended Breaks
- After Session 2 (longest session)
- Between major topic shifts

### Recording Environment Checklist
- [ ] Quiet room, no echo
- [ ] Good lighting (face visible)
- [ ] Microphone tested
- [ ] Screen share ready for slides
- [ ] Water nearby
- [ ] Phone on silent

### Files Needed for Recording
- [ ] PowerPoint slides: [filename]
- [ ] Transcript outlines: docs/[COURSE_CODE]-phase2-review.md
- [ ] Course content: courses/[folder]/en.md
```

## Phase B Addition to Review Document

```markdown
---

## Phase B: Pre-Production

### B1. Transcript Outlines

[Include full transcript outline for each chapter using template above]

### B2. PowerPoint Structures

[Include slide structure for each chapter using template above]

### B3. Recording Session Plan

[Include recording session plan using template above]

### B4. Content Gaps Identified
[Any unclear sections, outdated info, or content that needs clarification before recording]

### B5. Pre-Recording Checklist
- [ ] All transcript outlines complete
- [ ] All slide structures defined
- [ ] Images available (or specs finalized)
- [ ] Recording session plan approved by Rogzy
- [ ] Any content gaps resolved

---

**Phase B Status:** ⬜ NOT STARTED / 🔄 IN PROGRESS / ✅ COMPLETE
**Phase B Completed:** [YYYY-MM-DD]
**Notes:** [Context for Rogzy or next session]
```

---

# Phase C: Recording (Manual - Rogzy)

## Purpose
Rogzy records all video content following the pre-production materials.

## Prerequisites
- Phase B COMPLETE
- PowerPoint slides created
- Recording environment ready

## Handoff Document for Rogzy

```markdown
## [COURSE_CODE] Recording Handoff

### What's Ready
- ✅ Transcript outlines in docs/[COURSE_CODE]-phase2-review.md
- ✅ Slide structures defined
- ✅ Recording session plan

### Pre-Recording Checklist
- [ ] Review transcript outlines (don't memorize, just understand flow)
- [ ] PowerPoint slides finalized and loaded
- [ ] Recording setup tested (audio, video, screen share)
- [ ] Do a 2-minute test recording to check quality

### Recording Tips
- Follow the transcript outline as a guide, not a script
- Speak naturally - conversational tone
- Pause briefly between sections for easier editing
- If you stumble, pause, then restart that sentence cleanly
- Display slides at moments indicated in transcripts
- Note any sections that need re-recording

### Recording Sessions
[Paste recording session plan from Phase B]

### During Recording - Track These
For each chapter, note:
- [ ] Recorded successfully
- [ ] Needs partial re-record (section: _____)
- [ ] Time recorded: _____ min
- [ ] Any issues: _____

### Post-Recording
Add notes to docs/[COURSE_CODE]-phase2-review.md under Phase C section:
- Which chapters are done
- Any re-records needed
- Total time recorded
- Any content issues discovered while recording
```

## Phase C Addition to Review Document

```markdown
---

## Phase C: Recording

### Recording Log
| Ch | Title | Status | Duration | Re-record Needed | Notes |
|----|-------|--------|----------|------------------|-------|
| 1 | [Title] | ✅ / 🔄 | X min | No / Yes (section) | |
| 2 | [Title] | ✅ / 🔄 | X min | | |

### Issues Discovered During Recording
[Any content problems, outdated info, or clarifications needed]

### Re-Record List
[Specific sections that need to be re-recorded]

### Raw Footage Location
[Where video files are stored]

---

**Phase C Status:** ⬜ NOT STARTED / 🔄 IN PROGRESS / ✅ COMPLETE
**Phase C Completed:** [YYYY-MM-DD]
**Notes:** [Any post-recording context]
```

---

# Phase D: Post-Production

## Purpose
Finalize everything, verify course is complete and ready for publication.

## Prerequisites
- Phase C COMPLETE
- All recordings done
- Re-records completed

## Bootstrap Prompt
```
I am doing PHASE D (Post-Production) for [COURSE_CODE].
Repository: bitcoin-educational-content
Folder: courses/[FOLDER]/

FIRST: Read docs/[COURSE_CODE]-phase2-review.md (all previous phases)

TASKS:
1. Review Phase C recording notes from Rogzy
2. Final structure validation (run Phase A checks again)
3. Verify all images are in assets/en/ folder
4. Verify all quizzes have correct chapterId links
5. Update course.yml if needed (hours estimate, etc.)
6. Create final completion checklist
7. Mark course as PRODUCTION COMPLETE

OUTPUT: Update docs/[COURSE_CODE]-phase2-review.md with Phase D verification
Update this file (phase2-review-workflow.md) progress tracker
```

## Phase D Addition to Review Document

```markdown
---

## Phase D: Post-Production

### D1. Recording Review
- [ ] All chapters recorded
- [ ] Re-records completed
- [ ] Video quality acceptable
- [ ] Audio quality acceptable

### D2. Final Structure Check
[Re-run Phase A structure validation - note any issues]

### D3. Asset Verification
- [ ] All images present in assets/en/
- [ ] Image numbering correct (001, 002, ...)
- [ ] Thumbnail exists (assets/thumbnail.webp)

### D4. Quiz Verification
- [ ] All quizzes have valid chapterId
- [ ] Quiz content aligns with chapter content
- [ ] question.yml files complete

### D5. Metadata Updates
- [ ] course.yml hours estimate accurate
- [ ] proofreading entry updated
- [ ] Any other metadata changes

### D6. Final Checklist
- [ ] Course passes all structure standards
- [ ] All images in place
- [ ] All quizzes linked
- [ ] Videos recorded and stored
- [ ] Ready for publication

---

**Phase D Status:** ⬜ NOT STARTED / 🔄 IN PROGRESS / ✅ COMPLETE
**Phase D Completed:** [YYYY-MM-DD]

## COURSE PRODUCTION COMPLETE
**Completion Date:** [YYYY-MM-DD]
**Total Production Time:** [estimate]
**Notes:** [Any final notes for future reference]
```

---

# Key File Paths

## Existing Documentation
- `docs/btc102-split-plan.md` - Original Phase 1 plan (1265 lines)
- `docs/btc102-split-summary.md` - Phase 1 summary
- `docs/course_documentation.md` - PBN course standards

## Course Folders & Review Documents

**IMPORTANT:** Phase 2 review documents are stored IN the course folder, not in docs/

| Course | Folder | Review Doc Location |
|--------|--------|---------------------|
| BTC103 | `courses/btc103-new/` | `courses/btc103-new/phase2-review.md` |
| BIZ102 | `courses/biz102-new/` | `courses/biz102-new/phase2-review.md` |
| BTC102v2 | `courses/btc102v2/` | `courses/btc102v2/phase2-review.md` |
| SOV102 | `courses/sov102/` | `courses/sov102/phase2-review.md` |
| BTC104 | `courses/btc104/` | `courses/btc104/phase2-review.md` |
| BTC105 | `courses/btc105/` | `courses/btc105/phase2-review.md` |
| SCU102 | `courses/scu102-new/` | `courses/scu102-new/phase2-review.md` |

## Course Content Status
| Course | en.md | course.yml | assets/ | quizz/ |
|--------|-------|------------|---------|--------|
| BTC103 | ✅ | ✅ | ✅ | ✅ |
| BIZ102 | ✅ | ✅ | ✅ | ✅ |
| BTC102v2 | ✅ | ✅ | ✅ | ⬜ (hub - no quizzes needed) |
| SOV102 | ✅ | ✅ | ✅ | ✅ |
| BTC104 | ✅ | ✅ | ✅ | ✅ |
| BTC105 | ✅ | ✅ | ✅ | ✅ |
| SCU102 | ✅ | ✅ | ✅ | ✅ |

---

# How to Continue Work

1. **Check progress tracker** at top of this document
2. **Find the next uncompleted phase** for the current course (or start next course)
3. **Copy the bootstrap prompt** for that phase
4. **Read the per-course review doc** if it exists
5. **Execute the tasks** in the bootstrap prompt
6. **Update the review doc** with your findings
7. **Update this progress tracker** before ending session

This ensures every Claude session knows exactly where to pick up and what to do next.
