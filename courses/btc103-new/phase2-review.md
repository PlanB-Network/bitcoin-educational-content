# BTC103 Phase 2 Review

> This document tracks all work needed to complete BTC103 for production.
> Location: `courses/btc103-new/phase2-review.md`

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
| id | d08be07f-c643-44dd-a994-512e10bf8331 | ✅ |
| topic | economy | ✅ |
| subtopic | bitcoin-importance | ✅ |
| type | theory | ✅ |
| level | beginner | ✅ |
| hours | 2 | ✅ |
| professors_id | 2e1b5182-567e-453a-af29-36009340ff02 | ✅ |

**Issues:** None - all required fields present and valid.

### A2. Frontmatter Validation (en.md)

- [x] `name` present and descriptive: "Why Bitcoin Matters"
- [x] `goal` is single sentence, action-oriented: "Understand what Bitcoin is and why it represents a revolutionary alternative to traditional monetary systems."
- [x] `objectives` has 3-6 items (has 4):
  - Understand Bitcoin's origins and core technical concepts
  - Recognize Bitcoin's unique monetary properties
  - Understand why Bitcoin matters for financial freedom
  - Grasp Bitcoin's role as protection against monetary crises

**Issues:** None - frontmatter is complete and well-formed.

### A3. Structure Validation

- [x] First Part is Introduction
- [x] No text between Part headings and first Chapter
- [x] All Parts have `<partId>`
- [x] All Chapters have `<chapterId>`
- [x] **Going Further is last chapter of last content Part** - FIXED (2026-02-08)
- [x] Conclusion Part exists with only Conclusion chapter
- [x] `<isCourseConclusion>true</isCourseConclusion>` tag present

**Current Structure:**

| Part # | Part Title | partId | Chapters |
|--------|-----------|--------|----------|
| 1 | Introduction | ee11de75-9a2c-443f-b6ac-7e3085567a14 | Ch1: Welcome to BTC103 |
| 2 | Bitcoin in 5 Minutes | 44cbcb19-f147-4afe-b2c0-c2f69d9193fd | Ch2: The Origins, Ch3: A Decentralized Network, Ch4: Monetary Properties & Transparency, Ch5: Use Cases |
| 3 | Why Bitcoin Matters | 1e76792a-d32d-41e8-b065-7d47f8907af4 | Ch6: A Universal Currency, Ch7: Protection Against Crises, Ch8: Sound Money & Political Movement |
| 4 | Conclusion | a2d82d2d-1cef-441b-8a27-896709bd3afc | Ch9: Conclusion |

**Issues:**
1. ~~**CRITICAL:** Missing "Going Further" chapter~~ - FIXED (2026-02-08): Added Going Further chapter with chapterId `a7b8c9d0-e1f2-3a4b-5c6d-7e8f9a0b1c2d` as last chapter of Part 3

---

### A4. Image Inventory

**Summary:**
| Metric | Count |
|--------|-------|
| Current images | 24 |
| Target images | 25-30 |
| **GAP** | **1-6 images to create** |

**Per-Chapter Breakdown:**

| Ch # | Chapter Title | chapterId | Current | Target | Gap | Images Used |
|------|---------------|-----------|---------|--------|-----|-------------|
| 1 | Welcome to BTC103 | 68cabb01-6fd0-4dd6-a84a-700c6ab210de | 0 | 0-1 | 0 | None |
| 2 | The Origins | c2103e99-8cf9-44d9-8681-10884fde134f | 4 | 4-5 | 0 | 001, 002, 003, 004 |
| 3 | A Decentralized Network | 690e52c8-2495-4005-93b0-888b5f799713 | 4 | 4-5 | 0 | 005, 006, 007, 008 |
| 4 | Monetary Properties & Transparency | 4069bbba-eb66-4ab8-8a21-397e147b3564 | 2 | 4-5 | 2-3 | 009, 010 |
| 5 | Use Cases | b90c8bee-2136-4dcf-ae81-0b5298d96d11 | 1 | 4-5 | 3-4 | 011 |
| 6 | A Universal Currency | 008f328a-0c6c-4a18-b931-357848e96294 | 2 | 4-5 | 2-3 | 012, 013 |
| 7 | Protection Against Crises | 50f47586-6567-4427-b55d-dce1647f9213 | 6 | 4-5 | 0 | 014, 015, 016, 017, 018, 019 |
| 8 | Sound Money & Political Movement | 3bf91676-d887-45d3-b12f-c2f487b86890 | 5 | 4-5 | 0 | 020, 021, 022, 023, 024 |
| 9 | Going Further | a7b8c9d0-e1f2-3a4b-5c6d-7e8f9a0b1c2d | 0 | 1-2 | 1-2 | N/A |
| 9 | Conclusion | f1c2d3e4-a5b6-7c8d-9e0f-1a2b3c4d5e6f | 0 | 0 | 0 | None |

**Total Image Gap: 8-12 images needed**

---

### A5. Missing Images - Detailed Specifications

#### Chapter 4: Monetary Properties & Transparency (needs 2-3 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | bitcoin-supply-curve | Chart showing Bitcoin's issuance schedule from 2009-2140, with halving events marked and cumulative supply approaching 21M. Shows predictable monetary policy vs fiat unpredictability. | Chart/diagram | High |
| 2 | bitcoin-open-source | Illustration showing the open-source nature of Bitcoin Core - multiple developers reviewing code, GitHub repository, global collaboration. Emphasize transparency and auditability. | Illustration | Medium |
| 3 | running-node-validation | Diagram showing how running a Bitcoin node allows individual verification - computer with Bitcoin Core downloading and validating all blocks since 2009. | Diagram | Medium |

#### Chapter 5: Use Cases (needs 3-4 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | cross-border-payments | World map showing Bitcoin transactions crossing borders 24/7, contrasting with traditional banking hours and limitations. Highlight no intermediaries. | Illustration/map | High |
| 2 | store-of-value-growth | Chart showing Bitcoin's long-term price appreciation despite short-term volatility. Compare to gold and fiat purchasing power over time. | Chart | High |
| 3 | financial-freedom-wallet | Illustration showing person holding their own keys, contrasting with bank vaults. Emphasize self-custody and uncensorable access. | Illustration | Medium |
| 4 | lightning-network-speed | Diagram showing Lightning Network enabling instant, low-cost transactions as a second layer on top of Bitcoin's base layer. | Diagram | Low |

#### Chapter 6: A Universal Currency (needs 2-3 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | universal-access | Diverse group of people (different ages, backgrounds, locations) all accessing the same Bitcoin network with equal features. Shows equality of access. | Illustration | High |
| 2 | bitcoin-wallet-features | Infographic listing Bitcoin's features: free wallets, send anywhere, no ID required, accessible to all, no intermediaries. | Infographic | Medium |
| 3 | financial-inclusion-vs-liberation | Split image showing two perspectives: unbanked gaining access on one side, banked escaping restrictions on the other. | Illustration | Medium |

#### Going Further Chapter (needs 1-2 images - chapter to be created)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | learning-path-next-steps | Visual roadmap showing progression from BTC103 to practical courses (buying, securing, advanced topics). | Diagram | High |
| 2 | golden-rules-summary | Visual summary card of key takeaways and golden rules from the course. | Infographic | Medium |

---

### A6. Quiz Inventory

**Summary:**
| Metric | Count |
|--------|-------|
| Current quizzes | 9 |
| Content chapters (excluding intro/going-further/conclusion) | 7 |
| Required per-chapter (7 x 5) | 35 |
| Required for final exam | 40 |
| **Total recommended** | **75** (or minimum 40 with overlap) |
| **GAP** | **31-66 quizzes to create** |

**Per-Chapter Breakdown:**

| Ch # | Chapter Title | chapterId | Current | Required | Gap |
|------|---------------|-----------|---------|----------|-----|
| 1 | Welcome to BTC103 | 68cabb01-6fd0-4dd6-a84a-700c6ab210de | 0 | 0 | 0 |
| 2 | The Origins | c2103e99-8cf9-44d9-8681-10884fde134f | 5 | 5 | 0 |
| 3 | A Decentralized Network | 690e52c8-2495-4005-93b0-888b5f799713 | 0 | 5 | 5 |
| 4 | Monetary Properties & Transparency | 4069bbba-eb66-4ab8-8a21-397e147b3564 | 0 | 5 | 5 |
| 5 | Use Cases | b90c8bee-2136-4dcf-ae81-0b5298d96d11 | 0 | 5 | 5 |
| 6 | A Universal Currency | 008f328a-0c6c-4a18-b931-357848e96294 | 4 | 5 | 1 |
| 7 | Protection Against Crises | 50f47586-6567-4427-b55d-dce1647f9213 | 0 | 5 | 5 |
| 8 | Sound Money & Political Movement | 3bf91676-d887-45d3-b12f-c2f487b86890 | 0 | 5 | 5 |
| -- | Going Further (MISSING) | N/A | 0 | 0 | 0 |
| 9 | Conclusion | f1c2d3e4-a5b6-7c8d-9e0f-1a2b3c4d5e6f | 0 | 0 | 0 |
| -- | Final Exam Pool | N/A | 0 | 40 | 40 |

**Chapter Quiz Gap Total: 26 quizzes**
**Final Exam Pool Gap: 40 quizzes (can overlap with chapter quizzes)**
**Minimum Total Gap: 31 quizzes (to reach 40 minimum)**

**Current Quiz Mapping:**

| Quiz # | chapterId | Linked Chapter | Topic |
|--------|-----------|----------------|-------|
| 000 | c2103e99-8cf9-44d9-8681-10884fde134f | Ch 2: The Origins | Cypherpunks/Bitcoin origins |
| 001 | c2103e99-8cf9-44d9-8681-10884fde134f | Ch 2: The Origins | Cypherpunks/Bitcoin origins |
| 002 | c2103e99-8cf9-44d9-8681-10884fde134f | Ch 2: The Origins | Cypherpunks/Bitcoin origins |
| 003 | c2103e99-8cf9-44d9-8681-10884fde134f | Ch 2: The Origins | Cypherpunks/Bitcoin origins |
| 004 | c2103e99-8cf9-44d9-8681-10884fde134f | Ch 2: The Origins | Cypherpunks/Bitcoin origins |
| 005 | 008f328a-0c6c-4a18-b931-357848e96294 | Ch 6: A Universal Currency | Universal access/equality |
| 006 | 008f328a-0c6c-4a18-b931-357848e96294 | Ch 6: A Universal Currency | Universal access/equality |
| 007 | 008f328a-0c6c-4a18-b931-357848e96294 | Ch 6: A Universal Currency | Universal access/equality |
| 008 | 008f328a-0c6c-4a18-b931-357848e96294 | Ch 6: A Universal Currency | Universal access/equality |

---

### A7. Missing Quizzes - Topic Suggestions

#### Chapter 3: A Decentralized Network (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | What does "peer-to-peer" mean in the context of Bitcoin? | multiple-choice | easy |
| 2 | What is the role of a Bitcoin node in the network? | multiple-choice | medium |
| 3 | What is the blockchain and how does it function as a ledger? | multiple-choice | medium |
| 4 | What is mining and how does proof-of-work secure the network? | multiple-choice | medium |
| 5 | What is the halving and why does it matter for Bitcoin's supply? | multiple-choice | hard |

#### Chapter 4: Monetary Properties & Transparency (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | What is Bitcoin's maximum supply limit? | multiple-choice | easy |
| 2 | Why is Bitcoin's monetary policy considered "predictable"? | multiple-choice | medium |
| 3 | What is a satoshi and how divisible is Bitcoin? | multiple-choice | easy |
| 4 | Why is Bitcoin's open-source nature important for trust? | multiple-choice | medium |
| 5 | What is the purpose of running your own Bitcoin node? | multiple-choice | hard |

#### Chapter 5: Use Cases (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | Why is Bitcoin useful for cross-border payments? | multiple-choice | easy |
| 2 | What makes Bitcoin a potential "store of value"? | multiple-choice | medium |
| 3 | How does Bitcoin provide financial freedom in authoritarian regimes? | multiple-choice | medium |
| 4 | What is the Lightning Network and what problem does it solve? | multiple-choice | hard |
| 5 | Why is Bitcoin called "digital gold"? | multiple-choice | medium |

#### Chapter 6: A Universal Currency (needs 1 quiz)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | What does it mean that Bitcoin is "accessible to all"? | multiple-choice | medium |

#### Chapter 7: Protection Against Crises (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | What is hyperinflation and how has it affected populations historically? | multiple-choice | medium |
| 2 | How does Bitcoin protect against currency devaluation? | multiple-choice | medium |
| 3 | What happened in countries like Greece and Lebanon with banking restrictions? | multiple-choice | hard |
| 4 | Why is Bitcoin resistant to government seizure compared to bank accounts? | multiple-choice | medium |
| 5 | What does "opting out" of the traditional financial system mean? | multiple-choice | easy |

#### Chapter 8: Sound Money & Political Movement (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | What is the phrase "Not your keys, not your Bitcoin" referring to? | multiple-choice | easy |
| 2 | How do central banks erode purchasing power through monetary policy? | multiple-choice | hard |
| 3 | Why did the gold standard's collapse in 1971 matter for fiat currencies? | multiple-choice | hard |
| 4 | What philosophical groups and movements have embraced Bitcoin? | multiple-choice | medium |
| 5 | How is Bitcoin a "peaceful form of protest"? | multiple-choice | medium |

#### Final Exam Pool (needs 40 quizzes - can overlap with chapter quizzes)

| # | Topic | Related Chapter | Difficulty |
|---|-------|-----------------|------------|
| 1-5 | Bitcoin origins, Cypherpunks, genesis block message | Ch 2 | easy-medium |
| 6-10 | Decentralization, nodes, blockchain as ledger | Ch 3 | easy-medium |
| 11-15 | Mining, proof-of-work, halving mechanism | Ch 3 | medium-hard |
| 16-20 | 21M cap, satoshis, divisibility, open-source | Ch 4 | easy-medium |
| 21-25 | Cross-border payments, store of value, Lightning | Ch 5 | medium |
| 26-30 | Universal access, equal opportunity, pseudonymity | Ch 6 | easy-medium |
| 31-35 | Hyperinflation history, capital controls, seizure resistance | Ch 7 | medium-hard |
| 36-40 | Self-custody, fiat corruption, Bitcoin as political movement | Ch 8 | medium-hard |

---

### A8. Structural Fixes Required

| # | Issue | Location | Fix Required | Priority |
|---|-------|----------|--------------|----------|
| 1 | Missing "Going Further" chapter | Part 3 (Why Bitcoin Matters) | Add "Going Further" chapter as the last chapter of Part 3, before the Conclusion Part. Include: resources list, next courses to take, golden rules summary, external learning resources. | **Critical** |

**Detailed Fix for "Going Further" Chapter:**

Add the following after Chapter 8 (Sound Money & Political Movement) and before the Conclusion Part:

```markdown
## Going Further

<chapterId>going-further-ch09</chapterId>

### Resources & Next Steps

[Content to include:]
- Links to recommended courses (BTC101 for deeper philosophy, practical courses for buying/securing)
- External resources (books, podcasts, websites)
- Golden rules summary (verify don't trust, not your keys not your coins, etc.)
- Community resources (meetups, forums)

### Recommended Learning Path

1. BTC101 - Deep dive into Bitcoin philosophy
2. Practical acquisition courses
3. Security and self-custody courses
4. Advanced topics (Lightning, nodes, privacy)
```

---

### A9. Work Summary for Phase B

**Before starting Phase B, complete these tasks:**

#### Critical (Must Do)
- [x] Add "Going Further" chapter to Part 3 (before Conclusion Part) - DONE (2026-02-08)
- [x] Generate chapterId for new Going Further chapter - DONE (`a7b8c9d0-e1f2-3a4b-5c6d-7e8f9a0b1c2d`)

#### Images to Create (8-12 total)
- [ ] Ch 4: 2-3 images (bitcoin-supply-curve, bitcoin-open-source, running-node-validation)
- [ ] Ch 5: 3-4 images (cross-border-payments, store-of-value-growth, financial-freedom-wallet, lightning-network-speed)
- [ ] Ch 6: 2-3 images (universal-access, bitcoin-wallet-features, financial-inclusion-vs-liberation)
- [ ] Going Further: 1-2 images (learning-path-next-steps, golden-rules-summary)

#### Quizzes to Create (31-66 total)
- [ ] Ch 3: 5 quizzes (decentralization, nodes, blockchain, mining, halving)
- [ ] Ch 4: 5 quizzes (supply cap, monetary policy, divisibility, open-source, nodes)
- [ ] Ch 5: 5 quizzes (cross-border, store of value, financial freedom, Lightning, digital gold)
- [ ] Ch 6: 1 quiz (accessibility)
- [ ] Ch 7: 5 quizzes (hyperinflation, devaluation, banking restrictions, seizure resistance)
- [ ] Ch 8: 5 quizzes (self-custody, central bank policy, gold standard, movements, protest)
- [ ] Final exam pool: 40 quizzes (can overlap with above)

---

**Phase A Status:** ✅ COMPLETE
**Phase A Completed:** 2026-01-21
**Notes:**
- Course structure is solid with one critical fix needed (Going Further chapter)
- Images are well-distributed with some gaps in middle chapters (4, 5, 6)
- Quizzes are concentrated on only 2 chapters (2 and 6) - need better distribution
- Content quality is high, originating from proven BTC102 material
- The `<isCourseConclusion>true</isCourseConclusion>` tag is properly placed
- All partIds and chapterIds use valid UUIDs
