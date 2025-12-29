---
name: Sparrow Wallet - Stonewall
description: Forståelse og bruk av Stonewall-transaksjoner på Sparrow
---

![cover](assets/cover.webp)




> *Bryt forutsetningene for blokkjedeanalyse med matematisk bevisbar tvil mellom avsender og mottaker av transaksjonene dine*

## Hva er en Stonewall-transaksjon?



Stonewall er en spesifikk form for Bitcoin-transaksjon som er utformet for å øke brukernes konfidensialitet når de bruker penger, ved å imitere en coinjoin mellom to personer, uten å faktisk være en. Faktisk er ikke denne transaksjonen et samarbeidsprosjekt. En bruker kan bygge den på egen hånd, kun ved å bruke UTXO-er som tilhører ham som input. Du kan altså opprette en Stonewall-transaksjon til enhver anledning, uten å måtte synkronisere med en annen bruker.



Stonewall-transaksjonen fungerer på følgende måte: Som input til transaksjonen bruker utstederen 2 UTXO som tilhører den. På utgangssiden produserer transaksjonen 4 utganger, hvorav 2 er av nøyaktig samme beløp. De andre 2 vil være utenlandsk valuta. Av de to utgangene med samme beløp vil bare én faktisk gå til betalingsmottakeren.



Det er altså bare to roller i en Stonewall-transaksjon:




- Utstederen, som foretar den faktiske betalingen ;
- Mottakeren, som kanskje ikke er klar over transaksjonens spesifikke natur og bare forventer betaling fra avsenderen.



La oss ta et eksempel for å forstå denne transaksjonsstrukturen. Alice er hos bakeren for å kjøpe baguetten sin, som koster 4 000 sats`. Hun ønsker å betale i bitcoins, samtidig som hun opprettholder en form for konfidensialitet rundt betalingen. Så hun bestemmer seg for å lage en Stonewall-transaksjon for betalingen.



![image](assets/fr/01.webp)



Ved å analysere denne transaksjonen kan vi se at bakeren faktisk har mottatt 4 000 sats` som betaling for baguetten. Alice brukte 2 UTXO-er som input: en på 10 000 sats` og en på 15 000 sats`. På utgangssiden har Alice gjenvunnet 3 UTXO: en på 4 000 sats`, en på 6 000 sats` og en på 11 000 sats`. Alice har derfor en nettobalanse på - 4 000 sats` på denne transaksjonen, noe som stemmer godt overens med prisen på baguetten.



I dette eksempelet har jeg med vilje utelatt mining-gebyrene for å gjøre det lettere å forstå. I virkeligheten bæres transaksjonskostnadene i sin helhet av utstederen.



## Hva er forskjellen mellom Stonewall og Stonewall x2?



Stonewall-transaksjonen fungerer på samme måte som StonewallX2-transaksjonen, bortsett fra at sistnevnte krever samarbeid, i motsetning til den klassiske Stonewall-transaksjonen, derav navnet "x2". Stonewall-transaksjonen utføres nemlig uten behov for eksternt samarbeid: Avsenderen kan utføre den uten hjelp fra en annen person. I en Stonewall x2-transaksjon, derimot, blir en ekstra deltaker, en såkalt "collaborator", med i prosessen. Han eller hun bidrar med sine egne bitcoins til transaksjonen, sammen med avsenderens, og overtar hele beløpet til slutt (minus mining-kostnadene).



La oss gå tilbake til eksempelet med Alice på bakeriet. Hvis hun hadde ønsket å gjøre en Stonewall x2-transaksjon, ville Alice ha måttet samarbeide med Bob (en tredjepart) når hun satte opp transaksjonen. De ville ha tatt med seg en UTXO hver. Bob ville da ha mottatt hele beløpet av sitt bidrag ved exit. Bakeren ville ha mottatt betaling for baguetten sin på samme måte som i Stonewall-transaksjonen, mens Alice ville ha fått tilbake sin opprinnelige saldo, minus kostnaden for baguetten.



![image](assets/fr/02.webp)



Sett utenfra ville transaksjonen ha vært nøyaktig den samme.



![image](assets/fr/03.webp)



For å oppsummere har Stonewall- og Stonewall x2-transaksjoner en identisk struktur. Forskjellen mellom de to ligger i om de er basert på samarbeid eller ikke. Stonewall-transaksjonen utvikles individuelt, uten behov for samarbeid. Stonewall x2-transaksjonen, derimot, er avhengig av samarbeid mellom to personer for å bli satt opp.



[**-> Lær mer om Stonewall-transaksjoner x2**](https://planb.academy/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)



## Hva er poenget med en Stonewall-transaksjon?



Stonewall-strukturen tilfører transaksjonen en enorm mengde entropi, noe som gjør det vanskelig å analysere kjeder. Sett utenfra kan en slik transaksjon tolkes som en liten myntfusjon mellom to personer. Men i virkeligheten er det, i likhet med Stonewall x2-transaksjonen, en betaling. Denne metoden skaper derfor usikkerhet i kjedeanalysen, eller fører til og med til falske spor.



La oss ta eksempelet med Alice hos bakeren. Transaksjonen på blokkjeden ville sett slik ut:



![image](assets/fr/04.webp)



En utenforstående observatør som baserer seg på vanlig heuristikk for kjedeanalyse, kan feilaktig konkludere med at "*to personer har laget en liten coinjoin, med én UTXO hver som input og to UTXO-er hver som output*".



![image](assets/fr/05.webp)



Denne tolkningen er unøyaktig, for som du vet, ble én UTXO sendt til bakeren, de to innkommende UTXO-ene kom fra Alices, og hun gjenvant tre utvekslingsutganger.



![image](assets/fr/01.webp)



Selv om den utenforstående observatøren klarer å identifisere hvem som er paterne i Stonewall-transaksjonen, vil han ikke ha all informasjonen. Han vil ikke kunne avgjøre hvilken av de to UTXO-ene med samme beløp som tilsvarer betalingen. I tillegg vil han ikke kunne avgjøre om de to UTXO-posteringene kommer fra to forskjellige personer, eller om de tilhører én og samme person som har slått dem sammen. Dette siste poenget skyldes at Stonewall x2-transaksjonene, som er nevnt ovenfor, følger nøyaktig samme mønster som Stonewall-transaksjonene. Sett utenfra og uten ytterligere kontekstuell informasjon er det umulig å se forskjell på en Stonewall-transaksjon og en Stonewall x2-transaksjon. Førstnevnte er ikke samarbeidstransaksjoner, mens sistnevnte er det. Dette gjør utgiftene enda mer tvilsomme.



![image](assets/fr/03.webp)



## Hvordan gjennomfører jeg en Stonewall-transaksjon på Sparrow?



Opprinnelig utviklet av Samurai Wallet-teamet, ble Stonewall-transaksjoner overtatt av Ashigaru-applikasjonen, en fork fra den opprinnelige porteføljen som ble opprettet etter arrestasjonen av Samurai-utviklerne, og også på Sparrow Wallet.



Du må installere Sparrow og opprette en :



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

I motsetning til Stowaway- eller Stonewall x2-transaksjoner (*cahoots*) krever ikke Stonewall-transaksjoner bruk av Paynyms. De kan utføres direkte, uten spesielle forberedelser eller samarbeid med en annen bruker.



For å utføre en Stonewall-transaksjon på Sparrow er prosedyren svært enkel: Start med å opprette en transaksjon som vanlig, enten via `Send`-menyen, eller fra `UTXOs`-menyen hvis du ønsker å gjøre *Coin Control*.



![Image](assets/fr/06.webp)



Deretter legger du inn transaksjonsopplysningene: mottakerens adresse, en etikett, beløpet som skal sendes og beløpet eller gebyrsatsen, avhengig av markedsforholdene.



![Image](assets/fr/07.webp)



Før du bekrefter, er det her du kan velge Stonewall-strukturen. Nederst i grensesnittet erstatter du `Efficiency` med `Privacy`. Hvis dette alternativet ikke vises, betyr det at porteføljen din ikke har et tilstrekkelig antall UTXO-er til å bygge denne typen transaksjoner.



![Image](assets/fr/08.webp)



Etter at du har valgt `Privacy`-alternativet, vil du legge merke til at transaksjonens struktur er fullstendig endret: Den blir en Stonewall-transaksjon, som bruker flere av UTXO-ene dine som input og produserer to output med identiske beløp, hvorav det ene tilsvarer den faktiske betalingen på `100 000 sats`, i tillegg til utvekslingsoutputen.



![Image](assets/fr/09.webp)



Hvis alt er i orden, klikker du på "Opprett transaksjon".



Deretter kan du sjekke transaksjonsdetaljene dine en siste gang, og klikke på "Fullfør transaksjon for signering".



![Image](assets/fr/10.webp)



Signer deretter transaksjonen i henhold til metoden som er spesifikk for din portefølje, og klikk på `Broadcast Transaction` for å kringkaste den på Bitcoin-nettverket, i påvente av bekreftelse.



![Image](assets/fr/11.webp)



Du vet nå hvordan en Stonewall-transaksjon fungerer på Sparrow Wallet og hvordan du oppretter en. For å utdype din mestring av disse verktøyene som er designet for å styrke konfidensialiteten din i kjeden, inviterer jeg deg til å følge BTC 204-opplæringen min på Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c