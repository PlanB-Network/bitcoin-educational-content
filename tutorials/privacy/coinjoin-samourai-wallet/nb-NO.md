---
name: Coinjoin - Samourai Wallet
description: Hvordan utføre en coinjoin på Samourai Wallet?
---
![cover](assets/cover.webp)

***ADVARSEL:** Etter arrestasjonen av grunnleggerne av Samourai Wallet og beslagleggelsen av deres servere den 24. april, fungerer ikke lenger Whirlpool-verktøyet, selv for individer som har sin egen Dojo eller bruker Sparrow Wallet. Det er imidlertid fortsatt mulig at dette verktøyet kan bli gjeninnført i de kommende ukene eller relansert på en annen måte. Videre forblir den teoretiske delen av denne artikkelen relevant for å forstå prinsippene og målene med coinjoins generelt (ikke bare Whirlpool), samt forstå effektiviteten av Whirlpool-modellen.*

_Vi følger nøye med på utviklingen av denne saken samt utviklingen angående de tilknyttede verktøyene. Vær trygg på at vi vil oppdatere denne opplæringen etter hvert som ny informasjon blir tilgjengelig._

_Denne opplæringen er gitt kun til utdannings- og informasjonsformål. Vi støtter eller oppfordrer ikke til bruk av disse verktøyene til kriminelle formål. Det er hver brukers ansvar å overholde lovene i sin jurisdiksjon._

---

"*en bitcoin-lommebok for gatene*"

I denne opplæringen vil du lære hva en coinjoin er og hvordan du utfører en ved hjelp av Samourai Wallet-programvaren og Whirlpool-implementeringen.

## Hva er en coinjoin på Bitcoin?
**Coinjoin er en teknikk som bryter sporbarheten til bitcoins på blockchain**. Den stoler på en samarbeidstransaksjon med en spesifikk struktur med samme navn: coinjoin-transaksjonen.

Coinjoins forbedrer personvernet til Bitcoin-brukere ved å komplisere kjedeanalyse for eksterne observatører. Deres struktur tillater sammenslåing av flere mynter fra forskjellige brukere i en enkelt transaksjon, og dermed skjuler sporene og gjør det vanskelig å bestemme koblingene mellom inngangs- og utgangsadresser.

Prinsippet om coinjoin er basert på en samarbeidstilnærming: flere brukere som ønsker å blande sine bitcoins, setter inn identiske beløp som innganger i samme transaksjon. Disse beløpene blir deretter redistribuert som utganger av lik verdi til hver bruker. Ved slutten av transaksjonen blir det umulig å knytte en spesifikk utgang med en kjent bruker i inngang. Ingen direkte kobling eksisterer mellom inngangene og utgangene, noe som bryter assosiasjonen mellom brukerne og deres UTXO, samt historikken til hver mynt.
![coinjoin](assets/notext/1.webp)

Eksempel på en coinjoin-transaksjon (ikke fra meg): [323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://mempool.space/en/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)

For å utføre en coinjoin samtidig som hver bruker opprettholder kontroll over sine midler til enhver tid, begynner prosessen med konstruksjonen av transaksjonen av en koordinator, som deretter overfører den til deltakerne. Hver bruker signerer deretter transaksjonen etter å ha verifisert at den passer for dem. Alle innsamlede signaturer integreres til slutt i transaksjonen. Hvis et forsøk på å avlede midler blir gjort av en bruker eller koordinatoren, ved å endre utgangene av coinjoin-transaksjonen, vil signaturene vise seg å være ugyldige, noe som fører til at transaksjonen avvises av nodene.

Det finnes flere implementeringer av coinjoin, som Whirlpool, JoinMarket, eller Wabisabi, hver med mål om å håndtere koordinering blant deltakere og øke effektiviteten av coinjoin-transaksjoner.
I denne veiledningen skal vi dykke ned i implementeringen av **Whirlpool**, som jeg anser for å være den mest effektive løsningen for å utføre coinjoins på Bitcoin. Selv om det er tilgjengelig på flere lommebøker, vil vi i denne veiledningen utelukkende utforske bruken av det med Samourai Wallet mobilapplikasjonen, uten Dojo.
## Hvorfor utføre coinjoins på Bitcoin?
Et av de første problemene med ethvert peer-to-peer betalingssystem er dobbeltutgifter: hvordan forhindre at ondsinnede individer bruker de samme pengeenhetene flere ganger uten å måtte ty til en sentral autoritet for å megle?

Satoshi Nakamoto tilbød en løsning på dette dilemmaet gjennom Bitcoin-protokollen, et peer-to-peer elektronisk betalingssystem som opererer uavhengig av enhver sentral autoritet. I hans hvitbok fremhever han at den eneste måten å sertifisere fraværet av dobbeltutgifter på, er å sikre synligheten av alle transaksjoner innen betalingssystemet.

For å garantere at hver deltaker er klar over transaksjonene, må de offentliggjøres. Derfor er driften av Bitcoin avhengig av en transparent og distribuert infrastruktur, som tillater enhver nodoperatør å verifisere helheten av de elektroniske signaturkjedene og historikken til hver mynt, fra dens skapelse av en miner.

Den transparente og distribuerte naturen til Bitcoins blockchain betyr at enhver nettverksbruker kan følge og analysere transaksjonene til alle andre deltakere. Som et resultat er anonymitet på transaksjonsnivå umulig. Imidlertid bevares anonymiteten på individnivå. I motsetning til det tradisjonelle banksystemet hvor hver konto er knyttet til en personlig identitet, er midler på Bitcoin assosiert med par av kryptografiske nøkler, og tilbyr dermed brukerne en form for pseudonymitet bak kryptografiske identifikatorer.

Således er konfidensialiteten på Bitcoin kompromittert når eksterne observatører klarer å assosiere spesifikke UTXOer med identifiserte brukere. Når denne assosiasjonen er etablert, blir det mulig å spore deres transaksjoner og analysere historikken til deres bitcoins. Coinjoin er nettopp en teknikk utviklet for å bryte sporbarheten til UTXOer, og tilbyr dermed et visst lag av konfidensialitet til Bitcoin-brukere på transaksjonsnivå.

## Hvordan fungerer Whirlpool?
Whirlpool skiller seg ut fra andre coinjoin-metoder ved å bruke "_ZeroLink_" transaksjoner, som sikrer at det strengt tatt ikke er mulig med noen teknisk kobling mellom alle inngangene og alle utgangene. Denne perfekte blandingen oppnås gjennom en struktur hvor hver deltaker bidrar med et identisk beløp i inngang (bortsett fra gruvegebyrer), og dermed genererer utganger av perfekt like beløp.
Denne restriktive tilnærmingen til innganger gir Whirlpool coinjoin-transaksjoner en unik egenskap: total fravær av deterministiske koblinger mellom innganger og utganger. Med andre ord, hver utgang har en like stor sannsynlighet for å bli tilskrevet enhver deltaker, sammenlignet med alle andre utganger i transaksjonen.
Opprinnelig var antallet deltakere i hver Whirlpool coinjoin begrenset til 5, med 2 nye deltakere og 3 remixere (vi vil forklare disse konseptene videre). Imidlertid førte økningen i on-chain transaksjonsgebyrer observert i 2023 til at Samourai-teamene måtte revurdere modellen sin for å forbedre personvernet samtidig som kostnadene reduseres. Således, med tanke på markedsituasjonen for gebyrer og antall deltakere, kan koordinatoren nå organisere coinjoins inkludert 6, 7, eller 8 deltakere. Disse forbedrede øktene refereres til som "_Surge Cycles_". Det er viktig å merke seg at, uavhengig av konfigurasjonen, er det alltid bare 2 nye deltakere i Whirlpool coinjoins.

Således er Whirlpool-transaksjoner kjennetegnet ved et identisk antall innganger og utganger, som kan være:
- 5 innganger og 5 utganger;
![coinjoin](assets/notext/2.webp)
- 6 innganger og 6 utganger;
![coinjoin](assets/notext/3.webp)
- 7 innganger og 7 utganger;
![coinjoin](assets/notext/4.webp) - 8 innganger og 8 utganger.
![coinjoin](assets/notext/5.webp)
Modellen foreslått av Whirlpool er dermed basert på små coinjoin-transaksjoner. I motsetning til Wasabi og JoinMarket, hvor robustheten til anonsetene er avhengig av volumet av deltakere i en enkelt syklus, satser Whirlpool på kjeding av flere små sykluser.

I denne modellen betaler brukeren gebyrer kun ved sin første inngang i en pool, noe som tillater dem å delta i en mengde remixes uten ekstra gebyrer. Det er de nye deltakerne som dekker gruvegebyrene for remixerne.

Med hver tilleggs coinjoin som en mynt deltar i, sammen med sine tidligere møtte jevnaldrende, vil anonsetene vokse eksponentielt. Målet er derfor å dra nytte av disse gratis remixene som, ved hver forekomst, bidrar til å styrke tettheten av anonsetene assosiert med hver blandet mynt.

Whirlpool ble designet med tanke på to viktige krav:
- Tilgjengeligheten av implementering på mobile enheter, gitt at Samourai Wallet primært er en smarttelefonapplikasjon;
- Hastigheten på remixing-syklusene for å fremme en betydelig økning i anonsetene.
Disse imperativene veiledet utviklerne av Samourai Wallet i designet av Whirlpool, noe som førte dem til å begrense antall deltakere per syklus. For få deltakere ville ha kompromittert effektiviteten av coinjoin, drastisk redusert anonsetene generert hver syklus, mens for mange deltakere ville ha utgjort forvaltningsproblemer på mobilapplikasjoner og ville ha hindret flyten av sykluser.
**Til syvende og sist er det ikke nødvendig å ha et høyt antall deltakere per coinjoin på Whirlpool siden anonsetene oppnås gjennom akkumulering av flere coinjoin-sykluser.**

[-> Lær mer om Whirlpool anonseter.](https://planb.network/tutorials/privacy/wst-anonsets)

### Bassengene og coinjoin-gebyrene
For at disse flere syklusene effektivt skal øke anonsetene til de blandete myntene, må et visst rammeverk etableres for å begrense mengdene av UTXO som brukes. Whirlpool definerer dermed forskjellige bassenger.

Et basseng representerer en gruppe brukere som ønsker å blande sammen, som er enige om mengden UTXO som skal brukes for å optimalisere coinjoin-prosessen. Hvert basseng spesifiserer et fast beløp for UTXO, som brukeren må overholde for å delta. Således, for å utføre coinjoins med Whirlpool, må du velge et basseng. Bassengene som for øyeblikket er tilgjengelige er som følger:
- 0,5 bitcoins;
- 0,05 bitcoin;
- 0,01 bitcoin;
- 0,001 bitcoin (= 100 000 sats).

Ved å bli med i et basseng med dine bitcoins, vil de bli delt for å generere UTXOer som er fullstendig homogene med de til de andre deltakerne i bassenget. Hvert basseng har en maksimal grense; dermed, for beløp som overstiger denne grensen, vil du bli tvunget enten til å gjøre to separate innganger innenfor samme basseng eller å orientere deg mot et annet basseng med et høyere beløp:

| Basseng (bitcoin) | Maksimalt beløp per inngang (bitcoin) |
|-------------------|---------------------------------------|
| 0,5               | 35                                    |
| 0,05              | 3,5                                   |
| 0,01              | 0,7                                   |
| 0,001             | 0,025                                 |
Som nevnt tidligere, anses en UTXO for å tilhøre en pool når den er klar til å bli integrert i en coinjoin. Dette betyr imidlertid ikke at brukeren mister besittelsen av den. **Gjennom de forskjellige mikse-syklusene beholder du full kontroll over dine nøkler og, dermed, dine bitcoins.** Dette er det som skiller coinjoin-teknikken fra andre sentraliserte mikseteknikker.
For å delta i en coinjoin-pool, må tjenesteavgifter samt miningavgifter betales. Tjenesteavgiftene er faste for hver pool og er ment å kompensere teamene ansvarlige for utvikling og vedlikehold av Whirlpool.
Tjenesteavgifter for å bruke Whirlpool skal kun betales én gang ved inngangen til poolen. Etter dette trinnet har du muligheten til å delta i et ubegrenset antall remixes uten noen ekstra avgifter. Her er de nåværende faste avgiftene for hver pool:

| Pool (bitcoin) | Inngangsavgift (bitcoin) |
|----------------|-------------------------|
| 0.5            | 0.0175                  |
| 0.05           | 0.00175                 |
| 0.01           | 0.0005 (50,000 sats)    |
| 0.001          | 0.00005 (5,000 sats)    |


Disse avgiftene fungerer i hovedsak som en inngangsbillett for den valgte poolen, uavhengig av beløpet du legger i coinjoin. Så, enten du blir med i 0.01-poolen med nøyaktig 0.01 BTC eller går inn i den med 0.5 BTC, vil avgiftene forbli de samme i absolutt verdi.

Før man går videre til coinjoins, har brukeren dermed et valg mellom 2 strategier:
- Velge en mindre pool for å minimere tjenesteavgifter, vel vitende om at de vil motta flere små UTXOer i retur;
- Eller foretrekke en større pool, og gå med på å betale høyere avgifter for å ende opp med et redusert antall UTXOer av større verdi.

Det anbefales generelt å ikke slå sammen flere miksete UTXOer etter coinjoin-syklusene, da dette kan kompromittere den oppnådde konfidensialiteten, spesielt på grunn av Common-Input-Ownership Heuristic (CIOH). Derfor kan det være lurt å velge en større pool, selv om det betyr å betale mer, for å unngå å ha for mange småverdi UTXOer som output. Brukeren må veie disse kompromissene for å velge den poolen de foretrekker.

I tillegg til tjenesteavgiftene, må også miningavgiftene som er iboende i enhver Bitcoin-transaksjon, vurderes. Som Whirlpool-bruker vil du være nødt til å betale miningavgiftene for forberedelsestransaksjonen (`Tx0`) samt de for den første coinjoin. Alle påfølgende remixes vil være gratis, takket være Whirlpools modell som stoler på betalingen fra nye deltakere.

Faktisk, i hver Whirlpool coinjoin, er to brukere blant inngangene nye deltakere. De andre inngangene kommer fra remixere. Som et resultat, dekkes miningavgiftene for alle deltakerne i transaksjonen av disse to nye deltakerne, som da også vil dra nytte av gratis remixes:
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

Hver av disse kontoene oppfyller en spesifikk funksjon innenfor coinjoin-prosessen.

Alle disse kontoene er knyttet til et enkelt frø, som lar brukeren gjenopprette tilgang til alle sine bitcoins ved hjelp av deres gjenopprettingsfrase og, om aktuelt, deres passfrase. Det er imidlertid nødvendig å spesifisere til programvaren, under denne gjenopprettingsoperasjonen, de forskjellige kontoindeksene som ble brukt.

La oss nå se på de forskjellige stadiene av en Whirlpool coinjoin innenfor disse kontoene.

### De forskjellige stadiene av coinjoins på Whirlpool
**Steg 1: Tx0**
Utgangspunktet for enhver Whirlpool coinjoin er **innskudds**kontoen. Denne kontoen er den du automatisk bruker når du oppretter en ny Bitcoin-lommebok. Denne kontoen må krediteres med bitcoins som man ønsker å blande.
`Tx0` representerer det første steget i Whirlpool-blandingsprosessen. Målet er å forberede og likestille UTXO for coinjoin, ved å dele dem inn i enheter som tilsvarer beløpet til det valgte bassenget, for å sikre homogeniteten til blandingen. De likestilte UTXOene sendes deretter til **premix**-kontoen. Når det gjelder differansen som ikke kan gå inn i bassenget, blir den skilt ut i en spesifikk konto: **dårlig bank** (eller "doxxic change").
Denne innledende transaksjonen `Tx0` tjener også til å avregne tjenestegebyrene til blandingskoordinatoren. I motsetning til de følgende trinnene, er denne transaksjonen ikke samarbeidsvillig; brukeren må derfor påta seg alle gruvegebyrene:
![coinjoin](assets/en/7.webp)

I dette eksemplet på en `Tx0`-transaksjon, deles et innskudd på `372,000 sats` fra vår **innskudds**konto inn i flere utgående UTXO, som er fordelt som følger:
- Et beløp på `5,000 sats` ment for koordinatoren for tjenestegebyrer, som tilsvarer inngangen til bassenget på `100,000 sats`;
- Tre UTXO forberedt for blanding, omdirigert til vår **premix**-konto og registrert hos koordinatoren. Disse UTXOene er likestilt på `108,000 sats` hver, for å dekke gruvegebyrene for deres fremtidige innledende blanding;
- Overskuddet som ikke kan gå inn i bassenget, fordi det er for lite, anses som giftig veksel. Det sendes til sin spesifikke konto. Her utgjør denne vekselen `40,000 sats`;
- Til slutt er det `3,000 sats` som ikke utgjør en utgang, men er gruvegebyrene som er nødvendige for å bekrefte `Tx0`.

For eksempel, her er en ekte Whirlpool Tx0 (ikke fra meg): [edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46](https://mempool.space/en/tx/edef60744f539483d868caff49d4848e5cc6e805d6cdc8d0f9bdbbaedcb5fc46)

**Steg 2: Den giftige vekselen**
Overskuddet som ikke kunne integreres i bassenget, her tilsvarende `40,000 sats`, blir omdirigert til **dårlig bank**-kontoen, også referert til som "giftig veksel", for å sikre en streng separasjon fra de andre UTXO i lommeboken.

Denne UTXO er farlig for brukerens personvern, ettersom den ikke bare fortsatt er knyttet til sin fortid, og dermed muligens til identiteten til eieren, men i tillegg er den merket som tilhørende en bruker som har utført en coinjoin.
Hvis denne UTXO blir slått sammen med blandete utganger, vil de miste all konfidensialiteten oppnådd under coinjoin-syklusene, spesielt på grunn av Common-Input-Ownership-Heuristic (CIOH). Hvis den slås sammen med andre giftige veksler, risikerer brukeren å miste konfidensialitet siden dette vil koble de forskjellige inngangene fra coinjoin-syklusene. Derfor må den håndteres med forsiktighet. Måten å håndtere denne giftige UTXO på vil bli detaljert i den siste delen av denne artikkelen, og fremtidige veiledninger vil dekke disse metodene mer inngående på PlanB Network.

**Steg 3: Den første blandingen**
Etter at `Tx0` er fullført, sendes de likestilte UTXOene til **premix**-kontoen i vår lommebok, klare til å bli introdusert i deres første coinjoin-syklus, også kalt "initial mix". Hvis, som i vårt eksempel, `Tx0` genererer flere UTXOer for blanding, vil hver av dem bli integrert i en separat første coinjoin.

Ved slutten av disse første blandene, vil **premix**-kontoen være tom, mens våre mynter, etter å ha betalt gruvegebyrene for denne første coinjoin, vil bli justert nøyaktig til beløpet definert av det valgte bassenget. I vårt eksempel vil våre opprinnelige UTXOer på `108 000 sats` ha blitt redusert til nøyaktig `100 000 sats`.
![coinjoin](assets/en/8.webp)
**Steg 4: Remixene**
Etter den første blandingen, overføres UTXOene til **postmix**-kontoen. Denne kontoen samler de allerede blandete UTXOene og de som venter på remixing. Når Whirlpool-klienten er aktiv, er UTXOene i **postmix**-kontoen automatisk tilgjengelige for remixing og vil bli tilfeldig valgt for å delta i disse nye syklusene.

Som en påminnelse, er remixene deretter 100% gratis: ingen ekstra tjenestegebyrer eller gruvegebyrer kreves. Å holde UTXOene i **postmix**-kontoen opprettholder dermed deres verdi intakt og forbedrer samtidig deres anonsets. Det er derfor det er viktig å tillate disse myntene å delta i flere coinjoin-sykluser. Det koster deg strengt tatt ingenting, og det øker deres nivåer av anonymitet.
Når du bestemmer deg for å bruke blandede UTXOer, kan du gjøre dette direkte fra denne **postmix**-kontoen. Det er tilrådelig å beholde de blandede UTXOene på denne kontoen for å dra nytte av gratis remixes og for å unngå at de forlater Whirlpool-kretsen, noe som kunne redusere deres konfidensialitet.
Som vi vil se i den følgende opplæringen, finnes det også en `mix to`-mulighet som tilbyr muligheten til automatisk å sende dine blandede mynter til en annen lommebok, som for eksempel en kald lommebok, etter et definert antall coinjoins.
Etter å ha dekket teorien, la oss dykke inn i praksis med en opplæring i bruk av Whirlpool gjennom Samourai Wallet Android-appen!
## Opplæring: Coinjoin Whirlpool på Samourai Wallet
Det finnes mange muligheter for å bruke Whirlpool. Den jeg ønsker å introdusere her, er Samourai Wallet-alternativet (uten Dojo), en åpen kildekode Bitcoin lommebokforvaltningsapplikasjon på Android.

Å mikse på Samourai uten Dojo har fordelen av å være ganske enkelt å håndtere, raskt å sette opp, og krever ikke annet utstyr enn en Android-telefon og en internettforbindelse.

Men, denne metoden har to bemerkelsesverdige ulemper:
- Coinjoins vil kun skje når Samourai kjører i bakgrunnen og er tilkoblet. Dette betyr at hvis du ønsker å mikse og remixe dine bitcoins 24/7, må du konstant holde Samourai påslått;
- Hvis du bruker Whirlpool med Samourai Wallet uten å ta deg bryet med å koble til din egen Dojo, så må applikasjonen din koble til serveren som vedlikeholdes av Samourai-teamene, og du vil avsløre `xpub` fra lommeboken din til dem. Disse anonyme informasjonsbitene er nødvendige for at applikasjonen din skal finne transaksjonene dine.

Den ideelle løsningen for å overkomme disse begrensningene er å operere din egen Dojo assosiert med en Whirlpool CLI-instans på din personlige Bitcoin-node. På denne måten vil du unngå lekkasje av informasjon og oppnå fullstendig uavhengighet. Selv om opplæringen presentert nedenfor er nyttig for visse mål eller for nybegynnere, anbefales det å bruke din egen Dojo for å virkelig optimalisere din coinjoin-økt. En detaljert guide om å sette opp denne konfigurasjonen vil snart være tilgjengelig på PlanB Network.

### Installere Samourai Wallet
For å starte, vil du åpenbart trenge Samourai Wallet-appen. Du kan laste den ned direkte fra det offisielle nettstedet ved å bruke APK, fra deres GitLab, eller fra Google Play Store.

### Opprette en programvarelommebok
Etter å ha installert programvaren, må du fortsette med å opprette en Bitcoin-lommebok på Samourai. Hvis du allerede har en, kan du hoppe direkte til neste steg.

Når du åpner applikasjonen, trykk på den blå `Start`-knappen. Du vil da bli bedt om å velge en plassering i telefonens filer hvor den krypterte sikkerhetskopien av din nye lommebok vil bli lagret.

![samourai](assets/notext/9.webp)
Aktiver Tor ved å klikke på den tilsvarende hakken. På dette stadiet har du også muligheten til å velge en spesifikk Dojo. Men, i denne opplæringen, vil vi fortsette med standard Dojo; så du kan la alternativet være deaktivert. Når Tor er tilkoblet, trykk på `Create a new wallet`-knappen.
![samourai](assets/notext/10.webp)

Samourai Wallet ber deg deretter om å sette en BIP39-passfrase. Dette ekstra passordet er veldig viktig da det direkte virker på derivasjonen av dine private nøkler. Et potensielt tap av denne passfrasen ville resultere i manglende evne til å få tilgang til dine bitcoins, noe som gjør dem ugjenkallelig tapt. For å gjenopprette din Samourai-lommebok, er det avgjørende å ha både din 12-ords gjenopprettingsfrase og passfrasen.
Det er derfor avgjørende å velge en robust passfrase og lage en eller flere fysiske kopier, på papir eller på et metallisk medium, for å sikre sikkerheten til dine bitcoins. Etter å ha fullført disse oppgavene, merk av i boksen `Jeg er klar over at i tilfelle tap...`, deretter trykk på `NESTE`-knappen.
![samourai](assets/notext/11.webp)

Du må deretter definere en PIN-kode som består av 5 til 8 sifre. Denne koden vil sikre tilgangen til lommeboken din på telefonen din. Den vil bli forespurt hver gang du ønsker å åpne Samourai-applikasjonen. Velg en robust PIN-kode og sørg for å beholde en sikkerhetskopi. Etter det kan du trykke på `NESTE`-knappen.

![samourai](assets/notext/12.webp)

Samourai vil invitere deg til å angi PIN-koden din igjen for bekreftelse. Skriv den inn, deretter trykk `FULLFØR`.

![samourai](assets/notext/13.webp)

Du vil da få tilgang til din gjenopprettingsfrase bestående av 12 ord. Denne frasen lar deg gjenopprette lommeboken din med den tidligere angitte passfrasen. Det anbefales sterkt å lage en eller flere kopier av denne frasen på fysiske medier, som papir eller et metallisk materiale, for å sikre sikkerheten til dine bitcoins i tilfelle et problem.

Etter å ha laget disse sikkerhetskopiene, vil du bli dirigert til grensesnittet til din nye Samourai-lommebok.

![samourai](assets/notext/14.webp)

Du får tilbud om å skaffe din PayNym Bot. Du kan be om den hvis du ønsker, selv om den ikke er essensiell for vår opplæring.

![samourai](assets/notext/15.webp)
Før du fortsetter med å motta bitcoins på denne nye lommeboken, anbefales det sterkt å dobbeltsjekke gyldigheten av sikkerhetskopiene dine (passfrasen og gjenopprettingsfrasen). For å verifisere passfrasen, kan du velge ikonet til din PayNym Bot som ligger øverst til venstre på skjermen, deretter følge stien:
```plaintext
Innstillinger > Feilsøking > Passfrase/sikkerhetskopi-test
```

Skriv inn passfrasen din for å utføre verifiseringen.

![samourai](assets/notext/16.webp)

Samourai vil bekrefte om den er gyldig.

![samourai](assets/notext/17.webp)

For å verifisere sikkerhetskopien av gjenopprettingsfrasen din, tilgang ikonet til din PayNym Bot, som ligger øverst til venstre på skjermen, og følg denne stien:
```plaintext
Innstillinger > Lommebok > Vis 12-ords gjenopprettingsfrase
```

Samourai vil vise et vindu med gjenopprettingsfrasen din. Sørg for at den stemmer nøyaktig overens med din fysiske sikkerhetskopi.

For å gå videre og utføre en komplett gjenopprettingstest, noter et vitneelement av lommeboken din, som en av `xpubs`, deretter fortsett til å slette lommeboken din (forutsatt at den fortsatt er tom). Målet er å prøve å gjenopprette denne tomme lommeboken ved å bruke kun dine fysiske sikkerhetskopier. Hvis gjenopprettingen er vellykket, indikerer dette at sikkerhetskopiene dine er gyldige og pålitelige.

### Motta bitcoins
Etter å ha opprettet lommeboken din, vil du starte med en enkelt konto, identifisert med indeksen `0'`. Dette er **innskudds**kontoen vi snakket om i de tidligere delene. Det er til denne kontoen du må overføre bitcoinsene som er ment for coinjoins.

For å gjøre dette, klikk på det blå `+`-symbolet som ligger nederst til høyre på skjermen.

![samourai](assets/notext/18.webp)

Deretter klikker du på den grønne `Motta`-knappen.

![samourai](assets/notext/19.webp)

Samourai vil automatisk generere en ny tom adresse for å motta bitcoins.

![samourai](assets/notext/20.webp)
Du kan sende bitcoinene dine for å bli blandet der.
![samourai](assets/notext/21.webp)

### Lage Tx0
Når transaksjonen er bekreftet, kan vi starte coinjoins-prosessen. For å gjøre dette, klikk på den blå `+`-knappen nederst til høyre på skjermen.

![samourai](assets/notext/22.webp)

Deretter klikker du på `Whirlpool` i blått.

![samourai](assets/notext/23.webp)

Vent mens Whirlpool initialiseres og Samourai oppretter de nødvendige kontoene.

![samourai](assets/notext/24.webp)

Du vil da komme til Whirlpool-hjemmesiden. Klikk på `Start`.
![samourai](assets/notext/25.webp)
Velg UTXO fra **innskudds**kontoen som du ønsker å sende i coinjoin-sykluser, deretter klikker du på `Neste`.

![samourai](assets/notext/26.webp)

I neste steg må du velge gebyrnivået som skal tildeles `Tx0` samt til din første miks. Denne innstillingen vil bestemme hastigheten på din `Tx0` og din første coinjoin (eller første coinjoins) vil bli bekreftet. Husk at gruvegebyrene for `Tx0` og den første miksen er ditt ansvar, men du vil ikke måtte betale gruvegebyrer for de påfølgende remixene. Du har valget mellom `Lav`, `Normal`, eller `Høy` alternativer.

![samourai](assets/notext/27.webp)

I samme vindu har du muligheten til å velge bassenget du vil gå inn i. Gitt at jeg opprinnelig valgte en UTXO på `454,258 sats`, er mitt eneste mulige valg `100,000 sats`-bassenget. Denne siden presenterer deg også for bassengets tjenestegebyrer, i tillegg til gruvegebyrene, som lar deg vite den totale kostnaden for denne coinjoin-syklusen. Hvis alt passer for deg, velg det passende bassenget og fortsett ved å klikke på den blå `VERIFISER SYKLUSDETALJER`-knappen.

![samourai](assets/notext/28.webp)

Du kan deretter se alle detaljene i din coinjoin-syklus:
- antall UTXOer som vil gå inn i bassenget;
- de forskjellige påløpte gebyrene;
- mengden av doxxic endring...

Verifiser informasjonen, deretter klikk på den grønne `START SYKLUS`-knappen.

![samourai](assets/notext/29.webp)

Et vindu vil dukke opp for å tilby deg å merke den toksiske endringen som følge av din inngang i coinjoin-syklusen som "ikke-utgiftbar". Ved å velge `JA`, vil denne UTXOen ikke være synlig i lommeboken din og kan ikke velges for fremtidige transaksjoner. Imidlertid vil den forbli tilgjengelig i listen over UTXOer i lommeboken din, hvor du manuelt kan endre statusen dens. Det anbefales å velge dette alternativet for å unngå eventuelle håndteringsfeil som kan kompromittere personvernet ditt senere. Hvis du velger `NEI`, vil den toksiske endringen forbli tilgjengelig for bruk i lommeboken din. Hvis du vil lære mer om håndtering og bruk av denne toksiske endringen, anbefaler jeg at du leser den siste delen av denne opplæringen.

![samourai](assets/notext/30.webp)

Samourai vil deretter kringkaste din Tx0.

![samourai](assets/notext/31.webp)

### Gjennomføre coinjoins
Når Tx0 er kringkastet, kan du finne den i `Transaksjoner`-fanen i Whirlpool-menyen.

![samourai](assets/notext/32.webp)
Dine UTXOer klare for å bli blandet finnes i `Mixing in progress...`-fanen, som tilsvarer **Premix**-kontoen. ![samourai](assets/notext/33.webp)

Når `Tx0` er bekreftet, vil dine UTXOer automatisk bli registrert hos koordinatoren, og de innledende blandingsrundene vil starte suksessivt på en automatisk måte.

![samourai](assets/notext/34.webp)

Ved å sjekke `Remixing`-fanen, som tilsvarer **Postmix**-kontoen, vil du observere UTXOene som kommer fra de innledende blandingsrundene. Disse myntene vil forbli klare for påfølgende om-blanding, som ikke vil medføre noen ekstra gebyrer. Jeg anbefaler å konsultere denne andre artikkelen for å lære mer om om-blandingsprosessen og effektiviteten av en coinjoin-syklus: [REMIX - WHIRLPOOL](https://planb.network/tutorials/privacy/remix-whirlpool)

![samourai](assets/notext/35.webp)

Det er mulig å midlertidig suspendere om-blandingen av en UTXO ved å trykke på pauseknappen som er plassert til høyre for den. For å gjøre den kvalifisert for om-blanding igjen, klikk bare på samme knapp en gang til. Det er viktig å merke seg at bare én coinjoin kan utføres per bruker og per basseng samtidig. Så, hvis du har 6 UTXOer på `100 000 sats` klare for coinjoin, kan bare en av dem blandes. Etter å ha blandet en UTXO, fortsetter Samourai Wallet med å tilfeldig velge en ny UTXO fra din tilgjengelighet, for å diversifisere og balansere om-blandingen av hver mynt.

![samourai](assets/notext/36.webp)

For å sikre kontinuerlig tilgjengelighet av dine UTXOer for om-blanding, er det nødvendig å holde Samourai-applikasjonen aktiv i bakgrunnen. Du bør se en notifikasjon på telefonen din som bekrefter at Whirlpool kjører. Å lukke applikasjonen eller slå av telefonen din vil pause coinjoins.

### Fullføre coinjoins
For å bruke dine blandete bitcoins, gå til **Postmix**-kontoen merket `Remixing` i Whirlpool-menyfanene.

![samourai](assets/notext/37.webp)

Klikk på det blå Whirlpool-logoen som er plassert nederst til høyre.

![samourai](assets/notext/38.webp)

Deretter klikker du på `Spend Mixed UTXOs`.

![samourai](assets/notext/39.webp)

Du kan deretter angi mottakerens adresse og beløpet du vil sende, på samme måte som for enhver annen transaksjon gjort med Samourai Wallet. Den blå bakgrunnen indikerer at midlene blir brukt fra en Whirlpool-konto, og ikke fra **innskudds**kontoen.

![samourai](assets/notext/40.webp)

Ved å klikke på de 3 små prikkene øverst til høyre, har du muligheten til å velge spesifikke UTXOer.
![samourai](assets/notext/41.webp)
Ved å klikke på det hvite kvadratet øverst til høyre i vinduet, kan du skanne QR-koden til mottakeradressen med kameraet ditt.

![samourai](assets/notext/42.webp)

Angi nødvendig informasjon for din utgiftstransaksjon, og klikk deretter på den blå `VERIFY TRANSACTION`-knappen.

![samourai](assets/notext/43.webp)
I neste steg har du muligheten til å endre gebyrsatsen som er knyttet til transaksjonen din. Du kan også aktivere Stonewall-alternativet ved å krysse av i den tilsvarende boksen. Hvis Stonewall-alternativet ikke er valgbart, betyr det at din **Postmix**-konto ikke inneholder en UTXO av tilstrekkelig størrelse til å støtte denne spesifikke transaksjonsstrukturen.
[-> Lær mer om Stonewall-transaksjoner.](https://planb.network/tutorials/privacy/stonewall)

Hvis alt er til din tilfredshet, klikk på den grønne `SEND ... BTC`-knappen.

![samourai](assets/notext/44.webp)

Samourai vil deretter fortsette å signere transaksjonen din før den kringkastes på nettverket. Du trenger bare å vente til den er lagt til i en blokk av en miner.

![samourai](assets/notext/45.webp)

### Bruke en SCODE
Noen ganger tilbyr Samourai Wallet-teamene "SCODEs". En SCODE er en kampanjekode som gir rabatt på tjenestegebyrene i bassenget. Samourai Wallet tilbyr av og til slike koder til sine brukere under spesielle hendelser. Jeg råder deg [til å følge Samourai Wallet](https://twitter.com/SamouraiWallet) på sosiale medier for ikke å gå glipp av fremtidige SCODES.

For å bruke en SCODE på Samourai, før du starter en ny coinjoin-syklus, gå til Whirlpool-menyen og velg de tre små prikkene som ligger øverst til høyre på skjermen.

![samourai](assets/notext/46.webp)

Klikk på `SCODE (promo code) Whirlpool`.

![samourai](assets/notext/47.webp)

Skriv inn SCODE i vinduet som åpnet seg, og bekreft ved å klikke på `OK`.

![samourai](assets/notext/48.webp)

Whirlpool vil automatisk lukke seg. Vent på at Samourai skal bli ferdig med å laste, og åpne deretter Whirlpool-menyen igjen.

![samourai](assets/notext/49.webp)

Sørg for at din SCODE har blitt korrekt registrert ved å klikke en gang til på de tre små prikkene, og deretter velge `SCODE (promo code) Whirlpool`. Hvis alt er i orden, er du klar til å starte en ny Whirlpool-syklus med rabatt på tjenestegebyrene. Det er viktig å merke seg at disse SCODE-ene er midlertidige: de forblir gyldige i noen få dager før de blir foreldet.

## Hvordan vite kvaliteten på våre coinjoin-sykluser?
For at en coinjoin skal være virkelig effektiv, er det essensielt at den demonstrerer god uniformitet mellom mengdene av innganger og utganger. Denne uniformiteten forsterker antallet mulige tolkninger i øynene til en ekstern observatør, og øker dermed usikkerheten rundt transaksjonen. For å kvantifisere denne usikkerheten generert av en coinjoin, kan man ty til å beregne transaksjonens entropi. For en grundig utforskning av disse indikatorene, henviser jeg deg til opplæringen: [BOLTZMANN CALCULATOR](https://planb.network/en/tutorials/privacy/boltzmann-entropy). Whirlpool-modellen er anerkjent som den som bringer mest homogenitet til coinjoins.
Videre blir ytelsen til flere coinjoin-sykluser evaluert basert på omfanget av gruppene der en mynt er skjult. Størrelsen på disse gruppene definerer det som kalles anonsets. Det er to typer anonsets: den første vurderer personvernet oppnådd mot en retrospektiv analyse (fra nåtiden til fortiden) og den andre, mot en prospektiv analyse (fra fortiden til nåtiden). For en detaljert forklaring på disse to indikatorene, inviterer jeg deg til å konsultere opplæringen: [WHIRLPOOL STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/wst-anonsets)

## Hvordan håndtere postmix?
Etter å ha utført coinjoin-sykluser, er den beste strategien å holde dine UTXOer i **postmix**-kontoen, i påvente av deres fremtidige bruk. Det er til og med tilrådelig å la dem remixe på ubestemt tid til du trenger å bruke dem.

Noen brukere kan vurdere å overføre sine blandede bitcoins til en lommebok sikret av en hardware-lommebok. Dette er mulig, men det er viktig å følge anbefalingene fra Samourai Wallet nøye for ikke å kompromittere den oppnådde konfidensialiteten.

Sammenslåingen av UTXOer utgjør den mest hyppig gjorte feilen. Det er nødvendig å unngå å kombinere blandede UTXOer med ublandede UTXOer i samme transaksjon, for å unngå CIOH (*Common-Input-Ownership-Heuristic*). Dette krever nøye håndtering av dine UTXOer innenfor din lommebok, spesielt når det gjelder merking. Utover coinjoin, er sammenslåing av UTXOer generelt en dårlig praksis som ofte fører til tap av konfidensialitet når den ikke håndteres riktig.
Du bør også være årvåken om konsolideringen av blandede UTXOer med hverandre. Moderate konsolideringer er mulige hvis dine blandede UTXOer har betydelige anonsets, men dette vil uunngåelig redusere personvernet til myntene dine. Sørg for at konsolideringer verken er for store eller utført etter et utilstrekkelig antall remixes, da dette risikerer å etablere deduserbare koblinger mellom dine UTXOer før og etter coinjoin-syklusene. I tilfelle tvil om disse operasjonene, er den beste praksisen å ikke konsolidere postmix UTXOer, og å overføre dem en etter en til din hardware-lommebok, og generere en ny blank adresse hver gang. Husk igjen å merke hver mottatt UTXO på riktig måte.

Det frarådes også å overføre dine postmix UTXOer til en lommebok som bruker uvanlige skript. For eksempel, hvis du går inn i Whirlpool fra en multisig-lommebok som bruker `P2WSH`-skript, er det lite sjanse for at du vil bli blandet med andre brukere som har samme type lommebok opprinnelig. Hvis du forlater din postmix til denne samme multisig-lommeboken, vil personvernivået til dine blandede bitcoins bli sterkt redusert. Utover skript, er det mange andre lommebokavtrykk som kan lure deg.

Som med enhver Bitcoin-transaksjon, er det også passende å ikke gjenbruke mottaksadresser. Hver ny transaksjon må mottas på en ny blank adresse.

Den enkleste og sikreste løsningen er å la dine blandede UTXOer hvile i deres **postmix**-konto, la dem remixe og bare røre dem for å bruke. Samourai og Sparrow lommebøker har ekstra beskyttelser mot alle disse risikoene relatert til kjedeanalyse. Disse beskyttelsene hjelper deg med å unngå å gjøre feil.

## Hvordan håndtere doxxic change?
Videre må du være forsiktig med å håndtere doxxic change, vekslingen som ikke kunne gå inn i coinjoin-bassenget. Disse giftige UTXOene, som er et resultat av bruk av Whirlpool, utgjør en risiko for ditt personvern siden de etablerer en kobling mellom deg og bruken av coinjoin. Det er derfor avgjørende å håndtere dem med forsiktighet og ikke å kombinere dem med andre UTXOer, spesielt blandede UTXOer. Her er forskjellige strategier å vurdere for deres bruk:
- **Bland dem i mindre bassenger:** Hvis din giftige UTXO er stor nok til å gå inn i et mindre basseng på egen hånd, vurder å blande den. Dette er ofte det beste alternativet. Det er imidlertid avgjørende å ikke slå sammen flere giftige UTXOer for å få tilgang til et basseng, da dette kan koble dine forskjellige innganger.
- **Marker dem som "ikke-brukbare":** En annen tilnærming er å slutte å bruke dem, merk dem som "ikke-brukbare" i deres dedikerte konto, og bare Hodl. Dette sikrer at du ikke ved et uhell bruker dem. Hvis verdien av bitcoin øker, kan nye bassenger bedre egnet for dine giftige UTXOer dukke opp;
- **Gjør donasjoner:** Vurder å gjøre donasjoner, selv beskjedne, til utviklere som jobber med Bitcoin og tilhørende programvare. Du kan også donere til organisasjoner som aksepterer BTC. Hvis håndteringen av dine giftige UTXOer virker for komplisert, kan du enkelt kvitte deg med dem ved å gjøre en donasjon;
- **Kjøp gavekort:** Plattformer som [Bitrefill](https://www.bitrefill.com/) lar deg bytte bitcoins mot gavekort som kan brukes hos ulike forhandlere. Dette kan være en måte å kvitte seg med dine giftige UTXOer uten å miste den tilknyttede verdien;
- **Konsolider dem på Monero:** Samourai Wallet tilbyr nå en atombyttetjeneste mellom BTC og XMR. Dette er ideelt for å håndtere giftige UTXOer ved å konsolidere dem på Monero, uten å kompromittere ditt personvern via KYC, før du sender dem tilbake til Bitcoin. Imidlertid kan dette alternativet være kostbart i form av gruvegebyrer og premien på grunn av likviditetsbegrensninger;
- **Send dem til Lightning Network:** Å overføre disse UTXOene til Lightning Network for å dra nytte av reduserte transaksjonsgebyrer er et alternativ som kan være interessant. Imidlertid kan denne metoden avsløre visse opplysninger avhengig av din bruk av Lightning og bør derfor praktiseres med forsiktighet.

Detaljerte veiledninger om implementering av disse forskjellige teknikkene vil snart bli tilbudt på PlanB Network.

**Tilleggsressurser:**
[Samourai Wallet videoveiledning](https://planb.network/tutorials/wallet/samourai)
- [Samourai Wallet Dokumentasjon - Whirlpool](https://docs.samourai.io/whirlpool/basic-concepts);
- [Twitter-tråd om coinjoins](https://twitter.com/SamouraiWallet/status/1489220847336308739);
- [Blogginnlegg om coinjoins](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin).