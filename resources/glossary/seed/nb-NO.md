---
term: GRAIN
---

I den spesifikke konteksten av en hierarkisk deterministisk Bitcoin-portefølje er en seed en 512-biters informasjonsbit som er avledet fra en tilfeldig hendelse. Den brukes til å deterministisk og hierarkisk generate et sett med private nøkler og deres tilsvarende offentlige nøkler for en Bitcoin-portefølje. seed forveksles ofte med selve gjenopprettingsfrasen. Men det er ikke det samme. seed oppnås ved å bruke funksjonen `PBKDF2` på Mnemonic-frasen og en hvilken som helst passphrase.


seed ble oppfunnet med BIP32, som definerte grunnlaget for den hierarkiske deterministiske porteføljen. I denne standarden målte seed 128 bits. Dette gjør at alle nøklene i en portefølje kan avledes fra én enkelt informasjon, i motsetning til JBOK-porteføljer (*Just a Bunch Of Keys*), som krever nye sikkerhetskopier for hver nøkkel som genereres. BIP39 foreslo deretter en koding av denne seed for å gjøre det enklere for mennesker å lese den. Denne kodingen har form av en frase, vanligvis referert til som en Mnemonic-frase eller gjenopprettingsfrase. Denne standarden unngår feil ved lagring av seed, særlig takket være bruken av en sjekksum.


Utenfor Bitcoin-sammenheng er en seed i kryptografi generelt en startverdi som brukes til å generate kryptografiske nøkler, eller mer generelt, alle typer data som produseres av en pseudotilfeldige tallgenerator. Denne startverdien må være tilfeldig og uforutsigbar for å garantere sikkerheten til det kryptografiske systemet. seed introduserer entropi i systemet, men den påfølgende genereringsprosessen er deterministisk.


> i vanlig språkbruk refererer de fleste bitcoin-brukere til Mnemonic-frasen når de snakker om "seed", og ikke til den mellomliggende avledningstilstanden som ligger mellom Mnemonic-frasen og hovednøkkelen