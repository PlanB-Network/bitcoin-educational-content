---
term: BIP0113
---

Verandering in de berekening van alle timelock operaties (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence` en `OP_CHECKSEQUENCEVERIFY`). Het specificeert dat om de geldigheid van timelocks te evalueren, ze nu vergeleken moeten worden met de MTP (*Median Time Past*), wat de mediaan is van de timestamps van de laatste 11 blokken. Voorheen werd alleen de Timestamp van het vorige blok gebruikt. Deze methode maakt het systeem voorspelbaarder en voorkomt manipulatie van de tijdreferentie door miners. BIP113 werd geïntroduceerd via een Soft Fork op 4 juli 2016, naast BIP68 en BIP112, die voor het eerst werden geactiveerd met de BIP9-methode.