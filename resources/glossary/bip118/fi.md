---
termi: BIP118
---

Ehdotus Bitcoinin parantamiseksi, jonka tavoitteena on ottaa käyttöön kaksi uutta SigHash-lipun muokkaajaa: `SIGHASH_ANYPREVOUT` ja `SIGHASH_ANYPREVOUTANYSCRIPT`. Nämä ominaisuudet laajentavat Bitcoin-siirtojen mahdollisuuksia, erityisesti älykkäiden sopimusten ja päällysratkaisujen, kuten Lightning Networkin, osalta. BIP118 mahdollistaisi erityisesti Eltoo:n käytön. `SIGHASH_ANYPREVOUT`-ominaisuuden pääetu on mahdollistaa allekirjoitusten uudelleenkäyttö useissa siirroissa, mikä tarjoaa enemmän joustavuutta. Erityisesti nämä SigHashit mahdollistavat allekirjoituksen, joka ei kata yhtäkään siirron syötteistä.