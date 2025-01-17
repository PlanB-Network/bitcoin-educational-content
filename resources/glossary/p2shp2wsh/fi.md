---
term: P2SH-P2WSH

---
P2SH-P2WSH tarkoittaa *Pay to Script Hash - Pay to Witness Script Hash*. Se on vakioskriptimalli, jota käytetään UTXO:n käyttöehtojen luomiseen, joka tunnetaan myös nimellä "Nested SegWit".

P2SH-P2WSH otettiin käyttöön SegWitin käyttöönoton myötä elokuussa 2017. Tässä skriptissä kuvataan P2WSH, joka on kääritty P2SH:n sisään. Se lukitsee bitcoineja skriptin hashin perusteella. Erona klassiseen P2WSH:hon on se, että skripti on kääritty klassisen P2SH:n `redeemScript`:iin.

Tämä skripti luotiin SegWitin käyttöönoton yhteydessä helpottamaan sen käyttöönottoa. Se mahdollistaa tämän uuden standardin käytön myös sellaisissa palveluissa tai lompakoissa, jotka eivät vielä ole täysin yhteensopivia SegWitin kanssa. Nykyään ei siis ole enää kovin tärkeää käyttää tämäntyyppisiä pakattuja SegWit-skriptejä, koska useimmat lompakot ovat toteuttaneet natiivin SegWitin. P2SH-P2WSH-osoitteet kirjoitetaan käyttäen `Base58Check`-koodausta, ja ne alkavat aina `3`:lla, kuten kaikki P2SH-osoitteet.