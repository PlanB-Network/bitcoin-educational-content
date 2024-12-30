---
term: DEPTH
---

In the context of HD (Hierarchical Deterministic) wallets, depth refers to the specific level of a key (public or private), a chain code, an extended key, or an address within the wallet's derivation structure from the master key. Each level of this structure can be seen as a floor in a key tree, where the master key is at the root (depth 0) and the subsequent levels define various attributes such as:
the purpose (depth 1), the type of currency (depth 2), the account (depth 3), the chain type (depth 4), and the index of the specific address (depth 5).

![](../../dictionnaire/assets/18.webp)

To move from one depth to the next, a derivation process is used from a pair of parent keys to a pair of child keys.

> ► *The term "derivation floor" is sometimes also used instead of depth.*