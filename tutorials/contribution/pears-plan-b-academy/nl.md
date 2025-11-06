---
name: Plan ₿ Academie - Peren App
description: Hoe installeer en gebruik je de applicatie Plan ₿ Academy op Pears?
---

![cover](assets/cover.webp)


Je weet waarschijnlijk al dat Plan ₿ Academy de grootste educatieve database gewijd aan Bitcoin is, die cursussen, tutorials en duizenden open-source bronnen samenbrengt. Oorspronkelijk was Plan ₿ Academy een website. Maar wat zou er gebeuren als je er geen normale toegang meer toe had, bijvoorbeeld in het geval van censuur?


In deze tutorial leren we hoe we het **Plan ₿ Academy** platform echt censuurbestendig kunnen maken met **Pears**, een peer-to-peer (P2P) technologie ontwikkeld door **Holepunch** en ondersteund door **Tether**.


Pears is de software waarmee we het Plan ₿ Academy-platform kunnen uitvoeren zonder afhankelijk te zijn van een gecentraliseerde website. In deze tutorial installeren we Pears op je computer om toegang te krijgen tot Plan ₿ Academy via Pears.


Het doel van Pears is eenvoudig: het mogelijk maken om webapplicaties te distribueren en te gebruiken zonder afhankelijk te zijn van een gecentraliseerde infrastructuur (geen servers, geen hosts, geen tussenpersonen). Met andere woorden, zelfs als een cloudprovider uitvalt of een land een domein blokkeert, blijft de applicatie leven onder de peers van het netwerk. Dankzij deze aanpak blijft ons educatieve platform, Plan ₿ Academy, wereldwijd toegankelijk, zonder een enkel "single point of failure".


---

**TL;DR:**



- Peren installeren;



- Voer de volgende opdracht uit om de app Plan ₿ Academy te starten:


```shell
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


---

## 1. Wat is Peren?


Pears is tegelijkertijd een runtime-omgeving, een ontwikkeltool en een implementatieplatform voor peer-to-peer applicaties. Met deze open-source tool kun je software bouwen, delen en draaien zonder servers of infrastructuur, rechtstreeks tussen gebruikers. In praktische termen betekent dit dat in plaats van een applicatie op een centrale server te hosten, elke gebruiker een knooppunt in het netwerk wordt: ze delen een deel van de applicatie en gegevens met andere peers. Het hele systeem vormt een gedistribueerd netwerk waarin elke instantie samenwerkt om de service toegankelijk te houden.


![Image](assets/fr/01.webp)


Deze aanpak is gebaseerd op een set modulaire softwarecomponenten ontwikkeld door Holepunch:



- Hypercore**: een gedistribueerd logboek dat zorgt voor consistentie en beveiliging van gegevens zonder een centrale database.
- Hyperbee**: een index gebouwd bovenop Hypercore waarmee gegevens efficiënt kunnen worden georganiseerd en opgevraagd.
- Hyperdrive**: een gedistribueerd bestandssysteem dat wordt gebruikt om applicatiebestanden op te slaan en te synchroniseren tussen peers.
- Hyperswarm** en **HyperDHT**: netwerklagen die wereldwijd peer discovery en verbindingen mogelijk maken zonder centrale server.
- Secretstream**: een end-to-end encryptieprotocol dat de communicatie tussen peers beveiligt.


Door deze componenten te combineren, maakt Pears het mogelijk om autonome, versleutelde en gedistribueerde applicaties te maken, waarbij elke gebruiker actief deelneemt aan het netwerk. Deze gedecentraliseerde architectuur elimineert infrastructuurkosten, censuurrisico's en SPOF's (*Single Points of Failure*).


Pears is ontwikkeld door Holepunch, een bedrijf opgericht door Mathias Buus en Paolo Ardoino (CEO van Tether en CTO van Bitfinex), met de missie om peer-to-peer logica uit te breiden voorbij Bitcoin. Hun ambitie is om het "internet van peers" te bouwen, waar elke toepassing kan werken zonder toestemming, zonder servers en zonder tussenpersonen. Hun ambitie is om het "*Internet van peers*" te bouwen, waar elke toepassing kan werken zonder toestemming, zonder servers en zonder tussenpersonen. Holepunch zit al achter **Keet**, een volledig P2P video conferencing en messaging app.


https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b

*Deze Pears installatiehandleiding is verdeeld in meerdere secties, afhankelijk van uw besturingssysteem. Ga direct naar degene die overeenkomt met jouw omgeving om de juiste instructies te volgen:*



- Linux (Debian)** → Sectie **2**
- Ramen** → Sectie **3**
- macOS** → Sectie **4**


## 2. Hoe installeer ik Pears op Linux (Debian)?


Het installeren van Pears op Debian is relatief eenvoudig, maar vereist een paar vereisten, die we in deze sectie zullen beschrijven.


### 2.1. Werk het systeem bij


Voordat je iets anders doet, is het belangrijk om ervoor te zorgen dat je systeem up-to-date is.


```bash
sudo apt update && sudo apt upgrade -y
```


![Image](assets/fr/02.webp)


### 2.2. Afhankelijkheden installeren


Pears maakt gebruik van enkele systeembibliotheken, waaronder `libatomic1`, gebruikt door de Bare JavaScript runtime engine. Installeer deze met het volgende commando:


```bash
sudo apt install -y libatomic1 curl git
```


![Image](assets/fr/03.webp)


### 2.3. Node.js en npm installeren via NVM


Pears wordt gedistribueerd via *npm*, de *Node.js* pakketbeheerder. Hoewel Pears niet direct afhankelijk is van *Node.js* om te draaien, is het wel vereist voor installatie. De aanbevolen manier om *Node.js* op Linux te installeren is via *NVM* (*Node Version Manager*), waarmee je meerdere versies van Node naast elkaar kunt beheren.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


![Image](assets/fr/04.webp)


Herlaad vervolgens je terminal om *NVM* te activeren:


```bash
source ~/.bashrc
```


![Image](assets/fr/05.webp)


Controleer of *NVM* correct is geïnstalleerd:


```bash
nvm --version
```


![Image](assets/fr/06.webp)


Installeer vervolgens een stabiele versie van *Node.js* (bijvoorbeeld de huidige LTS-versie):


```bash
nvm install --lts
```


![Image](assets/fr/07.webp)


Controleer of *Node.js* en *npm* goed zijn geïnstalleerd:


```bash
node -v
npm -v
```


![Image](assets/fr/08.webp)


### 2.4. Pears installeren met npm


Zodra *npm* beschikbaar is, kun je de Pears CLI globaal op je systeem installeren. Hierdoor kun je het `pear` commando vanuit elke map uitvoeren.


```bash
npm install -g pear
```


![Image](assets/fr/09.webp)


### 2.5. Peren initialiseren


Voer na de installatie gewoon het volgende commando uit in je terminal:


```bash
pear
```


Bij de eerste start zal Pears verbinding maken met het peer-to-peer netwerk om de benodigde componenten te downloaden. Dit proces is niet afhankelijk van een centrale server - de bestanden worden rechtstreeks opgehaald bij andere peers.


![Image](assets/fr/10.webp)


Zodra de download is voltooid, voert u de opdracht opnieuw uit om te bevestigen dat alles werkt:


```bash
pear
```


![Image](assets/fr/11.webp)


Als alles correct is geïnstalleerd, verschijnt het helpmenu van Pears met een lijst van beschikbare opdrachten.


### 2.6. Peren testen met Keet


Om te controleren of Pears volledig operationeel is, kun je een bestaande P2P applicatie starten die beschikbaar is op het netwerk, zoals Keet, de open-source messaging en video conferencing software ontwikkeld door Holepunch.


```bash
pear run pear://keet
```


Dit commando laadt de Keet applicatie direct vanaf het Pears netwerk, zonder gebruik te maken van een centrale server. Als Keet correct opstart, betekent dit dat je Pears installatie volledig functioneel is.


![Image](assets/fr/12.webp)


Je Linux systeem is nu klaar om peer-to-peer applicaties te draaien en te hosten met Pears.


## 3. Hoe installeer ik Pears op Windows?


Het installeren van Pears op Windows is net zo eenvoudig als op Linux, maar vereist een paar specifieke tools.


*Als je Linux gebruikt en Pears al hebt geïnstalleerd, kun je direct naar **stap 5**.* gaan


### 3.1. Open PowerShell als beheerder


Start eerst PowerShell met beheerdersrechten:



- Klik op het menu Start;
- Typ "PowerShell";
- Klik met de rechtermuisknop op "*Windows PowerShell*";
- Selecteer "*Uitvoeren als beheerder*".


![Image](assets/fr/15.webp)


### 3.2. NVS downloaden


Pears wordt geïnstalleerd via *npm*, de *Node.js* package manager. Op Windows is de methode die wordt aanbevolen door Holepunch om *NVS* (*Node Version Switcher*) te gebruiken, wat stabieler is dan *NVM* op dit systeem.


Voer in PowerShell de volgende opdracht uit om de nieuwste versie van *NVS* te installeren:


```PowerShell
winget install jasongin.nvs
```


![Image](assets/fr/16.webp)


### 3.3. Node.js installeren


Start na de installatie PowerShell opnieuw op en voer vervolgens de volgende opdracht in:


```powershell
nvs
```


Je zou een lijst met beschikbare *Node.js* versies moeten zien. Selecteer de eerste door op de `a` toets van je toetsenbord te drukken.


![Image](assets/fr/17.webp)


*Node.js* is nu geïnstalleerd.


![Image](assets/fr/18.webp)


### 3.4. Installaties controleren


Zorg ervoor dat *Node.js* en *npm* toegankelijk zijn:


```powershell
node -v
npm -v
```


Beide commando's moeten een versienummer teruggeven.


![Image](assets/fr/19.webp)


### 3.5. Pears installeren met npm


Zodra *Node.js* en *npm* beschikbaar zijn, installeer je **Pears CLI** globaal op je systeem:


```powershell
npm install -g pear
```


Dit installeert de `pear` binary in je globale *npm* directory.


![Image](assets/fr/20.webp)


### 3.6. Peren controleren en initialiseren


Zodra de installatie is voltooid, uitvoeren:


```powershell
pear
```


Bij de eerste start zal Pears automatisch de benodigde componenten downloaden van het peer-to-peer netwerk. Dit proces kan enkele ogenblikken duren.


![Image](assets/fr/21.webp)


Als alles goed is gegaan, zou je het Pears CLI helpmenu moeten zien met de lijst van beschikbare subcommando's (run, seed, info...).


### 3.7. Test Peren met Keet


Om te controleren of Pears volledig operationeel is, kun je een bestaande P2P applicatie starten die beschikbaar is op het netwerk, zoals Keet - de open-source messaging en video conferencing software ontwikkeld door Holepunch.


```bash
pear run pear://keet
```


Dit commando laadt de Keet applicatie direct vanuit het Pears netwerk, zonder gebruik te maken van een centrale server. Als Keet succesvol opstart, betekent dit dat uw Pears installatie volledig functioneel is.


![Image](assets/fr/22.webp)


Je Windows systeem is nu klaar om peer-to-peer applicaties te draaien en te hosten met Pears.


## 4. Zo installeer je Pears op macOS


Het installeren van Pears op macOS is vergelijkbaar met Linux, maar vereist een paar aanpassingen die specifiek zijn voor de omgeving van Apple. Laten we deze stappen samen doorlopen.


*Als je Linux of Windows gebruikt en Pears al hebt geïnstalleerd, kun je direct doorgaan naar **stap 5**.*


### 4.1. Systeemvereisten controleren


Zorg er voor de installatie voor dat *Xcode Command Line Tools* op je systeem is geïnstalleerd. Dit pakket biedt de nodige bouwgereedschappen voor *Node.js* en zijn afhankelijkheden.


Open hiervoor een terminal met de sneltoets `Cmd + spatiebalk`, typ `Terminal` en druk op `Enter`. Voer vervolgens de volgende opdracht uit in de terminal om het te installeren:


```bash
xcode-select --install
```


Als de tools al op je systeem zijn geïnstalleerd, zal macOS je dat laten weten.


### 4.2. NVM installeren


Pears wordt gedistribueerd via *npm*, de *Node.js* pakketbeheerder. Hoewel Pears niet direct afhankelijk is van *Node.js* om te functioneren, is het vereist voor installatie. De aanbevolen methode voor het installeren van *Node.js* op macOS is *NVM* (*Node Version Manager*), waarmee je meerdere Node-versies tegelijk kunt beheren.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


Herlaad dan je terminal om *NVM* te activeren:


```bash
source ~/.zshrc
```


Als je *bash* gebruikt in plaats van *zsh*, voer dan uit:


```bash
source ~/.bashrc
```


Controleer vervolgens of *NVM* correct is geïnstalleerd:


```bash
nvm --version
```


Uw terminal zou de geïnstalleerde *NVM* versie moeten weergeven.


### 4.3. Node.js en npm installeren


Installeer vervolgens een stabiele versie van *Node.js* (bijvoorbeeld de huidige LTS-versie):


```bash
nvm install --lts
```


Zodra de installatie is voltooid, controleert u de geïnstalleerde versies:


```bash
node -v
npm -v
```


Beide commando's moeten een versienummer teruggeven.


### 4.4. Pears installeren met npm


Zodra *npm* beschikbaar is, kun je de Pears CLI globaal op je systeem installeren. Hierdoor kun je het `pear` commando vanuit elke map uitvoeren.


```bash
npm install -g pear
```


### 4.5. Peren initialiseren


Voer na de installatie gewoon het volgende commando uit in je terminal:


```bash
pear
```


Bij de eerste start maakt Pears verbinding met het peer-to-peer netwerk om de benodigde componenten te downloaden. Voor dit proces is geen centrale server nodig - bestanden worden direct opgehaald bij andere peers.


Zodra het downloaden is voltooid, voert u de opdracht opnieuw uit om te controleren of alles werkt:


```bash
pear
```


Als alles correct is geïnstalleerd, verschijnt het helpmenu van Pears met een lijst van beschikbare opdrachten.


### 4.6. Peren testen met Keet


Om te controleren of Pears volledig operationeel is, kun je een P2P applicatie starten die al beschikbaar is op het netwerk, zoals Keet, de open-source messaging en video conferencing software van Holepunch.


```bash
pear run pear://keet
```


Dit commando laadt de Keet app rechtstreeks vanuit het Pears netwerk, zonder gebruik te maken van een centrale server. Als Keet succesvol opstart, betekent dit dat uw Pears installatie volledig functioneel is.


Je macOS-systeem is nu klaar om peer-to-peer applicaties te draaien en te hosten met Pears.


## 5. Hoe gebruik je Plan ₿ Academy op peren?


Zodra Pears geïnstalleerd en actief is, kun je het **Plan ₿ Academy** platform direct starten via het P2P netwerk. Voer gewoon het volgende commando uit in je terminal (hetzelfde commando werkt op Linux, Windows en macOS):


```bash
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


![Image](assets/fr/13.webp)


Zodra het laden is voltooid, wordt Plan ₿ Academy geopend binnen uw Pears-omgeving, klaar om te worden gebruikt net als de oorspronkelijke website - maar zonder enige afhankelijkheid van een centrale server.


![Image](assets/fr/14.webp)


## 6. Zaaiplan ₿ Academie voor Peren


In het Pears-netwerk betekent *seed* een applicatie vanaf je eigen machine doorsturen naar andere peers. In de praktijk, wanneer je seed Plan ₿ Academy gebruikt, wordt jouw computer een gegevensbron waarmee andere gebruikers de applicatie kunnen downloaden zonder afhankelijk te zijn van een centrale server.


Dit mechanisme versterkt de veerkracht en censuurbestendigheid van onze applicatie op het Pears-netwerk. Hoe meer peers seed een applicatie, hoe meer beschikbaar en gedecentraliseerd het wordt, zelfs als sommige originele nodes offline gaan.


Om Plan ₿ Academy te helpen verspreiden, voer je gewoon het volgende commando uit:


```bash
pear seed pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


Zolang dit commando actief blijft, zal je apparaat deelnemen aan het distribueren van de bestanden van de applicatie. Als je de terminal sluit, stopt het uitwisselingsproces.


Om door te gaan met zaaien na een herstart, kun je de opdracht op de achtergrond uitvoeren of een systeemservice maken - bijvoorbeeld een systemd-service op Linux, een LaunchAgent op macOS of een geplande taak op Windows. Deze methoden zorgen ervoor dat de Plan ₿ Academy-applicatie automatisch verder gaat met zaaien bij het opstarten van het systeem.


Bedankt voor je bijdrage aan de decentrale distributie van Plan ₿ Academy on Pears en het helpen om Bitcoin onderwijs echt censuurbestendig te maken!