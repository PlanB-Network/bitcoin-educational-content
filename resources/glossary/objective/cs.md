---
term: CÍL
---

V deterministických a hierarchických (HD) peněženkách cíl (nebo _účel_ v angličtině), definovaný BIP43, představuje specifickou úroveň derivace. Tento index, umístěný na první hloubce derivačního stromu (`m / purpose' /`), identifikuje derivační standard přijatý peněženkou, aby se usnadnila kompatibilita mezi různými softwary pro správu peněženek. Například v případě adres SegWit (BIP84) je cíl označen jako `/84'/`. Tato metoda umožňuje efektivní organizaci klíčů mezi různými typy adres v rámci téže HD peněženky. Standardní používané indexy jsou:
* Pro P2PKH: `44'`;
* Pro P2WPKH-vnořené-v-P2SH: `49'`;
* Pro P2WPKH: `84'`;
* Pro P2TR: `86'`.

![](../../dictionnaire/assets/20.png)