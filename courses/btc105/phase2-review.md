# BTC105 Phase 2 Review

> This document tracks all work needed to complete BTC105 for production.
> Location: `courses/btc105/phase2-review.md`

## Progress Tracker
| Phase | Status | Date | Session |
|-------|--------|------|---------|
| A - Structure Review | ✅ | 2026-01-21 | Initial review |
| B - Pre-Production | ⬜ | | |
| C - Recording | ⬜ | | |
| D - Post-Production | ⬜ | | |

---

## Phase A: Structure & Content Review

### A1. Metadata Validation (course.yml)

| Field | Value | Status |
|-------|-------|--------|
| id | 4a7c2e9b-3f8d-5c1a-9e6b-7d4f8a2c5e0b | ✅ Valid UUID |
| topic | bitcoin | ✅ |
| subtopic | acquisition | ✅ |
| type | theory | ✅ |
| level | beginner | ✅ |
| hours | 2.5 | ✅ |
| professors_id | 2e1b5182-567e-453a-af29-36009340ff02 | ✅ |

**Issues:** None - all required metadata fields are present and valid.

### A2. Frontmatter Validation (en.md)

- [x] `name` present and descriptive: "How to Acquire Bitcoin"
- [x] `goal` is single sentence, action-oriented: "Learn the different methods to acquire bitcoin and choose the strategy that fits your needs"
- [x] `objectives` has 3-6 items (5 objectives present):
  1. Understand the key factors to consider before buying bitcoin
  2. Compare KYC vs No-KYC acquisition methods
  3. Master different acquisition strategies (lump sum, DCA, P2P)
  4. Learn about Bitcoin ETFs and institutional solutions
  5. Know what to do after your first purchase

**Issues:** None - frontmatter is complete and well-structured.

### A3. Structure Validation

- [x] First Part is Introduction (`# Introduction` with `<partId>introduction-part1</partId>`)
- [x] No text between Part headings and first Chapter
- [x] All Parts have `<partId>` (6 Parts, all have partIds)
- [x] All Chapters have `<chapterId>` (18 Chapters, all have chapterIds)
- [ ] **Going Further is last chapter of last content Part** - MISSING
- [ ] **Conclusion Part exists with only Conclusion chapter** - FAILS (Part 6 has 2 chapters)
- [x] `<isCourseConclusion>true</isCourseConclusion>` tag present (on Chapter 18)

**Issues:**
1. **CRITICAL: Missing "Going Further" chapter** - The course jumps directly from content chapters to Conclusion without a "Going Further" chapter containing resources and next steps.
2. **CRITICAL: Conclusion Part structure incorrect** - Part 6 "Conclusion" currently contains TWO chapters:
   - Chapter 17: "Building Your Personal Strategy"
   - Chapter 18: "Conclusion"

   Per PBN standards, the Conclusion Part should contain ONLY the Conclusion chapter. Chapter 17 should be moved to Part 5 (or a new Part), and a "Going Further" chapter should be added as the last chapter of the last content Part.

### A3.1 Complete Structure Map

| Part # | Part Title | partId | Chapters |
|--------|------------|--------|----------|
| 1 | Introduction | introduction-part1 | Ch 1-2 |
| 2 | Choosing Your Acquisition Strategy | strategy-decision-part2 | Ch 3-4 |
| 3 | Acquisition Methods | acquisition-methods-part3 | Ch 5-10 |
| 4 | Alternative Acquisition Methods | alternatives-part4 | Ch 11-12 |
| 5 | After Your First Purchase | after-purchase-part5 | Ch 13-16 |
| 6 | Conclusion | conclusion-part6 | Ch 17-18 |

| Ch # | Chapter Title | chapterId | Part | Type |
|------|---------------|-----------|------|------|
| 1 | Welcome to BTC105 | welcome-ch01 | 1 | Introduction |
| 2 | Prerequisites Before Buying Bitcoin | prerequisites-ch02 | 1 | Substantive |
| 3 | The Key Questions | key-questions-ch03 | 2 | Substantive |
| 4 | Understanding the Trade-offs | tradeoffs-ch04 | 2 | Substantive |
| 5 | Lump Sum Purchase (KYC) | lumpsum-kyc-ch05 | 3 | Substantive |
| 6 | Lump Sum Purchase (No-KYC) | lumpsum-nokyc-ch06 | 3 | Substantive |
| 7 | DCA - Dollar Cost Averaging (KYC) | dca-kyc-ch07 | 3 | Substantive |
| 8 | DCA Without KYC | dca-nokyc-ch08 | 3 | Substantive |
| 9 | Bitcoin ETFs | etf-ch09 | 3 | Substantive |
| 10 | Corporate Treasury & TradFi Solutions | treasury-tradfi-ch10 | 3 | Substantive |
| 11 | Common Alternatives | common-alternatives-ch11 | 4 | Substantive |
| 12 | Obscure & Advanced Methods | obscure-methods-ch12 | 4 | Substantive |
| 13 | All Methods Are Valid | all-methods-valid-ch13 | 5 | Substantive |
| 14 | Securing Your Bitcoin | securing-bitcoin-ch14 | 5 | Substantive |
| 15 | Taxes & Compliance | taxes-compliance-ch15 | 5 | Substantive |
| 16 | Selling & Off-Ramping | selling-offramp-ch16 | 5 | Substantive |
| 17 | Building Your Personal Strategy | personal-strategy-ch17 | 6 | Substantive (misplaced) |
| 18 | Conclusion | conclusion-ch18 | 6 | Conclusion |

---

### A4. Image Inventory

**Summary:**
| Metric | Count |
|--------|-------|
| Current images | 4 |
| Target images | 56-70 |
| **GAP** | **52-66 images to create** |

**Per-Chapter Breakdown:**

| Ch # | Chapter Title | Current | Target | Gap | Images Used |
|------|---------------|---------|--------|-----|-------------|
| 1 | Welcome to BTC105 | 0 | 0-1 | 0-1 | - |
| 2 | Prerequisites Before Buying Bitcoin | 0 | 4-5 | 4-5 | - |
| 3 | The Key Questions | 0 | 4-5 | 4-5 | - |
| 4 | Understanding the Trade-offs | 1 | 4-5 | 3-4 | 001.webp |
| 5 | Lump Sum Purchase (KYC) | 0 | 4-5 | 4-5 | - |
| 6 | Lump Sum Purchase (No-KYC) | 0 | 4-5 | 4-5 | - |
| 7 | DCA - Dollar Cost Averaging (KYC) | 2 | 4-5 | 2-3 | 002.webp, 003.webp |
| 8 | DCA Without KYC | 0 | 4-5 | 4-5 | - |
| 9 | Bitcoin ETFs | 0 | 4-5 | 4-5 | - |
| 10 | Corporate Treasury & TradFi | 0 | 4-5 | 4-5 | - |
| 11 | Common Alternatives | 1 | 4-5 | 3-4 | 004.webp |
| 12 | Obscure & Advanced Methods | 0 | 4-5 | 4-5 | - |
| 13 | All Methods Are Valid | 0 | 4-5 | 4-5 | - |
| 14 | Securing Your Bitcoin | 0 | 4-5 | 4-5 | - |
| 15 | Taxes & Compliance | 0 | 4-5 | 4-5 | - |
| 16 | Selling & Off-Ramping | 0 | 4-5 | 4-5 | - |
| 17 | Building Your Personal Strategy | 0 | 4-5 | 4-5 | - |
| 18 | Conclusion | 0 | 0 | 0 | - |
| - | Going Further (MISSING) | 0 | 1-2 | 1-2 | - |

**Current Image Details:**
| Image | Filename | Referenced In | Description |
|-------|----------|---------------|-------------|
| 1 | 001.webp | Ch 4 (tradeoffs-ch04) | KYC vs No-KYC comparison |
| 2 | 002.webp | Ch 7 (dca-kyc-ch07) | DCA concept visualization |
| 3 | 003.webp | Ch 7 (dca-kyc-ch07) | DCA plan setup |
| 4 | 004.webp | Ch 11 (common-alternatives-ch11) | Earning bitcoin for work |

---

### A5. Missing Images - Detailed Specifications

#### Chapter 1: Welcome to BTC105 (needs 0-1 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | btc105-course-overview | Visual showing the acquisition journey: Learn > Decide > Acquire > Secure. Simple roadmap showing what students will learn. | Illustration/diagram | Low |

#### Chapter 2: Prerequisites Before Buying Bitcoin (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | not-your-keys-concept | Visual representation of "Not your keys, not your coins" - showing exchange holding bitcoin vs self-custody | Illustration | High |
| 2 | hot-vs-hardware-wallet | Comparison diagram: phone with hot wallet app vs physical hardware wallet device. Show key storage location differences. | Diagram | High |
| 3 | wallet-types-comparison | Table/chart comparing hot wallets, hardware wallets, and their pros/cons (security, convenience, cost) | Chart/Table | High |
| 4 | recovery-phrase-backup | Illustration showing 24-word seed phrase being written on paper, stored securely (fireproof safe, metal backup) | Illustration | High |
| 5 | beginner-mistakes-infographic | Visual showing 5 common beginner mistakes: leaving on exchange, no backup, sharing holdings, overinvesting, timing market | Infographic | Medium |

#### Chapter 3: The Key Questions (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | investment-types-comparison | Visual comparing lump sum (single arrow) vs DCA (multiple small arrows over time) investment approaches | Diagram | High |
| 2 | privacy-spectrum | Spectrum visualization from "Full KYC" on left to "Full Privacy" on right, with methods placed along it | Diagram | High |
| 3 | automation-vs-manual | Comparison showing automated DCA (hands-off, recurring) vs manual purchases (more control, more effort) | Illustration | Medium |
| 4 | key-questions-checklist | Visual checklist of 5 key questions to answer: Amount? Privacy? Automation? Tech comfort? Regional availability? | Infographic | High |
| 5 | user-profile-decision-tree | Flowchart helping users identify which acquisition path matches their answers to key questions | Flowchart | Medium |

#### Chapter 4: Understanding the Trade-offs (needs 3-4 images, has 1)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | kyc-privacy-risk | Diagram showing how KYC links identity to bitcoin addresses, enabling blockchain analysis and tracking | Diagram | High |
| 2 | convenience-privacy-spectrum | Horizontal spectrum chart with acquisition methods placed from "Most Convenient" to "Most Private" | Chart | High |
| 3 | fees-comparison-table | Visual table comparing fees: KYC Exchange (0.1-1%), DCA Service (1-2%), P2P (3-10%), ATM (5-15%), Earning (0%) | Table/Chart | High |
| 4 | decision-framework-matrix | 2x2 matrix: Privacy (high/low) vs Convenience (high/low) with acquisition methods in each quadrant | Matrix diagram | Medium |

#### Chapter 5: Lump Sum Purchase (KYC) (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | kyc-exchange-workflow | Step-by-step flowchart: Create account > KYC > Deposit fiat > Buy > Withdraw to wallet | Flowchart | High |
| 2 | exchange-comparison | Comparison table of major exchanges (Kraken, Bitstamp, etc.) showing features, fees, regions | Table | High |
| 3 | order-types-explained | Visual explaining market order (instant) vs limit order (at your price) - show price chart with order examples | Diagram | Medium |
| 4 | payment-methods-comparison | Chart comparing payment methods: Bank transfer (cheaper, slower) vs Card (expensive, instant) | Chart | Medium |
| 5 | immediate-withdrawal-reminder | Visual emphasizing "Buy then Withdraw" - showing flow from exchange to personal wallet with warning about exchange risks | Illustration | High |

#### Chapter 6: Lump Sum Purchase (No-KYC) (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | p2p-escrow-flow | Diagram showing P2P trade flow: Seller deposits BTC > Buyer sends fiat > Seller confirms > BTC released | Flowchart | High |
| 2 | p2p-platforms-comparison | Comparison of Bisq, Peach, RoboSats, HodlHodl - showing features, privacy level, ease of use | Table | High |
| 3 | no-kyc-premium-explained | Visual explaining why no-KYC has 5-15% premium: privacy value, seller risk, lower liquidity | Diagram | Medium |
| 4 | in-person-trade-safety | Illustration showing safe in-person trading practices: public place, bring friend, verify on-chain, start small | Illustration | High |
| 5 | payment-methods-p2p | Icons/list of P2P payment methods: bank transfer, cash mail, gift cards, mobile apps, in-person cash | Icon grid | Medium |

#### Chapter 7: DCA - Dollar Cost Averaging (KYC) (needs 2-3 images, has 2)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | dca-volatility-smoothing | Chart showing how DCA smooths out price volatility over time vs trying to time the market | Line chart | High |
| 2 | dca-platform-comparison | Comparison table of DCA platforms (Relai, StackinSat, Bitstack, Bull Bitcoin) with features and fees | Table | Medium |
| 3 | dca-workflow | Simple flowchart: Choose platform > Set frequency > Set amount > Enable auto-withdraw > Consolidate periodically | Flowchart | Medium |

#### Chapter 8: DCA Without KYC (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | manual-dca-workflow | Weekly/monthly cycle diagram: Set reminder > Open P2P platform > Find offer > Complete trade > Withdraw | Flowchart | High |
| 2 | p2p-dca-platforms | Icons/comparison of RoboSats, Peach, LNP2PBot for regular no-KYC purchases | Icon comparison | High |
| 3 | kyc-vs-nokyc-dca-comparison | Side-by-side comparison table: Convenience, Privacy, Premium, Time required | Table | High |
| 4 | dca-discipline-reminder | Visual emphasizing discipline needed without automation - calendar with regular purchase reminders | Illustration | Medium |
| 5 | batch-purchases-concept | Diagram showing batching: Instead of 4 tiny weekly buys, do 1 larger bi-weekly buy (better for UTXO management) | Diagram | Medium |

#### Chapter 9: Bitcoin ETFs (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | etf-concept-explained | Diagram showing how ETF works: Investor buys shares > Fund holds bitcoin > Price tracking | Diagram | High |
| 2 | spot-vs-futures-etf | Comparison: Spot ETF (holds real BTC, tracks spot price) vs Futures ETF (holds contracts, can deviate) | Comparison diagram | High |
| 3 | etf-pros-cons | Visual pros/cons list: Pros (familiar, tax advantages, no keys) vs Cons (not your coins, fees, counterparty risk) | Split diagram | High |
| 4 | major-etfs-comparison | Table of major ETFs: IBIT, FBTC, GBTC, ARKB with tickers, fees, custodians | Table | Medium |
| 5 | etf-not-bitcoin-warning | Visual emphasizing "ETFs are NOT Bitcoin" - showing the difference between paper exposure and actual ownership | Warning illustration | High |

#### Chapter 10: Corporate Treasury & TradFi Solutions (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | corporate-treasury-rationale | Diagram showing why companies hold BTC: Hedge inflation, Diversification, Signal to stakeholders | Diagram | Medium |
| 2 | institutional-custody-features | Visual showing institutional custody: Qualified custody, Insurance, Multisig, Compliance, SLA | Icon list | Medium |
| 3 | btc-backed-products-warning | Illustration of bitcoin-backed products (loans, yield) with warning about counterparty risk (Celsius, BlockFi examples) | Warning diagram | High |
| 4 | business-compliance-checklist | Checklist for businesses: Accounting, Tax, Regulatory, Audit, Internal controls | Checklist | Medium |
| 5 | institutional-vs-individual | Comparison showing when institutional solutions apply vs individual acquisition methods | Comparison | Low |

#### Chapter 11: Common Alternatives (needs 3-4 images, has 1)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | earn-btc-methods | Visual showing ways to earn: Accept payments (business), Salary in BTC (employee), Freelance services | Icon grid | High |
| 2 | cashback-rewards | Illustration of bitcoin-back rewards: Debit cards, Shopping portals, Browser extensions | Icon grid | Medium |
| 3 | gift-card-workflow | Flow showing gift card strategy: Buy gift cards with BTC OR buy BTC with gift cards on P2P | Flowchart | Medium |
| 4 | btc-atm-info | Visual showing BTM: High fees (5-15%), Varying KYC, Limited locations - use CoinATMRadar to find | Info graphic | Medium |

#### Chapter 12: Obscure & Advanced Methods (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | home-mining-options | Visual showing home mining: USB miners (educational), ASIC miners (dedicated), Heat recycling miners | Icon grid | Medium |
| 2 | mining-considerations | Checklist/diagram: Electricity costs, Noise/heat, Mining pools needed, Hardware investment | Checklist | Medium |
| 3 | voucher-redemption | Simple flow: Purchase voucher > Get code > Redeem for BTC | Flowchart | Low |
| 4 | in-person-trading-venues | Icons showing where to trade: Bitcoin meetups, Conferences, Trusted networks | Icon grid | Medium |
| 5 | lightning-node-routing | Diagram showing how Lightning routing fees work for node operators | Technical diagram | Low |

#### Chapter 13: All Methods Are Valid (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | valid-methods-grid | Grid showing all valid methods with checkmarks: KYC Exchange, P2P, DCA, ATM, Earning - "All are valid starting points" | Grid | High |
| 2 | strategy-evolution-path | Diagram showing common progressions: KYC > No-KYC, Lump sum > DCA, Hot wallet > Hardware wallet, Beginner > Node runner | Flow diagram | High |
| 3 | analysis-paralysis-warning | Illustration warning against overthinking - "Don't let perfect be the enemy of good" - emphasize just starting | Illustration | Medium |
| 4 | btc-fungibility | Diagram showing all bitcoin is fungible - KYC and No-KYC bitcoin look the same on blockchain | Diagram | Medium |
| 5 | self-custody-priority | Visual emphasizing that self-custody is more important than optimizing acquisition method | Emphasis graphic | High |

#### Chapter 14: Securing Your Bitcoin (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | exchange-to-wallet-flow | Step-by-step: Have wallet > Get receive address > Exchange withdraw > Enter address > Confirm > Wait for confirmations | Flowchart | High |
| 2 | wallet-progression | Progression diagram: Small amounts (hot wallet) > Growing holdings (hardware wallet) > Significant holdings (multisig) | Progression | High |
| 3 | backup-essentials | Visual showing backup best practices: Write on paper/metal, Secure location, Never digital, Multiple locations, Test recovery | Checklist | High |
| 4 | btc104-teaser | Preview graphic showing what BTC104 covers: Wallet setup, Backup strategies, Hardware wallets, Multisig, Inheritance | Course preview | Medium |
| 5 | security-checklist | Quick security checklist: Wallet set up, Recovery phrase backed up, Secure storage, Test transaction, Understand restore | Checklist | High |

#### Chapter 15: Taxes & Compliance (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | tax-events-diagram | Visual showing taxable vs non-taxable events: Selling/Trading/Spending (taxable) vs Buying/Transferring/Gifting (usually not) | Split diagram | High |
| 2 | kyc-vs-nokyc-tax | Comparison: KYC (exchange reports, easier cost basis) vs No-KYC (no reporting, same legal obligations) | Comparison | High |
| 3 | record-keeping-template | Visual showing what to track: Date, Amount, Price, Fees, Source, Sale info | Template | Medium |
| 4 | long-vs-short-term-gains | Diagram showing holding period impact: < 1 year (higher tax) vs > 1 year (often lower tax) | Timeline diagram | High |
| 5 | tax-professional-triggers | List of when to consult professional: Large sales, Complex situations, Uncertainty, Amending returns, Law changes | Checklist | Medium |

#### Chapter 16: Selling & Off-Ramping (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | legitimate-sell-reasons | Visual showing valid reasons to sell: Emergency, Large purchase, Profits, Business, Taxes, Life changes | Icon grid | Medium |
| 2 | kyc-offramp-flow | Flow: Send BTC to exchange > Sell order > Withdraw fiat to bank | Flowchart | High |
| 3 | nokyc-offramp-options | Visual showing No-KYC off-ramps: P2P platforms, In-person trades, Gift cards, Direct spending | Icon grid | High |
| 4 | spending-alternatives | Diagram showing alternatives to selling: Direct spending, Gift cards, Debit cards, Bill payment | Diagram | Medium |
| 5 | spend-and-replace | Cycle diagram: Spend BTC > Replace with fiat > Maintain position while using BTC as currency | Cycle diagram | Medium |

#### Chapter 17: Building Your Personal Strategy (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | decision-tree-full | Complete decision tree from the chapter text: Privacy? > Lump sum? > Hands-off? > Tech comfort? | Flowchart | High |
| 2 | combined-methods-examples | Visual showing 3 example profiles: Pragmatic Stacker, Privacy-Focused User, Beginner | Profile cards | High |
| 3 | first-30-days-checklist | Visual checklist: Week 1 (Foundation), Week 2 (Learn), Week 3 (Strategy), Week 4 (Implement) | Timeline checklist | High |
| 4 | next-courses-roadmap | Visual showing recommended next courses: BTC104 (Security), SCU102 (Fraud), BTC101 (Fundamentals) | Course roadmap | Medium |
| 5 | key-takeaways-summary | Summary graphic: No perfect method, Self-custody non-negotiable, Strategy evolves, Ask questions | Summary | High |

#### Going Further Chapter (TO BE CREATED - needs 1-2 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | btc105-resources-summary | Visual summary of all resources mentioned in course: Tutorials, Platforms, Next courses | Resource map | High |
| 2 | golden-rules-acquisition | Summary of golden rules for acquiring bitcoin | Summary graphic | Medium |

---

### A6. Quiz Inventory

**Summary:**
| Metric | Count |
|--------|-------|
| Current quizzes | 9 |
| Content chapters (needing quizzes) | 14 |
| Required per-chapter (14 x 5) | 70 |
| Required for final exam | 40 |
| **Total recommended** | **110** |
| **GAP** | **101 quizzes to create** |

**Per-Chapter Breakdown:**

| Ch # | Chapter Title | chapterId | Current | Required | Gap |
|------|---------------|-----------|---------|----------|-----|
| 1 | Welcome to BTC105 | welcome-ch01 | 0 | 0 | 0 |
| 2 | Prerequisites Before Buying Bitcoin | prerequisites-ch02 | 1 | 5 | 4 |
| 3 | The Key Questions | key-questions-ch03 | 1 | 5 | 4 |
| 4 | Understanding the Trade-offs | tradeoffs-ch04 | 1 | 5 | 4 |
| 5 | Lump Sum Purchase (KYC) | lumpsum-kyc-ch05 | 0 | 5 | 5 |
| 6 | Lump Sum Purchase (No-KYC) | lumpsum-nokyc-ch06 | 0 | 5 | 5 |
| 7 | DCA - Dollar Cost Averaging (KYC) | dca-kyc-ch07 | 2 | 5 | 3 |
| 8 | DCA Without KYC | dca-nokyc-ch08 | 0 | 5 | 5 |
| 9 | Bitcoin ETFs | etf-ch09 | 0 | 5 | 5 |
| 10 | Corporate Treasury & TradFi | treasury-tradfi-ch10 | 0 | 5 | 5 |
| 11 | Common Alternatives | common-alternatives-ch11 | 4 | 5 | 1 |
| 12 | Obscure & Advanced Methods | obscure-methods-ch12 | 0 | 5 | 5 |
| 13 | All Methods Are Valid | all-methods-valid-ch13 | 0 | 5 | 5 |
| 14 | Securing Your Bitcoin | securing-bitcoin-ch14 | 0 | 5 | 5 |
| 15 | Taxes & Compliance | taxes-compliance-ch15 | 0 | 5 | 5 |
| 16 | Selling & Off-Ramping | selling-offramp-ch16 | 0 | 5 | 5 |
| 17 | Building Your Personal Strategy | personal-strategy-ch17 | 0 | 5 | 5 |
| 18 | Conclusion | conclusion-ch18 | 0 | 0 | 0 |
| - | Going Further (MISSING) | - | 0 | 0 | 0 |
| - | **Final Exam Pool** | - | - | 40 | 40 |

**Current Quiz Mapping:**

| Quiz # | chapterId | Linked Chapter | Topic (inferred from tags) |
|--------|-----------|----------------|---------------------------|
| 000 | key-questions-ch03 | Ch 3: The Key Questions | Good practice / wallets |
| 001 | prerequisites-ch02 | Ch 2: Prerequisites | Good practice / wallets |
| 002 | tradeoffs-ch04 | Ch 4: Understanding Trade-offs | Good practice / wallets |
| 003 | dca-kyc-ch07 | Ch 7: DCA (KYC) | Good practice / wallets |
| 004 | dca-kyc-ch07 | Ch 7: DCA (KYC) | Good practice / wallets |
| 005 | common-alternatives-ch11 | Ch 11: Common Alternatives | Good practice / wallets |
| 006 | common-alternatives-ch11 | Ch 11: Common Alternatives | Good practice / wallets |
| 007 | common-alternatives-ch11 | Ch 11: Common Alternatives | Good practice / wallets |
| 008 | common-alternatives-ch11 | Ch 11: Common Alternatives | Good practice / wallets |

---

### A7. Missing Quizzes - Topic Suggestions

#### Chapter 2: Prerequisites Before Buying Bitcoin (needs 4 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | "Not your keys, not your coins" - what does this principle mean? | Multiple-choice | Easy |
| 2 | What is the main difference between hot wallets and hardware wallets? | Multiple-choice | Easy |
| 3 | Why is it important to have a wallet ready BEFORE buying bitcoin? | Multiple-choice | Medium |
| 4 | What should you NEVER do with your recovery phrase? | Multiple-choice | Easy |

#### Chapter 3: The Key Questions (needs 4 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | What is DCA (Dollar Cost Averaging)? | Multiple-choice | Easy |
| 2 | What factors should you consider when choosing an acquisition method? | Multiple-choice | Medium |
| 3 | What is the main trade-off between KYC and No-KYC methods? | Multiple-choice | Medium |
| 4 | Why might regional availability affect your acquisition options? | Multiple-choice | Medium |

#### Chapter 4: Understanding the Trade-offs (needs 4 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | What is the main privacy risk of using KYC exchanges? | Multiple-choice | Medium |
| 2 | Why do No-KYC methods typically have higher premiums? | Multiple-choice | Medium |
| 3 | What is blockchain analysis and how does KYC enable it? | Multiple-choice | Hard |
| 4 | When might someone choose convenience over privacy? | Multiple-choice | Medium |

#### Chapter 5: Lump Sum Purchase (KYC) (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | What is the typical first step when using a KYC exchange? | Multiple-choice | Easy |
| 2 | Why are bank transfers usually cheaper than credit card purchases? | Multiple-choice | Easy |
| 3 | What should you do immediately after buying on an exchange? | Multiple-choice | Easy |
| 4 | What is the difference between a market order and a limit order? | Multiple-choice | Medium |
| 5 | Why is it important to research an exchange before using it? | Multiple-choice | Medium |

#### Chapter 6: Lump Sum Purchase (No-KYC) (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | What is an escrow system in P2P trading? | Multiple-choice | Medium |
| 2 | What is the typical premium for No-KYC purchases? | Multiple-choice | Easy |
| 3 | Name a safety consideration for in-person bitcoin trades | Multiple-choice | Easy |
| 4 | What are the advantages of P2P platforms like Bisq or Peach? | Multiple-choice | Medium |
| 5 | Why might P2P transactions take longer than exchange purchases? | Multiple-choice | Medium |

#### Chapter 7: DCA - Dollar Cost Averaging (KYC) (needs 3 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | What is the main psychological benefit of DCA? | Multiple-choice | Medium |
| 2 | What should you do periodically when using DCA services? | Multiple-choice | Medium |
| 3 | Why is consistency more important than amount in DCA? | Multiple-choice | Medium |

#### Chapter 8: DCA Without KYC (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | What is the main challenge of doing DCA without KYC? | Multiple-choice | Easy |
| 2 | What platforms can be used for manual No-KYC DCA? | Multiple-choice | Easy |
| 3 | Why might batching purchases be better for No-KYC DCA? | Multiple-choice | Medium |
| 4 | How does the time requirement differ between KYC and No-KYC DCA? | Multiple-choice | Easy |
| 5 | What is a Lightning-based P2P platform? | Multiple-choice | Medium |

#### Chapter 9: Bitcoin ETFs (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | What is a Bitcoin ETF? | Multiple-choice | Easy |
| 2 | What is the difference between a Spot ETF and a Futures ETF? | Multiple-choice | Medium |
| 3 | Why do Bitcoin ETFs NOT give you actual bitcoin ownership? | Multiple-choice | Easy |
| 4 | What is a potential benefit of ETFs for retirement accounts? | Multiple-choice | Medium |
| 5 | What annual fees do Bitcoin ETFs typically charge? | Multiple-choice | Medium |

#### Chapter 10: Corporate Treasury & TradFi Solutions (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | Why might a company hold bitcoin in its treasury? | Multiple-choice | Medium |
| 2 | What is qualified custody? | Multiple-choice | Hard |
| 3 | What happened to platforms like Celsius that offered bitcoin yield products? | Multiple-choice | Medium |
| 4 | What compliance considerations do businesses face when acquiring bitcoin? | Multiple-choice | Hard |
| 5 | When might institutional custody solutions be appropriate? | Multiple-choice | Medium |

#### Chapter 11: Common Alternatives (needs 1 quiz)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | What are the typical fees at Bitcoin ATMs? | Multiple-choice | Easy |

#### Chapter 12: Obscure & Advanced Methods (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | What determines profitability in bitcoin mining? | Multiple-choice | Medium |
| 2 | What is a bitcoin voucher? | Multiple-choice | Easy |
| 3 | Where can you find in-person bitcoin trading opportunities? | Multiple-choice | Easy |
| 4 | How can running a Lightning node help you earn bitcoin? | Multiple-choice | Hard |
| 5 | Why is accepting bitcoin for your business a good acquisition method? | Multiple-choice | Medium |

#### Chapter 13: All Methods Are Valid (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | Why is there "no wrong way" to acquire bitcoin? | Multiple-choice | Easy |
| 2 | What is more important than optimizing your acquisition method? | Multiple-choice | Easy |
| 3 | How might a user's acquisition strategy evolve over time? | Multiple-choice | Medium |
| 4 | What is "analysis paralysis" in the context of bitcoin acquisition? | Multiple-choice | Medium |
| 5 | Are KYC-purchased and No-KYC-purchased bitcoin distinguishable on the blockchain? | True-false | Medium |

#### Chapter 14: Securing Your Bitcoin (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | What is the first step before withdrawing bitcoin from an exchange? | Multiple-choice | Easy |
| 2 | How should your wallet setup evolve as your holdings grow? | Multiple-choice | Medium |
| 3 | What should you NEVER do with a digital copy of your recovery phrase? | Multiple-choice | Easy |
| 4 | Why should you test your backup before storing significant amounts? | Multiple-choice | Medium |
| 5 | What course covers bitcoin security in detail? | Multiple-choice | Easy |

#### Chapter 15: Taxes & Compliance (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | How is bitcoin typically treated for tax purposes? | Multiple-choice | Easy |
| 2 | Is buying bitcoin with fiat typically a taxable event? | True-false | Easy |
| 3 | What information should you track for tax purposes? | Multiple-choice | Medium |
| 4 | What is the benefit of holding bitcoin for more than one year before selling? | Multiple-choice | Medium |
| 5 | Do No-KYC purchases have the same legal tax obligations as KYC purchases? | True-false | Medium |

#### Chapter 16: Selling & Off-Ramping (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | What are legitimate reasons to sell bitcoin? | Multiple-choice | Easy |
| 2 | How does the selling process on a KYC exchange work? | Multiple-choice | Easy |
| 3 | What are alternatives to converting bitcoin to fiat? | Multiple-choice | Medium |
| 4 | What is the "spend and replace" strategy? | Multiple-choice | Medium |
| 5 | Why should you plan your off-ramp strategy in advance? | Multiple-choice | Medium |

#### Chapter 17: Building Your Personal Strategy (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | What should a beginner prioritize in their first week with bitcoin? | Multiple-choice | Easy |
| 2 | What is the recommended progression for wallet security? | Multiple-choice | Medium |
| 3 | Why might someone combine multiple acquisition methods? | Multiple-choice | Medium |
| 4 | What courses are recommended after completing BTC105? | Multiple-choice | Easy |
| 5 | What is the most important action after acquiring bitcoin? | Multiple-choice | Easy |

#### Final Exam Pool (needs 40 quizzes)

| # | Topic | Related Chapter | Difficulty |
|---|-------|-----------------|------------|
| 1 | Core principle: Not your keys, not your coins | Ch 2 | Easy |
| 2 | Hot wallet vs Hardware wallet security comparison | Ch 2 | Medium |
| 3 | Recovery phrase best practices | Ch 2 | Easy |
| 4 | DCA definition and benefits | Ch 3, 7 | Easy |
| 5 | KYC vs No-KYC fundamental trade-off | Ch 3, 4 | Medium |
| 6 | Privacy risks of blockchain analysis | Ch 4 | Hard |
| 7 | Fee comparison across acquisition methods | Ch 4 | Medium |
| 8 | Exchange KYC process steps | Ch 5 | Easy |
| 9 | Importance of immediate withdrawal | Ch 5 | Easy |
| 10 | P2P escrow mechanism | Ch 6 | Medium |
| 11 | No-KYC premium explanation | Ch 6 | Medium |
| 12 | DCA volatility smoothing effect | Ch 7 | Medium |
| 13 | UTXO consolidation in DCA | Ch 7 | Hard |
| 14 | No-KYC DCA discipline requirement | Ch 8 | Medium |
| 15 | Spot ETF vs Futures ETF | Ch 9 | Medium |
| 16 | ETF limitations (not actual bitcoin) | Ch 9 | Easy |
| 17 | ETF fee structure | Ch 9 | Easy |
| 18 | Corporate treasury rationale | Ch 10 | Medium |
| 19 | Counterparty risk in yield products | Ch 10 | Medium |
| 20 | Earning bitcoin for work | Ch 11 | Easy |
| 21 | Gift card acquisition strategies | Ch 11 | Easy |
| 22 | Bitcoin ATM fee ranges | Ch 11 | Easy |
| 23 | Home mining profitability factors | Ch 12 | Medium |
| 24 | Lightning node routing fees | Ch 12 | Hard |
| 25 | Bitcoin fungibility concept | Ch 13 | Medium |
| 26 | Strategy evolution patterns | Ch 13 | Medium |
| 27 | Self-custody as top priority | Ch 13 | Easy |
| 28 | Exchange to wallet withdrawal steps | Ch 14 | Easy |
| 29 | Wallet security progression | Ch 14 | Medium |
| 30 | Backup storage best practices | Ch 14 | Easy |
| 31 | Tax treatment of bitcoin | Ch 15 | Medium |
| 32 | Taxable vs non-taxable events | Ch 15 | Medium |
| 33 | Long-term vs short-term capital gains | Ch 15 | Medium |
| 34 | Record-keeping requirements | Ch 15 | Medium |
| 35 | KYC vs No-KYC tax obligations | Ch 15 | Medium |
| 36 | Off-ramp methods comparison | Ch 16 | Medium |
| 37 | Spend and replace strategy | Ch 16 | Medium |
| 38 | Spending as alternative to selling | Ch 16 | Easy |
| 39 | First 30 days checklist priorities | Ch 17 | Easy |
| 40 | Combined acquisition strategy examples | Ch 17 | Medium |

---

### A8. Structural Fixes Required

| # | Issue | Location | Fix Required | Priority |
|---|-------|----------|--------------|----------|
| 1 | **Missing "Going Further" chapter** | Part 5 (end) | Add "Going Further" chapter as last chapter of Part 5 (after-purchase-part5). Should contain: Resources summary, recommended next steps, golden rules for bitcoin acquisition | **Critical** |
| 2 | **Conclusion Part has wrong structure** | Part 6 (conclusion-part6) | Move Chapter 17 "Building Your Personal Strategy" from Part 6 to Part 5. Part 6 should contain ONLY Chapter 18 "Conclusion" | **Critical** |
| 3 | **Renumber chapters after restructure** | Multiple | After moving Ch17 and adding Going Further, ensure chapter IDs remain consistent. Current Ch17 becomes Part 5 chapter, new Going Further becomes Part 5 final chapter, Conclusion remains as sole chapter in Part 6 | **Critical** |

**Recommended Final Structure:**

```
Part 5: After Your First Purchase (after-purchase-part5)
  - Ch 13: All Methods Are Valid (all-methods-valid-ch13)
  - Ch 14: Securing Your Bitcoin (securing-bitcoin-ch14)
  - Ch 15: Taxes & Compliance (taxes-compliance-ch15)
  - Ch 16: Selling & Off-Ramping (selling-offramp-ch16)
  - Ch 17: Building Your Personal Strategy (personal-strategy-ch17) <-- MOVED FROM PART 6
  - Ch 18: Going Further (going-further-ch18) <-- NEW CHAPTER

Part 6: Conclusion (conclusion-part6)
  - Ch 19: Conclusion (conclusion-ch19) <-- RENUMBERED
  <isCourseConclusion>true</isCourseConclusion>
```

---

### A9. Work Summary for Phase B

**Before starting Phase B, complete these tasks:**

#### Critical (Must Do)
- [ ] Add "Going Further" chapter to Part 5 with resources, next steps, and golden rules
- [ ] Move "Building Your Personal Strategy" chapter from Part 6 to Part 5
- [ ] Ensure Conclusion Part contains ONLY the Conclusion chapter
- [ ] Update chapter IDs/numbers as needed after restructure
- [ ] Verify `<isCourseConclusion>true</isCourseConclusion>` remains on final Conclusion chapter

#### Images to Create (52-66 total)
- [ ] Ch 1: 0-1 images (see specs in A5)
- [ ] Ch 2: 4-5 images (see specs in A5)
- [ ] Ch 3: 4-5 images (see specs in A5)
- [ ] Ch 4: 3-4 images (see specs in A5)
- [ ] Ch 5: 4-5 images (see specs in A5)
- [ ] Ch 6: 4-5 images (see specs in A5)
- [ ] Ch 7: 2-3 images (see specs in A5)
- [ ] Ch 8: 4-5 images (see specs in A5)
- [ ] Ch 9: 4-5 images (see specs in A5)
- [ ] Ch 10: 4-5 images (see specs in A5)
- [ ] Ch 11: 3-4 images (see specs in A5)
- [ ] Ch 12: 4-5 images (see specs in A5)
- [ ] Ch 13: 4-5 images (see specs in A5)
- [ ] Ch 14: 4-5 images (see specs in A5)
- [ ] Ch 15: 4-5 images (see specs in A5)
- [ ] Ch 16: 4-5 images (see specs in A5)
- [ ] Ch 17: 4-5 images (see specs in A5)
- [ ] Going Further: 1-2 images (see specs in A5)

#### Quizzes to Create (101 total)
- [ ] Ch 2: 4 quizzes (see topics in A7)
- [ ] Ch 3: 4 quizzes (see topics in A7)
- [ ] Ch 4: 4 quizzes (see topics in A7)
- [ ] Ch 5: 5 quizzes (see topics in A7)
- [ ] Ch 6: 5 quizzes (see topics in A7)
- [ ] Ch 7: 3 quizzes (see topics in A7)
- [ ] Ch 8: 5 quizzes (see topics in A7)
- [ ] Ch 9: 5 quizzes (see topics in A7)
- [ ] Ch 10: 5 quizzes (see topics in A7)
- [ ] Ch 11: 1 quiz (see topics in A7)
- [ ] Ch 12: 5 quizzes (see topics in A7)
- [ ] Ch 13: 5 quizzes (see topics in A7)
- [ ] Ch 14: 5 quizzes (see topics in A7)
- [ ] Ch 15: 5 quizzes (see topics in A7)
- [ ] Ch 16: 5 quizzes (see topics in A7)
- [ ] Ch 17: 5 quizzes (see topics in A7)
- [ ] Final exam pool: 40 quizzes (see topics in A7)

---

**Phase A Status:** ✅ COMPLETE
**Phase A Completed:** 2026-01-21
**Notes:** Course has solid content but needs structural fixes (missing Going Further chapter, incorrect Conclusion Part structure). Significant image gap (4 current vs 56-70 target) and quiz gap (9 current vs 110 target) identified. Detailed specifications provided for all missing assets. Structure fixes are critical priority before Phase B.
