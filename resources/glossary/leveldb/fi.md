---
term: LEVELDB

---
Googlen suunnittelema kevyt, nopea ja avoimen lähdekoodin avainarvotallennuskirjasto. Sitä käytetään Bitcoinissa UTXO-joukon, transaktioindeksin ja lohkoindeksin tallentamiseen. Tämä tietokantajärjestelmä esiteltiin vuonna 2012 osana "Ultraprune" Pull Requestia, jonka tarkoituksena oli korvata BerkeleyDB. Tällä muutoksella oli merkittäviä vaikutuksia, kuten ensimmäisen lohkoketjun jakamisen luominen 24 lohkon suurella uudelleenjärjestelyllä 12. maaliskuuta 2013. Tämä tapaus kuvattiin yksityiskohtaisesti BIP50:ssä. Myöhemmin tämä järjestelmämuutos johti jopa tahattomaan hard forkiin 15. toukokuuta 2013.