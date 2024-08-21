---
term: P2SH-P2WPKH
---

P2SH-P2WPKH znamená *Pay to Script Hash - Pay to Witness Public Key Hash*. Jedná se o standardní skriptový model používaný k určení podmínek pro výdaje UTXO, známého také jako "Nested SegWit".

P2SH-P2WPKH byl představen s implementací SegWit v srpnu 2017. Tento skript je P2WPKH zabalený do P2SH. Blokuje bitcoiny na základě hashe veřejného klíče. Rozdíl oproti klasickému P2WPKH je, že skript je zabalen v `redeemScript` klasického P2SH.

Tento skript byl vytvořen při spuštění SegWit, aby usnadnil jeho přijetí. Umožňuje použití tohoto nového standardu, i když služby nebo peněženky ještě nejsou s SegWit nativně kompatibilní. Jedná se o druh přechodového skriptu k novému standardu. Dnes tedy již není velmi relevantní používat tyto typy zabalených SegWit skriptů, protože většina peněženek implementovala nativní SegWit. Adresy P2SH-P2WPKH jsou zapsány pomocí kódování `Base58Check` a vždy začínají `3`, jako jakákoli adresa P2SH.

> ► *`P2SH-P2WPKH` je také někdy nazýván `P2WPKH-nested-in-P2SH`.*