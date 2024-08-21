---
termi: P2PKH
---

P2PKH tarkoittaa *Maksa julkisen avaimen hajautusarvoon*. Se on standardi skriptimalli, jota käytetään UTXO:n käyttöehtojen määrittämiseen. Se mahdollistaa bitcoinien lukitsemisen julkisen avaimen hajautusarvoon, eli vastaanotto-osoitteeseen. Tämä skripti liittyy Legacy-standardiin ja sen esitteli Bitcoinin alkuaikoina Satoshi Nakamoto.

Toisin kuin P2PK:ssa, jossa julkinen avain sisällytetään skriptiin eksplisiittisesti, P2PKH käyttää julkisen avaimen kryptografista sormenjälkeä. Tämä skripti sisältää julkisen avaimen `SHA256`-hajautusarvon `RIPEMD160`-hajautuksen ja edellyttää, että varojen saamiseksi vastaanottajan on toimitettava julkinen avain, joka vastaa tätä hajautusarvoa, sekä kelvollinen digitaalinen allekirjoitus, joka on luotu yhdistettyä yksityistä avainta käyttäen. P2PKH-osoitteet koodataan käyttäen `Base58Check`-muotoa, mikä antaa niille robustiuden kirjoitusvirheitä vastaan käyttämällä tarkistussummaa. Nämä osoitteet alkavat aina numerolla `1`.