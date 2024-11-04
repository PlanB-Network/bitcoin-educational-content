---
term: MASTER KEY
---

In the context of HD (Hierarchical Deterministic) wallets, the master private key is a unique private key derived from the wallet's seed. To obtain the master key, the `HMAC-SHA512` function is applied to the seed, using the words "*Bitcoin seed*" literally as the key. The result of this operation produces a 512-bit output, with the first 256 bits constituting the master key, and the remaining 256 bits forming the master chain code. The master key and the master chain code serve as the starting point for deriving all child private and public keys in the HD wallet's tree structure. Therefore, the master private key is at depth 0 of derivation.

![](../../dictionnaire/assets/19.webp)