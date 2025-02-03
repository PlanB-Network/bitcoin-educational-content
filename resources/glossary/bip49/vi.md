---
term: BIP49

---
BIP49 is an informative BIP that introduces the derivation method used to generate Nested SegWit addresses in an HD wallet. The proposed derivation path follows the standards of BIP43 and BIP44, with the index `49'` (hardened derivation) at the depth of the goal. For example, the first address of a P2SH-P2WPKH account would be derived from the path: `m/49'/0'/0'/0/0`. Nested SegWit scripts were invented at the launch of SegWit to facilitate its adoption. They allow the use of this new standard, even on wallets not yet natively compatible with SegWit.