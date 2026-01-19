# SCU102 Creation Plan

## Overview

**Course**: SCU102 - Financial Fraud, Scams & Online Security
**Source**: BTC102 Part 1 "Prerequisites for understanding Bitcoin" (lines 75-549)
**Method**: Extract content from BTC102 and restructure into new course format

---

## Understanding the Split Process

The goal is to take the existing BTC102 content and **copy-paste it into a new structure**. This means:

1. **ORIGINAL content**: Text taken directly from BTC102 (copy-paste, minor edits for context)
2. **NEW content**: Text we need to write (introductions, transitions, conclusions)

Each piece of content will be tagged in the final `en.md` file:
```markdown
<!-- ORIGINAL: btc102/en.md lines XXX-YYY -->
[copied content]
<!-- END ORIGINAL -->

<!-- NEW -->
[newly written content]
<!-- END NEW -->
```

---

## Source Analysis: BTC102 Part 1

### Current BTC102 Structure (lines 75-549)

```
# Prerequisites for understanding Bitcoin (Part)
├── ## Scams and financial fraud (Chapter - lines 79-234)
│   ├── ### Bitcoin vs cryptos: understanding the differences
│   ├── ### The main scams to avoid
│   │   ├── #### Pyramid schemes and Ponzi schemes
│   │   ├── #### Pump & Dump
│   │   ├── #### Donation, Lottery, and Fake Giveaway Scams
│   │   ├── #### Shitcoins and cryptocurrencies on offer
│   │   ├── #### Identity theft and phishing
│   │   ├── #### Bitcoin Hardforks
│   │   └── #### Dishonest influencers and fake gurus
│   └── ### How to avoid scams
│
├── ## Online security (Chapter - lines 236-373)
│   ├── ### Why Cybersecurity Matters
│   ├── ### A clean, up-to-date computer
│   ├── ### The solution to the ID nightmare (password managers)
│   ├── ### 2FA: double protection
│   ├── ### Protecting your privacy
│   └── ### Step-by-step progression
│
└── ## Tips for newcomers (Chapter - lines 376-549)
    ├── ### Common mistakes to avoid
    ├── ### Defining an investment strategy
    ├── ### Understanding BTC's volatility
    ├── ### Managing and securing your Bitcoin wallet
    ├── ### Confidentiality and discretion
    ├── ### Tax implications
    ├── ### The Difference Between Trading, Investing, and Holding
    ├── ### Keep Learning
    └── ### Golden Rules to Keep in Mind
```

---

## Target Structure: SCU102

The new structure breaks out each major topic into its own chapter:

```
# Introduction (Part 1)
└── ## Introduction (Chapter 1) [NEW]

# Financial Fraud (Part 2)
├── ## Understanding Financial Fraud (Chapter 2) [ORIGINAL: lines 85-103 + NEW intro]
├── ## Pyramid & Ponzi Schemes (Chapter 3) [ORIGINAL: lines 109-131]
├── ## Pump & Dump Schemes (Chapter 4) [ORIGINAL: lines 132-159]
└── ## Fake Giveaways & Lotteries (Chapter 5) [ORIGINAL: lines 160-168]

# Crypto Scams (Part 3)
├── ## Shitcoins & Airdrops (Chapter 6) [ORIGINAL: lines 170-172]
├── ## Phishing & Identity Theft (Chapter 7) [ORIGINAL: lines 174-179]
├── ## Bitcoin Hardforks Confusion (Chapter 8) [ORIGINAL: lines 180-191]
└── ## Dishonest Influencers (Chapter 9) [ORIGINAL: lines 192-219]

# How to Protect Yourself (Part 4)
└── ## Red Flags & Verification (Chapter 10) [ORIGINAL: lines 221-234 + NEW]

# Online Security (Part 5)
├── ## Why Cybersecurity Matters (Chapter 11) [ORIGINAL: lines 240-255]
├── ## Clean Computer Practices (Chapter 12) [ORIGINAL: lines 256-283]
├── ## Password Security (Chapter 13) [ORIGINAL: lines 285-305 + reference SCU101]
├── ## Two-Factor Authentication (Chapter 14) [ORIGINAL: lines 306-325 + reference SCU101]
├── ## Privacy Protection (Chapter 15) [ORIGINAL: lines 326-359 + reference SCU101]
└── ## Step-by-Step Security Progression (Chapter 16) [ORIGINAL: lines 360-373]

# Tips for Bitcoin Beginners (Part 6)
├── ## Common Mistakes to Avoid (Chapter 17) [ORIGINAL: lines 398-419]
├── ## Investment Strategy Basics (Chapter 18) [ORIGINAL: lines 421-448]
├── ## Understanding Volatility (Chapter 19) [ORIGINAL: lines 440-448]
├── ## Wallet Security Fundamentals (Chapter 20) [ORIGINAL: lines 450-469]
├── ## Confidentiality & Discretion (Chapter 21) [ORIGINAL: lines 470-485]
├── ## Tax Awareness (Chapter 22) [ORIGINAL: lines 486-495]
└── ## Trading vs Investing vs Holding (Chapter 23) [ORIGINAL: lines 497-528]

# Conclusion (Part 7)
├── ## Keep Learning (Chapter 24) [ORIGINAL: lines 529-537 + NEW]
├── ## Golden Rules (Chapter 25) [ORIGINAL: lines 539-548]
└── ## Next Steps (Chapter 26) [NEW]
```

---

## Content Mapping Table

| SCU102 Chapter | Source | BTC102 Lines | Content Type | Images | Quizzes |
|----------------|--------|--------------|--------------|--------|---------|
| Ch 1: Introduction | NEW | - | NEW | - | - |
| Ch 2: Understanding Financial Fraud | BTC102 | 85-103 | ORIGINAL + NEW intro | 005, 006 | - |
| Ch 3: Pyramid & Ponzi Schemes | BTC102 | 109-131 | ORIGINAL | 007 | 000, 004 |
| Ch 4: Pump & Dump | BTC102 | 132-159 | ORIGINAL | 008, 009 | 003 |
| Ch 5: Fake Giveaways | BTC102 | 160-168 | ORIGINAL | 010 | 002 |
| Ch 6: Shitcoins & Airdrops | BTC102 | 170-172 | ORIGINAL + NEW expansion | - | - |
| Ch 7: Phishing | BTC102 | 174-179 | ORIGINAL | - | 001 |
| Ch 8: Bitcoin Hardforks | BTC102 | 180-191 | ORIGINAL | 011 | - |
| Ch 9: Dishonest Influencers | BTC102 | 192-219 | ORIGINAL | 012 | - |
| Ch 10: Red Flags | BTC102 | 221-234 | ORIGINAL | - | - |
| Ch 11: Why Cybersecurity Matters | BTC102 | 240-255 | ORIGINAL | - | 009 |
| Ch 12: Clean Computer | BTC102 | 256-283 | ORIGINAL | 013, 014 | 007, 008 |
| Ch 13: Password Security | BTC102 | 285-305 | ORIGINAL + SCU101 ref | 015 | 006 |
| Ch 14: 2FA | BTC102 | 306-325 | ORIGINAL + SCU101 ref | 016, 017, 018 | 005 |
| Ch 15: Privacy | BTC102 | 326-359 | ORIGINAL + SCU101 ref | 019, 020 | - |
| Ch 16: Step-by-Step | BTC102 | 360-373 | ORIGINAL | - | - |
| Ch 17: Common Mistakes | BTC102 | 398-419 | ORIGINAL | 021, 022 | - |
| Ch 18: Investment Strategy | BTC102 | 421-439 | ORIGINAL | 023 | 014 |
| Ch 19: Volatility | BTC102 | 440-448 | ORIGINAL | 024 | - |
| Ch 20: Wallet Security | BTC102 | 450-469 | ORIGINAL | 025, 026 | 011, 012 |
| Ch 21: Confidentiality | BTC102 | 470-485 | ORIGINAL | - | 010 |
| Ch 22: Tax Awareness | BTC102 | 486-495 | ORIGINAL | 027, 028 | - |
| Ch 23: Trading vs Investing | BTC102 | 497-528 | ORIGINAL | - | 013 |
| Ch 24: Keep Learning | BTC102 | 529-537 | ORIGINAL + NEW | 029 | - |
| Ch 25: Golden Rules | BTC102 | 539-548 | ORIGINAL | - | - |
| Ch 26: Next Steps | NEW | - | NEW | - | - |

---

## Quiz Mapping

Based on quiz analysis, these quizzes belong to SCU102:

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

## Asset Mapping

| Image # | Topic | Target Chapter |
|---------|-------|----------------|
| 005 | Bitcoin vs Crypto ecosystem | Ch 2 |
| 006 | Crypto ecosystem warning | Ch 2 |
| 007 | Ponzi/Pyramid diagram | Ch 3 |
| 008 | Pump & Dump cycle | Ch 4 |
| 009 | Signal groups warning | Ch 4 |
| 010 | Fake giveaway example | Ch 5 |
| 011 | Bitcoin hardforks diagram | Ch 8 |
| 012 | Dishonest influencers | Ch 9 |
| 013 | Clean computer/antivirus | Ch 12 |
| 014 | 3-2-1 Backup rule | Ch 12 |
| 015 | Password manager concept | Ch 13 |
| 016 | 2FA concept | Ch 14 |
| 017 | 2FA app screenshot | Ch 14 |
| 018 | SIM swap warning | Ch 14 |
| 019 | VPN concept | Ch 15 |
| 020 | Privacy tools summary | Ch 15 |
| 021 | Tips overview | Ch 17 |
| 022 | Common mistakes list | Ch 17 |
| 023 | Budget planning | Ch 18 |
| 024 | Volatility chart | Ch 19 |
| 025 | Seed phrase importance | Ch 20 |
| 026 | Not your keys warning | Ch 20 |
| 027 | Tax implications | Ch 22 |
| 028 | Tax calendar | Ch 22 |
| 029 | Learning resources | Ch 24 |

**Total images for SCU102**: 25 (images 005-029)

---

## Implementation Steps

### Step 1: Create Course Folder Structure
```
courses/scu102/
├── course.yml
├── en.md
├── assets/
│   └── en/
│       └── [copy images 005-029 from btc102, renumber as 001-025]
└── quizz/
    ├── 000/ [copy from btc102/quizz/000]
    ├── 001/ [copy from btc102/quizz/001]
    ├── ...
    └── 014/ [copy from btc102/quizz/014]
```

### Step 2: Create course.yml
```yaml
level: beginner
hours: 3
topic: security
subtopic: fraud-protection
teachers:
  - rabbit-hole
contributors:
  - another-rabbit-hole
tags:
  - scams
  - fraud
  - security
  - privacy
```

### Step 3: Create en.md Content

For each chapter:
1. Copy the relevant lines from BTC102
2. Add `<!-- ORIGINAL -->` tags
3. Write NEW intro/transition text with `<!-- NEW -->` tags
4. Update image references (renumber from 005-029 to 001-025)
5. Ensure proper markdown hierarchy (# Part, ## Chapter, ### Subsection)

### Step 4: Copy Assets
- Copy images 005-029 from `btc102/assets/en/`
- Renumber to 001-025 in `scu102/assets/en/`
- Copy all language versions if available

### Step 5: Copy Quizzes
- Copy quiz folders 000-014 from `btc102/quizz/`
- Maintain same numbering in `scu102/quizz/`

### Step 6: Validation
- Check all image references work
- Check all internal links work
- Verify quiz placement
- Test markdown rendering

---

## Content to Write (NEW)

### Chapter 1: Introduction (fully NEW)
- Course overview and objectives
- Why scams and security matter for Bitcoiners
- What you'll learn
- Link to SCU101 for technical security tools
- Estimated completion time

### Chapter 6: Shitcoins & Airdrops (expand ORIGINAL)
- Original content is very short (3 lines)
- Need to expand with more examples
- Add red flags for identifying worthless tokens

### Chapter 26: Next Steps (fully NEW)
- Summary of what was learned
- Recommended next courses (BTC103, BTC104, SCU101)
- Resources for continued learning
- Final encouragement

### Transitions Between Parts (NEW)
- Brief intro text at start of each Part
- Connection to previous Part's content

---

## SCU101 Cross-References

For chapters that overlap with SCU101 technical tutorials, add reference boxes:

```markdown
> **Want to set this up?**
> For step-by-step tutorials on setting up [tool], check out SCU101:
> https://planb.academy/courses/scu101
```

Apply to:
- Chapter 13: Password managers (Bitwarden, KeePass tutorials in SCU101)
- Chapter 14: 2FA (Authy tutorial in SCU101)
- Chapter 15: Privacy (VPN, Tor tutorials in SCU101)

---

## File Naming Convention

### Image Renumbering
| BTC102 Image | SCU102 Image |
|--------------|--------------|
| 005.webp | 001.webp |
| 006.webp | 002.webp |
| 007.webp | 003.webp |
| ... | ... |
| 029.webp | 025.webp |

Formula: `SCU102_image = BTC102_image - 4`

---

## Checklist for Implementation

- [x] Create `courses/scu102/` folder
- [x] Create `course.yml` with metadata
- [x] Create `en.md` with all 26 chapters
- [x] Copy and renumber images (005-029 → 001-025)
- [x] Copy quiz folders (000-014)
- [x] Write NEW content for Chapter 1 (Introduction)
- [x] Write NEW content for Chapter 26 (Next Steps)
- [x] Expand Chapter 6 (Shitcoins) content
- [x] Add SCU101 cross-references in Chapters 13, 14, 15
- [x] Update all image references in en.md
- [x] Validate markdown structure
- [ ] Test build locally if possible
- [ ] Review content for accuracy and flow
- [ ] Add videos (:::video id=XXX::: placeholders)
- [ ] Create thumbnail

---

## Implementation Notes (2026-01-19)

### What Was Created

1. **Folder Structure**: `courses/scu102/` with:
   - `course.yml` - Course metadata
   - `en.md` - Main content file (26 chapters across 7 parts)
   - `assets/en/` - 25 images (001-025.webp)
   - `quizz/` - 15 quiz folders (000-014)

2. **Content Tagging**: All content in en.md is tagged with:
   - `<!-- ORIGINAL: btc102/en.md lines XXX-YYY -->` for copied content
   - `<!-- NEW -->` for newly written content
   - `<!-- END ORIGINAL -->` and `<!-- END NEW -->` closing tags

3. **New Content Written**:
   - Chapter 1: Full introduction with course overview, prerequisites, and learning objectives
   - Chapter 6: Expanded shitcoin/airdrop warnings with red flags lists
   - Chapter 26: Complete conclusion with summary, next steps, and resources
   - Part introductions for all 7 parts

4. **Cross-References Added**:
   - SCU101 references in Chapters 13 (Passwords), 14 (2FA), 15 (Privacy)
   - Links to other Plan B Academy courses throughout

### What Still Needs Review

- Overall content flow and readability
- Accuracy of copied content (ensure no context was lost)
- Quiz placement - quizzes are numbered 000-014 but chapter assignments may need adjustment
- Video IDs will need to be created/assigned

---

## Notes

- Keep original BTC102 untouched until SCU102 is validated
- All translations will need to follow the same structure later
- Video placeholders (:::video id=XXX:::) will need new video IDs later
- Thumbnail placeholder needed

---

*Document created: 2026-01-19*
*Last updated: 2026-01-19*
*Implementation completed: 2026-01-19*

---

## Session Summary (2026-01-19)

### What Was Done This Session

1. **Created SCU102 course folder structure**:
   - `courses/scu102/course.yml` - Course metadata (beginner, 3 hours, security topic)
   - `courses/scu102/en.md` - Full content file with 26 chapters in 7 parts
   - `courses/scu102/assets/en/` - 25 images (001-025.webp, renumbered from btc102 005-029)
   - `courses/scu102/quizz/` - 15 quiz folders (000-014, copied from btc102)

2. **Content created with tagging**:
   - All ORIGINAL content tagged with `<!-- ORIGINAL: btc102/en.md lines XXX-YYY -->`
   - All NEW content tagged with `<!-- NEW -->`
   - Closing tags: `<!-- END ORIGINAL -->` and `<!-- END NEW -->`

3. **New content written**:
   - Chapter 1: Full introduction (course overview, what you'll learn, prerequisites, SCU101 reference)
   - Chapter 6: Expanded shitcoins section (added red flags for worthless tokens and airdrops)
   - Chapter 26: Complete conclusion (summary, next steps, recommended courses)
   - Part introductions for all 7 parts

4. **Cross-references added**:
   - SCU101 tutorial links in Chapters 13, 14, 15
   - Links to BTC101, BTC103, SEC101 throughout

### What Needs User Review

1. **Content in `courses/scu102/en.md`**:
   - Read through for flow and accuracy
   - Check that ORIGINAL content wasn't taken out of context
   - Verify NEW content tone matches Plan B Academy style
   - Confirm chapter structure makes sense

2. **Quiz placement**:
   - Quizzes 000-014 are copied but not embedded in specific chapters
   - May need `:::quizz id=XXX:::` tags added to chapters

3. **Missing elements**:
   - No `:::video id=XXX:::` tags (videos need to be created separately)
   - No thumbnail.webp
   - No translations (only en.md created)

### Files to Review

| File | Purpose | Status |
|------|---------|--------|
| `courses/scu102/en.md` | Main course content | **NEEDS REVIEW** |
| `courses/scu102/course.yml` | Course metadata | Ready |
| `courses/scu102/assets/en/*.webp` | 25 images | Ready (copied from btc102) |
| `courses/scu102/quizz/000-014/` | 15 quiz folders | Ready (copied from btc102) |
| `docs/scu102-creation.md` | Implementation doc | Updated |
| `docs/btc102-split-plan.md` | Master plan | Updated |

### Next Steps After Review

1. User reviews `courses/scu102/en.md` and provides feedback
2. Make any requested changes to SCU102
3. Once SCU102 is approved, proceed to ECO105 (Why Bitcoin Matters)
4. Document learnings from SCU102 to streamline remaining course creation
