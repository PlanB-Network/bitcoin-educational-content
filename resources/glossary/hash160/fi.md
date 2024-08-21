---
term: HASH160
---

Kryptografinen funktio, jota käytetään Bitcoinissa, erityisesti Legacy- ja SegWit v0 -vastaanotto-osoitteiden luomiseen. Se yhdistää kaksi hash-funktiota, jotka suoritetaan peräkkäin syötteeseen: ensin SHA256, sitten RIPEMD160. Tämän funktion tuloksena on siis 160 bittiä.

$$\text{HASH160}(x) = \text{RIPEMD160}(\text{SHA256}(x))$$