---
term: CHECKSUM

---
Tarkistussumma on datajoukosta laskettu arvo, jota käytetään tiedon eheyden ja pätevyyden tarkistamiseen sen siirron tai tallennuksen aikana. Tarkistussumma-algoritmit on suunniteltu havaitsemaan tahattomat virheet tai tietojen tahattomat muutokset, kuten siirtovirheet tai tiedostojen korruptoituminen. On olemassa erityyppisiä tarkistussummakoodeja, kuten pariteettitarkistuksia, modulaarisia tarkistussummia, kryptografisia hash-funktioita tai BCH-koodeja (*Bose, Ray-Chaudhuri ja Hocquenghem*).

Bitcoinissa tarkistussummia käytetään sovellustasolla varmistamaan vastaanottavien osoitteiden eheys. Tarkistussumma lasketaan käyttäjän osoitteen hyötykuormasta ja lisätään sitten tähän osoitteeseen mahdollisten virheiden havaitsemiseksi osoitteen syöttämisen aikana. Tarkistussumma esiintyy myös palautuslausekkeissa (mnemonic).

> ► *Somme de contrôle on suomeksi käännettynä "tarkistussumma". Ranskankielessä on yleisesti hyväksytty käyttää suoraan termiä "checksum".*