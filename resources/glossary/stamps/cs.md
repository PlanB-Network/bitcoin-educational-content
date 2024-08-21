---
term: STAMPS
---

Protokol, který umožňuje integraci formátovaných obrazových dat přímo na Bitcoin blockchain prostřednictvím raw multisignature transakcí (P2MS). Stamps kóduje binární obsah obrázku v base 64 a přidává jej do klíčů 1/3 P2MS. Jeden klíč je skutečný a používá se k utracení prostředků, zatímco další dva jsou fiktivní klíče (přidružený soukromý klíč je neznámý), které ukládají data. Kódováním dat přímo jako veřejné klíče, namísto použití výstupů `OP_RETURN`, jsou obrázky uložené protokolem Stamps zvláště pracně zpracovatelné pro uzly. Tato metoda významně vytváří více UTXO, což zvyšuje velikost sady UTXO a představuje problémy pro plné uzly.