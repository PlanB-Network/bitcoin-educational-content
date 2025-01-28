---
term: BIP143

---
Introduces a new way of hashing the transaction for signature verification in post-SegWit scripts. The goal is to minimize redundant operations during verification and to include the value of the UTXOs in the input in the signature. This solves two major issues with the original transaction hashing algorithm:


- The quadratic growth of data hashing with the number of signatures;
- The absence of including the input value in the signature, which posed a risk to hardware wallets, especially regarding the knowledge of transaction fees incurred.

Since the SegWit update, explained in BIP141, introduces a new form of transactions whose script will not be verified by old nodes, BIP143 takes this opportunity to address this issue without requiring a hard fork. Therefore, BIP143 is part of the SegWit soft fork.