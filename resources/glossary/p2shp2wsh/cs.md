---
term: P2SH-P2WSH
---

P2SH-P2WSH znamená *Pay to Script Hash - Pay to Witness Script Hash*. Jedná se o standardní skriptový model používaný k určení podmínek pro výdaje UTXO, známého také jako "Nested SegWit".

P2SH-P2WSH byl představen s implementací SegWit v srpnu 2017. Tento skript popisuje P2WSH zabalený v P2SH. Blokuje bitcoiny na základě hashe skriptu. Rozdíl oproti klasickému P2WSH je, že skript je zabalen v `redeemScript` klasického P2SH.

Tento skript byl vytvořen při spuštění SegWit, aby usnadnil jeho adopci. Umožňuje použití tohoto nového standardu, i když služby nebo peněženky ještě nejsou nativně kompatibilní se SegWit. Dnes tedy již není velmi relevantní používat tyto typy zabalených SegWit skriptů, protože většina peněženek implementovala nativní SegWit. Adresy P2SH-P2WSH jsou zapsány pomocí kódování `Base58Check` a vždy začínají `3`, jako jakákoli adresa P2SH.