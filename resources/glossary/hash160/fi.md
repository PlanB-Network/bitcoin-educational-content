---
term: HASH160

definition: Funktio, jossa yhdistetään SHA256 ja RIPEMD160 ja jota käytetään Bitcoin-osoitteiden luomiseen.
---
Bitcoinissa käytetty salausfunktio, jota käytetään erityisesti Legacy- ja SegWit v0 -vastaanottoosoitteiden luomiseen. Siinä yhdistetään kaksi hash-funktiota, jotka suoritetaan peräkkäin syötteeseen: ensin SHA256 ja sitten RIPEMD160. Tämän funktion tuloste on siis 160 bittiä.

$$\text{HASH160}(x) = \text{RIPEMD160}(\text{SHA256}(x))$$$