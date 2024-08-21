---
termi: BIP12
---

Ehdotus Gavin Andresenilta Bitcoin-siirtoskriptien joustavuuden ja yksityisyyden parantamiseksi. Tämä BIP ehdottaa uuden skriptioperaation, nimeltään `OP_EVAL`, toteuttamista, joka mahdollistaa skriptin arvioinnin `scriptSig`-datan sisällä siirtotapahtuman vahvistusprosessin aikana. BIP12:n päämuutos on mahdollistaa yhden skriptin sisällyttäminen toiseen skriptiin. Tämä tekniikka mahdollistaa monimutkaisempien ehtojen luomisen, jotka voidaan tarkistaa käytettäessä, ilman että niitä tarvitsee paljastaa bitcoineja lähettäville käyttäjille käytettyyn osoitteeseen. BIP12 korvattiin myöhemmin turvallisemmilla ehdotuksilla, erityisesti BIP16 (P2SH) kanssa, joka tarjoaa erilaisen menetelmän samojen tavoitteiden saavuttamiseksi kuin `OP_EVAL`.