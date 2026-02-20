---
name: Programming Bitcoin
goal: Build a complete Bitcoin library from scratch and understand Bitcoin's cryptographic foundations
objectives: 
 - Implement finite field arithmetic and elliptic curve operations in Python
 - Construct and parse Bitcoin transactions programmatically
 - Create testnet addresses and broadcast transactions over the network
 - Master the mathematical foundations underlying Bitcoin's security model
---
# A Journey into Bitcoin's Scripts and Programs

This intensive two-day course, taught by Jimmy Song, takes you deep into Bitcoin's technical foundations by building a complete Bitcoin library from the ground up. Starting with the essential mathematics of finite fields and elliptic curves, you'll progress through transaction parsing, script execution, and network communication. Through hands-on coding exercises in Jupyter notebooks, you'll create your own testnet address, construct transactions manually, and broadcast them directly to the network—all while gaining a profound understanding of the cryptographic principles that make Bitcoin secure and trustless.

Enjoy the journey!

+++

# Introduction

<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>

## Course Overview

<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>

Welcome to the course PRO 202 _**Programming Bitcoin**_, an intensive journey that takes you from finite field arithmetic all the way to building and broadcasting real transactions on Bitcoin’s Testnet.

In this course, you will progressively build a Bitcoin library in Python while acquiring the cryptographic, protocol, and software foundations necessary to reason precisely about Bitcoin’s security and inner workings. The PRO 202 approach is thoroughly hands-on: every concept is immediately implemented in Jupyter notebooks, ensuring that theory and code strengthen each other.

### Essential Mathematical Concepts for Bitcoin

This first section establishes the indispensable mathematical groundwork. You will implement finite field arithmetic and elliptic curve operations (group law, addition, doubling, scalar multiplication...) — the prerequisites for ECDSA. The goal is twofold: to understand the algebraic structure that makes cryptographic signatures possible and to build reliable Python tools for manipulating them.

You will then formalize the components of ECDSA: key generation, point formatting, hashing, signature creation, and verification. This section directly connects theory to practice, emphasizing implementation details and the robustness of the underlying security model.

### Bitcoin Transaction Inner Workings

In the second section, you will dissect the structure of a Bitcoin transaction: UTXOs, inputs/outputs, sequences, scripts, encodings, and more. You will write code to construct, sign, and verify transactions, gaining a precise understanding of what is committed by the hash and why.

Next, you will implement a minimal _Script_ executor, review key opcodes, and validate spending paths. The objective is to make you capable of auditing transaction behavior, diagnosing validation failures, and reasoning about the safety of spending policies.

### Bitcoin Network Inner Workings

In the third section, you will place transactions within the broader system: block structure, headers, difficulty, and the Proof-of-Work mechanism. You will handle protocol messages, block headers, and Merkle trees.

Finally, you will study peer-to-peer node communication, message optimization, and the introduction of SegWit.

As with every course on Plan ₿ Academy, the final section includes an evaluation designed to consolidate your understanding. Ready to uncover the inner workings of Bitcoin and write the code that powers it? Let’s begin!









# Essential Mathematical Concepts for Bitcoin
<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>

## Mathematics for Bitcoin Implementation
<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)

### Bitcoin Programming Foundations: Core Mathematical Structures

This course condenses the essential mathematics behind Bitcoin’s cryptographic systems into a highly practical workflow. Concepts are explained, demonstrated with examples, and then implemented in Jupyter Notebook. The guiding idea is simple: you only truly understand a cryptographic primitive once you code it. Across the two-day structure, students generate testnet addresses, build and broadcast [transactions](https://planb.academy/resources/glossary/transaction-tx), and eventually interact with the network without block explorers. All of this requires a solid foundation in finite fields and elliptic curves.

### Finite Fields: The Arithmetic Engine of Cryptography

A finite field F(p) is an arithmetic system defined by a prime number p, containing elements 0 through p–1. Prime fields ensure every non-zero element has an inverse and all operations remain within the field. Arithmetic wraps around using modulo p for addition, subtraction, and multiplication. Python’s `pow(base, exp, mod)` enables efficient modular exponentiation, crucial for large exponents used in real cryptographic operations.

#### Multiplicative Behavior
Multiplying any non-zero element k by all elements of a prime field produces a permutation of the field. This property guarantees uniformity and prevents structural weaknesses, making prime fields ideal for secure key generation and [digital signatures](https://planb.academy/resources/glossary/digital-signature).

#### Division and Fermat’s Little Theorem
Division is implemented via multiplicative inverses. Fermat’s Little Theorem states that  
n^(p–1) ≡ 1 (mod p),
so the inverse is n^(p–2). Python supports this directly with `pow(n, -1, p)`. These operations appear constantly in [ECDSA](https://planb.academy/resources/glossary/ecdsa) and Bitcoin’s underlying cryptographic routines.

### Elliptic Curves: Nonlinear Structures for Public-Key Security

Elliptic curves follow the equation y² = x³ + ax + b. Bitcoin uses secp256k1, defined as y² = x³ + 7 over a finite field. Points on an elliptic curve form a mathematical group under point addition. A line drawn through two points P and Q intersects the curve at a third point R; reflecting R across the x-axis yields P + Q. This system is associative and includes an identity element: the point at infinity.

Doubling a point uses a tangent line instead of a secant line, with slope derived from the curve’s derivative. Although these formulas involve calculus over real numbers, they become fully discrete and exact when the curve is defined over a finite field—the context used in Bitcoin.

### From Mathematics to Bitcoin Cryptography

Finite fields provide deterministic, invertible arithmetic; elliptic curves provide a nonlinear structure where computing k·P is easy but reversing it is computationally infeasible. Combining both yields the foundation for Bitcoin’s public/private keys, ECDSA signatures, and transaction security. Understanding these fundamentals prepares students to implement keys, transactions, and signatures directly—without abstractions or external tools.

## Elliptic Curve Cryptography
<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)

This chapter introduces elliptic curves defined over finite fields and explains why they form the mathematical backbone of Bitcoin’s [cryptography](https://planb.academy/resources/glossary/cryptography). While elliptic curves over real numbers appear smooth and continuous, applying the same equations over a finite field creates a discrete, scattered set of points. Despite the visual difference, all point addition formulas, slopes, and algebraic rules behave exactly the same—only the arithmetic changes to modular arithmetic. Bitcoin uses the curve y² = x³ + 7 (secp256k1), which preserves symmetry and nonlinear behavior essential for cryptographic security.

### Verifying Points and Finite Field Implementation

A point lies on a finite-field elliptic curve if its coordinates satisfy the curve equation under modulo p. Verifying a point such as (73,128) on F₁₃₇ requires checking that y² mod p equals x³ + 7 mod p. Implementing this in code involves creating classes for finite field elements and curve points. Operator overloading ensures that all arithmetic—addition, multiplication, exponentiation, division—is automatically performed modulo p. Once these abstractions exist, more advanced cryptographic operations become straightforward to write and reason about.

#### Group Properties and Point Addition
Elliptic curve points form a mathematical group under addition. The group satisfies closure, associativity, identity (the point at infinity), and inverses (reflection across the x-axis). Geometric constructions confirm these properties, making scalar multiplication (P added to itself repeatedly) well defined. These group rules enable elliptic curve cryptography and ensure consistent, predictable behavior under repeated point operations.

### Cyclic Groups and the Discrete Logarithm Problem

Choosing a generator point G on a curve allows us to generate a cyclic group: G, 2G, 3G, …, nG = 0. The points appear nonlinear and unpredictable, even when generated sequentially. This unpredictability creates the foundation for the discrete logarithm problem: computing P = sG is easy, but determining s from P is computationally infeasible for large groups. This one‑way function is what makes [public key](https://planb.academy/resources/glossary/public-key) cryptography secure. Scalars ([private keys](https://planb.academy/resources/glossary/private-key)) are written in lowercase; points (public keys) in uppercase.

#### Efficient Scalar Multiplication
To compute sG efficiently, implementations use the double‑and‑add algorithm: scanning the scalar’s binary representation, doubling the point each step, and adding G only when the bit is 1. This reduces computation from O(n) additions to O(log n), enabling practical cryptographic operations even with 256‑bit scalars.

#### The secp256k1 Curve in Bitcoin

Bitcoin uses the curve secp256k1, defined by y² = x³ + 7 over a prime field where p = 2²⁵⁶ − 2³² − 977. The generator point G has fixed coordinates chosen using a deterministic NUMS (“nothing up my sleeve”) procedure. The group order n is a large prime close to 2²⁵⁶, ensuring that every nonzero point generates the same group. The size of 2²⁵⁶ (~10⁷⁷) is astronomically large, making brute‑forcing private keys physically impossible. Even a trillion supercomputers running for a trillion years would not meaningfully reduce the key space.

### Public Keys, Private Keys, and SEC Serialization

A private key is a random scalar s; the public key is P = sG. Because solving the discrete log problem is infeasible, P can be shared without revealing s. Public keys must be serialized for transmission using SEC format. Uncompressed SEC format uses 65 bytes: prefix 0x04 + x‑coordinate + y‑coordinate. The compressed format uses only 33 bytes: prefix 0x02 or 0x03 (depending on y’s parity) + x‑coordinate. Bitcoin originally used uncompressed keys but now prefers compressed ones for efficiency.

#### Bitcoin Address Creation

Bitcoin addresses are hashes of public keys, not the raw keys themselves. To generate an address, serialize the public key in SEC format, compute hash160 (SHA‑256 then RIPEMD‑160), prepend the network prefix (0x00 for mainnet, 0x6F for testnet), compute a checksum using double SHA‑256, append the first four checksum bytes, and encode the result using Base58. This encoding removes ambiguous characters and includes the checksum to prevent transcription errors. The multi‑step pipeline hides the public key until a spend occurs, adds network identification, and ensures human‑readable, error‑resistant addresses.

# Bitcoin Transaction Inner Workings
<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>

## Bitcoin Transaction Parsing and ECDSA Signatures
<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)

### Understanding ECDSA: Bitcoin's Digital Signature Foundation

Bitcoin relies on ECDSA, an elliptic curve–based signature scheme offering strong security with far smaller key sizes than RSA. Its security comes from the elliptic curve discrete logarithm problem: given P = eG, computing P is easy, but deriving e from P is computationally infeasible. This asymmetry enables public key cryptography while keeping private keys secure.

#### DER Encoding of ECDSA Signatures

Bitcoin encodes ECDSA signatures using the DER format:  
- 0x30 (sequence marker)  
- length byte  
- 0x02 + length + R bytes  
- 0x02 + length + S bytes  

This adds overhead, expanding a 64‑byte signature to ~71–72 bytes. [Taproot](https://planb.academy/resources/glossary/taproot) eliminates this inefficiency by adopting fixed‑size [Schnorr](https://planb.academy/resources/glossary/schnorr-protocol) signatures.

### Signature Commitments and the Signing Process

ECDSA signatures rely on a commitment equation: UG + VP = KG. The signer selects non‑zero U and V values, and a random [nonce](https://planb.academy/resources/glossary/nonce) K, proving knowledge of the private key without revealing it. The message is hashed into Z, a random K is generated, R is the x‑coordinate of KG, and S = (Z + RE)/K. The signature is the pair (R, S). Security critically depends on using a unique, unpredictable K—if K is reused or leaked, the private key is compromised. Modern implementations use deterministic K generation (RFC 6979) to avoid RNG failures.

#### Signature Verification
Given Z, (R, S), and public key P, the verifier computes U = Z/S and V = R/S, then checks whether the x‑coordinate of UG + VP equals R. This works because the verification algebra reconstructs KG without needing the private key. Forging signatures would require solving the discrete log problem or breaking the hash function.

#### Schnorr Signatures and Historical Context

Schnorr signatures are mathematically cleaner and support aggregation features, but were patented when Bitcoin launched. ECDSA offered a free alternative, though with more complexity and larger signatures. With the patents expired, Bitcoin added Schnorr signatures via Taproot, providing fixed 64‑byte signatures and improved privacy. ECDSA remains supported for legacy compatibility.


### Transaction Structure and Inputs/Outputs

A Bitcoin transaction consists of:  
- version (4 bytes, little‑endian)  
- input list  
- output list  
- locktime (4 bytes)

Inputs reference previous [UTXOs](https://planb.academy/resources/glossary/utxo) by their transaction hash and output index, and include an unlocking [script](https://planb.academy/resources/glossary/script) (scriptSig) and a sequence number used for timelocks or RBF. Outputs specify the amount (8 bytes) and the locking script (scriptPubKey), defining spending conditions. Bitcoin addresses are representations of these scripts.

#### The UTXO Model
Bitcoin tracks unspent outputs rather than account balances. UTXOs must be spent entirely—partial spending is impossible. To spend 1 BTC from a 100 BTC UTXO, a transaction must include a change output. Forgetting the change output turns the remainder into a miner fee.

#### Transaction Serialization and Parsing

Transactions use a compact binary format. After the version field, a varint encodes the number of inputs. Inputs include:  
- previous tx hash (32 bytes)  
- output index (4 bytes)  
- scriptSig (varstr)  
- sequence (4 bytes)

Outputs include an 8‑byte amount and scriptPubKey (varstr). Locktime controls when the transaction becomes valid. Serialization uses little‑endian ordering for most integers. Parsers consume bytes sequentially and delegate to specialized classes for inputs, outputs, and scripts.

### Fees, Change, and Malleability

Fees are implicit:  
fee = sum(input values) – sum(output values).  
Any unassigned value becomes the fee, making correct change output construction essential. Before [SegWit](https://planb.academy/resources/glossary/segwit), signatures allowed malleability—modifying S to N-S produced a new valid transaction with a different ID. Bitcoin now enforces a low‑S rule, and SegWit isolates signatures from the txid calculation, making IDs stable and enabling second‑layer protocols like [Lightning](https://planb.academy/resources/glossary/lightning-network).

## Bitcoin Script and Transaction Validation
<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)

Bitcoin Script is a small, stack-based smart contract language that defines how coins can be spent. Every output carries a scriptPubKey (locking script) and every input carries a scriptSig (unlocking script). Together they form a program that must evaluate to “true” for the spend to be valid. Script is intentionally not Turing-complete so that all execution paths are predictable and easy to validate across the network.

### Script Operations and Execution Model

A script is a sequence of data elements and opcodes. Data pushes (signatures, public keys, hashes) are placed onto the stack, while opcodes starting with `OP_` transform the stack. After execution, the top stack element must be non-zero for success. Examples: `OP_DUP` duplicates the top element, `OP_HASH160` applies SHA256 then RIPEMD160, and `OP_CHECKSIG` verifies a signature against the transaction’s sighash and a public key, pushing 1 for valid, 0 for invalid. Parsing rules distinguish between raw data (length-prefixed) and opcodes (looked up by byte value), and a small virtual machine executes them deterministically on every [node](https://planb.academy/resources/glossary/node).

### P2PK and P2PKH: Core Payment Patterns

The earliest pattern, Pay-to-Public-Key (P2PK), locked coins directly to a full public key: the scriptPubKey is `<pubkey> OP_CHECKSIG`, and the scriptSig is just a signature. It is simple but space-inefficient and exposes the public key before the coins are spent.

#### P2PKH and Addresses
Pay-to-Public-Key-Hash (P2PKH) improves this by locking to a 20‑byte hash of the public key. The scriptPubKey is `OP_DUP OP_HASH160 <pubkey_hash> OP_EQUALVERIFY OP_CHECKSIG`, and the scriptSig provides `<signature> <pubkey>`. Execution checks that the provided public key hashes to the committed value and then verifies the signature. This hides the public key until spend time, reduces size, and matches the familiar “1…” mainnet address format.

### Transaction Validation and Signature Hashing

A node validating a transaction must ensure:  
1) Each input references an existing, unspent output.  
2) Total input value ≥ total output value (the difference is the fee).  
3) Each scriptSig correctly unlocks its referenced scriptPubKey.

Signature verification requires constructing the exact message that was signed, called the sighash. For legacy ECDSA, validation empties all scriptSigs, replaces the current input’s scriptSig with the corresponding scriptPubKey, appends a 4‑byte hash type (usually `SIGHASH_ALL`), and double‑hashes the result. That 256‑bit value is what `OP_CHECKSIG` uses. Alternative hash types (e.g., `SINGLE`, `NONE`, with or without `ANYONECANPAY`) change which parts of the transaction are committed to, enabling niche use cases like collaborative funding or partially specified transactions, but they are rarely used in practice.

#### Quadratic Hashing and SegWit
Because each input in a legacy transaction requires its own sighash computation over a structure that includes all inputs, validation time can grow quadratically with the number of inputs. Large multi‑input transactions once caused noticeable validation delays. SegWit redesigned sighash calculation to cache shared parts and reduce complexity to linear time, improving scalability and making denial‑of‑service attacks harder.

### Script Puzzles and Security Lessons

Script can express far more than simple “one signature unlocks these coins.” Script puzzles demonstrate this by encoding arbitrary conditions—math problems, hash preimage challenges, or even collision bounties—where anyone who provides the correct data can spend the coins. However, outputs that rely only on public data (no signatures) are vulnerable to [miner](https://planb.academy/resources/glossary/miner) front‑running: once a valid solution appears in the [mempool](https://planb.academy/resources/glossary/mempool), any miner can copy it and redirect the payout to themselves.

The practical lesson is that real-world contracts almost always include signature checks, even when they contain more complex logic such as multisig, timelocks, or hashlocks. Signatures bind the solution to a specific party, preserving incentives and preventing others from stealing the payout. Understanding Script’s stack model, standard patterns, and subtle pitfalls is essential for designing secure Bitcoin smart contracts and for reasoning about how transactions are actually validated on the network.

## Transaction Construction and Pay-to-Script Hash

<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)

### Building Bitcoin Transactions and P2SH

Bitcoin transaction construction bridges theoretical protocol knowledge with practical implementation. A transaction selects UTXOs to spend, builds outputs with locking scripts, creates signatures for each input, and serializes everything in the exact format nodes expect. The process requires understanding sighash generation, Script behavior, and correct fee and change handling.

### Basic Transaction Construction

Each transaction input references a previous output by txid and index. Outputs specify amounts in satoshis and locking scripts. The difference between total inputs and total outputs is the fee. To sign an input, a modified version of the transaction is serialized, its sighash is computed, and the private key signs it. The resulting signature and public key form the ScriptSig. Once every input is signed, the raw transaction can be broadcast to the network.

### Multisignature Transactions

Bare multisig uses `OP_CHECKMULTISIG` to require m-of-n signatures. Due to an early off-by-one bug, OP_CHECKMULTISIG consumes an extra stack element, requiring an initial `OP_0` in the ScriptSig. Bare multisig is functional but inefficient: all public keys appear on-chain, making scriptPubKeys large, expensive, and difficult to encode as addresses. These limitations motivated the introduction of pay-to-script-hash.

#### P2SH Architecture
P2SH hides complex scripts behind a 20-byte HASH160. The scriptPubKey is fixed: `OP_HASH160 <20-byte hash> OP_EQUAL`. The underlying redeem script—containing multisig, timelocks, or other conditions—is only revealed and executed when spending. The sender only sees the hash, while the receiver manages the redeem script privately. This design reduces on-chain size, improves privacy, and enables complex contracts without burdening senders.

### P2SH Spending and Implementation

To spend a P2SH output, the ScriptSig must include the necessary unlocking data *plus* the redeem script itself. Validation occurs in two steps:  
1) HASH160(redeem_script) must match the scriptPubKey hash.  
2) After verification, the redeem script is executed with the provided data.

When generating signatures for a P2SH input, the sighash process uses the redeem script in place of the scriptPubKey. Each signer must possess the full redeem script to generate valid signatures. P2SH addresses use version byte 0x05 on mainnet (“3…” addresses) and 0xC4 on testnet (“2…” addresses).

#### Practical Security Considerations

Losing a redeem script means losing funds: spending requires both the private keys and the redeem script itself. Multisig participants must verify that their public keys are correctly included before accepting deposits. P2SH supports advanced constructions like multisig, timelocks, and hashlocks, but errors in script logic can permanently lock funds, so testing on testnet is essential.

P2SH improves privacy by hiding spending conditions until the first spend, but once the redeem script appears on-chain, it becomes permanently visible. Despite this, the benefits of reduced size, backward compatibility, and flexible contract support made P2SH a major milestone, influencing later upgrades such as SegWit and Taproot.

# Bitcoin Network Inner Workings
<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>

## Bitcoin Blocks and Proof of Work
<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)

Bitcoin [blocks](https://planb.academy/resources/glossary/block) group transactions and secure them using [proof of work](https://planb.academy/resources/glossary/proof-of-work). Each block includes an 80‑byte [header](https://planb.academy/resources/glossary/block-header) plus a list of transactions. Despite the heavy energy cost of producing a valid block, verifying one is cheap: storing all ~900k headers requires only ~72 MB, allowing even small devices to verify the chain’s proof of work efficiently.

### Coinbase Transactions and Block Rewards

Each block begins with exactly one [Coinbase transaction](https://planb.academy/resources/glossary/coinbase-transaction)—the only way new bitcoin enter circulation. It has a zeroed prev-tx hash and an index of 0xffffffff, uniquely identifying it. The subsidy started at 50 BTC and halves every 210,000 blocks (50, 25, 12.5, 6.25, 3.125, …). Miners also include transaction fees. Because the 4‑byte nonce is too small for modern ASICs, miners modify data in the Coinbase transaction to change the [Merkle](https://planb.academy/resources/glossary/merkle-tree) root and create additional search space. [BIP34](https://planb.academy/resources/glossary/bip) requires embedding the block height in the Coinbase scriptSig to ensure every Coinbase txid is unique.

### Block Header Fields and Soft Fork Signaling

The 80‑byte header contains:  
- version (4 bytes)  
- previous block hash (32 bytes)  
- Merkle root (32 bytes)  
- timestamp (4 bytes)  
- bits ([difficulty](https://planb.academy/resources/glossary/difficulty) target, 4 bytes)  
- nonce (4 bytes)

Version numbers evolved into a bit‑field signaling system via BIP9, allowing miners to coordinate [soft-fork](https://planb.academy/resources/glossary/soft-fork) readiness. The timestamp is a 32‑bit Unix time value and will need updating around the year 2106.

#### Bits Field and Targets  
The bits field encodes the target in compact form: target = coefficient × 256^(exponent−3). Valid block hashes must be numerically below this target. Because hashes are interpreted as little-endian integers, valid hashes often appear with many trailing zeros when displayed in hex.

### Difficulty, Validation, and Adjustments

Difficulty is defined as lowest_target / current_target, expressing how much harder mining is today compared to the easiest possible difficulty. Validation requires only comparing the hash of the header to the target—extremely cheap relative to mining.

Every 2016 blocks, Bitcoin adjusts difficulty to target ~10‑minute block intervals. The adjustment compares the actual time for the previous 2016 blocks with the expected two weeks. Limits constrain adjustments to within a factor of four. Major real‑world events—such as China’s mining ban—demonstrated this mechanism’s resilience when hash rate dropped sharply and difficulty adjusted downward to compensate.

### Block Subsidy and Total Supply

The subsidy at height h is computed as: subsidy = 5_000_000_000 >> (h // 210_000). This yields the halving schedule that converges toward a total supply of ~21 million BTC. Summing the geometric series (50 + 25 + 12.5 + …) × 210,000 explains the cap. Miners may claim less than the allowed subsidy but never more, or the block becomes invalid. As subsidies shrink over successive halvings, transaction fees become an increasingly important component of miner revenue and long‑term network security.

## Network Communication and Merkle Trees
<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)

### Bitcoin Network Architecture

Bitcoin’s [peer-to-peer](https://planb.academy/resources/glossary/peertopeer-p2p) network operates as a decentralized gossip system where nodes relay transactions and blocks without trusting one another. New nodes bootstrap by contacting hardcoded DNS seeds maintained by core developers. These DNS seeds return IPs of active peers, enabling nodes to discover the network and then request additional peers via getaddr. Networking is intentionally not [consensus](https://planb.academy/resources/glossary/consensus)‑critical, so implementations may differ as long as consensus rules remain unchanged.

### Message Structure and Handshake

All Bitcoin P2P messages use a fixed envelope: a 4‑byte magic value (F9BEB4D9 for mainnet), a 12‑byte ASCII command, a 4‑byte little‑endian payload length, a 4‑byte checksum (first 4 bytes of [hash](https://planb.academy/resources/glossary/hash-function)256), and the payload. Common commands include version, verack, inv, getdata, tx, block, getheaders, headers, ping, and pong.

The handshake begins when a connecting node sends a version message. The receiver replies with verack and its own version. Once both sides exchange these two messages, the connection is active and nodes may begin relaying inventories and data.

### Merkle Trees and Merkle Roots

Bitcoin stores a single 32‑byte Merkle root in each block header as a commitment to all transactions in the block. Transactions are hashed (hash256), paired, concatenated, and hashed repeatedly until one hash remains. When a level has an odd count, the last hash is duplicated. Internally, hashes are big‑endian, while serialized block data uses little‑endian, requiring reversals before and after tree construction.

#### Merkle Proofs and SPV  
Merkle proofs allow verifying that a transaction is included in a block without downloading the entire block. The proof consists of sibling hashes along the path to the root. Lightweight SPV clients store only block headers and request these proofs from [full nodes](https://planb.academy/resources/glossary/full-node). Because a Merkle tree grows logarithmically, proving inclusion in a block with thousands of transactions requires only a few hundred bytes.

Taproot extends this concept by committing spending conditions to a Merklized script tree (MAST), revealing only the executed branch along with a Merkle proof. This improves both efficiency and privacy.

### Network Operations and Block Synchronization

Nodes use getdata to request transactions or blocks, specifying a type ID (1=tx, 2=block, 3=filtered block, 4=compact block) plus a 32‑byte identifier. For chain sync, nodes send getheaders with a starting block hash, receiving up to 2000 headers in response. Each returned header is 80 bytes followed by a dummy transaction count of zero.

Full verification of received blocks requires two checks:  
1. The block hash must be below the target encoded in the bits field.  
2. The Merkle root computed from all transactions (with proper endianness handling) must match the header’s root.  

Only if both conditions succeed does a node accept the block, reflecting Bitcoin’s “don’t trust, verify” principle.

## Advanced Node Communication and Segregated Witness
<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)

This session unifies advanced P2P networking with Segregated Witness, showing how modern Bitcoin software interacts directly with nodes while using SegWit-aware transaction structures. Developers learn to retrieve blocks, scan for relevant transactions, and construct transactions using only raw network communication—no block explorers required.

### Block-Based Transaction Retrieval and Privacy

[Wallets](https://planb.academy/resources/glossary/wallet) must detect incoming payments by scanning blocks for outputs matching their scriptPubKey. Retrieving whole blocks protects privacy better than requesting individual transactions, which leaks strong signals about user activity. Even block requests may leak information on low-volume chains, making compact block filters (BIP158) essential for privacy‑preserving light clients. Filters may produce false positives but never false negatives, allowing clients to download only potentially relevant blocks without revealing specific addresses.

### Trustless Network Interaction

The `get_block` workflow demonstrates proper network usage: send getdata, receive a block, then independently verify its Merkle root and proof of work. A block is accepted only if the received header hash matches the requested hash and its computed Merkle root matches the header. This embodies “don’t trust, verify,” ensuring even malicious peers cannot trick nodes into accepting altered data.

#### Retrieving Transactions from Blocks  
A block’s transactions can be scanned for matching scriptPubKeys using simple iteration. Production wallets perform this continuously as new blocks arrive, proving ownership of outputs strictly through cryptographic validation rather than relying on third‑party APIs.

### SegWit Goals and Design

Segregated Witness (SegWit) fixed transaction malleability by removing signature data from the txid calculation. This enabled reliable pre‑signed transaction chains and made the Lightning Network practical. SegWit also increased block capacity using “block weight”: old nodes still see ≤1 MB blocks, while upgraded nodes validate up to 4 MB including witness data. Versioned witness programs (v0–v1 so far) create a structured upgrade path for future script types.

#### P2WPKH (Native SegWit)

P2WPKH replaces the legacy P2PKH structure with a 22‑byte script: OP_0 + push20 + hash160(pubkey). Spending moves the signature and pubkey into a separate witness field.  
- Pre‑SegWit nodes: see “anyone‑can‑spend,” treat it as valid.  
- Post‑SegWit nodes: recognize OP_0 + 20‑byte hash and validate using witness data.

This separation fixes malleability and reduces fees. The witness uses a varint count followed by the signature and pubkey.

#### P2SH-P2WPKH (Backward-Compatible SegWit)

To allow old wallets to send to SegWit addresses, P2WPKH scripts can be wrapped in P2SH.  
- scriptPubKey: standard P2SH hash160(redeemScript)  
- scriptSig: the redeemScript (the P2WPKH program)  
- witness: signature + pubkey  

Validation layers:  
1. Pre‑BIP16 nodes accept the redeemScript as valid.  
2. Post‑BIP16 nodes evaluate it, leaving OP_0 + hash on the stack.  
3. SegWit nodes perform full witness validation.

#### P2WSH for Complex Scripts

P2WSH generalizes SegWit for multisig and advanced scripts by committing to SHA256(script) instead of hash160. A typical 2‑of‑3 multisig witness stack:  
- empty element (CHECKMULTISIG bug)  
- sig1  
- sig2  
- witness script (the multisig script)

SegWit nodes verify SHA256(witnessScript) matches the scriptPubKey hash and then execute it. Using SHA256 and a 32‑byte hash allows distinguishing P2WSH from P2WPKH and strengthens security.

#### P2SH-P2WSH (Maximum Compatibility)

Complex SegWit scripts can also be P2SH‑wrapped:  
- scriptSig: redeemScript (OP_0 + 32‑byte hash)  
- witness: signatures + witnessScript  

Validation passes through three generations of rules exactly as with P2SH‑P2WPKH. This wrapper was essential for early Lightning deployments needing multisig without malleability. While native P2WSH is preferred today, the wrapped form ensures compatibility across older wallet systems.

### SegWit’s Impact

SegWit provided:  
- stable transaction IDs  
- lower fees via discounted witness data  
- higher block throughput via block weight  
- compatibility for old nodes  
- a clean upgrade path for Taproot and future extensions  

Together with trustless network interaction, these tools form the backbone of modern Bitcoin development.


# Final Section

<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>

## Reviews & Ratings

<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>
<isCourseReview>true</isCourseReview>

## Final Exam

<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>


<isCourseExam>true</isCourseExam>

## Conclusion


<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>

<isCourseConclusion>true</isCourseConclusion>
