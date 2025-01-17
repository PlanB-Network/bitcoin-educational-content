---
term: SIGHASH_NONE (0X02)

---
SigHash-tyyppi Merkki, jota käytetään Bitcoin-tapahtuman allekirjoituksissa osoittamaan, että allekirjoitus koskee kaikkia tapahtuman syötteitä, mutta ei mitään sen tuotoksia. `SIGHASH_NONE` tarkoittaa, että allekirjoittaja sitoutuu vain syötteisiin, jolloin lähdöt jäävät määrittelemättä tai muokattaviksi allekirjoittamisen jälkeen. Tämäntyyppinen allekirjoitus on hyödyllinen tapauksissa, joissa allekirjoittaja haluaa valtuuttaa muut osapuolet päättämään, miten bitcoinit jaetaan transaktiossa.