---
name: My Node
description: Sett opp din bitcoin MyNode
---

![bilde](assets/0.webp)

https://mynodebtc.com/

Den enkleste, mest kraftfulle måten å kjøre en Bitcoin og Lightning node på! Vi kombinerer den beste åpen kildekode-programvaren med vårt grensesnitt, administrasjon og støtte slik at du enkelt, privat og sikkert kan bruke Bitcoin og Lightning.

## Typer Node-oppsett

Det finnes ulike Node-oppsett. MyNode er utmerket. Det følger med mange apper, og enda flere hvis du betaler for premiumversjonen. Ellers er det veldig kjedelig å laste ned alle disse appene selv. MyNode gjør dette ganske enkelt som du vil se.

Et alternativ og lignende valg er RaspiBlitz. GUI-en er ikke like fin, og appene overlapper mye med appene som følger med MyNode, men Raspiblitz er gratis åpen kildekode-programvare (FOSS) og MyNode er ikke helt det. En annen forskjell er at MyNode kjøres i en Docker-container. Jeg finner Docker skremmende og vanskelig å feilsøke. Dette er bare et problem hvis du støter på feil eller bugs. Utvikleren tilbyr hjelp for premiumbrukere og det er også en Telegram-chatgruppe.

RaspiBlitz er bare flere programmer installert på Linux, uten Docker. Den eksterne harddisken kan enkelt kobles til en annen Linux-maskin med Bitcoin Core, og vips, så er du i gang, skulle du trenge det.

Et annet alternativ er å bare installere Bitcoin Core og en Electrum Server-variant (det finnes flere) på et operativsystem. Jeg har guider for Linux (Raspberry Pi), Mac og Windows.

## Handleliste

- Raspberry Pi 4, 4Gb minne eller 8Gb (4Gb er nok)

- Offisiell Raspberry Pi-strømforsyning (Veldig viktig! Ikke kjøp generisk, seriøst)

- Et etui til Pi. FLIRC-etuiet er fantastisk. Hele etuiet er en varmespreder og du trenger ikke en vifte, som kan være støyende

- 16 Gb microSD-kort (du trenger ett, men noen få er hendige)

- En minnekortleser (de fleste datamaskiner vil ikke ha en spor for et microSD-kort).

- Ekstern SSD 1Tb harddisk.  
  Merk: SSD er avgjørende. ikke bruk bærbar ekstern harddisk selv om den er billigere

- En ethernet-kabel (for å koble til hjemmeruteren din)

- Du trenger ikke en skjerm

## Last ned MyNode-bilde

Naviger til MyNode-nettstedet Lenke

![bilde](assets/1.webp)

Klikk <Last ned nå>

Last ned Raspberry Pi 4-versjonen:

![bilde](assets/2.webp)

Det er en stor fil:

![bilde](assets/3.webp)

Last ned SHA 256-hashene

![bilde](assets/4.webp)

Åpne terminalen på Mac eller Linux eller Kommandoprompt for Windows. Skriv:

```bash
shasum -a 256 NEDLASTETFILNAVN # <--- Mac/Linux
certUtil -hashfile NEDLASTETFILNAVN SHA256 # <--- Windows
```

Datamaskinen tenker i 20 sekunder eller så. Deretter, sjekk at utdata-hashfilen stemmer overens med den som ble lastet ned fra nettstedet i forrige trinn. Hvis den er identisk, kan du fortsette.
Flash SD-kortet

## Last ned og installer Balena Etcher. Lenke

Jeg klarte ikke å finne den digitale signaturen for dette. Hvis du vet hvordan, vennligst gi meg beskjed så jeg kan oppdatere denne artikkelen.

Etcher er selvforklarende å bruke. Sett inn ditt micro SD-kort og flash Raspberry Pi-programvaren (.img-fil) på SD-kortet.

![bilde](assets/5.webp)
![bilde](assets/6.webp)
Når du er ferdig, er stasjonen ikke lenger lesbar. Du kan få en feil fra operativsystemet, og stasjonen bør forsvinne fra skrivebordet. Trekk ut kortet.

## Sett opp Pi-en og sett inn SD-kortet

Delene (kabinettet er ikke vist):

![bilde](assets/12.webp)
![bilde](assets/13.webp)

Koble til ethernet-kabelen, og USB-kontakten for harddisken (ikke strøm ennå). Unngå å koble til de blåfargede USB-portene i midten. De er USB 3. MyNode anbefaler at du bruker USB 2-porten, selv om stasjonen kan være USB 3-kompatibel.

![bilde](assets/14.webp)

Micro SD-kortet går her:

![bilde](assets/15.webp)

Til slutt, koble til strømmen:

![bilde](assets/16.webp)

## Finn IP-adressen til Pi-en

Du trenger aldri en skjerm med MyNode. Du trenger imidlertid en annen datamaskin på hjemmenettverket. Hvis Pi-en din ikke er koblet til med ethernet, og du vil stole på WiFi, krever det å finne IP høyt nivå av datakunnskaper. Beklager, kan ikke hjelpe deg. Du trenger en ethernet-tilkobling. (Problemet kommer fra å trenge tilgang til en skjerm og operativsystemet for å koble til WiFi og angi et passord).

Sjekk ruteren din, for en liste over alle IP-ene til alle tilkoblede enheter.

Jeg skrev inn 192.168.0.1 i nettleseren (instruksjoner som fulgte med ruteren min), logget inn, og kunne se en enhet "MyNode" med IP 192.168.0.18. Merk at disse IP-adressene ikke er offentlig synlige på internett (de går gjennom ruteren først), de er bare identifikatorer for enheter på hjemmenettverket ditt.

Det er avgjørende å finne IP-en.

> OPPDATERING: du kan bruke terminalen på en Mac eller Linux-maskin for å finne IP-adressen til alle Ethernet-tilkoblede enheter på hjemmenettverket ved å bruke kommandoen “arp -a”. Utdataene er ikke så pene som det ruteren vil vise, men all informasjonen du trenger er der. Hvis det ikke er åpenbart hvilken som er Pi-en, utfør prøving og feiling.

## SSH inn i Pi-en

Du har muligheten til å logge på enheten eksternt via SSH-kommando, men det er ikke nødvendig (det er det hvis RaspiBlitz Node). Jeg vil vise deg hvordan uansett, da det er veldig praktisk.

Åpne en Mac eller Linux-datamaskin (for Windows, last ned putty, et SSH-verktøy) og skriv:

```bash
ssh admin@192.168.0.18
```

Bruk din egen IP-adresse. Brukernavnet for MyNode-enheten er "admin" som standard. Passordet er "bolt" som standard.

Hvis du har brukt Pi-en din før og byttet rundt på micro SD-kortet, vil du få denne feilen:

![bilde](assets/17.webp)

Det du må gjøre er å navigere til hvor "known_hosts"-filen er og slette den. Det er trygt å gjøre det. Feilmeldingen viser deg stien. For meg var det /Users/MittBrukernavn/.ssh/

Ikke glem "." før ssh, dette indikerer at det er en skjult mappe.

Prøv så SSH-kommandoen igjen.

Denne gangen vil du se denne utdataen:

![bilde](assets/18.webp)

Filen du slettet har blitt slettet, og du legger til et nytt fingeravtrykk. Skriv ja og <enter>.

Du vil bli bedt om å angi passordet. Det er "bolt"
Du har nå fått terminaltilgang til MyNode Pi, uten en skjerm, og kan bekrefte at alt er lastet jevnt og trutt.
![bilde](assets/19.webp)

## Tilgang via nettleseren

Åpne en nettleser. Det må være en datamaskin på hjemmenettverket ditt, du kan ikke gjøre dette utenfra. Det finnes en måte, men det er vanskelig. Jeg har ikke testet det.

Skriv inn IP-adressen i nettleserens adressevindu. Dette vil skje:

![bilde](assets/20.webp)

Skriv inn passordet “bolt” – endre det senere.

Deretter vil dette skje:

![bilde](assets/21.webp)

Velg Format Drive

![bilde](assets/22.webp)

Nå venter vi.

På et tidspunkt vil du bli spurt om du vil legge inn din produktnøkkel, eller bruke den gratis “community edition” — Jeg kommer til å vise Premium-utgaven. Jeg anbefaler å betale for premiumversjonen hvis du har råd, det er virkelig verdt det.

![bilde](assets/23.webp)

Du vil deretter se fremgangen av nedlastede blokker. Det tar dager:

![bilde](assets/24.webp)

Det er trygt å slå av maskinen under nedlastingen hvis du trenger det. Gå til innstillinger og finn knappen for å slå av maskinen. Ikke bare dra ut ledningen, du kan korruptere installasjonen eller harddisken.

Sørg for, tidlig i prosessen, å gå til “Innstillinger” og deaktivere quicksync. Det vil starte den innledende blokknedlastingen fra begynnelsen.

![bilde](assets/25.webp)

Jeg ønsket å fortsette med å lage guiden, så her er en annen MyNode jeg forberedte tidligere. Dette er hvordan siden ser ut når blockchain er synkronisert, og flere “apper” har blitt aktivert og synkronisert:

![bilde](assets/26.webp)

Merk at Electrum Server også trenger å synkroniseres, så så snart Bitcoin Blockchain er synkronisert, klikk på knappen for å starte den prosessen – tar en dag eller to. Alt annet er aktivert på noen få minutter etter at du velger å aktivere det. Du kan klikke på ting og utforske. Du vil ikke ødelegge noe. Hvis noe går i stykker (dette skjedde med meg, men jeg tror på grunn av billige deler) må du re-flash og starte nedlastingen på nytt. Problemet jeg har med MyNode er at hvis du trenger å “re-flash”, ender du opp med å måtte starte blockchain-synkroniseringen på nytt fra scratch. Det finnes tekniske måter å omgå dette på, men det er ikke enkelt.

Hvis du vil prøve en annen node også, for eksempel en RaspiBlitz, trenger du en ekstra SSD ekstern harddisk, og et annet micro SD-kort for å flashe. Ellers er det samme utstyr, du kan bare ikke kjøre MyNode og RaspiBlitz samtidig, åpenbart. Hvis du vil gjøre det, er det på tide å shoppe etter en annen Raspberry Pi.

Nå som du har en node i drift, bruk den, ikke bare la den sitte der uten å gjøre noe for deg. Følg min artikkel (og video) om hvordan du kobler din Electrum Desktop Wallet til Electrum Server og Bitcoin Core her.