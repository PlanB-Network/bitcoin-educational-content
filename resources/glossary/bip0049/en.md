---
term: BIP0049
---

BIP49 is an informative BIP that introduces the derivation method used to generate Nested SegWit addresses in an HD wallet. The proposed derivation path follows the standards of BIP43 and BIP44, with the index `49'` (hardened derivation) at the purpose level. For example, the first address of a P2SH-P2WPKH account would be derived from the path: `m/49'/0'/0'/0/0`. Nested SegWit scripts were introduced at the launch of SegWit to ease its adoption, enabling users to benefit from SegWit features even in wallets that were not yet fully SegWit-native.

