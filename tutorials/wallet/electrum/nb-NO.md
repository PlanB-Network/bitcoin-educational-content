---
name: Electrum

description: Fullstendig Electrum-guide, fra 0 til helt
---

![cover](assets/cover.webp)

Beskrivelse for Electrum

https://twitter.com/ElectrumWallet
https://electrum.org/
https://electrum.readthedocs.io/

> "Jeg må si, da jeg kom over denne guiden ble jeg sjokkert. Gratulerer til Arman the Parman for dette. Det ville ha vært en skam å ikke ha den her og oversette den til så mange språk som mulig. Ærlig talt, gi det fyren et tips." Rogzy

Originalinnlegg:

![Electrum Desktop Wallet (Mac / Linux) - last ned, verifiser, koble til din node.](https://youtu.be/wHmQNcRWdHM)

![Å gjøre en Bitcoin-transaksjon med Electrum](https://youtu.be/-d_Zd7VcAfQ)

## Hvorfor Electrum?

Dette er en detaljert guide om hvordan du bruker Electrum Bitcoin Wallet, med løsninger på alle dens fallgruver og særegenheter - noe jeg har utviklet etter flere års bruk, og undervisning av studenter om Bitcoin-sikkerhet/privatliv. Electrum er ikke den beste Bitcoin-lommeboken for personen som ønsker å holde alt så enkelt som mulig, og foretrekker å forbli på nybegynnernivå. I stedet er det for personen som er, eller aspirerer til å være, en "power" bruker.

For den nye Bitcoiner, er den utmerket kun under tilsyn av en erfaren bruker for å vise dem veien. Hvis man lærer å bruke den alene, ville det være trygt forutsatt at de tar seg tid og bruker den i et testmiljø med bare et lite antall sats først. Denne guiden støtter den innsatsen, men den er også en god referanse for alle andre.

> Advarsel: Denne guiden er stor. Ikke prøv å gjøre alt dette på en dag. Det er best å lagre guiden og jobbe med den over tid.

## Nedlasting av Electrum

Ideelt sett, bruk en dedikert Bitcoin-datamaskin for dine Bitcoin-transaksjoner (Min guide for dette https://armantheparman.com/mint/) _(OGSÅ tilgjengelig i personvernseksjonen)_. Det er greit å øve med små beløp på en "skitten" datamaskin når du først lærer (hvem vet hvor mye skjult skadelig programvare din vanlige datamaskin har samlet opp gjennom årene – du vil ikke utsette dine Bitcoin-lommebøker for dem).

Få Electrum fra https://electrum.org/.

Klikk på Last ned-fanen øverst.

Klikk på nedlastingslenken som tilsvarer din datamaskin. Enhver Linux- eller Mac-datamaskin kan bruke Python-lenken (rød sirkel). En Linux-datamaskin med en Intel- eller AMD-brikke kan bruke Appimage (grønn sirkel; dette er som en Windows-kjørbar fil). En Raspberry Pi-enhet har en ARM-mikroprosessor og kan kun bruke Python-versjonen (rød sirkel), ikke Appimage, selv om Pi kjører Linux. Den blå sirkelen er for Windows og den svarte sirkelen er for Mac.

![image](assets/1.webp)

## Verifisering av Electrum

Formålet med å "verifisere" nedlastingen er å forsikre seg om at ikke en eneste bit av data har blitt tuklet med. Det forhindrer deg i å bruke en "hacket" ondsinnet versjon av programvaren. Det er greit å hoppe over dette forutsatt at du kun bruker den nedlastede kopien til øving, dvs. ikke bruk lommebøker som holder seriøse penger. Deretter, når du er klar til å bruke Electrum for dine ekte midler, bør du slette din kopi og starte på nytt, denne gangen ved å verifisere nedlastingen din.
For å gjøre dette bruker vi verktøy for offentlig/privat nøkkelkryptografi – gpg, som vi har skrevet en guide om her (https://armantheparman.com/gpg/). Gpg-verktøyet følger med alle Linux-operativsystemer. For Mac og Windows, se gpg-lenken for nedlastingsinstruksjoner.
I tillegg til å laste ned Electrum-programvaren, trenger du også, for sikkerhetens skyld, den digitale SIGNATUREN til programvaren. Dette er en tekststreng (det er faktisk et tall kodet ved hjelp av tekst) som utvikleren har produsert med sin PRIVATE gpg-nøkkel. Ved å bruke gpg-programmet, kan vi deretter "teste" SIGNATUREN mot hans OFFENTLIGE nøkkel (laget fra utviklerens private nøkkel) som alle har tilgang til, i motsetning til nedlastingsFILEN.

Med andre ord, med de tre inndataene (signatur, offentlig nøkkel og datafil), får vi en sann eller falsk utgang for å bekrefte at filen ikke har blitt tuklet med.

For å få signaturen, klikk på lenken som tilsvarer filen du lastet ned (se fargede piler):

![bilde](assets/2.webp)

Å klikke på lenken kan automatisk laste ned filen til nedlastingsmappen din, eller den kan åpnes i nettleseren. Hvis den åpnes i nettleseren, må du lagre filen. Du kan høyreklikke og velge "lagre som". Avhengig av operativsystemet eller nettleseren, må du kanskje høyreklikke på det hvite området, ikke teksten.

Nedenfor er hvordan den nedlastede teksten ser ut. Du kan se at det er flere signaturer – disse er signaturer fra forskjellige personer. Du kan verifisere hver eller noen. Jeg vil vise deg hvordan du bare verifiserer utviklerens.

![bilde](assets/3.webp)

Deretter må du skaffe ThomasVs offentlige nøkkel – han er hovedutvikleren. Du kan få den direkte fra ham, hans Keybase-konto, Github, eller noen andre, fra en nøkkeltjener, eller fra Electrum-nettstedet.

Å få den fra Electrum-nettstedet er faktisk den minst sikre måten, fordi hvis dette nettstedet er ondsinnet (det er nettopp det vi sjekker for) hvorfor får vi en offentlig nøkkel fra det (den offentlige nøkkelen kunne være falsk)?

For å holde det enkelt for nå, vil jeg vise deg hvordan du får den fra nettstedet uansett, men ha dette i bakhodet. Her er kopien (https://github.com/spesmilo/electrum/blob/master/pubkeys/ThomasV.asc) på GitHub som du kan sammenligne den med.

Rull litt ned på siden for å finne lenken til ThomasVs offentlige nøkkel (rød sirkel nedenfor). Klikk på den og last den ned, eller hvis den åpner litt tekst i en nettleser, høyreklikk for å lagre.

![bilde](assets/4.webp)

Du har nå 3 nye filer, sannsynligvis alle i nedlastingsmappen. Det spiller ingen rolle hvor de er, men det gjør prosessen enklere hvis du legger dem alle i samme mappe.

De tre filene:

1. Electrum-nedlastingen
2. Signaturfilen (vanligvis er det samme filnavn som Electrum-nedlastingen med et ".asc" tillegg
3. ThomasVs offentlige nøkkel.

Åpne en terminal på Mac eller Linux, eller kommandoprompt (CMD) på Windows.

Naviger til Nedlastingsmappen (eller hvor enn du la de tre filene). Hvis du ikke har noen anelse om hva dette betyr, lær fra denne korte videoen for Linux/Mac (https://www.youtube.com/watch?v=AO0jzD1hpXc) og denne for Windows (https://www.youtube.com/watch?v=9zMWXD-xoxc). Husk at på Linux-datamaskiner er mappenavn følsomme for store og små bokstaver.
I terminalen, skriv dette for å importere ThomasVs offentlige nøkkel inn i datamaskinens "nøkkelring" (nøkkelringen er et abstrakt konsept – det er faktisk bare en fil på datamaskinen din):
```bash
gpg --import ThomasV.asc
```

Sørg for at filnavnet stemmer overens med det du har lastet ned. Legg også merke til at det er et dobbelt bindestrek og ikke et enkelt bindestrek. Merk også at det er et mellomrom før og etter "--import". Deretter trykker du <enter>.

Filen skal importeres. Hvis du får en feil, sjekk at du er i katalogen hvor filen faktisk eksisterer. For å sjekke hvilken katalog du er i (på Mac eller Linux), skriv pwd. For å se hvilke filer som er i katalogen du er i (på Mac eller Linux), skriv ls. Du bør se tekstfilen "ThomasV.asc" oppført, muligens blant andre filer.

Deretter kjører vi kommandoen for å verifisere signaturen.

```bash
gpg --verify Electrum-4.1.5.tar.gz.asc Electrum-4.1.5.tar.gz
```

Legg merke til at det er 4 "elementer" her, hver adskilt av et mellomrom. Jeg har uthevet teksten vekselvis for å hjelpe deg med å se. De fire elementene er:

1. gpg-programmet
2. --verify-alternativet
3. filnavnet på signaturen
4. filnavnet på programmet

Interessant nok, noen ganger kan du utelate det 4. elementet og datamaskinen gjetter hva du mener. Jeg er ikke sikker, men jeg tror det bare fungerer hvis filnavnene kun skiller seg ved "asc" på slutten.

Ikke bare kopier filnavnene som jeg har vist her – sørg for at de stemmer overens med filnavnet på det du har på systemet ditt.

Trykk <enter> for å kjøre kommandoen. Du bør se en "god signatur fra ThomasV" for å indikere suksess. Det vil være noen feil fordi vi ikke har de offentlige nøklene for de andre personenes signaturer som er inneholdt i signaturfilen (dette systemet med å kombinere signaturer i én fil kan endre seg i senere versjoner). Også, det er en advarsel nederst som vi kan ignorere (dette varsler oss om at vi ikke har eksplisitt fortalt datamaskinen at vi stoler på ThomasVs offentlige nøkkel).

Nå har vi en verifisert kopi av Electrum som er trygg å bruke.

## Kjøre Electrum

### Kjøre Electrum hvis du bruker Python

Hvis du lastet ned Python-versjonen, er dette hvordan du får det til å fungere. Du vil se på nedlastingssiden dette:

![bilde](assets/5.webp)

For Linux, er det en god idé å først oppdatere systemet ditt:

```bash
sudo apt-get update
sudo apt-get upgrade
```

Kopier den uthevede gule teksten, lim den inn i terminalen, og trykk <enter>. Du vil bli bedt om passordet ditt, muligens en bekreftelse for å fortsette, og deretter vil den installere disse filene ("avhengigheter").

Du må også pakke ut den zippede filen til en katalog etter ditt valg. Dette kan du gjøre med det grafiske brukergrensesnittet, eller fra kommandolinjen (kommandoen markert med rosa) – husk at filnavnene dine kan variere. (Merk at da vi verifiserte nedlastingen i forrige avsnitt, var det zip-filen vi verifiserte, ikke den utpakkede katalogen.)

Det er et alternativ for å "installere" ved hjelp av PIP-programmet, men dette er unødvendig, og legger til ekstra trinn og installasjon av filer. Bare kjør programmet ved hjelp av terminalen for å omgå alt dette.

Stegene (Linux) er:

1. naviger til katalogen hvor filene er pakket ut
2. skriv: ./run_electrum

På en Mac er stegene de samme, men du må kanskje først installere Python3, og bruke denne kommandoen for å kjøre:

```bash
```python3 ./run_electrum```

Når Electrum kjører, vil terminalvinduet forbli åpent. Hvis du lukker det, vil det avslutte Electrum-programmet. Bare minimer det mens du bruker Electrum.

### Kjøre Electrum med Appimage

Dette er litt enklere, men ikke like enkelt som en Windows kjørbar fil. Avhengig av versjonen av Linux du bruker, kan Appimage-filer som standard ha attributter satt slik at utførelse er forbudt av systemet. Vi må endre dette. Hvis dine Appimages fungerer, kan du hoppe over dette steget. Naviger til hvor filen er, ved å bruke terminal, og kjør deretter denne kommandoen:

```bash
sudo chmod ug+x Electrum-4.1.5-x86_64.AppImage
```

“sudo” gir superbrukerprivilegier; “chmod” er en kommando for å endre modus, som endrer hvem som kan lese, skrive eller utføre; “ug+x” betyr at vi endrer bruker og gruppe for å tillate utførelse.

Juster filnavnet for å matche din versjon.

Deretter vil Electrum kjøre ved å dobbeltklikke på Appimage-ikonet.

### Kjøre Electrum med Mac

Dobbeltklikk bare på den nedlastede filen (den er et “drev”). Et vindu vil åpne seg. Dra Electrum-ikonet i vinduet til skrivebordet ditt, eller hvor du vil beholde programmet. Du kan deretter “kaste ut” drevet, og slette drevet (den nedlastede filen).

For å kjøre programmet, dobbeltklikk det bare. Du kan få noen Mac-spesifikke “nanny” feil som må omgås.

### Kjøre Electrum med Windows

Til tross for at jeg hater Windows mest av alt, er dette den enkleste metoden. Dobbeltklikk bare på den kjørbare filen for å kjøre.

## Start med en dummy lommebok

Når du først laster Electrum, vil et vindu åpne seg slik:

![bilde](assets/6.webp)

Vi vil senere velge din server manuelt, men for nå, la standardinnstillingen være og auto-koble.

Deretter, opprett en dummy lommebok – ikke sett noen midler i denne lommeboken. Formålet med denne dummy lommeboken er å gå gjennom programvaren og sørge for at alt fungerer bra før du laster opp din ekte lommebok. Vi prøver å unngå å ved et uhell gi fra oss privatliv med en ekte lommebok. Hvis du bare øver, kan lommeboken du oppretter anses som en dummy lommebok uansett.

Du kan la navnet stå som “default_wallet” eller endre det til hva du vil, og klikk neste. Senere, hvis du har flere lommebøker, kan du finne dem og åpne dem på dette stadiet ved først å klikke “Velg…”

![bilde](assets/7.webp)

Velg “Standard lommebok” og <Neste>:

![bilde](assets/8.webp)

Deretter, velg “Jeg har allerede et frø”. Jeg vil ikke at du skal venne deg til å opprette et Electrum-frø, da det bruker sitt eget protokoll som ikke er kompatibelt med andre lommebøker – dette er grunnen til at vi ikke klikker på “nytt frø”.

![bilde](assets/9.webp)

Gå til https://iancoleman.io/bip39/ og opprett et dummy frø. Først, endre antall ord til 12 (som er vanlig praksis), deretter klikk “generer” og kopier ordene i boksen til utklippstavlen din.

![bilde](assets/10.webp)

Deretter limer du inn ordene i Electrum. Her er et eksempel:

![bilde](assets/11.webp)

Electrum vil se etter ord som matcher dets egen protokoll. Vi må omgå det. Klikk på alternativer, og velg BIP39 Seed:

![bilde](assets/12.webp)
Frøet blir deretter gyldig. (Før dette, forventet Electrum et Electrum-frø, så dette frøet ble sett på som ugyldig). Før du klikker neste, legg merke til teksten som sier "Checksum OK". Det er viktig (for den ekte lommeboken du kanskje bruker senere) at du ser dette før du fortsetter, da det bekrefter gyldigheten av frøet du la inn. Advarselen nær bunnen kan ignoreres, det er Electrum-utviklerens klaging om BIP39 og deres "FUD'ey" påstander om at deres versjon (som ikke er kompatibel med andre lommebøker) er overlegen.

> En rask avstikker for en viktig advarsel. Formålet med kontrollsummen er å forsikre deg om at du har angitt frøet ditt uten skrivefeil. Kontrollsummen er den siste delen av frøet (det 12. ordet ender opp som kontrollsumordet) som matematisk er bestemt av den første delen av frøet (11 ord). Hvis du skulle skrive noe feil i starten, vil ikke kontrollsumordet matematisk stemme overens, og lommebokprogramvaren vil varsle deg med en advarsel. Dette betyr ikke at frøet ikke kan brukes til å opprette en funksjonell Bitcoin-lommebok. Forestill deg å opprette en lommebok med en skrivefeil, laste lommeboken med bitcoin, og så en dag kan du trenge å gjenopprette lommeboken, men når du gjør det, gjenskaper du ikke skrivefeilen – du vil gjenopprette feil lommebok! Det er ganske farlig at Electrum lar deg fortsette å lage en lommebok hvis kontrollsummen din er ugyldig, så vær advart, det er ditt ansvar å sørge for. Andre lommebøker vil ikke la deg fortsette, noe som er mye tryggere. Dette er en av tingene jeg mener når jeg sier at Electrum er greit å bruke, når du lærer å bruke det ordentlig (Electrum-utviklere bør fikse dette).

Legg merke til at hvis du ønsket å legge til en passfrase, er sjansen til å velge det i dette alternativvinduet, helt på toppen.

Etter å ha klikket OK, vil du bli tatt tilbake til der du skrev inn frøsetningen. Hvis du valgte et passfrasealternativ, skriver du IKKE inn det med frøordene (forespørselen om det kommer neste).

Hvis du ikke ba om en passfrase, vil du se denne skjermen neste – flere alternativer for din lommebok skripttype og avledningssti som du kan lære om her (https://armantheparman.com/public-and-private-keys/), men bare la standardinnstillingene stå og fortsett.

![bilde](assets/13.webp)

> For ekstra info: Det første alternativet lar deg velge mellom legacy (adresser som starter med "1"), pay-to-script-hash (adresser som starter med "3"), eller bech32/native segwit (adresser som starter med "bc1q"). På skrivetidspunktet støtter Electrum ennå ikke taproot (adresser som starter med "bc1p"). Det andre alternativet i dette vinduet lar deg endre avledningsstien. Jeg foreslår at du aldri endrer dette, spesielt før du forstår hva det betyr. Folk vil understreke viktigheten av å skrive ned avledningsstien slik at du kan gjenopprette lommeboken din om nødvendig, men hvis du lar den stå som standard, kommer du sannsynligvis til å være i orden, så ikke få panikk – men det er fortsatt god praksis å skrive ned avledningsstien.

Neste, vil du få muligheten til å legge til et PASSORD. Dette må ikke forveksles med "PASSFRASE". Et passord låser filen på datamaskinen din. En passfrase er en del av oppbyggingen av den private nøkkelen. Siden dette er en dummy lommebok, kan du la passordfeltet stå tomt og fortsette.

![bilde](assets/14.webp)
Du vil få et pop-up vindu om varsler for ny versjon (jeg foreslår at du velger nei). Lommeboken vil deretter generere seg selv og være klar til bruk (men husk, denne lommeboken er ment for sletting, det er bare en dummy lommebok).
![bilde](assets/15.webp)

Det er noen ting jeg foreslår at du gjør for å sette opp programvaremiljøet (kreves kun én gang):

### Endre enhetene til BTC

Gå til toppmenyen, verktøy –> electrum preferanser, og der under generell-fanen, vil du finne alternativet for å endre "baseenhet" til BTC.
Aktiver fanene for Adresser og Mynter

Gå til toppmenyen, vis, og velg "vis adresser". Gå deretter tilbake til vis og velg "vis mynter".

### Aktiver Oneserver

Som standard kobler Electrum seg til en tilfeldig node. Den kobler seg også til mange andre sekundære noder. Jeg er ikke sikker på hvilke data som utveksles med disse sekundære nodene, men vi ønsker ikke at det skal skje, av personvernhensyn. Selv om du spesifiserer en node, f.eks. din egen node, vil disse flere andre nodene også være koblet til, og jeg er ikke sikker på hvilken informasjon som deles. Uansett, det er enkelt å forhindre. Før jeg viser deg hvordan du spesifiserer din egen node, vil vi tvinge Electrum til kun å koble seg til én server om gangen.

> Det er en måte å gjøre dette på ved å spesifisere "oneserver" fra kommandolinjen, men jeg anbefaler ikke denne måten. Jeg vil vise et alternativ som jeg tror er enklere i det lange løp, og mer sannsynlig å ikke la deg ved et uhell koble til andre noder.

Grunnen til at vi bruker en dummy lommebok er at hvis vi hadde lastet inn vår ekte lommebok, med våre ekte bitcoin, ville vi utilsiktet ha koblet til en tilfeldig node nå (selv om vi valgte "sett server manuelt" i starten, kobler den fortsatt til disse andre sekundære nodene av en eller annen grunn (hei Electrum-utviklere, dere burde fikse dette). Hvis lommeboken vår var privat, ville dette vært en katastrofe.

Vi kan heller ikke gjøre trinnene jeg vil vise deg nedenfor uten først å laste opp en type lommebok. (Vi skal redigere en konfigurasjonsfil som bare blir befolket og klar for redigering når en lommebok er lastet).

**Lukk Electrum (VIKTIG, hvis du ikke gjør dette, vil de følgende endringene du gjør bli slettet).**

### LINUX/MAC Konfigurasjonsfil

Åpne terminalen i Linux eller Mac (Windows-instruksjoner senere):

Du bør automatisk være i hjemmemappen. Derfra, naviger til den skjulte electrum-innstillingene mappen (dette er forskjellig fra hvor applikasjonen er).

```bash
cd .electrum
```

Merk punktet før "electrum" som indikerer at det er en skjult mappe.

En annen måte å komme dit på er å skrive:

```bash
cd ~/.electrum
```

hvor "~" representerer stien til hjemmekatalogen din. Du kan se den fulle stien til din nåværende katalog med kommandoen "pwd".

Når du er i ".electrum"-katalogen, skriv "nano config" og trykk <enter>.

En tekstredigerer vil åpne seg (kalt nano) med konfigurasjonsfilen åpen. Musen fungerer ikke mye her. Bruk piltastene for å komme til linjen som sier:

```json
"oneserver": false,
```

Endre "false" til "true"; og ikke forstyr syntaksen (ikke slett kommaet eller semikolonet).

Trykk <ctrl> x, for å avslutte, deretter "y" for å lagre, deretter <enter> som bekrefter endringen uten å redigere filnavnet.
Nå kjør Electrum igjen. Deretter klikker du på sirkelen nederst til høyre, som åpner nettverksinnstillingene. Deretter, nær toppen i oversikt-fanen, vil du se "tilkoblet til 1 node" - dette indikerer suksess.

Like under det, vil du se et tekstfelt og serverens adresse er der. Du er for øyeblikket tilkoblet den tilfeldige noden. Mer om tilkobling til en node i neste seksjon.

### Windows konfigurasjonsfil

Windows konfigurasjonsfilen er litt vanskeligere å finne. Katalogen er: `C:/Users/Parman/AppData/Roaming/Electrum`

Selvfølgelig må du endre "Parman" til ditt eget brukernavn for datamaskinen.

I den mappen vil du finne konfigurasjonsfilen. Åpne den med en teksteditor og rediger linjen:

```json
"oneserver": false,
```

Endre "false" til "true"; ikke forstyr syntaksen (ikke slett kommaet eller semikolon).

Deretter lagrer du filen og avslutter.

## Koble Electrum til en node

Neste, vi ønsker å koble vår dummy lommebok til en node av vårt valg. Hvis du ikke er klar til å kjøre en node, kan du gjøre en av følgende:

1. Koble til en venns personlige node (krever Tor)
2. Koble til en pålitelig bedrifts node
3. Koble til en tilfeldig node (ikke anbefalt).

Forresten, her er instruksjoner for å kjøre din egen node, og dette er grunnene til at du bør. (alle veiledninger i Node-seksjonen eller i våre gratis kurs)

### Koble til en venns node via Tor (Guide kommer snart.)

### Koble til en pålitelig bedrifts node

Den eneste grunnen til å gjøre dette ville være hvis du må få tilgang til blockchain og du ikke har din egen node tilgjengelig (eller en venns).

La oss koble til Bitaroo sin node - Vi får vite at de ikke samler data. De er en Bitcoin Only exchange, drevet av en lidenskapelig Bitcoiner. Å koble til dem innebærer litt tillit, men det er bedre enn å koble til en tilfeldig node, som kunne være et overvåkingsselskap.

Kom til Nettverksinnstillingene ved å klikke på sirkelen i nedre høyre del av Lommebokens vindu (rødt indikerer ikke tilkoblet, grønt indikerer tilkoblet, og blått indikerer tilkoblet via Tor).

![bilde](assets/16.webp)

Når du klikker på sirkelikonet, vil et pop-up vindu dukke opp: Lommeboken din vil vise "tilkoblet til 1 node" siden vi tvang det tidligere.

Fjern merket for "velg server automatisk"-boksen, og skriv deretter inn Bitaroo sine detaljer som vist:

![bilde](assets/17.webp)

Lukk vinduet, og nå burde vi være tilkoblet til Bitaroo sin node. For å bekrefte, bør sirkelen være grønn. Klikk på den igjen og sjekk at serverdetaljene ikke har endret seg tilbake til en tilfeldig node.

### Koble til din egen node

Hvis du har din egen node, er det flott. Hvis du kun har Bitcoin Core, og ikke en Electrum SERVER også, vil du ennå ikke kunne koble en Electrum LOMMEBOK til noden din.

> Merk: Electrum Server og Electrum Lommebok er forskjellige ting. Serveren er programvare som kreves for at Electrum Lommebok skal kunne kommunisere Bitcoin blockchain - Jeg vet ikke hvorfor det ble designet på denne måten - muligens for hastighet, men jeg kan ta feil.
Hvis du kjører en node-programvarepakke som MyNode (den jeg anbefaler folk å starte med), Raspiblitz (anbefales etter hvert som du blir mer avansert), eller Umbrel (jeg personlig anbefaler den ikke ennå, da jeg har opplevd for mange problemer), vil du kunne koble til lommeboken din enkelt ved å skrive inn IP-adressen til datamaskinen (Raspberry Pi) som kjører noden, pluss et kolon, og 50002, som vist på bildet i forrige avsnitt. (Lenger ned vil jeg vise deg hvordan du finner IP-adressen til noden din).

Åpne Nettverksinnstillingene (klikk på den grønne eller røde sirkelen nederst til høyre). Fjern merket for "velg server automatisk", deretter skriv inn din IP-adresse som jeg har gjort din vil være annerledes, men kolonet og "50002" skal være det samme.

![bilde](assets/18.webp)

Lukk vinduet, og nå skal vi være koblet til noden din. For å bekrefte, klikk på sirkelen igjen og sjekk at serverdetaljene ikke har endret seg tilbake til en tilfeldig node.

Noen ganger, til tross for at alt ser ut til å være gjort riktig, nekter den å koble til. Her er ting å prøve...

- Oppgrader til en nyere versjon av Electrum, og din node-programvare
- Prøv å slette cache-mappen i ".electrum"-katalogen
- Prøv å endre porten fra 50002 til 50001 i nettverksinnstillingene
- Bruk denne guiden for å koble til ved hjelp av Tor som et alternativ (https://armantheparman.com/tor/)
- Installer Electrum Server på nytt på noden

## FINNE IP-ADRESSEN TIL NODEN DIN

En IP-adresse er ikke noe en vanlig bruker vanligvis vet hvordan man skal se opp og bruke. Jeg har hjulpet mange mennesker med å kjøre en node, og deretter koble lommebøkene deres til noden – et vanlig problem ser ut til å være å finne IP-adressen.

For MyNode, kan du skrive inn i et nettleservindu: `mynode.local`

Noen ganger fungerer ikke "mynode.local" (sørg for at du ikke skriver det i en Google-søkefelt. For å tvinge navigasjonsfeltet til å gjenkjenne teksten din som en adresse og ikke et søk, foran teksten med `http://` slik: `http://mynode.local`. Hvis det ikke fungerer, prøv det med en "s", slik: `https://mynode.local`.

Dette vil gi tilgang til enheten, og du kan klikke på innstillingslenken (se min blå "sirkel" nedenfor) for å vise denne skjermen hvor IP-adressen er plassert:

![bilde](assets/19.webp)

Denne siden vil laste og du vil se nodens IP (blå "sirkel")

![bilde](assets/20.webp)

Deretter, i fremtiden, kan du skrive 192.168.0.150, eller http://192.168.0.150 inn i nettleseren din.

For Raspiblitz (når du ikke kobler til en skjerm), trenger du en annen metode (som også fungerer for MyNode):

Logg inn på nettsiden til ruteren din – her vil vi finne IP-adressen til alle dine tilkoblede enheter. Ruteren sin nettside vil være en IP-adresse som du skriver inn i en nettleser. Min ser slik ut:

    http://192.168.0.1

For å få påloggingsinformasjonen til ruteren, kan du se den i brukermanualen eller noen ganger til og med på en klistrelapp på selve ruteren. Se etter brukernavn og passord. Hvis du ikke finner det, prøv Bruker: "admin" Passord: "password"

Hvis du klarer å logge inn, vil du se dine tilkoblede enheter og fra deres navn, kan det være klart hvilken som er noden din. IP-adressen vil være der.
### Hvis de to første metodene mislykkes, vil den siste fungere, men den er kjedelig:
Først, finn IP-adressen til en hvilken som helst enhet på nettverket ditt (den nåværende datamaskinen vil duge).

På en Mac finner du den i Nettverkspreferanser:

![bilde](assets/21.webp)

Vi er interessert i de første 4 elementene (192.168.0), ikke det 4. elementet, "166" som du ser på bildet (ditt vil være annerledes).

For Linux, bruk kommandolinjen:

```bash
ifconfig | grep inet
```

Den vertikale linjen er "pipe"-symbolet, og du finner det under <delete>-tasten. Du vil se noe output og en IP-adresse. (Ignorer 127.0.0.1 det er ikke den, og ignorer netmasken)

For Windows, åpne kommandoprompten (cmd) og skriv:

```bash
ipconfig/all
```

og trykk Enter. IP-adressen kan finnes i outputen.

Det var den enkle delen. Den vanskelige delen er nå å finne nodens IP-adresse – vi må brute-force gjette. La oss si for eksempel at datamaskinens IP-adresse starter med 192.168.0.xxx, da for noden din, i en nettleser, prøv: `https://192.168.0.2`

Det minste mulige nummeret er 2 (0 betyr hvilken som helst enhet, og 1 tilhører ruteren) og det høyeste, tror jeg er 255 (dette skjer for å være 11111111 i binært, det største nummeret holdt av 1 byte).

En etter en, jobb deg oppover mot 255. Til slutt vil du stoppe ved det korrekte nummeret som laster MyNode-siden din (eller RaspiBlitz-siden). Da vil du vite hvilket nummer du skal angi i Electrum-nettverksinnstillingene dine for å koble til noden din.

Det vil se omtrent slik ut (sørg for at du inkluderer kolon og nummer etterpå):

![bilde](assets/22.webp)

> Det er nyttig å vite at disse IP-adressene er INTERNE til hjemmenettverket ditt. Ingen utenfor kan se dem, og de er ikke sensitive. De er litt som telefonutvidelser i en stor organisasjon som dirigerer deg til forskjellige telefoner.

## Slett dummy-lommeboken

Nå har vi lykkes med å koble til én og bare én node. Slik vil Electrum laste som standard fra nå av. Du bør nå slette dummy-lommeboken (Meny: fil –> slett), i tilfelle du ved et uhell sender midler til denne usikre lommeboken (Den er usikker fordi vi ikke opprettet den på en sikker måte).

## Lag en øvelseslommebok

Etter å ha slettet dummy-lommeboken, start på nytt og lag en ny, på samme måte, bare denne gangen, skriv ned seed-ordene og oppbevar dem ganske trygt.

Det er en god idé å lære hvordan Electrum fungerer med denne øvelseslommeboken, uten den tungvinte maskinvarelommeboken (nødvendig for høy sikkerhet). Bare legg en liten mengde bitcoin i denne lommeboken – Anta at du vil miste disse pengene. Når du er dyktig, lær deretter å bruke Electrum med en maskinvarelommebok.

I den nye lommeboken du har opprettet, vil du se en liste over adresser. De grønne kalles "mottaksadresser". De er et produkt av 3 ting:

- Seed-frasen
- Passfrasen
- Derivasjonsveien

Din nye lommebok har et sett med mottaksadresser som kan matematisk og reproduserbart opprettes av hvilken som helst programvarelommebok som har seed, passfrase og derivasjonsvei. Det er 4,3 milliarder av dem! Mer enn du vil trenge. Electrum viser deg bare de første 20, og deretter flere etter hvert som du bruker opp de første.
Mer informasjon om bitcoin private nøkler kan du finne i denne guiden.
![bilde](assets/23.webp)

Dette er veldig forskjellig fra noen andre lommebøker som bare viser 1 adresse om gangen.

Fordi du skrev inn seed-frasen da du opprettet denne lommeboken, har Electrum den private nøkkelen for hver av adressene, og det er mulig å bruke midler fra disse adressene.

Merk også at det finnes gule adresser, kalt "endringsadresser" – Dette er bare et annet sett med adresser fra en annen matematisk gren (det finnes ytterligere 4,3 milliarder av disse). De brukes av lommeboken til automatisk å sende overskytende midler tilbake til lommeboken som veksel. For eksempel, hvis du tar 1,5 bitcoin og bruker 0,5 på en handel, må resten på 1,0 gå et sted. Lommeboken din vil bruke den til den neste tomme gule endringsadressen – ellers går den til gruvearbeideren! For mer informasjon om dette (UTXOs) se denne guiden. (https://armantheparman.com/utxo/)

Deretter, gå tilbake til Ian Colman private nøkkel-nettsiden og skriv inn seeden (i stedet for å generere en). Du vil se under at informasjonen om den private og offentlige nøkkelen endres; alt under er avhengig av tingene ovenfor på siden.

> Husk, du bør "aldri" skrive inn seeden på en datamaskin for din ekte Bitcoin-lommebok – skadelig programvare kan stjele den. Vi bruker bare en øvelseslommebok, for læringsformål, så det er greit for nå.

Rull ned og endre avledningsveien til BIP84 (segwit) for å matche din Electrum-lommebok ved å klikke på BIP84-fanen.

![bilde](assets/24.webp)

Under det vil du se den utvidede private nøkkelen for kontoen og den utvidede offentlige nøkkelen for kontoen:

![bilde](assets/25.webp)

Gå til Electrum, og sammenlign at de stemmer overens. Det er en meny øverst, lommebok –>informasjon:

![bilde](assets/26.webp)

Dette dukker opp:

![bilde](assets/27.webp)

Legg merke til at de to offentlige nøklene stemmer overens.

Neste, sammenlign adressene. Gå tilbake til Ian Colemans nettsted og rull til bunnen:

![bilde](assets/28.webp)

Legg merke til at de stemmer overens med adressene i Electrum.

Nå skal vi sjekke endringsadressene. Rull litt opp til avledningsveien og endre det siste 0 til en 1:

![bilde](assets/29.webp)

Rull ned og sammenlign adressene med de gule adressene i Electrum

Hvorfor gjorde vi alt dette?

Vi tok seed-ordene og satte dem gjennom to forskjellige uavhengige programvareprogrammer for å sikre at de ga oss samme informasjon. Dette reduserer betydelig risikoen for at ondsinnet kode lurer inne og gir oss falske private eller offentlige nøkler, eller adresser.

Det neste å gjøre er å motta en liten test og bruke den innenfor lommeboken fra en adresse til en annen.

## Testing av Lommeboken (Lær å bruke den)

Her vil jeg vise deg hvordan du mottar en UTXO til lommeboken din og deretter flytter den (bruker den) til en annen adresse innenfor lommeboken. Dette er en veldig liten mengde som vi ikke vil ha noe imot å risikere å miste.

Dette har flere formål.

- Det vil bevise at du har makten til å bruke mynter i den nye lommeboken.
- Det vil demonstrere hvordan du bruker Electrum-programvaren til å gjøre en utgift (og noen funksjoner), før vi legger til ekstra kompleksitet for sikkerhet (ved å bruke en maskinvarelommebok eller en luftgappet datamaskin)
- Det vil forsterke ideen om at du har mange adresser å velge mellom for å motta og bruke, innenfor samme lommebok.
Åpne din test Electrum Wallet og klikk på fanen "Addresses", deretter høyreklikker du på den første adressen og velger Kopier –> Adresse:
![image](assets/30.webp)

Adressen er nå i datamaskinens minne.

Gå nå til en børs hvor du har litt bitcoin, og la oss ta ut en liten mengde til denne adressen, si 50 000 sats. Jeg kommer til å bruke Coinbase som et eksempel fordi det er den mest brukte børsen, selv om de er en fiende av Bitcoin, og jeg er motvillig til å logge inn på en gammel forlatt konto for dette formålet.

Logg inn, og klikk på Send/Motta-knappen, som per i dag er i øvre høyre hjørne av nettsiden.

![image](assets/31.webp)

Jeg har åpenbart ingen midler hos Coinbase, men bare forestill deg at det er midler her og følg med: Lim inn adressen fra Electrum i "Til"-feltet som jeg har gjort. Du må også velge et beløp (jeg foreslår 50 000 sats eller så). Ikke legg til en "valgfri melding" – Coinbase samler inn nok av dine data (og selger dem), det er ikke nødvendig å hjelpe dem. Til slutt, klikk på "Fortsett". Etter det vet jeg ikke hvilke andre pop-ups du vil få, du er på egen hånd, men metoden er lik for alle børser.

![image](assets/32.webp)

Avhengig av børsen, kan du se satsene i lommeboken din umiddelbart, eller det kan være noen timer/dagers forsinkelse.

Merk at Electrum vil vise deg mottatte mynter selv om de ikke har blitt bekreftet på blockchain. Myntene du har blir lest fra en Bitcoin Node sin venteliste, eller "mempool". Når den kommer på en blokk, vil du se midlene som bekreftet.

Nå som vi har en UTXO i lommeboken vår, bør vi merke den. Bare vi kan se denne etiketten, den har ingenting å gjøre med det offentlige hovedboken. Alle våre Electrum-etiketter er kun synlige på datamaskinen vi bruker. Vi kan faktisk lagre en fil og bruke den til å gjenopprette alle våre etiketter til en annen datamaskin som kjører samme lommebok.

### Lag en etikett for en UTXO

Jeg trengte en donasjon til denne testlommeboken, takk til @Sathoarder for å gi meg en live UTXO (10 000 sats), og en annen person (anon) donerte til samme adresse (5000 sats). Legg merke til at det er 15 000 sats i den første adressebalansen, og totalt 2 transaksjoner (ytterste høyre kolonne). Nederst er saldoen 10 000 sats bekreftet, og ytterligere 5 000 sats er ubekreftet (fortsatt i mempool).

![image](assets/33.webp)

Nå, hvis vi går over til fanen "Coins", kan vi se to "mottatte mynter" eller UTXOer. De er begge i samme adresse.

![image](assets/34.webp)

Går tilbake til adressefanen, hvis du dobbeltklikker på "etiketter"-området ved siden av adressen, vil du kunne skrive inn litt tekst, deretter trykke <enter> for å lagre:

![image](assets/35.webp)

Dette er god praksis slik at du kan holde styr på hvor myntene dine kom fra, om de er KYC-frie eller ikke, og hvor mye hver UTXO kostet deg (i tilfelle du trenger å selge og beregne skatten som skal stjeles fra deg av regjeringen din).
Ideelt sett bør du unngå å samle opp flere mynter i samme adresse. Hvis du likevel bestemmer deg for å gjøre det (ikke gjør det), kan du merke hver mynt i stedet for å merke dem alle med samme etikett ved å bruke adressemetoden. Du kan faktisk ikke gå til "mynter"-fanen og redigere etikettene der (nei, det ville vært for intuitivt!). Du må gå til Historikk-fanen, finne transaksjonen, merke den, og deretter vil du se etikettene i myntseksjonen. Alle etiketter du ser i myntseksjonen kommer fra adresseetikettene ELLER historikketikettene, men enhver historikketikett overstyrer en adresseetikett. For å sikkerhetskopiere etikettene dine til en fil, kan du eksportere dem fra menyen øverst, lommebok–>etiketter–>eksporter.
Videre, la oss bruke myntene fra den første adressen til den andre adressen. Høyreklikk på den første adressen og velg "bruk fra" (Dette er faktisk ikke nødvendig i dette scenarioet, men forestill deg at vi har mange mynter i mange adresser; ved å bruke denne funksjonen, kan vi tvinge lommeboken til kun å bruke de myntene vi ønsker. Hvis vi ønsker å velge flere mynter i flere adresser, kan vi velge adressene med et venstreklikk mens vi holder inne kommandotasten, deretter høyreklikk, og velg "bruk fra":

![bilde](assets/36.webp)

Når du gjør det, vil det være en grønn linje nederst i lommebokvinduet som indikerer antall valgte mynter og det totale beløpet tilgjengelig for bruk.

Du kan også bruke individuelle mynter innenfor en adresse og ekskludere andre i samme adresse, men dette frarådes fordi du etterlater mynter i en adresse som har blitt kryptografisk svekket på grunn av bruk av en av myntene (en annen grunn til ikke å sette flere mynter i en adresse, bortsett fra av personvernhensyn, er at gitt at du bør bruke dem alle hvis du bruker en, blir dette unødvendig dyrt). Slik velger du en enkelt mynt fra en delt adresse, men ikke gjør det:

![bilde](assets/37.webp)

Nå har vi valgt de to myntene for bruk. Videre bestemte vi hvor vi skal bruke dem. La oss sende dem til den andre adressen. Vi trenger å kopiere adressen slik:

![bilde](assets/38.webp)

Deretter går du til "Send"-fanen, og limer inn den andre adressen i "betal til"-feltet. Ikke nødvendig å legge til en beskrivelse; du kunne, men du kan gjøre det senere ved å redigere etiketter. For beløpet, velg "Maks" for å bruke alle de valgte myntene. Deretter klikker du på "Betal", og deretter klikker du på "avansert"-knappen på popup-vinduet som vises.

![bilde](assets/39.webp)

Klikk alltid på "avansert" på dette stadiet slik at vi kan få fin kontroll og sjekke nøyaktig hva som er i transaksjonen. Her er transaksjonen:

![bilde](assets/40.webp)

Vi ser to interne hvite bokser/vinduer. Den øverste er inngangsvinduet (hvilke mynter som brukes), og den nederste er utgangene (hvor myntene går).

Merk, statusen (øverst til venstre) er "usignert" for øyeblikket. "Beløp sendt" er 0 fordi myntene overføres innenfor lommeboken. Gebyret er 481 sats. Merk at hvis det var 480 sats, ville det siste nullen bli droppet, slik som dette, 0.0000048 og for et trøtt øye, kan dette se ut som 48 sats – vær forsiktig (noe Electrum-utviklerne burde fikse).
Størrelsen på transaksjonen refererer til datastørrelsen i bytes, ikke mengden bitcoin. "Replace by fee" er på som standard, og det lar deg sende transaksjonen på nytt med et høyere gebyr om nødvendig. LockTime lar deg justere når transaksjonen er gyldig – jeg har ikke eksperimentert med det ennå, men råder mot å bruke det med mindre du fullt ut forstår hva du gjør og har øvd med små beløp.

Nederst har vi noen fancy verktøy for justering av gruvegebyr. Alt du trenger å gjøre for interne overføringer er å sette det til minimumsgebyret på 1 sat/byte. Skriv bare inn tallet manuelt i Target fee-feltet. For å sjekke et passende gebyr for en ekstern betaling, kan du konsultere https://mempool.space for å se hvor opptatt mempoolen er, og noen foreslåtte gebyrer vises.

![bilde](assets/41.webp)

Jeg har valgt 1 sat/byte.

I inndatavinduet ser vi to oppføringer. Den første er 5000 sat-donasjonen. Vi ser på venstre side dens transaksjonshash (som vi kan slå opp på blockchain). Ved siden av den er det en "21" – dette indikerer at det er utdata merket 21 i den transaksjonen (det er faktisk den 22. utdataen fordi den første er merket null).

Noe å merke seg her: UTXOer eksisterer kun inne i en transaksjon. For å bruke en UTXO må vi referere til den, og sette den referansen inn i inndataen til en ny transaksjon. Utdataene blir da nye UTXOer og den gamle UTXOen blir en STXO (Spent transaction output).

Den andre linjen er 10 000 sat-donasjonen. Den har en "0" ved siden av transaksjonshashen den kom fra fordi den er den første (og muligens eneste) utdataen for den transaksjonen.

I vinduet nederst ser vi vår adresse. Legg merke til at bitcoin-totalen av inndataene ikke helt samsvarer med totalen av utdataene. Forskjellen går til gruvearbeideren. Gruvearbeideren ser på avviket i alle transaksjonene i blokken den prøver å utvinne, og legger det tallet til sin belønning. (Gruvegebyrer på denne måten er helt frakoblet fra transaksjonskjeden og starter et nytt liv).

Hvis vi justerer gruvegebyret, vil utdataverdien automatisk endre seg.

> Det er verdt å påpeke her: Legg merke til fargen på adressene i transaksjonsvinduet. Husk at de grønne adressene er oppført i adressefanen din. Hvis en adresse er uthevet i grønt (eller gult) i et transaksjonsvindu, har Electrum gjenkjent adressen som en av sine egne. Hvis adressen ikke har noen utheving, er det en ekstern adresse (ekstern til den nåværende åpne lommeboken), og du bør sjekke den med ekstra forsiktighet.

Når du har sjekket alt i transaksjonen og er sikker på at du er fornøyd med hvilke mynter du bruker, og hvor myntene går, kan du klikke på "finalise".

![bilde](assets/42.webp)

Etter at du har klikket på "finalise", kan du ikke lenger gjøre redigeringer – Hvis du trenger det, må du lukke dette og starte på nytt. Legg merke til at "finalise"-knappen har endret seg til "export", og nye knapper har dukket opp: "save", "combine", "sign" og "broadcast". "Broadcast"-knappen er grået ut fordi transaksjonen er usignert og dermed ugyldig på dette stadiet.

Når du klikker på sign, hvis du har et passord for lommeboken vil du bli bedt om det, og deretter vil statusen (øverst til høyre) endre seg fra "Unsigned" til "Signed". Deretter vil "Broadcast"-knappen være tilgjengelig.
Etter at du har sendt ut, kan du lukke transaksjonsvinduet. Hvis du går til adressefanen, vil du nå se at den første adressen er tom, og den andre adressen har 1 UTXO.
Merk: Du vil se alle disse endringene selv før transaksjonen har blitt minet til en blokk, eller "bekreftet". Dette er fordi Electrum oppdaterer saldoer/transaksjoner basert på ikke bare blockchain-data, men også mempool-data. Ikke alle lommebøker gjør dette.

Noe som er verdt å påpeke er at i stedet for å sende ut, kan vi lagre transaksjonen for senere. Den kan lagres enten i usignert eller signert tilstand.

Klikk på "export"-knappen (paradoksalt nok, IKKE klikk på "save"-knappen), og du vil se en rekke alternativer. Transaksjonen er kodet med tekst, og derfor kan den lagres på en rekke måter.

![bilde](assets/43.webp)

Å lagre til en QR-kode er veldig interessant. Hvis du velger dette, vil en QR dukke opp:

![bilde](assets/44.webp)

Du kan deretter ta et bilde av QR-koden. Det er en rekke ting du kan gjøre med dette, men for nå, la oss bare si at du laster den tilbake i lommeboken senere. Du kan lukke Electrum, laste lommeboken igjen, og gå til menyen Verktøy:

![bilde](assets/45.webp)

Dette vil laste opp datamaskinens kamera. Du viser deretter kameraet bildet av QR-koden på telefonen din, og dette vil laste transaksjonen tilbake, akkurat slik du forlot den.

Det er ikke intuitivt hvordan man laster en lagret transaksjon, så ta spesielt notat. Å laste en transaksjon er ikke et "verktøy", men alternativet er skjult i verktøymenyen (noe Electrum-utviklerne burde fikse).

En lignende prosess er mulig med en transaksjon lagret som en fil. Prøv å øve med enten metode, innenfor samme lommebok. Jeg vil ikke gå gjennom det her, men du kan bruke denne funksjonen til å sende en transaksjon rundt mellom samme lommebok på forskjellige datamaskiner, mellom multisignatur-lommebøker, og til og fra maskinvarelommebøker. Her er noen instruksjoner.

Nå, tilbake til "save"-knappen – dette er ikke måten å lagre transaksjonsteksten på. Det dette faktisk gjør er å fortelle Electrum-lommeboken å gjenkjenne denne transaksjonen på den lokale datamaskinen som blir sendt inn som en betaling. Hvis du gjør det ved en feiltakelse, vil du se transaksjonen med et lite datamaskinikon. Du kan høyreklikke og slette transaksjonen – ikke bekymre deg, du kan ikke slette bitcoin på denne måten. Electrum vil da glemme at denne transaksjonen noen gang skjedde, og vil "refundere" satsene tilbake og vise satsene på riktig sted hvor de faktisk eksisterer.

### Endringsadresser

Endringsadresser er interessante. Du trenger å forstå UTXOs for å forstå denne forklaringen. Hvis du bruker til en adresse et beløp som er mindre enn UTXO, så vil de gjenværende bitcoinene gå til gruvearbeideren med mindre en endringsutgang er spesifisert.

Du kan ha en 6.15 bitcoin UTXO og ønsker å bruke 0.15 bitcoin for å donere til noen protestanter som blir undertrykt av den tyranniske "demokratiske" regjeringen et sted i verden. Du ville da ta de 6.15 bitcoinene (ved å bruke "spend from"-funksjonen i Electrum), og legge dem i en transaksjon.

Du ville lime inn protestantenes adresse i "pay to"-feltet, kanskje du ville sette "EndTheFed & WEF" i "description"-feltet, og for beløpet, ville du sette 0.15 bitcoin og klikke "pay", deretter "advanced".
På transaksjonsskjermen, i inndatavinduet, vil du se 6.15 bitcoin UTXO. I utdatavinduet vil du se en adresse uten utheving (dette er protestantenes adresse) med 0.15 bitcoin ved siden av. Du vil også se en gul adresse med litt mindre enn 6.0 bitcoin. Dette er endringsadressen som automatisk velges av lommeboken fra en av sine egne gule endringsadresser. Formålet med endringsadressen er slik at lommeboken kan plassere vekslepenger i dem uten å rote til tilgjengeligheten til mottaksadressene som du kanskje har planer for, eller sendt fakturaer for. Hvis de skal brukes senere av kunder, for eksempel, vil du ikke at lommeboken din automatisk bruker dem og fyller dem opp. Det er rotete og dårlig for personvernet.
Merk at når du justerer gruveavgiften, vil mengden av endringsutgangen automatisk justere seg, ikke betalingsbeløpet.

### Manuell endring eller betal til mange

Dette er en virkelig interessant funksjon av Electrum. Du får tilgang til den slik.

![bilde](assets/46.webp)

Du kan deretter angi flere destinasjoner for UTXO-saldoen du bruker, slik:

![bilde](assets/47.webp)

Lim inn adressen, skriv inn et komma, deretter et mellomrom, deretter beløpet, deretter <enter>, og gjør det igjen. IKKE SKRIV INN BELØP I "BELØP"-VINDUENE – Electrum vil fylle ut totalen her etter hvert som du skriver de individuelle beløpene i "Betal til"-vinduet.

Dette lar deg manuelt bestemme hvor endringen går (f.eks. en spesifikk adresse i lommeboken din, eller en annen lommebok), eller du kan betale til mange personer samtidig. Hvis totalen din ikke er høy nok til å matche størrelsen på UTXO-en, vil Electrum fortsatt opprette en ekstra endringsutgang for deg.

Funksjonen Betal til Mange gir også muligheten til å lage dine egne "PayJoins" eller "CoinJoins" – utenfor rekkevidden av denne artikkelen, men jeg har en guide her. (https://armantheparman.com/cj/)

## Lommebøker

Jeg ønsker å demonstrere en Kun Se-Lommebok ved bruk av Electrum. For å gjøre det, må jeg først definere "lommebok". Det er to måter "lommebok" brukes på i Bitcoin:

- Type A, "lommebok" – refererer til programvaren som viser deg adressene og saldoene dine, f.eks. Electrum, Blue Wallet, Sparrow Wallet osv.

- Type B, "lommebok" – refererer til den unike samlingen av adresser som er assosiert med kombinasjonen av vår seed_phrase/passphrase/derivation_path. Det er 8.6 milliarder adresser i enhver lommebok (4.3 milliarder mottaksadresser, og 4.3 milliarder endringsadresser). Hvis du endrer noe i seed phrase, passphrase, eller derivation path, får du en ubrukt lommebok med nye, og alle unike, 8.6 milliarder tomme adresser.

Hvilken type noen refererer til når de bruker ordet "lommebok" er åpenbart i konteksten.

## Kun Se-Lommebok – en øvelse

Det er ikke helt åpenbart hva en kun se-lommebok er for, men jeg vil starte med å forklare hva det er, hvordan man lager en øvelsesversjon, og så vil vi komme tilbake til formålet senere når jeg forklarer mer om maskinvarelommebøker. (For en grundig gjennomgang av hvordan du bruker en maskinvarelommebok, og ulike spesifikke merker, se her.)
Vi skal lage en dummy vanlig lommebok (denne gangen legger vi til litt mer kompleksitet med en passfrase), og deretter dens tilsvarende overvåkingslommebok. Hvis du vil, kan du kopiere den jeg lagde nøyaktig, eller lage din egen – denne lommeboken skal forkastes; ikke faktisk bruk den. Start med å generere et 12-ords frø ved hjelp av Ian Coleman-nettstedet.
Legg merke til de 12 tilfeldige ordene i skjermbildet nedenfor, og at jeg har skrevet inn en passfrase i passfrasefeltet:

PASSFRASE: “Craig Wright er en løgner og en svindler og hører hjemme i fengsel. Også, Ross Ulbricht bør slippes ut fra fengsel umiddelbart.”

Passfrasen kan være opptil 100 tegn lang, og ideelt sett bør den være utvetydig og ikke for kort – Den jeg har brukt er bare for moro skyld – Jeg foreslår generelt å unngå store bokstaver og symboler bare for å redusere stresset ditt i å prøve kombinasjoner hvis du noen gang hadde et problem med å huske passfrasen din.

![bilde](assets/48.webp)

Deretter, i Electrum, gå til menyfilen–>ny/gjenopprett. Skriv et unikt navn for å opprette en ny lommebok og klikk “neste”.

![bilde](assets/49.webp)

De neste stegene bør du være kjent med nå, så jeg vil liste dem uten bilder:

- Standard lommebok
- Jeg har allerede et frø
- Kopier og lim inn de 12 ordene i boksen, eller skriv dem inn manuelt.
- Klikk på alternativer og velg BIP39, og klikk også på passfrase avkrysningsruten (“utvid dette frøet med egendefinerte ord”)
- Skriv inn passfrasen din nøyaktig som du gjorde på Ian Coleman-siden
- La standard skriptsemantikk og avledningssti være
- Ikke nødvendig å legge til et passord (låser lommeboken)

Gå nå tilbake til Ian Coleman-nettstedet, ned til “avledningssti”-delen, og klikk på “BIP 84”-fanen for å velge samme skriptsemantikk som standardene i Electrum (Native Segwit).

![bilde](assets/50.webp)

De utvidede private og offentlige nøklene er rett nedenfor, og de endrer seg når du gjør endringer i avledningsstien (eller noe annet høyere opp på siden).

![bilde](assets/51.webp)

Du vil også se “BIP32 utvidede private/offentlige” nøkler – disse skal ignoreres for nå.

Den utvidede private nøkkelen for kontoen kan brukes til å fullstendig regenerere lommeboken din. Den utvidede offentlige nøkkelen for kontoen, derimot, kan bare produsere en begrenset versjon av samme lommebok (overvåkingslommebok) – Hvis du legger denne nøkkelen i Electrum, vil den fortsatt produsere alle de 8,6 milliarder adressene som frøet eller den utvidede private nøkkelen ville ha, men det vil ikke være noen private nøkler tilgjengelig for Electrum, så ingen utgifter er mulig. La oss gjøre det nå for å demonstrere poenget:

Kopier “den utvidede offentlige nøkkelen for kontoen” til utklippstavlen.

Gå deretter til Electrum, la den nåværende lommeboken vi lagde være åpen, og gå til fil–>ny/gjenopprett. Prosessen for å lage lommeboken er litt annerledes enn før:

- Standard lommebok
- Bruk en hovednøkkel
- Lim inn den utvidede offentlige nøkkelen i boksen og fortsett
- Ikke nødvendig å skrive inn en passfrase; den er allerede en del av den utvidede offentlige nøkkelen
- Ikke nødvendig å skrive inn skriptsemantikken og avledningsstien
- Ikke nødvendig å legge til et passord (låser lommeboken)

Når lommeboken lastes, bør du legge merke til at nøyaktig de samme adressene lastes som tidligere da frøet ble angitt. Du bør også legge merke til øverst i tittellinjen, det står “overvåkingslommebok”. Denne lommeboken kan vise deg adressene dine og saldoene (ved å sjekke saldoer via en node), men du er ikke i stand til å SIGNERE transaksjoner (fordi overvåkingslommeboken ikke har noen private nøkler).
Så hva er poenget med det?
En grunn, og ikke den viktigste, er at du potensielt kan observere lommeboken din og saldoen på en datamaskin uten å eksponere dine private nøkler for eventuell skadelig programvare på datamaskinen.

En annen grunn er at det er NØDVENDIG for å kunne gjøre betalinger hvis du velger å holde dine private nøkler utenfor datamaskinen; jeg skal forklare:

> Maskinvarelommebøker (HWW) ble skapt slik at en enhet kan holde dine private nøkler sikkert (låst med en PIN-kode), aldri eksponere nøklene for en datamaskin (selv når den er koblet til en datamaskin via en kabel), og de kan ikke selv koble seg til internett. En slik enhet kan ikke gjennomføre transaksjoner på egen hånd fordi alle bitcoin-transaksjoner starter med å referere til en UTXO(er) på blokkjeden (som er på en node). En lommebok må spesifisere hvilket transaksjons-ID UTXOen er i, og hvilken utgang av transaksjonen som skal brukes. Først etter å ha spesifisert inngangen kan en ny transaksjon skapes i utgangspunktet, for ikke å snakke om å bli signert. Maskinvarelommebøker kan ikke skape transaksjoner fordi de ikke har tilgang til noen UTXOer – de er ikke koblet til noe! En utvidet offentlig nøkkel blir vanligvis trukket ut fra HWW, og adresser vises deretter på en datamaskin – mange vil være kjent med Ledger-programvaren eller Trezor Suite som viser adresser og saldoer på datamaskinen deres – dette er en overvåkende lommebok. Disse programmene kan skape transaksjoner, men de kan ikke signere. De kan kun få transaksjoner signert av HWWer som er koblet til dem. HWW tar den nygenererte transaksjonen fra den overvåkende lommeboken, signerer den, og sender den deretter tilbake til datamaskinen for kringkasting til en node. HWW kan ikke kringkaste selv, dens tilknyttede overvåkende lommebok gjør det. På denne måten samarbeider de to lommebøkene (offentlig nøkkellommebok på datamaskinen, og privat nøkkellommebok i HWW) for å generere, signere og kringkaste, alt mens de sørger for at de private nøklene forblir isolert og borte fra en internett-tilkoblet enhet.

## Delvis Signerte Bitcoin Transaksjoner (PSBTs)

Det er mulig for en transaksjon å bli skapt og lagret til en fil, senere lastet inn, signert, lagret, senere lastet inn igjen, og deretter til slutt kringkastet – jeg sier ikke at noen trenger å gjøre dette; det er bare noe som er mulig.

Tenk nå på en 3 av 5 multisignatur-lommebok – 5 private nøkler skaper en lommebok, og 3 er nødvendige for å fullstendig signere en transaksjon (Se her for å lære mer om nøkler i multisignatur-lommebøker). Det er mulig å ha 5 forskjellige datamaskiner hver med en av de fem private nøklene.

Datamaskin én kunne generere en transaksjon og signere den. Den kunne deretter lagre den til en fil, og sende den via e-post til Datamaskin 2. Datamaskin 2 kan deretter signere, og potensielt lagre filen til en QR-kode, og overføre QR-koden via en Zoom-samtale til Datamaskin 3 på den andre siden av verden. Datamaskin 3 kan fange opp QR-koden, laste transaksjonen inn i Electrum, og signere transaksjonen. Etter de første 2 signaturene var transaksjonen en PSBT (delvis signert bitcoin transaksjon). Etter den 3. signaturen ble transaksjonen fullstendig signert og gyldig, klar for kringkasting.

For å lære mer om PSBTs, se denne guiden. (https://armantheparman.com/psbt/)

## Bruk av Maskinvarelommebøker med Electrum

Jeg har en guide om bruk av maskinvarelommebøker generelt, som jeg tror ville være viktig for folk som er nye til HWWer, å lese. (https://armantheparman.com/using-hwws/)
Det finnes også guider om ulike merker av HWW-er som kobles til Sparrow Bitcoin Wallet her. (https://armantheparman.com/hwws/)
Dette vil være min første guide som viser hvordan man bruker en hardware wallet med Electrum – Jeg kommer til å bruke ColdCard hardware wallet for å demonstrere. Dette er ikke ment å være en detaljert guide om ColdCard spesifikt, den guiden finner du her. Jeg viser kun Electrum-spesifikke punkter. (https://armantheparman.com/cc/)

### Koble til via micro SD-kortet (air-gapped)

Før du kobler til din ekte lommebok via ColdCard, håper jeg du har gjennomgått de tidligere stegene med å laste en Electrum dummy lommebok og sette opp nettverksparametrene.

Deretter, på ColdCard, sett inn SD-kortet. Jeg antar at du allerede har opprettet din seed. Hvis du tilgår lommeboken med en passfrase, bruk den nå. Rull ned og velg menyen Avansert/Verktøy –>Eksporter Lommebok –> Electrum Lommebok.

Du kan rulle ned og lese meldingen. Den tilbyr alltid å velge “1” for å angi et ikke-null konto nummer (noe som er en del av avledningsveien), men hvis du fulgte mitt råd, har du ikke rotet med standard avledningsveier så du vil ikke ønske et ikke-null konto nummer; trykk bare på hake for å fortsette.

Deretter velger du skriptsemantikken. De fleste vil velge “Native Segwit”.

Det vil si “Electrum lommebokfil skrevet”, og vil vise filnavnet. Gjør et mentalt notat av det.

Ta deretter ut micro SD-kortet og sett det i datamaskinen med Electrum.

Noen operativsystemer vil automatisk åpne filutforskeren når du setter inn microSD. Mange vil se den nye lommebokfilen og dobbeltklikke på den, og lure på hvorfor den ikke fungerer. Det er ikke et flott design. Du må faktisk ignorere filutforskeren (lukke den), og åpne lommebokfilen ved hjelp av Electrum:

Åpne Electrum. Hvis den allerede er åpen med en annen lommebok, velg fil –> ny. Vi leter etter dette vinduet:

![bilde](assets/52.webp)

Her er trikset, det er ikke intuitivt. Klikk på “velg”. Naviger deretter i filsystemet på microSD-kortet og finn lommebokfilen og åpne den.

Nå har du åpnet din hardware lommeboks tilsvarende overvåkingslommebok. Fint.

### Koble til via USB-kabelen.

Denne metoden burde være enklere, men for Linux-datamaskiner, er det mye vanskeligere. Noe som kalles “Udev-regler” må oppdateres. Slik gjør du det (detaljert guide https://armantheparman.com/gpg-articles/ ), og kort sagt:

Det er en god idé å sørge for at systemet er oppdatert. Deretter:

```bash
sudo apt-get install libusb-1.0-0-dev libudev-dev
```

deretter...

```bash
python3 -m pip install ckcc-protocol
```

Hvis du får en feil, sørg for at pip er installert. Du kan sjekke med (pip –version), og du kan installere det med (sudo apt install python3-pip)

Opprett eller endre eksisterende, filen, /etc/udev/rules.d/

Slik:

```bash
sudo nano /etc/udev/rules.d
```

En tekstredigerer vil åpne. Kopier teksten fra her og lim den inn i rules.d-filen, lagre og avslutt.

![bilde](assets/53.webp)

Kjør deretter disse kommandoene en etter den andre:

```bash
sudo groupadd plugdev
sudo usermod -aG plugdev $(whoami)
sudo udevadm control –reload-rules && sudo udevadm trigger
```
Hvis du får meldingen "gruppen plugdev finnes allerede", er det greit, fortsett. Etter det andre kommandoen, vil du ikke få noen tilbakemelding/svar, bare fortsett til den tredje kommandoen.
Du må kanskje koble fra og deretter koble til ColdCard til datamaskinen igjen.

Hvis du etter alt dette fortsatt ikke klarer å koble til ColdCard, ville jeg prøvd å oppdatere firmwaren (veiledning kommer snart, men for nå kan du finne instruksjoner på produsentens nettsted).

Deretter, opprett en ny lommebok:

- Standard lommebok
- Bruk en maskinvareenhet
- Den vil skanne og oppdage din ColdCard. Fortsett.
- Velg skriptsemantikk og avledningssti
- Bestem om lommebokfilen skal krypteres (anbefales)

### Transaksjoner med ColdCard

Med kabelen tilkoblet, er transaksjoner enkle. Å signere transaksjoner vil være sømløst.

Hvis du bruker enheten på en luftgappet måte, må du manuelt overføre den lagrede transaksjonen mellom enhetene ved hjelp av microSD-kortet. Det er noen triks.

Etter å ha opprettet en transaksjon og fullført den, må du klikke på eksportknappen i nedre venstre hjørne. Du vil se "lagre til fil" som motintuitivt, er ikke det vi vil ha. Du må faktisk først gå til den aller siste menyopsjonen som sier "for maskinvarelommebøker", og deretter, fra det valget, finne den andre "lagre til fil" og velge den. Deretter lagrer du filen til microSD, tar ut kortet og setter det i ColdCard. Husk at du kanskje må bruke en passfrase for å velge riktig lommebok. Skjermen vil si klar til å signere. Klikk på hake-tegnet, inspiser transaksjonen, og fortsett ved å bekrefte med hake-tegnet. Når det er gjort, ta ut kortet, og sett det tilbake i datamaskinen.

Deretter må vi åpne transaksjonen ved hjelp av electrum. Funksjonen er skjult i menyen verktøy –> last inn transaksjon. Naviger i filsystemet og finn filen. Det vil være tre filer hver gang du signerer. Den opprinnelige lagrede filen som Watching Wallet lagde, og to laget av ColdCard (jeg vet ikke hvorfor den gjør dette). En vil si "signert" og en vil si "endelig". Det er ikke intuitivt, men den "signerte" er ikke nyttig, vi trenger å åpne den "endelige" transaksjonen.

Når du har lastet den inn, kan du klikke på "kringkast" og betalingen vil bli gjort.

## Oppdatering av Electrum og den skjulte ".electrum"-mappen

Electrum finnes på datamaskinen din på to steder. Det er selve applikasjonen, og det er en skjult konfigurasjonsmappe. Den mappen finnes på forskjellige steder avhengig av operativsystemet ditt:

Windows:

> C:/Users/ditt_brukernavn_her/AppData/Roaming/Electrum

Mac:

> /Users/ditt_brukernavn_her/.electrum

Linux:

> /home/ditt_brukernavn_her/.electrum

Merk at "." før "electrum" i Linux og Mac – det indikerer at mappen er skjult. Merk også at denne mappen kun blir opprettet (automatisk) første gang du kjører Electrum. Mappen inneholder electrum-konfigurasjonsfilen og også mappen som holder alle lommebøkene du har lagret.

Hvis du sletter Electrum-programmet fra datamaskinen din, vil den skjulte mappen forbli, med mindre du aktivt sletter den også.
For å oppgradere Electrum, følger du samme prosedyre som jeg beskrev i begynnelsen for å laste ned og verifisere. Du vil da ha to kopier av programmet på datamaskinen din, og du kan kjøre begge – hvert program vil få tilgang til den samme skjulte Electrum-mappen for sin konfigurasjon og lommeboktilgang. Alle tingene vi lagret, som grunnenheten, standardnoden å koble til, andre preferanser og tilgang til lommebøker, vil forbli fordi alt dette er lagret i den mappen.
### Flytte din Electrum og lommebøker til en annen datamaskin

For å gjøre dette, kan du kopiere programfilene til en USB-stasjon, og også kopiere .electrum-mappen. Kopier eller flytt dem deretter til den nye datamaskinen. Du trenger ikke å verifisere programmet igjen. Sørg for å kopiere .electrum-mappen til standardplasseringen (husk å kopiere den FØR du kjører Electrum for første gang på den datamaskinen, ellers vil en tom standard .electrum-mappe bli fylt, og du kan bli forvirret).

## Etiketter

Som jeg forklarte tidligere, på adressetabellen, er det en etikettkolonne. Du kan dobbeltklikke der og legge inn notater for deg selv (det er bare på datamaskinen din, ikke offentlig, og ikke på blockchain).

![bilde](assets/54.webp)

Når du flytter din Electrum-lommebok til en annen datamaskin, kan du ønske å ikke miste alle disse notatene. Du kan sikkerhetskopiere dem til en fil ved å bruke menyen, lommebok–> etiketter –>eksporter, og deretter på den nye datamaskinen, bruke lommebok–>etiketter–>import.

## Tips:

Hvis du finner denne ressursen nyttig, og du ønsker å støtte det jeg gjør for Bitcoin, kan du donere noen sats her:

Statisk Lynadresse: dandysack84@walletofsatoshi.com
https://armantheparman.com/electrum/