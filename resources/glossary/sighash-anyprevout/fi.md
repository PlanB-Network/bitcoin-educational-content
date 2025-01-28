---
term: SIGHASH_ANYPREVOUT

---
Ehdotus uuden SigHash Flag -muuntimen toteuttamiseksi Bitcoinissa, joka on otettu käyttöön BIP118:n myötä. `SIGHASH_ANYPREVOUT` mahdollistaa suuremman joustavuuden transaktioiden hallinnassa, erityisesti kehittyneissä sovelluksissa, kuten Lightning-verkon maksukanavissa ja Eltoo-päivityksessä. `SIGHASH_ANYPREVOUT` mahdollistaa sen, että allekirjoitus ei ole sidottu mihinkään tiettyyn aiempaan UTXO:hon (*Any Previous Output*). Yhdessä `SIGHASH_ALL`:n kanssa käytettynä se mahdollistaa kaikkien tapahtuman ulostulojen allekirjoittamisen, mutta ei minkään sisääntulon. Tämä mahdollistaisi allekirjoituksen uudelleenkäytön eri tapahtumissa, kunhan tietyt ehdot täyttyvät.

> ► *Tämä SigHash-muunnin SIGHASH_ANYPREVOUT on johdettu ideasta SIGHASH_NOINPUT, jonka Joseph Poon ehdotti alun perin vuonna 2016 parantaakseen Lightning Network -konseptiaan. *