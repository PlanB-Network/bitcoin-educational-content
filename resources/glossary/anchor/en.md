---
term: Anchor
definition: In the RGB protocol, a set of data proving the inclusion of a commitment in a Bitcoin transaction, without publicly revealing its content.
---

In the RGB protocol, an Anchor represents a set of client-side data used to prove the inclusion of a single commitment in a transaction. In the RGB protocol, an Anchor is made up of the following elements:


- The Bitcoin Transaction ID (txid) from the Witness Transaction;
- The Multi Protocol Commitment (MPC);
- The Deterministic Bitcoin Commitment (DBC);
- The Extra Transaction Proof (ETP) if the Tapret commitment mechanism is used.

An Anchor therefore serves to establish a verifiable link between a specific Bitcoin transaction and private data validated by the RGB protocol. It guarantees that this data is indeed included in the Blockchain, without its exact content being publicly revealed.
