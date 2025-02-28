---
term: MERKLE TREE

---
Merkle Tree on kryptografinen akkumulaattori. Se on menetelmä, jolla voidaan todistaa tietyn tiedon osan kuuluminen suurempaan joukkoon. Se on tietorakenne, joka helpottaa tiedon todentamista kompaktissa muodossa. Bitcoin-järjestelmässä Merkle-puita käytetään lohkon transaktioiden ryhmittelyyn ja tiivistämiseen yhdeksi hashiksi, jota kutsutaan Merkle Rootiksi (tai "*Root Hash*"). Kukin transaktio hakataan, sitten vierekkäiset hakaset hakataan hierarkkisesti yhteen, kunnes saadaan Merkle Root.

![](../../dictionnaire/assets/1.webp)

Tämän rakenteen avulla voidaan nopeasti tarkistaa, sisältyykö tietty transaktio tiettyyn lohkoon, ilman että kaikkia transaktioita tarvitsee analysoida. Jos minulla on esimerkiksi käytössäni vain Merkle Root ja haluan todentaa, että `TX 7` todellakin kuuluu puuhun, tarvitsen vain seuraavat todisteet:


- "TX 7";
- `HASH 8`;
- `HASH 5-6`;
- `HASH 1-2-3-4`.

Näiden tietojen avulla pystyn laskemaan välisolmut Merkle-juureen asti.

![](../../dictionnaire/assets/2.webp)

Merkle Trees -menetelmää käytetään erityisesti kevyissä solmuissa (ns. "SPV"), jotka säilyttävät vain lohkojen otsikot, mutta eivät transaktioita. Tämä rakenne on myös UTREEXO-protokollassa, joka mahdollistaa UTXO-solmujen joukon tiivistämisen, ja MAST Taproot -protokollassa.

> ► *Merkle Tree on nimetty Ralph Merklen mukaan, joka on salakirjoittaja ja joka suunnitteli tämän rakenteen vuonna 1979. Merkle-puuta voidaan kutsua myös "hash-puuksi". Ranskaksi siitä käytetään nimitystä "Arbre de Merkle" tai "arbre de hachage".*