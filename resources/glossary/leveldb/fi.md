---
termi: LEVELDB
---

Kevyt, nopea ja avoimen lähdekoodin avain-arvo tallennuskirjasto, jonka on suunnitellut Google. Sitä käytetään Bitcoinissa UTXO-joukon, tapahtumaindeksin ja lohkoindeksin tallentamiseen. Tämä tietokantajärjestelmä otettiin käyttöön vuonna 2012 osana "Ultraprune" Pull Requestia, jonka tavoitteena oli korvata BerkeleyDB. Tällä muutoksella oli merkittäviä seurauksia, mukaan lukien ensimmäisen lohkoketjun haaran syntyminen merkittävällä 24 lohkon uudelleenjärjestelyllä 12. maaliskuuta 2013. Tämä tapahtuma on yksityiskohtaisesti kuvattu BIP50:ssä. Myöhemmin, tämä järjestelmän muutos johti jopa tahattomaan kovaan haaraan (hard fork) 15. toukokuuta 2013.