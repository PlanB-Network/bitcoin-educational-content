# BTC 102 Split Project - Master Plan

## Project Overview

**Objective**: Split the current BTC 102 course ("Getting your first bitcoins" - 14 hours) into 7 smaller, focused courses with ~5-minute content bites. Each new course will be standalone while maintaining coherence with the broader curriculum.

**Branch**: `split-btc102`

**Key Principles**:
1. Only modify English markdown files (`en.md`)
2. Keep original BTC 102 intact until all new courses are created
3. Document all content mappings for future multi-language bootstrap
4. Mark NEW content vs ORIGINAL content (from BTC102) clearly
5. Follow standard course structure (Introduction → Content Sections → Conclusion)
6. All courses are FREE

---

## Project Workflow

### Current Phase: Course Definition & Review
We are reviewing each of the 7 new courses one by one to define their detailed structure before any implementation begins.

### Course Review Status

| # | Course Code | Course Name | Review Status | Implementation Status | Notes |
|---|-------------|-------------|---------------|----------------------|-------|
| 1 | SCU102 | Financial Fraud, Scams & Online Security | ✅ REVIEWED | ✅ **IMPLEMENTED** | Completed 2026-01-19 |
| 2 | BTC103 | Why Bitcoin Matters | ✅ REVIEWED | ✅ **IMPLEMENTED** | Completed 2026-01-19 |
| 3 | BIZ102 | Bitcoin Industry Overview | ✅ REVIEWED | ✅ **IMPLEMENTED** | Completed 2026-01-19 |
| 4 | BTC105 | How to Acquire Bitcoin | ✅ REVIEWED | ✅ **IMPLEMENTED** | Completed 2026-01-20 |
| 5 | BTC104 | How to Secure Bitcoin | ✅ REVIEWED | ✅ **IMPLEMENTED** | Completed 2026-01-20 |
| 6 | SOV102 | Bitcoin Inheritance Planning | ✅ REVIEWED | ✅ **IMPLEMENTED** | Completed 2026-01-20 |
| 7 | BTC102v2 | Your First Bitcoin Journey (Hub) | NOT STARTED | - | **NEXT** (Created last) |

### After All Reviews Complete
Once all 7 courses have been reviewed and approved:
1. Set up implementation plan
2. Fork/create courses one at a time
3. Final cleanup

---

## Current BTC 102 Structure Analysis

| Part | Title | Chapters | Lines (approx) |
|------|-------|----------|----------------|
| Intro | Course overview | 1 | 23-74 |
| Part 1 | Prerequisites for understanding Bitcoin | Scams & fraud, Online security, Tips for newcomers | 75-549 |
| Part 2 | Understanding what you're getting into | Bitcoin in 5 min, Why BTC matters, BTC industry, Layered architecture | 550-1194 |
| Part 3 | Setting up your plan | Choose profile, Hodler, Stacker, Active User, Paranoid | 1195-2191 |
| Part 4 | Protecting Your Heirs and Wealth | Inheritance plan, Conclusion | 2192-2527 |
| Final | Reviews, Exam, Conclusion | 3 | 2528-2545 |

**Available Assets**: 28 language translations, 100+ images per language, quizzes (000-013+), videos

---

## Proposed New Courses (7 Total)

### Course 1: SCU102 - Financial Fraud, Scams & Online Security
**Discipline**: Security (SCU)
**Level**: Beginner (102)
**Estimated Duration**: 3 hours
**Source**: BTC102 Part 1 - ALL chapters (Scams, Online Security, Tips for newcomers)
**Review Status**: ✅ REVIEWED (2026-01-19)
**Implementation Doc**: [scu102-creation.md](scu102-creation.md)

---

#### Source Content Mapping (BTC102 en.md)

| BTC102 Chapter | Lines | Content |
|----------------|-------|---------|
| Scams and financial fraud | 79-234 | All fraud types, how to avoid scams |
| Online security | 236-373 | Cybersecurity basics, privacy |
| Tips for newcomers | 376-549 | Common mistakes, investment strategy, discretion |

---

#### Course Structure (Parts & Chapters)

The structure follows standard course format:
- `#` = Part (with `<partId>`)
- `##` = Chapter (with `<chapterId>`)
- `###` = Subsection within chapter

```
# Part 1: Introduction
└── ## Chapter 1: Introduction [NEW]

# Part 2: Financial Fraud
├── ## Chapter 2: Understanding Financial Fraud [ORIGINAL + NEW]
├── ## Chapter 3: Pyramid & Ponzi Schemes [ORIGINAL]
├── ## Chapter 4: Pump & Dump Schemes [ORIGINAL]
└── ## Chapter 5: Fake Giveaways & Lotteries [ORIGINAL]

# Part 3: Crypto Scams
├── ## Chapter 6: Shitcoins & Airdrops [ORIGINAL + NEW expansion]
├── ## Chapter 7: Phishing & Identity Theft [ORIGINAL]
├── ## Chapter 8: Bitcoin Hardforks Confusion [ORIGINAL]
└── ## Chapter 9: Dishonest Influencers [ORIGINAL]

# Part 4: How to Protect Yourself
└── ## Chapter 10: Red Flags & Verification [ORIGINAL]

# Part 5: Online Security
├── ## Chapter 11: Why Cybersecurity Matters [ORIGINAL]
├── ## Chapter 12: Clean Computer Practices [ORIGINAL]
├── ## Chapter 13: Password Security [ORIGINAL + SCU101 ref]
├── ## Chapter 14: Two-Factor Authentication [ORIGINAL + SCU101 ref]
├── ## Chapter 15: Privacy Protection [ORIGINAL + SCU101 ref]
└── ## Chapter 16: Step-by-Step Security Progression [ORIGINAL]

# Part 6: Tips for Bitcoin Beginners
├── ## Chapter 17: Common Mistakes to Avoid [ORIGINAL]
├── ## Chapter 18: Investment Strategy Basics [ORIGINAL]
├── ## Chapter 19: Understanding Volatility [ORIGINAL]
├── ## Chapter 20: Wallet Security Fundamentals [ORIGINAL]
├── ## Chapter 21: Confidentiality & Discretion [ORIGINAL]
├── ## Chapter 22: Tax Awareness [ORIGINAL]
├── ## Chapter 23: Trading vs Investing vs Holding [ORIGINAL]
└── ## Chapter 24: Going Further [ORIGINAL + NEW] ← Resources, golden rules, next steps

# Part 7: Conclusion
└── ## Chapter 25: Conclusion [STANDARDIZED - isCourseConclusion tag only]
```

**Total: 7 Parts, 25 Chapters**

---

#### Quiz Mapping (15 quizzes)

| Quiz # | Question Topic | Target Chapter |
|--------|----------------|----------------|
| 000 | Ponzi scheme characteristics | Ch 3: Pyramid & Ponzi |
| 001 | Phishing identification | Ch 7: Phishing |
| 002 | Donation scam precautions | Ch 5: Fake Giveaways |
| 003 | Pump & Dump definition | Ch 4: Pump & Dump |
| 004 | Ponzi scheme mechanism | Ch 3: Pyramid & Ponzi |
| 005 | Two-factor authentication | Ch 14: 2FA |
| 006 | Password manager advantages | Ch 13: Password Security |
| 007 | 3-2-1 backup rule | Ch 12: Clean Computer |
| 008 | System/software updates | Ch 12: Clean Computer |
| 009 | Online security importance | Ch 11: Why Cybersecurity |
| 010 | Discretion about holdings | Ch 21: Confidentiality |
| 011 | Protecting mnemonic phrase | Ch 20: Wallet Security |
| 012 | Self-custody definition | Ch 20: Wallet Security |
| 013 | Trading vs investing | Ch 23: Trading vs Investing |
| 014 | Invest what you can afford | Ch 18: Investment Strategy |

**Total quizzes for SCU102**: 15 (quizz 000-014)

---

#### Asset Mapping (25 images)

| BTC102 Image | SCU102 Image | Topic | Chapter |
|--------------|--------------|-------|---------|
| 005 | 001 | Bitcoin vs Crypto ecosystem | Ch 2 |
| 006 | 002 | Crypto ecosystem warning | Ch 2 |
| 007 | 003 | Ponzi/Pyramid diagram | Ch 3 |
| 008 | 004 | Pump & Dump cycle | Ch 4 |
| 009 | 005 | Signal groups warning | Ch 4 |
| 010 | 006 | Fake giveaway example | Ch 5 |
| 011 | 007 | Bitcoin hardforks diagram | Ch 8 |
| 012 | 008 | Dishonest influencers | Ch 9 |
| 013 | 009 | Clean computer/antivirus | Ch 12 |
| 014 | 010 | 3-2-1 Backup rule | Ch 12 |
| 015 | 011 | Password manager concept | Ch 13 |
| 016 | 012 | 2FA concept | Ch 14 |
| 017 | 013 | 2FA app screenshot | Ch 14 |
| 018 | 014 | SIM swap warning | Ch 14 |
| 019 | 015 | VPN concept | Ch 15 |
| 020 | 016 | Privacy tools summary | Ch 15 |
| 021 | 017 | Tips overview | Ch 17 |
| 022 | 018 | Common mistakes list | Ch 17 |
| 023 | 019 | Budget planning | Ch 18 |
| 024 | 020 | Volatility chart | Ch 19 |
| 025 | 021 | Seed phrase importance | Ch 20 |
| 026 | 022 | Not your keys warning | Ch 20 |
| 027 | 023 | Tax implications | Ch 22 |
| 028 | 024 | Tax calendar | Ch 22 |
| 029 | 025 | Learning resources | Ch 24 |

**Total images**: 25 (renumbered from BTC102 005-029 to SCU102 001-025)

---

#### Content Classification

| Content Type | Chapters | Notes |
|--------------|----------|-------|
| ORIGINAL (copy from BTC102) | Ch 2-5, 7-25 | Lines 79-549 restructured |
| NEW | Ch 1, 26 | Introduction, Next Steps |
| ORIGINAL + NEW expansion | Ch 6 | Shitcoins section needs expansion |
| ORIGINAL + SCU101 refs | Ch 13, 14, 15 | Add cross-references to tutorials |

---

#### SCU101 Cross-Reference Strategy

For chapters 13, 14, 15, add reference boxes pointing to SCU101 tutorials:
- Ch 13: Bitwarden/KeePass tutorials
- Ch 14: Authy 2FA tutorial
- Ch 15: IVPN/Mullvad VPN tutorials, Tor browser

SCU102 explains **why** these tools matter; SCU101 shows **how** to set them up.

---

#### Implementation Checklist

See [scu102-creation.md](scu102-creation.md) for detailed implementation steps.

---

### Course 2: BTC103 - Why Bitcoin Matters
**Discipline**: Bitcoin (BTC)
**Level**: Beginner (103)
**Estimated Duration**: 2 hours
**Source**: BTC102 Part 2 - "Bitcoin in 5 minutes" + "Why is Bitcoin important?" chapters (lines 554-841)
**Review Status**: ✅ REVIEWED (2026-01-19)
**Implementation Status**: ✅ **IMPLEMENTED** (2026-01-19)
**Implementation Doc**: [btc103-creation.md](btc103-creation.md)

---

#### Source Content Mapping (BTC102 en.md)

| BTC102 Chapter | Lines | Content |
|----------------|-------|---------|
| Bitcoin in 5 minutes | 554-701 | Origins, Cypherpunks, blockchain, mining, monetary properties |
| Why is Bitcoin important? | 702-841 | Universal currency, protection against crises, sound money |

---

#### Course Structure (4 Parts, 9 Chapters)

```
# Part 1: Introduction
└── ## Chapter 1: Welcome to ECO105 [NEW]

# Part 2: Bitcoin in 5 Minutes
├── ## Chapter 2: The Origins [ORIGINAL: lines 564-604]
├── ## Chapter 3: A Decentralized Network [ORIGINAL: lines 605-636]
├── ## Chapter 4: Monetary Properties & Transparency [ORIGINAL: lines 637-672]
└── ## Chapter 5: Use Cases [ORIGINAL: lines 673-695]

# Part 3: Why Bitcoin Matters
├── ## Chapter 6: A Universal Currency [ORIGINAL: lines 710-728]
├── ## Chapter 7: Protection Against Crises [ORIGINAL: lines 730-776]
└── ## Chapter 8: Sound Money & Political Movement [ORIGINAL: lines 778-841]

# Part 4: Conclusion
└── ## Chapter 9: Conclusion [STANDARD]
```

---

#### Quiz Mapping (9 quizzes)

| BTC102 Quiz | BTC103 Quiz | Question Topic | Target Chapter |
|-------------|-------------|----------------|----------------|
| 015 | 000 | Bitcoin in 5 min | Ch 2: The Origins |
| 016 | 001 | Bitcoin in 5 min | Ch 2: The Origins |
| 017 | 002 | Bitcoin in 5 min | Ch 2: The Origins |
| 018 | 003 | Bitcoin in 5 min | Ch 2: The Origins |
| 019 | 004 | Bitcoin in 5 min | Ch 2: The Origins |
| 020 | 005 | Why Bitcoin matters | Ch 6: A Universal Currency |
| 021 | 006 | Why Bitcoin matters | Ch 6: A Universal Currency |
| 022 | 007 | Why Bitcoin matters | Ch 6: A Universal Currency |
| 023 | 008 | Why Bitcoin matters | Ch 6: A Universal Currency |

---

#### Asset Mapping (24 images)

| BTC102 Image | BTC103 Image | Topic |
|--------------|--------------|-------|
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

#### Implementation Checklist

- [x] Create `courses/eco105/` folder
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
- [x] Update quiz chapterIds
- [x] Validate markdown

---

### Course 3: BIZ102 - Bitcoin Industry Overview
**Discipline**: Business (BIZ)
**Level**: Beginner (102)
**Estimated Duration**: 2 hours
**Source**: BTC102 Part 2 - "Understanding the Bitcoin industry" + "Layered Architecture" chapters (lines 844-1194)
**Review Status**: ✅ REVIEWED (2026-01-19)
**Implementation Status**: ✅ **IMPLEMENTED** (2026-01-19)
**Implementation Doc**: [biz102-creation.md](biz102-creation.md)

---

#### Source Content Mapping (BTC102 en.md)

| BTC102 Chapter | Lines | Content |
|----------------|-------|---------|
| Understanding the Bitcoin industry | 844-1086 | Industry birth, altcoins, institutions, regulation, banks, exchanges, wallets, mining, development |
| The Layered Architecture of Bitcoin | 1087-1194 | Lightning Network, Sidechains, RGB, Merchant tools, Personal perspective |

---

#### Course Structure (5 Parts, 12 Chapters)

```
# Part 1: Introduction
└── ## Chapter 1: Welcome to BIZ102 [NEW]

# Part 2: Birth of a Global Industry
├── ## Chapter 2: A Radical Innovation [ORIGINAL: lines 850-866]
├── ## Chapter 3: The Proliferation of Altcoins [ORIGINAL: lines 867-903]
└── ## Chapter 4: Institutional Adoption [ORIGINAL: lines 905-922]

# Part 3: Industry Infrastructure
├── ## Chapter 5: Regulation & Government Approaches [ORIGINAL: lines 925-941]
├── ## Chapter 6: Banks' Stance on Bitcoin [ORIGINAL: lines 943-948]
├── ## Chapter 7: Cryptocurrency Exchanges & Custody [ORIGINAL: lines 949-1024]
└── ## Chapter 8: Wallets, Mining & Development [ORIGINAL: lines 1026-1084]

# Part 4: Bitcoin's Layered Architecture
├── ## Chapter 9: Extension Layers [ORIGINAL: lines 1092-1143]
├── ## Chapter 10: Merchant Tools [ORIGINAL: lines 1144-1172]
└── ## Chapter 11: Going Further [ORIGINAL: lines 1181-1191 + NEW]

# Part 5: Conclusion
└── ## Chapter 12: Conclusion [STANDARD - isCourseConclusion tag only]
```

**Total: 5 Parts, 12 Chapters**

---

#### Quiz Mapping (10 quizzes)

| BTC102 Quiz | BIZ102 Quiz | Question Topic | Target Chapter |
|-------------|-------------|----------------|----------------|
| 025 | 000 | Bitcoin vs altcoins (decentralization) | Ch 3: Proliferation of Altcoins |
| 026 | 001 | Private keys ownership | Ch 7: Exchanges & Custody |
| 027 | 002 | Bitcoin Core maintainers (5 in 2025) | Ch 8: Development |
| 028 | 003 | P2P platforms & KYC | Ch 7: Exchanges & Custody |
| 029 | 004 | Bitmain/ASICs mining | Ch 8: Mining |
| 030 | 005 | Layered approach benefits | Ch 9: Extension Layers |
| 031 | 006 | Sidechains (Liquid, RSK) | Ch 9: Extension Layers |
| 032 | 007 | RGB Single-use Seal | Ch 9: Extension Layers |
| 033 | 008 | Lightning Network inventors | Ch 9: Extension Layers |
| 034 | 009 | Lightning Network payments | Ch 9: Extension Layers |

---

#### Asset Mapping (11 images)

| BTC102 Image | BIZ102 Image | Topic | Chapter |
|--------------|--------------|-------|---------|
| 054 | 001 | Birth of global industry | Ch 2: Radical Innovation |
| 055 | 002 | Institutional adoption table | Ch 4: Institutional Adoption |
| 056 | 003 | Regulation/government | Ch 5: Regulation |
| 057 | 004 | Government approaches | Ch 5: Regulation |
| 058 | 005 | KYC platforms | Ch 7: Exchanges |
| 059 | 006 | Bitcoin development | Ch 8: Development |
| 060 | 007 | Bitcoin Core maintainers | Ch 8: Development |
| 061 | 008 | Lightning Network | Ch 9: Extension Layers |
| 062 | 009 | RGB protocol | Ch 9: Extension Layers |
| 063 | 010 | Layered design | Ch 9: Extension Layers |
| 064 | 011 | Bitcoin highway | Ch 11: Going Further |

**Total images**: 11 (renumbered from BTC102 054-064 to BIZ102 001-011)

---

#### Implementation Checklist

- [x] Create `courses/biz102-new/` folder
- [x] Create `course.yml` with UUID
- [x] Copy images (054-064 → 001-011)
- [x] Copy quizzes (025-034 → 000-009)
- [x] Create `en.md` with frontmatter
- [x] Write NEW intro chapter
- [x] Copy Part 2 content (Birth of Global Industry)
- [x] Copy Part 3 content (Industry Infrastructure)
- [x] Copy Part 4 content (Layered Architecture)
- [x] Add "Going Further" chapter
- [x] Add conclusion chapter
- [x] Update all image references
- [x] Add ORIGINAL/NEW tags
- [x] Update quiz chapterIds
- [x] Validate markdown structure

---

### Course 4: BTC105 - How to Acquire Bitcoin
**Discipline**: Bitcoin (BTC)
**Level**: Beginner (105)
**Estimated Duration**: 2-2.5 hours
**Source**: BTC102 Part 3 - "Setting up your plan" (lines 1195-2191)
**Review Status**: ✅ REVIEWED (2026-01-19)
**Implementation Doc**: [btc105-creation.md](btc105-creation.md)

---

#### Source Content Mapping (BTC102 en.md)

| BTC102 Section | Lines | Content |
|----------------|-------|---------|
| Choose your profile intro | 1199-1283 | Factors for choosing strategy, risks, lifestyle |
| Wallets and Security Strategies | 1286-1386 | Wallet types overview (partial - security to BTC104) |
| Methods of Acquisition | 1388-1441 | KYC vs No-KYC methods |
| The 4 Types of Bitcoin Users | 1443-1507 | Profile overview |
| The Hodler | 1509-1631 | Long-term investment (extract acquisition parts) |
| The Stacker | 1633-1781 | DCA strategy (core of BTC105) |
| The Active User | 1783-1974 | Daily use, earning BTC (extract acquisition parts) |
| The Paranoid | 1976-2190 | Privacy-focused acquisition (extract acquisition parts) |

---

#### Course Structure (6 Parts, 14 Chapters)

```
# Part 1: Introduction
└── ## Chapter 1: Welcome to BTC105 [NEW]

# Part 2: Understanding Your Profile
├── ## Chapter 2: Why Define Your User Profile? [ORIGINAL: lines 1199-1229]
├── ## Chapter 3: Potential Risks and Lifestyle [ORIGINAL: lines 1231-1275]
└── ## Chapter 4: The Four Bitcoin User Profiles [ORIGINAL: lines 1443-1507]

# Part 3: Acquisition Methods
├── ## Chapter 5: Wallet Basics for Acquisition [ORIGINAL: lines 1286-1386 - partial]
├── ## Chapter 6: Buying with Identity Verification (KYC) [ORIGINAL: lines 1394-1417]
└── ## Chapter 7: Buying Without Identity Verification (No-KYC) [ORIGINAL: lines 1419-1441]

# Part 4: Acquisition Strategies by Profile
├── ## Chapter 8: The Hodler's Acquisition Strategy [ORIGINAL: extracted from Hodler chapter]
├── ## Chapter 9: The Stacker's DCA Strategy [ORIGINAL: lines 1633-1781]
├── ## Chapter 10: The Active User's Acquisition Approach [ORIGINAL: extracted]
└── ## Chapter 11: The Paranoid User's Anonymous Acquisition [ORIGINAL: extracted]

# Part 5: Practical Implementation
├── ## Chapter 12: Setting Up Your First Purchase [NEW + ORIGINAL]
└── ## Chapter 13: Going Further [NEW + ORIGINAL]

# Part 6: Conclusion
└── ## Chapter 14: Conclusion [STANDARD - isCourseConclusion tag]
```

**Total: 6 Parts, 14 Chapters**

---

#### Quiz Mapping (Estimated 17 quizzes)

| BTC102 Quiz | Topic | BTC105 Quiz | Target Chapter |
|-------------|-------|-------------|----------------|
| 035 | User profile factors | 000 | Ch 2/3: Profile |
| 036 | Investment considerations | 001 | Ch 2/3: Profile |
| 037 | Wallet selection | 002 | Ch 5: Wallet Basics |
| 039 | Acquisition basics | 003 | Ch 6/7: Acquisition |
| 040-042 | Hodler principles | 004-006 | Ch 8: Hodler |
| 045-049 | Stacker/DCA | 007-011 | Ch 9: Stacker |
| 050-052 | Active User | 012-014 | Ch 10: Active User |
| 055-056 | Paranoid buying | 015-016 | Ch 11: Paranoid |

**Note**: Security-focused quizzes (038, 043-044, 053-054, 057-059) go to BTC104.

---

#### Asset Mapping (Estimated 27 images)

| BTC102 Range | Topic | BTC105 Range |
|--------------|-------|--------------|
| 065-069 | Profile/Risk | 001-005 |
| 070-073 | Wallet/Acquisition | 006-009 |
| 074 | Four profiles | 010 |
| 075, 077-079 | Hodler | 011-014 |
| 080, 082-084 | Stacker | 015-018 |
| 085-086, 088-090 | Active User | 019-023 |
| 091-092, 095-096 | Paranoid | 024-027 |

**Note**: Security-focused images (076, 081, 087, 093-094) go to BTC104.

---

#### Implementation Checklist

- [ ] Create `courses/btc105/` folder
- [ ] Create `course.yml` with UUID
- [ ] Copy relevant images (065-096, exclude security-focused)
- [ ] Copy/assign quizzes (acquisition-related only)
- [ ] Create `en.md` with frontmatter
- [ ] Write NEW intro chapter
- [ ] Copy profile content (Part 2)
- [ ] Copy acquisition methods (Part 3)
- [ ] Extract acquisition strategies from profile chapters (Part 4)
- [ ] Write practical implementation chapter
- [ ] Add "Going Further" chapter with BTC104 cross-reference
- [ ] Add conclusion chapter
- [ ] Update all image references
- [ ] Add ORIGINAL/NEW tags
- [ ] Update quiz chapterIds
- [ ] Validate markdown structure

---

### Course 5: BTC104 - How to Secure Bitcoin
**Discipline**: Bitcoin (BTC)
**Level**: Beginner (104)
**Estimated Duration**: 1.5-2 hours
**Source**: BTC102 Part 3 - Wallet and security sections (lines 1286-1386, 1552-1555)
**Review Status**: ✅ REVIEWED (2026-01-20)
**Implementation Status**: ✅ **IMPLEMENTED** (2026-01-20)
**Implementation Doc**: [btc104-creation.md](btc104-creation.md)

---

#### Course Philosophy

**Target Audience**: Complete beginners who just acquired (or are about to acquire) their first bitcoin.

**Goal**: A step-by-step guide through the ENTIRE process:
1. Understanding what wallets are
2. Choosing the right wallet for their situation
3. Setting up their first wallet
4. Securing their seed phrase properly
5. Receiving bitcoin (from exchange or third party)
6. Best practices moving forward

**What this course is NOT**:
- An advanced security encyclopedia (multisig, nodes, etc.)
- A course for people with large holdings
- Comprehensive coverage of all security options

**Approach**: Keep it simple, practical, and actionable. Complex topics mentioned briefly with placeholders for future advanced courses.

---

#### Source Content Mapping (BTC102 en.md)

| BTC102 Section | Lines | Relevant Content |
|----------------|-------|------------------|
| Wallets and Security Strategies | 1286-1386 | Hot/cold wallets overview |
| Backup tutorial reference | 1384-1386, 1552-1555 | Seed phrase basics |
| Hodler chapter | 1536-1564 | Hardware wallet setup |
| Stacker chapter | 1662-1700 | Hot wallet recommendations, transfer to hardware |

---

#### Course Structure (5 Parts, 14 Chapters)

```
# Part 1: Introduction
└── ## Chapter 1: Welcome to BTC104 [NEW]
└── ## Chapter 2: Why You Need Your Own Wallet [ORIGINAL + NEW]

# Part 2: Understanding Wallets
├── ## Chapter 3: What Is a Bitcoin Wallet? [NEW + concepts]
├── ## Chapter 4: Types of Wallets [ORIGINAL: lines 1292-1371 adapted]
└── ## Chapter 5: Custodial vs Self-Custody [ORIGINAL: lines 1351-1371]

# Part 3: Setting Up Your First Wallet
├── ## Chapter 6: Choosing Your First Wallet [NEW]
├── ## Chapter 7: Creating Your Wallet [NEW + tutorial refs]
├── ## Chapter 8: Securing Your Seed Phrase [ORIGINAL + NEW]
└── ## Chapter 9: Receiving Your First Bitcoin [NEW + ORIGINAL adapted]

# Part 4: Best Practices & Growing Your Security
├── ## Chapter 10: Security Best Practices [NEW]
├── ## Chapter 11: When to Upgrade Your Security [ORIGINAL adapted]
└── ## Chapter 12: Common Mistakes and How to Avoid Them [NEW]

# Part 5: Conclusion
├── ## Chapter 13: Your Security Journey [NEW]
└── ## Chapter 14: Conclusion [STANDARD - isCourseConclusion tag]
```

**Total: 5 Parts, 14 Chapters**

---

#### Quiz Mapping (3 quizzes from BTC102)

| BTC102 Quiz | BTC104 Quiz | Topic | Target Chapter |
|-------------|-------------|-------|----------------|
| 037 | 000 | Wallet selection | Ch 4: Types of Wallets |
| 047 | 001 | Hardware wallet for long-term | Ch 11: Upgrading Security |
| 045 | 002 | Hot → Hardware transfer | Ch 11: Upgrading Security |

**Note**: Advanced quizzes (055 metal backup, 058 air-gapped) saved for future advanced course.

---

#### Asset Mapping (3 images)

| BTC102 Image | BTC104 Image | Topic | Chapter |
|--------------|--------------|-------|---------|
| 070 | 001 | Wallet overview diagram | Ch 3: What Is a Wallet |
| 071 | 002 | Hot/Cold comparison | Ch 4: Types of Wallets |
| 072 | 003 | Hybrid approach diagram | Ch 11: When to Upgrade |

---

#### Tutorial Cross-References

**Hot Wallet Tutorials** (Primary - for beginners):
- green (Blockstream Green)
- blue-wallet
- sparrow (desktop)

**Hardware Wallet Tutorials** (Mentioned for "when to upgrade"):
- ledger-nano-s-plus, ledger-flex, trezor, bitbox02, jade-plus-green

**Backup Tutorial**:
- backup-mnemonic (critical for Ch 8)

---

#### Implementation Checklist

- [x] Create `courses/btc104/` folder
- [x] Create `course.yml` with UUID
- [x] Copy images (070-072 → 001-003)
- [x] Copy quizzes (037, 045, 047 → 000-002)
- [x] Create `en.md` with frontmatter
- [x] Write NEW chapters (1, 3, 6, 7, 9, 10, 12, 13)
- [x] Adapt ORIGINAL content (2, 4, 5, 8, 11)
- [x] Add conclusion chapter with isCourseConclusion tag
- [x] Update all image references
- [x] Add ORIGINAL/NEW tags
- [x] Update quiz chapterIds
- [x] Validate markdown structure

---

#### Future Advanced Security Course (Placeholder)

Topics saved for a future **BTC2XX - Advanced Bitcoin Security** course:
- Multisignature wallets (detailed setup)
- BIP39 passphrases
- Metal seed backups
- Running your own node
- Air-gapped devices
- Advanced UTXO management

This keeps BTC104 focused and beginner-friendly.

---

### Course 6: SOV102 - Bitcoin Inheritance Planning
**Discipline**: Sovereignty (SOV)
**Level**: Beginner (102)
**Estimated Duration**: 1-1.5 hours
**Source**: BTC102 Part 4 - "Protecting Your Heirs and Wealth" (lines 2192-2420)
**Review Status**: ✅ REVIEWED (2026-01-20)
**Implementation Status**: ✅ **IMPLEMENTED** (2026-01-20)
**Implementation Doc**: [sov102-creation.md](sov102-creation.md)

---

#### Source Content Mapping (BTC102 en.md)

| BTC102 Section | Lines | Content |
|----------------|-------|---------|
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

---

#### Course Structure (5 Parts, 11 Chapters)

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
└── Ch 11: Conclusion [STANDARD - isCourseConclusion tag]
```

**Total: 5 Parts, 11 Chapters**

---

#### Quiz Mapping (5 quizzes)

| BTC102 Quiz | SOV102 Quiz | Question Topic | Target Chapter |
|-------------|-------------|----------------|----------------|
| 060 | 000 | Role of inheritance letter | Ch 8: Write the Letter |
| 061 | 001 | Why handwritten on paper | Ch 8: Write the Letter |
| 062 | 002 | Not giving mnemonic to one person | Ch 6: Trusted Assistants |
| 063 | 003 | Risk of too much info disclosure | Ch 8: Write the Letter |
| 064 | 004 | Clear instructions essential | Ch 8: Write the Letter |

---

#### Asset Mapping (4 images)

| BTC102 Image | SOV102 Image | Topic | Chapter |
|--------------|--------------|-------|---------|
| 097 | 001 | Pamela Morgan's book cover | Ch 2: Why Inheritance Matters |
| 098 | 002 | Cédric's profile diagram | Ch 5: Understanding Your Profile |
| 099 | 003 | Tools needed | Ch 4: What You'll Need |
| 100 | 004 | Sealed envelope storage | Ch 9: Review and Store |

**Total images**: 4 (renumbered from BTC102 097-100 to SOV102 001-004)

---

#### Implementation Checklist

- [x] Create `courses/sov102/` folder
- [x] Create `course.yml` with UUID
- [x] Copy images (097-100 → 001-004)
- [x] Copy quizzes (060-064 → 000-004)
- [x] Create `en.md` with frontmatter
- [x] Write NEW intro chapter
- [x] Copy Part 2 content (Preparation)
- [x] Copy Part 3 content (Creating Your Plan)
- [x] Copy Part 4 content (Finalize and Maintain)
- [x] Add "Going Further" chapter
- [x] Add conclusion chapter with isCourseConclusion tag
- [x] Update all image references
- [x] Add ORIGINAL/NEW tags
- [x] Update quiz chapterIds
- [x] Validate markdown structure

---

### Course 7: BTC102v2 - Your First Bitcoin Journey (Hub Course)
**Discipline**: Bitcoin (BTC)
**Level**: Beginner (102)
**Estimated Duration**: 1-2 hours
**Source**: NEW content + navigation guide
**Review Status**: NOT STARTED
**Note**: This course is created LAST after all others are complete

**Proposed Structure**:
- Section 1: Introduction
  - Course overview (shortened)
  - Learning path overview
- Section 2: Quick Start Guide
  - Condensed Bitcoin basics (link to BTC101)
  - Your first steps
- Section 3: Your Learning Path
  - Profile quiz
  - Recommended course sequence
- Section 4: Course Directory
  - Links to all split courses with descriptions
- Section 5: Conclusion
  - Next steps
  - Resources

**Detailed Review Notes**:
*(To be filled during in-depth review session)*

---

## Content Mapping & Tracking System

### Tagging Convention for Content Origin

When creating new courses, all content will be tagged:

```markdown
<!-- ORIGINAL: btc102/en.md lines XXX-YYY -->
[Original content here]
<!-- END ORIGINAL -->

<!-- NEW -->
[Newly written content here]
<!-- END NEW -->
```

This allows:
1. Clear tracking of what came from BTC102
2. Future automated splitting of other language files
3. Translation teams to know what needs fresh translation vs reuse

### Course Structure Formatting Rules

**CRITICAL**: The desktop app has specific rendering rules that must be followed:

1. **No text between Part and first Chapter**: Text placed between a `# Part Name` and the first `## Chapter Name` will NOT be displayed in the desktop app. Part introductions must go inside the first chapter of that part.

   ```markdown
   # Part Name

   <partId>part-id</partId>

   This text WILL NOT be shown in the app!  ❌

   ## First Chapter
   ```

   **Correct format:**
   ```markdown
   # Part Name

   <partId>part-id</partId>

   ## First Chapter

   <chapterId>chapter-id</chapterId>

   Introduction text goes here inside the chapter. ✅
   ```

2. **Part separators**: The `#` heading itself is the part separator. Do NOT use `+++` between parts. The `+++` is only used once in some courses to separate a course intro text block (before any `#`) from the first `# Part`. If your course starts directly with `# Part`, no `+++` is needed.

3. **IDs are required**: Every `#` part needs a `<partId>` and every `##` chapter needs a `<chapterId>`.

4. **Standardized Conclusion Format**: Every course must end with a standardized conclusion section. Do NOT create custom conclusion content with multiple chapters. Instead:

   ```markdown
   ## Going Further

   <chapterId>going-further-ch##</chapterId>

   [Content about next steps, resources, golden rules, etc. goes here as a regular chapter in the last content Part]

   # Conclusion

   <partId>conclusion-part#</partId>

   ## Conclusion

   <chapterId>conclusion-ch##</chapterId>
   <isCourseConclusion>true</isCourseConclusion>
   ```

   **Key rules:**
   - The `# Conclusion` Part should contain ONLY the `## Conclusion` chapter
   - The `<isCourseConclusion>true</isCourseConclusion>` tag is REQUIRED
   - All "going further", "next steps", "golden rules", and similar content should go in a **chapter** (not section) called "Going Further" as the LAST chapter of the previous Part
   - Do NOT create elaborate conclusion content - the standardized conclusion is intentionally minimal

---

## Quiz Mapping

| Original Quiz | Target Course | Notes |
|---------------|---------------|-------|
| 000 | TBD | Needs content review |
| 001 | TBD | Needs content review |
| 002 | TBD | Needs content review |
| ... | ... | ... |

*Quiz content needs to be analyzed and mapped to appropriate new courses*

---

## Asset Mapping

| Image Range | Topic | Target Course |
|-------------|-------|---------------|
| 001-004 | Course overview | BTC102v2 |
| 005-0XX | Scams/fraud/security | SCU102 |
| ... | ... | ... |

*Full asset mapping to be completed during each course's in-depth review*

---

## Implementation Plan of Action

### Phase 1: Documentation & Planning
- [x] Analyze BTC102 structure
- [x] Define 7 new courses
- [x] Create this master plan document
- [x] Finalize course codes
- [x] Merge SCU103 into SCU102

### Phase 2: In-Depth Course Reviews (CURRENT PHASE)
Review each course one by one to:
- Define exact content mapping from BTC102
- Identify what's NEW vs ORIGINAL content
- Map specific assets (images)
- Map specific quizzes
- Finalize section structure
- Note any dependencies or cross-references

**Review Order**:
1. [x] SCU102 - Financial Fraud, Scams & Online Security ✅ **IMPLEMENTED**
2. [x] BTC103 - Why Bitcoin Matters ✅ **IMPLEMENTED**
3. [x] BIZ102 - Bitcoin Industry Overview ✅ **IMPLEMENTED**
4. [x] BTC105 - How to Acquire Bitcoin ✅ **IMPLEMENTED**
5. [x] BTC104 - How to Secure Bitcoin ✅ **IMPLEMENTED**
6. [x] SOV102 - Bitcoin Inheritance Planning ✅ **IMPLEMENTED**
7. [ ] BTC102v2 - Hub Course ← **NEXT**

### Phase 3: Course Creation (After all reviews approved)
For each course:
1. Create course folder (`courses/XXX###/`)
2. Create `course.yml` with proper metadata
3. Create `en.md` with tagged content
4. Copy relevant assets to new `assets/` folder
5. Map relevant quizzes
6. Create placeholder for: thumbnail, videos
7. Review and validate structure

**Implementation Order** (after all reviews complete):
1. SCU102 (Financial Fraud, Scams & Online Security)
2. BTC103 (Why Bitcoin Matters)
3. BIZ102 (Industry Overview)
4. BTC105 (How to Acquire)
5. BTC104 (How to Secure)
6. SOV102 (Inheritance Planning)
7. BTC102v2 (Hub course) - created last, ties everything together

### Phase 3: BTC102 Revision
- Create BTC102 v2 as navigation/hub course
- Keep original BTC102 files untouched until v2 is validated
- Implement v2 as replacement

### Phase 4: Cleanup
- Remove temporary files/tools created during split
- Final validation
- PR preparation

---

## Decisions Made

| Decision | Outcome | Date |
|----------|---------|------|
| SCU103 merged into SCU102 | Online security content combined with fraud/scams into single SCU102 course | 2026-01-19 |
| Course codes finalized | SCU102, ECO105, BIZ102, BTC103, BTC104, SOV102, BTC102v2 | 2026-01-19 |

## Open Questions (To Address During Reviews)

1. **Video Strategy**: New videos will be created - should placeholder chapters be marked?

2. **Quiz Splitting**: Should quizzes be reviewed and split now or during each course review?

3. **Thumbnail Creation**: Handle separately or use placeholders?

4. **SCU102 vs SCU101 overlap**: Ensure SCU102 references SCU101 for technical tools, doesn't duplicate

---

## Standard Course Structure Requirements

### Required course.yml Fields

Every course MUST have these fields in `course.yml`:

```yaml
# REQUIRED FIELDS
id: [UUID]                    # Unique identifier (generate with uuidgen or Python uuid)
topic: [string]               # bitcoin, business, mining, protocol, security, sociology, sovereignty
subtopic: [string]            # Specific subtopic within the topic
type: [theory|practice]       # Course type
level: [beginner|intermediate|expert|wizard]  # Difficulty level
hours: [number]               # Estimated completion time
teaching_format: [self_paced|professor_led]   # Teaching format

professors_id:                # List of professor UUIDs
  - [UUID]
contributor_names:            # List of contributor names
  - [name]

original_language: [lang]     # Original language code (e.g., "en")
proofreading:                 # At minimum, the original language
  - language: [lang]
    last_contribution_date:
    urgency: 1
    contributor_names:
    reward: 0

# OPTIONAL FIELDS (add when ready)
published_at: [YYYY-MM-DD]    # Publication date
project_id: [UUID]            # Project identifier
tags:                         # Searchable tags
  - [tag1]
  - [tag2]
videos:                       # Video metadata (add when videos created)
  - id: [UUID]
    youtube:
      - [lang]: [youtube_id]
```

### Required Markdown Structure

Every course `en.md` MUST follow this structure:

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

[Content here]

# Conclusion
<partId>conclusion-part#</partId>

## Conclusion
<chapterId>conclusion-ch##</chapterId>
<isCourseConclusion>true</isCourseConclusion>
```

### Required Directory Structure

```
courses/[course-code]/
├── course.yml           # REQUIRED - Course metadata
├── en.md                # REQUIRED - English content (minimum)
├── [lang].md            # OPTIONAL - Translations (fr.md, de.md, etc.)
├── assets/
│   ├── en/              # REQUIRED - English assets
│   │   ├── 001.webp
│   │   └── ...
│   ├── [lang]/          # OPTIONAL - Translated assets
│   └── thumbnail.webp   # OPTIONAL - Course thumbnail
└── quizz/
    ├── 000/
    │   ├── question.yml  # Quiz metadata
    │   ├── en.yml        # English answers
    │   └── [lang].yml    # Translated answers
    └── .../
```

---

## File Structure Preview

```
courses/
├── btc102/          # KEEP INTACT until v2 ready - DO NOT MODIFY
│   ├── course.yml
│   ├── en.md        # Source file for splitting
│   ├── [28 language files]
│   ├── assets/
│   └── quizz/
│
├── scu102-new/      # NEW - Financial Fraud, Scams & Online Security
│   ├── course.yml   # ✅ Has id, type, teaching_format
│   ├── en.md        # ✅ Correct structure (7 parts, 25 chapters)
│   ├── assets/
│   │   └── en/      # ✅ 25 images (001-025.webp)
│   └── quizz/       # ✅ 15 quizzes (000-014)
│
├── btc103-new/      # NEW - Why Bitcoin Matters ✅ IMPLEMENTED
│   ├── course.yml   # ✅ Has id, type, teaching_format
│   ├── en.md        # ✅ Correct structure (4 parts, 9 chapters)
│   ├── assets/
│   │   └── en/      # ✅ 24 images (001-024.webp)
│   └── quizz/       # ✅ 9 quizzes (000-008)
│
├── biz102-new/      # NEW - Bitcoin Industry Overview ✅ IMPLEMENTED
│   ├── course.yml   # ✅ Has id, type, teaching_format
│   ├── en.md        # ✅ Correct structure (5 parts, 12 chapters)
│   ├── assets/
│   │   └── en/      # ✅ 11 images (001-011.webp)
│   └── quizz/       # ✅ 10 quizzes (000-009)
│
├── btc105/          # NEW - How to Acquire Bitcoin ✅ IMPLEMENTED
│   ├── course.yml   # ✅ Has id, type, teaching_format
│   ├── en.md        # ✅ Correct structure (6 parts, 18 chapters)
│   ├── assets/
│   │   └── en/      # ✅ 4 images (001-004.webp)
│   └── quizz/       # ✅ 9 quizzes (000-008)
│
├── btc104/          # NEW - How to Secure Bitcoin ✅ IMPLEMENTED
│   ├── course.yml   # ✅ Has id, type, teaching_format
│   ├── en.md        # ✅ Correct structure (5 parts, 14 chapters)
│   ├── assets/
│   │   └── en/      # ✅ 3 images (001-003.webp)
│   └── quizz/       # ✅ 3 quizzes (000-002)
│
├── sov102/          # NEW - Bitcoin Inheritance Planning ✅ IMPLEMENTED
│   ├── course.yml   # ✅ Has id, type, teaching_format
│   ├── en.md        # ✅ Correct structure (5 parts, 11 chapters)
│   ├── assets/
│   │   └── en/      # ✅ 4 images (001-004.webp)
│   └── quizz/       # ✅ 5 quizzes (000-004)
│
└── btc102v2/        # LAST - Hub course (replaces btc102 eventually)
```

---

## Document History

| Date | Author | Changes |
|------|--------|---------|
| 2026-01-19 | Claude/Rogzy | Initial plan creation |
| 2026-01-19 | Claude/Rogzy | Merged SCU103 into SCU102, finalized course codes, added review status tracking |
| 2026-01-19 | Claude/Rogzy | **REVISED** SCU102 review: 7 Parts, 26 Chapters, 15 quizzes (000-014), 25 images. Created scu102-creation.md implementation doc |
| 2026-01-19 | Claude/Rogzy | **IMPLEMENTED** SCU102: Created folder structure, en.md (with ORIGINAL/NEW tags), copied quizzes (000-014), copied & renumbered assets (005-029 → 001-025). Ready for review. |
| 2026-01-19 | Claude/Rogzy | **STRUCTURE AUDIT**: Renamed scu201-new → scu102-new. Added missing course.yml fields (id, type, teaching_format). Added "Standard Course Structure Requirements" section documenting required fields, markdown structure, and directory layout for all future courses. |
| 2026-01-19 | Claude/Rogzy | **IMPLEMENTED** ECO105: Created folder structure, en.md (with ORIGINAL/NEW tags), copied quizzes (015-023 → 000-008), copied & renumbered assets (030-053 → 001-024), updated quiz chapterIds. 4 Parts, 9 Chapters, 9 quizzes, 24 images. |
| 2026-01-19 | Claude/Rogzy | **RENAMED** ECO105 → BTC103-new: Renamed folder eco105 to btc103-new, updated btc103-creation.md (formerly eco105-creation.md), updated all references in master plan. |
| 2026-01-19 | Claude/Rogzy | **FIX** Course code conflict: Renamed "How to Acquire Bitcoin" from BTC103 → BTC105 to avoid conflict with renamed "Why Bitcoin Matters" course. |
| 2026-01-19 | Claude/Rogzy | **IMPLEMENTED** BIZ102: Created folder structure, en.md (with ORIGINAL/NEW tags), copied quizzes (025-034 → 000-009), copied & renumbered assets (054-064 → 001-011), updated quiz chapterIds. 5 Parts, 12 Chapters, 10 quizzes, 11 images. Created biz102-creation.md implementation doc. |
| 2026-01-19 | Claude/Rogzy | **REVIEWED** BTC105: In-depth review completed. 6 Parts, 14 Chapters, ~17 quizzes, ~27 images. Source: BTC102 Part 3 lines 1195-2191. Note: BTC105 (acquisition) and BTC104 (security) share source content - extraction approach documented. Created btc105-creation.md implementation doc. |
| 2026-01-20 | Claude/Rogzy | **IMPLEMENTED** BTC105: Created folder structure, course.yml, en.md (6 Parts, 18 Chapters with NEW chapters for ETFs, Treasury/TradFi, Taxes, Selling). Copied relevant assets (4 images), copied & adapted quizzes (9 quizzes from BTC102). Method-based approach instead of profile-based. Includes clear ORIGINAL/NEW content tags. |
| 2026-01-20 | Claude/Rogzy | **IMPLEMENTED** BTC104: Created folder structure, course.yml, en.md (5 Parts, 14 Chapters). Beginner-focused, step-by-step wallet setup guide. Copied 3 images (070-072 → 001-003), 3 quizzes (037, 045, 047 → 000-002). Advanced topics (multisig, passphrases, nodes) noted as placeholders for future course. |
| 2026-01-20 | Claude/Rogzy | **IMPLEMENTED** SOV102: Created folder structure, course.yml, en.md (5 Parts, 11 Chapters). Follows Pamela Morgan's methodology. Copied 4 images (097-100 → 001-004), 5 quizzes (060-064 → 000-004). Preserves Pamela Morgan attribution and legal disclaimer. |

---

## How to Resume This Project

When starting a new session, point Claude to this document:
1. Read `docs/btc102-split-plan.md` for full context
2. Check the "Course Review Status" table to see what's next
3. Continue with the next course marked "NOT STARTED"

**Current Next Step**: Create BTC102v2 (Hub Course) - the final course that ties all split courses together

---

*This document serves as the single source of truth for the BTC102 split project. Update as decisions are made.*
