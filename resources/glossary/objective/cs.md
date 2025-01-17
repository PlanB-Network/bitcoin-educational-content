---
term: OBJECTIVE

---
V deterministických a hierarchických (HD) peněženkách představuje cíl (nebo _účel_ v angličtině), definovaný v BIP43, určitou úroveň odvození. Tento index, umístěný v první hloubce stromu derivace (`m / účel' /`), identifikuje standard derivace přijatý peněženkou, aby se usnadnila kompatibilita mezi různými softwary pro správu peněženek. Například v případě adres SegWit (BIP84) je cíl zaznamenán jako `/84'/`. Tato metoda umožňuje efektivní organizaci klíčů mezi různými typy adres v rámci jedné peněženky HD. Standardně se používají následující indexy:


- Pro P2PKH: `44'`;
- Pro P2WPKH-nested-in-P2SH: `49'`;
- Pro P2WPKH: `84'`;
- Pro P2TR: `86'`.

![](../../dictionnaire/assets/20.webp)