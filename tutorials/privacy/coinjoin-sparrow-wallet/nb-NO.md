---
name: Coinjoin - Sparrow Wallet
description: Hvordan utføre en coinjoin på Sparrow Wallet?
---
![cover](assets/cover.webp)

***ADVARSEL:** Etter arrestasjonen av grunnleggerne av Samourai Wallet og beslagleggelsen av deres servere den 24. april, fungerer ikke lenger Whirlpool-verktøyet, selv for personer som har sin egen Dojo eller bruker Sparrow Wallet. Det er imidlertid mulig at dette verktøyet kan bli gjeninnført i de kommende ukene eller relansert på en annen måte. Videre forblir den teoretiske delen av denne artikkelen relevant for å forstå prinsippene og målene med coinjoins generelt (ikke bare Whirlpool), samt for å forstå effektiviteten av Whirlpool-modellen.*

_Vi følger nøye med på utviklingen av denne saken samt utviklingen angående de tilknyttede verktøyene. Vær trygg på at vi vil oppdatere denne opplæringen etter hvert som ny informasjon blir tilgjengelig._

_Denne opplæringen er kun tilgjengelig for utdannings- og informasjonsformål. Vi støtter eller oppfordrer ikke til bruk av disse verktøyene til kriminelle formål. Det er brukerens ansvar å overholde lovene i sin jurisdiksjon._

---

I denne opplæringen vil du lære hva en coinjoin er og hvordan du utfører en ved hjelp av Sparrow Wallet-programvaren og Whirlpool-implementeringen.

## Hva er en coinjoin på Bitcoin?
**En coinjoin er en teknikk som bryter sporbarheten til bitcoins på blockchain**. Den støtter seg på en samarbeidstransaksjon med en spesifikk struktur med samme navn: coinjoin-transaksjonen.

Coinjoins forbedrer personvernet til Bitcoin-brukere ved å komplisere kjedeanalyse for eksterne observatører. Deres struktur tillater sammenslåing av flere mynter fra forskjellige brukere i en enkelt transaksjon, noe som gjør det vanskelig å bestemme koblingene mellom inngangs- og utgangsadresser.

Prinsippet med coinjoin er basert på en samarbeidstilnærming: flere brukere som ønsker å blande sine bitcoins, setter inn identiske beløp som innganger i samme transaksjon. Disse beløpene blir deretter redistribuert som utganger av lik verdi til hver bruker. Ved slutten av transaksjonen blir det umulig å knytte en spesifikk utgang til en kjent bruker ved inngangen. Ingen direkte kobling eksisterer mellom inngangene og utgangene, noe som bryter tilknytningen mellom brukerne og deres UTXO, samt historikken til hver mynt.
![coinjoin](assets/notext/1.webp)

Eksempel på en coinjoin-transaksjon (ikke fra meg): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)

For å utføre en coinjoin samtidig som hver bruker beholder kontroll over sine midler til enhver tid, begynner prosessen med konstruksjonen av transaksjonen av en koordinator, som deretter overfører den til hver deltaker. Hver bruker signerer deretter transaksjonen etter å ha verifisert at den passer for dem. Alle innsamlede signaturer integreres til slutt i transaksjonen. Hvis et forsøk på å avlede midler blir gjort av en bruker eller koordinatoren, gjennom en modifikasjon av coinjoin-transaksjonens utganger, vil signaturene vise seg å være ugyldige, noe som fører til at transaksjonen avvises av nodene.

Det finnes flere implementeringer av coinjoin, som Whirlpool, JoinMarket, eller Wabisabi, hver med mål om å håndtere koordinering blant deltakere og øke effektiviteten av coinjoin-transaksjoner.
I denne veiledningen fokuserer vi på **Whirlpool**-implementasjonen, som jeg anser for å være den mest effektive løsningen for å utføre coinjoins på Bitcoin. Selv om den er tilgjengelig på flere lommebøker, utforsker denne veiledningen eksklusivt bruken av den med Sparrow Wallet Desktop-programvaren.

## Hvorfor Utføre CoinJoins på Bitcoin?

Et av de første problemene med ethvert peer-to-peer betalingssystem er dobbeltutgifter: hvordan forhindre at ondsinnede individer bruker de samme pengeenhetene flere ganger uten å måtte ty til en sentral autoritet for avgjørelse?

Satoshi Nakamoto tilbød en løsning på dette dilemmaet gjennom Bitcoin-protokollen, et peer-to-peer elektronisk betalingssystem som opererer uavhengig av enhver sentral autoritet. I hans hvitbok understreker han at den eneste måten å sertifisere fraværet av dobbeltutgifter på, er å sikre synligheten av alle transaksjoner innen betalingssystemet.

For å sikre at hver deltaker er klar over transaksjonene, må de offentliggjøres. Dermed er driften av Bitcoin avhengig av en transparent og distribuert infrastruktur, som tillater enhver nodoperatør å verifisere helheten av de elektroniske signaturkjedene og historikken til hver mynt, fra dens skapelse av en miner.

Den transparente og distribuerte naturen til Bitcoins blockchain betyr at enhver nettverksbruker kan følge og analysere transaksjonene til alle andre deltakere. Følgelig er anonymitet på transaksjonsnivå umulig. Imidlertid bevares anonymiteten på individnivå. I motsetning til det tradisjonelle banksystemet hvor hver konto er knyttet til en personlig identitet, er midler på Bitcoin assosiert med par av kryptografiske nøkler, og tilbyr dermed brukerne en form for pseudonymitet bak kryptografiske identifikatorer.

Derfor er konfidensialiteten på Bitcoin kompromittert når eksterne observatører klarer å assosiere spesifikke UTXOer med identifiserte brukere. Når denne assosiasjonen er etablert, blir det mulig å spore deres transaksjoner og analysere historikken til deres bitcoins. Coinjoin er nettopp en teknikk utviklet for å bryte sporebarheten til UTXOer, og tilbyr dermed et visst lag av konfidensialitet til Bitcoin-brukere på transaksjonsnivå.

## Hvordan Fungerer Whirlpool?

Whirlpool skiller seg ut fra andre coinjoin-metoder ved å bruke "_ZeroLink_"-transaksjoner, som sikrer at det strengt tatt ikke er mulig med en teknisk kobling mellom alle inngangene og alle utgangene. Denne perfekte blandingen oppnås gjennom en struktur hvor hver deltaker bidrar med et identisk beløp i inngang (unntatt gruvegebyrer), og dermed genererer utganger av perfekt like beløp.

Denne restriktive tilnærmingen på innganger gir Whirlpool coinjoin-transaksjoner en unik karakteristikk: total fravær av deterministiske koblinger mellom inngangene og utgangene. Med andre ord, hver utgang har en like stor sannsynlighet for å bli tilskrevet enhver deltaker, sammenlignet med alle de andre utgangene av transaksjonen.
Opprinnelig var antallet deltakere i hver Whirlpool coinjoin begrenset til 5, med 2 nye deltakere og 3 remixere (vi vil forklare disse konseptene videre). Imidlertid førte økningen i on-chain transaksjonsgebyrer observert i 2023 til at Samourai-teamene måtte revurdere modellen sin for å forbedre personvernet samtidig som kostnadene reduseres. Dermed, med tanke på markedsituasjonen for gebyrer og antall deltakere, kan koordinatoren nå organisere coinjoins inkludert 6, 7, eller 8 deltakere. Disse forbedrede øktene refereres til som "_Surge Cycles_". Det er viktig å merke seg at, uavhengig av oppsettet, er det alltid bare 2 nye deltakere i Whirlpool coinjoins.

Derfor er Whirlpool-transaksjoner kjennetegnet ved et identisk antall innganger og utganger, som kan være:
- 5 innganger og 5 utganger;
![coinjoin](assets/notext/2.webp)
- 6 innganger og 6 utganger;
![coinjoin](assets/notext/3.webp)
- 7 innganger og 7 utganger;
![coinjoin](assets/notext/4.webp)
- 8 innganger og 8 utganger. ![coinjoin](assets/notext/5.webp)
Modellen foreslått av Whirlpool er dermed basert på små coinjoin-transaksjoner. I motsetning til Wasabi og JoinMarket, hvor robustheten av anonsetene er avhengig av volumet av deltakere i en enkelt syklus, satser Whirlpool på kjeding av flere små sykluser.

I denne modellen pådrar brukeren seg kun gebyrer ved sin første inngang i en pool, noe som tillater dem å delta i en mengde remixes uten ekstra gebyrer. Det er de nye deltakerne som bærer mining-gebyrene for remixerne.

Med hver tilleggs coinjoin som en mynt deltar i, sammen med sine tidligere møtte peers, vil anonsetene vokse eksponentielt. Målet er dermed å dra nytte av disse gratis remixene som, ved hver forekomst, bidrar til å styrke tettheten av anonsetene assosiert med hver blandet mynt.

Whirlpool ble designet med tanke på to viktige krav:
- Tilgjengeligheten av implementering på mobile enheter, gitt at Samourai Wallet primært er en smarttelefonapplikasjon;
- Hastigheten på remixing-syklusene for å fremme en betydelig økning i anonsetene.

Disse imperativene veiledet utviklerne av Samourai Wallet i designet av Whirlpool, noe som førte dem til å begrense antall deltakere per syklus. For få deltakere ville ha kompromittert effektiviteten av coinjoin, drastisk redusert anonsetene generert med hver syklus, mens for mange deltakere ville ha utgjort forvaltningsproblemer på mobile applikasjoner og ville ha hindret flyten av sykluser.

**Til syvende og sist er det ikke nødvendig å ha et høyt antall deltakere per coinjoin på Whirlpool siden anonsetene er laget over akkumuleringen av flere coinjoin-sykluser.**
[-> Lær mer om Whirlpool anonseter.](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)
### Coinjoin-pools og gebyrer
For å sikre at flere sykluser effektivt øker anonsetene til blandete mynter, må et visst rammeverk etableres for å begrense mengdene av UTXOer som brukes. Whirlpool definerer ulike pools for dette formålet.

En pool representerer en gruppe brukere som ønsker å blande sammen, som er enige om mengden av UTXOer som skal brukes for å optimalisere coinjoin-prosessen. Hver pool spesifiserer et fast beløp for UTXOen, som brukeren må overholde for å delta. Således, for å utføre coinjoins med Whirlpool, må du velge en pool. De for øyeblikket tilgjengelige poolene er som følger:
- 0,5 bitcoins;
- 0,05 bitcoin;
- 0,01 bitcoin;
- 0,001 bitcoin (= 100 000 sats).

Ved å bli med i en pool med dine bitcoins, vil de bli delt for å generere UTXOer som er fullstendig homogene med de til de andre deltakerne i poolen. Hver pool har en maksimumsgrense; dermed, for beløp som overstiger denne grensen, vil du bli tvunget enten til å gjøre to separate innganger innenfor samme pool eller å flytte til en annen pool med et høyere beløp:

| Pool (bitcoin) | Maksimalt beløp per inngang (bitcoin) |
|----------------|---------------------------------------|
| 0,5            | 35                                    |
| 0,05           | 3,5                                   |
| 0,01           | 0,7                                   |
| 0,001          | 0,025                                 |
Som nevnt tidligere, anses en UTXO for å tilhøre en pool når den er klar til å bli integrert i en coinjoin. Dette betyr imidlertid ikke at brukeren mister besittelsen av den. **Gjennom de ulike mikse-syklusene beholder du full kontroll over nøklene dine og, som en konsekvens, dine bitcoins.** Dette er det som skiller coinjoin-teknikken fra andre sentraliserte mikseteknikker.
For å gå inn i en coinjoin-pool, må tjenesteavgifter samt gruveavgifter betales. Tjenesteavgiftene er faste for hver pool og er ment å kompensere teamene ansvarlige for utviklingen og vedlikeholdet av Whirlpool. For Sparrow Wallet-brukere, blir disse avgiftene videreført av Samourai-teamene til utviklerne av Sparrow.

Tjenesteavgiftene for å bruke Whirlpool skal betales én gang ved inngangen til poolen. Når dette trinnet er fullført, har du muligheten til å delta i et ubegrenset antall remikser uten ekstra avgifter. Her er de nåværende faste avgiftene for hver pool:

| Pool (bitcoin) | Inngangsavgift (bitcoin) |
|----------------|--------------------------|
| 0.5            | 0.0175                   |
| 0.05           | 0.00175                  |
| 0.01           | 0.0005 (50,000 sats)     |
| 0.001          | 0.00005 (5,000 sats)     |


Disse avgiftene fungerer i hovedsak som en inngangsbillett til den valgte poolen, uavhengig av beløpet du legger i coinjoin. Så, enten du blir med i 0.01-poolen med nøyaktig 0.01 BTC eller du går inn med 0.5 BTC, vil avgiftene forbli de samme i absolutt verdi.

Før man fortsetter med coinjoins, har brukeren derfor et valg mellom 2 strategier:
- Velge en mindre pool for å minimere tjenesteavgifter, vel vitende om at de vil motta flere små UTXOer i retur;
- Eller foretrekke en større pool, og gå med på å betale høyere avgifter for å ende opp med et redusert antall UTXOer med større verdi.

Det anbefales generelt å ikke slå sammen flere miksete UTXOer etter coinjoin-syklusene, da dette kan kompromittere den oppnådde konfidensialiteten, spesielt på grunn av Common-Input-Ownership Heuristic (CIOH). Derfor kan det være lurt å velge en større pool, selv om det betyr å betale mer, for å unngå å ha for mange småverdi UTXOer som output. Brukeren må vurdere disse avveiningene for å velge den poolen de foretrekker.

I tillegg til tjenesteavgifter, må også gruveavgifter som er iboende i enhver Bitcoin-transaksjon, vurderes. Som en Whirlpool-bruker, vil du være nødt til å betale gruveavgiftene for forberedelsestransaksjonen (`Tx0`) samt de for den første coinjoin. Alle påfølgende remikser vil være gratis, takket være Whirlpools modell som stoler på betalingen fra nye deltakere.

Faktisk, i hver Whirlpool coinjoin, er to brukere blant inngangene nye deltakere. De andre inngangene kommer fra remiksere. Som et resultat, dekkes gruveavgiftene for alle deltakerne i transaksjonen av disse to nye deltakerne, som da også vil dra nytte av gratis remikser:
![coinjoin](assets/en/6.webp)
Takket være dette avgiftssystemet, skiller Whirlpool seg virkelig ut fra andre coinjoin-tjenester siden anonsettene til UTXOene ikke er proporsjonale med prisen betalt av brukeren. Dermed er det mulig å oppnå betydelig høye nivåer av anonymitet ved kun å betale poolens inngangsavgifter og gruveavgiftene for to transaksjoner (den `Tx0` og den første miksen).
Det er viktig å merke seg at brukeren også må dekke gruvegebyrene for å ta ut sine UTXOer fra bassenget etter å ha fullført flere coinjoins, med mindre de har valgt `mix to`-alternativet, som vi vil diskutere i opplæringen nedenfor.
### HD-lommebokkontoene som brukes av Whirlpool
For å utføre en coinjoin via Whirlpool, må lommeboken generere flere distinkte kontoer. En konto, i konteksten av en HD (Hierarchical Deterministic) lommebok, utgjør en seksjon som er helt isolert fra de andre, denne separasjonen skjer på det tredje dybdenivået i lommebokens hierarki, det vil si på nivået av `xpub`.
En HD-lommebok kan teoretisk avlede opp til `2^(32/2)` forskjellige kontoer. Den opprinnelige kontoen, som brukes som standard på alle Bitcoin-lommebøker, tilsvarer indeksen `0'`.

For lommebøker tilpasset Whirlpool, som Samourai eller Sparrow, brukes 4 kontoer for å møte behovene til coinjoin-prosessen:
- **Innskudds**kontoen, identifisert ved indeksen `0'`;
- **Dårlig bank** (eller doxxic change) kontoen, identifisert ved indeksen `2 147 483 644'`;
- **Premix**-kontoen, identifisert ved indeksen `2 147 483 645'`;
- **Postmix**-kontoen, identifisert ved indeksen `2 147 483 646'`.

Hver av disse kontoene oppfyller en spesifikk funksjon innenfor coinjoin.

Alle disse kontoene er knyttet til et enkelt frø, som lar brukeren gjenopprette tilgang til alle sine bitcoins ved å bruke sin gjenopprettingsfrase og, om aktuelt, deres passfrase. Det er imidlertid nødvendig å spesifisere til programvaren, under denne gjenopprettingsoperasjonen, de forskjellige kontoindeksene som ble brukt.

La oss nå se på de forskjellige stadiene av en Whirlpool coinjoin innenfor disse kontoene.

### De forskjellige stadiene av coinjoins på Whirlpool
**Stadium 1: Tx0**
Utgangspunktet for enhver Whirlpool coinjoin er **innskudds**kontoen. Denne kontoen er den du automatisk bruker når du oppretter en ny Bitcoin-lommebok. Denne kontoen må krediteres med bitcoins du ønsker å blande.

`Tx0` representerer det første stadiet i Whirlpool-blandingsprosessen. Målet er å forberede og likestille UTXOene for coinjoin, ved å dele dem inn i enheter som tilsvarer beløpet til det valgte bassenget, for å sikre homogeniteten av blandingen. De likestilte UTXOene sendes deretter til **premix**-kontoen. Når det gjelder differansen som ikke kan gå inn i bassenget, blir den skilt ut i en spesifikk konto: **dårlig bank** (eller "doxxic change").

Denne innledende transaksjonen `Tx0` tjener også til å avgjøre tjenestegebyrene som skyldes til mix-koordinatoren. I motsetning til de følgende stadiene, er denne transaksjonen ikke samarbeidsvillig; brukeren må derfor påta seg de fulle gruvegebyrene:
![coinjoin](assets/en/7.webp)
I dette eksemplet på en transaksjon `Tx0`, deles et innskudd på `372,000 sats` fra vår **innskudds**konto inn i flere utgående UTXOer, som er fordelt som følger:
- Et beløp på `5,000 sats` ment for koordinatoren for tjenestegebyrer, som tilsvarer inngangen til bassenget på `100,000 sats`;
- Tre UTXOer forberedt for blanding, omdirigert til vår **premix**-konto og registrert med koordinatoren. Disse UTXOene er likestilt på `108,000 sats` hver, for å dekke gruvegebyrene for deres fremtidige første blanding;
- Overskuddet, som ikke kan gå inn i bassenget fordi det er for lite, anses som giftig veksling. Det blir sendt til sin spesifikke konto. Her utgjør denne vekslingen `40,000 sats`;
- Til slutt er det `3,000 sats` som ikke utgjør en utgang, men er gruveavgiftene som er nødvendige for å bekrefte `Tx0`.

For eksempel, her er en ekte Tx0 Whirlpool (som ikke kommer fra meg): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)

**Steg 2: Den Giftige Vekslingen**
Overskuddet, som ikke har klart å integrere seg i bassenget, her tilsvarende `40,000 sats`, blir omdirigert til **dårlig bank**-kontoen, også referert til som "giftig veksling", for å sikre en streng separasjon fra de andre UTXOene i lommeboken.

Denne UTXOen er farlig for brukerens personvern fordi den ikke bare alltid er knyttet til sin fortid, og derfor muligens til identiteten til eieren, men i tillegg er den notert som tilhørende en bruker som har utført en coinjoin.

Hvis denne UTXOen slås sammen med blandete utganger, vil sistnevnte miste all personvernet vunnet under coinjoin-syklusene, spesielt på grunn av CIOH (*Common-Input-Ownership-Heuristic*). Hvis den slås sammen med andre giftige vekslinger, risikerer brukeren å miste personvern siden dette vil koble de forskjellige inngangene fra coinjoin-syklusene. Den må derfor behandles med forsiktighet. Måten å håndtere denne giftige UTXOen på vil bli detaljert i den siste delen av denne artikkelen, og fremtidige veiledninger vil gå dypere inn i disse metodene på PlanB Network.

**Steg 3: Den Innledende Blandingen**
Etter fullføringen av `Tx0`, blir de likestilte UTXOene sendt til **premix**-kontoen i vår lommebok, klare til å bli introdusert i deres første syklus av coinjoin, også kalt "innledende blanding". Hvis, som i vårt eksempel, `Tx0` genererer flere UTXOer ment for blanding, vil hver av dem bli integrert i en separat innledende coinjoin.
Ved slutten av disse innledende blandinger, vil **premix**-kontoen være tom, mens våre mynter, etter å ha betalt gruveavgiftene for denne første coinjoin, vil bli justert nøyaktig til beløpet definert av det valgte bassenget. I vårt eksempel vil våre innledende UTXOer på `108 000 sats` ha blitt redusert til nøyaktig `100 000 sats`.
![coinjoin](assets/en/8.webp)
**Steg 4: Remixene**
Etter den innledende blandingen, blir UTXOene overført til **postmix**-kontoen. Denne kontoen samler de allerede blandete UTXOene og de som venter på remixing. Når Whirlpool-klienten er aktiv, er UTXOene som ligger i **postmix**-kontoen automatisk tilgjengelige for remixing og vil bli tilfeldig valgt for å delta i disse nye syklusene.

Som en påminnelse, er remixene deretter 100% gratis: ingen ekstra tjenesteavgifter eller gruveavgifter kreves. Å holde UTXOene i **postmix**-kontoen opprettholder dermed deres verdi intakt, og samtidig forbedrer deres anonsets. Det er derfor viktig å tillate disse myntene å delta i flere coinjoin-sykluser. Det koster deg strengt tatt ingenting, og det øker deres nivåer av anonymitet.
Når du bestemmer deg for å bruke blandede UTXOer, kan du gjøre dette direkte fra denne **postmix**-kontoen. Det er tilrådelig å beholde de blandede UTXOene på denne kontoen for å dra nytte av gratis remixes og for å forhindre at de forlater Whirlpool-kretsen, noe som kunne redusere deres personvern.
Som vi vil se i den følgende opplæringen, finnes det også `mix to`-alternativet som tilbyr muligheten til automatisk å sende dine blandede mynter til en annen lommebok, som for eksempel en kald lommebok, etter et definert antall coinjoins.

Etter å ha diskutert teorien, la oss dykke inn i praksis med en opplæring i bruk av Whirlpool via Sparrow Wallet skrivebordsprogramvare!

## Opplæring: Coinjoin Whirlpool på Sparrow Wallet
Det finnes mange alternativer for å bruke Whirlpool. Den første jeg vil introdusere deg for er Sparrow Wallet-alternativet, en åpen kildekode Bitcoin lommebokforvaltningsprogramvare for PC.
Å bruke Sparrow har fordelen av å være ganske enkelt å komme i gang med, raskt å sette opp, og krever ikke annet utstyr enn en datamaskin og en internettforbindelse. Det er imidlertid en betydelig ulempe: coinjoins vil bare skje når Sparrow er lansert og tilkoblet. Dette betyr at hvis du ønsker å blande og remixe dine bitcoins 24/7, må du konstant holde datamaskinen din påslått.

### Installer Sparrow Wallet
For å begynne, vil du åpenbart trenge Sparrow Wallet-programvaren. Du kan direkte laste den ned fra [det offisielle nettstedet](https://sparrowwallet.com/download/) eller på [deres GitHub](https://github.com/sparrowwallet/sparrow/releases).

Før du installerer programvaren, vil det være viktig å verifisere signaturen og integriteten til den nedlastede kjørbare filen. Hvis du ønsker flere detaljer om installasjonsprosessen og verifisering av Sparrow-programvaren, anbefaler jeg deg å lese denne andre opplæringen: *[The Sparrow Wallet Guides](https://planb.network/tutorials/wallet/desktop/sparrow-7e9a77c0-013d-4f8e-a811-408b71dc7607)*

### Opprett en programvarelommebok
Etter å ha installert programvaren, må du fortsette med å opprette en Bitcoin-lommebok. Det er viktig å merke seg at for å delta i coinjoins, er bruken av en programvarelommebok (også kalt en "hot wallet") essensiell. Derfor **vil det ikke være mulig å utføre coinjoins med en lommebok sikret av en maskinvarelommebok**.

Selv om det ikke er avgjørende, i tilfelle du planlegger å blande betydelige mengder, anbefales det sterkt å velge bruk av en sterk BIP39-passfrase for denne lommeboken.

For å opprette en ny lommebok, åpne Sparrow, klikk deretter på `File`-fanen og `New Wallet`.

![sparrow](assets/notext/9.webp)

Velg et navn for denne lommeboken, for eksempel: "Coinjoin Wallet". Klikk på `Create Wallet`-knappen.

![sparrow](assets/notext/10.webp)

La standardinnstillingene stå, og klikk deretter på `New or Imported Software Wallet`-knappen.

![sparrow](assets/notext/11.webp)

Når du får tilgang til lommebokopprettelsesvinduet, anbefaler jeg å velge en 12-ords sekvens, da det er mer enn tilstrekkelig. Velg `Generate New` for å generere en ny gjenopprettingsfrase, og klikk på `Use Passphrase` hvis du ønsker å legge til en BIP39-passfrase. Det er viktig å lage en fysisk sikkerhetskopi av gjenopprettingsinformasjonen din, enten på papir eller på et metallstøtte, for å sikre sikkerheten til dine bitcoins.

![sparrow](assets/notext/12.webp)
Sørg for gyldigheten av sikkerhetskopi av gjenopprettingsfrasen din før du klikker på `Confirm Backup...`. Sparrow vil deretter be deg om å skrive inn frasen din igjen for å verifisere at du har notert den. Når dette trinnet er fullført, fortsett ved å klikke på `Create Keystore`.
![sparrow](assets/notext/13.webp)
La den foreslåtte avledningsstien være standard og trykk på `Import Keystore`. I mitt eksempel avviker avledningsstien litt siden jeg bruker Testnet for denne opplæringen. Avledningsstien som skal vises for deg er som følger:
```plaintext
m/84'/0'/0'
```

![sparrow](assets/notext/14.webp)

Etter det vil Sparrow vise avledningsdetaljene for din nye lommebok. I tilfelle du har satt en passfrase, er det sterkt anbefalt å notere din `Master fingerprint`. Selv om dette hovednøkkelfingeravtrykket ikke er sensitiv informasjon, vil det være nyttig for deg for å senere verifisere at du faktisk får tilgang til riktig lommebok og for å bekrefte fraværet av feil når du taster inn din passfrase.

Klikk på `Apply`-knappen.

![sparrow](assets/notext/15.webp)

Sparrow inviterer deg til å opprette et passord for lommeboken din. Dette passordet vil være nødvendig for å få tilgang til den via Sparrow Wallet-programvaren. Velg et sterkt passord, lag en sikkerhetskopi av det, og klikk deretter på `Set Password`.

![sparrow](assets/notext/16.webp)

### Motta bitcoins
Etter å ha opprettet lommeboken din, vil du i utgangspunktet ha en enkelt konto, med indeksen `0'`. Dette er **innskudds**kontoen vi snakket om i de tidligere delene. Dette er kontoen du trenger å sende bitcoins til for å blande dem.

For å gjøre dette, velg `Receive`-fanen på venstre side av vinduet. Sparrow vil automatisk generere en ny blank adresse for å motta bitcoins.

![sparrow](assets/notext/17.webp)

Du kan angi en etikett for denne adressen, og deretter sende bitcoinsene som skal blandes til den.

![sparrow](assets/notext/18.webp)

### Gjøre Tx0
Når transaksjonen din er bekreftet, kan du deretter gå til `UTXOs`-fanen.

![sparrow](assets/notext/19.webp)

Velg deretter UTXO(ene) du ønsker å sende inn til coinjoin-syklusene. For å velge flere UTXOer samtidig, hold nede `Ctrl`-tasten mens du klikker på UTXOene du velger.

![sparrow](assets/notext/20.webp)

Klikk deretter på `Mix Selected`-knappen nederst i vinduet. Hvis denne knappen ikke vises på grensesnittet ditt, er det fordi du er på en lommebok sikret med en maskinvarelommebok. Du må bruke en programvarelommebok for å utføre coinjoins med Sparrow.
![sparrow](assets/notext/21.webp)
Et vindu åpnes for å forklare hvordan Whirlpool fungerer. Dette er en forenkling av det jeg forklarte i de tidligere delene. Klikk på `Next` for å fortsette.

![sparrow](assets/notext/22.webp)

På neste side kan du angi en "SCODE" hvis du har en. En SCODE er en kampanjekode som tilbyr rabatt på tjenesteavgiftene i bassenget. Samourai Wallet gir av og til slike koder til sine brukere under spesielle hendelser. Jeg råder deg til å [følge Samourai Wallet](https://twitter.com/SamouraiWallet) på sosiale medier slik at du ikke går glipp av fremtidige SCODES.
På samme side må du også sette gebyrsatsen for `Tx0` og din første miks. Dette valget vil påvirke bekreftelseshastigheten for din forberedende transaksjon og din første coinjoin. Husk at du er ansvarlig for gruvegebyrene for `Tx0` og den første miksen, men du vil ikke skyldige gruvegebyrer for påfølgende remikser. Juster `Premix Priority`-skyveknappen i henhold til dine preferanser, og klikk deretter på `Next`.
![sparrow](assets/notext/23.webp)

I dette nye vinduet vil du ha muligheten til å velge bassenget du ønsker å gå inn i ved å bruke rullegardinlisten. I mitt tilfelle, etter å ha valgt en UTXO på `456 214 sats`, er mitt eneste mulige valg bassenget på `100 000 sats`. Dette grensesnittet informerer deg også om tjenestegebyrene som skal betales, samt antall UTXOer som vil bli integrert i bassenget. Hvis betingelsene virker tilfredsstillende for deg, fortsett ved å klikke på `Preview Premix`.

![sparrow](assets/notext/24.webp)

Etter dette trinnet vil Sparrow be deg om å angi passordet for lommeboken din, det du opprettet da du lagde den i programvaren. Når passordet er angitt, vil du få tilgang til forhåndsvisningen av din `Tx0`. På venstre side av vinduet ditt vil du se at Sparrow har generert de forskjellige kontoene som er nødvendige for å bruke Whirlpool (`Deposit`, `Premix`, `Postmix`, og `Badbank`). Du vil også ha muligheten til å se strukturen på din `Tx0`, med de forskjellige utgangene:
- Tjenestegebyrene;
- De likestilte UTXOene som er ment å gå inn i bassenget;
- Den giftige endringen (Doxxic Change).

![sparrow](assets/notext/25.webp)

Hvis transaksjonen er etter din smak, klikk på `Broadcast Transaction` for å kringkaste din `Tx0`. Ellers har du muligheten til å justere parameterne for denne `Tx0` ved å velge `Clear` for å slette inndataene og starte opprettelsesprosessen fra begynnelsen.

### Utføre Coinjoins
Når Tx0 er kringkastet, vil du finne dine UTXOer klare til å bli mikset i `Premix`-kontoen.
![sparrow](assets/notext/26.webp)

Når `Tx0` er bekreftet, vil dine UTXOer bli registrert hos koordinatoren, og de første mikseprosessene vil automatisk starte etter hverandre.

![sparrow](assets/notext/27.webp)

Ved å sjekke `Postmix`-kontoen, vil du observere UTXOene som resulterer fra de første mikseprosessene. Disse myntene vil forbli klare for påfølgende remiksing, som ikke vil medføre noen ekstra gebyrer.

![sparrow](assets/notext/28.webp)

I `Mixes`-kolonnen er det mulig å se antall coinjoins utført av hver av dine mynter. Som vi vil se i de følgende avsnittene, er det som virkelig betyr noe ikke så mye antallet remikser i seg selv, men heller de tilknyttede anonsettene, selv om disse to indikatorene er delvis relaterte.

![sparrow](assets/notext/29.webp)

For å midlertidig stoppe coinjoins, klikk bare på `Stop Mixing`. Du vil ha muligheten til å gjenoppta operasjonene når som helst ved å velge `Start Mixing`.

![sparrow](assets/notext/30.webp)
For å sikre kontinuerlig tilgjengelighet av dine UTXOer for omrøring, er det nødvendig å holde Sparrow-programvaren aktiv. Å lukke programvaren eller slå av datamaskinen vil pause coinjoins. En løsning for å omgå dette problemet er å deaktivere sovefunksjoner gjennom operativsystemets innstillinger. I tillegg tilbyr Sparrow et alternativ for å forhindre at datamaskinen automatisk går i dvale, som du kan finne under `Verktøy`-fanen med tittelen `Forhindre datamaskin i å sove`.
![sparrow](assets/notext/31.webp)

### Fullføring av coinjoins
For å bruke dine blandede bitcoins, har du flere alternativer. Den mest direkte metoden er å få tilgang til `Postmix`-kontoen og velge `Send`-fanen.

![sparrow](assets/notext/32.webp)

I denne delen vil du ha muligheten til å angi mottakeradressen, beløpet du vil sende, og transaksjonsgebyrene, på samme måte som for enhver annen transaksjon gjort med Sparrow Wallet. Hvis du ønsker, kan du også dra nytte av avanserte personvernfunksjoner som Stonewall, ved å klikke på `Personvern`-knappen.

![sparrow](assets/notext/33.webp)

[-> Lær mer om Stonewall-transaksjoner.](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)

Hvis du ønsker å gjøre et mer presist utvalg av dine mynter å bruke, gå til `UTXOer`-fanen. Velg UTXOene du spesifikt ønsker å forbruke, deretter trykk på `Send valgte`-knappen for å initiere transaksjonen.

![sparrow](assets/notext/34.webp)
Til slutt, `Bland til...`-alternativet tilgjengelig på Sparrow tillater automatisk fjerning av en valgt UTXO fra coinjoin-sykluser, uten å pådra seg ekstra gebyrer. Denne funksjonen muliggjør bestemmelsen av et antall omrøringer etter hvilket UTXOen ikke vil bli reintegrert i din `Postmix`-konto, men vil i stedet bli overført direkte til en annen lommebok. Dette alternativet brukes ofte til automatisk å sende blandede bitcoins til en kald lommebok.
For å bruke dette alternativet, start med å åpne mottakerlommeboken ved siden av din coinjoin-lommebok innenfor Sparrow-programvaren.

![sparrow](assets/notext/35.webp)

Deretter, gå til `UTXOer`-fanen, og klikk på `Bland til...`-knappen nederst i vinduet.

![sparrow](assets/notext/36.webp)

Et vindu åpnes, start med å velge destinasjonslommeboken fra rullegardinlisten.

![sparrow](assets/notext/37.webp)

Velg coinjoin-terskelen hvorpå uttaket vil bli gjort automatisk. Jeg kan ikke gi deg et eksakt antall omrøringer å utføre, da dette varierer i henhold til din personlige situasjon og dine personvernsmål, men unngå å velge en terskel for lav. Jeg anbefaler å konsultere denne andre artikkelen for å lære mer om omrøringsprosessen: [REMIX - WHIRLPOOL](https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa)

Du kan la `Indeksområde`-alternativet stå på sin standardverdi, `Full`. Denne funksjonen tillater blanding samtidig fra forskjellige klienter, men det er ikke det vi ønsker å gjøre i denne opplæringen. For å fullføre og aktivere `Bland til...`-alternativet, trykk `Start Whirlpool på nytt`.

![sparrow](assets/notext/38.webp)

Vær imidlertid forsiktig når du bruker `Bland til`-alternativet, da fjerning av blandede mynter fra din `Postmix`-konto kan øke risikoen for å kompromittere ditt personvern betydelig. Grunnene til dette potensialet er detaljert i de følgende seksjonene.

## Hvordan vite kvaliteten på våre coinjoin-sykluser?
For at en coinjoin skal være virkelig effektiv, er det essensielt at den presenterer god homogenitet mellom mengdene av innganger og utganger. Denne uniformiteten forsterker antallet mulige tolkninger i øynene til en ekstern observatør, og øker dermed usikkerheten rundt transaksjonen. For å kvantifisere denne usikkerheten generert av en coinjoin, kan man ty til å beregne transaksjonens entropi. For en grundig utforskning av disse indikatorene, henviser jeg deg til opplæringen: [BOLTZMANN CALCULATOR](https://planb.network/en/tutorials/privacy/boltzmann-entropy). Whirlpool-modellen er anerkjent som den som bringer mest homogenitet i coinjoins. Deretter evalueres ytelsen til flere coinjoin-sykluser basert på størrelsen på gruppene der en mynt er skjult. Størrelsen på disse gruppene definerer det som kalles anonsets. Det er to typer anonsets: den første vurderer personvernet oppnådd mot retrospektiv analyse (fra nåtiden til fortiden) og den andre, mot prospektiv analyse (fra fortiden til nåtiden). For en detaljert forklaring på disse to indikatorene, inviterer jeg deg til å konsultere opplæringen: [WHIRLPOOL STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)

## Hvordan håndtere postmix?
Etter å ha utført coinjoin-sykluser, er den beste strategien å holde dine UTXOer i **postmix**-kontoen, i påvente av deres fremtidige bruk. Det er til og med tilrådelig å la dem remixe på ubestemt tid til du trenger å bruke dem.

Noen brukere kan vurdere å overføre sine blandede bitcoins til en lommebok sikret av en hardware wallet. Dette er mulig, men det er viktig å følge anbefalingene fra Samourai Wallet nøye for ikke å kompromittere den oppnådde konfidensialiteten.

Å slå sammen UTXOer er den mest frekvente feilen som blir gjort. Det er nødvendig å unngå å kombinere blandede UTXOer med ublandede UTXOer i samme transaksjon, for å unngå CIOH (*Common-Input-Ownership-Heuristic*). Dette krever nøye håndtering av dine UTXOer innenfor din lommebok, spesielt når det gjelder merking. Utover coinjoin, er sammenslåing av UTXOer generelt en dårlig praksis som ofte fører til tap av personvern når det ikke håndteres riktig.

Det er også viktig å være forsiktig med å konsolidere blandede UTXOer med hverandre. Moderate konsolideringer er tenkelige hvis dine blandede UTXOer har betydelige anonsets, men dette vil uunngåelig redusere konfidensialiteten til myntene dine. Sørg for at konsolideringer verken er for store eller utført etter et utilstrekkelig antall remixes, da dette risikerer å etablere deduserbare koblinger mellom dine UTXOer før og etter coinjoin-syklusene. I tilfelle tvil om disse manipulasjonene, er den beste praksisen å ikke konsolidere postmix-UTXOene, og å overføre dem en etter en til din hardware wallet, og generere en ny blank adresse hver gang. Husk igjen å merke hver mottatt UTXO på riktig måte.
Det frarådes også å overføre dine postmix-UTXOer til en lommebok som bruker uvanlige skript. For eksempel, hvis du går inn i Whirlpool fra en multisig-lommebok som bruker `P2WSH`-skript, er det lite sjanse for at du vil bli blandet med andre brukere som opprinnelig har samme type lommebok. Hvis du trekker dine postmix til denne samme multisig-lommeboken, vil personvernivået til dine blandede bitcoins bli sterkt redusert. Utover skript, er det mange andre lommebokavtrykk som kan lure deg.
Som med enhver Bitcoin-transaksjon, er det også viktig å ikke gjenbruke mottaksadresser. Hver ny transaksjon bør mottas på en ny, blank adresse.
Den enkleste og sikreste løsningen er å la dine blandede UTXOer hvile i deres **postmix**-konto, la dem remixe og kun røre dem for å bruke. Samourai og Sparrow lommebøker har ekstra beskyttelser mot alle disse risikoene relatert til kjedeanalyse. Disse beskyttelsene hjelper deg med å unngå å gjøre feil.
## Hvordan håndtere doxxic endring?
Videre må du være forsiktig med å håndtere doxxic endring, endringen som ikke kunne gå inn i coinjoin-bassenget. Disse giftige UTXOene, som er et resultat av bruk av Whirlpool, utgjør en risiko for ditt personvern siden de etablerer en kobling mellom deg og bruk av coinjoin. Derfor er det avgjørende å håndtere dem med forsiktighet og ikke kombinere dem med andre UTXOer, spesielt blandede UTXOer. Her er forskjellige strategier å vurdere for å bruke dem:
- **Bland dem i mindre bassenger:** Hvis din giftige UTXO er stor nok til å gå inn i et mindre basseng alene, vurder å blande den. Dette er ofte det beste alternativet. Det er imidlertid avgjørende å ikke slå sammen flere giftige UTXOer for å få tilgang til et basseng, da dette kan koble dine forskjellige innganger;
- **Merk dem som "ikke-brukbare":** En annen tilnærming er å ikke lenger bruke dem, å merke dem som "ikke-brukbare" i deres dedikerte konto, og bare Hodl. Dette sikrer at du ikke ved et uhell bruker dem. Hvis verdien av bitcoin øker, kan nye bassenger bedre egnet for dine giftige UTXOer dukke opp;
- **Gjør donasjoner:** Vurder å gjøre donasjoner, selv beskjedne, til utviklere som jobber med Bitcoin og tilhørende programvare. Du kan også donere til organisasjoner som aksepterer BTC. Hvis håndtering av dine giftige UTXOer virker for komplisert, kan du enkelt kvitte deg med dem ved å gjøre en donasjon;
- **Kjøp gavekort:** Plattformer som [Bitrefill](https://www.bitrefill.com/) lar deg bytte bitcoins mot gavekort som kan brukes hos ulike handlende. Dette kan være en måte å kvitte seg med dine giftige UTXOer uten å miste den tilknyttede verdien.
- **Konsolider dem på Monero:** Samourai Wallet tilbyr nå en atombyttetjeneste mellom BTC og XMR. Dette er ideelt for å håndtere giftige UTXOer ved å konsolidere dem på Monero, uten å kompromittere ditt personvern via CIOH, før du sender dem tilbake til Bitcoin. Imidlertid kan dette alternativet være kostbart i form av gruvegebyrer og premien på grunn av likviditetsbegrensninger.
- **Send dem til Lightning Network:** Å overføre disse UTXOene til Lightning Network for å dra nytte av reduserte transaksjonsgebyrer er et alternativ som kan være interessant. Imidlertid kan denne metoden avsløre visse opplysninger avhengig av din bruk av Lightning og bør derfor praktiseres med forsiktighet.

Detaljerte veiledninger om implementering av disse forskjellige teknikkene vil snart bli tilbudt på PlanB Network.

**Tilleggsressurser:**
[Sparrow Wallet Video Tutorial](https://planb.network/tutorials/wallet/desktop/sparrow-7e9a77c0-013d-4f8e-a811-408b71dc7607)
[Samourai Wallet Video Tutorial](https://planb.network/tutorials/wallet/mobile/samourai-46f88b20-5d1e-47e0-be53-237ff8737956)
- [Samourai Wallet Dokumentasjon - Whirlpool](https://docs.samourai.io/whirlpool/basic-concepts);
- [Twitter-tråd om CoinJoins](https://twitter.com/SamouraiWallet/status/1489220847336308739);
- [Blogginnlegg om CoinJoins](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin).