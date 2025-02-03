---
term: BIP118

---
Bitcoinin parantamista koskeva ehdotus, jonka tarkoituksena on ottaa käyttöön kaksi uutta SigHash Flag -muunninta: `SIGHASH_ANYPREVOUT` ja `SIGHASH_ANYPREVOUTANYSCRIPT`. Nämä ominaisuudet laajentavat Bitcoin-tapahtumien ominaisuuksia erityisesti älykkäiden sopimusten ja Lightning Networkin kaltaisten overlay-ratkaisujen osalta. BIP118 mahdollistaisi erityisesti Eltoon käytön. `SIGHASH_ANYPREVOUT`:n tärkein etu on se, että se mahdollistaa allekirjoitusten uudelleenkäytön useissa transaktioissa, mikä lisää joustavuutta. Erityisesti nämä SigHashit mahdollistavat allekirjoituksen, joka ei kata yhtään transaktion syötettä.