---
name: Mastering Liquid Development
goal: Build applications on Liquid using developer tools, Liquid Script, and the Simplicity smart contract language
objectives:
  - Understand the UTXO-based Liquid model versus EVM account-based approaches
  - Master Liquid Script opcodes and covenant capabilities for advanced transactions
  - Develop wallets and implement atomic swaps using LWK and native protocols
  - Write, test, and deploy smart contracts using Simplicity and SimplicityHL
---

# Your path to Liquid Application Development

In this course, you will learn how to build applications on the Liquid Network from the ground up. We start with the mental model shift from EVM-style development to Liquid's UTXO-based approach, then dive deep into Liquid Script opcodes and covenant capabilities that enable advanced transaction types.

This is an advanced developer course designed for programmers who want to build on Bitcoin sidechains. You will work with the Liquid Wallet Kit (LWK), implement native and cross-chain swaps using protocols like LiquiDex and Boltz, and ultimately learn Simplicity—the next-generation smart contract language designed for formal verification and security. By the end, you will be equipped to architect and deploy secure decentralized applications on Liquid.

+++

# Introduction to Liquid and Elements
<partId>e2e76d70-2bde-4190-8ed1-17ee1a337bb5</partId>

## Overview of Liquid Architecture and Governance Model
<chapterId>17650c4b-cd1f-4bc6-b490-708f92dc9306</chapterId>

![video](https://www.youtube.com/watch?v=d0TmI19Lkc8)

### Liquid Network Governance and Architecture

The Liquid Network represents a federated sidechain solution built on top of Bitcoin, designed to extend Bitcoin's capabilities while maintaining a close relationship with its source code and operational principles. Before diving into the technical details, it is essential to understand the relationship between Blockstream and the Liquid Federation, as this is often misunderstood. Blockstream serves as the technical provider for the Liquid Federation, supplying software and hardware, but does not have direct access to or control over the Liquid Network itself. Each operator of the federation maintains their own independent access to their functionality, creating a separation between the technology provider and the network operators.

The Liquid Network runs on Elements, which is essentially Bitcoin Core with specific extensions. The codebases are so closely related that Elements can synchronize a Bitcoin node up until the Taproot activation in November 2021. The slight differences that prevent full synchronization beyond that point stem from Taproot being developed first in Liquid before being ported to Bitcoin, resulting in minor variations like different exact opcodes. Approximately 80 to 90 percent of the Elements code comes directly from Bitcoin Core, making it a true extension rather than a separate implementation. This close relationship serves an important purpose: Liquid acts as a testing ground for new Bitcoin technologies, with both Segwit and Taproot being analyzed within Elements before their Bitcoin deployment.

The federation operates through a consensus mechanism requiring 11 out of 15 signatures for block validity. Block production follows a round-robin system where every minute, one of the 15 functionaries proposes a block, the remaining functionaries validate and sign it, and then everyone combines the signatures to add the block to the chain. If one functionary is unavailable during their turn, that round is simply skipped, and the next functionary continues the process. This built-in redundancy means the network can tolerate temporary outages without significant disruption, as handling such situations is part of the network's designed resilience.

### Confidential Transactions and Asset Issuance

One of the most significant features distinguishing Liquid from Bitcoin is native asset issuance. Users can issue their own assets within the network without requiring smart contracts or specialized programming tools. The network handles all protocols and transactions natively, meaning every wallet that supports one asset can support any asset without additional development. This native handling is particularly valuable for financial applications and securities because it eliminates the need to audit smart contracts for each new asset, addressing one of the major pain points in EVM-based chains where constant auditing still fails to prevent theft.

Confidential transactions represent another cornerstone feature of the Liquid Network. When sending a transaction, observers can only see the UTXOs, sources, and destinations, similar to Bitcoin. However, both the asset type and the amount remain hidden from outside observers. This means a transaction swapping 10 Bitcoin for USDT appears identical to a simple payment between friends. The privacy implications extend beyond personal financial privacy to trading advantages, as no one can front-run transactions or determine address balances. This confidentiality was initially more expensive due to larger transaction sizes, roughly ten times bigger than non-confidential transactions. Recent protocol improvements through the Elements Improvement Proposal process have implemented discount CT, ensuring confidential and non-confidential transactions now cost exactly the same, removing any financial incentive to sacrifice privacy.

The peg-in process allows users to bring Bitcoin into the Liquid Network. Users receive a pegging address, send their Bitcoin to that address, and after 102 blocks can claim the equivalent LBTC within Liquid. The 102-block requirement mirrors the same number of confirmations Bitcoin miners must wait before spending their mining rewards, following the principle that if this security measure is sufficient for miners, it is sufficient for the federation. The peg-out process is more restricted, limited to federation members only, as a security measure against potential unknown vulnerabilities. Regular users can still convert LBTC back to Bitcoin through atomic trustless swaps offered by various companies, often faster than a direct peg-out since these typically occur via Lightning.

### Federation Structure and Security Model

The Liquid Federation comprises several distinct roles with different capabilities. Wallet users can create transactions but cannot verify them independently since they typically use thin clients connecting to block explorers. Node operators run Elements nodes and continuously validate the chain. Federation members form a superset of the 15 functionaries and participate in governance decisions while also having the ability to perform actual peg-outs. Functionary operators run the specialized hardware called HSMs that handle the cryptographic keys for both block signing and the Bitcoin wallet controlling pegged funds.

A common criticism of Liquid suggests that operators could simply extract keys and act maliciously. However, the keys are held within Hardware Security Modules that prevent direct access even with physical possession of the device. While nothing can be declared absolutely impossible, extracting keys from an HSM is extraordinarily difficult and would not go unnoticed. The security model ensures that even if some operators became malicious, they would still lack the ability to access the keys directly. Blockstream deliberately makes its own operations more difficult by maintaining this separation, choosing to do things correctly rather than conveniently.

The federation governance operates through three boards: the membership board deciding who can join, the oversight board handling internal controls and decision-making processes, and the technology board working closely with Blockstream on technical features. Changes to the network protocol follow the Elements Improvement Proposal process, modeled after Bitcoin's BIP system. This structured approach ensures transparency and community input on network modifications while maintaining the stability that financial applications require.

### Block Finality and Emergency Recovery

Liquid provides two-minute transaction finality, meaning once a block has one confirmation on top of it, the transaction can never be replaced or reorganized. Only the topmost block can theoretically be replaced by another block at the same height, though in over three million blocks this has never occurred. This finality guarantee stems from the HSM security model, where each device will never sign a block below the last block it has signed. The federation cannot collude to change this rule because doing so would require modifying the HSM itself, which presents the same level of difficulty as extracting the keys entirely.

The Bitcoin wallet holding pegged funds operates on an 11 out of 15 multisignature scheme with an important addition: after 4,032 blocks, approximately four weeks, the UTXOs become spendable by emergency keys through a two out of three signature. This contingency plan ensures that if a catastrophic event rendered the network unable to produce blocks, the nearly 3,800 Bitcoin currently on the network could be recovered and returned to their owners. However, this emergency mechanism requires constant maintenance, as the federation must continuously sweep these UTXOs on the Bitcoin side regardless of fee rates to prevent them from ever becoming spendable by the emergency keys. The fees collected on Liquid, currently around three and a half Bitcoin after spending on Bitcoin-side transactions, primarily fund this sweeping process rather than generating profit for any party.

## Overview of the Liquid Ecosystem and Use Cases
<chapterId>f38b612c-358b-4008-89b0-c10296beed86</chapterId>

**No video -- TBD**

# Liquid vs EVM Mental Models
<partId>25f5d368-f564-4023-8102-ae48e8b5c6f4</partId>

## UTXO vs ABM, Liquid vs EVM, Native Functionality
<chapterId>4af39f93-be2a-4e6d-9804-7007be46bccd</chapterId>

![video](https://www.youtube.com/watch?v=8Q1JPKvp7TE)

# Liquid Script & Covenant Opcodes
<partId>543358ad-f8dc-421e-a7ef-c3ca739941b3</partId>

## Bitcoin Script vs Liquid Script, Demo
<chapterId>40852b20-591b-442f-b1f8-10b5147e5da0</chapterId>

**No video -- TBD**

## Comprehensive Deep Dive into Available Opcodes, Use Cases, Example Code Walkthrough
<chapterId>a78be043-ac6b-4f27-bc71-b8198de7cf52</chapterId>

**No video -- TBD**

# Overview of Developer Tools
<partId>4196370f-1e62-4515-af76-8a1430e9a603</partId>

## Overview of Liquid Dev Tooling: LWK, GDK, Swap Protocols, Simplicity, etc.
<chapterId>1a8fc4a3-a0ea-4cff-b1c1-5715aab1fbdd</chapterId>

**No video -- TBD**

## Environment Setup, Nigiri, Demo and Other Tooling to Get Started
<chapterId>0b028459-3b98-486f-be3c-e55f8ba90593</chapterId>

**No video -- TBD**

# Liquid Wallet Kit (LWK)
<partId>481107ee-bf8b-4b21-8578-25762869556f</partId>

## Liquid Wallet Tools Overview (GDK), LWK Intro
<chapterId>a59b7eb2-71b1-4149-bf27-8f3bda1f4049</chapterId>

![video](https://www.youtube.com/watch?v=a3MPR3-5xy0)

## LWK Walk-through Demo, Cargo Install, CLI, liquidwebwallet.org
<chapterId>5ee78e63-5ff2-4fc7-8d00-f2192d15f6a9</chapterId>

**No video -- TBD**

# Native and Cross-chain Liquid Swaps
<partId>c8918dad-0606-47b2-9436-ace981c2575f</partId>

## Native Liquid Swaps & the LiquiDex Protocol
<chapterId>33efe303-7a94-468a-8665-15c3fddfdba9</chapterId>

![video](https://www.youtube.com/watch?v=miMz-5gF6qM&t=774s)

## Cross-chain Swaps, Boltz, HTLCs via Liquid Script, Atomic Swaps, Tapscript Opcodes
<chapterId>3d382f25-d917-4128-b524-5d228ca9a359</chapterId>

![video](https://www.youtube.com/watch?v=7D3jKD-ynnA)

## EVM vs Elements (Solidity vs Simplicity)
<chapterId>b60a18d9-2b39-4346-bcbd-20cb347cae34</chapterId>

**No video -- TBD**

# Introduction to Simplicity and Simplicity HL
<partId>5ccebdf5-2eda-4a59-bfd5-072a5f1edbda</partId>

## Intro to Simplicity: History, Philosophy, and Design Goals
<chapterId>03ee73ff-8a5f-4cbd-9e9b-f90eb4bcc58b</chapterId>

**No video -- TBD**

## Simplicity Syntax, Jets, Combinators, and Simple Contract Examples with Demo
<chapterId>2050afc0-5de1-4900-87b8-fd27a050960e</chapterId>

**No video -- TBD**

# Writing & Testing SimplicityHL Contracts
<partId>784d251a-896f-4b04-9bcb-1fd093763aa5</partId>

## Defining Contract Semantics, Type-checks, Simplicity HL Interpreter
<chapterId>1e28fe14-3ffb-4bbe-ab7e-4d4dc284b332</chapterId>

**No video -- TBD**

## Liquid Features Using SimplicityHL (e.g., Confidentiality Within Contracts)
<chapterId>f3855a4c-9826-4cfa-99dc-7ca3779afd3c</chapterId>

**No video -- TBD**

# Building Simplicity Apps
<partId>526bf638-3295-431e-9fb0-e07b6c5892ce</partId>

## DApp Architectures: Wallets, Attestations, Assets
<chapterId>c95aaabd-ed57-4ce9-adc4-375bfc01fcac</chapterId>

**No video -- TBD**

## Security Best Practices and Formal Verification
<chapterId>5f13beae-f09a-4f43-9713-43d350e16cc2</chapterId>

**No video -- TBD**

# Final Section
<partId>ff916f68-42d3-45f3-beae-e1115768f5c0</partId>


## Reviews & Ratings
<chapterId>45c1d7e4-9bfc-4acc-9a66-e4da66e72ca5</chapterId>


<isCourseReview>true</isCourseReview>

## Conclusion
<chapterId>cad281aa-aec6-4e8a-b1f3-48a3b923f917</chapterId>

<isCourseConclusion>true</isCourseConclusion>
