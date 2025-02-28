---
term: BIP32

---
BIP32 introduced the concept of a hierarchical deterministic wallet (HD wallet). This proposal allows for the generation of a hierarchy of key pairs from a common `master seed`, using one-way derivation functions. Each generated key pair can itself be the parent of other child keys, thus forming a tree-like (hierarchical) structure. The advantage of BIP32 is that it enables the management of multiple different key pairs with the need to only keep a single seed to regenerate them. This innovation has notably helped combat the issue of address reuse, which is serious for user privacy. BIP32 also allows for the creation of sub-branches within the same wallet to facilitate its management.