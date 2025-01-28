---
term: P2PK

---
P2PK on lyhenne sanoista *Pay to Public Key*. Se on Bitcoinissa käytetty vakioskriptimalli, jolla luodaan UTXO:n käyttöehdot. Se mahdollistaa bitcoinien lukitsemisen suoraan julkiseen avaimeen osoitteen sijaan.

Teknisesti P2PK-skripti sisältää julkisen avaimen ja ohjeen, joka vaatii vastaavan digitaalisen allekirjoituksen varojen avaamiseksi. Kun omistaja haluaa käyttää bitcoineja, hänen on annettava siihen liittyvällä yksityisellä avaimella tuotettu allekirjoitus. Tämä allekirjoitus tarkistetaan ECDSA:n (*Elliptic Curve Digital Signature Algorithm*) avulla. P2PK:ta käytettiin usein Bitcoinin varhaisissa versioissa, erityisesti Satoshi Nakamoton toimesta. Nykyään sitä ei käytetä enää juuri lainkaan.