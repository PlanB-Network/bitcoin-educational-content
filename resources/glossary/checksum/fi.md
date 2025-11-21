---
term: CHECKSUM
---

Tarkistussumma on datajoukosta laskettu arvo, jota käytetään tiedon eheyden ja pätevyyden tarkistamiseen siirron tai tallennuksen aikana. Tarkistussumma-algoritmit on suunniteltu havaitsemaan tahattomat virheet tai tietojen tahattomat muutokset, kuten siirtovirheet tai tiedostojen korruptoituminen. On olemassa erityyppisiä tarkistussummakoodeja, kuten pariteettitarkistuksia, modulaarisia tarkistussummia, kryptografisia Hash-funktioita tai BCH-koodeja (*Bose, Ray-Chaudhuri ja Hocquenghem*).


Bitcoin:ssa tarkistussummia käytetään sovellustasolla varmistamaan vastaanotettujen osoitteiden eheys. Tarkistussumma lasketaan käyttäjän Address:n hyötykuormasta ja lisätään sitten kyseiseen Address:een, jotta voidaan havaita mahdolliset virheet sen syötteessä. Tarkistussumma on mukana myös palautuslausekkeissa (mnemonics).


> ► *On yleisesti hyväksytty käyttää englanninkielistä termiä "checksum" suoraan ranskaksi.*