---
term: BIP0143
---

Introduces a new way of hashing the transaction for signature verification in post-SegWit scripts. The goal is to minimize redundant operations during verification and to include the input UTXO values in the signature. This solves two major issues with the original transaction hashing algorithm:
**The quadratic growth in hashing complexity with an increasing number of signatures**
**The absence of input values in the signature, which created risks for hardware wallets, particularly in verifying the transaction fees being spent.**
Since the SegWit upgrade (explained in BIP141) introduced a new type of transaction script that older nodes would not verify, BIP143 leveraged this opportunity to resolve these issues without requiring a hard fork.

BIP143 was therefore included as part of the SegWit soft fork.