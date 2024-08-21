---
termi: MERKLE-PUU
---

Merkle-puu on kryptografinen kertymä. Se on menetelmä todistaa tietyn tiedon jäsenyys suuremmassa joukossa. Se on tietorakenne, joka helpottaa tiedon vahvistamista tiiviissä muodossa. Bitcoin-järjestelmässä Merkle-puita käytetään ryhmittelemään ja tiivistämään lohkon transaktiot yhteen tiivisteeseen, jota kutsutaan Merkle-juureksi (tai "*Root Hash*"). Jokainen transaktio hajautetaan, sitten vierekkäiset hajautukset hajautetaan yhdessä hierarkkisesti, kunnes Merkle-juuri saadaan.

![](../../dictionnaire/assets/1.png)

Tämä rakenne mahdollistaa nopean vahvistuksen siitä, sisältyykö tietty transaktio annettuun lohkoon tutkimatta kaikkia transaktioita. Esimerkiksi, jos minulla on vain Merkle-juuri ja haluan varmistaa, että `TX 7` on todella osa puuta, tarvitsisin vain seuraavat todisteet:
* `TX 7`;
* `HASH 8`;
* `HASH 5-6`;
* `HASH 1-2-3-4`.
Näiden tietojen avulla pystyn laskemaan välisolmut aina Merkle-juureen saakka.

![](../../dictionnaire/assets/2.png)

Merkle-puita käytetään erityisesti kevyissä solmuissa (tunnetaan nimellä "SPV"), jotka säilyttävät vain lohkojen otsikot, mutta eivät transaktioita. Tätä rakennetta käytetään myös UTREEXO-protokollassa, protokollassa, joka mahdollistaa solmujen UTXO-joukon tiivistämisen, sekä MAST Taprootissa.

> ► *Merkle-puu on nimetty Ralph Merklen mukaan, kryptografin, joka suunnitteli tämän rakenteen vuonna 1979. Merkle-puuta voidaan myös kutsua "hajautuspuuksi". Ranskaksi se viitataan nimellä "Arbre de Merkle" tai "arbre de hachage".*