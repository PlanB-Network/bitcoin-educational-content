---
name: Bitcoin og BTCPay Server
goal: Installer BTCPay Server for din bedrift
objectives:
  - Forstå hva btcpayserver er.
  - Selv-hoste og konfigurere BTCPay Server.
  - Bruke btcpayserver i din daglige virksomhet.
---

# Bitcoin og BTCPay Server

Dette er et introduksjonskurs om BTCPay Server Operator skrevet av Alekos og Bas, som ble tilpasset Plan ₿ kursformatet av melontwist og asi0.

EN UFULLSTENDIG HISTORIE

"Dette Er Løgner, Min Tillit Til Deg Er Ødelagt, Jeg Vil Gjøre Deg Foreldet".

Produsert av BTCPay Server Foundation

+++

# Introduksjon

<partId>59e43fe3-b494-5da6-b4b4-9df5bdf08916</partId>

## Kritisk anerkjennelse for Forfatterens Bitcoin og BTCPay Server

<chapterId>e1fe6294-3c82-5203-9537-779f9087c35a</chapterId>

La oss starte med hva BTCPay Server er og hvor den kommer fra. Vi verdsetter åpenhet og visse standarder for å danne tillit i Bitcoin-rommet.
Et prosjekt i rommet brøt disse verdiene. BTCPay Servers hovedutvikler, Nicolas Dorier, tok dette personlig og lovet å gjøre dem foreldet. Her er vi mange år senere og jobber mot denne fremtiden, fullstendig åpen kildekode, hver dag.

> Dette er løgner, min tillit til deg er ødelagt, jeg vil gjøre deg foreldet.
> Nicolas Dorier

Etter ordene uttalt av Nicolas, var det på tide å begynne å bygge. Mye arbeid gikk inn i det vi nå kaller BTCPay Server. Flere mennesker ønsket å hjelpe til med dette dyttet. De mest gjenkjennelige er r0ckstardev, MrKukks, Pavlenex, og den første handelsmannen som brukte programvaren, astupidmoose.

Hva betyr åpen kildekode, og hva går inn i et slikt prosjekt?

FOSS står for Free & Open-Source Software. Det første refererer til vilkår som tillater hvem som helst å kopiere, modifisere, og til og med distribuere versjoner (selv for profitt) av programvaren. Det siste refererer til åpent å dele kildekoden, oppmuntre offentligheten til å bidra og forbedre den.
Dette bringer inn erfarne brukere entusiastiske om å bidra til programvaren de allerede bruker og henter verdi fra, noe som over tid viser seg å vinne i adopsjon over proprietær programvare. Det er i tråd med Bitcoin-ethoset at "informasjon lengter etter å være fri." Det bringer sammen lidenskapelige mennesker som danner et fellesskap og er rett og slett mer moro. Som Bitcoin, er FOSS uunngåelig.

### Før vi begynner

Dette kurset består av flere deler. Mange vil bli tatt hånd om av din klasseromslærer, demo-miljøer som du får tilgang til, en hostet server for deg selv, og muligens et domenenavn. Hvis du fullfører dette kurset uavhengig, vær oppmerksom på at miljøene merket som DEMO ikke vil være tilgjengelige for deg.
NB. Hvis du følger dette kurset via klasserom, kan servernavn variere avhengig av din klasseromsoppsett. Variabler i servernavn kan være forskjellige på grunn av dette.

### Kursstruktur

Hvert kapittel har mål og kunnskapsvurderinger. I dette kurset vil vi dekke hver av disse og ha en oppsummering av nøkkelfunksjoner ved hver leksjonsblokk (dvs. kapittel). Illustrasjoner er fremhevet for å gi visuell tilbakemelding og forsterke nøkkelkonsepter i en visuell aspekt. Mål er satt i starten av hver leksjonsblokk. Disse målene går utover en sjekkliste. Disse gir deg en veiledning inn i et nytt ferdighetssett. Kunnskapsvurderinger blir gradvis mer utfordrende oppsett av din BTCPay Server.

### Hva mottar studentene med kurset?
Med BTCPay Server-kurset kan en student forstå de grunnleggende prinsippene, både teknisk og ikke-teknisk, om Bitcoin. Den omfattende opplæringen i bruk av Bitcoin gjennom BTCPay Server vil tillate studenter å operere sin egen Bitcoin-infrastruktur.
### Viktige nettadresser eller kontaktmuligheter

BTCPay Server Foundation, som tillot Alekos og Bas å skrive dette kurset, er i Tokyo, Japan. BTCPay Server-stiftelsen kan nås gjennom nettstedet som er oppført;

- https://foundation.btcpayserver.org
- bli med i de offisielle chat-kanalene: https://chat.btcpayserver.org

## Introduksjon til Bitcoin

<chapterId>5c0bc234-c188-5b4a-94d5-adee87a120e2</chapterId>

### Forstå Bitcoin gjennom klasseromsøvelse

Dette er en klasseromsøvelse, så hvis du tar dette kurset selv, kan du ikke utføre det, men du kan fortsatt gå gjennom denne øvelsen. For å fullføre denne oppgaven er det minimum antall personer mellom 9 og 11.

Øvelsen starter etter å ha sett introduksjonen "Hvordan Bitcoin og blokkjeden fungerer" av BBC.

![hvordan bitcoin og blokkjeden fungerer](https://youtu.be/mhE_vvwAiRc)

Denne øvelsen krever minst ni personer for å delta. Hensikten med øvelsen er å fysisk få en ide om hvordan Bitcoin fungerer. Ved å spille hver rolle i nettverket, vil du ha en interaktiv og leken måte å lære på. Denne øvelsen involverer ikke Lightning Network.

### Eksempel; Krever 9 / 11 personer

Rollene er:

- 1 Kunde
- 1 Forhandler
- 7 til 9 Bitcoin-noder

**Oppsett er som følger:**

Kunden kjøper et produkt fra butikken med Bitcoin.

**Scenario 1 - Tradisjonelt banksystem**

- Oppsett:
  - Se diagrammer/forklaring i vedlagte Figjam - [Aktivitetsskjematisk](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
  - Få tre studentfrivillige til å spille rollene som Kunde (Alice), Forhandler (Bob), og Bank.
- Spill ut hendelsesforløpet:
  - Kunde- blar gjennom butikken på nett og finner en vare til $25 som de ønsker, og informerer Forhandleren om at de ønsker å kjøpe
  - Forhandler- ber om betaling.
  - Kunde- sender kortinformasjon til Forhandler
  - Forhandler- videresender informasjonen til Banken (identifiserer både sin egen og identiteten/informasjonen) og ber om betaling av
  - Bank samler informasjon om Kunde og Forhandler (Alice og Bob) og sjekker at kundens saldo er tilstrekkelig.
  - Trekker $25 fra Alices konto, legger $24 til Bobs konto, tar $1 for tjenesten
  - Forhandleren mottar tommel opp fra Banken og sender varen til kunden.
- Kommentarer:
  - Bob og Alice må ha et forhold til en bank.
  - Banken samler identifiserende informasjon om både Bob og Alice.
  - Banken tar en andel.
  - Banken må stoles på å ha forvaring av hver deltakers penger hele tiden.

**Scenario 2 - Bitcoin-systemet**

- Oppsett:
  - Se diagrammer/forklaring i vedlagte Figjam - [Aktivitetsskjematisk](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
- Erstatt Bank med ni studenter som vil spille rollen som en Datamaskin (Bitcoin-noder/Minere) i et nettverk for å erstatte Banken.
- Hver av de 9 Datamaskinene har en komplett historisk oversikt over alle tidligere transaksjoner som noen gang er gjort (dermed nøyaktige saldoer uten forfalskninger), samt et sett med regler:
  - Verifiser at transaksjonen er riktig signert (nøkkelenpasserlåsen)
  - Kringkast og motta gyldige transaksjoner til jevnaldrende i nettverket, forkast ugyldige (inkludert alle som forsøker å bruke de samme midlene to ganger)
- Oppdater/Legg til poster periodisk med nye transaksjoner mottatt fra "tilfeldig" datamaskin forutsatt at alt innhold er gyldig (merk: vi ignorerer, for nå, Proof of Work-komponenten til alt dette, for enkelhets skyld), ellers avvis disse og fortsett som før til neste "tilfeldige" datamaskin sender en oppdatering
  - Den riktige mengden ble belønnet hvis innholdet var gyldig.
- Spill ut hendelsesforløpet:
  - Kunde- blar gjennom butikken på nettet og finner en vare til $25 som de ønsker, og informerer Selgeren om at de ønsker å kjøpe
  - Selger- ber om betaling ved å sende kunden en faktura/adresse fra sin lommebok.
  - Kunde- konstruerer en transaksjon (sender $25 verdt av BTC til en adresse oppgitt av Selger) og kringkaster den til Bitcoin-nettverket.
- Datamaskiner- mottar transaksjonen og verifiserer:
  - Det er minst $25 av BTC i adressen som sendes fra
  - Transaksjonen er riktig signert (“låst opp” av kunden)
  - Hvis ikke tilfellet, vil transaksjonen ikke bli spredt gjennom nettverket, og hvis så, da spres den og holdes i venting.
  - Selgere kan sjekke at transaksjonen er under behandling og venter.
- En datamaskin blir “tilfeldig” valgt til å foreslå å fullføre den foreslåtte transaksjonen ved å kringkaste “en blokk” som inneholder den; hvis den sjekker ut, vil de motta en BTC-belønning.
  - VALGFRITT/AVANSERT - i stedet for å tilfeldig velge en Datamaskin, simuler gruvedrift ved å ha Datamaskiner rulle terninger til et forhåndsbestemt utfall inntreffer (f.eks. den første som ruller dobbelt seksere blir valgt)
  - Det kan også spilles ut hva som ville skje hvis to Datamaskiner vinner omtrent samtidig, noe som resulterer i en kjedesplittelse.
  - Datamaskiner sjekker gyldigheten, oppdaterer/legger til poster i sine hovedbøker hvis regler er oppfylt, og kringkaster blokk til jevnaldrende.
  - Den tilfeldig valgte datamaskinen mottar en belønning for å foreslå en gyldig blokk.
  - Selger sjekker at transaksjonen ble avsluttet; dermed ble midler mottatt, og varen ble sendt til kunden.
- Kommentarer:
  - Legg merke til at det ikke var behov for et eksisterende bankforhold.
  - Ingen tredjepart nødvendig for å fasilitere; erstattet av kode/insentiver.
  - Ingen datainnsamling av noen utenfor den direkte utvekslingen og bare den nødvendige mengden må utveksles mellom deltakerne (f.eks. leveringsadresse).
  - Ingen tillit er nødvendig mellom menneskene (annet enn at Selgeren sender varen), på mange måter som et kontantkjøp.
  - Pengene eies direkte av individene.
  - Bitcoin-hovedboken er avbildet i dollar for enkelhets skyld, men i virkeligheten er det BTC.
  - Vi simulerer en enkelt transaksjon som blir kringkastet, men i virkeligheten er flere transaksjoner under behandling i nettverket, og blokker inkluderer tusenvis av transaksjoner på en gang. Noder sjekker også at det ikke er noen dobbeltutgiftstransaksjoner under behandling (jeg ville kastet ut alle unntatt en hvis det var tilfellet).
- Jukse-scenarier:
  - Hva om kunden ikke hadde $25 BTC?
    - De ville ikke kunne opprette transaksjonen fordi “låsing” og “eierskap” er det samme, og datamaskiner sjekker at transaksjonen er riktig signert; ellers avviser de den.
- Hva om den tilfeldig valgte datamaskinen forsøker å "endre i hovedboken"?    - Blokken ville blitt avvist, ettersom hver andre datamaskin har en komplett historikk og ville lagt merke til endringen, noe som bryter med en av deres regler.
    - Tilfeldig Datamaskin ville ikke fått en belønning, og ingen transaksjoner fra deres blokk ville blitt endelig godkjent.

## Kunnskapsvurdering

<chapterId>1461f064-933d-50ea-8935-324b68ec5d5f</chapterId>

### KA Klasseromsdiskusjon

Diskuter noen forenklinger gjort i klasseromsøvelsen under det andre scenarioet og beskriv hva det faktiske Bitcoin-systemet gjør mer detaljert.

### KA Vokabular gjennomgang

Definer følgende nøkkelbegreper introdusert i den forrige seksjonen:

- Node
- Mempool
- Difficulty Target
- Block

**Diskuter betydningen av noen ytterligere begreper som en gruppe:**

Blockchain, Transaksjon, Dobbel-Utgifter, Byzantinske Generalers Problem, Mining, Proof of Work (PoW), Hash-funksjon, Blokkbelønning, Blockchain, Lengste Kjede, 51% Angrep, Output, Output Lock, Endring, Satoshis, Offentlig/Privat Nøkkel, Adresse, Offentlig-nøkkel Kryptografi, Digital Signatur, Lommebok

# Introduksjon til BTCPay Server

<partId>9c8a2d0c-9ba1-5c39-874c-f9eaf1bba663</partId>

## Forstå BTCPay Server innloggingsskjerm

<chapterId>14aad54c-9bd8-54f2-9455-178b8ae63408</chapterId>

### Arbeide med BTCPay Server

Målet med denne kursblokken vil være å ha en generell forståelse av BTCPay Server-programvaren. I et delt miljø, er det anbefalt å følge instruktørens demonstrasjon og følge med i BTCPay Server Kursboken for å følge læreren. Du vil lære å opprette en lommebok gjennom flere metoder. Eksempler inkluderer oppsett av Hot wallet og maskinvarelommebøker koblet gjennom BTCPay Server Vault. Disse målene forekommer i Demo-miljøet, vist og gitt tilgang til av kursinstruktøren din.

Hvis du følger dette kurset på egen hånd, kan du finne en liste over tredjepartsverter for Demo-formål på https://directory.btcpayserver.org/filter/hosts. Vi anbefaler sterkt mot å bruke disse tredjepartsalternativene som produksjonsmiljøer, men de tjener de riktige formålene for en introduksjon til å bruke Bitcoin og BTCPay Server.

Som en BTCPay Server rockstar-trainee, kan du ha tidligere erfaring med å sette opp en Bitcoin-node. Dette kurset vil snakke spesifikt skreddersydd til BTCPay Server Software-stacken.

Mange av alternativene i BTCPay Server finnes i en eller annen form i annen Bitcoin Wallet-relatert programvare.

### BTCPay Server Innloggingsskjerm

Når du ønskes velkommen til Demo-miljøet, blir du bedt om å ‘Logg inn’ eller ‘Opprett din konto.’ Serveradministratorer kan slå av funksjonen for å opprette nye kontoer av sikkerhetsgrunner. BTCPay Server-logoer og knappefarger kan endres fordi BTCPay Server er Open Source-programvare. En tredjepartsvert kan White-label programvaren og endre hele utseendet.

![bilde](assets/en/0.webp)

### Opprett en Konto-vindu

Å opprette kontoer på BTCPay Server krever gyldige e-postadressestrenger; example@email.com ville være en gyldig streng for e-post.

Passordet må være minst 8 tegn langt, inkludert bokstaver, tall og tegn. Etter å ha satt passordet en gang, må du verifisere det inntastede passordet for å sikre at det er korrekt til det som ble skrevet i det første passordfeltet.
Når både E-post og Passord feltene er riktig utfylt, klikk på "Opprett konto"-knappen. Dette vil lagre e-posten og passordet på instruktørens BTCPay Server-instans.
![bilde](assets/en/1.webp)

**!Merk!**

Hvis du følger dette kurset på egen hånd, ville oppretting av denne kontoen være noe du kanskje gjør på en tredjeparts vert; derfor nevner vi igjen aldri å bruke disse som produksjonsmiljøer, men kun til treningsformål.

### Kontoopprettelse av BTCPay Server Administrator

Administratoren av BTCPay Server-instansen kan også opprette kontoer for BTCPay Server. Administratoren av BTCPay Server-instansen kan klikke på "Serverinnstillinger" (1), klikke på "Brukere"-fanen (2), og klikke på "+ Legg til bruker"-knappen (3) øverst til høyre på Brukere-fanen. I Mål (4.3) vil du lære mer om administratorkontroll av kontoer.

![bilde](assets/en/2.webp)

Som administrator trenger du brukerens e-postadresse og sette et standard passord. Det anbefales som administrator å informere brukeren om at de bør endre dette passordet før de bruker kontoen av sikkerhetsgrunner. Hvis administratoren IKKE setter et passord og SMTP har blitt satt opp på serveren, vil brukeren motta en e-post med en invitasjonslenke for å opprette kontoen sin og sette passordet selv.

### Eksempel

Når du følger kurset med en instruktør, følg lenken gitt av instruktøren og opprett kontoen din på demomiljøet som tilbys. Sørg for at e-postadressen og passordet ditt er lagret sikkert; du vil trenge disse påloggingsopplysningene for resten av demo-målene i dette kurset.

Din instruktør kan ha samlet e-postadressen på forhånd og sendt en invitasjonslenke før denne øvelsen. Hvis instruert, sjekk din e-post.

Når du tar kurset uten en instruktør, opprett kontoen din ved å bruke BTCPay Server demomiljøet; gå til

https://mainnet.demo.btcpayserver.org/login.

Denne kontoen bør kun brukes til demonstrasjon/opplæringsformål og aldri for forretninger.

### Ferdighetssammendrag

I denne delen lærte du følgende:

- Hvordan opprette en konto på en vertsserver gjennom grensesnittet.
- Hvordan en serveradministrator manuelt kan legge til brukere i serverinnstillingene.

### Kunnskapsvurdering

#### KA Konseptuell Gjennomgang

Gi grunner til hvorfor det er en dårlig idé å bruke en Demo Server til produksjonsformål.

## Administrasjon av brukerkonto(er)

<chapterId>b58ca6ee-b7fc-5e81-a6aa-c8ff212b4c55</chapterId>

### Kontoadministrasjon på BTCPay Server

Etter at en butikkeier har opprettet kontoen sin, kan de administrere den nederst til venstre i BTCPay Server UI. Under Konto-knappen finnes det flere innstillinger på høyere nivå.

- Mørk/Lys modus.
- Skjul sensitiv info-knapp.
- Administrer konto.

![bilde](assets/en/3.webp)

### Mørk og Lys modus

Brukere av BTCPay Server kan velge mellom en Lys eller Mørk versjon av UI. Kundevendte sider vil ikke endres. De bruker kunde-prefererte innstillinger angående mørk eller lys modus.

### Skjul sensitiv info-knapp

Knappen for å skjule sensitiv info gir et raskt og enkelt sikkerhetslag. Når du trenger å operere din BTCPay Server, men det kan være folk som lurer over skulderen din i et offentlig rom, slå på Skjul sensitiv info, og alle verdiene i BTCPay Server vil bli skjult. Noen kan være i stand til å se over skulderen din, men kan ikke lenger se verdiene du håndterer.

### Administrer konto

Når brukerkontoen har blitt opprettet, er dette stedet for å administrere passord, 2fa, eller API-nøkler.
### Administrer konto - Konto

Du kan eventuelt oppdatere kontoen din med en annen e-postadresse. For å sikre at e-postadressen din er korrekt, tillater BTCPay Server deg å sende en verifiseringse-post. Klikk lagre hvis brukeren setter en ny e-postadresse og bekrefter at verifiseringen fungerte. Brukernavnet forblir det samme som den forrige e-posten.

En bruker kan bestemme seg for å slette hele kontoen sin. Dette kan gjøres ved å klikke på sletteknappen på konto-fanen.

![bilde](assets/en/4.webp)

**!Merk!**

Etter å ha endret e-posten, vil ikke brukernavnet for kontoen endre seg. Den tidligere oppgitte e-postadressen vil forbli innloggingsnavnet.

### Administrer konto - Passord

En student kan ønske å endre passordet sitt. Han kan gjøre dette ved å gå til Passord-fanen. Her må han skrive inn sitt gamle passord og kan endre det til et nytt.

![bilde](assets/en/5.webp)

### To-Faktor Autentisering (2fa)

For å begrense konsekvensene av et stjålet passord, kan du bruke to-faktor autentisering (2fa), en relativt ny sikkerhetsmetode. Du kan aktivere to-faktor autentisering via Administrer konto og fanen for to-faktor autentisering. Du må fullføre et andre trinn etter å ha logget inn med brukernavnet og passordet ditt.

BTCPay Server tillater to måter å aktivere 2FA på, App-basert 2FA (Authy, Google, Microsoft autentikatorer) eller gjennom Sikkerhetsenheter (FIDO2 eller LNURL Auth).

### To-Faktor Autentisering - App basert

Basert på mobiltelefonens operativsystem (Android eller iOS), kan brukere velge mellom følgende apper;

1. Last ned en to-faktor autentikator;
   - Authy for [Android](https://play.google.com/store/apps/details?id=com.authy.authy) eller [iOS](https://apps.apple.com/us/app/authy/id494168017)
   - Microsoft Authenticator for [Android](https://play.google.com/store/apps/details?id=com.azure.authenticator) eller [iOS](https://apps.apple.com/us/app/microsoft-authenticator/id983156458)
   - Google Authenticator for [Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=e%C2%80) eller [iOS](https://apps.apple.com/us/app/google-authenticator/id388497605)
2. Etter nedlasting og installasjon av Autentikator-Appen.
   - Skann QR-koden som tilbys av BTCPay Server
   - Eller skriv inn nøkkelen generert av BTCPay Server manuelt i din Autentikator-app.
3. Autentikator-appen vil gi deg en unik kode. Skriv inn den unike koden i BTCPay Server for å verifisere oppsettet, og klikk bekreft for å fullføre prosessen.

![bilde](assets/en/6.webp)

### Ferdighetssammendrag

I denne delen lærte du følgende:

- Kontoadministrasjonsalternativer og de ulike måtene å administrere en konto på en BTCPay Server-instans.
- Hvordan sette opp app-basert 2FA.

### Kunnskapsvurdering

#### KA Konseptuell Gjennomgang

Beskriv hvordan app-basert 2FA bidrar til å sikre kontoen din

## Opprette en ny butikk

<chapterId>463b3634-b49f-5512-a711-3b2e096fc2e0</chapterId>

### Opprett din butikk-veiviser
Når en ny bruker logger seg inn på BTCPay Server, er miljøet tomt og trenger en første butikk. Introduksjonsveiviseren til BTCPay Server vil gi brukeren muligheten til å ‘Opprett din butikk’ (1). En butikk kan ses på som et hjem for dine Bitcoin-behov. En ny BTCPay Server Node vil starte med å synkronisere Bitcoin Blockchain (2). Avhengig av hvilken infrastruktur du kjører BTCPay Server på, kan dette variere fra noen timer til noen dager. Instansens nåværende versjon vises i nedre høyre hjørne av BTCPay Server UI. Dette er nyttig for referanse når man feilsøker.
![bilde](assets/en/7.webp)

### Veiviser for å opprette din butikk

Å følge dette kurset vil starte med en litt annerledes skjerm enn den forrige siden. Ettersom instruktøren din har forberedt demomiljøet, har Bitcoin blockchain blitt synkronisert på forhånd, og derfor vil du ikke se nodenes synkroniseringsstatus.

En bruker kan bestemme seg for å slette hele kontoen sin. Dette kan gjøres ved å klikke på sletteknappen på konto-fanen.

![bilde](assets/en/8.webp)

**!Merk!**

BTCPay Server-kontoer kan lage ubegrensede mengder butikker. Hver butikk er en lommebok eller et “hjem”.

### Eksempel

Start med å klikke på "Opprett din butikk".

![bilde](assets/en/9.webp)

Dette vil opprette ditt første hjem og dashbord for å bruke BTCPay server.

(1) Etter å ha klikket på "Opprett din butikk", vil BTCPay Server kreve at du navngir butikken; dette kan være hva som helst som er nyttig for deg.

![bilde](assets/en/10.webp)

(2) En standard butikkvaluta må settes neste, enten en fiatvaluta eller denominert i en Bitcoin / Sats-standard. For demomiljøet vil vi sette den til USD.

![bilde](assets/en/11.webp)

(3) Som en siste parameter på butikkoppsettet, krever BTCPay Server at du setter en "Foretrukket pris kilde" for å sammenligne Bitcoins pris mot den nåværende fiatprisen slik at butikken din viser den korrekte vekslingskursen mellom Bitcoin og butikkens fiatvaluta. Vi vil holde oss til standarden i demoen og sette dette til Kraken-børsen. BTCPay Server bruker Kraken API for å sjekke vekslingskursene.

![bilde](assets/en/12.webp)

(4) Nå som disse butikkparametrene er satt, klikk på Opprett-knappen, og BTCPay Server vil opprette dashbordet for din første butikk, hvor veiviseren vil fortsette.

![bilde](assets/en/13.webp)

Gratulerer, du har opprettet din første butikk, og dette avrunder denne øvelsen.

![bilde](assets/en/14.webp)

### Ferdighetssammendrag

I denne delen lærte du:

- Opprettelse av butikk og konfigurering av en standardvaluta kombinert med preferanser for pris kilde.
- Hver "Butikk" er et nytt hjem adskilt fra andre butikker på denne installasjonen av BTCPay Server.

# Introduksjon til Sikring av Bitcoin-nøkler

<partId>25da22d8-fd37-51c5-af2a-58b9f3b046b2</partId>

## Forståelse av Generering av Bitcoin-nøkler

<chapterId>d162735b-847b-578e-83b8-a044ab703ec5</chapterId>

### Hva er involvert i generering av bitcoin-nøkler?

Bitcoin-lommebøker, når de opprettes, lager en såkalt "seed". I det siste målet opprettet du en "seed", Serien med ord generert før er også kjent som mnemoniske fraser. Seedet brukes til å utlede individuelle Bitcoin-nøkler fra og brukes til å sende eller motta Bitcoin. Seed-fraser bør aldri deles med tredjeparter eller upålitelige jevnaldrende.
Frøgenereringen utføres langs industristandarden kjent som det "Hierarkiske Deterministiske" (HD) rammeverket.
![bilde](assets/en/15.webp)

### Adresser

BTCPay Server er bygget for å generere en ny Adresse. Dette avhjelper problemet med gjenbruk av offentlig nøkkel eller Adresse. Å bruke samme offentlige nøkkel gjør det veldig enkelt å spore hele din betalingshistorikk. Å tenke på nøkler som engangsbruksgavekort ville betydelig forbedre ditt personvern. Vi bruker også Bitcoin-adresser, ikke forveksle disse med offentlige nøkler.

En Adresse blir avledet fra den offentlige nøkkelen gjennom en "hashing algoritme". De fleste lommebøker og transaksjoner vil imidlertid vise Adresser heller enn disse offentlige nøklene. Adresser er generelt kortere enn offentlige nøkler og begynner vanligvis med en `1`, `3`, eller `bc1`, mens offentlige nøkler begynner med `02`, `03`, eller `04`.

- Adresser som starter med `1.....` er fortsatt veldig vanlige adresser. Som nevnt i kapittelet om å opprette en ny butikk, er disse arvede adresser. Denne adressetypen er ment for P2PKH-transaksjoner. P2Pkh bruker Base58-koding, som gjør adressen store og små bokstaver sensitiv. Dens struktur er basert på den offentlige nøkkelen med en ekstra siffer som identifikator.

- Adresser som starter med `bc1...` er sakte i ferd med å bli veldig vanlige adresser. Disse er kjent som (native) SegWit-adresser. Disse tilbyr en bedre gebyrstruktur enn de andre nevnte adressene. Native SegWit-adresser bruker Bech32-koding og tillater kun små bokstaver.

- Adresser som starter med `3...` brukes ofte fortsatt av børser for innskuddsadresser. Disse adressene er nevnt i kapittelet om å opprette en ny butikk, innpakket eller nestede SegWit-adresser. De kan imidlertid også fungere som en "Multisig-adresse". Når de brukes som en SegWit-adresse, er det igjen noen besparelser på transaksjonsgebyrer, men mindre enn Native SegWit. P2SH-adresser bruker Base58-koding. Dette gjør den store og små bokstaver sensitiv, som den arvede adressen.

- Adresser som starter med `2...` er Testnett-adresser. De er ment for å motta testnett-bitcoin (tBTC). Du bør aldri blande dette og sende Bitcoin til disse adressene. For utviklingsformål kan du generere en testnett-lommebok. Det finnes flere kraner på nettet for å få testnett Bitcoin. Kjøp aldri Testnett Bitcoin. Testnett Bitcoin blir utvunnet. Dette kan være en grunn for en utvikler til å bruke Regtest i stedet. Dette er et lekegrindmiljø for utviklere, som mangler visse nettverkskomponenter. Bitcoin er imidlertid, for utviklingsformål, veldig nyttig.

### Offentlige Nøkler

Offentlige nøkler blir mindre brukt i praksis i dag. Over tid har bitcoin-brukere erstattet dem med Adresser i stedet. De eksisterer fortsatt og blir fortsatt brukt av og til. Offentlige nøkler er generelt mye lengre strenger enn adresser. Akkurat som med adresser, starter de med en spesifikk identifikator.

- Først, `02...` og `03...` er veldig standard offentlige nøkkelidentifikatorer kodet i SEC-format. Disse kan behandles og omdannes til adresser for mottak, brukes til å opprette multi-sig-adresser, eller for å verifisere en signatur. Tidlige Bitcoin-transaksjoner brukte offentlige nøkler som en del av P2PK-transaksjoner.

- HD-lommebøker bruker imidlertid en annen struktur. `xpub...`, `ypub...` eller `zpub...` kalles utvidede offentlige nøkler eller xpubs. Disse nøklene brukes til å avlede mange offentlige nøkler ettersom det er en del av HD-lommeboken. Siden din xpub holder oversikten over hele din historie, som betyr tidligere og fremtidige transaksjoner, del aldri disse med upålitelige parter.

### Ferdighetssammendrag

I denne seksjonen lærte du følgende:
- Forskjellene mellom adresser og offentlige nøkkel datatyper og fordelene med å bruke adresser over offentlige nøkler.
### Kunnskapsvurdering

Beskriv fordelen med å bruke ferske adresser for hver transaksjon sammenlignet med gjenbruk av adresser eller metoder med offentlige nøkler

## Sikring av nøkler med maskinvarelommebok

<chapterId>c54a6d61-5a43-5fdb-93ae-c6750de9c612</chapterId>

### Lagring av Bitcoin-nøkler

Etter å ha generert en seed phrase, listen over 12 - 24 ord generert i denne boken krever riktig sikkerhetskopiering og sikkerhet, ettersom disse ordene er den eneste måten å gjenopprette tilgang til en lommebok på. Strukturen til HD-lommebøker og hvordan den genererer adresser deterministisk ved hjelp av den ene seeden, alle dine opprettede adresser vil bli sikkerhetskopiert ved hjelp av denne ene listen med mnemoniske ord som representerer din seed eller gjenopprettingsfrase.

Hold din gjenopprettingsfrase sikret. Hvis den blir tilgjengelig for noen, spesielt med ondsinnet hensikt, kan de flytte midlene dine. Å holde seeden trygg og sikret, men også å huske den, er gjensidig for hverandre. Det finnes flere metoder for å lagre Bitcoin private nøkler, hver med fordeler og ulemper, enten det gjelder sikkerhet, personvern, bekvemmelighet eller fysiske midler. På grunn av viktigheten av private nøkler, har Bitcoin-brukere en tendens til å lagre og trygt oppbevare disse nøklene i "selvforvaring" fremfor å bruke "forvaringstjenester" som banker. Avhengig av brukeren, må han bruke enten en kaldlagringsløsning eller en varm lommebok.

### Varm og kald lagring av bitcoin-nøkler

Vanligvis er bitcoin-lommebøker betegnet som en Varm Lommebok eller Kald Lommebok. De fleste kompromissene ligger i bekvemmelighet, brukervennlighet og sikkerhetsrisikoer. Hver av disse metodene kan også sees i en forvaringsløsning. Imidlertid er kompromissene her mest basert på sikkerhet og personvern og går utover dette kursets omfang.

### Varm lommebok

Varme lommebøker er den mest praktiske måten å samhandle med Bitcoin gjennom mobil, web eller skrivebordsprogramvare. Lommeboken er alltid koblet til internett, noe som gjør det mulig for brukere å sende eller motta Bitcoin. Dette er imidlertid også dens svakhet, lommeboken, siden den alltid er online, er nå mer sårbar for angrep fra hackere eller skadelig programvare på enheten din. I BTCPay Server lagres de private nøklene på instansen. Enhver som får tilgang til din BTCPay Server-butikk, kunne stjele midler fra denne adressen hvis ondsinnet. Når BTCPay Server kjører i et hostet miljø, bør du alltid vurdere dette i din sikkerhetsprofil og helst ikke bruke en Varm-lommebok i et slikt tilfelle. Når BTCPay Server er installert på egen maskinvare, sikret og betrodd av deg, senkes risikoprofilen betydelig, men den forsvinner aldri!

### Kald lommebok

Individer flytter sine Bitcoin til en kald lommebok fordi den kan isolere de private nøklene fra internett. Å fjerne internettforbindelsen fra ligningen reduserer risikoen for skadelig programvare, spionprogramvare og SIM-bytter. Kald lagring anses å være overlegen varm lagring når det gjelder sikkerhet og autonomi, så lenge tilstrekkelige forholdsregler tas for å unngå å miste de private Bitcoin-nøklene. Kald lagring er mest egnet for store mengder Bitcoin, som ikke er ment å bli brukt ofte på grunn av kompleksiteten i lommebokoppsettet.

Det finnes ulike metoder for hvordan man kan lagre Bitcoin-nøkler i kald lagring, fra papirlommebøker til hjernelommebøker, maskinvarelommebøker, eller, fra begynnelsen, en lommebokfil. De fleste lommebøker bruker BIP 39 for å generere seed phrase. Imidlertid har det ennå ikke blitt oppnådd enighet om å bruke den innenfor Bitcoin core-programvaren. Bitcoin Core-programvaren vil fortsatt generere en Wallet.dat-fil som du trenger å lagre på et sikkert offline-sted.

### Ferdighetssammendrag

I denne seksjonen lærte du:

- Forskjellene mellom varme og kalde lommebøker når det gjelder funksjonalitet og deres kompromisser.

### Kunnskapsvurdering Konseptuell Gjennomgang
- Hva er en lommebok?
- Hva er forskjellen mellom varme og kalde lommebøker?

- Beskriv hva som menes med "å generere en lommebok"?

## Bruke dine Bitcoin-nøkler

<chapterId>bff488de-5052-56e6-b696-97e896f762ae</chapterId>

### BTCPay Server-lommebok

BTCPay Server består av følgende standard lommebokfunksjoner:

- Transaksjoner
- Send
- Motta
- Reskan
- Trekkbetalinger
- Utbetalinger
- PSBT
- Generelle innstillinger

### Transaksjoner

Administratorer kan se inn- og utgående transaksjoner for lommeboken på kjeden som er koblet til denne spesifikke butikken i transaksjonsvisningen. Hver transaksjon har en distinksjon mellom mottatt og sendt. Mottatt vil være grønn og utgående transaksjoner vil være røde. Innenfor BTCPay Server-transaksjonsvisningen vil administratorer også se et sett med standard etiketter.

| Transaksjonstype | Beskrivelse                                          |
| ---------------- | ---------------------------------------------------- |
| App              | Betaling ble mottatt gjennom en appopprettet faktura |
| invoice          | Betaling ble mottatt gjennom en faktura              |
| payjoin          | Ikke betalt, fakturatimeren har fortsatt ikke utløpt |
| payjoin-exposed  | UTXO ble eksponert gjennom et faktura payjoin-forslag|
| payment-request  | Betaling ble mottatt gjennom en betalingsforespørsel |
| payout           | Betaling ble sendt gjennom en utbetaling eller refusjon |

### Hvordan sende

BTCPay servers sendefunksjon sender transaksjoner fra din BTCPay Server-lommebok på kjeden. BTCPay Server tillater flere måter å signere transaksjonene dine for å bruke midler. En transaksjon kan signeres med;

- Maskinvarelommebok
- Lommebøker som støtter PSBT
- HD privat nøkkel eller gjenopprettingsfrø.
- Varm lommebok

#### Maskinvarelommebok

BTCPay Server har innebygd støtte for maskinvarelommebøker som lar deg bruke maskinvarelommeboken din med BTCPay Vault uten å lekke informasjon til tredjepartsapper eller servere. Integreringen av maskinvarelommebok innenfor BTCPay Server lar deg importere maskinvarelommeboken din og bruke de innkommende midlene med en enkel bekreftelse på enheten din. Dine private nøkler forlater aldri enheten, og alle midler blir validert mot din fullnode, så det er ingen datalekkasje.

#### Signering med en lommebok som støtter PSBT

PSBT (Partially Signed Bitcoin Transactions) er et utvekslingsformat for Bitcoin-transaksjoner som fortsatt trenger å bli fullstendig signert. PSBT støttes i BTCPay Server og kan signeres med kompatible maskinvare- og programvarelommebøker.

Konstruksjonen av en fullstendig signert Bitcoin-transaksjon går gjennom følgende trinn:

- En PSBT konstrueres med spesifikke innganger og utganger, men ingen signaturer
- Den eksporterte PSBT kan importeres av en lommebok som støtter dette formatet
- Transaksjonsdataene kan inspiseres og signeres ved hjelp av lommeboken
- Den signerte PSBT-filen blir eksportert fra lommeboken og importert med BTCPay Server
- BTCPay Server produserer den endelige Bitcoin-transaksjonen
- Du verifiserer resultatet og kringkaster det til nettverket

#### Signering med HD privat nøkkel eller mnemonic frø

Hvis du har opprettet en lommebok før ved å bruke BTCPay Server, kan du bruke midlene ved å legge inn din private nøkkel i et passende felt. Sett en passende "AccountKeyPath" i lommebok> Innstillinger; ellers kan du ikke bruke.

#### Signering med en varm lommebok

Hvis du opprettet en ny lommebok når du satte opp butikken din og aktiverte den som en varm lommebok, vil den automatisk bruke frøet lagret på en server for å signere.

### RBF (Replace-By-Fee)
Replace-By-Fee (RBF) er en Bitcoin-protokollfunksjon som lar deg erstatte en tidligere sendt transaksjon (mens den fortsatt er ubekreftet). Dette gjør det mulig å randomisere transaksjonsavtrykket til lommeboken din eller erstatte det med en høyere gebyrsats for å flytte transaksjonen høyere opp i køen for bekreftelsesprioritet (mining). Dette vil effektivt erstatte den opprinnelige transaksjonen ettersom den høyere gebyrsatsen vil bli prioritert, og når den er bekreftet, vil den ugyldiggjøre den opprinnelige (ingen dobbeltutgift).
Trykk på "Avanserte Innstillinger"-knappen for å se RBF-alternativene;

![bilde](assets/en/16.webp)

- Randomiser for høyere personvern, lar transaksjonen bli erstattet automatisk for randomisering av transaksjonsavtrykk.
- Ja, Merk transaksjon for RBF og bli eksplisitt erstattet (Ikke erstattet som standard, kun ved inndata)
- Nei, Ikke tillat at transaksjonen blir erstattet.

### Myntvalg

Myntvalg er en avansert personvernforbedrende funksjon som lar deg velge mynter du ønsker å bruke når du utformer en transaksjon. For eksempel, betale med mynter som er ferske fra en conjoin-blanding.

Myntvalg fungerer naturlig med lommebokens etikettfunksjon. Dette lar deg merke innkommende midler for jevnere UTXO-håndtering og utgifter.

BTCpay Server støtter også BIP-329 for etiketthåndtering. BIP-329 tillater etiketter på; hvis du overfører fra en lommebok som støtter denne spesifikke BIP-en og setter etiketter, vil BTCPay Server gjenkjenne disse og importere dem. Når du migrerer servere, kan denne informasjonen også eksporteres og importeres til det nye miljøet.

### Hvordan Motta

Når du klikker på motta-knappen i BTCPay Server, genererer den en ubrukt adresse som kan brukes til å motta betalinger. Administratorer kan også generere en ny adresse ved å generere en ny "Faktura".

BTCPay Server vil alltid be om å generere den neste tilgjengelige adressen for å unngå adressegjenbruk. Etter å ha klikket på "Generer neste tilgjengelige BTC-adresse", genererte BTCPay Server en ny adresse og QR. Det lar deg også direkte sette en Etikett til adressen for bedre håndtering av adressene dine.

![bilde](assets/en/17.webp)

![bilde](assets/en/18.webp)

#### Re-skann

Re-skann-funksjonen er avhengig av Bitcoin Core 0.17.0s "Scantxoutset" for å skanne den nåværende tilstanden til blockchain (kalt UTXO Set) for mynter som tilhører det konfigurerte avledningsskjemaet. Lommebok re-skann løser to problemer BTCPay Server-brukere opplever.

1. Gap limit-problemet - De fleste tredjepartslommebøker er lette lommebøker som deler en node mellom mange brukere. Lettvekts- og fullnodestøttede lommebøker begrenser antallet (typisk 20) adresser uten saldo de sporer på blockchain for å forhindre ytelsesproblemer. BTCPay Server genererer en ny adresse for hver faktura. Med dette i tankene, etter at BTCPay Server har generert 20 påfølgende ubetalte fakturaer, stopper den eksterne lommeboken med å hente transaksjonene, og antar at ingen nye transaksjoner har skjedd. Din eksterne lommebok vil ikke vise dem når fakturaene betales på den 21., 22., osv. På den andre siden sporer BTCPay Server-lommeboken enhver adresse den genererer sammen med en mye større gapgrense. Den er ikke avhengig av en tredjepart og kan alltid vise en korrekt saldo.
2. Løsningen med gap-grense - Hvis din [eksterne/eksisterende lommebok](https://docs.btcpayserver.org/WalletSetup/#use-an-existing-wallet) tillater konfigurasjon av gap-grense, er den enkle løsningen å øke den. Imidlertid tillater flertallet av lommebøker ikke dette. De eneste lommebøkene som tillater konfigurasjon av gap-grense som vi kjenner til, er Electrum, Wasabi og Sparrow Wallet. Dessverre vil du sannsynligvis støte på et problem med mange andre lommebøker. For den beste brukeropplevelsen og personvernet, vurder å droppe eksterne lommebøker og bruke BTCPay Servers interne lommebok.
#### BTCPay Server bruker “mempoolfullrbf=1”

BTCPay Server bruker “mempoolfullrbf=1”; vi har lagt dette til som standard i din BTCPay Server-oppsett. Vi har imidlertid også gjort det til et fragment du kan deaktivere selv. Uten “mempoolfullrbf=1”, hvis en kunde dobbeltbruker en betaling med en transaksjon som ikke signaliserer RBF, ville selgeren bare vite etter bekreftelse.

En administrator kan ønske å velge bort denne innstillingen. Med følgende streng kan du endre standardinnstillingen.

```
BTCPAYGEN_EXCLUDE_FRAGMENTS="$BTCPAYGEN_EXCLUDE_FRAGMENTS;opt-mempoolfullrbf"
. btcpay-setup.sh -i**
```

### Innstillinger for BTCPay Server-lommebok

Innstillinger for lommebok innen BTCPay Server gir en klar og rask oversikt over de generelle innstillingene for lommeboken din. Alle disse innstillingene er forhåndsutfylt hvis lommeboken ble opprettet med BTCPay Server.

![bilde](assets/en/19.webp)

Innstillinger for lommebok innen BTCPay Server gir en klar og rask oversikt over de generelle innstillingene for lommeboken din. Alle disse innstillingene er forhåndsutfylt hvis lommeboken ble opprettet med BTCPay Server. BTCPay Servers lommebokinnstillinger starter med lommebokens status. Er det en Watch-only eller Hot wallet? Avhengig av lommeboktypen, kan handlingene variere fra å reskanne lommeboken for manglende transaksjoner, beskjære gamle transaksjoner fra historikken, registrere lommeboken for betalingslenker, eller erstatte og slette den nåværende lommeboken knyttet til butikken. I BTCPay Servers lommebokinnstilling kan administratorer sette en Etikett for lommeboken for bedre lommebokforvaltning. Her vil administratoren også kunne se Avledningsskjemaet, kontonøkkel (xpub), Fingerprint og Keypath. Betalinger i lommebokinnstillinger har bare 2 hovedinnstillinger. Betalingen er ugyldig hvis transaksjonen mislykkes i å bekrefte innen (angitte minutter) etter fakturaens utløp. Vurder fakturaen som bekreftet når betalingstransaksjonen har X antall bekreftelser. Administratorer kan også sette en veksle for å vise anbefalte gebyrer ved betalinger eller sette et manuelt bekreftelsesmål i antall blokker.

![bilde](assets/en/20.webp)

**!Merk!**

Hvis du følger dette kurset på egen hånd, ville oppretting av denne kontoen være noe du kanskje gjør på en tredjepartsvert, derfor nevner vi igjen aldri å bruke disse som produksjonsmiljøer, men heller bare til treningsformål.

### Eksempel

#### Sette opp en Bitcoin-lommebok i BTCPay Server

BTCPay Server tillater to måter å sette opp lommebok på. En måte er å importere en allerede eksisterende Bitcoin-lommebok. Importen kan gjøres ved å koble til en maskinvarelommebok, importere en lommebokfil, angi en Utvidet offentlig nøkkel, skanne en lommeboks QR-kode, eller det minst foretrukne, angi et tidligere opprettet gjenopprettingsfrø for lommeboken for hånd. I BTCPay Server er det også mulig å opprette en ny lommebok. Det er to mulige måter å konfigurere BTCPay Server på når du genererer en ny lommebok.
Valget av en "hot wallet" i BTCPay Server muliggjør funksjoner som 'Payjoin' eller 'Liquid'. Det er imidlertid en ulempe, gjenopprettingsfrøet som genereres for denne lommeboken, vil bli lagret på serveren, hvor hvem som helst med Admin-kontroll kan hente gjenopprettingsfrøet. Siden din private nøkkel er avledet fra gjenopprettingsfrøet ditt, kan en ondsinnet aktør få tilgang til dine nåværende og fremtidige midler!
For å redusere en slik risiko i BTCPay Server, kan en Admin sette i Serverinnstillinger > Retningslinjer > "Tillat ikke-adminer å opprette hot wallets for butikkene sine" til nei, som det er som standard. For å forbedre sikkerheten til disse Hot wallets, bør serveradministratoren aktivere 2FA-autentisering på kontoer som får ha Hot wallets. Å lagre private nøkler på en offentlig server er farlig og kommer med risikoer. Noen er liknende til risikoer med Lightning Network (se neste kapittel for risikoer med Lightning Network).

Den andre muligheten BTCPay Server tilbyr for å generere en ny lommebok er ved å opprette en "Watch-Only wallet". BTCPay Server vil generere dine private nøkler én gang. Etter at brukeren bekrefter å ha skrevet ned deres Seed Phrase, vil BTCPay Server slette de private nøklene fra serveren. Som et resultat har butikken din nå en Watch-only wallet tilknyttet. For å bruke midlene mottatt på din watch-only Wallet, se kapittel Hvordan sende, enten ved å bruke BTCPay Server Vault, PSBT (partially signed bitcoin transaction), eller, minst anbefalt, manuelt oppgi din seed phrase.

Du opprettet en ny 'Butikk' i den siste delen. Installasjonsveiviseren vil fortsette med å spørre om å "Sette opp en lommebok" eller "Sette opp en Lightning node". I dette eksemplet vil du følge prosessen med "Sette opp en lommebok" (1).

![bilde](assets/en/21.webp)

Etter å ha klikket på "Sette opp en lommebok", vil veiviseren fortsette med å be om hvordan du ønsker å fortsette; BTCPay Server tilbyr nå muligheten til å koble en eksisterende Bitcoin-lommebok til din nye butikk. Hvis du ikke har en lommebok, foreslår BTCPay Server å opprette en ny. Dette eksemplet vil følge trinnene for "opprette en ny lommebok" (2). Følg trinnene for å lære hvordan du "Kobler en eksisterende lommebok (1).

![bilde](assets/en/22.webp)

**!Merk!**

Hvis du tar dette kurset i et klasserom, er det nåværende eksemplet og frøet vi genererte kun til utdanningsformål. Det bør aldri være noen betydelig mengde annet enn nødvendig gjennom øvelsene på disse adressene.

(1) Fortsett "Ny lommebok"-veiviseren ved å klikke på "Opprett en ny lommebok"-knappen.

![bilde](assets/en/23.webp)

(2) Etter å ha klikket på “Opprett en ny lommebok”, vil det neste vinduet i veiviseren gi alternativene “Hot wallet” og “Watch-only wallet”. Hvis du følger med en instruktør, er miljøet ditt en delt Demo, og du kan bare opprette en Watch-only wallet. Legg merke til forskjellen mellom begge figurene nedenfor. Siden du er i Demo-miljøet og følger med instruktøren, opprett en "Watch-only wallet" og fortsett med "Ny Lommebok"-veiviseren.

![bilde](assets/en/24.webp)

![bilde](assets/en/25.webp)

(3) Når du fortsetter den nye lommebokveiviseren, er du nå i seksjonen for å opprette BTC watch-only wallet. Her får vi muligheten til å sette lommebokens "Adresse type" BTCPay Server lar deg velge din foretrukne adressetype; per skrivetidspunktet for dette kurset, anbefales det fortsatt å bruke bech32-adresser. Lær mer i detalj om adresser i det første kapittelet av denne delen.

- Segwit (bech32)
- Native SegWit-adresser er adresser som starter med `bc1q`.  
  - Eksempel: `bc1qXXXXXXXXXXXXXXXXXXXXXX`
- Legacy
  - Legacy-adresser er adresser som starter med tallet `1`.
  - Eksempel: `15e15hXXXXXXXXXXXXXXXXXXXX`
- Taproot (For avanserte brukere)
  - Taproot-adresser starter med `bc1p`.
  - Eksempel: `bc1pXXXXXXXXXXXXXXXXXXXXXXXX`
- Segwit wrapped
  - Segwit wrapped-adresser er adresser som starter med `3`.
  - Eksempel: `37BBXXXXXXXXXXXXXXX`

Velg segwit (anbefalt) som din foretrukne lommebokadresse.

![bilde](assets/en/26.webp)

(4) Når du setter parameteren for lommeboken, tillater BTCPay Server brukerne å sette en valgfri passfrase gjennom BIP39, sørg for å bekrefte passordet ditt.

![bilde](assets/en/27.webp)

(5) Etter å ha satt lommebokens adressetype og muligens satt noen avanserte alternativer, klikk på Opprett, og BTCPay Server vil generere din nye lommebok. Merk at dette er det siste steget før du genererer din Seed phrase. Sørg for at du kun gjør dette i et miljø hvor noen ikke kan stjele seed phrase ved å se på skjermen din.

![bilde](assets/en/28.webp)

(6) I den følgende skjermen av veiviseren, viser BTCPay Server deg Recovery seed phrase for din nygenererte lommebok; disse er nøklene til å gjenopprette lommeboken din og signere transaksjoner. BTCPay Server genererer en seed phrase på 12 ord. Disse ordene vil bli slettet fra serveren etter denne oppsettsskjermen. Denne lommeboken er spesifikt en Watch-only lommebok. Det anbefales ikke å lagre denne seed phrase digitalt eller ved fotografisk bilde. Brukere kan kun gå videre i veiviseren hvis de aktivt erkjenner at de har skrevet ned sin seed phrase.

![bilde](assets/en/29.webp)

(7) Etter å ha klikket Ferdig og sikret den nygenererte Bitcoin seed phrase, vil BTCPay Server oppdatere butikken din med den nye tilknyttede lommeboken og er klar til å motta betalinger. I brukergrensesnittet, i venstre navigasjonsmeny, legg merke til hvordan Bitcoin nå er uthevet og aktivert under Wallet.

![bilde](assets/en/30.webp)

### Eksempel: Skrive ned en seed phrase

Dette er et veldig spesielt og sikkert øyeblikk for å bruke Bitcoin. Som nevnt tidligere, bør bare du ha tilgang til eller kunnskap om din seed phrase. Når du følger med en instruktør og klasse, bør seeden som genereres kun brukes i dette kurset. For mange faktorer, nysgjerrige øyne fra klassekamerater, usikre systemer og mange andre gjør disse nøklene kun til utdanningsformål og ikke til å stole på. Likevel bør nøklene som genereres fortsatt lagres for eksempler i kurset.

Den første metoden vi vil bruke i den nåværende situasjonen, også den minst sikre, er å skrive ned seed phrase i riktig rekkefølge. Et Seed phrase-kort er i kursmaterialet som er gitt til studenten eller funnet på BTCPay Server GitHub. Vi vil bruke dette kortet til å skrive ned ordene som ble generert i det forrige steget. Sørg for å skrive dem ned i riktig rekkefølge. Etter at du har skrevet dem ned, sjekk dem mot det som ble gitt av programvaren for å sikre at du skrev dem ned i riktig rekkefølge. Når du har skrevet det ned, klikk på avkrysningsboksen som sier at du har skrevet ned din seed phrase på riktig måte.

### Eksempel: Lagring av en seed phrase på en Hardware Wallet

I dette kurset berører vi lagring av en seed phrase på en hardware wallet. Å følge dette kurset med en instruktør kan noen ganger ikke inkludere en slik enhet. I kursmaterialet er det skrevet en liste over hardware wallets som ville passe til denne øvelsen.
Vi vil bruke BTCPay Server vault og en Blockstream Jade hardware wallet i dette eksemplet.
Du kan også følge med på video for referanse om hvordan du kobler til en hardware wallet.
![BTCPay Server - Hvordan koble hardware wallet med BTCPay Vault.](https://youtu.be/s4qbGxef43A)

Last ned BTCPay Server Vault: https://github.com/btcpayserver/BTCPayServer.Vault/releases

Sørg for at du laster ned de riktige filene for ditt system. Windows-brukere bør laste ned [BTCPayServerVault-2.0.5-setup.exe](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-2.0.5-setup.exe)-pakken, Mac-brukere laster ned [BTCPayServerVault-osx-x64-2.0.5.dmg](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-osx-x64-2.0.5.dmg), og Linux-brukere bør laste ned [BTCPayServerVault-Linux-2.0.5.tar.gz](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-Linux-2.0.5.tar.gz)

Etter å ha installert BTCPay Server Vault, start programvaren ved å klikke på ikonet på skrivebordet ditt. Når BTCPay Server Vault er riktig installert og startet for første gang, vil den be om tillatelse til å bli brukt med webapplikasjoner. Den vil be om å gi tilgang til den spesifikke BTCPay Server du jobber med. Aksepter disse betingelsene. BTCPay Server Vault vil nå søke etter maskinvareenheten. Når enheten er funnet, vil BTCPay Server gjenkjenne at Vault kjører og har hentet enheten din.

**!Merk!**

Ikke gi SSH-nøklene dine eller serveradministratorkontoen din til noen andre enn administratorer når du bruker en hot wallet. Alle som har tilgang til disse kontoene vil ha tilgang til midlene i Hot Wallet.

### Ferdighetssammendrag

I denne seksjonen lærte du følgende:

- Transaksjonsvisningen av Bitcoin-lommeboken og dens ulike kategoriseringer.
- Ulike alternativer som er tilgjengelige når du sender fra en Bitcoin-lommebok, fra hardware til hot wallets.
- Gap limit-problemet som oppstår når man bruker de fleste lommebøker, og hvordan korrigere dette.
- Hvordan generere en ny Bitcoin-lommebok innenfor BTCPay Server, inkludert lagring av nøklene i en hardware wallet og sikkerhetskopiering av gjenopprettingsfrasen.

I dette målet har du lært hvordan du genererer en ny Bitcoin-lommebok innenfor BTCPay Server. Vi har ennå ikke gått inn på hvordan du sikrer eller bruker disse nøklene. I en rask oversikt over dette målet har du lært hvordan du setter opp den første butikken. Du har lært hvordan du genererer en Bitcoin Recovery Seed frase.

### Kunnskapsvurdering Praktisk Gjennomgang

Beskriv en metode for å generere nøkler og et skjema for å sikre dem, sammen med avveiningene/risikoene ved sikkerhetsskjemaet.

## BTCPay Server Lightning Wallet

<chapterId>1bbece7e-0197-57e6-a93a-561cf384d946</chapterId>

Når en serveradministrator setter opp en ny BTCPay Server-instans, kan han sette opp en lightning network-implementering, LND, Core Lightning, eller Eclair; se Del Konfigurering av BTCPay Server for mer detaljerte installasjonsinstruksjoner.
Hvis fulgt av et klasserom, fungerer tilkoblingen av en Lightning-node til din BTCPay Server gjennom en egendefinert node. En bruker som ikke er serveradministrator på BTCPay Server, vil ikke kunne bruke den interne Lightning-noden som standard. Dette er for å beskytte servereieren mot å miste sine midler. Serveradministratorer kan installere en Plugin for å gi tilgang til deres Lightning-node gjennom LNBank; dette er utenfor omfanget av denne boken; les mer om LNBank på den offisielle plugin-siden.
### Koble til intern node (serveradministrator)

Serveradministratoren kan bruke BTCPay Servers interne Lightning Node. Uavhengig av Lightning-implementasjonen, er tilkoblingen til den interne Lightning-noden den samme.

Gå til en tidligere oppsatt butikk, og klikk på "Lightning"-lommeboken i venstremenyen. BTCPay Server gir to oppsettsmuligheter, Bruke den interne noden (kun Serveradmin som standard) eller en egendefinert node (ekstern tilkobling). Serveradministratorer kan klikke på "Bruk intern node"-alternativet. Det kreves ingen ytterligere konfigurasjon. Klikk på "lagre"-knappen og legg merke til varselet som sier, "BTC Lightning-node oppdatert". Butikken har nå lykkes med å få Lightning-nettverkskapasiteter.

### Koble til ekstern node (butikkeier/serverbruker)

Som butikkeiere er det som standard ikke tillatt å bruke serveradministratorens Lightning Node. Tilkoblingen må gjøres til en ekstern node, enten en node eid av butikkeieren før en BTCPay Server-oppsett, en LNBank-plugin hvis gjort tilgjengelig av serveradministratoren, eller en forvalterløsning som Alby.

Gå til en tidligere oppsatt butikk, og klikk på "Lightning" under lommebøker i venstremenyen. Ettersom butikkeiere som standard ikke har lov til å bruke den interne noden, er dette alternativet nedtonet. Å bruke en egendefinert node er det eneste alternativet som standard er tilgjengelig for butikkeiere.

BTCPay Server trenger tilkoblingsinformasjon; den tidligere lagde (eller forvalterløsningen) vil levere denne informasjonen spesifikk for en Lightning-implementasjon. Innen BTCPay Server kan butikkeiere bruke følgende tilkoblinger;

- C-lightning via TCP eller Unix domain socket connection.
- Lightning Charge via HTTPS
- Eclair via HTTPS
- LND via REST proxy
- LNDhub via REST API

![bilde](assets/en/31.webp)

Klikk på "test tilkobling" for å sikre at du har angitt tilkoblingsdetaljene riktig. Etter at tilkoblingen bekreftes å være god, klikk lagre, og BTCPay Server viser at butikken er oppdatert med en Lightning Node.

### Administrere intern Lightning-node LND (Serveradministrator)

Etter tilkobling av den interne Lightning-noden, vil serveradministratorer legge merke til nye fliser på Dashbordet spesifikt for Lightning-informasjon.

- Lightning-saldo
- BTC i kanaler
  - BTC åpner kanaler
  - BTC lokal saldo
  - BTC fjernsaldo
  - BTC lukker kanaler
- BTC On-chain
  - BTC bekreftet
  - BTC ubekreftet
  - BTC reservert
- Lightning-tjenester
  - Ride the Lightning (RTL).

Ved å klikke enten på Ride the Lightning-logoen i "Lightning-tjenester"-flisen eller "Lightning" under lommebøker i venstremenyen, kan serveradministratorer nå RTL for administrasjon av Lightning-noden.

**Merk!**

Tilkobling av den interne Lightning-noden mislykkes - Hvis den interne tilkoblingen mislykkes, bekreft:

1. At Bitcoin on-chain-noden er fullstendig synkronisert
2. At den interne lightning-noden er "Aktivert" under "Lightning" > "Innstillinger" > "BTC Lightning-innstillinger"
Hvis du ikke klarer å koble til din Lightning-node, prøv å starte serveren på nytt, eller les mer detaljer i BTCPay Servers offisielle dokumentasjon; https://docs.btcpayserver.org/Troubleshooting/ . Du kan ikke akseptere lightning-betalinger i butikken din før Lightning-noden din vises som "Online". Prøv å teste Lightning-tilkoblingen din ved å klikke på lenken "Public Node Info"
### Lightning-lommebok

Innenfor Lightning-lommebokalternativet i venstre menylinje, vil serveradministratorer finne enkel tilgang til RTL, deres Public node Info, og Lightning-innstillinger spesifikke for deres BTCPay Server-butikk.

#### Intern nodeinfo

Serveradministratorer kan klikke på intern nodeinfo og få et øyeblikksbilde av serverstatusen deres (Online/ Offline) og tilkoblingsstreng for Clearnet eller Tor.

![bilde](assets/en/32.webp)

#### Endre tilkobling

Hvis butikkeieren bestemmer seg for å bruke endringer innen Lightning-innstillinger - Endre tilkobling.
Ved siden av Public Node info-butikken, kan eiere finne dette alternativet. Det vil gjenopprette den opprinnelige oppsettet for den eksterne lightning-nodetilkoblingen, fylle ut den nye Lightning-nodeninformasjonen, klikke lagre, og oppdatere butikken med den nye nodeninformasjonen.

![bilde](assets/en/33.webp)

#### Tjenester

Hvis serveradministratoren bestemmer seg for å installere flere tjenester for Lightning-implementeringen, vil de bli listet her. Med en standard LND-implementering, vil administratorer ha Ride The Lightning (RTL) som et standardverktøy for nodestyring.

#### BTC Lightning-lommebokinnstillinger

Etter å ha lagt til Lightning-noden til butikken i et tidligere steg, innenfor innstillingene til Lightning-lommeboken, kan butikkeiere fortsatt velge å deaktivere den for sin butikk ved å bruke vekselen på toppen av Lightning-innstillinger.

![bilde](assets/en/34.webp)

#### Lightning-betalingsalternativer

Butikkeiere kan sette parametere for følgende for å forbedre Lightning-opplevelsen for kundene sine.

- Vis Lightning-betalingsbeløp i Satoshis.
- Legg til hop-hints for private kanaler til Lightning-fakturaen.
- Foren URL/QR-koder for on-chain og Lightning-betalinger ved utsjekking.
- Sett en beskrivelsesmal for lightning-fakturaer.

#### LNURL

Butikkeiere kan velge å enten bruke eller ikke bruke LNURL. En Lightning Network URL, eller LNURL, er en foreslått standard for interaksjoner mellom Lightning-betaler og mottaker. Kort sagt, en LNURL er en bech32-kodet url prefikset med lnurl. Lightning-lommeboken forventes å dekode URL-en, kontakte URL-en, og vente på et JSON-objekt med videre instruksjoner, mest merkbart en tag som definerer oppførselen til knurlen.

- Aktiver LNURL
- LNURL Classic Mode
  - For lommebokkompatibilitet, Bech32-kodet (klassisk) vs klartekst URL (kommende)
- Tillat mottakeren å sende en kommentar.

### Eksempel 1

#### Koble til Lightning med intern node (Administrator)

Dette alternativet er kun tilgjengelig hvis du er Administrator for denne instansen eller hvis Administratoren har endret standardinnstillingene der brukere kan bruke den interne lightning-noden.

Som administrator, klikk på Lightning Wallet i venstre menylinje. BTCPay Server vil be om å bruke en av to alternativer for å koble en Lightning Node, en intern node, eller en tilpasset ekstern node. Klikk på Bruk intern node og klikk på lagre.

#### Administrere din Lightning-node (RTL)

Etter å ha koblet til den interne lightning-noden, vil BTCPay Server oppdatere og vise en notifikasjon "BTC Lightning node oppdatert", som bekrefter at du nå har koblet Lightning til butikken din.

Å administrere lightning-noden er en oppgave for serverens Administrator. Dette innebærer.

- Håndtere transaksjoner
- Administrere likviditet
  - Innkommende likviditet
  - Utgående likviditet
- Administrere jevnaldrende og kanaler
  - Tilkoblede jevnaldrende
  - Kanalavgifter
  - Kanalstatus
- Å ta hyppige sikkerhetskopier av kanaltilstandene.
- Sjekke ruterapporter
- Alternativt, bruk tjenester som Loop.

All lynknuteadministrasjon gjøres som standard med RTL (forutsatt at du kjører på en LND-implementering). Administratorer kan klikke på sin Lightning Wallet i BTCPay Server og finne en knapp for å åpne RTL. Hoveddashboardet til BTCPay Server er nå oppdatert med Lightning Network-fliser, inkludert rask tilgang til RTL.

### Eksempel 2

#### Koble til lynet med Alby

Når du kobler til med en forvalter som Alby, bør butikkeiere først opprette en konto, besøk: https://getalby.com/

![bilde](assets/en/35.webp)

Etter å ha opprettet Alby-kontoen, gå til din BTCPay Server-butikk.

Steg 1: Klikk på 'Sett opp en Lightning-nod' på Dashboardet eller 'Lightning' under lommebøker.

![bilde](assets/en/36.webp)

Steg 2: Sett inn dine Wallet-tilkoblingsopplysninger som tilbys av Alby. På Dashboardet til Alby, klikk på Wallet. Her vil du finne "Wallet Connection Credentials". Kopier disse opplysningene. Lim inn opplysningene fra Alby i tilkoblingskonfigurasjonsfeltet i BTCPay Server.

![bilde](assets/en/37.webp)

Steg 3: Etter å ha gitt BTCPay Server tilkoblingsdetaljene, klikk på "Test Connection"-knappen for å sikre at tilkoblingen fungerer ordentlig. Legg merke til meldingen "Connection to lightning node successful" øverst på skjermen din. Dette bekrefter at alt fungerer som det skal.

![bilde](assets/en/38.webp)

Steg 4: Klikk lagre, og butikken din er nå koblet til en lynnod av Alby.

![bilde](assets/en/39.webp)

**!Merk!**

Stol aldri på en forvaltet Lightning-løsning med mer verdi enn du er villig til å tape.

### Ferdighetssammendrag

I denne delen lærte du:

- Hvordan koble til en intern eller ekstern Lightning-nod
- Innholdet og funksjonen til ulike Lightning-relaterte fliser på Dashboardet
- Hvordan konfigurere Lightning-lommebok ved hjelp av Voltage Surge eller Alby

### Kunnskapsvurdering Praktisk Gjennomgang

Beskriv noen av de ulike alternativene for å koble en Lightning-lommebok til butikken din.

# BTCPay Server-grensesnitt

<partId>25e88b81-e1ab-515f-a035-09f2a3075556</partId>

## Oversikt over Dashboard

<chapterId>410ff28b-a272-5c91-93e0-48d5b28c53ab</chapterId>

BTCPay Server er en modulær programvarepakke. Det er imidlertid standarder som hver BTCPay Server vil ha, og administratoren/brukerne vil samhandle med. Starter med Dashboardet. Hovedinngangspunktet til hver BTCPay Server etter innlogging. Dashboardet gir en oversikt over hvordan butikken din presterer, lommebokens nåværende saldo, og de siste transaksjonene de siste 7 dagene. Siden det er en modulær visning, kan Plugins utnytte denne visningen til sin fordel og skape sine fliser på Dashboardet. For denne læreboken vil vi bare snakke om standard plugins/apps og deres respektive visninger gjennom BTCPay Server.

### Dashboard-fliser

Innenfor hovedvisningen av BTCPay Server-dashboardet er det et par standardfliser tilgjengelig. Disse flisene er ment for butikkeieren eller administratoren for å raskt kunne administrere butikken sin i en oversikt.

- Lommeboksaldo
- Transaksjonsaktivitet
- Lightning-saldo (hvis Lightning er aktivert på butikken)
- Lightning-tjenester (hvis Lightning er aktivert på butikken)
- Nylige transaksjoner.
- Nylige fakturaer
- Pågående aktive folkefinansieringer
- Butikkens ytelse / mest solgte varer.
Flisen for Lommeboksaldo gir en rask oversikt over midlene og ytelsen til lommeboken din. Den kan vises i enten BTC eller Fiat-valuta i et ukentlig, månedlig eller årlig diagram.
![bilde](assets/en/40.webp)

### Transaksjonsaktivitet

Ved siden av flisen for Lommeboksaldo viser BTCPay Server en rask oversikt over ventende utbetalinger, antall Transaksjoner de siste 7 dagene, og om butikken din har utstedt noen refusjoner. Ved å klikke på Administrer-knappen blir du tatt med til administrasjonen for ventende utbetalinger (lær mer om utbetalinger i BTCPay Server - Betalingskapittel).

![bilde](assets/en/41.webp)

### Lightning-saldo

Dette er kun synlig når Lightning er aktivert.

Når Administratoren har tillatt tilgang til Lightning-nettverket, har BTCPay Server-dashboardet nå en ny flis med informasjon om din Lightning-node. Hvor mye BTC som er i kanaler, hvordan dette er balansert lokalt eller eksternt (innkommende eller utgående likviditet) om kanaler er i ferd med å lukkes eller åpnes, og hvor mye bitcoin som holdes on-chain på lightning-noden.

![bilde](assets/en/42.webp)

### Lightning-tjenester

Dette er kun synlig når lightning er aktiv.

Ved siden av å se din Lightning-saldo på BTCPay Server-dashboardet, vil administratorer også se flisen for Lightning-tjenester. Her kan administratorer finne raske knapper for verktøy de bruker for å administrere sin Lightning-node; for eksempel, Ride the Lightning er et av de standardverktøyene med BTCPay Server for Lightning-nodeadministrasjon.

![bilde](assets/en/43.webp)

### Nylige transaksjoner

Flisen for nylige transaksjoner vil vise butikkens mest nylige transaksjoner. Med ett klikk kan Administratoren for BTCPay Server-instansen nå se den siste transaksjonen og se om det er behov for oppmerksomhet mot den.

![bilde](assets/en/44.webp)

### Nylige fakturaer

Flisen for nylige fakturaer viser de 6 siste fakturaene generert av din BTCPay Server, inkludert Status og fakturabeløp. Flisen inkluderer også en "Vis alle"-knapp for enkelt å få tilgang til den fullstendige fakturaoversikten.

![bilde](assets/en/45.webp)

### Point Of Sale og Crowdfunds

Ettersom BTCPay Server leverer et sett med standard plugins eller apper, er Point Of Sale og Crowdfund de to hovedpluginene til BTCPay Server. Med hver butikk og lommebok kan en BTCPay Server-bruker generere så mange Point Of Sales eller Crowdfunds som han ser passende. Hver vil opprette en ny dashboardflis som viser ytelsen til pluginene.

![bilde](assets/en/46.webp)

Legg merke til den lille forskjellen mellom en Point of Sale og Crowdfund-flis. Administratoren ser de øverste varene solgt i Point of Sales-flisen. I Crowdfund-flisen blir dette Top Perks. Begge flisene har raske knapper for å administrere den respektive appen og se nylige fakturaer opprettet av toppvarer eller toppfordeler.

![bilde](assets/en/47.webp)

**!?Merk!?**

Balansediagrammer og nylige transaksjoner er kun tilgjengelige for en on-chain betalingsmetode. Informasjon om Lightning Network-saldoer og transaksjoner står på gjøremålslisten. Fra og med BTCPay Server Versjon 1.6.0, er grunnleggende Lightning Network-saldoer tilgjengelige.

### Ferdighetssammendrag

I denne delen lærte du følgende:

- Den grunnleggende layouten av fliser på hovedlandingssiden er kjent som Dashboardet.
- En grunnleggende forståelse av innholdet i hver flis.

### Kunnskapsvurderingsgjennomgang

List opp så mange fliser fra minnet som du kan fra Dashboardet.

## BTCPay Server - Butikkinnstillinger

<chapterId>e8faef7b-278d-550e-a511-bc3a442daf64</chapterId>
Innen BTCPay Server-programvaren kjenner vi til 2 typer innstillinger. BTCPay Server-butikkspesifikke innstillinger, innstillingsknappen funnet i venstre menylinje under Dashboard, og BTCPay Server-innstillinger, funnet nederst på menylinjen rett over Konto. BTCPay Server Server-spesifikke innstillinger kan kun vises av serveradministratorer.
Butikkinnstillingene består av mange faner for å kategorisere hver gruppe med innstillinger.

- Generelt
- Priser
- Utseende ved utsjekking
- Tilgangstoken
- Brukere
- Roller
- Webhooks
- Utbetalingsprosessorer
- E-poster
- Skjemaer

### Generelt

I fanen for Generelle Innstillinger setter butikkeiere sin merkevarebygging og standarder for betaling. Ved den første oppsettet av butikken, ble et butikknavn gitt; dette vil bli reflektert i de Generelle innstillingene under Butikknavn. Her kan butikkeieren også sette opp sitt nettsted for å matche merkevarebyggingen og en Butikk-ID for at Administratoren skal gjenkjenne i databasen.

#### Merkevarebygging

Siden BTCPay Server er FOSS, kan en butikkeier gjøre tilpasset merkevarebygging for å matche sin butikk. Sett merkevarefargen, lagre din merkevares logoer, og legg til tilpasset CSS for offentlige/kundevendte sider (Fakturaer, Betalingsforespørsler, Trekkbetalinger)

#### Betaling

I betalingsinnstillingene får butikkeiere sette sin butikks standardvaluta (enten i Bitcoin eller i hvilken som helst fiatvaluta).

#### Tillat hvem som helst å opprette fakturaer

Denne innstillingen er ment for utviklere eller byggere på toppen av BTCPay Server. Med denne innstillingen slått på for din butikk, aktiverer den den ytre verden til å opprette fakturaer på din BTCPay Server-instans.

#### Legg til ekstra gebyr (nettverksgebyr) til fakturaer

En funksjon innen BTCPay for å beskytte handlende fra støvangrep eller kunder for å drive en høy kostnad i gebyrer senere når handlende trenger å flytte mye bitcoin på en gang. For eksempel, kunden opprettet en faktura for 20$ og betalte den delvis, betalte 1$ 20 ganger til fakturaen var fullt betalt. Handlende har nå en større transaksjon, noe som øker gruvekostnaden i tilfelle handlende bestemmer seg for å flytte de midlene senere. Som standard påfører BTCPay et ekstra nettverkskostnad til det totale fakturabeløpet for å dekke den utgiften for handlende når fakturaen betales i flere transaksjoner. BTCPay tilbyr flere alternativer for å tilpasse denne beskyttelsesfunksjonen. Du kan påføre et nettverksgebyr:

- Bare hvis kunden gjør mer enn én betaling for fakturaen (I eksemplet ovenfor, hvis kunden opprettet en faktura for 20\$ og betalte 1\$, er det totale skyldige beløpet nå 19\$ + nettverksgebyret. Nettverksgebyret påføres etter den første betalingen)
- På hver betaling (inkludert den første betalingen, i vårt eksempel, vil totalen være 20\$ + nettverksgebyr med en gang, selv på den første betalingen)
- Aldri legg til nettverksgebyr (deaktiverer nettverksgebyret helt)

Selv om det beskytter mot støvtransaksjoner, kan det også reflektere negativt på bedrifter hvis det ikke kommuniseres ordentlig. Kunder kan ha ytterligere spørsmål og tenke at du overbelaster dem.

#### Fakturaen utløper hvis det fulle beløpet ikke er betalt etter?

Fakturatimeren er satt til 15 minutter som standard. Timeren er en beskyttelsesmekanisme mot volatilitet siden den låser Bitcoin-beløpet i henhold til Bitcoin til fiat-ratene. Hvis kunden ikke betaler fakturaen innen den definerte perioden, anses fakturaen som utløpt. Fakturaen anses som "betalt" så snart transaksjonen er synlig på blockchain (0-bekreftelser) men anses som "fullført" når den når antall bekreftelser handlende har definert (vanligvis, 1-6). Timeren er tilpassbar etter minutter.

#### Vurder fakturaen som betalt selv om det betalte beløpet er X% mindre enn forventet?
Når en kunde bruker en børs lommebok for å betale direkte for en faktura, tar børsen et lite gebyr. Dette betyr at en slik faktura ikke anses som fullstendig betalt. Fakturaen får statusen "delvis betalt". Du kan sette prosentsatsen her hvis en handlende ønsker å akseptere underbetalte fakturaer.
### Satser

I BTCPay Server, når en faktura genereres, trenger den alltid den mest oppdaterte og nøyaktige Bitcoin til fiat-prisen. Når du oppretter en ny butikk i BTCPay Server, blir administratorer bedt om å sette deres foretrukne priskilde; etter at butikken er satt opp, kan butikkeiere alltid endre sin priskilde i denne fanen.

#### Avansert regel scripting for satser

Hovedsakelig brukt av avanserte brukere. Hvis aktivert, kan butikkeiere lage skript rundt prisoppførsel og hvordan de skal belaste kundene sine.

#### Testing

Et raskt teststed for dine foretrukne valutapar. Dette inkluderer også en funksjon for å sjekke standard valutapar via REST-spørring.

### Utseende ved utsjekking

Fanen for utseende ved utsjekking starter med fakturaspesifikke innstillinger og en standard betalingsmetode, og aktiverer spesifikke betalingsmetoder når satt krav er oppfylt.

#### Fakturainnstillinger

Standard betalingsmetoder. BTCPay Server i en standard konfigurasjon har tre alternativer.

- BTC (on-chain)
- BTC (LNURL-pay)
- BTC (Off-chain & Lightning)

Vi kan sette parametere for vår butikk, hvor en kunde kun vil samhandle med Lightning når prisen er mindre enn X beløp og omvendt for On-chain transaksjoner når X er større enn Y alltid presentere On-chain betalingsalternativet.

![bilde](assets/en/48.webp)

#### Utsjekking

Fra BTCPay Server utgivelse 1.7, ble det introdusert et nytt utsjekkingsgrensesnitt, Checkout V2, som det kalles. Siden utgivelse 1.9 ble standardisert, kan administratorer og butikkeiere fortsatt sette utsjekkingen til den forrige utgivelsen. Ved å bruke vekslingen "Bruk den klassiske utsjekkingen", kan en butikkeier sette butikken tilbake til den forrige utsjekkingsopplevelsen. BTCPay Server har også et utvalg av forhåndsinnstillinger for nettbasert handel eller en opplevelse i butikk.

![bilde](assets/en/49.webp)

Når en kunde samhandler med butikken og genererer en faktura, er det en utløpstid for fakturaen. Som standard setter BTCPay Server dette til 5 minutter, og administratoren kan sette dette til hva de anser som passende. Utsjekkingssiden kan videre tilpasses ved å sjekke følgende parametere:

- Feire betaling ved å vise konfetti
- Vis butikkens topptekst (Navn og logo)
- Vis "Betal i lommebok"-knappen
- Foren URL/QR-koder for on-chain og off-chain betalinger
- Vis Lightning betalingsbeløp i Satoshis
- Auto-detekter språk ved utsjekking

![bilde](assets/en/50.webp)

Når Auto-detekter språk ikke er satt, vil BTCPay Server som standard vise Engelsk. En butikkeier kan endre dette standardvalget til sitt foretrukne språk.

![bilde](assets/en/51.webp)

Klikk på rullegardinmenyen og butikkeiere kan sette en egendefinert HTML-tittel som skal vises på utsjekkingssiden.

![bilde](assets/en/52.webp)

For å sikre at kunden kjenner sin betalingsmetode, kan en butikkeier eksplisitt sette sin utsjekking til alltid å kreve at brukerne velger sin foretrukne betalingsmetode. Når fakturaen er betalt, tillater BTCPay Server kunden å returnere til nettbutikken. Butikkeiere kan sette denne omdirigeringen etter at kunden har betalt automatisk.

![bilde](assets/en/53.webp)

#### Offentlig kvittering

Innenfor innstillingene for offentlig kvittering, kan en butikkeier sette kvitteringssidene til å være offentlige og vise betalingslisten på kvitteringssiden og QR-koden for kvitteringen for at kunden enkelt kan få tilgang til den digitalt.
### Tilgangstokens

Tilgangstokens brukes for å pare seg med visse e-handelsintegrasjoner eller tilpassede bygde integrasjoner.

### Brukere

Butikkbrukere er der butikkeieren kan administrere sine ansatte, deres kontoer og tilgang til butikken. Etter at de ansatte har opprettet kontoene sine, kan butikkeieren legge til spesifikke brukere i butikken som gjestebrukere eller eiere. For å ytterligere definere den ansattes rolle, se neste avsnitt om "BTCPay Server butikkinnstillinger - Roller."

### Roller

En butikkeier finner kanskje ikke brukerens standardroller betydningsfulle nok. I innstillingene for tilpassede roller kan en butikkeier definere de eksakte behovene for hver rolle i sin virksomhet.

(1) For å opprette en ny rolle, klikk på "+ Legg til rolle"-knappen.

(2) Skriv inn et rollenavn, for eksempel "Kasserer".

(3) Konfigurer de individuelle tillatelsene for rollen.

- Modifiser dine butikker.
- Administrer vekslingskontoer knyttet til dine butikker.
  - Vis vekslingskontoer knyttet til dine butikker.
- Administrer dine uttrekkingsbetalinger.
- Opprett uttrekkingsbetalinger.
  - Opprett ikke-godkjente uttrekkingsbetalinger.
- Modifiser fakturaer.
  - Vis fakturaer.
  - Opprett en faktura.
  - Opprett fakturaer fra lynknutene assosiert med dine butikker.
- Vis dine butikker.
  - Vis fakturaer.
  - Vis dine betalingsforespørsler.
  - Modifiser butikkenes webhooks.
- Modifiser dine betalingsforespørsler.
  - Vis dine betalingsforespørsler.
- Bruk lynknutene assosiert med dine butikker.
  - Vis lynfakturaene assosiert med dine butikker.
  - Opprett fakturaer fra lynknutene assosiert med dine butikker.
- Sett inn midler til vekslingskontoer knyttet til dine butikker.
- Ta ut midler fra vekslingskontoer til din butikk.
- Handle med midler på din butikks vekslingskontoer.

Når rollen er opprettet, er navnet fast og kan ikke endres etterpå i redigeringsmodus.

### Webhooks

Innen BTCPay Server er det ganske enkelt å lage en ny "Webhook". I BTCPay Server butikkinnstillinger - Webhooks-fanen, kan en butikkeier enkelt opprette en ny webhook ved å klikke på "+ Opprett Webhook". Webhooks tillater BTCPay Server å sende HTTP-hendelser relatert til din butikk til andre servere eller e-handelsintegrasjoner.

Du er nå i visningen for å opprette en Webhook. Sørg for at du kjenner din Payload URL og lim denne inn i din BTCPay Server. Mens du har limt inn payload URL, vises webhook-hemmeligheten under. Kopier webhook-hemmeligheten og oppgi den på endepunktet. Når alt er satt, kan du veksle i BTCPay Server til Automatisk gjenlevering. Vi vil prøve å gjenlevere enhver mislykket levering etter 10 sekunder, 1 minutt, og opptil 6 ganger etter 10 minutter. Du kan veksle mellom hver hendelse eller spesifisere hendelsene for dine behov. Sørg for å aktivere webhooken og trykk på Legg til webhook for å lagre den.

Webhooks er ikke ment å være kompatible med Bitpay API. Det er to separate IPN-er (i BitPay-termer: "Øyeblikkelig Betalingsvarsler") i BTCPay Server.

- Webhook
- Varslinger

Bruk kun Varslings-URL når du oppretter fakturaer gjennom Bitpay API.

### Utbetalingsprosessorer
Utbetalingsprosessorer arbeider sammen med utbetalingskonseptet i BTCPay Server. En utbetalingsaggregator for å samle flere transaksjoner og sende dem samtidig. Med utbetalingsprosessorer kan en butikkeier automatisere de samlede utbetalingene. BTCPay Server tilbyr to metoder for automatiserte utbetalinger, On-chain og Off-chain (LN).
Butikkeieren kan klikke og konfigurere begge utbetalingsprosessorene separat. En butikkeier ønsker kanskje bare å kjøre on-chain-prosessoren en gang hver X timer, mens off-chain kan gå hvert få minutter. For On-chain kan du også sette et mål for hvilken blokk den skal inkluderes i. Som standard er dette satt til 1 (eller den neste tilgjengelige blokken). Legg merke til at innstillingen av Off-chain utbetalingsprosessor kun har intervalltidsur og ingen blokkmål. Lightning network-betalinger er øyeblikkelige.

![bilde](assets/en/62.webp)
![bilde](assets/en/63.webp)

Butikkeiere kan bare konfigurere on-chain-prosessoren hvis de har en Hot-wallet koblet til butikken sin.

![bilde](assets/en/64.webp)

Etter å ha satt opp en Utbetalingsprosessor, kan du raskt fjerne eller endre den ved å returnere til fanen for Utbetalingsprosessor i BTCPay Server Butikkinnstillinger.

**!?Merk!?**

Utbetalingsprosessor on-chain - Onchain utbetalingsprosessoren kan bare fungere på en butikk konfigurert med en Hot wallet koblet til. Hvis det ikke er noen hot wallet koblet til, holder ikke BTCPay Server nøklene til lommeboken og vil ikke kunne behandle utbetalingene automatisk.

### E-poster

BTCPay Server kan bruke e-poster for varslinger eller, når det er satt opp riktig, for å gjenopprette kontoer som ble opprettet på instansen, ettersom standard BTCPay Server ikke sender en e-post når passordet er tapt, for eksempel.

![bilde](assets/en/65.webp)

Før en butikkeier kan sette e-postregler for å utløse på spesifikke hendelser i butikken sin, må vi sette opp noen grunnleggende e-postinnstillinger. BTCPay Server trenger disse innstillingene for å sende e-poster for hendelser basert på butikken din eller for tilbakestilling av passord.

BTCPay Server har gjort det enklere å fylle ut denne informasjonen ved å bruke "Hurtigfyll"-alternativet:

- Gmail.com
- Yahoo.com
- Mailgun
- Office365
- SendGrid

Ved å bruke hurtigfyll-alternativet, vil BTCPay Server forhåndsutfylle feltene for SMTP-serveren og porten; nå trenger butikkeieren bare å fylle ut sine legitimasjonsopplysninger i en e-postadresse, innlogging (som vanligvis er lik e-postadressen din), og passordet ditt. Det avanserte alternativet BTCPay Server tilbyr i e-postinnstillingene er å deaktivere TLS-sertifikatsikkerhetskontroller; som standard er dette aktivert.

![bilde](assets/en/66.webp)

Med e-postregler kan en butikkeier sette spesifikke hendelser for å utløse e-poster til spesifikke e-postadresser.

- Faktura Opprettet
- Faktura Mottok Betaling
- Faktura Behandles
- Faktura Utløpt
- Faktura Avregnet
- Faktura Ugyldig
- Faktura Betaling Avregnet

Hvis kunden har oppgitt en e-postadresse, kan disse utløserne også sende informasjonen til kunden. Butikkeiere kan forhåndsutfylle emnelinjen for å gjøre det klart hvorfor denne e-posten skjedde og hvilken utløser som forårsaket den.

![bilde](assets/en/67.webp)

### Skjemaer

Siden BTCPay Server ikke samler inn noen data, ønsker en butikkeier kanskje å legge til et tilpasset skjema til sin utsjekkingsopplevelse; på denne måten kan butikkeieren samle inn tilleggsinformasjon fra kunden sin. BTCPay Server Skjemabygger består av to deler, en visuell og en mer avansert kodevisning av skjemaene.
Når du oppretter et nytt skjema, åpner BTCPay Server et nytt vindu som ber om grunnleggende informasjon om hva du ønsker at det nye skjemaet ditt skal be om. Først må butikkeieren gi et klart navn til sitt nye skjema, dette navnet KAN IKKE endres etter at det er satt.
![bilde](assets/en/68.webp)

Etter at butikkeieren har gitt skjemaet et navn, kan du også veksle bryteren for "Tillat skjema for offentlig bruk" til PÅ, og den blir grønn. Dette er slik at skjemaet blir brukt på alle kundevendte steder. For eksempel, hvis en butikkeier oppretter 1 separat faktura ikke gjennom sitt Point Of Sale, kan han fortsatt ønske å samle informasjonen fra kunden; denne vekslingen til PÅ tillater at denne informasjonen blir samlet.

![bilde](assets/en/69.webp)

Hvert skjema starter med minst 1 nytt skjemafelt. En butikkeier kan velge hvilken type felt det skal være;

- Tekst
- Nummer
- Passord
- E-post
- URL
- Telefonnumre
- Dato
- Skjulte felt
- Feltsett
- Et tekstområde for åpne kommentarer.
- Valgvelger

Hver type kommer med sine parametere å fylle ut. Butikkeieren kan sette det etter sitt ønske. Under det første opprettede feltet, kan butikkeiere fortsette å legge til nye felt til dette ene skjemaet.

![bilde](assets/en/70.webp)

#### Avanserte tilpassede skjemaer

BTCPay Server lar deg også bygge skjemaer i kode. JSON, spesielt. I stedet for å se på redigereren, kan butikkeiere klikke på KODE-knappen rett ved siden av redigereren og komme inn i koden til skjemaene sine. I en feltdefinisjon kan bare følgende felt settes; verdiene til feltene lagres i metadataene til fakturaen:

| Felt                  | Beskrivelse                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| .fields.constant      | Hvis sann, må .value settes i skjemadefinisjonen, og brukeren vil ikke kunne endre feltets verdi. (eksempel: skjemadefinisjonens versjon)                                                                                                                                                                                                                                                                                                       |
| .fields.type          | HTML-inndatatype tekst, radio, avkrysningsboks, passord, skjult, knapp, farge, dato, datetime-local, måned, uke, tid, e-post, nummer, område, søk, url, velg, tel                                                                                                                                                                                                                                                                                                |
| .fields.options       | Hvis .fields.type er select, listen over valgbare verdier                                                                                                                                                                                                                                                                                                                                                                                                           |
| .fields.options.text  | Teksten som vises for dette alternativet                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| .fields.options.value | Verdien av feltet hvis dette alternativet er valgt                                                                                                                                                                                                                                                                                                                                                                                                                  |
| .fields.type=fieldset | Opprett et HTML-feltsett rundt barna .fields.fields (se nedenfor)                                                                                                                                                                                                                                                                                                                                                                                              |
| .fields.name          | JSON-egenskapsnavnet til feltet slik det vil vises i fakturaens metadata                                                                                                                                                                                                                                                                                                                                                                                    |
| .fields.value         | Standardverdien til feltet                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| .fields.required      | hvis sant, vil feltet være påkrevd                                                                                                                                                                                                                                                                                                                                                                                                                                |
| .fields.label         | Etiketten til feltet                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| .fields.helpText      | Tilleggstekst for å gi en forklaring på feltet.                                                                                                                                                                                                                                                                                                                                                                                                           |
| .fields.fields        | Du kan organisere feltene dine i en hierarki, slik at underordnede felt kan være nøstet innenfor fakturaens metadata. Denne strukturen kan hjelpe deg med å bedre organisere og håndtere den innsamlede informasjonen, noe som gjør det lettere å få tilgang til og tolke den. For eksempel, hvis du har et skjema som samler inn kundeinformasjon, kan du gruppere feltene under et overordnet felt kalt kunde. Innenfor dette overordnede feltet kan du ha underordnede felt som navn, e-post og adresse. |
Feltnavnet representerer JSON-egenskapsnavnet som lagrer den brukerleverte verdien i fakturaens metadata. Noen velkjente navn kan tolkes og endre fakturaens innstillinger.

| Feltnavn          | Beskrivelse              |
| ----------------- | ------------------------ |
| invoice_amount    | Fakturaens beløp         |
| invoice_currency  | Fakturaens valuta        |

Du kan forhåndsutfylle feltene i en faktura automatisk ved å legge til spørringsstrenger til skjemaets URL, slik som "?your_field=value".

Her er noen bruksområder for denne funksjonen:

- Assistering av brukerinndata: Forhåndsutfyll felt med kjent kundeinformasjon for å gjøre det enklere for dem å fullføre skjemaet. For eksempel, hvis du allerede kjenner en kundes e-postadresse, kan du forhåndsutfylle e-postfeltet for å spare dem for tid.
- Personalisering: Tilpass skjemaet basert på kundepreferanser eller segmentering. For eksempel, hvis du har forskjellige kundenivåer, kan du forhåndsutfylle skjemaet med relevant data, som deres medlemskapsnivå eller spesifikke tilbud.
- Sporing: Spor kildene til kundebesøk ved hjelp av skjulte felt og forhåndsutfylte verdier. For eksempel kan du opprette lenker med forhåndsutfylte utm_media-verdier for hver markedsføringskanal (f.eks., Twitter, Facebook, E-post). Dette hjelper deg med å analysere effektiviteten av dine markedsføringsanstrengelser.
- A/B-testing: Forhåndsutfyll felt med forskjellige verdier for å teste forskjellige versjoner av skjemaet, noe som gjør det mulig for deg å optimalisere brukeropplevelsen og konverteringsratene.

### Ferdighetssammendrag

I denne delen lærte du følgende:

- Oppsettet og funksjonene til fanene i Butikkinnstillinger
- En rekke alternativer for finjustering av håndteringen av underliggende valutakurser, delbetalinger, små underbetalinger og mer.
- Tilpasse utseendet på utsjekkingen, inkludert prisavhengig hovedkjede vs. Lightning-aktivering på fakturaer.
- Håndtere nivåer av butikktilgang og tillatelser på tvers av roller.
- Konfigurere automatiserte e-poster og deres utløsere
- Opprette egendefinerte skjemaer for å samle inn ytterligere kundeinformasjon ved utsjekking.

### Kunnskapsvurderinger

#### KA Gjennomgang

Hva er forskjellen mellom Butikkinnstillinger og Serverinnstillinger?

#### KA Hypotetisk

Beskriv noen alternativer du kan velge i Utsjekkingsutseende > Fakturainnstillinger, og hvorfor.

## BTCPay Server - Serverinnstillinger

<chapterId>1dd858a2-49ea-586b-9bc1-75a65f508df6</chapterId>

BTCPay Server består av to forskjellige innstillingsvisninger. Den ene er dedikert til Butikkinnstillinger og den andre for Serverinnstillinger. Sistnevnte er kun tilgjengelig hvis du er en Serveradministrator og ikke for butikkeiere. Serveradministratorer kan legge til brukere, opprette egendefinerte roller, konfigurere e-postserveren, sette retningslinjer, utføre vedlikeholdsoppgaver, sjekke alle tjenester knyttet til BTCPay Server, laste opp filer til serveren, eller sjekke logger.

### Brukere

Som nevnt i forrige del, kan Serveradministratorer invitere brukere til serveren sin ved å legge dem til i Brukere-fanen.

### Serveromfattende egendefinerte Roller

BTCPay Server kjenner to typer egendefinerte roller, de butikkspesifikke egendefinerte rollene og serveromfattende Egendefinerte roller i BTCPay Server-innstillingene. Begge holder et lignende sett med tillatelser; imidlertid, hvis satt gjennom BTCpay Server Innstillinger - Roller-fanen, vil den anvendte rollen være serveromfattende og gjelde for flere butikker. Legg merke til en "Serveromfattende" tag til de egendefinerte rollene i Serverinnstillingene.
### Serveromfattende tilpassede roller

Serveromfattende tilpassede rolletillatelser;

- Endre dine butikker.
- Administrere børskontoer knyttet til dine butikker.
  - Se børskontoer knyttet til dine butikker.
- Administrere dine uttaksbetalinger.
- Opprette uttaksbetalinger.
  - Opprette ikke-godkjente uttaksbetalinger.
- Endre fakturaer.
  - Se fakturaer.
  - Opprette en faktura.
  - Opprette fakturaer fra lynknutepunktene assosiert med dine butikker.
- Se dine butikker.
  - Se fakturaer.
  - Se dine betalingsforespørsler.
  - Endre butikkenes webhooks.
- Endre dine betalingsforespørsler.
  - Se dine betalingsforespørsler.
- Bruke lynknutepunktene assosiert med dine butikker.
  - Se lynfakturaer assosiert med dine butikker.
  - Opprette fakturaer fra lynknutepunktene assosiert med dine butikker.
- Sette inn midler til børskontoer knyttet til dine butikker.
- Ta ut midler fra børskontoer til din butikk.
- Handle med midler på din butikks børskontoer.

**!?Merk!?**

Når rollen blir opprettet, er navnet fast og kan ikke endres etterpå i redigeringsmodus.

### E-post

Serveromfattende e-postinnstillinger ser lik ut som de i butikkspesifikke e-postinnstillinger. Imidlertid håndterer denne oppsettet ikke bare utløsere for butikker eller administratorlogger. Denne e-postoppsettet gjør også passordgjenoppretting tilgjengelig på BTCPay Server ved innlogging. Det fungerer på samme måte som de butikkspesifikke innstillingene; administratorer kan raskt fylle inn sine e-postparametere og legge inn sine e-postopplysninger, og serveren kan nå sende e-poster.

### Retningslinjer

BTCPay Server-policyadministratorer kan sette noen innstillinger om temaer som eksisterende brukerinnstillinger, nye brukerinnstillinger, varselsinnstillinger og vedlikeholdsinnstillinger. Disse er ment for å registrere nye brukere som admin eller vanlige brukere eller til og med skjule BTCPay Server fra søkemotorer ved å legge til i serverheaderen din.

#### Eksisterende brukerinnstillinger

Alternativene tilgjengelig her er separate fra tilpassede roller. Disse ekstra tillatelsene kan gjøre en butikk eller butikkeier sårbar for angrep. Retningslinjer som kan legges til eksisterende brukere:

- Tillate ikke-adminer å bruke det interne lynknutepunktet i butikkene deres.
  - Dette ville tillate butikkeiere å bruke serveradministratorens lynknutepunkt og derfor hans midler! Vær oppmerksom, dette er ikke en løsning for å gi tilgang til lyn.
- Tillate ikke-adminer å opprette hot wallets for butikkene deres.
  - Dette ville tillate hvem som helst med en konto på din BTCPay Server-instans å opprette Hot-wallets og lagre deres gjenopprettingsfrø på administratorens server. Dette kan gjøre administratoren ansvarlig for å holde tredjeparts midler!
- Tillate ikke-adminer å importere hot wallets for butikkene deres.
  - Likt som det forrige emnet om å opprette Hot wallets, tillater denne retningslinjen import av en hot wallet, med de samme farene nevnt i seksjonen for å opprette hot wallets.

#### Innstillinger for nye brukere

Vi kan sette noen viktige innstillinger for å håndtere nye brukere som kommer til serveren. Vi kan sette en bekreftelses-e-post for nye registreringer, deaktivere opprettelse av nye brukere gjennom innloggingsskjermen, og begrense ikke-adminers tilgang til brukeroppretting over API.

- Kreve en bekreftelses-e-post for registrering.
  - Serveradministratoren må ha satt opp en e-postserver!
- Deaktivere ny brukerregistrering på serveren
- Deaktivere ikke-adminers tilgang til API-endepunktet for brukeroppretting.

Som standard har BTCPay Server slått på deaktivering av ny brukerregistrering og slått av ikke-adminers tilgang til API-endepunktet for brukeroppretting. Dette er ut fra et sikkerhetsaspekt der ingen tilfeldig person som kanskje har funnet BTCPay-innloggingen til serveren din, kan begynne å opprette kontoer.
#### Varslingsinnstillinger
![bilde](assets/en/76.webp)

#### Vedlikeholdsinnstillinger

BTCPay Server er et Open Source-prosjekt som finnes på GitHub. Når BTCPay Server slipper en ny versjon av programvaren, kan administratorer få beskjed om at en ny versjon er tilgjengelig. Administratorer kan også ønske å forhindre søkemotorer (google, yahoo, duckduckgo) fra å indeksere BTCPay Server-domenet. Siden BTCPay Server er FOSS, kan utviklere over hele verden ønske å skape nye funksjoner; BTCPay Server har en eksperimentell funksjon som, når aktivert, lar en administrator bruke funksjoner som ikke er ment for produksjon ennå, kun for testformål.

- Sjekk utgivelser på GitHub og varsle når en ny BTCPay Server-versjon er tilgjengelig.
- Forhindre søkemotorer fra å indeksere dette nettstedet
- Aktiver eksperimentelle funksjoner.

![bilde](assets/en/77.webp)

#### Plugins

BTCPay Server kan legge til Plugins og utvide funksjonssettet sitt. Pluginene lastes som standard fra BTCPay Server-plugin-builder-repositoriet. En administrator kan imidlertid velge å se plugins i en Pre-release-tilstand, og hvis plugin-utvikleren tillater det, kan serveradministratoren nå installere beta-versjoner av plugins.

![bilde](assets/en/78.webp)

##### Tilpasningsinnstillinger

En standard BTCPay Server-implementering vil være tilgjengelig gjennom domenet som er satt opp for den ved installasjon. En serveradministrator kan imidlertid omkartlegge rot-domene og vise en av de opprettede appene fra en spesifikk butikk. Serveradministratoren kan også kartlegge spesifikke domener til spesifikke apper.

- Vis appen på nettstedets rot
  - Viser liste over mulige apper å vise på rot-domene.

![bilde](assets/en/79.webp)

- Kartlegg spesifikke domener til spesifikke apper.
  - Når du klikker for å sette opp et spesifikt domene for spesifikke apper, kan administratoren sette så mange domener pekt på spesifikke apper som nødvendig.

![bilde](assets/en/80.webp)

#### Blokkutforskere

BTCPay Server kommer som standard med mempool.space som sin blokkutforsker for transaksjoner. Når BTCPay Server genererer en ny faktura, og det er en transaksjon knyttet til den, kan butikkeieren klikke for å åpne transaksjonen; BTCPay Server vil standard peke mot mempool.space som en blokkutforsker; en serveradministrator kan endre dette etter eget ønske.

![bilde](assets/en/81.webp)

### Tjenester

Innstillingene for BTCPay Server: Tjenester-fanen gir en oversikt over komponentene din BTCPay Server bruker. Tjenestene din BTCPay Server eksponerer kan variere avhengig av implementeringsmetoden.

En BTCPay Server-administrator kan klikke på "Se informasjon" bak hver tjeneste for å åpne den og sette spesifikke innstillinger.

![bilde](assets/en/82.webp)

#### LND (gRPC)

BTCPay eksponerer LNDs GRPC-tjeneste for ekstern bruk; du vil finne tilkoblingsinformasjon i denne spesifikke innstillingsmenyen; kompatible lommebøker er oppført her. BTCPay Server gir også en QR-kode for tilkobling å skanne og bruke i mobil lommeboken.

Serveradministratorer kan åpne flere detaljer for å se;

- Vertsdetaljer
- Bruk av SSL
- Macaroon
- AdminMacaroon
- InvoiceMacaroon
- ReadonlyMacaroon
- GRPC SSL Cipher suite (GRPC_SSL_CIPHER_SUITES)

#### LND (REST)

BTCPay eksponerer LNDs REST-tjeneste for ekstern bruk; du vil finne tilkoblingsinformasjon her; kompatible lommebøker er oppført her. Blant de kompatible lommebøkene er Joule, Alby, og ZeusLN. BTCPay Server gir en QR-kode for tilkobling, skann og bruk i den kompatible lommeboken.

- REST Uri
- Macaroon
- AdminMacaroon - InvoiceMacaroon
- ReadonlyMacaroon

#### LND Seed Backup

LND seed backup er nyttig for å gjenopprette midler fra din LND-lommebok i tilfelle korrupsjon av din server. Siden Lightning-noden er en Hot-wallet, kan du finne den konfidensielle seed-informasjonen på denne siden.

LND dokumenterer gjenopprettingsprosessen. Se https://github.com/lightningnetwork/lnd/blob/master/docs/recovery.md for dokumentasjon.

#### Ride The Lightning

Ride the Lightning er et verktøy for administrasjon av Lightning-noder, bygget som Open Source-programvare. BTCPay Server bruker RTL som komponent for administrasjon av Lightning-noder i sin stakk. BTCPay Server-administratorer kan nå RTL gjennom Serverinnstillinger - Tjenester-fanen eller ved å klikke på Lightning-lommeboken.

#### Full node P2P

Serveradministratorer kan ønske å koble sin Bitcoin-node til en mobil lommebok. Denne siden eksponerer informasjon for å koble seg eksternt til din fullnode via P2P-protokollen. På tidspunktet for skriving av denne boken, lister BTCPay Server opp Blockstream Green og Wasabi-lommebok som kompatible lommebøker. BTCPay Server gir en QR-kode for tilkobling, skann og bruk i den kompatible lommeboken.

#### Full node RPC

Denne siden eksponerer informasjon for å koble seg eksternt til din fullnode via RPC-protokollen.

#### SSH

SSH brukes til vedlikeholdsformål. BTCPay Server viser den opprinnelige tilkoblingskommandoen for å nå din server og SSH offentlige nøkler autorisert for å koble til din server. Serveradministratorer kan ønske å slå av SSH-endringer gjennom UI av BTCPay Server.

#### Dynamisk DNS

Dynamisk DNS lar deg ha et stabilt DNS-navn som peker til din server, selv om din IP-adresse endrer seg regelmessig. Dette anbefales hvis du er vert for BTCPay Server hjemme og ønsker å ha et clearnet-domene for å få tilgang til din server.

Merk at du må konfigurere din NAT og BTCPay Server-installasjon riktig for å få HTTPS-sertifikatet.

### Tema

BTCPay Server kommer som standard med to temaer: Lys og Mørk modus. Disse kan byttes ved å klikke på Konto nederst til venstre og veksle mellom Mørkt tema eller Lyst tema. BTCPay Server-administratorer kan legge til sitt tema ved å tilby et tilpasset CSS-tema.

Administratorer kan utvide Lys/Mørk-temaet ved å legge til sitt eget tilpassede CSS eller sette sitt tilpassede tema som et fullstendig tilpasset.

![bilde](assets/en/83.webp)

#### Server Branding

Serveradministratorer kan endre BTCPay Server-brandingen ved å sette en serveromfattende branding av ditt selskap. Siden BTCPay Server er FOSS, kan serveradministratorer white label programvaren og endre utseendet for å passe til deres virksomhet.

![bilde](assets/en/84.webp)

### Vedlikehold

Som serveradministrator forventer brukerne dine at du tar godt vare på serveren. Innenfor BTCPay Servers Vedlikeholdsfane, kan admin utføre noe essensielt vedlikehold. Sett domenenavnet til BTCPay Server-instansen, Restart eller rengjør serveren. Muligens viktigst, kjør oppdateringer.

BTCPay Server er et Open Source-prosjekt og oppdateres ofte. Hver ny utgivelse annonseres enten gjennom dine BTCPay Server-notifikasjoner eller på de offisielle kanalene BTCPay Server kommuniserer gjennom.

![bilde](assets/en/85.webp)

#### Domenenavn

Etter at BTCPay Server er satt opp, kan en administrator ønske å endre fra sitt opprinnelige domene. Innenfor Vedlikeholdsfanen, kan administratoren endre domenet. Etter å ha klikket bekreft og satt opp de riktige DNS-postene på domenet, oppdaterer og restarter BTCPay Server for å returnere til det nye domenet.

![bilde](assets/en/86.webp)

#### Restart

Restart BTCPay Server og relaterte tjenester.

![bilde](assets/en/87.webp)

#### Rengjør
BTCPay Server kjører med Docker-komponenter; med oppdateringer kan det hende det blir rester av Docker-bilder, temp-filer, osv. Serveradministratorer kan rydde opp i dette og gjenvinne plass i sitt miljø ved å kjøre rense-skriptet.
![bilde](assets/en/88.webp)

#### Oppdatering

Muligens det viktigste alternativet i Vedlikehold-fanen. BTCPay Server er bygget av fellesskapet, og derfor er oppdateringssyklusene hyppigere enn de fleste programvareprodukter. Når BTCPay Server har en ny utgivelse, vil administratorer bli varslet i sitt varslingssenter. Ved å klikke på oppdateringsknappen, vil BTCPay Server sjekke GitHub for den nyeste utgivelsen, oppdatere Serveren og starte på nytt. Før oppdatering, rådes serveradministratorer alltid til å lese utgivelsesnotatene distribuert gjennom de offisielle kanalene til BTCPay Server.

![bilde](assets/en/89.webp)

### Logger

Å stå overfor et problem er aldri gøy. Dette dokumentet forklarer den mest vanlige arbeidsflyten og stegene for å effektivt identifisere problemet ditt og løse det selv eller med hjelp fra fellesskapet.

Det er avgjørende å identifisere problemet.

#### Replikere problemet

Først og fremst, prøv å bestemme når problemet oppstår. Prøv å replikere problemet. Prøv å oppdatere og starte Serveren på nytt for å verifisere at du kan reprodusere problemet ditt. Hvis det beskriver problemet ditt bedre, ta et skjermbilde.

##### Oppdatere serveren

Sjekk din versjon av BTCPay Server hvis den er mye eldre enn [den nyeste versjonen](https://github.com/btcpayserver/btcpayserver/releases) av BTCPay Server. Å oppdatere Serveren din kan løse problemet.

##### Starte serveren på nytt

Å starte Serveren din på nytt er en enkel måte å løse mange av de mest vanlige problemene med BTCPay Server. Du må kanskje SSH inn i Serveren din for å starte den på nytt.

##### Starte en tjeneste på nytt

For noen problemer, kan det hende du bare trenger å starte en bestemt tjeneste i din BTCPay Server-distribusjon på nytt. Som for eksempel å starte lets encrypt-containeren på nytt for å fornye SSL-sertifikatet.

```bash
sudo su -
cd btcpayserver-docker
docker restart letsencrypt-nginx-proxy-companion
```

Bruk docker ps for å finne navnet på en annen tjeneste du ønsker å starte på nytt.

#### Se gjennom loggene

Logger kan gi et vesentlig stykke informasjon. I de følgende avsnittene vil vi beskrive hvordan du får logginformasjon for ulike deler av BTCPay.

##### BTCPay Logger

Siden v1.0.3.8, kan du enkelt få tilgang til BTCPay Server-logger fra frontenden. Hvis du er en serveradmin, gå til Serverinnstillinger > Logger og åpne loggfilen. Hvis du ikke vet hva en bestemt feil i loggene betyr, nevn det når du feilsøker.

Hvis du ønsker mer detaljerte logger og bruker en Docker-distribusjon, kan du se logger for spesifikke Docker-containere ved hjelp av kommandolinjen. Se disse [instruksjonene for å ssh](https://docs.btcpayserver.org/FAQ/ServerSettings/#how-to-ssh-into-my-btcpay-running-on-vp%C2%80) inn i en instans av BTCPay som kjører på en VPS.

På neste side, en generell liste over containernavnene som brukes for BTCPay Server.

Kjør kommandoene nedenfor for å skrive ut logger etter containernavn. Erstatt containernavnet for å se andre containerlogger.

```bash
sudo su -
cd btcpayserver-docker
docker ps
docker logs --tail 100 generated_btcpayserver_1
```

| Logger for   | Container Navn                    |
| ------------ | --------------------------------- |
| BTCPayServer | generated_btcpayserver_1          |
| NBXplorer    | generated_nbxplorer_1             |
| Bitcoind     | btcpayserver_bitcoind             |
| Postgres     | generated_postgres_1              |
| proxy        | letsencrypt-nginx-proxy-companion |
| Nginx        | nginx-gen                         |
| Nginx        | nginx                             |
| c-lightning  | btcpayserver_clightning_bitcoin   |
| LND          | btcpayserver_lnd_bitcoin          |
| RTL          | generated_lnd_bitcoin_rtl_1       |
| Thunderhub   | generated_bitcoin_thub_1          |
| LibrePatron  | librepatron                       |
| Tor          | tor-gen                           |
| Tor          | tor                               |

###### Lightning Network LND - Docker

Det er noen måter å få tilgang til dine LND logger når du bruker Docker. Først logg inn som root:

```bash
sudo su -
Naviger til riktig mappe:
cd btcpayserver-docker
# Finn container navn:
docker ps
Skriv ut logger ved container navn:
docker logs --tail 100 btcpayserver_lnd_bitcoin
```

Alternativt kan du raskt skrive ut logger ved å bruke container ID (bare de første unike ID-tegnene er nødvendige, som de to lengst til venstre tegnene):

```bash
docker logs 'legg til din container ID'
```

Hvis du av en eller annen grunn trenger flere logger

```bash
sudo su -
cd /var/lib/docker/volumes/generated_lnd_bitcoin_datadir/_data/logs/ bitcoin/mainnet/
ls
```

Du vil se noe som

```bash
lnd.log lnd.log.13 lnd.log.15 lnd.log.16.gz lnd.log.17.gz
```

For å få tilgang til ukomprimerte logger av disse loggene gjør `cat lnd.log` eller hvis du vil ha en annen, bruk `cat lnd.log.15`.

For å få tilgang til komprimerte logger i `.gzip` bruk `gzip -d lnd.log.16.gz` (i dette tilfellet får vi tilgang til `lnd.log.16.gz`). Dette bør gi deg en ny fil, hvor du kan gjøre `cat lnd.log.16`. I tilfelle det ovennevnte ikke fungerer, kan det hende du må installere gzip først med `sudo apt-get install gzip`.

###### Lightning Network c-lightning - Docker

```bash
sudo su -
docker ps
# Finn c-lightning container ID.
docker logs 'legg til din container ID her'
```

alternativt, bruk dette

```bash
docker logs --tail 100 btcpayserver_clightning_bitcoin
```

Du kan også få logg informasjon med c-lightning cli kommando.

```bash
bitcoin-lightning-cli.sh getlog
```

#### Bitcoin Node Logger

I tillegg til å [se på logger](https://docs.btcpayserver.org/Troubleshooting/#2-looking-through-the-logs) av din Bitcoind container, kan du også bruke noen av [bitcoin-cli kommandoene](https://developer.bitcoin.org/reference/rpc/index.html)

[(åpner nytt vindu)](https://developer.bitcoin.org/reference/rpc/index.html) for å få informasjon fra din bitcoin node. BTCPay inkluderer et skript for å tillate deg å kommunisere med din Bitcoin node enkelt.

Inne i btcpayserver-docker mappen, få blockchain informasjon ved hjelp av din node:

```bash
bitcoin-cli.sh getblockchaininfo
```

### Filer

BTCPay Server har et lokalt filsystem og laster opp Store (produkt) eiendeler, Logoer og merkevarebygging direkte til Serveren. Serverens filsystem er kun tilgjengelig for Serveradministratorer; butikkeiere kan laste opp sine logoer/merkevarebygging på butikknivå.
Når serveradministratoren er i fanen for Filoppbevaring, er det mulig å direkte laste opp til serveren din eller endre filoppbevaringsleverandøren til et Lokalt filsystem eller Azure Blob Storage.
![bilde](assets/en/90.webp)

![bilde](assets/en/91.webp)

### Ferdighetssammendrag

I denne seksjonen lærte du følgende:

- Forskjellen mellom Lagre- og Serverinnstillinger, spesielt slik de relaterer seg til Brukere, Roller og E-poster
- Sette serveromfattende policyer for Lightning eller Bitcoin hot wallet bruk og opprettelse, ny brukerregistrering og e-postvarslinger.
- Hvordan legge til egendefinerte temaer (i stedet for enkle lys/mørke alternativer som tilbys) samt opprette egendefinerte logoer
- Utføre enkle servervedlikeholdsoppgaver via GUI-en som tilbys
- Feilsøke problemer, inkludert å hente detaljer for noen av Docker-containerne eller noden din
- Administrere filoppbevaring

### Kunnskapsvurdering

#### KA Konseptuell Gjennomgang

Hva er forskjellen på Roller tildelt gjennom Server vs Butikkinnstillinger, og hva beskriver en potensiell bruk for den ene over den andre?

#### KA Praktisk Gjennomgang

Beskriv noen mulige bruksområder aktivert i fanen for Policyer.

#### KA Praktisk Gjennomgang

Beskriv noen handlinger en administrator kanskje rutinemessig gjør i fanen for Vedlikehold.

## BTCPay Server - Betalinger

<chapterId>e2b71ff9-3f4f-5e71-9771-8e03fbbef00f</chapterId>

En faktura er et dokument selgeren utsteder til kjøperen for å samle inn betaling.

I BTCPay Server representerer en faktura et dokument som må betales innenfor et definert tidsintervall til en fast vekslingskurs. Fakturaer har en utløpsdato fordi de låser vekslingskursen innenfor en spesifisert tidsramme for å beskytte mottakeren mot prisfluktuasjoner.

Kjernen i BTCPay Server er evnen til å fungere som et Bitcoin fakturahåndteringssystem. En faktura er et essensielt verktøy for å spore og håndtere en mottatt betaling.

Med mindre du bruker en innebygd [Wallet](https://docs.btcpayserver.org/Wallet/) for å motta betalinger manuelt, vil alle betalinger innenfor en butikk vises på Fakturasiden. Denne siden sorterer betalinger kumulativt etter dato og er et sentralt stykke for fakturahåndtering og feilsøking av betaling.

![bilde](assets/en/92.webp)

### Generelt

#### Fakturastatus

Tabellen nedenfor lister opp og beskriver standard fakturastatus i BTCPay og foreslår vanlige handlinger. Handlingene er kun anbefalinger. Det er opp til brukerne å definere den beste handlingsmåten for deres brukstilfelle og virksomhet.

| Fakturastatus              | Beskrivelse                                                                                                                             | Handling                                                                                                                      |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Ny                         | Ikke betalt, fakturatimeren har fortsatt ikke utløpt                                                                                    | Ingen                                                                                                                        |
| Ny (delvisBetalt)          | Betalt, ikke i fullt, fakturatimeren har fortsatt ikke utløpt                                                                           | Ingen                                                                                                                        |
| Utløpt                     | Ikke betalt, fakturatimeren har utløpt                                                                                                  | Ingen                                                                                                                        |
| Utløpt (delvisBetalt) \*\* | Betalt, ikke i fullt beløp, og utløpt                                                                                                   | Kontakt kjøper for å ordne en refusjon eller be dem om å betale det skyldige beløpet. Eventuelt merk fakturaen som avregnet eller ugyldig |
| Utløpt (betaltSent)        | Betalt, i fullt beløp, etter at fakturatimeren har utløpt                                                                               | Kontakt kjøper for å ordne en refusjon eller behandle ordren hvis sene bekreftelser er akseptable.                           |
| Avregnet (betaltOver)      | Betalt mer enn fakturabeløpet, avregnet, mottatt tilstrekkelig antall bekreftelser                                                      | Kontakt kjøper for å ordne en refusjon for det ekstra beløpet, eller eventuelt vent på at kjøper tar kontakt med deg        |
| Behandling                 | Betalt i sin helhet, men har ikke mottatt tilstrekkelig antall bekreftelser spesifisert i butikkinnstillingene                                   | Kontakt kjøper for å ordne en refusjon for det ekstra beløpet, eller vent eventuelt på at kjøperen tar kontakt med deg                         |
| Behandling (betaltOver)    | Betalt mer enn fakturabeløpet, ikke mottatt tilstrekkelig antall bekreftelser                                                      | Vent til det er avklart, deretter kontakt kjøper for å ordne en refusjon for det ekstra beløpet, eller vent eventuelt på at kjøperen tar kontakt med deg |
| Avklart                    | Betalt, i sin helhet, mottatt tilstrekkelig antall bekreftelser i butikk                                                                     | Utfør ordren                                                                                                            |
| Avklart (merket)           | Statusen ble manuelt endret til avklart fra en behandling eller ugyldig status                                                             | Butikkadmin har markert betalingen som avklart                                                                               |
| Ugyldig\*                  | Betalt, men klarte ikke å motta tilstrekkelig antall bekreftelser innen tiden spesifisert i butikkinnstillingene                              | Sjekk transaksjonen på en blockchain-utforsker, hvis den mottok tilstrekkelig bekreftelser, merk som avklart                    |
| Ugyldig (merket)           | Statusen ble manuelt endret til ugyldig fra en avklart eller utløpt status                                                                 | Butikkadmin har markert betalingen som ugyldig                                                                               |
| Ugyldig (betaltOver)       | Betalt mer enn fakturabeløpet, men klarte ikke å motta tilstrekkelig antall bekreftelser innen tiden spesifisert i butikkinnstillingene | Sjekk transaksjonen på en blockchain-utforsker, hvis den mottok tilstrekkelig bekreftelser, merk som avklart                    |

#### Fakturadetaljer

Fakturadetaljsiden inneholder all informasjon relatert til en faktura.

Fakturainformasjon opprettes automatisk basert på fakturastatus, valutakurs, osv. Produktinformasjon opprettes automatisk hvis fakturaen ble opprettet med produktinformasjon, slik som i Point of Sale-appen.

#### Filtrering av fakturaer

Fakturaer kan filtreres via de raske filtrene som ligger ved siden av søkeknappen eller de avanserte filtrene, som kan aktiveres ved å klikke på (Hjelp)-lenken øverst. Brukere kan filtrere fakturaer etter butikk, ordre-id, vare-id, status eller dato.

#### Eksport av faktura

BTCPay Server-fakturaer kan eksporteres i CSV- eller JSON-format. For mer informasjon om fakturaeksport og regnskap.

#### Refusjon av en faktura

Hvis du av en eller annen grunn ønsker å utstede en refusjon, kan du enkelt opprette en refusjon fra fakturavisningen.

#### Arkivering av fakturaer

Som et resultat av funksjonen for ikke å gjenbruke adresser i BTCPay Server, er det vanlig å se mange utløpte fakturaer på fakturasiden til butikken din. For å skjule dem fra visningen din, velg dem i listen og merk dem som arkivert. Fakturaer som har blitt merket som arkivert, slettes ikke. Betaling til en arkivert faktura vil fortsatt bli oppdaget av din BTCPay Server (betaltSent-status). Du kan se butikkens arkiverte fakturaer når som helst ved å velge arkiverte fakturaer fra nedtrekksfilteret for søk.

#### Standardvaluta

Butikkens standardvaluta, dette ble satt ved opprettelsesveiviseren for butikken

#### Tillat hvem som helst å opprette faktura

Du bør aktivere dette alternativet hvis du ønsker å tillate omverdenen å opprette fakturaer i butikken din. Dette alternativet er kun nyttig hvis du bruker betalingsknappen eller hvis du utsteder fakturaer via API eller tredjeparts HTML-nettsted. PoS-appen er forhåndsgodkjent og trenger ikke dette aktivert for at en tilfeldig besøkende skal kunne åpne din PoS-butikk og opprette en faktura.

#### Legg til ekstra avgift (nettverksavgift) til faktura

- Kun hvis kunden gjør mer enn én betaling for fakturaen
- Ved hver betaling
- Aldri legg til nettverksavgift

#### Faktura utløper hvis det fulle beløpet ikke er betalt etter .. Minutter.
Fakturatimeren er satt til 15 minutter som standard. Timeren er en beskyttelsesmekanisme mot volatilitet siden den låser kryptovalutamengden i henhold til krypto-til-fiat-kursene. Hvis kunden ikke betaler fakturaen innen den definerte perioden, anses fakturaen som utløpt. Fakturaen anses som "betalt" så snart transaksjonen er synlig på blokkjeden (0-bekreftelser), men anses som "fullført" når den når antall bekreftelser handelsmannen har definert (vanligvis 1-6). Timeren er tilpassbar.
#### Vurder fakturaen som betalt selv om det betalte beløpet er ..% mindre enn forventet.

I en situasjon der en kunde bruker en utvekslingslommebok for å betale direkte for en faktura, tar utvekslingen et lite gebyr. Dette betyr at en slik faktura ikke anses som fullstendig fullført. Fakturaen får status "delvis betalt". Hvis en handelsmann ønsker å akseptere underbetalte fakturaer, kan du sette prosentsatsen her

### Forespørsler

Betalingsforespørsler er en funksjon som lar eiere av BTCPay-butikker opprette langvarige fakturaer. Midler betales til en betalingsforespørsel ved hjelp av vekslingskursen på betalingstidspunktet. Dette lar brukere gjøre betalinger etter eget ønske uten å forhandle eller verifisere vekslingskurser med butikkeieren på betalingstidspunktet.

Brukere kan betale forespørsler i delbetalinger. Betalingsforespørselen forblir gyldig til den er betalt i sin helhet, eller hvis butikkeieren krever en utløpstid. Adresser gjenbrukes aldri. En ny adresse genereres hver gang brukeren klikker betal for å opprette en faktura for betalingsforespørselen.

Butikkeiere kan skrive ut betalingsforespørsler (eller eksportere fakturadata) for regnskapsføring og bokføring. BTCPay merker automatisk fakturaer som Betalingsforespørsler i butikkens fakturaliste.

#### Tilpass dine betalingsforespørsler

- Fakturabeløp - Sett forespurt betalingsbeløp
- Valuta - Vis forespurt beløp i Fiat eller Kryptovaluta
- Betalingsmengde - Tillat kun enkelbetalinger eller delbetalinger
- Utløpstid - Tillat betalinger til en dato eller uten utløp
- Beskrivelse - Tekstredigerer, Datatabeller, Integrer Bilder & Videoer
- Utseende - Farge og stil med CSS-temaer

![bilde](assets/en/93.webp)

#### Opprett en betalingsforespørsel

I venstremenyen, gå til Betalingsforespørsel og klikk "Opprett Betalingsforespørsel".

![bilde](assets/en/94.webp)

Oppgi Forespørselsnavn, Beløp, Visningsvaluta, Tilhørende Butikk, Utløpstid & Beskrivelse (Valgfritt)

Velg alternativet Tillat betaler å opprette fakturaer i deres valuta hvis du ønsker å tillate delbetalinger.

Klikk Lagre & Vis for å se gjennom betalingsforespørselen din.

BTCPay oppretter en URL for betalingsforespørselen. Del denne URL-en for å vise betalingsforespørselen din. Trenger du flere av samme forespørsel? Du kan duplisere betalingsforespørsler ved å bruke Klon-alternativet i hovedmenyen.

![bilde](assets/en/95.webp)

**ADVARSEL**

Betalingsforespørsler er butikkavhengige, noe som betyr at hver betalingsforespørsel er assosiert med en butikk under opprettelsen. Sørg for å ha en lommebok koblet til butikken din som betalingsforespørselen tilhører.

#### Betalt forespørsel

Betalere og forespørrere kan se statusen for betalingsforespørselen etter å ha sendt betalingen. Statusen vil vises som Avregnet hvis betalingen er mottatt i sin helhet. Hvis det kun ble gjort delbetalinger, vil Gjenværende beløp vise saldoen som skyldes.

![bilde](assets/en/96.webp)

#### Tilpass betalingsforespørsler

Innholdet i beskrivelsen kan redigeres ved hjelp av betalingsforespørselens tekstredigerer. Begge alternativene er tilgjengelige hvis du ønsker å bruke ekstra fargetemaer eller egendefinert CSS-styling.

Ikke-tekniske brukere kan bruke et [bootstrap-tema](https://docs.btcpayserver.org/Development/Theme/#2-bootstrap-themes). Ytterligere tilpasning kan gjøres ved å gi ekstra CSS-kode, som vist nedenfor.

```css
```css
:root {  --btcpay-font-family-base: "Source Sans Pro", -apple-system,
    BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --btcpay-primary: #7d4698;
  --btcpay-primary-accent: #59316b;
  --btcpay-body-text: #333a41;
  --btcpay-body-bg: #fff;
  --btcpay-bg-tile: #f8f9fa;
}

#mainNav {
  color: white;
  background: lineær-gradient(#59316b, #331840);
}

#mainNav .btn-link {
  color: white;
}
```

### Uttrekkspayments

Tradisjonelt deler en mottaker sin Bitcoin-adresse for å gjøre en Bitcoin-betaling, og senderen sender senere penger til denne adressen. Et slikt system kalles Push-betaling, ettersom senderen initierer betalingen mens mottakeren kan være utilgjengelig, og skyver betalingen til mottakeren.

Men, hva med å snu rollene?

Hva om, i stedet for at en sender skyver betalingen, tillater senderen mottakeren å trekke betalingen når mottakeren finner det passende? Dette er konseptet med en Uttrekkspayment. Dette tillater flere nye applikasjoner, som:

- Et abonnementstjeneste (hvor abonnenten tillater tjenesten å trekke penger hver x mengde tid)
- Refusjoner (hvor handelsmannen tillater kunden å trekke refusjonspengene til sin lommebok når de finner det passende)
- Tidsbasert fakturering for frilansere (hvor personen som ansetter tillater frilanseren å trekke penger til sin lommebok ettersom tid rapporteres)
- Patronasje (hvor patronen tillater mottakeren å trekke penger hver måned for å fortsette å støtte deres arbeid)
- Automatisk salg (hvor en kunde av en børs ville tillate en børs å trekke penger fra deres lommebok for å selge automatisk hver måned)
- Balanseuttakssystem (hvor en tjeneste med høyt volum tillater brukere å be om uttak fra deres saldo, tjenesten kan da enkelt samle alle utbetalingene til mange brukere på faste intervaller)

### Utbetalinger

Utbetalingsfunksjonaliteten er knyttet til [Uttrekkspayments](https://docs.btcpayserver.org/PullPayments/). Denne funksjonen lar deg opprette utbetalinger innenfor din BTCPay. Denne funksjonen lar deg behandle uttrekkspayment (refusjoner, lønnsutbetalinger, eller uttak).

#### Eksempel 1: Refusjon

La oss starte med refusjonseksemplet. Kunden har kjøpt en vare i butikken din, men må dessverre returnere varen. De ønsker en refusjon. Innen BTCPay, kan du opprette en [Refusjon](https://docs.btcpayserver.org/Refund/) og gi kunden en lenke for å kreve pengene sine. Når kunden har oppgitt sin adresse og krevd pengene, vil det vises i Utbetalinger.

Den første statusen den har er Venter på Godkjenning. Butikkansatte kan sjekke om flere venter, og etter å ha gjort utvalget, bruker du Handlingsknappen.

Alternativer på handlingsknappen

- Godkjenn valgte utbetalinger
- Godkjenn & send valgte utbetalinger
- Avbryt valgte utbetalinger

Neste steg er å Godkjenn & send valgte utbetalinger ettersom vi ønsker å refundere kunden. Sjekk Kundens Adresse, viser beløpet og om vi ønsker at gebyrer skal trekkes fra refusjonen eller ikke. Når du har gjort sjekkene, er det bare å signere transaksjonen som gjenstår.

Kunden blir nå oppdatert på Krav-siden. Han kan følge transaksjonen ettersom han er gitt en lenke til en blokkutforsker og hans transaksjon. Når transaksjonen har blitt bekreftet, og statusen endres til Fullført.

#### Eksempel 2: Lønn
La oss nå se på utbetaling av lønn, ettersom dette drives fra innsiden av butikken og ikke per kundens forespørsel. Grunnlaget er det samme; det bruker Pull-betalinger. Men i stedet for å opprette en refusjon, vil vi lage en [Pull Payment](https://docs.btcpayserver.org/PullPayments/).
Gå til Pull Payments-fanen i din BTCPay-server. Øverst til høyre, klikk på Opprett Pull Payment-knappen.

Nå er vi i opprettelsen av utbetalingen, gi den et navn og ønsket beløp i ønsket valuta, fyll ut beskrivelsen, så ansatte vet hva det handler om. Den neste delen er lik refusjoner. Den ansatte fyller ut mottaksadressen og beløpet han ønsker å kreve fra denne utbetalingen. Han kan bestemme seg for å gjøre det til 2 separate krav, til forskjellige adresser, eller til og med delvis kreve over lynnettet.

Hvis det er flere ventende utbetalinger, kan du samle disse for å bli signert og sendt ut. Når signert, flytter utbetalingene til fanen Pågår og viser transaksjonen. Når den er akseptert av nettverket, flytter utbetalingen til fanen Fullført. Fanen Fullført er rent for historiske formål. Den holder de bearbeidede utbetalingene og transaksjonen som tilhører den.

### Pull-betalinger

#### Konsept

Når en avsender konfigurerer en Pull-betaling, kan de konfigurere en rekke egenskaper:

- Navn på Pull-forespørsel
- Et grensebeløp
- En enhet (som BTC, SAT, USD)
- Betalingsmetoder
  - BTC On-chain
  - BTC Off-chain
- Beskrivelse
- Egendefinert CSS
- Sluttdato (valgfritt for Lightning Network BOLT11)

Etter dette kan avsenderen dele pull-betalingen ved hjelp av en lenke med mottakeren, som tillater mottakeren å opprette en utbetaling. Mottakeren vil velge sin utbetaling:

- Hvilken betalingsmetode å bruke
- Hvor pengene skal sendes

Når en utbetaling er opprettet, vil den telle mot pull-betalingens grense for gjeldende periode. Avsenderen vil deretter godkjenne utbetalingen ved å sette raten som utbetalingen vil bli sendt og fortsette med betaling.

For avsenderen tilbyr vi en enkel-å-bruke måte å samle betalingen av flere utbetalinger fra [BTCPay Intern Lommebok](https://docs.btcpayserver.org/Wallet/).

#### Greenfield API

BTCPay Server tilbyr et fullstendig API til både avsender og mottaker som er dokumentert på `/docs`-siden av din instans. (eller på dokumentasjonsnettstedet https://docs.btcpayserver.org)

Siden vårt API eksponerer full kapasitet av pull-betalinger, kan en avsender automatisere betalinger etter egne behov.

### Ferdighetssammendrag

I denne delen lærte du følgende:

- Dyp forståelse av BTCPay Servers fakturastatus samt handlinger som kan utføres på dem
- Tilpasse og administrere forlenget levetid fakturamekanismer kjent som Forespørsler.
- De ytterligere fleksible betalingsmulighetene som åpnes med BTCPay Servers unike Pull Payment-funksjon, spesielt hvordan håndtere refusjoner og lønnsutbetalinger.

### Kunnskapsvurdering

#### KA Konseptuell Gjennomgang

Hva er noen forskjeller mellom fakturaer og betalingsforespørsler, og hva kan være en god grunn til å bruke sistnevnte?

#### KA Konseptuell Gjennomgang

Hvordan utvider pull-betalinger på det som typisk kan gjøres on-chain? Beskriv noen bruksområder de muliggjør.

## BTCPay Server Standard Plugins

<chapterId>7d673dc4-bd5d-5411-819b-f135f1d86636</chapterId>

### Standard Plugins og Apper
BTCPay-serveren kommer med et standard sett med Plugins (Apps) som kan gjøre BTCPay Server til en e-handelsbetalingsportal. Med tillegg av et Point Of Sale, Crowdfund-plattform, og en enkel Betal-knapp, blir BTCPay Server en enkel-å-implementere løsning.
### Point Of Sale

En av de standard Plugins i BTCPay Server er Point of Sale (PoS). Med PoS-pluginen kan en butikkeier opprette en Webshop direkte fra BTCPay Server, butikkeieren trenger ikke tredjeparts e-handelsløsninger for å drive en Webshop. Den nettbaserte PoS-appen lar brukere med fysiske butikker lett akseptere Bitcoin, uten gebyrer eller en tredjepart, direkte til deres lommebok. PoS kan enkelt vises på nettbrett eller andre enheter som støtter nettsurfing. Brukere kan enkelt opprette en hjemmeskjermsnarvei for rask tilgang til webappen.

#### Hvordan opprette et nytt Point of Sale

BTCPay Server lar butikkeiere raskt opprette et Point of Sale i flere oppsett. BTCPay Server anerkjenner at ikke hver butikk er e-handel, og ikke hver butikk er en bar eller restaurant, og den kommer med flere standardoppsett for din PoS.

Når butikkeieren klikker på "Point of Sale" i hans venstre menylinje, vil BTCPay Server nå be om et navn; dette navnet vil være synlig i venstre menylinje. Klikk Opprett for å lage PoS.

![bilde](assets/en/97.webp)

#### Oppdater nyopprettet Point of Sale

Etter å ha opprettet et nytt PoS, vil den følgende skjermen være for å oppdatere ditt Point of Sale og legge til varer for butikken din.

##### App-navn

Navnet gitt her til ditt Point of Sale vil være synlig i hovedmenyen til BTCPay Server.

##### Visningstittel

Publikum vil se den offentlige tittelen eller navnet når de besøker butikken din. BTCPay Server navngir som standard butikken din “Tea shop”. Erstatt dette med din butikks navn.

![bilde](assets/en/98.webp)

#### Velg Point of Sale-stil

BTCPay Server er i stand til å vise sitt Point Of Sale på flere måter.

- Produktliste
  - En butikkvisning hvor kunder kun kan kjøpe 1 produkt om gangen.
- Produktliste med en handlekurv.
  - En butikkvisning hvor kunder kan kjøpe flere varer samtidig og få en handlekurvoversikt til høyre på skjermen sin.
- Kun tastatur
  - Ingen produktliste, bare et tastatur for direkte fakturering.
- Skriv ut visning (Utskrivbar produktliste med QR)
  - Hvis du ikke alltid kan vise produktlisten din digitalt, trenger du en "offline" løsning for produkter; BTCPay Server har en utskriftsvisning som fungerer som en Offline-butikk.

![bilde](assets/en/99.webp)

#### Point Of Sale-stil - Produktliste

![bilde](assets/en/100.webp)

#### Point Of Sale-stil - Produktliste + Handlekurv

![bilde](assets/en/101.webp)

#### Point Of Sale-stil - Kun tastatur

![bilde](assets/en/102.webp)

#### Point Of Sale-stil - Skriv ut visning

![bilde](assets/en/103.webp)

#### Valuta

Butikkeieren kan sette en annen valuta for sitt Point of Sale enn hans generelt innstilte standardvaluta. Butikkens standardvaluta vil automatisk fylle ut dette feltet.

#### Beskrivelse

Fortell verden om butikken din; hva selger du, og for hvor mye? Alt som forklarer butikken din går her.

![bilde](assets/en/104.webp)

#### Produkter
Når et Salgspunkt blir opprettet, legger en standard BTCPay Server til et par varer i butikken for referanse. Klikk på Rediger-knappen på noen av de standard varene for å bedre forstå hver mulige valgmulighet for en vare.

Å opprette et nytt produkt i butikken din består av følgende felt;

- Tittel
- Pris (fast, minimum, eller tilpasset)
- Bilde-URL
- Beskrivelse
- Lagerbeholdning
- ID
- Kjøp-knapp Tekst
- Aktiver/Deaktiver

Når butikkeieren har fylt ut alle de nye produktfeltene, klikk på lagre, og du vil legge merke til at Produktseksjonen i Salgspunktet nå blir fylt opp. Sørg alltid for å lagre øverst til høyre på skjermen din for å forhindre at butikkeiere kan miste fremgangen sin på å legge til produkter.

Butikkeiere kan også bruke "Råredigereren" for å konfigurere produktene sine. Råredigereren krever en grunnleggende forståelse av JSON-strukturer.

![bilde](assets/en/105.webp)

#### Kasse

BTCPay Server tillater små tilpasninger av kassen spesifikt for PoS. Butikkeieren kan sette teksten "Kjøp for x" eller be om spesifikk kundeinformasjon ved å legge til skjemaer.

#### Tips

Ikke alle butikker trenger alternativet for Tips på salgene sine. Butikkeiere kan veksle dette av eller på som de finner passende for butikken sin. Hvis butikken bruker tips vekslet på, kan butikkeieren sette teksten i feltet for tips de liker. BTCPay Server-tips fungerer basert på en prosentandel. Butikkeiere kan legge til flere prosentandeler med komma separasjon.

#### Rabatter

Som butikkeier, ønsker du kanskje å gi kunden en tilpasset rabatt ved kassen; vekslingen for Rabatter blir tilgjengelig ved kassen i butikken din. Dette er imidlertid sterkt frarådet mot selvbetjeningssystemer.

#### Tilpassede Betalinger

Når alternativet for Tilpassede Betalinger er vekslet på, får kunden muligheten til å angi sin egen pris lik eller høyere enn den opprinnelige fakturaen generert av butikken.

#### Tilleggsvalg

Etter å ha satt opp alt for ditt Salgspunkt, er det noen ekstra valg igjen. Butikkeiere kan enkelt integrere sitt PoS gjennom en Iframe eller integrere en betalingsknapp som lenker til et spesifikt butikkprodukt. For å stilisere den nettopp opprettede PoS-butikken, kan eiere legge til tilpasset CSS nederst i tilleggsvalgene.

#### Slett denne appen

Hvis butikkeieren ønsker å fullstendig slette Salgspunktet fra sin BTCPay Server, nederst ved oppdatering av PoS, kan butikkeiere klikke på Slett denne appen-knappen for å fullstendig ødelegge sin PoS-app. Når du klikker på "Slett denne appen", vil BTCPay Server be om bekreftelse ved å skrive `DELETE` og bekrefte ved å klikke på Slett-knappen. Etter sletting returnerer butikkeieren til BTCPay Server-dashboardet.

### BTCPay Server - Crowdfund

Ved siden av Salgspunkt-pluginen, har BTCPay Server muligheten til å opprette en folkefinansiering. Akkurat som enhver annen Crowdfund-plattform, kan butikkeiere sette et mål, opprette fordeler for bidrag, og tilpasse det etter deres behov.

#### Hvordan sette opp en ny folkefinansiering

Klikk på Crowdfund-pluginen gjennom hovedmenyen til venstre på din BTCPay Server, under Plugin-seksjonen. BTCPay Server vil nå be om et navn for folkefinansieringen; dette navnet vil også bli vist i venstre menylinje.

![bilde](assets/en/106.webp)

#### Oppdater nyopprettet Salgspunkt

Når Appen er gitt et navn, vil neste skjerm være å oppdatere Appen for å ha kontekst.

#### App-navn

Navnet gitt til din Crowdfund vil være synlig i hovedmenyen til BTCPay Server.

#### Visningstittel

Tittelen gitt til folkefinansieringen for offentligheten.
#### Tagline
Gi innsamlingsaksjonen en slagord for å gjenkjenne hva innsamlingen handler om.

![bilde](assets/en/107.webp)

#### Fremhevet bilde-URL

Hver innsamlingsaksjon har sitt hovedbilde, det ene banneret du direkte gjenkjenner. Dette bildet kan lagres på serveren din hvis du har administrative rettigheter, administratorer kan laste opp under BTCPay Server-innstillingene - Filer. Når du er en butikkeier, må bildet lastes opp på nettet gjennom en tredjepartsvert (for eksempel imgur)

#### Gjør innsamlingsaksjonen offentlig

Denne bryteren gjør innsamlingsaksjonen din offentlig og dermed synlig for omverdenen. For testformål eller for å se om temaet ditt er anvendt korrekt, kan man ønske å holde dette satt til AV i perioden med å bygge innsamlingsaksjonen.

#### Beskrivelse

Fortell verden om innsamlingsaksjonen din, hva samler du inn til? Alt som forklarer innsamlingsaksjonen din går her.

![bilde](assets/en/108.webp)

#### Innsamlingsmål

Sett et mål for hva innsamlingsaksjonen skal tjene til prosjektet og hvilken valuta målet skal være i. Sørg for at hvis målene dine er satt mellom datoer, inkluder disse mål- og sluttdatoene under Mål i innsamlingsaksjonen.

![bilde](assets/en/109.webp)

#### Fordeler

Fordeler hjelper mye med din crowdfunding. Dette er fordi fordeler gir folk en måte å delta i kampanjen din på. De spiller på både egoistiske motivasjoner så vel som velgjørende motivasjoner. Og de lar deg få tilgang til dine støttespilleres utgifter, ikke bare deres filantropiske lommebok -- du kan gjette hvilken som er mer betydelig.

Å opprette en ny fordel består av følgende felt;

- Tittel
- Pris (fast, minimum eller tilpasset)
- Bilde-URL
- Beskrivelse
- Lager
- ID
- Kjøp-knapp-tekst.
- Aktiver/Deaktiver

Når butikkeieren har fylt ut alle feltene for den nye fordelen, klikk på lagre, og du vil legge merke til at Fordel-seksjonen i innsamlingsaksjonene nå blir befolket.

![bilde](assets/en/110.webp)

### BTCPay Server - Point Of Sale

#### Bidrag

Butikkeiere kan velge hvordan de vil vise Fordeler, hvordan de er sortert, eller til og med rangert mot de andre fordelene. Imidlertid, når målene for innsamlingsaksjonen er nådd, kan butikkeieren ønske å stoppe donasjoner som strømmer mot denne innsamlingen. Derfor kan han veksle på "Ikke tillat ytterligere bidrag etter å ha nådd målet". Dette vil stoppe innsamlingsaksjonen fra å akseptere donasjoner.

##### Innsamlingsaksjonens oppførsel

Innsamlingsaksjonens standard teller kun fakturaer opprettet med innsamlingsaksjonen mot målet. Det kan imidlertid være tilfeller der butikkeieren ønsker at alle fakturaer laget i denne butikken skal telle mot innsamlingsaksjonen.

#### Tilleggsvalg for tilpasning

BTCpay Server tilbyr et par ekstra tilpasninger. Legg til lyder, animasjoner eller til og med diskusjonstråder til innsamlingsaksjonen. Butikkeiere kan også endre utseendet og følelsen av innsamlingsaksjonen ved å legge inn sin egen tilpassede CSS.

#### Slett denne appen

Hvis butikkeieren ønsker å fullstendig slette innsamlingsaksjonen fra sin BTCPay Server, kan butikkeiere klikke på "Slett denne appen"-knappen nederst ved oppdatering av innsamlingsaksjonen for å fullstendig ødelegge innsamlingsaksjonsappen sin. Når du klikker på "Slett denne appen", vil BTCPay Server be om bekreftelse ved å skrive `SLETT` og bekrefte ved å klikke på Slett-knappen. Etter sletting returnerer butikkeieren til BTCPay Server-dashboardet.

### BTCPay Server - Betalingsknapp
Enkelt integrerbare HTML- og svært tilpassbare betalingsknapper lar butikkeiere motta tips og donasjoner. I venstre menylinje på BTCPay Server, under seksjonen for Plugins, kan butikkeiere klikke på "Pay Button" og klikke Aktiver for å opprette en betalingsknapp.

#### Generelle Innstillinger

Innenfor de generelle innstillingene for betalingsknappen, kan butikkeiere sette

- Standardpris
- Standardvaluta
- Standard betalingsmetode
  - Bruk butikkens standard
  - BTC on-chain
  - BTC Off-chain (Lightning)
  - BTC Off-chain (LNURL-pay)
- Beskrivelse ved utsjekking
- Ordre-ID

#### Visningsalternativer

BTCPay Servers betalingsknapp kan konfigureres for å passe ulike stiler. Knapper kan ha et fast eller tilpasset beløp, enten vist med en skyvekontroll eller pluss og minus veksler.

#### Bruk Modal

Når de oppretter betalingsknappen, kan butikkeiere velge dens oppførsel når en kunde klikker på den og vise den i en modal eller som en ny side.

**!?Merk!?**

Advarsel: Betalingsknappen bør kun brukes for tips og donasjoner

Bruk av betalingsknappen for e-handelsintegrasjoner anbefales ikke siden ordre relevant informasjon kan endres av brukeren. For e-handel bør du bruke vår Greenfield API. Hvis denne butikken behandler kommersielle transaksjoner, råder vi deg til å opprette en separat butikk før du bruker betalingsknappen.

#### Tilpass tekst på betalingsknapp

Som standard sier BTCPay Servers betalingsknapp "Pay With BTCPay". Butikkeiere kan sette denne teksten etter ønske og endre BTCPay Server-logoen til sin egen. Sett teksten ved å bruke "Pay Button Text" og lim inn bilde-URL-en under "Pay Button Image URL".

##### Bildets størrelse

Størrelsen på bildet i knappen kan kun settes til tre standarder.

- 146x40px
- 168x46px
- 209x57px

#### Knappetype

BTCPay Server kjenner til tre tilstander for betalingsknappen.

- Fast beløp
  - Den tidligere angitte prisen er i knappens generelle innstillinger.
- Tilpasset beløp
  - BTCPay Servers betalingsknapp har + og - veksler for å sette en tilpasset pris.
  - Når du bruker tilpasset beløp, vil BTCPay Server be om et Min, Maks, og hvor gradvis det skal øke.
  - Knapper kan settes til "Bruk enkel inntastingsstil". Dette fjerner +/- vekslerne.
  - Tilpass knappen inline hvor knappen og vekslerne vises på linje.
- Skyvekontroll
  - Lignende til tilpasset beløp, men visuelt forskjellig da den har en skyvekontroll i stedet for +/- vekslerne.
  - Når du bruker Skyvekontrollen, vil BTCPay Server be om et Min, Maks, og hvor gradvis det skal øke.

**!?Merk!?**

Sletting av betalingsknappen kan gjøres øverst i advarselsbeskrivelsen.

#### Betalingsvarsler

Server IPN (Instant Payment Notification) er ment for webhooks og kan fylles ut med en URL for å poste kjøpsdata.

#### E-postvarsler

Når betaling har skjedd, kan BTCPay Server varsle butikkeieren.

#### Nettleseromdirigering

Når kunden fullfører kjøpet, vil han bli omdirigert til denne lenken hvis satt av butikkeieren.

#### Avanserte alternativer for betalingsknapp

Spesifiser ekstra spørringsstrengparametere som skal legges til utsjekkingssiden når fakturaen er opprettet. For eksempel, `lang=da-DK` ville laste utsjekkingssiden på dansk som standard.

#### Bruk App som Endepunkt

Lenk direkte betalingsknappen til et element i en av PoS- eller Crowdfund-appene før.
Butikkeiere kan klikke på rullegardinmenyen og velge ønsket App; når Appen er valgt, kan butikkeieren legge til varen som skal lenkes.
#### Generert Kode

Siden BTCPay Servers betalingsknapp er lett-inkluderbar HTML, viser BTCPay Server den genererte koden for å kopiere inn på en nettside nederst etter at betalingsknappen er konfigurert.

Butikkeiere kan kopiere den genererte koden inn på sin nettside, og betalingsknappen fra BTCPay Server er direkte aktiv på deres nettside.

#### Betalingsvarsler

Server IPN (Instant Payment Notification) er ment for webhooks og kan fylles ut med en URL for å poste kjøpsdata.

#### E-postvarsler

Når en betaling har skjedd, kan BTCPay Server varsle butikkeieren.

#### Nettleseromdirigering

Når kunden fullfører kjøpet, vil han bli omdirigert til denne lenken hvis den er satt av butikkeieren.

#### Avanserte Betalingsknapp Alternativer

Spesifiser ekstra spørringsstrengparametere som skal legges til på betalingssiden når fakturaen er opprettet. For eksempel, `lang=da-DK` ville laste betalingssiden på dansk som standard.

#### Bruk App som Endepunkt

Lenk direkte betalingsknappen til en vare i en av PoS- eller Crowdfund-appene ovenfor. Butikkeiere kan klikke på rullegardinmenyen og velge ønsket app, når appen er valgt, kan butikkeieren legge til varen som skal lenkes.

#### Generert Kode

Siden BTCPay Servers betalingsknapp er lett-inkluderbar HTML, viser BTCPay Server den genererte koden for å kopiere inn på en nettside nederst etter at betalingsknappen er konfigurert. Butikkeiere kan kopiere den genererte koden inn på sin nettside og betalingsknappen fra BTCPay Server er direkte aktiv på deres nettside.

### Ferdighetssammendrag

I denne seksjonen lærte du:

- Hvordan bruke BTCPay Servers integrerte PoS-plugin for å enkelt opprette en tilpasset butikk
- Hvordan bruke BTCPay Servers integrerte Crowdfund-plugin for å enkelt opprette en tilpasset crowdfund-app
- Generere kode for en tilpasset betalingsknapp ved hjelp av Pay Button-plugin

### Kunnskapsvurdering

#### KA Gjennomgang

Hva er de tre innebygde pluginene som kommer standard med BTCPay Server? Beskriv med noen få ord hvordan hver kan brukes.

# Konfigurering av BTCPay Server

<partId>ff38596c-7de3-5e5c-ba50-9b9edbbbb5eb</partId>

## Grunnleggende forståelse av installasjon av BTCPay Server på et LunaNode-miljø

<chapterId>d0a28514-ffcf-529b-9156-29141f0b060a</chapterId>

### Installere BTCPay Server på Hosted Env. (LunaNode)

Disse stegene vil gi all informasjonen som er nødvendig for å begynne å bruke BTCPay Server på LunaNode. Det er mange alternativer for hvordan programvaren kan distribueres.
Du kan finne alle detaljene om BTCPay Server på https://docs.btcpayserver.org.

#### Hvor starter vi?

I denne delen vil du gjøre deg kjent med LunaNode som hostingleverandør, lære om de første stegene for å bruke din BTCPay Server, og lære hvordan du går frem med Lightning Network. Etter at vi har gått gjennom alle stegene, kan du drive en nettbutikk eller crowdfund-plattform som aksepterer Bitcoin!

Dette er en av mange måter å distribuere BTCPay Server på. Les vår dokumentasjon for flere detaljer,

https://docs.btcpayserver.org.

### BTCPay Server - LunaNode-distribusjon

#### LunaNode-distribusjon
Først, gå til nettsiden til LunaNode.com, hvor vi vil opprette en ny konto. Klikk på "Sign Up" øverst til høyre eller bruk "Get Started"-veiviseren på hjemmesiden deres.
![bilde](assets/en/111.webp)

Etter at du har opprettet din nye konto, sender LunaNode en verifiseringsepost. Når du har verifisert kontoen, sammenlignet med Voltage, blir du umiddelbart presentert for å fylle opp kontosaldoen din. Denne saldoen er nødvendig for å betale for serverplass og hostingkostnader.

![bilde](assets/en/112.webp)

#### Legg til kreditt på din LunaNode-konto

Når du har klikket på "Deposit credit", får du muligheten til å sette hvor mye du ønsker å fylle opp kontoen din med og hvordan du ønsker å betale for det. LunaNode og BTCPay Server vil koste mellom 10$USD og 20$USD per måned.
Sammenlignet med Voltage.cloud, får du full tilgang til din Virtual Private Server (VPS fra nå av) og derfor har du litt mer kontroll over serveren din. Etter at du har opprettet din nye konto, sender LunaNode en verifiseringsepost.
Når du har verifisert kontoen, sammenlignet med Voltage, blir du nå umiddelbart presentert for å fylle opp kontosaldoen din. Denne saldoen er nødvendig for å betale for serverplass og hostingkostnader.

#### Hvordan distribuere en ny server?

I denne guiden vil vi gå gjennom oppsettet ved å opprette et sett med API-nøkler og bruke BTCPay Server-lanseringen laget av LunaNode.

På LunaNode-dashboardet ditt, klikk på API øverst til høyre. Dette åpner en ny side. Vi trenger bare å sette et navn for API-nøkkelen. Resten vil bli tatt hånd om av LunaNode og vil ikke bli dekket i denne guiden. Klikk på knappen "Create API Credential".
Etter å ha opprettet API-legitimasjonen, får du en lang streng med bokstaver og tegn. Dette er din API-nøkkel.

![bilde](assets/en/113.webp)

#### Hvordan distribuere en ny server?

Det er 2 deler til disse legitimasjonene, API-nøkkel og API-ID; vi trenger begge. Før vi går til neste steg, la oss åpne en ny fane i nettleseren og gå til https://launchbtcpay.lunanode.com/

Her vil du bli bedt om å oppgi din API-nøkkel og API-ID. Dette er for å verifisere at det er du som setter opp denne nye serveren. API-nøkkelen bør fortsatt være åpen i forrige fane; hvis du ruller ned i tabellen nedenfor, vil du finne API-ID-en.

Gå tilbake til siden med Launcher, fyll ut feltene med din API-nøkkel og ID, og klikk på fortsett.

![bilde](assets/en/114.webp)

I neste steg kan du oppgi et domenenavn. Hvis du allerede eier et domene og ønsker å bruke dette for BTCPay Server, sørg for at du også legger til DNS-posten (kalt en `A`-post) på domenet ditt. Hvis du ikke eier et domene, bruk domenet som tilbys av LunaNode i stedet (du kan endre dette senere i BTCPay Server-innstillingene) og klikk Fortsett.

Les mer om å sette eller endre en DNS-post for BTCPay Server; https://docs.btcpayserver.org/FAQ/Deployment/#how-to-change-your-btcpay-server-domain-name

#### Lanser BTCPay Server på LunaNode

Etter å ha tatt stegene før dette, kan vi sette alle alternativene for vår nye server. Her vil vi velge Bitcoin (BTC) som vår støttede valuta; vi kan sette en e-post for å få varsler om fornyelse av krypteringssertifikater; dette er ikke obligatorisk.
Denne veiledningen tar sikte på å sette opp et Mainnet-miljø (ekte Bitcoin-verden); imidlertid tillater LunaNode deg også å sette dette til Testnet eller Regtest for utviklingsformål. Vi vil la den stå på Mainnet-alternativet for denne veiledningen.
Velg din Lightning-implementering. LunaNode tilbyr to forskjellige implementeringer, LND og Core Lightning. For denne veiledningen vil vi ta LND. Det er små, men sanne forskjeller i begge implementeringene; for mer om dette, anbefaler vi å lese den omfattende dokumentasjonen; https://docs.btcpayserver.org/LightningNetwork#getting-started-with-btcpay-server-and-core-lightning-cln

![bilde](assets/en/115.webp)

LunaNode tilbyr flere Virtual Machine (VM)-planer. Disse varierer i prisområder og spesifikasjoner for serveren. For denne veiledningen vil en m2-plan være tilstrekkelig; imidlertid, hvis du har merket av for mer enn bare Bitcoin som valuta, vurder å bruke minst m4.

Akselerer den innledende blokkjedesynkroniseringen; dette er valgfritt og avhenger av dine behov. Det er avanserte alternativer som å sette en Lightning Alias, peke til en spesifikk GitHub-utgivelse, eller sette SSH-nøkler; ingen av disse vil bli berørt i denne veiledningen.

Etter å ha fylt ut skjemaet, må du klikke på Launch VM, og Lunanode vil starte opprettingen av din nye VM, inkludert BTCPay Server installert på den. Denne prosessen tar et par minutter; når serveren din er klar, gir LunaNode deg lenken til din nye BTCPay Server.

Etter opprettelsesprosessen, klikk på lenken til din BTCPay Server; her vil du bli bedt om å opprette en Administrator-konto.

![bilde](assets/en/116.webp)

### Ferdighetssammendrag

I denne delen lærte du:

- Å opprette og finansiere en konto på LunaNode
- Bruke BTCPay Server Launcher for å opprette din egen server

### Kunnskapsvurdering

#### KA Konseptuell Gjennomgang

Beskriv noen av forskjellene mellom å kjøre en instans av BTCPay Server på en VPS kontra å opprette en konto på en hostet instans.

## Installere BTCPay Server på et Voltage-miljø

<chapterId>11c7d284-b4d2-5542-872c-df9bd9c1491b</chapterId>

Du vil bli kjent med Voltage.cloud som vertstjenesteleverandør, lære om de første stegene for å bruke din BTCPay Server, og lære hvordan du går frem med Lightning Network. Etter at vi har gått gjennom alle stegene, kan du drive en nettbutikk eller en crowdfunding-plattform som aksepterer Bitcoin!

Dette er en av mange måter å distribuere BTCPay Server på. Les vår dokumentasjon for flere detaljer,
https://docs.btcpayserver.org.

### BTCPay Server - Voltage.cloud-utrulling

Først, gå til nettsiden Voltage.cloud og registrer deg for en ny konto. Når du oppretter en konto kan du melde deg på en 7 dagers gratis prøveperiode. Enten klikk på Sign Up øverst til høyre eller bruk "Prøv en gratis 7 dagers prøveperiode" på hjemmesiden deres.

![bilde](assets/en/117.webp)

Etter at du har opprettet en konto, klikk på `NODES`-knappen på dashbordet ditt. Når vi har valgt Noder og opprettet en ny node, blir vi presentert med de mulige nodene Voltage tilbyr. Siden denne veiledningen også vil gå over LightningNetwork, må vi først velge vår Lightning-implementering før vi oppretter en BTCPay Server. Klikk på LightningNode.

![bilde](assets/en/118.webp)
Her må du velge hvilken type Lightning-node du ønsker. Voltage har en rekke alternativer for ditt lynoppsett. Dette er forskjellig når du distribuerer med for eksempel LunaNode. For hensikten med denne veiledningen, vil en Lite Node være tilstrekkelig. Les mer om forskjellene på Voltage.cloud.
![bilde](assets/en/119.webp)

Gi noden din et navn, sett et passord, og sikre dette passordet. Hvis dette passordet blir mistet, mister du tilgang til dine sikkerhetskopier, og Voltage kan ikke gjenopprette det. Opprett noden, og Voltage viser deg fremgangen. Voltage har opprettet din Lightning Node. Vi kan nå opprette BTCPay Server-instansen og direkte få tilgang til Lightning-nettverket.

Klikk på Nodes øverst til venstre på dashbordet ditt. Her kan du sette opp neste del av din BTCPay Server-instans. Klikk på "opprett ny" når du er i nodenes oversikt. Du får en lignende skjerm som før. Nå i stedet for Lightning Node, velger vi BTCPay Server.

Voltage viser deg geolokasjonen til din BTCPay Server, voltage hoster i US West-regionen. Her vil du også se kostnaden for å hoste serveren. Klikk Opprett og gi din BTCPay Server et navn. Aktiver Lightning og Voltage viser deg Lightning-noden opprettet i det forrige steget. Klikk Opprett, og Voltage vil opprette en BTCPay Server-instans.

![bilde](assets/en/120.webp)

Etter at du har trykket opprett, presenterer Voltage deg med standard brukernavn og passord. Disse er lik ditt tidligere satt passord i Voltage. Klikk på Logg inn på konto-knappen for å omdirigere deg til din BTCPay Server.

Velkommen til din nye BTCPay Server-instans. Siden vi allerede har satt opp Lightning i opprettelsesprosessen, viser den deg at Lightning allerede er aktivert!

### Ferdighetssammendrag

I dette kapittelet lærte du:

- Å opprette en konto på Voltage.cloud
- Steg for å få BTCPay Server til å kjøre sammen med en Lightning-node på kontoen

### Kunnskapsvurdering

#### KA Konseptuell Gjennomgang

Hva er noen nøkkel forskjeller mellom Voltage og LunaNode oppsettene?

## Installere BTCPay Server på en Umbrel-node

<chapterId>3298e292-6476-5fe0-836c-7fa021348799</chapterId>

Ved slutten av disse stegene, kan du akseptere lynbetalinger til din BTCPay-butikk på ditt lokale nettverk. Denne prosessen vil også gjelde hvis du kjører en umbrel-node i en restaurant eller bedrift. Hvis du ønsker å koble denne butikken til et offentlig nettsted, følg den avanserte øvelsen for å eksponere din umbrel-node for offentligheten.

https://umbrel.com/

![bilde](assets/en/121.webp)

### BTCPay Server - Umbrel-distribusjon

Etter at din Umbrel-node er fullstendig synkronisert med Bitcoin-blockchainen, gå til Umbrel App Store, og søk etter BTCPay Server under Apps.

![bilde](assets/en/122.webp)

Klikk på BTCPay Server for å se App-detaljene. Når detaljene er åpne for BTCPay Server, viser nederste høyre kravene for at Appen skal kjøre ordentlig. Det viser at den krever Bitcoin og Lightning-node. Hvis du ikke har installert Lightning-noden på din Umbrel, klikk Installer. Denne prosessen kan ta et par minutter.

![bilde](assets/en/123.webp)

Etter å ha installert din lightning Node:

1. Klikk åpne i app-detaljene eller på Appen i Umbrels dashbord.
2. Klikk sett opp en ny node; du vil bli vist 24 ord for gjenoppretting av din lightning-node.
3. Skriv disse ned.

![bilde](assets/en/124.webp)
Umbrel vil be om verifisering av ordene som nettopp ble skrevet ned. Etter at Lightning-noden er satt opp, gå tilbake til Umbrel App Store og finn BTCPay Server. Klikk på installasjonsknappen, og Umbrel vil vise om de nødvendige komponentene er installert og at BTCPay Server krever tilgang til disse komponentene. Etter installasjonen, klikk Åpne i øvre høyre hjørne av appdetaljene eller åpne BTCPay Server gjennom ditt Umbrels dashbord.
Umbrel vil be om verifisering av ordene som nettopp ble skrevet ned.

![bilde](assets/en/125.webp)

**!?Merk!?**

Sørg for å lagre disse på et passende sted, slik du tidligere lærte med lagring av nøkler.

Etter at Lightning-noden er satt opp, gå tilbake til Umbrel App Store og finn BTCPay Server. Klikk på installasjonsknappen, og Umbrel vil vise om de nødvendige komponentene er installert og at BTCPay Server krever tilgang til disse komponentene.

![bilde](assets/en/126.webp)

Etter installasjonen, klikk Åpne i øvre høyre hjørne av appdetaljene eller åpne BTCPay Server gjennom ditt Umbrels dashbord.

![bilde](assets/en/127.webp)

### Ferdighetssammendrag

I denne delen lærte du:

- Stegene for å installere BTCPay Server med Lightning-funksjonalitet på en Umbrel-node

### Kunnskapsvurdering

#### KA Konseptuell Gjennomgang

Hvordan skiller oppsettet på Umbrel seg fra de to tidligere vertsalternativene?

# Konklusjon

<partId>d72e6fa5-0870-5f00-9143-9466ed22e2bd</partId>



## Evaluer kurset
<chapterId>d90bb93d-b894-551e-9fd6-6855c739a904</chapterId>
<isCourseReview>true</isCourseReview>

## Kurskonklusjon

<chapterId>c07ac2a5-f97e-5c57-8a80-4955b48128d4</chapterId>

![bilde](assets/en/128.webp)

Du bør også ha en generell forståelse av hva Bitcoin er, hvordan det fungerer, og hvordan det kan skaleres med sekundærlag som Lightning Network. I dette kurset dekket vi grundig hvordan hvem som helst kan bruke BTCPay Server, fra første installasjon til opprettelse av butikk og kompleks fakturahåndtering, for å bli en økonomisk selvstendig individ eller handelsmann.

Gratulerer med fullføringen av dette kurset. Vi håper du har likt innholdet og fortsetter å bruke og utforske BTCPay Server, og er like spent på den lovende fremtiden Bitcoin og det voksende fellesskapet av byggere og deltakere vil bringe frem som vi er.

> **FOSS er uunngåelig.**

### Ordliste

| Term                                        | Definisjon                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 51% Attack                                  | Handlingen av å bevisst bygge en ny lengste kjede av blokker for å erstatte blokker i blockchainen. Dette lar deg erstatte transaksjoner som har blitt minet inn i blockchainen. Denne typen angrep er enklest å utføre når du har flertallet av gruvekraften, derfor kalles det en "Majoritetsangrep" eller et "51% Angrep".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| AccountKey                                  | Konto nøkkelen for å rebase                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| AccountKeyPath                              | Stien fra roten til konto nøkkelen er prefikset av fingeravtrykket til den offentlige hovednøkkelen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Adresse                                     | Bitcoin-adresser kompakt koder informasjonen som er nødvendig for å betale en mottaker. En moderne adresse består av en streng med bokstaver og tall som starter med bc1 og ser ut som bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4. En adresse er en forkortelse for mottakerens låseskript, som kan brukes av en avsender for å signere over midler til mottakeren. De fleste adresser representerer enten mottakerens offentlige nøkkel eller en form for skript som definerer mer komplekse betingelser for bruk. Det foregående eksemplet er en bech32-adresse som koder et vitneprogram som låser midler til hashen av en offentlig nøkkel (Se Pay-to-Witness-Public-Key-Hash). Det finnes også eldre adresseformater som starter med 1 eller 3 som bruker Base58Check-adressekoding for å representere hash av offentlige nøkler eller skripthasher.                                                                   |
| Adresse Type                                | En adresse kan representere flere forskjellige skript. Adresser er kodet og prefikset for å formidle deres skripttype. Legacy-adresser bruker Base58, og når en legacy-adresse er hashen av en offentlig nøkkel, en såkalt P2PKH-adresse, begynner den med en ‘1’. Mindre ofte er en legacy-adresse en hash av et skript, i så fall vil den begynne med en ‘3’. For øyeblikket er alle SegWit-adresser kodet i Bech32 og begynner med prefikset ‘bc1’.                                                                                                                                                                                                                                                                                                                                                                                                               |
| App                                         | BTCPay Server har plugins som kan fungere som en applikasjon i seg selv.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| BIP 329                                     | Eksport/import av lommeboketiketter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| BIP49                                       | Definerer avledningsskjemaet for HD-lommebøker som bruker P2WPKH-nestet-i-P2SH (BIP 141) serialiseringsformat for transaksjoner med segregert vitne.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Bitcoin Adresse                             | Alfanumerisk streng hvor du sender dine bitcoin, så den "lever" der nå. Er en identifikator, som består av en streng med omtrent 33 bokstaver og tall kombinert. I en nåværende protokollversjon starter en adresse med 1, 3, eller b. Å ha en mottakers adresse er en nødvendig del for å initiere en bitcoin-transaksjon. Bitcoin-adresser genereres fra offentlige nøkler, og flere adresser kan genereres fra ett sett med offentlige nøkler for å forbedre personvernet. Bitcoin-adresser fungerer akkurat som e-postadresser, hvis du vil sende en melding trenger du å vite hvor den skal, det samme gjelder for bitcoin. Før du sender en bitcoin-transaksjon, må du sørge for at mottakerens adresse er nøyaktig siden bitcoin-transaksjoner er irreversible, og du kan sende bitcoin til en adresse som ikke tilhører en mottaker.                         |
| bitcoin versus Bitcoin                      | Bitcoin er det monetære nettverket, og bitcoin (med liten b) er en monetær enhet på Bitcoin-nettverket. Du bruker bitcoin-valuta eller en token for å gjennomføre transaksjoner på et Bitcoin-nettverk.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Blokk                                       | En blokk er en datastruktur i Bitcoin-blockchainen som består av en header og en kropp av Bitcoin-transaksjoner. Blokken er merket med et tidsstempel og forplikter seg til en spesifikk forgjenger (foreldre) blokk. Når hashet, gir blokkheaderen beviset på arbeid som gjør blockchainen probabilistisk uforanderlig. Blokker må overholde reglene som er håndhevet av nettverkskonsensus for å utvide blockchainen. Når en blokk er lagt til i blockchainen, anses de inkluderte transaksjonene for å ha sin første bekreftelse.                                                                                                                                                                                                                                                                                                                           |
| Block Explorer                              | Et nettbasert verktøy som gjør det mulig å søke etter sanntids- og historisk informasjon om en blockchain, inkludert data relatert til blokker, transaksjoner, adresser og mer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Blokkhash                                   | En blokkhash er SHA-256-hashen av blokkens data og representeres vanligvis i heksadesimalformat. En blokkhash kan tolkes som et veldig stort tall. For å oppfylle kravet til Proof-of-Work, må en blokkhash være under en viss terskel. Derfor starter alle blokkhasher med en rekke nuller etterfulgt av en alfanumerisk streng. Noen blokker har så mange som tjue ledende nuller, mens tidligere blokker har så få som åtte. Antallet nuller som kreves, viser omtrentlig vanskelighetsgraden av gruvedrift på tidspunktet blokken ble publisert. |
| Blokkhøyde                                  | Hver blokk er nummerert i stigende rekkefølge, startende fra null.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Blokkbelønning                              | Består av blokksubsidien (nyopprettede bitcoin) og summen av alle transaksjonsgebyrer fra transaksjoner inkludert i blokken.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Blokkstørrelse                              | Hver blokk har en begrenset mengde data den kan inneholde. Data som ikke passet inn i en bestemt blokk, vil bli registrert i en av de følgende blokkene. Når det gjelder bitcoinblokker, pleide de å ha en blokkstørrelse på 1mb, men etter en soft fork kan blokkstørrelsen teknisk sett inneholde opptil 4mb med data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Blokksubsidie                               | Mengden av ny bitcoin preget i hver blokk. Hver blokk som produseres og legges til i blokkjeden, lar skaperen av blokken prege en viss mengde ny bitcoin. Subsidien startet på 50 BTC per blokk, og halveres hver 210 000 blokker eller omtrent hvert 4. år.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Blokkjede                                   | En distribuert logg, eller database, over alle Bitcoin-transaksjoner. Transaksjoner grupperes i diskrete oppdateringer kalt blokker, begrenset opp til 4 millioner vektenheter. Blokker produseres omtrent hvert 10. minutt via en stokastisk prosess kalt gruvedrift. Hver blokk inkluderer et beregningsintensivt "proof of work." Kravet til proof of work brukes til å regulere blokkintervallene og beskytte blokkjeden mot angrep for å omskrive historien: en angriper måtte overgå eksisterende proof of work for å erstatte allerede publiserte blokker, noe som gjør hver blokk probabilistisk uforanderlig ettersom den er begravet under påfølgende blokker.                                                                                                                                                 |
| BTCPAY Server Vault                         | For optimal balanse mellom brukervennlighet, sikkerhet og personvern, anbefales det å bruke BTCPay Server Wallet med en maskinvare-lommebok. BTCPay Vault er bygget for å koble sammen maskinvare-lommeboken og BTCPay Server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Byzantinske Generalers Problem              | Et spillteoriproblem som beskriver vanskeligheten desentraliserte parter har med å komme til enighet uten å stole på en betrodd sentral part. Navnet kommer fra scenariet med flere generaler som beleirer Byzantium. De har omringet byen, men de må kollektivt bestemme når de skal angripe. Hvis alle generalene angriper samtidig, vil de vinne, men hvis de angriper på forskjellige tidspunkter, vil de tape. Generalene har ingen sikre kommunikasjonskanaler seg imellom fordi eventuelle meldinger de sender eller mottar kan ha blitt avlyttet eller bedragersk sendt av Byzantiums forsvarere. Hvordan kan generalene organisere seg for å angripe samtidig?                                                                                                                                 |
| Sensur                                      | Kontroll over hvilken informasjon som kan overføres til massene. Når det kommer til bitcoin, handler sensur om evnen til å stoppe transaksjonen av tredjeparter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Veksel                                      | Delen av UTXOene som returneres til avsenderens lommebok, vanligvis via en annen adresse. Beløper seg til summen av inngangene minus beløpet som er brukt og transaksjonsgebyret.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Child Pays For Parent (CPFP)                | En teknikk for å øke gebyret hvor en bruker utfører en transaksjon fra en utestående transaksjon med lavt gebyr i en "barn"-transaksjon med høyt gebyr for å oppmuntre gruvearbeidere til å inkludere begge transaksjonene i en blokk.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Coinbase Transaction                        | Den aller første transaksjonen i hver blokk som fordeler blokkbelønningen og transaksjonsgebyrene til den som utvinner blokken.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Coincidence of Wants                        | Et økonomisk fenomen der to parter hver holder en gjenstand som den andre ønsker, så de bytter disse gjenstandene direkte uten noe monetært medium.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Cold Storage                                | En måte å håndtere data på uten å være tilkoblet internett.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Cold Wallet                                 | En type bitcoin-lommebok som sikkert lagrer dine private nøkler frakoblet, vanligvis på en fysisk enhet. Også kjent som en maskinvarelommebok, og den beskytter dine digitale bitcoin fra nettbaserte hackere ved å bruke en enhet som ligner på et flash-stasjon som ikke er koblet til internett.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Command Line Interface (CLI)                | Interaksjon med en enhet eller et dataprogram med kommandoer fra en bruker eller klient, og respons fra enheten eller programmet, i form av tekstlinjer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Commitment Transaction                      | En forpliktelsestransaksjon er en Bitcoin-transaksjon, signert av begge kanalpartnere, som koder den nyeste saldoen i en kanal. Hver gang en ny betaling blir gjort eller videresendt ved bruk av kanalen, vil kanalsaldoen oppdateres, og en ny forpliktelsestransaksjon vil bli signert av begge parter. Viktig, i en kanal mellom Alice og Bob, beholder både Alice og Bob sin egen versjon av forpliktelsestransaksjonen, som også er signert av den andre parten. Kanalen kan når som helst lukkes av enten Alice eller Bob hvis de sender inn sin forpliktelsestransaksjon til Bitcoin-blockchainen. Å sende inn en eldre (utdatert) forpliktelsestransaksjon anses som juks (dvs. et brudd på protokollen) i Lightning Network og kan straffes av den andre parten, som kan kreve alle midlene i kanalen for seg selv, via en straffetransaksjon. |
| Confirmation                                | Når en transaksjon er inkludert i en blokk, har den én bekreftelse. Så snart en annen blokk blir utvunnet på blockchainen, har transaksjonen to bekreftelser, og så videre. Seks eller flere bekreftelser anses som tilstrekkelig bevis på at en transaksjon ikke kan reverseres.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Crowdfund (CF)                              | En standard plugin for BTCPay Server som lar en butikkeier enkelt opprette en typisk folkefinansieringsnettsted. De kan enkelt sette et mål, opprette fordeler for bidrag, og tilpasse det etter sine behov.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Cryptography                                | Et spesielt system, hvor det opprinnelige budskapet endres slik at bare de tiltenkte mottakerne kan motta det.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Dashboard                                   | Den sentrale landingssiden til BTCPay Server. Den gir en oversikt over all aktivitet for en butikk, vist på tvers av en rekke sammendragsfliser.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Demo                                        | Refererer til det virtuelle miljøet som programvaredemoer finner sted innenfor.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Deployment                                  | Programvareutplassering er alle aktivitetene som gjør et programvaresystem tilgjengelig for bruk. Den generelle utplasseringsprosessen består av flere sammenhengende aktiviteter med mulige overganger mellom dem.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Derivasjonssti                              | Et stykke data som forteller en hierarkisk deterministisk (HD) lommebok hvordan den skal utlede en spesifikk nøkkel innenfor et tre av nøkler. Derivasjonsstier brukes som en Bitcoin-standard og ble introdusert med HD-lommebøker som en del av BIP 32.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Vanskelighetsjustering                      | Justering av vanskelighetsmål, hver 2016 blokker (omtrent to uker) for å forsøke å sikre at blokker blir utvunnet omtrent hvert 10. minutt i gjennomsnitt. Det skaper derfor en konsekvent tid mellom blokker og en konsekvent utstedelse av nye bitcoins inn i nettverket (via blokkbelønningen).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Vanskelighetsmål                            | Brukt i utvinning, det er et tall som en blokkhash må være under for at blokken skal legges til på blockchainen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Digital Signatur                            | En digital signatur er et matematisk skjema for å verifisere autentisiteten og integriteten til digitale meldinger eller dokumenter. Det kan sees som et kryptografisk løfte der meldingen ikke er skjult.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Deltbart                                    | Egenskapen til en vare som kan deles inn i mindre mengder uten å miste verdi. Fordi økonomiske transaksjoner ofte forekommer i varierende mengder, må en valuta være deltbar for å bli brukt bredt i en økonomi.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Docker                                      | Programvare som pakker programvare inn i standardiserte enheter kalt containere som har alt programvaren trenger for å kjøre, inkludert biblioteker, systemverktøy, kode og kjøretid.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Dobbel-Utgifte                              | Resultatet av å lykkes med å bruke noen penger mer enn én gang. Bitcoin beskytter mot dobbel-utgifter ved å verifisere at hver transaksjon som legges til i blockchainen overholder konsensusreglene; dette betyr å sjekke at inngangene for transaksjonen ikke har blitt brukt tidligere.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Holdbar                                     | Egenskapen til penger, der valutaen kan opprettholde sin opprinnelige tilstand over tid og tåle gjentatt bruk. En holdbar valuta må kunne overleve potensiell skade.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Electrum                                    | Electrum er en av de mest populære Bitcoin-lommebøkene, opprettet i 2011.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Utvidet offentlig nøkkel (Xpub)             | Utvidet offentlig nøkkel, også kjent som Xpub, en offentlig nøkkel som fungerer som en forelder til nøkler som er utledet fra xpub som en funksjon av HD-lommeboken. Denne Xpub er en standard introdusert i BIP 32. Lommebøker bruker den bak kulissene for å utlede offentlige nøkler. Deling av Xpub frarådes ikke, dine midler vil ikke være i direkte risiko for å bli flyttet, xpub kan ikke utlede private nøkler. Fordelen med å dele en xpub kan være for crowdfunding-formål i BTCPay Server. Xpub deles gjennom online midler, mens de private nøklene forblir offline på en HWW.                                                                                                                                                                                                                             |
| F.U.D.                                      | Forkortelse for Frykt, usikkerhet og tvil; Vanligvis fremkalt med vilje for å sette en konkurrent i en ulempe.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Gebyr                                       | I konteksten av Lightning Network, vil noder kreve rutegebyrer for å videresende andre brukeres betalinger. Enkeltnoder kan sette sine egne gebyrpolitikker som vil bli beregnet som summen av en fast base_fee og en fee_rate som avhenger av betalingsbeløpet. I konteksten av Bitcoin, betaler avsenderen av en transaksjon et transaksjonsgebyr til gruvearbeidere for å inkludere transaksjonen i en blokk. Bitcoin transaksjonsgebyrer inkluderer ikke et basisgebyr og avhenger lineært av transaksjonens vekt, men ikke på beløpet.                                                                                                                                                                                                                                                              |
| Fiat                                        | Mynt utstedt av regjeringen som ikke er støttet av en vare som gull.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Finite                                      | Refererer til Bitcoins begrensede tilgang.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Fork                                        | En endring i et protokoll eller en kodebit. Forks blir vanligvis introdusert for å oppgradere et prosjekt. I det åpne kildekode-samfunnet eksisterer forks fordi mange individer velger å laste ned og kjøre den samme programvaren på forskjellige tidspunkter og ikke alltid oppdaterer. Hvis to brukere laster ned og kjører versjon 1 av en programvare, og bare én bruker oppgraderer når versjon 2 blir utgitt, kjører brukeren som oppdaterte en fork av versjon 1.                                                                                                                                                                                                                                                                                                                                                                                                            |
| Funding Transaction                         | Transaksjon brukt til å åpne en betalingskanal. Verdien (i bitcoin) av funding-transaksjonen er nøyaktig kapasiteten til betalingskanalen. Utdata fra funding-transaksjonen er et 2-av-2 multisignatur-script (multisig) hvor hver kanalpartner kontrollerer én nøkkel. På grunn av sin multisig-natur, kan den bare brukes ved gjensidig avtale mellom kanalpartnerne. Den vil til slutt bli brukt av en av forpliktelsestransaksjonene eller av avslutningstransaksjonen.                                                                                                                                                                                                                                                                                                                                                                                     |
| Fungible                                    | Å være noe (som penger eller en vare) av slik natur at en del eller mengde kan erstattes av en annen lik del eller mengde for å betale en gjeld eller gjøre opp en konto                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Gap Limit                                   | Refererer til standard antall offentlige adresser som sjekkes for transaksjoner i blockchain for å beregne en konto sin saldo. Transaksjoner mottatt på en adresse utover adresse gap-grensen blir ikke oppdaget.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Genesis Block                               | Første blokk i Bitcoin-blockchainen. Satoshi Nakamoto, skaperen av Bitcoin, minet Genesis-blokken 3. januar 2009 og inkluderte den dagens Financial Times overskrift, “Chancellor on brink of second bailout for banks.”                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Github                                      | En plattform og skybasert tjeneste for programvareutvikling og versjonskontroll ved bruk av Git, som lar utviklere lagre og administrere koden sin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Gossip Protocol                             | LN-noder sender og mottar informasjon om topologien til Lightning Network gjennom sladder-meldinger som utveksles med deres jevnaldrende. Gossip-protokollen er hovedsakelig definert i BOLT #7 og definerer formatet på node_announcement, channel_announcement, og channel_update meldinger. For å forhindre spam, vil node-annonseringsmeldinger bare bli videresendt hvis noden allerede har en kanal, og kanal-annonseringsmeldinger vil bare bli videresendt hvis funding-transaksjonen til kanalen har blitt bekreftet av Bitcoin-nettverket. Vanligvis kobler Lightning-noder seg med sine kanalpartnere, men det er også greit å koble seg til en hvilken som helst annen Lightning-node for å behandle sladder-meldinger.                                                                                                                                       |
| Gresham's Law                               | Lov som sier at “dårlig penger driver ut gode”. Med andre ord, i en økonomi der to valutaer er i bruk, vil individer bruke de dårlige pengene, som stadig mister verdi, og holde på de gode pengene, som beholder sin verdi. Dermed vil de dårlige pengene dominere når det gjelder sirkulasjon og bruk i daglige transaksjoner, mens de gode pengene vil dominere når det gjelder sparing og langsiktig investering.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Halving                                     | En hendelse som reduserer utstedelsesraten av bitcoin med halvparten hvert 210 000 blokker (omtrent fire år).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Hard Fork                                   | En konsensusendring som ikke er bakoverkompatibel. Bakoverinkompatibilitet oppstår når en tidligere ugyldig oppførsel blir gjort gyldig. For å opprettholde konsensus over en hard fork, er alle noder nødt til å oppgradere. Ellers vil gamle noder avvise transaksjoner eller blokker som ugyldige under de gamle reglene, mens oppgraderte noder vil akseptere dem som gyldige. Av denne grunn unngås hard forks for enhver pris i Bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Hardware Wallet (HWW)                       | En spesiell type Bitcoin-lommebok som lagrer brukerens private nøkler i en sikker maskinvareenhet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Hash Function                               | En kryptografisk hashfunksjon er en matematisk algoritme som kartlegger data av vilkårlig størrelse til en bitstreng av en fast størrelse (en hash) og er designet for å være en enveisfunksjon, det vil si, en funksjon som er upraktisk å invertere. Den eneste måten å gjenskape inndata fra utdataen til en ideell kryptografisk hashfunksjons er å forsøke en brute-force søk av mulige inndata for å se om de produserer en match.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Hash Rate                                   | Et mål på hvor mange hasher gruvearbeidere samlet produserer per sekund på Bitcoin-nettverket. En enkelt hash er et forsøk på å skape et Proof-of-Work for en blokk.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Hot Wallet                                  | En enhet med eksterne tilkoblinger, spesielt til internett. En hot wallet er en Bitcoin-lommebok som kobles til internett. Disse lommebøkene er mer praktiske for daglig bruk, men er ikke like sikre som kaldlagringsalternativer fordi de samhandler med internett.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Initial Block Download (IBD)                | Prosessen med å bygge hele Bitcoin-blockchainen fra bunnen av. Når en ny node settes opp og blir med i nettverket, kobler den seg til andre noder og spør dem om blokker. Den nye noden behandler disse blokkene og bygger blockchainen til den har tatt igjen og er synkronisert med nettverket.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Invoice                                     | Et kommersielt dokument utstedt av en selger til en kjøper i forbindelse med en salgstransaksjon og som angir produktene, mengdene og de avtalte prisene for produkter eller tjenester selgeren har levert til kjøperen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Know Your Customer (KYC)                    | Lover som er ment å forhindre at finansielle institusjoner blir brukt til ulovlige pengeoverføringer ved å kreve at alle finansielle kontoer kan identifiseres til enkeltpersoner eller organisasjoner.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Layer 2                                     | Et nettverk bygget på toppen av en blockchain, f.eks., Lightning Network.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Legacy Address                              | Legacy-adresser bruker Base58, og når en legacy-adresse er hashen av en offentlig nøkkel, en såkalt P2PKH-adresse, begynner den med en ‘1’.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Lightning Network                           | Et protokoll på toppen av Bitcoin. Det skaper et nettverk av betalingskanaler som muliggjør videresending av betalinger gjennom nettverket uten behov for tillit, med hjelp av HTLCs og onion routing. Andre komponenter i Lightning Network er gossip-protokollen, transportlaget og betalingsforespørsler.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Liquidity                                   | Mål på flere egenskaper ved en bestemt eiendels ordrebok innenfor et gitt marked. Likviditet er en indikator på hvor mye av en markedsinnvirkning en stor ordre vil ha på prisen på en eiendel. En eiendel med mer likviditet har dypere ordrebokdybde. Dette betyr at den vil kunne absorbere flere ordre med mindre prisbevegelser.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Lengste Kjede                               | Kjeden av blokker som tok mest innsats å bygge. Navngitt slik fordi intuitivt vil en blockchain med flere blokker i seg ha tatt mer energi å bygge enn en kjede med færre blokker i seg, men mer nøyaktig er det kjeden som krevde mer arbeid å produsere, så et bedre navn kunne ha vært "tyngste kjede."                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Hovedkjede                                  | I konteksten av Lightning Network refererer dette til Bitcoin-nettverket.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Byttemiddel                                 | En type vare som letter utvekslingen av andre varer og tjenester innenfor en økonomi. Historisk sett ble ting som skjell, perler og gull brukt som byttemidler.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Mempool                                     | Kort for "minnepool," det er en midlertidig lagring for transaksjoner som har blitt mottatt av en node.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Miner                                       | En node engasjert i prosessen med å bygge blockchain ved å legge til nye blokker gjennom prosessen med hashing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Mining                                      | Prosessen med å konstruere en blokk fra nylige Bitcoin-transaksjoner og deretter løse et beregningsproblem som kreves som proof of work. Det er prosessen hvorved den delte bitcoin-hovedboken (dvs. Bitcoin-blockchain) oppdateres og ved hvilken nye transaksjoner inkluderes i hovedboken. Det er også prosessen hvorved ny bitcoin utstedes. Hver gang en ny blokk opprettes, vil mining-noden motta ny bitcoin opprettet innenfor coinbase-transaksjonen av den blokken.                                                                                                                                                                                                                                                                                                                                                                                 |
| Multisignatur (multisig)                    | Et skript som krever mer enn én signatur for å autorisere utgifter. Betalingskanaler er alltid kodet som multisig-adresser som krever én signatur fra hver partner i betalingskanalen. I standardtilfellet av en to-partners betalingskanal, brukes en 2-av-2 multisig-adresse.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Node                                        | En datamaskin som deltar i et nettverk. Spesielt Bitcoin- eller Lightning-nettverkene.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Output                                      | Pakke med bitcoins opprettet i en bitcoin-transaksjon.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Output Lock                                 | Et sett med krav plassert på en output. Disse kravene må oppfylles for å kunne bruke outputen i en transaksjon. Det mest vanlige eksempelet er et enkelt krav om å ha den private nøkkelen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| P2SH Adresse                                | P2SH-adresser er Base58Check-kodinger av 20-byte hashen av et skript. P2SH-adresser starter med en "3." P2SH-adresser skjuler all kompleksiteten, slik at avsenderen av en betaling ikke ser skriptet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| P2WPKH Adresse                              | "Native SegWit v0"-adresseformatet, P2WPKH-adresser er bech32-kodet og starter med "bc1q".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| P2WSH Adresse                               | "Native Segwit v0"-skriptadresseformatet, P2WSH-adresser er bech32-kodet og starter med "bc1q".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Delvis Signert Bitcoin Transaksjon (PSBT)  | En Bitcoin-standard som letter portabiliteten av usignerte transaksjoner, som gjør det mulig for flere parter å enkelt signere samme transaksjon. Dette er mest nyttig når flere parter ønsker å legge til innganger i samme transaksjon. PSBT ble introdusert av BIP 174, og lar brukere lettere signere transaksjoner på en kaldlagringsenhet og deretter kringkaste den signerte transaksjonen fra en enhet koblet til internett.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Stifinning                                  | Prosessen med å finne en vei for betaling fra kilde til destinasjon i Lightning Network.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Pay-to-Public-Key-Hash (P2PKH)              | P2PKH er en type utgang som låser bitcoin til hashen av en offentlig nøkkel. En utgang låst av et P2PKH-skript kan låses opp (brukes) ved å presentere den offentlige nøkkelen som matcher hashen og en digital signatur skapt av den tilsvarende private nøkkelen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Pay-to-Script-Hash (P2SH)                   | P2SH er en allsidig type utgang som tillater bruk av komplekse Bitcoin-skript. Med P2SH presenteres ikke det komplekse skriptet som detaljerer betingelsene for å bruke utgangen (innløsningsskriptet) i låseskriptet. I stedet låses verdien til hashen av et skript, som må presenteres og oppfylles for å bruke utgangen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Pay-to-Taproot (P2TR)                       | Aktivert i november 2021, er Taproot en ny type utgang som låser bitcoin til et tre av betingelser for bruk, eller en enkelt rotbetingelse.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Pay-to-Witness-Public-Key-Hash (P2WPKH)     | P2WPKH er SegWit-ekvivalenten til P2PKH, som bruker et segregert vitne. Signaturen for å bruke en P2WPKH-utgang plasseres i vitnetreet i stedet for ScriptSig-feltet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Pay-to-Witness-Script-Hash (P2WSH)          | P2WSH er SegWit-ekvivalenten til P2SH, som bruker et segregert vitne. Signaturen og skriptet for å bruke en P2WSH-utgang plasseres i vitnetreet i stedet for ScriptSig-feltet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Payjoin                                     | En spesiell type Bitcoin-transaksjon hvor både avsenderen og mottakeren bidrar med innganger for å bryte den vanlige eierskapsheuristikken for innganger, en antagelse brukt for å fjerne personvern fra bitcoin-brukere.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Betalingskanal                              | Et finansielt forhold mellom to noder på Lightning Network, opprettet ved hjelp av en bitcoin-transaksjon som betaler til en multisignaturadresse. Kanalpartnerne kan bruke kanalen til å sende bitcoin frem og tilbake mellom hverandre uten å måtte legge til alle transaksjonene på Bitcoin-blockchainen. I en typisk betalingskanal legges kun to transaksjoner, finansieringstransaksjonen og forpliktelsestransaksjonen, til blockchainen. Betalinger sendt over kanalen blir ikke registrert i blockchainen og sies å skje "off-chain."                                                                                                                                                                                                                                                                                                         |
| Betalingsforespørsel                        | En funksjon som lar eiere av BTCPay-butikker opprette langvarige fakturaer. Midler betalt til en betalingsforespørsel bruker vekslingskursen på betalingstidspunktet. Dette lar brukere gjøre betalinger når det passer dem, uten å måtte forhandle eller verifisere vekslingskurser med butikkeieren på betalingstidspunktet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Utbetaling                                  | Utbetalingsfunksjonaliteten er knyttet til Pull Payments. Denne funksjonen lar deg behandle pull-betalinger (refusjoner, lønnsutbetalinger eller uttak).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Plugin                                      | Et programtillegg som er installert på et program, som forbedrer dets kapasiteter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Point Of Sale (PoS)                         | En standard plugin av BTCPay Server som lar en butikkeier opprette en nettbutikk direkte fra BTCPay Server. Butikkeieren trenger ikke noen tredjeparts e-handelsløsninger for å drive en nettbutikk.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Bærbarhet                                   | Evnen et gode har til å bli enkelt transportert over avstander. Bærbarhet er en viktig egenskap ved lydende penger; for at en valuta skal bli bredt adoptert, og derfor brukbar, må den kunne bevege seg på tvers av grenser, mellom individer, og over lange avstander med relativ letthet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Proof Of Work (PoW)                         | Data som krever betydelig beregning for å finne, og som enkelt kan verifiseres av hvem som helst for å bevise mengden arbeid som var nødvendig for å produsere den. I Bitcoin må gruvearbeidere finne en numerisk løsning på SHA-256-algoritmen som møter et nettverksomfattende mål, kalt vanskelighetsmålet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Pseudonym                                   | Et falskt navn brukt av individer for å beskytte deres identitet eller bygge en reputasjon separat fra deres virkelige identitet. Offentlige nøkler brukes for å tillate Bitcoin-brukere å motta bitcoin samtidig som de forblir pseudonyme med hensyn til blokkjeden.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Offentlig-nøkkel Kryptografi                | Involverer et par nøkler kjent som en offentlig nøkkel og en privat nøkkel, som er assosiert med en enhet som trenger å autentisere sin identitet elektronisk eller for å signere eller kryptere data. Den offentlige nøkkelen er publisert og den tilsvarende private nøkkelen holdes hemmelig. Data som er kryptert med den offentlige nøkkelen kan kun dekrypteres med den tilsvarende private nøkkelen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Offentlig/Privat Nøkkel                     | Nøkkelpar brukt i offentlig-nøkkel kryptografi. Den offentlige nøkkelen deles med andre åpent, og kan tenkes på som et kontonummer, mens den private nøkkelen holdes hemmelig og kan tenkes på som et passord.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Trekkbetaling                               | Tradisjonelt, for å gjøre en Bitcoin-betaling, deler mottakeren sin bitcoin-adresse og senderen sender senere penger til denne adressen. Et slikt system kalles skyvebetaling ettersom senderen initierer betalingen mens mottakeren kan være utilgjengelig, og i effekt skyver betalingen til mottakeren. I stedet for det typiske scenarioet hvor en sender "skyver" betalingen, tillater senderen mottakeren å trekke betalingen på et tidspunkt mottakeren anser som passende.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Kaninhullet                                 | En referanse til Alice I Eventyrland hvor helten begir seg ut på et eventyr ved å entre et kaninhull. Innen Bitcoin refererer det til de tilsynelatende uendelige emnene man utforsker og ser i et nytt lys når de har begynt å forstå Bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Motta                                       | Prosessen med å få bitcoin sendt til en oppgitt adresse.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Registrere                                  | Prosessen med å opprette en konto eller melde seg på en tjeneste, vanligvis gjort ved å velge et brukernavn og passord.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Erstatt Ved Avgift (RBF)                    | En Bitcoin-transaksjon kan bli betegnet som RBF for å tillate senderen å erstatte denne transaksjonen med en annen lignende transaksjon som betaler en høyere avgift. Denne mekanismen eksisterer for å tillate brukere å reagere hvis nettverket blir overbelastet og avgiftene stiger uventet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Repositorium                                | I versjonskontrollsystemer er et repositorium en datastruktur som lagrer metadata for et sett med filer eller katalogstruktur.[1] Avhengig av om versjonskontrollsystemet i bruk er distribuert, som Git eller Mercurial, eller sentralisert, som Subversion, CVS, eller Perforce, kan hele settet med informasjon i repositoriet være duplisert på hvert brukersystem eller kan vedlikeholdes på en enkelt server.[2] Noen av metadataene som et repositorium inneholder inkluderer, blant annet, en historisk oversikt over endringer i repositoriet, et sett med commit-objekter, og et sett med referanser til commit-objekter, kalt hoder.                                                                                                                                                                                                                                  |
| Rescan                                      | Prosessen med å skanne den nåværende tilstanden til UTXO-settet for mynter som tilhører et tidligere konfigurert avledningsskjema.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Revokation Key                              | Hver Revocable Sequence Maturity Contract (RSMC) inneholder to tilbakekallingsnøkler. Hver kanalpartner kjenner en tilbakekallingsnøkkel. Ved å kjenne begge tilbakekallingsnøklene, kan utdataen fra RSMC brukes innenfor den forhåndsdefinerte tidsbegrensningen. Mens man forhandler en ny kanaltilstand, deles de gamle tilbakekallingsnøklene, dermed "tilbakekaller" man den gamle tilstanden. Tilbakekallingsnøkler brukes for å avskrekke kanalpartnere fra å kringkaste en gammel kanaltilstand.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Routing                                     | Prosessen med å bruke Lightning Network-stien for å gjøre en betaling.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Routing Fees                                | I Lightning Network, avgifter belastet for å videresende andre brukeres betalinger. Individuelle noder kan sette sine egne avgiftspolitikker som vil bli beregnet som summen av en fast base_fee og en fee_rate som avhenger av betalingsbeløpet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Salability                                  | Hvor lett en vare kan selges på markedet når som helst eieren ønsker det, med minst mulig tap i prisen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Satoshi (sat)                               | En satoshi er den minste enheten (valør) av bitcoin som kan registreres på blockchain. En satoshi er 1/100 milliondel (0.00000001) av en bitcoin og er oppkalt etter skaperen av Bitcoin, Satoshi Nakamoto.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Satoshi Nakamoto                            | Navnet brukt av personen eller gruppen av personer som designet Bitcoin og skapte dens opprinnelige referanseimplementasjon. Som en del av implementasjonen, utviklet de også den første blockchain-databasen. I prosessen var de de første til å løse problemet med dobbeltutgifter for digital valuta. Deres virkelige identitet forblir ukjent.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Satoshi Per Byte                            | En enhet for å måle transaksjonsprioritet, definert av transaksjonens avgift i satoshi delt på størrelsen på transaksjonen i byte.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Satoshi Per Verabyte                        | Lignende konsept som Satoshi Per Byte, men for nyere adresser som bruker Segwit. Lik transaksjonens størrelse i vektenheter delt på 4. Vektenheter beregnes ved å ta transaksjonsstørrelsen (uten vitnet) ganger 3, lagt til transaksjonsstørrelsen inkludert vitnet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Scarcity                                    | Egenskapen til en vare som ikke kan replikeres uten kostnad. Knapphet er ikke avhengig av antall eksisterende enheter av en vare, men heller på kostnaden ved å produsere flere enheter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Script                                      | Bitcoin bruker et skriptingssystem for transaksjoner kalt Bitcoin Script. Det ligner programmeringsspråket Forth, er enkelt, basert på stakk og behandles fra venstre til høyre. Det er bevisst Turing-ufullstendig, uten løkker eller rekursjon.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Seed Phrase                                 | En liste med ord som lagrer all informasjonen som trengs for å gjenopprette Bitcoin-midler på kjeden. Lommebokprogramvare vil typisk generere en seed phrase og instruere brukeren til å skrive den ned på papir. Hvis brukerens datamaskin bryter sammen eller harddisken blir korrupt, kan de laste ned samme lommebokprogramvare igjen og bruke papirbackupen for å få tilbake bitcoinsene sine.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Segregated Witness (SegWit)                 | Segregated Witness (SegWit) er en oppgradering til Bitcoin-protokollen introdusert i 2017 som legger til et nytt vitnefelt for signaturer og andre transaksjonsautorisasjonsbevis. Dette nye vitnefeltet er unntatt fra beregningen av transaksjons-IDen, noe som løser de fleste klasser av tredjeparts transaksjonsmalleabilitet. Segregated Witness ble implementert som en myk oppdatering og er en endring som teknisk sett gjør Bitcoins protokollregler mer restriktive.                                                                                                                                                                                                                                                                                                                                                                                                                |
| Self-Sovereignty                            | En modell for håndtering av digitale identiteter der enkeltpersoner eller bedrifter har eneansvar over evnen til å kontrollere sine kontoer og personlige data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Send                                        | Prosessen med å flytte bitcoin til en adresse.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Sensitivity Mode                            | Aktivert via en veksleknapp i butikkinnstillingene, aktivering resulterer i at numeriske verdier (f.eks. mengde bitcoin) blir skjult i alle visninger.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Server Settings                             | Innstillinger innenfor BTCPay Server som gjelder serveromfattende (i motsetning til Store Settings som er begrenset i omfang til en enkelt butikk).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| SHA-256                                     | En kryptografisk hashfunksjon. Et medlem av en familie av hashfunksjoner kalt Secure Hashing Algorithm (SHA) funksjoner.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Shopify                                     | Et kanadisk multinasjonalt e-handelsselskap med hovedkontor i Ottawa, Ontario. Shopify er navnet på sin proprietære e-handelsplattform for nettbutikker og detaljhandelssystemer for salgspunkt.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| SMTP                                        | Simple Mail Transfer Protocol er en internettstandard kommunikasjonsprotokoll for elektronisk postoverføring.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Soft Fork                                   | En protokolloppgradering som er kompatibel både fremover og bakover, slik at den tillater både gamle noder og nye noder å fortsette å bruke samme kjede.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Software Stack                              | I databehandling er en løsningsstabel eller programvarestabel et sett med programvaresubsystemer eller komponenter som er nødvendige for å skape en komplett plattform slik at ingen ytterligere programvare er nødvendig for å støtte applikasjoner                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Store                                       | En butikk innenfor BTCPay Server kan ses på som et "Hjem" til en spesifikk bitcoin-lommebok, utvidet med alle funksjonene til BTCPay Server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Store Settings                              | Innstillinger innenfor BTCPay Server spesifikke for en butikk.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Taproot                                     | Oppgradering til Bitcoin som ville introdusere flere nye funksjoner. Oppgraderingen er beskrevet i BIPs 340, 341, og 342, og introduserer Schnorr-signaturordningen, Taproot, og Tapscript. Sammen introduserer disse oppgraderingene nye, mer effektive, fleksible og private måter å overføre bitcoin på.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Thier's Law                                 | Lov som sier at god valuta vil drive ut dårlig valuta.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Third-Party Host                            | Når et nettsted for en enkeltperson eller et selskap kjøres på servere eid og administrert av et annet selskap. Alternativet er å ha ditt nettsted hostet på dine servere i ditt eget datasenter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Timelock                                    | En tidsbegrensning er en type hindring som begrenser bruken av noen bitcoin til et spesifisert fremtidig tidspunkt eller blokkhøyde. Tidsbegrensninger spiller en fremtredende rolle i mange Bitcoin-kontrakter, inkludert betalingskanaler og HTLCs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Topologi                                    | Topologien til Lightning Network beskriver formen på Lightning Network som en matematisk graf. Noder i grafen er Lightning-noder (nettverksdeltakere/peers). Kantene i grafen er betalingskanalene. Topologien til Lightning Network blir offentlig kringkastet med hjelp av gossip-protokollen, med unntak av uannonserte kanaler. Dette betyr at Lightning Network kan være betydelig større enn det annonserte antallet kanaler og noder. Å kjenne topologien er av spesiell interesse i prosessen med kildebassert ruting av betalinger, der avsenderen oppdager en rute.                                                                                                                                                                                                                           |
| Transaksjon                                 | Transaksjoner er datastrukturer brukt av Bitcoin for å overføre bitcoin fra en adresse til en annen. Flere tusen transaksjoner blir aggregert i en blokk, som deretter blir registrert (minet) på blokkjeden. Den første transaksjonen i hver blokk, kalt coinbase-transaksjonen, genererer nye bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Transaksjons-ID                             | En streng av bokstaver og tall som identifiserer en spesifikk transaksjon på blokkjeden. Strengen er rett og slett den doble SHA-256 hashen av en transaksjon. Denne hashen kan brukes til å slå opp en transaksjon på en node eller blokkutforsker.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| To-faktor autentisering (2FA)               | En identitets- og tilgangsstyrings sikkerhetsmetode som krever to former for identifikasjon for å få tilgang til ressurser og data, ofte med en sekundær enhet i tillegg til det standard innloggingspassordet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Usensurerbar                                | Egenskapen at ingen enhet har muligheten til å reversere en Bitcoin-transaksjon eller svarteliste en lommebok eller adresse.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Ubetvingelig                                | Egenskapen at ingen enhet kan ta bitcoin fra en enhet mot deres vilje.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Ubrukte Transaksjonsutganger (UTXO)         | Utganger som ennå ikke er brukt, og dermed tilgjengelige for å bli brukt i nye transaksjoner.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Brukeropplevelse (UX)                       | Hvordan en bruker samhandler med og opplever et produkt, system eller tjeneste. Det inkluderer en persons oppfatninger av nytte, brukervennlighet og effektivitet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Brukergrensesnitt (UI)                      | Punktet for menneske-datamaskin interaksjon og kommunikasjon i en enhet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Verifiserbar                                | Egenskapen til et gode som kan lett skilles fra bedragere og forfalskninger.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Virtuell                                    | Å være på eller simulert på en datamaskin eller datanettverk.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Virtuell maskin (VM)                        | I databehandling er en virtuell maskin virtualiseringen eller emuleringen av et datasystem. Virtuelle maskiner er basert på datamaskinarkitekturer og gir funksjonaliteten til en fysisk datamaskin. Deres implementasjoner kan involvere spesialisert maskinvare, programvare, eller en kombinasjon av de to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Virtuell Privat Server                      | En virtuell privat server er en virtuell maskin solgt som en tjeneste av en internett hosting-tjeneste. Uttrykket "virtuell dedikert server" har også en lignende betydning. En virtuell privat server kjører sin egen kopi av et operativsystem, og kunder kan ha superbruker-nivå tilgang til den operativsysteminstansen, så de kan installere nesten hvilken som helst programvare som kjører på det OS-et.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Volatilitet                                 | Mål på graden av variasjon i en eiendels pris over tid. Eiendeler som opplever store endringer i pris regelmessig er mer volatile, mens eiendeler som har en mer stabil pris er mindre volatile.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Wallet                                      | Bitcoin-lommebøker holder en brukers nøkler, noe som gjør det mulig for brukere å motta bitcoin, signere transaksjoner og sjekke sin kontobalanse. De private og offentlige nøklene som holdes i en bitcoin-lommebok, tjener to distinkte funksjoner, men er knyttet sammen i skapelsen. Bitcoin-lommebøker inneholder en brukers nøkler, ikke deres faktiske bitcoin. Konseptuelt er en lommebok som en nøkkelring i den forstand at den holder mange par av private og offentlige nøkler. Disse nøklene brukes til å signere transaksjoner, noe som gjør det mulig for en bruker å bevise at de eier transaksjonsutganger på blokkjeden, dvs. deres bitcoin. All bitcoin er registrert på blokkjeden i form av transaksjonsutganger.                                                                                                                                                                                                                      |
| Wasabi Wallet                               | En åpen kildekode, ikke-forvaringsbasert, personvern-fokusert Bitcoin-lommebok for Desktop som implementerer tillitsløs CoinJoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Watch-Only Wallet                           | Bitcoin-lommebøker som lar deg holde styr på din bitcoin i kald lagring mens de deaktiverer muligheten til å bruke midler. Dette er fordi watch-only lommebøker ikke lagrer eller bruker private nøkler, og er derfor ute av stand til å autorisere noen utgifter på vegne av brukeren.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Whale                                       | Innenfor konteksten av Bitcoin, er en whale noen som holder en stor mengde bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| White-Label                                 | Et white-label produkt er et produkt eller tjeneste produsert av ett selskap som andre selskaper merkevarebygger for å få det til å se ut som om de hadde laget det.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Whitepaper                                  | Introduserer en ny idé eller emne for diskusjon. Bitcoin whitepaper introduserte Bitcoin som et "Peer-to-peer elektronisk kontantsystem" som "ikke krever pålitelige tredjeparter". Satoshi Nakamoto slapp whitepaperet 31. oktober 2008 til en e-postliste av kryptografer og cypherpunks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Wrapped Segwit                              | En designimplementering inkludert i SegWit-oppgraderingen ment for å gjøre det lettere for lommebøker og annen Bitcoin-programvare å støtte SegWit. For å oppnå dette, brukes de to innfødte SegWit-skriptene, P2WPKH og P2WSH, som "redeemScript" av en P2SH-transaksjon, noe som resulterer i wrapped SegWit skripttyper av P2SH-P2WPKH og P2SH-P2WSH henholdsvis.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

![bilde](assets/en/129.webp)