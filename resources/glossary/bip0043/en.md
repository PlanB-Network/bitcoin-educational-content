---
term: BIP0043
---

A proposal introducing a dedicated derivation path level to define the purpose field in HD wallet structures, as originally introduced in BIP32. According to BIP43, the first level of derivation of an HD wallet, just after the master key denoted as `m/`, is reserved for the purpose number which indicates the derivation standard used for the rest of the path. This number is recorded as a hardened index. For example, if the wallet follows the SegWit standard (BIP84), the beginning of its derivation path would be: `m/84'/`. 
BIP43 clarifies which standards are followed by each wallet, improving interoperability between different implementations. The standardization of subsequent derivation path levels is described in BIP44.