---
name: BLOCKSTREAM Explorer
description: Utforsk hovedområdet Layer i Bitcoin og Liquid Network
---

![cover](assets/cover.webp)



BLOCKSTREAM Explorer er et prosjekt som legger til rette for utforskning av transaksjoner og Global State i Bitcoin-protokollen, samt [*Sidechain*](https://planb.network/en/resources/glossary/Sidechain) Liquid som er utviklet av BLOCKSTREAM-selskapet.



Utforskeren [BLOCKSTREAM.info] (https://BLOCKSTREAM.info) ble startet i 2014 av BLOCKSTREAM, et selskap grunnlagt av Adam Back, og har som mål å tilby en robust infrastruktur for Bitcoin, som garanterer interoperabilitet og transaksjonssporing mellom lagene (On-Chain og Liquid), samtidig som den forbedrer brukernes sikkerhet og personvern.



I denne veiledningen presenterer vi hva som gjør den annerledes, tjenestene den tilbyr, og hvordan den gir sømløs overvåking av driften og statusen til Bitcoins On-Chain- og Liquid-lag.



## Kom i gang med BLOCKSTREAM



### Naviger i hovedkanalen



Når du går til BLOCKSTREAM.info explorer, på "**Dashboard**", er hovedprotokollkanalen Bitcoin valgt som standard. Fra denne Interface har du en oversikt over :





- Hovedkjedestørrelse: Nylig utvunnede blokker.



![blocks](assets/fr/01.webp)



Denne delen gir informasjon om nylig utvunnede blokker, Timestamp, antall transaksjoner som inngår i hver BLOCK, størrelsen i kilobyte (kB) og målingen av hver BLOCK i vektenheter (**WU** = *Weight Units*). Denne siste målingen er av interesse, ettersom den gjør det mulig for oss å evaluere optimaliseringen av BLOCK, gitt at hver BLOCK i hovedkjeden er begrenset til `4 000 000 WU`, eller `4 000 kWU`.





- Nylige transaksjoner.



![transactions](assets/fr/02.webp)



Transaksjonsdelen inneholder informasjon om transaksjonens unike identifikator, Bitcoin-verdien som er involvert, størrelsen i virtuelle byte (vB) - som representerer summen av alle data (inndata og utdata) - og den tilhørende avgiftssatsen. For eksempel vil en transaksjon med en størrelse på 153 vB til en sats på 2 sat/vB medføre en kostnad på 306 satoshis.



### Utforskning av væsker



Fra "**Blocks**"-menyen kan du spore historikken til hele hovedkjeden tilbake til den siste BLOCK som ble utvunnet.



![blocs](assets/fr/03.webp)



Ved å klikke på en spesifikk BLOCK kan du få mer informasjon om informasjonen og transaksjonene som inngår i den. For eksempel, for BLOCK 919330: du har Hash av BLOCK. Du kan også navigere til forrige BLOCK, ettersom hver utvunnet BLOCK (bortsett fra Genesis) er knyttet til den forrige, og beholder Hash fra forgjengeren.



![metadata](assets/fr/04.webp)



Ved å klikke på **"Detaljer"**-knappen kan du få mer informasjon om denne BLOCK, for eksempel dens status, som bekrefter at den har blitt lagt til i den beholdte og forplantede hovedkjeden. Du har også vanskelighetsgraden som denne BLOCK utvinnes med: denne vanskelighetsgraden representerer datakraften som kreves for å løse det kryptografiske problemet med Mining, og justeres hver 2016. blokk (ca. 2 uker).



![details](assets/fr/05.webp)



Under denne detaljseksjonen finner vi alle transaksjonene som inngår i denne BLOCK.



Den aller første transaksjonen i BLOCK kalles **transaksjonsmyntbasen**. Den brukes til å allokere Miners Mining-belønning (alle avgifter knyttet til transaksjonene som er inkludert i BLOCK og BLOCK-tilskuddet). Bitcoinsene som skapes av denne transaksjonen kan bare brukes når ytterligere 100 påfølgende blokker har blitt utvunnet. Med andre ord, for å kunne bruke dem, må Miner vente på produksjonen av BLOCK **919430**. Dette er kjent som [*"forfallsperioden"*] (https://planb.network/fr/resources/glossary/maturity-period).



Coinbase er en spesiell transaksjon: det er den eneste uten reell input, ettersom den ikke bruker noen bitcoins fra en tidligere transaksjon.




![coinbase](assets/fr/06.webp)



Alle andre transaksjoner er delt inn i to seksjoner: innganger og utganger.



For at bitcoins skal kunne brukes som input i en ny transaksjon, må initiativtakeren til transaksjonen bevise at han eller hun er i besittelse av bitcoins ved å oppgi en signatur som tilsvarer et bestemt skript. Hver bitcoins (UTXO) inneholder et skript som generelt krever en spesifikk signatur som bare innehaverens private nøkkel kan gi. Disse skriptene er ***scriptSig*** (i ASM), skrevet i Bitcoin Script, og kan være av ulike typer. I dette eksemplet kan vi se at UTXO-ene som ble brukt, var av typen P2SH til en utdata av typen P2WPKH (*Pay-to-Witness-Public-Key-Hash*).



Du kan spore historikken til en spesifikk UTXO ved hjelp av heuristikk. Vi inviterer deg til å oppdage de forskjellige Bitcoin-heuristikkene og hvordan du kan styrke konfidensialiteten til Bitcoin-transaksjonene dine:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



La oss ta eksemplet med denne transaksjonens utgående utgift. Ved å klikke på transaksjonsidentifikatoren blir vi omdirigert til delen **Transaksjoner** på siden med transaksjonsdetaljer.



![transaction](assets/fr/08.webp)



Fra denne siden kan du finne ut hvilken BLOCK transaksjonen var inkludert i. Avhengig av hvilken type Address som brukes, kan transaksjonen optimalisere dataene (*virtuelle byte*) og dermed betale mindre transaksjonsgebyrer. Denne transaksjonen sparte for eksempel 53 % i gebyrer ved å bruke et opprinnelig SegWit BECH32 Address-format som starter med `bc1q`.



![trx_details](assets/fr/09.webp)



## Liquid-belegg



Liquid Network er en [*Sidechain*](https://planb.network/en/resources/glossary/Sidechain) og en åpen kildekodeløsning på nivå 2 for Bitcoin-protokollen. Den muliggjør raskere og mer konfidensielle Bitcoin-transaksjoner.



Klikk på **"Liquid"**-knappen i BLOCKSTREAM.info-utforskeren for å bytte til Liquid Network.



![liquid](assets/fr/10.webp)



Når vi klikker på en av transaksjonene vi ønsker å følge, ser vi at beløpene for Bitcoin-brikkene er erstattet av ordene "**Konfidensielt**". I dette nettverket kan transaksjoner være konfidensielle, så vi kan ikke se beløpene for hver UTXO, verken i eller utenfor transaksjonen.



![liquid_trx](assets/fr/11.webp)



Vi merker oss imidlertid at prinsippene og mekanismene som finnes i Layer i Bitcoin-protokollen, er de samme: Bitcoin-låseskript og UTXO-sporbarhet.



![liquid_details](assets/fr/12.webp)



Liquid Network tilbyr også digitale eiendeler som ikke er deponerte, og som kan brukes av organisasjoner. I menyen **"Eiendeler"** finner du en liste over registrerte eiendeler, summen av dem og domenet de er knyttet til.



![assets](assets/fr/13.webp)



For hver eiendel kan du spore historikken for utstedelses- og brenningstransaksjoner (ved å slette summen i omløp).



![assets_trxs](assets/fr/14.webp)




## Flere alternativer



BLOCKSTREAM.info explorer inkluderer også visualiseringer og sporing av transaksjoner på Testnet, Bitcoin, On-Chain og Liquid Network.



![testnet](assets/fr/15.webp)



Når du går til Testnet-nettverket, bruker du ikke ekte bitcoins, men du har alle funksjonene som er beskrevet ovenfor.



![liquid_testnet](assets/fr/16.webp)



Dette nettverket har en annen kjedelengde, som du kan koble til og teste driften av Bitcoin- og Liquid-mekanismene.





- API-seksjonen er dedikert til alle som ønsker å integrere visse Explorer-funksjoner i sin egen applikasjon. Gjennom denne API kan du for eksempel avhøre hovedkjeden i de ulike lagene (On-Chain og Liquid), spore transaksjoner og finne ut gjennomsnittsgebyrene for transaksjoner i en BLOCK.



![api](assets/fr/17.webp)



Du er nå klar til å utnytte det fulle potensialet i BLOCKSTREAM Explorer til å spørre etter blokkjeder på On-Chain- og Liquid-lagene. Vi håper du har funnet denne veiledningen informativ, og anbefaler vår veiledning om en annen Bitcoin Explorer:



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f