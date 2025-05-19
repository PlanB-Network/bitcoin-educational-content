---
term: Anchor
---

RGB-protokollassa Anchor edustaa asiakaspuolen tietosarjaa, jota käytetään osoittamaan yksittäisen Commitment:n sisällyttäminen tapahtumaan. RGB-protokollassa Anchor koostuu seuraavista Elements:sta:




- transaction ID Bitcoin (txid) alkaen Witness Transaction ;
- Multi Protocol Commitment (MPC);
- Deterministic Bitcoin Commitment (DBC);
- Extra Transaction Proof (ETP), jos käytetään Tapret Commitment -mekanismia.


Anchor:n tarkoituksena on siis luoda todennettavissa oleva yhteys tietyn Bitcoin-tapahtuman ja RGB-protokollalla validoitujen yksityisten tietojen välille. Se takaa, että nämä tiedot todella sisältyvät Blockchain:een ilman, että niiden tarkkaa sisältöä julkistetaan.