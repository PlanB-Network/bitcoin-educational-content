---
term: BIP0032
definition: Introduction of HD (hierarchical deterministic) wallets allowing all keys of a wallet to be generated from a single seed.
---

BIP32 introduced the concept of a hierarchical deterministic wallet (HD wallet). This proposal allows for the generation of a hierarchy of key pairs from a common `master seed`, using one-way derivation functions. Each generated key pair can itself be the parent of other child keys, forming a tree-like (hierarchical) structure. 
The key advantage of BIP32 is that it allows users to manage multiple key pairs while only needing to store a single seed to regenerate them. This innovation significantly improved wallet usability and security, and it also helped reduce address reuse, which poses serious privacy risks for users. Additionally, BIP32 enables the creation of multiple sub‑branches within the same wallet, improving organizational flexibility and wallet management.