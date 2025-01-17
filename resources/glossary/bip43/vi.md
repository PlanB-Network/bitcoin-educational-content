---
term: BIP43

---
Proposal for improvement that introduces the use of a derivation path level to describe the purpose field in the structure of HD wallets, previously introduced in BIP32. According to BIP43, the first level of derivation of an HD wallet, just after the master key denoted as `m/`, is reserved for the purpose number which indicates the derivation standard used for the rest of the path. This number is recorded as a hardened index. For example, if the wallet follows the SegWit standard (BIP84), the beginning of its derivation path would be: `m/84'/`. BIP43 thus allows for the clarification of the standards adhered to by each wallet software to have better interoperability among them. The standardization of the rest of the derivation path is described in BIP44.