# SOV102 Phase 2 Review

> This document tracks all work needed to complete SOV102 (Bitcoin Inheritance Planning) for production.
> Location: `courses/sov102/phase2-review.md`

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
| id | 455676ad-2a81-48f4-b141-5257b9652c61 | ✅ |
| topic | sovereignty | ✅ |
| subtopic | inheritance | ✅ |
| type | theory | ✅ |
| level | beginner | ✅ |
| hours | 1.5 | ✅ |
| professors_id | [2e1b5182-567e-453a-af29-36009340ff02] | ✅ |

**Issues:** None - all required fields present and valid.

### A2. Frontmatter Validation (en.md)

- [x] `name` present and descriptive: "Bitcoin Inheritance Planning"
- [x] `goal` is single sentence, action-oriented: "Learn how to create a practical Bitcoin inheritance plan to ensure your loved ones can access your wealth."
- [x] `objectives` has 3-6 items (5 objectives present):
  1. Understand why Bitcoin inheritance planning is essential
  2. Identify trusted assistants to help your heirs
  3. Create a comprehensive inventory of your Bitcoin assets
  4. Write an effective inheritance letter
  5. Securely store your inheritance plan

**Issues:** None - frontmatter is complete and well-structured.

### A3. Structure Validation

- [x] First Part is Introduction
- [x] No text between Part headings and first Chapter
- [x] All Parts have `<partId>`:
  - Part 1: `introduction-sov102`
  - Part 2: `preparation-sov102`
  - Part 3: `creating-plan-sov102`
  - Part 4: `finalize-sov102`
  - Part 5: `conclusion-sov102`
- [x] All Chapters have `<chapterId>`:
  - Ch 1: `welcome-ch01`
  - Ch 2: `why-inheritance-ch02`
  - Ch 3: `misconceptions-ch03`
  - Ch 4: `what-you-need-ch04`
  - Ch 5: `your-profile-ch05`
  - Ch 6: `trusted-assistants-ch06`
  - Ch 7: `inventory-ch07`
  - Ch 8: `write-letter-ch08`
  - Ch 9: `review-store-ch09`
  - Ch 10: `going-further-ch10`
  - Ch 11: `conclusion-ch11`
- [x] Going Further is last chapter of last content Part (Part 4: Finalize and Maintain)
- [x] Conclusion Part exists with only Conclusion chapter
- [x] `<isCourseConclusion>true</isCourseConclusion>` tag present

**Issues:** None - structure fully compliant with PBN standards.

**Course Structure Summary:**

| Part # | Part Name | Chapters |
|--------|-----------|----------|
| 1 | Introduction | Ch 1-2 (Welcome, Why Inheritance Matters) |
| 2 | Preparation | Ch 3-5 (Misconceptions, What You'll Need, Your Profile) |
| 3 | Creating Your Plan | Ch 6-8 (Trusted Assistants, Inventory, Write Letter) |
| 4 | Finalize and Maintain | Ch 9-10 (Review & Store, Going Further) |
| 5 | Conclusion | Ch 11 (Conclusion) |

---

### A4. Image Inventory

**Summary:**
| Metric | Count |
|--------|-------|
| Current images | 4 |
| Target images | 22-27 |
| **GAP** | **18-23 images to create** |

**Per-Chapter Breakdown:**

| Ch # | Chapter Title | Type | Current | Target | Gap | Images Used |
|------|---------------|------|---------|--------|-----|-------------|
| 1 | Welcome to SOV102 | Intro | 0 | 0-1 | 0-1 | - |
| 2 | Why Bitcoin Inheritance Matters | Content | 1 | 4-5 | 3-4 | 001.webp |
| 3 | Common Misconceptions | Content | 0 | 4-5 | 4-5 | - |
| 4 | What You'll Need | Content | 1 | 4-5 | 3-4 | 003.webp |
| 5 | Understanding Your Profile | Content | 1 | 4-5 | 3-4 | 002.webp |
| 6 | Step 1 - Select Trusted Assistants | Content | 0 | 4-5 | 4-5 | - |
| 7 | Step 2 - Create Your Inventory | Content | 0 | 4-5 | 4-5 | - |
| 8 | Step 3 - Write the Inheritance Letter | Content | 0 | 4-5 | 4-5 | - |
| 9 | Step 4 - Review and Store | Content | 1 | 4-5 | 3-4 | 004.webp |
| 10 | Going Further | Resources | 0 | 1-2 | 1-2 | - |
| 11 | Conclusion | Conclusion | 0 | 0 | 0 | - |

**Current Images:**
- `001.webp` - Used in Ch 2 (Why Bitcoin Inheritance Matters)
- `002.webp` - Used in Ch 5 (Understanding Your Profile)
- `003.webp` - Used in Ch 4 (What You'll Need)
- `004.webp` - Used in Ch 9 (Review and Store)

### A5. Missing Images - Detailed Specifications

#### Chapter 1: Welcome to SOV102 (needs 0-1 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | course-overview | Visual overview of the 5-part course structure showing the journey from understanding to implementation | diagram/infographic | low |

#### Chapter 2: Why Bitcoin Inheritance Matters (needs 3-4 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | lost-bitcoin-scenario | Illustration showing a grieving family unable to access bitcoin - locked wallet with question marks | illustration | high |
| 2 | bank-vs-bitcoin | Comparison diagram: traditional bank with "forgot password" vs Bitcoin with no recovery option | diagram | high |
| 3 | four-goals-inheritance | Visual representation of Pamela Morgan's 4 goals: access timing, theft protection, long-term security, avoiding disputes | infographic | medium |

#### Chapter 3: Common Misconceptions (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | myth-lawyer | Myth vs Reality: "I need a lawyer" - show crossed-out lawyer with checkmark on DIY plan | illustration | high |
| 2 | myth-trust | Myth vs Reality: "I need to trust a third party" - show distributed trust model | diagram | high |
| 3 | myth-theft | Myth vs Reality: "Planning makes theft easy" - show balanced security scales | illustration | medium |
| 4 | myth-value | Myth vs Reality: "My BTC value is too small" - show BTC growth chart over time | chart | medium |
| 5 | myth-heirs | Myth vs Reality: "My heirs will figure it out" - show confused heir vs guided heir | illustration | high |

#### Chapter 4: What You'll Need (needs 3-4 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | planning-checklist | Visual checklist of required materials: paper, pen, envelopes, phone, computer | illustration | medium |
| 2 | secure-environment | Illustration of a calm, private workspace for creating the plan | illustration | low |
| 3 | 30-minute-timer | Visual showing "30 minutes of your time" concept - clock with progress | illustration | low |

#### Chapter 5: Understanding Your Profile (needs 3-4 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | user-profile-types | Different Bitcoin user profiles: HODLer, trader, technical, non-technical | illustration | high |
| 2 | wallet-types-overview | Overview of wallet types: mobile, hardware, exchange, multisig | diagram | high |
| 3 | self-assessment-questions | Visual representation of the key questions to consider about your situation | infographic | medium |

#### Chapter 6: Step 1 - Select Trusted Assistants (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | trusted-assistant-roles | Two roles diagram: trusted relative + experienced Bitcoin user | diagram | high |
| 2 | trust-knowledge-matrix | 2x2 matrix showing trust level vs Bitcoin knowledge for evaluating candidates | diagram | high |
| 3 | contact-comparison-table | Example visual of the comparison table template with sample entries | screenshot/mockup | medium |
| 4 | what-assistants-can-do | Checklist of tasks trusted assistants should be able to perform | infographic | medium |
| 5 | professional-options | Icons showing professional options: Bitcoin lawyers, estate planners | illustration | low |

#### Chapter 7: Step 2 - Create Your Inventory (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | inventory-categories | Visual breakdown of inventory categories: exchanges, hot wallets, hardware wallets, other | diagram | high |
| 2 | inventory-template | Example inventory table template with column headers explained | screenshot/mockup | high |
| 3 | asset-locations | Illustration showing different places where bitcoin can be stored | infographic | medium |
| 4 | snapshot-concept | Visual explaining "snapshot of current situation" vs taking action | illustration | medium |
| 5 | security-layers | Diagram showing different security layers: PIN, passphrase, 2FA, physical location | diagram | medium |

#### Chapter 8: Step 3 - Write the Inheritance Letter (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | letter-components | Visual breakdown of letter sections: intro, contacts, inventory, safety, final message | infographic | high |
| 2 | handwritten-example | Illustration of handwritten letter on paper (not actual content) | illustration | high |
| 3 | security-accessibility-balance | Scale showing balance between security (too little info) and accessibility (too much info) | diagram | high |
| 4 | letter-do-dont | Visual comparison of what TO include vs what NOT to include in the letter | diagram | medium |
| 5 | envelope-storage | Illustration of sealed tamper-evident envelope concept | illustration | medium |

#### Chapter 9: Step 4 - Review and Store (needs 3-4 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | storage-locations | Multiple secure storage locations: home safe, trusted person, bank vault | illustration | high |
| 2 | review-checklist | Visual checklist of items to verify before finalizing | infographic | medium |
| 3 | tamper-evident-envelope | Detailed illustration of tamper-evident envelope with security features | illustration | medium |

#### Chapter 10: Going Further (needs 1-2 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | advanced-solutions | Overview of advanced options: multisig, timelocks, Liana wallet | diagram | medium |
| 2 | review-schedule | Calendar showing recommended review intervals | illustration | low |

---

### A6. Quiz Inventory

**Summary:**
| Metric | Count |
|--------|-------|
| Current quizzes | 5 |
| Content chapters requiring quizzes | 7 |
| Required per-chapter (7 x 5) | 35 |
| Required for final exam | 40 |
| **Total recommended** | **75** |
| **GAP** | **70 quizzes to create** |

**Per-Chapter Breakdown:**

| Ch # | Chapter Title | chapterId | Current | Required | Gap |
|------|---------------|-----------|---------|----------|-----|
| 1 | Welcome to SOV102 | welcome-ch01 | 0 | 0 | 0 |
| 2 | Why Bitcoin Inheritance Matters | why-inheritance-ch02 | 0 | 5 | 5 |
| 3 | Common Misconceptions | misconceptions-ch03 | 0 | 5 | 5 |
| 4 | What You'll Need | what-you-need-ch04 | 0 | 5 | 5 |
| 5 | Understanding Your Profile | your-profile-ch05 | 0 | 5 | 5 |
| 6 | Step 1 - Select Trusted Assistants | trusted-assistants-ch06 | 1 | 5 | 4 |
| 7 | Step 2 - Create Your Inventory | inventory-ch07 | 0 | 5 | 5 |
| 8 | Step 3 - Write the Inheritance Letter | write-letter-ch08 | 4 | 5 | 1 |
| 9 | Step 4 - Review and Store | review-store-ch09 | 0 | 5 | 5 |
| 10 | Going Further | going-further-ch10 | 0 | 0 | 0 |
| 11 | Conclusion | conclusion-ch11 | 0 | 0 | 0 |

**Current Quiz Mapping:**

| Quiz # | chapterId | Linked Chapter | Topic |
|--------|-----------|----------------|-------|
| 000 | write-letter-ch08 | Ch 8: Write the Inheritance Letter | Role of inheritance letter in estate plan |
| 001 | write-letter-ch08 | Ch 8: Write the Inheritance Letter | Why handwritten letter on paper |
| 002 | trusted-assistants-ch06 | Ch 6: Select Trusted Assistants | What NOT to do when passing access |
| 003 | write-letter-ch08 | Ch 8: Write the Inheritance Letter | Risk of disclosing too much information |
| 004 | write-letter-ch08 | Ch 8: Write the Inheritance Letter | Essential action for heirs to recover BTC |

### A7. Missing Quizzes - Topic Suggestions

#### Chapter 2: Why Bitcoin Inheritance Matters (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | Consequences of not having an inheritance plan | multiple-choice | easy |
| 2 | Key differences between Bitcoin and traditional bank accounts for inheritance | multiple-choice | medium |
| 3 | Pamela Morgan's four goals for inheritance planning | multiple-choice | medium |
| 4 | Why there is no "forgot password" option for Bitcoin | multiple-choice | easy |
| 5 | Responsibilities that come with Bitcoin's financial sovereignty | multiple-choice | medium |

#### Chapter 3: Common Misconceptions (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | True/false: You need a lawyer to create a Bitcoin inheritance plan | true-false | easy |
| 2 | Why third-party trust can be minimized in inheritance planning | multiple-choice | medium |
| 3 | How planning affects security risk vs no planning | multiple-choice | medium |
| 4 | Why "my BTC value is too small" is a misconception | multiple-choice | easy |
| 5 | What happens if heirs try to "figure it out" without instructions | multiple-choice | medium |

#### Chapter 4: What You'll Need (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | Recommended materials for creating an inheritance plan | multiple-choice | easy |
| 2 | Why a distraction-free environment is important | multiple-choice | easy |
| 3 | Estimated time needed for basic inheritance planning | multiple-choice | easy |
| 4 | Why paper documentation is preferred over digital | multiple-choice | medium |
| 5 | Role of envelopes in the inheritance plan | multiple-choice | easy |

#### Chapter 5: Understanding Your Profile (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | Factors that affect your inheritance plan complexity | multiple-choice | medium |
| 2 | Why knowing your wallet types matters for inheritance | multiple-choice | medium |
| 3 | Assessment questions for inheritance planning | multiple-choice | easy |
| 4 | How heir's technical knowledge affects the plan | multiple-choice | medium |
| 5 | Example profile characteristics (Cedric's profile) | multiple-choice | easy |

#### Chapter 6: Step 1 - Select Trusted Assistants (needs 4 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | The two key roles for trusted assistants | multiple-choice | easy |
| 2 | What trusted assistants should NOT have access to | multiple-choice | medium |
| 3 | Qualities to look for in a trusted relative | multiple-choice | medium |
| 4 | Qualities to look for in a Bitcoin-knowledgeable assistant | multiple-choice | medium |

#### Chapter 7: Step 2 - Create Your Inventory (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | What types of assets to include in the inventory | multiple-choice | easy |
| 2 | Key information to document for each asset | multiple-choice | medium |
| 3 | Purpose of the inventory (snapshot vs action) | multiple-choice | medium |
| 4 | Where NOT to store the inventory document | multiple-choice | medium |
| 5 | Categories of Bitcoin storage to consider | multiple-choice | easy |

#### Chapter 8: Step 3 - Write the Inheritance Letter (needs 1 quiz)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | Essential sections to include in the inheritance letter | multiple-choice | medium |

#### Chapter 9: Step 4 - Review and Store (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | Key elements to verify before finalizing the letter | multiple-choice | easy |
| 2 | Recommended storage locations for the inheritance plan | multiple-choice | medium |
| 3 | Purpose of tamper-evident envelopes | multiple-choice | easy |
| 4 | Who to inform about the inheritance plan's existence | multiple-choice | medium |
| 5 | When to consult with a lawyer or notary | multiple-choice | medium |

#### Final Exam Pool (needs 40 additional quizzes)

| # | Topic | Related Chapter | Difficulty |
|---|-------|-----------------|------------|
| 1 | Why Bitcoin inheritance requires explicit planning | Ch 2 | easy |
| 2 | The four goals of Bitcoin inheritance planning | Ch 2 | medium |
| 3 | Misconception about needing a lawyer | Ch 3 | easy |
| 4 | Misconception about trusting third parties | Ch 3 | medium |
| 5 | Security vs accessibility tradeoff | Ch 8 | hard |
| 6 | Role of trusted relative vs Bitcoin expert | Ch 6 | medium |
| 7 | Information that should be in the inventory | Ch 7 | medium |
| 8 | Why handwritten documentation is preferred | Ch 8 | medium |
| 9 | Safe storage locations for inheritance documents | Ch 9 | medium |
| 10 | When to update your inheritance plan | Ch 10 | easy |
| 11 | Risks of revealing too much information | Ch 8 | hard |
| 12 | Risks of revealing too little information | Ch 8 | hard |
| 13 | What assistants should be able to do | Ch 6 | medium |
| 14 | What assistants should NOT do | Ch 6 | medium |
| 15 | Types of wallets to document | Ch 7 | easy |
| 16 | Information about exchange accounts | Ch 7 | medium |
| 17 | Purpose of the inheritance letter intro section | Ch 8 | easy |
| 18 | Purpose of the contacts section | Ch 8 | easy |
| 19 | Purpose of the safety instructions section | Ch 8 | medium |
| 20 | How to verify correct contact information | Ch 6 | medium |
| 21 | Advanced solution: multisig with timelock | Ch 10 | hard |
| 22 | Cross-referencing assistant opinions | Ch 8 | medium |
| 23 | PIN vs passphrase documentation | Ch 7 | medium |
| 24 | 2FA backup considerations | Ch 7 | medium |
| 25 | What happens to exchange accounts after death | Ch 7 | medium |
| 26 | Hardware wallet documentation requirements | Ch 7 | medium |
| 27 | Mobile wallet documentation requirements | Ch 7 | easy |
| 28 | Why multiple copies of the letter | Ch 9 | easy |
| 29 | Informing heirs vs keeping contents secret | Ch 9 | medium |
| 30 | Legal integration considerations | Ch 9 | medium |
| 31 | Frequency of inheritance plan review | Ch 10 | easy |
| 32 | Triggers for updating the plan | Ch 10 | medium |
| 33 | Prerequisites for this course | Ch 1 | easy |
| 34 | What distinguishes Bitcoin from bank inheritance | Ch 2 | medium |
| 35 | Family dispute prevention | Ch 2 | medium |
| 36 | The "snapshot" approach to inventory | Ch 7 | medium |
| 37 | Why not to take action during inventory | Ch 7 | medium |
| 38 | Trust level assessment for assistants | Ch 6 | medium |
| 39 | Bitcoin knowledge assessment for assistants | Ch 6 | medium |
| 40 | Liana wallet as advanced solution | Ch 10 | hard |

---

### A8. Structural Fixes Required

| # | Issue | Location | Fix Required | Priority |
|---|-------|----------|--------------|----------|
| - | None | - | - | - |

**The course structure is fully compliant with PBN standards. No structural fixes are required.**

---

### A9. Work Summary for Phase B

**Before starting Phase B, complete these tasks:**

#### Critical (Must Do)
- [x] Verify course structure (COMPLETE - no issues found)
- [x] Verify isCourseConclusion tag (COMPLETE - present)

#### Images to Create (18-23 total)
- [ ] Ch 1: 0-1 images (optional course overview)
- [ ] Ch 2: 3-4 images (lost bitcoin, bank vs bitcoin, four goals)
- [ ] Ch 3: 4-5 images (5 myth-busting illustrations)
- [ ] Ch 4: 3-4 images (checklist, environment, timer)
- [ ] Ch 5: 3-4 images (profiles, wallet types, self-assessment)
- [ ] Ch 6: 4-5 images (roles, matrix, table, tasks, professionals)
- [ ] Ch 7: 4-5 images (categories, template, locations, snapshot, layers)
- [ ] Ch 8: 4-5 images (components, handwritten, balance, do/don't, envelope)
- [ ] Ch 9: 3-4 images (locations, checklist, tamper-evident)
- [ ] Ch 10: 1-2 images (advanced solutions, schedule)

#### Quizzes to Create (70 total)
- [ ] Ch 2: 5 quizzes (why inheritance matters)
- [ ] Ch 3: 5 quizzes (misconceptions)
- [ ] Ch 4: 5 quizzes (what you need)
- [ ] Ch 5: 5 quizzes (your profile)
- [ ] Ch 6: 4 quizzes (trusted assistants - has 1)
- [ ] Ch 7: 5 quizzes (inventory)
- [ ] Ch 8: 1 quiz (letter - has 4)
- [ ] Ch 9: 5 quizzes (review and store)
- [ ] Final exam pool: 40 quizzes (cross-chapter coverage)

---

**Phase A Status:** ✅ COMPLETE
**Phase A Completed:** 2026-01-21
**Notes:**
- Course structure is excellent and fully compliant with PBN standards
- Main gaps are in images (4 current, need ~22) and quizzes (5 current, need 75)
- Existing quizzes are concentrated on Ch 6 and Ch 8; other content chapters have none
- Image distribution is uneven; most chapters lack visual aids
- Content is well-organized following Pamela Morgan's methodology from "Cryptoasset Inheritance Planning"
