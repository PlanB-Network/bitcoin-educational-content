---
name: Mestre BTC Pay Server
goal: Konfigurer en BTC Pay Server-instans for en lokal bedrift
objectives:
- Forstå grunnleggende om BTCPay Servers rolle i betalingsbehandling
- Mestre den indre virkemåten til BTCPay Server-konfigurasjonsprosessen
- Distribuere BTCPay Server på sky- og nodebaserte miljøer
- Bli en BTC Pay Server-operatør
---
# Reisen til finansiell suverenitet

Tillit er skjør, spesielt når det gjelder penger. Dette introduksjonskurset veileder deg gjennom BTCPay Server, et kraftig verktøy som lar deg akseptere Bitcoin-betalinger uten å stole på tredjeparter. Du vil lære det grunnleggende om å bli en BTCPay Server-operatør

Laget av Alekos og Bas, og tilpasset av melontwist og asi0, avslører dette kurset hvordan enkeltpersoner og bedrifter bygger alternativer til tradisjonelle betalingssystemer. Enten du er nysgjerrig på Bitcoin eller klar til å drifte betalingsinfrastrukturer for bedrifter, vil du oppdage praktiske ferdigheter som utfordrer status quo. Klar til å utforske hvordan finansiell uavhengighet faktisk ser ut?
+++
# Innledning


<partId>59e43fe3-b494-5da6-b4b4-9df5bdf08916</partId>


## Kursoversikt


<chapterId>785ed2bc-94ae-4962-a26a-edf5742a3c72</chapterId>


Velkommen til POS 305-kurset på BTCPay Server!


Målet med denne opplæringen er å lære deg hvordan du installerer, konfigurerer og bruker BTCPay Server i din bedrift eller organisasjon. BTCPay Server er en åpen kildekodeløsning som lar deg behandle Bitcoin-betalinger på en selvstendig, sikker og kostnadseffektiv måte. Dette kurset er primært rettet mot avanserte brukere som ønsker å mestre selvhosting av BTCPay Server for full integrering i den daglige driften.


**Avsnitt 1: Introduksjon til BTCPay Server**

Vi begynner med en generell presentasjon av BTCPay Server, inkludert påloggingsskjermen, administrasjon av brukerkontoer og opprettelse av en ny butikk. Denne introduksjonen vil hjelpe deg med å forstå BTCPay Server Interface og forstå de grunnleggende funksjonene som trengs for å begynne å bruke dette verktøyet.


**Avsnitt 2: Introduksjon til sikring av Bitcoin-nøkler**

Sikkerheten til Bitcoin-midlene dine er svært viktig. I denne delen vil vi utforske generering av kryptografiske nøkler, bruk av maskinvarelommebøker for å sikre disse nøklene, og hvordan du samhandler med nøklene dine via BTCPay Server. Du vil også lære hvordan du konfigurerer en BTCPay Server Lightning Wallet for å optimalisere transaksjonene dine.


**Avsnitt 3: BTCPay Server Interface**

Denne delen vil veilede deg gjennom BTCPay Server-brukeren Interface. Du vil lære hvordan du navigerer i dashbordet, konfigurerer butikk- og serverinnstillinger, administrerer betalinger og drar nytte av integrerte plugins. Målet er å gi deg verktøyene du trenger for å tilpasse installasjonen etter dine spesifikke behov.


**Avsnitt 4: Konfigurere BTCPay Server**

Til slutt vil vi fokusere på den praktiske installasjonen av BTCPay Server i ulike miljøer. Enten du bruker LunaNode, Voltage eller en Umbrel-node, vil du lære de viktigste trinnene for å distribuere og konfigurere BTCPay Server, med tanke på spesifikasjonene i hvert miljø.


Er du klar til å mestre BTCPay Server og utvide virksomheten din? La oss sette i gang!


## Kritisk anerkjennelse for Author's Bitcoin og BTCPay Server


<chapterId>e1fe6294-3c82-5203-9537-779f9087c35a</chapterId>


La oss starte med å forstå hva BTCPay Server er og dens opprinnelse. Vi verdsetter åpenhet og visse standarder for å skape tillit i Bitcoin-rommet.

Et prosjekt i rommet brøt disse verdiene. BTCPay Servers hovedutvikler, Nicolas Dorier, tok dette personlig og lovet å gjøre dem overflødige. Her er vi, mange år senere, og jobber mot denne fremtiden, helt åpen kildekode, hver dag.


> Dette er løgn, min tillit til deg er brutt, jeg vil gjøre deg foreldet.
> Nicolas Dorier

Etter ordene fra Nicolas var det på tide å begynne å bygge. En betydelig mengde arbeid gikk inn i det vi nå kaller BTCPay Server. Flere mennesker ønsket å bidra til denne innsatsen. De mest gjenkjennelige er r0ckstardev, MrKukks, Pavlenex og den første kjøpmannen som brukte programvaren, astupidmoose.


Hva betyr åpen kildekode, og hva går inn i et slikt prosjekt?


[FOSS](https://planb.academy/resources/glossary/foss) står for Free & Open-Source Software. Førstnevnte betyr at hvem som helst kan kopiere, endre og til og med distribuere versjoner av programvaren (til og med for å tjene penger). Sistnevnte betyr at kildekoden deles åpent, og at allmennheten oppfordres til å bidra og forbedre den.

Dette tiltrekker seg erfarne brukere som er entusiastiske når det gjelder å bidra til programvaren de allerede bruker og har nytte av, noe som til syvende og sist viser seg å være mer vellykket enn proprietær programvare. Det er i tråd med Bitcoins etos om at "informasjon lengter etter å være gratis" Det samler lidenskapelige mennesker som danner et fellesskap, og det er rett og slett morsommere. I likhet med Bitcoin er FOSS uunngåelig.


### Før vi begynner


Dette kurset består av flere deler. Mange vil bli tatt hånd om av klasselæreren din, demomiljøer som du får tilgang til, en hostet server for deg selv og eventuelt et domenenavn. Hvis du gjennomfører dette kurset på egen hånd, må du være oppmerksom på at miljøene som er merket som DEMO, ikke vil være tilgjengelige for deg.

NB. Hvis du følger dette kurset i et klasserom, kan servernavnene variere avhengig av oppsettet i klasserommet. Variablene i servernavnene kan derfor være forskjellige.


### Kursstruktur


Hvert kapittel har mål og kunnskapsvurderinger. I dette kurset vil vi gå gjennom hvert av disse og gi et sammendrag av de viktigste funksjonene på slutten av hver leksjonsblokk (dvs. kapittel). Illustrasjoner er med for å gi visuell tilbakemelding og forsterke nøkkelbegreper på en visuell måte. I begynnelsen av hver leksjonsblokk er det satt opp mål. Disse målene er mer enn en sjekkliste. De gir deg en veiledning til et nytt ferdighetssett. Kunnskapsevalueringene blir gradvis mer utfordrende etter hvert som oppsettet av BTCPay-serveren er fullført.


### Hva får studentene med seg fra kurset?


Med BTCPay Server-kurset kan en student forstå de grunnleggende prinsippene, tekniske og ikke-tekniske, for Bitcoin. Den omfattende opplæringen i bruk av Bitcoin gjennom BTCPay Server vil gjøre det mulig for studentene å drifte sin egen Bitcoin-infrastruktur.


### Viktige nettadresser eller kontaktmuligheter


BTCPay Server Foundation, som gjorde det mulig for Alekos og Bas å skrive dette kurset, ligger i Tokyo, Japan. BTCPay Server Foundation kan nås via den oppførte nettsiden.



- https://foundation.btcpayserver.org
- Bli med i de offisielle chattekanalene: https://chat.btcpayserver.org


## Introduksjon til Bitcoin


<chapterId>5c0bc234-c188-5b4a-94d5-adee87a120e2</chapterId>


### Forståelse av Bitcoin via klasseromsøvelse


Dette er en klasseromsøvelse, så hvis du tar dette kurset selv, kan du ikke utføre den, men du kan likevel gå gjennom denne øvelsen. For å fullføre denne oppgaven kreves det minst 9 til 11 personer.


Øvelsen starter etter at du har sett introduksjonen "How Bitcoin and the Blockchain works" av BBC.


:::video id=c20b6df7-0c3a-4785-94b9-42ef59093acc:::


Denne øvelsen krever minst ni deltakere. Denne øvelsen har som mål å gi en fysisk forståelse av hvordan Bitcoin fungerer. Ved å spille hver rolle i nettverket får du en interaktiv og leken måte å lære på. Denne øvelsen involverer ikke [Lightning Network](https://planb.academy/resources/glossary/lightning-network).


### Eksempel: Krever 9 / 11 personer


Rollene er..:



- 1 Kunde
- 1 Kjøpmann
- 7 til 9 Bitcoin-[noder](https://planb.academy/resources/glossary/node)


**Oppsettet er som følger:**


Kundene kjøper et produkt fra butikken med Bitcoin.


**Scenario 1 - Tradisjonelt banksystem**



- Gjør deg klar:
  - Se diagrammer/forklaringer i vedlagte Figjam - [Aktivitetsskjema](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
  - Få tre frivillige elever til å spille rollene som kunde (Alice), kjøpmann (Bob) og bank.
- Spill ut hendelsesforløpet:
  - Kunde - surfer i butikken på nettet og finner en vare til $25, som de vil ha, og informerer kjøpmannen om at de ønsker å kjøpe den
  - Selger - ber om betaling.
  - Kunden - sender kortinformasjon til forhandleren
  - Forhandler - sender informasjon til banken (identifiserer både sin egen og identiteten/informasjonen), og ber om betaling av
  - Banken innhenter informasjon om kunden og brukerstedet (Alice og Bob) og kontrollerer at kundens saldo er tilstrekkelig.
  - Trekker \$25 fra Alices konto, legger \$24 til Bobs konto, tar \$1 for tjenesten
  - Forhandleren får tommelen opp fra banken og sender varen til kunden.
- Kommentarer:
  - Bob og Alice må ha et forhold til en bank.
  - Banken innhenter identifiserende informasjon om både Bob og Alice.
  - Bank tar et kutt.
  - Banken må til enhver tid ha tillit til at hver deltakers penger er i bankens varetekt.


**Scenario 2 - Bitcoin-systemet**



- Gjør deg klar:
  - Se diagrammer/forklaringer i vedlagte Figjam - [Aktivitetsskjema](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
  - Erstatt banken med ni studenter som skal spille rollen som en datamaskin (Bitcoin Nodes/Miners) i et nettverk som skal erstatte banken.
- Hver av de ni datamaskinene har en komplett historisk oversikt over alle tidligere transaksjoner som noensinne er foretatt (og dermed nøyaktige saldoer uten forfalskninger), samt et sett med regler:
  - Kontroller at transaksjonen er riktig signert (thekeyfitsthelock)
  - Sende og motta gyldige transaksjoner til andre i nettverket, og forkaste ugyldige transaksjoner (inkludert transaksjoner som forsøker å bruke de samme pengene to ganger)
- Oppdater/legg til poster med jevne mellomrom med nye transaksjoner mottatt fra en "tilfeldig" datamaskin, forutsatt at alt innholdet er gyldig (merk: vi ignorerer foreløpig Proof of Work-komponenten i alt dette, for enkelhets skyld), ellers avviser vi disse og fortsetter som før til den neste "tilfeldige" datamaskinen sender en oppdatering
  - Det riktige beløpet ble belønnet hvis innholdet var gyldig.
- Spill ut hendelsesforløpet:
  - Kunde - surfer i butikken på nettet og finner en vare til $25 som de vil ha, og informerer kjøpmannen om at de ønsker å kjøpe den
  - Forhandler - ber om betaling ved å sende kunden en Invoice/Address fra sin Wallet.
  - Kunden - konstruerer en transaksjon (sender BTC til en verdi av 25 dollar til en Address levert av forhandleren) og sender den til Bitcoin-nettverket.
- Datamaskiner - mottar transaksjonen og verifiserer den:
  - Det er minst 25 dollar i BTC i Address som sendes fra
  - Transaksjonen er signert på riktig måte ("låst opp" av kunden)
  - Hvis dette ikke er tilfelle, vil ikke transaksjonen bli forplantet gjennom nettverket, og hvis så er tilfelle, vil den forplante seg og bli holdt i venteposisjon.
  - Forhandlere kan sjekke at transaksjonen er ventende og venter.
- En datamaskin blir "tilfeldig" valgt til å foreslå å fullføre den foreslåtte transaksjonen ved å kringkaste "en [blokk](https://planb.academy/resources/glossary/block)" som inneholder den; hvis den sjekker ut, vil de motta en BTC-belønning.
  - VALGFRI/AVANSERT - i stedet for å velge en datamaskin tilfeldig, kan du simulere Mining ved å la datamaskinene kaste terninger til et forhåndsbestemt resultat inntreffer (f.eks. at den første som slår to seksere, blir valgt)
  - Den kan også spille ut hva som vil skje hvis to datamaskiner vinner omtrent samtidig, noe som resulterer i en kjededeling.
  - Datamaskiner sjekker gyldigheten, oppdaterer/legger til poster i hovedboken hvis reglene er oppfylt, og sender transaksjonsblokken til andre datamaskiner.
  - Den tilfeldig valgte datamaskinen får en belønning for å foreslå en gyldig blokk.
  - Transaksjonen ble fullført, det vil si at pengene ble mottatt, og varen ble sendt til kunden.
- Kommentarer:
  - Legg merke til at det ikke var behov for et eksisterende bankforhold.
  - Ingen tredjeparter trengs for å legge til rette; erstattes av kodeks/insentiver.
  - Ingen datainnsamling av noen utenfor den direkte Exchange, og bare den nødvendige mengden må utveksles mellom deltakerne (f.eks. frakt Address).
  - Det kreves ingen tillit mellom personene (bortsett fra selgeren som sender varen), som ved et kontantkjøp på mange måter.
  - Pengene eies direkte av den enkelte.
  - Bitcoin Ledger er avbildet i dollar for enkelhets skyld, men i virkeligheten er det BTC.
  - Vi simulerer at en enkelt transaksjon sendes ut, men i virkeligheten er det flere transaksjoner som venter i nettverket, og blokker kan inneholde tusenvis av transaksjoner samtidig. Nodene verifiserer også at det ikke er noen transaksjoner med dobbeltforbruk på vent (jeg ville forkastet alle unntatt én i dette tilfellet).
- Juksescenarioer:
  - Hva om kunden ikke hadde $ 25 BTC?
    - De vil ikke kunne opprette transaksjonen fordi "opplåsing" og "Ownership" er det samme, og datamaskiner sjekker at transaksjonen er riktig signert; hvis ikke, avviser de den
  - Hva om den tilfeldig valgte datamaskinen forsøker å "endre Ledger"?
    - Blokkeringen vil bli avvist, ettersom alle andre datamaskiner har en fullstendig historikk og vil legge merke til endringen, som bryter med en av deres regler.
    - Random Computer ville ikke få noen belønning, og ingen transaksjoner fra blokken deres ville bli fullført.


## Vurdering av kunnskap


<chapterId>1461f064-933d-50ea-8935-324b68ec5d5f</chapterId>


### KA Diskusjon i klasserommet


Diskuter noen av forenklingene som ble gjort i klasseromsøvelsen under det andre scenariet, og beskriv mer detaljert hva det faktiske Bitcoin-systemet gjør.


### KA Gjennomgang av ordforråd


Definer følgende nøkkelbegreper som ble introdusert i forrige avsnitt:



- Knutepunkt
- [Mempool](https://planb.academy/resources/glossary/mempool)
- [Vanskelighetsgrad](https://planb.academy/resources/glossary/difficulty) Mål
- Blokk


**Diskuter betydningen av noen flere begreper i fellesskap:**


Blockchain, Transaksjon, Double-Spend, Bysantinske generalers problem, [Mining](https://planb.academy/resources/glossary/mining), Proof of Work (PoW), Hash Funksjon, Block reward, Blockchain, Lengste kjede, 51 %-angrep, Utgang, Utgangslås, Endring, [Satoshis](https://planb.academy/resources/glossary/satoshi-sat), Offentlig/privat nøkkel, Address, [Kryptografi](https://planb.academy/resources/glossary/cryptography) med [offentlig nøkkel](https://planb.academy/resources/glossary/public-key), [Digital signatur](https://planb.academy/resources/glossary/digital-signature), Wallet


# Vi introduserer BTCPay Server


<partId>9c8a2d0c-9ba1-5c39-874c-f9eaf1bba663</partId>


## Forstå innloggingsskjermen til BTCPay Server


<chapterId>14aad54c-9bd8-54f2-9455-178b8ae63408</chapterId>


### Arbeide med BTCPay Server


Målet med denne kursblokken er å få en generell forståelse av BTCPay Server-programvaren. I et delt miljø anbefales det å følge instruktørens demonstrasjon og se i kursboken BTCPay Server Coursebook for å følge med læreren. Du vil lære hvordan du oppretter en Wallet ved hjelp av flere metoder. Eksempler inkluderer Hot Wallet-oppsett og maskinvarelommebøker som er koblet til gjennom BTCPay Server Vault. Disse målene forekommer i demomiljøet, som vises og gis tilgang til av kursinstruktøren din.


Hvis du følger dette kurset på egen hånd, kan du finne en liste over tredjepartsverter for demo-formål på https://directory.btcpayserver.org/filter/hosts. Vi fraråder på det sterkeste å bruke disse tredjepartsalternativene som produksjonsmiljøer, men de tjener det rette formålet for å introdusere bruken av Bitcoin og BTCPay Server.


Som BTCPay Server rockstar-trainee har du kanskje tidligere erfaring med å sette opp en Bitcoin-node. Dette kurset er spesielt skreddersydd for BTCPay Server-programvarestakken.


Mange av alternativene i BTCPay Server finnes i en eller annen form i annen Bitcoin Wallet-relatert programvare.


### Innloggingsskjerm for BTCPay-server


Når du blir ønsket velkommen til demomiljøet, blir du bedt om å "logge inn" eller "opprette konto" Serveradministratorer kan deaktivere funksjonen for å opprette nye kontoer av sikkerhetsmessige årsaker. BTCPay Server-logoer og knappefarger kan endres fordi BTCPay Server er programvare med åpen kildekode. En tredjepartsvert kan hvitmerke programvaren og endre hele utseendet.


![image](assets/en/001.webp)


### Vinduet Opprett en konto


Opprettelse av kontoer på BTCPay Server krever gyldige Address e-poststrenger; example@email.com vil være en gyldig streng for e-post.


Passordet må bestå av minst 8 tegn, inkludert bokstaver, tall og tegn. Når du har angitt passordet én gang, må du kontrollere at passordet er det samme som det som ble skrevet inn i det første passordfeltet.


Når både e-post- og passordfeltene er riktig utfylt, klikker du på knappen "Opprett konto". Dette vil lagre e-postadressen og passordet på instruktørens BTCPay Server-forekomst.


![image](assets/en/002.webp)


**Merk!


Hvis du følger dette kurset på egen hånd, vil du sannsynligvis opprette denne kontoen på en tredjepartsvert, og derfor understreker vi igjen at disse ikke bør brukes som produksjonsmiljøer, men kun til opplæringsformål.


### Kontoopprettelse av BTCPay Server Administrator


Administratoren av BTCPay Server-forekomsten kan også opprette kontoer for BTCPay Server. Administratoren av BTCPay Server-forekomsten kan klikke på "Serverinnstillinger" (1), klikke på fanen "Brukere" (2) og klikke på knappen "+ Legg til bruker" (3) øverst til høyre i fanen Brukere. I Mål (4.3) vil du lære mer om administratorkontroll av kontoer.


![image](assets/en/003.webp)


Som administrator trenger du brukerens e-post Address og angir et standardpassord. Det anbefales at administratoren informerer brukeren om å endre dette passordet før kontoen tas i bruk, av sikkerhetsmessige årsaker. Hvis administratoren ikke angir et passord og SMTP er konfigurert på serveren, vil brukeren motta en e-post med en lenke til en invitasjon til å opprette kontoen og angi et passord selv.


### Eksempel


Når du følger kurset med en instruktør, følger du lenken fra instruktøren og oppretter kontoen din i demomiljøet. Sørg for at e-postadressen din Address og passordet ditt er lagret på en sikker måte; du vil trenge disse påloggingsopplysningene for resten av demomålene i dette kurset.


Læreren din kan ha samlet inn e-postadressen Address på forhånd og sendt en invitasjonslenke før denne øvelsen. Sjekk e-posten din hvis du har fått beskjed om det.


Når du tar kurset uten instruktør, oppretter du kontoen din ved hjelp av demomiljøet for BTCPay Server; gå til


https://Mainnet.demo.btcpayserver.org/login.


Denne kontoen skal kun brukes til demonstrasjon/opplæring og aldri til forretningsformål.


### Oppsummering av ferdigheter


I denne delen lærte du følgende:



- Slik oppretter du en konto på en hostet server via Interface.
- Hvordan en serveradministrator kan legge til brukere manuelt i serverinnstillingene.


### Vurdering av kunnskap


#### KA Konseptuell gjennomgang


Gi en begrunnelse for hvorfor det er en dårlig idé å bruke en demo-server til produksjonsformål.


## Administrere brukerkonto(er)


<chapterId>b58ca6ee-b7fc-5e81-a6aa-c8ff212b4c55</chapterId>


### Kontoadministrasjon på BTCPay Server


Etter at en butikkeier har opprettet kontoen sin, kan de administrere den nederst til venstre i BTCPay Server-brukergrensesnittet. Under knappen Konto finnes det flere innstillinger på høyere nivå.



- Mørk/lys-modus.
- Vippebryter for å skjule sensitiv informasjon.
- Administrer konto.


![image](assets/en/004.webp)


### Mørk og lys modus


Brukere av BTCPay Server kan velge mellom en lys eller mørk modusversjon av brukergrensesnittet. Kundevendte sider endres ikke. De bruker kundeprefererte innstillinger for mørk eller lys modus.


### Veksle for å skjule sensitiv informasjon


Knappen Hide Sensitive Info gir en rask og enkel Layer-sikkerhet. Når du trenger å bruke BTCPay Server, men det kan være folk som lurer over skulderen din på et offentlig sted, kan du slå på Hide Sensitive Info, og alle verdiene i BTCPay Server vil bli skjult. Noen kan kanskje se deg over skulderen, men kan ikke lenger se verdiene du håndterer.


### Administrer konto


Når brukerkontoen er opprettet, er det her du kan administrere passord, 2FA eller API-nøkler.


### Administrer konto - Konto


Du kan eventuelt oppdatere kontoen din med en annen e-post Address. For å sikre at e-postadressen din Address er riktig, lar BTCPay Server deg sende en bekreftelses-e-post. Klikk på lagre hvis brukeren angir en ny e-post Address og bekrefter at bekreftelsen fungerte. Brukernavnet forblir det samme som den forrige e-posten.


En bruker kan velge å slette hele kontoen sin. Dette kan gjøres ved å klikke på sletteknappen i Konto-fanen.


![image](assets/en/005.webp)


**Merk!


Etter at du har endret e-postadressen, endres ikke brukernavnet for kontoen. Den tidligere oppgitte e-postadressen Address vil fortsatt være påloggingsnavnet.


### Administrer konto - Passord


En student ønsker kanskje å endre passordet sitt. Dette kan gjøres ved å gå til fanen Passord. Her må han eller hun skrive inn det gamle passordet og kan endre det til et nytt.


![image](assets/en/006.webp)


### To-faktor autentisering (2fa)


For å begrense konsekvensene av et stjålet passord kan du bruke tofaktorautentisering (2FA), som er en relativt ny sikkerhetsmetode. Du kan aktivere tofaktorautentisering via Administrer konto og fanen for tofaktorautentisering. Du må fullføre et nytt trinn etter at du har logget inn med brukernavn og passord.


BTCPay Server støtter to metoder for å aktivere 2FA: appbasert 2FA (Authy, Google, Microsoft Authenticators) eller gjennom sikkerhetsenheter (FIDO2 eller LNURL Auth).


### To-faktor autentisering - App-basert


Basert på mobiltelefonens operativsystem (Android eller iOS) kan brukerne velge mellom følgende apper;


1. Last ned en tofaktorautentisering.


   - Authy for [Android](https://play.google.com/store/apps/details?id=com.authy.authy) eller [iOS](https://apps.apple.com/us/app/authy/id494168017)
   - Microsoft Authenticator for [Android](https://play.google.com/store/apps/details?id=com.azure.authenticator) eller [iOS](https://apps.apple.com/us/app/microsoft-authenticator/id983156458)
   - Google Authenticator for [Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=e%C2%80) eller [iOS](https://apps.apple.com/us/app/google-authenticator/id388497605)

2. Etter at du har lastet ned og installert Authenticator-appen.


   - Skann QR-koden fra BTCPay Server
   - Eller skriv inn den genererte nøkkelen fra BTCPay Server manuelt i Authenticator-appen din.

3. Authenticator-appen vil gi deg en unik kode. Skriv inn den unike koden i BTCPay Server for å bekrefte oppsettet, og klikk på bekreft for å fullføre prosessen.


![image](assets/en/007.webp)


### Oppsummering av ferdigheter


I denne delen lærte du følgende:



- Alternativer for kontoadministrasjon og de ulike måtene å administrere en konto på en BTCPay Server-forekomst.
- Slik konfigurerer du appbasert 2FA.


### Vurdering av kunnskap


#### KA Konseptuell gjennomgang


Beskriv hvordan appbasert 2FA bidrar til å sikre kontoen din.


## Opprette en ny butikk


<chapterId>463b3634-b49f-5512-a711-3b2e096fc2e0</chapterId>


### Opprett butikkveiviseren din


Når en ny bruker logger seg på BTCPay Server, er miljøet tomt og trenger en første butikk. Introduksjonsveiviseren til BTCPay Server gir brukeren muligheten til å "Opprett din butikk" (1). En butikk kan sees på som et hjem for dine Bitcoin-behov. En ny BTCPay Server Node vil starte med å synkronisere Bitcoin Blockchain (2). Avhengig av hvilken infrastruktur du kjører BTCPay Server på, kan dette ta alt fra noen timer til noen dager. Forekomstens gjeldende versjon vises nederst i høyre hjørne av BTCPay Server-brukergrensesnittet. Dette er nyttig som referanse ved feilsøking.


![image](assets/en/008.webp)


### Opprett butikkveiviseren din


Når du følger dette kurset, vil du starte med et litt annet skjermbilde enn på forrige side. Ettersom instruktøren har klargjort demomiljøet, har Bitcoin Blockchain blitt synkronisert på forhånd, og du vil derfor ikke se nodenes synkroniseringsstatus.


En bruker kan velge å slette hele kontoen sin. Dette kan gjøres ved å klikke på sletteknappen i Konto-fanen.


![image](assets/en/009.webp)


**Merk!


BTCPay Server-kontoer kan opprette et ubegrenset antall butikker. Hver butikk er en Wallet eller et "hjem".


### Eksempel


Begynn med å klikke på "Opprett butikk".


![image](assets/en/010.webp)


Dette vil opprette ditt første hjem og dashbord for bruk av BTCPay Server.


(1) Etter at du har klikket på "Opprett din butikk", vil BTCPay Server kreve at du navngir butikken; dette kan være hva som helst som er nyttig for deg.


![image](assets/en/011.webp)


(2) Deretter må du angi en standard butikkvaluta, enten en fiat-valuta eller en valuta denominert i Bitcoin eller Sats. For demomiljøet setter vi den til USD.


![image](assets/en/012.webp)


(3) Som en siste parameter i butikkoppsettet krever BTCPay Server at du angir en "Foretrukket priskilde" for å sammenligne Bitcoins pris mot den gjeldende fiat-prisen, slik at butikken din viser riktig Exchange-kurs mellom Bitcoin og den butikkinnstilte fiat-valutaen. Vi holder oss til standardinnstillingen i demo-eksemplet og setter denne til Kraken Exchange. BTCPay Server bruker Kraken API for å sjekke Exchange-kursene.


![image](assets/en/013.webp)


(4) Nå som disse butikkparametrene er angitt, klikker du på Opprett-knappen, og BTCPay Server oppretter den første butikkens dashbord, der veiviseren vil fortsette.


![image](assets/en/014.webp)


Gratulerer, du har opprettet din første butikk, og dette er slutten på denne øvelsen.


![image](assets/en/015.webp)


### Oppsummering av ferdigheter


I denne delen har du lært:



- Opprettelse av butikk og konfigurering av standardvaluta, kombinert med preferanser for priskilde.
- Hver "butikk" er et nytt hjem atskilt fra andre butikker på denne installasjonen av BTCPay Server.


# Introduksjon til sikring av Bitcoin-nøkler


<partId>25da22d8-fd37-51c5-af2a-58b9f3b046b2</partId>


## Forståelse av generering av Bitcoin-nøkler


<chapterId>d162735b-847b-578e-83b8-a044ab703ec5</chapterId>


### Hva er involvert i generering av Bitcoin-nøkler?


Bitcoin lommebøker, når de opprettes, skaper en såkalt "[seed](https://planb.academy/resources/glossary/seed)". I det siste målet opprettet du en "seed", Ordserien som ble generert før, er også kjent som Mnemonic-fraser. seed brukes til å utlede individuelle Bitcoin-nøkler og brukes til å sende eller motta Bitcoin. seed-fraser skal aldri deles med tredjeparter eller ikke-klarerte motparter.


seed-generering utføres i henhold til industristandarden kjent som "Hierarchical Deterministic"-rammeverket (HD).


![image](assets/en/016.webp)


### Adresser


BTCPay Server er bygget for å generate en ny Address. Dette lindrer problemet med gjenbruk av offentlige nøkler eller Address. Ved å bruke den samme offentlige nøkkelen blir det veldig enkelt å spore hele betalingshistorikken din. Hvis du tenker på nøkler som engangskuponger, vil det forbedre personvernet ditt betydelig. Vi bruker også Bitcoin-adresser, men ikke forveksle disse med offentlige nøkler.


En Address blir avledet fra den offentlige nøkkelen gjennom en "hashing-algoritme" De fleste lommebøker og transaksjoner vil imidlertid vise adresser i stedet for de offentlige nøklene. Adresser er generelt kortere enn offentlige nøkler og begynner vanligvis med `1`, `3` eller `bc1`, mens offentlige nøkler begynner med `02`, `03` eller `04`.



- Adresser som begynner med `1.....` er fortsatt svært vanlige adresser. Som nevnt i kapittelet "Opprette en ny butikk", er dette eldre adresser. Denne Address-typen er ment for P2PKH-transaksjoner. P2PKH bruker Base58-koding, noe som gjør at Address skiller mellom store og små bokstaver. Strukturen er basert på den offentlige nøkkelen med et ekstra siffer som identifikator.



- Adresser som begynner med `bc1...` er i ferd med å bli svært vanlige adresser. Disse er kjent som (opprinnelige) [SegWit](https://planb.academy/resources/glossary/segwit)-adresser. Disse tilbyr en bedre avgiftsstruktur enn de andre nevnte adressene. Native SegWit-adresser bruker Bech32-koding og tillater bare små bokstaver.



- Adresser som begynner med `3...` brukes fortsatt ofte av børser for innskuddsadresser. Disse adressene er nevnt i kapittelet "Opprette en ny butikk", innpakkede eller nestede SegWit-adresser. De kan imidlertid også fungere som en "Multisig Address". Når de brukes som en SegWit Address, er det noen besparelser på [transaksjonsgebyrer](https://planb.academy/resources/glossary/transaction-fees), men igjen mindre enn med innfødte SegWit. P2SH-adresser bruker Base58-koding. Dette gjør den case-sensitiv, som den eldre Address.



- Adresser som begynner med `2...` er Testnet-adresser. De er ment å motta Testnet Bitcoin (tBTC). Du bør aldri blande dette sammen og sende Bitcoin til disse adressene. For utviklingsformål kan du generate en Testnet Wallet. Det finnes flere kraner på nettet for å få Testnet Bitcoin. Du må aldri kjøpe Testnet Bitcoin. Testnet Bitcoin er utvunnet. Dette kan være en grunn for en utvikler til å bruke Regtest i stedet. Dette er et lekeplassmiljø for utviklere, og mangler visse nettverkskomponenter. Bitcoin er imidlertid svært nyttig for utviklingsformål.


### Offentlige nøkler


Offentlige nøkler er mindre brukt i praksis i dag. Over tid har Bitcoin-brukere erstattet dem med adresser i stedet. De finnes fortsatt, og de brukes fortsatt av og til. Offentlige nøkler er generelt sett mye lengre strenger enn adresser. Akkurat som med adresser starter de med en spesifikk identifikator.



- For det første er `02...` og `03...` veldig standard offentlige nøkkelidentifikatorer kodet i SEC-format. Disse kan behandles og gjøres om til adresser for mottak, brukes til å opprette multi-sig-adresser eller til å verifisere en signatur. Tidlige Bitcoin-transaksjoner brukte offentlige nøkler som en del av P2PK-transaksjoner.



- HD-lommebøker bruker imidlertid en annen struktur. `xpub...`, `ypub...` eller `zpub...` kalles utvidede offentlige nøkler, eller [xpubs](https://planb.academy/resources/glossary/xpub). Disse nøklene brukes til å utlede mange offentlige nøkler som en del av HD Wallet. Ettersom xpuben din inneholder hele historikken din, det vil si tidligere og fremtidige transaksjoner, må du aldri dele disse med parter som ikke er til å stole på.


### Oppsummering av ferdigheter


I denne delen lærte du følgende:



- Forskjellene mellom adresser og offentlige nøkkeldatatyper og fordelene ved å bruke adresser fremfor offentlige nøkler.


### Vurdering av kunnskap


Beskriv fordelen med å bruke nye adresser for hver transaksjon sammenlignet med gjenbruk av Address eller metoder med offentlig nøkkel.


## Sikring av nøkler med en Hardware Wallet


<chapterId>c54a6d61-5a43-5fdb-93ae-c6750de9c612</chapterId>


### Oppbevaring av Bitcoin-nøkler


Etter at du har generert en seed-frase, må listen med 12-24 ord som genereres i denne boken, sikkerhetskopieres og sikres på riktig måte, ettersom disse ordene er den eneste måten å gjenopprette tilgangen til en Wallet på. Strukturen til HD-lommebøker og hvordan den genererer adresser deterministisk ved hjelp av en enkelt seed betyr at alle adressene du oppretter, vil bli sikkerhetskopiert ved hjelp av denne ene listen med Mnemonic-ord, som representerer din seed- eller gjenopprettingsfrase.


Hold gjenopprettingsfrasen din sikker. Hvis noen får tilgang til den, spesielt med ondsinnede hensikter, kan de flytte pengene dine. Hold seed trygt og sikkert, samtidig som du husker at det er gjensidig mellom dem. Det finnes flere metoder for lagring av private Bitcoin-nøkler, hver med sine egne fordeler og ulemper når det gjelder sikkerhet, personvern, bekvemmelighet og fysisk lagring. På grunn av viktigheten av private nøkler har Bitcoin-brukere en tendens til å lagre og oppbevare disse nøklene på en trygg måte i "selvforvaring" i stedet for å bruke "depottjenester" som banker. Avhengig av brukeren må de enten bruke en Cold-lagringsløsning eller en Hot Wallet.


### Hot og Cold lagring av Bitcoin-nøkler


Vanligvis er Bitcoin-lommebøker denominert i en Hot Wallet eller en Cold Wallet. De fleste avveiningene ligger i bekvemmelighet, brukervennlighet og sikkerhetsrisiko. Hver av disse metodene kan også ses i en depotløsning. Avveiningene her er imidlertid for det meste sikkerhets- og personvernbaserte og går utover omfanget av dette kurset.


### Hot Wallet


Hot-lommebøker er den mest praktiske måten å samhandle med Bitcoin på via mobil-, nett- eller skrivebordsprogramvare. Wallet er alltid koblet til internett, slik at brukerne kan sende eller motta Bitcoin. Dette er imidlertid også dens svakhet; ettersom Wallet alltid er online, er den nå mer sårbar for angrep fra hackere eller skadelig programvare på enheten din. I BTCPay Server lagrer Hot-lommebøker de private nøklene på forekomsten. Alle som får tilgang til BTCPay Server-butikken din, kan potensielt stjele penger fra denne Address hvis de er ondsinnede. Når BTCPay Server kjører i et hostet miljø, bør du alltid ta hensyn til dette i sikkerhetsprofilen din og helst ikke bruke en Hot Wallet i et slikt tilfelle. Når BTCPay Server er installert på maskinvare som eies og sikres av deg, blir risikoprofilen betydelig lavere, men den forsvinner aldri helt.


### Cold Wallet


Privatpersoner flytter Bitcoin til en Cold Wallet fordi den kan isolere de private nøklene fra internett, og dermed beskytte dem mot potensielle trusler på nettet. Ved å fjerne internettforbindelsen fra ligningen reduseres risikoen for skadelig programvare, spionprogrammer og SIM-bytte. Cold-lagring antas å være bedre enn Hot-lagring når det gjelder sikkerhet og autonomi, forutsatt at det tas tilstrekkelige forholdsregler for å hindre at de private nøklene i Bitcoin går tapt. Cold-lagring er best egnet for store mengder Bitcoin, som ikke er ment å bli brukt ofte på grunn av Wallet-oppsettets kompleksitet.


Det finnes ulike metoder for å lagre Bitcoin-nøkler i Cold-lagring, fra papirlommebøker til hjernelommebøker, maskinvarelommebøker eller, fra begynnelsen av, en Wallet-fil. De fleste lommebøker bruker [BIP](https://planb.academy/resources/glossary/bip) 39 til generate seed frasen. Innenfor Bitcoin core-programvaren er det imidlertid ennå ikke oppnådd enighet om bruken av den. Bitcoin core-programvaren vil fortsatt generate en Wallet.dat-fil, som du må lagre på et sikkert frakoblet sted.


### Oppsummering av ferdigheter


I denne delen har du lært:



- Forskjellene mellom Hot- og Cold-lommebøker når det gjelder funksjonalitet og avveininger.


### Kunnskapsvurdering Konseptuell gjennomgang



- Hva er en Wallet?



- Hva er forskjellen mellom Hot og Cold lommebøker?



- Beskriv hva som menes med å "generere en Wallet"?


## Bruke Bitcoin-tastene dine


<chapterId>bff488de-5052-56e6-b696-97e896f762ae</chapterId>


### BTCPay-server Wallet


BTCPay Server består av følgende standard Wallet-funksjoner:



- Transaksjoner
- Send
- Motta
- Rescan
- Trekk betalinger
- Utbetalinger
- [PSBT](https://planb.academy/resources/glossary/psbt)
- Generelle innstillinger


### Transaksjoner


Administratorer kan se innkommende og utgående transaksjoner for On-Chain Wallet som er koblet til denne spesifikke butikken i transaksjonsvisningen. Hver transaksjon har et skille mellom mottatte og sendte beløp. Mottatte vil være Green, og utgående transaksjoner vil være røde. I BTCPay Server-transaksjonsvisningen vil administratorer også se et sett med standardetiketter.



| Transaksjonstype | Beskrivelse                                      |
| ----------------- | ------------------------------------------------ |
| App               | Betaling ble mottatt via en app-opprettet faktura |
| Faktura           | Betaling ble mottatt via en faktura               |
| [Payjoin](https://planb.academy/resources/glossary/payjoin)           | Ikke betalt, fakturatimeren har ennå ikke utløpt  |
| Payjoin-eksponert | [UTXO](https://planb.academy/resources/glossary/utxo) ble eksponert via et payjoin-forslag i en faktura |
| Betalingsforespørsel | Betaling ble mottatt via en betalingsforespørsel |
| Utbetaling        | Betaling ble sendt via en utbetaling eller refusjon |

### Hvordan sende


BTCPay-serverens sendefunksjon sender transaksjoner fra din BTCPay-server On-Chain Wallet. BTCPay Server tillater flere måter å signere transaksjonene dine på for å bruke penger. En transaksjon kan signeres med;



- Hardware Wallet
- Lommebøker som støtter PSBT
- HD-privatnøkkel eller gjenopprettingsfrø.
- Hot Wallet


#### Hardware Wallet


BTCPay Server har innebygd støtte for Hardware Wallet, slik at du kan bruke Hardware Wallet med BTCPay Vault uten å lekke informasjon til tredjepartsapper eller -servere. Hardware Wallet-integrasjonen i BTCPay Server gjør at du kan importere Hardware Wallet og bruke innkommende midler med en enkel bekreftelse på enheten din. De private nøklene dine forlater aldri enheten, og alle midler valideres mot din Full node, noe som sikrer at ingen data lekker ut.


#### Signering med en Wallet som støtter PSBT


PSBT (delvis signerte Bitcoin-transaksjoner) er et utvekslingsformat for Bitcoin-transaksjoner som fortsatt ikke er fullstendig signert. PSBT støttes i BTCPay Server og kan signeres med kompatible maskinvare- og programvarelommebøker.


Konstruksjonen av en fullstendig signert Bitcoin-transaksjon går gjennom følgende trinn:



- En PSBT blir konstruert med spesifikke innganger og utganger, men ingen signaturer
- Den eksporterte PSBT kan importeres av en Wallet som støtter dette formatet
- Transaksjonsdataene kan inspiseres og signeres ved hjelp av Wallet
- Den signerte PSBT-filen blir eksportert fra Wallet og importert med BTCPay Server
- BTCPay Server produserer den endelige Bitcoin-transaksjonen
- Du verifiserer resultatet og sender det til nettverket


#### Signering med privat HD-nøkkel eller Mnemonic seed


Hvis du har opprettet en Wallet før du bruker BTCPay Server, kan du bruke pengene ved å skrive inn den private nøkkelen din i et passende felt. Angi en riktig "AccountKeyPath" i Wallet> Innstillinger; ellers kan du ikke bruke.


#### Signering med en Hot Wallet


Hvis du opprettet en ny Wallet da du satte opp butikken og aktiverte den som en Hot Wallet, vil den automatisk bruke seed som er lagret på en server for å signere.


### RBF (Replace-by-fee)


Replace-by-fee (RBF) er en Bitcoin-protokollfunksjon som lar deg erstatte en tidligere kringkastet transaksjon (mens den fortsatt er ubekreftet). Dette gjør det mulig å randomisere Wallet-transaksjonens fingeravtrykk eller erstatte den med en høyere gebyrsats for å flytte transaksjonen høyere i køen med bekreftelsesprioritet (Mining). Dette vil effektivt erstatte den opprinnelige transaksjonen ettersom den høyere gebyrsatsen vil bli prioritert, og når den er bekreftet, vil den ugyldiggjøre den opprinnelige transaksjonen (ingen dobbeltbruk).


Trykk på knappen "Avanserte innstillinger" for å vise alternativene for RBF.


![image](assets/en/017.webp)



- Randomize for bedre personvern gjør det mulig å erstatte transaksjonen automatisk for randomisering av transaksjonens fingeravtrykk.
- Ja, flagg transaksjonen for RBF og bli erstattet eksplisitt (ikke erstattet som standard, kun ved input)
- Nei, ikke la transaksjonen bli erstattet.


### Coin Utvalg


Coin-valg er en avansert personvernfunksjon som lar deg velge mynter du vil bruke når du utarbeider en transaksjon. For eksempel ved å betale med mynter som kommer fra en conjoin-mix.


Coin-valg fungerer naturlig med Wallet-etikettfunksjonen. Dette lar deg merke innkommende midler for enklere UTXO-administrasjon og -bruk.


BTCPay Server støtter BIP-329 for etikettadministrasjon. Hvis du overfører fra en Wallet som støtter BIP-329 og har angitt etiketter, vil BTCPay Server gjenkjenne og importere dem automatisk. Ved migrering av servere kan denne informasjonen også eksporteres og importeres til det nye miljøet.


### Hvordan motta


Når du klikker på mottaksknappen i BTCPay Server, genereres det en ubrukt Address som kan brukes til å motta betalinger. Administratorer kan også generate en ny Address ved å opprette en ny "Invoice"


BTCPay Server vil alltid be deg om å generate følgende tilgjengelige Address for å forhindre gjenbruk av Address. Etter å ha klikket på "generate neste tilgjengelige BTC Address", genererer BTCPay Server en ny Address og QR. Det lar deg også sette en [etikett](https://planb.academy/resources/glossary/label) direkte til Address for bedre administrasjon av adressene dine.


![image](assets/en/018.webp)


![image](assets/en/019.webp)


#### Skann på nytt


Rescan-funksjonen er avhengig av Bitcoin core 0.17.0s "Scantxoutset" for å skanne den nåværende tilstanden til Blockchain (kalt UTXO Set) for mynter som tilhører den konfigurerte avledningsordningen. En Wallet-skanning løser to vanlige problemer som BTCPay Server-brukere ofte støter på.


1. Gap-grenseproblem - De fleste tredjeparts lommebøker er lette lommebøker som deler en node mellom mange brukere. Lette og Full node-avhengige lommebøker begrenser antallet (vanligvis 20) adresser uten saldo de sporer på Blockchain for å forhindre ytelsesproblemer. BTCPay Server genererer en ny Address for hver Invoice. Med det ovennevnte i bakhodet, etter at BTCPay Server har generert 20 ubetalte fakturaer på rad, slutter den eksterne Wallet å hente transaksjonene, forutsatt at ingen nye transaksjoner har skjedd. Din eksterne Wallet vil ikke vise dem når fakturaene er betalt den 21., 22. osv. På den annen side sporer BTCPay Server Wallet internt alle Address den genererer, sammen med en betydelig høyere gap-grense. Den er ikke avhengig av en tredjepart og kan alltid vise en korrekt saldo.

2. Gap-limit-løsningen - Hvis din [eksterne/eksisterende Wallet](https://docs.btcpayserver.org/WalletSetup/#use-an-existing-Wallet) tillater konfigurasjon av gap-limit, er den enkle løsningen å øke den. De fleste lommebøker tillater imidlertid ikke dette. De eneste lommebøkene som for øyeblikket støtter gap-limit-konfigurasjon som vi kjenner til, er Electrum, Wasabi og Sparrow wallet. Dessverre vil du sannsynligvis støte på problemer med mange andre lommebøker. For best mulig brukeropplevelse og personvern bør du vurdere å bruke BTCPay-serverens interne Wallet i stedet for eksterne lommebøker.


#### BTCPay Server bruker "mempoolfullrbf=1"


BTCPay Server bruker "mempoolfullrbf=1"; vi har lagt til dette som standard i oppsettet av BTCPay Server. Vi har imidlertid også gjort det til en funksjon du kan deaktivere selv. Uten "mempoolfullrbf=1", hvis en kunde dobbeltspenderer en betaling med en transaksjon som ikke signaliserer RBF, vil selgeren først få vite det etter bekreftelse.


Det kan være lurt for en administrator å velge bort denne innstillingen. Du kan endre standardinnstillingen ved hjelp av følgende streng.


```
BTCPAYGEN_EXCLUDE_FRAGMENTS="$BTCPAYGEN_EXCL UDE_FRAGMENTS;opt-mempoolfullrbf"
. btcpay-setup.sh -i
```


### BTCPay Server Wallet-innstillinger


Wallet-innstillingene i BTCPay Server gir en klar og tydelig oversikt over de generelle innstillingene for din Wallet. Alle disse innstillingene er forhåndsutfylt hvis Wallet ble opprettet med BTCPay Server.


![image](assets/en/020.webp)


Wallet-innstillingene i BTCPay Server gir en klar og tydelig oversikt over Wallets generelle innstillinger. Alle disse innstillingene er forhåndsutfylt hvis Wallet ble opprettet med BTCPay Server. Wallet-innstillingene i BTCPay Server starter med Wallet-statusen. Er det en Watch-only eller en Hot Wallet? Avhengig av Wallet-typen kan handlingene variere, inkludert å skanne Wallet på nytt for manglende transaksjoner, fjerne gamle transaksjoner fra historikken, registrere Wallet for betalingskoblinger eller erstatte og slette den nåværende Wallet-en som er knyttet til butikken. I BTCPay Servers Wallet-innstillinger kan administratorer angi en etikett for Wallet for bedre Wallet-administrasjon. Her vil administratoren også kunne se avledningsskjema, kontonøkkel (xpub), fingeravtrykk og nøkkelbane. Betalinger i Wallet-innstillingene har bare to hovedinnstillinger. Betaling er ugyldig hvis transaksjonen ikke bekreftes innen (angitte minutter) etter utløpet av Invoice. Betrakt Invoice som bekreftet når betalingstransaksjonen har X antall bekreftelser. Administratorer kan også angi en veksling for å vise anbefalte gebyrer på betalingsskjermen eller angi et manuelt bekreftelsesmål i antall blokker.


![image](assets/en/021.webp)


**Merk!


Hvis du følger dette kurset på egen hånd, vil du sannsynligvis opprette denne kontoen på en tredjepartsvert. Derfor anbefaler vi igjen at disse ikke brukes som produksjonsmiljøer, men kun til opplæringsformål.


### Eksempel


#### Sett opp en Bitcoin Wallet i BTCPay Server


BTCPay Server tilbyr to metoder for å sette opp en Wallet. Den ene måten er å importere en eksisterende Bitcoin Wallet. Importen kan gjøres ved å koble til en Hardware Wallet, importere en Wallet-fil, legge inn en utvidet offentlig nøkkel, skanne en Wallets QR-kode eller, minst gunstig, legge inn en tidligere opprettet Wallet-gjenoppretting seed for hånd. I BTCPay Server er det også mulig å opprette en ny Wallet. Det er to mulige måter å konfigurere BTCPay Server på når du genererer en ny Wallet.


Hot Wallet-alternativet i BTCPay Server muliggjør funksjoner som 'PayJoin' eller 'Liquid'. Det er imidlertid en ulempe: Gjenopprettings-seed generert for denne Wallet vil bli lagret på serveren, der alle med administratorkontroll kan hente den. Ettersom den private nøkkelen din er avledet fra gjenopprettings-seed, kan en ondsinnet aktør få tilgang til dine nåværende og fremtidige midler!


For å redusere denne risikoen i BTCPay Server kan en administrator sette verdien i Serverinnstillinger > Policyer > "Tillat ikke-administratorer å opprette Hot-lommebøker for butikkene sine" til "nei", ettersom det er standardverdien. For å forbedre sikkerheten til disse Hot-lommebøkene bør serveradministratoren aktivere 2FA-autentisering på kontoer som har tillatelse til å ha Hot-lommebøker. Lagring av private nøkler på en offentlig server er en farlig praksis og medfører betydelige risikoer. Noen av dem ligner på Lightning Network-risikoene (se neste kapittel for Lightning Network-risikoer).


Det andre alternativet BTCPay Server tilbyr for å generere en ny Wallet er ved å opprette en Watch-only wallet. BTCPay Server vil generate dine private nøkler én gang. Etter at brukeren har bekreftet å ha skrevet ned sin seed-setning, vil BTCPay Server slette de private nøklene fra serveren. Som et resultat har butikken din nå en Watch-only wallet koblet til den. For å bruke pengene du har mottatt på din Watch-only wallet, se kapittelet Hvordan sende, enten ved å bruke BTCPay Server Vault, PSBT (Partially Signed Bitcoin Transaction), eller, minst anbefalt, ved å manuelt oppgi din seed-frase.


Du opprettet en ny "Store" i den siste delen. Installasjonsveiviseren fortsetter med å be deg om å "Sette opp en Wallet" eller "Sette opp en Lightning-node". I dette eksemplet vil du følge veiviserprosessen "Sett opp en Wallet" (1).


![image](assets/en/022.webp)


Etter at du har klikket på "Sett opp en Wallet", fortsetter veiviseren med å spørre hvordan du vil fortsette; BTCPay Server tilbyr nå muligheten til å koble en eksisterende Bitcoin Wallet til den nye butikken din. Hvis du ikke har en Wallet, foreslår BTCPay Server at du oppretter en ny. Dette eksemplet følger trinnene for å "opprette en ny Wallet" (2). Følg trinnene for å lære hvordan du "kobler til en eksisterende Wallet (1).


![image](assets/en/023.webp)


**Merk!


Hvis du tar dette kurset i et klasserom, må du være oppmerksom på at det aktuelle eksempelet og seed som vi har generert, kun er ment for undervisningsformål. Det skal aldri være noe vesentlig annet enn det som kreves gjennom øvelsene på disse adressene.


(1) Fortsett veiviseren "Ny Wallet" ved å klikke på knappen "Opprett en ny Wallet".


![image](assets/en/024.webp)


(2) Når du har klikket på "Opprett en ny Wallet", vil det neste vinduet i veiviseren gi alternativene "Hot Wallet" og "Watch-only wallet" Hvis du følger med en instruktør, er miljøet ditt en delt Demo, og du kan bare opprette en Watch-only wallet. Legg merke til forskjellen mellom de to figurene nedenfor. Når du befinner deg i demomiljøet og følger med instruktøren, oppretter du en "Watch-only wallet" og fortsetter med veiviseren "Ny Wallet".


![image](assets/en/025.webp)


![image](assets/en/026.webp)


(3) Fortsetter du med den nye Wallet-veiviseren, er du nå i Opprett BTC Watch-only wallet-delen. Her får vi angi Wallets "Address-type" BTCPay Server lar deg velge din foretrukne Address-type; i skrivende stund anbefales det fortsatt å bruke bech32-adresser. Du kan lære mer om adresser i første kapittel i denne delen.



- SegWit (bech32)
  - Innfødte SegWit-adresser begynner med `bc1q`.
  - Eksempel: `bc1qXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`
- Arven
  - Legacy-adresser er adresser som begynner med tallet `1`.
  - Eksempel: `15e15hXXXXXXXXXXXXXXXXXXXXXXXXXXXX`
- Taproot (For avanserte brukere)
  - Taproot-adresser begynner med `bc1p`.
  - Eksempel: `bc1pXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`
- SegWit innpakket
  - SegWit-innpakkede adresser begynner med `3`.
  - Eksempel: `37BBXXXXXXXXXXXXXXXXXXXXX`


Velg SegWit (anbefalt) som din foretrukne Wallet Address-type.


![image](assets/en/027.webp)


(4) Når parameteren for Wallet stilles inn, tillater BTCPay Server brukerne å stille inn en valgfri passphrase gjennom BIP39; husk å bekrefte passordet ditt.


![image](assets/en/028.webp)


(5) Etter at du har angitt Wallets Address-type og muligens angitt noen avanserte alternativer, klikker du på Opprett, og BTCPay Server vil generate din nye Wallet. Merk at dette er det siste trinnet før du genererer seed frasen din. Sørg for at du bare gjør dette i et miljø der noen ikke kan stjele seed-frasen ved å se på skjermen din.


![image](assets/en/029.webp)


(6) I det følgende skjermbildet i veiviseren viser BTCPay Server deg Recovery seed-frasen for din nylig genererte Wallet; dette er nøklene til å gjenopprette Wallet og signere transaksjoner. BTCPay Server genererer en seed-frase på 12 ord. Disse ordene vil bli slettet fra serveren etter dette oppsettskjermbildet. Denne Wallet er spesifikt en Watch-only wallet. Det anbefales ikke å lagre denne seed-frasen digitalt eller med fotografisk bilde. Brukere kan bare gå videre i veiviseren hvis de aktivt bekrefter at de har skrevet ned seed-frasen sin.


![image](assets/en/030.webp)


(7) Etter at du har klikket på Ferdig og sikret den nylig genererte Bitcoin seed-setningen, vil BTCPay Server oppdatere butikken din med den vedlagte nye Wallet og er klar til å motta betalinger. I brukerens Interface, i navigasjonsmenyen til venstre, legger du merke til hvordan Bitcoin nå er uthevet og aktivert under Wallet.


![image](assets/en/031.webp)


### Eksempel: Skrive ned en seed-frase


Dette er et spesielt sikkert tidspunkt å bruke Bitcoin på. Som nevnt tidligere, er det bare du som skal ha tilgang til eller kunnskap om seed-frasen din. Ettersom du følger med en instruktør og et klasserom, skal seed som genereres, bare brukes i dette emnet. Det er for mange faktorer, inkludert nysgjerrige øyne fra klassekamerater, usikre systemer og annet, som gjør at disse nøklene kun er pedagogiske og upålitelige. De genererte nøklene bør likevel lagres for kurseksempler.


Den første metoden vi vil bruke i denne situasjonen, som også er den minst sikre, er å skrive ned seed-frasen i riktig rekkefølge. Et seed-frasekort er inkludert i kursmaterialet som studenten får, eller kan finnes på BTCPay Server GitHub. Vi vil bruke dette kortet til å skrive ned ordene som ble generert i forrige trinn. Sørg for å skrive dem ned i riktig rekkefølge. Etter at du har skrevet dem ned, kan du sjekke dem opp mot det som ble gitt av programvaren for å sikre at du skrev dem ned i riktig rekkefølge. Når du har skrevet dem ned, klikker du i avmerkingsboksen for å bekrefte at du har skrevet ned seed-frasen på riktig måte.


### Eksempel: Lagring av en seed-frase på en Hardware Wallet


I dette kurset tar vi for oss lagring av en seed-frase på en Hardware Wallet. Hvis du følger dette kurset med en instruktør, kan det noen ganger inkludere en slik enhet. I kursmaterialet har vi samlet en liste over maskinvarelommebøker som egner seg for denne øvelsen.


I dette eksemplet bruker vi BTCPay Server hvelv og en Blockstream Jade Hardware Wallet.


Du kan også følge med på en videoguide om hvordan du kobler til en Hardware Wallet.

:::video id=8e61664b-e0c0-416d-8ef9-b631bf28ec4d:::


Last ned BTCPay Server Vault: https://github.com/btcpayserver/BTCPayServer.Vault/releases


Sørg for at du laster ned de riktige filene for ditt spesifikke system. Windows-brukere bør laste ned pakken [BTCPayServerVault-2.0.5-setup.exe](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-2.0.5-setup.exe), Mac-brukere bør laste ned pakken [BTCPayServerVault-osx-x64-2.0.5.dmg](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-osx-x64-2.0.5.dmg), og Linux-brukere bør laste ned pakken [BTCPayServerVault-Linux-2.0.5.tar.gz](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-Linux-2.0.5.tar.gz)


Etter at du har installert BTCPay Server Vault, starter du programvaren ved å klikke på ikonet på skrivebordet. Når BTCPay Server Vault er riktig installert og startet for første gang, vil den be om tillatelse til å bli brukt med webapplikasjoner. Den vil be om å få tilgang til den spesifikke BTCPay Serveren du arbeider med. Godta disse betingelsene. BTCPay Server Vault vil nå søke etter maskinvareenheten. Når enheten er funnet, vil BTCPay Server gjenkjenne at Vault kjører og har hentet enheten din.


**Merk!


Ikke gi SSH-nøklene eller serveradministratorkontoen din til andre enn administratorer når du bruker en Hot Wallet. Alle med tilgang til disse kontoene vil ha tilgang til midlene i Hot Wallet.


### Oppsummering av ferdigheter


I denne delen lærte du følgende:



- Transaksjonsvisningen av Bitcoin Wallet og dens ulike kategoriseringer.
- Det finnes ulike alternativer når du sender fra en Bitcoin Wallet, fra maskinvare til Hot lommebøker.
- Problemet med gap-grensen ved bruk av de fleste lommebøker, og hvordan dette kan løses.
- Hvordan generate en ny Bitcoin Wallet i BTCPay Server, inkludert lagring av nøklene i en Hardware Wallet og sikkerhetskopiering av gjenopprettingsfrasen.


I dette målet har du lært hvordan du generate oppretter en ny Bitcoin Wallet i BTCPay Server. Vi har ennå ikke gått inn på hvordan du sikrer eller bruker disse nøklene. I en rask oversikt over dette målet har du lært hvordan du setter opp den første butikken. Du har lært hvordan du generate en Bitcoin Recovery seed frase.


### Kunnskapsvurdering Praktisk gjennomgang


Beskriv en metode for å generere nøkler og et opplegg for å sikre dem, sammen med avveiningene/risikoen ved sikkerhetsopplegget.


## BTCPay Server Lightning Wallet


<chapterId>1bbece7e-0197-57e6-a93a-561cf384d946</chapterId>


Når en serveradministrator konfigurerer en ny BTCPay Server-forekomst, kan de sette opp en Lightning Network-implementering, for eksempel LND, Core Lightning eller Eclair; se delen Konfigurere BTCPay Server for mer detaljerte installasjonsinstruksjoner.


Hvis du følger med i et klasserom, fungerer det å koble en Lightning-node til BTCPay Server gjennom en egendefinert node. En bruker som ikke er serveradministrator på BTCPay Server, vil som standard ikke kunne bruke den interne Lightning-noden. Dette er for å beskytte servereieren mot å miste pengene sine. Serveradministratorer kan installere en plugin for å gi tilgang til Lightning-noden gjennom LNBank, men dette er utenfor denne bokens omfang. For mer informasjon om LNBank, se den offisielle plugin-siden.


### Koble til intern node (serveradministrator)


Serveradministratoren kan bruke BTCPay Servers interne Lightning Node. Uansett Lightning-implementering er tilkoblingen til den interne Lightning-noden den samme.


Gå til en tidligere oppsettbutikk, og klikk på "Lightning" Wallet i menyen til venstre. BTCPay Server gir to oppsettmuligheter: bruk av den interne noden (kun serveradministrator som standard) eller en tilpasset node (ekstern tilkobling). Serveradministratorer kan klikke på alternativet "Bruk intern node". Det er ikke behov for mer konfigurasjon. Klikk på "lagre"-knappen og legg merke til varselet som sier "BTC Lightning-node oppdatert". Butikken har nå fått Lightning Network-funksjoner.


### Koble til ekstern node (serverbruker/butikkeier)


Som standard har ikke butikkeiere lov til å bruke serveradministratorens Lightning Node. Tilkoblingen må opprettes til en ekstern node, enten en node som eies av butikkeieren før du setter opp en BTCPay-server, en LNBank-plugin hvis den er gjort tilgjengelig av serveradministratoren, eller en depotløsning som Alby.


Gå til en tidligere oppsatt butikk, og klikk på "Lightning" under lommebøker i menyen til venstre. Ettersom butikkeiere ikke har lov til å bruke den interne noden som standard, er dette alternativet nedtonet. Bruk av en egendefinert node er det eneste alternativet som er tilgjengelig som standard for butikkeiere.


BTCPay Server krever tilkoblingsinformasjon; den forhåndslagde (eller depotløsningen) vil levere denne informasjonen spesielt skreddersydd til en Lightning-implementering. I BTCPay Server kan butikkeiere bruke følgende tilkoblinger;



- C-lightning via TCPellerUnixdomainsocketconnection.
- Lynlading via HTTPS
- Eclair via HTTPS
- LND via REST-proxyen
- LNDhub via REST API


![image](assets/en/032.webp)


Klikk på "Test tilkobling" for å sikre at du har angitt tilkoblingsdetaljene riktig. Etter at tilkoblingen er bekreftet å være god, klikker du på "Lagre", og BTCPay Server viser at butikken er oppdatert med en Lightning Node.


### Administrere intern Lightning-node LND (serveradministrator)


Etter at du har koblet til den interne Lightning Node, vil serveradministratorer legge merke til nye fliser på dashbordet som er spesielt beregnet på Lightning-informasjon.



- Lynbalanse
- BTC i kanaler
  - BTC åpner kanaler
  - BTC lokal saldo
  - BTC ekstern saldo
  - BTC stenger kanaler
- BTC On-Chain
  - BTC bekreftet
  - BTC ubekreftet
  - BTC reservert
- Lyntjenester
  - Ride the Lightning (RTL).


Ved å klikke på Ride the Lightning-logoen i "Lightning-tjenester"-flisen eller på "Lightning" under lommebøker i menyen til venstre, kan serveradministratorer nå RTL for Lightning-nodeadministrasjon.


**Merk!


Tilkobling av den interne Lightning Node mislykkes - Hvis den interne tilkoblingen mislykkes, bekreft:


1. Bitcoin On-Chain-noden er fullstendig synkronisert

2. Den interne lynnoden er "Aktivert" under "Lyn" > "Innstillinger" > "BTC Lyninnstillinger"


Hvis du ikke klarer å koble til Lightning-noden din, kan du prøve å starte serveren på nytt, eller lese mer informasjon i den offisielle dokumentasjonen til BTCPay Server; https://docs.btcpayserver.org/Troubleshooting/. Du kan ikke godta lynbetalinger i butikken din før Lightning-noden din vises som "Online". Prøv å teste Lightning-tilkoblingen din ved å klikke på lenken "Public Node Info".


### Lyn Wallet


I Lightning Wallet-alternativet i menylinjen til venstre finner serveradministratorer enkel tilgang til RTL, deres Public node Info og Lightning-innstillinger som er spesifikke for deres BTCPay Server-butikk.


#### Intern nodeinformasjon


Serveradministratorer kan klikke på den interne nodeinformasjonen for å se serverstatusen (online/offline) og tilkoblingsstrengen for Clearnet eller [Tor](https://planb.academy/resources/glossary/tor).


![image](assets/en/033.webp)


#### Endre tilkobling


Hvis du vil endre den eksterne Lightning-noden, går du til "Lightning Settings" og klikker på "Change connection" (ved siden av "Public Node info"). Dette tilbakestiller det eksisterende oppsettet. Skriv inn de nye nodeopplysningene, klikk på Lagre, og butikken oppdateres deretter.


![image](assets/en/034.webp)


#### Tjenester


Hvis serveradministratoren bestemmer seg for å installere flere tjenester for Lightning-implementeringen, vil de bli oppført her. Med en standard LND-implementering vil administratorer ha Ride The Lightning (RTL) som et standardverktøy for nodeadministrasjon.


#### BTC Lightning Wallet-innstillinger


Etter at du har lagt til Lightning-noden i butikken i et tidligere trinn, kan butikkeiere fortsatt velge å deaktivere den for butikken ved å bruke vekslebryteren øverst i Lightning-innstillingene.


![image](assets/en/035.webp)


#### Lightning Betalingsalternativer


Butikkeiere kan angi følgende parametere for å forbedre Lightning-opplevelsen for kundene sine.



- Vis beløp for lynbetalinger i Satoshis.
- Legg til hopptips for private kanaler i Lightning Invoice.
- Forene On-Chain- og Lightning-betalings-URL/QR-koder i kassen.
- Angi en beskrivelsesmal for lynfakturaer.


#### LNURL


Butikkeiere kan velge å bruke eller ikke bruke LNURL. En Lightning Network URL, eller LNURL, er en foreslått standard for interaksjon mellom Lightning Payer og betalingsmottaker. Kort fortalt er en LNURL en bech32-kodet URL med LNURL som prefiks. Lightning Wallet forventes å dekode URL-en, kontakte URL-en og vente på et JSON-objekt med ytterligere instruksjoner, særlig en tagg som definerer oppførselen til LNURL-en.



- Aktiver LNURL
- LNURL Klassisk modus
  - For Wallet-kompatibilitet, Bech32-kodet (klassisk) vs. URL i klartekst (kommende)
- Tillat betalingsmottakeren å sende en kommentar.


### Eksempel 1


#### Koble til Lightning med den interne noden (administrator)


Dette alternativet er bare tilgjengelig hvis du er administrator for denne forekomsten, eller hvis administratoren har endret standardinnstillingene slik at brukerne kan bruke den interne lynnoden.


Som administrator klikker du på Lightning Wallet i menylinjen til venstre. BTCPay Server vil be deg om å velge ett av to alternativer for tilkobling av en Lightning Node: en intern node eller en tilpasset ekstern node. Klikk på "Bruk intern node" og klikk deretter på "Lagre"


#### Administrere Lightning-noden din (RTL)


Etter at du har koblet til den interne Lightning-noden, oppdateres BTCPay Server og viser et varsel "BTC Lightning node updated", som bekrefter at du nå har koblet Lightning til butikken din.


Administrasjon av lynnoden er en oppgave for serveradministratoren. Dette innebærer følgende:


- Administrer transaksjon
- Styring av likviditet
  - Innkommende likviditet
  - Utgående likviditet
- Håndtering av kolleger og kanaler
  - Tilkoblede jevnaldrende
  - Kanalavgifter
  - Kanalstatus
- Ta hyppige sikkerhetskopier av kanalstatusene.
- Kontroll av rutingrapporter
- Alternativt kan du bruke tjenester som Loop.


All Lightning-nodeadministrasjon gjøres som standard med RTL (forutsatt at du kjører på en LND-implementering). Administratorer kan klikke på sin Lightning Wallet i BTCPay Server og finne en knapp for å åpne RTL. Hovedinstrumentbordet i BTCPay Server er nå oppdatert med Lightning Network-fliser, inkludert rask tilgang til RTL.


### Eksempel 2


#### Koble til lynnedslag med Alby


Når du skal koble deg til en depotmottaker som Alby, bør butikkeiere først opprette en konto og gå til https://getalby.com/


![image](assets/en/036.webp)


Etter at du har opprettet Alby-kontoen, går du til BTCPay Server-butikken din.


Trinn 1: Klikk på "Sett opp en Lightning-node" på dashbordet eller på "Lightning" under lommebøker.


![image](assets/en/037.webp)


Trinn 2: Sett inn Wallet-tilkoblingslegitimasjonen du har fått fra Alby. Klikk på Wallet på dashbordet til Alby. Her finner du "Wallet Connection Credentials". Kopier disse legitimasjonsopplysningene. Lim inn legitimasjonen fra Alby i feltet Connection configuration i BTCPay Server.


![image](assets/en/038.webp)


Trinn 3: Når du har gitt BTCPay Server tilkoblingsdetaljene, klikker du på knappen "Test tilkobling" for å sikre at tilkoblingen fungerer som den skal. Legg merke til meldingen "Connection to lightning node successful" øverst på skjermen. Dette bekrefter at alt fungerer som forventet.


![image](assets/en/039.webp)


Trinn 4: Klikk på "Lagre", og butikken din er nå koblet til en Lightning-node av Alby.


![image](assets/en/040.webp)


**Merk!


Stol aldri på en depotmottaker Lightning-løsning med mer verdi enn du er villig til å tape.


### Oppsummering av ferdigheter


I denne delen har du lært:



- Slik kobler du til en intern eller ekstern Lightning-node
- Innholdet og funksjonen til ulike lynrelaterte fliser i dashbordet
- Slik konfigurerer du Lightning Wallet ved hjelp av Voltage Surge eller Alby


### Kunnskapsvurdering Praktisk gjennomgang


Beskriv noen av de ulike alternativene for å koble en Lightning Wallet til butikken din.


# BTCPay-server Interface


<partId>25e88b81-e1ab-515f-a035-09f2a3075556</partId>


## Oversikt over dashbordet


<chapterId>410ff28b-a272-5c91-93e0-48d5b28c53ab</chapterId>


BTCPay Server er en modulær programvarepakke. Det finnes imidlertid standarder som hver BTCPay Server må overholde, og disse standardene vil styre samspillet mellom administratoren og brukerne. Vi begynner med dashbordet. Hovedinngangspunktet for hver BTCPay Server etter innlogging. Dashbordet gir en oversikt over butikkens ytelse, Wallets nåværende saldo og transaksjonene fra de siste 7 dagene. Ettersom det er en modulær visning, kan plugins bruke denne visningen til sin fordel og lage sine egne fliser på dashbordet. I dette kurset vil vi bare diskutere standard plugins og apper, sammen med deres respektive visninger, i hele BTCPay Server.


### Dashbordfliser


I hovedvisningen av BTCPay Server-dashbordet er det et par standardfliser tilgjengelig. Disse flisene er utformet for at butikkeieren eller administratoren raskt skal kunne administrere butikken sin i én oversikt.



- Wallet balanse
- Transaksjonsaktivitet
- Lightning Balance (hvis Lightning er aktivert i butikken)
- Lightning Services (hvis Lightning er aktivert i butikken)
- Nylige transaksjoner.
- Nylige fakturaer
- Nåværende aktive crowdfundings
- Butikkresultat / bestselgende varer.


### Wallet balanse


Wallet-saldoflisen gir en rask oversikt over Wallets midler og resultater. Den kan vises i enten BTC eller Fiat-valuta i en ukentlig, månedlig eller årlig graf.


![image](assets/en/041.webp)


### Transaksjonsaktivitet


Ved siden av Wallet-saldoflisen viser BTCPay Server en rask oversikt over ventende utbetalinger, antall transaksjoner de siste 7 dagene, og om butikken din har utstedt refusjoner. Ved å klikke på Administrer-knappen kommer du til administrasjonen for ventende utbetalinger (les mer om utbetalinger i kapittelet BTCPay Server - Betalinger).


![image](assets/en/042.webp)


### Lynbalanse


Dette er bare synlig når Lightning er aktivert.


Når administratoren har tillatt Lightning Network-tilgang, har BTCPay Server-dashbordet nå en ny flis med informasjon om Lightning-noden. Hvor mye BTC som er i kanaler, hvordan dette er balansert lokalt eller eksternt (innkommende eller utgående likviditet), om kanaler stenger eller åpner, og hvor mye Bitcoin som holdes On-Chain på lynnoden.


![image](assets/en/043.webp)


### Lyntjenester


Dette er bare synlig når lynet er aktivt.


I tillegg til å se Lightning-saldoen din på dashbordet til BTCPay Server, vil administratorer også se flisen for Lightning-tjenester. Her kan administratorer finne hurtigknapper for verktøy de bruker til å administrere Lightning-noden sin; for eksempel er Ride the Lightning et av standardverktøyene med BTCPay Server for administrasjon av Lightning-noder.


![image](assets/en/044.webp)


### Nylige transaksjoner


Flisen Nylige transaksjoner viser butikkens nyeste transaksjoner. Med ett klikk kan administratoren av BTCPay Server-instansen nå se den siste transaksjonen og se om det er behov for oppmerksomhet rundt den.


![image](assets/en/045.webp)


### Nylige fakturaer


Flisen Nylige fakturaer viser de seks siste fakturaene som er generert av BTCPay-serveren, inkludert status og Invoice-beløp. Flisen inneholder også en "Vis alle"-knapp for enkel tilgang til hele Invoice-oversikten.


![image](assets/en/046.webp)


### Point of Sale og crowdfunding


Ettersom BTCPay Server leverer et sett med standard plugins eller apper, er Point Of Sale og Crowdfund de to viktigste plugins av BTCPay Server. Med hver butikk og Wallet kan en BTCPay Server-bruker generate så mange Point Of Sales eller Crowdfunds som de finner passende. Hver av dem vil opprette en ny dashbordflis som viser plugin-modulenes ytelse.


![image](assets/en/047.webp)


Legg merke til den lille forskjellen mellom en Point of Sale- og Crowdfund-flise. Administratoren ser de mest solgte varene i Point of Sales-flisen. I Crowdfund-flisen blir dette Toppfordeler. Begge flisene har hurtigknapper for å administrere de respektive appene og se de siste fakturaene som er opprettet av toppartikler eller toppfordeler.


![image](assets/en/048.webp)


**Merk!


Saldografer og nylige transaksjoner er bare tilgjengelige for On-Chain-betalingsmåter. Informasjon om Lightning Network-saldoer og -transaksjoner er på to-do-listen. Fra og med BTCPay Server versjon 1.6.0 er grunnleggende Lightning Network-saldoer tilgjengelige.


### Oppsummering av ferdigheter


I denne delen lærte du følgende:



- Kjerneoppsettet av fliser på hovedsiden kalles Dashboard.
- En grunnleggende forståelse av innholdet i hver brikke.


### Gjennomgang av kunnskapsvurdering


List opp så mange fliser fra minnet som mulig fra dashbordet.


## BTCPay Server - Butikkinnstillinger


<chapterId>e8faef7b-278d-550e-a511-bc3a442daf64</chapterId>


I BTCPay Server-programvaren kjenner vi til to typer innstillinger. BTCPay Server-butikkspesifikke innstillinger, innstillingsknappen som finnes i menylinjen til venstre under dashbordet, og BTCPay Server-innstillinger, som du finner nederst i menylinjen, rett over Konto. De BTCPay Server-serverspesifikke innstillingene kan bare vises av serveradministratorer.


Butikkinnstillingene består av mange faner for å kategorisere hvert sett med innstillinger.



- Generelt
- Priser
- Utseende i kassen
- Adgangstokener
- Brukere
- Roller
- Webhooks
- Utbetalingsprosessorer
- E-poster
- Skjemaer


### Generelt


I fanen Generelle innstillinger angir butikkeiere standardinnstillingene for merkevarebygging og betaling. Ved førstegangsoppsettet av butikken ble det oppgitt et butikknavn, og dette gjenspeiles i de generelle innstillingene under Butikknavn. Her kan butikkeieren også angi at nettstedet skal samsvare med merkevaren og en butikk-ID som administratoren kan gjenkjenne i databasen.


#### Merkevarebygging


Siden BTCPay Server er FOSS, kan en butikkeier gjøre tilpasset merkevarebygging for å matche butikken sin. Angi merkevarefargen, lagre merkevarens logoer og legg til tilpasset CSS for offentlige / kundevendte sider (fakturaer, betalingsforespørsler, pull-betalinger)


#### Betaling


I betalingsinnstillingene kan butikkeiere angi butikkens standardvaluta (enten Bitcoin eller en hvilken som helst fiat-valuta).


#### Tillat hvem som helst å opprette fakturaer


Denne innstillingen er ment for utviklere eller byggere på toppen av BTCPay Server. Når denne innstillingen er aktivert for butikken din, kan omverdenen opprette fakturaer på BTCPay Server-forekomsten din.


#### Legg til en ekstra avgift (nettverksavgift) på fakturaer


En funksjon i BTCPay for å beskytte selgere mot Dust-angrep eller kunder fra å pådra seg en høy kostnad i gebyrer senere når selgeren trenger å flytte et stort beløp Bitcoin på en gang. For eksempel opprettet kunden en Invoice for 20 $ og betalte den delvis, og betalte 1 $ 20 ganger til Invoice var fullt betalt. Forhandleren har nå en større transaksjon, noe som øker Mining-kostnaden hvis forhandleren bestemmer seg for å flytte disse midlene senere. Som standard legger BTCPay til en ekstra nettverkskostnad til det totale Invoice-beløpet for å dekke denne utgiften for forhandleren når Invoice betales i flere transaksjoner. BTCPay tilbyr flere alternativer for å tilpasse denne beskyttelsesfunksjonen. Du kan legge til en nettverksavgift:



- Bare hvis kunden foretar mer enn én betaling for Invoice (I eksempelet ovenfor, hvis kunden opprettet en Invoice for 20\$ og betalte 1\$, er det totale beløpet for Invoice som skal betales nå 19\$ + nettverksavgiften. Nettverksgebyret legges til etter den første betalingen)
- På hver betaling (inkludert den første betalingen, i vårt eksempel vil totalsummen være 20\$ + nettverksavgift med en gang, selv på den første betalingen)
- Legg aldri til nettverksavgift (deaktiverer nettverksavgiften helt)


Selv om det beskytter mot Dust-transaksjoner, kan det også ha en negativ innvirkning på virksomheten hvis det ikke kommuniseres på riktig måte. Kundene kan ha flere spørsmål og tro at du tar for mye betalt.


#### Invoice utløper hvis ikke hele beløpet er betalt etter?


Invoice-timeren er satt til 15 minutter som standard. Timeren fungerer som en beskyttelsesmekanisme mot volatilitet, ettersom den låser Bitcoin-beløpet i henhold til Bitcoin-til-fiat Exchange-satsene. Hvis kunden ikke betaler Invoice innen den definerte perioden, anses Invoice som utløpt. Invoice anses som "betalt" så snart transaksjonen er synlig på Blockchain (med null bekreftelser), og er "fullført" når den når det antallet bekreftelser som forhandleren har definert (vanligvis 1-6). Timeren kan tilpasses i minutter.


#### Betrakt Invoice som betalt selv om det betalte beløpet er X % mindre enn forventet?


Når en kunde bruker en Exchange Wallet til å betale direkte for en Invoice, tar Exchange et lite gebyr. Dette betyr at en slik Invoice ikke anses som fullstendig fullført. Invoice er merket som "delvis betalt". Du kan angi prosentsatsen her hvis en forhandler ønsker å godta underbetalte fakturaer.


### Priser


Når en Invoice genereres i BTCPay Server, trenger den alltid den mest oppdaterte og nøyaktige Bitcoin-til-fiat-prisen. Når du oppretter en ny butikk i BTCPay Server, blir administratorer bedt om å angi sin foretrukne priskilde. Etter at butikken er satt opp, kan butikkeiere når som helst endre priskilden i denne fanen.


#### Avansert skripting av satsregler


Hovedsakelig brukt av kraftbrukere. Hvis den er slått på, kan butikkeiere lage skript rundt prisatferd og hvordan de skal belaste kundene sine.


#### Testing


Et raskt teststed for dine foretrukne valutapar. Denne funksjonen inkluderer også muligheten til å sjekke standard valutapar via en REST-spørring.


### Utseende i kassen


Fanen Checkout Appearance begynner med Invoice-spesifikke innstillinger og en standard betalingsmåte, og aktiverer spesifikke betalingsmåter når de angitte kravene er oppfylt.


#### Invoice-innstillinger


Standard betalingsmetoder. BTCPay Server tilbyr tre alternativer i standardkonfigurasjonen.



- BTC (On-Chain)
- BTC (LNURL-pay)
- BTC (off-chain og Lightning)


Vi kan angi parametere for butikken vår, der en kunde bare vil samhandle med Lightning når prisen er mindre enn X-beløpet, og omvendt for On-Chain-transaksjoner, når X er større enn Y, alltid presentere On-Chain-betalingsalternativet.


![image](assets/en/049.webp)


#### Kasse


Fra og med BTCPay Server versjon 1.7 ble en ny Checkout Interface, Checkout V2, introdusert. Siden versjon 1.9 ble standardisert, kan administratorer og butikkeiere fortsatt sette kassen til den forrige versjonen. Ved å bruke bryteren "Bruk den klassiske kassen" kan butikkeieren tilbakestille butikken til den tidligere kassaopplevelsen. BTCPay Server har også et utvalg forhåndsinnstillinger for netthandel eller en butikkopplevelse.


![image](assets/en/050.webp)


Når en kunde samhandler med butikken og genererer en Invoice, er det en utløpstid for Invoice. Som standard setter BTCPay Server denne til 5 minutter, og administratorer kan justere den etter eget ønske. Kassesiden kan tilpasses ytterligere ved å sjekke følgende parametere:



- Feir betalingen ved å vise konfetti
- Vis butikkens topptekst (navn og logo)
- Vis "Betal i Wallet"-knappen
- Forene On-Chain- og off-chain-betalinger URL/QR
- Visning av lynbetalingsbeløp i Satoshis
- Automatisk gjenkjenning av språk i kassen


![image](assets/en/051.webp)


Når automatisk språkgjenkjenning ikke er angitt, vil BTCPay Server som standard vise engelsk. Butikkeieren kan endre denne standardinnstillingen til sitt foretrukne språk.


![image](assets/en/052.webp)


Klikk på rullegardinmenyen, så kan butikkeiere angi en egendefinert HTML-tittel som skal vises på kassesiden.


![image](assets/en/053.webp)


For å sikre at kundene vet hvilken betalingsmåte de skal bruke, kan butikkeieren eksplisitt angi at brukerne alltid må velge ønsket betalingsmåte i kassen. Når Invoice er betalt, lar BTCPay Server kunden gå tilbake til nettbutikken. Butikkeiere kan angi at denne viderekoblingen skal skje automatisk etter at kunden har betalt.


![image](assets/en/054.webp)


#### Offentlig mottakelse


I innstillingene for offentlige kvitteringer kan butikkeieren angi at kvitteringssidene skal være offentlige, slik at betalingslisten og QR-koden vises på kvitteringssiden, slik at kunden enkelt kan få tilgang til den.


![image](assets/en/055.webp)


### Adgangstokener


Tilgangstokener brukes for sammenkobling med visse e-handelsintegrasjoner eller spesialbygde integrasjoner.


![image](assets/en/056.webp)


### Brukere


Butikkbrukere er der butikkeieren kan administrere sine ansatte, deres kontoer og tilgang til butikken. Etter at medarbeiderne har opprettet kontoene sine, kan butikkeieren legge til bestemte brukere i butikken som gjestebrukere eller eiere. For å definere medarbeiderens rolle ytterligere, se neste avsnitt om "BTCPay Server Butikkinnstillinger - Roller"


![image](assets/en/057.webp)


### Roller


En butikkeier synes kanskje ikke at brukerens standardroller er viktige nok. I innstillingene for egendefinerte roller kan butikkeieren definere de nøyaktige behovene for hver rolle i virksomheten.


(1) Klikk på knappen "+ Legg til rolle" for å opprette en ny rolle.


![image](assets/en/058.webp)


(2) Skriv inn et rollenavn, for eksempel "Kasserer".


![image](assets/en/059.webp)


(3) Konfigurer de individuelle tillatelsene for rollen.



- Endre butikkene dine.
- Administrer Exchange-kontoer knyttet til butikkene dine.
  - Se Exchange-kontoer som er knyttet til butikkene dine.
- Administrer trekkbetalingene dine.
- Opprett pull-betalinger.
  - Opprett ikke-godkjente pull-betalinger.
- Endre fakturaer.
  - Se fakturaer.
  - Opprett en Invoice.
  - Opprett fakturaer fra lynnodene som er knyttet til butikkene dine.
- Se butikkene dine.
  - Se fakturaer.
  - Se betalingsanmodningene dine.
  - Endre butikkenes webhooks.
- Endre betalingsforespørsler.
  - Se betalingsanmodningene dine.
- Bruk lynnodene som er knyttet til butikkene dine.
  - Se lynfakturaene som er knyttet til butikkene dine.
  - Opprett fakturaer fra lynnodene som er knyttet til butikkene dine.
- Sett inn penger på Exchange-kontoer som er knyttet til butikkene dine.
- Ta ut penger fra Exchange-kontoer til butikken din.
- Handle penger på butikkens Exchange-kontoer.


Når rollen opprettes, er navnet fast og kan ikke endres etter at den er i redigeringsmodus.


![image](assets/en/060.webp)


### Webhooks


I BTCPay Server er det rimelig enkelt å lage en ny "Webhook". I BTCPay Server Store-innstillingene - Webhooks-fanen kan en butikkeier enkelt opprette en ny webhook ved å klikke på "+ Create Webhook". Webhooks gjør det mulig for BTCPay Server å sende HTTP-hendelser relatert til butikken din til andre servere eller e-handelsintegrasjoner.


![image](assets/en/061.webp)


Du er nå i visningen for å opprette en webhook. Sørg for at du kjenner URL-adressen til nyttelasten og lim den inn i BTCPay-serveren. Mens du limte inn URL-adressen for nyttelasten, viser den webhook-hemmeligheten under. Kopier webhook-hemmeligheten og oppgi den på endepunktet. Når alt er satt opp, kan du veksle i BTCPay Server til "Automatic redelivery" BTCPay Server vil prøve å levere en mislykket levering på nytt etter 10 sekunder, 1 minutt og opptil 6 ganger etter 10 minutter. Du kan veksle mellom hver hendelse eller spesifisere hendelsene for dine behov. Sørg for å aktivere webhooken og trykk på "Legg til webhook"-knappen for å lagre den.


![image](assets/en/062.webp)


Webhooks er ikke ment å være kompatible med Bitpay API. Det finnes to separate IPN-er (i BitPay-termer: "Instant Payment Notifications") i BTCPay Server.



- Webhookp
- Varsler


Bruk kun Notification URL når du oppretter fakturaer via Bitpay API.


### Utbetalingsprosessorer


Utbetalingsprosessorer fungerer sammen med utbetalingskonseptet i BTCPay Server. En utbetalingsaggregator for å samle flere transaksjoner og sende dem samtidig. Med utbetalingsprosessorer kan en butikkeier automatisere batch-utbetalingene. BTCPay Server tilbyr to metoder for automatiserte utbetalinger: On-Chain og off-chain (LN).


Butikkeieren kan klikke og konfigurere begge utbetalingsprosessorene hver for seg. En butikkeier vil kanskje bare kjøre On-Chain-prosessoren én gang hver X. time, mens off-chain-prosessoren kan kjøres med noen minutters mellomrom. For On-Chain kan du også angi et mål for hvilken blokk den skal inkluderes. Som standard er dette satt til 1 (eller neste tilgjengelige blokk). Legg merke til at innstillingen av off-chain-utbetalingsprosessoren bare har intervalltimeren og ikke noe blokkmål. Lightning Network-utbetalinger er øyeblikkelige.


![image](assets/en/063.webp)

![image](assets/en/064.webp)


Butikkeiere kan bare konfigurere On-Chain-prosessoren hvis de har en Hot Wallet koblet til butikken sin.


![image](assets/en/065.webp)


Etter at du har satt opp en utbetalingsprosessor, kan du raskt fjerne eller endre den ved å gå tilbake til fanen Utbetalingsprosessor i innstillingene for BTCPay Server Store.


**Note**


Utbetalingsprosessor On-Chain - Utbetalingsprosessoren On-Chain kan bare fungere på en butikk som er konfigurert med en Hot Wallet tilkoblet. Hvis ingen Hot Wallet er tilkoblet, har ikke BTCPay-serveren Wallet-nøklene og vil ikke kunne behandle utbetalinger automatisk.


### E-poster


BTCPay Server kan bruke e-postmeldinger til varslinger eller, når det er riktig innstilt, til å gjenopprette kontoer som er opprettet på forekomsten. Som standard sender ikke BTCPay Server en e-post når passordet går tapt, for eksempel.


![image](assets/en/066.webp)


Før en butikkeier kan angi e-postregler for å utløse spesifikke hendelser i butikken, må de først sette opp noen grunnleggende e-postinnstillinger. BTCPay Server krever disse innstillingene for å sende e-poster for hendelser relatert til butikken din eller for tilbakestilling av passord.


BTCPay Server har gjort det enklere å fylle ut denne informasjonen ved å bruke "Quick Fill"-alternativet:



- Gmail.com
- Yahoo.com
- Postkanon
- Office365
- SendGrid


Ved å bruke hurtigutfyllingsalternativet vil BTCPay Server forhåndsutfylle feltene for SMTP-serveren og porten. Nå trenger butikkeieren bare å fylle ut legitimasjonen sin, inkludert en e-post Address, innlogging (som vanligvis er lik din e-post Address) og passordet sitt. Det avanserte alternativet i e-postinnstillingene for BTCPay Server er å Deaktivere TLS-sertifikatets sikkerhetskontroller; som standard er dette aktivert.


![image](assets/en/067.webp)


Med e-postregler kan butikkeieren angi at bestemte hendelser skal utløse e-post til bestemte e-postadresser.



- Invoice Opprettet
- Invoice Mottatt betaling
- Invoice-prosessering
- Invoice Utgått på dato
- Invoice Avgjort
- Invoice Ugyldig
- Invoice Betaling avgjort


Hvis kunden har oppgitt en e-post Address, kan disse utløserne også sende informasjonen til kunden. Butikkeiere kan forhåndsutfylle emnelinjen for å gjøre det klart hvorfor denne e-posten ble sendt og hva som utløste den.


![image](assets/en/068.webp)


### Skjemaer


Ettersom BTCPay Server ikke samler inn data, kan det være lurt for butikkeieren å legge til et tilpasset skjema i kassaopplevelsen; på denne måten kan butikkeieren samle inn ytterligere informasjon fra kunden. BTCPay Server Skjemabygger består av to deler: en visuell og en mer avansert kodevisning av skjemaene.


Når du oppretter et nytt skjema, åpner BTCPay Server et nytt vindu der du blir bedt om å oppgi grunnleggende informasjon om hva du vil at det nye skjemaet skal spørre om. Først må butikkeieren oppgi et klart navn på det nye skjemaet; dette navnet kan ikke endres etter at det er angitt.


![image](assets/en/069.webp)


Etter at butikkeieren har gitt skjemaet et navn, kan du også sette bryteren for "Tillat offentlig bruk av skjema" til PÅ, slik at Green blir slått på. Dette sikrer at skjemaet brukes på alle steder som henvender seg til kundene. Hvis en butikkeier for eksempel oppretter et eget Invoice-skjema som ikke brukes på salgsstedet, kan det hende at de likevel ønsker å samle inn informasjon fra kunden. Denne vekslingsknappen gjør det mulig å samle inn slik informasjon.


![image](assets/en/070.webp)


Hvert skjema starter med minst ett nytt skjemafelt. Butikkeieren kan velge hvilken type felt det skal være.



- Tekst
- Antall
- Passord
- E-post
- URL
- Telefonnumre
- Dato
- Skjulte felt
- Fieldset
- Et tekstområde for åpne kommentarer.
- Alternativvelger


Hver type har sine egne parametere som skal fylles ut. Butikkeieren kan stille dem inn etter eget ønske. Under det første feltet som er opprettet, kan butikkeieren legge til nye felt i skjemaet.


![image](assets/en/071.webp)


#### Avanserte tilpassede skjemaer


BTCPay Server lar deg også bygge skjemaer i kode. JSON, spesielt. I stedet for å se på redigeringsverktøyet kan butikkeiere klikke på CODE-knappen rett ved siden av redigeringsverktøyet og gå inn i koden til skjemaene sine. I en feltdefinisjon kan bare følgende felt angis; verdiene til feltene lagres i metadataene til Invoice:



| Felt | Beskrivelse |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| .fields.constant | Hvis true, må .value settes i skjema-definisjonen, og brukeren vil ikke kunne endre feltets verdi. (eksempel: skjema-definisjonens versjon) |
| .fields.type | HTML-inputtypen text, radio, checkbox, password, hidden, button, color, date, datetime-local, month, week, time, email, number, range, search, url, select, tel |
| .fields.options | Hvis .fields.type er select, listen over valgbare verdier |
| .fields.options.text | Teksten som vises for dette alternativet |
| .fields.options.value | Verdien av feltet hvis dette alternativet er valgt |
| .fields.type=fieldset | Opprett et HTML-fieldset rundt barna .fields.fields (se nedenfor) |
| .fields.name | JSON-egenskapsnavnet til feltet slik det vil vises i fakturaens metadata |
| .fields.value | Standardverdien for feltet |
| .fields.required | hvis true, vil feltet være obligatorisk |
| .fields.label | Ledeteksten (label) til feltet |
| .fields.helpText | Tilleggstekst for å gi en forklaring av feltet. |
| .fields.fields | Du kan organisere feltene dine i et hierarki, slik at underfelt kan nøstes inn i fakturaens metadata. Denne strukturen kan hjelpe deg med å organisere og administrere den innsamlede informasjonen bedre, noe som gjør den enklere å få tilgang til og tolke. For eksempel, hvis du har et skjema som samler inn kundeinformasjon, kan du gruppere feltene under et foreldrefelt kalt customer. Innenfor dette foreldrefeltet kan du ha underfelt som name, Email og address. |

Feltnavnet representerer JSON-egenskapsnavnet som lagrer den brukerdefinerte verdien i Invoices metadata. Noen velkjente navn kan tolkes og endres for å justere Invoices innstillinger.



| Feltnavn         | Beskrivelse           |
| ---------------- | ---------------------- |
| invoice_amount   | Fakturabeløp          |
| invoice_currency | Fakturavaluta         |

Du kan forhåndsutfylle feltene i et Invoice-skjema automatisk ved å legge til spørringsstrenger i skjemaets URL-adresse, for eksempel "?your_field=value".


Her er noen eksempler på bruksområder for denne funksjonen:



- Hjelper brukeren med inndata: Forhåndsutfyll felter med kjent kundeinformasjon for å gjøre det enklere for dem å fylle ut skjemaet. Hvis du for eksempel allerede kjenner kundens e-postadresse Address, kan du forhåndsutfylle e-postfeltet for å spare tid.
- Personalisering: Tilpass skjemaet basert på kundepreferanser eller segmentering. Hvis du for eksempel har ulike kundenivåer, kan du forhåndsutfylle skjemaet med relevante data, for eksempel medlemsnivå eller spesifikke tilbud.
- Sporing: Spor kilden til kundebesøk ved hjelp av skjulte felt og forhåndsutfylte verdier. Du kan for eksempel opprette lenker med forhåndsutfylte utm_media-verdier for hver markedsføringskanal (f.eks. Twitter, Facebook, e-post). Dette hjelper deg med å analysere effektiviteten av markedsføringstiltakene dine.
- A/B-testing: Forhåndsutfyll felter med forskjellige verdier for å teste ulike skjemavarianter, slik at du kan optimalisere brukeropplevelsen og konverteringsraten.


### Oppsummering av ferdigheter


I denne delen lærte du følgende:



- Oppsettet og funksjonene til fanene i Butikkinnstillinger
- En rekke alternativer for å finjustere håndteringen av underliggende Exchange-satser, delbetalinger, små underbetalinger og mer.
- Tilpass utseendet på kassen, inkludert prisavhengig hovedkjede vs. Lightning-aktivering på fakturaer.
- Administrer tilgangsnivåer og tillatelser på tvers av roller.
- Konfigurer automatiserte e-poster og utløsere for disse
- Opprett egendefinerte skjemaer for innhenting av ytterligere kundeinformasjon i kassen.


### Kunnskapsvurderinger


#### KA-gjennomgang


Hva er forskjellen mellom Butikkinnstillinger og Serverinnstillinger?


#### KA Hypotetisk


Beskriv noen alternativer du kan velge i Kasseutseende > Invoice-innstillinger, og hvorfor.


## BTCPay Server - Serverinnstillinger


<chapterId>1dd858a2-49ea-586b-9bc1-75a65f508df6</chapterId>


BTCPay Server består av to forskjellige innstillingsvisninger. Den ene er dedikert til butikkinnstillinger, og den andre til serverinnstillinger. Sistnevnte er kun tilgjengelig for serveradministratorer og ikke for butikkeiere. Serveradministratorer kan legge til brukere, opprette egendefinerte roller, konfigurere e-postserveren, angi retningslinjer, kjøre vedlikeholdsoppgaver, sjekke alle tjenester knyttet til BTCPay Server, laste opp filer til serveren eller sjekke logger.


### Brukere


Som nevnt i forrige del kan serveradministratorer invitere brukere til serveren sin ved å legge dem til i kategorien Brukere.


### Tilpassede roller på hele serveren


BTCPay Server har to typer egendefinerte roller: butikkspesifikke egendefinerte roller og serveromfattende egendefinerte roller i BTCPay Server-innstillingene. Begge har et lignende sett med tillatelser, men hvis de angis via BTCpay Server Settings - Roles-fanen, vil den anvendte rollen være serveromfattende og gjelde for flere butikker. Legg merke til en "Server-wide"-tagg for de egendefinerte rollene i Serverinnstillinger.


![image](assets/en/072.webp)


### Tilpassede roller på hele serveren


Tillatelsessett for egendefinerte roller på hele serveren;



- Endre butikkene dine.
- Administrer Exchange-kontoer knyttet til butikkene dine.
  - Se Exchange-kontoer som er knyttet til butikkene dine.
- Administrer trekkbetalingene dine.
- Opprett pull-betalinger.
  - Opprett ikke-godkjente pull-betalinger.
- Endre fakturaer.
  - Se fakturaer.
  - Opprett en Invoice.
  - Opprett fakturaer fra lynnodene som er knyttet til butikkene dine.
- Se butikkene dine.
  - Se fakturaer.
  - Se betalingsanmodningene dine.
  - Endre butikkenes webhooks.
- Endre betalingsforespørsler.
  - Se betalingsanmodningene dine.
- Bruk lynnodene som er knyttet til butikkene dine.
  - Se lynfakturaene som er knyttet til butikkene dine.
  - Opprett fakturaer fra lynnodene som er knyttet til butikkene dine.
- Sett inn penger på Exchange-kontoer som er knyttet til butikkene dine.
- Ta ut penger fra Exchange-kontoer til butikken din.
- Handle penger på butikkens Exchange-kontoer.


**Merk!


Når rollen opprettes, er navnet fast og kan ikke endres etter at den er i redigeringsmodus.


### E-post


Innstillingene for e-post på hele serveren ligner på innstillingene for butikkspesifikk e-post. Dette oppsettet håndterer imidlertid ikke bare utløsere for butikker eller administratorlogger, men også utløsere for andre hendelser. Dette e-postoppsettet gjør også passordgjenoppretting tilgjengelig på BTCPay Server ved innlogging. Det fungerer på samme måte som de butikkspesifikke innstillingene; administratorer kan raskt fylle ut e-postparametrene og angi e-postlegitimasjonen sin, slik at serveren kan sende e-post.


![image](assets/en/073.webp)


### Retningslinjer


Administratorer av BTCPay Server-policyer kan angi ulike innstillinger for emner som innstillinger for eksisterende brukere, innstillinger for nye brukere, varslingsinnstillinger og vedlikeholdsinnstillinger. Disse er ment for å registrere nye brukere som administratorer eller vanlige brukere, eller for å skjule BTCPay Server fra søkemotorer ved å legge den til i serverhodet.


![image](assets/en/074.webp)


#### Eksisterende brukerinnstillinger


Alternativene som er tilgjengelige her, er atskilt fra egendefinerte roller. Disse ekstra tillatelsene kan gjøre en butikk eller eieren sårbar for angrep. Retningslinjer som kan legges til for eksisterende brukere:



- Tillat ikke-administratorer å bruke den interne Lightning-noden i butikkene sine.
  - Dette vil gjøre det mulig for butikkeiere å bruke serveradministratorens Lightning-node og dermed hans midler! Vær oppmerksom på at dette ikke er en løsning for å gi tilgang til Lightning.
- Tillat ikke-administratorer å opprette Hot-lommebøker for butikkene sine.
  - Dette vil gjøre det mulig for alle med en konto på BTCPay-serverforekomsten din å opprette Hot-lommebøker og lagre seed-gjenoppretting på administratorens server. Dette kan gjøre administratoren ansvarlig for å holde tredjeparts midler!
- Tillat ikke-administratorer å importere Hot-lommebøker til butikkene sine.
  - I likhet med det forrige emnet om å opprette Hot-lommebøker, tillater denne policyen import av en Hot Wallet, med de samme farene som er nevnt i avsnittet om å opprette Hot-lommebøker.


![image](assets/en/075.webp)


#### Nye brukerinnstillinger


Vi kan angi noen viktige innstillinger for å administrere nye brukere som kommer til serveren. Vi kan angi en e-postbekreftelse for nye registreringer, deaktivere oppretting av nye brukere via påloggingsskjermen og begrense ikke-admins' tilgang til brukeroppretting via API-et.



- Krev en e-postbekreftelse for registrering.
  - Serveradministratoren må ha satt opp en e-postserver.
- Deaktiver registrering av nye brukere på serveren
- Deaktiver tilgang til API-sluttpunktet for brukeroppretting for ikke-administratorer.


Som standard har BTCPay Server slått på "Deaktiver registrering av nye brukere på serveren" og slått av ikke-administratorer tilgang til API-endepunktet for brukeropprettelse. Dette er av sikkerhetshensyn, slik at tilfeldige personer som snubler over BTCPay-påloggingen din ikke kan opprette kontoer.


![image](assets/en/076.webp)


#### Varslingsinnstillinger


![image](assets/en/077.webp)


#### Vedlikeholdsinnstillinger


BTCPay Server er et Open Source-prosjekt som ligger på GitHub. Hver gang BTCPay Server lanserer en ny versjon av programvaren, kan administratorer bli varslet om at en ny versjon er tilgjengelig. Administratorer vil kanskje også unngå at søkemotorer (som Google, Yahoo og DuckDuckGo) indekserer BTCPay Server-domenet. Ettersom BTCPay Server er FOSS, kan utviklere over hele verden ønske å lage nye funksjoner. BTCPay Server har en eksperimentell funksjon som, når den er slått på, gjør det mulig for administratorer å bruke funksjoner som ikke er ment for produksjon, men snarere for testformål.



- Sjekk utgivelser på GitHub og bli varslet når en ny BTCPay Server-versjon er tilgjengelig.
- Motvirke at søkemotorer indekserer dette nettstedet
- Aktiver eksperimentelle funksjoner.


![image](assets/en/078.webp)


#### Plugins


BTCPay Server kan legge til plugins og utvide funksjonssettet. Plugins lastes som standard inn fra BTCPay Server-plugin-byggerens depot. En administrator kan imidlertid velge å se programtillegg i en forhåndsversjon, og hvis programtilleggsutvikleren tillater det, kan serveradministratoren nå installere betaversjoner av programtillegg.


![image](assets/en/079.webp)


##### Innstillinger for tilpasning


En standard BTCPay Server-distribusjon vil være tilgjengelig via domenet som ble satt opp under installasjonen. En serveradministrator kan imidlertid tilordne rotdomenet på nytt og vise en av de opprettede appene fra en bestemt butikk. Serveradministratoren kan også tilordne bestemte domener til bestemte apper.



- Vis appen på nettstedets rot
  - Viser en liste over mulige apper som skal vises på rotdomenet.


![image](assets/en/080.webp)



- Tilordne bestemte domener til bestemte apper.
  - Når du klikker for å sette opp et bestemt domene for bestemte apper, kan administratoren sette opp så mange domener som peker til bestemte apper som nødvendig.


![image](assets/en/081.webp)


#### Blokkutforskere


BTCPay Server leveres som standard med Mempool.space som Block explorer for transaksjoner. Når BTCPay Server genererer en ny Invoice og en transaksjon er knyttet til den, kan butikkeieren klikke for å åpne transaksjonen. BTCPay Server vil som standard peke mot Mempool.space som Block explorer, men en serveradministrator kan endre dette til sitt foretrukne alternativ.


![image](assets/en/082.webp)


### Tjenester


Fanen "BTCPay Server-innstillinger: Tjenester" er en oversikt over komponentene som BTCPay-serveren din bruker. Tjenestene som BTCPay Server eksponerer kan variere avhengig av distribusjonsmetoden.


En BTCPay-serveradministrator kan klikke på "Se informasjon" bak hver tjeneste for å åpne den og angi spesifikke innstillinger.


![image](assets/en/083.webp)


#### LND (gRPC)


BTCPay eksponerer LNDs GRPC-tjeneste for eksternt forbruk; du finner tilkoblingsinformasjon i denne spesifikke innstillingsmenyen; kompatible lommebøker er oppført her. BTCPay Server gir også en QR-kode for tilkobling, som kan skannes og brukes i en mobil Wallet.


Serveradministratorer kan åpne flere detaljer for å se.



- Detaljer om verten
- Bruk av SSL
- Makroner
- AdminMacaroon
- FakturaMacaroon
- SkrivebeskyttetMacaroon
- GRPC SSL Cipher suite (GRPC_SSL_CIPHER_SUITES)


#### LND (REST)


BTCPay eksponerer LNDs REST-tjeneste for eksternt forbruk; du finner tilkoblingsinformasjon [her]((https://docs.btcpayserver.org/FAQ/LightningNetwork/#how-to-find-node-info-and-open-a-direct-channel-with-a-store-using-btcpay); kompatible lommebøker er oppført [her](https://docs.btcpayserver.org/FAQ/Wallet/#can-i-use-a-hardware-wallet-with-btcpay-server).. Blant de kompatible lommebøkene er Joule, Alby og ZeusLN. BTCPay Server tilbyr en QR-kode for tilkobling, som kan skannes og brukes i en kompatibel Wallet.



- REST URI
- Makron
- AdminMacaroon
- FakturaMacaroon
- SkrivebeskyttetMacaroon


#### LND seed Backup


LND seed-sikkerhetskopien er nyttig for å gjenopprette midler fra din LND Wallet i tilfelle serverfeil. Ettersom Lightning-noden er en Hot-Wallet, finner du konfidensiell seed-informasjon på denne siden.


LND dokumenterer gjenopprettingsprosessen. Se https://github.com/lightningnetwork/LND/blob/master/docs/recovery.md for dokumentasjon.


#### Ride The Lightning


Ride the Lightning er et verktøy for Lightning-nodeadministrasjon som er bygget som programvare med åpen kildekode. BTCPay Server bruker RTL som Lightning-nodeadministrasjonskomponent i stakken. BTCPay Server-administratorer kan nå RTL via Serverinnstillinger - fanen Tjenester eller ved å klikke på Lightning Wallet.


#### Full node P2P


Serveradministratorer ønsker kanskje å koble Bitcoin-noden sin til en mobil Wallet. Denne siden gir informasjon om hvordan du kobler deg eksternt til din Full node via P2P-protokollen. I skrivende stund viser BTCPay Server Blockstream Green- og Wasabi-lommebøker som kompatible lommebøker. BTCPay Server tilbyr en QR-kode for tilkobling, som kan skannes og brukes i en kompatibel Wallet.


#### Full node RPC


Denne siden inneholder informasjon om hvordan du kobler deg eksternt til Full node via RPC-protokollen.


#### SSH


SSH brukes til vedlikeholdsformål. BTCPay Server viser den første tilkoblingskommandoen for å nå serveren din og offentlige SSH-nøkler som er autorisert til å koble til serveren din. Serveradministratorer kan ønske å deaktivere SSH-endringer via BTCPay Server-brukergrensesnittet.


#### Dynamisk DNS


Dynamisk DNS lar deg ha et stabilt DNS-navn som peker til serveren din, selv om IP Address endres regelmessig. Dette anbefales hvis du er vert for BTCPay Server hjemme og ønsker å ha et klart nettdomene for å få tilgang til serveren din.


Merk at du må konfigurere NAT og BTCPay Server-installasjonen riktig for å få HTTPS-sertifikatet.


### Tema


BTCPay Server leveres som standard med to temaer: Lys og mørk modus. Disse kan byttes ved å klikke på Konto nederst til venstre og veksle mellom mørkt og lyst tema. BTCPay Server-administratorer kan legge til sitt eget tema ved å oppgi et tilpasset CSS-tema.


Administratorer kan utvide Light/Dark-temaet ved å legge til sin egen egendefinerte CSS eller angi det egendefinerte temaet som et fullstendig egendefinert tema.


![image](assets/en/084.webp)


#### Merkevarebygging av servere


Serveradministratorer kan endre BTCPay Server-merkevaren ved å angi en serveromfattende merkevare for bedriften din. Ettersom BTCPay Server er FOSS, kan serveradministratorer hvitmerke programvaren og tilpasse utseendet slik at det passer til deres virksomhet.


![image](assets/en/085.webp)


### Vedlikehold


Som serveradministrator forventer brukerne at du tar godt vare på serveren. I BTCPay Server-fanen Vedlikehold kan administratoren utføre en del viktig vedlikehold. Angi domenenavnet til BTCPay Server-forekomsten, start serveren på nytt eller rydde opp i den. Og kanskje viktigst av alt, kjøre oppdateringer.


BTCPay Server er et Open Source-prosjekt og oppdateres ofte. Hver nye utgivelse kunngjøres enten via BTCPay Server-varsler eller på de offisielle kanalene BTCPay Server kommuniserer gjennom.


![image](assets/en/086.webp)


#### Domenenavn


Etter at BTCPay Server er satt opp, kan det hende at en administrator ønsker å endre bort fra sitt opprinnelige domene. Under fanen Vedlikehold kan administratoren endre domenet. Etter at du har klikket på bekreft og satt opp de riktige DNS-postene på domenet, oppdateres BTCPay Server og starter på nytt for å gå tilbake til det nye domenet.


![image](assets/en/087.webp)


#### Start på nytt


Start BTCPay Server og relaterte tjenester på nytt.


![image](assets/en/088.webp)


#### Ren


BTCPay Server kjører med Docker-komponenter, og ved oppdateringer kan det være rester av Docker-bilder, midlertidige filer osv. Serveradministratorer kan frigjøre plass ved å kjøre Clean-skriptet.


![image](assets/en/089.webp)


#### Oppdatering


Det er det viktigste alternativet i kategorien Vedlikehold. BTCPay Server er bygget av fellesskapet, og derfor er oppdateringssyklusene hyppigere enn de fleste programvareprodukter. Når BTCPay Server har en ny versjon, vil administratorer bli varslet i varslingssenteret. Ved å klikke på oppdateringsknappen vil BTCPay Server sjekke GitHub for den nyeste versjonen, oppdatere serveren og starte på nytt. Før oppdatering anbefales serveradministratorer alltid å lese utgivelsesmerknadene som distribueres gjennom de offisielle kanalene til BTCPay Server.


![image](assets/en/090.webp)


### Logger


Det er aldri morsomt å stå overfor et problem. Dette dokumentet beskriver den vanligste arbeidsflyten og de vanligste trinnene for å identifisere og løse problemet på en effektiv måte, enten på egen hånd eller med hjelp fra fellesskapet.


Det er avgjørende å identifisere problemet.


#### Replikering av problemet


Først og fremst må du prøve å finne ut når problemet oppstår. Prøv å gjenskape problemet. Prøv å oppdatere og starte serveren på nytt for å bekrefte at du kan reprodusere problemet. Hvis det beskriver problemet bedre, kan du ta et skjermbilde.


##### Oppdatering av serveren


Sjekk din versjon av BTCPay Server hvis den er mye eldre enn [nyeste versjon](https://github.com/btcpayserver/btcpayserver/releases) av BTCPay Server. Oppdatering av serveren din kan løse problemet.


##### Starter serveren på nytt


Å starte serveren på nytt er en enkel måte å løse mange av de vanligste problemene med BTCPay-serveren på. Det kan hende du må SSH inn på serveren din slik at du kan starte den på nytt.


##### Starte en tjeneste på nytt


Det kan hende at du bare trenger å starte en bestemt tjeneste på nytt i BTCPay Server-distribusjonen for enkelte problemer, for eksempel å starte letsencrypt-containeren på nytt for å fornye SSL-sertifikatet.


```bash
sudo su -
cd btcpayserver-docker
docker restart letsencrypt-nginx-proxy-companion
```


Bruk docker ps for å finne navnet på en annen tjeneste du ønsker å starte på nytt.


#### Ser gjennom loggene


Logger kan gi viktig informasjon. I de følgende avsnittene vil vi beskrive hvordan du får tak i logginformasjon for ulike deler av BTCPay.


##### BTCPay-logger


Siden v1.0.3.8 kan du enkelt få tilgang til BTCPay-serverlogger fra frontend. Hvis du er serveradministrator, går du til Serverinnstillinger > Logger og åpner loggfilen. Hvis du ikke vet hva en bestemt feil i loggene betyr, kan du nevne det når du feilsøker.


Hvis du vil ha mer detaljerte logger og bruker en Docker-distribusjon, kan du vise logger for spesifikke Docker-containere ved hjelp av kommandolinjen. Se disse [instruksjonene for å ssh](https://docs.btcpayserver.org/FAQ/ServerSettings/#how-to-ssh-into-my-btcpay-running-on-vp%C2%80) inn i en forekomst av BTCPay som kjører på en VPS.


På neste side finner du en generell liste over containernavnene som brukes for BTCPay Server.


Kjør kommandoene nedenfor for å skrive ut logger etter beholdernavn. Bytt ut beholdernavnet for å vise andre beholderlogger.


```bash
sudo su -
cd btcpayserver-docker
docker ps
docker logs --tail 100 generated_btcpayserver_1
```



| Logg for      | Beholdernavn                       |
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


Det er flere måter å få tilgang til LND-loggene dine på når du bruker Docker. Først logger du på som root:


```bash
sudo su -
Navigate to the correct directory:
cd btcpayserver-docker
# Find container name:
docker ps
Print logs by container name:
docker logs --tail 100 btcpayserver_lnd_bitcoin
```


Alternativt kan du raskt skrive ut logger ved å bruke beholder-ID-en (bare de første unike ID-tegnene er nødvendige, for eksempel de to tegnene lengst til venstre):


```bash
docker logs 'add your container ID'
```


Hvis du av en eller annen grunn trenger flere logger


```bash
sudo su -
cd /var/lib/docker/volumes/generated_lnd_bitcoin_datadir/\_data/logs/ bitcoin/mainnet/
ls
```


Du vil se noe sånt som


```bash
lnd.log lnd.log.13 lnd.log.15 lnd.log.16.gz lnd.log.17.gz
```


For å få tilgang til ukomprimerte logger av disse loggene, gjør `cat LND.log` eller hvis du vil ha en annen, bruk `cat LND.log.15`.


For å få tilgang til komprimerte logger i `.gzip`, bruk `gzip -d LND.log.16.gz` (i dette tilfellet får vi tilgang til `LND.log.16.gz`). Dette bør gi deg en ny fil, hvor du kan gjøre `cat LND.log.16`. Hvis dette ikke fungerer, kan det hende du må installere gzip først med `sudo apt-get install gzip`.


###### Lightning Network c-lightning - Docker


```bash
sudo su -
docker ps
# Find the c-lightning container ID.
docker logs 'add your container ID here'
```


Alternativt kan du bruke denne:


```bash
docker logs --tail 100 btcpayserver_clightning_bitcoin
```


Du kan også få logginformasjon med kommandoen c-lightning CLI.


```bash
bitcoin-lightning-cli.sh getlog
```


#### Bitcoin Node-logger


I tillegg til å [se på logger](https://docs.btcpayserver.org/Troubleshooting/#2-looking-through-the-logs) i bitcoind-containeren din, kan du også bruke noen av [bitcoin-cli-kommandoene](https://developer.Bitcoin.org/reference/RPC/index.html)


[(åpner nytt vindu)](https://developer.Bitcoin.org/reference/RPC/index.html) for å innhente informasjon fra Bitcoin-noden din. BTCPay inkluderer et skript som gjør det enkelt å kommunisere med Bitcoin-noden din.


I btcpayserver-docker-mappen henter du Blockchain-informasjonen ved hjelp av noden din:


```bash
bitcoin-cli.sh getblockchaininfo
```


### Filer


BTCPay Server har et lokalt filsystem som gjør det mulig å laste opp butikkressurser (produkter), logoer og merkevarebygging direkte til serveren. Serverens filsystem er bare tilgjengelig for serveradministratorer; butikkeiere kan laste opp logoer eller merkevarebygging på butikknivå.


Når serveradministratoren befinner seg i fanen Fillagring, er det mulig å laste opp direkte til serveren eller endre fillagringsleverandøren til et lokalt filsystem eller Azure Blob Storage.


![image](assets/en/091.webp)


![image](assets/en/092.webp)


### Oppsummering av ferdigheter


I denne delen lærte du følgende:



- Forskjellen mellom Store- og Server-innstillinger, spesielt når det gjelder brukere, roller og e-postmeldinger
- Angi serveromfattende policyer for bruk og oppretting av Lightning eller Bitcoin Hot Wallet Wallet Wallet Wallet, registrering av nye brukere og e-postvarsler.
- Hvordan legge til egendefinerte temaer (i stedet for de enkle lys/mørke-alternativene som tilbys), samt lage egendefinerte logoer
- Utfør enkle vedlikeholdsoppgaver på serveren via det medfølgende brukergrensesnittet
- Feilsøke problemer, inkludert henting av detaljer for en av Docker-containerne eller noden din
- Administrer fillagring


### Vurdering av kunnskap


#### KA Konseptuell gjennomgang


Hva er forskjellen på roller som tildeles via server- og butikkinnstillinger, og hva kan man bruke den ene til fremfor den andre?


#### KA Praktisk gjennomgang


Beskriv noen mulige bruksområder som er aktivert i Policy-fanen.


#### KA Praktisk gjennomgang


Beskriv noen handlinger en administrator rutinemessig kan utføre i kategorien Vedlikehold.


## BTCPay Server - Betalinger


<chapterId>e2b71ff9-3f4f-5e71-9771-8e03fbbef00f</chapterId>


En Invoice er et dokument som selgeren utsteder til kjøperen for å kreve betaling.


I BTCPay Server representerer en Invoice et dokument som må betales innen et definert tidsintervall til en fast Exchange-kurs. Fakturaer har utløpsdatoer fordi de låser Exchange-kursen innenfor en spesifisert tidsramme, noe som beskytter mottakeren mot prissvingninger.


Kjernen i BTCPay Server er muligheten til å fungere som et Bitcoin Invoice-styringssystem. En Invoice er et viktig verktøy for å spore og administrere mottatte betalinger.


Med mindre du bruker en innebygd [Wallet](https://docs.btcpayserver.org/Wallet/) for å motta betalinger manuelt, vil alle betalinger i en butikk vises på siden Fakturaer. Denne siden sorterer betalinger kumulativt etter dato og fungerer som en sentral ressurs for Invoice-administrasjon og feilsøking av betalinger.


![image](assets/en/093.webp)


### Generelt


#### Invoice-statuser


Tabellen nedenfor viser og beskriver standard Invoice-statusene i BTCPay, sammen med forslag til vanlige tiltak. Handlingene er bare anbefalinger. Det er opp til brukerne å definere hva som er best for deres brukstilfelle og virksomhet.



| Fakturastatus | Beskrivelse | Handling |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| New | Ikke betalt, fakturatimeren har ennå ikke utløpt | Ingen |
| New (paidPartial) | Betalt, ikke fullt beløp, fakturatimeren har ennå ikke utløpt | Ingen |
| Expired | Ikke betalt, fakturatimeren er utløpt | Ingen |
| Expired (paidPartial) ** | Betalt, ikke fullt beløp, og utløpt | Kontakt kjøper for å avtale refusjon eller be dem betale restbeløpet. Marker eventuelt fakturaen som settled eller invalid |
| Expired (paidLate) | Betalt, fullt beløp, etter at fakturatimeren er utløpt | Kontakt kjøper for å avtale refusjon eller behandle ordren dersom sene bekreftelser aksepteres. |
| Settled (paidOver) | Betalt mer enn fakturabeløpet, oppgjort, mottatt tilstrekkelig antall bekreftelser | Kontakt kjøper for å avtale refusjon av det overskytende beløpet, eller vent på at kjøper kontakter deg |
| Processing | Betalt fullt ut, men har ikke mottatt tilstrekkelig antall bekreftelser spesifisert i butikkinnstillingene | Kontakt kjøper for å avtale refusjon av det overskytende beløpet, eller vent på at kjøper kontakter deg |
| Processing (paidOver) | Betalt mer enn fakturabeløpet, ikke mottatt tilstrekkelig antall bekreftelser | Vent til status blir settled, kontakt deretter kjøper for refusjon av overskytende beløp, eller vent på kontakt |
| Settled | Betalt, fullt ut, mottatt tilstrekkelig antall bekreftelser i butikken | Fullfør ordren |
| Settled (marked) | Status ble manuelt endret til settled fra en processing- eller invalid-status | Butikkadministrator har markert betalingen som settled |
| Invalid* | Betalt, men mottok ikke tilstrekkelig antall bekreftelser innen tiden spesifisert i butikkinnstillingene | Sjekk transaksjonen på en blockchain-utforsker; hvis den har fått nok bekreftelser, marker som settled |
| Invalid (marked) | Status ble manuelt endret til invalid fra en settled- eller expired-status | Butikkadministrator har markert betalingen som invalid |
| Invalid (paidOver) | Betalt mer enn fakturabeløpet, men mottok ikke nok bekreftelser innen fristen i butikkinnstillingene | Sjekk transaksjonen på en blockchain-utforsker; hvis den har fått nok bekreftelser, marker som settled |

#### Detaljer om Invoice


Invoice-informasjonssiden inneholder all informasjon knyttet til en Invoice.


Invoice-informasjon opprettes automatisk basert på Invoice-status, Exchange-pris osv. Produktinformasjon opprettes automatisk hvis Invoice ble opprettet med produktinformasjon, for eksempel i Point of Sale-appen.


#### Invoice-filtrering


Fakturaer kan filtreres ved hjelp av hurtigfiltrene ved siden av søkeknappen eller de avanserte filtrene, som du kan veksle mellom ved å klikke på (Hjelp)-lenken øverst. Brukerne kan filtrere fakturaer etter butikk, ordre-ID, vare-ID, status eller dato.


#### Invoice eksport


BTCPay Server-fakturaer kan eksporteres i CSV- eller JSON-format. For mer informasjon om Invoice eksport og regnskap.


#### Refundering av en Invoice


Hvis du av en eller annen grunn ønsker å utstede en refusjon, kan du enkelt opprette en refusjon fra Invoice-visningen.


#### Arkivering av fakturaer


Som et resultat av at BTCPay Server ikke har noen Address-funksjon for gjenbruk, er det vanlig å se mange utløpte fakturaer på butikkens Invoice-side. For å skjule dem fra visningen, velger du dem i listen og markerer dem som arkivert. Fakturaer som er merket som arkiverte, slettes ikke. Betaling til en arkivert Invoice vil fortsatt bli oppdaget av BTCPay-serveren din (paidLate-status). Du kan når som helst se butikkens arkiverte fakturaer ved å velge arkiverte fakturaer fra rullegardinmenyen for søkefilteret.


#### Standard valuta


Butikkens standardvaluta, som ble angitt i veiviseren for oppretting av butikken.


#### Tillat hvem som helst å opprette en Invoice


Du bør aktivere dette alternativet hvis du vil tillate omverdenen å opprette fakturaer i butikken din. Dette alternativet er bare nyttig hvis du bruker betalingsknappen eller hvis du utsteder fakturaer via API eller et tredjeparts HTML-nettsted. PoS-appen er forhåndsautorisert og krever ikke at denne innstillingen er aktivert for at en tilfeldig besøkende skal kunne åpne POS-butikken din og opprette en Invoice.


#### Legg til en ekstra avgift (nettverksavgift) til Invoice



- Bare hvis kunden foretar mer enn én betaling for Invoice
- Ved hver betaling
- Legg aldri til en nettverksavgift


#### Invoice utløper hvis ikke hele beløpet er betalt etter ... Protokoll.


Invoice-timeren er satt til 15 minutter som standard. Tidtakeren fungerer som en beskyttelsesmekanisme mot volatilitet, ettersom den låser kryptovalutabeløpet basert på krypto-til-fiat-kursene. Hvis kunden ikke betaler Invoice innen den definerte perioden, anses Invoice som utløpt. Invoice anses som "betalt" så snart transaksjonen er synlig på Blockchain (med null bekreftelser), og anses som "fullført" når den når det antallet bekreftelser som forhandleren har definert (vanligvis 1-6). Timeren kan tilpasses.


#### Betrakt Invoice som betalt selv om det betalte beløpet er ..% mindre enn forventet.


I en situasjon der en kunde bruker en Exchange Wallet til å betale direkte for en Invoice, tar Exchange et lite gebyr. Dette betyr at en slik Invoice ikke anses som fullstendig fullført. Invoice er merket som "delvis betalt" Hvis en forhandler ønsker å godta underbetalte fakturaer, kan du angi prosentsatsen her


### Forespørsler


Betalingsforespørsler er en funksjon som gjør det mulig for BTCPay-butikkeiere å opprette fakturaer med lang levetid. Midler betales i henhold til betalingsforespørselen ved hjelp av Exchange-satsen som gjelder på betalingstidspunktet. Dette gjør det mulig for brukere å foreta betalinger når det passer dem uten å måtte forhandle eller verifisere Exchange-satser med butikkeieren på betalingstidspunktet.


Brukere kan betale for forespørsler i delbetalinger. Betalingsforespørselen forblir gyldig til den er betalt i sin helhet, eller hvis butikkeieren krever en utløpstid. Adresser gjenbrukes aldri. En ny Address genereres hver gang brukeren klikker på betal for å opprette en Invoice for betalingsforespørselen.


Butikkeiere kan skrive ut betalingsforespørsler (eller eksportere Invoice-data) for journalføring og regnskap. BTCPay merker automatisk fakturaer som betalingsforespørsler i butikkens Invoice-liste.


#### Tilpass betalingsforespørslene dine



- Invoice Beløp - Angi ønsket betalingsbeløp
- Pålydende - Vis det forespurte beløpet i Fiat eller kryptovaluta
- Betalingsmengde - Tillat kun enkeltbetalinger eller delbetalinger
- Utløpstid - Tillat betalinger frem til en dato eller uten utløp
- Beskrivelse - Tekstredigeringsprogram, datatabeller, innbygging av bilder og videoer
- Utseende - farge og stil med CSS-temaer


![image](assets/en/094.webp)


#### Opprett en betalingsforespørsel


Gå til Betalingsanmodning i menyen til venstre og klikk på "Opprett betalingsanmodning".


![image](assets/en/095.webp)


Oppgi navn på forespørselen, beløp, visningsbetegnelse, tilknyttet butikk, utløpstid og beskrivelse (valgfritt)


Velg alternativet Tillat betalingsmottaker å opprette fakturaer i deres denominasjon hvis du vil tillate delbetalinger.


Klikk på Lagre og vis for å se gjennom betalingsforespørselen din.


BTCPay oppretter en URL for betalingsforespørselen. Del denne URL-en for å se betalingsforespørselen din. Trenger du flere av den samme forespørselen? Du kan duplisere betalingsforespørsler ved å bruke alternativet Klon i hovedmenyen.


![image](assets/en/096.webp)


**ADVARSEL**


Betalingsforespørsler er butikkavhengige, noe som betyr at hver betalingsforespørsel er knyttet til en butikk når den opprettes. Sørg for å ha en Wallet koblet til butikken som betalingsforespørselen tilhører.


#### Betalt forespørsel


Betalingsmottaker og rekvirent kan se status for betalingsanmodningen etter at betalingen er sendt. Status vises som Oppgjort hvis betalingen er mottatt i sin helhet. Hvis bare delbetalinger har blitt utført, viser Beløp som skal betales den gjenstående saldoen.


![image](assets/en/097.webp)


#### Tilpass betalingsforespørsler


Beskrivelsesinnholdet kan redigeres ved hjelp av tekstredigeringsprogrammet for betalingsforespørselen. Begge alternativene er tilgjengelige hvis du vil bruke flere fargetemaer eller tilpasset CSS-styling.


Ikke-tekniske brukere kan bruke et [bootstrap-tema](https://docs.btcpayserver.org/Development/Theme/#2-bootstrap-themes). Ytterligere tilpasning kan gjøres ved å tilføre ytterligere CSS-kode, som vist nedenfor.


```css
:root {
--btcpay-font-family-base: "Source Sans Pro", -apple-system,
BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
--btcpay-primary: #7d4698;
--btcpay-primary-accent: #59316b;
--btcpay-body-text: #333a41;
--btcpay-body-bg: #fff;
--btcpay-bg-tile: #f8f9fa;
}

#mainNav {
color: white;
background: linear-gradient(#59316b, #331840);
}

#mainNav .btn-link {
color: white;
}
```


### Trekk betalinger


Tradisjonelt deler en mottaker sin Bitcoin Address for å foreta en Bitcoin-betaling, og avsenderen sender senere penger til denne Address. Et slikt system kalles push-betaling, ettersom avsenderen initierer betalingen mens mottakeren kanskje ikke er tilgjengelig, og sender betalingen til mottakeren.


Men hva med å snu på rollene?


Hva om avsenderen i stedet for å pushe betalingen, lar mottakeren trekke betalingen på et tidspunkt som mottakeren finner passende? Dette er konseptet Pull-betaling. Dette åpner for flere nye bruksområder, for eksempel:



- En abonnementstjeneste (der abonnenten lar tjenesten trekke penger hver x antall timer)
- Refusjoner (der forhandleren lar kunden trekke refusjonspengene til Wallet når de selv ønsker det)
- Tidsbasert fakturering for frilansere (der den som ansetter frilanseren lar frilanseren trekke penger inn i Wallet etter hvert som tiden blir rapportert)
- Mécénat (der mæcenen lar mottakeren ta ut penger hver måned for å fortsette å støtte arbeidet deres)
- Automatisk salg (der en kunde av en Exchange tillater en Exchange å trekke penger fra sin Wallet for å selge automatisk hver måned)
- Saldouttakssystem (der en tjeneste med høyt volum lar brukerne be om uttak fra saldoen sin, og tjenesten kan deretter enkelt samle alle utbetalingene til mange brukere med faste intervaller)


### Utbetalinger


Utbetalingsfunksjonaliteten er knyttet til funksjonen [Pull Payments](https://docs.btcpayserver.org/PullPayments/). Denne funksjonen lar deg opprette utbetalinger i BTCPay. Med denne funksjonen kan du behandle pull-betalinger (refusjoner, lønnsutbetalinger eller uttak).


#### Eksempel 1: Refusjon


La oss begynne med eksemplet med refusjon. Kunden har kjøpt en vare i butikken din, men dessverre må de returnere den. De ønsker en refusjon. I BTCPay kan du opprette en [Refusjon](https://docs.btcpayserver.org/Refund/) og gi kunden en lenke til å kreve pengene sine. Når kunden har oppgitt Address og gjort krav på pengene, vil det vises i utbetalingsdelen.


Den første statusen den har, er Venter på godkjenning. Butikkmedarbeiderne kan sjekke om det er flere som venter, og når du har gjort valget, bruker du knappen Handlinger.


Alternativer på handlingsknappen



- Godkjenn utvalgte utbetalinger
- Godkjenn og send utvalgte utbetalinger
- Avbryt valgte utbetalinger


Neste trinn er å godkjenne og sende valgte utbetalinger, ettersom vi ønsker å refundere kunden. Sjekk kundens Address, som viser beløpet og om vi ønsker at gebyrene skal trekkes fra refusjonen eller ikke. Når du har fullført kontrollene, er det bare å signere transaksjonen.


Kunden blir nå oppdatert på Claiming-siden. Han kan følge transaksjonen ved at han får en lenke til en Block explorer og transaksjonen sin. Når transaksjonen er bekreftet, endres statusen til "Fullført".


#### Eksempel 2: Lønn


La oss nå se nærmere på lønnsutbetaling, siden dette styres fra butikken og ikke i henhold til kundens forespørsel. Det underliggende konseptet er det samme; det bruker pull-betalinger. Men i stedet for å opprette en refusjon, lager vi en [Pull Payment](https://docs.btcpayserver.org/PullPayments/).


Gå til Pull Payments-fanen på BTCPay-serveren din. Klikk på knappen Opprett pull-betaling øverst til høyre.


Nå er vi i ferd med å opprette utbetalingen, gi den et navn og ønsket beløp i den valgte valutaen. Fyll ut beskrivelsen, slik at den ansatte vet hva det dreier seg om. Den neste delen ligner på refusjoner. Den ansatte fyller ut Destinasjon Address og beløpet han ønsker å kreve fra denne utbetalingen. Han kan bestemme seg for å gjøre det til to separate krav, til forskjellige adresser, eller til og med delvis kreve over lynet.


Hvis det er flere ventende utbetalinger, kan du samle disse for å signere og sende dem ut. Når utbetalingene er signert, flyttes de til fanen Pågående og viser Transaksjon. Når utbetalingen er akseptert av nettverket, flyttes den til fanen Fullført. Fanen Fullført er kun for historiske formål. Den inneholder de behandlede utbetalingene og transaksjonene som hører til den


### Trekk betalinger


#### Konsept


Når en avsender konfigurerer en Pull-betaling, kan de konfigurere en rekke egenskaper:



- Dra forespørsel Navn
- Et grensebeløp
- En enhet (for eksempel BTC, SAT, USD)
- Betalingsmetoder
  - BTC On-Chain
  - BTC off-chain
- Beskrivelse
- Tilpasset CSS
- Sluttdato (valgfritt for Lightning Network BOLT11)


Deretter kan avsenderen dele pull-betalingen med mottakeren ved hjelp av en lenke, slik at mottakeren kan opprette en utbetaling. Mottakeren velger selv utbetalingen:



- Hvilken betalingsmetode du skal bruke
- Hvor du skal sende pengene


Når en utbetaling er opprettet, vil den telle med i pull-betalingsgrensen for den aktuelle perioden. Avsenderen godkjenner deretter utbetalingen ved å angi hvilken sats utbetalingen skal sendes til, og fortsetter med betalingen.


For avsenderen tilbyr vi en brukervennlig metode for å samle flere utbetalinger fra [BTCPay Internal Wallet](https://docs.btcpayserver.org/Wallet/).


#### Greenfield API


BTCPay Server tilbyr et fullstendig API til både avsender og mottaker som er dokumentert på `/docs`-siden i din forekomst. (eller på dokumentasjonsnettstedet https://docs.btcpayserver.org)


Siden API-et vårt gir full tilgang til pull-betalinger, kan en avsender automatisere betalingene etter egne behov.


### Oppsummering av ferdigheter


I denne delen lærte du følgende:



- Inngående forståelse av BTCPay Server's Invoice-statuser, samt handlinger som kan utføres på dem
- Tilpass og administrer Invoice-mekanismer med forlenget levetid, kjent som Requests.
- De ekstra fleksible betalingsmulighetene som åpnes med BTCPay Servers unike Pull Payment-funksjon, spesielt når det gjelder håndtering av refusjoner og lønnsutbetalinger.


### Vurdering av kunnskap


#### KA Konseptuell gjennomgang


Hva er forskjellen mellom fakturaer og betalingsanmodninger, og hva kan være en god grunn til å bruke sistnevnte?


#### KA Konseptuell gjennomgang


Hvordan utvider pull-betalinger det som vanligvis kan gjøres med On-Chain? Beskriv noen brukstilfeller de muliggjør.


## BTCPay Server Standard Plugins


<chapterId>7d673dc4-bd5d-5411-819b-f135f1d86636</chapterId>


### Standard plugins og apper


BTCPay Server leveres med et standardsett med plugins (apper) som kan gjøre BTCPay Server om til en betalingsgateway for e-handel. Med tillegg av et salgssted, en Crowdfund-plattform og en enkel betalingsknapp blir BTCPay Server en løsning som er enkel å distribuere.


### Utsalgssted


En av standardtilleggene til BTCPay Server er Point of Sale (PoS). Med PoS-tillegget kan en butikkeier opprette en nettbutikk direkte fra BTCPay Server; butikkeieren trenger ikke tredjeparts e-handelsløsninger for å drive en nettbutikk. Den nettbaserte PoS-appen gjør det mulig for brukere med fysiske butikker å enkelt akseptere Bitcoin, uten gebyrer eller en tredjepart, direkte i sin Wallet. PoS kan enkelt vises på nettbrett eller andre enheter som støtter nettsurfing. Brukerne kan enkelt opprette en snarvei på startskjermen for å få rask tilgang til webappen.


#### Slik oppretter du et nytt salgssted


BTCPay Server gjør det mulig for butikkeiere å raskt opprette et salgssted med flere oppsett. BTCPay Server erkjenner at ikke alle butikker er e-handel, og ikke alle butikker er en bar eller restaurant, og den leveres med flere standardoppsett for PoS.


Når butikkeieren klikker på "Point of Sale" i menylinjen til venstre, vil BTCPay Server nå be om et navn; dette navnet vil være synlig i menylinjen til venstre. Klikk på Opprett for å opprette PoS.


![image](assets/en/098.webp)


#### Oppdater det nyopprettede Point of Sale


Etter at du har opprettet en ny PoS, kan du i følgende skjermbilde oppdatere Point of Sale og legge til varer i butikken.


##### Appens navn


Navnet som gis her til salgsstedet ditt, vil være synlig i hovedmenyen på BTCPay Server.


##### Vis tittel


Publikum vil se tittelen eller navnet på butikken din når de besøker den. BTCPay Server navngir som standard butikken din "Te-butikk" Erstatt dette med butikkens navn.


![image](assets/en/099.webp)


#### Velg salgsstedets stil


BTCPay Server er i stand til å vise salgsstedet på flere måter.



- Produktliste
  - En butikkvisning der kundene bare kan kjøpe ett produkt om gangen.
- Produktliste med handlevogn.
  - En butikkvisning der kundene kan kjøpe flere varer samtidig og få en oversikt over handlekurven til høyre på skjermen.
- Kun tastatur
  - Ingen produktliste, bare et tastatur for direktefakturering.
- Utskriftsvisning (utskrivbar produktliste med QR)
  - Hvis du ikke alltid kan vise produktlisten din digitalt, trenger du en "offline"-løsning for produkter; BTCPay Server har en utskriftsskjerm som fungerer som en offline-butikk.


![image](assets/en/100.webp)


#### Point Of Sale Style - Produktliste


![image](assets/en/101.webp)


#### Point Of Sale Style - Produktliste + handlevogn


![image](assets/en/102.webp)


#### Point Of Sale Style - kun tastatur


![image](assets/en/103.webp)


#### Point of Sale Style - Print display


![image](assets/en/104.webp)


#### Valuta


Butikkeieren kan angi en annen valuta for utsalgsstedet enn den generelle standardvalutaen som er angitt. Butikkens standardvaluta vil automatisk fylle ut dette feltet.


#### Beskrivelse


Fortell verden om butikken din; hva selger du, og for hvor mye? Alt som forklarer butikken din skal stå her.


![image](assets/en/105.webp)


#### Produkter


Når et utsalgssted opprettes, legger en standard BTCPay-server til et par elementer i butikken som referanse. Klikk på Rediger-knappen på et av standardelementene for å få en bedre forståelse av alle de mulige alternativene for et element.


Når du oppretter et nytt produkt i butikken, består det av følgende felter;



- Tittel
- Pris (fast, minimum eller tilpasset)
- Bilde-URL
- Beskrivelse
- Lagerbeholdning
- ID
- Kjøp Knapptekst.
- Aktivere/deaktivere


Når butikkeieren har fylt ut alle de nye produktfeltene, klikker du på lagre, og du vil legge merke til at produktdelen i Point of Sale nå fylles ut. Lagre alltid øverst i høyre hjørne av skjermen for å unngå at butikkeiere mister fremdriften når de legger til produkter.


Butikkeiere kan også bruke "Raw Editor" til å konfigurere produktene sine. Raw Editor krever en grunnleggende forståelse av JSON-strukturer.


![image](assets/en/106.webp)


#### Kasse


BTCPay Server gir mulighet for små PoS-spesifikke kassetilpasninger. Butikkeieren kan angi teksten "Kjøp for x" eller be om spesifikke kundedata ved å legge dem til i skjemaene.


#### Tips


Bare noen butikker trenger muligheten for tips om salget sitt. Butikkeiere kan slå dette av eller på etter eget ønske. Hvis butikken bruker tips slått på, kan butikkeieren angi teksten i feltet for tipsene de ønsker. BTCPay Server-tips fungerer basert på et prosentbeløp. Butikkeiere kan legge til flere prosentandeler, atskilt med komma.


#### Rabatter


Som butikkeier kan det være lurt å gi kunden en tilpasset rabatt i kassen; bryteren for Rabatter blir tilgjengelig i butikkens kasse. Dette frarådes imidlertid på det sterkeste ved bruk av selvbetjente kassasystemer.


#### Tilpassede betalinger


Når alternativet Egendefinerte betalinger er slått på, kan kunden legge inn en fast pris som er lik eller høyere enn den opprinnelige Invoice generert av butikken.


#### Ytterligere alternativer


Etter at du har satt opp alt for salgsstedet ditt, er det noen ekstra alternativer igjen. Butikkeiere kan enkelt legge inn PoS gjennom en Iframe eller legge inn en betalingsknapp som lenker til en bestemt butikkvare. For å stilisere den nettopp opprettede PoS-butikken, kan eiere legge til tilpasset CSS nederst i tilleggsalternativene.


#### Slett denne appen


Hvis butikkeieren ønsker å slette salgsstedet helt fra BTCPay Server, kan butikkeiere nederst i oppdateringen av PoS klikke på Slett denne app-knappen for å ødelegge PoS-appen fullstendig. Når du klikker på "Slett denne appen", vil BTCPay Server be om bekreftelse ved å skrive `DELETE` og bekrefte ved å klikke på Slett-knappen. Etter å ha slettet, kommer butikkeieren tilbake til BTCPay Server-dashbordet.


### BTCPay Server - Crowdfund


Ved siden av Point of Sale-plugin har BTCPay Server muligheten til å opprette en crowdfund. Akkurat som alle andre Crowdfund-plattformer, kan butikkeiere sette et mål, lage fordeler for bidrag og tilpasse det til deres behov.


#### Slik oppretter du en ny crowdfund


Klikk på Crowdfund-plugin via hovedmenyen til venstre på BTCPay Server, under Plugin-delen. BTCPay Server vil nå be om et navn for Crowdfund; dette navnet vil også vises i menylinjen til venstre.


![image](assets/en/107.webp)


#### Oppdater det nyopprettede Point of Sale


Når appen har fått et navn, er neste skjermbilde å oppdatere appen slik at den har en kontekst.


#### Appens navn


Navnet du har gitt Crowdfund-fondet ditt, vil være synlig i hovedmenyen på BTCPay Server.


#### Vis tittel


Tittelen er gitt til Crowdfund for publikum.


#### Tagline


Gi innsamlingsaksjonen en one-liner for å vise hva innsamlingen handler om.


![image](assets/en/108.webp)


#### URL til utvalgt bilde


Hver crowdfund har sitt hovedbilde, det ene banneret som du kjenner igjen direkte. Dette bildet kan lagres på serveren din hvis du har administrative rettigheter. Administratorer kan laste opp under BTCPay Server-innstillinger - Filer. Når du er butikkeier, må bildet lastes opp til nettet via en tredjepartsvert (for eksempel Imgur).


#### Gjør crowdfundingen offentlig


Denne bryteren gjør crowdfundingen offentlig og dermed synlig for omverdenen. For testformål eller for å se om temaet ditt brukes riktig, bør du holde denne innstilt på AV så lenge du bygger crowdfundingen.


#### Beskrivelse


Fortell verden om din Crowdfund. Hva samler du inn penger til? Alt som forklarer folkeinnsamlingen din skal stå her.


![image](assets/en/109.webp)


#### Crowdfunding-mål


Sett et mål for hva innsamleren skal tjene til prosjektet, og hvilken valuta målet skal være i. Sørg for at hvis målene dine er satt mellom datoer, må du inkludere disse mål- og sluttdatoene under Mål i crowdfund.


![image](assets/en/110.webp)


#### Frynsegoder


Frynsegoder kan forbedre crowdfunding-innsatsen din betydelig. Dette er fordi frynsegoder gir folk en måte å delta i kampanjen din på. De utnytter både egoistiske og velvillige motivasjoner. Og de gir deg tilgang til støttespillernes forbruk, ikke bare deres filantropiske pengepung - du kan selv gjette hva som er viktigst.


Når du oppretter en ny fordel, består den av følgende felt.



- Tittel
- Pris (fast, minimum eller tilpasset)
- Bilde-URL
- Beskrivelse
- Lagerbeholdning
- ID
- Kjøp Knapptekst.
- Aktivere/deaktivere


Når butikkeieren har fylt ut alle feltene for den nye frynsegoden, klikker du på lagre, og du vil legge merke til at frynsegoder-delen i Crowdfunds nå fylles ut.


![image](assets/en/111.webp)


### BTCPay Server - salgssted


#### Bidrag


Butikkeiere kan velge hvordan frynsegoder skal vises, hvordan de skal sorteres, eller til og med rangere dem opp mot andre frynsegoder. Når Crowdfunds-målene er nådd, kan det imidlertid være at butikkeieren ønsker å stoppe donasjoner til denne innsamlingsaksjonen. Derfor kan han slå på "Ikke tillat ytterligere bidrag etter at målet er nådd". Dette vil forhindre at innsamlingsaksjonen tar imot donasjoner.


##### Crowdfunding-atferd


Crowdfunds standard teller bare fakturaer som er opprettet med Crowdfund, mot målet. Det kan imidlertid være tilfeller der butikkeieren ønsker at alle fakturaer som er opprettet i denne butikken, skal telle med i crowdfundingen.


#### Ytterligere alternativer for tilpasning


BTCpay Server tilbyr et par ekstra tilpasninger. Legg til lyder, animasjoner eller til og med diskusjonstråder i Crowdfund. Butikkeiere kan også endre utseendet og følelsen av Crowdfund ved å legge inn sin egen tilpassede CSS.


#### Slett denne appen


Hvis butikkeieren ønsker å slette Crowdfund helt fra BTCPay Server, kan de nederst i oppdateringen av Crowdfund klikke på knappen "Slett denne appen" for å fjerne Crowdfund-appen helt. Når du klikker på "Slett denne appen", vil BTCPay Server be om bekreftelse ved å skrive `DELETE` og bekrefte ved å klikke på Slett-knappen. Etter å ha slettet, kommer butikkeieren tilbake til BTCPay Server-dashbordet.


### BTCPay Server - Betalingsknapp


HTML-betalingsknapper som enkelt kan integreres og tilpasses, gjør det mulig for butikkeiere å motta tips og donasjoner. I menylinjen til venstre på BTCPay Server, under Plugins-delen, kan butikkeiere klikke på "Betalingsknapp" og klikke på Aktiver for å opprette en betalingsknapp.


#### Generelle innstillinger


I de generelle innstillingene for betalingsknappen kan butikkeiere angi



- Standard pris
- Standard valuta
- Standard betalingsmåte
  - Bruk butikkens standard
  - BTC On-Chain
  - BTC off-chain (Lyn)
  - BTC off-chain (LNURL-betaling)
- Beskrivelse av kassen
- Bestillings-ID


#### Visningsalternativer


BTCPay Servers betalingsknapp kan konfigureres slik at den passer til ulike stiler. Knappene kan ha et fast eller egendefinert beløp, som enten vises med en glidebryter eller pluss- og minusknapper.


#### Bruk Modal


Når du oppretter betalingsknappen, kan butikkeiere velge hvordan den skal oppføre seg når en kunde klikker på den, og vise den i en modal eller som en ny side.


**Merk!


Advarsel: Betalingsknappen skal kun brukes til tips og donasjoner


Det anbefales ikke å bruke betalingsknappen for e-handelsintegrasjoner, siden brukeren kan endre bestillingsrelevant informasjon. For e-handel bør du bruke Greenfield API-et vårt. Hvis denne butikken behandler kommersielle transaksjoner, anbefaler vi at du oppretter en egen butikk før du bruker betalingsknappen.


#### Tilpass teksten på betalingsknappen


Som standard står det "Betal med BTCPay" på BTCPay Servers betalingsknapp. Butikkeiere kan angi denne teksten etter eget ønske og endre BTCPay Server-logoen til sin egen. Still inn teksten ved å bruke "Pay Button Text" og lim inn bilde-URL-en under "Pay Button Image URL".


##### Bildestørrelse


Størrelsen på bildet i knappen kan bare settes til tre standardverdier.



- 146x40 px
- 168x46 px
- 209x57 px


#### Knappetype


BTCPay Server kjenner til tre tilstander for betalingsknappen.



- Fast beløp
  - Den tidligere innstilte prisen finnes i knappens generelle innstillinger.
- Tilpasset beløp
  - BTCPay Server's Pay-knapp har + og - for å angi en tilpasset pris.
  - Når du bruker det egendefinerte beløpet, vil BTCPay Server be om en Min, Max og hvor gradvis det skal øke.
  - Knappene kan settes til "Use Simple input style" (Bruk enkel inndatastil), noe som fjerner +/- bryterne.
  - Monter knappen inline der knappen og bryterne vises inline.
- Skyvekontroll
  - Den ligner på det tilpassede beløpet, men er visuelt annerledes ettersom den har en glidebryter i stedet for +/- bryterne.
  - Når du bruker glidebryteren, vil BTCPay Server be om en Min, Max og hvor gradvis den skal øke.


**Merk!


Betalingsknappen kan slettes øverst i advarselsbeskrivelsen.


#### Betalingsvarsler


Server IPN (Instant Payment Notification) er designet for webhooks og kan konfigureres med en URL til etterkjøpsdata.


#### E-postvarsler


Når en betaling er utført, kan BTCPay Server varsle butikkeieren.


#### Omdirigering av nettleser


Når kunden fullfører kjøpet, vil han eller hun bli omdirigert til denne lenken hvis butikkeieren har angitt det.


#### Avanserte alternativer for betalingsknapp


Angi flere spørringsstrengparametere som skal legges til på betalingssiden når Invoice er opprettet. For eksempel vil `lang=da-DK` laste inn betalingssiden på dansk som standard.


#### Bruk appen som endepunkt


Du kan koble betalingsknappen direkte til en vare i en av PoS- eller Crowdfund-appene som du har brukt tidligere.


Butikkeiere kan klikke på rullegardinmenyen og velge ønsket app. Når appen er valgt, kan butikkeieren legge til varen som skal kobles til.


#### Generert kode


Ettersom BTCPay Servers betalingsknapp er en HTML-kode som enkelt kan bygges inn, viser BTCPay Server den genererte koden som skal kopieres inn på et nettsted nederst etter at betalingsknappen er konfigurert.


Butikkeiere kan kopiere den genererte koden til nettstedet sitt, og betalingsknappen fra BTCPay Server er direkte aktiv på nettstedet deres.


#### Betalingsvarsler


Server IPN (Instant Payment Notification) er designet for webhooks og kan konfigureres med en URL for å legge ut kjøpsdata.


#### E-postvarsler


Når en betaling er utført, kan BTCPay Server varsle butikkeieren.


#### Omdirigering av nettleser


Når kunden fullfører kjøpet, vil han eller hun bli omdirigert til denne lenken hvis butikkeieren har angitt det.


#### Avanserte alternativer for betalingsknapp


Angi flere spørringsstrengparametere som skal legges til på betalingssiden når Invoice er opprettet. For eksempel vil `lang=da-DK` laste inn betalingssiden på dansk som standard.


#### Bruk appen som endepunkt


Du kan koble betalingsknappen direkte til en vare i en av PoS- eller Crowdfund-appene som du har brukt tidligere. Butikkeiere kan klikke på rullegardinmenyen og velge ønsket app. Når appen er valgt, kan butikkeieren legge til varen som skal kobles til.


#### Generert kode


Ettersom BTCPay Servers betalingsknapp er en HTML-kode som enkelt kan bygges inn, viser BTCPay Server den genererte koden som skal kopieres til et nettsted nederst etter at betalingsknappen er konfigurert. Butikkeiere kan kopiere den genererte koden til nettstedet sitt, og betalingsknappen fra BTCPay Server er direkte aktiv på nettstedet deres.


### Oppsummering av ferdigheter


I denne delen har du lært:



- Slik bruker du BTCPay Servers integrerte PoS-tillegg for å enkelt opprette en tilpasset butikk
- Slik bruker du BTCPay Servers integrerte Crowdfund-plugin for å lage en tilpasset crowdfund-app på en enkel måte
- Generere kode for en egendefinert betalingsknapp ved hjelp av Pay Button-tillegget


### Vurdering av kunnskap


#### KA-gjennomgang


Hva er de tre innebygde plugin-modulene som følger med BTCPay Server som standard? Beskriv med noen få ord hvordan hver av dem kan brukes.


# Konfigurere BTCPay Server


<partId>ff38596c-7de3-5e5c-ba50-9b9edbbbb5eb</partId>


## Grunnleggende forståelse av å installere BTCPay Server på et LunaNode-miljø


<chapterId>d0a28514-ffcf-529b-9156-29141f0b060a</chapterId>


### Installere BTCPay-server på en hostet enhet (LunaNode)


Disse trinnene vil gi deg all nødvendig informasjon for å komme i gang med å bruke BTCPay Server på LunaNode. Det finnes mange alternativer for å distribuere programvaren.

Du finner alle detaljer om BTCPay Server på https://docs.btcpayserver.org.


#### Hvor skal vi begynne?


I denne delen vil du bli kjent med LunaNode som hostingleverandør, lære om de første stegene i bruken av BTCPay-serveren og lære hvordan du bruker Lightning Network. Etter at vi har gått gjennom alle trinnene, kan du drive en nettbutikk eller crowdfund-plattform som aksepterer Bitcoin!


Dette er en av mange måter å distribuere BTCPay Server på. Les dokumentasjonen vår for mer informasjon.


https://docs.btcpayserver.org.


### BTCPay Server - LunaNode-distribusjon


#### LunaNode-distribusjon


Først går du til nettsiden til LunaNode.com, hvor vi oppretter en ny konto. Klikk på Registrer deg øverst til høyre, eller bruk veiviseren Kom i gang på hjemmesiden deres.


![image](assets/en/112.webp)


Etter at du har opprettet en ny konto, sender LunaNode deg en e-post med bekreftelse. Når du har bekreftet kontoen, sammenlignet med Voltage, får du umiddelbart muligheten til å fylle opp kontosaldoen din. Denne saldoen er nødvendig for å dekke serverplass og hostingkostnader.


![image](assets/en/113.webp)


#### Legg til kreditt på LunaNode-kontoen din


Når du har klikket på "Sett inn kreditt", får du angi hvor mye du vil fylle på kontoen din med og hvordan du vil betale for det. LunaNode og BTCPay Server vil koste mellom $ 10 og $ 20 per måned.

Sammenlignet med Voltage.cloud får du full tilgang til din virtuelle private server (VPS), slik at du har mer kontroll over serveren din. Etter at du har opprettet en ny konto, sender LunaNode deg en bekreftelses-e-post.

Når du har bekreftet kontoen, sammenlignet med Voltage, får du umiddelbart muligheten til å fylle opp kontosaldoen din. Denne saldoen er nødvendig for å dekke serverplassen og hostingkostnadene.


#### Hvordan distribuerer jeg en ny server?


I denne veiledningen går vi gjennom installasjonsprosessen ved å opprette et sett med API-nøkler og bruke BTCPay Server-startprogrammet som er utviklet av LunaNode.


I LunaNode-dashbordet klikker du på API øverst til høyre. Dette åpner en ny side. Vi trenger bare å angi et navn for API-nøkkelen. Resten tar LunaNode seg av, og vil ikke bli dekket i denne guiden. Klikk på knappen Create API Credential.

Når du har opprettet API-legitimasjonen, får du en lang streng med bokstaver og tegn. Dette er API-nøkkelen din.


![image](assets/en/114.webp)


#### Hvordan distribuerer jeg en ny server?


Det er to deler av denne påloggingsinformasjonen, API-nøkkel og API-ID; vi trenger begge deler. Før vi går videre til neste trinn, åpner vi en ny fane i nettleseren og går til https://launchbtcpay.lunanode.com/


Her vil du bli bedt om å oppgi API-nøkkel og API-ID. Dette er for å fortelle deg at det er du som har levert denne nye serveren. API-nøkkelen skal fortsatt være åpen i den forrige fanen; hvis du blar nedover i tabellen nedenfor, finner du API-ID-en.


Du kan gå tilbake til siden med Launcher, fylle ut feltene med API-nøkkelen og ID-en din, og klikke på Fortsett.


![image](assets/en/115.webp)


I neste trinn kan du oppgi et domenenavn. Hvis du allerede eier et domene og ønsker å bruke dette til BTCPay Server, må du sørge for at du også legger til DNS-oppføringen (kalt en "A"-oppføring) på domenet ditt. Hvis du ikke eier et domene, kan du i stedet bruke domenet som LunaNode tilbyr (du kan endre dette senere i BTCPay Server-innstillingene), og klikk på Fortsett.


Les mer om hvordan du angir eller endrer en DNS-post for BTCPay Server; https://docs.btcpayserver.org/FAQ/Deployment/#how-to-change-your-btcpay-server-domain-name


#### Start BTCPay Server på LunaNode


Etter å ha tatt trinnene før, kan vi angi alle alternativene for den nye serveren vår. Her velger vi Bitcoin (BTC) som vår støttede valuta. Vi kan også angi en e-post for å motta varsler om fornyelse av krypteringssertifikater, noe som er valgfritt.


Denne guiden tar sikte på å sette opp et Mainnet-miljø (Bitcoin i den virkelige verden), men LunaNode lar deg også sette det til Testnet eller Regtest for utviklingsformål. Vi lar det stå på Mainnet-alternativet i denne veiledningen.


Du kan velge din Lightning-implementasjon. LunaNode tilbyr to ulike implementasjoner, LND og Core Lightning. I denne guiden tar vi utgangspunkt i LND. Det er få, men reelle forskjeller i begge implementasjonene; for mer om dette anbefaler vi å lese den omfattende dokumentasjonen: https://docs.btcpayserver.org/LightningNetwork#getting-started-with-btcpay-server-and-core-lightning-cln


![image](assets/en/116.webp)


LunaNode tilbyr flere planer for virtuelle maskiner (VM). Disse varierer når det gjelder prisklasse og serverspesifikasjoner. I denne veiledningen er det tilstrekkelig med en m2-plan, men hvis du har valgt mer enn bare Bitcoin som valuta, bør du vurdere å bruke minst en m4.


Fremskynde den første Blockchain-synkroniseringen; dette er valgfritt og avhenger av dine behov. Det finnes avanserte alternativer, for eksempel å angi et Lightning-alias, peke på en spesifikk GitHub-versjon eller angi SSH-nøkler; ingen av disse vil bli dekket i denne veiledningen.


Etter at du har fylt ut skjemaet, må du klikke på Launch VM, og Lunanode vil begynne å opprette din nye VM, inkludert BTCPay Server installert på den. Denne prosessen tar et par minutter; når serveren din er klar, gir LunaNode deg lenken til din nye BTCPay Server.


Etter opprettelsesprosessen klikker du på lenken til BTCPay-serveren din; her vil du bli bedt om å opprette en administratorkonto.


![image](assets/en/117.webp)


### Oppsummering av ferdigheter


I denne delen har du lært:



- Opprette og finansiere en konto på LunaNode
- Bruk BTCPay Server Launcher til å opprette din egen server


### Vurdering av kunnskap


#### KA Konseptuell gjennomgang


Beskriv noen av forskjellene mellom å kjøre en forekomst av BTCPay Server på en VPS og å opprette en konto på en hostet forekomst.


## Installere BTCPay Server i et Voltage-miljø


<chapterId>11c7d284-b4d2-5542-872c-df9bd9c1491b</chapterId>


Du vil bli kjent med Voltage.cloud som hostingleverandør, lære om de første trinnene i bruken av BTCPay-serveren din og lære hvordan du bruker Lightning Network. Etter at vi har gått gjennom alle trinnene, kan du drive en nettbutikk eller crowdfund-plattform som aksepterer Bitcoin!


Dette er en av mange måter å distribuere BTCPay Server på. Les dokumentasjonen vår for mer informasjon.

https://docs.btcpayserver.org.


### BTCPay Server - Voltage.cloud-distribusjon


Først går du til nettstedet Voltage.cloud og registrerer deg for en ny konto. Når du oppretter en konto, kan du registrere deg for en 7-dagers gratis prøveperiode. Du kan enten klikke på Sign Up øverst til høyre eller bruke "Try a free 7-day trial" på hjemmesiden.


![image](assets/en/118.webp)


Etter at du har opprettet en konto, klikker du på knappen `NODES` på dashbordet. Når vi har valgt Nodes og opprettet en ny node, får vi presentert de mulige nodenes Voltage-tilbud. Siden denne guiden også vil dekke Lightning Network, på Voltage, må vi først velge vår Lightning-implementering før vi oppretter en BTCPay Server. Klikk på LightningNode.


![image](assets/en/119.webp)


Her må du velge hva slags Lightning-node du vil ha. Voltage har en rekke alternativer for belysningsoppsettet ditt. Dette er annerledes når du distribuerer med for eksempel LunaNode. I denne veiledningen er det tilstrekkelig med en Lite Node. Les mer om forskjellene i Voltage.cloud.


![image](assets/en/120.webp)


Gi noden et navn, angi et passord og sikre dette passordet. Hvis du mister passordet, mister du tilgangen til sikkerhetskopiene dine, og Voltage kan ikke gjenopprette det. Opprett noden, og Voltage viser deg fremdriften. Voltage har opprettet Lightning Node. Vi kan nå opprette BTCPay Server-forekomsten og få direkte tilgang til Lightning Network.


Klikk på Nodes øverst til venstre i dashbordet. Her kan du sette opp den neste delen av BTCPay Server-forekomsten din. Klikk på "Opprett ny" når du er i nodeoversikten. Du får et lignende skjermbilde som før. Nå velger vi BTCPay Server i stedet for Lightning Node.


Voltage viser deg geolokaliseringen til BTCPay-serveren din, som er hostet i US West-regionen. Her vil du også se kostnadene for hosting av serveren. Klikk på Opprett og gi BTCPay-serveren et navn. Aktiver Lightning, og Voltage viser deg Lightning-noden som ble opprettet i forrige trinn. Klikk på Create, og Voltage oppretter en BTCPay Server-forekomst.


![image](assets/en/121.webp)


Etter at du har trykket på opprett, presenterer Voltage deg med standard brukernavn og passord. Disse ligner på ditt tidligere angitte passord i Voltage. Klikk på knappen Logg inn på konto for å omdirigere deg til BTCPay-serveren din.


Velkommen til din nye BTCPay Server-forekomst. Siden vi allerede har satt opp Lightning i opprettelsesprosessen, viser den at Lightning allerede er aktivert!


### Oppsummering av ferdigheter


I dette kapittelet lærte du:



- Opprette en konto på Voltage.cloud
- Fremgangsmåte for å få BTCPay Server til å kjøre sammen med en Lightning-node på kontoen


### Vurdering av kunnskap


#### KA Konseptuell gjennomgang


Hva er de viktigste forskjellene mellom Voltage- og LunaNode-oppsettene?


## Installere BTCPay Server på en Umbrel-node


<chapterId>3298e292-6476-5fe0-836c-7fa021348799</chapterId>


Når du er ferdig med disse trinnene, kan du akseptere lynbetalinger til BTCPay-butikken din på ditt lokale nettverk. Denne prosessen gjelder også hvis du driver en umbrel-node i en restaurant eller bedrift. Hvis du vil koble denne butikken til et offentlig nettsted, følger du øvelsen Avansert for å eksponere umbrel-noden din for offentligheten.


https://umbrel.com/


![image](assets/en/122.webp)


### BTCPay Server - Umbrel-distribusjon


Etter at Umbrel-noden din er fullstendig synkronisert med Bitcoin Blockchain, går du til Umbrel App Store og søker etter BTCPay Server under Apper.


![image](assets/en/123.webp)


Klikk på BTCPay Server for å se detaljer om appen. Når detaljene for BTCPay Server er åpne, viser det nederste høyre hjørnet kravene for at appen skal kjøre som den skal. Den viser at den krever en Bitcoin og Lightning-node. Hvis du ikke har installert Lightning Node på Umbrel, klikker du på Installer. Denne prosessen kan ta et par minutter.


![image](assets/en/124.webp)


Etter at du har installert Lightning Node:


1. Klikk på Åpne i appdetaljene eller på appen i Umbrels-dashbordet.

2. Klikk på Sett opp en ny node. Du får opp 24 ord for gjenoppretting av lynnoden din.

3. Skriv ned disse.


![image](assets/en/125.webp)


Umbrel vil be om bekreftelse på ordene som nettopp ble skrevet ned. Etter at Lightning-noden er satt opp, går du tilbake til Umbrel App Store og finner BTCPay Server. Klikk på installasjonsknappen, og Umbrel vil vise om de nødvendige komponentene er installert og at BTCPay Server krever tilgang til disse komponentene. Etter installasjonen klikker du på Open øverst til høyre i App details eller åpner BTCPay Server via Umbrels dashbord.


Umbrel vil be om bekreftelse på ordene som nettopp er skrevet ned.


![image](assets/en/126.webp)


**Merk!


Sørg for at disse oppbevares på et sikkert sted, slik du tidligere har lært om oppbevaring av nøkler.


Etter at Lightning-noden er satt opp, går du tilbake til Umbrel App Store og finner BTCPay Server. Klikk på installasjonsknappen, og Umbrel vil vise om de nødvendige komponentene er installert og at BTCPay Server krever tilgang til disse komponentene.


![image](assets/en/127.webp)


Etter installasjonen klikker du på Åpne øverst til høyre i appdetaljene eller åpner BTCPay Server via Umbrels-dashbordet.


![image](assets/en/128.webp)


### Oppsummering av ferdigheter


I denne delen har du lært:



- Fremgangsmåte for å installere BTCPay Server med Lightning-funksjonalitet på en Umbrel-node


### Vurdering av kunnskap


#### KA Konseptuell gjennomgang


Hvordan skiller oppsettet på Umbrel seg fra de to foregående alternativene?


# Siste del


<partId>d72e6fa5-0870-5f00-9143-9466ed22e2bd</partId>




## Anmeldelser og rangeringer

<chapterId>d90bb93d-b894-551e-9fd6-6855c739a904</chapterId>

<isCourseReview>true</isCourseReview>

## Kursets konklusjon


<chapterId>c07ac2a5-f97e-5c57-8a80-4955b48128d4</chapterId>

<isCourseConclusion>true</isCourseConclusion>