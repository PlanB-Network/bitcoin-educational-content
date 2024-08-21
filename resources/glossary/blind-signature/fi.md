---
termi: SOKEA ALLEKIRJOITUS
---

Chaumin sokeat allekirjoitukset ovat digitaalisen allekirjoituksen muoto, jossa allekirjoituksen antaja ei tiedä viestin sisältöä, jonka hän allekirjoittaa. Allekirjoitus voidaan kuitenkin myöhemmin varmentaa alkuperäisen viestin kanssa. Tämän tekniikan kehitti kryptografi David Chaum vuonna 1983.

Kuvitellaan esimerkki yrityksestä, joka haluaa todentaa luottamuksellisen asiakirjan, kuten sopimuksen, paljastamatta sen sisältöä. Yritys soveltaa maskausprosessia, joka kryptografisesti muuntaa alkuperäisen asiakirjan palautuvalla tavalla. Tämä muunnettu asiakirja lähetetään sertifiointiviranomaiselle, joka soveltaa sokeaa allekirjoitusta tietämättä taustalla olevaa sisältöä. Saatuaan maskatun allekirjoitetun asiakirjan yritys poistaa maskauksen allekirjoituksesta. Tuloksena on alkuperäinen asiakirja, joka on viranomaisen allekirjoituksella todennettu, ilman että viranomainen on koskaan nähnyt alkuperäistä sisältöä.

Näin ollen Chaumin sokeat allekirjoitukset mahdollistavat asiakirjan aitouden todentamisen tietämättä sen sisältöä, varmistaen sekä käyttäjän tietojen luottamuksellisuuden että allekirjoitetun asiakirjan eheyden.

Bitcoinissa tätä protokollaa käytetään Chaumin pankkien järjestelmissä lisäkerroksena (Cashu, Fedimint ym.), mutta erityisesti Chaumin coinjoin-protokollissa, varmistamaan, että koordinaattori ei pysty yhdistämään sisääntuloa ja ulostuloa.