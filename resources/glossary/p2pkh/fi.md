---
term: P2PKH

---
P2PKH tarkoittaa *Pay to Public Key Hash*. Se on vakioskriptimalli, jota käytetään UTXO:n käyttöehtojen määrittämiseen. Se mahdollistaa bitcoinien lukitsemisen julkisen avaimen hashiin eli vastaanottavaan osoitteeseen. Tämä skripti liittyy Legacy-standardiin, ja Satoshi Nakamoto otti sen käyttöön Bitcoinin varhaisissa versioissa.

Toisin kuin P2PK, jossa julkinen avain on nimenomaisesti sisällytetty käsikirjoitukseen, P2PKH käyttää julkisen avaimen kryptografista sormenjälkeä. Tämä käsikirjoitus sisältää julkisen avaimen `SHA256`:n `RIPEMD160`-hashtimerkin, ja siinä määrätään, että saadakseen varat käyttöönsä vastaanottajan on esitettävä julkinen avain, joka vastaa tätä hashtimerkkiä, sekä voimassa oleva digitaalinen allekirjoitus, joka on luotu siihen liittyvästä yksityisestä avaimesta. P2PKH-osoitteet koodataan käyttäen `Base58Check`-muotoa, joka antaa niille varmuuden kirjoitusvirheitä vastaan käyttämällä tarkistussummaa. Osoitteet alkavat aina numerolla `1`.