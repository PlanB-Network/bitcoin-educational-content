---
name: "BTC101 — Teacher Guide"
goal: "Provide structured lesson plans for educators delivering BTC101: The Bitcoin Journey in classroom or live settings."
objectives:
  - "Equip teachers with per-chapter learning objectives and key talking points"
  - "Offer ready-made discussion questions and assignment ideas for each chapter"
  - "Provide pacing guidance for an estimated ~7-hour course delivery"
---

# BTC101 Teacher Guide

This guide is designed for educators delivering BTC101 in a classroom, workshop, or live online setting. It mirrors the structure of the student course — same parts and chapters — but provides teacher-specific content: learning objectives, key concepts to emphasize, teaching tips, discussion questions, and assignment ideas.

**How to use this guide:**

- Each chapter includes an **estimated time**. These are approximations — adjust to your audience and format. The total is roughly 7 hours.
- **Learning Objectives** use measurable verbs (explain, identify, compare, demonstrate) so you can assess whether students achieved them.
- **Key Concepts** are the essential ideas you must convey. If time is short, prioritize these.
- **Teaching Tips** offer suggested flow, useful analogies, and common misconceptions to watch for.
- **Discussion Questions** are open-ended prompts for classroom engagement.
- **Assignment Ideas** are optional homework or in-class activities.
- **Quiz Focus** tells you which difficulty levels from the quiz bank to prioritize for that chapter.

**Prerequisites for students:** None. BTC101 is a beginner course requiring no prior knowledge.

**Materials needed:** Access to the BTC101 slide deck (images in `assets/en/`), internet connection for live demos (optional), printed quiz sheets (generated via `quizz_to_pdf.py`).

+++

# Part 1 — Introduction

Estimated time for this part: ~30 minutes

This part sets the stage. Students need to understand what Bitcoin is at a high level and where it came from. Do not go deep into technical details here — the goal is to spark curiosity and provide historical context.

## Course Overview

**Estimated time: ~10 minutes**

### Learning Objectives
- Describe what Bitcoin is at a high level (protocol + currency)
- Distinguish between "Bitcoin" (the protocol) and "bitcoin" (the monetary unit)
- Identify the main topics covered in the course (money, wallets, technical aspects, acquisition, future)

### Key Concepts
- Bitcoin is both a computer protocol and a monetary unit
- It is neutral and decentralized — not controlled by any entity or institution
- Bitcoin uses cryptography, network communication, and blockchain technology
- The course covers: monetary aspects, wallets, mining, transactions, Lightning Network, and Bitcoin's future
- No prior knowledge is required — this is an accessible beginner course

### Teaching Tips
Start by asking the class: "What do you already know or think about Bitcoin?" This surfaces preconceptions you can address throughout the course. Emphasize the dual nature of Bitcoin early — students often confuse the network/protocol (capital B) with the currency unit (lowercase b). Use the analogy: "Bitcoin is like the internet (a protocol), and bitcoin is like email (one application running on it)." Keep this chapter brief — it is a roadmap, not a deep dive.

### Discussion Questions
1. What comes to mind when you hear the word "Bitcoin"? Is your first reaction positive, negative, or neutral — and why?
2. Can you think of other technologies that are both a protocol and an everyday tool? (Examples: the internet/email, HTTP/websites)

### Assignment Ideas
- Write 3 sentences describing what you think Bitcoin is before starting the course. You will revisit this at the end to see how your understanding evolved.

### Quiz Focus
- Use easy-difficulty questions only. This chapter is introductory — quiz questions should confirm students understand the course scope.


## The Prehistory of Bitcoin

**Estimated time: ~20 minutes**

### Learning Objectives
- Explain the cypherpunk movement and its relevance to Bitcoin's creation
- Name at least 3 key figures or projects that preceded Bitcoin (e.g., David Chaum/DigiCash, Wei Dai/B-money, Tim May)
- Summarize the 3 foundational cypherpunk texts and their core ideas
- Describe the context in which Satoshi Nakamoto published the Bitcoin whitepaper

### Key Concepts
- The cypherpunk movement (1980s-1990s): believed cryptography could protect individual rights against governments and corporations
- Key figures: Julian Assange, Wei Dai, Tim May, David Chaum, Eric Hughes
- Three foundational texts: "A Cypherpunk's Manifesto" (Hughes, 1993 — privacy as a right), "The Crypto Anarchist Manifesto" (May, 1992 — cryptographic anarchy), "A Declaration of the Independence of Cyberspace" (Barlow, 1996 — cyberspace beyond government reach)
- Predecessors: DigiCash (Chaum, 1980s — anonymous electronic money, failed commercially), B-money (Wei Dai — anonymous digital currency with community-based fraud detection, never implemented)
- Satoshi Nakamoto published the Bitcoin whitepaper in 2008, combining proof of work, cryptographic timestamps, and decentralization
- Bitcoin represents the culmination of cypherpunk ideals: transparency, decentralization, individual sovereignty

### Teaching Tips
Frame this chapter as a "detective story" — Bitcoin did not appear out of nowhere. Walk students through the timeline visually (use the course images showing the development of innovations). A common misconception is that Bitcoin was the first digital currency — emphasize the many failed predecessors and what they got wrong (centralization, trusted third parties). End by teasing the question: "But is Bitcoin real money?" to transition into Part 2.

### Discussion Questions
1. Why did projects like DigiCash fail where Bitcoin succeeded? What was fundamentally different?
2. The cypherpunks believed privacy is a right, not a privilege. Do you agree? Can you think of situations where financial privacy matters?
3. Why does it matter that Bitcoin's creator is anonymous?

### Assignment Ideas
- Research one Bitcoin predecessor (DigiCash, B-money, Hashcash, or Bit Gold) and write a short paragraph explaining what it tried to do and why it failed.
- Read the first paragraph of "A Cypherpunk's Manifesto" by Eric Hughes and summarize its main argument in your own words.

### Quiz Focus
- Use easy-difficulty questions. Focus on name recognition (who created what) and timeline awareness.


# Part 2 — Money

Estimated time for this part: ~100 minutes

This is a foundational part. Students must understand what money is before they can understand why Bitcoin matters. Take time here — the concepts of store of value, monetary devaluation, and hyperinflation are the "why" behind Bitcoin. If students grasp this part well, the rest of the course clicks into place.

## Money Throughout History

**Estimated time: ~25 minutes**

### Learning Objectives
- Explain the 3 main functions of money (store of value, medium of exchange, unit of account)
- Trace the evolution of money from commodity money to digital money
- Identify the key characteristics of good money (fungibility, divisibility, liquidity, durability, portability, scarcity)
- Compare gold, fiat currencies, and Bitcoin across these characteristics

### Key Concepts
- Money is a communication tool: it allows exchange across time (savings) and across language/culture (universal trade)
- Money is not a government invention — it emerged naturally from markets and voluntary consensus
- Functions of money: store of value (durable), medium of exchange (widely accepted), unit of account (measuring stick for value)
- Evolution: raw materials (grain, livestock) → commodity money (shells, salt) → precious metals (gold) → banknotes → digital (bank cards) → blockchain/Lightning
- Gold became dominant due to "monetary Darwinism" — rarity, durability, divisibility — but struggles with portability and divisibility in a digital world
- Bitcoin combines the scarcity of gold with the portability of digital money
- Prices are signals — they guide how society allocates resources

### Teaching Tips
Begin with a concrete question: "What makes something money? Would this pen work as money? Why or why not?" Walk through the characteristics using physical examples (a gold coin vs. a dollar bill vs. a phone showing a Bitcoin wallet). The biggest insight for students is often that money is a *technology* that evolved, not something decreed by governments. Use the "coincidence of wants" problem to explain why barter fails — it makes the need for money visceral. When comparing gold, fiat, and Bitcoin, use a table on the board showing each characteristic (scarcity, portability, divisibility, durability) with checkmarks.

### Discussion Questions
1. If money is a technology, what "problem" does it solve? Can you imagine a world without money?
2. Why did gold beat other commodities (shells, salt, cattle) as money? What changed that made gold insufficient?
3. In what ways is Bitcoin better than gold? In what ways is it worse?

### Assignment Ideas
- **Research task**: Pick one historical form of money (Rai stones, wampum, salt, cowrie shells) and write 200 words on why it worked as money and what caused it to fail.
- **Comparison table**: Create a table comparing gold, the US dollar, and Bitcoin across the 6 characteristics of good money (fungibility, divisibility, liquidity, durability, portability, scarcity). Rate each as high/medium/low.

### Quiz Focus
- Mix easy and intermediate questions. This chapter has 18 quiz questions in the bank — select 6-8 covering the functions and characteristics of money.


## Fiduciary Currencies

**Estimated time: ~25 minutes**

### Learning Objectives
- Define what a fiduciary (fiat) currency is and explain why it is called "fiduciary" (trust-based)
- Describe the historical pattern of monetary devaluation (gold centralization → new currency → devaluation → delinking from gold)
- Explain how the dollar has lost 98% of its value in 100 years
- Articulate why Bitcoin is proposed as an alternative to fiat currencies

### Key Concepts
- "Fiduciary" comes from "trust" — fiat currencies have no intrinsic value, they depend on trust in the issuing institution
- Central banks (Fed, ECB, PBoC) control the money supply — they decide how much money is printed
- The devaluation playbook is ancient (Roman Empire onward): centralize gold → mint new currency → gradually debase it → break the gold link entirely
- Silent devaluation: justified as "in the interest of the people," it erodes savings while making debt easier to repay
- Historical losses: the dollar lost 98% in 100 years, the euro 30% in 20 years, the pound 99% since creation
- CBDCs (Central Bank Digital Currencies) represent even more centralized control over money
- Bitcoin requires no trusted third party — it separates money from the state
- Hayek quote (1984): "I don't believe we shall ever have a good money again before we take the thing out of the hands of government"

### Teaching Tips
The Roman Empire analogy is powerful — walk through it step by step (gold centralization → coin minting → coin clipping → currency collapse). Students are often shocked by the "98% dollar devaluation" stat — show it visually if possible (purchasing power chart over time). Be careful not to be preachy about fiat — present the facts and let students draw conclusions. A common misconception: students think inflation is just "prices going up." Clarify that inflation is the expansion of the money supply; rising prices are a *symptom*. The Hayek quote is a strong closer for this chapter.

### Discussion Questions
1. If the dollar has lost 98% of its value, why do people still use it? What keeps the system running?
2. How is the Roman Empire's monetary devaluation similar to what central banks do today?
3. What are the potential risks and benefits of CBDCs from a citizen's perspective?

### Assignment Ideas
- Look up the current inflation rate in your country. How much purchasing power would you lose over 10 years at that rate? Calculate it.
- Read the Hayek quote in context. Do you agree that money should be separated from government? Write a short argument for or against.

### Quiz Focus
- Mix easy and intermediate questions. Prioritize questions about the fiduciary system's mechanics and the devaluation pattern.


## Hyperinflation

**Estimated time: ~25 minutes**

### Learning Objectives
- Define hyperinflation and distinguish it from regular inflation
- Describe the 4 phases of hyperinflation (loss of confidence → currency collapse → printing spiral → new currency)
- Summarize 3 historical examples of hyperinflation (Germany 1922-23, Hungary 1945-46, Zimbabwe 2007-08)
- Explain why hyperinflation is always the result of deliberate monetary policy decisions, not external forces

### Key Concepts
- Hyperinflation = complete loss of confidence + drastic inflation due to money printing; not 20%/year, but 20%/month or per day
- Impact on savings: at 2% inflation, you lose 10% in 5 years; at 7%, half in 10 years; at 20%, half in 3 years
- The 4 phases: (1) loss of confidence in centralized monetary power, (2) currency collapse as people flee to stable currencies, (3) vicious circle of printing, (4) a new currency is introduced with stricter controls
- Germany (1922-23): post-WWI reparations → 29,500% monthly inflation in Oct 1923 → prices doubled every 3.7 days → people burned money for heat
- Hungary (1945-46): worst hyperinflation in history → 41.9 quadrillion % monthly inflation in July 1946 → prices doubled every 15 hours
- Zimbabwe (2007-08): land reforms → currency collapse → 79.6 billion % monthly inflation → dollar suspended, foreign currencies adopted
- Key lesson: hyperinflation does not happen by chance — it is the direct consequence of irresponsible monetary decisions

### Teaching Tips
This chapter is emotionally powerful — use it. The Germany, Hungary, and Zimbabwe stories are vivid and relatable. Show the images of worthless banknotes, people burning money, or wheelbarrows of cash. Ask students: "What would you do if your savings lost half their value overnight?" The common misconception is that hyperinflation "can't happen here" — point out that it has happened across continents, cultures, and eras. Emphasize that the pattern is always the same: government overprints → currency collapses → citizens suffer. This chapter should make students viscerally understand *why* a fixed-supply currency matters.

### Discussion Questions
1. Could hyperinflation happen in a developed country today (e.g., the US, EU)? What conditions would need to be met?
2. In each historical example, who suffered the most — and who benefited?
3. If you lived in Zimbabwe in 2008, what would you have done to protect your savings?

### Assignment Ideas
- **Case study**: Choose one of the 3 hyperinflation examples and research it further. Write 300 words on: What caused it? Who suffered most? How was it resolved?
- **Math exercise**: If inflation is 20% per month, calculate how much a $1,000 savings account would be worth after 6 months and after 12 months.

### Quiz Focus
- Use easy and intermediate questions. Focus on the phases of hyperinflation and the historical examples.


## 21 Million Bitcoins

**Estimated time: ~25 minutes**

### Learning Objectives
- Explain Bitcoin's fixed supply of 21 million units and why it matters
- Describe the halving mechanism and its effect on new bitcoin issuance
- Explain the mining difficulty adjustment and its purpose
- Articulate how game theory protects Bitcoin's monetary policy from change
- Demonstrate that Bitcoin's supply is publicly auditable

### Key Concepts
- Bitcoin has a hard cap of 21 million units, enforced by code and consensus
- New bitcoins are created through mining: miners solve cryptographic puzzles and are rewarded with new BTC
- The halving: every 210,000 blocks (~4 years), the mining reward is cut in half. Started at 50 BTC, now 3.125 BTC (5th epoch, 2024)
- The halving table: a predictable, stair-step issuance curve approaching 21 million around year 2140
- Mining difficulty adjustment: every 2,016 blocks (~2 weeks), difficulty recalibrates to maintain ~10 min average block time, regardless of how many miners participate
- Game theory protection: changing the 21M cap would require all users to agree to devalue their own savings — economically irrational
- Auditability: anyone running a node can verify the total supply with a single command (`bitcoin-cli gettxoutsetinfo`)
- Contrast with fiat: Bitcoin's monetary policy is transparent, predictable, and not subject to political decisions

### Teaching Tips
The halving table is a visual centerpiece — display it and let students trace how the supply approaches 21 million asymptotically. Use the analogy of gold mining: "Imagine if we knew exactly how much gold was left in the earth and exactly when each ounce would be mined." The difficulty adjustment is often misunderstood — explain it as a thermostat that keeps block production at a steady rate. For game theory, pose the question: "Would you vote to print more bitcoin if it meant your existing bitcoin was worth less?" The `gettxoutsetinfo` command is a powerful moment — if possible, show it live or share a screenshot. This makes "don't trust, verify" tangible.

### Discussion Questions
1. Why is a predictable monetary policy important? What happens when a monetary policy can be changed by a small group?
2. The last bitcoin will be mined around 2140. How will miners be compensated after that? Does this concern you?
3. Compare Bitcoin's supply transparency to the Federal Reserve's balance sheet. Which one can you verify yourself?

### Assignment Ideas
- **Calculation exercise**: Using the halving table, calculate what percentage of all Bitcoin will have been mined by 2030. By 2040.
- **Thought experiment**: Write 200 words on what would happen if someone tried to create a "22nd million bitcoin." Who would need to agree, and why would they (or wouldn't they)?

### Quiz Focus
- Use intermediate and hard questions. This chapter is conceptually dense — quiz on the halving mechanism, difficulty adjustment, and the role of game theory.


# Part 3 — Bitcoin Wallets

Estimated time for this part: ~70 minutes

This part transitions from "why Bitcoin" to "how to use Bitcoin." Students will learn about wallets, security, and long-term storage. Make it practical — if possible, do a live demo of a wallet. The security levels framework is a useful mental model students should internalize.

## What Are Bitcoin Wallets?

**Estimated time: ~20 minutes**

### Learning Objectives
- Explain what a Bitcoin wallet is and its 3 main functions (receive, send, secure)
- Distinguish between private keys and public keys using the asymmetric cryptography model
- Explain why "not your keys, not your coins" is a fundamental principle
- Clarify the common misconception that bitcoins are "stored in" a wallet

### Key Concepts
- A wallet interacts with the Bitcoin network in 3 ways: receive, send, and secure bitcoins
- Wallets come in many forms: software (phone/PC), hardware (USB-like device), or even paper
- Asymmetric cryptography: private key (spending power, must be secret) → public key (derived from private key) → address (derived from public key, safe to share)
- The mnemonic phrase (12 or 24 words) represents the private key — this is the master backup
- Bitcoins are not "in" the wallet — they are recorded on the blockchain. The wallet holds the keys that prove ownership.
- The mailbox analogy: anyone can deposit money through the slot (public address), but only you can open it (private key)
- The probability of guessing a mnemonic phrase is like finding a specific atom in the universe (2^256 possibilities)
- Use each address only once for maximum privacy

### Teaching Tips
The biggest "aha moment" in this chapter is that bitcoins are not stored in wallets — the wallet holds keys, and the blockchain holds the record. Use the mailbox analogy from the course. Many students confuse public keys and addresses — clarify that the address is derived from the public key and is what you share. If you have access to a wallet app, do a quick live demo showing a receive address being generated. Emphasize the mnemonic phrase: "These 12 or 24 words ARE your bitcoin. If someone has them, they have your money."

### Discussion Questions
1. Why is it important that you can regenerate your wallet from a mnemonic phrase? What does this imply about the role of the wallet software?
2. The mailbox analogy: how does it break down? Are there aspects of Bitcoin wallets that the analogy doesn't capture?

### Assignment Ideas
- Download a Bitcoin testnet wallet (e.g., Sparrow on testnet) and generate a receive address. Screenshot the address and note: which part is the public key? Which is the address?
- Explain in your own words why "not your keys, not your coins" matters, using a real-world analogy.

### Quiz Focus
- Mix easy and intermediate questions. Focus on the key/address distinction and the mnemonic phrase concept.


## Bitcoin Wallets and Security

**Estimated time: ~20 minutes**

### Learning Objectives
- List the 5 security levels for Bitcoin wallets (Level 0 to Level 4)
- Explain the trade-offs between convenience and security at each level
- Recommend an appropriate security level based on use case (daily spending vs. long-term savings vs. corporate)
- Define custodial vs. non-custodial wallets

### Key Concepts
- Security is not one-size-fits-all — it depends on: who can access funds, intended use, technical skills, and budget
- Level 0 (Custodial): a third party holds your keys (like a bank). They can restrict access at any time.
- Level 1 (Hot wallet): software wallet on phone/PC. You hold keys, but the device is internet-connected. Back up mnemonic phrase!
- Level 2 (Cold wallet): hardware wallet (Ledger, Satochip, Tapsigner). Keys stored offline. Must physically sign transactions.
- Level 3 (Cold wallet + passphrase): adds a BIP39 passphrase (extra word) on top of the mnemonic. Two things to back up separately.
- Level 4 (Multisig): multiple wallets required to sign a transaction. For corporate use or very large amounts. Parts stored in different locations.
- Key principle: adapt security to the amount and use case. Don't over-engineer (complexity can cause losses too).
- Essential advice: avoid custodial services, use mobile for daily expenses, cold wallet for savings

### Teaching Tips
Present the 5 levels as a spectrum, not a ladder. Not everyone needs Level 4 — and over-engineering can be as dangerous as under-securing (if you lose one of your multisig keys, you lose everything). Use real examples: "Level 1 is like cash in your pocket — fine for coffee money. Level 2 is like a safe at home. Level 4 is like a bank vault with multiple keyholders." The custodial vs. non-custodial distinction is critical — many students use exchanges without realizing they don't own their bitcoin. Ask: "If the exchange goes bankrupt tomorrow, can you get your bitcoin?"

### Discussion Questions
1. Which security level would you choose for: (a) $50 in bitcoin for weekly coffee, (b) $5,000 in savings, (c) $100,000 for a company? Why?
2. What are the risks of over-securing your bitcoin? Can too much security be a problem?
3. Why should you avoid keeping large amounts on exchanges?

### Assignment Ideas
- Create a security plan for a hypothetical person who just bought $2,000 worth of Bitcoin. Recommend a wallet type, backup strategy, and explain your reasoning.

### Quiz Focus
- Mix easy and intermediate questions. Focus on the security levels and custodial vs. non-custodial distinction.


## Setting Up a Wallet

**Estimated time: ~15 minutes**

### Learning Objectives
- List the critical security practices when setting up a new wallet (covering cameras, no photos, no digital copies)
- Explain the proper way to physically record a mnemonic phrase
- Identify common mistakes that lead to loss of funds

### Key Concepts
- When the wallet generates your mnemonic phrase, this is the most security-sensitive moment
- Critical rules: cover cameras, no photos, no typing into a computer, no SMS, no leaving words unattended
- Write the mnemonic phrase on paper (or use a template) with a pen, clearly and neatly
- Make a second copy and store it in a different physical location
- Ink fades — protect the paper from moisture, fire, and environmental damage
- Both hot and cold wallets use the mnemonic phrase standard — it works across compatible software
- Red flag: if a wallet does not provide a mnemonic phrase, be suspicious

### Teaching Tips
This is a practical, hands-on chapter. If possible, demonstrate setting up a wallet live (using a testnet wallet or a demo device). Walk through each "do not" with a story: "Someone took a photo of their seed phrase and their phone was hacked — they lost everything." The key message is simple: treat the mnemonic phrase like cash. Students who are new to Bitcoin often don't realize how irreversible mistakes are — there is no "forgot password" button. Stress that the BTC102 course goes deeper into this setup process.

### Discussion Questions
1. Why is there no "forgot password" or "reset" option in Bitcoin? Is this a feature or a flaw?
2. What is the safest place to store a paper backup of your mnemonic phrase?

### Assignment Ideas
- Practice: Using a testnet wallet, go through the full wallet setup process. Record (on paper) the mnemonic phrase following all the security rules. Then restore the wallet from the phrase to verify it works.

### Quiz Focus
- Use easy-difficulty questions. This is a practical chapter — quiz on the security do's and don'ts.


## Passing the Test of Time

**Estimated time: ~15 minutes**

### Learning Objectives
- Explain why long-term storage of bitcoin requires special considerations beyond a software wallet
- Describe the steel engraving method for durable mnemonic phrase backup
- Outline the key components of a Bitcoin inheritance plan
- Explain why privacy matters for long-term Bitcoin security

### Key Concepts
- Long-term threats to bitcoin storage: loss, theft, and degradation of backups
- Steel engraving: record the mnemonic phrase on a steel plate — resistant to fire and water. Various commercial solutions exist (Blockmit, etc.)
- Inheritance plan: a handwritten letter specifying the nature of assets, how to access them, and trusted contacts. Discuss with an accountant/attorney for tax compliance, but never give them direct access to keys.
- Privacy: buy bitcoin without providing identification when possible; do not discuss your holdings with others; do not share details of your security setup
- Summary of wallet types: mobile/PC (daily), hardware (medium/long term), multisig (corporate/large amounts)
- "Not your keys, not your coins" + "your words = your money" are the two fundamental mantras

### Teaching Tips
This chapter addresses what students rarely think about: what happens to their bitcoin in 10 years? After death? Use the analogy of a treasure map — if you die and nobody can read the map, the treasure is lost forever. The inheritance plan topic can feel uncomfortable, but emphasize that it applies even to young people (accidents happen). Privacy advice should be delivered matter-of-factly: "You wouldn't tell strangers how much money you have in the bank — apply the same rule to bitcoin."

### Discussion Questions
1. If you were hit by a bus tomorrow, could your family access your bitcoin? What would they need?
2. Why might talking about your Bitcoin holdings publicly put you at risk?
3. How would you explain a Bitcoin inheritance plan to a family member who knows nothing about Bitcoin?

### Assignment Ideas
- Draft a simple inheritance plan for your (hypothetical or real) Bitcoin holdings. Include: what assets exist, where the mnemonic phrase is stored, who should be contacted, and how to access the funds.

### Quiz Focus
- Use intermediate-difficulty questions. Focus on backup durability and the components of an inheritance plan.


# Part 4 — The Technical Aspects of Bitcoin

Estimated time for this part: ~100 minutes

This is the most technical part of the course. Go slower, use diagrams and visuals extensively. The goal is not to make students into developers — it is to give them enough technical understanding to feel confident about why Bitcoin works. The 4-step transaction lifecycle and the proof-of-work explanation are the two anchors of this part.

## Launching Bitcoin

**Estimated time: ~15 minutes**

### Learning Objectives
- State the key dates in Bitcoin's early history (Oct 31 2008, Jan 3 2009, Jan 12 2009, May 22 2010)
- Explain the significance of the Genesis block's embedded message
- Describe the roles of Satoshi Nakamoto and Hal Finney in Bitcoin's launch
- Explain why Satoshi's disappearance actually strengthened Bitcoin

### Key Concepts
- October 31, 2008: Satoshi Nakamoto publishes the Bitcoin whitepaper on the cypherpunk mailing list
- January 3, 2009: Genesis block created. Embedded message: "Chancellor on brink of second bailout for banks" — a commentary on the financial system
- January 9, 2009: Bitcoin 0.1.0 released. Hal Finney joins as the second node/miner. "Running Bitcoin" tweet.
- January 12, 2009: First Bitcoin transaction — 10 BTC from Satoshi to Hal Finney (block 170)
- November 22, 2009: BitcoinTalk forum created — birthplace of Bitcoin culture (Hodl, Bitcoin logo, Pizza Day)
- May 22, 2010 (Pizza Day): Laszlo Hanyecz buys 2 pizzas for 10,000 BTC — first physical goods purchase with Bitcoin
- 2010-2011: Satoshi gradually withdraws, last known communication April 23, 2011
- Bitcoin's 99.988% uptime since launch — it has run continuously despite Satoshi's absence
- Satoshi's departure removed a single point of failure — Bitcoin became truly decentralized

### Teaching Tips
Tell this as a narrative — a story with characters (Satoshi, Hal Finney, Laszlo). The Genesis block message is a dramatic hook: "The very first block in Bitcoin's history contains a newspaper headline about bank bailouts. That's not a coincidence." Pizza Day is always a crowd favorite — 10,000 BTC for 2 pizzas is viscerally memorable. The key lesson from Satoshi's disappearance: Bitcoin doesn't need a leader. This is what makes it fundamentally different from companies or other crypto projects.

### Discussion Questions
1. Why did Satoshi embed a newspaper headline in the Genesis block? What was the message?
2. 10,000 BTC for 2 pizzas — was Laszlo foolish, or was this an important moment for Bitcoin? Why?
3. Why is it significant that Bitcoin continued to work perfectly after its creator disappeared?

### Assignment Ideas
- Read the abstract of the Bitcoin whitepaper (just the first paragraph). Summarize in your own words what problem Satoshi was trying to solve.

### Quiz Focus
- Use easy and intermediate questions. Focus on key dates, figures, and the significance of early events.


## Bitcoin Transactions

**Estimated time: ~25 minutes**

### Learning Objectives
- Describe the 4 steps of a Bitcoin transaction (create → propagate → mine → verify)
- Explain the role of transaction fees and why they exist
- Define the mempool and its function
- Explain why 6 confirmations is the standard for considering a transaction immutable
- Articulate why no trusted third party is needed in a Bitcoin transaction

### Key Concepts
- Step 1 — Create: Alice provides Bob her address (like a Bitcoin IBAN). Bob creates a transaction in his wallet, sets the amount and fee, and signs it with his private key.
- Step 2 — Propagate: Bob's wallet broadcasts the transaction to a node, which relays it to the entire network. The transaction is now in the mempool (waiting room).
- Step 3 — Mine: A miner bundles the transaction into a block, solves the proof-of-work puzzle, and adds the block to the blockchain.
- Step 4 — Verify: Alice's node receives the new block and confirms the transaction. After 6 additional blocks are mined on top, the transaction is considered immutable.
- Fees create a free market: block space is limited (~1MB, expanded to ~4MB with SegWit), so users compete for inclusion by offering fees. Higher fee = faster confirmation.
- Transaction size depends on complexity, not on the bitcoin amount being sent
- The entire process is decentralized and trustless — no bank or intermediary involved
- Users control the system through nodes; miners hold limited power

### Teaching Tips
The 4-step model is the backbone of this chapter — draw it as a flow diagram. For each step, use the Alice and Bob example from the course. The mempool concept often confuses students: explain it as a "waiting room" where transactions sit until a miner picks them up. The fee market is a crucial concept — use the analogy of a busy highway with a toll: "Pay more, get in the fast lane." Emphasize that a transaction isn't truly "done" until 6 confirmations. If you have access to a block explorer (mempool.space), do a quick live demo showing a pending transaction.

### Discussion Questions
1. Why does Bitcoin need fees? What would happen if transactions were free?
2. If no single entity controls Bitcoin transactions, how can we be sure they are valid?
3. Why is it recommended to wait for 6 confirmations before considering a transaction final?

### Assignment Ideas
- **Live exercise**: Visit mempool.space and find a recent transaction. Identify: the sender address, receiver address, fee paid, and number of confirmations.
- Draw the 4-step transaction process from memory with a brief description of each step.

### Quiz Focus
- Use intermediate and hard questions. This is a core technical chapter — quiz on the transaction lifecycle, the role of fees, and the mempool.


## Bitcoin Nodes

**Estimated time: ~20 minutes**

### Learning Objectives
- List the 4 main functions of a Bitcoin node (store blockchain, validate transactions, transmit information, enforce rules)
- Explain why nodes are essential for decentralization
- Describe the trade-off between block size and network decentralization
- Summarize the 2017 "block size war" and its outcome (SegWit + Lightning)

### Key Concepts
- A node = any device running Bitcoin software (typically Bitcoin Core)
- 4 functions: maintain blockchain copy, validate transactions, relay information, enforce consensus rules
- ~45,000 nodes worldwide — to stop Bitcoin, all would need to be shut down simultaneously
- Nodes are the "legal system" of Bitcoin — they enforce the rules. Miners propose, nodes verify.
- Running a node is cheap by design: ~500GB storage, ~5GB/month bandwidth, Raspberry Pi hardware is sufficient
- This affordability is deliberate: if nodes were expensive, only large institutions could run them → centralization
- The block size war (2017): big-blockers (miners, exchanges) wanted larger blocks for more transactions vs. small-blockers (nodes, users) who wanted to preserve decentralization
- Small-blockers won → SegWit activated → paved the way for the Lightning Network
- Key insight: users, through nodes, hold the real power in Bitcoin — not miners

### Teaching Tips
Students often wonder "why would I run a node?" Answer: because it's the only way to verify for yourself that the rules are being followed. The block size war is a fascinating case study in governance — present it as a political struggle within Bitcoin. The outcome (users won over corporations) demonstrates that Bitcoin is truly governed by its users. If possible, show a photo of a Raspberry Pi node setup — it makes "anyone can run a node" tangible. The 100x block size thought experiment is a great way to illustrate the decentralization trade-off.

### Discussion Questions
1. If running a node cost $10,000/year instead of $10/year, how would that change Bitcoin?
2. During the block size war, miners and exchanges wanted bigger blocks. Users and nodes disagreed. Who should have more power, and why?
3. What does "Don't trust, verify" mean in the context of running a Bitcoin node?

### Assignment Ideas
- Research the block size war of 2017. Write a short summary: What were the two sides? What was at stake? What was the outcome?
- Calculate: If blocks were 100MB instead of 1MB, how large would the full blockchain be today (assuming ~800,000 blocks)?

### Quiz Focus
- Use intermediate and hard questions. Focus on node functions, the decentralization argument, and the block size war.


## Miners

**Estimated time: ~25 minutes**

### Learning Objectives
- Explain the Proof of Work mechanism and why it exists
- Describe how miners are compensated (block subsidy + transaction fees)
- Explain the mining difficulty adjustment and its 2-week cycle
- Trace the evolution of mining hardware (CPU → GPU → ASIC)
- Describe how Bitcoin solves the Byzantine Generals Problem

### Key Concepts
- Proof of Work = a "universal lottery" where miners compete to find a valid hash (SHA-256) for the next block
- The hash must meet a difficulty target — finding it is hard, verifying it is easy (asymmetry is key)
- ASICs (Application-Specific Integrated Circuits): specialized machines that only compute SHA-256 hashes, billions per second
- PoW transforms energy into currency — connecting the physical world to the digital world
- Mining reward = block subsidy (newly minted BTC) + transaction fees from included transactions
- Block subsidy started at 50 BTC, currently 3.125 BTC (halves every ~4 years)
- Difficulty adjustment every 2,016 blocks: if blocks are found too fast, difficulty increases; too slow, it decreases
- Mining pools: miners combine resources to get smaller but more regular payouts
- Byzantine Generals Problem: how to coordinate without trust. Bitcoin solves it through PoW — it is more profitable to follow the rules than to cheat.
- 51% attack: theoretically possible but economically irrational — attacker must spend more energy than all honest miners combined
- The coinbase transaction is always the first in a block — it is the miner's reward

### Teaching Tips
The lottery analogy is the best way to explain PoW: "Imagine everyone in the world is rolling dice trying to get a specific number. The first person to roll it wins a prize, and then a new round starts." ASICs are impressive — mention that the global hashrate exceeds 500 TH/s (500,000 billion attempts per second). The Byzantine Generals Problem is where game theory meets computer science — tell it as a story. Students often ask "isn't mining wasteful?" — address this head-on but save the deep ecology discussion for the next chapter. The key insight: the energy cost is what makes Bitcoin secure. Without it, there is no security.

### Discussion Questions
1. Why can't Bitcoin use a more "energy-efficient" consensus mechanism like Proof of Stake? What would change?
2. If you were a miner, would you mine solo or join a pool? Why?
3. Explain in your own words how Proof of Work solves the "trust" problem between strangers on the internet.

### Assignment Ideas
- **Research**: Find the current Bitcoin hashrate and difficulty level on a site like blockchain.com. How has the hashrate changed over the past year?
- **Thought exercise**: Explain the Byzantine Generals Problem to someone who has never heard of Bitcoin, and then explain how Bitcoin solves it.

### Quiz Focus
- Use intermediate and hard questions. This is one of the most technically demanding chapters — focus on PoW mechanics, the difficulty adjustment, and miner incentives.


## Bitcoin and Ecology

**Estimated time: ~15 minutes**

### Learning Objectives
- Articulate the main criticisms about Bitcoin's energy consumption and the counterarguments
- Explain why miners tend to use cheap, often renewable, energy sources
- Describe how Bitcoin mining can be a "buyer of last resort" for stranded energy
- Compare Bitcoin's energy use to the current financial system's environmental footprint
- Distinguish between Keynesian and Austrian economic perspectives on consumption and sustainability

### Key Concepts
- Bitcoin mining consumes significant electricity — this is by design (PoW security)
- But: the energy cost cannot be evaluated "per transaction" — miners secure the entire network and all past transactions
- Miners seek the cheapest electricity → often stranded, renewable, or surplus energy (hydroelectric, geothermal, flared gas)
- Example: methane flaring at oil wells can be converted to electricity for mining — turning a pollutant into a productive use
- Bitcoin mining as a "last resort buyer": incentivizes building power plants in remote areas before grid connection
- The current financial system also has enormous energy and environmental costs (data centers, bank branches, armored transport, printing, etc.)
- Austrian economics perspective: sound money (fixed supply) → less overconsumption → better long-term sustainability
- Keynesian economics: encourages consumption and debt → environmental degradation over time
- Bitcoin = long-term thinking vs. fiat = short-term consumption incentives

### Teaching Tips
This is a debate-heavy chapter — lean into it. Present both sides fairly: "Critics say Bitcoin uses as much energy as a small country. Advocates say the comparison is misleading." The key nuance: Bitcoin's energy consumption is the cost of decentralized security — compare it to the cost of the entire banking system, not to a single payment. The methane flaring example is compelling and concrete. The Austrian vs. Keynesian framing is intellectually rich but may be new to students — keep it accessible. End with: "Don't trust, verify for yourself!"

### Discussion Questions
1. "Bitcoin wastes energy." Do you agree or disagree? How would you respond to this claim?
2. Is it fair to compare Bitcoin's energy use to Visa's energy per transaction? Why or why not?
3. How might a currency with a fixed supply change consumption patterns compared to an inflationary currency?

### Assignment Ideas
- Find a recent article (2024 or later) about Bitcoin's energy consumption. Summarize the main argument and evaluate whether the author considered the counterarguments discussed in class.

### Quiz Focus
- Use intermediate-difficulty questions. Focus on the energy debate arguments and the miner incentive to seek cheap energy.


# Part 5 — How Do You Obtain Bitcoin?

Estimated time for this part: ~70 minutes

This part is practical. Students move from "understanding Bitcoin" to "using Bitcoin." Cover volatility honestly, present the different acquisition methods, and emphasize risk awareness. DCA (Dollar Cost Averaging) is the key strategy concept to convey.

## Bitcoin Never Sleeps!

**Estimated time: ~15 minutes**

### Learning Objectives
- Explain why Bitcoin's price is volatile and how volatility has changed over time
- Identify the main adoption waves in Bitcoin's history (technophiles, dark web, ICOs, NFTs/DeFi, institutional)
- Describe the relationship between halving cycles and market cycles
- Explain why Bitcoin's volatility does not affect the protocol itself

### Key Concepts
- Bitcoin is volatile — prices can swing 10-50% in days. This is normal for an emerging asset class.
- Adoption waves: (1) cypherpunks/technophiles, (2) dark web/Silk Road, (3) ICO frenzy 2017, (4) NFT/DeFi bubble 2020, (5) institutional adoption (ETFs, corporate treasuries)
- Each wave brings new users, but also speculative bubbles and corrections
- Halving cycles (~4 years) correlate with market cycles: reduced supply → price pressure → euphoria → correction
- The protocol doesn't care about price: Bitcoin works exactly the same at $1 or $100,000
- Bitcoin is unique: repeated "bubbles" that don't kill it — because it's a functioning global currency, not just speculation
- As Bitcoin matures and grows, volatility is expected to decrease over time
- Market operates 24/7/365 — no market hours, no holidays

### Teaching Tips
Students are often scared of volatility. Normalize it: "Bitcoin's price went from $1 to $100,000 with many 80% drops along the way." The adoption S-curve is a useful framework — place the class on the curve and ask: "Where do you think we are?" The halving-cycle correlation is interesting but should be presented as an observation, not a guaranteed pattern. Remind students that using the word "bubble" for something that keeps coming back stronger each time is a misuse of the term.

### Discussion Questions
1. If Bitcoin drops 50% tomorrow, does that mean it failed? Why or why not?
2. Where on the technology adoption S-curve do you think Bitcoin is today? Why?
3. Is Bitcoin's volatility a bug or a feature? Does volatility serve any useful purpose?

### Assignment Ideas
- Look at Bitcoin's price chart over the past 10 years. Identify 3 major drops (>40%). For each, write one sentence explaining what caused it and whether Bitcoin recovered.

### Quiz Focus
- Use easy and intermediate questions. Focus on adoption waves and the halving-cycle relationship.


## Obtaining Bitcoins by Working

**Estimated time: ~20 minutes**

### Learning Objectives
- Describe how a parallel Bitcoin economy is developing (merchants, services, peer-to-peer)
- Explain the advantages of earning bitcoin directly vs. buying on an exchange
- List practical solutions for merchants to accept Bitcoin (OpenNode, Swiss Bitcoin Pay, BTCPay Server)
- Discuss El Salvador's Bitcoin legal tender experiment and its evolution

### Key Concepts
- Bitcoin enables a parallel economy: sell goods/services and get paid in bitcoin, wallet to wallet
- El Salvador made Bitcoin legal tender in 2021; in 2025, it was downgraded (IMF pressure) — acceptance is now voluntary
- BTCMap.org: open-source map of all businesses accepting Bitcoin worldwide
- Advantages of earning bitcoin (vs. buying): censorship resistance, reduced fees, no exchange needed, dollar-cost averaging through work
- Merchant solutions by business size: OpenNode (simple online), Swiss Bitcoin Pay (small businesses), BTCPay Server (large organizations/enthusiasts)
- Earning bitcoin = acquiring without worrying about market timing

### Teaching Tips
This chapter makes Bitcoin tangible. If BTCMap works in your region, show it live — students seeing local businesses that accept Bitcoin is powerful. The El Salvador story is evolving — present it objectively (bold experiment, political complexity, IMF dynamics). For merchant acceptance, explain that it's getting easier every year. A common question: "But who pays in bitcoin if the price might go up?" Answer: circular economies and people who earn in bitcoin spend in bitcoin.

### Discussion Questions
1. If you ran a small business, would you accept Bitcoin? What would concern you?
2. What are the pros and cons of earning Bitcoin through work vs. buying it on an exchange?
3. Why did the IMF push back on El Salvador's Bitcoin legal tender law?

### Assignment Ideas
- Visit BTCMap.org and find 3 businesses near you (or in your country) that accept Bitcoin. What types of businesses are they?
- Research one country where Bitcoin has become important for everyday commerce. Write 200 words about how and why.

### Quiz Focus
- Use easy and intermediate questions. Focus on merchant acceptance methods and the advantages of earning vs. buying.


## Saving with Bitcoin

**Estimated time: ~20 minutes**

### Learning Objectives
- Explain the Dollar Cost Averaging (DCA) strategy and its advantages
- Distinguish between DCA and spontaneous (lump-sum) purchases
- Define KYC (Know Your Customer) and explain its implications for Bitcoin buyers
- List the main types of Bitcoin acquisition platforms (DCA platforms, brokers, peer-to-peer, ATMs)
- Explain what a UTXO is and why consolidation matters

### Key Concepts
- Warning: only invest what you can afford to lose. Bitcoin is volatile. Past performance is not a guarantee.
- Checklist before buying: secure wallet, solid understanding, savings plan, long-term vision
- DCA (Dollar Cost Averaging): buy small amounts at regular intervals → smooths out volatility, ideal for long-term savings
- Spontaneous purchase: all-at-once buy to gain immediate exposure. Requires emotional discipline (avoid FOMO/FUD).
- UTXO management: frequent small DCA purchases create many small UTXOs. Periodically consolidate to reduce future transaction fees.
- Platform types: DCA platforms (auto-recurring), broker platforms (Kraken, Bitstamp — large amounts, KYC required), peer-to-peer/non-KYC solutions
- KYC: identity verification required by regulated platforms. Debate: anti-money-laundering vs. privacy concerns.
- Non-KYC options: Bitcoin ATMs, peer-to-peer exchanges, physical meetups
- Always withdraw bitcoin from exchanges to your own wallet after purchase
- Tax obligations vary by jurisdiction — consult local regulations

### Teaching Tips
DCA is the most practical takeaway for most students. Explain it simply: "Buy $50 of bitcoin every week, no matter the price. In 5 years, you'll have accumulated steadily without stressing about timing." Contrast with the emotional rollercoaster of trying to "buy the dip." The UTXO consolidation concept is often new — explain it as: "Imagine having 100 envelopes with $1 each vs. 1 envelope with $100. Spending is cheaper with the single envelope." KYC is a controversial topic — present both sides neutrally. Remind students: "Not your keys, not your coins" applies to exchanges too.

### Discussion Questions
1. Why is DCA often recommended for beginners over lump-sum purchases?
2. What are the trade-offs between using a KYC platform vs. a non-KYC solution?
3. Why is it important to withdraw your bitcoin from an exchange to your own wallet?

### Assignment Ideas
- **DCA simulation**: If you had invested $50/week in Bitcoin for the past 2 years, how much would you have today? Use a DCA calculator (like dcabtc.com) and report the results.
- Write a 1-paragraph explanation of KYC for a friend who asks: "Why do they need my ID to buy bitcoin?"

### Quiz Focus
- Use easy and intermediate questions. Focus on DCA mechanics, the KYC distinction, and the importance of self-custody.


## Hyper-bitcoinization

**Estimated time: ~15 minutes**

### Learning Objectives
- Define hyper-bitcoinization and place it within the technology adoption S-curve
- Identify the multidisciplinary impact of Bitcoin (economics, law, cryptography, philosophy, energy, politics)
- Articulate the argument that we are still early in Bitcoin adoption
- Describe the vision of a Bitcoin-based future and its societal implications

### Key Concepts
- Bitcoin adoption follows an S-curve: early adopters → takeoff → mass adoption → saturation
- We have passed the early adopter phase but are still in the early majority phase — "you are just in time"
- Bitcoin forces companies, universities, regulators, and individuals to adapt
- Bitcoin is multidisciplinary: it touches cryptography, game theory, economics, computer science, philosophy, energy, law, and regulation
- The rise of Bitcoin means new tools, services, and regulations must be created
- Vision: a world where human sovereignty is a right, privacy is respected, and money is not manipulated
- Milton Friedman (1999): predicted "reliable e-cash" that enables anonymous online transfers

### Teaching Tips
This is a forward-looking, visionary chapter. Let it breathe — this is where students project themselves into the future. The S-curve graphic is key: "Where are we? Where might we be in 10 years?" Be honest about uncertainties while conveying the magnitude of the shift. The Friedman quote from 1999 is remarkable because it predates Bitcoin by 10 years — use it to show that the idea was anticipated by mainstream economists. End with: "Bitcoin is a 0 to 1 — a fundamentally new thing. Take your time understanding it."

### Discussion Questions
1. Where on the adoption S-curve do you think Bitcoin is today? What evidence supports your answer?
2. If Bitcoin becomes the global standard for savings, how would everyday life change?
3. Bitcoin touches economics, law, technology, energy, philosophy... Which field do you find most interesting in relation to Bitcoin?

### Assignment Ideas
- Write a 200-word "letter from the future" (the year 2040) describing how Bitcoin is used in daily life. Be specific: how do people pay? How do they save? What changed?

### Quiz Focus
- Use intermediate and hard questions. Focus on the adoption curve concept and the multidisciplinary nature of Bitcoin.


# Part 6 — The Future of Bitcoin

Estimated time for this part: ~50 minutes

This final part looks forward. Lightning Network is the most practically important topic — ensure students understand the "layered" approach. The last two chapters are broader in scope and more philosophical. End the course on an empowering note.

## The Lightning Network

**Estimated time: ~25 minutes**

### Learning Objectives
- Explain why the Bitcoin base layer cannot handle unlimited transactions (the blockchain trilemma)
- Describe how the Lightning Network works as a second layer (payment channels, off-chain transactions)
- Explain the concept of payment routing through a network of channels
- Distinguish between custodial and non-custodial Lightning wallets
- List concrete use cases enabled by Lightning (micropayments, streaming money, everyday payments)

### Key Concepts
- The blockchain trilemma: decentralization, security, scalability — Bitcoin prioritizes the first two
- Bitcoin base layer: ~1MB blocks every ~10 min = limited to a few thousand transactions per block
- This is deliberate: small blocks keep nodes cheap → decentralization preserved
- Lightning Network = a fast payment layer built on top of Bitcoin
- Payment channels: two parties lock funds in a shared onchain transaction, then exchange sats offchain (instant, nearly free)
- Opening and closing channels are onchain transactions; everything in between is offchain
- Network of channels: pay anyone through a path of connected channels (routing, hop by hop)
- Liquidity: a channel's capacity and the direction sats can flow determine whether a payment can route
- HTLCs (Hashed Time-Locked Contracts): trustless payments through intermediaries — either the payment completes entirely, or it fails entirely (atomic)
- Penalty mechanism: if someone tries to cheat by broadcasting an old state, they lose all funds in the channel
- Custodial wallets (balance held by a service) vs. non-custodial wallets (you hold keys — Phoenix, Zeus)
- Use cases: everyday payments, micropayments, streaming money, content creator tips, gaming
- Main implementations: LND, Core Lightning, Eclair, LDK

### Teaching Tips
The layered architecture analogy works well: "Bitcoin is the foundation (concrete, slow, extremely strong). Lightning is the highway built on top (fast, efficient, designed for daily traffic)." Many students initially think Lightning "replaces" Bitcoin — clarify that it complements it. Payment channels can be explained with the "bar tab" analogy: you open a tab (open channel), run up charges over the evening (offchain payments), and settle at the end of the night (close channel). The atomic payment property is important: "Either the whole payment goes through, or nothing moves — you can't lose money in transit."

### Discussion Questions
1. Why didn't Bitcoin simply increase block size instead of building Lightning? What trade-off would that involve?
2. What types of transactions make more sense on Lightning vs. on the base layer?
3. Would you trust a custodial Lightning wallet for small amounts? What about for your savings?

### Assignment Ideas
- Download a Lightning wallet (Phoenix or Zeus on testnet/mainnet with a small amount) and make a payment. Describe the experience — how fast was it? What did you notice compared to an onchain transaction?
- Research one Lightning use case (podcasting 2.0, gaming, tipping) and describe how it works.

### Quiz Focus
- Use intermediate and hard questions. Focus on the layered architecture, payment channels, and the difference between custodial and non-custodial Lightning.


## Beyond Lightning: Other Protocols to Scale Bitcoin

**Estimated time: ~15 minutes**

### Learning Objectives
- Explain the layered approach to Bitcoin scaling (base layer + multiple upper layers)
- Describe what a sidechain is and give an example (Liquid)
- Summarize Ark, RGB, and Taproot Assets at a high level
- Explain why Bitcoin's base layer is deliberately conservative while upper layers innovate

### Key Concepts
- Bitcoin's scaling philosophy: a conservative base layer + experimental upper layers — each making different trade-offs
- Sidechains: separate blockchains connected to Bitcoin via a two-way peg. Example: Liquid (Blockstream) — faster settlements, asset issuance, enhanced privacy, but trust a federation instead of PoW
- Ark: groups many user operations into few onchain transactions. No inbound liquidity needed (unlike Lightning). Privacy close to coinjoin. Still young/experimental.
- RGB: smart contracts and assets on Bitcoin using client-side validation. Data stays offchain between relevant parties; blockchain just anchors commitments. Scalable and private, but requires careful data management.
- Taproot Assets: protocol by Lightning Labs for issuing assets (stablecoins, tokens) on Bitcoin and transferring them via Lightning
- Key insight: Bitcoin is not "frozen" — it evolves through layers without compromising the base layer's security and decentralization

### Teaching Tips
This chapter is a high-level overview — don't try to make students experts on each protocol. The key takeaway is the *philosophy*: "Keep the base layer simple and secure; let upper layers experiment." Use the analogy of a building: the foundation (Bitcoin) never changes, but you can add floors on top (Lightning, Liquid, Ark, RGB). Each protocol makes different trade-offs — present this as a strength, not a weakness. Liquid's federation model is a good comparison point: "It's faster, but you trust a group of companies instead of trusting math."

### Discussion Questions
1. Why is it important that Bitcoin's base layer stays conservative and changes slowly?
2. What is the main trade-off that Liquid makes compared to Bitcoin's base layer?
3. If you could build one application on RGB or Taproot Assets, what would it be?

### Assignment Ideas
- Create a one-page comparison table of: Bitcoin base layer, Lightning Network, Liquid, Ark, and RGB. For each, note: speed, privacy level, trust model, and maturity level.

### Quiz Focus
- Use easy and intermediate questions. Focus on the layered concept and the basic description of each protocol.


## Red Pill or Blue Pill?

**Estimated time: ~10 minutes**

### Learning Objectives
- Reflect on the broader societal implications of Bitcoin (financial freedom, censorship resistance, inclusivity)
- Articulate the connection between technology, money, and individual sovereignty
- Consider the open questions Bitcoin raises about the future of work, governance, and freedom

### Key Concepts
- The Matrix reference: Bitcoin is a choice — once you understand it, you see the financial system differently
- AI and automation: 80%+ of jobs may be displaced — how we organize money matters enormously for the post-automation world
- Key questions: Who controls money? Is currency private property? Can accounts be frozen without due process? Who guarantees the financial system?
- Bitcoin properties: divisible, instantly transportable, uncensorable, negligible verification cost, fixed supply (21M)
- 2.4 billion people worldwide have no bank account — Bitcoin offers equality of access regardless of social status or geography
- Bitcoin is apolitical: no privileges for leaders or influencers — same rules for everyone
- The censorship question: who decides what is censored? Financial censorship = cutting someone off from the economy
- Bitcoin is a peaceful revolution — changing the monetary system from the bottom up
- "Don't Trust, Verify" — the course's ultimate takeaway

### Teaching Tips
This is the closing chapter — make it personal and reflective. The Matrix analogy resonates: "Now that you've seen how money really works, you can't unsee it." Don't be prescriptive about what students should believe — pose the questions and let them think. The stat about 2.4 billion unbanked people brings Bitcoin out of the Western tech bubble and into a global human rights context. End on an empowering note: "You now understand something that 99% of the world doesn't. What you do with that knowledge is up to you."

### Discussion Questions
1. After this course, has your view of money changed? How?
2. "Bitcoin is for everyone" — but is it equally accessible? What barriers still exist?
3. If you could explain one thing about Bitcoin to a policymaker, what would it be?

### Assignment Ideas
- **Final reflection**: Write 300 words on: "What is the most important thing I learned in this course, and how does it change my understanding of money?"
- **Challenge**: Explain Bitcoin to a friend or family member in under 2 minutes. Report back: What questions did they ask? What was hardest to explain?

### Quiz Focus
- Use intermediate and hard questions. Focus on the societal and philosophical dimensions — financial sovereignty, censorship resistance, and global access.
