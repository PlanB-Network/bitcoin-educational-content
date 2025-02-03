---
term: STACK

---
Bitcoin UTXO:n käyttöehtojen soveltamiseen käytettävän komentosarjakielen yhteydessä pino on "LIFO"-tietorakenne (*Last In, First Out*), jota käytetään väliaikaisten elementtien tallentamiseen komentosarjan suorittamisen aikana. Skriptin jokainen operaatio manipuloi näitä pinoja, joihin voidaan lisätä (*push*) tai poistaa (*pop*) elementtejä. Skriptit käyttävät pinoja lausekkeiden arviointiin, väliaikaisten muuttujien tallentamiseen ja ehtojen hallintaan.

Bitcoin-skriptin suorittamisen aikana voidaan käyttää kahta pinoa: pääpinoa ja alt-pinoa (vaihtoehtoista pinoa). Pääpinoa käytetään suurimpaan osaan skriptin toiminnoista. Tässä pinossa komentosarjatoiminnot lisäävät, poistavat tai käsittelevät tietoja. Vaihtoehtoisessa pinossa puolestaan säilytetään väliaikaisesti tietoja komentosarjan suorituksen aikana. Erityiset op-koodit, kuten `OP_TOALTSTACK` ja `OP_FROMALTSTACK`, mahdollistavat elementtien siirtämisen pääpinosta vaihtoehtoiseen pinoon ja päinvastoin.

Esimerkiksi tapahtuman validoinnin aikana allekirjoitukset ja julkiset avaimet työnnetään pääpinoon ja niitä käsitellään peräkkäisillä opcodeilla sen tarkistamiseksi, että allekirjoitukset vastaavat avaimia ja tapahtumatietoja.

> ► *Englanniksi "pile" tarkoittaa "pino". Englanninkielistä termiä käytetään yleensä myös ranskaksi teknisissä keskusteluissa.*