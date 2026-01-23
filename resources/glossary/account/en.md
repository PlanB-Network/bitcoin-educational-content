---
term: Account
definition: In an HD wallet, a derivation level (depth 3) allowing hierarchical organization of keys and addresses.
---

In HD (Hierarchical Deterministic) wallets, an account represents a derivation layer at depth 3 according to BIP32. Each account is sequentially numbered starting from `/0'/` (hardened derivation, so `/2^31/` or `/2 147 483 648/`). It is at this derivation depth that the well-known `xpubs` are located. Nowadays, typically only one account is used per HD wallet. However, they were originally designed to segregate various categories of use within the same wallet. For example, considering a standard derivation path for an external Taproot (P2TR) receiving address: `m/86'/0'/0'/0/0`, the account index is the second `/0'/`.



