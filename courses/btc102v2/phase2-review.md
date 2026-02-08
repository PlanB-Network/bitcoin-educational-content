# BTC102v2 Phase 2 Review

> This document tracks all work needed to complete BTC102v2 (Your First Bitcoin Journey) for production.
> Location: `courses/btc102v2/phase2-review.md`
>
> **Note:** BTC102v2 is a "hub" course that guides learners to other specialized courses. It has different requirements than standard courses (no quizzes needed).

## Progress Tracker
| Phase | Status | Date | Session |
|-------|--------|------|---------|
| A - Structure Review | ✅ | 2026-01-21 | Claude Opus 4.5 |
| B - Pre-Production | ⬜ | | |
| C - Recording | ⬜ | | |
| D - Post-Production | ⬜ | | |

---

## Phase A: Structure & Content Review

### A1. Metadata Validation (course.yml)

| Field | Value | Status |
|-------|-------|--------|
| id | `d493c2bb-c0d0-4d77-9a68-c9ee5631c8ba` | ✅ Valid UUID |
| topic | `bitcoin` | ✅ |
| subtopic | `getting-started` | ✅ |
| type | `theory` | ✅ |
| level | `beginner` | ✅ |
| hours | `1` | ✅ |
| professors_id | `2e1b5182-567e-453a-af29-36009340ff02` | ✅ |

**Additional Fields Present:**
- teaching_format: `self_paced` ✅
- contributor_names: `Plan B Network` ✅
- original_language: `en` ✅
- proofreading: Configured ✅
- tags: `bitcoin`, `getting-started`, `beginner`, `learning-path`, `hub` ✅

**Issues:** None. All required fields are present and valid.

---

### A2. Frontmatter Validation (en.md)

- [x] `name` present and descriptive: "Your First Bitcoin Journey"
- [x] `goal` is single sentence, action-oriented: "Navigate your Bitcoin learning path with confidence by discovering the right courses for your goals."
- [x] `objectives` has 3-6 items (4 objectives):
  1. Understand the complete Bitcoin learning journey
  2. Identify your Bitcoin user profile
  3. Find the right courses for your specific needs
  4. Build a solid foundation for Bitcoin ownership

**Issues:** None. Frontmatter is complete and well-structured.

---

### A3. Structure Validation

- [x] First Part is Introduction
- [x] No text between Part headings and first Chapter
- [x] All Parts have `<partId>`
- [x] All Chapters have `<chapterId>`
- [x] Going Further is last chapter of last content Part (Chapter 9 in Part 4)
- [x] Conclusion Part exists with only Conclusion chapter
- [x] `<isCourseConclusion>true</isCourseConclusion>` tag present

**Part/Chapter Structure:**

| Part # | Part Name | partId | Chapters |
|--------|-----------|--------|----------|
| 1 | Introduction | `introduction-btc102v2` | Ch 1-2 |
| 2 | Your Learning Path | `learning-path-btc102v2` | Ch 3-4 |
| 3 | Course Directory | `course-directory-btc102v2` | Ch 5-7 |
| 4 | Getting Started | `getting-started-btc102v2` | Ch 8-9 |
| 5 | Conclusion | `conclusion-btc102v2` | Ch 10 |

**Chapter Detail:**

| Ch # | Chapter Title | chapterId | Part |
|------|---------------|-----------|------|
| 1 | Welcome to Your Bitcoin Journey | `welcome-ch01` | Introduction |
| 2 | Course Overview | `overview-ch02` | Introduction |
| 3 | Understanding Your Profile | `your-profile-ch03` | Your Learning Path |
| 4 | Recommended Course Sequences | `course-sequences-ch04` | Your Learning Path |
| 5 | Safety & Security Courses | `safety-courses-ch05` | Course Directory |
| 6 | Understanding Bitcoin Courses | `understanding-courses-ch06` | Course Directory |
| 7 | Practical Bitcoin Courses | `practical-courses-ch07` | Course Directory |
| 8 | Your First Steps | `first-steps-ch08` | Getting Started |
| 9 | Going Further | `going-further-ch09` | Getting Started |
| 10 | Conclusion | `conclusion-ch10` | Conclusion |

**Issues:** None. Structure fully complies with PBN standards.

---

### A4. Image Inventory

**Summary:**
| Metric | Count |
|--------|-------|
| Current images | 4 |
| Target images | 4-8 |
| **GAP** | **0-4 images (see analysis)** |

**Current Images in `assets/en/`:**
- `001.webp` - Referenced in Chapter 2 (Course Overview)
- `002.webp` - Referenced in Chapter 2 (Course Overview)
- `003.webp` - Referenced in Chapter 2 (Course Overview)
- `004.webp` - Referenced in Chapter 2 (Course Overview)

**Per-Chapter Breakdown:**

| Ch # | Chapter Title | Type | Current | Target | Gap | Notes |
|------|---------------|------|---------|--------|-----|-------|
| 1 | Welcome to Your Bitcoin Journey | Introduction | 0 | 0-1 | 0 | OK - Intro chapter |
| 2 | Course Overview | Substantive | 4 | 4-5 | 0-1 | Good coverage |
| 3 | Understanding Your Profile | Substantive | 0 | 4-5 | 4-5 | **Needs images** |
| 4 | Recommended Course Sequences | Substantive | 0 | 4-5 | 4-5 | **Needs images** |
| 5 | Safety & Security Courses | Directory | 0 | 1-2 | 1-2 | Link/reference chapter |
| 6 | Understanding Bitcoin Courses | Directory | 0 | 1-2 | 1-2 | Link/reference chapter |
| 7 | Practical Bitcoin Courses | Directory | 0 | 1-2 | 1-2 | Link/reference chapter |
| 8 | Your First Steps | Substantive | 0 | 2-3 | 2-3 | Action-oriented chapter |
| 9 | Going Further | Resources | 0 | 1-2 | 1-2 | Resource summary |
| 10 | Conclusion | Conclusion | 0 | 0 | 0 | OK - No images needed |

**Hub Course Image Consideration:**

BTC102v2 is a hub/navigation course that primarily directs learners to other courses. The chapter types differ from standard content courses:
- **Directory chapters (5-7)**: These describe other courses and link to them. Minimal images needed.
- **Substantive chapters (3-4)**: These describe user profiles and learning paths. Could benefit from diagrams.
- **Action chapter (8)**: Provides practical steps. Could use 2-3 supportive images.

**Recommended Image Priority:**
1. High Priority: Chapter 3 (user profile infographic) and Chapter 4 (learning path diagrams)
2. Medium Priority: Chapter 8 (action steps visual)
3. Low Priority: Chapters 5-7 and 9 (could use simple icons/thumbnails but not essential)

**Total Recommended Additional Images:** 8-12 (depending on production goals)

---

### A5. Missing Images - Detailed Specifications

#### Chapter 3: Understanding Your Profile (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | `user-profiles-overview` | Quadrant diagram showing four Bitcoin user profiles (Hodler, Stacker, Active User, Privacy-Focused) with key characteristics of each | Diagram/Infographic | High |
| 2 | `hodler-profile` | Icon/illustration representing the Hodler profile - person with locked vault/safe, long-term focus, minimal activity | Illustration | Medium |
| 3 | `stacker-profile` | Icon/illustration representing the Stacker profile - person with recurring purchases, DCA concept, building blocks | Illustration | Medium |
| 4 | `active-user-profile` | Icon/illustration representing the Active User - person making transactions, Lightning symbol, mobile wallet | Illustration | Medium |
| 5 | `privacy-focused-profile` | Icon/illustration representing Privacy-Focused user - person with shield/mask, no-KYC symbol, privacy tools | Illustration | Medium |

#### Chapter 4: Recommended Course Sequences (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | `path-a-cautious-beginner` | Flowchart showing Path A sequence: SCU102 -> BTC103 -> BTC105 -> BTC104 -> SOV102, with time estimates | Diagram | High |
| 2 | `path-b-eager-acquirer` | Flowchart showing Path B sequence: BTC105 -> BTC104 -> SCU102 -> BTC103 -> SOV102 | Diagram | High |
| 3 | `path-c-industry-professional` | Flowchart showing Path C sequence: BTC103 -> BIZ102 -> SCU102 -> BTC105 -> BTC104 | Diagram | Medium |
| 4 | `path-d-privacy-focused` | Flowchart showing Path D sequence: SCU102 -> BTC103 -> BTC105 -> BTC104 -> SOV102 | Diagram | Medium |
| 5 | `course-map-complete` | Master diagram showing all courses with interconnections and recommended flows | Diagram | High |

#### Chapter 5: Safety & Security Courses (needs 1-2 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | `scu102-thumbnail` | Course thumbnail/icon for SCU102 - security shield, lock, warning symbols | Icon/Thumbnail | Low |
| 2 | `btc104-thumbnail` | Course thumbnail/icon for BTC104 - wallet, key, security | Icon/Thumbnail | Low |

#### Chapter 6: Understanding Bitcoin Courses (needs 1-2 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | `btc103-thumbnail` | Course thumbnail/icon for BTC103 - Bitcoin logo, "why" concept | Icon/Thumbnail | Low |
| 2 | `biz102-thumbnail` | Course thumbnail/icon for BIZ102 - industry/business theme | Icon/Thumbnail | Low |

#### Chapter 7: Practical Bitcoin Courses (needs 1-2 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | `btc105-thumbnail` | Course thumbnail/icon for BTC105 - acquisition/buying theme | Icon/Thumbnail | Low |
| 2 | `sov102-thumbnail` | Course thumbnail/icon for SOV102 - inheritance/family theme | Icon/Thumbnail | Low |

#### Chapter 8: Your First Steps (needs 2-3 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | `four-steps-checklist` | Visual checklist showing the 4 steps: Choose Path -> Start Course -> Practice -> Continue Learning | Diagram | Medium |
| 2 | `practice-actions` | Icons showing practice activities after each course (implement security, make purchase, set up wallet, create plan) | Infographic | Medium |
| 3 | `journey-ahead` | Inspirational image showing the broader Bitcoin learning journey beyond these courses | Illustration | Low |

#### Chapter 9: Going Further (needs 1-2 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | `course-summary-table` | Visual version of the course summary table with priorities highlighted | Infographic | Low |
| 2 | `planb-network-resources` | Icon showing additional PBN resources available | Icon | Low |

---

### A6. Quiz Inventory

**Hub Course Status: N/A**

Per the Phase 2 workflow documentation, BTC102v2 is designated as a "hub" course:
- From workflow doc table: "BTC102v2 | Quiz: 0 | hub - no quizzes needed"
- Hub courses guide learners to other courses rather than teaching substantive content themselves

**Summary:**
| Metric | Value |
|--------|-------|
| Current quizzes | 0 |
| Required quizzes | 0 (hub course) |
| quizz/ folder exists | No |
| **GAP** | **None - N/A for hub course** |

**Rationale:**
- BTC102v2 serves as a navigation/orientation course
- Content is primarily directional (pointing to other courses)
- Assessment of learning happens in the individual specialized courses
- Adding quizzes here would test navigation knowledge, not Bitcoin knowledge

---

### A7. Missing Quizzes - Topic Suggestions

**N/A - Hub Course**

BTC102v2 does not require quizzes per the workflow specification. Assessment of Bitcoin knowledge is handled by the individual courses:
- SCU102: Security knowledge quizzes
- BTC103: Bitcoin fundamentals quizzes
- BIZ102: Industry knowledge quizzes
- BTC104: Security implementation quizzes
- BTC105: Acquisition knowledge quizzes
- SOV102: Inheritance planning quizzes

If quizzes are later desired for engagement purposes, potential topics could include:
- Identifying which learning path matches a scenario
- Matching user profiles to recommended courses
- Course sequencing knowledge

However, this is **not recommended** as it adds friction without substantive educational value.

---

### A8. Structural Fixes Required

| # | Issue | Location | Fix Required | Priority |
|---|-------|----------|--------------|----------|
| - | None identified | - | - | - |

**Structure Assessment: PASS**

The course structure fully complies with PBN standards:
- All Parts have proper partIds
- All Chapters have proper chapterIds
- Going Further correctly positioned
- Conclusion section properly formatted
- isCourseConclusion tag present
- No text between Part headings and first Chapter
- First Part is Introduction

---

### A9. Work Summary for Phase B

**Before starting Phase B, complete these tasks:**

#### Critical (Must Do)
- [x] Structural validation - COMPLETE, no fixes needed
- [x] Metadata validation - COMPLETE, all fields valid
- [x] Quiz status determination - COMPLETE, N/A for hub course

#### Images to Create (Recommended: 8-12 total, Minimum: 4-5)

**High Priority (Before Phase B):**
- [ ] Ch 3: 1 image - User profiles quadrant diagram
- [ ] Ch 4: 2-3 images - Learning path flowcharts (at minimum: Path A and course map)

**Medium Priority (Can be concurrent with Phase B):**
- [ ] Ch 3: 4 images - Individual profile illustrations
- [ ] Ch 4: 2 images - Additional path diagrams
- [ ] Ch 8: 2-3 images - Action steps visuals

**Low Priority (Nice to have):**
- [ ] Ch 5-7: 6 images - Course thumbnails/icons
- [ ] Ch 9: 1-2 images - Summary visuals

#### Quizzes to Create
- N/A - Hub course does not require quizzes

#### Content Review Notes
- Course content is well-written and comprehensive
- Links to other courses are properly formatted with PlanB Academy URLs
- Four user profiles are clearly defined
- Four learning paths provide good guidance
- Course directory sections provide appropriate detail for each linked course

---

## Phase A Completion Summary

**Phase A Status:** ✅ COMPLETE
**Phase A Completed:** 2026-01-21

**Key Findings:**
1. **Structure:** Fully compliant with PBN standards - no fixes needed
2. **Metadata:** All required fields present and valid
3. **Images:** 4 existing images (all in Chapter 2). Recommended 8-12 additional images, with 4-5 being high priority for user profiles and learning paths visualization
4. **Quizzes:** N/A - Hub course designation means no quizzes required

**Recommendations for Phase B:**
1. Create high-priority images (user profiles diagram, learning path flowcharts) before starting pre-production
2. Consider whether medium-priority images add sufficient value for the hub course format
3. Focus video recording on guiding learners effectively through the course selection process
4. Emphasize the practical value of choosing the right learning path

**Notes for Next Session:**
- BTC102v2 is a unique course in the split - it's a navigation hub rather than content course
- Video production should focus on being welcoming and orientational
- Consider whether all learning path diagrams need separate slides or can be shown as one comprehensive map
- The course is relatively short (1 hour) - recording should be straightforward
