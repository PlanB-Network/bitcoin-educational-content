---
name: Ashigaru - Stowaway
description: Hvordan gjennomfører jeg en Payjoin-transaksjon på Ashigaru?
---
![cover](assets/cover.webp)



> *Tving blokkjede-spioner til å revurdere alt de tror de vet

Payjoin er en Bitcoin-transaksjonsstruktur som er utformet for å forbedre brukernes konfidensialitet ved å involvere direkte samarbeid med betalingsmottakeren. Det finnes flere implementeringer som gjør det enklere å implementere og automatisere prosessen. Den mest kjente av disse er utvilsomt Stowaway, som opprinnelig ble utviklet av Samurai Wallet-teamet og nå er integrert i fork Ashigaru.



## Hvordan fungerer Stowaway?



Som tidligere nevnt integrerer Ashigaru et PayJoin-verktøy kalt "Stowaway". Dette er tilgjengelig i Ashigaru-appen på Android. For at en Payjoin skal kunne gjennomføres, må mottakeren (som også tar rollen som samarbeidspartner) bruke programvare som er kompatibel med Stowaway, dvs. foreløpig bare Ashigaru.



Stowaway er basert på en kategori av transaksjoner som Samurai omtalte som "Cahoots". En Cahoot er en samarbeidstransaksjon mellom flere brukere, som involverer en utveksling av informasjon utenfor Bitcoin-blokkjeden. Ashigaru tilbyr for øyeblikket to Cahoots-verktøy: Stowaway (Payjoins) og StonewallX2.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b

Cahoots-transaksjoner krever utveksling av delvis signerte transaksjoner mellom brukere. Denne prosessen kan være lang og omstendelig, spesielt når den utføres eksternt. Det er imidlertid fortsatt mulig å gjøre dette manuelt, hvis samarbeidspartnerne befinner seg på samme sted. Konkret innebærer dette å skanne fem QR-koder i rekkefølge, som utveksles mellom de to deltakerne.



På avstand blir denne metoden for kompleks. For å bøte på dette har Samourai utviklet en Tor-basert kryptert kommunikasjonsprotokoll kalt "*Soroban*". Takket være Soroban er utvekslingen som kreves for en Payjoin automatisert og foregår i bakgrunnen.



Denne krypterte kommunikasjonen krever en forbindelse og autentisering mellom Cahoot-deltakerne. Dette er grunnen til at Soroban er avhengig av brukernes Paynyms. Hvis du ennå ikke er kjent med hvordan Paynyms fungerer, kan du ta en titt på denne dedikerte veiledningen for å lære mer:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

Kort fortalt er et Paynym en unik identifikator som er knyttet til din wallet, og som gjør det mulig å aktivere ulike funksjoner, inkludert kryptert veksling. Den har form av en identifikator ledsaget av en illustrasjon. Her er for eksempel den jeg bruker på Testnet:



![Image](assets/fr/01.webp)



**For å oppsummere:**





- payjoin" = Spesifikk struktur for samarbeidstransaksjoner;





- `Stowaway` = Payjoin-implementering tilgjengelig på Ashigaru ;





- `Cahoots` = Samourais navn på alle deres typer samarbeidstransaksjoner, spesielt Payjoin `Stowaway`, som i dag er overtatt på Ashigaru ;





- soroban = Kryptert kommunikasjonsprotokoll etablert på Tor som gjør det mulig å samarbeide med andre brukere i en `Cahoots`-transaksjon;





- paynym" = Unik wallet-identifikator som brukes til å opprette kommunikasjon med en annen bruker på "Soroban" for å gjennomføre en "Chahoots"-transaksjon.



Hvis du vil se nærmere på hvordan Payjoins fungerer og hvor nyttige de er i forbindelse med personvern i kjeden, anbefaler jeg denne andre veiledningen:



https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

## Hvordan oppretter jeg en forbindelse mellom Paynyms?



For å komme i gang må du selvfølgelig installere Ashigaru og opprette en :



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

For å gjennomføre en ekstern Cahoots-transaksjon, inkludert en PayJoin (*Stowaway*) via Ashigaru, må du først "følge" brukeren du ønsker å samarbeide med, ved hjelp av deres Paynym. Når det gjelder en blindpassasjer, betyr dette at du må følge personen du ønsker å sende bitcoins til. Hvis du ennå ikke vet hvordan du følger en annen Paynym, finner du den detaljerte prosedyren i denne veiledningen :



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## Hvordan gjør jeg en Payjoin på Ashigaru?



For å gjennomføre en Stowaway-transaksjon klikker du på bildet av Paynym øverst til venstre på skjermen, og deretter åpner du menyen `Collaborate`. Personen som deltar i transaksjonen sammen med deg, må gjøre det samme, med mindre dere utveksler QR-koder ansikt til ansikt.



![Image](assets/fr/02.webp)



Du har to alternativer: Velg `Initiate` hvis du er avsender av betalingen, eller `Participate` hvis du er betalingsmottaker for denne payjoinen.



![Image](assets/fr/03.webp)



Hvis du er mottaker, er prosedyren veldig enkel. For fjernsamarbeid via Soroban-nettverket klikker du på `Delta`, velger kontoen du ønsker å bruke, og trykker deretter på `VENT PÅ FORESPØRSLER OM CAHOOTS` for å avvente forespørselen fra betaleren.



![Image](assets/fr/04.webp)



For personlig samarbeid via QR-kodeskanning går du til startsiden til wallet, trykker på QR-kodeikonet øverst på skjermen og skanner deretter QR-koden fra betaleren som initierer transaksjonen.



![Image](assets/fr/05.webp)



Hvis du har rollen som betaler, dvs. den som initierer transaksjonen, går du til menyen `Collaborate` og velger `Initiate`.



![Image](assets/fr/06.webp)



Siden vi ønsker å foreta en Payjoin Stowaway, velger du dette alternativet for transaksjonstype.



![Image](assets/fr/07.webp)



Deretter kan du velge mellom samarbeid på nettet (*Cahoots* via *Soroban*) eller samarbeid ansikt til ansikt, med utveksling av QR-koder.



![Image](assets/fr/08.webp)



### Cahoots på nett



Hvis du har valgt alternativet `Online`, velger du mottakeren fra Paynyms du følger.



![Image](assets/fr/09.webp)



Klikk på `Sett opp transaksjon`, og velg deretter kontoen du ønsker å foreta utgiften fra.



![Image](assets/fr/10.webp)



På neste side angir du transaksjonsdetaljene: beløpet som skal sendes til mottakeren og gebyrsatsen. Det er ikke nødvendig å oppgi en mottakeradresse, ettersom mottakeren selv vil sende den under PSBT-utvekslinger.



Klikk deretter på `Gjennomgå transaksjonsoppsett`.



![Image](assets/fr/11.webp)



Kontroller informasjonen nøye, sørg for at samarbeidspartneren din lytter til *Cahoots*-forespørsler, og klikk deretter på den grønne "BEGIN TRANSACTION"-knappen for å starte utvekslingen av PSBT-er via Soroban.



![Image](assets/fr/12.webp)



Vent til begge deltakerne har signert transaksjonen, og send den deretter ut på Bitcoin-nettverket.



![Image](assets/fr/13.webp)



### Diskusjoner ansikt til ansikt



Hvis du ønsker å utføre byttet personlig, velger du transaksjonstypen `STONEWALL X2` og deretter alternativet `In Person / Manual`.



![Image](assets/fr/14.webp)



Klikk på `Sett opp transaksjon`, og velg deretter kontoen du ønsker å foreta utgiften fra.



![Image](assets/fr/15.webp)



På neste side angir du transaksjonsdetaljene: beløpet som skal sendes til mottakeren og gebyrsatsen. Det er ikke nødvendig å oppgi en mottakeradresse, ettersom mottakeren selv vil sende den under PSBT-utvekslinger.



Klikk deretter på `Gjennomgå transaksjonsoppsett`.



![Image](assets/fr/16.webp)



Sjekk detaljene, og trykk deretter på den grønne "BEGIN TRANSACTION"-knappen for å begynne å utveksle PSBT-er via QR-kodeskanning.



![Image](assets/fr/17.webp)



Utvekslingen skjer ved å veksle på å skanne med samarbeidspartneren: Klikk på "VIS QR-KODE" for å vise QR-koden din til samarbeidspartneren, som skanner den. Han klikker deretter på "VIS QR-KODE" for å vise sin, og du skanner den med "LANSER QR-SKANNER". Gjenta denne prosessen til alle fem utvekslingstrinnene er fullført.



![Image](assets/fr/18.webp)



Når alle byttene er fullført, kontrollerer du transaksjonsdetaljene og frigjør dem ved å dra i den grønne pilen nederst på skjermen.



![Image](assets/fr/19.webp)



[The transaction has been published](https://mempool.space/testnet4/tx/82efd3700bba87b0f172e9cc045e441b38622c95a60df9f39a21f63eb4590a96). Strukturen er som følger:



![Image](assets/fr/20.webp)



*Kreditt: [mempool.space](https://mempool.space/)*



Hvis vi analyserer denne transaksjonen, ser vi min UTXO på `164 211 sats` på input-siden, samt UTXO på `190 002 sats` som tilhører den faktiske mottakeren av betalingen. På utgangssiden mottar jeg en utvekslings-UTXO på 63 995 sats, mens mottakeren mottar en UTXO på 290 002 sats. Når vi sammenligner input og output, ser vi at mottakeren faktisk har tjent 100 000 sats`, som tilsvarer beløpet på min faktiske betaling, og at jeg har tapt 100 000 sats`, som jeg har lagt til mining-kostnadene.



Jeg kan selvsagt beskrive denne strukturen fordi jeg har bygget transaksjonen selv. Men for en utenforstående observatør er det som regel umulig å avgjøre hvilke UTXO-er som tilhører hvilken deltaker, enten det gjelder innganger eller utganger.



For å utdype kunnskapen din om onchain personvernhåndtering på Bitcoin, anbefaler jeg at du tar BTC 204-opplæringen min på Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c