---
term: BIP118

---
Proposal for improving Bitcoin aimed at introducing two new SigHash Flag modifiers: `SIGHASH_ANYPREVOUT` and `SIGHASH_ANYPREVOUTANYSCRIPT`. These features extend the capabilities of Bitcoin transactions, particularly in terms of smart contracts and overlay solutions like the Lightning Network. BIP118 would notably enable the use of Eltoo. The main advantage of `SIGHASH_ANYPREVOUT` is to allow the reuse of signatures across multiple transactions, which offers more flexibility. Specifically, these SigHashes allow for a signature that covers none of the transaction's inputs.