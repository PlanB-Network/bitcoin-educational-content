---
term: OBJECTIVE
---

In deterministic and hierarchical (HD) portfolios, the purpose, defined by BIP43, represents a specific derivation level. This index, located at the first depth of the derivation tree (`m / purpose' /`), identifies the derivation standard adopted by the portfolio, to facilitate compatibility between different portfolio management software. For example, in the case of SegWit addresses (BIP84), the purpose is noted as `/84'/`. This method enables keys to be organized efficiently between different address types within a single HD portfolio. The standard indexes used are :


- For P2PKH: `44'` ;
- For P2WPKH-nested-in-P2SH: `49'` ;
- For P2WPKH: `84'` ;
- For P2TR: `86'`.