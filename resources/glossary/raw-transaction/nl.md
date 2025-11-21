---
term: RUWE TRANSACTIE
---

Een Bitcoin transactie die is opgebouwd en ondertekend, in binaire vorm. Een ruwe transactie (*raw TX*) is de laatste representatie van een transactie, net voordat deze wordt uitgezonden op het netwerk. Deze transactie bevat alle benodigde informatie voor opname in een blok:


- De versie;
- De vlag;
- De ingangen;
- De uitgangen;
- De sluittijd;
- De getuige.


Wat een "*rauwe transactie*" genoemd wordt, vertegenwoordigt de ruwe gegevens die tweemaal door de SHA256 Hash functie gehaald worden om generate de transactie txid te maken. Deze gegevens worden vervolgens gebruikt in Merkle Tree van het blok om de transactie te integreren in Blockchain.


> dit concept wordt soms ook "geserialiseerde transactie" genoemd. In het Frans kunnen deze termen respectievelijk vertaald worden als "transaction brute" en "transaction sérialisée".