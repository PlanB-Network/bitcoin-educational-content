---
term: BIP0383
definition: multi() and sortedmulti() functions for describing multisig scripts in descriptors.
---

Introduces the functions `multi(NUM, KEY, ..., KEY)` and `sortedmulti(NUM, KEY, ..., KEY)` for descriptors. These functions describe multisignature scripts, with `sortedmulti` ensuring compatibility by sorting public keys in lexicographical order during import. 
BIP383 was implemented along with all other descriptor-related BIPs (except BIP386) in version 0.17 of Bitcoin Core.

