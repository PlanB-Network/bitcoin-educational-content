---
term: CÍL
---

V deterministických a hierarchických (HD) portfoliích představuje účel definovaný v BIP43 konkrétní úroveň odvození. Tento index, umístěný v první hloubce stromu odvození (`m / účel' /`), identifikuje standard odvození přijatý portfoliem, aby se usnadnila kompatibilita mezi různými softwary pro správu portfolia. Například v případě adres SegWit (BIP84) je účel zaznamenán jako `/84'/`. Tato metoda umožňuje efektivní uspořádání klíčů mezi různými typy Address v rámci jednoho portfolia HD. Standardně používané indexy jsou :




- Pro P2PKH: `44'` ;
- Pro P2WPKH- vnořený do P2SH: `49'` ;
- Pro P2WPKH: `84'` ;
- Pro P2TR: `86'`.