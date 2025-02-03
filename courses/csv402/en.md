---
name: The RGB protocol, from theory to practice
goal: Acquire the skills needed to understand and use RGB
objectives: 

  - Understand the fundamental concepts of the RGB protocol
  - Master the principles of client-side validation and Bitcoin commitments
  - Learn how to create, manage and transfer RGB contracts
  - How to operate an RGB-compatible Lightning node

---
# Discovering the RGB protocol

Dive into the world of RGB, a protocol designed to implement and enforce digital rights, in the form of contracts and assets, based on the consensus rules and operations of the Bitcoin blockchain. This comprehensive training course guides you through the technical and practical foundations of RGB, from the concepts of "Client-side Validation" and "Single-use Seals", to the implementation of advanced smart contracts.

Through a structured, step-by-step program, you'll discover the mechanisms of client-side validation, deterministic commitments on Bitcoin and interaction patterns between users. Learn how to create, manage and transfer RGB tokens on Bitcoin or the Lightning Network.

Whether you're a developer, Bitcoin enthusiast, or simply curious to learn more about this technology, this training course will provide you with the tools and knowledge you need to master RGB and build innovative solutions on Bitcoin.

The course is based on a live seminar organized by Fulgur'Ventures and taught by three renowned teachers and RGB experts.

+++
# Introduction

<partId>c6f7a70f-d894-595f-8c0a-b54759778839</partId>

## Course presentation

<chapterId>cf2f087b-6c6b-5037-8f98-94fc9f1d7f46</chapterId>

Hello everyone, and welcome to this training course dedicated to RGB, a client-side validated smart contract system running on Bitcoin and the Lightning Network. The structure of this course is designed to enable in-depth exploration of this complex subject. Here's how the course is organized:

**Section 1: Theory

The first section is dedicated to the theoretical concepts needed to understand the fundamentals of client-side validation and RGB. As you'll discover in this course, RGB introduces a host of technical concepts not usually seen in Bitcoin. In this section, you'll also find a glossary providing definitions for all terms specific to the RGB protocol.

**Section 2: Practice

The second section will focus on the application of the theoretical concepts seen in section 1. We'll learn how to create and manipulate RGB contracts. We'll also see how to program with these tools. These first two sections are presented by Maxim Orlovsky.

**Section 3: Applications

The final section is led by other speakers who present concrete RGB-based applications, to highlight real-life use cases.

---
This training course originally grew out of a two-week advanced development bootcamp in Viareggio, Tuscany, organized by [Fulgur'Ventures](https://fulgur.ventures/). The first week, focused on Rust and SDKs, can be found in this other course:

https://planb.network/courses/lnp402
In this course, we focus on the second week of the bootcamp, which focuses on RGB.

**Week 1 - LNP402:**

![RGB-Bitcoin](assets/fr/001.webp)

**Week 2 - Current training CSV402:**

![RGB-Bitcoin](assets/fr/002.webp)

Many thanks to the organizers of these live courses and to the 3 teachers who took part:


- Maxim Orlovsky: *Ex Tenebrae sententia sapiens dominabitur astris. Cypher, AI, robotics, transhumanism. Creator of RGB, Prime, Radiant and lnp_bp, mycitadel_io & cyphernet_io* ;
- Hunter Trujilo: *Developer, Rust, Bitcoin, Lightning, RGB* ;
- Federico Tenga: *I'm doing my bit to turn the world into a cypherpunk dystopia. Currently working on RGB at Bitfinex*.

The written version of this training course was drafted using 2 main resources:


- Videos of Maxim Orlovsky, Hunter Trujilo and Frederico Tenga's seminar at Lightning Bootcamp ;
- The RGB documentation, the production of which was sponsored by [Bitfinex](https://www.bitfinex.com/).

# RGB in theory

<partId>80e797ee-3f33-599f-ab82-e82eeee08219</partId>

## Introduction to distributed computing concepts

<chapterId>f52f8af5-5d7c-588b-b56d-99b97176204b</chapterId>

![video](https://youtu.be/AF2XbifPGXM)

RGB is a protocol designed to apply and enforce digital rights (in the form of contracts and assets) in a scalable and confidential way, based on the consensus rules and operations of the Bitcoin blockchain. The aim of this first chapter is to present the basic concepts and terminology around the RGB protocol, highlighting in particular its close links with basic distributed computing concepts such as Client-side Validation and Single-use Seals.

In this chapter, we explore the fundamentals of **distributed consensus systems** and see how RGB fits into this family of technologies. We'll also introduce the main principles that help us understand why RGB aims to be extensible and independent of Bitcoin's own consensus mechanism, while relying on it when necessary.

### Introduction

Distributed computing, a specific branch of computer science, studies the protocols used to circulate and process information on a network of nodes. Together, these nodes and the protocol rules constitute what is known as a distributed system. Among the essential properties that characterize such a system are :


- The **capability of independent verification and validation** of certain data by each node;
- The possibility for nodes to construct (depending on the protocol) a complete or partial view of the information. These views are the **states** of the distributed system;
- The **chronological order** of operations, so that data is reliably time-stamped and there is a consensus on the sequence of events (sequence of states).

In particular, the notion of **consensus** in a distributed system covers two aspects:


- Recognition of the validity** of state changes (according to protocol rules);
- The **agreement on the order** of these state changes, which makes it impossible to rewrite or reverse validated operations a posteriori (this is also known in Bitcoin as "double-spend protection").

The first functional, permission-free implementation of a distributed consensus mechanism was introduced by Satoshi Nakamoto with Bitcoin, thanks to the combined use of a blockchain data structure and a Proof-of-Work (PoW) algorithm. In this system, the credibility of the block history depends on the computing power devoted to it by the nodes (miners). Bitcoin is therefore a major and historic example of a distributed consensus system open to all (*permissionless*).

In the world of blockchain and distributed computing, we can distinguish two fundamental paradigms: ***blockchain*** in the traditional sense, and ***state channels***, the best example of which in production is the Lightning Network. The blockchain is defined as a register of chronologically ordered events, replicated by consensus within an open, permission-free network. State channels, on the other hand, are peer-to-peer channels that enable two (or more) participants to maintain an updated state off-chain, using the blockchain only when opening and closing these channels.

In the context of Bitcoin, you're no doubt familiar with the principles of mining, decentralization and finality of transactions on the blockchain, as well as how payment channels work. With RGB, we're introducing a new paradigm called **Client-side Validation**, which, unlike blockchain or Lightning, consists in locally (client-side) storing and validating the state transitions of a smart contract. This also differs from other "DeFi" techniques (_rollups_, _plasma_, _ARK_, etc.), in that Client-side Validation relies on the blockchain to prevent double-spending and to have a time-stamping system, while keeping the register of off-chain states and transitions, only with the participants concerned.

![RGB-Bitcoin](assets/fr/003.webp)

Later on, we'll also introduce an important term: the notion of "**stash**", which refers to the set of client-side data required to preserve the state of a contract, as this data is not replicated globally across the network. Finally, we'll look at the rationale behind RGB, a protocol that takes advantage of Client-side Validation, and why it complements existing approaches (blockchain and state channels).

### Trilemmas in distributed computing

To understand how Client-side Validation and RGB address problems not solved by blockchain and Lightning, let's discover 3 major "trilemmas" in distributed computing:


- Scalability, Decentralization, Privacy** ;
- CAP** Theorem (Consistency, Availability, Partition Tolerance) ;
- CIA** trilemma (Confidentiality, Integrity, Availability).

#### 1. Scalability, decentralization and confidentiality


- Blockchain (Bitcoin)**

Blockchain is highly decentralized, but not very scalable. What's more, since everything is in a global, public register, confidentiality is limited. We can try to improve confidentiality with zero-knowledge technologies (confidential transactions, mimblewimble schemes, etc.), but the public chain cannot hide the transaction graph.


- Lightning/State channels**

State channels (as with the Lightning Network) are more scalable and more private than blockchain, as transactions take place off-chain. However, the obligation to publicly announce certain elements (funding transactions, network topology) and the monitoring of network traffic can partly compromise confidentiality. Decentralization also suffers: routing is cash-intensive, and major nodes can become centralization points. This is precisely the phenomenon we're beginning to see on Lightning.


- Client-side Validation (RGB)**

This new paradigm is even more scalable and more confidential, because not only can we integrate zero-disclosure proof-of-knowledge techniques, but there is no global graph of transactions, since nobody holds the entire register. On the other hand, it also implies a certain compromise on decentralization: the issuer of a smart contract can have a central role (like a "contract deployer" in Ethereum). However, unlike blockchain, with Client-side Validation, you only store and validate the contracts you're interested in, which improves scalability by avoiding the need to download and verify all existing states.

![RGB-Bitcoin](assets/fr/004.webp)

#### 2. CAP Theorem (Consistency, Availability, Partition tolerance)

The CAP theorem emphasizes that it is impossible for a distributed system to simultaneously satisfy consistency (*Consistency*), availability (*Availability*) and partition tolerance (*Partition tolerance*).


- Blockchain**

The blockchain favors consistency and availability, but doesn't do well with network partitioning: if you can't see a block, you can't act and have the same view as the whole network.


- Lightning** (in French)

A system of state channels has availability and partitioning tolerance (since two nodes can remain connected to each other even if the network is fragmented), but overall consistency depends on the opening and closing of channels on the blockchain.


- Client-side Validation (RGB)**

A system like RGB offers consistency (each participant validates its data locally, without ambiguity) and partitioning tolerance (you keep your data autonomously), but does not guarantee global availability (everyone has to make sure they have the relevant pieces of history, and some participants may not publish anything or stop sharing certain information).

![RGB-Bitcoin](assets/fr/005.webp)

#### 3. CIA trilemma (Confidentiality, Integrity, Availability)

This trilemma reminds us that confidentiality, integrity and availability cannot all be optimized at the same time. Blockchain, Lightning and Client-side Validation fall differently into this balance. The idea is that no single system can provide everything; it is necessary to combine several approaches (blockchain's time-stamping, Lightning's synchronous approach, and local validation with RGB) to obtain a coherent package offering good guarantees in each dimension.

![RGB-Bitcoin](assets/fr/006.webp)

### The role of blockchain and the notion of sharding

The blockchain (in this case, Bitcoin) serves primarily as a _time-stamping_ mechanism and protection against double spending. Instead of inserting the complete data of a smart contract or decentralized system, we simply include **cryptographic commitments** (_commitments_) to transactions (in the sense of Client-side Validation, which we'll call "state transitions"). Thus :


- We free the blockchain from a large amount of data and logic;
- Each user stores only the history required for his own portion of the contract (his "*shard*"), rather than replicating the global state.

Sharding is a concept that originated in distributed databases (e.g. MySQL for social networks such as Facebook or Twitter). To solve the problem of data volume and synchronization latencies, the database is segmented into _shards_ (USA, Europe, Asia, etc.). Each segment is locally consistent and only partially synchronized with the others.

For RGB-type smart contracts, we shard according to the contracts themselves. Each contract is an independent _shard_. For example, if you only hold USDT tokens, you don't have to store or validate the entire history of another token like USDC. On Bitcoin, the blockchain doesn't do _sharding_: you have a global set of UTXOs. With Client-side Validation, each participant retains only the contract data it holds or uses.

We can therefore imagine the ecosystem as follows:


- The blockchain (Bitcoin)** as a foundation that ensures complete replication of a minimal register and serves as a time-stamping layer;
- The Lightning Network** for fast, confidential transactions, still based on the security and final settlement of the Bitcoin blockchain;
- RGB and Client-side Validation** to add more complex smart contract logic, without cluttering up the blockchain or losing confidentiality.

![RGB-Bitcoin](assets/fr/007.webp)

These three elements form a triangular whole, rather than a linear stack of "layer 2", "layer 3" and so on. Lightning can connect directly to Bitcoin, or be associated with Bitcoin transactions that incorporate RGB data. Similarly, a "BiFi" use (finance on Bitcoin) can compose with the blockchain, with Lightning and with RGB according to needs for confidentiality, scalability or contract logic.

![RGB-Bitcoin](assets/fr/008.webp)

### The notion of state transitions

In any distributed system, the aim of the validation mechanism is to be able to **determine the validity and chronological order of state changes**. The aim is to verify that the protocol rules have been respected, and to prove that these state changes follow one another in a definitive, unassailable order.

To understand how this validation works in the context of **Bitcoin** and, more generally, to grasp the philosophy behind Client-side Validation, let's first take a look back at the mechanisms of the Bitcoin blockchain, before seeing how Client-side Validation differs from them and what optimizations it makes possible.

![RGB-Bitcoin](assets/fr/009.webp)

In the case of the Bitcoin blockchain, transaction validation is based on a simple rule:


- All network nodes download every block and transaction;
- They validate these transactions to verify the correct evolution of the UTXO set (all unspent outputs);
- They store this data (in the form of blocks) so that the history can be replayed if necessary.

![RGB-Bitcoin](assets/fr/010.webp)

However, this model has two major drawbacks:


- Scalability**: since each node must process, verify and archive everyone's transactions, there is an obvious limit to transaction capacity, linked in particular to the maximum block size (1 MB on average over 10 minutes for Bitcoin, excluding cookies);
- Privacy**: everything is broadcast and stored publicly (amounts, destination addresses, etc.), which limits the confidentiality of exchanges.

![RGB-Bitcoin](assets/fr/012.webp)

In practice, this model works for Bitcoin as a base layer (Layer 1), but may become insufficient for more complex uses that simultaneously require high transaction throughput and a certain degree of confidentiality.

Client-side Validation is based on the opposite idea: rather than requiring the entire network to validate and store all transactions, each participant (client) will validate only the part of the history that concerns him or her:


- When a person receives an asset (or any other digital property), they only need to know and verify the chain of operations (state transitions) that lead to that asset and prove its legitimacy;
- This sequence of operations, from the ***Genesis*** (initial issue) to the most recent transaction, forms an acyclic directed graph (DAG) or shard, i.e. a fraction of the overall history.

![RGB-Bitcoin](assets/fr/013.webp)

At the same time, so that the rest of the network (or more precisely, the underlying layer, such as Bitcoin) can lock in the final state without seeing the details of this data, Client-side Validation relies on the notion of ***commitment***.

A *commitment* is a cryptographic commitment, typically a _hash_ (SHA-256 for example) inserted into a Bitcoin transaction, which proves that private data has been included, without revealing this data.

Thanks to these _commitments_, we can prove:


- The existence of information (since it is committed to a hash) ;
- The anteriority of this information (because it is anchored and time-stamped in the blockchain, with a date and block order).

The exact content, however, is not revealed, thus preserving its confidentiality.

In concrete terms, here's how an RGB state transition works:


- You prepare a new state transition (e.g. the transfer of an RGB token);
- You generate a cryptographic commitment to this transition and insert it into a Bitcoin transaction (these commitments are called "*anchors*" in the RGB protocol);
- The counterparty (the recipient) retrieves the customer-side history associated with this asset and validates end-to-end consistency, from the genesis of the smart contract to the transition you transmit to it.

![RGB-Bitcoin](assets/fr/014.webp)

Client-side Validation offers two major benefits:


- Scalability:**

The commitments (*commitments*) included in the blockchain are small (of the order of a few dozen bytes). This ensures that block space is not saturated, as only the hash needs to be included. It also enables the off-chain protocol to evolve, as each user only has to store his or her history fragment (his or her _stash_).


- Privacy :**

Transactions themselves (i.e. their detailed content) are not published on-chain. Only their fingerprints (*hash*) are. Thus, amounts, addresses and contract logic remain private, and the receiver can verify, locally, the validity of his shard by inspecting all previous transitions. There is no reason for the receiver to make this data public, except in the event of a dispute or where proof is required.

In a system like RGB, multiple state transitions from different contracts (or different assets) can be aggregated into a single Bitcoin transaction via a single _commitment_. This mechanism establishes a deterministic, time-stamped link between the on-chain transaction and the off-chain data (the client-side validated transitions), and enables multiple shards to be simultaneously recorded in a single anchor point, further reducing the on-chain cost and footprint.

In practice, when this Bitcoin transaction is validated, it permanently "locks" the state of the underlying contracts, since it becomes impossible to modify the hash already inscribed in the blockchain.

![RGB-Bitcoin](assets/fr/015.webp)

### The stash concept

A **stash** is the set of client-side data that a participant must absolutely retain to maintain the integrity and history of an RGB smart contract. Unlike a Lightning channel, where certain states can be reconstructed locally from shared information, the stash of an RGB contract is not replicated elsewhere: if you lose it, no one will be able to restore it to you, as you are responsible for your share of the history. This is why you need to adopt a system with reliable backup procedures in RGB.

![RGB-Bitcoin](assets/fr/016.webp)

### Single-use Seal: origins and operation

When accepting an asset such as a currency, two guarantees are essential:


- The authenticity of the item received;
- The uniqueness of the item received, to avoid double expenses.

For physical assets, such as a banknote, physical presence is enough to prove that it has not been duplicated. However, in the digital world, where assets are purely informational, this verification is more complex, as information can easily multiply and be duplicated.

As we saw earlier, the sender's revelation of the history of state transitions enables us to ensure the authenticity of an RGB token. By having access to all transactions since the genesis transaction, we can confirm the token's authenticity. This principle is similar to that of Bitcoin, where the history of coins can be traced back to the original coinbase transaction to verify their validity. However, unlike Bitcoin, this history of state transitions in RGB is private and kept on the client side.

To prevent double-spending of RGB tokens, we use a mechanism called "**Single-use Seal**". This system ensures that each token, once used, cannot be fraudulently reused a second time.

Single-use Seals are cryptographic primitives, proposed in 2016 by Peter Todd, akin to the concept of physical seals: once a seal has been placed on a container, it becomes impossible to open or modify it without irreversibly breaking the seal.

![RGB-Bitcoin](assets/fr/018.webp)

This approach, transposed to the digital world, makes it possible to prove that a sequence of events has indeed taken place, and that it can no longer be altered a posteriori. Single-use Seals thus go beyond the simple logic of `hash + timestamp`, adding the notion of a seal that can be closed **only once**.

![RGB-Bitcoin](assets/fr/017.webp)

For Single-use Seals to work, you need a publication proof medium capable of proving the existence or absence of a publication, and difficult (if not impossible) to falsify once the information has been disseminated. A **blockchain** (like Bitcoin) can fill this role, as can a paper newspaper with a public circulation, for example. The idea is as follows:


- We want to prove that a certain commitment on a message `h(m)` has been published to an audience without revealing the content of the message `m` ;
- We want to prove that no other competing `h(m')` message commitment has been published in place of `h(m)` ;
- We also want to be able to check that message `m` exists before a certain date.

A blockchain lends itself ideally to this role: as soon as a transaction is included in a block, the whole network has the same unfalsifiable proof of its existence and content (at least in part, since the _commitment_ can hide the details while proving the authenticity of the message).

A Single-use Seal can therefore be seen as a formal promise to publish a message (still unknown at this stage) once and only once, in a way that can be verified by all interested parties.

Unlike simple _commitments_ (hash) or timestamps, which attest to a date of existence, a Single-use Seal offers the additional guarantee that **no alternative commitment** can coexist: you can't close the same seal twice, or attempt to replace the sealed message.

The following comparison helps to understand this principle:


- Cryptographic commitment (hash)**: With a hash function, you can commit to a piece of data (a number) by publishing its hash. The data remains secret until you reveal the pre-image, but you can prove that you knew it in advance;
- Timestamp (blockchain)**: By inserting this hash in the blockchain, we also prove that we knew it at a precise moment (that of inclusion in a block);
- Single-use Seal**: With single-use seals, we go one step further by making the commitment unique. With a single hash, you can create several contradictory commitments in parallel (the problem of the doctor who announces "*It's a boy*" to the family and "*It's a girl*" in his personal diary). The Single-use Seal eliminates this possibility by connecting the commitment to a proof-of-publication medium, such as the Bitcoin blockchain, so that an expenditure of UTXO definitively seals the commitment. Once spent, the same UTXO cannot be re-spent to replace the commitment.

| Single-use Seals | Timestamps | Simple commitment (digest/hash) | Single-use Seals |

| -------------------------------------------------------------------------------- | ------------------------------- | ---------- | ---------------- |

| Publication of the commitment does not reveal the message | Yes | Yes | Yes | Yes

| Proof of date of commitment / existence of message before a certain date | Impossible | Possible | Possible | Possible

| Proof that no other alternative commitment can exist | Impossible | Possible |

Single-use Seals work in three main stages:

**Seal Definition :**


- Alice defines in advance the rules for publishing the seal (when, where and how the message will be published);
- Bob accepts or acknowledges these conditions.

![RGB-Bitcoin](assets/fr/021.webp)

**Seal Closing :**


- At runtime, Alice closes the seal by publishing the actual message (usually in the form of a _commitment_, e.g. a hash);
- It also provides a **witness** (cryptographic proof) proving that the seal is closed and irrevocable.

![RGB-Bitcoin](assets/fr/019.webp)

**Seal Verification :**


- Once the seal is closed, Bob can no longer open it: he can only check that it has been closed;
- Bob collects the seal, the **witness** and the message (or his commitment) to make sure that everything matches and that there are no competing seals or different versions.

The process can be summarized as follows:

```txt
# Défini par Alice, validé ou accepté par Bob
seal <- Define()
# Fermeture du sceau par Alice avec le message
witness <- Close(seal, message)
# Vérification par Bob
bool <- Verify(seal, witness, message)
```

Client-side validation, however, goes one step further: if the definition of a seal itself remains outside the blockchain, it is possible (in theory) for someone to challenge the existence or legitimacy of the seal in question. To overcome this problem, a chain of interlocking Single-use Seals is used:


- Each closed seal contains the definition of the following seal;
- We register these closures (with their _commitments_) within the blockchain (in a Bitcoin transaction);
- Thus, any attempt to modify a previous seal would contradict the history embedded in Bitcoin.

This is precisely what the RGB system does:


- Published messages are _commitments_ to client-side validated data;
- The seal definition is associated with a Bitcoin UTXO ;
- The seal closes when this UTXO is spent or when a new output is credited to the same commitment;
- The transaction chain that spends these UTXOs corresponds to the proof of publication: every transition or change of state on RGB is thus anchored in Bitcoin.

To sum up:


- The _seal definition_ is the UTXO you intend to seal a future commitment;
- The _seal closing_ occurs when you spend this UTXO, creating a transaction that contains the commitment;
- The _witness_ is the transaction itself, which proves that you have closed the seal with this content;
- You can't prove that a seal hasn't been closed (you can't be absolutely sure that a UTXO hasn't already been spent or won't be spent in a block you haven't seen yet), but you can prove that it has indeed been closed.

This uniqueness is important for Client-side Validation: when you validate a state transition, you check that it corresponds to a unique UTXO, not previously spent in a competing commitment. This is what guarantees the absence of double spending in off-chain smart contracts.

### Multiple commitments and roots

An RGB smart contract may need to spend several Single-use Seals (several UTXOs) simultaneously. What's more, a single Bitcoin transaction may reference several distinct contracts, each sealing its own state transition. This requires a **multi-commitment** mechanism to prove, deterministically and uniquely, that none of the commitments exists in duplicate. This is where the notion of **anchor** comes into play in RGB: a special structure linking a Bitcoin transaction and one or more client-side commitments (state transitions), each potentially belonging to a different contract. We'll take a closer look at this concept in the next chapter.

![RGB-Bitcoin](assets/fr/023.webp)

Two of the project's main GitHub repositories (under the LNPBP organization) group together the basic implementations of these concepts studied in the first chapter:


- client_side_validation** : Contains Rust primitives for local validation ;
- single_use_seals**: Implements the logic to define and close these seals securely.

![RGB-Bitcoin](assets/fr/020.webp)

Note that these software bricks are Bitcoin agnostic; in theory, they could be applied to any other proof-of-publication medium (another registry, a journal, etc.). In practice, RGB relies on Bitcoin for its robustness and broad consensus.

![RGB-Bitcoin](assets/fr/021.webp)

### Questions from the public

#### Towards wider use of Single-use Seals

Peter Todd also created the _Open Timestamps_ protocol, and the Single-use Seal concept is a natural extension of these ideas. Beyond RGB, other use cases can be envisaged, such as the construction of _sidechains_ without resorting to _merge mining_ or drivechain-related proposals like BIP300. Any system requiring a single commitment can, in principle, exploit this cryptographic primitive. Today, RGB is the first major full-scale implementation.

#### Data availability problems

Since in Client-side Validation, each user stores his or her own part of the history, data availability is not guaranteed globally. If a contract issuer withholds or revokes certain information, you may be unaware of the actual evolution of the offer. In some cases (such as stablecoins), the issuer is expected to maintain public data to prove the volume in circulation, but there is no technical obligation to do so. It is therefore possible to design deliberately opaque contracts with unlimited supply, which raises questions of trust.

#### Sharding and contract isolation

Each contract represents an isolated _shard_: USDT and USDC, for example, do not have to share their histories. Atomic swaps are still possible, but this does not involve merging their registers. Everything is done by cryptographic commitment, without disclosing the entire history graph to each participant.

### Conclusion

We've seen where the concept of Client-side Validation fits in with blockchain and _state channels_, how it responds to distributed computing trilemmas, and how it leverages the Bitcoin blockchain uniquely to avoid double-spending and for *time-stamping*. The idea is based on the notion of **Single-use Seal**, enabling the creation of unique commitments that you can't re-spend at will. In this way, each participant uploads only the history that is strictly necessary, increasing the scalability and confidentiality of smart contracts while retaining the security of Bitcoin as a backdrop.

The next step will be to explain in more detail how this Single-use Seal mechanism is applied in Bitcoin (via UTXOs), how anchors are created and validated, and then how complete smart contracts are built in RGB. In particular, we'll look at the issue of multiple commitments, the technical challenge of proving that a Bitcoin transaction simultaneously seals multiple state transitions in different contracts, without introducing vulnerabilities or double commitments.

Before diving into the more technical details of the second chapter, feel free to reread the key definitions (Client-side Validation, Single-use Seal, anchors, etc.) and keep in mind the overall logic: we're looking to reconcile the strengths of the Bitcoin blockchain (security, decentralization, time-stamping) with those of off-chain solutions (speed, confidentiality, scalability), and this is precisely what RGB and Client-side Validation are trying to achieve.

## The commitment layer

<chapterId>cc2fe85a-9cc7-5b8c-a00a-c0a867241061</chapterId>

![video](https://youtu.be/FS6PDprWl5Q)

In this chapter, we'll look at the implementation of Client-side Validation and Single-use Seals within the Bitcoin blockchain. We'll present the main principles of RGB's **commitment layer** (layer 1), with a particular focus on the **TxO2** scheme, which RGB uses to define and close a seal in a Bitcoin transaction. Next, we'll discuss two important points that haven't yet been covered in detail:


- The _deterministic Bitcoin commitments_;
- Multi-protocol commitments.

It is the combination of these concepts that enables us to superimpose several systems or contracts on top of a single UTXO and therefore a single blockchain.

It should be remembered that the cryptographic operations described can be applied, in absolute terms, to other blockchains or publishing media, but Bitcoin's characteristics (in terms of decentralization, resistance to censorship and openness to all) make it the ideal foundation for developing advanced programmability such as that required by **RGB**.

### Commitment schemes in Bitcoin and their use by RGB

As we saw in the first chapter of the course, Single-use Seals are a general concept: we make a promise to include a commitment (_commitment_) in a specific location of a transaction, and this location acts like a seal that we close on a message. However, on the Bitcoin blockchain, there are several options for choosing where to place this _commitment_.

To understand the logic, let's recall the basic principle: to close a _single-use seal_, we spend the sealed area by inserting the _commitment_ on a given message. In Bitcoin, this can be done in a number of ways:


- Use a public key or address**

We can decide that a specific public key or address is the _single-use seal_. As soon as this key or address appears on-chain in a transaction, it means that the seal is closed with a certain message.


- Use a Bitcoin** transaction output

This means that a _single-use seal_ is defined as a precise _outpoint_ (a TXID + output number pair). As soon as this _outpoint_ is spent, the seal is closed.

While working on RGB, we identified at least 4 different ways to implement these seals on Bitcoin:


- Define the seal via a public key, and close it in an _output_ ;
- Define the seal with an _outpoint_ and close it with an _output_ ;
- Define the seal via the value of a public key, and close it in a _input_ ;
- Define the seal via an _outpoint_, and close it in an _input_.

| Seal definition | Seal closure | Additional requirements | Main application | Possible engagement schemes |

| ------------- | ------------------------- | --------------------- | ----------------------------------------------------------------- | ---------------------------- | ------------------------------ |

| P2(W)PKH | None at present | Keytweak, taptweak, opret |

| TxO2 | Transaction output | Transaction output | Requires deterministic commitments on Bitcoin | RGBv1 (universal) | Keytweak, tapret, opret |

| PkI | Public key value | Transaction entry | Taproot only & not compatible with Legacy wallets | Bitcoin-based identities | Sigtweak, witweak |

| TxO1 | Transaction output | Transaction input | Taproot only & not compatible with Legacy wallets | None at present | Sigtweak, witweak |

We won't go into detail about each of these configurations, as in RGB we've chosen to use **an _outpoint_ as the definition of the seal**, and to place the _commitment_ in the output of the transaction spending this _outpoint_. We can therefore introduce the following concepts for the sequel:


- "Seal definition "** : A given _outpoint_ (identified by TXID + output no.) ;
- "Seal closing "**: The transaction that spends this _outpoint_, in which a _commitment_ is added to a message.

This scheme has been selected for its compatibility with RGB architecture, but other configurations could be useful for different uses.

The "O2" in "TxO2" reminds us that both definition and closure are based on the expenditure (or creation) of a transaction output.

### TxO2 diagram example

As a reminder, defining a _single-use seal_ does not necessarily require publishing an on-chain transaction. It's enough for Alice, for example, to already have an unspent UTXO. She can decide: "This _outpoint_ (already existing) is now my seal". She notes this locally (_client-side_), and until this UTXO is spent, the seal is considered open.

![RGB-Bitcoin](assets/fr/024.webp)

On the day it wants to close the seal (to signal an event, or to anchor a particular message), it spends this UTXO in a new transaction (this transaction is often called the "_witness transaction_" (unrelated to _segwit_, it's just the term we give it). This new transaction will contain the _commitment_ to the message.

![RGB-Bitcoin](assets/fr/025.webp)

Note that in this example :


- No one but Bob (or the people to whom Alice chooses to reveal the full proof) will know that a certain message is hidden in this transaction;
- Everyone can see that the _outpoint_ has been spent, but only Bob holds the proof that the message is actually anchored in the transaction.

To illustrate this TxO2 scheme, we can use a _single-use seal_ as a mechanism for revoking a PGP key. Instead of publishing a revocation certificate on servers, Alice can say: "This Bitcoin output, if spent, means that my PGP key is revoked".

Alice therefore has a specific UTXO, to which a certain state or data (known only to her) is associated locally (on the client side).

Alice informs Bob that if this UTXO is spent, a particular event will be deemed to have occurred. From the outside, all we see is a Bitcoin transaction; but Bob knows that this expenditure has a hidden meaning.

![RGB-Bitcoin](assets/fr/026.webp)

As Alice spends this UTXO, she closes the seal on a message indicating her new key, or simply the revocation of the old one. In this way, anyone monitoring on-chain will see that the UTXO is spent, but only those with the full proof will know that it is precisely the revocation of the PGP key.

![RGB-Bitcoin](assets/fr/027.webp)

In order for Bob or anyone else involved to check the hidden message, Alice must provide him with off-chain information.

![RGB-Bitcoin](assets/fr/028.webp)

Alice must therefore provide Bob with :


- The message itself (for example, the new PGP key) ;
- Cryptographic proof that the message was involved in the transaction (known as _extra transaction proof_ or _anchor_).

![RGB-Bitcoin](assets/fr/029.webp)

Third parties don't have this information. They only see that a UTXO has been spent. Confidentiality is therefore assured.

To clarify the structure, let's summarize the process in two transactions:


- Transaction 1**: This contains the _seal definition_, i.e. the _outpoint_ that will serve as the seal.

![RGB-Bitcoin](assets/fr/031.webp)


- Transaction 2**: Spends this _outpoint_. This closes the seal and, in the same transaction, inserts the _commitment_ on the message.

![RGB-Bitcoin](assets/fr/033.webp)

We therefore call the second transaction the "_witness transaction_".

To illustrate this from another angle, we can represent two layers:


- The top layer (blockchain, public)**: everyone sees the transaction and knows that a _outpoint_ has been spent;
- The lower layer (client-side, private)** : only Alice (or the person concerned) knows that this expense corresponds to such and such a message, via the cryptographic proof and the message she keeps locally.

![RGB-Bitcoin](assets/fr/034.webp)

But when closing the seal, the question arises as to where the _commitment_ should be inserted

In the previous section, we briefly mentioned how the Client-side Validation model can be applied to RGB and other systems. Here, we tackle the part about **deterministic Bitcoin commitments** and how to integrate them into a transaction. The idea is to understand why we are trying to insert a single commitment into the _witness transaction_, and above all how to ensure that there can be no other undisclosed competing commitments.

### Commitment locations in a transaction

When you give someone proof that a certain message is embedded in a transaction, you need to be able to guarantee that there isn't another form of commitment (a second, hidden message) in the same transaction that hasn't been revealed to you. For client-side validation to remain robust, you need a **deterministic** mechanism for placing a single _commitment_ in the transaction that closes the _single-use seal_.

The _witness transaction_ spends the famous UTXO (or _seal definition_) and this expenditure corresponds to the closing of the seal. Technically speaking, we know that each outpoint can only be spent once. This is precisely what underpins Bitcoin's resistance to double spending. But the spending transaction may have several _inputs_, several _outputs_, or be composed in a complex way (coinjoins, Lightning channels, etc.). We therefore need to clearly define where to insert the _commitment_ in this structure, unambiguously and uniformly.

Whatever the method (PkO, TxO2, etc.), the _commitment_ can be inserted :


- In an Input** via :
    - Sigtweak** (modifies the `r` component of the ECDSA signature, similar to the "Sign-to-contract" principle) ;
    - Witweak** (the transaction's _segregated witness_ data is modified).
- In an Output** via :
    - Keytweak** (the recipient's public key is "tweaked" with the message) ;
    - Opret** (the message is placed in a non-spendable output `OP_RETURN`) ;
    - Tapret** (or _Taptweak_), which relies on taproot to insert commitment into the script part of a taproot key, thus modifying the public key deterministically.

![RGB-Bitcoin](assets/fr/035.webp)

Here are the details of each method:

![RGB-Bitcoin](assets/fr/038.webp)

***Sig tweak (sign-to-contract) :***

An earlier scheme involved exploiting the random part of a signature (ECDSA or Schnorr) to embed the _commitment_: this is the technique known as "**Sign-to-contract**". You replace the randomly generated nonce with a hash containing the data. In this way, the signature implicitly reveals your commitment, without any additional space in the transaction. This approach has a number of advantages:


- No on-chain overload (you use the same place as the basic nonce);
- In theory, this can be quite discrete, as the nonce is initially a random datum.

However, 2 major drawbacks have emerged:


- Multisig before Taproot: when you have several signatories, you need to decide which signature will carry the _commitment_. Signatures can be ordered differently, and if a signatory refuses, you lose control over the outcome of the _commitment_;
- MuSig and the shared nonce: with Schnorr multisig (*MuSig*), nonce generation is a multiparty algorithm, and it becomes virtually impossible to tweak the nonce individually.

In practice, **sig tweak** is also not very compatible with existing hardware (hardware wallets) and formats (Lightning, etc.). So this great idea is hard to put into practice.

***Key tweak (pay-to-contract) :***

The **key tweak** takes up the historical concept of _pay-to-contract_. We take the public key `X` and tweak it by adding the value `H(message)`. Specifically, if `X = x * G` and `h = H(message)`, then the new key will be `X' = X + h * G`. This tweaked key hides the commitment to the `message`. The holder of the original private key can, by adding `h` to his private key `x`, prove that he has the key to spend the output. In theory, this is elegant, because :


- The _commitment_ is entered without adding any additional fields;
- You don't store any additional on-chain data.

In practice, however, we come up against the following difficulties:


- Wallets no longer recognize the standard public key, since it has been "tweaked", so they can't easily associate UTXO with your usual key;
- Hardware wallets are not designed to sign with a key that is not derived from their standard derivation;
- You need to adapt your scripts, descriptors, etc.

In the context of RGB, this path was envisaged until 2021, but it proved too complicated to make it work with current standards and infrastructure.

***Witness tweak :***

Another idea, which certain protocols such as _inscriptions Ordinals_ have put into practice, is to place the data directly in the `witness` section of the transaction (hence the expression "witness tweak"). However, this method :


- Makes engagement immediately visible (you literally paste raw data into the witness);
- May be subject to censorship (miners or nodes may refuse to relay if it is too large or any other arbitrary characteristic);
- Consumes space in the blocks, contrary to RGB's objective of discretion and lightness.

In addition, witness is designed to be prunable in certain contexts, which can make having robust proofs more complicated.

***Open-return (opret) :***

Very simple in its operation, an `OP_RETURN` allows you to store a hash or message in a special field of the transaction. But it's immediately detectable: everyone sees that there's a _commitment_ in the transaction, and it can be censored or discarded, as well as adding extra output. Since this increases transparency and size, it's considered less satisfactory from the point of view of a Client-side Validation solution.

```txt
34-byte_Opret_Commitment =
OP_RETURN   OP_PUSHBYTE_32   <mpc::Commitment>
|_________| |______________| |_________________|
1-byte       1-byte         32 bytes
```

### Tapret

The final option is the use of **Taproot** (introduced with BIP341) with the *Tapret* scheme. *Tapret* is a more complex form of deterministic commitment, which brings improvements in terms of footprint on the blockchain and confidentiality for contract operations. The main idea is to hide the commitment in the `Script Path Spend` part of a [taproot transaction](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki).

![RGB-Bitcoin](assets/fr/036.webp)

Before describing how the commitment is inserted into a taproot transaction, let's look at the **exact form** of the commitment, which must **imperatively** correspond to a 64-byte string [constructed](https://github.com/BP-WG/bp-core/blob/master/dbc/src/tapret/mod.rs#L179-L196) as follows:

```txt
64-byte_Tapret_Commitment =
OP_RESERVED ...  ... .. OP_RESERVED   OP_RETURN   OP_PUSHBYTE_33  <mpc::Commitment>  <Nonce>
|___________________________________| |_________| |______________| |_______________|  |______|
OP_RESERVED x 29 times = 29 bytes      1 byte         1 byte          32 bytes        1 byte
|________________________________________________________________| |_________________________|
TAPRET_SCRIPT_COMMITMENT_PREFIX = 31 bytes                    MPC commitment + NONCE = 33 bytes
```


- The 29 bytes `OP_RESERVED`, followed by `OP_RETURN`, then `OP_PUSHBYTE_33`, form the 31-byte _prefix_ part;
- Next comes a 32-byte _commitment_ (usually the Merkle root from **MPC**), to which we add 1 byte of **Nonce** (a total of 33 bytes for this second part).

So the 64-byte `Tapret` method looks like an `Opret` to which we've prefixed 29 bytes of `OP_RESERVED` and added an extra byte as a Nonce.

To maintain flexibility in terms of implementation, confidentiality and scaling, the Tapret scheme takes into account various use cases, depending on requirements:


- Unique incorporation of a Tapret commitment into a taproot transaction without a pre-existing Script Path structure;
- Integration of a Tapret commitment into a Taproot transaction already equipped with a Script Path.

Let's take a closer look at each of these two scenarios.

#### Tapret incorporation without existing Script Path

In this first case, we start from a taproot output key (*Taproot Output Key*) `Q` which contains only the internal public key `P` *(Internal Key*), with no associated script path (*Script Path*) :

![RGB-Bitcoin](assets/fr/047.webp)


- `P`: the internal public key for the _Key Path Spend_.
- `G`: the generating point of the elliptic curve [secp256k1](https://en.bitcoin.it/wiki/Secp256k1).
- t = tH_TWEAK(P)` is the tweak factor, calculated via a _tagged hash_ (e.g. `SHA-256(SHA-256(TapTweak) || P)`), in accordance with [BIP86](https://github.com/bitcoin/bips/blob/master/bip-0086.mediawiki#address-derivation). This proves that there is no hidden script.

To include a **Tapret** commitment, add a **Script Path Spend** with a **unique script**, as follows:

![RGB-Bitcoin](assets/fr/048.webp)


- t = tH_TWEAK(P || Script_root)` then becomes the new tweak factor, including the **Script_root**.
- `Script_root = tH_BRANCH(64-byte_Tapret_Commitment)` represents the root of this **script**, which is simply a hash of type `SHA-256(SHA-256(TapBranch) || 64-byte_Tapret_Commitment)`.

The proof of inclusion and uniqueness in the taproot tree here boils down to the single internal public key `P`.

#### Tapret integration into a pre-existing Script Path

The second scenario concerns a more complex `Q` taproot** output, which already contains several scripts. For example, we have a tree of 3 scripts:

![RGB-Bitcoin](assets/fr/049.webp)


- tH_LEAF(x)` designates the normalized tagged hash function of a leaf script.
- a, B, C` represent scripts already included in the taproot structure.

To add the Tapret commitment, we need to insert an *unspendable script* at the first level of the tree, shifting the existing scripts one level down. Visually, the tree becomes :

![RGB-Bitcoin](assets/fr/050.webp)


- tHABC` represents the tagged hash of the top level grouping `A, B, C`.
- tHT` represents the hash of the script corresponding to the 64-byte `Tapret`.

According to taproot rules, each branch/leaf must be combined according to a lexicographical hash order. There are two possible cases:


- `tHT` > `tHABC`: the Tapret commitment moves to the right of the tree. The uniqueness proof only needs `tHABC` and `P` ;
- tHT` < `tHABC`**: the Tapret commitment is placed on the left. To prove that there is no other Tapret commitment on the right, `tHAB` and `tHC` must be revealed to demonstrate the absence of any other such script.

Visual example for the first case (`tHABC < tHT`):

![RGB-Bitcoin](assets/fr/051.webp)

Example for the second case (`tHABC > tHT`):

![RGB-Bitcoin](assets/fr/052.webp)

#### Optimization with the nonce

To improve confidentiality, we can "mine" (a more accurate term would be "bruteforcing") the value of the `<Nonce>` (the last byte of the 64-byte `Tapret`) in an attempt to obtain a hash `tHT` such that `tHABC < tHT`. In this case, the commitment is placed on the right, saving the user from having to divulge the entire contents of existing scripts to prove the Tapret's uniqueness.

In summary, the `Tapret` offers a discrete and deterministic way of incorporating a commitment into a taproot transaction, while respecting the requirement for uniqueness and unambiguity essential to RGB's Client-side Validation and Single-use Seal logic.

#### Valid exits

For RGB commitment transactions, the main requirement for a valid Bitcoin commitment scheme is as follows: The transaction (*witness transaction*) must provably contain a single commitment. This requirement makes it impossible to construct an alternative history for client-side validated data within the same transaction. This means that the message around which the _single-use seal_ closes is unique.

To satisfy this principle, and regardless of the number of outputs in a transaction, we require that **one and only one output** can contain a commitment (*commitment*). For each of the schemes used (*Opret* or *Tapret*), the only valid outputs that can contain an RGB _commitment_ are :


- The first output `OP_RETURN` (if present) for the *Opret* scheme;
- The first taproot output (if present) for the *Tapret* scheme.

Note that it is quite possible for a transaction to contain a single `Opret` commitment and a single `Tapret` commitment in two separate outputs. Thanks to the deterministic nature of Seal Definition, these two commitments then correspond to two distinct pieces of data validated on the client side.

### Analysis and practical choices in RGB

When we started RGB, we reviewed all these methods to determine where and how to place a _commitment_ in a transaction in a deterministic way. We defined some criteria:


- Compatibility with different scenarios (e.g. multisig, Lightning, hardware wallets, etc.);
- Impact on on-chain space ;
- Difficulty of implementation and maintenance ;
- Confidentiality and resistance to censorship.

| Trace and on-chain sizing | Client-side sizing | Portfolio integration | Hardware compatibility | Lightning compatibility | Taproot compatibility |

| --------------------------------------------------- | ------------------------ | ------------------ | ----------------------------- | ------------------------ | ----------------------- | --------------------- |

| Keytweak (deterministic P2C) | 🟢 | 🟡 | 🔴 | 🟠 | 🔴 BOLT, 🔴 Bifrost | 🟠 Taproot, 🟢 MuSig |

| Sigtweak (deterministic S2C) | 🟢 | 🟠 | 🔴 | 🔴 BOLT, 🔴 Bifrost | 🟠 Taproot, 🔴 MuSig |

| Opret (OP_RETURN) | 🔴 | 🟢 | 🟢 | 🟠 | 🔴 BOLT, 🟠 Bifrost | - |

| Tapret algorithm: top-left node | 🟠 | 🔴 | 🟠 | 🟢 | 🔴 BOLT, 🟢 Bifrost | 🟢 Taproot, 🟢 MuSig |

| Tapret algorithm #4: any node + proof | 🟢 | 🟠 | 🟢 | 🔴 BOLT, 🟢 Bifrost | 🟢 Taproot, 🟢 MuSig |

| Deterministic commitment scheme | Standard | On-chain cost | Size of customer-side evidence |

| ------------------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |

| Keytweak (deterministic P2C) | LNPBP-1, 2 | 0 bytes | 33 bytes (untweaked key) |

| Sigtweak (deterministic S2C) | WIP (LNPBP-39) | 0 bytes | 0 bytes |

| Opret (OP_RETURN) | - | 36 (v)bytes (TxOut additional) | 0 bytes |

| Tapret algorithm: top-left node | LNPBP-6 | 32 bytes in witness (8 vbytes) on any n-of-m multisig and spend per script path | 0 bytes on taproot scriptless scripts ~270 bytes in a single script case, ~128 bytes if more than one script |

| Tapret algorithm #4: any node + proof of uniqueness | LNPBP-6 | 32 bytes in the witness (8 vbytes) for single script cases, 0 bytes in the witness in most other cases | 0 bytes on taproot scriptless scripts, 65 bytes until the Taptree has a dozen scripts |

| Layer | On-chain cost (bytes/vbytes) | On-chain cost (bytes/vbytes) | On-chain cost (bytes/vbytes) | On-chain cost (bytes/vbytes) | On-chain cost (bytes/vbytes) | Client-side cost (bytes) | Client-side cost (bytes) | Client-side cost (bytes) | Client-side cost (bytes) | Client-side cost (bytes) |

| ------------------------------ | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ------------------------ | ------------------------ | ------------------------ | ------------------------ | ------------------------ |

| **Type** | **Tapret** | **Tapret #4** | **Keytweak** | **Sigtweak** | **Opret** | **Tapret** | **Tapret #4** | **Keytweak** | **Sigtweak** | **Opret** |

| Single-sig | 0 | 0 | 0 | 0 | 32 | 0 | 0 | 32 | 0? | 0 | 0 |

| MuSig (n-of-n) | 0 | 0 | 0 | 32 | 0 | 0 | 32 | ? > 0 | 0 |

| Multi-sig 2-of-3 | 32/8 | 32/8 or 0 | 0 n/a | 32 | ~270 | 65 | 32 | n/a | 0 |

| Multi-sig 3-of-5 | 32/8 | 32/8 or 0 | 0 n/a | 32 | ~340 | 65 | 32 | n/a | 0 |

| Multi-sig 2-of-3 with timeouts | 32/8 | 0 | 0 n/a | 32 | 64 | 65 | 32 | n/a | 0 | 0

| Layer | Cost on-chain (vbytes) | Cost on-chain (vbytes) | Cost on-chain (vbytes) | Cost on client side (bytes) | Cost on client side (bytes) |

| -------------------------------- | ---------------------- | ---------------------- | ---------------------- | ------------------------ | ------------------------ |

| **Type** | **Base** | **Tapret #2** | **Tapret #4** | **Tapret #2** | **Tapret #4** |

| MuSig (n-of-n) | 16.5 | 0 | 0 | 0 | 0 | 0

| FROST (n-of-m) | ? | 0 | 0 | 0 | 0 |

| Multi_a (n-of-m) | 1+16n+8m | 8 | 8 | 33 * m | 65 |

| MuSig branch / Multi_a (n-of-m) | 1+16n+8n+8xlog(n) | 8 | 0 | 64 | 65 |

| With timeouts (n-of-m) | 1+16n+8n+8xlog(n) | 8 | 0 | 64 | 65 |

| Method | Confidentiality and scalability | Interoperability | Compatibility | Portability | Complexity |

| ----------------------------------------- | ------------------------------ | ---------------- | ------------- | ----------- | ---------- |

| Keytweak (deterministic P2C) | 🟢 | 🔴 | 🔴 | 🟡 | 🟡 |

| Sigtweak (deterministic S2C) | 🟢 | 🔴 | 🔴 | 🟢 | 🔴 |

| Opret (OP_RETURN) | 🔴 | 🟠 | 🔴 | 🟢 | 🟢 |

| Algo Tapret: top-left node | 🟠 | 🟢 | 🔴 | 🟠 |

| Algo Tapret #4: Any node + proof | 🟢 | 🟢 | 🟠 | 🔴 |

In the course of the study, it became clear that none of the commitment schemes was fully compatible with the current Lightning standard (which does not employ Taproot, _muSig2_ or additional _commitment_ support). Efforts are underway to modify Lightning's channel construction (*BiFrost*) to allow the insertion of RGB commitments. This is another area where we need to review the transaction structure, the keys and the way in which channel updates are signed.

The analysis showed that, in fact, other methods (key tweak, sig tweak, witness tweak, etc.) presented other forms of complication:


- Either we have a large on-chain volume;
- Either there is a radical incompatibility with the existing wallet code;
- Either the solution is not viable in non-cooperative multisig.

For RGB, two methods in particular stand out: ***Opret*** and ***Tapret***, both classified as "Transaction Output", and compatible with the TxO2 mode used by the protocol.

### Multi Protocol Commitments - MPC

In this section, we look at how **RGB** handles the aggregation of multiple contracts (or, more precisely, their _transition bundles_) within a single commitment (*commitment*) recorded in a Bitcoin transaction via a deterministic scheme (according to `Opret` or `Tapret`). To achieve this, the order of Merkelization of the various contracts takes place in a structure called **MPC Tree** (_Multi Protocol Commitment Tree_). In this section, we'll look at the construction of this MPC Tree, how to obtain its root, and how multiple contracts can share the same transaction confidentially and unambiguously.

Multi Protocol Commitment (MPC) is designed to meet two needs:


- The construction of the `mpc::Commitment` hash: this will be included in the Bitcoin blockchain according to an `Opret` or `Tapret` scheme, and must reflect all the state changes to be validated;
- Simultaneous storage of multiple contracts in a single _commitment_, enabling separate updates on multiple assets or RGB contracts to be managed in a single Bitcoin transaction.

In concrete terms, each _transition bundle_ belongs to a particular contract. All this information is inserted into a **MPC Tree**, whose root (`mpc::Root`) is then hashed again to give the `mpc::Commitment`. It is this last hash that is placed in the Bitcoin transaction (_witness transaction_), according to the deterministic method chosen.

![RGB-Bitcoin](assets/fr/042.webp)

#### MPC Root Hash

The value actually written on-chain (in `Opret` or `Tapret`) is called `mpc::Commitment`. This is calculated in the form of [BIP-341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki), according to the formula :

```txt
mpc::Commitment = SHA-256(SHA-256(mpc_tag) || SHA-256(mpc_tag) || depth || cofactor || mpc::Root )
```

where :


- `mpc_tag` is a tag: `urn:ubideco:mpc:commitment#2024-01-31`, chosen according to [RGB tagging conventions](https://github.com/RGB-WG/rgb-core/blob/master/doc/Commitments.md);
- `depth` (1 byte) indicates the depth of the *MPC Tree* ;
- cofactor` (16 bits, in Little Endian) is a parameter used to promote the uniqueness of the positions assigned to each contract in the tree;
- `mpc::Root` is the root of *MPC Tree*, calculated according to the process described in the next section.

![RGB-Bitcoin](assets/fr/044.webp)

#### MPC Tree construction

To build this MPC Tree, we need to ensure that each contract corresponds to a unique leaf position. Suppose we have :


- c` contracts to be included, indexed by `i` in `i = {0,1,..,C-1}` ;
- For each contract `c_i`, we have an identifier `ContractId(i) = c_i`.

We then construct a tree of width `w` and depth `d` such that `2^d = w`, with `w > C`, so that each contract can be placed in a separate _leaf_. The position `pos(c_i)` of each contract in the tree is determined by :

```txt
pos(c_i) = c_i mod (w - cofactor)
```

where `cofactor` is an integer that increases the probability of obtaining distinct positions for each contract. In practice, construction follows an iterative process:


- We start from a minimum depth (`d=3` by convention to hide the exact number of contracts);
- We try different `cofactors` (up to `w/2`, or a maximum of 500 for performance reasons);
- If we fail to position all contracts without collision, we increment `d` and start again.

The aim is to avoid trees that are too tall, while keeping the risk of collision to a minimum. Note that the collision phenomenon follows a random distribution logic, linked to the [Anniversary Paradox](https://en.wikipedia.org/wiki/Birthday_problem).

#### Inhabited leaves

Once `C` distinct positions `pos(c_i)` have been obtained for contracts `i = {0,1,..,C-1}`, each sheet is filled with a hash function (*tagged hash*):

```txt
tH_MPC_LEAF(c_i) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x10 || c_i || BundleId(c_i))
```

where :


- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, is always chosen according to the Merkle conventions of RGB ;
- `0x10` identifies a _contract leaf_ ;
- `c_i` is the 32-byte contract identifier (derived from the Genesis hash);
- bundleId(c_i)` is a 32-byte hash describing the set of `State Transitions` relative to `c_i` (gathered into a *Transition Bundle*).

#### Uninhabited leaves

The remaining leaves, not assigned to a contract (i.e. `w - C` leaves), are filled with a "dummy" value (_entropy leaf_) :

```txt
tH_MPC_LEAF(j) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x11 || entropy || j )
```

where :


- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, is always chosen according to the Merkle conventions of RGB ;
- `0x11` denotes an _entropy leaf_ ;
- `entropy` is a random value of 64 bytes, chosen by the person building the tree;
- `j` is the position (in 32 bits Little Endian) of this leaf in the tree.

#### MPC nodes

After generating the `w` leaves (inhabited or not), we proceed to merkelization. Any internal nodes are hashed as follows:

```txt
tH_MPC_BRANCH(tH1 || tH2) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || b || d || w || tH1 || tH2)
```

where :


- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, is always chosen according to the Merkle conventions of RGB ;
- b` is the _branching factor_ (8 bits). Most often, `b=0x02` because the tree is binary and complete;
- d` is the depth of the node in the tree;
- `w` is the tree width (in 256-bit Little Endian binary);
- tH1` and `tH2` are the hashes of the child nodes (or leaves), already calculated as shown above.

Progressing in this way, we obtain the root `mpc::Root`. We can then calculate `mpc::Commitment` (as explained above) and insert it on-chain.

To illustrate this, let's imagine an example where `C=3` (three contracts). Their positions are assumed to be `pos(c_0)=7`, `pos(c_1)=4`, `pos(c_2)=2`. The other leaves (positions 0, 1, 3, 5, 6) are _entropy leaves_. The diagram below shows the sequence of hashes to the root with :


- `BUNDLE_i` which represents `BundleId(c_i)` ;
- `tH_MPC_LEAF(A)` and so on, which represent leaves (some for contracts, others for entropy) ;
- Each branch `tH_MPC_BRANCH(...)` combines the hashes of its two children.

The final result is the **mpc::Root**, then the `mpc::Commitment`.

![RGB-Bitcoin](assets/fr/053.webp)

#### MPC shaft check

When a verifier wishes to ensure that a `c_i` contract (and its `BundleId`) is included in the final `mpc::Commitment`, he simply receives a Merkle proof. This proof indicates the nodes needed to trace the leaves (in this case, `c_i`'s _contract leaf_) back to the root. There's no need to disclose the entire *MPC Tree*: this protects the confidentiality of other contracts.

In the example, a `c_2` verifier only needs an intermediate hash (`tH_MPC_LEAF(D)`), two `tH_MPC_BRANCH(...)`, the `pos(c_2)` position proof and the `cofactor` value. It can then locally reconstruct the root, then recalculate the `mpc::Commitment` and compare it to the one written in the Bitcoin transaction (within `Opret` or `Tapret`).

![RGB-Bitcoin](assets/fr/054.webp)

This mechanism ensures that :


- The status relative to `c_2` is indeed included in the aggregate information block (client-side);
- No one can build an alternative history with the same transaction, because the on-chain _commitment_ points to a single MPC root.

#### Summary of the MPC structure

Multi Protocol Commitment* (MPC) is the principle that enables RGB to aggregate multiple contracts into a single Bitcoin transaction, while maintaining the uniqueness of commitments and confidentiality vis-à-vis other participants. Thanks to the deterministic construction of the tree, each contract is assigned a unique position, and the presence of "dummy" leaves (*Entropy Leaves*) partially masks the total number of contracts participating in the transaction.

The entire Merkle tree is never stored on the client. We simply generate a _Merkle path_ for each contract concerned, to be transmitted to the recipient (who can then validate the commitment). In some cases, you may have several assets that have passed through the same UTXO. You can then merge several _Merkle paths_ into a so-called _multi-protocol commitment block_, to avoid duplicating too much data.

Each _Merkle proof_ is therefore lightweight, especially as the tree depth will not exceed 32 in RGB. There's also a notion of "Merkle block", which retains more information (cross-section, entropy, etc.), useful for combining or separating several branches.

That's why it took so long to finalize RGB. We had the overall vision from 2019: putting everything on client-side, circulating tokens off-chain. But for details like sharding for multiple contracts, the structure of the Merkle tree, how to handle collisions and merge proofs... all this required iterations.

### Anchors: a global assembly

Following on from the construction of our commitments (`Opret` or `Tapret`) and our MPC (*Multi Protocol Commitment*), we need to address the notion of **Anchor** in the RGB protocol. An Anchor is a client-side validated structure that brings together the elements needed to verify that a Bitcoin commitment actually contains specific contractual information. In other words, an Anchor summarizes all the data needed to validate the _commitments_ described above.

An Anchor consists of three ordered fields:


- `Txid`
- `MPC Proof`
- extra Transaction Proof - ETP

Each of these fields plays a part in the validation process, whether it's a matter of reconstructing the underlying Bitcoin transaction or proving the existence of a hidden commitment (particularly in the case of `Tapret`).

#### TxId

The `Txid` field corresponds to the 32-byte identifier of the Bitcoin transaction containing the `Opret` or `Tapret` commitment.

In theory, it would be possible to find this `Txid` by tracing the chain of state transitions which themselves point to each witness transaction, following the logic of Single-use Seals. However, to facilitate and accelerate verification, this `Txid` is simply included in the Anchor, thus saving the validator from having to go back through the entire off-chain history.

#### MPC Proof

The second field, `MPC Proof`, refers to the proof that this particular contract (e.g. `c_i`) is included in the _Multi Protocol Commitment_. It is a combination of :


- `pos_i`, the position of this contract in the MPC tree;
- cofactor`, the value defined to resolve position collisions;
- the `Merkle Proof`, i.e. the set of nodes and hashes used to reconstruct the MPC root and verify that the contract identifier and its `Transition Bundle` are committed to the root.

This mechanism was described in the previous section on building the *MPC Tree*, where each contract obtains a unique leaf thanks to the :

```txt
pos(c_i) = c_i mod (w - cofactor)
```

Then, a deterministic merkelization scheme is used to aggregate all the leaves (contracts + entropy). In the end, the `MPC Proof` allows the root to be reconstructed locally and compared with the `mpc::Commitment` included on-chain.

#### Extra Transaction Proof - ETP

The third field, the **ETP**, depends on the type of commitment used. If the commitment is of type `Opret`, no additional proof is required. The validator inspects the first `OP_RETURN` output of the transaction and finds the `mpc::Commitment` directly there.

**If the commitment is of type `Tapret`**, an additional proof called *Extra Transaction Proof - ETP* must be provided. It contains :


- The internal public key (`P`) of the taproot output in which the *commitment* is embedded;
- The partner nodes of the `Script Path Spend` (when the Tapret *commitment* is inserted in a script), in order to prove the exact location of this script in the taproot tree:
 - If the `Tapret` *commitment* is on the right-hand branch, we reveal the left-hand node (e.g. `tHABC`),
 - If the `Tapret` *commitment* is on the left, you need to disclose 2 nodes (e.g. `tHAB` and `tHC`) to prove that no other *commitment* is present on the right-hand side.
- The `nonce` may be used to "mine" the best configuration, allowing the *commitment* to be placed on the right of the tree (proof optimization).

This additional proof is essential because, unlike `Opret`, the `Tapret` commitment is integrated into the structure of a taproot script, which requires revealing part of the taproot tree in order to correctly validate the location of the *commitment*.

![RGB-Bitcoin](assets/fr/045.webp)

The **Anchors** therefore encapsulate all the information required to validate a Bitcoin commitment in the context of RGB. They indicate both the relevant transaction (`Txid`) and the proof of contract positioning (`MPC Proof`), while managing the additional proof (`ETP`) in the case of `Tapret`. In this way, an Anchor protects the integrity and uniqueness of the off-chain state by ensuring that the same transaction cannot be reinterpreted for other contractual data.

### Conclusion

In this chapter, we cover :


- How to apply the Single-use Seals concept in Bitcoin (in particular via a _outpoint_);
- The various methods for deterministically inserting a _commitment_ into a transaction (Sig tweak, Key tweak, witness tweak, op_return, Taproot/Tapret) ;
- The reasons why RGB focuses on Tapret commitments ;
- Multi-contract management via _multi-protocol commitments_, essential if you don't want to expose an entire state or other contracts when you want to prove a specific point;
- We've also seen the role of _Anchors_, which bring everything together (transaction TXID, Merkle tree proof and Taproot proof) in a single package.

In practice, the technical implementation is divided between several dedicated Rust _crates_ (in _client_side_validation_, _commit-verify_, _bp_core_, etc.). The fundamental notions are there:

![RGB-Bitcoin](assets/fr/046.webp)

In the next chapter, we'll look at the purely off-chain component of RGB, namely contract logic. We'll see how RGB contracts, organized as partially replicated _finite state machines_, achieve much higher expressiveness than Bitcoin scripts, while preserving the confidentiality of their data.

## Introduction to smart contracts and their states

<chapterId>04a9569f-3563-5382-bf53-0c7069343ba0</chapterId>

![video](https://youtu.be/tmAVdyXGmj4)

In this and the next chapter, we'll look at the notion of **smart contract** within the RGB environment and explore the different ways in which these contracts can define and evolve their *state*. We'll see why the RGB architecture, using the ordered sequence of Single-use Seals, makes it possible to execute various types of ***Contract Operations*** in a scalable way and without going through a centralized registry. We'll also look at the fundamental role of ***Business Logic*** in framing the evolution of the contract state.

### Smart contracts and digital bearer rights

RGB's aim is to provide an infrastructure for implementing smart contracts on Bitcoin. By "smart contract" we mean an agreement between several parties that is automatically and computationally enforced, without human intervention to enforce the clauses. In other words, the law of the contract is enforced by the software, not by a trusted third party.

This automation raises the question of decentralization: how can we free ourselves from a centralized registry (e.g. a central platform or database) to manage ownership and contract performance? The original idea, taken up by RGB, is to return to a mode of ownership known as "bearer instruments". Historically, certain securities (bonds, shares, etc.) were issued in bearer form, enabling anyone who physically possessed the document to enforce his or her rights.

![RGB-Bitcoin](assets/fr/055.webp)

RGB applies this concept to the digital world: rights (and obligations) are encapsulated in data that is manipulated off-chain, and the status of this data is validated by the participants themselves. This allows, a priori, a much greater degree of confidentiality and independence than that offered by other approaches based on public registers.

### Introduction to Smart Contract RGB status

A smart contract in RGB can be seen as a state machine, defined by :


- A **State**, i.e. the set of information reflecting the current configuration of the contract;
- A **Business Logic** (set of rules), which describes under what conditions and by whom the state can be modified.

![RGB-Bitcoin](assets/fr/056.webp)

It's important to understand that these contracts are not limited to the simple transfer of tokens. They can embody a wide variety of applications: from traditional assets (tokens, stocks, bonds) to more complex mechanics (usage rights, commercial terms, etc.). Unlike other blockchains, where the contract code is accessible and executable by all, RGB's approach compartmentalizes access and knowledge of the contract to participants ("***contract participants***"). There are several roles:


- The issuer** or creator of the contract, who defines the Genesis of the contract and its initial variables;
- Parties with rights** (*ownership*) or other enforcement capabilities ;
- Observers**, potentially limited to seeing certain information, but who cannot trigger modifications.

This separation of roles contributes to censorship resistance, by ensuring that only authorized persons can interact with the contractual state. It also gives RGB the ability to scale horizontally: the majority of validations take place outside the blockchain, and only cryptographic anchors (the *commitments*) are inscribed on Bitcoin.

### Status and Business Logic in RGB

From a practical point of view, the contract's **Business Logic** takes the form of rules and scripts, defined in what RGB calls a **Schema**. The Schema encodes :


- State structure (which fields are public? Which fields are owned by which parties?
- Validity conditions (what must be checked before authorizing a state update?) ;
- Authorizations (who can initiate a *State Transition*? Who can only observe?).

At the same time, the **Contract State** often breaks down into two components:


- A **Global State**: public part, potentially observable by all (depending on configuration);
- Owned States**: private parts, allocated specifically to owners via UTXOs referenced in the contract logic.

As we'll see in the following chapters, any status update (*Contract Operation*) must dock to a Bitcoin _commitment_ (via `Opret` or `Tapret`) and comply with the *Business Logic* scripts to be considered valid.

### Contract Operations: creation and evolution of the State

In the RGB universe, a ***Contract Operation*** is any event that changes the contract from a **old state** to a **new state**. These operations follow the following logic:


- We take note of the current status of the contract;
- We apply the rule or operation (a ***State Transition***, a ***Genesis*** if it's the very first state, or a ***State Extension*** if there's a public *valency* to retrigger);
- We anchor the modification via a new _commitment_ on the blockchain, closing one _single-use seal_ and creating another ;
- The rights holders concerned validate locally (*client-side*) that the transition conforms to the *Schema* and that the associated Bitcoin transaction is registered on-chain.

![RGB-Bitcoin](assets/fr/057.webp)

The end result is an updated contract, now with a different state. This transition does not require the entire Bitcoin network to be concerned with the details, since only a small cryptographic fingerprint (the _commitment_) is recorded in the blockchain. The sequence of Single-use Seals prevents any double-spending or double-use of the State.

### Operations chain: from Genesis to Terminal State

To put this into perspective, an RGB smart contract starts with a **Genesis**, the very first state. Thereafter, various Contract Operations follow one another, forming a DAG (*Directed Acyclic Graph*) of operations:


- Each transition is based on a previous state (or several, in the case of convergent transitions);
- The chronological order is guaranteed by the inclusion of each transition in a Bitcoin anchor, time-stamped and unalterable thanks to consensus by Proof-of-Work ;
- When no more operations are in progress, a **Terminal State** is reached: the most recent and complete state of the contract.

![RGB-Bitcoin](assets/fr/012.webp)

This DAG topology (instead of a simple linear chain) reflects the possibility that different parts of the contract may evolve in parallel, as long as they do not contradict each other. RGB then takes care of avoiding any inconsistencies by *client-side* verification of each participant involved.

### Summary

Smart contracts in RGB introduce a model of digital bearer instruments, decentralized but anchored in Bitcoin for time-stamping and guaranteeing the order of transactions. Automated execution of these contracts is based on :


- A **Contract State*, indicating the current configuration of the contract (rights, balances, variables, etc.);
- A **Business Logic** (*Schema*), defining which transitions are allowed and how they must be validated;
- Contract Operations**, which update this state step by step, thanks to commitments anchored in Bitcoin transactions.

In the next chapter, we'll go into more detail about the concrete representation of these ***states*** and ***state transitions*** at the off-chain level, and how they relate to the UTXOs and Single-use Seals embedded in Bitcoin. This will be an opportunity to see how RGB's internal mechanics, based on client-side validation, manage to maintain the consistency of smart contracts while preserving data confidentiality.

## RGB contract operations

<chapterId>78c44e88-50c4-5ec4-befe-456c1a9f080b</chapterId>

![video](https://youtu.be/lUTjeuM0oTA)

In this chapter, we'll look at how operations in smart contracts and state transitions work, again within the RGB protocol. The aim will also be to understand how several participants cooperate to transfer ownership of an asset.

### State transitions and their mechanics

The general principle is still that of Client-side Validation, where state data is held by the owner and validated by the recipient. However, the specificity here with RGB lies in the fact that Bob, as recipient, asks Alice to incorporate certain information into the contract data in order to have real control over the asset received, via a hidden reference to one of his UTXOs.

To illustrate the process of a *State Transition* (which is one of the fundamental ***Contract Operations*** in RGB), let's take a step-by-step example of an asset transfer between Alice and Bob:

**Initial situation:**

Alice has a ***stash RGB*** of locally validated data (*client-side*). This stash refers to one of her UTXOs on Bitcoin. This means that a _seal definition_ in this data points to a UTXO belonging to Alice. The idea is to enable her to transfer certain digital rights linked to an asset (e.g. RGB tokens) to Bob.

![RGB-Bitcoin](assets/fr/058.webp)

**Bob also has UTXOs :**

Bob, on the other hand, has at least one UTXO of his own, with no direct link to Alice's. In the event that Bob has no UTXO, it is still possible to make the transfer to him using the *witness transaction* itself: the output of this transaction will then include the commitment (_commitment_) and implicitly associate ownership of the new contract with Bob.

![RGB-Bitcoin](assets/fr/059.webp)

**Construction of the new property (*New State*) :**

Bob sends Alice information encoded in the form of an ***invoice*** (we'll go into more detail on invoice construction in later chapters), asking her to create a new state that conforms to the rules of the contract. This state will include a new *seal definition* pointing to one of Bob's UTXOs. In this way, Bob is given ownership of the assets defined in this new state, for example a certain amount of RGB tokens.

![RGB-Bitcoin](assets/fr/060.webp)

**Preparation of the sample transaction:**

Alice then creates a Bitcoin transaction spending the UTXO referenced in the previous seal (the one that legitimized her as the holder). In the output of this transaction, a *commitment* (via `Opret` or `Tapret`) is inserted to anchor the new RGB state. The `Opret` or `Tapret` commitments are derived from a *MPC tree* (as seen in previous chapters), which can aggregate several transitions from different contracts.

**Transmission of *Consignment* to Bob:**

Before broadcasting the transaction, Alice sends Bob a ***Consignment*** containing all the necessary *client-side* data (his *stash*) and the new state information in Bob's favor. At this point, Bob applies the RGB consensus rules:


- It validates all the RGB data contained in the *Consignment*, including the new state which grants it ownership of the asset;
- Relying on the *Anchors* included in the *Consignment*, it verifies the chronology of witness transactions (from Genesis to the most recent transition) and validates the corresponding commitments in the blockchain.

**Transition completion:**

If Bob is satisfied, he may give his approval (for example, by signing the *consignment*). Alice can then broadcast the prepared sample transaction. Once confirmed, this closes the seal previously held by Alice and formalizes ownership by Bob. Anti-double-spending security is then based on the same mechanism as in Bitcoin: the UTXO is spent, proving that Alice can no longer reuse it.

![RGB-Bitcoin](assets/fr/061.webp)

The new state now references Bob's UTXO, giving Bob the ownership previously held by Alice. The Bitcoin output where the RGB data is anchored becomes the irrevocable proof of the transfer of ownership.

An example of a minimal DAG (*Directed Acyclic Graph*) comprising two contract operations (a **Genesis** then a ***State Transition***) can illustrate how the RGB state (*client-side* layer, in red) connects to the Bitcoin blockchain (*Commitment* layer, in orange).

![RGB-Bitcoin](assets/fr/062.webp)

It shows that a Genesis defines a seal (*seal definition*), then a *State Transition* closes this seal to create a new one in another UTXO.

In this context, here are a few reminders of terminology:


- An ***Assignment*** combines :
    - A ***Seal Definition*** (which points to a UTXO);
    - Owned States**, i.e. data linked to ownership (for example, the quantity of tokens transferred).
- A **Global State** brings together the general properties of the contract, visible to all, and ensuring the global consistency of evolutions.

State Transitions**, described in the previous chapter, are the main form of contract operation. They refer to one or more previous states (from Genesis or another State Transition) and update them to a new state.

![RGB-Bitcoin](assets/fr/063.webp)

This diagram shows how, in a *State Transition Bundle*, several seals can be closed in a single sample transaction, while simultaneously opening new seals. Indeed, an interesting feature of the RGB protocol is its ability to scale: several transitions can be aggregated into a Transition Bundle, each aggregation being associated with a distinct leaf of the *MPC tree* (a unique bundle identifier). Thanks to the *Deterministic Bitcoin Commitment* (DBC) mechanism, the entire message is inserted into a `Tapret` or `Opret` output, while closing previous seals and possibly defining new ones. The `Anchor* serves as a direct link between the commitment stored in the blockchain and the client-side validation structure (*client-side*).

In the following chapters, we'll look at all the components and processes involved in building and validating a State Transition. Most of these elements are part of the RGB consensus, implemented in the **RGB Core Library**.

### Transition Bundle

On RGB, it is possible to bundle different State Transitions belonging to the same contract (i.e. sharing the same **ContractId**, derived from the Genesis **OpId**). In the simplest case, as between Alice and Bob in the example above, a **Transition Bundle** contains just one transition. But support for multi-payer operations (such as coinjoins, Lightning channel openings, etc.) means that several users can combine their State Transitions in a single bundle.

Once collected, these transitions are anchored (by the MPC + DBC mechanism) in a single Bitcoin transaction:


- Each State Transition is hashed and grouped into a Transition Bundle ;
- The Transition Bundle is itself hashed and inserted into the MPC tree leaf corresponding to this contract (a BundleId);
- The MPC tree is finally engaged via `Opret` or `Tapret` in the witness transaction, which thus closes the consumed seals and defines the new seals.

Technically speaking, the **BundleId** inserted in the MPC sheet is obtained from a tagged hash applied to the strict serialization of the bundle's *InputMap* field:

```txt
BundleId = SHA256( SHA256(bundle_tag) || SHA256(bundle_tag) || InputMap )
```

In which `bundle_tag = urn:lnp-bp:rgb:bundle#2024-02-03` for example.

The *InputMap* is a data structure which lists, for each input `i` of the sample transaction, the reference to the *OpId* of the corresponding State Transition. For example:

```txt
InputMap =
N               input_0    OpId(input_0)    input_1    OpId(input_1)   ...    input_N-1  OpId(input_N-1)
|____________________| |_________||______________| |_________||______________|       |__________||_______________|
16-bit Little Endian   32-bit LE   32-byte hash
|_________________________| |_________________________|  ...  |___________________________|
MapElement1                MapElement2                       MapElementN
```


- `N` is the total number of entries in the transaction that refer to an `OpId`;
- opId(input_j)` is the operation identifier of one of the State Transitions present in the bundle.

By referencing each entry only once and in an orderly fashion, we prevent the same seal from being spent twice in two simultaneous State Transitions.

### State Generation and Active State

State Transitions can therefore be used to transfer ownership of an asset from one person to another. However, they are not the only possible operations in the RGB protocol. The protocol defines three **Contract Operations** :


- State Transition** ;
- Genesis** ;
- State Extension**.

Among these, **Genesis** and **State Extension** are sometimes called "*State Generation operations*", because they create new states without immediately closing any. This is a very important point: **Genesis** and **State Extension** do not involve closing a seal. Rather, they define a new seal, which must then be spent by a subsequent **State Transition** to be truly validated in the blockchain history.

![RGB-Bitcoin](assets/fr/064.webp)

The **Active State** of a contract is often defined as the set of latest states resulting from the history (the DAG) of transactions, starting with the Genesis and following all anchors in the Bitcoin blockchain. Any old states that are already obsolete (i.e. attached to spent UTXOs) are no longer considered active, but remain essential for checking the consistency of the history.

### Genesis

The Genesis is the starting point of every RGB contract. It is created by the contract issuer and defines the initial parameters, in accordance with the **Schema**. In the case of an RGB token, the Genesis may specify, for example :


- The number of tokens originally created and their owners;
- Total possible issue ceiling ;
- Any re-issue rules, and which participants are eligible.

Being the first transaction in the contract, the Genesis does not reference any previous state, nor does it close any seal. However, to appear in the history and be validated, the Genesis must be **consumed** (closed) by a first State Transition (often a scan/auto-spend transaction to the issuer itself, or the initial distribution to users).

### State Extension

State Extensions** offer an original feature for smart contracts. They make it possible to redeem certain digital rights (*Valencies*) provided for in the contract definition, without immediately closing the seal. Most often, this concerns :


- Distributed token issues;
- Asset swap mechanisms ;
- Conditional reissues (which may include the destruction of other assets, etc.).

Technically speaking, a State Extension references a *Redeem* (a particular type of RGB input) that corresponds to a *Valency* defined previously (for example, in Genesis or another State Transition). It defines a new seal, available to the person or condition benefiting from it. For this seal to become effective, it must be spent by a subsequent State Transition.

![RGB-Bitcoin](assets/fr/065.webp)

For example: the Genesis creates a right of issue (*Valency*). This can be exercised by an authorized actor, who then builds a State Extension :


- It refers to the Valency (redeem);
- It creates a new *assignment* (new *Owned State* data) pointing to a UTXO ;
- A future State Transition, issued by the owner of this new UTXO, will actually transfer or distribute the newly issued tokens.

### Components of a Contract Operation

I'd now like to take a detailed look at each of the constituent elements of a **Contract Operation** in RGB. A Contract Operation is the action which modifies the state of a contract, and which is validated on the client side, in a deterministic way, by the legitimate recipient. In particular, we'll see how the Contract Operation takes into account, on the one hand, the **old state** (*Old State*) of the contract, and on the other, the definition of a **new state** (*New State*).

```txt
+---------------------------------------------------------------------------------------------------------------------+
|  Contract Operation                                                                                                 |
|                                                                                                                     |
|  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |
|  | Ffv |     | ContractId | SchemaId |      | TransitionType | ExtensionType |      | Testnet |     | AltLayers1 |  |
|  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |
|                                                                                                                     |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|  | Metadata                                      |  | Global State                                               |  |
|  |                                               |  | +----------------------------------+                       |  |
|  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
|  | |          Structured Data            |       |  | | |  GlobalStateType  | |  Data  | |     ...     ...       |  |
|  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
|  |                                               |  | +----------------------------------+                       |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
|                                                                                                                     +---------> OpId |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
|  | Inputs                                        |  | Assignments                                                |  |
|  |                                               |  |                                                            |  |
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  | | Input #1                                  | |  | | Assignment #1                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ + ---------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  |                                               |  |                                                            |  |
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  | | Input #2                                  | |  | | Assignment #2                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  |                                               |  |                                                            |  |
|  |       ...           ...          ...          |  |     ...          ...             ...                       |  |
|  |                                               |  |                                                            |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|                                                                                                                     |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|  | Redeems                                       |  | Valencies                                                  |  |
|  |                                               |  |                                                            |  |
|  | +------------------------------+              |  |                                                            |  |
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |
| OpId +--------------> PrevOpId | | ValencyType | |  ...   ...   |  |  | ValencyType |  | ValencyType |         ...              |  |
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |
|  | +------------------------------+              |  |                                                            |  |
|  |                                               |  |                                                            |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------+
```

If we look at the diagram above, we can see that a Contract Operation includes elements referring to the **New State** and others referring to the updated **Old State**.

The elements of the **New State** are :


- Assignments**, in which are defined :
 - The **Seal Definition**;
 - The **Owned State**.
- The **Global State**, which can be modified or enriched ;
- Valencies**, possibly defined in a State Transition or Genesis.

The **Old State** is referenced via :


- Inputs**, which point to *Assignments* of previous state transitions (not present in Genesis);
- Redeems**, which refer to previously defined Valencies (only in State Extensions).

In addition, a Contract Operation includes more general fields specific to the operation:


- ffv` (*Fast-forward version*): 2-byte integer indicating the contract version;
- transitionType` or ExtensionType`: 16-bit integer specifying the Transition or Extension type, according to the business logic;
- `ContractId`: 32-byte number referring to the *OpId* of the contract Genesis. Included in Transitions and Extensions, but not in Genesis ;
- schemaId: present only in Genesis, this is the 32-byte hash representing the structure (*Schema*) of the contract;
- testnet`: Boolean indicating whether you are on the Testnet or Mainnet network. Genesis only;
- altlayers1`: variable identifying the alternative layer (sidechain or other) used to anchor data in addition to Bitcoin. Only present in Genesis ;
- metadata": field which can store temporary information, useful for validating a complex contract, but which must not be recorded in the final status history.

Finally, all these fields are condensed by a customized hashing process, to produce a unique fingerprint, the `OpId`. This `OpId` is then integrated into the Transition Bundle, enabling it to be authenticated and validated within the protocol.

Each *Contract Operation* is therefore identified by a 32-byte hash named `OpId`. This hash is calculated by a SHA256 hash of all the elements making up the operation. In other words, each *Contract Operation* has its own cryptographic commitment, which includes all the data needed to verify the authenticity and consistency of the operation.

An RGB contract is then identified by a `ContractId`, derived from the Genesis `OpId` (since there is no pre-Genesis operation). In concrete terms, we take the Genesis `OpId`, reverse the byte order and apply a Base58 encoding. This encoding makes the `ContractId` easier to handle and recognize.

### Status update methods and rules

The **Contract State** represents the set of information that the RGB protocol must track for a given contract. It is composed of :


- A single Global State**: this is the public, global part of the contract, visible to all;
- One or more Owned States**: each Owned State is associated with a unique seal (and therefore a UTXO on Bitcoin). A distinction is made between :
    - The **public** Owned States,
    - The **private** Owned States.

![RGB-Bitcoin](assets/fr/066.webp)

The *Global State* is directly included in the *Contract Operation* as a single block. The *Owned States* are defined in each *Assignment*, alongside the *Seal Definition*.

A major feature of RGB is the way in which the Global State and Owned States are modified. There are generally two types of behavior:


- Mutable**: when a state element is described as mutable, each new operation replaces the previous state with a new state. The old data is then considered obsolete;
- Accumulating**: when a state element is defined as accumulating, each new operation adds new information to the previous state, without overwriting it. The result is a kind of accumulated history.

If, in the contract, a state element is not defined as mutable or cumulative, this element will remain empty for subsequent operations (in other words, there are no new versions for this field). It's the contract Schema (i.e. the coded business logic) that determines whether a state (Global or Owned) is mutable, cumulative or fixed. Once the Genesis has been defined, these properties can only be modified if the contract itself allows it, for example via a specific State Extension.

The table below illustrates how each type of Contract Operation can manipulate (or not) the Global State and the Owned State:

| Genesis | State Extension | State Transition |

| ---------------------------- | :-----: | :-------------: | :--------------: |

| **Add Global State** | + | - | + |

| n/a | - | + | **Mutation of Global State** | - | + |

| **Add Owned State** | + | - | + |

| **Mutation of Owned State** | n/a | No | + |

| **Add Valencies** | + | + | + | + |

**`+`** : action possible if the contract's Schema allows it.

**`-`**: the operation must be confirmed by a subsequent State Transition (the State Extension alone does not close the Single-use Seal).

In addition, the temporal scope and update rights of each type of data can be distinguished in the following table:

| Metadata | Global State | Owned State |

| ------------------------------- | ---------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |

| Defined for a single Contract Operation | Defined globally for the contract | Defined for each seal (*Assignment*) | Defined for a single Contract Operation | Defined globally for the contract | Defined for each seal (*Assignment*) | Defined for each seal (*Assignment*) | Defined for each contract

| Non-actualizable (ephemeral data) | Transaction issued by actors (issuer, etc.) | Depends on the rightful holder of the seal (the one who can spend it in a subsequent transaction) |

| The state is defined before the operation (by the *Seal Definition* of the previous operation) | The state is established at the end of the operation | The state is established at the end of the operation | The state is defined before the operation (by the *Seal Definition* of the previous operation) | The state is established at the end of the operation | The state is defined before the operation (by the *Seal Definition* of the previous operation)

### Global State

The Global State is often described as "nobody owns, everybody knows". It contains general information about the contract, which is publicly visible. For example, in a token-issuing contract, it potentially contains :


- The ticker (symbolic abbreviation of the token): `ticker` ;
- The full name of the token: `name` ;
- Precision (number of decimal places): `precision` ;
- Initial offer (and/or maximum token limit): `issuedSupply` ;
- Issue date: `created` ;
- Legal data or other public information: `data`.

This Global State can be placed on public resources (websites, IPFS, Nostr, Torrent, etc.) and distributed to the community. Also, the economic incentive (the need to hold and transfer these tokens, etc.) naturally drives contract users to maintain and propagate this data themselves.

### Assignments

The *Assignment* is the basic structure for defining :


- The seal (*Seal Definition*), which points to a specific UTXO;
- The *Owned State*, i.e. the property or data associated with this seal.

An *Assignment* can be seen as the analogue of a Bitcoin transaction output, but with more flexibility. Herein lies the logic of property transfer: the *Assignment* associates a particular type of asset or right (`AssignmentType`) with a seal. Whoever possesses the private key of the UTXO linked to this seal (or whoever can spend this UTXO) is considered the owner of this *Owned State*.

One of RGB's great strengths lies in the ability to reveal (*reveal*) or hide (*conceal*) the *Seal Definition* and *Owned State* fields at will. This offers a powerful combination of confidentiality and selectivity. For example, you can prove that a transition is valid without disclosing all the data, by providing the revealed version to the person who has to validate it, while third parties only see the hidden version (a hash). In practice, the `OpId` of a transition is always calculated from the *concealed* data.

![RGB-Bitcoin](assets/fr/067.webp)

#### Seal Definition

The *Seal Definition*, in its revealed form, has four basic fields: `txptr`, `vout`, `blinding` and `method` :


- txptr**: this is a reference to a UTXO on Bitcoin :
    - In the case of a **Genesis seal**, it points directly to an existing UTXO (the one associated with the Genesis);
    - In the case of a **Graph seal**, we can have :
        - A simple `txid`, if pointing to a specific UTXO,
        - Or a `WitnessTx`, which designates a self-reference: the seal points to the transaction itself. This is particularly useful when no external UTXO is available, for example in Lightning channel opening transactions, or if the recipient has no UTXO.
- vout** : the output number of the transaction indicated by `txptr`. Present only for a standard Graph seal (not for `WitnessTx`);
- blinding**: a random number of 8 bytes, to reinforce confidentiality and prevent brute force attempts on the UTXO's identity;
- method** : indicates the anchoring method used (`Tapret` or `Opret`).

The *concealed* form of the Seal Definition is a SHA256 hash (tagged) of the concatenation of these 4 fields, with a tag specific to RGB.

![RGB-Bitcoin](assets/fr/068.webp)

#### Owned States

The second component of *Assignment* is the Owned State. Unlike the Global State, it can exist in public or private form:


- Public Owned State**: everyone knows the data associated with the seal. For example, a public image;
- Private Owned State**: the data is hidden, known only to the owner (and potentially the validator if necessary). For example, the number of tokens held.

RGB defines four possible state types (*StateTypes*) for an Owned State:


- Declarative**: contains no numerical data, just a declarative right (e.g. a right to vote). The hidden and revealed forms are identical;
- Fungible**: represents a fungible quantity (like tokens). In revealed form, we have `amount` and `blinding`. In hidden form, we have a single *Pedersen commitment* which hides the amount and the blinding;
- Structured**: stores structured data (up to 64 kB). In revealed form, it's the data blob. In hidden form, it's a tagged hash of this blob:

```txt
SHA-256(SHA-256(tag_data) || SHA-256(tag_data) || blob)
```

With, for example :

```txt
tag_data = urn:lnp-bp:rgb:state-data#2024-02-12
```


- Attachments**: links a file (audio, image, binary, etc.) to the Owned State, storing the file hash `file_hash`, the MIME type `media type` and a cryptographic salt `salt`. The file itself is hosted elsewhere. In hidden form, it is a hash tagged with the three preceding data items:

```txt
SHA-256(SHA-256(tag_attachment) || SHA-256(tag_attachment) || file_hash || media_type || salt)
```

With, for example :

```txt
tag_attachment = urn:rgb:state-attach#2024-02-12
```

To summarize, here are the 4 possible types of state in the public and hidden form:

```txt
State                      Concealed form                              Revealed form
+---------------------------------------------------------------------------------------------------------
+--------------------------------------------------------------------------------+
|                                                                                |
Declarative        |                              < void >                                          |
|                                                                                |
+--------------------------------------------------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             |         +--------+ +----------+       |
Fungible           | | Pedersen Commitement | | <========== |         | Amount | | Blinding |       |
| +----------------------+ |             |         +--------+ +----------+       |
+--------------------------+             +---------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             |         +--------------------+        |
Structured         | |     Tagged Hash      | | <========== |         |     Data Blob      |        |
| +----------------------+ |             |         +--------------------+        |
+--------------------------+             +---------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             | +-----------+ +------------+ +------+ |
Attachments        | |     Tagged Hash      | | <========== | | File Hash | | Media Type | | Salt | |
| +----------------------+ |             | +-----------+ +------------+ +------+ |
+--------------------------+             +---------------------------------------+
```

| **Declarative** | **Fungible** | **Structured** | **Attachments** |

| --------------------- | -------------- | ------------------------------------ | ----------------------------- | ---------------------------- |

| None | 64-bit signed or unsigned integer | Any strict data type | Any file |

| Info type** | None | Signed or unsigned | Strict types | MIME type |

| Pedersen commitment | Hashing with blinding | Hashed file ID

| Size limits** | N/A | 256 bytes | Up to 64 KB | Up to ~500 Gb |

### Inputs

The Inputs of a *Contract Operation* refer to the *Assignments* that are being spent in this new operation. An Input indicates :


- prevOpId` : the identifier (`OpId`) of the previous operation where the *Assignment* was located;
- assignmentType` : the type of *Assignment* (for example, `assetOwner` for a token) ;
- `Index`: the index of the *Assignment* in the list associated with the previous `OpId`, determined after a lexicographic sorting of the hidden seals.

Inputs never appear in Genesis, since there are no previous Assignments. Nor do they appear in State Extensions (because State Extensions don't close seals; rather, they redefine new seals based on Valencies).

When we have Owned States of type `Fungible`, the validation logic (via the AluVM script provided in the Schema) checks the consistency of the sums: the sum of incoming tokens (*Inputs*) must be equal to the sum of outgoing tokens (in the new *Assignments*).

### Metadata

The **Metadata** field can be up to 64 KiB and is used to include temporary data useful for validation, but not integrated into the permanent state of the contract. For example, intermediate calculation variables for complex scripts can be stored here. This space is not intended to be stored in the global history, which is why it is outside the scope of Owned States or Global State.

### Valencies

Valencies** are an original RGB protocol mechanism. They can be found in Genesis, State Transitions or State Extensions. They represent numerical rights that can be activated by a State Extension (via *Redeems*), then finalized by a subsequent Transition. Each Valency is identified by a `ValencyType` (16 bits). Its semantics (reissue right, token swap, burn right, etc.) are defined in the Schema.

In concrete terms, we could imagine a Genesis defining a "right to reissue" valency. A State Extension will consume it (*Redeem*) if certain conditions are met, in order to introduce a new quantity of tokens. Then, a State Transition emanating from the holder of the seal thus created can transfer these new tokens.

### Redeems

Redeems are the Valency equivalent of Inputs for Assignments. They only appear in State Extensions, as this is where a previously defined Valency is activated. A Redeem consists of two fields:


- `PrevOpId` : the `OpId` of the operation where the Valency was specified;
- `ValencyType`: the type of Valency you wish to activate (each `ValencyType` can only be used once by State Extension).

Example: a Redeem can correspond to a CoinSwap execution, depending on what was coded in the Valency.

### RGB status characteristics

We're now going to take a look at several fundamental state characteristics in RGB. In particular, we'll look at :


- The **Strict Type System**, which imposes a precise and typed organization of data;
- The importance of separating **validation** from **ownership** ;
- The **consensus evolution** system in RGB, which includes the notions of *fast-forward* and *push-back*.

As always, bear in mind that everything to do with contract status is validated on the client side according to consensus rules set out in the protocol, and whose ultimate cryptographic reference is anchored in Bitcoin transactions.

#### Strict Type System

RGB uses a *Strict Type System* and a deterministic serialization mode (*Strict Encoding*). This organization is designed to guarantee perfect reproducibility and precision in the definition, handling and validation of contract data.

In many programming environments (JSON, YAML...), the data structure can be flexible, even too permissive. In RGB, on the other hand, the Structure and Types of each field are defined with explicit constraints. For example :


- Each variable has a specific type (for example, an 8-bit unsigned integer `u8`, or a 16-bit signed integer, etc.);
- Types can be composed (nested types). This means you can define a type based on other types (e.g. an aggregate type containing a `u8` field, a `bool` field, etc.);
- Collections can also be specified: lists (*list*), sets (*set*) or dictionaries (*map*), with a deterministic order of progression;
- Each field is bounded (*lower bound* / *upper bound*). We also impose limits on the number of elements in collections (containment);
- Data is byte-aligned and serialization is strictly defined and unambiguous.

Thanks to this strict encoding protocol :


- The order of the fields is always the same, regardless of the implementation or programming language used;
- The hashes calculated on the same data set are therefore reproducible and identical (strictly deterministic *commitments*);
- Boundaries prevent uncontrolled growth in data size (e.g. too many fields);
- This form of encoding facilitates cryptographic verification, as each participant knows exactly how to serialize and hash the data.

In practice, the structure (*Schema*) and the resulting code (*Interface* and associated logic) are compiled. A descriptive language is used to define the contract (types, fields, rules) and generate a strict binary format. When compiled, the result is :


- A *Memory Layout* for each field;
- Semantic identifiers (which indicate whether changing a variable name has an impact on the logic, even if the memory structure remains the same).

The strict type system also enables precise monitoring of changes: any modification to the structure (even a change of field name) is detectable and can lead to a change in the overall footprint.

Finally, each compilation produces a fingerprint, a cryptographic identifier that attests to the exact version of the code (data, rules, validation). For example, an identifier of the form :

```txt
BEiLYE-am9WhTW1-oK8cpvw4-FEMtzMrf-mKocuGZn-qWK6YF#ginger-parking-nirvana
```

This makes it possible to manage consensus or implementation updates, while ensuring detailed traceability of the versions used in the network.

To prevent the state of an RGB contract from becoming too cumbersome to validate on the client side, a consensus rule imposes a maximum size of `2^16` bytes (64 Kio) for any data involved in validation calculations. This applies to each variable or structure: no more than 65536 bytes, or the equivalent in numbers (32768 16-bit integers, etc.). This also applies to collections (lists, sets, maps), which may not exceed `2^16` elements.

This limit guarantees :


- Controls the maximum size of data to be manipulated during a state transition;
- Compatibility with the virtual machine (*AluVM*) used to run the validation scripts.

#### The Validation != Ownership paradigm

One of RGB's major innovations is the strict separation between two concepts:


- Validation**: checking that a state transition respects the rules of the contract (business logic, history, etc.);
- The **ownership** (ownership, or control): the fact of owning the Bitcoin UTXO that allows the Single-use Seal to be spent (or closed), and thus the state transition to take place.

Validation** takes place at the level of the RGB software stack (libraries, *commitments* protocol, etc.). Its role is to ensure that the internal rules of the contract (amounts, permissions, etc.) are respected. Observers or other participants can also validate the data history.

Ownership**, on the other hand, relies entirely on Bitcoin's security. Owning the private key of a UTXO means controlling the ability to launch a new transition (closing the Single-use Seal). So, even if someone can see or validate the data, they can't change the state if they don't own the UTXO concerned.

![RGB-Bitcoin](assets/fr/069.webp)

This approach limits the classic vulnerabilities encountered in more complex blockchains (where all the code of a smart contract is public and modifiable by anyone, which has sometimes led to hacks). On RGB, an attacker cannot simply interact with the on-chain state, as the right to act on the state (*ownership*) is protected by the Bitcoin layer.

What's more, this decoupling allows RGB to integrate naturally with the Lightning Network. Lightning channels can be used to engage and move RGB assets without engaging on-chain *commitments* every time. We'll take a closer look at this integration of RGB on Lightning in later chapters of the course.

#### Consensus developments in RGB

In addition to semantic code versioning, RGB includes a system for evolving or updating a contract's consensus rules over time. There are two main forms of evolution:


- Fast-forward**
- Push-back** (in French)

A fast-forward occurs when a previously invalid rule becomes valid. For example, if the contract evolves to allow a new type of `AssignmentType` or a new field :


- This cannot be compared to a classic blockchain hardfork, as RGB works in client-side validation and does not affect the overall compatibility of the blockchain ;
- In practical terms, this type of change is indicated by the `Ffv` (*fast-forward version*) field in the contract operation;
- Current holders are not harmed: their status remains valid;
- New beneficiaries (or new users), on the other hand, need to update their software (their wallet) to recognize the new rules.

A push-back means that a previously valid rule becomes invalid. It is therefore a "hardening" of the rules, but not strictly speaking a softfork:


- Existing holders may be impacted (they could find themselves with assets rendered obsolete or invalid in the new version);
- We can consider that we are in fact creating a new protocol: whoever adopts the new rule departs from the old one;
- The issuer may decide to re-issue assets in this new protocol, forcing users to maintain two separate wallets (one for the old protocol, the other for the new), if they want to manage both versions.

In this chapter on RGB contract operations, we've explored the fundamental principles underlying this protocol. As you will have noticed, the inherent complexity of the RGB protocol requires the use of many technical terms. So, in the next chapter, I'll provide you with a glossary that will summarize all the concepts covered in this first theoretical part, with definitions of all the technical terms relating to RGB. Then, in the next section, we'll take a practical look at the definition and implementation of RGB contracts.

## RGB Glossary

<chapterId>545e16a4-3cca-44a3-9fd5-dbc5868abf97</chapterId>

If you need to come back to this short glossary of important technical terms used in the RGB world (listed in alphabetical order), you'll find it useful. This chapter isn't essential if you've already understood everything we've covered in the first section.

#### AluVM

The abbreviation AluVM stands for "_Algorithmic logic unit Virtual Machine_", a register-based virtual machine designed for smart contract validation and distributed computing. It is used (but not exclusively reserved) for the validation of RGB contracts. Scripts or operations included in an RGB contract can thus be executed in the AluVM environment.

For further information: [AluVM official website](https://www.aluvm.org/)

#### Anchor

An Anchor represents a set of client-side data used to prove the inclusion of a unique _commitment_ in a transaction. In the RGB protocol, an Anchor consists of the following elements:


- The Bitcoin transaction identifier (TXID) of the **witness transaction** ;
- The **Multi Protocol Commitment (MPC)** ;
- The **Deterministic Bitcoin Commitment (DBC)**;
- The **Extra Transaction Proof (ETP)** if the **Tapret** commitment mechanism is used (see the section dedicated to this model).

An Anchor therefore serves to establish a verifiable link between a specific Bitcoin transaction and private data validated by the RGB protocol. It guarantees that these data are indeed included in the blockchain, without their exact content being publicly exposed.

#### Assignment

In RGB's logic, an Assignment is the equivalent of a transaction output that modifies, updates or creates certain properties within the state of a contract. An Assignment comprises two elements:


- A **Seal Definition** (reference to a specific UTXO) ;
- An **Owned State** (data describing the state associated with this new owner).

An Assignment therefore indicates that a portion of the state (for example, an asset) is now allocated to a particular holder, identified via a Single-use Seal linked to a UTXO.

#### Business Logic

The Business Logic groups together all the rules and internal operations of a contract, described by its **schema** (i.e. the structure of the contract itself). It dictates how the state of the contract can evolve, and under what conditions.

#### Client-side Validation

Client-side Validation refers to the process by which each party (client) verifies a set of data exchanged privately, according to the rules of a protocol. In the case of RGB, this exchanged data is grouped together in what are known as **consignments**. Unlike the Bitcoin protocol, which requires all transactions to be published on-chain, RGB allows only _commitments_ (anchored in Bitcoin) to be stored in public, while the essential contract information (transitions, attestations, proofs) remains off-chain, shared only between the users concerned.

#### Commitment

A Commitment (in the cryptographic sense) is a mathematical object, denoted `C`, derived deterministically from an operation on structured data `m` (the message) and a random value `r`. We write :

$$
C = \text{commit}(m, r)
$$

This mechanism comprises two main operations:


- Commit**: a cryptographic function is applied to a message `m` and a random number `r` to produce `C` ;
- Verify**: we use `C`, the `m` message and the `r` value to check that this commitment is correct. The function returns `True` or `False`.

A commitment must respect two properties:


- Binding**: it must be impossible to find two different messages producing the same `C` :

$$
m' : \, | \, : m' \neq m \quad \text{and} \quad r' : \, | \, : r' \neq r \quad
$$

Such as :

$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$


- Hiding**: knowledge of `C` must not reveal the contents of `m`.

In the RGB protocol, a commitment is included in a Bitcoin transaction to prove the existence of a certain piece of information at a given time, without revealing the information itself.

#### Consignment

A **Consignment** groups together the data exchanged between the parties, subject to Client-side Validation in RGB. There are two main categories of consignment:


- Contract Consignment**: supplied by the *issuer* (contract issuer), it includes initialization information such as Schema, Genesis, Interface and Interface Implementation.
- Transfer Consignment**: supplied by the paying party (*payer*). It contains the entire history of state transitions leading up to the terminal consignment (i.e. the final state received by the payer).

These consignments are not recorded publicly on the blockchain; they are exchanged directly between the parties concerned via the communication channel of their choice.

#### Contract

A Contract is a set of rights executed digitally between several actors via the RGB protocol. It has an active state and a business logic, defined by a Schema, which specifies which operations are authorized (transfers, extensions, etc.). The state of a contract, as well as its validity rules, are expressed in the Schema. At any given time, the contract evolves only in accordance with what is permitted by this Schema and by validation scripts (run, for example, in AluVM).

#### Contract Operation

A Contract Operation is a contract status update performed according to Schema rules. The following operations exist in RGB:


- State Transition** ;
- Genesis** ;
- State Extension**.

Each operation modifies the state by adding or replacing certain data (Global State, Owned State...).

#### Contract Participant

A Contract Participant is an actor who takes part in operations relating to the contract. In RGB, a distinction is made between :


- The issuer of the contract, which creates the Genesis (the origin of the contract);
- The contract parties, i.e. the holders of rights to the state of the contract;
- Public parties, who can build State Extensions if the contract offers Valencies accessible to the public.

#### Contract Rights

Contract Rights refer to the various rights that can be exercised by those involved in an RGB contract. They fall into several categories:


- Ownership rights**, associated with the ownership of a particular UTXO (via a _Seal Definition_);
- Executive rights**, i.e. the ability to build one or more transitions (State Transitions) in accordance with the Schema ;
- Public rights**, when the Schema authorizes certain public uses, for example the creation of a State Extension via the redemption of a Valency.

#### Contract State

The Contract State corresponds to the current state of a contract at a given moment. It can be made up of both public and private data, reflecting the state of the contract. RGB distinguishes between :


- The **Global State**, which includes the contract's public properties (set up in Genesis or added via authorized updates);
- Owned States**, which belong to specific owners, identified by their UTXOs.

#### Deterministic Bitcoin Commitment - DBC

Deterministic Bitcoin Commitment (DBC) is the set of rules used to provably and uniquely register a _commitment_ in a Bitcoin transaction. In the RGB protocol, there are two main forms of DBC:


- Opret**
- Tapret**

These mechanisms define precisely how the _commitment_ is encoded in the output or structure of a Bitcoin transaction, to ensure that this commitment is deterministically traceable and verifiable.

#### Directed Acyclic Graph - DAG

A DAG (or *Acyclic Guided Graph*) is a cycle-free graph, enabling topological scheduling. Blockchains, like the _shards_ of RGB contracts, can be represented by DAGs.

For further information: [Directed Acyclic Graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph)

#### Engraving

Engraving is an optional data string that successive owners of a contract can enter into the contract history. This feature exists, for example, in the **RGB21** interface and enables commemorative or descriptive information to be added to the contract history.

#### Extra Transaction Proof - ETP

The ETP (*Extra Transaction Proof*) is the part of the Anchor that contains the additional data required to validate a **Tapret** *commitment* (in the context of _taproot_). It includes, among other things, the taproot script's internal public key (_internal PubKey_) and information specific to the _Script Path Spend_.

#### Genesis

Genesis refers to the set of data, governed by a Schema, that forms the initial state of any contract in RGB. It can be compared to Bitcoin's _Genesis Block_ concept, or to the Coinbase transaction concept, but here at the _client-side_ and RGB token level.

#### Global State

The Global State is the set of public properties contained in the Contract State. It is defined at Genesis and, depending on the contract rules, can be updated by authorized transitions. Unlike Owned States, the Global State does not belong to a particular entity; it is closer to a public registry within the contract.

#### Interface

The Interface is the set of instructions used to decode the binary data compiled in a Schema or in contract operations and their states, in order to make them readable for the user or his wallet. It acts as an interpretation layer.

#### Interface Implementation

Interface Implementation is the set of declarations that link an **Interface** to a **Schema**. It enables the semantic translation performed by the Interface itself, so that the raw data of a contract can be understood by the user or the software involved (the wallets).

#### Invoice

An Invoice takes the form of a URL encoded in [base58](https://en.wikipedia.org/wiki/Binary-to-text_encoding#Base58), which embeds the data necessary for the construction of a **State Transition** (by the payer). In other words, it's an invoice enabling the counterparty (*payer*) to create the corresponding transition to transfer the asset or update the state of the contract.

#### Lightning Network

The Lightning Network is a decentralized network of payment channels (or _state channels_) on Bitcoin, made up of 2/2 multi-signature wallets. It enables fast, low-cost _off-chain_ transactions, while relying on Bitcoin's Layer 1 for arbitration (or closure) when necessary.

For more information on how Lightning works, I recommend you take this other course:

https://planb.network/courses/lnp201
#### Multi Protocol Commitment - MPC

Multi Protocol Commitment (MPC) refers to the Merkle tree structure used in RGB to include, within a single Bitcoin transaction, several **Transition Bundles** from different contracts. The idea is to group together several commitments (potentially corresponding to different contracts or different assets) in a single anchor point in order to optimize the occupation of block space.

#### Owned State

An Owned State is the part of a Contract State that is enclosed in an Assignment and associated with a particular holder (via a Single-use Seal pointing to a UTXO). This represents, for example, a digital asset or a specific contractual right assigned to that person.

#### Ownership

Ownership refers to the ability to control and spend a UTXO referenced by a Seal Definition. When an Owned State is linked to a UTXO, the owner of this UTXO has the right, potentially, to transfer or evolve the associated state, according to the rules of the contract.

#### Partially Signed Bitcoin Transaction - PSBT

A PSBT (_Partially Signed Bitcoin Transaction_) is a Bitcoin transaction that is not yet fully signed. It can be shared between several entities, each of which can add or verify certain elements (signatures, scripts...), until the transaction is deemed ready for on-chain distribution.

For further information: [BIP-0174](https://github.com/bitcoin/bips/blob/master/bip-0174.mediawiki)

#### Pedersen commitment

A Pedersen commitment is a type of cryptographic commitment with the property of being **homomorphic** with respect to the addition operation. This means that it is possible to validate the sum of two commitments without revealing the individual values.

Formally, if :

$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$

then :

$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$

This property is useful, for example, for concealing the amounts of tokens exchanged, while still being able to verify the totals.

Further information: [Pedersen commitment](https://link.springer.com/chapter/10.1007/3-540-46766-1_9)

#### Redeem

In a State Extension, a Redeem refers to the action of reclaiming (or exploiting) a previously declared **Valency**. As a Valency is a public right, the Redeem allows an authorized participant to claim a specific contract state extension.

#### Schema

A Schema in RGB is a declarative piece of code describing the set of variables, rules and business logic (*Business Logic*) that govern the operation of a contract. The Schema defines the state structure, the types of transitions allowed and the validation conditions.

#### Seal Definition

The Seal Definition is the part of an Assignment that associates the _commitment_ with a UTXO owned by the new holder. In other words, it indicates where the condition is located (in which UTXO), and establishes ownership of an asset or right.

#### Shard

A Shard represents a branch in the DAG of the State Transitions history of an RGB contract. In other words, it is a coherent subset of the contract's overall history, corresponding, for example, to the sequence of transitions required to prove the validity of a given asset since the _Genesis_.

#### Single-use Seal

A Single-use Seal is a cryptographic promise of commitment to an as yet unknown message, which will be revealed only once in the future and must be known by all members of a specific audience. The aim is to prevent the creation of multiple competing commitments for the same seal.

#### Stash

The Stash is the set of client-side data that a user stores for one or more RGB contracts, for the purpose of validation (*Client-side Validation*). This includes transition history, consignments, proofs of validity, etc. Each holder retains only the parts of the history they need (*shards*).

#### State Extension

A State Extension is a contract operation used to re-trigger state updates by redeeming previously declared **Valencies**. To be effective, a State Extension must then be closed by a State Transition (which updates the final state of the contract).

#### State Transition

State Transition is the operation that changes the state of an RGB contract to a new state. It can modify Global State and/or Owned State data. In practice, each transition is verified by Schema rules and anchored in the Bitcoin blockchain via a _commitment_.

#### Taproot

Refers to Bitcoin's Segwit v1 transaction format, introduced by [BIP341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki) and [BIP342](https://github.com/bitcoin/bips/blob/master/bip-0342.mediawiki). Taproot improves the confidentiality and flexibility of scripts, in particular by making transactions more compact and harder to distinguish from one another.

#### Terminal Consignment - Consignment Endpoint

The Terminal Consignment (or _Consignment Endpoint_) is a *transfer consignment* containing the final state of the contract, including the State Transition created from the recipient's Invoice (*payee*). It is therefore the endpoint of a transfer, with the necessary data to prove that ownership or state has been transferred.

#### Transition Bundle

A Transition Bundle is a set of RGB State Transitions (belonging to the same contract) that are all engaged in the same ***witness transaction*** Bitcoin. This makes it possible to bundle several updates or transfers into a single on-chain anchor.

#### UTXO

A Bitcoin UTXO (*Unspent Transaction Output*) is defined by the hash of a transaction and the output index (*vout*). It is also sometimes called an _outpoint_. In the RGB protocol, reference to an UTXO (via a **Seal Definition**) enables the location of the **Owned State**, i.e. the property held on the blockchain.

#### Valency

A Valency is a public right which does not require state storage as such, but which can be redeemed via a **State Extension**. It is therefore a form of possibility open to all (or certain players), declared in the logic of the contract, in order to carry out a particular extension at a later date.

#### Witness Transaction

The Witness Transaction is the Bitcoin transaction that closes the Single-use Seal around a message containing a Multi Protocol Commitment (MPC). This transaction spends a UTXO or creates one, so as to seal the commitment linked to the RGB protocol. It acts as an on-chain proof that the state has been set at a specific point in time.

# Programming on RGB

<partId>148a7436-d079-56d9-be08-aaa4c14c6b3a</partId>

## Implementing RGB contracts

<chapterId>8333ea5f-51c7-5dd5-b1d7-47d491e58e51</chapterId>

![video](https://youtu.be/Uo1UoxiImsI)

In this chapter, we'll take a closer look at how an RGB contract is defined and implemented. We'll see what the components of an RGB contract are, what their roles are and how they are constructed.

### The components of an RGB contract

So far, we've already discussed the **Genesis**, which represents the starting point of a contract, and we've seen how it fits in with the logic of a *Contract Operation* and the state of the protocol. The complete definition of an RGB contract, however, is not limited to the Genesis alone: it involves three complementary components which, together, form the heart of the implementation.

The first component is called the **Schema**. This is a file describing the fundamental structure and business logic (*business logic*) of the contract. It specifies the data types used, the validation rules, the operations permitted (e.g. initial token issuance, transfers, special conditions, etc.) - in short, the general framework that dictates how the contract works.

The second component is the **Interface**. It focuses on how users (and by extension, portfolio software) will interact with this contract. It describes the semantics, i.e. the readable representation of the various fields and actions. So, while the Schema defines how the contract works technically, the Interface defines how to present and expose these functionalities: method names, data display, etc.

The third component is the **Interface Implementation**, which complements the previous two by acting as a kind of bridge between the Schema and the Interface. In other words, it associates the semantics expressed by the Interface with the underlying rules defined in the Schema. It is this implementation that will manage, for example, the conversion between a parameter entered in the wallet and the binary structure imposed by the protocol, or the compilation of validation rules in machine language.

This modularity is an interesting feature of RGB, as it allows different groups of developers to work separately on these aspects (*Schema*, *Interface*, *Implementation*), as long as they follow the protocol's consensus rules.

To sum up, each contract consists of :


- Genesis**, which is the initial state of the contract (and can be likened to a special transaction defining the first ownership of an asset, a right, or any other parameterizable data);
- Schema**, which describes the contract's business logic (data types, validation rules, etc.);
- Interface**, which provides a semantic layer for both wallets and human users, clarifying the reading and execution of transactions;
- Implementation** interface, which bridges the gap between business logic and presentation, to ensure that contract definition is consistent with the user experience.

![RGB-Bitcoin](assets/fr/070.webp)

It's important to note that for a wallet to manage an RGB asset (be it a fungible token or a right of any kind), it must have all these elements compiled: *Schema*, *Interface*, *Interface Implementation* and *Genesis*. This is transmitted via a ***contract consignment***, i.e. a data package containing everything needed to validate the client-side contract.

To help clarify these notions, here is a summary table comparing the components of an RGB contract with concepts already known either in object-oriented programming (OOP) or in the Ethereum ecosystem:

| RGB Contract Component | Meaning | OOP Equivalent | Ethereum Equivalent |

| ---------------------------- | --------------------------------------- | -------------------------------------------------- | ---------------------------------- |

| Class constructor | Contract constructor | Initial state of the contract

| Class | Contract business logic

| Contract semantics | Interface (Java) / trait (Rust) / protocol (Swift) | ERC Standard |

| Application Binary Interface (ABI) | Impl (Rust) / Implements (Java) | Mapping of semantics and logic

The left-hand column shows the elements specific to the RGB protocol. The middle column shows the concrete function of each component. Then, in the "OOP equivalent" column, we find the equivalent term in object-oriented programming:


- The **Genesis** plays a role similar to that of a *Class constructor*: this is where the state of the contract is initialized;
- The **Schema** is the description of a class, i.e. the definition of its properties, methods and underlying logic;
- The **Interface** corresponds to *interfaces* (Java), *traits* (Rust) or *protocols* (Swift): these are the public definitions of functions, events, fields... ;
- The **Interface Implementation** corresponds to *Impl* in Rust or *Implements* in Java, where we specify how the code will actually execute the methods announced in the interface.

In the Ethereum context, the Genesis is closer to the *contract constructor*, the Schema to the contract definition, the Interface to a standard such as ERC-20 or ERC-721, and the Interface Implementation to the ABI (*Application Binary Interface*), which specifies the format of interactions with the contract.

The advantage of RGB's modularity also lies in the fact that different stakeholders can write, for example, their own Interface Implementation, as long as they respect the logic of the *Schema* and the semantics of the *Interface*. Thus, an issuer could develop a new, more user-friendly front-end (Interface), without modifying the logic of the contract, or conversely, one could extend the Schema to add functionality, and provide a new version of the adapted Interface Implementation, while the old implementations would remain valid for basic functionality.

When we compile a new contract, we generate a Genesis (the first step in issuing or distributing the asset), as well as its components (Schema, Interface, Interface Implementation). After this, the contract is fully operational and can be propagated to wallets and users. This method, where Genesis is combined with these three components, guarantees a high degree of customization (each contract can have its own logic), decentralization (everyone can contribute to a given component), and security (validation remains strictly defined by the protocol, without depending on arbitrary on-chain code as is often the case on other blockchains).

I'd now like to take a closer look at each of these components: the **Schema**, the **Interface** and the **Interface Implementation**.

### Schema

In the previous section, we saw that in the RGB ecosystem, a contract is made up of several elements: the Genesis, which establishes the initial state, and several other complementary components. The purpose of the Schema is to declaratively describe all the business logic of the contract, i.e. the data structure, the types used, the permitted operations and their conditions. It is therefore a very important element in making a contract operational on the client side, since each participant (a wallet, for example) must check that the state transitions it receives conform to the logic defined in the Schema.

A Schema can be likened to a "class" in object-oriented programming (OOP). Generally speaking, it serves as a model defining the components of a contract, such as :


- The different types of Owned States and Assignments ;
- Valencies, i.e. special rights that can be triggered (*redeemed*) for certain operations;
- Global State fields, which describe global, public and shared properties of the contract;
- The Genesis structure (the very first operation that activates the contract) ;
- The permitted forms of State Transitions and State Extensions, and how these operations can modify the ;
- Metadata associated with each operation, to store temporary or additional information;
- Rules that determine how internal contract data can evolve (for example, whether a field is mutable or cumulative);
- Sequences of operations considered valid: for example, an order of transitions to be respected or a set of logical conditions to be satisfied.

![RGB-Bitcoin](assets/fr/071.webp)

When the *issuer* of an asset on RGB publishes a contract, it provides the Genesis and Schema associated with it. Users or wallets who wish to interact with the asset retrieve this Schema to understand the logic behind the contract, and to be able to verify later that the transitions they will participate in are legitimate.

The first step, for anyone receiving information about an RGB asset (e.g. a token transfer), is to validate this information against the Schema. This involves using the Schema compilation to :


- Check that Owned States, Assignments and other elements are correctly defined and that they respect the imposed types (the so-called *strict type system*);
- Check that transition rules (validation scripts) are satisfied. These scripts can be run via AluVM, which is present on the client side and is responsible for validating the consistency of business logic (transfer amount, special conditions, etc.).

In practice, Schema is not executable code, as can be seen in blockchains that store on-chain code (EVM on Ethereum). On the contrary, RGB separates business logic (declarative) from executable code on the blockchain (which is limited to cryptographic anchors). Thus, the Schema determines the rules, but the application of these rules takes place outside the blockchain, at each participant's site, according to the Client-side Validation principle.

A Schema must be compiled before it can be used by RGB applications. This compilation produces a binary file (e.g. `.rgb`) or an encrypted binary file (`.rgba`). When the wallet imports this file, it knows :


- What each data type (integers, structures, arrays...) looks like thanks to the strict type system ;
- How Genesis should be structured (to understand asset initialization);
- The different types of operations (State Transitions, State Extensions) and how they can modify state ;
- The scripting rules (introduced in the Schema) that the AluVM engine will apply to check the validity of operations.

As explained in previous chapters, the *strict type system* gives us a stable, deterministic encoding format: all variables, whether Owned States, Global States or Valencies, are described precisely (size, lower and upper bounds if necessary, signed or unsigned type, etc.). It is also possible to define nested structures, for example to support complex use cases.

Optionally, the Schema can reference a root `SchemaId`, which facilitates the reuse of an existing basic structure (a template). In this way, you can evolve a contract or create variations (e.g. a new type of token) from an already proven template. This modularity avoids the need to recreate entire contracts, and encourages the standardization of best practices.

Another important point is that the logic of state evolution (transfers, updates, etc.) is described in the Schema in the form of scripts, rules and conditions. So, if the contract designer wishes to authorize a reissue or impose a burn mechanism (destruction of tokens), he can specify the corresponding scripts for AluVM in the validation part of the Schema.

#### Difference from programmable on-chain blockchains

Unlike systems like Ethereum, where the smart contract code (executable) is written into the blockchain itself, RGB stores the contract (its logic) off-chain, in the form of a compiled declarative document. This implies that :


- There is no Turing-complete VM running in every node of the Bitcoin network. The rules of an RGB contract are not executed on the blockchain, but in each user who wishes to validate a state;
- Contract data does not pollute the blockchain: only cryptographic evidence (*commitments*) is embedded in Bitcoin transactions (via `Tapret` or `Opret`);
- The Schema can be updated or declined (*fast-forward*, *push-back*, etc.), without requiring a fork on the Bitcoin blockchain. Wallets simply need to import the new Schema and adapt to consensus changes.

#### Use by the issuer and by users

When a *issuer* creates an asset (for example, a non-inflationary fungible token), it prepares :


- A Schema describing the rules of emission, transfer, etc. ;
- A Genesis adapted to this Schema (with the total number of tokens issued, the identity of the initial owner, any special Valencies for reissue, etc.).

It then makes the compiled Schema (a `.rgb` file) available to users, so that anyone receiving a transfer of this token can check the consistency of the operation locally. Without this Schema, a user would not be able to interpret the status data or check that it complies with the contract rules.

So when a new wallet wants to support an asset, it simply needs to integrate the relevant Schema. This mechanism makes it possible to add compatibility to new RGB asset types, without invasively changing the wallet's software base: all that's required is to import the Schema binary and understand its structure.

The Schema defines the business logic in RGB. It lists the evolution rules of a contract, the structure of its data (Owned States, Global State, Valencies) and the associated validation scripts (executable by AluVM). Thanks to this declarative document, the definition of a contract (compiled file) is clearly separated from the actual execution of the rules (client-side). This decoupling gives RGB great flexibility, enabling a wide range of use cases (fungible tokens, NFT, more sophisticated contracts) while avoiding the complexity and flaws typical of programmable on-chain blockchains.

#### Schema example

Let's take a look at a concrete example of Schema for an RGB contract. This is an extract in Rust from the file `nia.rs` (initials for "*Non-Inflatable Assets*"), which defines a model for fungible tokens that cannot be reissued beyond their initial supply (a non-inflationary asset). This type of token can be seen as the equivalent, in the RGB universe, of the ERC20 on Ethereum, i.e. fungible tokens that respect certain basic rules (e.g. on transfers, supply initialization, etc.).

Before diving into the code, it's worth recalling the general structure of an RGB Schema. There is a series of declarations framing :


- A possible `SchemaId` indicating the use of another basic Schema as a template;
- The **Global States** and **Owned States** (with their strict types) ;
- Valencies** (if any);
- The **Operations** (Genesis, State Transitions, State Extensions) that can reference these states and valencies;
- The **Strict Type System** used to describe and validate data;
- Validation scripts** (run via AluVM).

![RGB-Bitcoin](assets/fr/072.webp)

The code below shows the complete definition of the Rust Schema. We will comment it part by part, following the annotations (1) to (9) below:

```rust
// ===== PART 1: Function Header and SubSchema =====
fn nia_schema() -> SubSchema {
// definitions of libraries and variables
// ===== PART 2: General Properties (ffv, subset_of, type_system) =====
Schema {
ffv: zero!(),
subset_of: None,
type_system: types.type_system(),
// ===== PART 3: Global States =====
global_types: tiny_bmap! {
GS_NOMINAL => GlobalStateSchema::once(types.get("RGBContract.DivisibleAssetSpec")),
GS_DATA => GlobalStateSchema::once(types.get("RGBContract.ContractData")),
GS_TIMESTAMP => GlobalStateSchema::once(types.get("RGBContract.Timestamp")),
GS_ISSUED_SUPPLY => GlobalStateSchema::once(types.get("RGBContract.Amount")),
},
// ===== PART 4: Owned Types =====
owned_types: tiny_bmap! {
OS_ASSET => StateSchema::Fungible(FungibleType::Unsigned64Bit),
},
// ===== PART 5: Valencies =====
valency_types: none!(),
// ===== PART 6: Genesis: Initial Operations =====
genesis: GenesisSchema {
metadata: Ty::<SemId>::UNIT.id(None),
globals: tiny_bmap! {
GS_NOMINAL => Occurrences::Once,
GS_DATA => Occurrences::Once,
GS_TIMESTAMP => Occurrences::Once,
GS_ISSUED_SUPPLY => Occurrences::Once,
},
assignments: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
valencies: none!(),
},
// ===== PART 7: Extensions =====
extensions: none!(),
// ===== PART 8: Transitions: TS_TRANSFER =====
transitions: tiny_bmap! {
TS_TRANSFER => TransitionSchema {
metadata: Ty::<SemId>::UNIT.id(None),
globals: none!(),
inputs: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
assignments: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
valencies: none!(),
}
},
// ===== PART 9: Script AluVM and Entry Points =====
script: Script::AluVM(AluScript {
libs: confined_bmap! { alu_id => alu_lib },
entry_points: confined_bmap! {
EntryPoint::ValidateGenesis => LibSite::with(FN_GENESIS_OFFSET, alu_id),
EntryPoint::ValidateTransition(TS_TRANSFER) => LibSite::with(FN_TRANSFER_OFFSET, alu_id),
},
}),
}
}
```


- (1) - Function header and SubSchema**

The `nia_schema()` function returns a `SubSchema`, indicating that this Schema can partially inherit from a more generic schema. In the RGB ecosystem, this flexibility makes it possible to reuse certain standard elements of a master schema, and then define rules specific to the contract in question. Here, we choose not to enable inheritance, since `subset_of` will be `None`.


- (2) - General properties: ffv, subset_of, type_system**

The `ffv` property corresponds to the *fast-forward* version of the contract. A value of `zero!()` here indicates that we are at version 0 or the initial version of this schema. If you later wish to add new functionalities (new type of operation, etc.), you can increment this version to indicate a consensus change.

The `subset_of: None` property confirms the absence of inheritance. The `type_system` field refers to the strict type system already defined in the `types` library. This line indicates that all data used by the contract uses the strict serialization implementation provided by the library in question.


- (3) - Global States

In the `global_types` block, we declare four elements. We use the key, such as `GS_NOMINAL` or `GS_ISSUED_SUPPLY`, to reference them later:


- `GS_NOMINAL` refers to a `DivisibleAssetSpec` type, which describes various fields of the created token (full name, ticker, precision...);
- `GS_DATA` represents general data, such as a disclaimer, metadata, or other text;
- `GS_TIMESTAMP` refers to an issue date;
- `GS_ISSUED_SUPPLY` sets the total supply, i.e. the maximum number of tokens that can be created.

The keyword `once(...)` means that each of these fields can only appear once.


- (4) - Owned Types

In `owned_types`, we declare `OS_ASSET`, which describes a fungible state. We use `StateSchema::Fungible(FungibleType::Unsigned64Bit)`, indicating that the quantity of assets (tokens) is stored as a 64-bit unsigned integer. Thus, any transaction will send a certain amount of units of this token, which will be validated according to this strictly typed numerical structure.


- (5) - Valencies**

We indicate `valency_types: none!()`, which means that there are no Valencies in this schema, in other words no special or extra rights (such as reissue, conditional burn, etc.). If a schema included any, they would be declared in this section.


- (6) - Genesis: first operations

Here we enter the part that declares Contract Operations. The Genesis is described by :


- The absence of `metadata` (field `metadata: Ty::<SemId>::UNIT.id(None)`) ;
- Global States which must be present once each (`Once`);
- An Assignments list where `OS_ASSET` must appear `OnceOrMore`. This means that Genesis requires at least one `OS_ASSET` Assignment (an initial holder);
- No Valency : `valencies: none!()`.

This is how we limit the definition of the initial token issue: we must declare the supply issued (`GS_ISSUED_SUPPLY`), plus at least one holder (an Owned State of type `OS_ASSET`).


- (7) - Extensions

The `extensions: none!()` field indicates that no State Extension is foreseen in this contract. This means that there is no operation to redeem a digital right (Valency) or to perform a state extension before a Transition. Everything is done via Genesis or State Transitions.


- (8) - Transitions: TS_TRANSFER

In `transitions`, we define the `TS_TRANSFER` type of operation. We explain that :


- It has no metadata;
- It does not modify the Global State (which is already defined in Genesis);
- It takes one or more `OS_ASSETs` as inputs. This means it must spend existing Owned States;
- It creates (`assignments`) at least one new `OS_ASSET` (in other words, the recipient or recipients receive tokens) ;
- It generates no new Valency.

This models the behavior of a basic transfer, which consumes tokens on a UTXO, then creates new Owned States in favor of the recipients, and thus preserves the equality of the total amount between inputs and outputs.


- (9) - AluVM script and Entry Points** (in French)

Finally, we declare an AluVM script (`Script::AluVM(AluScript { ... })`). This script contains :


- One or more external libraries (`libs`) to be used during validation;
- Entry points pointing to function offsets in the AluVM code, corresponding to validation of the Genesis (`ValidateGenesis`) and each declared Transition (`ValidateTransition(TS_TRANSFER)`).

This validation code is responsible for applying business logic. For example, it will check :


- That the `GS_ISSUED_SUPPLY` is not exceeded during Genesis ;
- That the sum of `inputs` (tokens spent) equals the sum of `assignments` (tokens received) for `TS_TRANSFER`.

If these rules are not respected, the transition will be considered invalid.

This example of a "*Non Inflatable Fungible Asset*" Schema gives us a better understanding of the structure of a simple RGB fungible token contract. We can clearly see the separation between data description (Global and Owned States), operation declaration (Genesis, Transitions, Extensions) and validation implementation (AluVM scripts). Thanks to this model, a token behaves like a classic fungible token, but remains validated on the client side and does not depend on the on-chain infrastructure to execute its code. Only cryptographic commitments are anchored in the Bitcoin blockchain.

### Interface

The interface is the layer designed to make a contract readable and manipulable, both by users (human reading) and by portfolios (software reading). The Interface therefore plays a role comparable to that of an interface in an object-oriented programming language (Java, Rust trait, etc.), in that it exposes and clarifies the functional structure of a contract, without necessarily revealing the internal details of the business logic.

Unlike Schema, which is purely declarative and compiled into a binary file that is difficult to use as is, Interface provides the reading keys needed to :


- List and describe the Global States and Owned States included in the contract;
- Access the names and values of each field, so that they can be displayed (e.g. for a token, find out its ticker, maximum amount, etc.);
- Interpret and construct Contract Operations (Genesis, State Transition, or State Extension) by associating data with understandable names (e.g., perform a transfer by clearly specifying "amount" rather than a binary identifier).

![RGB-Bitcoin](assets/fr/073.webp)

Thanks to the Interface, you can, for example, write code in a wallet which, instead of manipulating fields, directly manipulates labels such as "number of tokens", "asset name", etc. This way, managing a contract becomes more intuitive. In this way, contract management becomes more intuitive.

#### General operation

This method has many advantages:


- Standardization:**

The same type of contract can be supported by a standard Interface, shared between several wallet implementations. This facilitates compatibility and code reuse.


- Clear separation between Schema and Interface:**

In RGB design, Schema (business logic) and Interface (presentation and manipulation) are two independent entities. The developers who write the contract logic can concentrate on the Schema, without worrying about ergonomics or data representation, while another team (or the same team, but on a different timeline) can develop the Interface.


- Flexible evolution:**

The Interface can be modified or added to after the asset has been issued, without having to change the contract itself. This is a major difference from some on-chain smart contract systems, where the Interface (often mixed with the execution code) is frozen in the blockchain.


- Multi-interface capability

The same contract could be exposed through different Interfaces adapted to distinct needs: a simple Interface for the end-user, another more advanced one for the issuer who needs to manage complex configuration operations. The wallet can then choose which Interface to import, depending on its use.

![RGB-Bitcoin](assets/fr/074.webp)

In practice, when the wallet retrieves an RGB contract (via a `.rgb` or `.rgba` file), it also imports the associated Interface, which is also compiled. At runtime, the wallet can, for example :


- Browse the list of states and read their names, to display Ticker, Initial Amount, Issue Date, etc. on the user interface, rather than an unreadable numeric identifier;
- Build an operation (such as a transfer) using explicit parameter names: instead of writing `assignments { OS_ASSET => 1 }`, it can offer the user an "Amount" field in a form, and translate this information into the strictly typed fields expected by the contract.

#### Difference from Ethereum and other systems

On Ethereum, the Interface (described via the ABI, *Application Binary Interface*) is generally derived from on-chain stored code (the smart contract). It can be costly or complicated to modify a specific part of the interface without touching the contract itself. However, RGB is based on an entirely off-chain logic, with data anchored in *commitments* on Bitcoin. This design makes it possible to modify the Interface (or its implementation) without impacting the fundamental security of the contract, as the validation of the business rules remains in the Schema and the referenced AluVM code.

#### Interface compilation

As with Schema, the Interface is defined in source code (often in Rust) and compiled into a `.rgb` or `.rgba` file. This binary file contains all the information required by the wallet to :


- Identify fields by name ;
- Link each field (and its value) to the strict system type defined in the contract;
- Know the different operations allowed and how to build them.

Once the Interface has been imported, the wallet can correctly display the contract and propose interactions to the user.

### Interfaces standardized by the LNP/BP association

In the RGB ecosystem, an Interface is used to give a readable and manipulable meaning to the data and operations of a contract. The Interface thus complements the Schema, which describes the business logic internally (strict types, validation scripts, etc.). In this section, we'll take a look at the standard Interfaces developed by the LNP/BP association for common contract types (fungible tokens, NFT, etc.).

As a reminder, the idea is that each Interface describes how to display and manipulate a contract on the wallet side, clearly naming the fields (such as `spec`, `ticker`, `issuedSupply`...) and defining the possible operations (such as `Transfer`, `Burn`, `Rename`...). Several Interfaces are already operational, but there will be more and more in the future.

#### Some ready-to-use interfaces

**RGB20** is the Interface for fungible assets, which can be compared to Ethereum's ERC20 standard. However, it goes a step further, offering more extensive functionality:


- For example, the ability to rename the asset (change of *ticker* or full name) after it has been issued, or to adjust its precision (*stock splits*);
- It can also describe mechanisms for secondary reissuance (limited or unlimited) and for burn and then replacement, in order to authorize the issuer to destroy and then recreate assets under certain conditions;

For example, the RGB20 Interface can be linked to the **Non-Inflatable Asset (NIA) scheme**, which imposes a non-inflatable initial supply, or to other more advanced schemes as required.

**RGB21** concerns NFT-type contracts, or more broadly, any unique digital content, such as the representation of digital media (images, music, etc.). In addition to describing the issue and transfer of a single asset, it includes features such as :


- Integrated support for direct inclusion of a file (up to 16 MB) in the contract (for client-side retrieval);
- The possibility for the owner to enter a "*engraving*" in the history to prove past ownership of an NFT.

**RGB25** is a hybrid standard combining fungible and non-fungible aspects. It is designed for partially fungible assets, such as real estate tokenization, where you want to split up a property while retaining a link to a single root asset (in other words, you have fungible pieces of a house, linked to a non-fungible house). Technically, this interface can be linked to the **Collectible Fungible Asset* (CFA)** schema, which takes into account the notion of splitting while tracing the original asset.

#### Interfaces under development

Other Interfaces are planned for more specialized uses, but are not yet available:


- RGB22**, dedicated to digital identities, to manage identifiers and on-chain profiles in the RGB ecosystem;
- RGB23**, for advanced time stamping, using some of the ideas of *Opentimestamps*, but with traceability features;
- RGB24**, which aims for the equivalent of a decentralized domain name system (DNS) similar to the *Ethereum Name Service* ;
- RGB26**, designed to manage DAOs (*Decentralized Autonomous Organization*) in a more complex format (governance, voting, etc.);
- RGB30**, very similar to RGB20 but with the particularity of taking into account decentralized initial issuance and using State Extensions. This would be used for assets whose re-issuance is managed by several entities, or subject to finer conditions.

Of course, depending on the date on which you consult this course, these interfaces may already be operational and accessible.

#### Interface example

This Rust code snippet shows a [RGB20](https://github.com/RGB-WG/rgb-std/blob/master/src/interface/rgb20.rs) Interface (fungible asset). This code is taken from the `rgb20.rs` file in the standard RGB library. Let's take a look at it to understand the structure of an Interface and how it provides a bridge between, on the one hand, the business logic (defined in the Schema) and, on the other, the functionalities exposed to wallets and users.

```rust
// ...
fn rgb20() -> Iface {
let types = StandardTypes::with(rgb20_stl());
Iface {
version: VerNo::V1,
name: tn!("RGB20"),
global_state: tiny_bmap! {
fname!("spec") => GlobalIface::required(types.get("RGBContract.DivisibleAssetSpec")),
fname!("data") => GlobalIface::required(types.get("RGBContract.ContractData")),
fname!("created") => GlobalIface::required(types.get("RGBContract.Timestamp")),
fname!("issuedSupply") => GlobalIface::one_or_many(types.get("RGBContract.Amount")),
fname!("burnedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
fname!("replacedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
},
assignments: tiny_bmap! {
fname!("inflationAllowance") => AssignIface::public(OwnedIface::Amount, Req::NoneOrMore),
fname!("updateRight") => AssignIface::public(OwnedIface::Rights, Req::Optional),
fname!("burnEpoch") => AssignIface::public(OwnedIface::Rights, Req::Optional),
fname!("burnRight") => AssignIface::public(OwnedIface::Rights, Req::NoneOrMore),
fname!("assetOwner") => AssignIface::private(OwnedIface::Amount, Req::NoneOrMore),
},
valencies: none!(),
genesis: GenesisIface {
metadata: Some(types.get("RGBContract.IssueMeta")),
global: tiny_bmap! {
fname!("spec") => ArgSpec::required(),
fname!("data") => ArgSpec::required(),
fname!("created") => ArgSpec::required(),
fname!("issuedSupply") => ArgSpec::required(),
},
assignments: tiny_bmap! {
fname!("assetOwner") => ArgSpec::many(),
fname!("inflationAllowance") => ArgSpec::many(),
fname!("updateRight") => ArgSpec::optional(),
fname!("burnEpoch") => ArgSpec::optional(),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_RESERVES
},
},
transitions: tiny_bmap! {
tn!("Transfer") => TransitionIface {
optional: false,
metadata: None,
globals: none!(),
inputs: tiny_bmap! {
fname!("previous") => ArgSpec::from_non_empty("assetOwner"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_non_empty("assetOwner"),
},
valencies: none!(),
errors: tiny_bset! {
NON_EQUAL_AMOUNTS
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("Issue") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.IssueMeta")),
globals: tiny_bmap! {
fname!("issuedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_non_empty("inflationAllowance"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
fname!("future") => ArgSpec::from_many("inflationAllowance"),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
ISSUE_EXCEEDS_ALLOWANCE,
INSUFFICIENT_RESERVES
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("OpenEpoch") => TransitionIface {
optional: true,
metadata: None,
globals: none!(),
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnEpoch"),
},
assignments: tiny_bmap! {
fname!("next") => ArgSpec::from_optional("burnEpoch"),
fname!("burnRight") => ArgSpec::required()
},
valencies: none!(),
errors: none!(),
default_assignment: Some(fname!("burnRight")),
},
tn!("Burn") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.BurnMeta")),
globals: tiny_bmap! {
fname!("burnedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnRight"),
},
assignments: tiny_bmap! {
fname!("future") => ArgSpec::from_optional("burnRight"),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_COVERAGE
},
default_assignment: None,
},
tn!("Replace") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.BurnMeta")),
globals: tiny_bmap! {
fname!("replacedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnRight"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
fname!("future") => ArgSpec::from_optional("burnRight"),
},
valencies: none!(),
errors: tiny_bset! {
NON_EQUAL_AMOUNTS,
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_COVERAGE
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("Rename") => TransitionIface {
optional: true,
metadata: None,
globals: tiny_bmap! {
fname!("new") => ArgSpec::from_required("spec"),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("updateRight"),
},
assignments: tiny_bmap! {
fname!("future") => ArgSpec::from_optional("updateRight"),
},
valencies: none!(),
errors: none!(),
default_assignment: Some(fname!("future")),
},
},
extensions: none!(),
error_type: types.get("RGB20.Error"),
default_operation: Some(tn!("Transfer")),
type_system: types.type_system(),
}
}
```

In this interface, we notice similarities with the Schema structure: we find a declaration of Global State, Owned States, Contract Operations (Genesis and Transitions), as well as error handling. But the Interface focuses on the presentation and manipulation of these elements for a wallet or any other application.

The difference with Schema lies in the nature of the types. Schema uses strict types (such as `FungibleType::Unsigned64Bit`) and more technical identifiers. The Interface uses field names, macros (`fname!()`, `tn!()`), and references to argument classes (`ArgSpec`, `OwnedIface::Rights`...). The aim here is to facilitate the functional understanding and organization of elements for the wallet.

In addition, the Interface can introduce additional functionality to the basic Schema (e.g. management of a `burnEpoch` right), as long as this remains consistent with the final validated client-side logic. The AluVM "script" section in the Schema will ensure cryptographic validity, while the Interface describes how the user (or wallet) interacts with these states and transitions.

#### Global State and Assignments

In the `global_state` section, we find fields such as `spec` (asset description), `data`, `created`, `issuedSupply`, `burnedSupply`, `replacedSupply`. These are fields that the wallet can read and present. For example:


- `spec` will display the token configuration;
- `issuedSupply` or `burnedSupply` give us the total number of tokens issued or burned, etc.

In the `assignments` section, we define various roles or rights. For example:


- `assetOwner` corresponds to the holding of tokens (it is the fungible *Owned State*) ;
- `burnRight` corresponds to the ability to burn tokens ;
- updateRight` corresponds to the right to rename the asset.

The `public` or `private` keyword (e.g. `AssignIface::public(...)`) indicates whether these states are visible (`public`) or confidential (`private`). As for `Req::NoneOrMore`, `Req::Optional`, they indicate the expected occurrence.

#### Genesis and transitions

The `genesis` part describes how the asset is initialized:


- The `spec`, `data`, `created`, `issuedSupply` fields are mandatory (`ArgSpec::required()`) ;
- Assignments such as `assetOwner` can be present in multiple copies (`ArgSpec::many()`), allowing tokens to be distributed to multiple initial holders;
- Fields such as `inflationAllowance` or `burnEpoch` may (or may not) be included in Genesis.

Then, for each Transition (`Transfer`, `Issue`, `Burn`...), the Interface defines which fields the operation expects as input, which fields the operation will produce as output, and any errors that may occur. For example:

**Transition :**


- Inputs : `previous` → must be an `assetOwner` ;
- Assignments : `beneficiary` → will be a new `assetOwner` ;
- Error: `NON_EQUAL_AMOUNTS` (the wallet will thus be able to handle cases where the input sum does not correspond to the output sum).

**Transition `Issue` :**


- Optional (`optional: true`), as additional emission is not necessarily activated;
- Inputs: `used` → an `inflationAllowance`, i.e. permission to add more tokens ;
- Assignments: `beneficiary` (new tokens received) and `future` (remaining `inflationAllowance`) ;
- Possible errors: `SUPPLY_MISMATCH`, `ISSUE_EXCEEDS_ALLOWANCE`, etc.

**Burn transition :**


- Inputs : `used` → a `burnRight` ;
- Globals : `burnedSupply` required ;
- Assignments: `future` → a possible continuation of the `burnRight` if we haven't burned everything ;
- Errors: `SUPPLY_MISMATCH`, `INVALID_PROOF`, `INSUFFICIENT_COVERAGE`.

Each operation is therefore described in a way that is readable for a wallet. This makes it possible to display a graphical interface where the user can clearly see: "You have the right to burn. Would you like to burn a certain amount? The code knows to fill in a `burnedSupply` field and check that the `burnRight` is valid.

To sum up, it's important to bear in mind that an Interface, however complete, does not by itself define the internal logic of the contract. The heart of the work is done by the **Schema**, which includes strict types, Genesis structure, transitions and so on. The Interface simply exposes these elements in a more intuitive and named way, for use in an application.

Thanks to RGB's modularity, the Interface can be upgraded (for example, by adding a `Rename` transition, correcting the display of a field, etc.) without having to rewrite the entire contract. Users of this Interface can then benefit immediately from these improvements, as soon as they update the `.rgb` or `.rgba` file.

But once you've declared an Interface, you need to link it to the corresponding Schema. This is done via the ***Interface Implementation***, which specifies how to map each named field (such as `fname!("assetOwner")`) to the strict ID (such as `OS_ASSET`) defined in the Schema. This ensures, for example, that when a wallet manipulates a `burnRight` field, this is the state which, in the Schema, describes the ability to burn tokens.

### Interface Implementation

In the RGB architecture, we have seen that each component (Schema, Interface, etc.) can be developed and compiled independently. However, there's still one indispensable element that links these different building blocks together: the ***Interface Implementation***. This is what explicitly maps the identifiers or fields defined in the Schema (on the business logic side) to the names declared in the Interface (on the presentation and user interaction side). So when a wallet loads a contract, it can understand exactly which field corresponds to what, and how an operation named in the Interface relates to the logic of the Schema.

An important point is that Interface Implementation is not necessarily intended to expose all Schema functionalities, nor all Interface fields: it can be limited to a subset. In practice, this makes it possible to restrict or filter certain aspects of the Schema. For example, you could have a Schema with four types of operation, but an Implementation Interface that maps only two of them in a given context. Conversely, if an Interface proposes additional endpoints, we can choose not to implement them here.

Here's a classic example of Interface Implementation, where we associate a *Non-Inflatable Asset* (NIA) Schema with the RGB20 Interface:

```rust
fn nia_rgb20() -> IfaceImpl {
let schema = nia_schema();
let iface = Rgb20::iface();
IfaceImpl {
version: VerNo::V1,
schema_id: schema.schema_id(),
iface_id: iface.iface_id(),
script: none!(),
global_state: tiny_bset! {
NamedField::with(GS_NOMINAL, fname!("spec")),
NamedField::with(GS_DATA, fname!("data")),
NamedField::with(GS_TIMESTAMP, fname!("created")),
NamedField::with(GS_ISSUED_SUPPLY, fname!("issuedSupply")),
},
assignments: tiny_bset! {
NamedField::with(OS_ASSET, fname!("assetOwner")),
},
valencies: none!(),
transitions: tiny_bset! {
NamedType::with(TS_TRANSFER, tn!("Transfer")),
},
extensions: none!(),
}
}
```

In this Implementation Interface :


- We explicitly reference the Schema, via `nia_schema()`, and the Interface, via `Rgb20::iface()`. The calls `schema.schema_id()` and `iface.iface_id()` are used to anchor the Interface Implementation on the compile side (this associates the cryptographic identifiers of these two components);
- A mapping is established between Schema elements and Interface elements. For example, the `GS_NOMINAL` field in the Schema is linked to the string `"spec"` on the Interface side (`NamedField::with(GS_NOMINAL, fname!("spec"))`). We do the same for operations, such as `TS_TRANSFER`, which we link to `"Transfer"` in the Interface... ;
- We can see that there are no valencies (`valencies: none!()`) or extensions (`extensions: none!()`), reflecting the fact that this NIA contract doesn't use these features.

The result after compilation is a separate `.rgb` or `.rgba` file, to be imported into the wallet in addition to the Schema and Interface. Thus, the software knows how to concretely connect this NIA contract (whose logic is described by its Schema) to the "RGB20" Interface (which provides human names and an interaction mode for fungible tokens), applying this Interface Implementation as a gateway between the two.

#### Why separate Interface Implementation?

Separation enhances flexibility. A single Schema could have several distinct Interface Implementations, each mapping a different set of functionalities. What's more, the Interface Implementation itself can evolve or be rewritten without requiring a change in either the Schema or the Interface. This retains RGB's principle of modularity: each component (Schema, Interface, Interface Implementation) can be versioned and updated independently, as long as the compatibility rules imposed by the protocol are respected (same identifiers, consistency of types, etc.).

In concrete use, when the wallet loads a contract, it must :


- Load the compiled **Schema** (to know the structure of the business logic) ;
- Load compiled **Interface** (to understand names and user-side operations) ;
- Load compiled **Interface Implementation** (to link Schema logic to Interface names, operation by operation, field by field).

This modular architecture makes possible use scenarios such as :


- Limit certain operations for certain users: offer a partial Implementation Interface that only gives access to basic transfers, without offering burn or update functions, for example;
- Change presentation: design an Interface Implementation that renames a field in the Interface or maps it differently, without altering the basis of the contract;
- Support multiple schemes: a wallet can load multiple Interface Implementations for the same Interface type, to handle different schemes (different token logics), provided their structure is compatible.

In the next chapter, we'll look at how a contract transfer works, and how RGB invoices are generated.

## Contract transfers

<chapterId>f043a307-d420-5752-b0d7-ebfd845802c0</chapterId>

![video](https://youtu.be/sVoKIi-1XbY)

In this chapter, we're going to analyze the process of a contract transfer in the RGB ecosystem. To illustrate this, we'll take a look at Alice and Bob, our usual protagonists, who wish to exchange an RGB asset. We'll also show some command excerpts from the `rgb` command-line tool, to see how it works in practice.

### Understanding RGB contract transfer

Let's take an example of a transfer between Alice and Bob. In this example, we assume that Bob is just starting to use RGB, while Alice already holds RGB assets in her wallet. We'll see how Bob sets up his environment, imports the relevant contract, then requests a transfer from Alice, and finally how Alice carries out the actual transaction on the Bitcoin blockchain.

#### 1) Installing the RGB wallet

First of all, Bob needs to install an RGB wallet, i.e. software compatible with the protocol. This does not contain any contracts at the outset. Bob will also need :


- A Bitcoin wallet to manage your UTXOs;
- A connection to a Bitcoin node (or to an Electrum server), so that you can identify your UTXOs and propagate your transactions on the network.

As a reminder, **Owned States** in RGB refer to Bitcoin UTXOs. We must therefore always be able to manage and spend UTXOs in a Bitcoin transaction that incorporates cryptographic commitments (`Tapret` or `Opret`) pointing to RGB data.

#### 2) Contract information acquisition

Bob then needs to retrieve the contract data he's interested in. This data can circulate via any channel: website, e-mail, messaging application... In practice, they are grouped together in a ***consignment***, i.e. a small packet of data containing :


- The **Genesis**, which defines the initial state of the contract;
- The **Schema**, which describes the business logic (strict types, validation scripts, etc.);
- The **Interface**, which defines the presentation layer (field names, accessible operations);
- The **Interface Implementation**, which concretely links the Schema to the Interface.

![RGB-Bitcoin](assets/fr/075.webp)

The total size is often of the order of a few kilobytes, as each component generally weighs less than 200 bytes. It may also be possible to broadcast this consignment in Base58, via censorship-resistant channels (like Nostr or via the Lightning Network, for example), or as a QR code.

#### 3) Contract import and validation

Once Bob has received the consignment, he imports it into his RGB wallet. This will then :


- Check that the Genesis and Schema are valid;
- Load Interface and Interface Implementation ;
- Update your client-side data stash.

Bob can now see the asset in his wallet (even if he doesn't own it yet) and understand what fields are available, what operations are possible... He then needs to contact a person who actually owns the asset to be transferred. In our example, this is Alice.

The process of discovering who holds a certain RGB asset is similar to finding a Bitcoin payer. The details of this connection depend on the use (marketplaces, private chat channels, invoicing, sale of goods and services, salary...).

#### 4) Issuing an invoice

To initiate the transfer of an RGB asset, Bob must first issue an invoice. This invoice is used to :


- Tell Alice the type of operation to be performed (for example, a `Transfer` from an RGB20 interface);
- Provide Alice with Bob's *seal definition* (i.e. the UTXO where he wishes to receive the asset);
- Specify the quantity of active ingredient required (e.g. 100 units).

Bob uses the `rgb` tool on the command line. Suppose he wants 100 units of a token whose `ContractId` is known, wants to rely on `Tapret`, and specifies its UTXO (`456e3..dfe1:0`) :

```bash
bob$ rgb invoice RGB20 100 <ContractId> tapret1st:456e3..dfe1:0
```

We'll take a closer look at the structure of RGB invoices at the end of this chapter.

#### 5) Invoice transmission

The generated invoice (e.g. as URL: `rgb:2WBcas9.../RGB20/100+utxob:...`) contains all the information Alice needs to prepare the transfer. As with the consignment, it can be encoded compactly (Base58 or another format) and sent via a messaging application, e-mail, Nostr...

![RGB-Bitcoin](assets/fr/076.webp)

#### 6) Transaction preparation on the Alice side

Alice receives Bob's invoice. In her RGB wallet, she has a stash containing the asset to be transferred. To spend the UTXO containing the asset, she must first generate a PSBT (*Partially Signed Bitcoin Transaction*), i.e. an incomplete Bitcoin transaction, using the UTXO she has:

```bash
alice$ wallet construct tx.psbt
```

This basic transaction (unsigned for the moment) will be used to anchor the cryptographic commitment linked to the transfer to Bob. Alice's UTXO will thus be spent, and in the output, we'll place the `Tapret` or `Opret` commitment for Bob.

#### 7) Generation of transfer consignment

Next, Alice builds the ***terminal consignment*** (sometimes called "transfer consignment") via the command :

```bash
alice$ rgb transfer tx.psbt <invoice> consignment.rgb
```

This new `consignment.rgb` file contains :


- The complete history of State Transitions required to validate the asset up to the present time (since Genesis);
- The new State Transition that transfers assets from Alice to Bob, according to the invoice Bob has issued;
- The incomplete Bitcoin transaction (*witness transaction*) (`tx.psbt`), which spends Alice's Single-use Seal, modified to include the cryptographic commitment to Bob.

At this stage, the transaction is not yet broadcast on the Bitcoin network. The consignment is larger than a basic consignment, as it includes the entire history (*proof chain*) to prove the asset's legitimacy.

#### 8) Bob checks and accepts the consignment

Alice transmits this **terminal consignment** to Bob. Bob will then :


- Check the validity of the State Transition (ensure that the history is consistent, that contract rules are respected, etc.);
- Add it to your local stash;
- Possibly generate a signature (`sig:...`) on the consignment, to prove that it has been examined and approved (sometimes called a "*payslip*").

```bash
bob$ rgb accept consignment.rgb
sig:DbwzvSu4BZU81jEpE9FVZ3xjcyuTKWWy2gmdnaxtACrS
```

![RGB-Bitcoin](assets/fr/077.webp)

#### 9) Option: Bob sends confirmation back to Alice (*payslip*)

If Bob wishes, he can send this signature back to Alice. This indicates:


- That it recognizes the transition as valid;
- That he agrees to the Bitcoin transaction being broadcast.

This is not compulsory, but it can provide Alice with the assurance that there will be no subsequent disputes over the transfer.

#### 10) Alice signs and publishes the transaction

Alice can then :


- Check Bob's signature (`rgb check <sig>`) ;
- Sign the *witness transaction* which is still a PSBT (`wallet sign`) ;
- Publish the witness transaction on the Bitcoin network (`-publish`).

```bash
alice$ rgb check <sig>
alice$ wallet sign —publish tx.psbt
```

![RGB-Bitcoin](assets/fr/078.webp)

Once confirmed, this transaction marks the conclusion of the transfer. Bob becomes the new owner of the asset: he now has an Owned State pointing to the UTXO he controls, proven by the presence of the commitment in the transaction.

To summarize, here is the complete transfer process:

![RGB-Bitcoin](assets/fr/079.webp)

### Advantages of RGB transfers


- Confidentiality** :

Only Alice and Bob have access to all State Transition data. They exchange this information outside the blockchain, via consignments. The cryptographic commitments in the Bitcoin transaction do not reveal the type of asset or the amount, which guarantees far greater confidentiality than other on-chain token systems.


- Customer-side validation** :

Bob can check the consistency of the transfer by comparing the *consignment* with the *anchors* in the Bitcoin blockchain. He does not need third-party validation. Alice doesn't have to publish the full history on the blockchain, which reduces the load on the base protocol and improves confidentiality.


- Simplified atomicity** :

Complex exchanges (atomic swaps between BTC and an RGB asset, for example) can be carried out within a single transaction, avoiding the need for HTLC or PTLC scripts. If the agreement is not broadcast, everyone can reuse their UTXOs in other ways.

### Transfer summary diagram

Before looking at the invoices in more detail, here's a summary diagram of the overall flow of an RGB transfer:


- Bob installs an RGB wallet and obtains the initial contract consignment;
- Bob issues an invoice mentioning the UTXO where to receive the asset;
- Alice receives the invoice, builds the PSBT and generates the terminal consignment;
- Bob accepts it, checks, adds the data to his stash, and signs (*payslip*) if necessary;
- Alice publishes the transaction on the Bitcoin network;
- Confirmation of the transaction makes the transfer official.

![RGB-Bitcoin](assets/fr/080.webp)

The transfer illustrates all the power and flexibility of the RGB protocol: a private exchange, validated on the client side, anchored minimally and discreetly on the Bitcoin blockchain, and retaining the best of the protocol's security (no risk of double-spending). This makes RGB a promising ecosystem for value transfers that are more confidential and scalable than on-chain programmable blockchains.

### Invoices RGB

In this section, we'll explain in detail how **invoices** work in the RGB ecosystem and how they enable operations (in particular transfers) to be carried out with a contract. First, we'll look at the identifiers used, then at how they are encoded, and finally at the structure of an invoice expressed as a URL (a format that's handy enough for use in wallets).

#### Identifiers and encoding

A unique identifier is defined for each of the following elements:


- An RGB contract;
- Its Schema (business logic) ;
- Its Interface and Interface Implementation ;
- Its assets (tokens, NFT, etc.),

This uniqueness is very important, as each component of the system must be distinguishable. For example, a contract X must not be confused with another contract Y, and two different interfaces (RGB20 vs. RGB21, for example) must have distinct identifiers.

To make these identifiers both efficient (small size) and readable, we use :


- Base58 encoding, which avoids the use of confusing characters (e.g. `0` and the letter `O`) and provides relatively short strings;
- A prefix indicating the nature of the identifier, usually in the form of `rgb:` or a similar URN.

For example, a `ContractId` could be represented by something like :

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```

The `rgb:` prefix confirms that this is an RGB identifier, and not an HTTP link or other protocol. Thanks to this prefix, wallets are able to interpret the string correctly.

#### Identifier segmentation

RGB identifiers are often quite long, as the underlying (cryptographic) security may require fields of 256 bits or more. To facilitate human reading and verification, we *chunk* these strings into several blocks separated by a hyphen (`-`). So, instead of having a long, uninterrupted string of characters, we divide it into shorter blocks. This practice is common for credit card or telephone numbers, and it also applies here for ease of verification. So, for example, a user or partner can be told: "*Please check that the third block is `9GEgnyMj7`*", rather than having to compare the whole thing at once. The last block is often used as a **checksum**, in order to have an error or typos detection system.

As an example, a `ContractId` in base58 encoded and segmented could be :

```txt
2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```

Each of the dashes breaks the string into sections. This does not affect the semantics of the code, only its presentation.

#### Using URLs for invoices

An RGB invoice is presented as a URL. This means that it can be clicked or scanned (as a QR code), and a wallet can directly interpret it to carry out a transaction. This simplicity of interaction differs from some other systems where you have to copy and paste various pieces of data into different fields in the software.

An invoice for a fungible token (e.g. an RGB20 token) might look like this:

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

Let's analyze this URL:


- `rgb:`** (prefix): indicates a link invoking the RGB protocol (analogous to `http:` or `bitcoin:` in other contexts);
- `2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX`**: represents the `ContractId` of the token you want to manipulate;
- `/RGB20/100`**: indicates that the `RGB20` interface is used and that 100 units of the asset are requested. The syntax is: `/Interface/amount` ;
- `+utxob:`**: specifies that information about the recipient UTXO (or, more precisely, the definition of the Single-use Seal) is added;
- `egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb`**: this is the *blinded* UTXO (or seal definition). In other words, Bob has masked his exact UTXO, so the sender (Alice) doesn't know what the exact address is. She only knows that there is a valid seal referring to a UTXO controlled by Bob.

The fact that everything fits into a single URL makes life easier for the user: a simple click or scan in the wallet, and the operation is ready to be executed.

One could imagine systems where a simple ticker (e.g. `USDT`) is used instead of the `ContractId`. However, this would raise major problems of trust and security: a ticker is not a unique reference (several contracts could claim to be called `USDT`). With RGB, we want a unique, unambiguous cryptographic identifier. Hence the adoption of the 256-bit string, encoded in base58 and segmented. The user knows that he is manipulating precisely the contract whose ID is `2WBcas9-yjz...` and not any other.

#### Additional URL parameters

You can also add additional parameters to the URL, in the same way as with HTTP, such as :

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb?sig=6kzbKKffP6xftkxn9UP8gWqiC41W16wYKE5CYaVhmEve
```


- `?sig=...`: represents, for example, a signature associated with the invoice, which some wallets can verify;
- If a wallet does not manage this signature, it simply ignores this parameter.

Let's take the case of an NFT via the RGB21 interface. For example, we could have :

```txt
rgb:7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK/RGB21/DbwzvSu-4BZU81jEp-E9FVZ3xj-cyuTKWWy-2gmdnaxt-ACrS+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

Here we see :


- `rgb:`**: URL prefix ;
- `7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK`**: Contract ID (NFT) ;
- rGB21**: interface for non-fungible assets (NFT) ;
- `DbwzvSu-4BZU81jEp-...`**: an explicit reference to the unique part of the NFT, for example a hash of the data blob (media, metadata...) ;
- `+utxob:egXsFnw-...`**: the seal definition.

The idea is the same: transmit a unique link that the wallet can interpret, clearly identifying the unique asset to be transferred.

#### Other operations via URL

RGB URLs aren't just used to request a transfer. They can also encode more advanced operations, such as issuing new tokens (*issuance*). For example:

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/issue/100000+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

Here we find :


- `rgb:` : protocol ;
- `2WBcas9-...`: Contract ID ;
- `/RGB20/issue/100000`: indicates that you want to invoke the "*Issue*" transition to create an additional 100,000 tokens;
- `+utxob:`: the seal definition.

For example, the wallet might read: "I have been asked to carry out an `issue` operation from the `RGB20` interface, on such and such a contract, for 100,000 units, for the benefit of such and such a Single-use Seal.*"

Now that we've looked at the main elements of RGB programming, I'll take you through the next chapter on how to draw up an RGB contract.

## Drafting smart contracts

<chapterId>0e0a645c-0049-588d-8965-b8c536590cc9</chapterId>

![video](https://youtu.be/GRwS-NvWF3I)

In this chapter, we'll take a step-by-step approach to writing a contract, using the command-line tool `rgb`. The aim is to show how to install and manipulate the CLI, compile a **Schema**, import the **Interface** and the **Interface Implementation**, then issue (*issue*) an asset. We'll also look at the underlying logic, including compilation and state validation. By the end of this chapter, you should be able to reproduce the process and create your own RGB contracts.

As a reminder, the internal logic of RGB is based on Rust libraries that you, as developers, can import into your projects to manage the Client-side Validation part. In addition, the LNP/BP Association team is working on bindings for other languages, but this has not yet been finalized. In addition, other entities such as Bitfinex are developing their own integration stacks (we'll talk about these in the last 2 chapters of the course). For the time being, therefore, the `rgb` CLI is the official reference, even if it remains relatively unpolished.

### Installation and presentation of the rgb tool

The main command is simply called `rgb`. It is designed to be reminiscent of `git`, with a set of sub-commands for manipulating contracts, invoking them, issuing assets and so on. Bitcoin Wallet is not currently integrated, but will be in an imminent version (0.11). This next version will enable users to create and manage their wallets (via descriptors) directly from `rgb`, including PSBT generation, compatibility with external hardware (e.g. a hardware wallet) for signing, and interoperability with software such as Sparrow. This will simplify the entire asset issuance and transfer scenario.

#### Installation via Cargo

We install the tool in Rust with :

```bash
cargo install rgb-contracts --all-features
```

(Note: the crate is called `rgb-contracts`, and the installed command will be named `rgb`. If a crate named `rgb` already existed, there could have been a collision, hence the name)

The installation compiles a large number of dependencies (e.g. command parsing, Electrum integration, zero-knowledge proofs management, etc.).

Once installation is complete, the :

```bash
rgb
```

Running `rgb` (without arguments) displays a list of available sub-commands, such as `interfaces`, `schema`, `import`, `export`, `issue`, `invoice`, `transfer`, etc. You can change the local storage directory (a stash that holds all logs, schematics and implementations), choose the network (testnet, mainnet) or configure your Electrum server.

![RGB-Bitcoin](assets/fr/081.webp)

#### First overview of controls

When you run the following command, you'll see that an `RGB20` interface is already integrated by default:

```bash
rgb interfaces
```

If this interface is not integrated, clone the :

```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```

Compile it:

```bash
cargo run
```

Then import the interface of your choice:

```bash
rgb import interfaces/RGB20.rgb
```

![RGB-Bitcoin](assets/fr/082.webp)

On the other hand, we are told that no schema has yet been imported into the software. Nor is there a contract in the stash. To see it, run the command :

```bash
rgb schemata
```

You can then clone the repository to retrieve certain schematics:

```bash
git clone https://github.com/RGB-WG/rgb-schemata
```

![RGB-Bitcoin](assets/fr/083.webp)

This repository contains, in its `src/` directory, several Rust files (for example `nia.rs`) which define schemas (NIA for "*Non Inflatable Asset*", UDA for "*Unique Digital Asset*", etc.). To compile, you can then run :

```bash
cd rgb-schemata
cargo run
```

This generates several `.rgb` and `.rgba` files corresponding to the compiled schematics. For example, you'll find `NonInflatableAsset.rgb`.

#### Importing Schema and Interface Implementation

You can now import the schematic into `rgb` :

```bash
rgb import schemata/NonInflatableAssets.rgb
```

![RGB-Bitcoin](assets/fr/084.webp)

This adds it to the local stash. If we run the following command, we see that the schema now appears:

```bash
rgb schemata
```

### Contract creation (issuing)

There are two approaches to creating a new asset:


- Either we use a script or code in Rust that builds a Contract by populating schema fields (global state, Owned States, etc.) and produces a `.rgb` or `.rgba` file;
- Or use the `issue` sub-command directly, with a YAML (or TOML) file describing the token's properties.

You can find examples in Rust in the `examples` folder, which illustrate how you build a `ContractBuilder`, fill in the `global state` (asset name, ticker, supply, date, etc.), define the Owned State (to which UTXO it is assigned), then compile all this into a *contract consignment* that you can export, validate and import into a stash.

The other way is to manually edit a YAML file to customize the `ticker`, the `name`, the `supply`, and so on. Suppose the file is called `RGB20-demo.yaml`. You can specify :


- `spec`: ticker, name, precision ;
- `terms`: a field for legal notices ;
- `issuedSupply` : the amount of token issued ;
- `assignments`: indicates the Single-use Seal (*seal definition*) and the quantity unlocked.

Here is an example of a YAML file to create:

```yaml
interface: RGB20Fixed
globals:
spec:
ticker: PBN
name: Plan B Network
details: "Pay attention: the asset has no value"
precision: 2
terms:
text: >
SUBJECT TO, AND WITHOUT IN ANY WAY LIMITING, THE REPRESENTATIONS AND WARRANTIES OF ANY SELLER. PROPERTY IS BEING SOLD “AS IS”...
media: ~
issuedSupply: 100000000
assignments:
assetOwner:
seal: tapret1st:b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1
amount: 100000000 # this is 1 million (we have two digits for cents)
```

![RGB-Bitcoin](assets/fr/085.webp)

Then simply run the command :

```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```

![RGB-Bitcoin](assets/fr/086.webp)

In my case, the unique schema identifier (to be enclosed in single quotes) is `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k` and I haven't put any issuer. So my order is :

```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```

If you don't know the schema ID, run the command :

```bash
rgb schemata
```

The CLI replies that a new contract has been issued and added to the stash. If we type the following command, we see that there is now an additional contract, corresponding to the one just issued:

```bash
rgb contracts
```

![RGB-Bitcoin](assets/fr/087.webp)

Then, the next command displays the global states (name, ticker, supply...) and the list of Owned States, i.e. allocations (for example, 1 million `PBN` tokens defined in UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1`).

```bash
rgb state '<ContractId>'
```

![RGB-Bitcoin](assets/fr/088.webp)

### Export, import and validation

To share this contract with other users, it can be exported from the stash to a :

```bash
rgb export '<ContractId>' myContractPBN.rgb
```

![RGB-Bitcoin](assets/fr/089.webp)

The `myContractPBN.rgb` file can be passed on to another user, who can add it to his stash with the command :

```bash
rgb import myContractPBN.rgb
```

On import, if it's a simple *contract consignment*, we'll get an "`Importing consignment rgb`" message. If it's a larger *state transition consignment*, the command will be different (`rgb accept`).

To ensure validity, you can also use the local validation function. For example, you could run :

```bash
rgb validate myContract.rgb
```

#### Stash usage, verification and display

As a reminder, the stash is a local inventory of schemas, interfaces, implementations and contracts (Genesis + transitions). Each time you run "import", you add an element to the stash. This stash can be viewed in detail with the command :

```bash
rgb dump
```

![RGB-Bitcoin](assets/fr/090.webp)

This will generate a folder with details of the entire stash.

### Transfer and PSBT

To carry out a transfer, you'll need to manipulate a local Bitcoin wallet to manage the `Tapret` or `Opret` commitments.

#### Generate an invoice

In most cases, interaction between the participants in a contract (e.g. Alice and Bob) takes place via the generation of an invoice. If Alice wants Bob to execute something (a token transfer, a reissue, an action in a DAO, etc.), Alice creates an invoice detailing her instructions to Bob. So we have :


- Alice** (the issuer of the invoice) ;
- Bob** (who receives and executes the invoice).

Unlike other ecosystems, an RGB invoice is not limited to the notion of payment. It can embed any request linked to the contract: revoke a key, vote, create an engraving (*engraving*) on an NFT, etc. The corresponding operation can be described in the contract interface. The corresponding operation can be described in the contract interface.

The following command generates an RGB invoice:

```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```

With :


- `$CONTRACT`: Contract identifier (*ContractId*) ;
- `$INTERFACE`: the interface to be used (e.g. `RGB20`) ;
- `$ACTION`: the name of the operation specified in the interface (for a simple fungible token transfer, this could be "Transfer"). If the interface already provides a default action, you don't need to enter it again here;
- `$STATE`: the status data to be transferred (for example, an amount of tokens if a fungible token is transferred);
- `$SEAL`: the beneficiary's (Alice's) Single-use Seal, i.e. an explicit reference to an UTXO. Bob will use this info to build the witness transaction, and the corresponding output will then belong to Alice (in *blinded UTXO* or unencrypted form).

For example, with the following commands

```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```

The CLI will generate an invoice like :

```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```

It can be transmitted to Bob via any channel (text, QR code, etc.).

#### Making a transfer

To transfer from this invoice :


- Bob (who holds the tokens in his stash) has a Bitcoin wallet. He needs to prepare a Bitcoin transaction (in the form of a PSBT, e.g. `tx.psbt`) which spends the UTXOs where the required RGB tokens are located, plus one UTXO for currency (exchange) ;
- Bob executes the following command:

```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```


- This generates a `consignment.rgb` file which contains :
 - The transition history proving to Alice that the tokens are genuine;
 - The new transition that transfers tokens to Alice's Single-use Seal ;
 - A witness transaction (unsigned).
- Bob sends this `consignment.rgb` file to Alice (by e-mail, a sharing server or an RGB-RPC protocol, Storm, etc.);
- Alice receives `consignment.rgb` and accepts it in its own stash :

```bash
alice$ rgb accept consignment.rgb
```


- The CLI checks the validity of the transition and adds it to Alice's stash. If invalid, the command fails with detailed error messages. Otherwise, it succeeds, and reports that the sample transaction has not yet been broadcast on the Bitcoin network (Bob is waiting for Alice's green light);
- By way of confirmation, the `accept` command returns a signature (*payslip*) which Alice can send to Bob to show him that she has validated the *consignment* ;
- Bob can then sign and publish (`--publish`) his Bitcoin transaction:

```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```


- As soon as this transaction is confirmed on-chain, ownership of the asset is considered transferred to Alice. Alice's wallet, monitoring the transaction's mining, sees the new Owned State appear in its stash.

In the next chapter, we'll take a closer look at integrating RGB into the Lightning Network.

## RGB on the Lightning Network

<chapterId>0962980a-8f94-5d0f-9cd0-43d7f884a01d</chapterId>

![video](https://youtu.be/mqCupTlDbA0)

In this chapter, I propose to examine how RGB can be used within the Lightning Network, to integrate and move RGB assets (tokens, NFTs, etc.) via off-chain payment channels.

The basic idea is that the RGB state transition (*State Transition*) can be committed to a Bitcoin transaction which, in turn, can remain off-chain until the Lightning channel is closed. So, each time the channel is updated, a new RGB state transition can be incorporated into the new committing transaction, which then invalidates the old transition. In this way, Lightning channels can be used to transfer RGB assets, and can be routed in the same way as conventional Lightning payments.

### Channel creation and funding

To create a Lightning channel that carries RGB assets, we need two elements:


- Bitcoin funding to create the channel's 2/2 multisig (the basic UTXO for the channel);
- RGB funding, which sends assets to the same multisig.

In Bitcoin terms, the funding transaction must exist to define the reference UTXO, even if it only contains a small amount of sats (it's just a matter of each output in future commitment transactions remaining above the dust limit all the same). For example, Alice may decide to provide 10k sats and 500 USDT (issued as an RGB asset). On the funding transaction, we add a commitment (`Opret` or `Tapret`) which anchors the RGB state transition.

![RGB-Bitcoin](assets/fr/091.webp)

Once the funding transaction has been prepared (but not yet broadcast), commitment transactions are created so that either party can close the channel unilaterally at any time. These transactions resemble Lightning's classic commitment transactions, except that we add an additional output containing the RGB anchor (OP_RETURN or Taproot) linked to the new state transition.

The RGB state transition then moves the assets from the 2/2 multisig of the funding to the outputs of the commitment transaction. The advantage of this process is that the security of the RGB state exactly matches Lightning's punitive mechanics: if Bob broadcasts an old channel state, Alice can punish him and spend the output, in order to recover both the sats and the RGB tokens. The incentive is therefore even stronger than in a Lightning channel without RGB assets, since an attacker can lose not only sats, but also the channel's RGB assets.

A commitment transaction signed by Alice and sent to Bob would therefore look like this:

![RGB-Bitcoin](assets/fr/092.webp)

And the accompanying commitment transaction, signed by Bob and sent to Alice, will look like this:

![RGB-Bitcoin](assets/fr/093.webp)

### Channel update

When a payment occurs between two channel participants (or they wish to change the asset allocation), they create a new pair of commitment transactions. The amount in sats on each output may or may not remain unchanged, depending on the implementation, as its main role is to enable the construction of valid UTXOs. On the other hand, the OP_RETURN (or Taproot) output must be modified to contain the new RGB anchor, representing the new distribution of assets in the channel.

For example, if Alice transfers 30 USDT to Bob in the channel, the new state transition will reflect a balance of 400 USDT for Alice and 100 USDT for Bob. The commit transaction is added to (or modified by) the OP_RETURN/Taproot anchor to include this transition. Note that, from RGB's point of view, the input to the transition remains the initial multisig (where on-chain assets are actually allocated until the channel closes). Only the RGB outputs (allocations) change, depending on the redistribution decided upon.

The commitment transaction signed by Alice, ready to be distributed by Bob :

![RGB-Bitcoin](assets/fr/094.webp)

The commitment transaction signed by Bob, ready to be distributed by Alice :

![RGB-Bitcoin](assets/fr/095.webp)

### HTLC management

In reality, the Lightning Network enables payments to be routed via multiple channels, using HTLCs (*Hashed Time-Locked Contracts*). It's the same with RGB: for every payment in transit through the channel, an HTLC output is added to the committing transaction, and an RGB allocation linked to this HTLC. Thus, whoever spends the HTLC output (thanks to the secret or after expiry of the timelock) recovers both the sats and the associated RGB assets. On the other hand, you obviously need to have enough cash on the road in terms of both sats and RGB assets.

![RGB-Bitcoin](assets/fr/096.webp)

The operation of RGB on Lightning must therefore be considered in parallel with that of the Lightning Network itself. If you'd like to delve deeper into this subject, I highly recommend you take a look at this other comprehensive training course:

https://planb.network/courses/lnp201
### RGB code map

Finally, before moving on to the next section, I'd like to give you an overview of the code used in RGB. The protocol is based on a set of Rust libraries and open source specifications. Here's an overview of the main repositories and crates:

![RGB-Bitcoin](assets/fr/097.webp)

#### Client-side Validation


- Repository**: [client_side_validation](https://github.com/LNP-BP/client_side_validation)
- Crates** : [client_side_validation](https://crates.io/crates/client_side_validation), [single_use_seals](https://crates.io/crates/single_use_seals)

Management of off-chain validation and Single-use Seals logic.

#### Deterministic Bitcoin Commitments (DBC)


- Repository**: [bp-core](https://github.com/BP-WG/bp-core)
- Crate**: [bp-dbc](https://crates.io/crates/bp-dbc)

Management of deterministic anchoring in Bitcoin transactions (Tapret, OP_RETURN, etc.).

#### Multi Protocol Commitment (MPC)


- Repository**: [client_side_validation](https://github.com/LNP-BP/client_side_validation)
- Crate** : [commit_verify](https://crates.io/crates/commit_verify)

Multiple engagement combinations and integration with different protocols.

#### Strict Types & Strict Encoding


- Specifications**: [website strict-types.org](https://www.strict-types.org/)
- Repositories**: [strict-types](https://github.com/strict-types/strict-types), [strict-encoding](https://github.com/strict-types/strict-encoding)
- Crates** : [strict_types](https://crates.io/crates/strict_types), [strict_encoding](https://crates.io/crates/strict_encoding)

The strict typing system and deterministic serialization used for client-side validation.

#### RGB Core


- Repository**: [rgb-core](https://github.com/RGB-WG/rgb-core)
- Crate**: [rgb-core](https://crates.io/crates/rgb-core)

The core of the protocol, which encompasses the main logic of RGB validation.

#### RGB Standard Library & Wallet


- Repository**: [rgb-std](https://github.com/RGB-WG/rgb-std)
- Crate** : [rgb-std](https://crates.io/crates/rgb-std)

Standard implementations, stash and wallet management.

#### RGB CLI


- Repository**: [rgb](https://github.com/RGB-WG/rgb)
- Crates**: [rgb-cli](https://crates.io/crates/rgb-cli), [rgb-wallet](https://crates.io/crates/rgb-wallet)

The `rgb` CLI and crate wallet, for command-line manipulation of contracts.

#### RGB Schema


- Repository**: [rgb-schemata](https://github.com/RGB-WG/rgb-schemata/)

Contains examples of schemas (NIA, UDA, etc.) and their implementations.

#### ALuVM


- Info** : [aluvm.org](https://www.aluvm.org/)
- Repositories**: [aluvm-spec](https://github.com/AluVM/aluvm-spec), [alure](https://github.com/AluVM/alure)
- Crates**: [aluvm](https://crates.io/crates/aluvm), [aluasm](https://crates.io/crates/aluasm)

Registry-based virtual machine used to run validation scripts.

#### Bitcoin Protocol - BP


- Repositories** : [bp-core](https://github.com/BP-WG/bp-core), [bp-std](https://github.com/BP-WG/bp-std), [bp-wallet](https://github.com/BP-WG/bp-wallet)

Add-ons to support the Bitcoin protocol (transactions, bypasses, etc.).

#### Ubiquitous Deterministic Computing - UBIDECO


- Repository**: [UBIDECO](https://github.com/UBIDECO)

Ecosystem linked to open-source deterministic developments.

# Building on RGB

<partId>3b4b0d66-0c1b-505a-b5ca-4b2e57dd73c2</partId>

## DIBA and the Bitmask project

<chapterId>dc92a5e8-ed93-5a3f-bcd0-d433932842f4</chapterId>

![video](https://youtu.be/nbUtV8GOR_U)

This final section of the course is based on presentations made by various speakers at the RGB bootcamp. It includes testimonials and reflections on RGB and its ecosystem, as well as presentations of tools and projects based on the protocol. This first chapter is moderated by Hunter Beast, and the next two by Frederico Tenga.

### From JavaScript to Rust, and into the Bitcoin ecosystem

At first, Hunter Beast worked mainly in JavaScript. Then he discovered **Rust**, whose syntax seemed unappealing and frustrating at first. However, he came to appreciate the power of the language, the control over memory (*heap* and *stack*), and the security and performance that come with it. He emphasizes that Rust is an excellent training ground for in-depth understanding of how a computer works.

Hunter Beast recounts his background in various projects in the *altcoin* ecosystem, such as Ethereum (with Solidity, TypeScript, etc.), and later Filecoin. He explains that he was initially impressed by some of the protocols, but ended up feeling disillusioned by most of them, not least because of their tokenomics. He denounces the dubious financial incentives, the inflationary creation of tokens that dilutes investors, and the potentially exploitative aspect of these projects. So he ended up adopting a **Bitcoin maximalist** stance, not least because some people opened his eyes to Bitcoin's sounder economic mechanisms, and to the robustness of this system.

### The appeal of RGB and building on layers

What definitively convinced him of Bitcoin's relevance, in his words, was the discovery of RGB and the concept of layers. He believes that existing functionalities on other blockchains could be reproduced on higher layers, above Bitcoin, without altering the basic protocol.

In February 2022, he joined **DIBA** to work specifically on RGB, and in particular on the **Bitmask** wallet. At the time, Bitmask was still at version 0.01 and was running RGB at version 0.4, only for the management of single tokens. He notes that this was less self-custody-oriented than today, as the logic was partly server-based. Since then, the architecture has evolved towards this model, much appreciated by bitcoiners.

### The foundations of the RGB protocol

The **RGB** protocol is the most recent and most advanced embodiment of the _colored coins_ concept, already explored around 2012-2013. At the time, several teams were looking to associate different bitcoin value on UTXOs, which led to multiple scattered implementations. This lack of standardization and the low demand at the time prevented these solutions from gaining a lasting foothold.

Today, RGB stands out for its conceptual robustness and unified specifications via the LNP/BP association. The principle is based on client-side validation. The Bitcoin blockchain only stores cryptographic commitments (_commitments_, via Taproot or OP_RETURN), while the majority of data (contract definitions, transfer histories, etc.) is stored by the users concerned. In this way, the storage load is distributed and the confidentiality of exchanges is reinforced, without weighing down the blockchain. This approach enables the creation of fungible assets (**RGB20** standard) or unique assets (**RGB21** standard), within a modular and scalable framework.

### The token function (RGB20) and unique assets (RGB21)

With **RGB20**, we define a fungible token on Bitcoin. The issuer chooses a _supply_, a _precision_, and creates a _contract_ in which he can then make transfers. Each transfer is referenced to a Bitcoin UTXO, which acts as a *Single-use Seal*. This logic ensures that the user will not be able to spend the same asset twice, since only the person capable of spending the UTXO actually holds the key to update the state of the client-side contract.

**RGB21** targets unique assets (or "NFT"). The asset has a supply of 1, and can be associated with metadata (image file, audio, etc.) described via a specific field. Unlike NFTs on public blockchains, data and their MIME identifiers can remain private, distributed peer-to-peer at the owner's discretion.

### The Bitmask solution: a wallet for RGB

To exploit RGB's capabilities in practice, the **DIBA** project has designed a wallet called [Bitmask](https://bitmask.app/). The idea is to provide a non-custodial, Taproot-based tool, accessible as a web application or browser extension. Bitmask manages both RGB20 and RGB21 assets, and integrates various security mechanisms:


- The core code is written in Rust, then compiled in WebAssembly to run in a JavaScript environment (React);
- Keys are generated locally, then stored encrypted locally ;
- State data (stash) is held in memory, serialized and encrypted via the **Carbonado** library, which performs compression, error correction, encryption and stream verification using Blake3.

Thanks to this architecture, all asset transactions take place on the client side. From the outside, the Bitcoin transaction is nothing more than a classic Taproot spending transaction, which nobody would suspect is also carrying a transfer of fungible tokens or NFTs. The absence of on-chain overloading (no publicly stored metadata) guarantees a certain degree of discretion and makes it easier to resist possible censorship attempts.

### Security and distributed architecture

Insofar as the RGB protocol requires each participant to retain its transaction history (to prove the validity of the transfers it receives), the question of storage arises. Bitmask proposes to serialize this stash locally, then send it to several servers or clouds (optional). The data remains encrypted by the user via **Carbonado**, so a server cannot read it. In the event of partial corruption, the error correction layer can reconstitute the content.

The use of CRDT (_Conflict-free replicated data type_) enables different versions of the stash to be merged, should they diverge. Everyone is free to host this data wherever they wish, as no single full node carries all the information linked to the asset. This exactly reflects the *Client-side Validation* philosophy, where each owner is responsible for storing evidence of the validity of their RGB asset.

### Towards a broader ecosystem: marketplace, interoperability and new functions

The company behind Bitmask is not limiting itself to the simple development of a wallet. DIBA intends to develop :


- A **marketplace** for exchanging tokens, particularly in **RGB21** form;
- Compatibility with other wallets (such as *Iris Wallet*);
- Transfer batching** techniques, i.e. the possibility of including several successive RGB transfers in a single transaction.

At the same time, we're working on **WebBTC** or **WebLN** (standards enabling websites to ask the wallet to sign Bitcoin or Lightning transactions), as well as on the ability to "teleburn" Ordinals entries (if we want to repatriate Ordinals to a more discreet and flexible RGB format).

### Conclusion

The whole process shows how the RGB ecosystem can be deployed and made accessible to end-users through robust technical solutions. The transition from an altcoin perspective to a more Bitcoin-centric vision, coupled with the discovery of *Client-side Validation*, illustrates a fairly logical path: we understand that it is possible to implement various functionalities (fungible tokens, NFT, smart contracts...) without forking the blockchain, simply by taking advantage of cryptographic commitments on Taproot transactions or OP_RETURNs.

The **Bitmask** wallet is part of this approach: on the blockchain side, all you see is an ordinary Bitcoin transaction; on the user side, you manipulate a web interface where you create, exchange and store all kinds of off-chain assets. This model clearly dissociates the monetary infrastructure (Bitcoin) from the issuing and transfer logic (RGB), while ensuring a high level of confidentiality and better scalability.

## Bitfinex's work on RGB

<chapterId>d4d80e07-5eac-5b29-a93a-123180e97047</chapterId>

![vidéo](https://youtu.be/5iAhsgCSL3U)

In this chapter, based on a presentation by Frederico Tenga, we look at a set of tools and projects created by the Bitfinex team dedicated to RGB, with the aim of fostering the emergence of a rich and diverse ecosystem around this protocol. The team's initial aim is not to release a specific commercial product, but rather to provide software building blocks, contribute to the RGB protocol itself, and propose concrete implementation references such as a mobile wallet (*Iris Wallet*) or an RGB-compatible Lightning node.

### Background and objectives

Since around 2022, the Bitfinex RGB team has been concentrating on developing the technology stack that enables RGB to be exploited and tested efficiently. Several contributions have been made:


- Participation in source code and protocol specifications, including writing enhancement proposals, fixing bugs, etc;
- Tools for developers to simplify the integration of RGB in their applications;
- Design of a mobile wallet named [Iris](https://iriswallet.com/) to experiment and illustrate best practices for using RGB ;
- Creation of a customized Lightning node, capable of managing channels with RGB assets;
- Supporting other teams building solutions on RGB, to encourage diversity and a strong ecosystem.

This approach aims to cover the entire chain of needs: from the low-level library (*[RGBlib](https://github.com/RGB-Tools/rgb-lib)*), enabling the implementation of a wallet, to the production aspect (a Lightning node, a wallet for Android, etc.).

### The RGBlib library: simplifying the development of RGB applications

An important point in democratizing the creation of RGB wallets and applications is to make available an abstraction simple enough so that developers don't have to learn everything about the protocol's internal logic. This is precisely the aim of **RGBlib**, written in Rust.

RGBlib acts as a bridge between the highly flexible (but sometimes complex) requirements of RGB that we have been able to study in previous chapters, and the concrete needs of an application developer. In other words, a wallet (or service) wishing to manage token transfers, asset issuance, verification, etc., can rely on RGBlib without knowing every cryptographic detail or every customizable RGB parameter.

The bookshop offers :


- Turnkey functions for issuing (_issuance_) assets (fungible or not);
- The ability to transfer (send/receive) assets by manipulating simple objects (addresses, amounts, UTXOs, etc.);
- A mechanism for storing and loading the status information (*consignments*) required for Client-side Validation.

RGBlib therefore relies on complex notions specific to RGB (Client-side Validation, Tapret/Opret anchors), but encapsulates them so that the final application doesn't have to reprogram everything or make risky decisions. What's more, RGBlib is already binded in several languages (Kotlin and Python), opening the door to uses beyond a simple Rust universe.

### Iris Wallet: an example of an RGB wallet on Android

To prove the effectiveness of RGBlib, the Bitfinex team has developed **Iris Wallet**, exclusively on Android at this stage. It's a mobile wallet that illustrates a user experience similar to that of an ordinary Bitcoin wallet: you can issue an asset, send it, receive it, and view its history, while remaining on a self-custody model.

Iris has a number of interesting features:

**Using an Electrum server:**

Like any wallet, Iris needs to know about transaction confirmations on the blockchain. Rather than embedding a complete node, Iris defaults to an Electrum server maintained by the Bitfinex team. Users can, however, configure their own server or another third-party service. In this way, Bitcoin transactions can be validated and information retrieved (indexing) in a modular way.

**The RGB proxy server:**

Unlike Bitcoin, RGB requires the exchange of off-chain metadata (*consignments*) between sender and receiver. To simplify this process, Iris offers a solution where communication takes place via a proxy server. The receiving wallet generates an *invoice* that mentions where the sender should send the *client-side* data. By default, the URL points to a proxy hosted by the Bitfinex team, but you can change this proxy (or host your own). The idea is to return to a familiar user experience where the recipient displays a QR code, and the sender scans this code for the transaction, without any complex additional manipulations.

**Continuous backup:**

In a strictly Bitcoin context, backing up your seed is generally sufficient (although these days we recommend backing up the seed and descriptors instead). With RGB, this isn't enough: you also need to keep the local history (the *consignments*) proving that you really do own an RGB asset. Each time you receive a receipt, the device stores new data, which is essential for subsequent spending. Iris automatically manages an encrypted backup in the user's Google Drive. This requires no special trust in Google, as the backup is encrypted, and more robust options (such as a personal server) are planned for the future to avoid any risk of censorship or deletion by a third-party operator.

**Other features:**


- Create a faucet to quickly test or distribute tokens for experimentation or promotion;
- A certification system (currently centralized) to distinguish a legitimate token from a fake one copying a famous ticker. In the future, this certification may become more decentralized (via DNS or other mechanisms).

All in all, Iris offers a user experience close to that of a classic Bitcoin wallet, masking the additional complexity (stash management, *consignment* history, etc.) thanks to RGBlib and the use of a proxy server.

### Proxy server and user experience

The proxy server introduced above deserves to be detailed, as it is the key to a smooth user experience. Instead of the sender having to manually transmit the *consignments* to the recipient, the RGB transaction takes place in the background via a :


- The recipient generates an *invoice* (containing, among other things, the proxy address);
- The sender sends (via an HTTP request) a transition project (the *consignment*) to the proxy ;
- The recipient retrieves this project, executes the *client-side* validation locally;
- The recipient then publishes, via the proxy, the acceptance (or possibly rejection) of the state transition ;
- The sender can view the validation status and, if accepted, broadcast the Bitcoin transaction finalizing the transfer.

In this way, the wallet behaves almost like a normal wallet. The user is unaware of all the intermediate steps. Admittedly, the current proxy is neither encrypted nor authenticated (which leaves concerns about confidentiality and integrity), but these improvements are possible in later versions. The proxy concept remains extremely useful for recreating the "I send a QR code, you scan to pay" experience.

### RGB integration on the Lightning Network

Another key focus of the Bitfinex team's work is to make the Lightning Network compatible with RGB assets. The aim is to enable Lightning channels in USDT (or any other token), and to benefit from the same advantages as bitcoin on Lightning (near-instantaneous transactions, routing, etc.). In concrete terms, this involves creating a Lightning node modified to :


- Open a channel by placing not only satoshis, but also one or more RGB assets in the funding UTXO multisig ;
- Generate Lightning commitment transactions (Bitcoin side) accompanied by corresponding RGB state transitions. Each time the channel is updated, an RGB transition redefines the asset distribution in the Lightning outputs;
- Enable unilateral closure, where the asset is retrieved in an exclusive UTXO, in compliance with Lightning Network rules (HTLC, timelock, punishment, etc.).

This solution, dubbed "**RGB Lightning Node**", uses LDK (*Lightning Dev Kit*) as a base, and adds the mechanisms needed to inject RGB tokens into the channels. Lightning commitments retain the classic structure (puncturable outputs, timelock...), and in addition anchor an RGB state transition (via `Opret` or `Tapret`). For the user, this opens the way to Lightning channels in stablecoins or in any other asset emitted via RGB.

### DEX potential and impact on Bitcoin

Once several assets are managed via Lightning, it becomes possible to imagine an **atomic exchange** on a single Lightning routing path, using the same logic of secrets and timelocks. For example, user A holds bitcoin on one Lightning channel, and user B holds USDT RGB on another Lightning channel. They can build a path linking their two channels and simultaneously exchange BTC for USDT, without the need for trust. This is nothing more than an **atomic swap** taking place in several hops, making outside participants almost oblivious to the fact that they are making a trade, not just a routing. This approach offers :


- Very low latency, as everything remains off-chain on Lightning.
- A superior **privacy**: nobody knows it's a trade, and not a normal routing ;
- Avoiding frontrunning, a recurring problem for on-chain DEX ;
- Reduced costs (you don't pay blockspace, just Lightning routing fees).

We can then imagine an ecosystem where Lightning nodes offer swap prices (by providing liquidity). Each node, if it wishes, can play the role of _market maker_, buying and selling various assets on Lightning. This prospect of a _layer-2_ DEX reinforces the idea that it is not necessary to fork or use third-party blockchains to obtain decentralized asset exchanges.

The impact on Bitcoin could be positive: Lightning's infrastructure (nodes, channels and services) would be more fully utilized thanks to the volumes generated by these *stablecoins*, derivatives and other tokens. Merchants interested in USDT payments on Lightning would mechanically discover BTC payments on Lightning (managed by the same stack). The maintenance and financing of the Lightning Network infrastructure could also benefit from the multiplication of these non-BTC flows, which would indirectly benefit Bitcoin users.

### Conclusion and resources

The Bitfinex team dedicated to RGB illustrates, through its work, the diversity of what can be done on top of the protocol. On the one hand, there's RGBlib, a library that facilitates the design of wallets and applications. On the other, we have Iris Wallet, a practical demonstration on Android of a neat end-user interface. Finally, the integration of RGB with Lightning shows that stablecoin channels are possible, and opens the way to a potential decentralized DEX on Lightning.

This approach remains largely experimental and continues to evolve: the RGBlib library is being refined as we go along, Iris Wallet is receiving regular enhancements, and the dedicated Lightning node is not yet a mainstream Lightning client.

For those who wish to learn more or contribute, several resources are available, including :


- [GitHub RGB Tools repositories](https://github.com/RGB-Tools);
- [An information site dedicated to Iris Wallet](https://iriswallet.com/) to test the wallet on Android.

In the next chapter, we'll take a closer look at how to launch an RGB Lightning node.

## RLN - RGB Lightning Node

<chapterId>ecaabe32-20ba-5f8c-8ca1-a3f095792958</chapterId>

![vidéo](https://youtu.be/piQQH4Q2nr0)

In this final chapter, Frederico Tenga takes you step-by-step through setting up a Lightning RGB node on a Regtest environment, and shows you how to create RGB tokens on it. By launching two separate nodes, you'll also discover how to open a Lightning channel between them and exchange RGB assets.

This video serves as a tutorial, similar to what we covered in a previous chapter, but specifically focused on Lightning this time!

The main resource for this video is the Github repository [RGB Lightning Node](https://github.com/RGB-Tools/rgb-lightning-node), which makes it easy for you to launch this configuration in Regtest.

### Deploying an RGB-compatible Lightning node

The process takes up and puts into practice all the concepts covered in the previous chapters:


- The idea that **UTXO** blocked on a 2/2 multisig of a Lightning channel can receive not only bitcoins, but also be a Single-use Seal of RGB assets (fungible or not) ;
- The addition, in each Lightning engagement transaction, of an output (`Tapret` or `Opret`) dedicated to anchoring the RGB state transition;
- The associated infrastructure (bitcoind/indexer/proxy) to validate Bitcoin transactions and exchange *client-side* data.

### Introducing rgb-lightning-node

The **`rgb-lightning-node`** project is a Rust daemon based on an `rust-lightning` (LDK) fork modified to take into account the existence of RGB assets in a channel. When a channel is opened, the presence of assets can be specified, and each time the channel state is updated, an RGB transition is created, reflecting the distribution of the asset in the Lightning outputs. This enables :


- Open Lightning channels in USDT, for example;
- Route these tokens through the network, provided the routing paths have sufficient liquidity;
- Exploit Lightning's punishment and timelock logic without modification: simply anchor the RGB transition in an additional output of the commitment transaction.

The code is still at the alpha stage: we recommend using it in **regtest** or on the **testnet** only.

### Node installation

To compile and install the `rgb-lightning-node` binary, we start by cloning the repository and its sub-modules, then we run the :

```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```

![RGB-Bitcoin](assets/fr/098.webp)


- The `--recurse-submodules` option also clones the necessary sub-devices (including the modified version of `rust-lightning`);
- The `--shallow-submodules` option restricts the depth of the clone to speed up downloading, while still providing access to essential commits.

From the project root, run the following command to compile and install the binary :

```bash
cargo install --locked --debug --path .
```

![RGB-Bitcoin](assets/fr/099.webp)


- `--locked` ensures that the version of dependencies is strictly respected;
- `--debug` is not compulsory, but can help you focus (you can use `--release` if you prefer) ;
- `--path .` tells `cargo install` to install from the current directory.

At the end of this command, an `rgb-lightning-node` executable will be available in your `$CARGO_HOME/bin/`. Make sure this path is in your `$PATH` so you can invoke the command from any directory.

### Performance requirements

To function, the `rgb-lightning-node` daemon requires the presence and configuration of :


- A `bitcoind`** node

Each RLN instance will need to communicate with `bitcoind` to broadcast and monitor its on-chain transactions. Authentication (login/password) and URL (host/port) will need to be provided to the daemon.


- An indexer** (Electrum or Esplora)

The daemon must be able to list and explore on-chain transactions, in particular to find the UTXO on which an asset has been anchored. You'll need to specify the URL of your Electrum server or Esplora.


- An RGB** proxy

As seen in previous chapters, the **proxy server** is a component (optional, but highly recommended) to simplify the exchange of *consignments* between Lightning peers. Once again, a URL must be specified.

IDs and URLs are entered when the daemon is _unlocked_ via the API. More on this later.

### Regtest launch

For simple use, there's a `regtest.sh` script that automatically starts, via Docker, a set of services: `bitcoind`, `electrs` (indexer), `rgb-proxy-server`.

![RGB-Bitcoin](assets/fr/100.webp)

This allows you to launch a local, isolated, pre-configured environment. It creates and destroys containers and data directories on each reboot. We'll begin by starting the :

```bash
./regtest.sh start
```

This script will :


- Create a `docker/` directory to store ;
- Run `bitcoind` in regtest, as well as the indexer `electrs` and the `rgb-proxy-server` ;
- Wait until everything is ready to use.

![RGB-Bitcoin](assets/fr/101.webp)

Next, we'll launch several RLN nodes. In separate shells, run, for example (to launch 3 RLN nodes) :

```bash
# 1st shell
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network regtest
# 2nd shell
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network regtest
# 3rd shell
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network regtest
```

![RGB-Bitcoin](assets/fr/102.webp)


- The `--network regtest` parameter indicates the use of the regtest configuration;
- `--daemon-listening-port` indicates on which REST port the Lightning node will listen for API calls (JSON);
- `--ldk-peer-listening-port` specifies which Lightning p2p port to listen on;
- `dataldk0/`, `dataldk1/` are the paths to the storage directories (each node stores its info separately).

You can also run commands on your RLN nodes from your browser:

```url
https://rgb-tools.github.io/rgb-lightning-node/
```

For a node to open a channel, it must first have bitcoins on an address generated with the following command (for node n°1, for example):

```bash
curl -X POST http://localhost:3001/address
```

The answer will provide you with an address.

![RGB-Bitcoin](assets/fr/103.webp)

On the `bitcoind` Regtest, we're going to mine a few bitcoins. Run :

```bash
./regtest.sh mine 101
```

![RGB-Bitcoin](assets/fr/104.webp)

Send funds to the node address generated above:

```bash
./regtest.sh sendtoaddress <address> <amount>
```

![RGB-Bitcoin](assets/fr/105.webp)

Then mine a block to confirm the transaction:

```bash
./regtest.sh mine 1
```

![RGB-Bitcoin](assets/fr/106.webp)

### Testnet launch (without Docker)

If you want to test a more realistic scenario, you can launch 3 RLN nodes on the Testnet rather than in Regtest, pointing to public services :

```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```

By default, if no configuration is found, the daemon will try to use the :


- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- `bitcoind_rpc_port`: `18332`
- indexer_url`: `ssl://electrum.iriswallet.com:50013`
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-rpc`

With login :


- `bitcoind_rpc_username`: `user`
- `bitcoind_rpc_username`: `password`

You can also customize these elements via the `init`/`unlock` API.

### Issuing an RGB token

To issue a token, we'll start by creating "colorable" UTXOs:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"up_to": false,
"num": 4,
"size": 2000000,
"fee_rate": 4.2,
"skip_sync": false
}' \
http://localhost:3001/createutxos
```

![RGB-Bitcoin](assets/fr/107.webp)

You can, of course, adapt the order. To confirm the transaction, we mine a :

```bash
./regtest.sh mine 1
```

We can now create an RGB asset. The command will depend on the type of asset you wish to create and its parameters. Here I'm creating a NIA (*Non Inflatable Asset*) token named "PBN" with a supply of 1000 units. The `precision` allows you to define the divisibility of the units.

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amounts": [
1000
],
"ticker": "PBN",
"name": "Plan B Network",
"precision": 0
}' \
http://localhost:3001/issueassetnia
```

![RGB-Bitcoin](assets/fr/108.webp)

The response includes the ID of the newly created asset. Remember to note this identifier. In my case, it's :

```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```

![RGB-Bitcoin](assets/fr/109.webp)

You can then transfer it on-chain, or allocate it in a Lightning channel. That's exactly what we're going to do in the next section.

### Opening a channel and transferring an RGB asset

You must first connect your node to a peer on the Lightning network using the `/connectpeer` command. In my example, I control both nodes. So I'll retrieve the public key of my second Lightning node with this command:

```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```

The command returns the public key of my node n°2 :

```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```

![RGB-Bitcoin](assets/fr/110.webp)

Next, we'll open the channel by specifying the relevant asset (`PBN`). The `/openchannel` command lets you define the size of the channel in satoshis and opt to include the RGB asset. It depends on what you want to create, but in my case, the command is :

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"peer_pubkey_and_opt_addr": "031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94@localhost:9736",
"capacity_sat": 1000000,
"push_msat": 10000000,
"asset_amount": 500,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"public": true,
"with_anchors": true,
"fee_base_msat": 1000,
"fee_proportional_millionths": 0,
"temporary_channel_id": "a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5"
}' \
http://localhost:3001/openchannel
```

Find out more here:


- `peer_pubkey_and_opt_addr`: Identifier of the peer we wish to connect to (the public key we found earlier);
- `capacity_sat`: Total channel capacity in satoshis ;
- `push_msat`: Amount in millisatoshis initially transferred to the peer when the channel is opened (here I immediately transfer 10,000 sats so that he can make an RGB transfer later) ;
- `asset_amount`: Amount of RGB assets to be committed to the channel ;
- `asset_id` : Unique identifier of the RGB asset engaged in the channel;
- `public`: Indicates whether the channel should be made public for routing on the network.

![RGB-Bitcoin](assets/fr/111.webp)

To confirm the transaction, 6 blocks are mined:

```bash
./regtest.sh mine 6
```

![RGB-Bitcoin](assets/fr/112.webp)

The Lightning channel is now open and also contains 500 `PBN` tokens on node n°1's side. If node n°2 wishes to receive `PBN` tokens, it must generate an invoice. Here's how to do it:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amt_msat": 3000000,
"expiry_sec": 420,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"asset_amount": 100
}' \
http://localhost:3002/lninvoice
```

With :


- `amt_msat`: Invoice amount in millisatoshis (minimum 3000 sats) ;
- `expiry_sec` : Invoice expiry time in seconds ;
- `asset_id` : Identifier of the RGB asset associated with the invoice ;
- `asset_amount`: Amount of RGB asset to be transferred with this invoice.

In response, you will get an RGB invoice (as described in previous chapters):

```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```

![RGB-Bitcoin](assets/fr/113.webp)

We will now pay this invoice from the first node, which holds the necessary cash with the `PBN` token:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```

![RGB-Bitcoin](assets/fr/114.webp)

Payment has been made. This can be verified by executing the command :

```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```

![RGB-Bitcoin](assets/fr/115.webp)

Here's how to deploy a Lightning node modified to carry RGB assets. This demonstration is based on :


- A regtest environment (via `./regtest.sh`) or testnet ;
- A Lightning node (`rgb-lightning-node`) based on a `bitcoind`, an indexer and an `rgb-proxy-server` ;
- A series of JSON REST APIs for opening/closing channels, issuing tokens, transferring assets via Lightning, etc.

Thanks to this process :


- Lightning engagement transactions include an additional output (OP_RETURN or Taproot) with the anchoring of an RGB transition;
- Transfers are made in exactly the same way as traditional Lightning payments, but with the addition of an RGB token;
- Multiple RLN nodes can be linked to route and experiment with payments across multiple nodes, provided there is sufficient liquidity in both bitcoins and asset RGB on the path.

The project remains in the alpha stage. It is therefore strongly recommended that you limit yourself to test environments (regtest, testnet).

The opportunities opened up by this LN-RGB compatibility are considerable: stablecoins on Lightning, DEX layer-2, transfer of fungible tokens or NFTs at very low cost... The previous chapters have outlined the conceptual architecture and validation logic. Now you have a practical view of how to get such a node up and running, for your future developments or tests.

# Conclusion

<partId>b0baebfc-d146-5938-849a-f835fafb386f</partId>

## Reviews & Ratings

<chapterId>0217e8b0-942a-5fee-bd91-9a866551eff3</chapterId>

<isCourseReview>true</isCourseReview>

## Conclusion

<chapterId>0309536d-c336-56a0-869e-a8395ed8d9ae</chapterId>

<isCourseConclusion>true</isCourseConclusion>
