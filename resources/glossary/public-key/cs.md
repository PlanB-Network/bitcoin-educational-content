---
term: VEŘEJNÝ KLÍČ

---
Veřejný klíč je prvek používaný v asymetrické kryptografii. Generuje se ze soukromého klíče pomocí nevratné matematické funkce. V Bitcoinu se veřejné klíče odvozují z přidruženého soukromého klíče pomocí algoritmů digitálního podpisu eliptické křivky ECDSA nebo Schnorr. Na rozdíl od soukromého klíče lze veřejný klíč volně sdílet, aniž by byla ohrožena bezpečnost prostředků. V rámci protokolu Bitcoin slouží veřejný klíč jako základ pro vytvoření bitcoinové adresy, která se pak používá k vytvoření podmínek pro výdaje na UTXO pomocí `scriptPubKey`. Veřejné klíče se často zaměňují s hlavním klíčem nebo s rozšířenými klíči (xpub...). Tyto prvky jsou však zcela odlišné.

> ► V angličtině se veřejný klíč nazývá "public key" Tento termín se někdy zkracuje na "pubkey" nebo "PK".*