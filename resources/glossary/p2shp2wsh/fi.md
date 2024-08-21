---
termi: P2SH-P2WSH
---

P2SH-P2WSH tarkoittaa *Maksa skriptitunnisteelle - Maksa todistusskriptitunnisteelle*. Se on standardi skriptimalli, jota käytetään määrittämään kulutusehdot UTXO:lle, joka tunnetaan myös nimellä "Nested SegWit".

P2SH-P2WSH otettiin käyttöön SegWitin toteutuksen yhteydessä elokuussa 2017. Tämä skripti kuvaa P2WSH:n, joka on kääritty P2SH:n sisään. Se lukitsee bitcoineja skriptin hajautusarvon perusteella. Erotuksena klassiseen P2WSH:een on, että skripti on kääritty klassisen P2SH:n `redeemScript`iin.

Tämä skripti luotiin SegWitin käyttöönoton yhteydessä helpottamaan sen omaksumista. Se mahdollistaa tämän uuden standardin käytön, jopa palveluiden tai lompakoiden kanssa, jotka eivät vielä ole natiivisti yhteensopivia SegWitin kanssa. Nykyään näiden käärittyjen SegWit-skriptien käyttö ei siis ole enää kovin relevanttia, koska useimmat lompakot ovat ottaneet käyttöön natiivin SegWitin. P2SH-P2WSH osoitteet kirjoitetaan käyttäen `Base58Check`-koodausta ja ne alkavat aina `3`:lla, kuten mikä tahansa P2SH-osoite.