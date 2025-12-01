---
name: Liquid Bootcamp Essentials
goal: Gain a comprehensive understanding of the Liquid Network and the Elements project, and learn how to implement advanced solutions in confidential transactions, tokenization, and decentralized network architecture.
objectives:
  - Understand the fundamentals of Liquid architecture and its relationship with Bitcoin.
  - Learn to configure and operate Liquid nodes using the Elements software.
  - Explore the use of confidential transactions and asset issuance on the Liquid Network.
  - Grasp the business and technical aspects of Liquid for applications in capital markets.
---

# Introducing to the Liquid network

Embark on an educational journey designed to provide a deep understanding of the Liquid Network and the Elements project. This bootcamp combines theory and practice to teach you the technical, architectural, and business fundamentals necessary to implement and leverage Liquid's capabilities. From confidential transactions to ecosystem design, this course is ideal for those looking to expand their knowledge of advanced tools within the Bitcoin ecosystem.

With presentations by industry experts, the course covers topics such as Liquid architecture, tokenization applications, technical concepts of Elements, and innovative use cases like the Breeze SDK. Designed to be accessible for beginners and intermediate users, the course also offers value to experienced developers seeking to master Liquid as a platform for optimizing their projects.
+++

# Introduction

<partId>9f8a83d5-27e0-4e6d-af12-6cd6eb667291</partId>

## Course overview

<chapterId>3192ee7d-255b-4c4f-ba18-e08c5ab98577</chapterId>

Welcome to the Liquid Bootcamp, a comprehensive training designed to equip you with the knowledge and skills to effectively leverage the Liquid Network and the Elements project. This course offers a comprehensive exploration of Liquid's distinctive features, including Confidential Transactions, asset issuance, and its federated network architecture, while also introducing the foundational concepts of Elements, the software that powers Liquid.

Throughout the boot camp, you will explore the practical applications of the Liquid Network, from setting up and operating nodes to understanding its use in Bitcoin's capital markets and tokenization. With presentations from industry experts, you will also gain insights into advanced topics like HTLCs, the Breeze SDK, and the Blockstream AMP project.

This bootcamp was originally conducted as an in-person event, following a structured schedule (as shown in the image) designed for live sessions. However, for this course adaptation, the content has been reorganized to better suit an online format and facilitate student comprehension. The new order ensures a logical progression from foundational concepts to more advanced and technical topics, thereby maximizing the learning experience.

This journey is structured to accommodate participants with varying levels of expertise, offering a blend of theoretical knowledge and hands-on experience. By the end of this boot camp, you will have a solid understanding of Liquid's architecture, its integration with Bitcoin, and how to utilize its innovative features to build and optimize financial solutions.

Dive into the world of the Liquid sidechain and unleash its full potential right now!
# Fundamentals

<partId>6dd86449-c0f7-4e51-9252-5f135cf019df</partId>

## Liquid Architecture

<chapterId>4bca9c70-d54d-4e9a-b2db-17c3a6fa655b</chapterId>

:::video id=ff6899d2-b47f-4c3d-983d-3bd66d2be59d:::

### Liquid Network Architecture and Consensus Model

The Liquid Network is a federated sidechain built on the Elements codebase, designed to extend Bitcoin’s capabilities while relying on its fundamental security. Unlike Bitcoin’s Proof-of-Work, Liquid operates on a Federated Consensus model. The network is maintained by a globally distributed group of members, including exchanges, trading desks, and infrastructure providers. From this membership, fifteen "functionaries" are selected to act as block signers.

These functionaries produce blocks in a deterministic round-robin fashion, with a new block generated every minute. This precise timing stands in contrast to Bitcoin’s probabilistic ten-minute intervals. For a block to be valid, it requires signatures from at least 11 of the 15 functionaries (a two-thirds plus one threshold). This mechanism provides Liquid with "two-block finality," meaning that once a transaction has two confirmations (approximately two minutes), it is mathematically impossible to reorganize the chain. This speed and certainty are critical for arbitrage, automated trading, and rapid inter-exchange settlement.

The federation is dynamic. Through the Dynamic Federation (Dynafed) protocol, the network can rotate functionaries or update parameters without requiring a hard fork. This allows the system to evolve and replace hardware or members seamlessly while maintaining continuous operation.

### Confidential Transactions and Asset Management

A defining feature of Liquid is its native support for Confidential Transactions (CT) and multiple assets. On the main Bitcoin chain, all transaction details—sender, receiver, and amount—are public. In Liquid, CT uses cryptographic commitments to hide the asset type and amount from the public ledger while still allowing the network to verify that the transaction is valid (i.e., no inflation occurred). Only the participants holding the blinding keys can view the specific values, offering a level of commercial privacy essential for institutions moving large positions.

Liquid treats all assets as "native" citizens of the blockchain. This includes Liquid Bitcoin (LBTC), stablecoins like USDT, and security tokens. Issuing an asset does not require complex smart contracts; it is a basic function of the protocol.

#### Regulated Assets and AMP
For assets requiring compliance, such as security tokens, Liquid employs the Blockstream Asset Management Platform (AMP). This introduces a permissioned layer where transactions require a second signature from an authorization server. This allows issuers to enforce rules—such as Whitelisting or KYC requirements—on a granular level, combining the efficiency of a blockchain with the regulatory controls of traditional finance.

### The Two-Way Peg and Security Infrastructure

The connection between Liquid and Bitcoin is maintained through a two-way peg. To "peg-in," a user sends Bitcoin to a generated address on the mainchain. These funds are locked for 102 confirmations (roughly 17 hours) to eliminate reorganization risks. Once confirmed, an equivalent amount of LBTC is minted on the Liquid sidechain.

The "peg-out" process enables users to redeem LBTC for Bitcoin. This requires the burning of LBTC and a cryptographic authorization from the federation. To prevent theft, peg-outs are strictly controlled by Peg-out Authorization Keys (PAKs) held by federation members. Additionally, funds can be swapped instantly via third-party providers like SideSwap, bypassing the settlement delay for faster liquidity.

#### Hardware Security Modules (HSMs)
Security is enforced strictly through hardware. Functionaries do not keep private keys on standard servers; instead, they operate Hardware Security Modules (HSMs). These devices are air-gapped from the logic of the host server and are programmed with strict rules. For example, an HSM will refuse to sign a block if its height is not greater than the previous one, preventing history rewrites. This "adversarial" security model assumes the host server could be compromised, ensuring the keys remain secure even if the physical location is breached.

## Fundamentals of Elements

<chapterId>1e9cfbed-108e-4067-afb9-4cf950cb43d3</chapterId>

:::video id=5652dcb2-4303-484c-8be5-d98063b39c1c:::

### Elements: The Foundation of Liquid

Elements is an open-source, blockchain platform derived from the Bitcoin Core codebase. It extends Bitcoin’s functionality by enabling sidechains—independent blockchains that can transfer assets to and from Bitcoin. While Bitcoin Core powers the Bitcoin network, Elements is the software engine behind the Liquid Network and other custom sidechains.

The relationship is straightforward: Liquid is a specific "instance" of an Elements sidechain, configured for production use with a federated consensus model. Developers familiar with Bitcoin will find Elements intuitive, as it retains the same RPC (Remote Procedure Call) interface and command-line structure (`elements-cli`, `elements-d`, `elements-qt`). The key difference lies in the configuration: setting `chain=liquidv1` connects a node to the main Liquid network, while `chain=elementsregtest` spins up a local regression testing environment where developers can generate blocks instantly and test without external dependencies.

#### Asset Issuance
A standout feature of Elements is native asset issuance. Unlike Ethereum, where tokens are complex smart contracts, assets in Elements are first-class citizens created via a simple RPC command (`issueasset`).
* **Unique Identifiers:** Each asset gets a unique 64-character hexadecimal ID.
* **Reissuance Tokens:** Issuers can optionally create reissuance tokens, which grant the holder the right to mint more of the asset later (useful for stablecoins or security tokens).
* **Asset Registry:** Since hex IDs are not human-readable, the Blockstream Asset Registry maps these IDs to names and tickers (e.g., "USDT"), similar to a DNS for assets.

### Privacy via Confidential Transactions

Elements addresses one of the primary limitations of public blockchains: the lack of commercial privacy. On Bitcoin, every transaction amount is visible to the world. Elements introduces **Confidential Transactions (CT)**, which cryptographically blind the amount and asset type while still allowing the network to verify the transaction's validity.

This is achieved using **Pedersen Commitments** and **Range Proofs**.
* **Pedersen Commitments** replace the visible amount with a cryptographic commitment. Due to homomorphic encryption, validators can check that *Input Commitments = Output Commitments + Fees* without ever seeing the actual values.
* **Range Proofs** prevent a user from creating money out of thin air (e.g., by using negative numbers) by proving mathematically that the hidden value is a positive integer within a valid range.

To an outside observer, a Confidential Transaction shows valid inputs and outputs but obscures *what* is being sent and *how much*. Only the sender and receiver (who possess the blinding keys) can view the cleartext data.

### Development and RPC Workflow

Interacting with an Elements node is primarily done through its JSON-RPC interface. This allows applications written in Python, JavaScript, or Go to communicate with the blockchain.

* **Setup:** A developer typically starts in `regtest` mode. This allows for the instant generation of blocks (`generateblock`) to confirm transactions immediately, bypassing the 1-minute block time of the live network.
* **Commands:** Standard Bitcoin commands like `getblockchaininfo` are available, alongside Elements-specific commands like `dumpblindingkey` (for auditing CTs) or `pegin` (for moving BTC into the sidechain).
* **Aliases:** To manage multiple nodes (e.g., a "sender" and "receiver" for testing), developers often use shell aliases like `e1-cli` and `e2-cli` pointing to different data directories, simulating a peer-to-peer network on a single machine.

This architecture empowers developers to build sophisticated financial applications—such as securities platforms or private payment gateways—using the robust and familiar tooling of the Bitcoin ecosystem.

## Connecting Bitcoin Layers

<chapterId>3ff2df4a-8995-4d5e-9b8a-cd114880e666</chapterId>

:::video id=31368c02-b979-44d7-b217-ceed96c7ca5c:::

### Cross-Layer Infrastructure and HTLCs

The Bitcoin ecosystem has evolved into a multi-layered architecture, with the Mainchain providing settlement, Lightning offering speed, and Liquid enabling advanced asset capabilities. Moving value between these layers without centralized intermediaries requires a trustless cryptographic primitive: the Hash Time Locked Contract (HTLC).

An HTLC creates a conditional payment channel that links independent systems atomically. It functions through two primary constraints: a **hash lock** and a **time lock**.
* **The Hash Lock:** Funds can be spent immediately if the receiver reveals a secret "preimage" that matches a specific cryptographic hash.
* **The Time Lock:** If the receiver fails to reveal the secret within a set timeframe (block height), the original sender can reclaim the funds.

 This dual-path structure ensures safety. In a cross-layer swap, the same hash lock is used on both networks. When the receiver reveals the secret to claim funds on one layer (e.g., Liquid), that secret becomes visible to the sender, who can then use it to claim the reciprocal funds on the other layer (e.g., Lightning). This cryptographic binding guarantees that the swap either completes successfully for both parties or fails for both, eliminating the risk of one party losing funds while the other gains them.

### The Taproot and MuSig2 Upgrade

Legacy HTLCs (SegWit v0) functioned well but suffered from privacy and efficiency drawbacks. They required publishing the entire script logic on-chain, making swap transactions easily identifiable to blockchain analysts and more expensive due to their data size. The introduction of Taproot (SegWit v1) and the MuSig2 protocol has revolutionized this architecture.

Taproot allows for **Key Aggregation** via MuSig2. Instead of revealing a complex script with multiple public keys, MuSig2 lets the swap participants combine their keys into a single aggregated public key.
* **Cooperative "Key Path":** If both parties agree to the swap (the "happy path"), they co-sign the transaction. To the network, this looks identical to a standard, single-signature payment. It consumes minimal block space and reveals absolutely no information about the swap conditions.
* **Adversarial "Script Path":** If one party becomes unresponsive or malicious, the underlying script (containing the hash/time locks) is revealed only then. This is organized in a Merkle tree, allowing the honest party to expose only the specific branch needed to recover funds, keeping the rest of the contract logic hidden.

### Practical Implementation: Liquid-Lightning Swaps

In practice, these protocols enable seamless interchange between Bitcoin's layers. A typical Liquid-to-Lightning swap begins with a client requesting a swap from a service provider. The client provides a Lightning invoice, and the provider locks the equivalent Liquid Bitcoin (L-BTC) into a Taproot-enabled HTLC address.

The atomicity is enforced when the payment settles. To claim the L-BTC, the service provider must have the preimage. They get this preimage only when they successfully pay the client's Lightning invoice. The moment the Lightning payment is finalized, the preimage is revealed, allowing the provider to unlock the Liquid funds.

#### Wallet Abstraction and UTXO Management
For end-users, this complexity is entirely abstracted. Modern wallets like Aqua handle the key generation, invoice creation, and signing processes in the background. The user simply "pays" a Lightning invoice using their Liquid balance. Behind the scenes, the service manages UTXO consolidation, periodically sweeping small, unclaimed, or refunded outputs to maintain wallet efficiency and minimize fee impacts during high-traffic periods.

## Liquid Network Overview

<chapterId>1968db03-2364-46c0-9670-9e9844289ca1</chapterId>

:::video id=0bac0a62-90f2-41da-ac7c-330c0604bc61:::

### Liquid Network Architecture and Consensus

The Liquid Network operates as a federated sidechain built upon the **Elements** codebase. While Elements—a fork of Bitcoin Core—provides the software foundation, Liquid is the production network implementation. Unlike Bitcoin's Proof-of-Work, which relies on competitive mining, Liquid utilizes a **Federated Consensus** model.

The network is maintained by fifteen globally distributed "functionaries." These entities operate specialized servers that perform two critical roles:
1.  **Block Production:** Functionaries take turns creating blocks in a deterministic round-robin schedule, generating a new block exactly every minute.
2.  **Block Signing:** For a block to be valid, it must be signed by at least 11 of the 15 functionaries.

This 11-of-15 threshold ensures the network can tolerate the failure of up to four nodes without halting. The primary advantage of this trade-off is **deterministic finality**. While Bitcoin deals in probabilities, Liquid achieves settlement certainty after two blocks (approximately two minutes). Once a block has a single confirmation on top of it, the chain cannot be reorganized, making it highly effective for arbitrage and rapid settlement.

### Confidential Transactions and Native Assets

Liquid’s defining feature is the default use of **Confidential Transactions (CT)**. On the Bitcoin mainchain, the sender, receiver, and amount are public. Liquid improves this by cryptographically blinding the amount and the asset type, while leaving the sender and receiver addresses visible for verification.

To ensure that a user cannot print money (e.g., by sending negative amounts), Liquid employs **Pedersen Commitments** and **Range Proofs**. These cryptographic primitives allow the network to verify that *Inputs = Outputs + Fees* and that all values are positive integers, without ever revealing the specific numbers to the public ledger. Only the participants holding the blinding keys can view the decrypted data.

#### Asset Issuance
Liquid treats all assets as "native." Whether it is Liquid Bitcoin (L-BTC), a stablecoin like USDT, or a security token, they all share the same architecture. Issuing an asset requires no smart contracts—only a simple RPC call.
* **Unregulated Assets:** Can be issued permissionlessly by anyone.
* **Regulated Assets:** Utilizing the Blockstream Asset Management Platform (AMP), issuers can enforce compliance rules (like KYC/AML) by requiring a second signature from an authorization server before an asset can be moved.

### The Two-Way Peg and Dynamic Federation

The bridge between Bitcoin and Liquid is the **Two-Way Peg**. It allows users to move BTC onto the sidechain (Peg-in) and back to the mainchain (Peg-out).

**The Peg-in Process:**
This is permissionless. A user sends BTC to a federation-controlled address. To protect against Bitcoin blockchain reorganizations, these funds must wait for **102 confirmations** (approx. 17 hours) before the equivalent L-BTC is minted on the sidechain.

**The Peg-out Process:**
To return to Bitcoin, L-BTC is burned. However, to prevent theft of the underlying Bitcoin reserves, peg-outs are not fully automated. They require authorization from a member holding a **Peg-Out Authorization Key (PAK)**. The Bitcoin funds themselves are secured in an 11-of-15 multisignature wallet, with keys held in Hardware Security Modules (HSMs) that are air-gapped from the functionaries' main servers.

**Dynamic Federation (Dynafed):**
To ensure longevity, Liquid employs Dynafed, a protocol that allows the network to rotate functionaries or update parameters without a hard fork. If a functionary needs to be replaced, the network broadcasts a transition transaction. After a two-week overlap period, the new configuration takes over, allowing the federation to evolve seamlessly while maintaining continuous uptime.

## Ecosystem and Capital Markets

<chapterId>5f4c0e50-b435-4b6c-b8b7-c55cc1a35431</chapterId>

:::video id=07e0b82f-2d60-4eb3-9b5d-2ccb7ad06e8a:::

### Liquid Network: Business Strategy and Ecosystem

Liquid is more than a technical sidechain; it is a business-focused infrastructure layer designed to handle the complex requirements of capital markets that the Bitcoin mainchain cannot efficiently support. While Lightning Network optimizes for high-frequency, low-value payments, Liquid targets high-value transfers, asset issuance, and inter-exchange settlement.

The ecosystem is driven by the **Liquid Federation**, a consortium of ~73 companies including exchanges, trading desks, and infrastructure providers. This collaborative model mirrors traditional financial clearinghouses but operates with greater transparency and significantly reduced settlement times (2 minutes vs T+2 days).

### The Tokenization of Real-World Assets (RWA)

The core business case for Liquid is "Tokenization"—representing real-world value (stocks, bonds, mining contracts) as digital tokens on the blockchain. This offers three primary advantages:
1.  **24/7 Global Markets:** Removing banking hours and geographic restrictions.
2.  **Operational Efficiency:** Eliminating reconciliation errors through a shared, immutable ledger.
3.  **Atomic Settlement:** Reducing counterparty risk by ensuring delivery happens simultaneously with payment.

#### Regulated Assets and AMP
Most institutional assets cannot trade permissionlessly due to legal requirements. The **Asset Management Platform (AMP)** is the technical standard that enforces these rules.
* **Whitelisting:** Issuers can restrict holding and trading to KYC-verified addresses.
* **Multisig Control:** Compliance actions (like freezing stolen funds or reissuing lost tokens) are managed via multisignature authorization, ensuring no single employee can act unilaterally.

This infrastructure is live today. Platforms like **Stalker** provide end-to-end tokenization services in Europe, while **Sideswap** acts as a decentralized exchange and non-custodial wallet, enabling peer-to-peer trading of assets like the **Blockstream Mining Note (BMN)** and tokenized MicroStrategy shares (CMSTR).

### Real-World Success: The Mayfell Case Study

The most compelling proof of Liquid's utility comes from **Mayfell** in Mexico. In a market where traditional financing relies on paper promissory notes—which are prone to loss, fraud, and slow processing—Mayfell moved the entire infrastructure to Liquid.

* **Scale:** Over 25,000 promissory notes issued, representing **$1.5 billion+** in value.
* **Privacy:** Using Liquid's Confidential Transactions, the loan amounts are visible only to the lender and borrower, preserving commercial privacy while allowing auditors to verify the integrity of the ledger.
* **Impact:** By connecting non-bank lenders to global capital markets via blockchain, Mayfell reduced costs and expanded access to credit for Mexican SMEs, demonstrating that Liquid’s value proposition extends far beyond speculative trading.

### Strategic Positioning vs. Other Chains

Liquid competes in a crowded market of tokenization platforms (Ethereum, Solana, etc.), but it holds distinct strategic advantages:
* **Regulatory Clarity:** Liquid uses Bitcoin (L-BTC) as its native asset. It does not have a pre-mined token or an ICO, avoiding the "unregistered security" risks that plague other L1 blockchains.
* **Stability:** Unlike Ethereum's account model where failed transactions still burn gas fees, Liquid’s UTXO model is deterministic and reliable for mission-critical financial data.
* **Privacy:** Default confidentiality is a requirement for most financial institutions, a feature Liquid offers natively that public chains struggle to implement without complex add-ons.

For developers, this ecosystem offers a clear opportunity: building the tools (dashboards, wallets, compliance integrations) that bridge traditional finance with Bitcoin’s secure settlement layer.

## Blockstream AMP

<chapterId>4f21a0a7-0dc0-44cf-8a3a-d9e2f8a3f05f</chapterId>

:::video id=f00822b4-dc1a-46ff-adfc-ff7c97a0024d:::

### Blockstream AMP: Permissioned Asset Control on Liquid

Blockstream AMP (Asset Management Platform) serves as a critical infrastructure layer on the Liquid Network, designed specifically for issuers of regulated digital securities and stablecoins. While Liquid provides a permissionless base layer with native asset issuance, regulated entities often require strict oversight and compliance capabilities. AMP bridges this gap by introducing a permissioned control layer over specific assets without sacrificing the privacy benefits of Liquid’s Confidential Transactions.

The platform’s core value proposition rests on two primary capabilities: comprehensive issuer visibility and transaction authorization. Unlike standard Liquid assets where amounts and types are blinded to everyone but the participants, AMP assets allow the issuer to maintain a completely unblinded audit trail. This transparency is essential for regulatory reporting and internal audits. Furthermore, AMP enforces a strict authorization model through a co-signing mechanism. Every transfer of an AMP asset requires a signature from the AMP server. This allows issuers to enforce complex rules off-chain—such as freezing accounts, whitelisting accredited investors, or imposing transfer limits—effectively acting as a centralized gatekeeper within a decentralized network.

#### Operational Trade-offs
This architecture introduces specific trade-offs. The system relies on the AMP server’s availability; if the server acts as a co-signer and goes offline, asset liquidity pauses. Additionally, while user-to-user privacy is maintained, investors must accept that the issuer has full visibility into their holdings. This model is ideal for compliant security tokens but unsuitable for censorship-resistant cryptocurrencies.

### Architecture Evolution and Integration Pathways

The AMP ecosystem is currently transitioning from its first iteration to a more flexible, interoperable "Version 2" architecture. The legacy system required issuers to maintain fully synchronized Elements nodes and forced developers to rely heavily on the monolithic Green SDK. While functional, this created high technical barriers to entry and limited wallet choices.

The next-generation architecture fundamentally simplifies these requirements by shifting complexity to the server. In this new model, the AMP server handles the heavy lifting of transaction construction, UTXO selection, and fee calculation. It presents the issuer with a Partially Signed Elements Transaction (PSET) that simply requires a signature. This "smart server, dumb wallet" approach eliminates the need for issuers to run full nodes and enables the use of hardware wallets and standard multisignature setups for treasury management.

For developers, this evolution means moving away from proprietary SDKs toward standard descriptors and PSET workflows. Wallets can now register multisignature descriptors with the AMP server to establish authorization rights. This aligns AMP development with broader Bitcoin wallet standards, making integration accessible to any application capable of handling PSBT/PSET formats. Developers building today are encouraged to utilize tools like the Liquid Wallet Kit (LWK), which supports these modern, descriptor-based architectures, ensuring their applications are future-proofed for the new AMP standards.

### The Liquid Wallet Ecosystem and Confidentiality

Building applications on Liquid requires navigating a more complex stack than standard Bitcoin development due to features like native assets and Confidential Transactions. The ecosystem is supported by a layered architecture: low-level libraries like `secp256k1-zkp` handle cryptographic primitives, while higher-level toolkits manage wallet logic.

Historically, the Green Development Kit (GDK) provided a comprehensive but rigid solution. The modern alternative is the Liquid Wallet Kit (LWK), which offers a modular approach. LWK separates concerns into distinct crates—handling descriptors, signing, and hardware communication independently—giving developers the flexibility to build custom solutions without the overhead of a monolithic library.

#### Handling Confidential Transactions
The most distinct challenge in this ecosystem is managing the blinding lifecycle. In Liquid, transaction outputs are encrypted using Elliptic Curve Diffie-Hellman (ECDH) key exchange. A sender uses the receiver's blinding public key to encrypt asset amounts and types, generating a range proof that verifies the transaction's validity without revealing values.

For a wallet to function, it must successfully reverse this process. When a wallet detects an incoming transaction, it attempts to unblind the output using its private blinding key. If the shared secret matches, the wallet can decrypt the value and add it to the user's balance. This process is computationally intensive and requires precise management of blinding factors to ensure transactions are mathematically balanced, a complexity that tools like LWK aim to abstract away for the developer.

# Technical

<partId>53629f58-b9e0-4a10-8ab2-d51b047414f8</partId>
<chapterId>f1fdf2b0-4b6a-4ba7-812c-7586dcb36713</chapterId>

## Breeze SDK - Nodeless

<chapterId>fb77442c-3d1e-427e-b2f5-16668ce4c643</chapterId>

:::video id=1a6289b5-fdae-4320-b5b1-41925150108c:::

### Introduction to Breeze Liquid SDK

The Breeze Liquid SDK is a self-custodial, open-source toolkit designed to bridge the gap between the Liquid Network and the broader Bitcoin ecosystem. Its primary mission is to abstract the complexities of Lightning Network node management and atomic swaps, allowing developers to build frictionless financial applications.

Built with a "mobile-first" philosophy, the core logic is written in Rust for performance and safety, but it utilizes UniFFI (Unified Foreign Function Interface) to provide native bindings for Kotlin, Swift, Python, C#, Dart, and Flutter. This ensures that developers can integrate Bitcoin functionality into their preferred environment without managing low-level cryptographic operations.

**Supported Transaction Types:**
The SDK operates with Liquid as its "home base." It excels at three specific operations:
1.  **Liquid-to-Liquid:** Direct on-chain transfers.
2.  **Liquid-to-Lightning:** Paying Lightning invoices using Liquid funds.
3.  **Liquid-to-Bitcoin:** Swapping funds directly to the Bitcoin mainchain.

*Note: The SDK does not support direct Lightning-to-Lightning or Bitcoin-to-Bitcoin transactions. It is strictly a Liquid-centric tool.*

### Payment Architectures: Submarine Swaps

To achieve interoperability between Liquid, Lightning, and Bitcoin without centralized custodians, Breeze relies on **Submarine Swaps**. These are atomic operations where a transaction either completes successfully on both networks or fails on both, ensuring funds are never lost in transit.

#### Lightning Send (Submarine Swap)
When a user pays a Lightning invoice, the SDK broadcasts a "lock-up" transaction on the Liquid Network. This effectively puts the funds in escrow. The swap provider (Boltz) detects this, pays the Lightning invoice, and then uses the payment preimage (the cryptographic receipt) to claim the locked Liquid funds.

#### Lightning Receive (Reverse Submarine Swap)
Receiving Lightning is the inverse process. The user generates an invoice, and the swap provider locks funds on the Lightning Network. The SDK monitors this process via WebSockets. Once the lock is confirmed, the SDK automatically executes a claim transaction to move the equivalent funds into the user's Liquid wallet.

#### Cross-Chain Bitcoin
For Liquid-to-Bitcoin transfers, the architecture uses a "dual-swap" mechanism. Lock-up transactions occur on both chains simultaneously. The sender claims funds on Bitcoin, while the receiver claims funds on Liquid. This enables trustless bridging without reliance on federated peg-outs or centralized exchanges.

### Developer Interface and Automated Management

The Breeze SDK simplifies the developer experience by condensing complex financial flows into a standardized three-step process: **Connect, Prepare, and Execute**.

1.  **Connect:** Initializes the wallet, syncs with the blockchain using the Liquid Wallet Kit (LWK), and establishes WebSocket connections for real-time monitoring.
2.  **Prepare:** Before committing funds, this step calculates and returns all associated network fees and swap costs, allowing the UI to present a clear total to the user.
3.  **Execute:** This step constructs the transaction, broadcasts it, and initiates the swap.

#### Automated Safety Mechanisms
One of the SDK's most critical features is **Automated Refund Management**. In the event of a network failure or a non-cooperative counterparty, funds could theoretically become stuck in a time-locked contract. The SDK abstracts the recovery logic entirely. It monitors the state of every swap; if a swap fails or times out, the SDK automatically constructs and broadcasts the refund transaction to return funds to the user's wallet.

Additionally, the SDK handles **Metadata Resolution**. It merges off-chain swap data (provided by the Boltz swapper) with on-chain transaction history. This ensures that the user's transaction history is human-readable, displaying invoice details and payment context rather than just raw hexadecimal transaction hashes.

# Final Section

<partId>7ec65e6b-6e63-41b6-92ea-6a13bc77c3ff</partId>

## Reviews & Ratings

<chapterId>e5f6348c-e207-40ae-8fef-6a068a6bf741</chapterId>

<isCourseReview>true</isCourseReview>

## Final Exam

<chapterId>b13c4aa8-ced6-11f0-8515-afd3f381a001</chapterId>
<isCourseExam>true</isCourseExam>

## Conclusion

<chapterId>e30a5587-d74b-4360-87fb-bbf3de1b0ba8</chapterId>
<isCourseConclusion>true</isCourseConclusion>
