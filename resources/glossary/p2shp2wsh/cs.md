---
term: P2SH-P2WSH

---
P2SH-P2WSH znamená *Pay to Script Hash - Pay to Witness Script Hash*. Jedná se o standardní model skriptu, který se používá pro stanovení podmínek utrácení na UTXO, známý také jako "Nested SegWit".

P2SH-P2WSH byla zavedena spolu s implementací SegWit v srpnu 2017. Tento skript popisuje P2WSH zabalený do P2SH. Uzamyká bitcoiny na základě hashe skriptu. Rozdíl oproti klasickému P2WSH spočívá v tom, že skript je zabalen do `redeemScript` klasického P2SH.

Tento skript byl vytvořen při spuštění systému SegWit, aby usnadnil jeho přijetí. Umožňuje používat tento nový standard i se službami nebo peněženkami, které ještě nejsou nativně kompatibilní se SegWit. Dnes již tedy není příliš relevantní používat tyto typy zabalených skriptů SegWit, protože většina peněženek má implementován nativní SegWit. Adresy P2SH-P2WSH jsou zapsány pomocí kódování `Base58Check` a vždy začínají na `3`, stejně jako jakákoli jiná adresa P2SH.