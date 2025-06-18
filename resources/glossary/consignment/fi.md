---
term: Consignment
---

Osana RGB-protokollaa ryhmittelee osapuolten välillä vaihdettavat tiedot, joihin sovelletaan *Client-side Validation*-protokollaa. Lähetyksiä on kahta pääluokkaa:




- Contract Consignment: liikkeeseenlaskijan toimittama, sisältää alustustiedot, kuten Schema, Genesis, Interface ja Interface Implementation.
- Siirto Consignment: maksajan toimittama. Sisältää koko tilasiirtymien historian, joka johtaa Terminal Consignment:ään (eli maksajan vastaanottamaan lopulliseen tilaan).


Näitä lähetyksiä ei kirjata julkisesti Blockchain:een, vaan ne vaihdetaan suoraan asianomaisten osapuolten välillä niiden valitseman viestintäkanavan kautta.