---
name: RoninDojo v2
description: Installere din RoninDojo v2 Bitcoin-node på en Raspberry Pi
---
![cover RoninDojo v2](assets/cover.webp)

***ADVARSEL:** Etter arrestasjonen av grunnleggerne av Samourai Wallet og beslagleggelsen av deres servere den 24. april, er visse funksjoner i RoninDojo, som Whirlpool, ikke lenger operative. Det er imidlertid mulig at disse verktøyene kan bli gjeninnført eller relansert på en annen måte i de kommende ukene. I tillegg, siden RoninDojo-koden var hostet på Samourais GitLab, som også ble beslaglagt, er det for øyeblikket ikke mulig å laste ned koden eksternt. RoninDojo-teamene jobber sannsynligvis med å publisere koden på nytt.*

_Vi følger nøye med på utviklingen av denne saken samt utviklingen angående de tilknyttede verktøyene. Vær trygg på at vi vil oppdatere denne opplæringen så snart ny informasjon blir tilgjengelig._

_Denne opplæringen er gitt kun for utdannings- og informasjonsformål. Vi støtter eller oppmuntrer ikke bruk av disse verktøyene til kriminelle formål. Det er hver brukers ansvar å overholde lovene i sin jurisdiksjon_

---

> "*Bruk Bitcoin med personvern.*"

I en tidligere opplæring hadde vi allerede forklart prosedyren for å installere og bruke RoninDojo v1. Men, i løpet av det siste året har RoninDojo-teamene lansert versjon 2 av deres implementasjon, som markerte et betydelig vendepunkt i programmets arkitektur. Faktisk, de gikk bort fra Linux Manjaro-distribusjonen til fordel for Debian. Følgelig tilbyr de ikke lenger et forhåndskonfigurert bilde for automatisk installasjon på Raspberry Pi. Men det er fortsatt en metode for å fortsette med en manuell installasjon. Dette er hva jeg brukte for min egen node, og siden da har RoninDojo v2 fungert fantastisk på min Raspberry Pi 4. Jeg tilbyr derfor en ny opplæring om hvordan man manuelt installerer RoninDojo v2 på en Raspberry Pi.

https://planb.network/tutorials/node/bitcoin/ronin-dojo-31d96647-029b-43e8-9fb5-95ec5dde72b0

## Innholdsfortegnelse:
- Hva er RoninDojo?
- Hvilket maskinvare å velge for å installere RoninDojo v2?
- Hvordan montere Raspberry Pi 4?
- Hvordan installere RoninDojo v2 på en Raspberry Pi 4?
- Hvordan bruke din RoninDojo v2-node?

## Hva er RoninDojo?
Dojo er opprinnelig en full Bitcoin-node-implementasjon, basert på Bitcoin Core, og utviklet av Samourai Wallet-teamene. Denne løsningen kan installeres på hvilket som helst utstyr. I motsetning til andre Core-implementasjoner, har Dojo blitt spesifikt optimalisert for å integrere med Android-applikasjonsmiljøet til Samourai Wallet. Når det gjelder RoninDojo, er det et verktøy designet for å lette installasjonen og styringen av en Dojo, samt ulike andre komplementære verktøy. Kort sagt, RoninDojo beriker den grunnleggende implementasjonen av Dojo ved å integrere en mengde tilleggsverktøy, samtidig som den forenkler installasjonen og styringen.

Ronin tilbyr også [en node-i-boks-løsning, kalt "*Tanto*"](https://ronindojo.io/en/products), en enhet med RoninDojo allerede installert på et system sammensatt av deres team. Tanto er et betalt alternativ, som kan være interessant for de som foretrekker å unngå tekniske komplikasjoner. Men siden kildekoden til RoninDojo er åpen, er det også mulig å distribuere den på din egen maskinvare. Dette alternativet, som er mer økonomisk, krever likevel noen ekstra manipulasjoner, som vi vil dekke i denne opplæringen.
RoninDojo er et Dojo, og dermed muliggjør det enkel integrasjon av Whirlpool CLI i din Bitcoin-node for å tilby den beste mulige coinjoin-opplevelsen. Med Whirlpool CLI blir det mulig å kontinuerlig remixe dine bitcoins, 24 timer i døgnet, 7 dager i uken, uten at din personlige datamaskin trenger å være på.

Utover Whirlpool CLI, inkluderer RoninDojo en rekke verktøy for å forbedre din Dojos funksjonaliteter. Blant disse analyserer Boltzmann-kalkulatoren personvernnivået til transaksjonene dine, Electrum-serveren tillater tilkobling av dine Bitcoin-lommebøker til din node, og Mempool-serveren gjør det mulig for deg å se transaksjonene dine lokalt, uten å lekke informasjon.

Sammenlignet med andre node-løsninger som Umbrel, er RoninDojo tydelig fokusert på on-chain løsninger og personvernverktøy. I motsetning til Umbrel, støtter ikke RoninDojo oppsett av en Lightning-node eller integrasjon av mer generalistiske serverapplikasjoner. Selv om RoninDojo tilbyr færre allsidige verktøy enn Umbrel, har det alle de essensielle funksjonalitetene for å håndtere din on-chain aktivitet.

Hvis du ikke trenger generalistiske funksjonaliteter eller de relatert til Lightning Network som tilbys av Umbrel, og du ser etter en enkel, stabil node med essensielle verktøy som Whirlpool eller Mempool, kunne RoninDojo være den ideelle løsningen. Mens Umbrel tenderer til å bli en mini multitasking-server orientert mot Lightning Network og allsidighet, fokuserer RoninDojo, i tråd med filosofien til Samourai Wallet, på grunnleggende verktøy for brukerens personvern.

Nå som vi har skissert RoninDojo, la oss se sammen hvordan man setter opp denne noden.

## Hvilket maskinvare å velge for å installere RoninDojo v2?
RoninDojo tilbyr et bilde for automatisk installasjon av programvaren på en [RockPro64](https://ronindojo.io/en/download). Imidlertid fokuserer vår veiledning på den manuelle installasjonsprosedyren på en Raspberry Pi 4. Selv om Raspberry Pi 5 nylig har blitt lansert, og denne veiledningen teoretisk sett skulle være kompatibel med denne nye modellen, har jeg ennå ikke hatt sjansen til å teste den personlig, og jeg har ikke funnet tilbakemeldinger fra samfunnet. Så snart jeg skaffer Pi 5 og kompatible komponenter, vil jeg oppdatere denne veiledningen for å holde deg informert. I mellomtiden anbefaler jeg å prioritere Pi 4, da den fungerer perfekt for min node.
For min del kjører jeg RoninDojo på en Raspberry Pi utstyrt med 8 GB RAM. Selv om noen medlemmer av samfunnet har klart å få det til å fungere på enheter med bare 4 GB RAM, har jeg ikke testet denne konfigurasjonen selv. Gitt den lille prisforskjellen, virker det klokt å velge 8 GB RAM-versjonen. Dette kan også vise seg nyttig hvis du planlegger å bruke din Raspberry Pi til andre formål i fremtiden.
Det er viktig å merke seg at RoninDojo-teamene har rapportert om hyppige problemer relatert til kabinettet og SSD-adapteren. Jeg har møtt disse problemene selv. **Derfor anbefales det sterkt å unngå kabinetter utstyrt med en USB-kabel for din nodes SSD.** Foretrekk heller et lagringsutvidelseskort spesifikt designet for din Raspberry Pi:

![lagringsutvidelseskort RPI4](assets/notext/1.webp)
For å lagre Bitcoin-blockchainen, trenger du en SSD som er kompatibel med lagringsutvidelseskortet du har valgt. For øyeblikket (februar 2024) er vi i en overgangsfase. Det forventes at om noen måneder vil ikke 1 TB-disker lenger være tilstrekkelige for å inneholde den voksende størrelsen på blockchainen, spesielt med tanke på de ulike applikasjonene du planlegger å integrere i noden din. Noen anbefaler derfor å investere i en 2 TB SSD for å ha ro i sinnet på lang sikt. Imidlertid, med den nedadgående trenden i SSD-priser år etter år, foreslår andre å nøye seg med en 1 TB-disk, som burde være tilstrekkelig for ett eller to år, og argumenterer med at når den blir foreldet, vil kostnaden for 2 TB-modeller sannsynligvis ha redusert. Valget avhenger derfor av dine personlige preferanser. Hvis du planlegger å beholde din RoninDojo for en betydelig varighet og ønsker å unngå teknisk håndtering i de kommende årene, ser alternativet med en 2 TB SSD ut til å være det mest forsiktige, da det gir deg en komfortabel margin for fremtiden.
I tillegg trenger du ulike småkomponenter:
- Et kabinett utstyrt med en vifte for å huse din Raspberry Pi og ditt lagringsutvidelseskort. Sett som inkluderer både SSD-utvidelseskortet og et kompatibelt kabinett er tilgjengelige på nettet;
- En strømkabel til din Raspberry Pi;
- Et micro SD-kort på minst 16 GB (selv om 8 GB teknisk sett kunne være tilstrekkelig, er prisforskjellen mellom 8 og 16 GB-kort ofte ubetydelig);
- En RJ45 Ethernet-kabel for nettverkstilkobling.

![node material](assets/notext/2.webp)

## Hvordan montere Raspberry Pi 4?
Monteringen av noden din vil variere avhengig av det valgte maskinvaren, spesielt typen kabinett. Imidlertid er den generelle oversikten over trinnene å følge generelt lik i monteringen.
Start med å installere SSD-en din på lagringsutvidelseskortet, og pass på å sikre de to låseskruene på baksiden.

![assembly1](assets/notext/3.webp)

Deretter fester du din Raspberry Pi til utvidelseskortet.

![assembly2](assets/notext/4.webp)

Fest også viften til Raspberry Pi.

![assembly3](assets/notext/5.webp)

Koble til de ulike komponentene, og pass på å bruke de riktige pinnene, med henvisning til manualen for kabinettet ditt. Kabinettprodusenter tilbyr ofte videotutorials for å hjelpe deg med monteringen. I mitt tilfelle har jeg et ekstra utvidelseskort utstyrt med en av/på-knapp. Dette er ikke essensielt for å lage en Bitcoin-node. Jeg bruker det hovedsakelig for å ha en strømbryter.

Hvis du, som meg, har et utvidelseskort utstyrt med en av/på-knapp, glem ikke å installere den lille "Auto Power On"-jumperen. Dette vil tillate noden din å starte automatisk så snart den får strøm. Denne funksjonen er spesielt nyttig i tilfelle strømbrudd, da den lar noden din starte på nytt av seg selv, uten manuell intervensjon fra din side.

![assembly4](assets/notext/6.webp)

Før du setter inn all maskinvaren i kabinettet, er det viktig å sjekke at din Raspberry Pi, lagringsutvidelseskortet, og viften fungerer ordentlig ved å slå dem på.

![assembly5](assets/notext/7.webp)
Til slutt, installer din Raspberry Pi i dens kabinett. Vær oppmerksom på at et senere steg vil kreve at du legger til micro SD-kortet i den tilsvarende porten på Raspberry Pi. Hvis kabinettet ditt er utstyrt med en åpning som lar deg sette inn SD-kortet uten å måtte åpne det (som er tilfellet med mitt illustrert på bildet), kan du fortsette å lukke kabinettet nå. Men, hvis kabinettet ditt ikke har direkte tilgang til micro SD-porten, må du vente til du har forberedt micro SD-kortet for å sette det inn før du fullfører monteringen.
![assembly6](assets/notext/8.webp)

## Hvordan installere RoninDojo v2 på en Raspberry Pi 4?

### Steg 1: Forbered det oppstartbare micro SD-kortet
Etter å ha montert maskinvaren din, er neste steg å installere RoninDojo. For dette vil vi forberede et oppstartbart micro SD-kort fra datamaskinen din, ved å brenne det passende diskbildet på det.
Du må bruke _**Raspberry Pi Imager**_-programvaren, designet for å lette nedlasting, konfigurering og skriving av operativsystemer på et micro SD-kort for bruk med en Raspberry Pi. Start med å installere denne programvaren på din personlige PC:
- For Ubuntu/Debian: https://downloads.raspberrypi.org/imager/imager_latest_amd64.deb
- For Windows: https://downloads.raspberrypi.org/imager/imager_latest.exe
- For Mac: https://downloads.raspberrypi.org/imager/imager_latest.dmg

Når programvaren er installert, åpne den, og sett inn ditt micro SD-kort i din personlige datamaskin. Fra Raspberry Pi Imager-grensesnittet, velg `CHOOSE OS`:

![choose OS](assets/notext/9.webp)

Deretter, gå til `Raspberry Pi OS (other)`-menyen:

![choose OS others](assets/notext/10.webp)

Velg operativsystemet som heter `Raspberry Pi OS (Legacy, 64-bit) Lite`, som er `0.3 GB` i størrelse:

![choose OS Legacy Lite](assets/notext/11.webp)

Etter å ha valgt operativsystemet, vil du bli omdirigert til hovedmenyen til Raspberry Pi Imager. Klikk på `CHOOSE STORAGE`:

![choose storage](assets/notext/12.webp)

Velg ditt micro SD-kort:

![choose micro sd](assets/notext/13.webp)

Etter å ha valgt operativsystemet og micro SD-kortet, klikk på `NEXT`:

![choose next](assets/notext/14.webp)

Et nytt vindu vil dukke opp. Velg `EDIT CONFIGURATION`:

![edit settings](assets/notext/15.webp)

I dette vinduet, gå til `GENERAL`-fanen og gjør følgende innstillinger (som er veldig viktige for at det skal fungere):
- Aktiver alternativet og tildel `RoninDojo` som vertsnavn;
- Aktiver `Set username and password`, skriv inn `pi` som brukernavn, velg et passord, og noter denne informasjonen, da den vil være nødvendig senere. Disse legitimasjonene er midlertidige og vil bli slettet etterpå;
- Deaktiver `Configure Wi-Fi`;
- Aktiver `Set locale settings` og velg din tidssone samt tastaturtypen som tilsvarer datamaskinen din;

![general settings](assets/notext/16.webp)

I SERVICES-fanen, klikk på `Enable SSH`-boksen og velg `Use a password for authentication`:

![services settings](assets/notext/17.webp)

Sørg også for at i `OPTIONS`-fanen, telemetri er deaktivert:

![options settings](assets/notext/18.webp)

Klikk på `SAVE`:
![innstillinger lagre](assets/notext/19.webp)Bekreft ved å klikke på `YES` for å starte opprettelsen av det bootbare micro SD-kortet:
![innstillinger ja](assets/notext/20.webp)

En melding vil informere deg om at alle data på micro SD-kortet vil bli slettet. Bekreft ved å klikke på `YES` for å starte prosessen:

![overskrive micro SD](assets/notext/21.webp)

Vent til programvaren er ferdig med å forberede ditt micro SD-kort:

![skriver micro SD](assets/notext/22.webp)

Når meldingen som indikerer slutten av prosessen vises, kan du fjerne micro SD-kortet fra datamaskinen din:

![skriving micro SD fullført](assets/notext/23.webp)

### Steg 2: Fullfør Node-monteringen
Du kan nå sette inn micro SD-kortet i den tilsvarende porten på din Raspberry Pi.

![micro SD](assets/notext/24.webp)

Deretter kobler du din Raspberry Pi til ruteren din ved hjelp av Ethernet-kabelen. Til slutt, slå på noden din ved å koble til strømkabelen og trykke på strømknappen (hvis oppsettet ditt inkluderer en).

### Steg 3: Opprett en SSH-forbindelse med Noden
Først er det nødvendig å finne IP-adressen til noden din. Du har muligheten til å bruke et verktøy som _[Advanced IP Scanner](https://www.advanced-ip-scanner.com/)_ eller _[Angry IP Scanner](https://angryip.org/)_, eller sjekke administrasjonsgrensesnittet til ruteren din. IP-adressen skal være i formen `192.168.1.??`. **For alle følgende kommandoer, erstatt `[IP]` med den faktiske IP-adressen til noden din**, (fjern klammene).

Start en terminal.

For å fjerne en mulig nøkkel allerede assosiert med IP-adressen til noden din, utfør kommandoen: 
`ssh-keygen -R [IP]`. 

En feil etter denne kommandoen er ikke alvorlig; det betyr ganske enkelt at nøkkelen ikke eksisterer i listen din over kjente verter (som er ganske sannsynlig). For eksempel, hvis IP-en til noden din er `192.168.1.40`, blir kommandoen: `ssh-keygen -R 192.168.1.40`.

Deretter, opprett en SSH-forbindelse med noden din ved å utføre kommandoen: 
`ssh pi@[IP]`.
En melding vil dukke opp angående vertens autentisitet: `The authenticity of host '[IP]' can't be established.` Dette indikerer at autentisiteten til enheten du prøver å koble til ikke kan verifiseres på grunn av mangel på en kjent offentlig nøkkel. Når du kobler til via SSH til en ny vert for første gang, vil denne meldingen alltid dukke opp. Du må svare `yes` for å legge til dens offentlige nøkkel i din lokale katalog, noe som vil forhindre at denne advarselsmeldingen vises under fremtidige SSH-forbindelser til denne noden. Derfor, skriv `yes` og trykk `enter` for å validere.
Du vil deretter bli bedt om å angi passordet ditt, det som tidligere ble satt som midlertidig i steg 1. Valider med `enter`. Du vil da være koblet til noden din via SSH.

Oppsummert, her er kommandoene å utføre:
- `ssh-keygen -R [IP]`
- `ssh pi@[IP]`
- `yes`
- Skriv inn det midlertidige passordet og valider.

### Steg 4: Oppdatering og Forberedelse
Du er nå koblet til noden din via en SSH-økt. På terminalen din, skal kommandoprompten være: `pi@RoninDojo:~ $`. For å starte, oppdater listen over tilgjengelige pakker og installer oppdateringer for eksisterende pakker med følgende kommando:
`sudo apt update && sudo apt upgrade -y`
Når oppdateringene er fullførte, fortsett med å installere *Git* og *Dialog* ved hjelp av kommandoen: `sudo apt install git dialog -y`

Deretter, klone `master`-grenen av _RoninOS_ Git-repositoriet ved å utføre:
`sudo git clone --branch master https://code.samourai.io/ronindojo/RoninOS.git /opt/RoninOS`

Kjør skriptet `customize-image.sh` med kommandoen:
`cd /opt/RoninOS/ && sudo ./customize-image.sh`

**Det er viktig å la skriptet kjøre uten avbrytelser og vente tålmodig på slutten av prosessen**, som tar omtrent 10 minutter. Når meldingen `Setup is complete` vises, kan du gå videre til neste steg.

### Steg 5: Lansering av RoninOS
Start RoninOS med kommandoen:
`sudo systemctl start ronin-setup`

Vis linjene i loggfilen med kommandoen:
`tail -f /home/ronindojo/.logs/setup.logs`

På dette stadiet, **er det viktig å la RoninOS starte og vente på at den** er ferdig med å kjøre. Dette tar omtrent 40 minutter. Når `All RoninDojo feature installations complete!` vises, kan du gå videre til steg 6.

### Steg 6: Tilgang til RoninUI og Endring av Påloggingsinformasjon
Etter at installasjonen er fullført, for å koble til noden din via en nettleser, sørg for at din personlige datamaskin er koblet til samme lokale nettverk som noden din. Hvis du bruker en VPN på maskinen din, deaktiver den midlertidig. For å få tilgang til nodens grensesnitt i nettleseren din, skriv inn i URL-feltet:
- Direkte IP-adressen til noden din, for eksempel, `192.168.1.??`;
- Eller, skriv `ronindojo.local`.

Når du er på RoninUI-hjemmesiden, vil du bli bedt om å starte oppsettet. For å gjøre dette, klikk på `Let's start`-knappen.

![lets start](assets/notext/25.webp)

På dette stadiet presenterer RoninUI deg med ditt `root`-passord. Det er essensielt å holde dette sikkert. Du kan velge en fysisk sikkerhetskopi, på papir, eller lagre det i en [passordbehandler](https://planb.network/courses/secu101/4/2).

![root password](assets/notext/26.webp)

Etter å ha lagret `root`-passordet, merk av for `I have backed up Root user credentials` og klikk på `Continue` for å fortsette.

![confirm root password](assets/notext/27.webp)

Neste steg involverer å opprette et brukerpassord, som vil bli brukt både for å få tilgang til RoninUI-webgrensesnittet og for å etablere SSH-økter med noden din. Velg et sterkt passord og sørg for å lagre det sikkert. Du må skrive inn dette passordet to ganger før du klikker på `Finish` for å validere. Når det gjelder brukernavnet, anbefales det å beholde standardvalget, `ronindojo`. Hvis du bestemmer deg for å endre det, husk å justere kommandoene i de følgende stegene tilsvarende.

![user credentials](assets/notext/28.webp)

Når disse handlingene er fullført, vent på at noden din skal initialiseres. Du vil da få tilgang til RoninUI-webgrensesnittet. Du er nesten ved slutten av prosessen, bare noen få små steg igjen!
![Ronin UI](assets/notext/29.webp)

### Steg 7: Fjern Midlertidige Påloggingsinformasjon
Åpne en ny terminal på din personlige datamaskin og etabler en SSH-forbindelse med noden din ved hjelp av følgende kommando:
`SSH ronindojo@[IP]`
Hvis for eksempel IP-adressen til noden din er `192.168.1.40`, vil den passende kommandoen være: `SSH ronindojo@192.168.1.40`

Hvis du endret brukernavnet ditt i det forrige trinnet, ved å erstatte standard brukernavn (`ronindojo`) med et annet, sørg for å bruke dette nye navnet i kommandoen. For eksempel, hvis du valgte `planb` som brukernavn og IP-adressen er `192.168.1.40`, vil kommandoen du skal skrive inn være:
`SSH planb@192.168.1.40`
Du vil bli bedt om å skrive inn brukerpassordet. Skriv det inn og trykk deretter `enter` for å validere. Du vil da få tilgang til RoninCLI-grensesnittet. Bruk piltastene på tastaturet ditt for å navigere til `Exit RoninDojo`-alternativet og trykk `enter` for å velge det.
![RoninCLI](assets/notext/30.webp)

På dette tidspunktet er du på terminalen til noden din, med en kommandoprompt lik: `ronindojo@RoninDojo:~ $`. For å fjerne den midlertidige brukeren som ble opprettet under konfigurasjonen av det oppstartbare micro SD-kortet, skriv inn følgende kommando og trykk `enter`:
`sudo deluser --remove-home pi`

Du vil bli bedt om å bekrefte brukerpassordet ditt. Skriv det inn og valider ved å trykke `enter`. Vent på at operasjonen skal fullføres, deretter bruk `exit`-kommandoen for å forlate terminalen.

Gratulerer! Din RoninDojo v2 node er nå konfigurert og klar til bruk. Den vil begynne sin IBD (*Initial Block Download*), fortsette med å laste ned og verifisere Bitcoin blockchain fra Genesis-blokken. Dette trinnet innebærer å hente alle Bitcoin-transaksjoner gjort siden 3. januar 2009, og tar litt tid. Når blockchain er fullstendig nedlastet, vil indekseren fortsette med å komprimere databasen. Varigheten av IBD kan variere betydelig. Din RoninDojo node vil være fullt operativ når denne prosessen er fullført.

**Hvis du migrerer fra en gammel RoninDojo v1 node** til denne nye versjonen med denne veiledningen samtidig som du beholder den samme SSD-en, bør noden din automatisk oppdage og gjenbruke de eksisterende dataene på disken, og spare deg for nødvendigheten av å utføre IBD igjen. I dette tilfellet trenger du bare å vente på at noden din resynkroniseres med de siste blokkene.

### Trinn 8: "veth* fix"
Hvis du støter på en feil med din RoninDojo v2 på Raspberry Pi, hvor etter en problemfri installasjon, blir noden din plutselig utilgjengelig via SSH men gjenopprettes etter en enkel omstart, da må du følge dette trinn 8. Denne vanlige feilen kan enkelt fikses med en løsning utviklet av fellesskapet: "_veth fix_". Denne mindre korreksjonen retter permanent de brå frakoblingene. Slik bruker du den.

Åpne en ny terminal på din personlige datamaskin og opprett en SSH-forbindelse med noden din ved å bruke følgende kommando:
`SSH ronindojo@[IP]`

Hvis for eksempel IP-adressen til noden din er `192.168.1.40`, ville den passende kommandoen være:
`SSH ronindojo@192.168.1.40`

Du vil bli bedt om å skrive inn brukerpassordet. Skriv det inn og trykk `enter` for å validere. Du vil da få tilgang til RoninCLI-grensesnittet. Bruk piltastene på tastaturet ditt for å navigere til `Exit RoninDojo`-alternativet og trykk `enter` for å velge det.
På dette tidspunktet er du på terminalen til noden din, med en kommandoprompt som ligner på: `ronindojo@RoninDojo:~ $`. For å anvende veth*-fiksen, skriv inn følgende kommando og trykk `enter`: `sudo nano /etc/dhcpcd.conf`

Bekreft passordet ditt igjen og trykk `enter`.

Du vil komme til `dhcpcd.conf`-filen. Du må kopiere følgende tekst, sørge for å inkludere asterisken, og legge den til nederst i filen: 
`denyinterfaces veth*`

For å gjøre dette, flytt til bunnen av filen ved å bruke pil ned på tastaturet, deretter bruk høyreklikk på musen for å lime inn teksten på en uavhengig linje.

Etter å ha lagt til teksten, trykk `ctrl X` for å starte avslutningen, etterfulgt av `ctrl Y` for å bekrefte lagring av endringene, og trykk `enter` for å fullføre og returnere til kommandoprompten. For å sikre at modifikasjonen har blitt korrekt anvendt, gjenåpne `dhcpcd.conf`-filen ved å bruke den passende kommandoen.

For å fullføre anvendelsen av fiksen, start noden din på nytt ved å utføre: 
`sudo reboot now`

På dette tidspunktet kan du lukke terminalen din. Tillat nødvendig tid for at din RoninDojo skal starte på nytt, hvoretter du bør kunne koble til igjen via nettleserens grafiske grensesnitt. Denne prosessen bør fikse den oppståtte feilen.

## Hvordan bruke din RoninDojo v2 node?

### Koble din lommebokprogramvare til Electrs
Den første bruken av din nylig installerte og synkroniserte node vil være å kringkaste dine transaksjoner til Bitcoin-nettverket. Du vil sannsynligvis ønske å koble dine ulike lommebøker til noden din for å kringkaste dine transaksjoner konfidensielt. Dette kan du gjøre gjennom Electrum Rust Server (electrs). Denne applikasjonen er vanligvis forhåndsinstallert på din RoninDojo-node. Hvis ikke, kan du manuelt installere den via RoninCLI-grensesnittet i `Applications > Manage Applications > Install Electrum Server`.

For å få Tor-adressen til din Electrum Server, fra RoninUI-webgrensesnittet, gå til:
`Pairing > Electrum server > Pair now`
![Pairing](assets/notext/31.webp)
![Electrs](assets/notext/32.webp)
Du må deretter skrive inn `Hostname`-adressen som slutter på `.onion` i din lommebokprogramvare, ledsaget av port `50001`. ![hostname](assets/notext/33.webp)
For eksempel, på Sparrow Wallet, gå bare til fanen:
`File > Preferences > Server > Private Electrum`

![Sparrow](assets/notext/34.webp)

### Koble din lommebokprogramvare til Samourai Dojo
Som et alternativ til å bruke Electrs, lar Dojo deg koble din kompatible programvarelommebok direkte til din RoninDojo-node. Lommebøker som Samourai Wallet og Sentinel tilbyr denne funksjonaliteten.

For å etablere forbindelsen, trenger du bare å skanne QR-koden til din Dojo. For å få tilgang til denne QR-koden via RoninUI, naviger til:
`Pairing > Samourai Dojo > Pair now`
![Samourai Dojo](assets/notext/35.webp)
For å koble din Samourai Wallet til din Dojo, skann denne QR-koden under appinstallasjonen:

![Samourai Wallet connection](assets/notext/36.webp)
Hvis du allerede hadde en Samourai Wallet før du satte opp din Ronin Dojo, er det nødvendig å sikkerhetskopiere lommeboken din, avinstallere og deretter installere Samourai Wallet-appen på nytt, før du gjenoppretter lommeboken din. Når du starter den reinstallerte appen, vil du ha muligheten til å koble til en ny Dojo. **Vær forsiktig, denne prosessen innebærer risikoen for å miste dine bitcoins hvis den ikke utføres korrekt!** Sørg for at du har sikkerhetskopi av din Samourai-lommebok i dine filer og verifiser gyldigheten av din passfrase via `Innstillinger > Feilsøk > Passfrase`. Det er også viktig å ha en lesbar sikkerhetskopi av din gjenopprettingsfrase og din passfrase. For mer presisjon i denne operasjonen, anbefales det å følge denne detaljerte opplæringen: [https://wiki.ronindojo.io/en/setup/v2_0_0-upgrade/reconnectsamourai](https://wiki.ronindojo.io/en/setup/v2_0_0-upgrade/reconnectsamourai).
### Bruke din egen Mempool.space blokkutforsker
En blokkutforsker transformerer råinformasjonen fra Bitcoin-blockchainen til et strukturert og lett leselig format. Med verktøy som *Mempool.space*, er det mulig å analysere transaksjoner, søke etter spesifikke adresser, eller til og med konsultere gjennomsnittlige gebyrrater for nettverkets mempooler i sanntid.

Men, å bruke online blokkutforskere utgjør risikoer for ditt personvern og innebærer tillit til dataene som tilbys av tredjeparter. Ved å bruke disse tjenestene uten å gå gjennom din egen node, kan du utilsiktet avsløre informasjon om dine transaksjoner og må stole på nøyaktigheten av informasjonen presentert av nettstedseieren.
For å redusere disse risikoene, anbefales det å bruke din egen instans av *Mempool.space* via Tor-nettverket, direkte hostet på din node. Denne løsningen sikrer bevaring av ditt personvern og autonomi av dine data.
For å gjøre dette, start med å installere *Mempool Space Visualizer* fra RoninUI. På webgrensesnittet, gå til `Dashboard`-fanen og klikk på `Manage` under `Mempool Space`:
`Dashboard > Mempool Space > Manage`
![Administrer mempool](assets/notext/37.webp)
Deretter klikker du på `Installer Mempool visualizer`-knappen:
![installer mempool](assets/notext/38.webp)
Bekreft ditt brukerpassord:
![passord mempool](assets/notext/39.webp)
Vent til installasjonen er fullført, og klikk deretter igjen på `Manage`-knappen:
![Mempool Administrer](assets/notext/40.webp)
Du vil få en `.onion`-lenke for å få tilgang til din egen instans av *Mempool.space* via Tor-nettverket.
![Mempool lenke](assets/notext/41.webp)
Jeg råder deg til å lagre denne lenken i dine favoritter på Tor-nettleseren eller legge den til i Tor Browser-appen på din smarttelefon for enkel og sikker tilgang fra hvor som helst. Hvis du ikke allerede har Tor-nettleseren, kan du laste den ned her: [https://www.torproject.org/download/](https://www.torproject.org/download/)
![Mempool Tor](assets/notext/42.webp)

### Bruke Whirlpool for å blande dine bitcoins
Din RoninDojo-node integrerer også _WhirlpoolCLI_, et kommandolinjegrensesnitt som muliggjør automatisering av Whirlpool coinjoins, og _WhirlpoolGUI_, et grafisk grensesnitt designet for å samhandle med _WhirlpoolCLI_.
Å utføre en coinjoin via Whirlpool krever at applikasjonen som brukes er aktiv for å gjennomføre remixes. Denne betingelsen kan være begrensende for de som ønsker å oppnå høye nivåer av anonsets. Faktisk må enheten som hoster applikasjonen som integrerer Whirlpool, forbli på kontinuerlig. Dette betyr at for å delta i remixes 24 timer i døgnet, må datamaskinen eller smarttelefonen din forbli påslått med Samourai eller Sparrow åpen kontinuerlig. En løsning på denne begrensningen er å bruke _WhirlpoolCLI_ på en maskin som alltid er på, som en Bitcoin node, noe som lar myntene dine remixe uten avbrudd, og uten behovet for å holde en annen enhet påslått.
En detaljert opplæring er under forberedelse for å veilede deg trinn for trinn gjennom prosessen med å coinjoine med Samourai Wallet og RoninDojo v2, fra A til Å.

For en dypere forståelse av coinjoin og bruken av det på Bitcoin, inviterer jeg deg også til å konsultere denne andre artikkelen: Forståelse og bruk av coinjoin på Bitcoin, hvor jeg detaljerer alt du trenger å vite om denne teknikken.

https://planb.network/tutorials/privacy/on-chain/coinjoin-dojo-c4b20263-5b30-4c74-ae59-dc8d0f8715c2
### Bruke Whirlpool Stat Tool (WST)

Etter å ha utført coinjoins med Whirlpool, er det nyttig å nøyaktig evaluere personvernnivået oppnådd for dine blandede UTXOs. For å gjøre dette, kan du bruke Python-verktøyet *Whirlpool Stat Tool*. Dette verktøyet lar deg måle både de prospektive og retrospektive poengene til dine UTXOs, samtidig som du analyserer deres diffusjonsrate i bassenget.

For å fordype din forståelse av beregningsmekanismene til disse anonsets, anbefaler jeg å lese artikkelen: REMIX - WHIRLPOOL, som detaljerer funksjonen til disse indeksene.

https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

For å få tilgang til WST-verktøyet, gå til RoninCLI. For å gjøre dette, åpne en terminal på din personlige datamaskin og etabler en SSH-forbindelse med noden din ved å bruke følgende kommando:
`SSH ronindojo@[IP]`

Hvis, for eksempel, IP-adressen til noden din er `192.168.1.40`, ville den passende kommandoen være:
`SSH ronindojo@192.168.1.40`

Hvis du endret brukernavnet ditt under trinn 6, ved å erstatte standardbrukernavnet (`ronindojo`) med et annet, sørg for å bruke dette nye navnet i kommandoen. For eksempel, hvis du valgte `planb` som ditt brukernavn og IP-adressen er `192.168.1.40`, ville kommandoen du skal angi være:
`SSH planb@192.168.1.40`

Du vil bli bedt om å angi brukerpassordet. Skriv det inn og trykk `enter` for å validere. Du vil da få tilgang til RoninCLI-grensesnittet. Bruk piltastene på tastaturet ditt for å navigere til `Samourai Toolkit`-menyen og trykk `enter` for å velge den:

![Samourai Toolkit](assets/notext/43.webp)

Deretter velger du `Whirlpool Stat Tool`:

![WST](assets/notext/44.webp)

Ved initialisering av WST, vil verktøyet fortsette med sin automatiske installasjon. Vent under dette trinnet. Bruksanvisningene vil rulle gjennom. Når installasjonen er fullført, trykk på en hvilken som helst tast for å få tilgang til WST-terminalen:

![WST kommandoer](assets/notext/45.webp)

Følgende kommandoprompt vil bli vist:
`wst#/tmp>`

Hvis du ønsker å avslutte dette grensesnittet og returnere til RoninCLI-menyen, skriv inn:
`quit`

Først er det nødvendig å konfigurere proxyen for å bruke Tor, for å sikre konfidensialitet når du henter data fra OXT. Skriv inn kommandoen:
`socks5 127.0.0.1:9050`
Deretter fortsett med å laste ned bassenginformasjonen som inneholder transaksjonen din:
`download 0001`
Erstatt `0001` med denominasjonskoden for bassenget du er interessert i. Denominasjonskodene er som følger på WST:
- Basseng 0.5 bitcoins: `05`
- Basseng 0.05 bitcoins: `005`
- Basseng 0.01 bitcoins: `001`
- Basseng 0.001 bitcoins: `0001`

Etter nedlastingen, last inn dataene ved å erstatte `0001` med koden for ditt basseng i denne kommandoen: `load 0001`

![WST lasting](assets/notext/46.webp)

Vent til lasting er fullført, noe som kan ta noen minutter. Når dataene er lastet, for å vite anonset-poengene for mynten din, utfør kommandoen `score` etterfulgt av din TXID (uten klammene):
`score [TXID]`

![WST score](assets/notext/47.webp)

WST vil deretter vise den retrospektive poengsummen (_Tilbakeblikkende metrikker_), etterfulgt av den prospektive poengsummen (_Fremtidsrettede metrikker_). I tillegg til anonset-poengene, vil WST også indikere diffusjonsraten for transaksjonen din innenfor bassenget, relativt til dens anonset.

**Det er viktig å merke seg at den prospektive poengsummen for mynten din bør beregnes fra TXID-en til din første miks, og ikke fra din nyeste miks. På den andre siden, beregnes den retrospektive poengsummen for en UTXO fra TXID-en til den siste syklusen.**

### Bruk av Boltzmann-kalkulatoren
Boltzmann-kalkulatoren er et verktøy for å analysere en Bitcoin-transaksjon, som tilbyr muligheten til å måle nivået av entropi blant andre avanserte metrikker. Disse dataene gir en kvantifisert vurdering av personvernet til en transaksjon og hjelper med å identifisere potensielle feil. Dette verktøyet er allerede integrert i din RoninDojo-node, noe som gjør det enkelt å få tilgang til og bruke.

Før vi går i detalj om prosedyren for å bruke Boltzmann-kalkulatoren, er det viktig å forstå betydningen av disse indikatorene, deres beregningsmetode og deres nytte. Selv om de er anvendelige på enhver Bitcoin-transaksjon, er disse indikatorene spesielt nyttige for å vurdere kvaliteten på en coinjoin-transaksjon.

**Den første indikatoren** som programvaren beregner er det totale antallet mulige kombinasjoner, indikert under `nb combinations` i verktøyet. Basert på verdiene til de involverte UTXOene, kvantifiserer denne indikatoren antall måter innganger kan assosieres med utganger på. Med andre ord, den bestemmer antallet plausible tolkninger en transaksjon kan generere. For eksempel, en coinjoin strukturert i henhold til Whirlpool 5x5-modellen presenterer `1496` mulige kombinasjoner:
![kombinasjoner](assets/notext/50.webp)
Kreditt: KYCP

**Den andre indikatoren** som beregnes er entropien til en transaksjon, betegnet ved `Entropy`. Når en transaksjon har et høyt antall mulige kombinasjoner, er det ofte mer relevant å referere til dens entropi. Dette er definert som den binære logaritmen av antallet mulige kombinasjoner. Her er formelen som brukes:
- $E$: entropien til transaksjonen;
- $C$: antallet mulige kombinasjoner for transaksjonen.
$$E = \log_2(C)$$
I matematikk tilsvarer den binære logaritmen (logaritme med base 2) den inverse operasjonen av å opphøye 2 til en potens. Med andre ord er den binære logaritmen til $x$ eksponenten som 2 må opphøyes til for å oppnå $x$. Derfor uttrykkes denne indikatoren i bits. La oss ta eksemplet med å beregne entropien for en coinjoin-transaksjon strukturert i henhold til Whirlpool 5x5-modellen, som, som nevnt tidligere, tilbyr et antall mulige kombinasjoner på `1496`:$$ C = 1496 $$
$$ E = \log_2(1496) $$
$$ E \approx 10.5469 \text{ bits}$$

Dermed viser denne coinjoin-transaksjonen en entropi på 10.5469 bits, noe som anses som meget tilfredsstillende. Jo høyere denne verdien er, desto flere forskjellige tolkninger tillater transaksjonen, noe som dermed forbedrer dens personvernivå.

La oss ta et ytterligere eksempel med en mer konvensjonell transaksjon, som har ett inngangspunkt og to utgangspunkter: [1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://mempool.space/en/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce)
I tilfellet med denne transaksjonen er den eneste mulige tolkningen: `(inp 0) > (Outp 0 ; Outp 1)`. Følgelig er dens entropi etablert til `0`:
$$ C = 1 $$
$$ E = \log_2(1) $$
$$ E \approx 0 \text{ bits}$$
**Den tredje indikatoren** som tilbys av Boltzmann-kalkulatoren er kalt `Wallet Efficiency`. Denne indikatoren vurderer transaksjonens effektivitet ved å sammenligne den med den optimale transaksjonen som er tenkelig i et identisk oppsett. Dette fører oss til å diskutere konseptet med maksimal entropi, som tilsvarer den høyeste entropien en spesifikk transaksjonsstruktur teoretisk kan oppnå. Således, for en Whirlpool 5x5 coinjoin-struktur, er maksimal entropi satt til `10.5469`. Transaksjonens effektivitet beregnes deretter ved å konfrontere denne maksimale entropien med den faktiske entropien til den analyserte transaksjonen. Formelen som brukes er som følger:
- $ER$: den faktiske entropien til transaksjonen, uttrykt i bits;
- $EM$: den maksimalt mulige entropien for en gitt transaksjonsstruktur, også i bits;
- $Ef$: effektiviteten til transaksjonen, i bits.
$$Ef = ER - EM$$ $$Ef = 10.5469 - 10.5469$$
$$Ef = 0 \text{ bits}$$

Denne indikatoren uttrykkes også som en prosentandel, dens formel er da:
- $CR$: antall faktiske mulige kombinasjoner;
- $CM$: maksimalt antall mulige kombinasjoner med samme struktur;
- $Ef$: effektiviteten uttrykt som en prosentandel.
$$Ef = \frac{CR}{CM}$$
$$Ef = \frac{1496}{1496}$$
$$Ef = 100\%$$

En effektivitet på `100%` indikerer altså at transaksjonen maksimerer sitt potensial for personvern basert på sin struktur.
**Det fjerde indikatoren**, entropitettheten, eller `Entropy Density`, gir et perspektiv på entropien i forhold til hver inngang eller utgang i transaksjonen. Denne indikatoren viser seg nyttig for å evaluere og sammenligne effektiviteten av transaksjoner av forskjellige størrelser. For å beregne den, deler du ganske enkelt den totale entropien til transaksjonen med det totale antallet innganger og utganger som er involvert. Tar eksemplet med en Whirlpool 5x5 coinjoin:
- $ED$: entropitettheten uttrykt i bits;
- $E$: entropien til transaksjonen uttrykt i bits;
- $T$: det totale antallet innganger og utganger i transaksjonen.
$$T = 5 + 5 = 10$$
$$ED = \frac{E}{T}$$
$$ED = \frac{10.5469}{10}$$
$$ED = 1.054 \text{ bits}$$
**Det femte informasjonsstykket** levert av Boltzmann-kalkulatoren er tabellen over samsvarssannsynligheter mellom innganger og utganger. Denne tabellen indikerer, gjennom `Boltzmann-score`, sannsynligheten for at en spesifikk inngang er koblet til en gitt utgang. Tar eksemplet med en Whirlpool coinjoin, ville sannsynlighetstabellen fremheve sjansene for kobling mellom hver inngang og utgang, og gi et kvantitativt mål på tvetydigheten eller forutsigbarheten av assosiasjoner i transaksjonen:

| %       | Utgang 0 | Utgang 1 | Utgang 2 | Utgang 3 | Utgang 4 |
|---------|----------|----------|----------|----------|----------|
| Inngang 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Inngang 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Inngang 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Inngang 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Inngang 4 | 34%      | 34%      | 34%      | 34%      | 34%      |

Her er det klart at hver inngang har en like stor sjanse for å være assosiert med hvilken som helst utgang, noe som forsterker tvetydigheten og konfidensialiteten til transaksjonen. Imidlertid, i tilfellet med en enkel transaksjon med en inngang og to utganger, er situasjonen annerledes:

| %       | Utgang 0 | Utgang 1 |
|---------|----------|----------|
| Inngang 0 | 100%     | 100%     |

Her ser vi at sannsynligheten for at hver utgang kommer fra inngang 0 er 100%. En lavere sannsynlighet oversetter dermed til større konfidensialitet, ved å fortynne de direkte koblingene mellom innganger og utganger.

**Det sjette informasjonsstykket** som tilbys er antallet deterministiske koblinger, supplert med forholdet mellom disse koblingene. Denne indikatoren avslører hvor mange forbindelser mellom inngangene og utgangene i den analyserte transaksjonen som er udiskutable, med en 100% sannsynlighet. Forholdet gir på sin side et perspektiv på vekten av disse deterministiske koblingene innenfor de totale koblingene i transaksjonen.

For eksempel presenterer en Whirlpool-type coinjoin-transaksjon ingen deterministiske koblinger, og viser derfor en indikator og forhold på 0%. På den annen side, i vår andre undersøkte transaksjon (med en inngang og to utganger), er indikatoren satt til 2 og forholdet når 100%. Således signaliserer en nullindikator utmerket konfidensialitet takket være fraværet av direkte og udiskutable koblinger mellom innganger og utganger.
**Hvordan få tilgang til Boltzmann-kalkulatoren på RoninDojo?** For å få tilgang til *Boltzmann-kalkulatoren*, gå til RoninCLI. For å gjøre dette, åpne en terminal på din personlige datamaskin og opprett en SSH-forbindelse med noden din ved å bruke følgende kommando: `SSH ronindojo@[IP]`

Hvis, for eksempel, nodens IP-adresse er `192.168.1.40`, ville den passende kommandoen være:
`SSH ronindojo@192.168.1.40`

Hvis du endret brukernavnet ditt under trinn 6, ved å erstatte standard brukernavn (`ronindojo`) med et annet, sørg for å bruke dette nye navnet i kommandoen. For eksempel, hvis du valgte `planb` som ditt brukernavn og IP-adressen er `192.168.1.40`, ville kommandoen du skal skrive inn være:
`SSH planb@192.168.1.40`

Du vil bli bedt om å skrive inn brukerpassordet. Skriv det inn og trykk deretter `enter` for å validere. Du vil da få tilgang til RoninCLI-grensesnittet. Bruk pilene på tastaturet ditt for å navigere til `Samourai Toolkit`-menyen og trykk `enter` for å velge den:

![Samourai Toolkit](assets/notext/43.webp)

Velg deretter `Boltzmann-kalkulatoren`:

![boltzmann](assets/notext/49.webp)

Du vil komme til programmets hjemmeside:

![boltzmann hjem](assets/notext/51.webp)

Skriv inn TXID-en for transaksjonen du ønsker å studere og trykk `enter`-tasten:

![boltzmann txid](assets/notext/52.webp)

Kalkulatoren gir deg deretter alle indikatorene vi tidligere har diskutert:

![boltzmann resultat](assets/notext/53.webp)

### Andre funksjoner i din RoninDojo v2
Din RoninDojo-node integrerer ulike andre funksjoner. Spesielt har du muligheten til å skanne spesifikk informasjon for å ta den i betraktning. For eksempel, noen ganger kan din Samourai-lommebok, koblet til RoninDojo, kanskje ikke vise bitcoinsene du faktisk holder. Hvis saldoen indikerer 0 mens du er sikker på å ha bitcoins i denne lommeboken, kan flere grunner forklare denne situasjonen, som en feil i avledningsveiene. Men en av årsakene kan også være at noden din ikke overvåker adressene dine ordentlig. For å løse dette problemet, kan du sørge for at noden din faktisk følger din `xpub` ved å bruke _xpub-verktøyet_. For å få tilgang til dette verktøyet via RoninUI, følg stien:
`Vedlikehold > XPUB-verktøy`

Skriv inn `xpub` som forårsaker problemet og klikk på `Sjekk`-knappen for å verifisere denne informasjonen:
![xpub verktøy](assets/notext/54.webp)
Sørg for at alle transaksjoner er riktig oppført. Det er også viktig å verifisere at avledningstypen som brukes, samsvarer med den i lommeboken din. Hvis dette ikke er tilfellet, klikk på `Skriv på nytt`, og velg deretter fra `BIP44`, `BIP49`, eller `BIP84` etter dine behov.
Utover dette verktøyet, er `Vedlikehold`-fanen i RoninUI full av andre nyttige funksjoner:
- *Transaksjonsverktøy*: Lar deg undersøke detaljene i en gitt transaksjon;
- *Adresseverktøy*: Lar deg bekrefte sporingen av en gitt adresse av din Dojo;
- *Reskanne blokker*: Tvinger noden din til å utføre en ny skanning av et spesifisert blokkområde.

`Push Tx`-fanen er en annen interessant funksjon i RoninUI, som muliggjør kringkasting av en signert transaksjon på Bitcoin-nettverket. Transaksjonen må oppgis i heksadesimal form.
Angående de andre fanene tilgjengelig på ditt RoninUI-dashboard:
- `Apps`: Huser Whirlpool-applikasjonen, og vil sikkert bli brukt til å integrere nye applikasjoner i fremtiden;
- `Logs`: Tilbyr sanntids tilgang til hendelsesloggene for programvaren din;
- `System Info`: Gir generell informasjon om noden din, som CPU-temperatur, bruk av lagringsplass, eller RAM-data. Du vil også finne `Reboot` og `Shut down` alternativene for å starte noden på nytt eller slå den av;
- `Settings`: Lar deg endre ditt brukerpassord.

Der har du det! Takk for at du fulgte denne veiledningen til slutten. Hvis du likte den, oppfordrer jeg deg til å dele den på sosiale medier. Videre, hvis du har muligheten, vurder å støtte utviklerne som gjør disse gratis og åpen kildekode-programvarene tilgjengelige for vårt samfunn med en donasjon: [https://donate.ronindojo.io/](https://donate.ronindojo.io/). For å fordype din kunnskap om RoninDojo og oppdage flere ressurser, anbefaler jeg sterkt å konsultere lenkene til de eksterne ressursene nevnt nedenfor.

**Eksterne ressurser:**
- [https://ronindojo.io/index.html](https://ronindojo.io/index.html)
- [https://wiki.ronindojo.io/en/home](https://wiki.ronindojo.io/en/home)
- [https://gist.github.com/LaurentMT/e758767ca4038ac40aaf](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [https://medium.com/@laurentmt/introducing-boltzmann-85930984a159](https://medium.com/@laurentmt/introducing-boltzmann-85930984a159)
- [https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry](https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry)