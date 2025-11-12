---
name: Pærer
description: Hvordan installerer og bruker jeg applikasjoner på Pears?
---

![cover](assets/cover.webp)



I denne opplæringen lærer vi hvordan du kjører applikasjoner på **Pears**, en peer-to-peer (P2P)-teknologi utviklet av **Holepunch** og støttet av **Tether**. Målet er enkelt: å gjøre det mulig å distribuere og bruke webapplikasjoner uten å være avhengig av noen sentralisert infrastruktur (ingen servere, ingen verter, ingen mellomledd). Med andre ord, selv om en skyleverandør stenger ned eller et land blokkerer et domene, lever applikasjonen videre blant nettverkskolleger.



## 1. Hva er pærer?



Pears er et kjøretidsmiljø, et utviklingsverktøy og en distribusjonsplattform for peer-to-peer-applikasjoner. Dette verktøyet med åpen kildekode gjør det mulig å bygge, dele og kjøre programvare uten en server eller infrastruktur, direkte mellom brukere. Konkret betyr dette at i stedet for å hoste en applikasjon på en sentral server, blir hver bruker en nettverksnode som deler deler deler av applikasjonen og data med andre likemenn. Hele systemet danner et distribuert nettverk, der hver instans samarbeider for å holde tjenesten tilgjengelig.



![Image](assets/fr/01.webp)



Denne tilnærmingen er basert på et sett med modulære programvarebrikker utviklet av Holepunch:




- Hypercore**: en distribuert logg som garanterer datakonsistens og sikkerhet uten en sentral database.
- Hyperbee**: en indekseringsenhet på toppen av Hypercore, for effektiv organisering og surfing av data.
- Hyperdrive**: et distribuert filsystem som brukes til å lagre og synkronisere applikasjonsfiler mellom jevnaldrende.
- Hyperswarm** og **HyperDHT**: nettverkslag som gjør det mulig å oppdage og opprette forbindelse mellom jevnaldrende over hele verden, uten en sentral server.
- Secretstream**: en E2E-krypteringsprotokoll for å sikre utvekslinger mellom to motparter.



Ved å kombinere disse komponentene gjør Pears det mulig å skape autonome, krypterte og distribuerte applikasjoner, der hver bruker deltar aktivt i nettverket. Denne desentraliserte arkitekturen eliminerer infrastrukturkostnader, sensurrisiko og SPOF-er (*Single Point of Failure*).



## 2. Prosjektets opprinnelse og filosofi



Pears utvikles av Holepunch, et selskap grunnlagt av Mathias Buus og Paolo Ardoino (CEO i Tether og CTO i Bitfinex), med mål om å utvide peer-to-peer-logikken utover Bitcoin. Deres ambisjon er å bygge "Peer-to-Peer Internet", der alle applikasjoner kan kjøre uten autorisasjon, uten servere og uten mellomledd. Holepunch står allerede bak **Keet**, en fullstendig P2P-videokonferanse- og meldingsapplikasjon.



*Denne installasjonsveiledningen for Pears er delt inn i flere deler avhengig av operativsystemet ditt. Gå direkte til den delen som svarer til ditt miljø for å følge de riktige instruksjonene :*




- Linux (Debian)** → Del **3**
- Windows** → Del **4**
- macOS** → Del **5**



## 3. Slik installerer du Pears på Linux (Debian)



Det er relativt enkelt å installere Pears på et Debian-system, men det krever noen forutsetninger, som vi skal gå nærmere inn på i dette avsnittet.



### 3.1. Oppdater systemet



Først og fremst er det viktig å sørge for at systemet ditt er oppdatert.



```bash
sudo apt update && sudo apt upgrade -y
```



![Image](assets/fr/02.webp)



### 3.2. Installer avhengigheter



Pears er avhengig av visse systembiblioteker, spesielt `libatomic1`, som brukes av Bare JavaScript-kjøretiden. Installer det med følgende kommando:



```bash
sudo apt install -y libatomic1 curl git
```



![Image](assets/fr/03.webp)



### 3.3. Installer Node.js og npm via NVM



Pears distribueres via *npm*, pakkebehandleren for *Node.js*. Selv om Pears ikke er direkte avhengig av *Node.js* for å fungere, er det nødvendig for installasjonen. Den anbefalte metoden for å installere *Node.js* på Linux er *NVM* (*Node Version Manager*), som lar deg administrere flere versjoner av Node parallelt.



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



![Image](assets/fr/04.webp)



Last deretter inn terminalen på nytt for å aktivere *NVM* :



```bash
source ~/.bashrc
```



![Image](assets/fr/05.webp)



Kontroller at *NVM* er installert:



```bash
nvm --version
```



![Image](assets/fr/06.webp)



Installer deretter en stabil versjon av *Node.js* (f.eks. den nåværende LTS):



```bash
nvm install --lts
```



![Image](assets/fr/07.webp)



Sjekk *Node.js*- og *npm*-installasjoner:



```bash
node -v
npm -v
```



![Image](assets/fr/08.webp)



### 3.4 Installere Pears med npm



Når *npm* er tilgjengelig, kan du installere Pears CLI globalt på systemet ditt. Dette gjør at du kan kjøre kommandoen `pear` fra hvilken som helst katalog.



```bash
npm install -g pear
```



![Image](assets/fr/09.webp)



### 3.5. Initialiser Pears



Etter installasjonen kjører du bare følgende kommando i terminalen:



```bash
pear
```



Ved første oppstart vil Pears koble seg til peer-to-peer-nettverket for å laste ned de nødvendige komponentene. Denne prosessen krever ingen sentral server: filene hentes direkte fra andre peers.



![Image](assets/fr/10.webp)



Når nedlastingen er fullført, kjører du kommandoen på nytt for å sjekke at alt fungerer:



```bash
pear
```



![Image](assets/fr/11.webp)



Hvis alt er riktig installert, vises Pears Help med en liste over tilgjengelige kommandoer.



### 3.6. Testing av pærer med Keet



For å sjekke at Pears er i full drift, kan du starte en P2P-applikasjon som allerede er tilgjengelig på nettverket, for eksempel Keet, Holepunchs programvare for meldinger og videokonferanser med åpen kildekode.



```bash
pear run pear://keet
```



Denne kommandoen laster inn Keet-applikasjonen direkte fra Pears-nettverket, uten å gå via en sentral server. Hvis Keet starter riktig, er Pears-installasjonen din fullt funksjonell.



![Image](assets/fr/12.webp)



Linux-systemet ditt er nå klart til å kjøre og være vert for peer-to-peer-applikasjoner med Pears.



## 4. Slik installerer du Pears på Windows



Det er like enkelt å installere Pears på Windows som på Linux, men det krever noen få spesialverktøy.



*Hvis du bruker Linux, kan du hoppe til trinn 6.*



### 4.1. Åpne PowerShell i administratormodus



Først og fremst kjører du PowerShell med administratorrettigheter :




- Klikk på Start-menyen;
- Skriv inn PowerShell ;
- Høyreklikk på "*Windows PowerShell*" ;
- Velg "*Kjør som administrator*".



![Image](assets/fr/15.webp)



### 4.2. Last ned NVS



Pears installeres via *npm*, *Node.js*-pakkebehandleren. På Windows anbefaler Holepunch å bruke *NVS* (*Node Version Switcher*), som er mer stabil enn *NVM* på dette systemet.



I PowerShell kjører du følgende kommando for å installere den nyeste versjonen av *NVS* :



```PowerShell
winget install jasongin.nvs
```



![Image](assets/fr/16.webp)



### 4.3. Installer Node.js



Etter installasjonen starter du PowerShell på nytt og skriver inn følgende kommando:



```powershell
nvs
```



Du bør se en liste over tilgjengelige *Node.js*-versjoner. Velg den første ved å trykke på `a`-tasten på tastaturet.



![Image](assets/fr/17.webp)



*Node.js* er installert.



![Image](assets/fr/18.webp)



### 4.4. Kontroller installasjoner



Sørg for at *Node.js* og *npm* er tilgjengelige:



```powershell
node -v
npm -v
```



Begge kommandoene må returnere et versjonsnummer.



![Image](assets/fr/19.webp)



### 4.5. Installere Pears med npm



Når *Node.js* og *npm* er tilgjengelige, installerer du **Pears CLI** globalt på systemet ditt:



```powershell
npm install -g pear
```



Dette vil installere `pear`-binærfilen i din globale *npm*-katalog.



![Image](assets/fr/20.webp)



### 4.6. Kontroller og initialiser Pears



Når installasjonen er fullført, kjører du :



```powershell
pear
```



Ved første oppstart vil Pears automatisk laste ned de nødvendige komponentene fra peer-to-peer-nettverket. Denne prosessen kan ta noen øyeblikk.



![Image](assets/fr/21.webp)



Hvis alt har gått bra, bør du se hjelpeskjermen for CLI Pears med en liste over tilgjengelige underkommandoer (run, seed, info...).



### 4.7. Testing av pærer med Keet



For å sjekke at Pears er i full drift, kan du starte en P2P-applikasjon som allerede er tilgjengelig på nettverket, for eksempel Keet, Holepunchs programvare for meldinger og videokonferanser med åpen kildekode.



```bash
pear run pear://keet
```



Denne kommandoen laster inn Keet-applikasjonen direkte fra Pears-nettverket, uten å gå via en sentral server. Hvis Keet starter riktig, er Pears-installasjonen din fullt funksjonell.



![Image](assets/fr/22.webp)



Windows-systemet ditt er nå klart til å kjøre og være vert for peer-to-peer-programmer med Pears.



## 5. Hvordan installerer jeg Pears på macOS?



Installasjonen av Pears på macOS ligner på installasjonen på Linux, men krever noen få justeringer som er spesifikke for Apple-miljøet. La oss utforske disse trinnene sammen.



*Hvis du bruker Linux eller Windows og allerede har installert Pears, kan du gå direkte til **trinn 6**



### 5.1. Sjekk systemkravene



Før du installerer, må du sørge for at *Xcode Command Line Tools* finnes på systemet ditt. Denne pakken inneholder de nødvendige kompileringsverktøyene for _Node.js_ og dens avhengigheter.



Dette gjør du ved å åpne en terminal med hurtigtasten `Cmd + mellomromstasten`, deretter skriver du `Terminal` og trykker på `Enter`. Du kan deretter skrive inn denne kommandoen i terminalen for å starte installasjonen:



```bash
xcode-select --install
```



Hvis verktøyene allerede er installert på systemet ditt, vil macOS informere deg om dette.



### 5.2. Installer NVM



Pears distribueres via *npm*, pakkebehandleren for *Node.js*. Selv om Pears ikke er direkte avhengig av *Node.js* for å fungere, er det nødvendig for installasjonen. Den anbefalte metoden for å installere *Node.js* på macOS er *NVM* (*Node Version Manager*), som lar deg administrere flere versjoner av Node parallelt.



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



Last deretter inn terminalen på nytt for å aktivere *NVM* :



```bash
source ~/.zshrc
```



Hvis du bruker *bash* i stedet for *zsh*, kjører du :



```bash
source ~/.bashrc
```



Kontroller deretter at *NVM* er installert:



```bash
nvm --version
```



Terminalen skal vise hvilken versjon av *NVM* som er installert på systemet ditt.



### 5.3. Installer Node.js og npm



Installer deretter en stabil versjon av *Node.js* (f.eks. den nåværende LTS):



```bash
nvm install --lts
```



Når installasjonen er fullført, kontrollerer du de installerte versjonene:



```bash
node -v
npm -v
```



Begge kommandoene må returnere et versjonsnummer.



### 5.4 Installere Pears med npm



Når *npm* er tilgjengelig, kan du installere Pears CLI globalt på systemet ditt. Dette gjør at du kan kjøre kommandoen `pear` fra hvilken som helst katalog.



```bash
npm install -g pear
```



### 5.5. Initialiser Pears



Etter installasjonen kjører du bare følgende kommando i terminalen:



```bash
pear
```



Ved første oppstart vil Pears koble seg til peer-to-peer-nettverket for å laste ned de nødvendige komponentene. Denne prosessen krever ingen sentral server: filene hentes direkte fra andre peers.



Når nedlastingen er fullført, kjører du kommandoen på nytt for å sjekke at alt fungerer:



```bash
pear
```



Hvis alt er riktig installert, vises Pears Help med en liste over tilgjengelige kommandoer.



### 5.6. Testing av pærer med Keet



For å sjekke at Pears er i full drift, kan du starte en P2P-applikasjon som allerede er tilgjengelig på nettverket, for eksempel Keet, Holepunchs programvare for meldinger og videokonferanser med åpen kildekode.



```bash
pear run pear://keet
```



Denne kommandoen laster inn Keet-applikasjonen direkte fra Pears-nettverket, uten å gå via en sentral server. Hvis Keet starter riktig, er Pears-installasjonen din fullt funksjonell.



MacOS-systemet ditt er nå klart til å kjøre og være vert for peer-to-peer-programmer med Pears.



## 6. Hvordan bruker jeg et program på Pears?



Når Pears er oppe og går, kan du kjøre det programmet du ønsker, direkte med følgende kommando:



```bash
pear run pear://[KEY]
```



Erstatt `[KEY]` med programnøkkelen du ønsker å bruke.



![Image](assets/fr/13.webp)



Hvis du vil lære hvordan du kjører Plan ₿ Academy-plattformen vår på Pears, kan du ta en titt på denne omfattende veiledningen :



https://planb.academy/tutorials/contribution/others/pears-plan-b-academy-77f0ae28-28fc-4465-a9f1-1c6654711770

Og for å finne ut hvordan du bruker Keet-meldingsapplikasjonen du nettopp har lansert på Pears, kan du ta en titt på denne veiledningen :



https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b