---
term: VOUT

---
Bitcoin-tapahtuman erityinen elementti, joka määrittää lähetettyjen varojen määränpään. Transaktio voi sisältää useita lähtöjä, joista kukin yksilöidään transaktion tunnisteen (`txid`) ja `vout`-nimisen indeksin yhdistelmällä. Tämä indeksi, joka alkaa numerosta `0`, merkitsee lähdön sijaintia transaktion lähdöissä. Näin ollen ensimmäinen ulostulo on `"vout": 0`, toinen `"vout": 1` ja niin edelleen.

Jokainen `vout` sisältää pääasiassa kaksi tietoa:


- lähetettyä summaa vastaava arvo bitcoineina ilmaistuna;
- lukitusskripti (`scriptPubKey`), jossa määritellään ehdot, joiden täyttyessä varat voidaan käyttää uudelleen tulevassa tapahtumassa.

Tietyn kappaleen `txid` ja `vout` yhdistelmä muodostaa esimerkiksi niin sanotun UTXO:n:

```text
txid: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf
vout: 0
outpoint: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf:0
```