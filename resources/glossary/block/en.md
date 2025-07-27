---
term: BLOCK
---

Data structure in the Bitcoin system. A block contains a set of valid transactions along with metadata stored in its header. Each block is linked to the previous one by including the hash of its predecessor’s header, forming the blockchain. 
The blockchain acts as a timestamping server, allowing every user to verify all past transactions, ensure no transaction is duplicated, and prevent double spending. 
Transactions within a block are organized in a Merkle tree, a cryptographic accumulator that produces a single hash summarizing all transactions, known as the Merkle root. 

A block header contains six fields:
* The block version;
* The hash of the previous block;
* The Merkle root of the transactions;
* The block timestamp;
* The difficulty target;
* The nonce.

For a block to be considered valid, its header, when hashed with `SHA256d` (a double SHA‑256 hash), must produce a value less than or equal to the difficulty target.