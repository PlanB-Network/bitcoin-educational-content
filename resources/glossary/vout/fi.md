---
term: VOUT
---

Erityinen elementti Bitcoin-siirrossa, joka määrittää lähetettyjen varojen kohteen. Siirto voi sisältää useita lähtöjä, joista jokainen on yksilöllisesti tunnistettavissa yhdistelmällä siirron tunniste (`txid`) ja indeksi nimeltä `vout`. Tämä indeksi, alkaen `0`, merkitsee lähdön sijainnin siirron lähtöjen sekvenssissä. Näin ollen ensimmäinen lähtö merkitään `"vout": 0`, toinen `"vout": 1`, ja niin edelleen.

Jokainen `vout` kapseloi pääasiassa kaksi tietokokonaisuutta:
* arvon, ilmaistuna bitcoineina, joka edustaa lähetettyä määrää;
* lukitus-skriptin (`scriptPubKey`), joka määrittelee ehdot, jotka on täytettävä, jotta varoja voidaan käyttää uudelleen tulevassa siirrossa.

`txid` ja tietyn `vout` yhdistelmä muodostaa niin kutsutun UTXO:n, esimerkiksi:

```text
txid: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf
vout: 0
outpoint: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf:0
```