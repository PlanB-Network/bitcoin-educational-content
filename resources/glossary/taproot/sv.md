---
term: Taproot
definition: Stor Bitcoin-uppdatering aktiverad i november 2021 som ger integritet, effektivitet och flexibilitet via BIP340, 341 och 342.
---

En större uppdatering av Bitcoin-protokollet, som antogs genom ett Soft Fork i november 2021. Denna uppdatering ger betydande förbättringar när det gäller integritet, effektivitet och flexibilitet genom att implementera BIP340, BIP341 och BIP342. Uppdateringen låstes in i block 687 284 den 12 juni 2021, när 90 % av de block som genererats under en period signalerade för, vilket indikerade att utvinnarna var redo att aktivera uppdateringen (*Speedy Trial*). Aktiveringen skedde till slut i block 709 632 den 14 november 2021, nästan fyra år efter de inledande diskussionerna i frågan mellan Pieter Wuille, Andrew Poelstra och Gregory Maxwell. Det var det första större uppdateringsförsöket sedan den omtvistade aktiveringen av SegWit 2017.


Taproot är också namnet på BIP341, implementerat i Soft Fork med samma namn, som introducerar en ny skriptmodell med namnet P2TR. Ett P2TR-skript låser bitcoins på en unik Schnorr-offentlig nyckel, betecknad som $K$. Denna nyckel $K$ är dock faktiskt ett aggregat av en offentlig nyckel $P$ och en offentlig nyckel $M$, den senare beräknas från Merkle Root i en lista med `scriptPubKey`. De bitcoins som är låsta med ett P2TR-skript kan användas på två olika sätt: antingen genom att publicera en signatur för den offentliga nyckeln $P$ eller genom att uppfylla ett av de skript som finns i Merkle Tree. Det första alternativet kallas en "*nyckelsökväg*" och det andra en "*skriptväg*".