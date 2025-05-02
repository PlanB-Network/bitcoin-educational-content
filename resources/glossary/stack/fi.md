---
term: AKKU
---

Komentosarjakielessä, jota käytetään Bitcoin UTXO:n käyttöehtojen liittämiseen, pino on LIFO (*Last In, First Out*) -tietorakenne, jota käytetään tilapäisen Elements:n tallentamiseen komentosarjan suorittamisen aikana. Skriptin jokainen operaatio käsittelee näitä pinoja, joihin voidaan lisätä (*push*) tai poistaa (*pop*) Elements:ta. Skriptit käyttävät pinoja lausekkeiden arviointiin, väliaikaisten muuttujien tallentamiseen ja ehtojen hallintaan.


Bitcoin-skriptiä suoritettaessa voidaan käyttää kahta pinoa: pääpinoa ja alt-pinoa (vaihtoehtoista pinoa). Pääpinoa käytetään suurimpaan osaan komentosarjan toiminnoista. Tässä pinossa komentosarjatoiminnot lisäävät, poistavat tai käsittelevät tietoja. Vaihtoehtoista pinoa taas käytetään tietojen väliaikaiseen säilyttämiseen komentosarjan suorituksen aikana. Erityiset op-koodit, kuten `OP_TOALTSTACK` ja `OP_FROMALTSTACK`, mahdollistavat Elements:n siirtämisen pääpinosta vaihtoehtoiseen pinoon ja päinvastoin.


Kun esimerkiksi tapahtuma validoidaan, allekirjoitukset ja julkiset avaimet työnnetään pääpinoon ja käsitellään peräkkäisillä opcodeilla sen tarkistamiseksi, että allekirjoitukset vastaavat tapahtuman avaimia ja tietoja.