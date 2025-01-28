---
term: BIP383

---
Introduces the functions `multi(NUM, KEY, ..., KEY)` and `sortedmulti(NUM, KEY, ..., KEY)` for descriptors. These functions allow for the description of multisignature scripts in the descriptors, with `sortedmulti` sorting the public keys in lexicographical order to ensure compatibility during import. BIP383 was implemented along with all other descriptor-related BIPs (except BIP386) in version 0.17 of Bitcoin Core.