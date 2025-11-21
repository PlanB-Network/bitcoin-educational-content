---
term: EXTRA-Nonce
---

Kenttä, jota käytetään lohkon Coinbase Transaction:n `scriptSig`-kentässä, joka mahdollistaa suuremman määrän testattavia vaihtoehtoja, jotta Hash olisi vaikeustavoitetta alhaisempi, klassisen Nonce:n lisäksi, joka löytyy suoraan kunkin lohkon otsikosta.


Coinbase Transaction:n extra-Nonce:n muuttaminen muuttaa tämän tapahtuman tunnistetta ja siten myös lohkon kaikkien tapahtumien Merkle Root:tä, mikä muuttaa myös lohkon otsikkoa. Näin Miner voi jatkaa hashien etsimistä, kun klassisen Nonce:n alue on jo käytetty loppuun, muuttamatta lohkoehdokkaansa rakennetta.


Mining-pooleissa ylimääräinen Nonce on usein jaettu kahteen osaan: poolin tuottama osa kunkin hakkurin tunnistamiseksi ja hakkurin muokkaama osa kelvollista osuutta etsiessään. Näin poolin eri hakkurit voivat työskennellä samanaikaisesti saman ehdokaslohkon parissa koko nonces-alueella ilman, että sama työ on päällekkäistä poolitasolla.