---
name: RaspiBlitz
description: Guide til å sette opp din RaspiBlitz
---

![bilde](assets/0.webp)

RaspiBlitz er en gjør-det-selv Lightning Node (LND og/eller Core Lightning) som kjører sammen med en Bitcoin-Fullnode på en RaspberryPi (1TB SSD) og en fin skjerm for enkel oppsett og overvåking.

RaspiBlitz er hovedsakelig rettet mot å lære hvordan du kjører din egen node desentralisert hjemmefra - fordi: Ikke din Node, Ikke dine Regler. Oppdag & utvikle det voksende økosystemet til Lightning Network ved å bli en full del av det. Bygg den som en del av en workshop eller som et helgeprosjekt selv.

![video](https://youtu.be/DTHlSPMz3ns)
RASPIBLITZ - Hvordan kjøre en Lightning og Bitcoin Full Node av BTC session

# Parmans Raspiblitz Oppsettsveiledning

Raspiblitz er et utmerket system for å kjøre en Bitcoin Node og tilknyttede apper. Jeg anbefaler dette og My Node noden til de fleste brukere (Ha to noder for redundans ideelt.) En stor fordel er at Raspiblitz noden er "Free Open Source Software", i motsetning til MyNode eller Umbrel. Hvorfor er det viktig? Vlad Costa forklarer. Du kan også kjøre RaspbiBlitz med en WiFi-tilkobling i stedet for ethernet – her er en tilleggsveiledning for det. (Jeg har ikke funnet en måte å gjøre dette med MyNode).

Du kan kjøpe en ferdig node med en tilknyttet miniskjerm, eller du kan bygge den selv (du trenger ikke en skjerm).

Veiledningen på github-siden er utmerket, men muligens for detaljert for en moderat erfaren bruker. Mine instruksjoner vil være mer konsise og forhåpentligvis lettere å følge.

I hovedsak er prosessen veldig lik prosessen med å sette opp en MyNode node med en Raspberry Pi 4. Raspiblitz-veiledningen foreslår at du kjøper en skjerm, men du trenger virkelig ikke en, og jeg ville ikke anbefale det. Du trenger ikke engang en ekstra tastatur eller mus. Bare tilgang til enhetens terminalmeny via en datamaskin på samme hjemmenettverk, og bruk ssh-kommandoen ved hjelp av terminal. Dette er mulig med Linux/Mac (enkelt) og litt vanskeligere med Windows.

## Steg 1: Kjøp utstyret.

Du trenger nøyaktig det samme utstyret som du trenger for å kjøre en MyNode node. Du kan prøve den ene eller den andre, den eneste forskjellen er dataene på microSD-kortet.

- Raspberry Pi 4, 4Gb minne eller 8Gb (4Gb er nok)
- Offisiell Raspberry Pi Strøm (Veldig Viktig! Ikke kjøp generisk, seriøst)
- Et etui til Pi. (FLIRC-etuiet er fantastisk. Hele etuiet er en varmespreder og du trenger ikke en vifte, som kan være støyende)
- 32 Gb microSD-kort (du trenger ett, men noen få er hendige.)
- En minnekortleser (de fleste datamaskiner vil ikke ha en spor for et microSD-kort).
- Ekstern SSD 1Tb harddisk.
- En ethernet-kabel (for å koble til hjemmeruteren din).

Du trenger ikke en skjerm (eller tastatur eller mus)

Merk: Dette er feil harddisk: Dette er en bærbar ekstern harddisk. Det er ikke en SSD. SSD er avgjørende. Dette er grunnen til at den er billig (Pris i AUD)

![bilde](assets/1.webp)

Dette er den riktige typen å få:

![bilde](assets/2.webp)

Dette er raskere, men unødvendig dyrt:

![bilde](assets/3.webp)

## Steg 2: Last ned Raspiblitz-bildet
Naviger til Raspiblitz GitHub-nettsiden, og finn "download image"-lenken:
![bilde](assets/4.webp)

SHA-256-hashen til den nedlastede filen er oppgitt på nettsiden. Den vil endre seg med hver oppdatering. Hvis du ikke forstår hva dette handler om, burde du det, så jeg skrev en guide du kan lese her.

![bilde](assets/5.webp)

## Steg 3: Verifiser Bilde

Før du fortsetter, hvis du ikke kjenner din vei rundt filsystemet på kommandolinjen, er det enkelt å lære, og du burde.

Her er en nyttig video for Linux, men gjelder også for Mac.

For Windows, her er en enkel opplæring.
Mac/Linux

Vent til filen er ferdig nedlastet (viktig!), og åpne deretter terminalen, naviger til hvor du lastet ned filen, og skriv inn følgende kommando...

```bash
shasum -a 256 xxxxxxxxxxxxxx
```

hvor xxxxxxxxxxxxxx er navnet på filen du nettopp lastet ned. Hvis du ikke er i katalogen der filen er, må du skrive inn hele banen.

Datamaskinen tenker i 20 sekunder eller så. Sjekk at utdata-hashfilen stemmer overens med den som ble lastet ned fra nettsiden i forrige trinn. Hvis den er identisk, kan du fortsette.
Windows

Åpne kommandoprompten og naviger til hvor filen er lastet ned, og skriv inn denne kommandoen:

```bash
certUtil -hashfile xxxxxxxxxxxxxxx SHA256
```

hvor xxxxxxxxxxxxxx er navnet på filen du nettopp lastet ned. Hvis du ikke er i katalogen der filen er, må du skrive inn hele banen.

Datamaskinen tenker i 20 sekunder eller så. Sjekk at utdata-hashfilen stemmer overens med den som ble lastet ned fra nettsiden i forrige trinn. Hvis den er identisk, kan du fortsette.

## Steg 4: Flash SD-kortet

Du kan bruke Balena Etcher til dette. Last det ned her.

Etcher er selvforklarende å bruke. Sett inn ditt micro SD-kort og flash Raspiblitz-programvaren (.img-fil) på SD-kortet.

![bilde](assets/6.webp)

![bilde](assets/7.webp)

![bilde](assets/8.webp)

![bilde](assets/9.webp)

Når det er gjort, er ikke stasjonen lenger lesbar. Du kan få en feilmelding fra operativsystemet, og stasjonen bør forsvinne fra skrivebordet. Ta ut kortet.

## Steg 5: Sett opp Pi-en og sett inn SD-kortet

Delene (kabinett ikke vist):

![bilde](assets/10.webp)

![bilde](assets/11.webp)

Koble til ethernet-kabelen, og harddiskens USB-kontakt (ikke strøm ennå). Unngå å koble til de blåfargede USB-portene i midten. De er USB 3. Bruk USB 2-porten, selv om disken kan være USB 3-kompatibel (mer pålitelig).

![bilde](assets/12.webp)

Micro SD-kortet går her:

![bilde](assets/13.webp)

Til slutt, koble til strømmen:

![bilde](assets/14.webp)

## Steg 6: Finn IP-adressen til Pi-en

Du trenger aldri en skjerm med Raspiblitz. Du trenger imidlertid en annen datamaskin på hjemmenettverket. Hvis din Pi ikke er koblet til med ethernet, og du vil stole på WiFi, krever det å finne IP-en noen dataferdigheter. Kan ikke hjelpe deg, beklager. Du trenger en ethernet-tilkobling. (Problemet kommer fra å trenge tilgang til en skjerm og operativsystemet for å koble til WiFi og angi et passord.)

Sjekk ruteren din, for en liste over alle IP-ene til alle tilkoblede enheter.
Jeg tastet inn 192.168.0.1 i nettleseren (instruksjoner som fulgte med ruteren min), logget inn og kunne se enheten min med IP-adressen 192.168.0.191. Merk at disse IP-adressene ikke er synlige for internett offentlig (de går gjennom ruteren først), de er bare identifikatorer for enheter på hjemmenettverket ditt.
Å finne IP-en er avgjørende.

> OPPDATERING: du kan bruke terminalen på en Mac eller Linux-maskin for å finne IP-adressen til alle Ethernet-tilkoblede enheter på hjemmenettverket ved å bruke kommandoen “arp -a”. Utdataene er ikke like pene som det ruteren vil vise, men all informasjonen du trenger er der. Hvis det ikke er åpenbart hvilken som er Pi, utfør prøving og feiling.

## Steg 7: SSH inn i Pi

Husk å sette SD-kortet inn i Pi før du slår den på. Vent noen minutter, og åpne deretter terminalen på en annen Linux/Mac.

For Mac/Linux, skriv i terminalen:

```bash
ssh admin@Din_Pi's_IP_adresse
```

For Windows, må du installere putty for å ssh inn i Pi. Skriv samme kommando som ovenfor.

Første gang du gjør dette, eller når du endrer OS på Pi ved å bytte SD-kort, kan du få denne feilen…

![bilde](assets/15.webp)

Måten å fikse det på er å navigere til hvor “known_hosts”-filen er (det forteller deg i feilmeldingen), og slette den. Kommandoen er "rm known_hosts"

Gjenta deretter ssh-kommandoen for å logge inn. Dette vil skje…

![bilde](assets/16.webp)

Skriv ja (hele ordet) for å fortsette.

Hvis vellykket, vil du bli bedt om et passord. Dette er ikke for datamaskinen din, men for raspiblitz. Det generiske passordet er “raspiblitz”, og du vil endre det senere. Terminalvinduet vil bli blått og du vil ha menyvalg som de gamle DOS-menyene. Naviger med piltastene eller musen.

![bilde](assets/17.webp)

Følg ledetrådene, sett passordene dine, og så vil den oppdage harddisken din og gi deg muligheten til å formatere den om nødvendig.

Deretter vil du bli spurt om du vil kopiere blockchain-data fra en annen kilde eller laste den ned på nytt. Å kopiere den er en læringsprosess og instruksjonene er ganske gode, og gode å ha for hånden….

![bilde](assets/18.webp)

Den enkle, men tregere måten er å laste ned hele kjeden fra bunnen av…

![bilde](assets/19.webp)

Masse tekst vil flimre over terminalskjermen. Du kan forveksle det med prosessen med nedlasting av blockchain, men for meg ser det ut som det genereres en privat nøkkel for kommunikasjon.

Deretter dukker lynvalg opp.

![bilde](assets/20.webp)

Lag et nytt passord for å låse lynlommeboken din, deretter vil en ny lommebok bli opprettet og du vil få 24 ord å skrive ned…

![bilde](assets/21.webp)

Sørg for at du skriver det ned og holder det sikkert. Jeg hørte om en person som ikke gjorde det fordi han ikke planla å bruke lyn, men så et år senere bestemte seg for å bruke det, og åpnet kanaler. Deretter innså han at ordene hans ikke var sikkerhetskopiert, og jeg husker det var ikke mulig å trekke ut ordene igjen fra enheten, han måtte lukke alle kanalene sine og starte på nytt. Han kom unna med det, men andre er kanskje ikke så heldige.

Etter dette ruller noen minutter med tekst ned terminalvinduet. Deretter…

![bilde](assets/22.webp)
Du vil bli logget ut av ssh-økten. Logg inn igjen, denne gangen med ditt nye passord, passord A. Når du er inne, vil du bli bedt om passord C for å låse opp din lightning-lommebok.
Nå venter vi. Sees om 2 uker. Du kan lukke terminalen, den gjør ingenting med Pi-en, det er bare et kommunikasjonsvindu.

![bilde](assets/23.webp)

Hvis du av en eller annen grunn ønsker å slå av Pi-en før blockchainen har fullført nedlastingen, er det greit så lenge du gjør det på riktig måte. Blockchainen vil fortsette nedlastingen der den slapp så snart du kobler til igjen.

Trykk CTRL+c for å avslutte den blå skjermen. Du vil få tilgang til Pi-ens Linux-terminal. Her kan du skrive "menu" som laster følgende skjerm, og derfra kan du slå av Pi-en.

![bilde](assets/24.webp)

SLUTT på veiledningen

Så fra nå av er noden din klar til å brukes. Hvis du fortsatt trenger hjelp til å navigere flere alternativer, se på github for flere veiledninger og guider https://github.com/raspiblitz/raspiblitz#feature-documentation