---
name: Ashigaru - Stonewall x2
description: Forståelse og bruk av Stonewall x2-transaksjoner på Ashigaru
---
![cover stonewall x2](assets/cover.webp)



> *Gjør hvert forbruk til en coinjoin

## Hva er en Stonewall x2-transaksjon?



Stonewall x2 er en spesifikk form for Bitcoin-transaksjon som er utformet for å øke brukernes konfidensialitet når de bruker penger, ved å samarbeide med en tredjepart som ikke er involvert i utgiftene. Denne metoden simulerer en mini-coinjoin mellom to deltakere, samtidig som det foretas en betaling til en tredjepart. Stonewall x2-transaksjoner er tilgjengelige i Ashigaru-applikasjonen, en fork fra Samourai Wallet (teamet som står bak opprettelsen av denne typen transaksjoner).



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Det fungerer relativt enkelt: Du bruker en UTXO som du har i din besittelse til å utføre betalingen, og får hjelp av en tredjepart som også bidrar med en egen UTXO. Transaksjonen ender opp med fire utganger: to av dem med like store beløp, den ene til betalingsmottakerens adresse, den andre til en adresse som tilhører samarbeidspartneren. En tredje UTXO returneres til en annen adresse som tilhører samarbeidspartneren, slik at han kan få tilbake det opprinnelige beløpet (en nøytral handling for ham, modulert med mining-kostnadene), og en siste UTXO returneres til en adresse som tilhører oss, noe som utgjør betalingsutvekslingen.



I Stonewall x2-transaksjonene er det altså definert tre ulike roller:




- Utstederen, som foretar den faktiske betalingen ;
- Samarbeidspartneren, som gjør bitcoins tilgjengelig for å forbedre anonymiteten til transaksjonen, samtidig som han får tilbake pengene sine i sin helhet på slutten (en nøytral handling for ham, modulert med mining-kostnadene);
- Mottakeren, som kanskje ikke er klar over transaksjonens spesifikke natur og bare forventer betaling fra avsenderen.



La oss ta et eksempel. Alice er hos bakeren for å kjøpe baguetten sin, som koster 4000 sats`. Hun ønsker å betale i bitcoins, samtidig som hun ønsker å holde betalingen konfidensiell. Hun ringer derfor sin venn Bob, som vil hjelpe henne med dette.



![image](assets/fr/01.webp)



Når vi analyserer denne transaksjonen, ser vi at bakeren faktisk mottok 4 000 sats` som betaling for baguetten. Alice brukte 10 000 sats` i input og fikk tilbake 6 000 sats` i output, noe som gir en nettobalanse på 4 000 sats`, som tilsvarer prisen på baguetten. Bob leverte 15 000 sats` i input og mottok to outputs: en på 4 000 sats` og en på 11 000 sats`, noe som gir en balanse på 0`.



I dette eksempelet har jeg med vilje utelatt mining-gebyrene for å gjøre det enklere å forstå. I virkeligheten deles transaksjonsgebyrene likt mellom betalingsutstederen og samarbeidspartneren.



## Hva er forskjellen mellom Stonewall og Stonewall x2?



En Stonewall X2-transaksjon fungerer på nøyaktig samme måte som en Stonewall-transaksjon, bortsett fra at førstnevnte er kollaborativ, mens sistnevnte ikke er det. Som vi har sett, involverer en Stonewall X2-transaksjon deltakelse fra en tredjepart som står utenfor betalingen, og som stiller sine bitcoins til rådighet for å øke konfidensialiteten i transaksjonen. I en klassisk Stonewall-transaksjon er det avsenderen som tar på seg rollen som samarbeidspartner.



La oss gå tilbake til eksempelet med Alice på bakeriet. Hvis hun ikke hadde klart å finne noen som Bob til å bli med henne på forbruksturen, kunne hun ha gjort en Stonewall på egen hånd. På den måten ville de to UTXO-ene på vei inn ha vært hennes, og hun ville ha plukket opp tre på vei ut.



![image](assets/fr/02.webp)




Sett utenfra ville transaksjonen ha forblitt den samme.



![image](assets/fr/05.webp)



Logikken bør derfor være som følger når du ønsker å bruke et Ashigaru-utgiftsverktøy:




- Hvis forhandleren ikke støtter Payjoin Stowaway, kan du foreta en samarbeidstransaksjon med en annen person utenfor betalingen takket være Stonewall x2 ;
- Hvis du ikke finner noen som kan foreta en Stonewall x2-transaksjon, kan du foreta en Stonewall only-transaksjon, som vil etterligne oppførselen til en Stonewall x2-transaksjon.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-033daa45-d42c-40e1-9511-cea89751c3d4

## Hva er poenget med en Stonewall x2-transaksjon?



Stonewall x2-strukturen tilfører transaksjonen en enorm mengde entropi, noe som forvirrer kjedeanalysen. Sett utenfra kan en slik transaksjon tolkes som en liten Coinjoin mellom to personer. Men i virkeligheten er det en betaling. Denne metoden skaper derfor usikkerhet i kjedeanalysen, eller fører til og med til falske spor.



La oss ta eksemplet med Alice, Bob og Boulanger. Transaksjonen på blokkjeden vil se slik ut:



![image](assets/fr/03.webp)



En utenforstående observatør som baserer seg på vanlig kjedeanalyseheuristikk, kan feilaktig konkludere med at "*Alice og Bob har gjort en liten coinjoin, med én UTXO hver inn og to UTXO-er hver ut*".



![image](assets/fr/04.webp)



Denne tolkningen er feil, for som du vet, ble en UTXO sendt til Boulanger, Alice har bare én utvekslingsutgang, og Bob har to.



![image](assets/fr/01.webp)



Selv om den utenforstående observatøren klarer å identifisere hvem som er oppdragsgiver for Stonewall x2-transaksjonen, vil han ikke ha all informasjonen. Han vil ikke kunne avgjøre hvilken av de to UTXO-ene med samme beløp som tilsvarer betalingen. Han vil heller ikke kunne avgjøre om det var Alice eller Bob som foretok betalingen. Til slutt vil han ikke kunne avgjøre om de to UTXO-ene som er lagt inn, er fra to forskjellige personer, eller om de tilhører én og samme person som har slått dem sammen. Dette siste poenget skyldes det faktum at de klassiske Stonewall-transaksjonene, som er omtalt ovenfor, følger nøyaktig samme mønster som Stonewall x2-transaksjonene. Sett utenfra og uten ytterligere kontekstuell informasjon er det umulig å skille en Stonewall-transaksjon fra en Stonewall x2-transaksjon. Førstnevnte er ikke samarbeidstransaksjoner, mens sistnevnte er det. Dette bidrar til å skape enda mer tvil om utgiften.



![image](assets/fr/05.webp)




## Hvordan oppretter jeg en forbindelse mellom Paynyms?



Som med andre samarbeidstransaksjoner på Ashigaru (*Cahoots*), innebærer Stonewall x2 utveksling av delvis signerte transaksjoner mellom avsenderen og samarbeidspartneren. Denne utvekslingen kan utføres manuelt, hvis du er fysisk til stede sammen med samarbeidspartneren din, eller automatisk ved hjelp av Soroban-kommunikasjonsprotokollen.



Hvis du velger det andre alternativet, må du opprette en forbindelse mellom Paynymene før du kan utføre en Stonewall x2. For å gjøre dette må din Paynym "*følge*" din samarbeidspartners Paynym, og vice versa. For å finne ut hvordan du gjør dette, kan du følge begynnelsen av denne andre veiledningen:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## Hvordan gjør jeg en Stonewall x2-transaksjon på Ashigaru?



For å gjennomføre en Stonewall x2-transaksjon klikker du på bildet av Paynym øverst til venstre på skjermen, og åpner deretter menyen `Collaborate`. Personen som deltar i transaksjonen sammen med deg, må gjøre det samme, med mindre dere utveksler QR-koder ansikt til ansikt.



![Image](assets/fr/06.webp)



Du har to alternativer: Velg `Initiate` hvis du er avsender av betalingen, eller `Participate` hvis du er den personen som samarbeider i transaksjonen, men verken er betaler eller mottaker.



![Image](assets/fr/07.webp)



Hvis du har rollen som samarbeidspartner, er prosedyren svært enkel. For fjernsamarbeid via Soroban-nettverket klikker du på `Delta`, velger kontoen du ønsker å bruke, og trykker deretter på `VENT PÅ FORESPØRSLER OM CAHOOTS` for å vente på forespørselen fra betaleren.



![Image](assets/fr/08.webp)



For personlig samarbeid via QR-kodeskanning går du til startsiden til wallet, trykker på QR-kodeikonet øverst på skjermen og skanner deretter QR-koden fra betaleren som initierer transaksjonen.



![Image](assets/fr/09.webp)



Hvis du har rollen som betaler, dvs. den som initierer transaksjonen, går du til menyen `Collaborate` og velger `Initiate`.



![Image](assets/fr/10.webp)



Siden vi ønsker å utføre en Stonewall x2, velger du dette alternativet for transaksjonstypen.



![Image](assets/fr/11.webp)



Deretter kan du velge mellom samarbeid på nettet (*Cahoots* via *Soroban*) eller samarbeid ansikt til ansikt, med utveksling av QR-koder.



![Image](assets/fr/12.webp)



### Cahoots på nett



Hvis du har valgt alternativet `Online`, velger du samarbeidspartneren din fra Paynyms du følger.



![Image](assets/fr/13.webp)



Klikk på `Sett opp transaksjon`, og velg deretter kontoen du ønsker å foreta utgiften fra.



![Image](assets/fr/14.webp)



På neste side angir du transaksjonsdetaljene: adressen til den faktiske mottakeren av betalingen, beløpet som skal sendes og gebyrsatsen. Klikk deretter på "Gjennomgå transaksjonsoppsett".



![Image](assets/fr/15.webp)



Kontroller informasjonen nøye, sørg for at samarbeidspartneren din lytter til *Cahoots*-forespørsler, og klikk deretter på den grønne "BEGIN TRANSACTION"-knappen for å starte utvekslingen av PSBT-er via Soroban.



![Image](assets/fr/16.webp)



Vent til begge deltakerne har signert transaksjonen, og send den deretter ut i Bitcoin-nettverket.



![Image](assets/fr/17.webp)



### Diskusjoner ansikt til ansikt



Hvis du ønsker å utføre byttet personlig, velger du transaksjonstypen `STONEWALL X2` og deretter alternativet `In Person / Manual`.



![Image](assets/fr/18.webp)



Klikk på `Sett opp transaksjon`, og velg deretter kontoen du ønsker å foreta utgiften fra.



![Image](assets/fr/19.webp)



På neste side angir du transaksjonsdetaljene: adressen til den faktiske mottakeren av betalingen, beløpet som skal sendes og gebyrsatsen. Klikk deretter på "Gjennomgå transaksjonsoppsett".



![Image](assets/fr/20.webp)



Sjekk detaljene, og trykk deretter på den grønne "BEGIN TRANSACTION"-knappen for å begynne å utveksle PSBT-er via QR-kodeskanning.



![Image](assets/fr/21.webp)



Utvekslingen skjer ved å veksle på å skanne med samarbeidspartneren: Klikk på "VIS QR-KODE" for å vise QR-koden din til samarbeidspartneren, som skanner den. Han klikker deretter på "VIS QR-KODE" for å vise sin, og du skanner den med "LANSER QR-SKANNER". Gjenta denne prosessen til alle fem utvekslingstrinnene er fullført.



![Image](assets/fr/22.webp)



Når alle byttene er fullført, kontrollerer du transaksjonsdetaljene og frigjør dem ved å dra i den grønne pilen nederst på skjermen.



![Image](assets/fr/23.webp)



[The transaction has been published](https://mempool.space/testnet4/tx/9082f3d989728aacd290535a1ac374ab8c04a241a1d798b378db626dabea7a24). Strukturen er som følger:



![Image](assets/fr/24.webp)



*Kreditt: [mempool.space](https://mempool.space/)*



Vi kan observere to inndata fra min portefølje, henholdsvis 91 869 sats og 64 823 sats, mens de to andre inndataene kommer fra min samarbeidspartners wallet. På utgangssiden sendes en UTXO på 100 000 sats` til den faktiske betalingsmottakeren, og to UTXO-er på 100 000 sats` og 159 578 sats` går tilbake til min samarbeidspartners portefølje. For ham er operasjonen nøytral, ettersom han får tilbake hele beløpet han hadde investert i inndata (unntatt mining-kostnadene som han bidro til). Til slutt mottar jeg en utveksling UTXO på 56 270 sats`, som tilsvarer differansen mellom min totale innsats og betalingen på 100 000 sats` som ble sendt til mottakeren.



Jeg kan selvsagt beskrive denne strukturen fordi jeg har bygget transaksjonen selv. Men for en utenforstående observatør er det som regel umulig å avgjøre hvilke UTXO-er som tilhører hvilken deltaker, enten det gjelder innganger eller utganger.



For å utdype kunnskapen din om onchain personvernhåndtering på Bitcoin, anbefaler jeg at du tar BTC 204-opplæringen min på Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c