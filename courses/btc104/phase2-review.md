# BTC104 Phase 2 Review

> This document tracks all work needed to complete BTC104 (How to Secure Bitcoin) for production.
> Location: `courses/btc104/phase2-review.md`

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
| id | `8b4e6c2a-1d9f-5e3b-7a0c-4f2d8e6a9b1c` | ✅ |
| topic | `bitcoin` | ✅ |
| subtopic | `security` | ✅ |
| type | `theory` | ✅ |
| level | `beginner` | ✅ |
| hours | `2` | ✅ |
| professors_id | `[2e1b5182-567e-453a-af29-36009340ff02]` | ✅ |

**Issues:** None. All required fields present and valid.

### A2. Frontmatter Validation (en.md)

- [x] `name` present and descriptive: "How to Secure Your Bitcoin"
- [x] `goal` is single sentence, action-oriented: "Learn to set up your first Bitcoin wallet and secure your seed phrase properly"
- [x] `objectives` has 3-6 items (has 6):
  1. Understand what a Bitcoin wallet is and how it works
  2. Choose the right wallet for your situation as a beginner
  3. Set up your first wallet step by step
  4. Secure your seed phrase properly
  5. Receive bitcoin to your own wallet
  6. Follow security best practices

**Issues:** None. Frontmatter is complete and well-structured.

### A3. Structure Validation

- [x] First Part is Introduction
- [x] No text between Part headings and first Chapter
- [x] All Parts have `<partId>`:
  - Part 1: `introduction-part1`
  - Part 2: `understanding-wallets-part2`
  - Part 3: `setup-wallet-part3`
  - Part 4: `best-practices-part4`
  - Part 5: `conclusion-part5`
- [x] All Chapters have `<chapterId>`:
  - Ch 1: `welcome-ch01`
  - Ch 2: `why-wallet-ch02`
  - Ch 3: `what-is-wallet-ch03`
  - Ch 4: `wallet-types-ch04`
  - Ch 5: `custodial-vs-selfcustody-ch05`
  - Ch 6: `choosing-first-wallet-ch06`
  - Ch 7: `creating-wallet-ch07`
  - Ch 8: `securing-seed-ch08`
  - Ch 9: `receiving-bitcoin-ch09`
  - Ch 10: `best-practices-ch10`
  - Ch 11: `upgrading-security-ch11`
  - Ch 12: `common-mistakes-ch12`
  - Ch 13: `security-journey-ch13`
  - Ch 14: `conclusion-ch14`
- [ ] Going Further is last chapter of last content Part - **MISSING**
- [x] Conclusion Part exists with only Conclusion chapter (Part 5 has 2 chapters: "Your Security Journey" and "Conclusion")
- [x] `<isCourseConclusion>true</isCourseConclusion>` tag present (on conclusion-ch14)

**Issues:**
1. **CRITICAL: Missing "Going Further" chapter** - The last content Part (Part 4: Best Practices) should have a "Going Further" chapter as its last chapter before the Conclusion Part. Currently ends with "Common Mistakes and How to Avoid Them" (ch12).
2. **Conclusion Part structure** - Part 5 (Conclusion) has two chapters: "Your Security Journey" (ch13) and "Conclusion" (ch14). Per standards, Conclusion Part should contain ONLY the Conclusion chapter. Consider merging ch13 content into ch14, or moving ch13 to be the last chapter of Part 4.

---

### A4. Image Inventory

**Summary:**
| Metric | Count |
|--------|-------|
| Current images | 3 |
| Target images | 37-47 |
| **GAP** | **34-44 images to create** |

**Images Found:**
- `assets/en/001.webp` - Referenced in Ch 2 (Why You Need Your Own Wallet)
- `assets/en/002.webp` - Referenced in Ch 4 (Types of Wallets)
- `assets/en/003.webp` - Referenced in Ch 11 (When to Upgrade Your Security)

**Per-Chapter Breakdown:**

| Ch # | Chapter Title | Type | Current | Target | Gap |
|------|---------------|------|---------|--------|-----|
| 1 | Welcome to BTC104 | Introduction | 0 | 0-1 | 0-1 |
| 2 | Why You Need Your Own Wallet | Content | 1 | 4-5 | 3-4 |
| 3 | What Is a Bitcoin Wallet? | Content | 0 | 4-5 | 4-5 |
| 4 | Types of Wallets | Content | 1 | 4-5 | 3-4 |
| 5 | Custodial vs Self-Custody | Content | 0 | 4-5 | 4-5 |
| 6 | Choosing Your First Wallet | Content | 0 | 4-5 | 4-5 |
| 7 | Creating Your Wallet | Content | 0 | 4-5 | 4-5 |
| 8 | Securing Your Seed Phrase | Content | 0 | 4-5 | 4-5 |
| 9 | Receiving Your First Bitcoin | Content | 0 | 4-5 | 4-5 |
| 10 | Security Best Practices | Content | 0 | 4-5 | 4-5 |
| 11 | When to Upgrade Your Security | Content | 1 | 4-5 | 3-4 |
| 12 | Common Mistakes and How to Avoid Them | Content | 0 | 4-5 | 4-5 |
| 13 | Your Security Journey | Conclusion-adjacent | 0 | 0-1 | 0-1 |
| 14 | Conclusion | Conclusion | 0 | 0 | 0 |

**Total Gap Estimate:** ~38-40 images needed

---

### A5. Missing Images - Detailed Specifications

#### Chapter 1: Welcome to BTC104 (needs 0-1 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | btc104-welcome | Course overview graphic showing a wallet icon with a protective shield, symbolizing security | illustration | low |

#### Chapter 2: Why You Need Your Own Wallet (needs 3-4 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | exchange-risks-timeline | Timeline showing major exchange failures: Mt. Gox (2014), FTX (2022), with icons for hacks, bankruptcies, account freezes | diagram | high |
| 2 | keys-concept | Visual showing "Not your keys, not your coins" - split screen with exchange holding keys vs user holding keys | illustration | high |
| 3 | self-custody-benefits | Icons showing benefits: no freezing, no third-party risk, full control | diagram | medium |

#### Chapter 3: What Is a Bitcoin Wallet? (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | wallet-not-storage | Illustration dispelling myth - wallet as key holder, not storage container; bitcoin lives on the network | illustration | high |
| 2 | public-private-keys | Diagram showing public key (shareable address) vs private key (secret), with mailbox analogy | diagram | high |
| 3 | seed-phrase-generation | Visual showing seed phrase (12/24 words) generating all private/public keys | diagram | high |
| 4 | mailbox-analogy | Illustrated mailbox analogy: public address = mailbox number, private key = key to open, seed phrase = master key | illustration | medium |

#### Chapter 4: Types of Wallets (needs 3-4 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | hot-wallet-examples | Screenshots/icons of recommended hot wallets: Green Wallet, Blue Wallet, Phoenix | screenshot/icons | high |
| 2 | hardware-wallet-examples | Photos/illustrations of hardware wallets: Ledger, Trezor, Coldcard, Jade, BitBox | photo/illustration | high |
| 3 | hot-vs-cold-comparison | Side-by-side comparison chart: hot (pros/cons) vs hardware (pros/cons) | diagram | high |

#### Chapter 5: Custodial vs Self-Custody (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | custodial-diagram | Diagram showing custodial: user -> exchange holds keys -> bitcoin | diagram | high |
| 2 | self-custody-diagram | Diagram showing self-custody: user holds keys -> direct bitcoin control | diagram | high |
| 3 | custodial-risks | Icons showing risks: hacks, bankruptcy, frozen accounts, government shutdown | illustration | medium |
| 4 | seed-phrase-test | Decision tree: "Did they show you a seed phrase?" Yes = self-custody, No = custodial | diagram | medium |

#### Chapter 6: Choosing Your First Wallet (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | green-wallet-logo | Green Wallet (Blockstream) logo and app screenshot | screenshot | high |
| 2 | blue-wallet-logo | Blue Wallet logo and app screenshot | screenshot | high |
| 3 | sparrow-wallet-logo | Sparrow Wallet logo and desktop screenshot | screenshot | high |
| 4 | fake-app-warning | Warning illustration: fake apps in app stores with red flags to look for | illustration | high |
| 5 | download-safely | Step-by-step: official website -> app store link -> verify developer | diagram | medium |

#### Chapter 7: Creating Your Wallet (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | wallet-creation-step1 | Screenshot: "Create New Wallet" button in app interface | screenshot | high |
| 2 | seed-phrase-display | Example seed phrase display (with warning: never share) - use fake words | illustration | high |
| 3 | writing-seed-phrase | Illustration: proper way to write seed phrase - pen, paper, numbered words | illustration | high |
| 4 | seed-verification | Screenshot: seed phrase verification step in wallet app | screenshot | medium |
| 5 | pin-setup | Screenshot: PIN/password setup screen | screenshot | medium |

#### Chapter 8: Securing Your Seed Phrase (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | seed-loss-consequences | Diagram: phone breaks + no seed = bitcoin lost forever | illustration | high |
| 2 | seed-theft-consequences | Diagram: someone sees seed = can steal from anywhere | illustration | high |
| 3 | dont-store-digitally | Icons with X marks: no computer, no phone, no cloud, no email, no photos | illustration | high |
| 4 | safe-storage-options | Icons: fireproof safe, locked drawer, hidden spot; backup in different location | illustration | high |
| 5 | metal-backup | Photo/illustration of metal seed backup plates | photo/illustration | medium |

#### Chapter 9: Receiving Your First Bitcoin (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | receive-address-qr | Example wallet screen showing QR code and address | screenshot | high |
| 2 | address-changes | Illustration showing multiple addresses all belonging to same wallet (privacy feature) | diagram | medium |
| 3 | exchange-withdrawal | Step-by-step: exchange withdrawal process to own wallet | screenshot/diagram | high |
| 4 | transaction-confirmation | Wallet screen showing pending then confirmed transaction | screenshot | high |
| 5 | double-check-address | Highlighting first/last characters of address to verify | diagram | medium |

#### Chapter 10: Security Best Practices (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | never-share-seed | Warning icon with examples of who NOT to share seed with (fake support, "experts") | illustration | high |
| 2 | verify-addresses | Close-up showing how to verify first/last 6 characters | diagram | high |
| 3 | scam-examples | Visual showing common scams: verify wallet emails, fake support, "send to double" | illustration | high |
| 4 | discretion-privacy | Illustration: don't talk about how much bitcoin you have | illustration | medium |
| 5 | wrench-attack | The "$5 wrench attack" concept - why discretion matters | illustration | medium |

#### Chapter 11: When to Upgrade Your Security (needs 3-4 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | upgrade-threshold | Decision diagram: when to get hardware wallet (amount > device cost, >$hundreds, long-term) | diagram | high |
| 2 | hardware-wallet-brands | Comparison of popular hardware wallets: Ledger, Trezor, Coldcard, Jade, BitBox | photo/illustration | high |
| 3 | hybrid-approach | Diagram: hot wallet for spending + hardware wallet for savings | diagram | high |

#### Chapter 12: Common Mistakes and How to Avoid Them (needs 4-5 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | mistake-exchange | Illustration: bitcoin sitting on exchange vs own wallet | illustration | high |
| 2 | mistake-lost-seed | Illustration: faded/damaged paper backup = lost bitcoin | illustration | high |
| 3 | mistake-fake-support | Screenshot-style: fake support message asking for seed | illustration | high |
| 4 | mistake-wrong-address | Clipboard malware swapping addresses | diagram | medium |
| 5 | checklist-visual | Visual checklist summary of all security steps | diagram | medium |

#### Chapter 13: Your Security Journey (needs 0-1 images)

| # | Image Name | Description | Style | Priority |
|---|------------|-------------|-------|----------|
| 1 | security-journey-path | Path illustration: beginner (hot wallet) -> intermediate (hardware) -> advanced (multisig) | illustration | low |

---

### A6. Quiz Inventory

**Summary:**
| Metric | Count |
|--------|-------|
| Current quizzes | 3 |
| Content chapters (excluding intro/conclusion) | 11 |
| Required per-chapter (11 × 5) | 55 |
| Required for final exam | 40 |
| **Total recommended** | **95** (or minimum 55 with overlap) |
| **GAP** | **52-92 quizzes to create** |

**Per-Chapter Breakdown:**

| Ch # | Chapter Title | chapterId | Current | Required | Gap |
|------|---------------|-----------|---------|----------|-----|
| 1 | Welcome to BTC104 | welcome-ch01 | 0 | 0 | 0 |
| 2 | Why You Need Your Own Wallet | why-wallet-ch02 | 0 | 5 | 5 |
| 3 | What Is a Bitcoin Wallet? | what-is-wallet-ch03 | 0 | 5 | 5 |
| 4 | Types of Wallets | wallet-types-ch04 | 1 | 5 | 4 |
| 5 | Custodial vs Self-Custody | custodial-vs-selfcustody-ch05 | 0 | 5 | 5 |
| 6 | Choosing Your First Wallet | choosing-first-wallet-ch06 | 0 | 5 | 5 |
| 7 | Creating Your Wallet | creating-wallet-ch07 | 0 | 5 | 5 |
| 8 | Securing Your Seed Phrase | securing-seed-ch08 | 0 | 5 | 5 |
| 9 | Receiving Your First Bitcoin | receiving-bitcoin-ch09 | 0 | 5 | 5 |
| 10 | Security Best Practices | best-practices-ch10 | 0 | 5 | 5 |
| 11 | When to Upgrade Your Security | upgrading-security-ch11 | 2 | 5 | 3 |
| 12 | Common Mistakes and How to Avoid Them | common-mistakes-ch12 | 0 | 5 | 5 |
| 13 | Your Security Journey | security-journey-ch13 | 0 | 0 | 0 |
| 14 | Conclusion | conclusion-ch14 | 0 | 0 | 0 |

**Per-chapter quiz gap: 52 quizzes needed**

**Current Quiz Mapping:**

| Quiz # | chapterId | Linked Chapter | Topic |
|--------|-----------|----------------|-------|
| 000 | wallet-types-ch04 | Ch 4: Types of Wallets | (wallet types - hard difficulty) |
| 001 | upgrading-security-ch11 | Ch 11: When to Upgrade Your Security | (upgrading security - intermediate) |
| 002 | upgrading-security-ch11 | Ch 11: When to Upgrade Your Security | (upgrading security - intermediate) |

---

### A7. Missing Quizzes - Topic Suggestions

#### Chapter 2: Why You Need Your Own Wallet (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | What does "Not your keys, not your coins" mean? | multiple-choice | easy |
| 2 | What happened to Mt. Gox customers in 2014? | multiple-choice | medium |
| 3 | What risks do you face when leaving bitcoin on an exchange? | multiple-choice | easy |
| 4 | True/False: If an exchange freezes your account, you can still access your bitcoin | true-false | easy |
| 5 | Why is self-custody compared to holding physical cash? | multiple-choice | medium |

#### Chapter 3: What Is a Bitcoin Wallet? (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | What does a Bitcoin wallet actually store? | multiple-choice | easy |
| 2 | What is the purpose of a public key/address? | multiple-choice | easy |
| 3 | What can someone do with your private key? | multiple-choice | medium |
| 4 | What is a seed phrase and what does it generate? | multiple-choice | medium |
| 5 | True/False: Your bitcoin is stored inside your wallet app | true-false | easy |

#### Chapter 4: Types of Wallets (needs 4 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | What is the main advantage of a hot wallet? | multiple-choice | easy |
| 2 | Why are hardware wallets more secure than hot wallets? | multiple-choice | medium |
| 3 | Which wallet type is best for large long-term holdings? | multiple-choice | easy |
| 4 | What is a disadvantage of hardware wallets? | multiple-choice | medium |

#### Chapter 5: Custodial vs Self-Custody (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | How can you tell if a wallet is custodial or self-custody? | multiple-choice | medium |
| 2 | What does "custodial" mean in Bitcoin context? | multiple-choice | easy |
| 3 | True/False: Bitcoin ETFs give you self-custody of bitcoin | true-false | easy |
| 4 | What is the main risk of custodial services? | multiple-choice | medium |
| 5 | Which of these is an example of self-custody? | multiple-choice | easy |

#### Chapter 6: Choosing Your First Wallet (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | Which wallet is recommended for most beginners? | multiple-choice | easy |
| 2 | How should you download a wallet app safely? | multiple-choice | medium |
| 3 | Why is searching the app store directly risky? | multiple-choice | medium |
| 4 | What should you check before downloading a wallet? | multiple-choice | easy |
| 5 | True/False: Blue Wallet supports the Lightning Network | true-false | easy |

#### Chapter 7: Creating Your Wallet (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | What should you do before the seed phrase appears? | multiple-choice | medium |
| 2 | What is the correct way to record your seed phrase? | multiple-choice | easy |
| 3 | Why should you verify your seed phrase backup? | multiple-choice | medium |
| 4 | What happens after you verify your seed phrase? | multiple-choice | easy |
| 5 | True/False: You can do the seed phrase backup step again later | true-false | medium |

#### Chapter 8: Securing Your Seed Phrase (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | What happens if you lose your seed phrase AND your phone breaks? | multiple-choice | easy |
| 2 | Why should you never store your seed phrase digitally? | multiple-choice | medium |
| 3 | Which of these is a safe way to store your seed phrase? | multiple-choice | easy |
| 4 | Why should you have a backup in a different location? | multiple-choice | medium |
| 5 | What is a metal seed backup used for? | multiple-choice | medium |

#### Chapter 9: Receiving Your First Bitcoin (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | What is a receiving address used for? | multiple-choice | easy |
| 2 | Why does your wallet generate a new address each time? | multiple-choice | medium |
| 3 | How should you share your address for in-person transfers? | multiple-choice | easy |
| 4 | What should you always do before sending bitcoin to an address? | multiple-choice | medium |
| 5 | True/False: One confirmation is usually enough for small amounts | true-false | easy |

#### Chapter 10: Security Best Practices (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | Who should you share your seed phrase with? | multiple-choice | easy |
| 2 | What is the "$5 wrench attack"? | multiple-choice | medium |
| 3 | What should you verify before sending bitcoin? | multiple-choice | easy |
| 4 | True/False: Real wallet support will never ask for your seed phrase | true-false | easy |
| 5 | What is a sign of a "too good to be true" bitcoin scam? | multiple-choice | medium |

#### Chapter 11: When to Upgrade Your Security (needs 3 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | When should you consider getting a hardware wallet? | multiple-choice | medium |
| 2 | What is the "hybrid approach" to wallet management? | multiple-choice | medium |
| 3 | What is multisignature (multisig) used for? | multiple-choice | hard |

#### Chapter 12: Common Mistakes and How to Avoid Them (needs 5 quizzes)

| # | Suggested Topic | Question Type | Difficulty |
|---|-----------------|---------------|------------|
| 1 | What is the problem with leaving bitcoin on exchanges too long? | multiple-choice | easy |
| 2 | What is the most common way people lose their seed phrase? | multiple-choice | medium |
| 3 | How can malware steal your bitcoin when sending? | multiple-choice | medium |
| 4 | True/False: Small amounts of bitcoin are not targeted by hackers | true-false | easy |
| 5 | What should you do before considering yourself "set up"? | multiple-choice | medium |

#### Final Exam Pool (needs 40+ additional quizzes for overlap/comprehensive coverage)

Topics to cover across the entire course for final exam:

| # | Topic | Related Chapter | Difficulty |
|---|-------|-----------------|------------|
| 1 | Exchange risk scenarios (Mt. Gox, FTX) | Ch 2 | medium |
| 2 | Key types and their purposes | Ch 3 | easy |
| 3 | Wallet security trade-offs | Ch 4 | medium |
| 4 | Identifying custodial vs self-custody | Ch 5 | medium |
| 5 | Safe download practices | Ch 6 | medium |
| 6 | Seed phrase importance | Ch 7, 8 | easy |
| 7 | Transaction verification | Ch 9 | medium |
| 8 | Common scam recognition | Ch 10 | medium |
| 9 | Hardware wallet benefits | Ch 11 | medium |
| 10 | Security mistakes to avoid | Ch 12 | medium |
| 11-40 | Mixed topics covering all chapters | All | varied |

**Note:** The final exam pool of 40 quizzes can overlap with chapter quizzes. With 52 per-chapter quizzes created, there would be sufficient coverage for the final exam. Recommend creating 55-60 total unique quizzes to ensure comprehensive coverage.

---

### A8. Structural Fixes Required

| # | Issue | Location | Fix Required | Priority |
|---|-------|----------|--------------|----------|
| 1 | Missing "Going Further" chapter | End of Part 4 (best-practices-part4) | Add a "Going Further" chapter with resources, next steps, golden rules. Should be placed after Ch 12 (Common Mistakes) and before Part 5 (Conclusion) | **Critical** |
| 2 | Conclusion Part has 2 chapters | Part 5 (conclusion-part5) | Per standards, Conclusion Part should contain ONLY the Conclusion chapter. Either: (a) merge Ch 13 "Your Security Journey" content into Ch 14 "Conclusion", OR (b) move Ch 13 to be part of Part 4 before the new "Going Further" chapter | **High** |

**Recommended Structure After Fixes:**

```
Part 4: Best Practices & Growing Your Security
  - Ch 10: Security Best Practices
  - Ch 11: When to Upgrade Your Security
  - Ch 12: Common Mistakes and How to Avoid Them
  - Ch 13: Your Security Journey (moved from Conclusion Part)
  - Ch 14: Going Further (NEW - resources, next courses, golden rules)

Part 5: Conclusion
  - Ch 15: Conclusion (with <isCourseConclusion>true</isCourseConclusion>)
```

**OR Alternative (simpler):**

```
Part 4: Best Practices & Growing Your Security
  - Ch 10: Security Best Practices
  - Ch 11: When to Upgrade Your Security
  - Ch 12: Common Mistakes and How to Avoid Them
  - Ch 13: Going Further (NEW)

Part 5: Conclusion
  - Ch 14: Conclusion (merge "Your Security Journey" content into this, keep isCourseConclusion tag)
```

---

### A9. Work Summary for Phase B

**Before starting Phase B, complete these tasks:**

#### Critical (Must Do)
- [ ] Add "Going Further" chapter at end of Part 4 with:
  - Links to related courses (BTC105, SOV102)
  - External resources for further learning
  - Golden rules summary for Bitcoin security
- [ ] Restructure Conclusion Part to contain only Conclusion chapter (merge or move "Your Security Journey")
- [ ] Update chapter IDs if chapters are renumbered

#### Images to Create (38-40 total)
- [ ] Ch 1: 0-1 images (see specs in A5)
- [ ] Ch 2: 3-4 images (see specs in A5)
- [ ] Ch 3: 4-5 images (see specs in A5)
- [ ] Ch 4: 3-4 images (see specs in A5)
- [ ] Ch 5: 4-5 images (see specs in A5)
- [ ] Ch 6: 4-5 images (see specs in A5)
- [ ] Ch 7: 4-5 images (see specs in A5)
- [ ] Ch 8: 4-5 images (see specs in A5)
- [ ] Ch 9: 4-5 images (see specs in A5)
- [ ] Ch 10: 4-5 images (see specs in A5)
- [ ] Ch 11: 3-4 images (see specs in A5)
- [ ] Ch 12: 4-5 images (see specs in A5)
- [ ] Going Further (new): 1-2 images

#### Quizzes to Create (52-55 total)
- [ ] Ch 2: 5 quizzes (see topics in A7)
- [ ] Ch 3: 5 quizzes (see topics in A7)
- [ ] Ch 4: 4 quizzes (see topics in A7)
- [ ] Ch 5: 5 quizzes (see topics in A7)
- [ ] Ch 6: 5 quizzes (see topics in A7)
- [ ] Ch 7: 5 quizzes (see topics in A7)
- [ ] Ch 8: 5 quizzes (see topics in A7)
- [ ] Ch 9: 5 quizzes (see topics in A7)
- [ ] Ch 10: 5 quizzes (see topics in A7)
- [ ] Ch 11: 3 quizzes (see topics in A7)
- [ ] Ch 12: 5 quizzes (see topics in A7)
- [ ] Final exam pool coverage verified

---

**Phase A Status:** ✅ COMPLETE
**Phase A Completed:** 2026-01-21
**Notes:**
- Course structure is nearly complete with good content quality
- Two structural issues need fixing before Phase B: missing "Going Further" and Conclusion Part structure
- Significant image gap (3 existing vs ~40 needed) - most chapters need 4-5 images each
- Significant quiz gap (3 existing vs ~55 needed) - detailed topic suggestions provided
- Chapter content is well-written and beginner-friendly
- All metadata and frontmatter are properly configured
