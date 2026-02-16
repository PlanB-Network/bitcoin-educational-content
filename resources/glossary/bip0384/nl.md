---
term: BIP0384
definition: combo() functie voor het beschrijven van meerdere soorten scripts voor dezelfde publieke sleutel in descriptors.
---

Introduceert de `combo(KEY)` functie voor descriptors. Deze functie beschrijft een verzameling mogelijke uitvoerscripts voor een gegeven openbare sleutel. Het omvat dus meerdere typen scripts tegelijk, waaronder P2PK, P2PKH, P2WPKH en P2SH-P2WPKH. Als de gegeven sleutel gecomprimeerd is, worden alle 4 scripttypen getest en als dat niet het geval is, worden alleen de 2 legacy scripttypen getest. Het doel is om de weergave van sleutels in descriptoren te vereenvoudigen door een enkele methode te bieden om generate verschillende varianten van uitvoerscripts gebaseerd op dezelfde openbare sleutel. BIP384 is geïmplementeerd samen met alle andere Descriptor gerelateerde BIP's (behalve BIP386) in versie 0.17 van Bitcoin core.