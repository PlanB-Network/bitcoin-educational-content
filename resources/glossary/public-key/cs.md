---
term: VEŘEJNÝ KLÍČ
---

Veřejný klíč je prvek používaný v asymetrické kryptografii. Je generován z privátního klíče pomocí nevratné matematické funkce. Na Bitcoinu jsou veřejné klíče odvozeny od jejich přidruženého privátního klíče prostřednictvím algoritmů digitálního podpisu eliptické křivky ECDSA nebo Schnorr. Na rozdíl od privátního klíče, veřejný klíč lze volně sdílet bez ohrožení bezpečnosti prostředků. V rámci protokolu Bitcoin slouží veřejný klíč jako základ pro vytvoření Bitcoinové adresy, která je pak použita k vytvoření podmínek pro výdaje na UTXO pomocí `scriptPubKey`. Veřejné klíče jsou často zaměňovány s hlavním klíčem nebo s rozšířenými klíči (xpub...). Tyto prvky jsou však značně odlišné.

> ► *V angličtině se veřejný klíč nazývá "public key." Tento termín je někdy zkracován jako "pubkey," nebo "PK."*