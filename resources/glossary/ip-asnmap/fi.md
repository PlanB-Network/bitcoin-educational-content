---
termi: IP_ASN.MAP
---

Tiedosto, jota käytetään Bitcoin Core:ssa ASMAP:n tallentamiseen, mikä parantaa IP-osoitteiden ryhmittelyä (eli kokoamista) nojaamalla Autonomisiin Järjestelmänumeroihin (ASN). Sen sijaan, että lähtevät yhteydet ryhmiteltäisiin IP-verkon etuliitteiden (/16) mukaan, tämä tiedosto mahdollistaa yhteyksien monipuolistamisen luomalla IP-osoitekartan ASNeille, jotka ovat ainutlaatuisia tunnisteita kullekin Internet-verkolle. Ideana on parantaa Bitcoin-verkon turvallisuutta ja topologiaa monipuolistamalla yhteyksiä suojaamaan tiettyjä hyökkäyksiä vastaan (erityisesti Erebus-hyökkäystä vastaan).