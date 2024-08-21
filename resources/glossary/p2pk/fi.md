---
termi: P2PK
---

P2PK tarkoittaa *Maksa julkiseen avaimeseen*. Se on standardi skriptimalli, jota käytetään Bitcoinissa määrittämään kulutusehdot UTXO:lle. Se mahdollistaa bitcoinien lukitsemisen suoraan julkiseen avaimeseen, sen sijaan että ne lukittaisiin osoitteeseen.
Teknisesti P2PK-skripti sisältää julkisen avaimen ja ohjeen, joka vaatii vastaavan digitaalisen allekirjoituksen varojen vapauttamiseksi. Kun omistaja haluaa käyttää bitcoineja, hänen on toimitettava allekirjoitus, joka on tuotettu yhdistettyä yksityistä avainta käyttäen. Tämä allekirjoitus varmennetaan käyttäen ECDSA:ta (*Elliptic Curve Digital Signature Algorithm*). P2PK:tä käytettiin usein Bitcoinin alkuaikoina, erityisesti Satoshi Nakamoton toimesta. Nykyään sitä käytetään lähes ei lainkaan.