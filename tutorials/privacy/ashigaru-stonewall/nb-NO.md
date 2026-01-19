---
name: Ashigaru - Stonewall
description: Forståelse og bruk av Stonewall-transaksjoner på Ashigaru
---
![cover stonewall](assets/cover.webp)



> *Bryt forutsetningene for blokkjedeanalyse med matematisk bevisbar tvil mellom avsender og mottaker av transaksjonene dine*

## Hva er en Stonewall-transaksjon?



Stonewall er en spesifikk form for Bitcoin-transaksjon som er utformet for å øke brukernes konfidensialitet når de bruker penger, ved å imitere en coinjoin mellom to personer, uten å faktisk være en. Faktisk er ikke denne transaksjonen et samarbeid. En bruker kan bygge den på egen hånd, kun ved å bruke UTXO-ene han eier som input. Du kan altså opprette en Stonewall-transaksjon til enhver anledning, uten å måtte synkronisere med en annen bruker.



Stonewall-transaksjonen fungerer på følgende måte: Som input til transaksjonen bruker utstederen 2 UTXO som tilhører den. På utgangssiden produserer transaksjonen 4 utganger, hvorav 2 er av nøyaktig samme beløp. De andre 2 vil være utenlandsk valuta. Av de to utgangene med samme beløp vil bare én faktisk gå til betalingsmottakeren.



Det er altså bare to roller i en Stonewall-transaksjon:




- Utstederen, som foretar den faktiske betalingen ;
- Mottakeren, som kanskje ikke er klar over transaksjonens spesifikke natur og bare forventer betaling fra avsenderen.



La oss ta et eksempel for å forstå denne transaksjonsstrukturen. Alice er hos bakeren for å kjøpe baguetten sin, som koster 4000 sats`. Hun ønsker å betale i bitcoins, samtidig som hun opprettholder en form for konfidensialitet rundt betalingen. Så hun bestemmer seg for å lage en Stonewall-transaksjon for betalingen.



![image](assets/fr/01.webp)



Ved å analysere denne transaksjonen kan vi se at bakeren faktisk har mottatt 4 000 sats` som betaling for baguetten. Alice brukte 2 UTXO som input: en på 10 000 sats og en på 15 000 sats. På utgangssiden har det gjenvunnet 3 UTXO: en på 4 000 sats, en på 6 000 sats og en på 11 000 sats. Alice har derfor en nettobalanse på - 4 000 sats` på denne transaksjonen, noe som stemmer godt overens med prisen på baguetten.



I dette eksempelet har jeg med vilje utelatt mining-gebyrene for å gjøre det lettere å forstå. I virkeligheten bæres transaksjonskostnadene i sin helhet av utstederen.



## Hva er forskjellen mellom Stonewall og Stonewall x2?



Stonewall-transaksjonen fungerer på samme måte som StonewallX2-transaksjonen, bortsett fra at sistnevnte krever samarbeid, i motsetning til den klassiske Stonewall-transaksjonen, derav navnet "x2". Stonewall-transaksjonen utføres nemlig uten behov for eksternt samarbeid: Avsenderen kan utføre den uten hjelp fra en annen person. I en Stonewall x2-transaksjon, derimot, blir en ekstra deltaker, en såkalt "collaborator", med i prosessen. Han eller hun bidrar med sine egne bitcoins til transaksjonen, i tillegg til avsenderens bitcoins, og overtar hele beløpet til slutt (modulert med mining-kostnadene).



La oss gå tilbake til eksempelet med Alice på bakeriet. Hvis hun hadde ønsket å gjøre en Stonewall x2-transaksjon, ville Alice ha måttet samarbeide med Bob (en tredjepart) når hun satte opp transaksjonen. De ville ha tatt med seg en UTXO hver. Bob ville da ha fått hele sitt bidrag tilbake. Bakeren ville ha mottatt betaling for baguetten sin på samme måte som i Stonewall-transaksjonen, mens Alice ville ha fått tilbake sin opprinnelige saldo, minus kostnaden for baguetten.



![image](assets/fr/02.webp)



Sett utenfra ville transaksjonen ha forblitt nøyaktig den samme.



![image](assets/fr/03.webp)



For å oppsummere har Stonewall- og Stonewall x2-transaksjoner en identisk struktur. Forskjellen mellom de to ligger i om de er basert på samarbeid eller ikke. Stonewall-transaksjonen utvikles individuelt, uten behov for samarbeid. Stonewall x2-transaksjonen, derimot, er avhengig av samarbeid mellom to personer for å bli satt opp.



[**-> Lær mer om Stonewall-transaksjoner x2**](https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)



## Hva er poenget med en Stonewall-transaksjon?



Stonewall-strukturen tilfører transaksjonen en enorm mengde entropi, noe som gjør det vanskelig å analysere kjeder. Sett fra utsiden kan en slik transaksjon tolkes som en liten coinjoin mellom to personer. Men i virkeligheten er det, i likhet med Stonewall x2-transaksjonen, en betaling. Denne metoden skaper derfor usikkerhet i kjedeanalysen, eller fører til og med til falske spor.



La oss ta eksempelet med Alice hos bakeren. Transaksjonen på blokkjeden ville sett slik ut:



![image](assets/fr/04.webp)



En utenforstående observatør som baserer seg på vanlig heuristikk for kjedeanalyse, kan feilaktig konkludere med at "**to personer har laget en liten coinjoin, med én UTXO hver som input og to UTXO-er hver som output**".



![image](assets/fr/05.webp)



Denne tolkningen er unøyaktig, for som du vet, ble en UTXO sendt til bakeren, de to innkommende UTXO-ene kom fra Alices, og hun gjenvant tre valutakursutganger.



![image](assets/fr/01.webp)



Selv om den utenforstående observatøren klarer å identifisere hvem som er paterne i Stonewall-transaksjonen, vil han ikke ha all informasjonen. Han vil ikke kunne avgjøre hvilken av de to UTXO-ene med samme beløp som tilsvarer betalingen. I tillegg vil han ikke kunne avgjøre om de to UTXO-ene som er lagt inn, er fra to forskjellige personer, eller om de tilhører én og samme person som har slått dem sammen. Dette siste poenget skyldes at Stonewall x2-transaksjonene, som er nevnt ovenfor, følger nøyaktig samme mønster som Stonewall-transaksjonene. Sett utenfra, og uten ytterligere kontekstuell informasjon, er det umulig å se forskjell på en Stonewall-transaksjon og en Stonewall x2-transaksjon. Førstnevnte er ikke samarbeidstransaksjoner, mens sistnevnte er det. Dette bidrar til å skape enda mer tvil om utgiftene.



![image](assets/fr/03.webp)



## Hvordan gjennomfører jeg en Stonewall-transaksjon på Ashigaru?



Stonewall-transaksjoner ble opprinnelig utviklet av Samourai Wallet-teamet, men er nå overtatt av Ashigaru-applikasjonen, en fork av den opprinnelige wallet som ble opprettet etter at Samourai-utviklerne ble arrestert. Du må installere Ashigaru og opprette en wallet:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

I motsetning til Stowaway- eller Stonewall x2-transaksjoner (*cahoots*) krever ikke Stonewall-transaksjoner bruk av Paynyms. De kan utføres direkte, uten forberedelser eller samarbeid med en annen bruker.



Du trenger faktisk ingen opplæring for å gjøre Stonewall-transaksjoner, ettersom Ashigaru genererer dem automatisk hver gang du bruker penger, så snart wallet inneholder nok UTXO-er.



Klikk på knappen `+` nederst til høyre på skjermen, og velg deretter `Send`.



![Image](assets/fr/06.webp)



Velg kontoen du ønsker å bruke penger fra.



![Image](assets/fr/07.webp)



Skriv deretter inn transaksjonsopplysningene: mottakerens adresse og beløpet som skal sendes, og trykk på pilen for å bekrefte.



![Image](assets/fr/08.webp)



Her kan du selvfølgelig justere standard transaksjonsgebyrer i henhold til markedsforholdene. Det mest interessante elementet på denne siden er imidlertid transaksjonstypen. Du vil legge merke til at Ashigaru automatisk har valgt `STONEWALL`. Klikk på knappen "Forhåndsvisning" for å finne ut mer.



![Image](assets/fr/09.webp)



Du kan se at transaksjonen faktisk er av Stonewall-typen: Den består av to innganger med samme beløp, to utganger med samme beløp, samt utvekslingsutgangene og, i mitt tilfelle, en ekstra inngang for å tilfredsstille betalingssummen.



![Image](assets/fr/10.webp)



Hvis du ikke ønsker å foreta en Stonewall-transaksjon, men foretrekker en vanlig betaling, klikker du på blyantikonet øverst til høyre på skjermen, og velger deretter `Simple` i stedet for `STONEWALL`.



![Image](assets/fr/11.webp)



Når du har kontrollert alle detaljene, drar du i den grønne pilen nederst på skjermen for å signere og godkjenne transaksjonen.



![Image](assets/fr/12.webp)



Du vet nå hvordan du utfører en Stonewall-transaksjon, og enda viktigere, hvordan den fungerer. Hvis du vil finne ut mer, kan du ta en titt på veiledningen min på Ashigaru Terminal, som forklarer hvordan du gjør coinjoins via Whirlpool.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add