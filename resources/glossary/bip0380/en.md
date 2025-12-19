---
term: BIP0380
---

BIP380 introduces a standard language for describing collections of output scripts used in HD Bitcoin wallets, known as “Output Script Descriptors.” 
The goal is to standardize how output scripts are represented and managed, making wallet backup, export, and import easier.
In addition to private data like the recovery phrase, the descriptors provide all the necessary information to retrieve the key pairs used in an HD wallet. While BIP380 describes the general framework for descriptors, BIP381–BIP386 specify the individual descriptor expression types. BIP380 was implemented along with all other descriptor-related BIPs (except BIP386) in version 0.17 of Bitcoin Core.

