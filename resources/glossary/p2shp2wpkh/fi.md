---
term: P2SH-P2WPKH

---
P2SH-P2WPKH tarkoittaa *Pay to Script Hash - Pay to Witness Public Key Hash*. Se on vakioskriptimalli, jota käytetään UTXO:n käyttöehtojen luomiseen, joka tunnetaan myös nimellä "Nested SegWit".

P2SH-P2WPKH otettiin käyttöön SegWitin käyttöönoton myötä elokuussa 2017. Tämä skripti on P2WPKH, joka on kääritty P2SH:n sisään. Se lukitsee bitcoineja julkisen avaimen hashin perusteella. Erona klassiseen P2WPKH:hon on se, että skripti on kääritty klassisen P2SH:n `redeemScript`:iin.

Tämä skripti luotiin SegWitin käyttöönoton yhteydessä helpottamaan sen käyttöönottoa. Se mahdollistaa tämän uuden standardin käytön myös sellaisissa palveluissa tai lompakoissa, jotka eivät vielä ole täysin yhteensopivia SegWitin kanssa. Se on eräänlainen siirtymäskripti kohti uutta standardia. Nykyään ei siis ole enää kovin merkityksellistä käyttää tämäntyyppisiä käärittyjä SegWit-skriptejä, koska useimmat lompakot ovat toteuttaneet natiivin SegWitin. P2SH-P2WPKH-osoitteet kirjoitetaan käyttäen `Base58Check`-koodausta, ja ne alkavat aina `3`:lla, kuten kaikki P2SH-osoitteet.

> ► *``P2SH-P2WPKH` kutsutaan joskus myös `P2WPKH-nested-in-P2SH`.*