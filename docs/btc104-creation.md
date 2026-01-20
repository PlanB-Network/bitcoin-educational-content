# BTC104 - How to Secure Your Bitcoin: Implementation Documentation

## Course Overview

**Course Code**: BTC104
**Title**: How to Secure Your Bitcoin
**Discipline**: Bitcoin (BTC)
**Level**: Beginner (104)
**Estimated Duration**: 1.5-2 hours
**Implementation Date**: 2026-01-20

---

## Course Philosophy

### Target Audience
Complete beginners who just acquired (or are about to acquire) their first bitcoin.

### Goal
A beginner-friendly, step-by-step guide through the ENTIRE process of:
1. Understanding what wallets are
2. Choosing the right wallet for their situation
3. Setting up their first wallet
4. Securing their seed phrase properly
5. Receiving bitcoin from an exchange or third party
6. Following best practices moving forward

### What This Course is NOT
- An advanced security encyclopedia (multisig, nodes, passphrases)
- A course for people with large holdings
- Comprehensive coverage of all security options

### Approach
Keep it simple, practical, and actionable. Complex topics are mentioned briefly with placeholders for future advanced courses.

---

## Source Content Mapping

### From BTC102 (en.md)

| BTC102 Section | Lines | Content Used |
|----------------|-------|--------------|
| Wallets and Security Strategies | 1286-1386 | Hot/cold wallets overview, wallet types |
| Backup tutorial reference | 1384-1386 | Tutorial link for backup-mnemonic |
| Hodler chapter | 1536-1564 | Hardware wallet setup references |
| Stacker chapter | 1662-1700 | Hot wallet recommendations |

### Key Adaptation Decisions

1. **Simplified from Profile-Based to Topic-Based**: Original BTC102 organized security by user profile (Hodler, Stacker, Active User, Paranoid). BTC104 organizes by topic (wallet types → setup → security practices) which is more logical for beginners.

2. **Hot Wallet First**: Recommends beginners start with hot wallets (free, easy), then graduate to hardware wallets as holdings grow.

3. **Advanced Topics as Placeholders**: Multisig, passphrases, metal backups, and running nodes are mentioned but noted as "for future advanced course."

---

## Final Course Structure

### Parts and Chapters (5 Parts, 14 Chapters)

```
# Part 1: Introduction
├── Ch 1: Welcome to BTC104 [NEW]
└── Ch 2: Why You Need Your Own Wallet [ORIGINAL + NEW]

# Part 2: Understanding Wallets
├── Ch 3: What Is a Bitcoin Wallet? [NEW + concepts]
├── Ch 4: Types of Wallets [ORIGINAL adapted]
└── Ch 5: Custodial vs Self-Custody [ORIGINAL adapted]

# Part 3: Setting Up Your First Wallet
├── Ch 6: Choosing Your First Wallet [NEW]
├── Ch 7: Creating Your Wallet [NEW + tutorial refs]
├── Ch 8: Securing Your Seed Phrase [ORIGINAL + NEW]
└── Ch 9: Receiving Your First Bitcoin [NEW]

# Part 4: Best Practices & Growing Your Security
├── Ch 10: Security Best Practices [NEW]
├── Ch 11: When to Upgrade Your Security [ORIGINAL adapted]
└── Ch 12: Common Mistakes and How to Avoid Them [NEW]

# Part 5: Conclusion
├── Ch 13: Your Security Journey [NEW]
└── Ch 14: Conclusion [STANDARD]
```

### Content Classification

| Content Type | Chapters | Notes |
|--------------|----------|-------|
| NEW | Ch 1, 3, 6, 7, 9, 10, 12, 13 | Welcome, wallet concepts, setup, practices |
| ORIGINAL (adapted) | Ch 2, 4, 5, 8, 11 | From BTC102 wallet sections |
| STANDARD | Ch 14 | Conclusion with isCourseConclusion tag |

---

## Asset Mapping

### Images Copied from BTC102

| BTC102 Image | BTC104 Image | Description | Used In |
|--------------|--------------|-------------|---------|
| 070.webp | 001.webp | Wallet overview diagram | Ch 2: Why You Need Your Own Wallet |
| 071.webp | 002.webp | Hot vs Cold comparison | Ch 4: Types of Wallets |
| 072.webp | 003.webp | Hybrid approach diagram | Ch 11: When to Upgrade |

**Total**: 3 images

### Images NOT Copied (Saved for Advanced Course)
- 076: Hardware wallet security diagram
- 081: Stacker security diagram
- 087: Active user security diagram
- 093, 094: Paranoid/advanced wallet setups

---

## Quiz Mapping

### Quizzes Copied from BTC102

| BTC102 Quiz | BTC104 Quiz | Topic | Chapter |
|-------------|-------------|-------|---------|
| 037 | 000 | Wallet selection | wallet-types-ch04 |
| 047 | 001 | Hardware wallet for long-term | upgrading-security-ch11 |
| 045 | 002 | Hot → Hardware transfer | upgrading-security-ch11 |

**Total**: 3 quizzes

### Quizzes NOT Copied (Saved for Advanced Course)
- 055: Metal backup with sealed envelope
- 058: Air-gapped/DIY hardware wallet
- Other advanced security quizzes

---

## Tutorial Cross-References

### Hot Wallet Tutorials (Primary - for beginners)
- https://planb.academy/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143 (Green Wallet)
- https://planb.academy/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90 (Blue Wallet)
- https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d (Sparrow)

### Hardware Wallet Tutorials (Mentioned for "when to upgrade")
- Ledger Nano S Plus
- Ledger Flex
- Trezor
- BitBox02
- Jade

### Backup Tutorial
- https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

---

## Implementation Checklist

### Phase 1: Setup
- [x] Create `courses/btc104/` folder
- [x] Create `courses/btc104/assets/en/` subfolder
- [x] Create `courses/btc104/quizz/` subfolder
- [x] Create `course.yml` with UUID and metadata

### Phase 2: Content
- [x] Create `en.md` with frontmatter
- [x] Write Part 1: Introduction (Ch 1-2)
- [x] Write Part 2: Understanding Wallets (Ch 3-5)
- [x] Write Part 3: Setting Up Your First Wallet (Ch 6-9)
- [x] Write Part 4: Best Practices (Ch 10-12)
- [x] Write Part 5: Conclusion (Ch 13-14)
- [x] Add ORIGINAL/NEW content tags throughout

### Phase 3: Assets
- [x] Copy image 070.webp → 001.webp
- [x] Copy image 071.webp → 002.webp
- [x] Copy image 072.webp → 003.webp
- [x] Update all image references in en.md

### Phase 4: Quizzes
- [x] Copy quiz 037 → 000
- [x] Copy quiz 047 → 001
- [x] Copy quiz 045 → 002
- [x] Update chapterId in each question.yml

### Phase 5: Documentation
- [x] Update btc102-split-plan.md with BTC104 details
- [x] Create this btc104-creation.md document

---

## Validation Checklist

- [x] All partIds are unique and follow pattern: `xxx-part#`
- [x] All chapterIds are unique and follow pattern: `xxx-ch##`
- [x] Final chapter has `<isCourseConclusion>true</isCourseConclusion>` tag
- [x] All image references use format `![image](assets/en/###.webp)`
- [x] Images exist at referenced paths
- [x] Quiz chapterIds match actual chapter IDs in en.md
- [x] ORIGINAL/NEW tags present on all content sections
- [x] Tutorial links are valid

---

## Future Advanced Security Course

Topics reserved for a future **BTC2XX - Advanced Bitcoin Security** course:

- Multisignature wallets (detailed setup with Liana, Sparrow)
- BIP39 passphrases (25th word)
- Metal seed backups (fire/water protection)
- Running your own Bitcoin node
- Air-gapped signing devices
- Advanced UTXO management
- Geographic distribution of backups
- Inheritance with multisig timelocks

This separation keeps BTC104 focused and accessible to beginners while preserving advanced content for dedicated users.

---

## Files Created/Modified

| File | Action |
|------|--------|
| `courses/btc104/course.yml` | CREATED |
| `courses/btc104/en.md` | CREATED |
| `courses/btc104/assets/en/001.webp` | COPIED from btc102 070.webp |
| `courses/btc104/assets/en/002.webp` | COPIED from btc102 071.webp |
| `courses/btc104/assets/en/003.webp` | COPIED from btc102 072.webp |
| `courses/btc104/quizz/000/` | COPIED from btc102 037, updated chapterId |
| `courses/btc104/quizz/001/` | COPIED from btc102 047, updated chapterId |
| `courses/btc104/quizz/002/` | COPIED from btc102 045, updated chapterId |
| `docs/btc102-split-plan.md` | UPDATED with BTC104 implementation details |
| `docs/btc104-creation.md` | CREATED (this file) |

---

## Notes

1. **Beginner Focus**: This course prioritizes simplicity over completeness. The goal is to get users successfully self-custodying bitcoin, not to make them security experts.

2. **Tutorial Heavy**: Rather than explaining every detail, the course points to existing tutorials for specific wallets. This keeps content concise and avoids duplication.

3. **Progressive Security**: The course explicitly tells beginners it's OK to start simple (hot wallet, paper backup) and upgrade later (hardware wallet, metal backup).

4. **Cross-References**: Clear pointers to:
   - BTC105 for acquisition
   - SOV102 for inheritance planning
   - Future advanced security course for multisig, etc.
