---
termi: SIGHASH_NONE (0X02)
---

SigHash-lipun tyyppi, jota käytetään Bitcoin-siirtojen allekirjoituksissa osoittamaan, että allekirjoitus koskee kaikkia siirron syötteitä, mutta ei yhtäkään sen tulosteista. `SIGHASH_NONE` käytön myötä allekirjoittaja sitoutuu vain syötteisiin, sallien tulosteiden pysyä määrittelemättöminä tai muokattavina allekirjoittamisen jälkeen. Tämän tyyppinen allekirjoitus on hyödyllinen tapauksissa, joissa allekirjoittaja haluaa valtuuttaa muut osapuolet päättämään, miten bitcoinit jaetaan siirrossa.