---
termi: P2SH-P2WPKH
---

P2SH-P2WPKH tarkoittaa *Maksa skriptitunnisteelle - Maksa todisteen julkisen avaimen tunnisteelle*. Se on standardi skriptimalli, jota käytetään määrittämään kulutusehdot UTXO:lle, joka tunnetaan myös nimellä "Nested SegWit".

P2SH-P2WPKH otettiin käyttöön SegWitin toteutuksen yhteydessä elokuussa 2017. Tämä skripti on P2WPKH, joka on kääritty P2SH:n sisään. Se lukitsee bitcoineja julkisen avaimen tunnisteen perusteella. Erotuksena klassiseen P2WPKH:oon on, että skripti on kääritty klassisen P2SH:n `redeemScript`iin.

Tämä skripti luotiin SegWitin käyttöönoton yhteydessä helpottamaan sen omaksumista. Se mahdollistaa tämän uuden standardin käytön, jopa palveluissa tai lompakoissa, jotka eivät vielä ole natiivisti yhteensopivia SegWitin kanssa. Se on eräänlainen siirtymäskripti kohti uutta standardia. Nykyään näiden käärittyjen SegWit-skriptien käyttö ei siis ole enää kovin relevanttia, koska useimmat lompakot ovat ottaneet käyttöön natiivin SegWitin. P2SH-P2WPKH-osoitteet kirjoitetaan käyttäen `Base58Check`-koodausta ja ne alkavat aina `3`:lla, kuten mikä tahansa P2SH-osoite.

> ► *`P2SH-P2WPKH` kutsutaan joskus myös `P2WPKH-nested-in-P2SH`.*