---
name: Amboss
description: Utforsk og analyser Lightning Network
---

![cover](assets/cover.webp)



Lightning Network er en Layer av Bitcoin-protokollen, som først og fremst ble utviklet for å fremme innføringen av Bitcoin-betalinger på daglig basis ved å øke behandlingshastigheten for hver transaksjon. Lightning Network er basert på desentraliseringsprinsippet og består av noder (datamaskiner som kjører en Lightning-implementering) som kommuniserer peer-to-peer og videresender data (betalinger og betalingsverifisering) til hverandre.



https://planb.network/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Akkurat som i hovedkjeden har det blitt viktig å gjøre det mulig for brukerne å kjenne til informasjonen og statusen i nettverket, for å gjøre det lettere å koble sammen noder og minimere likviditetsproblemet som vanligvis oppstår i nettverket. På Lightning Network anbefaler vi mikrobetalinger på relativt mindre beløp enn for transaksjoner på Bitcoin-hovedkjeden.



Det er viktig å merke seg at ikke alle Lightning-noder er tilgjengelige på Amboss-plattformen.



I likhet med [Mempool Space] (https://Mempool.space), som gir nyttig informasjon om Bitcoin-protokollens hovedkjede, har [Amboss] (https://amboss.space) siden 2022 gitt informasjon om :





- Noder på Lightning Network
- Betalingskanaler og deres betalingskapasitet
- Lightning Network-utviklingen over tid
- Statistikk over gebyrer til relay-noder for betalingene dine.



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

I denne veiledningen tar vi deg med på en omvisning i denne plattformen, som er en viktig ressurs for Lightning Network-brukere, de som ønsker å koble til noden sin for å utvide nettverket osv.




## Finn par



Et av målene med Amboss-plattformen er å gjøre det mulig for de ulike nodene i nettverket å koble seg sammen og kommunisere informasjon med hverandre. På plattformens hjemmeside kan du søke direkte etter navnet på en node du allerede kjenner, eller finne noder fra de mest populære Lightning-porteføljene du bruker.



![home](assets/fr/01.webp)



![wallet](assets/fr/02.webp)



https://planb.network/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f

På hjemmesiden finner du også noder som er klassifisert i henhold til :




- Kapasitetsutvikling: mengden Bitcoin som er knyttet til nodens offentlige nøkkel, og den totale mengden som er tilgjengelig i alle kanalene.
- Kanalutvikling: antall nye forbindelser til andre noder i nettverket.
- Nodepopularitet: hvor ofte noden brukes.



![nodes](assets/fr/03.webp)



Å velge riktig node å koble seg til handler derfor om å sjekke følgende kriterier:





- Sørg for at noden har tilstrekkelig med bitcoins; jo større kapasitet noden har, desto mer bitcoins kan du betale.





- Sørg for at noden har et stort antall tilkoblinger og åpne kanaler med andre noder i nettverket.





- Kontroller at noden er aktiv og fortsatt verdsatt av de andre nodene ved å sjekke antall nye kanaler. Jo flere nye kanaler noden har åpne, desto mer verdsatt er den av de andre nodene i nettverket.



Når du har funnet riktig node, klikker du på navnet for å komme til siden med informasjon om noden.



På denne Interface, ved å sjekke Timestamp for den nyopprettede kanalen, får du en pekepinn på aktiviteten til denne noden. Du finner også informasjon om kapasiteten til denne nodens kanaler: Denne informasjonen er viktig hvis du ønsker å bruke denne noden aktivt til å utføre betalinger.




![node_info](assets/fr/04.webp)



I venstre del finner du mer informasjon om plasseringen av denne noden. Du kan for eksempel vise :




- Den offentlige nøkkelen: identifikatoren rett under node-navnet.
- Den geografiske posisjonen til denne noden.




![channels](assets/fr/05.webp)



Denne Interface forteller deg tilkoblings-Address for denne noden: den har formen `pubkey@ip:port`. I vårt eksempel ønsker vi å koble oss til noden hvis :




- den offentlige nøkkelen `pubkey` er: `035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226`
- iP Address: `170.75.163.209`
- Porten: `9735`



![geoinfo](assets/fr/06.webp)



I delen **Channels** ser du listen over åpne kanaler og nodens forbindelser til andre noder i nettverket. På denne Interface er det flere opplysninger som er viktige for å bekrefte at denne noden svarer til våre behov eller er pålitelig:





- Innkommende forhold**: Beløpet noden vil belaste deg for hver million Satoshi den mottar, avhengig av hvilken kanal som er valgt.
- Forholdstallet (parts per million)** : som representerer antall Satoshi per million enheter som noden vil belaste deg når du bestemmer deg for å foreta en betaling via en av dens kanaler. La oss si at du bestemmer deg for å betale `10_000 Sats` via en kanal som har et ppm-forhold på `500 Sats`, da må du betale noden `10_000 * 500 / 1_000_000` satoshis, tilsvarende `5 Sats`.
- Maksimum [HTLC](https://planb.network/resources/glossary/htlc)** : Det maksimale beløpet denne noden tillater deg å transittere via en av disse kanalene.



Ved å se i tabellen i denne Interface kan du også finne all denne informasjonen om noden den er koblet til.



![channels_info](assets/fr/07.webp)



I delen **Kanalkart** kan du se fordelingen og kapasiteten til de ulike kanalene på denne noden. Du kan endre fordelingskriteriene som vises, ved å velge ett av alternativene i rullegardinlisten til høyre.



![cha_maps](assets/fr/08.webp)



Avsnittet **Lukkede kanaler** grupperer alle nodens tidligere kanaler i henhold til type lukking:




- Gjensidig stenging**: representerer en avtale mellom begge parter, som bruker sin private nøkkel til å signere transaksjonen som markerer stengingen av kanalen og fordelingen av saldoer i den
- En **tvungen stenging**: representerer en brå, ensidig stenging av en del av kanalen. Denne typen stenging anbefales ikke, ettersom Lightning Network er en straffebasert protokoll: Når du prøver å svindle saldoen i en kanal, risikerer du å miste all din tilgjengelige saldo i den kanalen.



![closed](assets/fr/09.webp)



Få informasjon om transittgebyrer for å dirigere betalingene dine gjennom en kanal på noden du bruker



![fees](assets/fr/10.webp)



## Nettverksinformasjon



Amboss fokuserer ikke bare på informasjon om nettverksmedlemmene, men også på selve nettverkets tilstand.



I delen **Statistikk**, under menyen "Simuleringer" til venstre, finner du en graf som viser sannsynligheten for en vellykket betaling som en funksjon av betalingsbeløpet.



Du vil faktisk legge merke til at kurven er fallende, for etter hvert som beløpet på betalingen din øker, er det mindre sjanse for at betalingen går gjennom. Dette gjenspeiler det reelle likviditetsproblemet på Lightning Network. For eksempel har en betaling på `10_000` satoshier `79 %` sjanse for å bli gjennomført. På den annen side har du mindre enn 13 % sjanse for å lykkes med en betaling på 3_000_000` satoshier.



![network](assets/fr/11.webp)



I menyen **Nettverksstatistikk** kan du vise grafisk statistikk for :




- Betalingskanaler
- Noder
- Kapasitet
- Avgifter
- Kanalutvikling.



![network_stat](assets/fr/12.webp)



I menyen **Markedsstatistikk** kan du under **Ordredetaljer** se etterspørselen etter likviditet på Lightning Network. Denne grafen kan også vise hvilke kanaler som er mest etterspurt og/eller hvilke som har betydelig kapasitet.



![markets](assets/fr/13.webp)




## Verktøy



Amboss tilbyr en rekke verktøy som hjelper deg med å optimalisere søk og handlinger.



### Lightning Network dekoder



Dette verktøyet er hovedsakelig ansvarlig for å gi deg detaljer om strukturen til en Lightning Invoice, Lightning Address eller Lightning URL.



På hjemmesiden, i **Verktøy**-delen, kan du for eksempel sende inn Lightning Address.



![decoder](assets/fr/14.webp)



Fra denne dekoderen kan du få informasjon som f.eks:




- nodens offentlige nøkkel som er knyttet til Lightning Address;
- Utløpstiden for en Invoice fra din Address;
- Minimum og maksimum du kan sende;
- Nostr-noden som er knyttet til Address, hvis Nostr er aktivert på denne noden.



![decode](assets/fr/15.webp)



### Magma IA



Oppdag det nyeste verktøyet som Amboss har lansert for effektiv administrasjon av tilkoblinger til Lightning Network-noder. Magma AI bruker dedikert kunstig intelligens for å fokusere på et viktig problem: å gjøre et godt utvalg av noder å koble seg til.



![magma](assets/fr/16.webp)



### Satoshi kalkulator



Finn ut den nåværende prisen på Bitcoin i din lokale valuta (EUR / USD). På hjemmesiden kan du bruke satoshi-kalkulatoren til å finne ut den gjeldende markedsprisen.



![calculator](assets/fr/17.webp)




Du har nå fått en komplett omvisning i plattformens funksjoner og analyseverktøy. Nedenfor finner du artikkelen vår om Bitcoin **Mempool.space**-utforskeren.



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f