---
term: Anchors.dat

definition: Bitcoin Core-tiedosto, joka tallentaa IP-osoitteita solmuista, joihin asiakas oli yhdistetty ennen sammutusta, jotta uudelleenyhteydelle voidaan helpottaa uudelleen käynnistyksellä.
---
Tiedosto, jota käytetään Bitcoin Core -asiakasohjelmassa tallentamaan niiden lähtevien solmujen IP-osoitteet, joihin asiakas oli yhteydessä ennen sammuttamista. Anchors.dat-tiedosto luodaan siis aina, kun solmu pysäytetään, ja se poistetaan, kun se käynnistetään uudelleen. Solmuja, joiden IP-osoitteet sisältyvät tähän tiedostoon, käytetään apuna yhteyksien nopeassa muodostamisessa, kun solmu käynnistetään uudelleen.