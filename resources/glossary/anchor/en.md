---
term: Anchor
---

In the RGB protocol, a Anchor represents a set of client-side data used to prove the inclusion of a single commitment in a transaction. In the RGB protocol, a Anchor is made up of the following elements:


- Transaction ID Bitcoin (txid) from Witness Transaction ;
- Multi Protocol Commitment (MPC);
- Deterministic Bitcoin Commitment (DBC);
- Extra Transaction Proof (ETP) if the Tapret commitment mechanism is used.

A Anchor therefore serves to establish a verifiable link between a specific Bitcoin transaction and private data validated by the RGB protocol. It guarantees that these data are indeed included in Blockchain, without their exact content being made public.