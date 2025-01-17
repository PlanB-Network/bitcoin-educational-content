---
term: HASH160

---
Bitcoinissa käytetty salausfunktio, jota käytetään erityisesti Legacy- ja SegWit v0 -vastaanottoosoitteiden luomiseen. Siinä yhdistetään kaksi hash-funktiota, jotka suoritetaan peräkkäin syötteeseen: ensin SHA256 ja sitten RIPEMD160. Tämän funktion tuloste on siis 160 bittiä.

$$\text{HASH160}(x) = \text{RIPEMD160}(\text{SHA256}(x))$$$