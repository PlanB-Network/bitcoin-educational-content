---
name: Coinjoin - Dojo
description: Hvordan utføre en coinjoin med din egen Dojo?
---
![cover](assets/cover.webp)

***ADVARSEL:** Etter arrestasjonen av grunnleggerne av Samourai Wallet og beslagleggelsen av deres servere den 24. april, fungerer ikke lenger Whirlpool-verktøyet, selv for personer som har sin egen Dojo eller bruker Sparrow Wallet. Det er imidlertid mulig at dette verktøyet kan bli gjeninnført i de kommende ukene eller relansert på en annen måte. Videre forblir den teoretiske delen av denne artikkelen relevant for å forstå prinsippene og målene med coinjoins generelt (ikke bare Whirlpool), samt forstå effektiviteten av Whirlpool-modellen.*

_Vi følger nøye med på utviklingen av denne saken samt utviklingen angående de tilknyttede verktøyene. Vær trygg på at vi vil oppdatere denne opplæringen etter hvert som ny informasjon blir tilgjengelig._

_Denne opplæringen er gitt kun til utdannings- og informasjonsformål. Vi støtter eller oppmuntrer ikke bruk av disse verktøyene til kriminelle formål. Det er brukerens ansvar å overholde lovene i sin jurisdiksjon._

---

I denne opplæringen vil du lære hva en coinjoin er og hvordan du utfører en ved hjelp av Samourai Wallet-programvaren og Whirlpool-implementeringen, ved å bruke din egen Dojo. Etter min mening er denne metoden for øyeblikket den beste for å blande dine bitcoins.

## Hva er en coinjoin på Bitcoin?
**En coinjoin er en teknikk som bryter sporbarheten til bitcoins på blockchain**. Den stoler på en samarbeidstransaksjon med en spesifikk struktur med samme navn: coinjoin-transaksjonen.

Coinjoins forbedrer personvernet til Bitcoin-brukere ved å komplisere kjedeanalyse for eksterne observatører. Deres struktur tillater sammenslåing av flere mynter fra forskjellige brukere i en enkelt transaksjon, noe som gjør det vanskelig å bestemme koblingene mellom inngangs- og utgangsadresser.

Prinsippet med coinjoin er basert på en samarbeidstilnærming: flere brukere som ønsker å blande sine bitcoins, setter inn identiske beløp som innganger i samme transaksjon. Disse beløpene blir deretter redistribuert som utganger av lik verdi til hver bruker. Ved slutten av transaksjonen blir det umulig å knytte en spesifikk utgang til en kjent bruker ved inngangen. Ingen direkte kobling eksisterer mellom inngangene og utgangene, noe som bryter tilknytningen mellom brukerne og deres UTXO, samt historikken til hver mynt.
![coinjoin](assets/notext/1.webp)

Eksempel på en coinjoin-transaksjon (ikke fra meg): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)

For å utføre en coinjoin samtidig som hver bruker opprettholder kontroll over sine midler til enhver tid, begynner prosessen med at transaksjonen blir konstruert av en koordinator, som deretter overfører den til deltakerne. Hver bruker signerer deretter transaksjonen etter å ha verifisert at den passer for dem. Alle innsamlede signaturer blir til slutt integrert i transaksjonen. Hvis et forsøk på å avlede midler blir gjort av en bruker eller koordinatoren, gjennom en modifikasjon av coinjoin-transaksjonens utganger, vil signaturene vise seg å være ugyldige, noe som fører til at transaksjonen avvises av nodene.

Det finnes flere implementeringer av coinjoin, som Whirlpool, JoinMarket, eller Wabisabi, hver med mål om å håndtere koordinering blant deltakere og øke effektiviteten av coinjoin-transaksjoner.
I denne veiledningen skal vi dykke ned i implementeringen av **Whirlpool**, som jeg anser for å være den mest effektive løsningen for å utføre coinjoins på Bitcoin. Selv om det er tilgjengelig på flere lommebøker, vil vi i denne veiledningen utelukkende utforske bruken av det med Samourai Wallet mobilapplikasjonen, uten Dojo.
## Hvorfor utføre coinjoins på Bitcoin?
Et av de første problemene med ethvert peer-to-peer betalingssystem er dobbeltutgifter: hvordan forhindre at ondsinnede individer bruker de samme pengeenhetene flere ganger uten å måtte ty til en sentral autoritet for å megle?

Satoshi Nakamoto tilbød en løsning på dette dilemmaet gjennom Bitcoin-protokollen, et peer-to-peer elektronisk betalingssystem som opererer uavhengig av enhver sentral autoritet. I hans hvitbok understreker han at den eneste måten å sertifisere fraværet av dobbeltutgifter på, er å sikre synligheten av alle transaksjoner innen betalingssystemet.

For å sikre at hver deltaker er klar over transaksjonene, må de offentliggjøres. Derfor er driften av Bitcoin avhengig av en transparent og distribuert infrastruktur, som tillater enhver nodoperatør å verifisere helheten av de elektroniske signaturkjedene og historikken til hver mynt, fra dens skapelse av en miner.

Den transparente og distribuerte naturen til Bitcoins blockchain betyr at enhver bruker av nettverket kan følge og analysere transaksjonene til alle andre deltakere. Som et resultat er anonymitet på transaksjonsnivå umulig. Imidlertid bevares anonymiteten på individnivå. I motsetning til det tradisjonelle banksystemet hvor hver konto er knyttet til en personlig identitet, er midler på Bitcoin assosiert med par av kryptografiske nøkler, og tilbyr dermed brukerne en form for pseudonymitet bak kryptografiske identifikatorer.

Således blir konfidensialiteten på Bitcoin kompromittert når eksterne observatører klarer å assosiere spesifikke UTXOer med identifiserte brukere. Når denne assosiasjonen er etablert, blir det mulig å spore deres transaksjoner og analysere historikken til deres bitcoins. Coinjoin er nettopp en teknikk utviklet for å bryte sporebarheten til UTXOer, og dermed tilby et visst lag av konfidensialitet til Bitcoin-brukere på transaksjonsnivå.

## Hvordan fungerer Whirlpool?
Whirlpool skiller seg ut fra andre coinjoin-metoder ved å bruke "_ZeroLink_" transaksjoner, som sikrer at det strengt tatt ikke er mulig med en teknisk kobling mellom alle inngangene og alle utgangene. Denne perfekte blandingen oppnås gjennom en struktur hvor hver deltaker bidrar med et identisk beløp i inngang (unntatt for miningavgifter), og dermed genererer utganger av perfekt like beløp.
Denne restriktive tilnærmingen til innganger gir Whirlpool coinjoin-transaksjoner en unik egenskap: den komplette fraværet av deterministiske koblinger mellom inngangene og utgangene. Med andre ord, hver utgang har en lik sannsynlighet for å bli tilskrevet enhver deltaker, sammenlignet med alle de andre utgangene i transaksjonen.
Opprinnelig var antallet deltakere i hver Whirlpool coinjoin begrenset til 5, med 2 nye deltakere og 3 remixere (vi vil forklare disse konseptene videre). Imidlertid førte økningen i on-chain transaksjonsgebyrer observert i 2023 til at Samourai-teamene måtte revurdere modellen sin for å forbedre personvernet samtidig som kostnadene reduseres. Således, med tanke på markedsituasjonen for gebyrer og antall deltakere, kan koordinatoren nå organisere coinjoins inkludert 6, 7, eller 8 deltakere. Disse forbedrede øktene refereres til som "_Surge Cycles_". Det er viktig å merke seg at, uavhengig av oppsettet, er det alltid bare 2 nye deltakere i Whirlpool coinjoins.

Således er Whirlpool-transaksjoner kjennetegnet ved et identisk antall innganger og utganger, som kan være:
- 5 innganger og 5 utganger;
![coinjoin](assets/notext/2.webp)
- 6 innganger og 6 utganger;
![coinjoin](assets/notext/3.webp)
- 7 innganger og 7 utganger;
![coinjoin](assets/notext/4.webp)- 8 innganger og 8 utganger.
![coinjoin](assets/notext/5.webp)
Modellen foreslått av Whirlpool er dermed basert på små coinjoin-transaksjoner. I motsetning til Wasabi og JoinMarket, hvor robustheten av anonsets er avhengig av volumet av deltakere i en enkelt syklus, satser Whirlpool på kjeding av flere små sykluser.

I denne modellen betaler brukeren avgifter kun ved deres første inngang i en pool, noe som tillater dem å delta i en mengde remixes uten ekstra avgifter. Det er de nye deltakerne som dekker mining-avgiftene for remixerne.

Med hver tilleggs coinjoin som en mynt deltar i, sammen med sine tidligere møtte peers, vil anonsets vokse eksponentielt. Målet er dermed å dra nytte av disse gratis remixene som, ved hver forekomst, bidrar til å øke tettheten av anonsets assosiert med hver blandet mynt.

Whirlpool ble designet med tanke på to viktige krav:
- Tilgjengeligheten av implementering på mobile enheter, gitt at Samourai Wallet primært er en smarttelefonapplikasjon;
- Hastigheten på remixing-sykluser for å fremme en betydelig økning i anonsets.
Disse imperativene veiledet utviklerne av Samourai Wallet i designet av Whirlpool, noe som førte dem til å begrense antallet deltakere per syklus. For få deltakere ville ha kompromittert effektiviteten av coinjoin, drastisk redusert anonsets generert hver syklus, mens for mange deltakere ville ha utgjort forvaltningsproblemer på mobile applikasjoner og ville ha hindret flyten av sykluser.
**Til syvende og sist er det ikke nødvendig å ha et høyt antall deltakere per coinjoin på Whirlpool siden anonsets oppnås gjennom akkumulering av flere coinjoin-sykluser.**

[-> Lær mer om Whirlpool anonsets.](https://planb.network/tutorials/privacy/wst-anonsets)

### Poolene og coinjoin-avgifter
For at disse flere syklusene effektivt skal øke anonsets av de blandete myntene, må et visst rammeverk etableres for å begrense mengdene av UTXO som brukes. Whirlpool definerer dermed forskjellige pooler.

En pool representerer en gruppe brukere som ønsker å blande sammen, som er enige om mengden UTXO å bruke for å optimalisere coinjoin-prosessen. Hver pool spesifiserer et fast beløp for UTXO, som brukeren må overholde for å delta. Således, for å utføre coinjoins med Whirlpool, må du velge en pool. Poolene som for øyeblikket er tilgjengelige er som følger:
- 0,5 bitcoins;
- 0,05 bitcoin;
- 0,01 bitcoin;
- 0,001 bitcoin (= 100 000 sats).

Ved å bli med i en pool med dine bitcoins, vil de bli delt for å generere UTXOs som er perfekt homogene med de til de andre deltakerne i poolen. Hver pool har en maksimal grense; dermed, for beløp som overstiger denne grensen, vil du bli tvunget enten til å gjøre to separate innganger innenfor samme pool eller å flytte til en annen pool med et høyere beløp:

| Pool (bitcoin) | Maksimalt beløp per inngang (bitcoin) |
|----------------|---------------------------------------|
| 0,5            | 35                                    |
| 0,05           | 3,5                                   |
| 0,01           | 0,7                                   |
| 0,001          | 0,025                                 |
Som nevnt tidligere, anses en UTXO å tilhøre en pool når den er klar til å integreres i en coinjoin. Dette betyr imidlertid ikke at brukeren mister besittelsen av den. **Gjennom de forskjellige mikse-syklusene beholder du full kontroll over nøklene dine og, som en konsekvens, dine bitcoins.** Dette er det som skiller coinjoin-teknikken fra andre sentraliserte mikseteknikker.

For å delta i en coinjoin-pool, må tjenesteavgifter samt miningavgifter betales. Tjenesteavgiftene er faste for hver pool og er ment å kompensere teamene ansvarlig for utvikling og vedlikehold av Whirlpool.
Tjenesteavgifter for å bruke Whirlpool betales kun én gang ved inngangen til poolen. Etter dette trinnet har du muligheten til å delta i et ubegrenset antall remikser uten noen ekstra avgifter. Her er de nåværende faste avgiftene for hver pool:

| Pool (bitcoin) | Inngangsavgift (bitcoin) |
|----------------|-------------------------|
| 0.5            | 0.0175                  |
| 0.05           | 0.00175                 |
| 0.01           | 0.0005 (50,000 sats)    |
| 0.001          | 0.00005 (5,000 sats)    |


Disse avgiftene fungerer i hovedsak som en inngangsbillett for den valgte poolen, uavhengig av beløpet du legger i coinjoin. Så, enten du blir med i 0.01-poolen med nøyaktig 0.01 BTC eller går inn i den med 0.5 BTC, vil avgiftene forbli de samme i absolutt verdi.

Før man går videre til coinjoins, har brukeren derfor et valg mellom 2 strategier:
- Velge en mindre pool for å minimere tjenesteavgifter, vel vitende om at de vil motta flere små UTXOer i retur;
- Eller foretrekke en større pool, samtykke til å betale høyere avgifter for å ende opp med et redusert antall UTXOer med større verdi.

Det anbefales generelt å ikke slå sammen flere miksete UTXOer etter coinjoin-syklusene, da dette kan kompromittere den oppnådde konfidensialiteten, spesielt på grunn av Common-Input-Ownership Heuristic (CIOH). Derfor kan det være lurt å velge en større pool, selv om det betyr å betale mer, for å unngå å ha for mange småverdi-UTXOer ved utgangen. Brukeren må veie disse avveiningene for å velge den poolen de foretrekker.

I tillegg til tjenesteavgifter, må også miningavgifter som er iboende i enhver Bitcoin-transaksjon, vurderes. Som Whirlpool-bruker vil du være nødt til å betale miningavgiftene for forberedelsestransaksjonen (`Tx0`) samt de for den første coinjoin. Alle påfølgende remikser vil være gratis, takket være Whirlpools modell som stoler på betalingen fra nye deltakere.

Faktisk, i hver Whirlpool coinjoin, er to brukere blant inngangene nye deltakere. De andre inngangene kommer fra remiksere. Som et resultat, dekkes miningavgiftene for alle deltakerne i transaksjonen av disse to nye deltakerne, som da også vil dra nytte av gratis remikser:
![coinjoin](assets/en/6.webp)
Takket være dette avgiftssystemet, skiller Whirlpool seg virkelig ut fra andre coinjoin-tjenester siden anonsettene til UTXOene ikke er proporsjonale med prisen betalt av brukeren. Således er det mulig å oppnå betydelig høye nivåer av anonymitet ved kun å betale inngangsavgiften til poolen og miningavgiftene for to transaksjoner (den `Tx0` og den første miksen).
Det er viktig å merke seg at brukeren også må dekke gruvegebyrene for å ta ut sine UTXOs fra bassenget etter å ha fullført flere coinjoins, med mindre de har valgt `mix to`-alternativet, som vi vil diskutere i opplæringen nedenfor.
### HD-lommebokkontoene som brukes av Whirlpool
For å utføre en coinjoin via Whirlpool, må lommeboken generere flere distinkte kontoer. En konto, i konteksten av en HD (*Hierarchical Deterministic*) lommebok, utgjør en seksjon som er helt isolert fra de andre, denne separasjonen skjer på det tredje dybdenivået i lommebokens hierarki, det vil si på nivået av `xpub`.

En HD-lommebok kan teoretisk avlede opp til `2^(32/2)` forskjellige kontoer. Den opprinnelige kontoen, som brukes som standard på alle Bitcoin-lommebøker, tilsvarer indeksen `0'`.

For lommebøker tilpasset Whirlpool, som Samourai eller Sparrow, brukes 4 kontoer for å møte behovene til coinjoin-prosessen:
- **Innskudds**kontoen, identifisert ved indeksen `0'`;
- **Dårlig bank** (eller doxxic change) kontoen, identifisert ved indeksen `2 147 483 644'`;
- **Premix**-kontoen, identifisert ved indeksen `2 147 483 645'`;
- **Postmix**-kontoen, identifisert ved indeksen `2 147 483 646'`.

Hver av disse kontoene oppfyller en spesifikk funksjon innenfor coinjoin.

Alle disse kontoene er knyttet til et enkelt frø, som lar brukeren gjenopprette tilgang til alle sine bitcoins ved hjelp av sin gjenopprettingsfrase og, om nødvendig, deres passfrase. Det er imidlertid nødvendig å spesifisere til programvaren, under denne gjenopprettingsoperasjonen, de forskjellige kontoindeksene som ble brukt.

La oss nå se på de forskjellige stadiene av en Whirlpool coinjoin innenfor disse kontoene.

### De forskjellige stadiene av coinjoins på Whirlpool
**Steg 1: Tx0**
Utgangspunktet for enhver Whirlpool coinjoin er **innskudds**kontoen. Denne kontoen er den du automatisk bruker når du oppretter en ny Bitcoin-lommebok. Denne kontoen må krediteres med bitcoins som man ønsker å blande.
`Tx0` representerer det første steget i Whirlpool-blandingsprosessen. Målet er å forberede og likestille UTXO for coinjoin, ved å dele dem inn i enheter som tilsvarer mengden av det valgte bassenget, for å sikre homogeniteten av blandingen. De likestilte UTXOene sendes deretter til **premix**-kontoen. Når det gjelder differansen som ikke kan gå inn i bassenget, blir den skilt ut i en spesifikk konto: **dårlig bank** (eller "doxxic change").
Denne innledende transaksjonen `Tx0` tjener også til å avregne tjenestegebyrene til mix-koordinatoren. I motsetning til de følgende trinnene, er denne transaksjonen ikke samarbeidsvillig; brukeren må derfor bære alle gruvegebyrene:
![coinjoin](assets/en/7.webp)

I dette eksemplet på en `Tx0`-transaksjon, deles et innskudd på `372,000 sats` fra vår **innskudds**konto inn i flere utgående UTXO, som er fordelt som følger:
- Et beløp på `5,000 sats` ment for koordinatoren for tjenestegebyrer, som tilsvarer inngangen til bassenget på `100,000 sats`;
- Tre UTXO forberedt for blanding, omdirigert til vår **premix**-konto og registrert med koordinatoren. Disse UTXOene er likestilt på `108,000 sats` hver, for å dekke gruvegebyrene for deres fremtidige innledende miks;
- Overskuddet som ikke kan gå inn i bassenget, fordi det er for lite, anses som giftig vekslepenger. Det blir sendt til sin spesifikke konto. Her utgjør denne endringen `40 000 sats`;
- Til slutt er det `3 000 sats` som ikke utgjør en utgang, men er gruvegebyrene som er nødvendige for å bekrefte `Tx0`.

For eksempel, her er en ekte Whirlpool Tx0 (ikke fra meg): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)

**Steg 2: Den giftige vekslepengene**
Overskuddet som ikke kunne integreres i bassenget, her tilsvarende `40 000 sats`, blir omdirigert til **dårlig bank**-kontoen, også referert til som "giftig vekslepenger", for å sikre en streng separasjon fra de andre UTXO i lommeboken.

Denne UTXO er farlig for brukerens personvern fordi den ikke bare fortsatt er knyttet til sin fortid, og derfor muligens til eierens identitet, men i tillegg er den notert som tilhørende en bruker som har utført en coinjoin.
Hvis denne UTXO blir slått sammen med blandete utganger, vil de miste all konfidensialiteten oppnådd under coinjoin-syklusene, spesielt på grunn av Common-Input-Ownership-Heuristic (CIOH). Hvis den slås sammen med andre giftige vekslepenger, risikerer brukeren å miste konfidensialitet siden dette vil koble de forskjellige inngangene fra coinjoin-syklusene. Derfor må den håndteres med forsiktighet. Måten å håndtere denne giftige UTXO på vil bli detaljert i den siste delen av denne artikkelen, og fremtidige veiledninger vil dekke disse metodene mer grundig på PlanB Network.

**Steg 3: Den første blandingen**
Etter at `Tx0` er fullført, blir de likestilte UTXOene sendt til **premix**-kontoen i lommeboken vår, klare til å bli introdusert i deres første coinjoin-syklus, også kalt "den første blandingen". Hvis, som i vårt eksempel, `Tx0` genererer flere UTXOer beregnet for blanding, vil hver av dem bli integrert i en separat første coinjoin.

Ved slutten av disse første blandingene, vil **premix**-kontoen være tom, mens myntene våre, etter å ha betalt gruvegebyrene for denne første coinjoin, vil bli justert nøyaktig til beløpet definert av det valgte bassenget. I vårt eksempel vil våre opprinnelige UTXOer på `108 000 sats` ha blitt redusert til nøyaktig `100 000 sats`.
![coinjoin](assets/en/8.webp)
**Steg 4: Remixene**
Etter den første blandingen, blir UTXOene overført til **postmix**-kontoen. Denne kontoen samler de allerede blandete UTXOene og de som venter på remixing. Når Whirlpool-klienten er aktiv, er UTXOene som befinner seg i **postmix**-kontoen automatisk tilgjengelige for remixing og vil bli tilfeldig valgt for å delta i disse nye syklusene.

Som en påminnelse, så er remixene deretter 100% gratis: ingen ekstra tjenestegebyrer eller gruvegebyrer kreves. Å holde UTXOene i **postmix**-kontoen opprettholder dermed deres verdi intakt og forbedrer samtidig deres anonsets. Det er derfor det er viktig å la disse myntene delta i flere coinjoin-sykluser. Det koster deg strengt tatt ingenting, og det øker deres anonymitetsnivåer.
Når du bestemmer deg for å bruke blandete UTXOer, kan du gjøre dette direkte fra denne **postmix**-kontoen. Det er tilrådelig å beholde de blandete UTXOene på denne kontoen for å dra nytte av gratis remixes og for å unngå at de forlater Whirlpool-kretsen, noe som kunne redusere deres konfidensialitet.
Som vi vil se i den følgende opplæringen, finnes det også `mix to`-alternativet som tilbyr muligheten til automatisk å sende dine blandete mynter til en annen lommebok, som for eksempel en kald lommebok, etter et definert antall coinjoins.
Etter å ha dekket teorien, la oss dykke inn i praksis med en opplæring om bruk av Whirlpool gjennom Samourai Wallet Android-applikasjonen, synkronisert med Whirlpool CLI og GUI på ditt eget Dojo!
## Opplæring: Coinjoin Whirlpool med Ditt Eget Dojo
Det finnes mange alternativer for å bruke Whirlpool. Den jeg ønsker å introdusere her er Samourai Wallet-alternativet, en åpen kildekode Bitcoin-lommebokadministrasjonsapplikasjon på Android, men denne gangen **med ditt eget Dojo**.

Å utføre coinjoins via Samourai Wallet ved bruk av ditt eget Dojo er, etter min mening, den mest effektive strategien for å utføre coinjoins på Bitcoin til dags dato. Denne tilnærmingen krever noe innledende investering i form av oppsett, men når den er på plass, tilbyr den muligheten til kontinuerlig å blande og remixe dine bitcoins, 24 timer i døgnet, 7 dager i uken, uten behov for å holde Samourai-applikasjonen aktiv til enhver tid. Faktisk, takket være Whirlpool CLI som opererer på en Bitcoin-node, er du alltid klar til å delta i coinjoins. Samourai-applikasjonen gir deg deretter muligheten til å bruke dine blandete midler når som helst, hvor som helst, direkte fra din smarttelefon. Dessuten har denne metoden fordelen av aldri å koble deg til servere administrert av Samourai-teamene, og dermed bevare din `xpub` fra enhver ekstern eksponering.

Denne teknikken er derfor ideell for de som søker maksimal personvern og de høyeste kvalitets coinjoin-syklusene. Imidlertid krever det å ha en Bitcoin-node til din disposisjon og, som vi vil se senere, krever noe oppsett. Den er dermed mer egnet for mellomliggende til avanserte brukere. For nybegynnere anbefaler jeg å bli kjent med coinjoin gjennom disse to andre opplæringene, som viser hvordan man gjør det fra Sparrow Wallet eller Samourai Wallet (uten Dojo):
- **[Sparrow Wallet coinjoin-opplæring](https://planb.network/en/tutorials/privacy/coinjoin-sparrow-wallet)**;
- **[Samourai Wallet coinjoin-opplæring (uten Dojo)](https://planb.network/en/tutorials/privacy/coinjoin-samourai-wallet)**.

### Forstå Oppsettet
For å starte, trenger du et Dojo! Dojo er en Bitcoin-node-implementasjon basert på Bitcoin Core, utviklet av Samourai-teamene.

For å kjøre ditt eget Dojo, har du muligheten til enten å installere en Dojo-node autonomt, eller å dra nytte av Dojo på toppen av en annen "node-i-boks" Bitcoin-node-løsning. For øyeblikket er de tilgjengelige alternativene:
- [RoninDojo](https://ronindojo.io/), som er et Dojo forbedret med ekstra verktøy, inkludert en installasjonsassistent og en administrasjonsassistent. Jeg detaljerer prosedyren for å sette opp og bruke RoninDojo i denne andre opplæringen: [RONINDOJO V2](https://planb.network/en/tutorials/node/ronin-dojo-v2);
- [Umbrel](https://umbrel.com/) med "Samourai Server"-applikasjonen;
- [MyNode](https://mynodebtc.com/) med "Dojo"-applikasjonen;
- [Nodl](https://www.nodl.eu/) med "Dojo"-applikasjonen;
- [Citadel](https://runcitadel.space/) med "Samourai"-applikasjonen.
![coinjoin](assets/notext/9.webp)
I vår oppsett vil vi samhandle med tre distinkte grensesnitt:
- **Samourai Wallet**, som vil huse vår Bitcoin-lommebok dedikert til coinjoins. Tilgjengelig gratis på Android, tillater denne FOSS-applikasjonen deg å kontrollere din mikse-lommebok, spesielt for å bruke dine postmix fra din smarttelefon;
- **Whirlpool CLI** (_Command Line Interface_), som vil operere på noden som huser Dojo. Denne programvaren vil ha tilgang til nøklene til din Samourai-lommebok. Den er ansvarlig for å kommunisere med koordinatoren og håndtere coinjoins kontinuerlig. Den fungerer som en kopi av din Samourai-lommebok på din node, klar til å delta i coinjoins når som helst;
- **Whirlpool GUI** (_Graphical User Interface_), det grafiske brukergrensesnittet vi vil bruke for å overvåke aktiviteten til Whirlpool CLI og initiere miksing på avstand. Whirlpool GUI gir en visuell representasjon av operasjonene utført av Whirlpool CLI. Denne programvaren må installeres på en datamaskin separat fra Dojo. For brukere av Umbrel, MyNode, Nodl, og Citadel, er Whirlpool GUI obligatorisk. Imidlertid, med RoninDojo, er Whirlpool GUI-grensesnittet allerede integrert i nodens webgrensesnitt via `Whirlpool`-applikasjonen. Derfor vil du ikke trenge å installere den på en separat PC.

Etter min mening representerer bruk av RoninDojo den beste løsningen for å utføre coinjoins med en Dojo. Siden denne node-i-boks-programvaren er i direkte partnerskap med Samourai-teamene, er RoninDojo mye mer optimalisert for å gjøre dette. I tillegg forenkler integrasjonen av Whirlpool GUI i webgrensesnittet oppsettsprosessen betydelig. I denne veiledningen vil jeg likevel forklare hvordan man gjør det med de andre løsningene som integrerer Dojo (Umbrel, Nodl, MyNode, og Citadel).

### Forberede din Dojo
For å begynne, må du installere Dojo og skaffe QR-koden eller lenken som vil tillate deg å koble til den eksternt. Denne lenken er en Tor-adresse som slutter på `.onion`. Hvis du bruker RoninDojo, naviger enkelt til `Pairing`-menyen for å få tilgang til denne informasjonen.
![coinjoin](assets/notext/10.webp)

Under `Samourai Dojo`, klikk på `Pair now`-knappen.

![coinjoin](assets/notext/11.webp)

Din tilkoblings QR-kode og den tilsvarende lenken vil bli vist.

![coinjoin](assets/notext/12.webp)

Hvis du er på Umbrel, gå til App Store og søk etter `Samourai Server`-applikasjonen. Den er plassert under `Bitcoin`-fanen.

![coinjoin](assets/notext/13.webp)

Installer applikasjonen.

![coinjoin](assets/notext/14.webp)

Ved åpning av applikasjonen, vil du da ha tilgang til QR-koden for å koble til din Dojo.

![coinjoin](assets/notext/15.webp)

Hvis du bruker en annen node-i-boks-programvare som MyNode, Citadel, eller Nodl, er prosessen lik den for Umbrel. Du må installere Samourai- eller Dojo-applikasjonen for å skaffe nødvendig informasjon for å koble til din Dojo.

![coinjoin](assets/notext/16.webp)

### Forberede din Samourai-lommebok
Etter å ha hentet tilkoblingsinformasjonen til din Dojo, er det nå på tide å sette opp lommeboken din for coinjoins. Det er to scenarioer: hvis du ennå ikke har en Samourai Wallet på smarttelefonen din, er prosessen enkel, bare opprett en ny.

På den andre siden, hvis du allerede har en Samourai Wallet, må du installere applikasjonen på nytt for å knytte den til en ny Dojo. Dette steget er nødvendig fordi tilkoblingen til en Dojo bare kan etableres ved første oppstart av applikasjonen. Imidlertid, takket være den automatisk genererte krypterte sikkerhetskopifilen av Samourai på telefonen din, er denne prosedyren enkel og rask.

*Hvis du aldri har brukt Samourai, kan du hoppe over disse innledende trinnene og gå direkte til installasjonen av applikasjonen.*

Først og fremst, sørg for at Samourai Wallet-applikasjonen din er oppdatert. For å gjøre dette, sjekk Google Play Store eller sammenlign versjonen av applikasjonen din i `Innstillinger > Annet` med den som er tilgjengelig på Samourai-nettstedet.

![coinjoin](assets/notext/17.webp)

Sørg for at du har din Samourai lommebok gjenopprettingsfrase og at den er leselig. Deretter, utfør en test av din BIP39-passfrase ved å navigere til `Innstillinger > Feilsøking > Passfrase/Backup test` for å bekrefte dens nøyaktighet.

![coinjoin](assets/notext/18.webp)
Skriv inn din passfrase, deretter verifiser at Samourai bekrefter dens gyldighet.
![coinjoin](assets/notext/19.webp)

Hvis din passfrase er ugyldig, eller hvis du ikke har din gjenopprettingsfrase, er det avgjørende å umiddelbart stoppe prosedyren! **Du risikerer å miste dine bitcoins under denne operasjonen.** I dette tilfellet anbefales det å overføre dine midler til en annen lommebok og starte med en ny blank Samourai lommebok. De følgende trinnene bør kun følges hvis du er sikker på at du har all nødvendig sikkerhetskopieringsinformasjon og at din passfrase er gyldig.

Fortsett deretter med å opprette en kryptert sikkerhetskopi av lommeboken din og kopier den til utklippstavlen din. For å utføre denne operasjonen, klikk på de tre små prikkene som ligger øverst til høyre på skjermen, deretter velg `Eksporter lommebok sikkerhetskopi`.

![coinjoin](assets/notext/20.webp)

**Fra dette steget av, ikke kopier noe annet til utklippstavlen din!** Det er helt avgjørende at du beholder din kopierte sikkerhetskopi.

Hvis du har utført de foregående trinnene korrekt, er du nå i stand til å trygt slette din Samourai lommebok. For å gjøre dette, gå til: `Innstillinger > Lommebok > Sikkert slett lommeboken`.

![coinjoin](assets/notext/21.webp)

![coinjoin](assets/notext/22.webp)

*Hvis du aldri har brukt Samourai og installerer applikasjonen fra bunnen av, kan du gjenoppta veiledningen ved dette trinnet.*

Din Samourai-applikasjon er nå tilbakestilt. Åpne applikasjonen og fortsett med oppsettstrinnene som om du brukte den for første gang.

![coinjoin](assets/notext/23.webp)

I neste trinn vil du få tilgang til siden dedikert til å konfigurere din Dojo. Velg `Dojo`-alternativet, deretter skriv inn din Dojos innloggingsinformasjon. For å gjøre dette, har du muligheten til å skanne informasjonen ved å trykke `Scan QR`.

![coinjoin](assets/notext/24.webp)

*For nye brukere av Samourai, vil det deretter være nødvendig å opprette en lommebok fra bunnen av. Hvis du trenger assistanse, kan du konsultere instruksjonene for å sette opp en ny Samourai lommebok [i denne veiledningen, spesifikt i seksjonen "Opprette en programvarelommebok"](https://planb.network/tutorials/privacy/coinjoin-samourai-wallet)*
Hvis du fortsetter med gjenopprettingen av en allerede eksisterende Samourai-lommebok, velg `Gjenopprett eksisterende lommebok`, deretter velger du `Jeg har en Samourai sikkerhetskopi-fil`.
![coinjoin](assets/notext/25.webp)
Normalt bør du alltid ha gjenopprettingsfilen din i utklippstavlen. Klikk deretter på `LIM INN` for å sette inn filen din på det angitte stedet. For å dekryptere den, vil det også være nødvendig å angi BIP39-passfrasen til lommeboken din i det tilsvarende feltet, som er plassert rett nedenfor. For å fullføre, klikk på `FERDIG`.
![coinjoin](assets/notext/26.webp)

Du vil deretter bli omdirigert til din Samourai-lommebok som, denne gangen, vil være koblet til din egen Dojo.

![coinjoin](assets/notext/27.webp)

### Installere Whirlpool GUI
Det er nå på tide å installere Whirlpool GUI, det grafiske brukergrensesnittet som vil tillate deg å administrere dine coinjoin-sykluser fra din vanlige PC. For RoninDojo-brukere er dette steget ikke nødvendig siden administrasjonen av coinjoins kan gjøres direkte via webgrensesnittet i `Apps > Whirlpool`. Men, hvis du bruker en annen Bitcoin "node-in-box"-løsning, er det avgjørende å fortsette med denne installasjonen.
![coinjoin](assets/notext/28.webp)
Gå til din personlige datamaskin og last ned Whirlpool-programvaren fra det offisielle Samourai Wallet-nettstedet, og velg versjonen som tilsvarer ditt operativsystem.

![coinjoin](assets/notext/29.webp)

Før du starter Whirlpool GUI, er det nødvendig å installere JAVA 8 eller en høyere versjon på maskinen din. For dette, [kan du installere OpenJDK](https://adoptium.net/).
![coinjoin](assets/notext/30.webp)
Det er også nødvendig å ha Tor Daemon eller Tor Browser operativ i bakgrunnen på datamaskinen din. Sørg for å starte Tor før hver Whirlpool GUI brukssesjon. Hvis Tor ikke er installert på maskinen din ennå, [kan du laste ned og installere det fra det offisielle prosjektets nettsted](https://www.torproject.org/download/), og deretter sørge for å starte det i bakgrunnen.

![coinjoin](assets/notext/31.webp)

Når JDK er installert på systemet ditt og Tor er lansert i bakgrunnen, kan du starte Whirlpool GUI.

![coinjoin](assets/notext/32.webp)

Fra Whirlpool GUI, klikk på `Avansert: Fjern CLI` for å koble din Whirlpool CLI som er på din Dojo. Du vil trenge Tor-adressen til din Whirlpool CLI.

![coinjoin](assets/notext/33.webp)

For å finne din Tor-adresse på Umbrel og andre "node-in-box"-løsninger, start ganske enkelt Samourai Server eller Dojo-applikasjonen (navnet kan variere avhengig av programvaren som brukes). Tor-adressen vil være direkte synlig på applikasjonens side.
![coinjoin](assets/notext/34.webp)
I Whirlpool GUI, skriv inn Tor-adressen du fikk tidligere i `CLI adresse`-feltet. Behold `http://`-prefikset, men ikke legg til `:8899`-porten på slutten. Lim inn bare adressen slik den ble gitt til deg.
![coinjoin](assets/notext/35.webp)
I Tor Proxy-feltet, skriv inn `socks5://127.0.0.1:9050` hvis du bruker Tor Daemon, eller `socks5://127.0.0.1:9150` hvis det er Tor Browser. Når du først kobler deg til Whirlpool CLI via Whirlpool GUI, er det mulig å la API-nøkkelfeltet stå tomt. Hvis dette ikke er din første tilkobling, vennligst skriv inn din API-nøkkel i det dedikerte området. Denne nøkkelen kan finnes på samme side som din Tor-adresse.
![coinjoin](assets/notext/36.webp)

Når du har fylt inn alt, klikk på `Connect`-knappen. Vennligst vent, tilkoblingen kan ta noen minutter.

![coinjoin](assets/notext/37.webp)

### Koble din Samourai Wallet til Whirlpool GUI
*For RoninDojo-brukere, kan du fortsette opplæringen her.*

Vi vil nå pare Samourai-lommeboken vi konfigurerte tidligere med Whirlpool GUI-programvaren, eller direkte med RoninDojo for de som bruker denne programvaren. Enten du bruker Whirlpool GUI eller RoninDojo, vil du bli bedt om å lime inn eller skanne paringsinformasjonen til din Samourai-lommebok.

![coinjoin](assets/notext/38.webp)

For å finne denne informasjonen, gå til lommebokens innstillinger.

![coinjoin](assets/notext/39.webp)

Klikk på `Transaksjoner`, deretter på `Par til Whirlpool GUI`.

![coinjoin](assets/notext/40.webp)

Samourai vil deretter gi deg nødvendig informasjon for å etablere tilkoblingen. Vær forsiktig, disse dataene er sensitive! Du kan overføre dem til din PC enten ved å kopiere dem direkte eller ved å skanne QR-koden som vises, ved å bruke datamaskinens webkamera etter å ha klikket på QR-kodesymbolet.

![coinjoin](assets/notext/41.webp)

Etter å ha utført denne operasjonen, i Whirlpool GUI, velg `Initialize GUI`. Vennligst vent, da dette trinnet kan ta et øyeblikk.

![coinjoin](assets/notext/42.webp)

Enten du bruker Whirlpool GUI eller RoninDojo, vil du bli bedt om å skrive inn passfrasen til din Samourai-lommebok. Sett den inn i det dedikerte feltet, deretter trykk på `Login`-knappen for å fortsette.

![coinjoin](assets/notext/43.webp)

Du vil da ankomme hjemmesiden til Whirlpool CLI

![coinjoin](assets/notext/44.webp)

### Initiere coinjoins fra Whirlpool GUI
*For RoninDojo-brukere, er prosessen identisk. Whirlpool-appgrensesnittet integrert i RoninDojo tilbyr de samme alternativene og funksjonalitetene som Whirlpool GUI-programvaren på skrivebordet. Derfor kan du følge disse instruksjonene på samme måte.*
Nå som alt er satt opp, er du klar til å starte miksingen av dine bitcoins. For å gjøre dette, overfør bitcoinsene du ønsker å mikse til **Deposit**-kontoen til din Samourai Wallet. Denne operasjonen kan utføres enten direkte via Samourai Wallet-appen eller på Whirlpool GUI. Fra hovedsiden, klikk på `+ Deposit`-knappen som er plassert øverst til venstre.

![coinjoin](assets/notext/45.webp)
Whirlpool GUI vil generere en mottaksadresse. Den vil også vise det minste beløpet som er nødvendig for å delta i hver coinjoin-pool. Dette beløpet varierer avhengig av gebyrmarkedet. Det anbefales å sette inn et beløp som er litt høyere enn det minimum som kreves, da hvis gruvegebyrene ikke synker, kan din UTXO bli avvist fra ønsket pool. Derfor, send dine bitcoins til den oppgitte adressen. For å få en ny adresse, klikk ganske enkelt på `Forny adresse`-knappen.
![coinjoin](assets/notext/46.webp)

Når innskuddet er bekreftet, vil du kunne se det dukke opp på **Innskudd**-kontoen i Whirlpool GUI.

![coinjoin](assets/notext/47.webp)

For å starte coinjoin-syklusene, velg UTXOene du ønsker å blande og trykk på `Premix`-knappen. Vær forsiktig: hvis du velger flere forskjellige UTXOer samtidig, vil de bli kombinert under `TX0`-forberedelsestransaksjonen. Denne sammenslåingen kan føre til en reduksjon i personvern, spesielt hvis UTXOene kommer fra forskjellige kilder, på grunn av Common Input Ownership Heuristic (CIOH).

![coinjoin](assets/notext/48.webp)

Whirlpool-konfigurasjonssiden åpnes. Du kan velge poolen du ønsker å gå inn i. Velg også gruvegebyrene dedikert til `TX0` og de første coinjoins. Nederst på denne siden vil et sammendrag presentere deg for mengden av doxxic endring samt beløpet og antallet UTXOer som vil bli likestilt og inkludert i coinjoin-syklusene. Hvis du er fornøyd med denne konfigurasjonen, trykk på `Premix`-knappen for å starte coinjoin-syklusene.
![coinjoin](assets/notext/49.webp)

Når `TX0` er opprettet, vil du kunne se dine likestilte UTXOer i **Premix**-kontoen, i påvente av bekreftelse. For å tillate at dine mynter automatisk remixes 24 timer i døgnet, 7 dager i uken, anbefaler jeg å aktivere `Automatisk miks premix & postmix`-alternativet. Du finner denne funksjonen i `Konfigurasjon`-fanen, plassert til venstre i Whirlpool GUI-vinduet ditt.
![coinjoin](assets/notext/50.webp)
Etter å ha startet coinjoins, kan du avslutte Whirlpool GUI samt Samourai Wallet. Bare din node trenger å forbli tilkoblet for å kunne delta i kontinuerlige coinjoins. Det er imidlertid tilrådelig å periodisk sjekke fremgangen til dine coinjoin-sykluser. Hvis du merker at dine UTXOer ikke lenger blir valgt for en coinjoin etter en stund, kan dette indikere en feil. I så fall, gå til Whirlpool CLI og velg `Start` for å gjenoppta din tilgjengelighet for coinjoins.

![coinjoin](assets/notext/51.webp)

Dine blandete UTXOer er synlige fra **Postmix**-kontoen på Whirlpool GUI. I tillegg har du muligheten til å vise og bruke dem direkte via Whirlpool-grensesnittet på din Samourai Wallet. For å få tilgang til denne menyen, klikk på det blå `+` nederst på skjermen din, og velg deretter `Whirlpool`.

![coinjoin](assets/notext/52.webp)

Whirlpool-kontoer er lett gjenkjennelige på Samourai Wallet ved deres blå farge. Dette lar deg bruke dine blandete UTXOer fra hvor som helst og når som helst, direkte fra smarttelefonen din.

![coinjoin](assets/notext/53.webp)
For å holde oversikt over dine automatiske coinjoins, anbefaler jeg også å sette opp en se-kun lommebok via Sentinel-appen. Legg til ZPUB-en til din **Postmix**-konto og overvåk fremgangen til dine coinjoin-sykluser i sanntid. Hvis du ønsker å forstå hvordan du bruker Sentinel, anbefaler jeg å konsultere denne andre opplæringen på PlanB Network: [**SENTINEL SE-KUN**](https://planb.network/tutorials/wallet/sentinel)