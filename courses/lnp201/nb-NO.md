---
name: Teoretisk introduksjon til Lightning Network
goal: Oppdage Lightning Network fra et teknisk perspektiv
objectives:
  - Forstå hvordan nettverkets kanaler fungerer.
  - Bli kjent med termer som HTLC, LNURL, og UTXO.
  - Tilegne seg kunnskap om håndtering av likviditet og gebyrer i LNN.
  - Gjenkjenne Lightning Network som et nettverk.
  - Forstå de teoretiske bruksområdene til Lightning Network.
---

# En reise til Bitcoins andre lag

Dette kurset er en teoretisk leksjon om den tekniske funksjonen til Lightning Network.

Velkommen til den spennende verdenen av Lightning Network, et andre lag av Bitcoin som er både sofistikert og fullt av potensial. Vi er i ferd med å dykke ned i de tekniske dybdene av denne teknologien, uten å fokusere på spesifikke opplæringer eller bruksscenarier. For å få mest mulig ut av dette kurset, er en solid forståelse av Bitcoin essensielt. Dette er en opplevelse som krever en seriøs og fokusert tilnærming. Du kan også vurdere å ta LN 202-kurset parallelt, som tilbyr en mer praktisk aspekt ved denne utforskningen. Gjør deg klar til å begi deg ut på en reise som kan endre din oppfatning av Bitcoin-økosystemet.

Nyt oppdagelsen!

+++

# Grunnleggende
<partId>32647d62-102b-509f-a3ba-ad1d6a4345f1</partId>

## Forstå Lightning Network
<chapterId>df6230ae-ff35-56ea-8651-8e65580730a8</chapterId>

![video en](https://youtu.be/QDQ8NG0l3hk)

Lightning Network er en andre-lags betalingsinfrastruktur bygget på Bitcoin-nettverket som muliggjør raske og kostnadseffektive transaksjoner. For å fullt ut forstå hvordan Lightning Network fungerer, er det essensielt å forstå hva betalingskanaler er og hvordan de fungerer.

En Lightning-betalingskanal er en slags "privat vei" mellom to brukere som tillater raske og gjentatte Bitcoin-transaksjoner. Når en kanal åpnes, blir den tildelt en fast kapasitet, som er definert på forhånd av brukerne. Denne kapasiteten representerer det maksimale beløpet av Bitcoin som kan overføres i kanalen til enhver tid.

Betalingskanaler er todireksjonale, noe som betyr at de har to "sider". For eksempel, hvis Alice og Bob åpner en betalingskanal, kan Alice sende Bitcoin til Bob, og Bob kan sende Bitcoin til Alice. Transaksjoner inne i kanalen endrer ikke den totale kapasiteten til kanalen, men de endrer fordelingen av den kapasiteten mellom Alice og Bob.

![explication](assets/fr/1.webp)

For at en transaksjon skal være mulig i en Lightning-betalingskanal, må brukeren som sender midlene ha nok Bitcoin på sin side av kanalen. Hvis Alice ønsker å sende 1 Bitcoin til Bob gjennom deres kanal, må hun ha minst 1 Bitcoin på sin side av kanalen.
Grenser og Funksjon av Betalingskanaler på Lightning.
Selv om kapasiteten til en Lightning-betalingskanal er fast, begrenser dette ikke det totale antallet transaksjoner eller det totale volumet av Bitcoin som kan overføres gjennom kanalen. For eksempel, hvis Alice og Bob har en kanal med en kapasitet på 1 Bitcoin, kan de utføre hundrevis av transaksjoner på 0.01 Bitcoin eller tusenvis av transaksjoner på 0.001 Bitcoin, så lenge den totale kapasiteten til kanalen ikke overskrides til enhver tid.

Til tross for disse begrensningene, er Lightning-betalingskanaler en effektiv måte å utføre raske og billige Bitcoin-transaksjoner. De lar brukere sende og motta Bitcoin uten å måtte betale høye transaksjonsgebyrer eller vente på lange bekreftelsesperioder på Bitcoin-nettverket.
Oppsummert tilbyr Lightning betalingskanaler en kraftfull løsning for de som ønsker å utføre raske og rimelige Bitcoin-transaksjoner. Det er imidlertid essensielt å forstå deres funksjon og begrensninger for å fullt ut kunne dra nytte av dem.
![explication](assets/fr/2.webp)

Eksempel:

- Alice har 100 000 SAT
- Bob har 30 000 SAT

Dette er den nåværende tilstanden til kanalen. Under en transaksjon bestemmer Alice seg for å sende 40 000 SAT til Bob. Hun kan gjøre dette fordi 40 000 < 100 000.

Den nye tilstanden til kanalen er derfor:

- Alice 60 000 SAT
- Bob 70 000 SAT

```
Initial tilstand av kanalen:
Alice (100 000 SAT) ============== Bob (30 000 SAT)

Etter Alices overføring til Bob på 40 000 SAT:
Alice (60 000 SAT) ============== Bob (70 000 SAT)

```
![explication](assets/fr/3.webp)

Nå ønsker Bob å sende 80 000 SAT til Alice. Uten å ha likviditeten, kan han ikke. Maksimal kapasitet av kanalen er 130 000 SAT, med en mulig utgift på opptil 60 000 SAT for Alice og 70 000 SAT for Bob.

![explication](assets/fr/4.webp)

## Bitcoin, adresser, UTXO og transaksjoner
<chapterId>0cfb7e6b-96f0-508b-9210-90bc1e28649d</chapterId>

![video](https://youtu.be/U9l5IVriCss)

I dette andre kapittelet tar vi oss tid til å studere hvordan Bitcoin-transaksjoner faktisk fungerer, noe som vil være svært nyttig for å forstå Lightning. Vi diskuterer også kort konseptet med multi-signatur adresser, som er avgjørende for å forstå det neste kapittelet om å åpne kanaler på Lightning-nettverket.

- Privat nøkkel > Offentlig nøkkel > Adresse: Under en transaksjon sender Alice penger til Bob. Sistnevnte gir en adresse gitt av hans offentlige nøkkel. Alice, som selv mottok pengene på en adresse via sin offentlige nøkkel, bruker nå sin private nøkkel for å signere transaksjonen og dermed låse opp bitcoinene fra adressen.
- I en Bitcoin-transaksjon må alle bitcoins flytte. Navngitt UTXO (Unspend Transaction Output), vil bitene av bitcoin alle forlate bare for å returnere til eieren etterpå.
  Alice har 0.002 BTC, Bob har 0 BTC. Alice bestemmer seg for å sende 0.0015 BTC til Bob. Hun vil signere en transaksjon på 0.002 BTC hvor 0.0015 vil gå til Bob og 0.0005 vil returnere til hennes lommebok.

![explication](assets/fr/5.webp)

Her, fra en UTXO (Alice har 0.002 BTC på en adresse), har vi skapt 2 UTXOs (Bob har 0.0015 og Alice har en ny UTXO (uavhengig av den forrige) på 0.0005 BTC).

```
Alice (0.002 BTC)
  |
  V
Bitcoin-transaksjon (0.002 BTC)
  |
  |----> Bob (0.0015 BTC)
  |
  V
Alice (ny UTXO: 0.0005 BTC)
```
I Lightning Network brukes multisignaturer. Derfor kreves 2 signaturer for å låse opp midlene, dvs. to private nøkler for å flytte pengene. Dette kan være Alice og Bob som sammen må være enige om å låse opp pengene (UTXOen). Spesifikt i LN er de 2/2-transaksjoner, så begge signaturer er absolutt nødvendige, i motsetning til 2/3 eller 3/5 multisignaturer hvor bare en kombinasjon av det totale antallet nøkler kreves.
![explication](assets/fr/6.webp)

# Åpning og lukking av kanaler
<partId>900b5b6b-ccd0-5b2f-9424-4b191d0e935d</partId>

## Kanalåpning
<chapterId>96243eb0-f6b5-5b68-af1f-fffa0cc16bfe</chapterId>

![video](https://youtu.be/Ty80WuN5X-g)

Nå skal vi se nærmere på åpning av kanaler og hvordan det gjøres gjennom en Bitcoin-transaksjon.

Lightning Network har ulike kommunikasjonsnivåer:

- P2P-kommunikasjon (Lightning Network-protokollen)
- Betalingskanal (Lightning Network-protokollen)
- Bitcoin-transaksjon (Bitcoin-protokollen)

![explication](assets/fr/7.webp)

For å åpne en kanal kommuniserer de to partene gjennom en kommunikasjonskanal:

- Alice: "Hei, jeg vil åpne en kanal!"
- Bob: "Ok, her er min offentlige adresse."

![explication](assets/fr/8.webp)

Alice har nå 2 offentlige adresser for å opprette en 2/2 multisig-adresse. Hun kan nå gjøre en bitcoin-transaksjon for å sende penger til den.

La oss si at Alice har en UTXO på 0.002 BTC og hun vil åpne en kanal med Bob på 0.0013 BTC. Hun vil opprette en transaksjon med 2 UTXOer som output:

- en UTXO på 0.0013 til 2/2 multisig-adressen
- en UTXO på 0.0007 til en av hennes vekseladresser (retur av UTXOer).

Denne transaksjonen er ennå ikke offentlig fordi hvis den er det på dette stadiet, stoler hun på Bob for å kunne låse opp pengene fra multisig.

Men hvordan går man frem?

Alice vil opprette en annen transaksjon kalt en "uttaks-transaksjon" før hun publiserer innskuddet av midler i multisig.

![explication](assets/fr/9.webp)

Uttakstransaksjonen vil bruke midlene fra multisig-adressen til en adresse hun eier (dette gjøres før alt publiseres).
Når begge transaksjonene er bygget, forteller Alice Bob at det er gjort og ber ham om en signatur med hans offentlige nøkkel, og forklarer at på denne måten kan hun gjenopprette pengene sine hvis noe går galt. Bob er enig fordi han ikke er uærlig.

Alice kan nå gjenopprette pengene alene, ettersom hun allerede har Bobs signatur. Hun publiserer transaksjonene. Kanalen er nå åpen med 0.0013 BTC (130 000 SAT) på Alices side.

![explication](assets/fr/10.webp)

## Lightning-transaksjon & Forpliktelsestransaksjon
<chapterId>7d3fd135-129d-5c5a-b306-d5f2f1e63340</chapterId>

![video](https://youtu.be/dzPMGiR_JSE)

![cover](assets/fr/11.webp)
La oss nå analysere hva som egentlig skjer bak kulissene når man overfører midler fra den ene siden til den andre i en kanal på Lightning Network, med begrepet forpliktelsestransaksjon. Uttakstransaksjonen/kontrakten på blokkjeden representerer kanalens tilstand, og garanterer hvem som eier midlene etter hver overføring. Så etter en overføring på Lightning Network, er det en oppdatering av denne transaksjonen/kontrakten som ikke utføres mellom de to partene, Alice og Bob, som skaper den samme transaksjonen med den nåværende kanaltilstanden i tilfelle lukking:
- Alice åpner en kanal med Bob med 130 000 SAT på sin side. Uttakstransaksjonen som begge godtar i tilfelle lukking, fastslår at 130 000 SAT vil gå til Alice ved lukking, og Bob er enig fordi det er rettferdig.

![cover](assets/fr/12.webp)

- Alice sender 30 000 SAT til Bob. Det er nå en ny uttakstransaksjon som fastslår at i tilfelle lukking, vil Alice motta 100 000 SAT og Bob 30 000 SAT. Begge er enige fordi det er rettferdig.

![cover](assets/fr/13.webp)

- Alice sender 10 000 SAT til Bob, og en ny uttakstransaksjon opprettes som fastslår at Alice vil motta 90 000 SAT og Bob 40 000 SAT i tilfelle lukking. Begge er enige fordi det er rettferdig.

![cover](assets/fr/14.webp)

```
Opprinnelig tilstand av kanalen:
Alice (130 000 SAT) =============== Bob (0 SAT)

Etter den første overføringen:
Alice (100 000 SAT) =============== Bob (30 000 SAT)

Etter den andre overføringen:
Alice (90 000 SAT) =============== Bob (40 000 SAT)

```

Pengene flytter seg aldri, men den endelige saldoen oppdateres via en signert, men ikke publisert transaksjon på blokkjeden. Uttakstransaksjonen er derfor en forpliktelsestransaksjon. Satoshi-overføringene er en annen, mer nylig forpliktelsestransaksjon som oppdaterer saldoen.

## Forpliktelsestransaksjoner
<chapterId>f2f61e5b-badb-5947-9a81-7aa530b44e59</chapterId>

![video](https://youtu.be/veCs39uVFUk)

Hvis forpliktelsestransaksjoner dikterer en kanaltilstand med likviditet på tidspunkt X, kan vi jukse ved å publisere en gammel tilstand? Svaret er ja, fordi vi allerede har forhåndssignaturen til begge deltakerne i den upubliserte transaksjonen.

![instruction](assets/fr/15.webp)

For å løse dette problemet, vil vi legge til kompleksitet:

- Tidsbegrensning = midler låst til blokk N
- Tilbakekallingsnøkkel = Alices hemmelighet og Bobs hemmelighet

Disse to elementene legges til i forpliktelsestransaksjonen. Som et resultat må Alice vente til slutten av tidsbegrensningen, og hvem som helst som holder tilbakekallingsnøkkelen kan flytte midlene uten å vente på slutten av tidsbegrensningen. Hvis Alice prøver å jukse, bruker Bob tilbakekallingsnøkkelen for å stjele og straffe Alice.

![instruction](assets/fr/16.webp)
Nå (og i virkeligheten) er ikke forpliktelsestransaksjonen den samme for Alice og Bob, de er symmetriske, men hver med forskjellige begrensninger. De gir hverandre sin hemmelighet for å skape tilbakekallingsnøkkelen til den forrige forpliktelsestransaksjonen. Så ved opprettelsen skaper Alice kanalen med Bob, 130 000 SAT på hennes side, hun har en Timelock som hindrer henne i å umiddelbart ta tilbake pengene sine, hun må vente litt. Tilbakekallingsnøkkelen kan låse opp pengene, men bare Alice har den (Alices forpliktelsestransaksjon). Når det er en overføring, vil Alice gi sin gamle hemmelighet til Bob, og derfor vil sistnevnte kunne tømme kanalen til den forrige tilstanden i tilfelle Alice prøver å jukse (Alice blir derfor straffet).

![instruction](assets/fr/17.webp)

På samme måte vil Bob gi sin hemmelighet til Alice. Slik at hvis han prøver å jukse, kan Alice straffe ham. Operasjonen gjentas for hver ny forpliktelsestransaksjon. En ny hemmelighet bestemmes og en ny tilbakekallingsnøkkel. Så for hver ny transaksjon må den forrige forpliktelsestransaksjonen ødelegges ved å gi tilbakekallingshemmeligheten. Slik at hvis Alice eller Bob prøver å jukse, kan den andre handle før (takket være Timelock) og dermed unngå juks. Under transaksjon #3, gis hemmeligheten til transaksjon #2 derfor for å tillate Alice og Bob å forsvare seg mot Alice eller Bob.

![instruction](assets/fr/18.webp)

Personen som skaper transaksjonen med Timelock (den som sender pengene) kan bare bruke tilbakekallingsnøkkelen etter Timelock. Imidlertid kan personen som mottar pengene bruke den før Timelock i tilfelle juks fra den ene siden til den andre av en kanal på Lightning Network. Spesielt detaljerer vi mekanismene som lar oss vokte mot mulig juks fra ens peer innenfor kanalen.

## Kanallukking
<chapterId>29a72223-2249-5400-96f0-3756b1629bc2</chapterId>

![video](https://youtu.be/zmAa2fj_V7w)

Vi er interessert i kanallukking gjennom en Bitcoin-transaksjon, som kan ta forskjellige former avhengig av tilfellet. Det er 3 typer kanallukking:

- Den gode: samarbeidende lukking
- Den brutale: tvungen lukking (ikke-samarbeidende)
- Juksemakeren: lukking av en juksemaker

![instruction](assets/fr/19.webp)
![instruction](assets/fr/20.webp)


### Den gode

De to peerene kommuniserer og blir enige om å lukke kanalen. De stopper alle transaksjoner og validerer en endelig tilstand av kanalen. De blir enige om nettverksgebyrer (personen som åpnet kanalen betaler avslutningsgebyrene). De skaper nå avslutningstransaksjonen. Det er en avslutningstransaksjon, forskjellig fra forpliktelsestransaksjoner fordi det ikke er noen Timelock og tilbakekallingsnøkkel. Transaksjonen blir deretter publisert, og Alice og Bob mottar sine respektive balanser. Denne typen lukking er rask (fordi det ikke er noen Timelock) og generelt billig.

![instruction](assets/fr/21.webp)


### Den brutale

Alice ønsker å lukke kanalen, men Bob svarer ikke fordi han er offline (internett- eller strømbrudd). Alice vil da publisere den mest nylige forpliktelsestransaksjonen (den siste). Transaksjonen blir publisert, og Timelock blir aktivert. Deretter ble gebyrene bestemt da denne transaksjonen ble opprettet X tid i fortiden! MemPool er nettverket som har endret seg siden, så protokollen standardiserer til gebyrer 5 ganger høyere enn de nåværende da transaksjonen ble opprettet. Opprettingsgebyr på 10 SAT, så transaksjonen anses for 50 SAT. På tidspunktet for tvungen lukking er nettverket:
- 1 SAT = overbetalt med 50\*- 100 SAT = underbetalt med 2\*

Dette gjør tvungen lukking lengre (Timelock) og spesielt mer risikabelt med tanke på gebyrer og mulig validering av gruvearbeidere.

![instruksjon](assets/fr/22.webp)

### Svindleren

Alice prøver å jukse ved å publisere en gammel forpliktelsestransaksjon. Men Bob overvåker MemPool og ser etter transaksjoner som prøver å publisere gamle. Hvis han finner noen, bruker han tilbakekallingsnøkkelen for å straffe Alice og ta alle SAT fra kanalen.

![instruksjon](assets/fr/23.webp)

Konklusjonen er at kanallukking i Lightning Network er et avgjørende skritt som kan ta forskjellige former. I en samarbeidslukking kommuniserer begge parter og blir enige om en endelig tilstand av kanalen. Dette er det raskeste og billigste alternativet. På den annen side skjer en tvungen lukking når en part ikke svarer. Dette er en dyrere og lengre situasjon på grunn av uforutsigbare transaksjonsgebyrer og aktivering av Timelock. Til slutt, hvis en deltaker prøver å jukse ved å publisere en gammel forpliktelsestransaksjon, kan svindleren bli straffet ved å miste alle SAT fra kanalen. Det er derfor avgjørende å forstå disse mekanismene for effektiv og rettferdig bruk av Lightning Network.

# Et likviditetsnettverk
<partId>a873f1cb-751f-5f4a-9ed7-25092bfdef11</partId>

## Lightning Network
<chapterId>45a7252c-fa4f-554b-b8bb-47449532918e</chapterId>

![video](https://youtu.be/44oBdNdXtEQ)

I dette syvende kapittelet studerer vi hvordan Lightning fungerer som et nettverk av kanaler og hvordan betalinger rutes fra deres kilde til deres destinasjon.

![cover](assets/fr/24.webp)
![cover](assets/fr/25.webp)

Lightning er et nettverk av betalingskanaler. Tusenvis av jevnaldrende med sine egne likviditetskanaler er koblet til hverandre, og dermed selvbruk for å utføre transaksjoner mellom uforbundne jevnaldrende. Likviditeten til disse kanalene kan ikke overføres til andre likviditetskanaler.

Alice -> Eden - > Bob`. Satoshis har ikke flyttet fra `Alice -> Bob`, men fra `Alice -> Eden`og fra`Eden -> Bob`.

Så hver person og kanal har forskjellig likviditet. For å gjøre betalinger, må du finne en rute i nettverket med nok likviditet. Hvis det ikke er nok, vil ikke betalingen gå gjennom.

Vurder følgende nettverk:

```
Initial state of the network:
Alice (130 SAT) ==== (0 SAT) Susie (90 SAT) ==== (200 SAT) Eden (150 SAT) ==== (100 SAT) Bob
```
![cover](assets/fr/26.webp)

Hvis Alice skal overføre 40 SAT til Bob, vil likviditeten bli omfordelt langs ruten mellom de to partene.

```
After Alice transfers 40 SAT to Bob:
Alice (90 SAT) ==== (40 SAT) Susie (50 SAT) ==== (240 SAT) Eden (110 SAT) ==== (140 SAT) Bob
```

![cover](assets/fr/27.webp)

Men, i den opprinnelige tilstanden, kan ikke Bob sende 40 SAT til Alice fordi Susie ikke har noen likviditet med Alice for å sende 40 SAT, så betaling er ikke mulig via denne ruten. Vi trenger derfor en annen rute der transaksjonen er mulig.

I det første eksemplet er det klart at Susie og Eden ikke har tapt noe og ikke har vunnet noe. Lightning Network-noder tar et gebyr for å gå med på å bli brukt til å rute transaksjonen!

Det er forskjellige gebyrer avhengig av hvor likviditeten er lokalisert
Alice - Bob
- Alice's avgift = Alice -> Bob
- Bob's avgift = Bob -> Alice

![cover](assets/fr/28.webp)

Det er to typer avgifter:

- en fast avgift uavhengig av beløpet: 1 SAT (standard, men kan endres)
- en variabel avgift (1 ppm som standard)

Eksempel på avgift:

- Alice - Susie; 1/1 (1 fast avgift og 1 variabel avgift)
- Susie - Eden; 0/200
- Eden - Bob; 1/1

Derfor:

- Avgift 1: (betalt av Alice til seg selv) 1 + (40,000\*0.000001)
- Avgift 2: 0 + 40,000 \* 0.0002 = 8 SAT
- Avgift 3: 1 + 40,000\* 0.000001 = 1.04 SAT

![cover](assets/fr/29.webp)

Frakt:

1. Sending av 40,009.04 Alice -> Susie; Alice betaler sine egne utgifter så det teller ikke
2. Susie gjør Eden en tjeneste ved å sende 40 001.04; hun tar denne kommisjonen på 8 SAT
3. Eden gjør tjenesten med å sende 40,000 til Bob, han tar sin avgift på 1.04 SAT.

Alice betalte en avgift på 9.04 SAT og Bob mottok 40,000 SAT.

![cover](assets/fr/30.webp)

I Lightning Network er det Alice's node som bestemmer ruten før betalingen sendes. Derfor er det en søken etter den beste ruten og Alice er den eneste som kjenner ruten og prisen. Betalingen sendes, men Susie har ingen informasjon.

![cover](assets/fr/31.webp)

For Susie eller Eden: de vet ikke hvem den endelige mottakeren er, eller hvem som sender betalingen. Dette er løkruting. Noden må holde en plan over nettverket for å finne sin rute, men ingen av mellomleddene har noen informasjon.

## HTLC - Hashed Time Locked Contract
<chapterId>4369b85a-1365-55d8-99e1-509088210116</chapterId>

![video](https://youtu.be/jI4nM297aHA)

I et tradisjonelt rutingssystem, hvordan kan vi sikre at Eden ikke jukser og respekterer sin del av kontrakten?

HTLC er en betalingskontrakt som bare kan låses opp med en hemmelighet. Hvis den ikke avsløres, så utløper kontrakten. Det er derfor en betinget betaling. Hvordan brukes de?

![instruction](assets/fr/32.webp)

Vurder følgende situasjon:
`Alice (100,000 SAT) ==== (30,000 SAT) Susie (250,000 SAT) ==== (0 SAT) Bob`

- Bob genererer en hemmelighet S (forbildet) og beregner hashen r = hash(s)
- Bob sender en faktura til Alice med "r" inkludert
- Alice sender en HTLC på 40,000 SAT til Susie med betingelsen om å avsløre "s'" slik at hash(s') = r
- Susie sender en lignende HTLC til Bob
- Bob låser opp Susie's HTLC ved å vise henne "s"
- Susie låser opp Alice's HTLC ved å vise henne "S"

Hvis Bob er offline og aldri henter hemmeligheten som gir ham legitimiteten til å motta pengene, så vil HTLC-en utløpe etter et visst antall blokker.

![instruction](assets/fr/33.webp)
HTLC-ene utløper i omvendt rekkefølge: først Susie-Bob utløpet, deretter Alice-Susie utløpet. På denne måten, hvis Bob kommer tilbake, endrer det ikke noe. Ellers, hvis Alice avbryter mens Bob kommer tilbake, vil det bli rot og folk kan ha jobbet for ingenting.
Så, hva skjer i tilfelle av lukking? Faktisk er våre forpliktelsestransaksjoner enda mer komplekse. Vi trenger å representere den mellomliggende balansen hvis kanalen lukkes.

Derfor er det en HTLC-ut på 40 000 satoshis (med begrensningene sett tidligere) i forpliktelsestransaksjonen via utgang #3.

![instruksjon](assets/fr/34.webp)

Alice har i forpliktelsestransaksjonen:

- Utgang #1: 60 000 SAT for Alice via en Timelock og tilbakekallingsnøkkel (det som gjenstår for henne)
- Utgang #2: 30 000 som allerede tilhører Susie
- Utgang #3: 40 000 i HTLC

Alices forpliktelsestransaksjon er med en HTLC-ut fordi hun sender en HTLC-inn til mottakeren, Susie.

![instruksjon](assets/fr/35.webp)

Derfor, hvis vi publiserer denne forpliktelsestransaksjonen, kan Susie hente HTCL-pengene med "s"-bildet. Hvis hun ikke har forhåndsbildet, henter Alice pengene en gang HTCL utløper. Tenk på utganger (UTXO) som forskjellige betalinger med forskjellige betingelser.
Når betalingen er gjort (utløp eller utførelse), endres kanaltilstanden og transaksjonen med HTCL eksisterer ikke lenger. Vi returnerer til noe klassisk.
I tilfelle av samarbeidslukking: vi stopper betalinger og derfor venter på utførelsen av overføringer/HTCL, transaksjonen er lett så mindre kostbar fordi det er maksimalt 1 eller 2 utganger.
Hvis tvunget lukking: vi publiserer med alle pågående HTLC-er, så det blir veldig tungt og veldig kostbart. Og det er et rot.

Oppsummert bruker Lightning Network rutingssystemet Hash Time-Locked Contracts (HTLC) for å sikre sikker og verifiserbar betaling. HTLC-er tillater betingede betalinger hvor penger kun kan låses opp med et hemmelig, og sikrer dermed at deltakerne oppfyller sine forpliktelser.
I eksemplet presentert, ønsker Alice å sende SAT til Bob gjennom Susie. Bob genererer en hemmelighet, lager en hash av den, og overfører den til Alice. Alice og Susie setter opp en HTLC basert på denne hashen. Når Bob låser opp Susies HTLC ved å vise henne hemmeligheten, kan Susie deretter låse opp Alices HTLC.
I tilfelle at Bob ikke avslører hemmeligheten innen en viss tidsperiode, utløper HTLC-en. Utløpet skjer i omvendt rekkefølge, noe som sikrer at hvis Bob kommer tilbake online, er det ingen uønskede konsekvenser.

Når kanalen lukkes, hvis det er en samarbeidslukking, avbrytes betalinger og HTLC-er løses, noe som generelt er mindre kostbart. Hvis lukkingen er tvunget, publiseres alle pågående HTLC-transaksjoner, noe som kan bli veldig kostbart og rotete.
Oppsummert legger HTLC-mekanismen til et ekstra lag med sikkerhet til Lightning Network, og sikrer at betalinger utføres korrekt og at brukerne oppfyller sine forpliktelser.

## Finne veien
<chapterId>7e2ae959-c2a1-512e-b5d6-8fd962e819da</chapterId>

![video](https://youtu.be/CqetCElRjUQ)

De eneste offentlige dataene er den totale kanalkapasiteten (Alice + Bob), men vi vet ikke hvor likviditeten er lokalisert.
For å få mer informasjon, lytter noden vår til LN-kommunikasjonskanalen for kunngjøringer av nye kanaler og oppdateringer til kanalavgifter. Noden din ser også på blockchain for kanallukninger.
Siden vi ikke har all informasjonen, må vi søke etter en graf/rute med informasjonen vi har (maksimal kanalkapasitet og ikke hvor likviditeten er plassert).
Kriterier:

- Suksesssannsynlighet - Gebyrer
- HTLC utløpstid
- Antall mellomliggende noder
- Tilfeldighet

![graph](assets/fr/36.webp)

Så hvis det er 3 mulige ruter:

- Alice > 1 > 2 > 5 > Bob
- Alice > 1 > 2 > 4 > 5 > Bob
- Alice 1 > 2 > 3 > Bob

Vi leter etter den beste ruten i teorien med de laveste gebyrene og den høyeste sjansen for suksess: maksimal likviditet og færrest mulige hopp.

For eksempel, hvis 2-3 bare har en kapasitet på 130 000 SAT, er det svært usannsynlig å sende 100 000, så valg #3 har ingen sjanse for suksess.

![graph](assets/fr/37.webp)

Nå har algoritmen gjort sine 3 valg og vil prøve den første:

Valg 1:

- Alice sender en HTLC på 100 000 SAT til 1;
- 1 lager en HTLC på 100 000 SAT til 2;
- 2 lager en HTLC på 100 000 SAT til 5, men 2 kan ikke gjøre det, så det annonseres.

Informasjonen sendes tilbake, så Alice bestemmer seg for å prøve den andre ruten:

- Alice sender en HTLC på 100 000 til 1;
- 1 lager en HTLC på 100 000 til 2;
- 2 lager en HTLC på 100 000 til 4;
- 4 lager en HTLC på 100 000 til 5;
- 5 lager en HTLC på 100 000 til Bob. 5 har likviditeten, så det er greit.
- Bob bruker preimage (hash) av HTLC og bruker dermed hemmeligheten til å hente de 100 000 SAT fra 5
- 5 har nå hemmeligheten til HTLC for å hente den blokkerte HTLC fra 4
- 4 har nå hemmeligheten til HTLC for å hente den blokkerte HTLC fra 2
- 2 har nå hemmeligheten til HTLC for å hente den blokkerte HTLC fra 1
- 1 har nå hemmeligheten til HTLC for å hente Alices blokkerte HTLC

Alice så ikke feilen med rute 1, hun ventet bare ett sekund lenger. En betalingsfeil oppstår når det ikke er noen mulig rute. For å lette søket etter en rute, kan Bob gi informasjon til Alice for å hjelpe med fakturaen hennes:

- Beløpet
- Hans adresse
- Hashen av preimage slik at Alice kan opprette HTLC
- Indikasjoner på Bobs kanaler

Bob kjenner likviditeten til kanaler 5 og 3 fordi han er direkte koblet til dem, han kan indikere dette til Alice. Han advarer Alice om at node 3 er ubrukelig, noe som forhindrer Alice fra potensielt å lage ruten sin.
Et annet element ville være de private kanalene (derfor ikke publisert på nettverket) som Bob kan ha. Hvis Bob har en privat kanal med 1, kan han fortelle Alice å bruke den, og det ville gi Alice > 1 > Bob'.

![graph](assets/fr/38.webp)
Avslutningsvis er ruting av transaksjoner på Lightning Network en kompleks prosess som krever vurdering av ulike faktorer. Selv om den totale kapasiteten til kanalene er offentlig, er den nøyaktige fordelingen av likviditet ikke direkte tilgjengelig. Dette tvinger noder til å estimere de mest sannsynlige vellykkede rutene, med tanke på kriterier som gebyrer, HTLC utløpstid, antall mellomliggende noder, og en tilfeldighetsfaktor. Når flere ruter er mulige, søker noder å minimere gebyrer og maksimere sjansene for suksess ved å velge kanaler med tilstrekkelig likviditet og et minimum antall hopp. Hvis et transaksjonsforsøk mislykkes på grunn av utilstrekkelig likviditet, prøves en annen rute til en vellykket transaksjon er gjennomført.
Videre, for å lette søk etter ruter, kan mottakeren gi tilleggsinformasjon som adressen, beløpet, preimage hash, og indikasjoner på deres kanaler. Dette kan bidra til å identifisere kanaler med tilstrekkelig likviditet og unngå unødvendige transaksjonsforsøk. Til syvende og sist er rutesystemet til Lightning Network designet for å optimalisere hastighet, sikkerhet, og effektivitet av transaksjoner samtidig som brukerens personvern bevares.

# Verktøy i Lightning Network
<partId>74d6c334-ec5d-55d9-8598-f05694703bf6</partId>

## Faktura, LNURL, Keysend
<chapterId>e34c7ecd-2327-52e3-b61e-c837d9e5e8b0</chapterId>

![video](https://youtu.be/XANzf1Qqp9I)

![cover](assets/fr/39.webp)

En LN-faktura (eller faktura) er lang og ikke behagelig å lese, men den tillater en tett representasjon av en betalingsforespørsel.

Eksempel:
lnbc1m1pskuawzpp5qeuuva2txazy5g483tuv9pznn9ft8l5e49s5dndj2pqq0ptyn8msdqqcqzpgxqrrsssp5v4s00u579atm0em6eqm9nr7d0vr64z5j2sm5s33x3r9m4lgfdueq9qyyssqxkjzzgx5ef7ez3dks0laxayx4grrw7j22ppgzyhpydtv6hmc39skf9hjxn5yd3kvv7zpjdxd2s7crcnemh2fz26mnr6zu83w0a2fwxcqnvujl3

- lnbc1m = lesbar del
- 1 = separasjon fra resten
- Deretter resten
- Bc1 = Bech32-koding (base 32), så 32 tegn brukes.
- 10 = 1.2.3.4.5.6.7.8.9.0
- 26 = abcdefghijklmnopqrstuvwxyz
- 32 = ikke "b-i-o" og ikke "1"

### lnbc1m

- ln = Lightning
- Bc = bitcoin (hovednett)
- 1 = beløp
- M = milli (10^-3 / u = mikro 10^-6 / n = nano 10^-9 / p = piko 10^-12'
  Her 1m = 1 * 0.001btc = 100,000 SAT
Vennligst betal 100 000 SAT på Lightning-nettverket til Bitcoin mainnet til pskuawzpp5qeuuva2txazy5g483tuv9pznn9ft8l5e49s5dndj2pqq0ptyn8msdqqcqzpgxqrrsssp5v4s00u579atm0em6eqm9nr7d0vr64z5j2sm5s33x3r9m4lgfdueq9qyyssqxkjzzgx5ef7ez3dks0laxayx4grrw7j22ppgzyhpydtv6hmc39skf9hjxn5yd3kvv7zpjdxd2s7crcnemh2fz26mnr6zu83w0a2fwxcqnvujl3
### Tidsstempel (når det ble opprettet)

Det inneholder 0 eller flere tilleggsdeler:

- Hash av forhåndsbildet
- Betalingshemmelighet (onion routing)
- Vilkaarlig data
- LN offentlig nøkkel til mottakeren
- Utløpstid (standard 1 time)
- Rutehint
- Signatur av hele

Det finnes andre typer fakturaer. LNURL meta-protokollen tillater å gi et direkte satoshi-beløp i stedet for å lage en forespørsel. Dette er veldig fleksibelt og tillater mange forbedringer når det gjelder brukeropplevelse.

![cover](assets/fr/40.webp)

En Keysend lar Alice sende penger til Bob uten Bobs forespørsel. Alice henter Bobs ID, skaper et forhåndsbilde uten å spørre Bob, og inkluderer det i betalingen sin. Så Bob vil motta en overraskelsesforespørsel hvor han kan låse opp pengene fordi Alice allerede har gjort jobben.

![cover](assets/fr/41.webp)

Konklusjonen er at en faktura på Lightning Network, selv om den er kompleks ved første øyekast, effektivt koder en betalingsforespørsel. Hver del av fakturaen inneholder nøkkelinformasjon, inkludert beløpet som skal betales, mottakeren, opprettelsestidspunktet, og potensielt annen informasjon som hashen av forhåndsbildet, betalingshemmeligheten, rutehint, og utløpstid. Protokoller som LNURL og Keysend tilbyr betydelige forbedringer når det gjelder fleksibilitet og brukeropplevelse, som for eksempel å sende midler uten tidligere forespørsel fra den andre parten. Disse teknologiene gjør betalingsprosessen jevnere og mer effektiv på Lightning Network.

## Administrere Likviditet
<chapterId>cc76d0c4-d958-57f5-84bf-177e21393f48</chapterId>

![video](https://youtu.be/MIbej28La7Y)

![instruction](assets/fr/42.webp)

Vi gir noen generelle retningslinjer for å svare på det evige spørsmålet om å administrere likviditet på Lightning.

I LN finnes det 3 typer mennesker:

- Kjøpere: de har utgående likviditet, som er det enkleste fordi de bare trenger å åpne kanaler
- Handelsmenn: det er mer komplisert fordi de trenger innkommende likviditet fra andre noder og andre aktører. De må ha folk koblet til seg
- Ruteringsnoder: de ønsker å være balansert med likviditet på begge sider og ha en god tilkobling til mange noder for å bli brukt så mye som mulig

Så hvis du trenger innkommende likviditet, kan du kjøpe den fra tjenester.

![instruction](assets/fr/43.webp)

Alice kjøper en kanal med Susie for 1 million satoshier, så hun åpner en kanal med direkte 1 000 000 SAT på den innkommende siden. Hun kan da akseptere opptil 1 million SAT i betaling fra kunder som er koblet med Susie (som er godt koblet).
En annen løsning ville være å foreta betalinger; du betaler 100 000 for X grunn, du kan nå motta 100 000.
![instruction](assets/fr/44.webp)

### Loop Out-løsning: Atomic swap LN - BTC

Alice 2 millioner - Susie 0

![instruction](assets/fr/45.webp)

Alice ønsker å sende likviditet til Susie, så hun utfører en Loop out (en spesiell node som tilbyr en pro-tjeneste for å rebalansere LN/BTC).
Alice sender 1 million til Loop via Susies node, så Susie har likviditeten og Loop sender on-chain-saldoen tilbake til Alices node.

![instruction](assets/fr/46.webp)

Så 1 million går til Susie, Susie sender 1 million til Loop, Loop sender 1 million til Alice. Alice har derfor flyttet likviditet til Susie til kostnaden av noen gebyrer betalt til Loop for tjenesten.

Det mest kompliserte med LN er å opprettholde likviditet.

![instruction](assets/fr/47.webp)

Konklusjonen er at likviditetsstyring på Lightning Network er et nøkkelspørsmål som avhenger av brukertypen: kjøper, handelsmann eller ruteringsnode. Kjøpere, som trenger utgående likviditet, har den enkleste oppgaven: de åpner rett og slett kanaler. Handelsmenn, som krever inngående likviditet, må være koblet til andre noder og aktører. Ruteringsnoder, derimot, søker å opprettholde en balanse av likviditet på begge sider. Flere løsninger eksisterer for å håndtere likviditet, som å kjøpe kanaler eller betale for å øke mottakskapasiteten. "Loop Out"-alternativet, som tillater en Atomic Swap mellom LN og BTC, tilbyr en interessant løsning for å rebalansere likviditet. Til tross for disse strategiene, forblir det å opprettholde likviditet på Lightning Network en kompleks utfordring.

# Gå videre
<partId>6bbf107d-a224-5916-9f0c-2b4d30dd0b17</partId>

## Sammendrag av kurset
<chapterId>a65a571c-561b-5e1c-87bf-494644653c22</chapterId>

![video](https://youtu.be/coaskEGRjiU)

Målet vårt var å forklare hvordan Lightning Network fungerer og hvordan det er avhengig av Bitcoin for å fungere.

Lightning Network er et nettverk av betalingskanaler. Vi har sett hvordan en betalingskanal fungerer mellom to interessenter, men vi har også utvidet vår visjon til hele nettverket, til begrepet et nettverk av betalingskanaler.

![instruction](assets/fr/48.webp)

Kanaler åpnes via en Bitcoin-transaksjon og kan romme så mange transaksjoner som mulig. Tilstanden til kanalen representeres av en forpliktelsestransaksjon som sender til hver interessent det de har på sin side av kanalen. Når en transaksjon finner sted innenfor kanalen, forplikter interessentene seg til den nye tilstanden ved å oppheve den gamle tilstanden og bygge en ny forpliktelsestransaksjon.

![instruction](assets/fr/49.webp)

Par beskytter seg mot juks med tilbakekallingsnøkler og en tidsbegrensning. Lukking ved gjensidig samtykke foretrekkes for å lukke kanalen. I tilfelle tvungen lukking, publiseres den siste forpliktelsestransaksjonen.

![instruction](assets/fr/50.webp)

Betalinger kan låne kanaler fra andre mellomliggende noder. Betingede betalinger på hash-tidslåsen (HTLC) tillater at midler låses til betalingen er fullstendig løst. Løkruting brukes i Lightning Network. Mellomliggende noder vet ikke det endelige bestemmelsesstedet for betalinger. Alice må beregne betalingsruten, men har ikke all informasjon om likviditet i mellomliggende kanaler.

![instruction](assets/fr/51.webp)

Det er et sannsynlighetskomponent når man sender en betaling via Lightning Network.

![instruction](assets/fr/52.webp)
For å motta betalinger må likviditet håndteres i kanalene, noe som kan gjøres ved å be andre om å åpne kanaler til oss, åpne kanaler selv, og bruke verktøy som Loop eller kjøpe/leie kanaler på markedsplasser.

## Fanis' intervju
<chapterId>077cb5f5-1626-5da5-9964-e67b1de503bf</chapterId>

Her er et sammendrag av intervjuet:

Lightning Network er en ultrarask betalingsløsning på Bitcoin som tillater å omgå begrensningene relatert til nettverkets skalerbarhet. Imidlertid er bitcoins på Lightning ikke like sikre som de på Bitcoin-kjeden fordi desentralisering og sikkerhet prioriteres over skalerbarhet.

Økt blokkstørrelse er ikke en god løsning da det kompromitterer noder og datakapasitet. I stedet tillater Lightning Network å opprette betalingskanaler mellom to Bitcoin-brukere uten å vise transaksjoner på blokkjeden, noe som sparer plass på blokker og tillater Bitcoin å skalere i dag.

Det er imidlertid kritikk angående skalerbarheten og sentraliseringen av Lightning Network, med potensielle problemer relatert til kanallukking og høye transaksjonsgebyrer. For å løse disse problemene anbefales det å unngå å åpne små kanaler for å unngå fremtidige problemer og å øke transaksjonsgebyrene med Child Pay for Parent.

Løsninger som vurderes for fremtiden til Lightning Network er batching og å opprette kanaler i grupper for å redusere transaksjonsgebyrer, samt å øke blokkstørrelsen på lang sikt. Det er imidlertid viktig å merke seg at bitcoins på Lightning ikke er like sikre som bitcoins på Bitcoin-kjeden.

Personvern på Bitcoin og Lightning er knyttet sammen, med løkruting som sikrer et visst nivå av personvern for transaksjoner. Imidlertid er alt på Bitcoin transparent som standard, med heuristikker brukt til å spore Bitcoins fra adresse til adresse på Bitcoin-kjeden.

Å kjøpe Bitcoins med KYC lar børsen vite uttakstransaksjoner, mens runde beløp og endringsadresser lar en vite hvilken del av en transaksjon som er ment for en annen person og hvilken del som er ment for en selv.

For å forbedre personvern, tillater felles handlinger og coinjoins å bryte sannsynlighetsberegninger ved å gjøre transaksjoner der flere personer gjør en transaksjon sammen. Kjedeanalysefirmaer har vanskeligere for å bestemme hva du gjør med dine bitcoins ved å følge.

På Lightning er bare to personer klar over transaksjonen, og den er mer konfidensiell enn Bitcoin. Løkruting betyr at et mellomliggende node ikke kjenner avsenderen og mottakeren av betalingen.

For å bruke Lightning Network, anbefales det å følge en opplæring på YouTube-kanalen din eller direkte på oppdag Bitcoin-nettstedet, eller å bruke opplæringen på Umbrell. Det er også mulig å sende vilkårlig tekst under en betaling på Lightning ved å bruke et dedikert felt for dette, noe som kan være nyttig for donasjoner eller meldinger.
Det er imidlertid viktig å merke seg at Lightning-ruteringsnoder kan bli regulert i fremtiden, med noen stater som forsøker å regulere ruteringsnoder. For handlende er det nødvendig å håndtere likviditet for å akseptere betalinger på Lightning Network, med nåværende begrensninger som kan overvinnes med passende løsninger.

Til slutt er fremtiden for Bitcoin lovende med en mulig projeksjon på en million om fem år. For å sikre profesjonaliseringen av industrien og skapelsen av et alternativt system til det eksisterende banksystemet, er det viktig å bidra til nettverket og slutte å stole.

## Evaluer kurset
<chapterId>38814c99-eb7b-5772-af49-4386ee2ce9b0</chapterId>
<isCourseReview>true</isCourseReview>

## Avsluttende eksamen
<chapterId>7ed33400-aef7-5f3e-bfb1-7867e445d708</chapterId>
<isCourseExam>true</isCourseExam>

## Anerkjennelser og fortsett å grave i kaninhullet
<chapterId>afc0d72b-4fbc-5893-90b2-e27fb519ad02</chapterId>
Gratulerer! 🎉
Du har fullført LN 201-treningen - Introduksjon til Lightning Network!
Du kan være stolt av deg selv fordi det ikke er lett. Vær klar over at få personer går så dypt inn i Bitcoin-kaninhullet.

Først og fremst, en stor takk til Fanis Michalakis for å tilby oss dette flotte gratis kurset om en mer etnisk aspekt av Lightning. Ikke nøl med å følge ham på Twitter, på bloggen hans, eller gjennom arbeidet hans ved LN-markedet.

Deretter, hvis du ønsker å hjelpe prosjektet, nøl ikke med å sponse oss på Patreon. Dine donasjoner vil bli brukt til å produsere innhold for nye treningskurs og selvfølgelig, vil du være den første til å bli informert (inkludert om Fanis' neste som er under arbeid!).

Lightning Network-eventyret fortsetter med Umbrel-treningen og implementeringen av en Lightning Network-node. Teorien er over, og det er på tide for praksis med LN 202-treningen nå!

Kyss og vi sees snart!

Rogzy'