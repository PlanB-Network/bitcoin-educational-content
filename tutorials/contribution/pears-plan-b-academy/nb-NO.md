---
name: Plan ₿ Academy - Pears App
description: Hvordan installerer og bruker jeg Plan ₿ Academy-applikasjonen på Pears?
---

![cover](assets/cover.webp)


Du vet sikkert allerede at Plan ₿ Academy er den største utdanningsdatabasen dedikert til Bitcoin, som samler kurs, opplæringsprogrammer og tusenvis av ressurser med åpen kildekode. Opprinnelig var Plan ₿ Academy et nettsted. Men hva ville skje hvis du ikke lenger kunne få tilgang til den på vanlig måte, for eksempel i tilfelle sensur?


I denne opplæringen lærer vi hvordan vi kjører **Plan ₿ Academy**-plattformen på en virkelig sensurresistent måte ved hjelp av **Pears**, en peer-to-peer-teknologi (P2P) utviklet av **Holepunch** og støttet av **Tether**.


Pears er programvaren som gjør det mulig for oss å kjøre Plan ₿ Academy-plattformen uten å være avhengig av et sentralisert nettsted. I denne veiledningen vil vi installere Pears på datamaskinen din for å få tilgang til Plan ₿ Academy gjennom Pears.


Målet med Pears er enkelt: å gjøre det mulig å distribuere og bruke webapplikasjoner uten å være avhengig av noen sentralisert infrastruktur (ingen servere, ingen verter, ingen mellomledd). Med andre ord, selv om en skyleverandør stenger ned eller et land blokkerer et domene, fortsetter applikasjonen å leve blant nettverkets jevnaldrende. Denne tilnærmingen gjør at utdanningsplattformen vår, Plan ₿ Academy, forblir tilgjengelig over hele verden, uten et eneste feilpunkt.


---

**TL;DR:**



- Installer Pears;



- Kjør følgende kommando for å starte Plan ₿ Academy-appen:


```shell
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


---

## 1. Hva er pærer?


Pears er på samme tid et kjøretidsmiljø, et utviklingsverktøy og en distribusjonsplattform for peer-to-peer-applikasjoner. Med dette verktøyet med åpen kildekode kan du bygge, dele og kjøre programvare uten servere eller infrastruktur, direkte mellom brukere. I praksis betyr dette at i stedet for å være vert for en applikasjon på en sentral server, blir hver bruker en node i nettverket: De deler en del av applikasjonen og data med andre likemenn. Hele systemet danner et distribuert nettverk der hver instans samarbeider om å holde tjenesten tilgjengelig.


![Image](assets/fr/01.webp)


Denne tilnærmingen er basert på et sett med modulære programvarekomponenter utviklet av Holepunch:



- Hypercore**: en distribuert logg som sikrer datakonsistens og -sikkerhet uten en sentral database.
- Hyperbee**: en indeks bygget på toppen av Hypercore som gjør det mulig å organisere og søke etter data på en effektiv måte.
- Hyperdrive**: et distribuert filsystem som brukes til å lagre og synkronisere applikasjonsfiler mellom jevnaldrende.
- Hyperswarm** og **HyperDHT**: nettverkslag som gjør det mulig å oppdage motparter og opprette forbindelser over hele verden uten en sentral server.
- Secretstream**: en ende-til-ende-krypteringsprotokoll som sikrer kommunikasjonen mellom motparter.


Ved å kombinere disse komponentene gjør Pears det mulig å lage autonome, krypterte og distribuerte applikasjoner, der hver bruker deltar aktivt i nettverket. Denne desentraliserte arkitekturen eliminerer infrastrukturkostnader, sensurrisiko og SPOF-er (*Single Points of Failure*).


Pears er utviklet av Holepunch, et selskap grunnlagt av Mathias Buus og Paolo Ardoino (CEO i Tether og CTO i Bitfinex), med mål om å utvide peer-to-peer-logikken utover Bitcoin. Deres ambisjon er å bygge "*Internet of peers*", der alle applikasjoner kan operere uten tillatelse, uten servere og uten mellomledd. Holepunch står allerede bak **Keet**, en fullstendig P2P-vennlig videokonferanse- og meldingsapp.


https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b

*Denne installasjonsveiledningen for Pears er delt inn i flere deler avhengig av operativsystemet ditt. Gå direkte til den delen som gjelder for ditt miljø for å følge de riktige instruksjonene:*



- Linux (Debian)** → Seksjon **2**
- Vinduer** → Seksjon **3**
- macOS** → Seksjon **4**


## 2. Hvordan installerer jeg Pears på Linux (Debian)?


Det er relativt enkelt å installere Pears på Debian, men det krever noen forutsetninger, som vi skal gå nærmere inn på i dette avsnittet.


### 2.1. Oppdater systemet


Før noe annet er det viktig å sørge for at systemet ditt er oppdatert.


```bash
sudo apt update && sudo apt upgrade -y
```


![Image](assets/fr/02.webp)


### 2.2. Installer avhengigheter


Pears er avhengig av noen systembiblioteker, inkludert `libatomic1`, som brukes av Bare JavaScript-kjøretidsmotoren. Installer det med følgende kommando:


```bash
sudo apt install -y libatomic1 curl git
```


![Image](assets/fr/03.webp)


### 2.3. Installer Node.js og npm via NVM


Pears distribueres gjennom *npm*, pakkebehandleren for *Node.js*. Selv om Pears ikke er direkte avhengig av *Node.js* for å kjøre, er det nødvendig for installasjonen. Den anbefalte måten å installere *Node.js* på Linux er gjennom *NVM* (*Node Version Manager*), som lar deg administrere flere versjoner av Node side om side.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


![Image](assets/fr/04.webp)


Last deretter inn terminalen på nytt for å aktivere *NVM*:


```bash
source ~/.bashrc
```


![Image](assets/fr/05.webp)


Kontroller at *NVM* er riktig installert:


```bash
nvm --version
```


![Image](assets/fr/06.webp)


Deretter installerer du en stabil versjon av *Node.js* (for eksempel den nåværende LTS-versjonen):


```bash
nvm install --lts
```


![Image](assets/fr/07.webp)


Kontroller at *Node.js* og *npm* er riktig installert:


```bash
node -v
npm -v
```


![Image](assets/fr/08.webp)


### 2.4. Installer Pears med npm


Når *npm* er tilgjengelig, kan du installere Pears CLI globalt på systemet ditt. Dette gjør at du kan kjøre kommandoen `pear` fra hvilken som helst katalog.


```bash
npm install -g pear
```


![Image](assets/fr/09.webp)


### 2.5. Initialiser Pears


Etter installasjonen kjører du bare følgende kommando i terminalen:


```bash
pear
```


Ved første oppstart vil Pears koble seg til peer-to-peer-nettverket for å laste ned de nødvendige komponentene. Denne prosessen er ikke avhengig av noen sentral server - filene hentes direkte fra andre peers.


![Image](assets/fr/10.webp)


Når nedlastingen er fullført, kjører du kommandoen på nytt for å bekrefte at alt fungerer:


```bash
pear
```


![Image](assets/fr/11.webp)


Hvis alt er riktig installert, vises Pears' hjelpemeny med en liste over tilgjengelige kommandoer.


### 2.6. Test pærer med Keet


For å verifisere at Pears er i full drift, kan du starte en eksisterende P2P-applikasjon som er tilgjengelig i nettverket, for eksempel Keet, den åpen kildekodebaserte meldings- og videokonferanseprogramvaren som er utviklet av Holepunch.


```bash
pear run pear://keet
```


Denne kommandoen laster inn Keet-applikasjonen direkte fra Pears-nettverket, uten å bruke en sentral server. Hvis Keet starter som det skal, betyr det at Pears-installasjonen din fungerer som den skal.


![Image](assets/fr/12.webp)


Linux-systemet ditt er nå klart til å kjøre og være vert for peer-to-peer-applikasjoner med Pears.


## 3. Slik installerer du Pears på Windows


Det er like enkelt å installere Pears på Windows som på Linux, men det krever noen spesifikke verktøy.


*Hvis du bruker Linux og allerede har installert Pears, kan du hoppe direkte til **Trinn 5**


### 3.1. Åpne PowerShell som administrator


Først starter du PowerShell med administratorrettigheter:



- Klikk på Start-menyen;
- Skriv inn "PowerShell";
- Høyreklikk på "*Windows PowerShell*";
- Velg "*Kjør som administrator*".


![Image](assets/fr/15.webp)


### 3.2. Last ned NVS


Pears installeres via *npm*, *Node.js*-pakkebehandleren. På Windows anbefaler Holepunch å bruke *NVS* (*Node Version Switcher*), som er mer stabil enn *NVM* på dette systemet.


Kjør følgende kommando i PowerShell for å installere den nyeste versjonen av *NVS*:


```PowerShell
winget install jasongin.nvs
```


![Image](assets/fr/16.webp)


### 3.3. Installer Node.js


Etter installasjonen starter du PowerShell på nytt og skriver inn følgende kommando:


```powershell
nvs
```


Du bør se en liste over tilgjengelige *Node.js*-versjoner. Velg den første ved å trykke på `a`-tasten på tastaturet.


![Image](assets/fr/17.webp)


*Node.js* er nå installert.


![Image](assets/fr/18.webp)


### 3.4. Verifiser installasjoner


Sørg for at *Node.js* og *npm* er tilgjengelige:


```powershell
node -v
npm -v
```


Begge kommandoene skal returnere et versjonsnummer.


![Image](assets/fr/19.webp)


### 3.5. Installer Pears med npm


Når *Node.js* og *npm* er tilgjengelige, installerer du **Pears CLI** globalt på systemet ditt:


```powershell
npm install -g pear
```


Dette installerer `pear`-binærfilen i din globale *npm*-katalog.


![Image](assets/fr/20.webp)


### 3.6. Verifiser og initialiser Pears


Når installasjonen er fullført, kjører du:


```powershell
pear
```


Ved første oppstart vil Pears automatisk laste ned de nødvendige komponentene fra peer-to-peer-nettverket. Denne prosessen kan ta noen øyeblikk.


![Image](assets/fr/21.webp)


Hvis alt gikk bra, bør du se Pears CLI-hjelpemenyen med en liste over tilgjengelige underkommandoer (run, seed, info...).


### 3.7. Test pærer med Keet


For å verifisere at Pears er i full drift, kan du starte en eksisterende P2P-applikasjon som er tilgjengelig i nettverket, for eksempel Keet - meldings- og videokonferanseprogramvaren med åpen kildekode utviklet av Holepunch.


```bash
pear run pear://keet
```


Denne kommandoen laster inn Keet-applikasjonen direkte fra Pears-nettverket, uten å bruke noen sentral server. Hvis Keet starter, betyr det at Pears-installasjonen din er fullt funksjonell.


![Image](assets/fr/22.webp)


Windows-systemet ditt er nå klart til å kjøre og være vert for peer-to-peer-programmer med Pears.


## 4. Slik installerer du Pears på macOS


Installasjonen av Pears på macOS ligner på Linux, men krever noen få justeringer som er spesifikke for Apples miljø. La oss gå gjennom disse trinnene sammen.


*Hvis du bruker Linux eller Windows og allerede har installert Pears, kan du hoppe direkte til **Trinn 5**


### 4.1. Kontroller systemforutsetningene


Før installasjon må du sørge for at *Xcode Command Line Tools* er installert på systemet ditt. Denne pakken inneholder de nødvendige byggeverktøyene for *Node.js* og dets avhengigheter.


For å gjøre dette åpner du en terminal ved å bruke snarveien `Cmd + mellomromstasten`, skriver `Terminal` og trykker `Enter`. Kjør deretter følgende kommando i terminalen for å installere den:


```bash
xcode-select --install
```


Hvis verktøyene allerede er installert på systemet ditt, vil macOS varsle deg om dette.


### 4.2. Installer NVM


Pears distribueres via *npm*, pakkebehandleren for *Node.js*. Selv om Pears ikke er direkte avhengig av *Node.js* for å fungere, er det nødvendig for installasjonen. Den anbefalte metoden for å installere *Node.js* på macOS er *NVM* (*Node Version Manager*), som lar deg administrere flere Node-versjoner samtidig.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


Last deretter inn terminalen på nytt for å aktivere *NVM*:


```bash
source ~/.zshrc
```


Hvis du bruker *bash* i stedet for *zsh*, kjører du:


```bash
source ~/.bashrc
```


Deretter kontrollerer du at *NVM* er riktig installert:


```bash
nvm --version
```


Terminalen skal vise den installerte *NVM*-versjonen.


### 4.3. Installer Node.js og npm


Deretter installerer du en stabil versjon av *Node.js* (for eksempel den nåværende LTS-versjonen):


```bash
nvm install --lts
```


Når installasjonen er fullført, kontrollerer du de installerte versjonene:


```bash
node -v
npm -v
```


Begge kommandoene skal returnere et versjonsnummer.


### 4.4. Installer Pears med npm


Når *npm* er tilgjengelig, kan du installere Pears CLI globalt på systemet ditt. Dette gjør at du kan utføre kommandoen `pear` fra hvilken som helst katalog.


```bash
npm install -g pear
```


### 4.5. Initialiser Pears


Etter installasjonen kjører du bare følgende kommando i terminalen:


```bash
pear
```


Ved første lansering kobler Pears seg til peer-to-peer-nettverket for å laste ned de nødvendige komponentene. Denne prosessen krever ingen sentral server - filene hentes direkte fra andre peers.


Når nedlastingen er fullført, kjører du kommandoen på nytt for å kontrollere at alt fungerer:


```bash
pear
```


Hvis alt er riktig installert, vises Pears' hjelpemeny med en liste over tilgjengelige kommandoer.


### 4.6. Test pærer med Keet


For å verifisere at Pears er i full drift, kan du starte en P2P-applikasjon som allerede er tilgjengelig i nettverket, for eksempel Keet, Holepunchs programvare for meldinger og videokonferanser med åpen kildekode.


```bash
pear run pear://keet
```


Denne kommandoen laster inn Keet-appen direkte fra Pears-nettverket, uten å bruke en sentral server. Hvis Keet starter vellykket, betyr det at Pears-installasjonen din er fullt funksjonell.


MacOS-systemet ditt er nå klart til å kjøre og være vert for peer-to-peer-programmer med Pears.


## 5. Slik bruker du Plan ₿ Academy på pærer


Når Pears er installert og kjører, kan du starte **Plan ₿ Academy**-plattformen direkte via P2P-nettverket. Bare kjør følgende kommando i terminalen (den samme kommandoen fungerer på Linux, Windows og macOS):


```bash
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


![Image](assets/fr/13.webp)


Når innlastingen er fullført, åpnes Plan ₿ Academy i Pears-miljøet ditt, klar til å brukes akkurat som det opprinnelige nettstedet - men uten å være avhengig av en sentral server.


![Image](assets/fr/14.webp)


## 6. Hvordan lage en såplan ₿ Academy on Pears


I Pears-nettverket betyr å *seed* en applikasjon å videredistribuere den til andre peers fra din egen maskin. I praksis, når du seed Plan ₿ Academy, blir datamaskinen din en datakilde som gjør det mulig for andre brukere å laste ned applikasjonen uten å være avhengig av en sentral server.


Denne mekanismen styrker robustheten og sensurmotstanden til applikasjonen vår i Pears-nettverket. Jo flere peers seed en applikasjon har, desto mer tilgjengelig og desentralisert blir den, selv om noen av de opprinnelige nodene skulle gå offline.


For å distribuere Plan ₿ Academy kjører du ganske enkelt følgende kommando:


```bash
pear seed pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


Så lenge denne kommandoen er aktiv, vil enheten din delta i distribusjonen av programmets filer. Hvis du lukker terminalen, stopper delingsprosessen.


Hvis du vil fortsette med seeding etter en omstart, kan du kjøre kommandoen i bakgrunnen eller opprette en systemtjeneste - for eksempel en systemd-tjeneste på Linux, en LaunchAgent på macOS eller en planlagt oppgave på Windows. Disse metodene sørger for at Plan ₿ Academy-programmet automatisk gjenopptar seeding ved oppstart av systemet.


Takk for at du bidrar til desentralisert distribusjon av Plan ₿ Academy på Pears og bidrar til å gjøre Bitcoin-utdanning virkelig sensurresistent!