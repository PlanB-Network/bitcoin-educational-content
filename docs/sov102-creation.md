# SOV102 - Bitcoin Inheritance Planning: Implementation Documentation

## Course Overview

**Course Code**: SOV102
**Title**: Bitcoin Inheritance Planning
**Discipline**: Sovereignty (SOV)
**Level**: Beginner (102)
**Estimated Duration**: 1-1.5 hours
**Implementation Date**: 2026-01-20

---

## Course Philosophy

### Target Audience
Bitcoin holders who have already acquired and secured their bitcoin (completed BTC105 and BTC104 equivalent knowledge) and now need to ensure their wealth can be passed on to loved ones.

### Goal
A practical, step-by-step guide to creating a Bitcoin inheritance plan, following Pamela Morgan's methodology from *Cryptoasset Inheritance Planning*.

### What This Course IS
- A beginner-friendly introduction to Bitcoin inheritance planning
- A practical guide to creating a basic inheritance letter
- Coverage of the key principles: trusted assistants, inventory, written instructions, secure storage

### What This Course is NOT
- Legal advice (explicitly stated and preserved from original)
- A comprehensive estate planning guide for complex situations
- Coverage of advanced technical solutions (decreasing multisig with timelocks is only mentioned briefly)

### Key Attribution
This course preserves full attribution to **Pamela Morgan** and her book *Cryptoasset Inheritance Planning*. The legal disclaimer stating this is not legal advice has been preserved.

---

## Source Content Mapping

### From BTC102 Part 4 (en.md lines 2192-2420)

| Section | Lines | Content Used |
|---------|-------|--------------|
| Creating an inheritance plan | 2196-2419 | Full inheritance planning content |
| Why it's necessary | 2204-2214 | Motivation for inheritance planning |
| Goals (Pamela Morgan's 4 goals) | 2215-2228 | Four key objectives |
| Example profile (Cédric) | 2230-2244 | Sample user profile |
| Before you start | 2246-2259 | Preparation, tools needed |
| Common misconceptions | 2263-2272 | Debunking myths |
| Step 1: Select trusted people | 2276-2299 | Choosing assistants |
| Step 2: Create inventory | 2300-2324 | Asset cataloging |
| Step 3: Write the letter | 2325-2392 | Drafting inheritance letter |
| Step 4: Review and store | 2398-2419 | Final steps, storage |

### Content NOT Included
The "Top 0.1% Most Prepared Bitcoiners" chapter (lines 2423-2527) was NOT included as it's primarily "what's next" content better suited for the hub course (BTC102v2).

---

## Final Course Structure

### Parts and Chapters (5 Parts, 11 Chapters)

```
# Part 1: Introduction
├── Ch 1: Welcome to SOV102 [NEW]
└── Ch 2: Why Bitcoin Inheritance Matters [ORIGINAL]

# Part 2: Preparation
├── Ch 3: Common Misconceptions [ORIGINAL]
├── Ch 4: What You'll Need [ORIGINAL]
└── Ch 5: Understanding Your Profile [ORIGINAL]

# Part 3: Creating Your Plan
├── Ch 6: Step 1 - Select Trusted Assistants [ORIGINAL]
├── Ch 7: Step 2 - Create Your Inventory [ORIGINAL]
└── Ch 8: Step 3 - Write the Inheritance Letter [ORIGINAL]

# Part 4: Finalize and Maintain
├── Ch 9: Step 4 - Review and Store [ORIGINAL]
└── Ch 10: Going Further [NEW]

# Part 5: Conclusion
└── Ch 11: Conclusion [STANDARD]
```

### Content Classification

| Content Type | Chapters | Notes |
|--------------|----------|-------|
| NEW | Ch 1, 10 | Welcome intro, Going Further |
| ORIGINAL | Ch 2-9 | Direct from BTC102 Part 4 |
| STANDARD | Ch 11 | Conclusion with isCourseConclusion tag |

---

## Asset Mapping

### Images Copied from BTC102

| BTC102 Image | SOV102 Image | Description | Used In |
|--------------|--------------|-------------|---------|
| 097.webp | 001.webp | Pamela Morgan's book cover | Ch 2: Why Inheritance Matters |
| 098.webp | 002.webp | Cédric's profile diagram | Ch 5: Understanding Your Profile |
| 099.webp | 003.webp | Tools needed (paper, pen, envelopes) | Ch 4: What You'll Need |
| 100.webp | 004.webp | Sealed envelope storage | Ch 9: Review and Store |

**Total**: 4 images

### Images NOT Copied
- 101.webp, 102.webp: From "Top 0.1%" chapter - saved for hub course (BTC102v2)

---

## Quiz Mapping

### Quizzes Copied from BTC102

| BTC102 Quiz | SOV102 Quiz | Topic | Chapter |
|-------------|-------------|-------|---------|
| 060 | 000 | Role of inheritance letter | write-letter-ch08 |
| 061 | 001 | Why handwritten on paper | write-letter-ch08 |
| 062 | 002 | Not giving mnemonic to one person | trusted-assistants-ch06 |
| 063 | 003 | Risk of too much info disclosure | write-letter-ch08 |
| 064 | 004 | Clear instructions essential | write-letter-ch08 |

**Total**: 5 quizzes

---

## Tutorial Cross-References

### Advanced Solution (Mentioned in Going Further)
- **Liana wallet** - For decreasing multisig with timelock:
  `https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04`

### Book Reference
- *Cryptoasset Inheritance Planning* by Pamela Morgan
  - Amazon link preserved: `https://www.amazon.com/gp/product/1947910116/`
  - Author Twitter: `https://x.com/pamelawjd`

---

## Implementation Checklist

### Phase 1: Setup
- [x] Create `courses/sov102/` folder
- [x] Create `courses/sov102/assets/en/` subfolder
- [x] Create `courses/sov102/quizz/` subfolder
- [x] Create `course.yml` with UUID and metadata

### Phase 2: Content
- [x] Create `en.md` with frontmatter
- [x] Write Part 1: Introduction (Ch 1-2)
- [x] Write Part 2: Preparation (Ch 3-5)
- [x] Write Part 3: Creating Your Plan (Ch 6-8)
- [x] Write Part 4: Finalize and Maintain (Ch 9-10)
- [x] Write Part 5: Conclusion (Ch 11)
- [x] Add ORIGINAL/NEW content tags throughout

### Phase 3: Assets
- [x] Copy image 097.webp → 001.webp
- [x] Copy image 098.webp → 002.webp
- [x] Copy image 099.webp → 003.webp
- [x] Copy image 100.webp → 004.webp
- [x] Update all image references in en.md

### Phase 4: Quizzes
- [x] Copy quiz 060 → 000 folder
- [x] Copy quiz 061 → 001 folder
- [x] Copy quiz 062 → 002 folder
- [x] Copy quiz 063 → 003 folder
- [x] Copy quiz 064 → 004 folder
- [x] Update chapterId in each question.yml

### Phase 5: Documentation
- [x] Update btc102-split-plan.md with SOV102 details
- [x] Create this sov102-creation.md document

---

## Validation Checklist

- [x] All partIds are unique and follow pattern: `xxx-sov102`
- [x] All chapterIds are unique and follow pattern: `xxx-ch##`
- [x] Final chapter has `<isCourseConclusion>true</isCourseConclusion>` tag
- [x] All image references use format `![image](assets/en/###.webp)`
- [x] Images exist at referenced paths
- [x] Quiz chapterIds match actual chapter IDs in en.md
- [x] ORIGINAL/NEW tags present on all content sections
- [x] Pamela Morgan attribution preserved
- [x] Legal disclaimer preserved

---

## Files Created/Modified

| File | Action |
|------|--------|
| `courses/sov102/course.yml` | CREATED |
| `courses/sov102/en.md` | CREATED |
| `courses/sov102/assets/en/001.webp` | COPIED from btc102 097.webp |
| `courses/sov102/assets/en/002.webp` | COPIED from btc102 098.webp |
| `courses/sov102/assets/en/003.webp` | COPIED from btc102 099.webp |
| `courses/sov102/assets/en/004.webp` | COPIED from btc102 100.webp |
| `courses/sov102/quizz/000/` | COPIED from btc102 060, updated chapterId |
| `courses/sov102/quizz/001/` | COPIED from btc102 061, updated chapterId |
| `courses/sov102/quizz/002/` | COPIED from btc102 062, updated chapterId |
| `courses/sov102/quizz/003/` | COPIED from btc102 063, updated chapterId |
| `courses/sov102/quizz/004/` | COPIED from btc102 064, updated chapterId |
| `docs/btc102-split-plan.md` | UPDATED with SOV102 implementation details |
| `docs/sov102-creation.md` | CREATED (this file) |

---

## Notes

1. **Attribution Critical**: The content explicitly credits Pamela Morgan and her book. This attribution is preserved in Ch 2 and at the end of Ch 9.

2. **Legal Disclaimer**: The original content explicitly states this is not legal advice. This disclaimer is preserved.

3. **Practical Focus**: The course is designed to be actionable - users should be able to create a basic inheritance plan by following the 4 steps.

4. **Cross-References**: Clear pointers to:
   - BTC104 for wallet security
   - BTC105 for acquisition
   - Liana tutorial for advanced inheritance solutions

5. **Content Reorganization**: The original BTC102 had all content in one long chapter. For SOV102, this was reorganized into:
   - Introduction (why it matters, goals)
   - Preparation (misconceptions, tools, profile)
   - Creating the plan (4 steps)
   - Finalize and maintain (storage, going further)
   - Conclusion

6. **Sample Letter Preserved**: The full sample inheritance letter from Pamela Morgan's methodology is preserved in Ch 8.
