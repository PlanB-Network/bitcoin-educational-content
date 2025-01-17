---
term: OBJECTIVE
---

In deterministic and hierarchical (HD) wallets, the objective (or _purpose_ in English), defined by BIP43, represents a specific level of derivation. This index, located at the first depth of the derivation tree (`m / purpose' /`), identifies the derivation standard adopted by the wallet, in order to facilitate compatibility between different wallet management software. For example, in the case of SegWit addresses (BIP84), the objective is noted as `/84'/`. This method allows for the efficient organization of keys among different types of addresses within the same HD wallet. The standard indexes used are:
* For P2PKH: `44'`;
* For P2WPKH-nested-in-P2SH: `49'`;
* For P2WPKH: `84'`;
* For P2TR: `86'`.

![](../../dictionnaire/assets/20.webp)

