---
term: BIP0118
---

Proposal introducing two new SigHash Flag modifiers: `SIGHASH_ANYPREVOUT` and `SIGHASH_ANYPREVOUTANYSCRIPT`. 
These additions extend the flexibility of Bitcoin transactions, particularly for smart contracts and second-layer solutions such as the Lightning Network.
One notable application of BIP118 is enabling the Eltoo update mechanism.
The main advantage of `SIGHASH_ANYPREVOUT` is that it allows signatures to be reused across multiple transactions, offering greater flexibility. Specifically, these SigHash flags make it possible to produce a signature that does not commit to any of the transaction's inputs.

