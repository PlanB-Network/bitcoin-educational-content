---
name: Stonewall
description: Forstå og bruke Stonewall-transaksjoner
---
![cover stonewall](assets/cover.webp)

***ADVARSEL:** Etter arrestasjonen av grunnleggerne av Samourai Wallet og beslagleggelsen av deres servere den 24. april, krever nå bruk av Samourai Wallet-appen en tilkobling til din egen Dojo for å fungere ordentlig. Bortsett fra dette, er Stonewall-transaksjoner ikke påvirket i det hele tatt og kan fortsatt utføres uten problemer. Faktisk utføres disse typene transaksjoner autonomt, uten behov for ekstern samarbeid eller tilkobling via Soroban.*

_Vi følger nøye med på utviklingen av denne saken samt utviklingen angående de tilknyttede verktøyene. Vær trygg på at vi vil oppdatere denne opplæringen etter hvert som ny informasjon blir tilgjengelig._

_Denne opplæringen er gitt kun for utdannings- og informasjonsformål. Vi støtter eller oppmuntrer ikke bruk av disse verktøyene til kriminelle formål. Det er brukerens ansvar å overholde lovene i sin jurisdiksjon._

---

> *"Bryt antakelsene til blockchain-analyse med matematisk beviselig tvil mellom avsender og mottaker av dine transaksjoner."*

## Hva er en Stonewall-transaksjon?
Stonewall er en spesifikk form for Bitcoin-transaksjon rettet mot å øke brukerens personvern under en transaksjon ved å etterligne en coinjoin mellom to parter, uten å faktisk være det. Faktisk er ikke denne transaksjonen samarbeidende. En bruker kan konstruere den alene, kun ved å involvere sine egne UTXOer som inndata. Derfor kan du opprette en Stonewall-transaksjon for enhver anledning uten å måtte koordinere med en annen bruker.

Operasjonen av en Stonewall-transaksjon er som følger: som inndata bruker avsenderen 2 UTXOer som tilhører dem. Som utdata produserer transaksjonen 4 utdata, inkludert 2 som vil være nøyaktig samme beløp. De andre 2 vil være vekslepenger. Blant de 2 utdataene av samme beløp, vil bare én faktisk gå til betalingsmottakeren.

Det er bare 2 roller i en Stonewall-transaksjon:
- Avsenderen, som gjør den faktiske betalingen;
- Mottakeren, som kanskje er uvitende om transaksjonens spesifikke natur og rett og slett forventer en betaling fra avsenderen.

La oss ta et eksempel for å forstå denne transaksjonsstrukturen. Alice er på bakeriet for å kjøpe sin baguette, som koster `4,000 sats`. Hun ønsker å betale i bitcoins samtidig som hun opprettholder et visst nivå av personvern i betalingen sin. Derfor bestemmer hun seg for å opprette en Stonewall-transaksjon for betalingen.
![transaction stonewall bakery](assets/en/1.webp)
Ved å analysere denne transaksjonen, kan vi se at bakeren faktisk mottok `4,000 sats` som betaling for baguetten. Alice brukte 2 UTXOer som inndata: en på `10,000 sats` og en på `15,000 sats`. Som utdata mottok hun 3 UTXOer: en på `4,000 sats`, en på `6,000 sats`, og en på `11,000 sats`. Alice har en netto balanse på `-4,000 sats` i denne transaksjonen, som tilsvarer prisen på baguetten.

I dette eksemplet utelot jeg bevisst gruvegebyrer for å lette forståelsen. I virkeligheten dekkes transaksjonsgebyrer fullt ut av avsenderen.

## Hva er forskjellen mellom Stonewall og Stonewall x2?
Stonewall-transaksjonen fungerer på samme måte som StonewallX2-transaksjonen, med den eneste forskjellen at sistnevnte krever samarbeid, i motsetning til den klassiske Stonewall-transaksjonen, derav betegnelsen "x2". Faktisk kan Stonewall-transaksjonen utføres uten å kreve ekstern samarbeid: avsenderen kan gjennomføre den uten assistanse fra en annen person. Imidlertid, for en Stonewall x2-transaksjon, slutter en ekstra deltaker, kalt "samarbeidspartneren", seg til prosessen. Samarbeidspartneren bidrar med sine egne bitcoins som inndata, sammen med avsenderens, og mottar hele summen som utdata (minus gruvegebyrer).

La oss gjenoppleve vårt eksempel med Alice på bakeriet. Hvis hun hadde ønsket å gjøre en Stonewall x2-transaksjon, måtte Alice ha samarbeidet med Bob (en tredjepart) når transaksjonen ble opprettet. De ville hver ha levert en inndata UTXO. Bob ville deretter ha mottatt det fulle beløpet av sin inndata som utdata. Bakeren ville ha mottatt betaling for sin baguette på samme måte som i Stonewall-transaksjonen, mens Alice ville ha fått tilbake sin opprinnelige saldo, minus kostnaden for baguetten.
![transaksjon stonewall x2](assets/en/2.webp)

Fra et eksternt perspektiv, ville mønsteret av transaksjonen ha forblitt nøyaktig det samme.
![Stonewall eller Stonewall x2 ?](assets/en/3.webp)

Oppsummert deler Stonewall og Stonewall x2-transaksjoner en identisk struktur. Forskjellen mellom de to ligger i deres samarbeidsnatur. Stonewall-transaksjonen er utviklet individuelt, uten behov for samarbeid. I motsetning, Stonewall x2-transaksjonen er avhengig av samarbeid mellom to personer for sin implementering.

[**-> Lær mer om Stonewall x2-transaksjoner**](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)

## Hva er formålet med en Stonewall-transaksjon?
Stonewall-strukturen legger til en betydelig mengde entropi til transaksjonen og skjuler kjedeanalysen. Fra et eksternt perspektiv kan en slik transaksjon tolkes som en liten coinjoin mellom to personer. Men i virkeligheten, akkurat som Stonewall x2-transaksjonen, er det en betaling. Denne metoden skaper derfor usikkerheter i kjedeanalysen, og kan til og med føre til falske spor.

La oss gjenoppleve Alices eksempel på bakeriet. Transaksjonen på blokkjeden ville sett ut som følger:
![Stonewall eller Stonewall x2 ?](assets/en/4.webp)
En ekstern observatør som stoler på vanlige kjedeanalyseheuristikker kunne feilaktig konkludere med at "*to personer har utført en liten coinjoin, med én UTXO hver som inndata og to UTXOer hver som utdata*".
![Stonewall eller Stonewall x2 ?](assets/en/5.webp)
Denne tolkningen er feil fordi, som du vet, en UTXO ble sendt til bakeren, de 2 UTXOene i inndata kommer fra Alice, og hun mottok 3 vekselutdata.

![transaksjon stonewall baker](assets/en/1.webp)
Selv om en utenforstående observatør klarer å identifisere mønsteret til Stonewall-transaksjonen, vil de ikke ha all informasjonen. De vil ikke kunne bestemme hvilken av de to UTXOene med samme beløp som tilsvarer betalingen. Videre vil de ikke kunne bestemme om de to UTXOene i inngangen kommer fra to forskjellige personer eller om de tilhører en enkelt person som har slått dem sammen. Dette siste punktet skyldes det faktum at Stonewall x2-transaksjoner, som vi snakket om ovenfor, følger nøyaktig samme mønster som Stonewall-transaksjoner. Fra utsiden og uten ytterligere informasjon om konteksten, er det umulig å skille en Stonewall-transaksjon fra en Stonewall x2-transaksjon. Imidlertid er de førstnevnte ikke samarbeidstransaksjoner, mens de sistnevnte er det. Dette legger enda flere tvil om denne utgiften.
![Stonewall eller Stonewall x2?](assets/en/3.webp)
## Hvordan gjøre en Stonewall-transaksjon på Samourai Wallet?
I motsetning til Stowaway eller Stonewall x2 (cahoots) transaksjoner, krever ikke Stonewall-transaksjonen bruk av Paynyms. Det kan gjøres direkte, uten noen forberedelsestrinn. For å gjøre dette, følg vår videoveiledning på Samourai Wallet:
![Stonewall Tutorial - Samourai Wallet](https://youtu.be/mlRtZvWGuk0?si=e_lSKJLvybWUna1j)

## Hvordan gjøre en Stonewall-transaksjon på Sparrow Wallet?
I motsetning til Stowaway eller Stonewall x2 (cahoots) transaksjoner, krever ikke Stonewall-transaksjonen bruk av Paynyms. Det kan gjøres direkte, uten noen forberedelsestrinn. For å gjøre dette, følg vår videoveiledning på Sparrow Wallet:
![Stonewall Tutorial - Sparrow Wallet](https://youtu.be/su89ljkV_OI?si=1jNaSJGvECUYe6Or)


**Eksterne Ressurser:**
- https://docs.samourai.io/en/spend-tools#stonewall.