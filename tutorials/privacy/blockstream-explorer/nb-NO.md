---
name: Blockstream Explorer
description: Utforsk hovedlaget i Bitcoin og Liquid Network
---

![cover](assets/cover.webp)



Blockstream Explorer er et prosjekt som gjør det lettere å utforske transaksjoner og den globale tilstanden til Bitcoin-protokollen, samt [*sidekjeden*] (https://planb.academy/en/resources/glossary/sidechain) Liquid utviklet av Blockstream-selskapet.



Utforskeren [blockstream.info] (https://blockstream.info) ble startet i 2014 av Blockstream, et selskap grunnlagt av Adam Back, og har som mål å tilby en robust infrastruktur for Bitcoin, som garanterer interoperabilitet og transaksjonssporing mellom lagene (on-chain og Liquid), samtidig som brukernes sikkerhet og personvern forbedres.



I denne veiledningen skal vi se på hva som skiller den fra andre, hvilke tjenester den tilbyr, og hvordan den gir sømløs overvåking av driften og statusen til Bitcoins on-chain- og Liquid-lag.



## Komme i gang med Blockstream explorer



### Naviger i hovedkanalen



Når du går til Blockstream.info explorer, på "**Dashboard**", er Bitcoin-protokollens hovedkjede valgt som standard. Fra dette grensesnittet har du oversikt over :





- Hovedkjedestørrelse: Nylig utvunnede blokker.



![blocks](assets/fr/01.webp)



Denne delen inneholder informasjon om nylig utvunnede blokker, tidsstempel, antall transaksjoner som er inkludert i hver blokk, størrelsen i kilobyte (kB) og målingen av hver blokk i vektenheter (**WU** = *Weight Units*). Den siste målingen er interessant fordi den gjør det mulig for oss å evaluere optimaliseringen av blokken, gitt at hver blokk i hovedkjeden er begrenset til "4 000 000 WU", eller "4 000 kWU".





- Nylige transaksjoner.



![transactions](assets/fr/02.webp)



Transaksjonsdelen inneholder informasjon om transaksjonens unike identifikator, bitcoin-verdien som er involvert, størrelsen i virtuelle byte (vB) - som representerer summen av alle data (input og output) - og den tilhørende gebyrsatsen. For eksempel vil en transaksjon med en størrelse på 153 vB til en sats på 2 sat/vB medføre et gebyr på 306 satoshis.



### Utforskning av væsker



Fra menyen "**Blocks**" kan du spore historikken til hele hovedkjeden tilbake til den siste blokken som ble utvunnet.



![blocs](assets/fr/03.webp)



Ved å klikke på en bestemt blokk kan du få mer informasjon om informasjonen og transaksjonene som inngår i den. For eksempel, for blokk 919330: du vil se hashen til blokken. Du kan også navigere til den forrige blokken, ettersom hver utvunnet blokk (bortsett fra Genesis) er knyttet til den forrige, og beholder hashen til forgjengeren.



![metadata](assets/fr/04.webp)



Ved å klikke på **"Detaljer"**-knappen kan du få mer informasjon om denne blokken, for eksempel dens status, som bekrefter at den har blitt lagt til i den beholdte og forplantede hovedkjeden. Du har også vanskeligheten som denne blokken er utvunnet med: denne vanskeligheten representerer datakraften som kreves for å løse det kryptografiske problemet med mining og justeres hver 2016 blokker (ca. 2 uker).



![details](assets/fr/05.webp)



Under denne detaljseksjonen finner vi alle transaksjonene som er inkludert i denne blokken.



Den aller første transaksjonen i blokken kalles **transaction coinbase**. Den brukes til å tildele utvinnerens mining-belønning (alle avgifter knyttet til transaksjonene som inngår i blokken og blokktilskuddet). Bitcoinsene som skapes av denne transaksjonen, kan bare brukes når ytterligere 100 påfølgende blokker har blitt utvunnet. Med andre ord, for å kunne bruke dem, må utvinneren vente på produksjonen av blokk **919430**. Dette er kjent som [*"forfallsperioden"*] (https://planb.academy/fr/resources/glossary/maturity-period).



Coinbase er en spesiell transaksjon: det er den eneste uten reell input, ettersom den ikke bruker noen bitcoins fra en tidligere transaksjon.




![coinbase](assets/fr/06.webp)



Alle andre transaksjoner er delt inn i to seksjoner: innganger og utganger.



For at bitcoins skal kunne brukes som input i en ny transaksjon, må initiativtakeren til transaksjonen bevise at han eller hun er i besittelse av bitcoins ved å oppgi en signatur som tilsvarer et bestemt skript. Hver bitcoins (UTXO) inneholder et skript som generelt krever en spesifikk signatur som bare innehaverens private nøkkel kan gi. Disse skriptene er ***scriptSig*** (i ASM), skrevet i Bitcoin Script, og kan være av ulike typer. I dette eksempelet kan vi se at UTXO-ene som ble brukt, var av typen P2SH til en utdata av typen P2WPKH (*Pay-to-Witness-Public-Key-Hash*).



Du kan spore historikken til en bestemt UTXO ved hjelp av heuristikk. Vi inviterer deg til å oppdage de forskjellige Bitcoin-heuristikkene og måter å styrke konfidensialiteten til transaksjonene dine på Bitcoin :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



La oss ta eksemplet med denne transaksjonens utgående utgift. Ved å klikke på transaksjonsidentifikatoren blir vi omdirigert til delen **Transaksjoner** på siden med transaksjonsdetaljer.



![transaction](assets/fr/08.webp)



Fra denne siden kan du finne ut hvilken blokk transaksjonen var inkludert i. Avhengig av hvilken type adresse som brukes, kan transaksjonen optimalisere dataene (*virtuelle byte*) og dermed betale mindre transaksjonsgebyrer. Denne transaksjonen sparte for eksempel 53 % i gebyrer ved å bruke et opprinnelig SegWit Bech32-adresseformat som starter med `bc1q`.



![trx_details](assets/fr/09.webp)



## Liquid-laget



Liquid Network er en [*sidekjede*] (https://planb.academy/en/resources/glossary/sidechain) og en åpen kildekodeløsning på nivå 2 for Bitcoin-protokollen. Den muliggjør raskere og mer konfidensielle bitcoin-transaksjoner.



Klikk på **"Liquid"**-knappen i Blockstream.info-utforskeren for å bytte til Liquid-nettverket.



![liquid](assets/fr/10.webp)



Når vi klikker på en av transaksjonene vi ønsker å spore, ser vi at bitcoin-beløpene er erstattet av ordene "**Confidential**". På dette nettverket kan transaksjoner være konfidensielle, slik at vi ikke kan se beløpene for hver UTXO, verken i eller utenfor transaksjonen.



![liquid_trx](assets/fr/11.webp)



Vi merker oss imidlertid at prinsippene og mekanismene i hovedlaget i Bitcoin-protokollen er de samme: bitcoin-låseskript og UTXO-sporbarhet.



![liquid_details](assets/fr/12.webp)



Liquid Network tilbyr også digitale eiendeler som ikke er deponerte, og som kan brukes av organisasjoner. I menyen **"Eiendeler"** finner du en liste over registrerte eiendeler, summen av disse og domenet de er knyttet til.



![assets](assets/fr/13.webp)



For hver eiendel kan du spore historikken for utstedelses- og brenningstransaksjoner (ved å slette summen i omløp).



![assets_trxs](assets/fr/14.webp)




## Flere alternativer



Blockstream.info explorer inkluderer også visualiseringer og sporing av transaksjoner på Testnet, Bitcoin, on-chain og Liquid Network.



![testnet](assets/fr/15.webp)



Når du går til Testnet-nettverket, bruker du ikke ekte bitcoins, men du har alle funksjonene som er beskrevet ovenfor.



![liquid_testnet](assets/fr/16.webp)



Dette nettverket har en annen kjedelengde, som du kan koble til og teste driften av Bitcoin- og Liquid-mekanismene.





- API-delen er dedikert til alle som ønsker å integrere visse Explorer-funksjoner i sin egen applikasjon. Gjennom denne API kan du for eksempel avhøre hovedkjeden i de ulike lagene (on-chain og Liquid), spore transaksjoner og finne ut de gjennomsnittlige avgiftene for transaksjoner i en blokk.



![api](assets/fr/17.webp)



Du er nå klar til å utnytte Blockstream Explorers fulle potensial for å spørre etter blokkjeder på on-chain- og Liquid-lagene. Vi håper du har funnet denne veiledningen informativ, og anbefaler vår veiledning om en annen Bitcoin-utforsker:



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f