---
term: P2SH-P2WPKH

---
P2SH-P2WPKH znamená *Pay to Script Hash - Pay to Witness Public Key Hash*. Jedná se o standardní model skriptu, který se používá pro stanovení podmínek utrácení na UTXO, známý také jako "Nested SegWit".

P2SH-P2WPKH byla zavedena se zavedením SegWit v srpnu 2017. Tento skript je P2WPKH zabalený do P2SH. Uzamyká bitcoiny na základě hashe veřejného klíče. Od klasického P2WPKH se liší tím, že skript je zabalen do `redeemScript` klasického P2SH.

Tento skript byl vytvořen při spuštění systému SegWit, aby usnadnil jeho přijetí. Umožňuje používat tento nový standard i se službami nebo peněženkami, které ještě nejsou nativně kompatibilní se SegWit. Je to jakýsi přechodový skript k novému standardu. Dnes již tedy není příliš relevantní používat tyto typy zabalených skriptů SegWit, protože většina peněženek má implementován nativní SegWit. Adresy P2SH-P2WPKH jsou zapsány pomocí kódování `Base58Check` a vždy začínají na `3`, stejně jako každá adresa P2SH.

> ► *`P2SH-P2WPKH` se také někdy nazývá `P2WPKH-nested-in-P2SH`.*