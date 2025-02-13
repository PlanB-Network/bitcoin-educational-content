---
name: Bygge med Elements og Liquid Network
goal: Lær deg å bruke og utvikle med Elements åpen kildekode-blokkjedeplattform og dens viktigste funksjoner
objectives: 

  - Forstå de grunnleggende konseptene i Elements blockchain-plattformen og Liquid sidekjeder.
  - Lær hvordan du konfigurerer og kjører Elements-noder for frittstående og sidekjede-konfigurasjoner.
  - Få praktisk erfaring med føderert blokksignering og Federated 2-Way Peg.
  - Sette opp og administrere sikre, effektive blokkjedemiljøer for reelle brukstilfeller.

---
# Bygg på væske og elementer

Oppdag de avanserte funksjonene og mulighetene i Liquid og Elements, og lær hvordan du effektivt kan bruke disse verktøyene til å forbedre utviklingsprosjektene dine. Denne opplæringen gir deg et komplett teoretisk og praktisk grunnlag, slik at du kan mestre funksjoner som konfidensielle transaksjoner, utstedte eiendeler og føderert blokksignering.

Liquid, som er basert på rammeverket Elements, er utviklet for å forbedre personvern, skalerbarhet og funksjonalitet for finansielle og tekniske løsninger. I dette kurset får du praktisk erfaring med utstedelse og forvaltning av aktiva, Federated 2-Way Peg og bruk av verktøy som elementsd og elements-cli, slik at du kan lage innovative løsninger som er skreddersydd til dine behov.

Dette kurset er skreddersydd for utviklere på alle erfaringsnivåer. Nybegynnere og viderekomne vil finne lettfattelige forklaringer og praktiske eksempler, mens avanserte brukere kan fordype seg i tekniske detaljer og mindre kjente funksjoner i Liquid og Elements.

Bli med oss for å heve kompetansen din, frigjøre det fulle potensialet til Liquid og Elements og skape effektive verktøy for fremtidens Liquid-innovasjon.

+++
# Innledning

<partId>8f34de87-6e9a-4e3b-a326-50fc7c1803b3</partId>

## Kurs Introduksjon

<chapterId>a721398e-7040-4edd-be53-b485ea759fa9</chapterId>

![Video](https://youtu.be/gkQfnwYLyI0?si=H6cIPhgZaSAwHaHI)

Formålet med Elements Academy er å introdusere og forklare nøkkelbegrepene i Elements, åpen kildekode-plattformen som Liquid er bygget på. Ved slutten av kurset skal du ha en god forståelse av hovedfunksjonene i Elements, for eksempel Confidential Transactions og Issued Assets, og prosessene som er involvert i driften av Elements Core.

Hver del vil ha leksjoner med forklarende tekst og en video som avsluttes med en quiz. Antall spørsmål er relatert til størrelsen på det foregående emnet. Del 10 oppsummerer kursets innhold og avsluttes med en større quiz.

Eventuelle spørsmål, forespørsler om ytterligere informasjon eller spørsmål om quizsvarene kan rettes til læreren din, James Dorfman.

## Oversikt over elementer

<chapterId>7a7f2712-5300-4a6d-b1ed-05eab731bc35</chapterId>

![Video](https://youtu.be/ns-JLGdkNig?si=fmWye_boRSvVF1Bt)

Elements er en åpen kildekodeplattform for blokkjeder med sidekjeder, som gir tilgang til kraftige funksjoner utviklet av medlemmer av fellesskapet, for eksempel Confidential Transactions og Issued Assets.

Elements er i bunn og grunn en protokoll som gjør det mulig å skape konsensus rundt transaksjonshistorikken og reglene som styrer overføring og opprettelse av eiendeler som er lagret i en distribuert blokkjedehovedbok.

Du finner mer bakgrunnsinformasjon om Elements på Elements Project-nettstedet (https://elementsproject.org/), den offisielle Liquid-bloggen (https://blog.liquid.net/) og utviklerportalen (https://liquid.net/devs).

### Elementer

Elements ble lansert i 2015 og reduserer interne utviklings- og forskningskostnader og utnytter den aller nyeste blokkjedeteknologien, noe som åpner for mange nye bruksområder for implementering. En Elements-basert blokkjede kan enten fungere som en frittstående blokkjede eller kobles til en annen og kjøres som en sidekjede. Ved å kjøre Elements som en sidekjede kan aktiva overføres mellom ulike blokkjeder på en verifiserbar måte.

Den bygger på og utvider Bitcoins kodebase, slik at utviklere som er kjent med Bitcoins API, raskt og kostnadseffektivt kan lage fungerende blokkjeder og teste proof-of-concept-prosjekter. Siden Elements er bygget på Bitcoin-kodebasen, kan den også fungere som en testbed for endringer i selve Bitcoin-protokollen.

Noen av hovedfunksjonene i Elements er listet opp nedenfor.

#### Konfidensielle transaksjoner

Som standard er alle adresser i Elements blindet ved hjelp av konfidensielle transaksjoner. Blinding er en prosess der beløpet og typen aktiva som overføres, er kryptografisk skjult for alle, bortsett fra deltakerne og de de velger å avsløre blindingsnøkkelen for.

#### Utstedte eiendeler

Utstedte aktiva på Elements gjør det mulig å utstede og overføre flere typer aktiva mellom nettverksdeltakere. En utstedt eiendel drar også fordel av konfidensielle transaksjoner og kan utstedes på nytt eller ødelegges av alle som har det relevante gjenutstedelsestokenet.

#### Federated 2-veis pinne

Elements er en generell blokkjedeplattform som også kan "kobles" til en eksisterende blokkjede (for eksempel Bitcoin) for å muliggjøre toveis overføring av eiendeler fra den ene kjeden til den andre. Ved å implementere Elements som en sidekjede kan du omgå noen av de iboende egenskapene til hovedkjeden, samtidig som du beholder en god del av sikkerheten som eiendeler sikret i hovedkjeden gir.

#### Signerte blokker

Elements bruker en sterk føderasjon av signatører, kalt Block Signers, som signerer og oppretter blokker på en pålitelig og tidsriktig måte. Dette fjerner transaksjonsforsinkelsen i PoW-gruvedriftsprosessen, som er utsatt for store variasjoner i blokktid på grunn av den tilfeldige poissonfordelingen. Federated Block Signing-prosessen oppnår pålitelig opprettelse av blokker uten å introdusere behovet for tredjeparts tillit eller beregningsalgoritmebasert utvinning.

Elements legger til alle disse funksjonene på toppen av Bitcoin Core-kodebasen, utvider hovedkjedeprotokollens muligheter og muliggjør nye bruksområder når den distribueres som en sidekjede eller som en frittstående blokkjedeløsning.

# Element

<partId>ac68d611-be84-432f-a3a8-620d310e131c</partId>

## Hvordan Elements fungerer

<chapterId>05d88877-58b0-455b-9ae6-a72d19070525</chapterId>

![Video](https://youtu.be/v0lzmfH81AY?si=V-xDWfmDLKyBcdPs)

Elements tilbyr en teknisk løsning på problemer som blockchain-brukere møter daglig: transaksjonsforsinkelser, manglende personvern og risiko for fungibilitet.

Elements løser disse problemene ved å bruke Federated Block Signing og Confidential Transactions.

I motsetning til Bitcoin-nettverket er prosessen for blokksignering i Elements ikke avhengig av Dynamic Membership Multiparty Signatures (DMMS) og Proof of Work (PoW). I stedet bruker Elements en sterk føderasjon av signatører, kalt Block Signers, som kan signere og opprette blokker på en pålitelig og tidsriktig måte. Dette fjerner transaksjonsforsinkelsen i PoW-gruvedriftsprosessen, som er utsatt for store variasjoner i blokktid på grunn av den tilfeldige poissonfordelingen. Federated Block Signing-prosessen oppnår pålitelig opprettelse av blokker uten å innføre behovet for tillit fra tredjeparter.

Elements kan kjøre som en sidekjede til en annen blokkjede, for eksempel Bitcoin, eller som en frittstående blokkjede uten avhengigheter til andre nettverk.

Når Strong Federation brukes som en sidekjede, inneholder den også medlemmer som muliggjør sikker og kontrollert overføring av aktiva mellom en hovedkjede og en Elements sidekjede. Den kontrollerte overføringen av aktiva kalles Federated 2-Way Peg, og medlemmene som utfører overføringen av aktiva, kalles Watchmen.

Prosessene som inngår i driften av et Elements-nettverk, og rollene til deltakerne i nettverket, er viktige for å forstå hvordan Elements fungerer.

Enten den er implementert som en sidekjede eller en frittstående blokkjede, bruker Elements Strong Federations of Block Signers til å produsere blokker.

### Sterke forbund

Elements bruker en konsensusmodell som først ble foreslått av Blockstream, kalt Strong Federations. En sterk føderasjon trenger ikke Proof of Work (PoW), men baserer seg i stedet på de kollektive handlingene til en gruppe deltakere som har gjensidig mistillit til hverandre, såkalte funksjonærer.

Rollene en funksjonær kan fylle i en sterk føderasjon er: Block Signers og Watchmen. Block Signers er påkrevd hvis du kjører Elements i enten sidekjede- eller frittstående blokkjede-modus, mens Watchmen kun er påkrevd i et sidekjede-oppsett.

Handlingene et medlem av en sterk føderasjon kan utføre, er delt mellom to forskjellige roller for å øke sikkerheten og begrense skaden en angriper kan forårsake.

Når disse deltakernes roller kombineres, kan Elements levere både rask opprettelse av blokker (raskere og endelig transaksjonsbekreftelse) og sikre, overførbare eiendeler (pegged assets som kan knyttes direkte til en annen blokkjede).

Du kan lese Whitepaper om sterke føderasjoner her: https://blockstream.com/strong-federations.pdf

### Blokker signatører

En blokkjede som Bitcoins utvides når alle som inngår i en dynamisk gruppe av blokkunderskrivere, utvider kjeden ved å vise bevis på utført arbeid. Den dynamiske karakteren til settet introduserer latency-problemer som er iboende i slike systemer.

Ved å bruke et fast sett med signatarer erstatter en føderert modell det dynamiske settet med et kjent sett med flere signaturer. Ved å redusere antallet deltakere som trengs for å utvide blokkjeden, øker systemets hastighet og skalerbarhet, samtidig som validering av alle parter sikrer integriteten til transaksjonshistorikken.

Føderert blokksignering består av flere faser:


- Trinn 1 - Bloksignerere foreslår kandidatblokker i en runde til alle andre deltakende blokksignerere.
- Trinn 2 - Hver blokksignerer signaliserer sin intensjon ved å forplikte seg til å signere den gitte kandidatblokken.
- Trinn 3 - Hvis den gitte terskelen for forhåndsforpliktelse er nådd, signerer hver Block Signer blokken.
- Trinn 4 - Hvis signaturterskelen (som kan være forskjellig fra den i trinn 3) er oppfylt, blir blokken akseptert og sendt til nettverket. Den sterke føderasjonen har oppnådd konsensus om den siste transaksjonsblokken.
- Trinn 5 - Neste blokk foreslås deretter av neste Block Signer i runden, og prosessen gjentas.

Fordi blokkgenereringen i en sterk føderasjon ikke er probabilistisk og er basert på et fast sett med underskrivere, vil den aldri bli utsatt for omorganiseringer av flere blokker. Dette gjør det mulig å redusere ventetiden i forbindelse med bekreftelse av transaksjoner betydelig. Det fjerner også insentivet til å utvinne penger for å tjene penger (dvs. blokkbelønningen) og erstatter det med et insentiv til å delta produktivt i et nettverk der alle deltakerne har samme felles mål: å sikre at nettverket fortsetter å fungere på en måte som er gunstig for alle. Dette gjøres uten å innføre et enkelt feilpunkt eller høyere krav til tillit.

### Elementer som en sidekjede - Watchmen og Federated 2-veis Peg

Når en sidekjede drives som en sidekjede, har noen medlemmer av Strong Federation en ekstra rolle å fylle, nemlig rollen som Watchmen. Vaktmennene er ansvarlige for overføring av eiendeler til og fra en Elements sidekjede, prosesser kjent som "Peg-In" og "Peg-Out".

For at en sidekjede skal fungere på en troverdig måte, må den gjøre det mulig for deltakerne å verifisere at tilførselen av aktiva er kontrollert og verifiserbar. En Elements sidekjede bruker en toveis føderert peg for å muliggjøre toveis overføring av aktiva inn og ut av en Elements-blockchain. Dette tilfredsstiller kravene til bevisbar utstedelse og overføringer mellom kjeder.

Funksjonen Federated 2-way Peg gjør det mulig for en eiendel å være interoperabel med andre blokkjeder og representativ for en annen blokkjedes opprinnelige eiendel. Ved å knytte blokkjeden din til en annen, kan du utvide hovedkjedens muligheter og overvinne noen av dens iboende begrensninger.

Overføringer til sidekjeden skjer når noen sender eiendeler fra hovedkjeden til en adresse som kontrolleres av en Watchmen-lommebok med flere signaturer. Dette fryser effektivt eiendelene på hovedkjeden. Watchmen validerer deretter transaksjonen og frigjør den samme mengden av den tilknyttede eiendelen i sidekjeden. De frigjorte eiendelene sendes til en lommebok i sidekjeden som kan bevise at den gjør krav på de opprinnelige eiendelene i hovedkjeden. Denne prosessen flytter effektivt aktiva fra hovedkjeden til sidekjeden.

For å overføre eiendeler tilbake til hovedkjeden, foretar en bruker en spesiell peg-out-transaksjon på sidekjeden. Denne transaksjonen kontrolleres av Watchmen, som deretter signerer en transaksjonsutgift fra multisignaturlommeboken de kontrollerer på hovedkjeden. Et visst antall deltakere i føderasjonen må signere før transaksjonen i hovedkjeden blir gyldig. Når vekterne sender en eiendel tilbake til hovedkjeden, ødelegger de også det tilsvarende beløpet på sidekjeden, slik at eiendelene i praksis overføres mellom blokkjedene.

## Sette opp og kjøre elementer

<chapterId>cc806e5a-81ab-457b-9531-9f863120a019</chapterId>

![Video](https://youtu.be/Frr_OjTEPAM?si=iq5XonJyQk8S5OAu)

Ettersom Elements er basert på Bitcoin-kodebasen, er komponentene som utgjør et fungerende nettverk, svært like.

Selve Elements node-programvaren heter `elementsd` og kjører som en daemon på en brukers maskin. En daemon (eller tjeneste i Windows) er et program som kjører som en bakgrunnstjeneste uten å kreve direkte kontroll av en pålogget bruker.

Merk: I dette dokumentet vil vi alltid referere til elementsd som daemon-versjonen, men alt kan gjøres med elements-qt, forutsatt at serveralternativet er aktivert.

Elements-demonen kobler seg til andre noder i nettverket slik at den kan utveksle transaksjons- og blokkdata, validere og utvide sin lokale kopi av nettverkets blokkjede.

Elements-programvaren består også av et klientprogram kalt "elements-cli", som lar deg sende RPC-kommandoer (Remote Procedure Call) til elementsd fra kommandolinjen. Dette kan for eksempel brukes til å spørre om en lommeboksaldo, vise transaksjons- eller blokkdata eller kringkaste en transaksjon. Dette oppsettet bør være kjent for alle som har brukt Bitcoins ekvivalenter; bitcoind og bitcoin-cli.

Ettersom en Elements-node kan konfigureres ved å sende inn parametere ved oppstart eller via en konfigurasjonsfil, er det mulig å ha mer enn én instans kjørende på samme maskin. Dette er nyttig for test- og utviklingsformål, ettersom du kan sette opp ditt eget lokale nettverk på én enkelt maskin, der hver Elements-node har sin egen kopi av blokkjededataene, administrerer sitt eget utvalg av ubekreftede gyldige transaksjoner og lytter til RPC-forespørsler på forskjellige porter.

### Elements Code Repository and Community

Elements er et prosjekt med åpen kildekode, og kildekoden finnes i Elements GitHub-repositoriet på https://github.com/ElementsProject/elements. Repositoryet inneholder kildekoden for programmene elementsd og elements-cli, sammen med installasjons- og byggeverktøy, en rekke tester og en del instruksjonsdokumentasjon.

Som et supplement til kodelageret finnes også nettstedet https://elementsproject.org, en ressurs med fokus på fellesskapet som inneholder forklaringer på hva Elements er, hvordan det fungerer og en omfattende opplæringsdel. Opplæringen fokuserer på å lære om Elements ved å følge kommandolinjeeksempler og viser deg hvordan du kan bygge enkle skrivebords- og webapplikasjoner på toppen av programmet. Nettstedet inneholder også en liste over populære Elements-diskusjonsfora, og det ligger på GitHub, noe som gjør det mulig å bidra til innholdet på nettstedet.

For å kunne kjøre Elements på maskinen din må du først klone (laste ned en kopi av) kildekoden, installere eventuelle avhengigheter som koden har, og til slutt bygge daemon- og klientkjørbare filer. Deretter er Elements-programvaren klar til å konfigureres og kjøres.

## Konfigurere noder og nettverk

<chapterId>df1ec0aa-84ea-4149-af7a-b4523d67e1d9</chapterId>

Konfigurasjonsinnstillinger kan sendes til en Elements-node ved oppstart for å endre måten den kjører på, validerer data, kobler seg til andre noder og initialiserer blokkjededataene sine.

Innstillingene lastes enten inn fra den angitte filen `elements.conf` eller sendes inn som parametere via kommandolinjen.

Noen av tingene kan endres ved hjelp av disse parameterne:


- Navnet på standardaktivaen som brukes i en frittstående blokkjedeimplementering.
- Nummeret på den første eiendelen som ble opprettet.
- Aktivaen som skal brukes ved betaling av transaksjonsgebyrer i nettverket.
- Lagringsplassen for blokkjededatafilene.
- RPC-legitimasjonen som brukes til å koble til en Bitcoin-node.
- Terskelen `n av m` som må oppfylles, og de gyldige offentlige nøklene som kan signere blokker.
- Skriptet som må være tilfredsstillende for å overføre aktiva inn og ut av en sidekjede.
- Om du vil koble deg til en Bitcoin-node som en sidekjede eller ikke.

Mange av disse utgjør en del av nettverkets konsensusregler, så det er viktig at de brukes på alle noder ved oppstart. Noen kan endres etter at en kjede har blitt initialisert, mens andre må fikses etter at de har blitt brukt til å initialisere en kjede.

Bruken av parametere vil bli gjennomgått senere i kurset etter hvert som de relateres til de ulike delene.

### Grunnleggende operasjoner ved hjelp av kommandolinjen

Dette kurset vil vise eksempler som bruker programmet `elements-cli` til å foreta RPC-kall til en eller flere Elements-noder. Dette gjøres fra en terminaløkt, og for å gjøre kommandoene mer kortfattede vil det bli brukt et `alias`. Når du ser noe i retning av følgende kommandoer, vil du bruke denne konvensjonen:

```bash
e1-dae
e1-cli getnewaddress
```

`e1-dae` og `e1-cli` er egentlig en typografisk snarvei som gjør bruk av terminalens `alias`-funksjon. `e1-dae` og `e1-cli` vil faktisk bli erstattet når kommandoen kjøres, og kommandoen som kjøres vil være lik:

```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir1
$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir1 getnewaddress
```

Det vi ser ovenfor er et kall for å starte Elements-dæmonen og et kall til elements-cli-programmene som ligger i katalogen `$HOME/elements/src`, samt en verdi for parameteren `datadir`. Med parameteren `datadir` kan vi fortelle daemon- og klientinstansene hvor de skal finne konfigurasjonsfilene sine og, i daemonens tilfelle, hvor den skal lagre sin kopi av blokkjeden. Ettersom de deler en konfigurasjonsfil, vil klienten kunne gjøre RPC-kall til demonen.

Ved å kjøre kommandoen ovenfor på nytt, men med en annen `datadir`-verdi, kan vi starte mer enn én forekomst av Elements, hver med sin egen kopi av blokkjeden og konfigurasjonsinnstillingene. På denne måten vil vi bruke aliasene `e2-dae` og `e2-cli` i kurset for å referere til en annen datadir-katalog enn e1s. Så eksemplet ovenfor for vår andre `e2`-forekomst vil være:

```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir2
$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir2 getnewaddress
```

Dette vil gjøre det mulig for oss å utføre alle slags operasjoner, for eksempel transaksjoner mellom noder, utstedelse av aktiva og kontroll av bruk av blinding i konfidensielle transaksjoner mellom ulike noder i samme nettverk.

# Bruke Element Praktisk brukertilfelle

<partId>3f31a30a-957a-4813-b5fe-5dccbb5366f3</partId>

## Konfidensielle transaksjoner

<chapterId>263b1c5b-59ed-49e7-b811-95c354f41eae</chapterId>

![Video](https://youtu.be/-by2xBtXQeE?si=7bLo_geGn3qh7MXN)

I dette avsnittet lærer du hvordan du bruker funksjonen Konfidensielle transaksjoner i Elements.

Alle adresser i Elements er som standard blindet ved hjelp av konfidensielle transaksjoner, som gjør at beløpet og typen aktiva som overføres, kun er synlig for deltakerne i transaksjonen (og de de velger å avsløre blindingsnøkkelen for), samtidig som det kryptografisk garanteres at det ikke kan brukes flere mynter enn det som er tilgjengelig.

### Konfidensielle adresser og konfidensielle transaksjoner

Når du oppretter en ny adresse i Elements ved hjelp av kommandoen `getnewaddress`, blir den som standard opprettet som en konfidensiell adresse.

For å demonstrere konfidensielle transaksjoner lar vi e2 sende penger til seg selv og deretter prøve å se transaksjonen fra e1. Dette vil demonstrere den konfidensielle naturen til transaksjoner i Elements.

Alle nye adresser som genereres av en Elements-node, er konfidensielle som standard. Vi kan demonstrere dette ved å få e2 til å generere en ny adresse.

```
e2-cli getnewaddress
```

Legg merke til at adressen begynner med e1. Dette identifiserer den som en konfidensiell adresse. Hvis du undersøker adressen nærmere ved hjelp av kommandoen getaddressinfo, får du flere detaljer om adressen.

```
e2-cli getaddressinfo <address>
```

Du kan se at det finnes en confidential_key-egenskap som forteller oss at det er en konfidensiell adresse.

Confidential_key er den offentlige blindingnøkkelen, som legges til selve den konfidensielle adressen. Dette er grunnen til at en konfidensiell adresse er så lang.

Den har også en tilknyttet ikke-konfidensiell adresse. Hvis du ønsker å bruke vanlige, ikke-konfidensielle, transaksjoner i Elements, bør du sende eiendeler til denne adressen i stedet for til den med prefikset lq1.

Vi kan nå få e2 til å sende penger til adressen den har generert. Dette vil senere vise at e1, som ikke er en av de handlende partene, ikke vil kunne se detaljene i transaksjonen.

```
e2-cli sendtoaddress <address>
```

Legg merke til transaksjons-ID-en. Bekreft transaksjonen.

```
e2-cli -generate 101
```

Se på transaksjonen der e2 sendte noen midler til seg selv fra e2s eget perspektiv.

```
e2-cli gettransaction <txid>
```

Hvis du blar opp i transaksjonsdetaljene, kan du se at e2 kan vise beløpene som er sendt og mottatt, samt eiendelen som er handlet. Du kan også se egenskapene amountblinder og assetblinder, som brukes til å blinde detaljene for andre noder som ikke er involvert i transaksjonen.

For å sjekke detaljene for den samme transaksjonen fra e1 må vi først få tak i de rå transaksjonsdetaljene.

```
e1-cli getrawtransaction <txid>
```

Den returnerer rå transaksjonsdetaljer. Hvis du ser i vout-delen, kan du se at det er tre forekomster. De to første instansene er mottaks- og endringsbeløpene, og den tredje er transaksjonsgebyret. Av disse tre beløpene er gebyret det eneste du kan se en verdi for, ettersom gebyret i seg selv alltid er ublindet i Elements.

### Blendende nøkler

De to første vout-seksjonene viser "blinde intervaller" av verdibeløpene og forpliktelsesdataene som fungerer som bevis på det faktiske beløpet og typen aktiva som er omsatt.

Selv om vi skulle importere e2s private nøkkel til e1s lommebok, vil den fortsatt ikke kunne se beløpene og typen aktiva som er handlet, fordi den fortsatt ikke har kjennskap til den blinde nøkkelen som brukes av e2. Vi skal bevise dette ved å importere den private nøkkelen som brukes av e2s lommebok til e1s. Først må vi eksportere nøkkelen fra e2

```
e2-cli dumpprivkey <address>
```

Importer den deretter til e1.

```
e1-cli importprivkey <privkey>
```

Nå kan vi bevise at e1 fortsatt ikke kan se verdiene.

```
e1-cli gettransaction <txid>
```

Faktisk viser den 0 som tx-beløpet når det faktisk var 1.

For å kunne se den faktiske, ublinde verdien, trenger vi blindingnøkkelen. For å gjøre dette eksporterer vi først blendingsnøkkelen fra e2.

```
e2-cli dumpblindingkey <address>
```

Importer den deretter til e1.

```
e1-cli importblindingkey <address> <blinding key>
```

Når vi nå får transaksjonsopplysningene fra e1.

```
e1-cli gettransaction <txid>
```

Det viser at med den importerte blindingnøkkelen kan vi nå se den faktiske verdien 1 i transaksjonen.

I dette avsnittet har vi sett at bruken av en blinding key skjuler beløp og type eiendeler i en transaksjon, og at vi ved å importere den riktige blinding key kan avsløre disse verdiene. I praksis kan en blindingnøkkel for eksempel gis til en revisor, hvis det er behov for å verifisere beløp og type eiendeler som en part har. Funksjonen Konfidensielle transaksjoner i Elements gjør det også mulig å utføre "range proofs". Med dette kan man bevise at et beløp av en eiendel holdes innenfor et gitt intervall, uten at det er nødvendig å avsløre selve beløpet.

Vi har også sett at konfidensielle transaksjoner er valgfrie, men aktiveres som standard når en ny adresse genereres.

Det var alt for denne leksjonen; lykke til med quizen og på gjensyn i neste leksjon!

## Utstedte eiendeler

<chapterId>c33c7020-5975-457a-99db-4f8b90d1fa1c</chapterId>

![Video](https://youtu.be/XnY4WZUNSs4?si=dG8I5OoSh_0EBdvL)

I denne delen lærer du hvordan du bruker funksjonen Utstedte eiendeler i Elements.

Utstedte aktiva gjør det mulig å utstede og overføre flere typer aktiva mellom deltakerne i Elements-nettverket. Alle noder i nettverket kan utstede sine egne aktiva. Utstedelser kan representere fungibelt eierskap av alle typer aktiva, inkludert kuponger, sedler, valutaer, innskudd, obligasjoner, aksjer osv. Issued Assets åpner for å bygge tillitsløse børser, opsjoner og andre avanserte smartkontrakter som involverer selvutstedte aktiva.

En utstedt eiendel drar også nytte av konfidensielle transaksjoner, og de kan utstedes på nytt av alle som har det tilknyttede tokenet.

Det første trinnet er at vi trenger tilgang til to Elements-noder, som vi kaller e1 og e2. Nodene har fått blokkjedene sine tilbakestilt, og standardaktivaen er delt mellom dem.

De to nodene er på samme lokale nettverk og er koblet til hverandre, og de deler derfor de samme transaksjonene i transaksjonsmempoolen og identiske blokkjeder. Selv om de kjører på samme maskin, er det verdt å merke seg at de ikke deler de samme blokkjedefilene. Hver node administrerer sin egen lokale kopi av blokkjeden, som inneholder den samme transaksjonshistorikken fordi de er i konsensus og følger de samme protokollreglene som hverandre.

La oss begynne med å sjekke hver enkelt nodes oversikt over de eksisterende aktivautstedelsene i nettverket.

Dette gjøres ved hjelp av kommandoen listissuances.

```
e1-cli listissuances
e2-cli listissuances
```

Som du kan se, viser begge nodene den samme utstedelseshistorikken. Begge viser én eiendel, den første utstedelsen av 21 millioner bitcoin, som ble opprettet da kjeden ble initialisert. Du kan se hex-id-en til eiendelen i resultatene av kommandoen ovenfor, og også etiketten som er tilordnet eiendelen, som er "bitcoin".

Det er verdt å merke seg at standardaktiva alltid får en etikett når kjeden initialiseres. Når du utsteder dine egne ressurser, kan du selv angi merkelapper for dem, noe vi skal gjøre om litt. Før vi kan gjøre det, må vi utstede vårt eget aktivum.

Vi får e1 til å utstede det nye aktivumet. Dette gjøres ved hjelp av kommandoen issueasset.

```
e1-cli issueasset 100 1 false
```

`issueasset` aksepterer 3 parametere.

Mengden av den nye eiendelen som skal utstedes, vi har brukt 100. Antall tokens som skal opprettes (tokens brukes til å utstede nye mengder av en eiendel), hvorav vi valgte 1. Den siste parameteren forteller Elements om aktivautstedelsen skal være blinded eller unblinded. Vi bruker unblinded ettersom vi ønsker å se utstedelsesbeløpene fra e2 om et øyeblikk, så vi skriver inn false.

Når du kjører kommandoen, returneres data om utstedelsen. Disse inkluderer transaksjons-ID-en, som du kan ta en kopi av for senere bruk, den unike hex-verdien til eiendelen og den unike hex-verdien til eiendelens token.

Generer en blokk for å bekrefte utstedelsestransaksjonen.

```
e1-cli -generate 1
```

Kjør kommandoen `listissuances` mot e1 igjen.

```
e1-cli listissuances
```

Det viser oss at e1 nå er klar over to utstedelser, den første utstedelsen av Bitcoin og den nyutstedte eiendelen vår, som vi kan se 100 av. Legg merke til hex-verdien til den nye eiendelen, og at det ikke er noen tilknyttet eiendelsetikett, slik det er for bitcoin-utstedelsen.

Sjekk e2s liste over kjente utstedelser igjen.

```
e2-cli listissuances
```

Det viser oss at e2 ikke er klar over aktivautstedelsen e1 foretok. Den kan bare se den opprinnelige utstedelsen av bitcoin som den allerede kunne se.

Dette skyldes at e2 ikke er klar over, og ikke ser, adressen som det nye aktivumet ble sendt til da det ble utstedt av e1.

Det er verdt å merke seg at selv om e2 ikke kan se selve utstedelsen, kan e1 likevel sende e2 noe av eiendelen. Det nye aktivumet vil da dukke opp som en tilgjengelig saldo i e2s lommebok, selv om den ikke er klar over den opprinnelige utstedelsen.

For at e2 skal kunne se den faktiske utstedelsen (og dermed det utstedte beløpet), må vi legge til adressen i e2 som en overvåket adresse.

For å gjøre dette må vi finne ut adressen som eiendelen ble sendt til. Til dette bruker vi transaksjons-ID-en vi kopierte tidligere, og får e1 til å hente detaljene for den transaksjonen, slik at vi kan finne ut hvilken adresse som skal legges til i overvåkningslisten til e2.

```
e1-cli gettransaction <the-issuance-transaction-id>
```

Hvis du blar opp forbi hex-verdien i transaksjonsdataene, ser du adressen som mottok 100 av de nye eiendelene våre, identifisert ved sin hex-verdi.

Kopier adressen slik at vi kan importere den til e2.

La oss nå importere adressen til e2. For å gjøre dette bruker vi kommandoen importaddress.

```
e2-cli importaddress <the-issued-to-address>
```

Hvis vi nå sjekker e2s liste over utstedelser.

```
e2-cli listissuances
```

Du kan se at den nyutstedte eiendelen vår nå er inkludert i listen. E2-noden kan også fastslå beløpet for eiendelen som ble utstedt, sammen med beløpet for det tilknyttede tokenet, ettersom utstedelsen var en ublindet utstedelse. For å aktivere bruken av asset-ID til navnemapping i Elements, må du først stoppe Elements.

```
e1-cli stop
```

Start den deretter på nytt med en tilleggsparameter som tilordner ressursens hex-kode til den angitte etiketten. Dette gjør det mulig for noden å vise data om ressursen i et mer lesbart format. Du kan legge til dette på slutten av elements.conf hvis du foretrekker det, så trenger du ikke å legge til argumentet til daemon hver gang du starter den. For eksempel

```
assetdir=5186d0bc8ed15e6ef85571bd2d8070573adf0e06fd4507082694526975ce4f35:My new asset (MNA)
```

Men vi vil bruke argumentmetoden her.

```
e1-dae -assetdir=<assetid-here>:<name-of-the-new-asset>
```

Spør noden etter en liste over utstedelser igjen.

```
e1-cli listissuances
```

Det viser oss at tilordningen av eiendelens hex-verdi til etiketten fungerer. Vi sjekker igjen på e2-nodens liste over utstedelser.

```
e2-cli listissuances
```

Du kan se at e2-noden ikke har tilgang til denne etiketten, fordi etiketter bare er tilgjengelige for den noden som har angitt dem. Vi kan faktisk tilordne en annen etikett til den samme ressursen hex på e2 enn vi gjorde på e1. Først stopper vi e2-noden.

```
e2-cli stop
```

Start på nytt med en annen etikett som er tilordnet hexen til den nye ressursen vår.

```
e2-dae -assetdir=<assetid-here>:<another-name-for-the-new-asset>
```

Notering av utstedelser fra e2.

```
e2-cli listissuances
```

Asset-etikettene er lokale for hver enkelt node, og det er bare hexen til asset som gjenkjennes av andre noder i nettverket.

Tilordningen av etikett til aktivaheks er nyttig når du utfører handlinger som transaksjoner og forespørsler om saldo i lommeboken, ettersom det gir en kortfattet måte å referere til en eiendel på. Hvis vi for eksempel ønsker å sende noe av den nye eiendelen vår (et beløp på 10) fra e1 til e2 uten å bruke etiketten.

Først må vi finne en adresse å sende ressursen til.

```
e2-cli getnewaddress
```

Bruk deretter kommandoen sendtoaddress.

```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <asset-id-here>
```

Bekreft transaksjonen ved å generere en blokk.

```
generate 1
```

Kontrollerer at eiendelen ble mottatt på e2.

```
e2-cli getwalletinfo
```

Vi kan se at eiendelen faktisk ble mottatt.

Legg merke til at e2 tilordner hex-koden til den mottatte ressursen og viser den ved hjelp av sin egen etikett. En enklere måte å gjøre det samme på ville vært å bruke e1s asset-label ved sending.

```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <name-of-the-new-asset>
```

Bak kulissene tilordner Elements lokale etiketter til hex-verdier for å forenkle bruken av utstedte ressurser.

I dette avsnittet har vi sett hvordan du utsteder og merker eiendeler. I neste avsnitt skal vi se på gjenutstedelse og destruksjon av mengder av en utstedt eiendel.

## Gjenutstedelse av eiendeler

<chapterId>78751b21-1dc8-4877-a406-e71bc80a95b0</chapterId>

![Video](https://youtu.be/5em79YHtYk0?si=rhponm6Hw9AB6RJp)

I denne delen lærer du hvordan du kan utstede mer av en allerede utstedt eiendel, og hvordan du kan destruere en gitt mengde av en utstedt eiendel.

Behovet for å utstede (skape mer) av en eiendel eller destruere en mengde av eiendelen er noe som sannsynligvis vil oppstå når eiendelen representerer noe som ikke har en fast forsyning. Dette kan for eksempel gjelde eiendeler som representerer gull i et hvelv. Etter hvert som enheter av gull flyttes inn og ut av hvelvet, må eiendelen som representerer hvelvets beholdning, justeres opp eller ned tilsvarende.

For å kunne utstede en mengde av en eiendel på nytt må man eie det tilknyttede tokenet som ble opprettet sammen med eiendelen da den opprinnelig ble utstedt.

Når du oppretter flere eksemplarer av et aktivum, spiller det ingen rolle hvilken node som utstedte aktivumet i utgangspunktet, så lenge noden som utsteder en ny mengde av et aktivum, er i besittelse av det som vanligvis kalles aktivumets reutstedelsestoken. Vi skal se på hvordan du oppretter gjenutstedelsestokenet, hvordan du bruker det til å gjenutstede en mengde av et aktivum, og hvordan du overfører gjenutstedelsestokenet til andre noder, slik at de også har tillatelse til å gjenutstede aktivumet.

Vi trenger tilgang til to Elements-noder, som vi kaller e1 og e2. Nodene har fått blokkjedene sine tilbakestilt, og standardaktivaen er delt mellom dem.

Vi lar e1 utstede 100 av en ny eiendel og opprette 1 gjenutstedelsestoken for den samme eiendelen. Vi oppretter utstedelsen som ublindet for å forenkle eksempelet. Så la oss gå videre og utstede eiendelen og det tilhørende reutstedelsestokenet.

```
e1-cli issueasset 100 1 false
```

Legg merke til ID-en til eiendelen og (gjenutstedelses-)tokenet.

Siden vi senere skal utstede flere av eiendelene på nytt fra e2, må vi notere transaksjons-ID-en som eiendelen ble utstedt i, og bruke den til å importere adressen eiendelen ble sendt til.

Bekreft transaksjonen.

```
e1-cli -generate 1
```

Vi skal nå sjekke transaksjonsdetaljene ved hjelp av kommandoen gettransaction:

```
e1-cli gettransaction <txid>
```

Hvis du blar opp forbi sekskanten i transaksjonsdataene, ser du at e1 i transaksjonen mottok 1 gjenutstedelsestoken og 100 av den tilknyttede eiendelen.

Ta en kopi av adressen slik at vi kan importere den til e2.

Og nå importerer jeg adressen til e2s lommebok.

```
e2-cli importaddress <address>
```

Vi kan nå se at både e1 og e2 er klar over utstedelsen av eiendelen.

```
e1-cli listissuances
e2-cli listissuances
```

For øyeblikket har e1 en mengde av eiendelen og 1 gjenutstedelsestoken, men e2 har ikke det.

```
e1-cli getwalletinfo
```

Legg også merke til at e1 har mindre av standardaktivaen enn tidligere fordi den betalte et lite beløp for å dekke transaksjonsgebyrer. Dette beløpet skal e1 kreve inn når den opprettede blokken er modnet over 100 blokker dyp.

```
e2-cli getwalletinfo
```

Ettersom e1 har gjenutstedelsestokenet, kan den gjenutstede flere av det. Dette gjøres ved å bruke kommandoen reissueasset. La oss la e1 utstede ytterligere 100 av eiendelen.

```
e1-cli reissueasset <asset-id> 100
```

Kontrollen av gjenutstedelsen fungerte.

```
e1-cli getwalletinfo
```

Du kan se at e1 nå har 200 av eiendelen som forventet.

Ettersom e2 ikke har et beløp av gjenutstedelsestokenet, vil de få en feilmelding hvis de prøver å utstede eiendelen på nytt.

```
e2-cli reissueasset <asset-id> 100
```

Legg merke til feilmeldingen.

Vi kan se detaljene for gjenutstedelsen fra e1 ved hjelp av kommandoen listissuances.

```
e1-cli listissuances
```

Legg merke til flagget `is_reissuance`.

Hvis vi nå sender e2 et beløp av gjenutstedelsestokenet, vil de selv kunne gjenutstede et beløp av eiendelen. Først trenger vi en adresse å sende det til. Det er verdt å merke seg at reissuance-tokenet behandles på samme måte som alle andre aktiva i elements når du sender og viser saldoer, og at det også kan brytes ned til mindre valører som alle andre aktiva, så vi trenger ikke å sende 1 reissuance-token til e2 for at de skal kunne utstede aktivumet på nytt. Alle valører vil være tilstrekkelig. Generering av en adresse for e2 for å motta gjenutstedelsestokenet.

```
e2-cli getnewaddress
```

Send deretter en brøkdel av RIT fra e1 til e2.

```
e1-cli sendtoaddress <address-of-e2> 0.1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Bekreft transaksjonen.

```
e1-cli -generate 1
```

Vi kan nå se at e2 holder de 0,1 den ble sendt.

```
e2-cli getwalletinfo
```

Dette betyr at e2 nå kan utstede flere av eiendelen som er knyttet til RIT-en den har i lommeboken sin. Vi får e2 til å utstede 500 av eiendelen på nytt.

```
e2-cli reissueasset <asset-id> 500
```

Kontroller resultatet av gjenutstedelsen.

```
e2-cli getwalletinfo
```

Du kan se at e2 nå har det gjenutstedte beløpet i lommeboken sin, og at selve RIT-en ikke forbrukes i prosessen med gjenutstedelse av aktiva.

Å ødelegge en mengde av en eiendel er noe alle som har minst den mengden som ødelegges, kan gjøre, og det er ikke styrt av gjenutstedelsestokenet.

```
e2-cli destroyamount <asset-id>
e2-cli getwalletinfo
```

I denne delen har vi sett hvordan man utsteder en eiendel, og hvordan man bruker reissuance-tokenet som eventuelt opprettes som en del av utstedelsen av eiendelen. Vi har også sett hvordan det er like enkelt å overføre et reissuance-token som å overføre et hvilket som helst annet aktivum, og at det å inneha et hvilket som helst beløp av et reissuance-token gir innehaveren rett til å utstede flere av det tilknyttede aktivumet. Det er derfor svært viktig å kontrollere hvem som har tilgang til reissuance-tokens i nettverket ditt. Vi har også sett hvordan man kan ødelegge en mengde av en eiendel, og at denne prosessen ikke kontrolleres av besittelsen av reissuance-tokenet.

# Element Federation

<partId>173a2440-0203-4dcc-8e2b-f8fa2cc8d3ca</partId>

## Blokkere signering

<chapterId>c47b217e-db14-4843-a66f-3e5f3a00a808</chapterId>

![Video](https://youtu.be/kxWX91fCnus?si=KItm_Am3_RrBcLBN)

Elements støtter en føderert signeringsmodell som gjør det mulig å angi hvor mange Strong Federation-medlemmer som må signere en foreslått blokk for å produsere en gyldig blokk.

Tidligere har vi for eksempel opprettet blokker ved hjelp av kommandoen `generate`, som ikke har behøvd å oppfylle et krav om multisignatur for at de opprettede blokkene skal bli akseptert av nettverket som gyldige.

Vi skal sette opp nodene våre slik at de krever oppretting av 2-av-2 multisig-blokker. Dette settes opp ved hjelp av parameteren signblockscript, som kan legges til i konfigurasjonsfilen eller sendes inn i noden ved oppstart. For å initialisere en kjede med denne parameteren, må vi først bygge skriptet som den består av.

Vi gjør dette ved hjelp av noen eksisterende noder, lagrer dataene de sender ut, og sletter deretter kjeden slik at vi kan starte den på nytt ved hjelp av signblockscript-parameteren vår. Dette er nødvendig ettersom skriptet er en del av nettverkets konsensusregler og må settes ved initialisering av kjeden. Det kan ikke legges til på et senere tidspunkt i en allerede eksisterende kjede.

Vi trenger tilgang til to Elements-noder, som vi kaller e1 og e2. Nodene har fått blokkjedene sine tilbakestilt, og standardaktivaen er delt mellom dem.

Sørg for at parameteren con_max_block_sig_size er satt til en høy verdi i elements.conf-filen, ellers vil blokksigneringen mislykkes senere i dette avsnittet. Vi har satt con_max_block_sig_size=2000 for denne veiledningen.

Ettersom vi skal nullstille blokkjeden og slette lommebøkene som er knyttet til e1 og e2, må vi ta en kopi av adressene, de offentlige nøklene og de private nøklene vi bruker til å generere blokksigneringsskriptet, slik at vi kan bruke dem senere.

Først må hver av de kommende blokksigneringsnodene generere en ny adresse, som du må ta en kopi av.

```
e1-cli getnewaddress
e2-cli getnewaddress
```

Deretter må vi hente ut de offentlige nøklene fra adressene og notere dem for senere bruk.

```
e1-cli getaddressinfo <e1-address>
e2-cli getaddressinfo <e2-address>
```

Deretter trekker vi ut de private nøklene, som vi importerer på nytt senere, slik at nodene kan signere blokkene etter at vi har initialisert blokkjeden og lommebokdataene på nytt.

```
e1-cli dumpprivkey <e1-address>
e2-cli dumpprivkey <e2-address>
```

Nå må vi generere et redeem-skript med et 2 av 2 multisignaturkrav. Dette gjør vi ved å bruke kommandoen createmultisig og sende den første parameteren som 2 og deretter oppgi to offentlige nøkler. Det er disse nøklene som eierskapet til må bevises senere når blokken opprettes.

En av nodene, e1 eller e2, kan generere multisig.

```
e1-cli createmultisig 2 '["<e1-pubkey>", "<e2-pubkey>"]'
```

Dermed har vi fått vårt redeemscript, som du kan kopiere for senere bruk.

Nå må vi slette den eksisterende blokkjeden og lommebokdataene, slik at vi kan starte på nytt med det nye signblockscriptet som en del av kjedens konsensusregler. Det er derfor vi måtte ta en kopi av noen av dataene tidligere, for eksempel de private nøklene som skal brukes i den nye kjeden til å signere blokker. Du må gjøre dette før du fortsetter.

Med eksisterende lommebok- og kjededata slettet kan vi nå starte nodene våre og få dem til å initialisere en ny kjede ved hjelp av signblockscript-parameteren. La oss sende inn -evbparams=dynafed:0:::: for å deaktivere dynafed-aktivering, fordi vi ikke trenger den avanserte funksjonen for dette eksemplet.

```
e1-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::
e2-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::
```

Nå må vi importere de private nøklene som vi lagret tidligere, slik at nodene våre kan signere og bidra til å fullføre foreslåtte blokker.

```
e1-cli importprivkey <e1-priv-key>
e2-cli importprivkey <e2-priv-key>
```

Bruken av kommandoen generate bør nå feile fordi den ikke oppfyller de nødvendige blokksigneringsreglene som nå håndheves av nodene våre.

```
e1-cli -generate 1
```

For å foreslå en ny blokk kan hver av nodene kalle kommandoen getnewblockhex. Denne kommandoen returnerer hex-koden til en ny blokk som må signeres før den blir akseptert av nodene i nettverket.

```
e1-cli getnewblockhex
```

Husk at kommandoen bare oppretter en foreslått blokk, den genererer ikke en.

For å bekrefte dette kan vi se at det for øyeblikket ikke finnes noen blokker i blokkjeden vår.

```
e1-cli getblockcount
```

Hvis vi prøver å sende inn blokkheksen uten å signere den først.

```
e1-cli submitblock <block-hex>
```

Vi får en melding om at blokkbeviset er ugyldig. Dette skyldes at det ennå ikke er signert av to av de to partene som kreves.

Så la oss få e1 til å signere den foreslåtte blokken.

```
e1-cli signblock <block-hex>
```

Få e2 til å signere sekskanten.

```
e2-cli signblock <block-hex>
```

Legg merke til at e2 ikke signerer utdataene som skapes ved at e1 signerer den foreslåtte blokken. De signerer begge den foreslåtte blokken hex uavhengig av hverandres resultater.

Nå må vi kombinere blokksignaturene til e1 og e2. Begge nodene kan gjøre dette, alt de trenger er den signerte blokkhexen fra den andre noden.

```
e1-cli combineblocksigs <block-hex> '["<signed-hex-from-e1>", "<signed-hex-from-e2>"]'
```

Du kan se at kommandoen combineblocksigs sender ut hex-koden til den signerte blokken samt statusen complete, som forteller oss at blokkens hex-kode er klar til å sendes inn.

Nå kan begge nodene sende inn den fullførte blokkheksen. Vi lar e1 gjøre det.

```
e1-cli submitblock <combined-signed-hex>
```

Kontrollerer at innsendingen var gyldig.

```
e1-cli getblockcount
e2-cli getblockcount
```

Du kan se at både e1 og e2 har akseptert blokken som gyldig og lagt den til i toppen av sine lokale kopier av blokkjeden.

For å oppsummere prosessen. I denne delen har vi


- Foreslått en blokk.
- Fikk hver node til å signere den.
- Kombinerte signaturene.
- Sjekket at signaturene er gyldige og oppfyller kjedens innløsningsterskel.
- Sendte inn blokken.

Hver node i nettverket validerte blokken og la den til i sin lokale kopi av blokkjeden.

### Block SIgning

Selv om prosessen i utgangspunktet virker kompleks, er sekvensen for blokksignering i Elements alltid den samme, og det første oppsettet trenger bare å utføres én gang:

1. Førstegangsoppsett (utføres én gang)

2. Det opprettes en multisignaturadresse kalt `signblockscript` ved hjelp av de offentlige nøklene til Federated Block Signers.

3. Redemo-skriptet fra dette brukes til å starte en ny blokkjede.

4. Blokkproduksjon (pågående)

5. Foreslåtte blokker genereres og utveksles for signering.

Når et visst antall signatører har signert den foreslåtte blokken, blir den kombinert og sendt til nettverket. Hvis den oppfyller kriteriene i kjedens `signblockscript`, godtar nodene den som en gyldig blokk.

## Element som sidekjede

<chapterId>432d7a65-255f-44a3-8b38-78508202cb37</chapterId>

![Video](https://youtu.be/egYzj4N8CB8?si=v7_-IXsjHPE-ARDe)

Elements er en åpen kildekodeplattform for blokkjeder som også kan "kobles" til en eksisterende blokkjede, for eksempel Bitcoin. Når Elements er knyttet til en annen blokkjede, sies det at den fungerer som en "sidekjede". Sidekjeder muliggjør toveis overføring av eiendeler fra én kjede til en annen. Ved å implementere Elements som en sidekjede kan du omgå noen av de iboende begrensningene til hovedkjeden, samtidig som du beholder en god del av sikkerheten som eiendeler sikret på hovedkjeden gir.

Mens en sidekjede kjenner til hovedkjeden og dens transaksjonshistorikk, har hovedkjeden ingen kjennskap til sidekjeden, og det er heller ikke nødvendig for driften av den. Dette gjør det mulig for sidekjedene å innovere uten begrensninger eller forsinkelser forbundet med forslag til forbedringer av hovedkjedens protokoll. I stedet for å forsøke å endre den direkte, gjør utvidelsen av hovedprotokollen det mulig for hovedkjeden å forbli sikker og spesialisert, slik at sidekjeden kan fungere problemfritt.

Ved å utvide funksjonaliteten til Bitcoin og utnytte den underliggende sikkerheten, kan en Elements-basert sidekjede tilby ny funksjonalitet som tidligere ikke var tilgjengelig for brukere av hovedkjeden. Et eksempel på en Elements-basert sidekjede i produksjonsbruk er Liquid Network.

For å initialisere en Elements-blockchain som en sidekjede, må vi bruke skriptparameteren federated peg. Denne parameteren kan angis i en nodes konfigurasjonsfil eller sendes inn ved oppstart.

Det fødererte peg-skriptet definerer hvilke medlemmer av den sterke føderasjonen som kan utføre peg-in- og peg-out-funksjoner. Disse funksjonærene kalles "vakter", ettersom de overvåker hovedkjeden og sidekjeden for gyldige peg-in- og peg-out-transaksjoner og utfører dem hvis de er gyldige. Å "pegge ut" betyr å flytte pegged assets ut av sidekjeden og inn i hovedkjeden, og å "pegge inn" betyr å flytte pegged assets inn i sidekjeden fra hovedkjeden. Når vi sier "flytte inn i sidekjeden", mener vi egentlig at midlene blir låst i en multisignaturadresse på hovedkjeden, og at en tilsvarende mengde av eiendelen opprettes på Elements sidekjede. Når vi sier "flytte ut av sidekjeden", mener vi at aktiva ødelegges på Elements sidekjede, og at tilsvarende beløp frigjøres fra de låste midlene på hovedkjeden. Tillatelse til å utføre peg-in- og peg-out-funksjonene krever at funksjonærene beviser eierskap til de offentlige nøklene som brukes i det fødererte peg-skriptet. Dette gjøres ved bruk av de tilsvarende private nøklene.

For å opprette et føderert peg-skript må vi derfor først få hver av nodene våre til å generere en offentlig nøkkel. Vi må også lagre de tilhørende private nøklene for senere bruk, ettersom vi må slette alle eksisterende kjededata og initialisere en ny kjede ved hjelp av det fødererte peg-skriptet. Dette er fordi det fødererte peg-skriptet utgjør en del av konsensusreglene for en sidekjede, og det kan ikke brukes på en eksisterende, ikke-pegget blokkjede på et senere tidspunkt.

Så la oss generere en adresse med hver av nodene våre, lagre de relevante dataene for senere bruk og generere det fødererte peg-skriptet som vi skal bruke til å initialisere sidekjeden vår senere.

Først må hver av nodene våre, som skal fungere som vakter i nettverket vårt, generere en ny adresse.

```
e1-cli getnewaddress
e2-cli getnewaddress
```

Deretter validerer vi adressen for å få tak i de offentlige nøklene.

```
e1-cli getaddressinfo <e1-address>
e2-cli getaddressinfo <e2-address>
```

Og deretter henter du de private nøklene som er knyttet til hver adresse.

```
e1-cli dumpprivkey <e1-address>
e2-cli dumpprivkey <e2-address>
```

Lagre de private og offentlige nøklene for senere bruk.

Nå må vi slette den eksisterende blokkjeden og lommebokdataene, siden vi skal initialisere en ny kjede ved hjelp av et føderert peg-skript. Du kan gjøre dette nå. Ikke glem å starte Bitcoin-daemon, som vi trenger for å pegge inn.

Nå kan vi initialisere en ny kjede med et føderert peg-skript som er opprettet ved hjelp av de offentlige nøklene vi lagret tidligere. Tallene vi skriver inn og som omgir de offentlige nøklene våre, definerer og avgrenser antallet nøkler som brukes, og nøkkeleierskapet som må bevises for å kunne pegge inn og ut av sidekjeden vår.

```
e1-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae
e2-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae
```

Nå skal vi importere de private nøklene som vi lagret tidligere, slik at nodene våre senere kan signere og fullføre overføringen av eiendeler mellom kjedene og oppfylle kravene i det fødererte peg-skriptet.

```
e1-cli importprivkey <priv-key-1>
e2-cli importprivkey <priv-key-1>
```

Vi må nå modne noen blokker i begge kjedene. Modning av blokker er et krav i peg-prosessen, ettersom det beskytter mot at omorganiseringer av blokker i hovedkjeden fører til en inflasjon av det peggede aktivatilbudet i sidekjeden.

For å holde dette avsnittet fokusert på den fødererte pinnen, vil vi generere blokker uten å bruke blokksigneringsmodellen vi så på i forrige avsnitt, og gå tilbake til å bruke kommandoen "generate" for å opprette nye blokker.

```
b-cli generate 101
e1-cli generate 1
```

Vi trenger ikke nødvendigvis å generere blokker for elementer akkurat nå. Men la oss generere en likevel. Det er god praksis for å unngå potensielle inkonsekvenser.

Nå er kjeden vår klar til å pegge inn. For å kunne peg-in må vi generere en spesiell type adresse ved hjelp av kommandoen getpeginaddress. Vær oppmerksom på at det bør gå så kort tid som mulig fra du genererer en peg-in-adresse med getpeginaddress til du gjør krav på den med claimpegin. peg-in-adresser er ikke langtidsholdbare og bør ikke gjenbrukes.

```
e1-cli getpeginaddress
```

Du kan se at kommandoen oppretter en ny hovedkjedeadresse, samt et nytt skript som må tilfredsstilles for å gjøre krav på peg-in-midlene. Hovedkjedeadressen er en `pay to script hash`-adresse som vil bli brukt av funksjonærer som utfører Watchmen-rollen i Elements-nettverket.

I likhet med getnewaddress legger getpeginaddress til en ny hemmelighet i den anropende nodens lommebok, så det er viktig å ta hensyn til sikkerhetskopiering av lommebokfilen i nodeadministrasjonsprosessen.

Vi skal nå sende noen bitcoin fra hovedkjeden til sidekjeden. Regresjonstestlommeboken vår i hovedkjeden har allerede noen midler.

```
b-cli getwalletinfo
```

Vi ser at lommeboken inneholder 50 bitcoin. Vi sender én bitcoin fra hovedkjeden til sidekjeden. Vi må sende penger til hovedkjedeadressen noden vår genererte tidligere.

```
b-cli sendtoaddress <e1-pegin-address>
```

Vi må ta vare på ID-en for denne transaksjonen, da vi trenger den som bevis på finansiering senere.

Vi kan nå se at saldoen i hovedlommeboken har sunket med beløpet vi sendte, pluss et ekstra lite beløp for å dekke transaksjonsgebyrene.

```
b-cli getwalletinfo
```

Vi må modne transaksjonen på nytt.

```
b-cli generate 101
```

For at Elements-noden vår skal kunne gjøre krav på peg-in-midlene, må vi skaffe et "bevis" på at peg-in-transaksjonen har blitt gjennomført. Det kryptografiske beviset bruker finansieringstransaksjonens ID til å beregne merkelbanen og beviser at transaksjonen er til stede i en bekreftet blokk.

```
b-cli gettxoutproof '["<tx-id>"]'
```

Vi trenger også de rå transaksjonsdataene.

```
b-cli getrawtransaction <tx-id>
```

Med beviset og rådataene for peg-in-transaksjonen kan elementnoden vår nå gjøre krav på peg-in ved hjelp av råtransaksjonen og transaksjonsbeviset.

```
e1-cli claimpegin <raw> <proof>
```

Merk at det finnes et valgfritt tredje argument som vi kunne ha gitt til claimpegin. Denne tredje parameteren kan brukes til å spesifisere sidekjedeadressen som de innkrevde midlene skal sendes til. Dette var ikke nødvendig i vårt eksempel, ettersom vi kalte kommandoen fra den samme noden som eier adressen som de innkrevde midlene skal sendes til.

Kontrollerer saldoen på e1.

```
e1-cli getwalletinfo
```

Genererer en blokk for å bekrefte kravet.

```
e1-cli generate 1
```

Kontrollerer saldoen på e1.

```
e1-cli getwalletinfo
```

Vi kan se at peg-in har blitt gjort krav på.

For peg-out er prosessen lik. En adresse genereres, penger sendes til den, og pengene frigjøres hvis transaksjonen er gyldig. Vi kommer ikke til å gå gjennom hele peg-out-prosessen, ettersom den involverer arbeid på hovedkjeden, noe som ligger utenfor dette kursets omfang. Trinnene i Elements-hendelsene er at det genereres en adresse i hovedkjeden.

```
b-cli getnewaddress
```

Midler sendes til hovedkjedeadressen fra en Elements-node ved hjelp av kommandoen sendtomainchain.

```
e1-cli sendtomainchain <new-address> 1
```

Genererer en blokk for å bekrefte transaksjonen.

```
e1-cli generate 1
```

Sjekk saldoen i nodens lommebok.

```
e1-cli getwalletinfo
```

Og se at saldoen har gått ned.

I dette avsnittet har vi sett hvordan du gjør det:


- Generer et føderert peg-skript.
- Initialiser en ny kjede som bruker skriptet som en parameterregel for nettverkskonsensus.
- Send penger fra hovedkjeden til sidekjeden.
- Gjør krav på midlene i Elements sidekjede.
- Forstå hvordan det å sende penger tilbake til hovedkjeden startes.

### FederatedPegScript

For at Elements skal kunne fungere som en sidekjede, må genesis-blokken i blokkjeden opprettes med et `fedpegscript` på plass. Dette gjøres ved å sende inn parameteren `fedpegscript` ved oppstart av noden. Skriptet vil da være en del av Elements-blockkjedens konsensusregler og gjøre det mulig å validere og utføre peg-in- og peg-out-forespørsler.

Fedpegscript består av offentlige nøkler som kontrolleres av de som er autorisert til å utføre peg-handlingene. Følgende viser et eksempel på formatet til et fedpegscript med 2-av-2 multisignaturer:

```
fedpegscript=5221<public key 1>21<public key 2>52ae
```

Merk: Tegnene utenfor de offentlige nøklene er skilletegn som angir krav til offentlig nøkkel og `n av m`. Malen for et 1-av-1 fedpegscript vil for eksempel være '5121<offentlig nøkkel 1>51ae'.

### Peg-in

Før en peg-in kan aksepteres av en Elements-sidekjede, må den ha tilstrekkelig med bekreftelser på hovedkjeden. Dette er nødvendig for å unngå inflasjon i tilbudet av den peggede eiendelen på Elements sidekjede, noe som kan forårsakes av en omorganisering av hovedkjeden.

Korte omorganiseringer av spissen av Bitcoin-blokkjeden forventes som en del av den normale driften av Proof of Work (PoW)-konsensusmekanismen. Elements aksepterer derfor kun en peg-in som gyldig når den har tilstrekkelig dybde i Bitcoin-blokkjeden. Dette forhindrer Elements fra å akseptere samme peg-in mer enn én gang.

### Peg-Out

En peg-out oppstår når en Elements-node kaller kommandoen `sendtomainchain`, som tar som input en hovedkjedeadresse (peg-out-destinasjonen) samt beløpet på den peggede eiendelen som skal `trekkes ut`. Dette oppretter en peg-out-transaksjon på sidekjeden. Når funksjonærene som fungerer som vektere oppdager at peg-out-transaksjonen er bekreftet på sidekjeden, sørger de for å frigjøre eiendelen på hovedkjeden til peg-out-destinasjonen, slik vi har lært i tidligere deler av kurset.

## Elementer som en frittstående blokkjede

<chapterId>50dff39b-2702-47d7-9c15-0b54b845e99f</chapterId>

![Video](https://youtu.be/u-3rV7DGtD0?si=G1__H0Uelf4sTUDM)

Så langt har vi sett på hvordan du kan kjøre Elements som en sidekjede. Den kan imidlertid også fungere som en frittstående blokkjedeløsning med sin egen standardaktiva. I dette oppsettet beholder en Elements-blockchain fortsatt alle funksjonene til en sidekjedeimplementering, for eksempel konfidensielle transaksjoner og utstedte aktiva, men trenger ikke peg-in eller peg-out for å legge til eller fjerne standard aktiva fra sirkulasjon.

I denne delen vil vi:

Initialiser en ny Elements-blockchain med en standard eiendel som heter `newasset`.

Angi at det skal opprettes 1 000 000 `newasset` sammen med 2 reissuance tokens for det.

Gjør krav på alle myntene som alle kan bruke.

Gjør krav på alle gjenutstedelsespoletter som alle kan bruke for "newasset".

Send eiendelen og gjenutstedelsestokenet til en annen nodes lommebok.

Send ut flere 'newasset' fra begge nodene.

For å initialisere et Elements-nettverk slik at det kan fungere som en frittstående blokkjede, må hver node startes med noen grunnleggende parametere. De brukes til å fortelle noden at den ikke skal prøve å validere peg-ins fra en annen blokkjede, navnet på nettverkets standardaktiva og mengden av standardaktiva og tilhørende reutstedelsestoken som skal opprettes.

Vi starter nå en ny kjede med disse parameterne på de to tilkoblede Elements-nodene våre. Vi navngir standardaktivaen `newasset` og utsteder én million av dem og to `newasset` reissueance-tokens.

```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
e2-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```

Merk at beløpene som brukes her, er i den minste pålydende verdien nettverket kan akseptere, slik at de to hundre millionene reissuance tokens faktisk tilsvarer to hele tokens. Det samme gjelder for pålydende på de første gratis myntene.

Sjekk nodens nåværende saldo i lommeboken.

```
e1-cli getwalletinfo
e2-cli getwalletinfo
```

Vi kan se at initialiseringen fungerte som den skulle.

Etter hvert som den første utstedelsen av eiendeler opprettes som "alle kan bruke", får vi e1 til å gjøre krav på dem alle, slik at vi kan fjerne e2s tilgang til dem.

```
e1-cli getnewaddress
e1-cli sendtoaddress <e1-address> 1000000 "" "" true
```

Merk at vi ikke trenger å spesifisere "newasset" som eiendelen som skal sendes, ettersom den allerede er standard eiendel og dermed også standard eiendel som brukes til å betale nettverksavgifter.

I Elements kan du sende flere typer aktiva til samme adresse, så vi kan gjenbruke adressen vi nettopp genererte for å motta standardaktivaen, og bruke den som destinasjonsadresse for gjenutstedelsestokens.

```
e1-cli sendtoaddress <e1-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Bekreft transaksjonene.

```
e1-cli generate 101
```

Vi sjekker at e1 er den eneste innehaveren av eiendelen og dens gjenutstedelsestoken nå.

```
e1-cli getwalletinfo
e2-cli getwalletinfo
```

Noe vi kan se er tilfelle.

Nå sender vi noe av "newasset" til e2, som for øyeblikket har en saldo på null.

```
e2-cli getnewaddress
e1-cli sendtoaddress <e2-address> 500 "" "" false
```

Merk at vi ikke trengte å spesifisere hvilken type ressurs som skal sendes, ettersom `newasset` er opprettet som nettverkets standardressurs

La oss også sende noen av reissuance-tokens for `newasset` til e2.

```
e1-cli sendtoaddress <e2-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Bekreft transaksjonene.

```
e1-cli generate 101
```

Vi kan sjekke at lommebøkene er oppdatert i henhold til dette.

```
e1-cli getwalletinfo
e2-cli getwalletinfo
```

Nå skal vi utstede noen av standardaktivaene fra e1 på nytt. Merk at muligheten til å gjøre dette aktiveres av oppstartsparameteren initialreissuancetokens. Hvis den utelates eller settes til null, vil det resultere i et standardaktivum som ikke kan utstedes på nytt på et senere tidspunkt.

```
e1-cli reissueasset newasset 100
```

Vi kunne bruke etiketten `newasset` i stedet for å måtte oppgi hex-id-verdien fordi en Elements-kjede alltid merker standardaktivet sitt.

Kontrollerer at gjenutstedelsen av standardaktivaen fungerte:

```
e1-cli generate 101
e1-cli getwalletinfo
```

Vi vil nå bevise at fordi e2 har noen av `newasset`-reutstedelsestokens, kan den også utstede standardaktivaen på nytt.

```
e2-cli reissueasset newasset 100
```

Kontrollerer at gjenutstedelsen av standardaktiva fra e2 fungerte.

```
e2-cli generate 101
e2-cli getwalletinfo
```

I denne delen har vi satt opp Elements som en frittstående blokkjede og sjekket at grunnleggende funksjonalitet fungerer som forventet.

Vi brukte oppstartsparametere for å:

Initialiser en ny Elements-blockchain med en standard eiendel som heter "newasset".

Angi mengden av standardaktiva som skal opprettes ved initialisering av kjeden.

Opprett noen gjenutstedelsestokens for standardaktiva og gjenutsted flere av standardaktiva fra begge nodene.

I vårt frittstående blockchain Elements-nettverk vil alle andre transaksjoner fungere på samme måte som eksemplene som dekkes i hoveddelene av kurset, men vil bruke "newasset" i stedet for "bitcoin" som standard- og avgiftsaktivum.

### Parametere for oppstart av noder og initialisering av kjeder

For å fortelle en Elements-node at den skal fungere som en frittstående blokkjede, må noen få parametere brukes sammen. Vi tar en titt på hver av dem nå og finner ut hva de gjør.

#### `validatepegin=0`

Ettersom en frittstående blokkjede ikke trenger å validere noen peg-in- eller peg-out-transaksjoner, må vi deaktivere disse kontrollene. Med denne innstillingen trenger du ikke å kjøre Bitcoin-klientprogramvaren eller lagre en kopi av Bitcoin-blokkjeden, ettersom Elements-nettverket vil fungere uavhengig.

#### `defaultpeggedassetname`

Her kan du angi navnet på standardaktivaen som opprettes ved initialisering av blokkjeden.

#### `initialfreecoins`

Antallet (tilsvarende Bitcoins Satoshi-enhet) av standardaktivaen som skal opprettes.

#### `initialreissuancetokens`

Antallet (tilsvarende Bitcoins Satoshi-enhet) av gjenutstedelsestokens for standardaktivaen som skal opprettes. Uten dette vil det være umulig å opprette flere av standardaktivaen. Hvis du ikke ønsker at det skal være mulig å opprette flere av standardaktivaen, kan dette settes til null eller utelates.

Ved hjelp av disse parameterne vil den vanlige måten å starte en node på se omtrent slik ut:

```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```

### Grunnleggende operasjoner

Parameteren `defaultpeggedassetname` gir standardaktivaen en etikett. Uten denne innstillingen vil standardaktivaen automatisk få navnet `bitcoin`. I tidligere avsnitt måtte vi, når vi sendte aktiva som vi selv utstedte, til en annen node, spesifisere enten aktivahexen eller den lokalt påførte aktivamerkelappen for å fortelle Elements hvilket aktivum vi sendte. Ettersom `defaultpeggedassetname` gjelder på tvers av alle noder, trenger vi ikke å navngi den når vi sender den, selv om navnet ikke er `bitcoin`. Alle funksjoner som tidligere ville ha sendt `bitcoin` som standard, vil nå sende det du valgte å kalle standardaktivaen.

Så det er så enkelt som å sende 10 av den nye standardaktivaen til en adresse:

```
e1-cli sendtoaddress <destination address> 10 "" "" true
```

Hvis du også har gitt noden en verdi for `initialreissuancetokens` som er større enn null, vil du også kunne utstede flere av standardaktivaen på nytt, noe som ikke er mulig hvis du kjører Elements som en sidekjede.

For å gjøre dette trenger alle noder som har et beløp av tokenet som er knyttet til standardaktivaen, bare å utstede en kommando i skjemaet:

```
e1-cli reissueasset <default asset name> <amount>
```

Ved å bruke parameterne ovenfor kan du drive Elements som en frittstående blokkjede med sin egen standardaktiva, frikoblet fra Bitcoin og andre blokkjeder.

## Konklusjon

<chapterId>7e2c916d-8114-424c-97f5-cbff9d73b8e3</chapterId>

![Video](https://youtu.be/CTMdamTZBBM?si=16LBcXvN4pBfC7lr)

I dette kurset har vi lært at Elements er en nettverksprotokoll med åpen kildekode som kan implementeres som en sidekjede til en annen blokkjede, eller som en frittstående blokkjedeløsning.

Vi har sett at kildekoden og nettstedet for Elements (https://github.com/ElementsProject/elements) ligger på GitHub, og at det finnes diskusjonsfora, for eksempel Build On L2 (https://community.liquid.net/c/developers/) eller Liquid Developers Telegram (https://t.me/liquid_devel), som kan brukes til å lære mer om distribusjon og utvikling av applikasjoner på Elements og Liquid. Viktige funksjoner som Confidential Transactions og Issued Assets ble gjennomgått, sammen med hvordan medlemmer av en Strong Federation muliggjør føderert blokksignering og 2-veis Peg-mekanismen.

Neste skritt er å utfordre deg selv med en kumulativ quiz som dekker alle de foregående delene, og deretter kan du begynne din Elements-reise ... lykke til!

# Konklusjon

<partId>d5dbd616-e291-42bc-aae3-6c44599dbd06</partId>

## Anmeldelser og rangeringer

<chapterId>beae23bd-2fd1-49fe-8f38-ed169acde51d</chapterId>

<isCourseReview>true</isCourseReview>

## Konklusjon

<chapterId>15f62056-c69c-467e-9565-af48d439a1f5</chapterId>

Gratulerer med fullført kurs!

Vi er glade for at du har nådd denne milepælen i din læringsreise. Gjennom ditt engasjement har du tilegnet deg verdifull kunnskap og ferdigheter som du vil ha god nytte av i din videre profesjonelle utvikling.