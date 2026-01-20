# BTC105 - How to Acquire Bitcoin: Implementation Document

## Course Overview

**Course Code**: BTC105
**Discipline**: Bitcoin (BTC)
**Level**: Beginner (105)
**Estimated Duration**: 2-2.5 hours
**Source**: BTC102 Part 3 - "Setting up your plan" (lines 1195-2191)
**Focus**: Bitcoin acquisition methods and purchasing strategies

---

## Revised Plan (v2) - January 2026

### Problem with v1 Structure

The original plan had redundancy between:
- Part 2 (Understanding Your Profile) - explaining profile types
- Part 4 (Acquisition Strategies by Profile) - repeating profiles with acquisition focus

### New Approach

Instead of organizing by user profiles, organize by **acquisition method**:
- Part 2 → Decision framework (help users find the right solution)
- Part 3 → One chapter per acquisition solution

---

## Available Exchange Tutorials Analysis

Based on analysis of `tutorials/exchange/` (36 tutorials):

### By Type:
| Category | Tutorials | Examples |
|----------|-----------|----------|
| **DCA Services (KYC)** | 5 | Relai, Stackinsat, Bitstack, Bull-bitcoin-europe, Bittr |
| **DCA Services (No-KYC)** | 2 | Stackinsat (partial), manual via P2P |
| **Lump Sum (KYC)** | 8 | Kraken, Bitstamp, Bitfinex, Paymium, Bitcoinvn |
| **Lump Sum (No-KYC)** | 0 | (use P2P platforms) |
| **P2P Platforms (No-KYC)** | 9 | Bisq, Peach, Robosats, Hodlhodl, Vexl, Mostro, Lnp2pbot |
| **Gift Cards/Spending** | 3 | Bitrefill, Moon, Coincards |
| **Swap Services** | 4 | Boltz, Kaleidoswap, Swap-market, Zeus-swap |
| **Regional** | 5 | Paymium (FR), Bitcoinvn (VN), Ejara (Africa), Tando, Bull-bitcoin-europe |

### Key Insight: No ETF Tutorials
There are currently no ETF-related tutorials in the repository. This is a gap worth addressing in BTC105, as ETFs are a significant acquisition method for traditional investors.

---

## NEW Course Structure (6 Parts, 17 Chapters)

```
# Part 1: Introduction
<partId>introduction-part1</partId>

## Chapter 1: Welcome to BTC105
<chapterId>welcome-ch01</chapterId>
[NEW - Course introduction, objectives, what you'll learn]

## Chapter 2: Prerequisites Before Buying Bitcoin
<chapterId>prerequisites-ch02</chapterId>
[NEW - Critical setup before first purchase]
- Why you need a wallet BEFORE buying
- Wallet types overview (hot vs hardware - details in BTC104)
- Exchange account vs self-custody concept
- Security basics reminder (link to SCU courses)
- Common beginner mistakes to avoid

# Part 2: Choosing Your Acquisition Strategy
<partId>strategy-decision-part2</partId>

## Chapter 3: The Key Questions
<chapterId>key-questions-ch03</chapterId>
[NEW + ORIGINAL - Decision framework]
- How much do you want to invest? (one-time vs recurring)
- Privacy preference: KYC or No-KYC?
- Time availability: manual or automated?
- Technical comfort level
- Regional availability considerations

## Chapter 4: Understanding the Trade-offs
<chapterId>tradeoffs-ch04</chapterId>
[ORIGINAL: lines 1388-1441 + NEW]
- KYC vs No-KYC: pros and cons
- Convenience vs Privacy spectrum
- Fees comparison across methods
- Decision matrix / flowchart

# Part 3: Acquisition Methods (One chapter per solution)
<partId>acquisition-methods-part3</partId>

## Chapter 5: Lump Sum Purchase (KYC)
<chapterId>lumpsum-kyc-ch05</chapterId>
[NEW + ORIGINAL - One-time purchases on centralized exchanges]
- When to use: large initial investment, traditional finance users
- How it works: exchange account → deposit fiat → buy → withdraw
- Recommended platforms: Kraken, Bitstamp, Bitfinex, Paymium (regional)
- Step-by-step guidance
- → Link to tutorials: kraken, bitstamp, bitfinex, paymium

## Chapter 6: Lump Sum Purchase (No-KYC)
<chapterId>lumpsum-nokyc-ch06</chapterId>
[NEW + ORIGINAL - P2P one-time purchases]
- When to use: privacy-conscious, avoiding KYC
- How it works: P2P marketplaces, escrow, various payment methods
- Recommended platforms: Bisq, Peach, Robosats, Hodlhodl, Vexl
- Premium/fees to expect
- Step-by-step guidance
- → Link to tutorials: bisq, peach, robosats, hodlhodl, vexl

## Chapter 7: DCA - Dollar Cost Averaging (KYC)
<chapterId>dca-kyc-ch07</chapterId>
[ORIGINAL: lines 1633-1781 - Stacker content + NEW]
- When to use: regular income, long-term accumulation mindset
- How it works: automated recurring purchases
- Benefits of DCA (averaging out volatility, discipline)
- Recommended platforms: Relai, Stackinsat, Bitstack, Bull-bitcoin-europe
- Setting up automation
- → Link to tutorials: relai-v2, stackinsat, bitstack, bull-bitcoin-europe

## Chapter 8: DCA Without KYC
<chapterId>dca-nokyc-ch08</chapterId>
[ORIGINAL: Paranoid content + NEW]
- When to use: privacy-focused stackers
- Challenge: automation is harder without KYC
- Manual DCA approach using P2P platforms
- Semi-automated options: Bitcoin vouchers, P2P bots
- Tools: Robosats, Peach (regular manual purchases), bitcoin-voucher-bot-p2p
- → Link to tutorials: robosats, peach, bitcoin-voucher-bot-p2p

## Chapter 9: Bitcoin ETFs
<chapterId>etf-ch09</chapterId>
[NEW - Important for traditional investors]
- What is a Bitcoin ETF?
- Spot ETF vs Futures ETF
- Pros: familiar brokerage, tax advantages (retirement accounts), regulated
- Cons: not your keys, fees, counterparty risk, no Bitcoin network access
- Major ETFs: BlackRock (IBIT), Fidelity (FBTC), etc.
- Who should consider ETFs
- Important caveat: "Not your keys, not your coins"

## Chapter 10: Corporate Treasury & TradFi Solutions
<chapterId>treasury-tradfi-ch10</chapterId>
[NEW - For businesses and institutions]
- Corporate Bitcoin treasury (MicroStrategy model)
- Bitcoin for business: why companies hold BTC
- Custodial solutions for institutions (Coinbase Prime, Fidelity Digital Assets)
- Bitcoin-backed financial products (loans, yield - with warnings)
- Regulated investment vehicles beyond ETFs
- Compliance and accounting considerations
- Who this is for: businesses, family offices, institutions

# Part 4: Alternative Acquisition Methods
<partId>alternatives-part4</partId>

## Chapter 11: Common Alternatives
<chapterId>common-alternatives-ch11</chapterId>
[ORIGINAL: Active User content + NEW]
- Earning BTC for work/services (freelancing, salary in BTC)
- Bitcoin-back rewards & cashback programs
- Gift cards: Bitrefill, Moon, Coincards
- Bitcoin ATMs: how they work, fees, KYC levels
- → Link to tutorials: bitrefill, moon, coincards

## Chapter 12: Obscure & Advanced Methods
<chapterId>obscure-methods-ch12</chapterId>
[NEW + ORIGINAL: Paranoid content]
- Mining (solo, pool, home mining) - brief overview
- Bitcoin vouchers & prepaid cards
- In-person cash trades (meetups, conferences)
- Earning through Lightning Network (routing fees)
- Accepting BTC payments for business
- → Link to tutorials: mining tutorials

# Part 5: After Your First Purchase
<partId>after-purchase-part5</partId>

## Chapter 13: All Methods Are Valid
<chapterId>all-methods-valid-ch13</chapterId>
[NEW - Reassurance and flexibility]
- Recap: there's no "wrong" way to acquire Bitcoin
- Your strategy can evolve over time
- Common progression paths (KYC → No-KYC, Lump sum → DCA, etc.)
- Don't let perfect be the enemy of good - just start
- You can always change methods later

## Chapter 14: Securing Your Bitcoin
<chapterId>securing-bitcoin-ch14</chapterId>
[NEW - Bridge to BTC104]
- Why security matters AFTER purchase
- Moving from exchange to self-custody
- Wallet setup basics (hot wallet first, hardware later)
- → Link to BTC104 for detailed security course

## Chapter 15: Taxes & Compliance
<chapterId>taxes-compliance-ch15</chapterId>
[NEW - Important reality check]
- Tax implications of buying Bitcoin (varies by country)
- Record-keeping best practices
- When/why to consult a tax professional
- KYC vs No-KYC: tax reporting differences
- Brief disclaimer: not financial/tax advice

## Chapter 16: Selling & Off-Ramping (The Reverse)
<chapterId>selling-offramp-ch16</chapterId>
[NEW - Complete the cycle]
- Why you might need to sell (not just "never sell")
- Same platforms work in reverse (exchanges, P2P)
- KYC exchanges for large off-ramps
- No-KYC options: P2P, gift cards, spending directly
- Tax events when selling
- → Link to relevant tutorials (same platforms)

# Part 6: Conclusion
<partId>conclusion-part6</partId>

## Chapter 17: Building Your Personal Strategy
<chapterId>personal-strategy-ch17</chapterId>
[NEW - Action plan]
- Summary decision tree / flowchart
- Combining methods (e.g., lump sum + DCA)
- Your first 30 days checklist
- Resources and next steps
- Link to BTC104 (security), BTC106 (using Bitcoin)

## Chapter 18: Conclusion
<chapterId>conclusion-ch18</chapterId>
<isCourseConclusion>true</isCourseConclusion>
```

**Total: 6 Parts, 18 Chapters**

---

## Comparison: v1 vs v2 vs v3 (Current)

| v1 (Original) | v2 (Jan 19 AM) | v3 (Current) |
|---------------|----------------|--------------|
| Part 1: Intro (1 ch) | Part 1: Intro (2 ch) | Part 1: Intro (2 ch) |
| Part 2: Profiles (3 ch) | Part 2: Strategy (2 ch) | Part 2: Strategy (2 ch) |
| Part 3: Methods (3 ch) | Part 3: Methods (5 ch) | Part 3: Methods (6 ch) + Treasury |
| Part 4: By Profile (4 ch) | Part 4: Alternatives (1 ch) | Part 4: Alternatives (2 ch) - split |
| Part 5: Implementation (2 ch) | - | Part 5: After Purchase (4 ch) - NEW |
| Part 6: Conclusion (1 ch) | Part 5: Conclusion (2 ch) | Part 6: Conclusion (2 ch) |
| **14 chapters** | **12 chapters** | **18 chapters** |

### Key Changes in v3:
- Added Ch 10: Corporate Treasury & TradFi
- Split alternatives into Common (Ch 11) vs Obscure (Ch 12)
- NEW Part 5 "After Your First Purchase" with:
  - Ch 13: All Methods Are Valid (reassurance)
  - Ch 14: Securing Your Bitcoin (bridge to BTC104)
  - Ch 15: Taxes & Compliance
  - Ch 16: Selling & Off-Ramping

---

## Tutorial Links Mapping

| Chapter | Tutorials to Link |
|---------|-------------------|
| Ch 5: Lump Sum KYC | kraken, bitstamp, bitfinex, paymium, bitcoinvn |
| Ch 6: Lump Sum No-KYC | bisq, bisq-v2, peach, robosats, hodlhodl, vexl, mostro |
| Ch 7: DCA KYC | relai-v2, stackinsat, bitstack, bull-bitcoin-europe, bittr |
| Ch 8: DCA No-KYC | robosats, peach, bitcoin-voucher-bot-p2p, lnp2pbot-v2 |
| Ch 9: ETFs | No tutorials yet (consider creating) |
| Ch 10: Treasury/TradFi | No tutorials yet (institutional focus) |
| Ch 11: Common Alternatives | bitrefill, moon, coincards, tando, flash |
| Ch 12: Obscure Methods | mining tutorials, bitcoin-voucher-bot-p2p |
| Ch 16: Selling/Off-ramp | Same as buying platforms (reverse flow)

---

## Open Questions

1. **ETF Chapter**: Should we create a standalone ETF tutorial, or is the chapter content sufficient?

2. **Regional Content**: How to handle region-specific platforms (Paymium for France, etc.)?
   - Option A: Mention in main chapters with regional flags
   - Option B: Separate "Regional Options" chapter

3. **Lightning-specific**: Should Lightning-native solutions (Robosats, Mostro) get special attention or be integrated into No-KYC chapters?

4. **Swap Services**: Boltz, Kaleidoswap, etc. - where do they fit? (More for converting than acquiring)

---

## Source Content Mapping (BTC102 en.md) - Updated for v3

| BTC102 Section | Lines | BTC105 Chapter (v3) |
|----------------|-------|---------------------|
| "Choose your profile" intro | 1199-1229 | Ch 3: Key Questions |
| Risks and lifestyle | 1231-1275 | Ch 4: Trade-offs |
| Wallet types overview | 1286-1386 | Ch 2: Prerequisites |
| KYC vs No-KYC | 1388-1441 | Ch 4: Trade-offs |
| Four profiles overview | 1443-1507 | NOT USED (profile approach removed) |
| Hodler chapter | 1509-1631 | Ch 5: Lump Sum KYC |
| Stacker chapter | 1633-1781 | Ch 7: DCA KYC |
| Active User chapter | 1783-1974 | Ch 11: Common Alternatives |
| Paranoid chapter | 1976-2190 | Ch 6, 8, 12: No-KYC methods |

---

## Quiz Mapping (Needs Update for v3)

**Note**: Quiz mapping needs to be revised for new chapter structure. Original profile-based quizzes will be redistributed to method-based chapters.

| Original Topic | New Target Chapter (v3) |
|----------------|-------------------------|
| Profile factors, investment considerations | Ch 3: Key Questions, Ch 4: Trade-offs |
| Wallet selection | Ch 2: Prerequisites |
| KYC acquisition | Ch 5: Lump Sum KYC |
| DCA fundamentals, platforms | Ch 7: DCA KYC |
| P2P methods, anonymous buying | Ch 6: Lump Sum No-KYC, Ch 8: DCA No-KYC |
| Earning BTC | Ch 11: Common Alternatives |
| Security-related quizzes | → BTC104 |

**NEW quizzes needed for v3**:
- Ch 9: ETFs (NEW topic)
- Ch 10: Treasury/TradFi (NEW topic)
- Ch 13: All Methods Valid (reassurance)
- Ch 15: Taxes & Compliance (NEW topic)
- Ch 16: Selling & Off-Ramping (NEW topic)

---

## Asset Mapping (Needs Update for v3)

Assets will need to be remapped to new chapter structure. Key changes:
- Profile-specific images → redistributed to method chapters
- NEW images needed for: ETFs, Treasury, Taxes, Selling

| Asset Category | Source | Target Chapters (v3) |
|----------------|--------|----------------------|
| Decision framework | BTC102 065-069 | Ch 3, 4 |
| Wallet overview | BTC102 070-072 | Ch 2: Prerequisites |
| Acquisition methods | BTC102 073 | Ch 5, 6, 7, 8 |
| DCA illustrations | BTC102 080-084 | Ch 7: DCA KYC |
| P2P illustrations | BTC102 091-096 | Ch 6, 8: No-KYC |
| Earning BTC | BTC102 085-090 | Ch 11: Common Alternatives |
| Hardware/security images | BTC102 076, 081, 087, 093, 094 | → BTC104 |

**NEW assets needed**:
- Ch 9: ETF comparison chart, brokerage screenshot examples
- Ch 10: Corporate treasury diagram
- Ch 15: Tax record-keeping illustration
- Ch 16: Off-ramp flowchart

---

## Content Classification (v3)

| Content Type | Chapters | Notes |
|--------------|----------|-------|
| NEW | Ch 1, 9, 10, 13, 14, 15, 16, 17, 18 | Intro, ETFs, Treasury, After Purchase section, Conclusion |
| ORIGINAL (adapted) | Ch 2, 3, 4 | Decision framework content |
| ORIGINAL (adapted) | Ch 5, 6, 7, 8 | Acquisition methods (reorganized by method, not profile) |
| ORIGINAL (adapted) | Ch 11, 12 | Alternatives (split into common vs obscure) |

---

## Cross-References

BTC105 should cross-reference:
- **BTC104** (How to Secure Bitcoin): Ch 2 (prerequisites), Ch 14 (securing), throughout
- **SCU102** (Financial Fraud & Security): Ch 2 (prerequisites), Ch 6 (P2P safety)
- **SCU101** (Computer Security tutorials): Ch 2 (prerequisites)
- **BTC106** (Using Bitcoin): Ch 17 (next steps) - if exists

---

## Implementation Checklist (v3) - ✅ COMPLETED

### Phase 1: Setup
- [x] Create `courses/btc105/` folder
- [x] Create `course.yml` with UUID and metadata
- [x] Create `en.md` with frontmatter

### Phase 2: Content Creation - Part 1 & 2
- [x] Ch 1: Write NEW welcome/intro
- [x] Ch 2: Write NEW prerequisites (wallet need, security basics)
- [x] Ch 3: Adapt decision framework from BTC102
- [x] Ch 4: Adapt trade-offs content from BTC102

### Phase 3: Content Creation - Part 3 (Acquisition Methods)
- [x] Ch 5: Lump Sum KYC (adapt from Hodler content)
- [x] Ch 6: Lump Sum No-KYC (adapt from Paranoid content)
- [x] Ch 7: DCA KYC (adapt from Stacker content)
- [x] Ch 8: DCA No-KYC (adapt from Paranoid content)
- [x] Ch 9: Write NEW ETF chapter
- [x] Ch 10: Write NEW Treasury/TradFi chapter

### Phase 4: Content Creation - Part 4 (Alternatives)
- [x] Ch 11: Common alternatives (adapt from Active User)
- [x] Ch 12: Obscure methods (adapt from Paranoid + NEW)

### Phase 5: Content Creation - Part 5 (After Purchase)
- [x] Ch 13: Write NEW "All Methods Valid" reassurance
- [x] Ch 14: Write NEW "Securing Your Bitcoin" bridge
- [x] Ch 15: Write NEW "Taxes & Compliance"
- [x] Ch 16: Write NEW "Selling & Off-Ramping"

### Phase 6: Content Creation - Part 6 (Conclusion)
- [x] Ch 17: Write NEW "Building Your Strategy"
- [x] Ch 18: Add standard conclusion

### Phase 7: Assets
- [x] Map and copy relevant images from BTC102 (073, 080, 082, 089 → 001-004)
- [ ] Create NEW images for ETF, Treasury, Taxes, Selling chapters (FUTURE)
- [x] Renumber all images
- [x] Update all image references

### Phase 8: Quizzes
- [x] Review and adapt existing quizzes to new chapters (9 quizzes copied)
- [ ] Create NEW quizzes for new chapters (9, 10, 13, 15, 16) (FUTURE)
- [x] Update quiz chapterIds

### Phase 9: Validation
- [x] Add ORIGINAL/NEW content tags
- [x] Validate markdown structure
- [x] Cross-check all tutorial links
- [x] Final review

---

## Key Decisions Made

1. **ETF Depth**: Overview with major ETF comparison table. Sufficient for beginner course.

2. **Treasury Chapter Audience**: Kept brief, acknowledging it's more relevant for business owners. Appropriate for awareness.

3. **Tax Chapter Scope**: General principles only with strong disclaimer. No regional sections - too variable.

4. **Selling Chapter**: Single chapter covering both KYC and No-KYC. Sufficient for beginner overview.

5. **Regional Platforms**: Mentioned in main chapters with notes (e.g., "France: Paymium").

6. **Chapter Order Change**: Swapped Ch 15 (Taxes) and Ch 16 (Selling) - taxes now comes before selling as requested.

---

## Final Implementation Summary

**Course**: BTC105 - How to Acquire Bitcoin
**Location**: `courses/btc105/`
**Structure**: 6 Parts, 18 Chapters

### Files Created
| File | Description |
|------|-------------|
| `course.yml` | Course metadata (id, topic: bitcoin, subtopic: acquisition, level: beginner) |
| `en.md` | Full course content (~1400 lines) with ORIGINAL/NEW tags |
| `assets/en/001-004.webp` | 4 images from BTC102 (073, 080, 082, 089) |
| `quizz/000-008/` | 9 quizzes adapted from BTC102 with updated chapterIds |

### Content Classification
| Type | Chapters |
|------|----------|
| NEW | Ch 1, 9, 10, 13, 14, 15, 16, 17, 18 |
| ORIGINAL (adapted) | Ch 2, 3, 4, 5, 6, 7, 8, 11, 12 |

### Quiz Mapping
| BTC105 Quiz | Source | Target Chapter |
|-------------|--------|----------------|
| 000 | BTC102/036 | Ch 3: Key Questions |
| 001 | BTC102/037 | Ch 2: Prerequisites |
| 002 | BTC102/039 | Ch 4: Trade-offs |
| 003 | BTC102/048 | Ch 7: DCA KYC |
| 004 | BTC102/049 | Ch 7: DCA KYC |
| 005 | BTC102/050 | Ch 11: Common Alternatives |
| 006 | BTC102/051 | Ch 11: Common Alternatives |
| 007 | BTC102/053 | Ch 11: Common Alternatives |
| 008 | BTC102/054 | Ch 11: Common Alternatives |

---

## Document History

| Date | Author | Changes |
|------|--------|---------|
| 2026-01-19 | Claude | Initial BTC105 review document created (v1) |
| 2026-01-19 | Claude | Revised to method-based structure (v2) - 12 chapters |
| 2026-01-19 | Claude | Added Treasury, split alternatives, added After Purchase section (v3) - 18 chapters |
| 2026-01-20 | Claude | **IMPLEMENTED**: Full course created. 6 Parts, 18 Chapters, 4 images, 9 quizzes. Swapped Ch 15/16 order. Added implementation summary. |

