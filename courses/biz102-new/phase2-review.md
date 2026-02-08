# BIZ102 Phase 2 Review

> This document tracks all work needed to complete BIZ102 (Bitcoin Industry Overview) for production.
> Location: `courses/biz102-new/phase2-review.md`

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
| id | `8b2e6f3a-1c4d-5e7f-9a0b-2c3d4e5f6a7b` | ✅ |
| topic | `business` | ✅ |
| subtopic | `bitcoin-industry` | ✅ |
| type | `theory` | ✅ |
| level | `beginner` | ✅ |
| hours | `2` | ✅ |
| professors_id | `2e1b5182-567e-453a-af29-36009340ff02` | ✅ |

**Issues:** None. All required fields are present and properly formatted.

---

### A2. Frontmatter Validation (en.md)

- [x] `name` present and descriptive: "Bitcoin Industry Overview"
- [x] `goal` is single sentence, action-oriented: "Understand the key players, infrastructure, and layered architecture that make up the Bitcoin ecosystem"
- [x] `objectives` has 3-6 items (has 4 objectives)
  - Understand the birth and evolution of the Bitcoin industry
  - Learn about the different types of exchanges, wallets, and infrastructure
  - Discover how Bitcoin's layered architecture enables scalability and new features
  - Explore merchant tools for accepting Bitcoin payments

**Issues:** None. Frontmatter is complete and well-structured.

---

### A3. Structure Validation

- [x] First Part is Introduction
- [x] No text between Part headings and first Chapter
- [x] All Parts have `<partId>`
- [x] All Chapters have `<chapterId>`
- [x] Going Further is last chapter of last content Part (Part 4: Bitcoin's Layered Architecture)
- [x] Conclusion Part exists with only Conclusion chapter (Part 5)
- [x] `<isCourseConclusion>true</isCourseConclusion>` tag present

**Course Structure Summary:**

| Part # | Part Name | partId | Chapters |
|--------|-----------|--------|----------|
| 1 | Introduction | `a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d` | Ch 1: Welcome to BIZ102 |
| 2 | Birth of a Global Industry | `c3d4e5f6-a7b8-9c0d-1e2f-3a4b5c6d7e8f` | Ch 2-4 |
| 3 | Industry Infrastructure | `a7b8c9d0-e1f2-3a4b-5c6d-7e8f9a0b1c2d` | Ch 5-8 |
| 4 | Bitcoin's Layered Architecture | `b8c9d0e1-f2a3-4b5c-6d7e-8f9a0b1c2d3e` | Ch 9-11 (incl. Going Further) |
| 5 | Conclusion | `c9d0e1f2-a3b4-5c6d-7e8f-9a0b1c2d3e4f` | Ch 12: Conclusion |

**Issues:** None. Structure follows PBN standards correctly.

---

### A4. Image Inventory

**Summary:**
| Metric | Count |
|--------|-------|
| Current images | 11 |
| Target images | 30-38 |
| **GAP** | **19-27 images to create** |

**Per-Chapter Breakdown:**

| Ch # | Chapter Title | chapterId | Current | Target | Gap | Images Used |
|------|---------------|-----------|---------|--------|-----|-------------|
| 1 | Welcome to BIZ102 | `b2c3d4e5-f6a7-8b9c-0d1e-2f3a4b5c6d7e` | 0 | 0-1 | 0 | - |
| 2 | A Radical Innovation | `d4e5f6a7-b8c9-0d1e-2f3a-4b5c6d7e8f9a` | 1 | 4-5 | 3-4 | 001.webp |
| 3 | The Proliferation of Altcoins | `e5f6a7b8-c9d0-1e2f-3a4b-5c6d7e8f9a0b` | 0 | 4-5 | 4-5 | - |
| 4 | Institutional Adoption | `f6a7b8c9-d0e1-2f3a-4b5c-6d7e8f9a0b1c` | 1 | 4-5 | 3-4 | 002.webp |
| 5 | Regulation and Government Approaches | `b8c9d0e1-f2a3-4b5c-6d7e-8f9a0b1c2d3e` | 2 | 4-5 | 2-3 | 003.webp, 004.webp |
| 6 | The Banks' Stance on Bitcoin | `c9d0e1f2-a3b4-5c6d-7e8f-9a0b1c2d3e4f` | 0 | 4-5 | 4-5 | - |
| 7 | Cryptocurrency Exchanges and Bitcoin Custody | `d0e1f2a3-b4c5-6d7e-8f9a-0b1c2d3e4f5a` | 1 | 4-5 | 3-4 | 005.webp |
| 8 | Wallets, Mining and Development | `e1f2a3b4-c5d6-7e8f-9a0b-1c2d3e4f5a6b` | 2 | 4-5 | 2-3 | 006.webp, 007.webp |
| 9 | Extension Layers | `f2a3b4c5-d6e7-8f9a-0b1c-2d3e4f5a6b7c` | 3 | 4-5 | 1-2 | 008.webp, 009.webp, 010.webp |
| 10 | Merchant Tools for Accepting Bitcoin | `a3b4c5d6-e7f8-9a0b-1c2d-3e4f5a6b7c8d` | 0 | 4-5 | 4-5 | - |
| 11 | Going Further | `b4c5d6e7-f8a9-0b1c-2d3e-4f5a6b7c8d9e` | 1 | 1-2 | 0-1 | 011.webp |
| 12 | Conclusion | `d0e1f2a3-b4c5-6d7e-8f9a-0b1c2d3e4f5a` | 0 | 0 | 0 | - |

**Total Image Gap:** ~24 images needed (using midpoint of ranges)

---

### A5. Missing Images - Detailed Specifications

#### Chapter 2: A Radical Innovation (needs 3-4 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | `012-bitcoin-timeline` | Timeline showing Bitcoin's growth from 2009 to present: key milestones like first exchange, $1, $100, $1000, institutional adoption, ETF approvals | Infographic/Timeline | High |
| 2 | `013-industry-growth` | Chart or visualization showing the exponential growth of Bitcoin ecosystem: market cap, number of companies, developer activity | Chart/Diagram | High |
| 3 | `014-disruptive-innovation` | Conceptual illustration showing Bitcoin disrupting traditional finance - perhaps a visual metaphor of old vs new financial systems | Illustration | Medium |
| 4 | `015-builders-vs-resistors` | Split visualization showing two groups: builders/adopters embracing Bitcoin vs traditional institutions resisting | Illustration | Medium |

#### Chapter 3: The Proliferation of Altcoins (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | `016-altcoin-explosion` | Visualization showing the explosion of cryptocurrencies from 5,000 (2019) to millions (2025), emphasizing most are scams | Chart/Diagram | High |
| 2 | `017-bitcoin-vs-altcoins-table` | Visual representation of the comparison table already in content (liquidity, adoption, decentralization, etc.) | Infographic/Table | High |
| 3 | `018-scam-warning-signs` | Visual showing common altcoin marketing tactics to watch out for: misleading claims, promises of returns | Illustration | High |
| 4 | `019-bitcoin-fundamentals` | Diagram showing what makes Bitcoin unique: decentralization, security, censorship-resistance, global adoption | Diagram | Medium |
| 5 | `020-ico-era` | Historical context showing the 2017 ICO boom and subsequent collapse of most projects | Timeline/Chart | Low |

#### Chapter 4: Institutional Adoption (needs 3-4 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | `021-cbdc-map` | World map showing countries exploring or implementing CBDCs (China, EU, Sweden, etc.) | Map/Infographic | High |
| 2 | `022-bitcoin-vs-cbdc-table` | Visual representation of the comparison table: public, open, borderless, neutral, censorship-resistant | Infographic/Table | High |
| 3 | `023-institutional-interest` | Visualization of major institutions entering Bitcoin space: companies, funds, banks | Illustration/Diagram | Medium |
| 4 | `024-libra-failure` | Timeline or illustration showing Facebook's Libra project launch and eventual abandonment | Timeline | Low |

#### Chapter 5: Regulation and Government Approaches (needs 2-3 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | `025-regulatory-spectrum` | Detailed visualization showing range of government approaches from restrictive to welcoming | Spectrum/Diagram | High |
| 2 | `026-bitcoin-classification` | Diagram showing different ways governments classify Bitcoin: currency, property, commodity, etc. | Diagram | Medium |
| 3 | `027-compliance-landscape` | Checklist or flowchart showing what Bitcoin users/businesses need to consider for compliance | Flowchart | Low |

#### Chapter 6: The Banks' Stance on Bitcoin (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | `028-bank-threat-perception` | Illustration showing how banks view Bitcoin as threat to their intermediation model | Illustration | High |
| 2 | `029-bank-restrictions` | Examples of bank restrictions on crypto businesses: account closures, service limitations | Infographic | High |
| 3 | `030-bank-hypocrisy` | Visual showing banks researching blockchain while restricting Bitcoin access | Illustration | Medium |
| 4 | `031-banking-access-map` | Map or chart showing which banks/countries are more crypto-friendly | Map/Chart | Medium |
| 5 | `032-future-banking-bitcoin` | Conceptual image showing potential future integration of Bitcoin with traditional banking | Illustration | Low |

#### Chapter 7: Cryptocurrency Exchanges and Bitcoin Custody (needs 3-4 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | `033-exchange-types` | Diagram showing different types of exchanges: P2P, Bitcoin-only, general trading platforms | Diagram | High |
| 2 | `034-kyc-privacy-tradeoff` | Visualization showing the tradeoff between KYC compliance and privacy | Illustration | High |
| 3 | `035-exchange-risks` | Visual showing risks of leaving Bitcoin on exchanges: hacking, seizure, bankruptcy (Mt.Gox, FTX) | Infographic | High |
| 4 | `036-self-custody-golden-rule` | Strong visual emphasizing "Not your keys, not your coins" message | Illustration | Medium |

#### Chapter 8: Wallets, Mining and Development (needs 2-3 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | `037-wallet-types` | Comprehensive diagram showing hardware, software, and DIY wallet options | Diagram | High |
| 2 | `038-mining-ecosystem` | Diagram showing mining ecosystem: hardware manufacturers, pools, individual miners | Diagram | High |
| 3 | `039-mining-evolution` | Timeline showing evolution of mining from CPU to GPU to ASIC | Timeline | Medium |

#### Chapter 9: Extension Layers (needs 1-2 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | `040-sidechain-concept` | Detailed diagram explaining how sidechains connect to Bitcoin main chain via two-way peg | Diagram | High |
| 2 | `041-liquid-rsk-comparison` | Comparison diagram showing features of Liquid vs RSK sidechains | Comparison/Table | Medium |

#### Chapter 10: Merchant Tools for Accepting Bitcoin (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | `042-merchant-solutions-spectrum` | Spectrum showing merchant solutions from simple (hot wallet) to advanced (BTCPay Server) | Spectrum/Diagram | High |
| 2 | `043-bitcoin-payment-benefits` | Infographic showing benefits: no chargebacks, lower fees, no bank required, global | Infographic | High |
| 3 | `044-pos-options` | Visual comparison of point-of-sale options: OpenNode, BTCPay Server, Swiss Bitcoin Pay | Comparison | High |
| 4 | `045-business-treasury` | Illustration showing Bitcoin as business treasury asset with fixed 21M supply | Illustration | Medium |
| 5 | `046-merchant-adoption-examples` | Examples of businesses accepting Bitcoin across different industries | Collage/Examples | Low |

#### Chapter 11: Going Further (needs 0-1 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | `047-bitcoin-highway` | Visual metaphor of the "Bitcoin highway" mentioned in the chapter - showing infrastructure being built | Illustration | Medium |

---

### A6. Quiz Inventory

**Summary:**
| Metric | Count |
|--------|-------|
| Current quizzes | 10 |
| Content chapters requiring quizzes | 8 (Ch 2-9) |
| Required per-chapter (8 x 5) | 40 |
| Required for final exam | 40 |
| **Total recommended** | **80** |
| **GAP** | **70 quizzes to create** |

**Per-Chapter Breakdown:**

| Ch # | Chapter Title | chapterId | Current | Required | Gap |
|------|---------------|-----------|---------|----------|-----|
| 1 | Welcome to BIZ102 | `b2c3d4e5-f6a7-8b9c-0d1e-2f3a4b5c6d7e` | 0 | 0 | 0 |
| 2 | A Radical Innovation | `d4e5f6a7-b8c9-0d1e-2f3a-4b5c6d7e8f9a` | 0 | 5 | 5 |
| 3 | The Proliferation of Altcoins | `e5f6a7b8-c9d0-1e2f-3a4b-5c6d7e8f9a0b` | 1 | 5 | 4 |
| 4 | Institutional Adoption | `f6a7b8c9-d0e1-2f3a-4b5c-6d7e8f9a0b1c` | 0 | 5 | 5 |
| 5 | Regulation and Government Approaches | `b8c9d0e1-f2a3-4b5c-6d7e-8f9a0b1c2d3e` | 0 | 5 | 5 |
| 6 | The Banks' Stance on Bitcoin | `c9d0e1f2-a3b4-5c6d-7e8f-9a0b1c2d3e4f` | 0 | 5 | 5 |
| 7 | Cryptocurrency Exchanges and Bitcoin Custody | `d0e1f2a3-b4c5-6d7e-8f9a-0b1c2d3e4f5a` | 2* | 5 | 3 |
| 8 | Wallets, Mining and Development | `e1f2a3b4-c5d6-7e8f-9a0b-1c2d3e4f5a6b` | 2 | 5 | 3 |
| 9 | Extension Layers | `f2a3b4c5-d6e7-8f9a-0b1c-2d3e4f5a6b7c` | 5 | 5 | 0 |
| 10 | Merchant Tools for Accepting Bitcoin | `a3b4c5d6-e7f8-9a0b-1c2d-3e4f5a6b7c8d` | 0 | 5 | 5 |
| 11 | Going Further | `b4c5d6e7-f8a9-0b1c-2d3e-4f5a6b7c8d9e` | 0 | 0 | 0 |
| 12 | Conclusion | `e4f5a6b7-c8d9-0e1f-2a3b-4c5d6e7f8a9b` | 0 | 0 | 0 |

*Note: ~~Quiz 001 and 003 were mapped to the Conclusion chapter chapterId~~ - FIXED (2026-02-08): Conclusion chapter given new chapterId `e4f5a6b7-c8d9-0e1f-2a3b-4c5d6e7f8a9b`. Quizzes 001 and 003 now correctly resolve to Ch 7 (Exchanges) only.

**Current Quiz Mapping:**

| Quiz # | chapterId | Linked Chapter | Notes |
|--------|-----------|----------------|-------|
| 000 | `e5f6a7b8-c9d0-1e2f-3a4b-5c6d7e8f9a0b` | Ch 3: The Proliferation of Altcoins | OK |
| 001 | `d0e1f2a3-b4c5-6d7e-8f9a-0b1c2d3e4f5a` | Ch 12: Conclusion | **ERROR: Needs remapping** |
| 002 | `e1f2a3b4-c5d6-7e8f-9a0b-1c2d3e4f5a6b` | Ch 8: Wallets, Mining and Development | OK |
| 003 | `d0e1f2a3-b4c5-6d7e-8f9a-0b1c2d3e4f5a` | Ch 12: Conclusion | **ERROR: Needs remapping** |
| 004 | `e1f2a3b4-c5d6-7e8f-9a0b-1c2d3e4f5a6b` | Ch 8: Wallets, Mining and Development | OK |
| 005 | `f2a3b4c5-d6e7-8f9a-0b1c-2d3e4f5a6b7c` | Ch 9: Extension Layers | OK |
| 006 | `f2a3b4c5-d6e7-8f9a-0b1c-2d3e4f5a6b7c` | Ch 9: Extension Layers | OK |
| 007 | `f2a3b4c5-d6e7-8f9a-0b1c-2d3e4f5a6b7c` | Ch 9: Extension Layers | OK |
| 008 | `f2a3b4c5-d6e7-8f9a-0b1c-2d3e4f5a6b7c` | Ch 9: Extension Layers | OK |
| 009 | `f2a3b4c5-d6e7-8f9a-0b1c-2d3e4f5a6b7c` | Ch 9: Extension Layers | OK |

---

### A7. Missing Quizzes - Topic Suggestions

#### Chapter 2: A Radical Innovation (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | When was Bitcoin launched and who created it? | multiple-choice | easy |
| 2 | What does "radical innovation" mean in the context of Bitcoin? | multiple-choice | medium |
| 3 | Why can governments and institutions no longer ignore Bitcoin? | multiple-choice | medium |
| 4 | What is the difference between those who see Bitcoin as a threat vs. opportunity? | multiple-choice | easy |
| 5 | What is Bitcoin's stance on seeking permission or approval? | true-false | easy |

#### Chapter 3: The Proliferation of Altcoins (needs 4 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | How many tokens were listed on CoinMarketCap by 2025? | multiple-choice | easy |
| 2 | What is the primary difference between Bitcoin and most altcoins regarding decentralization? | multiple-choice | medium |
| 3 | What are common misleading claims about altcoins to watch out for? | multiple-choice | medium |
| 4 | Why is liquidity important when comparing Bitcoin to altcoins? | multiple-choice | hard |

#### Chapter 4: Institutional Adoption (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | What is a CBDC (Central Bank Digital Currency)? | multiple-choice | easy |
| 2 | Which countries are exploring or developing CBDCs? | multiple-choice | medium |
| 3 | Why did Facebook's Libra project fail? | multiple-choice | medium |
| 4 | What key property does Bitcoin have that CBDCs lack? | multiple-choice | medium |
| 5 | How does Bitcoin differ from institutional blockchain projects? | multiple-choice | hard |

#### Chapter 5: Regulation and Government Approaches (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | Can the Bitcoin protocol itself be regulated? | true-false | easy |
| 2 | Give an example of a country with heavy Bitcoin restrictions | multiple-choice | easy |
| 3 | Give an example of a country with Bitcoin-friendly regulations | multiple-choice | easy |
| 4 | What challenges do governments face when classifying Bitcoin? | multiple-choice | medium |
| 5 | What should Bitcoin users stay informed about regarding regulations? | multiple-choice | medium |

#### Chapter 6: The Banks' Stance on Bitcoin (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | Why do traditional banks view Bitcoin as a threat? | multiple-choice | easy |
| 2 | What reasons do banks cite when restricting crypto businesses? | multiple-choice | medium |
| 3 | What is the contradiction in banks' approach to blockchain vs Bitcoin? | multiple-choice | medium |
| 4 | How have some banks responded to Bitcoin businesses? | multiple-choice | easy |
| 5 | What is the banks' goal with blockchain research vs Bitcoin's design? | multiple-choice | hard |

#### Chapter 7: Cryptocurrency Exchanges and Bitcoin Custody (needs 3 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | What is the "golden rule" regarding Bitcoin custody? | multiple-choice | easy |
| 2 | What are the advantages of P2P exchanges over centralized exchanges? | multiple-choice | medium |
| 3 | What are the main risks of leaving Bitcoin on an exchange? | multiple-choice | medium |

#### Chapter 8: Wallets, Mining and Development (needs 3 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | What are the main types of Bitcoin wallets? | multiple-choice | easy |
| 2 | What role do mining pools play in the Bitcoin ecosystem? | multiple-choice | medium |
| 3 | Who controls updates to the Bitcoin protocol? | multiple-choice | hard |

#### Chapter 10: Merchant Tools for Accepting Bitcoin (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | What is the simplest way for a small business to accept Bitcoin? | multiple-choice | easy |
| 2 | What is BTCPay Server and what are its advantages? | multiple-choice | medium |
| 3 | What benefits does accepting Bitcoin provide for merchants? | multiple-choice | medium |
| 4 | How does Bitcoin eliminate chargeback risk for merchants? | multiple-choice | medium |
| 5 | Why might Bitcoin be attractive as a business treasury asset? | multiple-choice | hard |

#### Final Exam Pool (needs 40 additional quizzes)

| # | Topic | Related Chapter | Difficulty |
|---|-------|-----------------|------------|
| 1 | Bitcoin's creation date and creator | Ch 2 | easy |
| 2 | Definition of "zero to one" innovation | Ch 2 | medium |
| 3 | Why most altcoins are scams | Ch 3 | medium |
| 4 | Bitcoin vs altcoin decentralization | Ch 3 | medium |
| 5 | CBDC definition and purpose | Ch 4 | easy |
| 6 | Bitcoin vs CBDC comparison | Ch 4 | medium |
| 7 | Facebook Libra failure reasons | Ch 4 | medium |
| 8 | Government regulatory approaches | Ch 5 | medium |
| 9 | Bitcoin classification challenges | Ch 5 | hard |
| 10 | Bank restrictions on crypto | Ch 6 | medium |
| 11 | Banks' blockchain vs Bitcoin stance | Ch 6 | hard |
| 12 | KYC definition and implications | Ch 7 | easy |
| 13 | P2P exchange advantages | Ch 7 | medium |
| 14 | Exchange custody risks | Ch 7 | medium |
| 15 | "Not your keys, not your coins" | Ch 7 | easy |
| 16 | Hardware wallet purpose | Ch 8 | easy |
| 17 | Mining pool function | Ch 8 | medium |
| 18 | Bitcoin Core maintainers role | Ch 8 | hard |
| 19 | BIP process explanation | Ch 8 | hard |
| 20 | Lightning Network purpose | Ch 9 | easy |
| 21 | Lightning Network benefits | Ch 9 | medium |
| 22 | Sidechain definition | Ch 9 | medium |
| 23 | Liquid sidechain features | Ch 9 | hard |
| 24 | RGB protocol purpose | Ch 9 | hard |
| 25 | Single-use Seals concept | Ch 9 | hard |
| 26 | Layered architecture benefits | Ch 9 | medium |
| 27 | Internet protocol comparison | Ch 9 | medium |
| 28 | BTCPay Server features | Ch 10 | medium |
| 29 | Merchant Bitcoin benefits | Ch 10 | easy |
| 30 | Lightning for payments | Ch 10 | medium |
| 31 | Self-custody for merchants | Ch 10 | medium |
| 32 | Bitcoin as treasury asset | Ch 10 | medium |
| 33 | Bitcoin's fixed supply | Ch 10 | easy |
| 34 | Cross-course: Bitcoin industry size | Ch 2 | medium |
| 35 | Cross-course: Institutional adoption timeline | Ch 4 | hard |
| 36 | Cross-course: Regulatory landscape changes | Ch 5 | hard |
| 37 | Cross-course: Exchange evolution | Ch 7 | medium |
| 38 | Cross-course: Mining industry changes | Ch 8 | medium |
| 39 | Cross-course: Layer 2 development | Ch 9 | hard |
| 40 | Cross-course: Merchant adoption trends | Ch 10 | medium |

---

### A8. Structural Fixes Required

| # | Issue | Location | Fix Required | Priority |
|---|-------|----------|--------------|----------|
| 1 | ~~Quiz 001 mapped to Conclusion chapter~~ | `quizz/001/question.yml` | ~~Change chapterId~~ FIXED: Resolved by giving Conclusion a new chapterId | ~~Critical~~ Done |
| 2 | ~~Quiz 003 mapped to Conclusion chapter~~ | `quizz/003/question.yml` | ~~Change chapterId~~ FIXED: Resolved by giving Conclusion a new chapterId | ~~Critical~~ Done |
| 3 | ~~Duplicate chapterId between Ch 7 and Ch 12~~ | en.md | FIXED (2026-02-08): Conclusion chapter changed to `e4f5a6b7-c8d9-0e1f-2a3b-4c5d6e7f8a9b` | ~~Critical~~ Done |

---

### A9. Work Summary for Phase B

**Before starting Phase B, complete these tasks:**

#### Critical (Must Do)
- [x] **FIX DUPLICATE CHAPTERID** - DONE (2026-02-08): Conclusion chapter changed to `e4f5a6b7-c8d9-0e1f-2a3b-4c5d6e7f8a9b`
- [x] Quiz 001 and 003 now correctly map to Ch 7 (Exchanges) - verified: both quizzes are about exchanges/wallets content

#### Images to Create (24 total)
- [ ] Ch 2: 4 images (see specs in A5) - `012-015`
- [ ] Ch 3: 5 images (see specs in A5) - `016-020`
- [ ] Ch 4: 4 images (see specs in A5) - `021-024`
- [ ] Ch 5: 3 images (see specs in A5) - `025-027`
- [ ] Ch 6: 5 images (see specs in A5) - `028-032`
- [ ] Ch 7: 4 images (see specs in A5) - `033-036`
- [ ] Ch 8: 3 images (see specs in A5) - `037-039`
- [ ] Ch 9: 2 images (see specs in A5) - `040-041`
- [ ] Ch 10: 5 images (see specs in A5) - `042-046`
- [ ] Ch 11: 1 image (see specs in A5) - `047`

#### Quizzes to Create (70 total)
- [ ] Ch 2: 5 quizzes (see topics in A7)
- [ ] Ch 3: 4 quizzes (see topics in A7)
- [ ] Ch 4: 5 quizzes (see topics in A7)
- [ ] Ch 5: 5 quizzes (see topics in A7)
- [ ] Ch 6: 5 quizzes (see topics in A7)
- [ ] Ch 7: 3 quizzes (see topics in A7)
- [ ] Ch 8: 3 quizzes (see topics in A7)
- [ ] Ch 10: 5 quizzes (see topics in A7)
- [ ] Final exam pool: 40 quizzes (see topics in A7)

---

**Phase A Status:** ✅ COMPLETE
**Phase A Completed:** 2026-01-21
**Notes:**
- Critical issue discovered: Duplicate chapterId between Chapter 7 (Exchanges) and Chapter 12 (Conclusion). Must be fixed before Phase B.
- Course structure is otherwise well-organized with proper PBN standards compliance.
- Most chapters need additional images (24 total) and quizzes (70 total) to meet production standards.
- Quiz 001 and 003 appear to be incorrectly mapped but may actually be for Chapter 7 if the duplicate ID issue is resolved correctly.
