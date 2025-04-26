---
term: STAMPS

---
Protokol, který umožňuje integraci formátovaných obrazových dat přímo do blockchainu Bitcoinu prostřednictvím surových transakcí s více podpisy (P2MS). Razítka zakódují binární obsah obrázku v bázi 64 a přidají jej ke klíčům 1/3 P2MS. Jeden klíč je skutečný a slouží k utrácení prostředků, zatímco další dva jsou fiktivní klíče (přidružený soukromý klíč není znám), které ukládají data. Díky tomu, že data jsou kódována přímo jako veřejné klíče, a ne pomocí výstupů `OP_RETURN`, jsou obrazy uložené pomocí protokolu Stamps pro uzly obzvláště náročné na pracovní zátěž. Tato metoda zejména vytváří více UTXO, což zvyšuje velikost sady UTXO a představuje problém pro plné uzly.