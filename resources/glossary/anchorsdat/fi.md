---
termi: ANCHORS.DAT
---

Tiedosto, jota käytetään Bitcoin Core -asiakasohjelmassa tallentamaan ulospäin suuntautuvien solmujen IP-osoitteet, joihin asiakas oli yhdistetty ennen sammuttamista. Näin ollen anchors.dat-tiedosto luodaan joka kerta, kun solmu pysäytetään, ja se poistetaan, kun se käynnistetään uudelleen. Tässä tiedostossa olevien solmujen IP-osoitteita käytetään auttamaan nopeasti yhteyksien muodostamisessa, kun solmu käynnistetään uudelleen.