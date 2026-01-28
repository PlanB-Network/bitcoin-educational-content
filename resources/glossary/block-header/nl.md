---
term: Block header
definition: Structuur van 80 bytes die de metadata van een blok bevat (versie, vorige hash, Merkle root, tijdstempel, target, nonce).
---

De blokkop is een datastructuur die dient als belangrijkste component in de opbouw van een Bitcoin blok. Elk blok bestaat uit een header en een lijst van transacties. De block header bevat cruciale informatie die de integriteit en geldigheid van een blok binnen de Blockchain garandeert. De koptekst van het blok bevat 80 bytes aan metadata en is samengesteld uit de volgende Elements:


- De blokversie;
- De Hash van het vorige blok;
- De Merkle Tree wortel van de transacties;
- Het blok Timestamp;
- De moeilijkheidsgraad;
- De Nonce.


Hier is bijvoorbeeld de koptekst van blok nummer 785.530 in hexadecimaal formaat, gedolven door Foundry USA op 15 april 2023:


```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```


Als we deze kop uitsplitsen, kunnen we dit herkennen:


- De versie:


```text
00e0ff3f
```



- De vorige Hash:


```text
5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
```



- De Merkle Root:


```text
206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
```



- De Timestamp:


```text
bcb13a64
```



- Het doel:


```text
b2e00517
```



- De Nonce:


```text
43f09a40
```


Om geldig te zijn moet een blok een header hebben die, na gehasht te zijn met `SHA256d`, een Hash oplevert die kleiner of gelijk is aan de moeilijkheidsdoelstelling.


