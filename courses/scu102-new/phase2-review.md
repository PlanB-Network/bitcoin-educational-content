# SCU102 Phase 2 Review

> This document tracks all work needed to complete SCU102 for production.
> Location: `courses/scu102-new/phase2-review.md`

## Progress Tracker
| Phase | Status | Date | Session |
|-------|--------|------|---------|
| A - Structure Review | :white_check_mark: | 2026-01-21 | Claude Opus 4.5 |
| B - Pre-Production | :white_large_square: | | |
| C - Recording | :white_large_square: | | |
| D - Post-Production | :white_large_square: | | |

---

## Phase A: Structure & Content Review

### A1. Metadata Validation (course.yml)

| Field | Value | Status |
|-------|-------|--------|
| id | `7cf4360f-4491-43c4-a3d2-a746e92b2c48` | :white_check_mark: |
| topic | `security` | :white_check_mark: |
| subtopic | `fraud-protection` | :white_check_mark: |
| type | `theory` | :white_check_mark: |
| level | `beginner` | :white_check_mark: |
| hours | `3` | :white_check_mark: |
| professors_id | `2e1b5182-567e-453a-af29-36009340ff02` | :white_check_mark: |

**Issues:** None. All required fields are present and valid.

### A2. Frontmatter Validation (en.md)

- [x] `name` present and descriptive: "Prerequisite to Bitcoin"
- [x] `goal` is single sentence, action-oriented: "Learn to identify common scams, protect yourself from financial fraud, and build strong security habits for your Bitcoin journey."
- [x] `objectives` has 3-6 items (has 5 objectives)

**Issues:** None. Frontmatter is complete and well-formatted.

### A3. Structure Validation

- [x] First Part is Introduction
- [x] No text between Part headings and first Chapter
- [x] All Parts have `<partId>`
- [x] All Chapters have `<chapterId>`
- [ ] **Going Further is last chapter of last content Part** - Going Further (ch24) is in Part 6, but should be the last chapter before Conclusion Part
- [x] Conclusion Part exists with only Conclusion chapter
- [x] `<isCourseConclusion>true</isCourseConclusion>` tag present

**Course Structure Overview:**

| Part # | Part Title | partId | Chapters |
|--------|------------|--------|----------|
| 1 | Introduction | `intro-scu102-part1` | Ch1: Welcome to SCU102 |
| 2 | Financial Fraud | `financial-fraud-part2` | Ch2-5 (4 chapters) |
| 3 | Crypto Scams | `crypto-scams-part3` | Ch6-9 (4 chapters) |
| 4 | How to Protect Yourself | `protection-part4` | Ch10 (1 chapter) |
| 5 | Online Security | `online-security-part5` | Ch11-16 (6 chapters) |
| 6 | Tips for Bitcoin Beginners | `beginner-tips-part6` | Ch17-24 (8 chapters, includes Going Further) |
| 7 | Conclusion | `conclusion-part7` | Ch25: Conclusion |

**Chapter List:**

| Ch # | Chapter Title | chapterId | Part |
|------|---------------|-----------|------|
| 1 | Welcome to SCU102 | `intro-scu102-ch1` | 1-Introduction |
| 2 | Understanding Financial Fraud | `understanding-fraud-ch2` | 2-Financial Fraud |
| 3 | Pyramid & Ponzi Schemes | `ponzi-schemes-ch3` | 2-Financial Fraud |
| 4 | Pump & Dump Schemes | `pump-dump-ch4` | 2-Financial Fraud |
| 5 | Fake Giveaways & Lotteries | `fake-giveaways-ch5` | 2-Financial Fraud |
| 6 | Shitcoins & Airdrops | `shitcoins-ch6` | 3-Crypto Scams |
| 7 | Phishing & Identity Theft | `phishing-ch7` | 3-Crypto Scams |
| 8 | Bitcoin Hardforks Confusion | `hardforks-ch8` | 3-Crypto Scams |
| 9 | Dishonest Influencers | `influencers-ch9` | 3-Crypto Scams |
| 10 | Red Flags & Verification | `red-flags-ch10` | 4-Protection |
| 11 | Why Cybersecurity Matters | `cybersecurity-ch11` | 5-Online Security |
| 12 | Clean Computer Practices | `clean-computer-ch12` | 5-Online Security |
| 13 | Password Security | `passwords-ch13` | 5-Online Security |
| 14 | Two-Factor Authentication | `2fa-ch14` | 5-Online Security |
| 15 | Privacy Protection | `privacy-ch15` | 5-Online Security |
| 16 | Step-by-Step Security Progression | `progression-ch16` | 5-Online Security |
| 17 | Common Mistakes to Avoid | `mistakes-ch17` | 6-Beginner Tips |
| 18 | Investment Strategy Basics | `investment-ch18` | 6-Beginner Tips |
| 19 | Understanding Volatility | `volatility-ch19` | 6-Beginner Tips |
| 20 | Wallet Security Fundamentals | `wallet-security-ch20` | 6-Beginner Tips |
| 21 | Confidentiality & Discretion | `discretion-ch21` | 6-Beginner Tips |
| 22 | Tax Awareness | `taxes-ch22` | 6-Beginner Tips |
| 23 | Trading vs Investing vs Holding | `trading-investing-ch23` | 6-Beginner Tips |
| 24 | Going Further | `going-further-ch24` | 6-Beginner Tips |
| 25 | Conclusion | `conclusion-ch25` | 7-Conclusion |

**Issues:**
1. **CRITICAL: Quiz chapterId mismatch** - The 15 existing quizzes reference legacy chapterIds that do not match the new course chapterIds. All quiz question.yml files need to be updated with correct chapterIds from the new course structure.

---

### A4. Image Inventory

**Summary:**
| Metric | Count |
|--------|-------|
| Current images | 25 |
| Target images | ~88-95 |
| **GAP** | **~63-70 images to create** |

**Per-Chapter Breakdown:**

| Ch # | Chapter Title | Type | Current | Target | Gap | Images Referenced |
|------|---------------|------|---------|--------|-----|-------------------|
| 1 | Welcome to SCU102 | Introduction | 0 | 0-1 | 0 | None |
| 2 | Understanding Financial Fraud | Substantive | 2 | 4-5 | 2-3 | 001.webp, 002.webp |
| 3 | Pyramid & Ponzi Schemes | Substantive | 1 | 4-5 | 3-4 | 003.webp |
| 4 | Pump & Dump Schemes | Substantive | 2 | 4-5 | 2-3 | 004.webp, 005.webp |
| 5 | Fake Giveaways & Lotteries | Substantive | 1 | 4-5 | 3-4 | 006.webp |
| 6 | Shitcoins & Airdrops | Substantive | 0 | 4-5 | 4-5 | None |
| 7 | Phishing & Identity Theft | Substantive | 0 | 4-5 | 4-5 | None |
| 8 | Bitcoin Hardforks Confusion | Substantive | 1 | 4-5 | 3-4 | 007.webp |
| 9 | Dishonest Influencers | Substantive | 1 | 4-5 | 3-4 | 008.webp |
| 10 | Red Flags & Verification | Substantive | 0 | 4-5 | 4-5 | None |
| 11 | Why Cybersecurity Matters | Substantive | 0 | 4-5 | 4-5 | None |
| 12 | Clean Computer Practices | Substantive | 2 | 4-5 | 2-3 | 009.webp, 010.webp |
| 13 | Password Security | Substantive | 1 | 4-5 | 3-4 | 011.webp |
| 14 | Two-Factor Authentication | Substantive | 3 | 4-5 | 1-2 | 012.webp, 013.webp, 014.webp |
| 15 | Privacy Protection | Substantive | 2 | 4-5 | 2-3 | 015.webp, 016.webp |
| 16 | Step-by-Step Security Progression | Substantive | 0 | 4-5 | 4-5 | None |
| 17 | Common Mistakes to Avoid | Substantive | 2 | 4-5 | 2-3 | 017.webp, 018.webp |
| 18 | Investment Strategy Basics | Substantive | 1 | 4-5 | 3-4 | 019.webp |
| 19 | Understanding Volatility | Substantive | 1 | 4-5 | 3-4 | 020.webp |
| 20 | Wallet Security Fundamentals | Substantive | 2 | 4-5 | 2-3 | 021.webp, 022.webp |
| 21 | Confidentiality & Discretion | Substantive | 0 | 4-5 | 4-5 | None |
| 22 | Tax Awareness | Substantive | 2 | 4-5 | 2-3 | 023.webp, 024.webp |
| 23 | Trading vs Investing vs Holding | Substantive | 0 | 4-5 | 4-5 | None (has table instead) |
| 24 | Going Further | Going Further | 1 | 1-2 | 0-1 | 025.webp |
| 25 | Conclusion | Conclusion | 0 | 0 | 0 | None |

**Total Current Images:** 25
**Total Target Images (minimum):** 88 (22 substantive chapters x 4)
**Total Target Images (optimal):** 95 (22 substantive chapters x 4-5 + 2 for Going Further)
**Gap:** 63-70 images to create

---

### A5. Missing Images - Detailed Specifications

#### Chapter 2: Understanding Financial Fraud (needs 2-3 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | fraud-landscape | Overview diagram showing the types of fraud in crypto ecosystem - pyramid pointing to different scam types | Diagram | High |
| 2 | bitcoin-vs-crypto-comparison | Side-by-side comparison showing Bitcoin (stable, decentralized) vs altcoins (speculative, centralized) - complementing 001.webp | Illustration | Medium |
| 3 | fraud-warning-signs | Visual checklist of general warning signs for financial fraud | Infographic | Medium |

#### Chapter 3: Pyramid & Ponzi Schemes (needs 3-4 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | ponzi-mechanics | Step-by-step diagram showing how money flows in a Ponzi scheme - new investors paying old investors | Diagram | High |
| 2 | pyramid-growth | Visual showing exponential growth requirements of pyramid schemes and why they collapse | Diagram | High |
| 3 | defi-ponzi-example | Illustration of how DeFi protocols can mask Ponzi mechanics with technical jargon | Diagram | Medium |
| 4 | ponzi-red-flags | Checklist infographic of Ponzi scheme warning signs (guaranteed returns, withdrawal issues, recruitment incentives) | Infographic | High |

#### Chapter 4: Pump & Dump Schemes (needs 2-3 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | pump-dump-timeline | Timeline diagram showing the stages: accumulation, promotion, public FOMO, dump, crash | Diagram | High |
| 2 | fomo-psychology | Illustration showing emotional manipulation tactics used in pump & dump schemes | Illustration | Medium |
| 3 | signal-group-warning | Visual warning about private "signal" groups on Telegram/Discord | Illustration | Medium |

#### Chapter 5: Fake Giveaways & Lotteries (needs 3-4 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | fake-celebrity-giveaway | Example mockup of fake celebrity giveaway scam (generic, not showing real person) | Screenshot mockup | High |
| 2 | advance-fee-fraud | Diagram showing how advance fee fraud works - victim sends money, never receives prize | Diagram | High |
| 3 | legitimate-vs-scam | Side-by-side comparison of legitimate promotion vs scam giveaway characteristics | Comparison | Medium |
| 4 | social-media-verification | How to verify account legitimacy (checkmarks, follower patterns, account age) | Infographic | Medium |

#### Chapter 6: Shitcoins & Airdrops (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | airdrop-scam-flow | Diagram showing how malicious airdrops work to steal funds | Diagram | High |
| 2 | technical-red-flags | Visual checklist of technical warning signs for worthless tokens | Infographic | High |
| 3 | marketing-red-flags | Visual checklist of marketing warning signs (celebrity endorsements, guaranteed returns) | Infographic | High |
| 4 | wallet-interaction-danger | Warning diagram about connecting wallets to unknown websites | Diagram | High |
| 5 | legitimate-vs-scam-token | Comparison of legitimate project characteristics vs scam token | Comparison | Medium |

#### Chapter 7: Phishing & Identity Theft (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | phishing-attack-types | Overview diagram of different phishing vectors (email, social media, phone, mail) | Diagram | High |
| 2 | fake-website-detection | Side-by-side comparison of real vs fake website URL patterns | Screenshot mockup | High |
| 3 | email-phishing-example | Annotated example of phishing email with red flags highlighted | Screenshot mockup | High |
| 4 | private-key-warning | Strong visual warning about never sharing private keys/seed phrases | Warning graphic | High |
| 5 | verification-checklist | Steps to verify legitimacy before clicking links or taking action | Infographic | Medium |

#### Chapter 8: Bitcoin Hardforks Confusion (needs 3-4 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | hardfork-explanation | Simple diagram explaining what a hardfork is and how it creates two chains | Diagram | High |
| 2 | btc-vs-bch-bsv | Comparison table/graphic showing BTC vs BCH vs BSV and their key differences | Comparison | High |
| 3 | ticker-verification | How to verify you're buying real Bitcoin (BTC) vs forks | Infographic | High |
| 4 | hardfork-marketing-tactics | Warning about deceptive marketing used by Bitcoin forks | Illustration | Medium |

#### Chapter 9: Dishonest Influencers (needs 3-4 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | influencer-tactics | Diagram showing common manipulation tactics (fake results, luxury lifestyle, FOMO) | Diagram | High |
| 2 | paid-signal-group-warning | Visual warning about paid trading groups and their true economics | Illustration | High |
| 3 | influencer-red-flags | Checklist of warning signs for dishonest influencers | Infographic | High |
| 4 | good-habits-checklist | Visual checklist of good habits to avoid influencer manipulation | Infographic | Medium |

#### Chapter 10: Red Flags & Verification (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | master-red-flags | Comprehensive visual summary of all red flags covered in course | Infographic | High |
| 2 | dont-trust-verify | Visual representation of "Don't trust, verify" principle | Illustration | High |
| 3 | fomo-decision-tree | Decision tree for when you feel FOMO - pause, research, verify | Diagram | High |
| 4 | verification-steps | Step-by-step process for verifying legitimacy of any crypto opportunity | Infographic | High |
| 5 | transition-security | Bridge graphic connecting scam awareness to security practices | Illustration | Medium |

#### Chapter 11: Why Cybersecurity Matters (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | bitcoin-self-custody | Visual showing "you are your own bank" concept and responsibilities | Illustration | High |
| 2 | irreversible-transactions | Diagram showing why Bitcoin transactions cannot be reversed or recovered | Diagram | High |
| 3 | attack-vectors | Overview of different ways hackers can target Bitcoin users | Diagram | High |
| 4 | security-layers | Layered defense concept - multiple security measures protecting your Bitcoin | Diagram | Medium |
| 5 | cybersecurity-foundation | Visual metaphor for building security habits from the ground up | Illustration | Medium |

#### Chapter 12: Clean Computer Practices (needs 2-3 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | software-update-importance | Visual showing patching vulnerabilities before hackers exploit them | Diagram | High |
| 2 | download-sources | Diagram showing official sources vs dangerous download sites | Comparison | High |
| 3 | software-verification | Steps to verify software authenticity before installation | Infographic | Medium |

#### Chapter 13: Password Security (needs 3-4 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | weak-vs-strong-password | Visual comparison of weak passwords vs strong generated ones | Comparison | High |
| 2 | password-manager-flow | How password managers work - one master password, many unique passwords | Diagram | High |
| 3 | password-reuse-danger | Visual showing domino effect when one reused password is compromised | Diagram | High |
| 4 | password-manager-benefits | Infographic of password manager benefits (sync, autofill, generation) | Infographic | Medium |

#### Chapter 14: Two-Factor Authentication (needs 1-2 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | sms-vs-app-2fa | Comparison showing why app-based 2FA is more secure than SMS | Comparison | High |
| 2 | yubikey-overview | Introduction to hardware security keys for advanced users | Illustration | Medium |

#### Chapter 15: Privacy Protection (needs 2-3 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | privacy-security-connection | Diagram showing how privacy and security reinforce each other | Diagram | High |
| 2 | vpn-providers-criteria | Checklist for choosing a trustworthy VPN provider | Infographic | High |
| 3 | encrypted-communications | Overview of encrypted messaging, email, and file storage options | Diagram | Medium |

#### Chapter 16: Step-by-Step Security Progression (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | security-progression-ladder | Visual ladder/staircase showing security improvements from beginner to advanced | Diagram | High |
| 2 | week-by-week-plan | Timeline showing realistic security improvement schedule | Timeline | High |
| 3 | security-habit-building | Visual of building consistent security habits over time | Illustration | Medium |
| 4 | risk-value-correlation | Diagram showing how security needs increase as Bitcoin holdings grow | Diagram | High |
| 5 | digital-hygiene-checklist | Comprehensive checklist of digital hygiene practices | Infographic | Medium |

#### Chapter 17: Common Mistakes to Avoid (needs 2-3 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | tech-mistakes-overview | Visual summary of technological mistakes (seed phrase, exchanges, privacy) | Infographic | High |
| 2 | financial-mistakes-overview | Visual summary of financial mistakes (overinvesting, FOMO, taxes) | Infographic | High |
| 3 | mistake-prevention-checklist | Combined checklist for avoiding both types of mistakes | Infographic | Medium |

#### Chapter 18: Investment Strategy Basics (needs 3-4 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | budget-calculation | Visual showing income - expenses - savings = investment budget | Diagram | High |
| 2 | dca-concept | Diagram explaining Dollar Cost Averaging and smoothing volatility | Diagram | High |
| 3 | time-horizon-comparison | Visual comparing short-term trading vs long-term investing mindsets | Comparison | High |
| 4 | strategy-before-action | Visual emphasizing importance of having a written plan before investing | Illustration | Medium |

#### Chapter 19: Understanding Volatility (needs 3-4 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | volatility-visualization | Chart-style graphic showing typical Bitcoin price swings | Chart | High |
| 2 | emotional-decision-cycle | Diagram showing how emotions lead to buy high/sell low behavior | Diagram | High |
| 3 | zoom-out-perspective | Visual showing short-term volatility vs long-term trend | Chart | High |
| 4 | risk-tolerance-assessment | Visual guide for assessing personal risk tolerance | Infographic | Medium |

#### Chapter 20: Wallet Security Fundamentals (needs 2-3 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | seed-phrase-backup | Visual guide for properly backing up seed phrase (write, store, protect) | Infographic | High |
| 2 | exchange-vs-self-custody | Comparison of exchange custody risks vs self-custody responsibility | Comparison | High |
| 3 | seed-phrase-storage-donts | Warning graphic: never store seed phrase digitally or in cloud | Warning graphic | High |

#### Chapter 21: Confidentiality & Discretion (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | discretion-importance | Visual showing why keeping Bitcoin holdings private matters | Illustration | High |
| 2 | social-media-warning | Warning about sharing Bitcoin information on social media | Warning graphic | High |
| 3 | compartmentalization | Diagram showing how to compartmentalize Bitcoin-related activities | Diagram | High |
| 4 | physical-security-threats | Visual showing real-world threats from revealing holdings | Illustration | High |
| 5 | opsec-checklist | Operational security checklist for Bitcoin holders | Infographic | Medium |

#### Chapter 22: Tax Awareness (needs 2-3 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | tax-varies-by-country | Visual map/diagram showing tax treatment varies globally | Diagram | High |
| 2 | record-keeping-importance | Visual showing importance of keeping transaction records | Infographic | High |
| 3 | tax-professional-consultation | Visual emphasizing when to consult tax professionals | Illustration | Medium |

#### Chapter 23: Trading vs Investing vs Holding (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | trading-warning | Strong visual warning that most traders lose money | Warning graphic | High |
| 2 | three-approaches-comparison | Visual comparison of trading, investing, and HODLing approaches | Comparison | High |
| 3 | time-commitment-comparison | Visual showing time/effort required for each approach | Diagram | High |
| 4 | hodl-philosophy | Visual representation of the long-term HODL mindset | Illustration | Medium |
| 5 | beginner-recommendation | Visual clearly recommending investing/HODLing over trading for beginners | Infographic | High |

#### Chapter 24: Going Further (needs 0-1 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | golden-rules-summary | Visual summary of the three golden rules from the chapter | Infographic | Medium |

---

### A6. Quiz Inventory

**Summary:**
| Metric | Count |
|--------|-------|
| Current quizzes | 15 |
| Required per-chapter (17 content chapters x 5) | 85 |
| Required for final exam | 40 |
| **Total recommended** | **125** |
| **GAP** | **110 quizzes to create** |

**Note on Content Chapters:**
- Total chapters: 25
- Excluding: Ch1 (Welcome), Ch24 (Going Further), Ch25 (Conclusion)
- Content chapters needing quizzes: 22

**Revised Calculation:**
| Metric | Count |
|--------|-------|
| Current quizzes | 15 |
| Required per-chapter (22 content chapters x 5) | 110 |
| Required for final exam | 40 |
| **Total recommended** | **150** (or 110 with overlap for exam) |
| **GAP** | **95-135 quizzes to create** |

**Per-Chapter Breakdown:**

| Ch # | Chapter Title | chapterId | Current | Required | Gap |
|------|---------------|-----------|---------|----------|-----|
| 1 | Welcome to SCU102 | `intro-scu102-ch1` | 0 | 0 | 0 |
| 2 | Understanding Financial Fraud | `understanding-fraud-ch2` | 0 | 5 | 5 |
| 3 | Pyramid & Ponzi Schemes | `ponzi-schemes-ch3` | 0 | 5 | 5 |
| 4 | Pump & Dump Schemes | `pump-dump-ch4` | 0 | 5 | 5 |
| 5 | Fake Giveaways & Lotteries | `fake-giveaways-ch5` | 0 | 5 | 5 |
| 6 | Shitcoins & Airdrops | `shitcoins-ch6` | 0 | 5 | 5 |
| 7 | Phishing & Identity Theft | `phishing-ch7` | 0 | 5 | 5 |
| 8 | Bitcoin Hardforks Confusion | `hardforks-ch8` | 0 | 5 | 5 |
| 9 | Dishonest Influencers | `influencers-ch9` | 0 | 5 | 5 |
| 10 | Red Flags & Verification | `red-flags-ch10` | 0 | 5 | 5 |
| 11 | Why Cybersecurity Matters | `cybersecurity-ch11` | 0 | 5 | 5 |
| 12 | Clean Computer Practices | `clean-computer-ch12` | 0 | 5 | 5 |
| 13 | Password Security | `passwords-ch13` | 0 | 5 | 5 |
| 14 | Two-Factor Authentication | `2fa-ch14` | 0 | 5 | 5 |
| 15 | Privacy Protection | `privacy-ch15` | 0 | 5 | 5 |
| 16 | Step-by-Step Security Progression | `progression-ch16` | 0 | 5 | 5 |
| 17 | Common Mistakes to Avoid | `mistakes-ch17` | 0 | 5 | 5 |
| 18 | Investment Strategy Basics | `investment-ch18` | 0 | 5 | 5 |
| 19 | Understanding Volatility | `volatility-ch19` | 0 | 5 | 5 |
| 20 | Wallet Security Fundamentals | `wallet-security-ch20` | 0 | 5 | 5 |
| 21 | Confidentiality & Discretion | `discretion-ch21` | 0 | 5 | 5 |
| 22 | Tax Awareness | `taxes-ch22` | 0 | 5 | 5 |
| 23 | Trading vs Investing vs Holding | `trading-investing-ch23` | 0 | 5 | 5 |
| 24 | Going Further | `going-further-ch24` | 0 | 0 | 0 |
| 25 | Conclusion | `conclusion-ch25` | 0 | 0 | 0 |

**Current Quiz Mapping (LEGACY - NEEDS UPDATE):**

All 15 existing quizzes reference legacy chapterIds that do NOT match the new course structure:

| Quiz # | Legacy chapterId | Quizzes Count | Status |
|--------|------------------|---------------|--------|
| 000-004 | `8af2948b-2ab5-54c4-862c-3414b8a285a2` | 5 | NEEDS REMAPPING |
| 005-009 | `f0873bf2-6a6f-5485-bb7a-d84be14f404d` | 5 | NEEDS REMAPPING |
| 010-014 | `33134b3f-92c1-5185-afb6-88599e47e801` | 5 | NEEDS REMAPPING |

**CRITICAL:** Before creating new quizzes, the existing 15 quizzes must be reviewed and assigned to appropriate chapters in the new course structure.

---

### A7. Missing Quizzes - Topic Suggestions

#### Chapter 2: Understanding Financial Fraud (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | Difference between Bitcoin ecosystem and crypto industry | multiple-choice | easy |
| 2 | Key characteristics that make Bitcoin different from altcoins | multiple-choice | medium |
| 3 | Why the crypto space is fertile ground for fraud | true-false | easy |
| 4 | Understanding why scam experiences affect the whole community | multiple-choice | easy |
| 5 | Identifying centralized vs decentralized projects | multiple-choice | medium |

#### Chapter 3: Pyramid & Ponzi Schemes (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | How Ponzi schemes generate "returns" | multiple-choice | easy |
| 2 | Red flags of pyramid schemes (guaranteed returns, recruitment) | multiple-choice | easy |
| 3 | Why Ponzi schemes inevitably collapse | multiple-choice | medium |
| 4 | How DeFi can mask Ponzi mechanics | multiple-choice | hard |
| 5 | The key question to ask about any investment opportunity | multiple-choice | easy |

#### Chapter 4: Pump & Dump Schemes (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | Stages of a pump & dump scheme | multiple-choice | medium |
| 2 | Why FOMO is dangerous in crypto | true-false | easy |
| 3 | Warning signs of "signal" groups | multiple-choice | easy |
| 4 | Why pump & dump is illegal market manipulation | true-false | easy |
| 5 | Long-term strategy vs quick money schemes | multiple-choice | medium |

#### Chapter 5: Fake Giveaways & Lotteries (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | Identifying fake celebrity giveaway scams | multiple-choice | easy |
| 2 | Red flag: being asked to send crypto first | true-false | easy |
| 3 | How advance fee fraud works | multiple-choice | medium |
| 4 | Verifying social media account legitimacy | multiple-choice | medium |
| 5 | Why legitimate entities never ask you to send crypto first | true-false | easy |

#### Chapter 6: Shitcoins & Airdrops (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | Technical red flags for worthless tokens | multiple-choice | medium |
| 2 | Marketing red flags ("next Bitcoin", guaranteed returns) | multiple-choice | easy |
| 3 | Dangers of connecting wallet to unknown websites | multiple-choice | medium |
| 4 | Why unsolicited tokens in your wallet are suspicious | true-false | easy |
| 5 | What to never share (private keys, seed phrase) | multiple-choice | easy |

#### Chapter 7: Phishing & Identity Theft (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | Common phishing attack vectors (email, social, phone) | multiple-choice | easy |
| 2 | How to verify sender identity before acting | multiple-choice | medium |
| 3 | Why you should navigate to websites directly, not via links | true-false | easy |
| 4 | What information should never be shared online | multiple-choice | easy |
| 5 | Identifying fake vs legitimate website URLs | multiple-choice | medium |

#### Chapter 8: Bitcoin Hardforks Confusion (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | What is a hard fork in Bitcoin | multiple-choice | medium |
| 2 | The correct ticker for original Bitcoin | multiple-choice | easy |
| 3 | Difference between BTC, BCH, and BSV | multiple-choice | medium |
| 4 | Why some forks use deceptive marketing | multiple-choice | easy |
| 5 | Trade-offs of increased block size (BCH/BSV) | multiple-choice | hard |

#### Chapter 9: Dishonest Influencers (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | Tactics used by crypto influencers to attract followers | multiple-choice | easy |
| 2 | Why "free" advice from influencers isn't really free | multiple-choice | medium |
| 3 | Problems with paid trading signal groups | multiple-choice | medium |
| 4 | Why you can't replicate influencer results | multiple-choice | medium |
| 5 | The golden rule about information on the internet | multiple-choice | easy |

#### Chapter 10: Red Flags & Verification (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | The "Don't trust, verify" principle | multiple-choice | easy |
| 2 | What to do when feeling FOMO | multiple-choice | easy |
| 3 | Comprehensive red flags checklist | multiple-choice | medium |
| 4 | Why most giveaways are scams | true-false | easy |
| 5 | Long-term learning vs short-term gambling | multiple-choice | easy |

#### Chapter 11: Why Cybersecurity Matters (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | What "you are your own bank" means for security | multiple-choice | easy |
| 2 | Why Bitcoin transactions cannot be reversed | multiple-choice | medium |
| 3 | Consequences of security lapses in Bitcoin | multiple-choice | easy |
| 4 | Why Bitcoin is a high-value target for hackers | true-false | easy |
| 5 | The relationship between value held and security needed | multiple-choice | medium |

#### Chapter 12: Clean Computer Practices (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | Why keeping software updated is important | multiple-choice | easy |
| 2 | Safe sources for downloading software | multiple-choice | easy |
| 3 | How to verify software authenticity | multiple-choice | medium |
| 4 | The 3-2-1 backup strategy | multiple-choice | medium |
| 5 | Benefits of using antivirus software | true-false | easy |

#### Chapter 13: Password Security (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | Why password reuse is dangerous | multiple-choice | easy |
| 2 | Benefits of using a password manager | multiple-choice | easy |
| 3 | Characteristics of a strong password | multiple-choice | medium |
| 4 | Difference between Bitwarden and KeePass | multiple-choice | medium |
| 5 | What the master password protects | multiple-choice | easy |

#### Chapter 14: Two-Factor Authentication (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | What 2FA adds to password protection | multiple-choice | easy |
| 2 | Why app-based 2FA is better than SMS | multiple-choice | medium |
| 3 | What to do with 2FA recovery codes | multiple-choice | easy |
| 4 | What SIM swap attacks target | multiple-choice | medium |
| 5 | When to use hardware security keys (YubiKey) | multiple-choice | hard |

#### Chapter 15: Privacy Protection (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | Relationship between privacy and security | multiple-choice | easy |
| 2 | What a VPN does and doesn't protect | multiple-choice | medium |
| 3 | Criteria for choosing a trustworthy VPN | multiple-choice | medium |
| 4 | Benefits of encrypted messaging (Signal, SimpleX) | multiple-choice | easy |
| 5 | Why to use privacy-focused browsers | multiple-choice | easy |

#### Chapter 16: Step-by-Step Security Progression (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | Why gradual security improvement works best | multiple-choice | easy |
| 2 | Good first step for beginners (password manager) | multiple-choice | easy |
| 3 | When to add more advanced security practices | multiple-choice | medium |
| 4 | Relationship between holdings value and security needs | multiple-choice | medium |
| 5 | The importance of consistency in digital hygiene | true-false | easy |

#### Chapter 17: Common Mistakes to Avoid (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | Consequences of losing your seed phrase | multiple-choice | easy |
| 2 | Risks of keeping bitcoin on exchanges | multiple-choice | easy |
| 3 | Why revealing your holdings is dangerous | multiple-choice | medium |
| 4 | Financial mistake: investing more than you can lose | true-false | easy |
| 5 | Difference between trading and investing | multiple-choice | medium |

#### Chapter 18: Investment Strategy Basics (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | How to calculate your investment budget | multiple-choice | easy |
| 2 | What Dollar Cost Averaging (DCA) means | multiple-choice | easy |
| 3 | Benefits of DCA for beginners | multiple-choice | medium |
| 4 | Importance of having a time horizon | multiple-choice | medium |
| 5 | Why written strategy beats emotional decisions | true-false | easy |

#### Chapter 19: Understanding Volatility (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | Typical Bitcoin price volatility ranges | multiple-choice | medium |
| 2 | Why volatility isn't a bug but a feature | multiple-choice | medium |
| 3 | How to know if you've invested too much | multiple-choice | easy |
| 4 | Emotional responses to avoid during volatility | multiple-choice | easy |
| 5 | Why never to borrow money to buy bitcoin | true-false | easy |

#### Chapter 20: Wallet Security Fundamentals (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | What "not your keys, not your coins" means | multiple-choice | easy |
| 2 | How to properly store a recovery phrase | multiple-choice | easy |
| 3 | Risks of storing seed phrase digitally | multiple-choice | medium |
| 4 | Why multiple backup locations are important | multiple-choice | medium |
| 5 | Difference between exchange custody and self-custody | multiple-choice | easy |

#### Chapter 21: Confidentiality & Discretion (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | Why discretion about holdings is crucial | multiple-choice | easy |
| 2 | Real-world risks of revealing Bitcoin ownership | multiple-choice | medium |
| 3 | How to compartmentalize Bitcoin-related activity | multiple-choice | medium |
| 4 | What information should never be shared publicly | multiple-choice | easy |
| 5 | Benefits of separate email for Bitcoin activities | multiple-choice | easy |

#### Chapter 22: Tax Awareness (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | Whether Bitcoin is exempt from taxes | true-false | easy |
| 2 | Why tax treatment varies by jurisdiction | multiple-choice | easy |
| 3 | Common ways Bitcoin gains are taxed | multiple-choice | medium |
| 4 | Importance of consulting tax professionals | multiple-choice | easy |
| 5 | Why to understand taxes before major transactions | multiple-choice | medium |

#### Chapter 23: Trading vs Investing vs Holding (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | Key differences between trading and investing | multiple-choice | easy |
| 2 | Why most beginner traders lose money | multiple-choice | medium |
| 3 | What HODL means in Bitcoin culture | multiple-choice | easy |
| 4 | Which approach is best for beginners | multiple-choice | easy |
| 5 | Warren Buffett's advice applied to Bitcoin | multiple-choice | medium |

#### Final Exam Pool (needs 40 additional quizzes)

Cross-cutting topics for the final exam pool:

| # | Topic | Related Chapters | Difficulty |
|---|-------|-----------------|------------|
| 1 | Comprehensive scam identification | Ch 2-9 | medium |
| 2 | Security best practices overview | Ch 11-16 | medium |
| 3 | Investment strategy principles | Ch 17-23 | medium |
| 4 | Privacy and discretion combined | Ch 15, 21 | medium |
| 5 | "Don't trust, verify" applications | Ch 10, multiple | easy |
| 6 | Self-custody principles | Ch 20, 11 | medium |
| 7 | FOMO and emotional decisions | Ch 4, 9, 19 | easy |
| 8 | Password and 2FA combined | Ch 13, 14 | medium |
| 9 | Ponzi scheme vs legitimate investment | Ch 3, 18 | hard |
| 10 | Influencer manipulation tactics | Ch 9, 4 | medium |
| 11 | Bitcoin vs altcoin key differences | Ch 2, 8 | medium |
| 12 | Phishing prevention across channels | Ch 7 | medium |
| 13 | Seed phrase security comprehensive | Ch 20, 17 | hard |
| 14 | VPN and privacy tools | Ch 15 | medium |
| 15 | Clean computer practices summary | Ch 12 | easy |
| 16 | Tax awareness fundamentals | Ch 22 | medium |
| 17 | Trading risks for beginners | Ch 23 | hard |
| 18 | Airdrop and shitcoin dangers | Ch 6 | medium |
| 19 | Giveaway scam identification | Ch 5 | easy |
| 20 | Hardfork confusion prevention | Ch 8 | medium |
| 21-40 | Additional cross-cutting topics covering all chapters | Various | Mixed |

---

### A8. Structural Fixes Required

| # | Issue | Location | Fix Required | Priority |
|---|-------|----------|--------------|----------|
| 1 | **Quiz chapterId mismatch** | All quiz question.yml files | Update all 15 existing quizzes to reference correct chapterIds from new course structure | Critical |
| 2 | Content gap after Conclusion heading | Ch 25 (line 721-724) | Add conclusion content summarizing key takeaways and next steps | High |
| 3 | Course name mismatch | en.md frontmatter | Consider updating "Prerequisite to Bitcoin" to match course code "SCU102: Financial Fraud, Scams & Online Security" for clarity | Medium |

**Detailed Fix Instructions:**

**Fix #1: Quiz chapterId Remapping**
The 15 existing quizzes need to be reviewed for content and assigned to appropriate chapters:

Suggested remapping (requires content review):
- Quizzes 000-004 (wallet/security related): Assign to Ch 20 (`wallet-security-ch20`)
- Quizzes 005-009 (wallet/security related): Assign to Ch 20 or distribute across Ch 11-16
- Quizzes 010-014 (wallet/security related): Assign to appropriate security chapters

Each quiz question.yml file needs `chapterId` field updated from legacy UUID to new descriptive chapterId.

**Fix #2: Conclusion Content**
The Conclusion chapter (line 721-724) has the heading and tag but no content. Add:
- Summary of key takeaways from the course
- Encouragement for continued learning
- Links to recommended next courses (BTC101, SCU101)
- Final reminders about security and scam awareness

---

### A9. Work Summary for Phase B

**Before starting Phase B, complete these tasks:**

#### Critical (Must Do)
- [ ] **Fix #1:** Update all 15 quiz question.yml files with correct chapterIds
- [ ] **Fix #2:** Add content to Conclusion chapter (Ch 25)
- [ ] Review and optionally update course name in frontmatter

#### Images to Create (63-70 total)
- [ ] Ch 2: 2-3 images (see specs in A5)
- [ ] Ch 3: 3-4 images (see specs in A5)
- [ ] Ch 4: 2-3 images (see specs in A5)
- [ ] Ch 5: 3-4 images (see specs in A5)
- [ ] Ch 6: 4-5 images (see specs in A5)
- [ ] Ch 7: 4-5 images (see specs in A5)
- [ ] Ch 8: 3-4 images (see specs in A5)
- [ ] Ch 9: 3-4 images (see specs in A5)
- [ ] Ch 10: 4-5 images (see specs in A5)
- [ ] Ch 11: 4-5 images (see specs in A5)
- [ ] Ch 12: 2-3 images (see specs in A5)
- [ ] Ch 13: 3-4 images (see specs in A5)
- [ ] Ch 14: 1-2 images (see specs in A5)
- [ ] Ch 15: 2-3 images (see specs in A5)
- [ ] Ch 16: 4-5 images (see specs in A5)
- [ ] Ch 17: 2-3 images (see specs in A5)
- [ ] Ch 18: 3-4 images (see specs in A5)
- [ ] Ch 19: 3-4 images (see specs in A5)
- [ ] Ch 20: 2-3 images (see specs in A5)
- [ ] Ch 21: 4-5 images (see specs in A5)
- [ ] Ch 22: 2-3 images (see specs in A5)
- [ ] Ch 23: 4-5 images (see specs in A5)
- [ ] Ch 24: 0-1 images (see specs in A5)

#### Quizzes to Create (95-135 total)
- [ ] Remap existing 15 quizzes to appropriate chapters
- [ ] Ch 2: 5 quizzes (see topics in A7)
- [ ] Ch 3: 5 quizzes (see topics in A7)
- [ ] Ch 4: 5 quizzes (see topics in A7)
- [ ] Ch 5: 5 quizzes (see topics in A7)
- [ ] Ch 6: 5 quizzes (see topics in A7)
- [ ] Ch 7: 5 quizzes (see topics in A7)
- [ ] Ch 8: 5 quizzes (see topics in A7)
- [ ] Ch 9: 5 quizzes (see topics in A7)
- [ ] Ch 10: 5 quizzes (see topics in A7)
- [ ] Ch 11: 5 quizzes (see topics in A7)
- [ ] Ch 12: 5 quizzes (see topics in A7)
- [ ] Ch 13: 5 quizzes (see topics in A7)
- [ ] Ch 14: 5 quizzes (see topics in A7)
- [ ] Ch 15: 5 quizzes (see topics in A7)
- [ ] Ch 16: 5 quizzes (see topics in A7)
- [ ] Ch 17: 5 quizzes (see topics in A7)
- [ ] Ch 18: 5 quizzes (see topics in A7)
- [ ] Ch 19: 5 quizzes (see topics in A7)
- [ ] Ch 20: 5 quizzes (see topics in A7)
- [ ] Ch 21: 5 quizzes (see topics in A7)
- [ ] Ch 22: 5 quizzes (see topics in A7)
- [ ] Ch 23: 5 quizzes (see topics in A7)
- [ ] Final exam pool: 40 quizzes (see topics in A7)

---

**Phase A Status:** :white_check_mark: COMPLETE
**Phase A Completed:** 2026-01-21
**Notes:**
- This is a comprehensive course with 25 chapters covering financial fraud, crypto scams, online security, and beginner tips.
- The most critical issue is the quiz chapterId mismatch - all 15 existing quizzes reference legacy UUIDs that don't exist in the new course structure.
- The course has good image coverage (25 images) but needs approximately 63-70 more to meet the 4-5 per substantive chapter target.
- The course needs significant quiz work: 95-135 new quizzes to meet the 5-per-chapter plus 40-exam-pool standard.
- Conclusion chapter needs content added.
