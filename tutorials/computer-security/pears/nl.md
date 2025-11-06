---
name: Peren
description: Hoe installeer en gebruik ik applicaties op Pears?
---

![cover](assets/cover.webp)



In deze tutorial leren we hoe we applicaties kunnen draaien op **Pears**, een peer-to-peer (P2P) technologie ontwikkeld door **Holepunch** en ondersteund door **Tether**. Het doel is simpel: het mogelijk maken om webapplicaties te distribueren en te gebruiken zonder afhankelijk te zijn van een gecentraliseerde infrastructuur (geen servers, geen hosts, geen tussenpersonen). Met andere woorden, zelfs als een cloud provider sluit of een land een domein blokkeert, leeft de applicatie voort onder netwerk peers.



## 1. Wat is Peren?



Pears is een runtime-omgeving, ontwikkeltool en implementatieplatform voor peer-to-peer toepassingen. Deze open-source tool maakt het mogelijk om software te bouwen, te delen en te draaien zonder server of infrastructuur, rechtstreeks tussen gebruikers. Concreet betekent dit dat in plaats van een applicatie op een centrale server te hosten, elke gebruiker een netwerkknooppunt wordt dat een deel van de applicatie en gegevens deelt met andere peers. Het hele systeem vormt een gedistribueerd netwerk, waarbij elke instantie samenwerkt om de service toegankelijk te houden.



![Image](assets/fr/01.webp)



Deze aanpak is gebaseerd op een set modulaire softwarebouwstenen ontwikkeld door Holepunch:




- Hypercore**: een gedistribueerd logboek dat gegevensconsistentie en -beveiliging garandeert zonder een centrale database.
- Hyperbee**: een indexer bovenop Hypercore, voor efficiënte gegevensorganisatie en bladeren.
- Hyperdrive**: een gedistribueerd bestandssysteem dat wordt gebruikt om applicatiebestanden op te slaan en te synchroniseren tussen peers.
- Hyperswarm** en **HyperDHT**: netwerklagen die het mogelijk maken om peers wereldwijd te ontdekken en met elkaar te verbinden, zonder een centrale server.
- Secretstream**: een E2E encryptieprotocol om uitwisselingen tussen twee peers te beveiligen.



Door deze componenten te combineren, maakt Pears het mogelijk om autonome, versleutelde en gedistribueerde applicaties te maken, waarbij elke gebruiker actief deelneemt aan het netwerk. Deze gedecentraliseerde architectuur elimineert infrastructuurkosten, censuurrisico's en SPOF's (*Single Point of Failure*).



## 2. Oorsprong en filosofie van het project



Pears wordt ontwikkeld door Holepunch, een bedrijf opgericht door Mathias Buus en Paolo Ardoino (CEO van Tether en CTO van Bitfinex), met de missie om peer-to-peer logica uit te breiden voorbij Bitcoin. Hun ambitie is om het "Peer-to-Peer Internet" te bouwen, waar elke toepassing kan draaien zonder autorisatie, zonder servers en zonder tussenpersonen. Hun ambitie is om het "Peer-to-Peer Internet" te bouwen, waar elke toepassing kan draaien zonder autorisatie, zonder servers en zonder tussenpersonen. Holepunch zit al achter **Keet**, een volledig P2P video conferencing en messaging applicatie.



*Deze Pears installatiehandleiding is onderverdeeld in verschillende secties, afhankelijk van uw besturingssysteem. Ga direct naar de sectie die overeenkomt met jouw omgeving om de juiste instructies te volgen :*




- Linux (Debian)** → Deel **3**
- Vensters** → Deel **4**
- macOS** → Deel **5**



## 3. Hoe installeer ik Pears op Linux (Debian)?



Het installeren van Pears op een Debian systeem is relatief eenvoudig, maar vereist wel een paar vereisten, die we in deze sectie uit de doeken doen.



### 3.1. het systeem bijwerken



Eerst en vooral is het belangrijk om ervoor te zorgen dat je systeem up-to-date is.



```bash
sudo apt update && sudo apt upgrade -y
```



![Image](assets/fr/02.webp)



### 3.2. afhankelijkheden installeren



Pears vertrouwt op bepaalde systeembibliotheken, met name `libatomic1`, gebruikt door de Bare JavaScript runtime. Installeer deze met het volgende commando:



```bash
sudo apt install -y libatomic1 curl git
```



![Image](assets/fr/03.webp)



### 3.3. Node.js en npm installeren via NVM



Pears wordt gedistribueerd via *npm*, de *Node.js* pakketbeheerder. Hoewel Pears niet direct afhankelijk is van *Node.js* om te functioneren, is het noodzakelijk voor de installatie. De aanbevolen methode voor het installeren van *Node.js* op Linux is *NVM* (*Node Version Manager*), waarmee je meerdere versies van Node parallel kunt beheren.



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



![Image](assets/fr/04.webp)



Herlaad dan je terminal om *NVM* te activeren:



```bash
source ~/.bashrc
```



![Image](assets/fr/05.webp)



Controleer of *NVM* is geïnstalleerd:



```bash
nvm --version
```



![Image](assets/fr/06.webp)



Installeer vervolgens een stabiele versie van *Node.js* (bijvoorbeeld de huidige LTS):



```bash
nvm install --lts
```



![Image](assets/fr/07.webp)



Controleer *Node.js* en *npm* installaties:



```bash
node -v
npm -v
```



![Image](assets/fr/08.webp)



### 3.4 Peren installeren met npm



Zodra *npm* beschikbaar is, kun je Pears CLI globaal op je systeem installeren. Hierdoor kun je het `pear` commando vanuit elke map uitvoeren.



```bash
npm install -g pear
```



![Image](assets/fr/09.webp)



### 3.5. Peren initialiseren



Voer na de installatie gewoon het volgende commando uit in je terminal:



```bash
pear
```



Bij de eerste keer opstarten zal Pears verbinding maken met het peer-to-peer netwerk om de benodigde componenten te downloaden. Dit proces vereist geen centrale server: bestanden worden rechtstreeks verkregen van andere peers.



![Image](assets/fr/10.webp)



Zodra het downloaden is voltooid, voert u de opdracht opnieuw uit om te controleren of alles werkt:



```bash
pear
```



![Image](assets/fr/11.webp)



Als alles correct is geïnstalleerd, wordt Pears Help weergegeven met een lijst van beschikbare opdrachten.



### 3.6. Peren testen met Keet



Om te controleren of Pears volledig operationeel is, kun je een P2P applicatie starten die al beschikbaar is op het netwerk, zoals Keet, Holepunch's open-source messaging en videoconferencing software.



```bash
pear run pear://keet
```



Dit commando laadt de Keet-toepassing rechtstreeks vanaf het Pears-netwerk, zonder via een centrale server te gaan. Als Keet correct opstart, is je Pears installatie volledig functioneel.



![Image](assets/fr/12.webp)



Je Linux systeem is nu klaar om peer-to-peer applicaties te draaien en te hosten met Pears.



## 4. Hoe installeer ik Pears op Windows?



Het installeren van Pears op Windows is net zo eenvoudig als op Linux, maar vereist een paar speciale tools.



*Als je Linux gebruikt, kun je stap 6.* overslaan



### 4.1. open PowerShell in beheerdersmodus



Voer eerst PowerShell uit met beheerdersrechten:




- Klik op het menu Start;
- Type PowerShell ;
- Klik met de rechtermuisknop op "*Windows PowerShell*" ;
- Selecteer "*Uitvoeren als beheerder*".



![Image](assets/fr/15.webp)



### 4.2. NVS downloaden



Pears wordt geïnstalleerd via *npm*, de *Node.js* package manager. Op Windows is de methode die wordt aanbevolen door Holepunch om *NVS* (*Node Version Switcher*) te gebruiken, wat stabieler is dan *NVM* op dit systeem.



Voer in PowerShell de volgende opdracht uit om de nieuwste versie van *NVS* te installeren:



```PowerShell
winget install jasongin.nvs
```



![Image](assets/fr/16.webp)



### 4.3. Node.js installeren



Start PowerShell na de installatie opnieuw op en voer de volgende opdracht in:



```powershell
nvs
```



Je zou een lijst met beschikbare *Node.js* versies moeten zien. Selecteer de eerste door op de `a` toets van je toetsenbord te drukken.



![Image](assets/fr/17.webp)



*Node.js* is geïnstalleerd.



![Image](assets/fr/18.webp)



### 4.4. Controleer installaties



Zorg ervoor dat *Node.js* en *npm* toegankelijk zijn:



```powershell
node -v
npm -v
```



Beide commando's moeten een versienummer teruggeven.



![Image](assets/fr/19.webp)



### 4.5. Peren installeren met npm



Zodra *Node.js* en *npm* beschikbaar zijn, installeer je **Pears CLI** globaal op je systeem:



```powershell
npm install -g pear
```



Dit installeert de `pear` binary in je globale *npm* directory.



![Image](assets/fr/20.webp)



### 4.6. Peren controleren en initialiseren



Zodra de installatie is voltooid, voert u :



```powershell
pear
```



Bij de eerste keer opstarten zal Pears automatisch de benodigde componenten downloaden van het peer-to-peer netwerk. Dit proces kan enkele ogenblikken duren.



![Image](assets/fr/21.webp)



Als alles goed is gegaan, zou je het CLI Pears helpscherm moeten zien met een lijst van beschikbare subcommando's (run, seed, info...).



### 4.7. Peren testen met Keet



Om te controleren of Pears volledig operationeel is, kun je een P2P applicatie starten die al beschikbaar is op het netwerk, zoals Keet, Holepunch's open-source messaging en videoconferencing software.



```bash
pear run pear://keet
```



Dit commando laadt de Keet-toepassing rechtstreeks vanaf het Pears-netwerk, zonder via een centrale server te gaan. Als Keet correct opstart, is je Pears installatie volledig functioneel.



![Image](assets/fr/22.webp)



Je Windows systeem is nu klaar om peer-to-peer applicaties te draaien en te hosten met Pears.



## 5. Hoe installeer ik Pears op macOS?



Het installeren van Pears op macOS is vergelijkbaar met het installeren op Linux, maar vereist een paar aanpassingen die specifiek zijn voor de Apple-omgeving. Laten we deze stappen samen ontdekken.



*Als je Linux of Windows gebruikt en Pears al hebt geïnstalleerd, kun je direct doorgaan naar **stap 6**.*



### 5.1. Controleer de systeemvereisten



Voordat je begint met installeren, moet je ervoor zorgen dat *Xcode Command Line Tools* aanwezig is op je systeem. Dit pakket biedt de benodigde compilatiegereedschappen voor _Node.js_ en de afhankelijkheden ervan.



Open hiervoor een terminal met de sneltoets `Cmd + spatiebalk`, typ dan `Terminal` en druk op de `Enter` toets. Je kunt dan dit commando in de terminal invoeren om de installatie te starten:



```bash
xcode-select --install
```



Als de tools al op je systeem zijn geïnstalleerd, zal macOS je dat laten weten.



### 5.2. NVM installeren



Pears wordt gedistribueerd via *npm*, de *Node.js* pakketbeheerder. Hoewel Pears niet direct afhankelijk is van *Node.js* om te functioneren, is het noodzakelijk voor de installatie. De aanbevolen methode voor het installeren van *Node.js* op macOS is *NVM* (*Node Version Manager*), waarmee je meerdere versies van Node parallel kunt beheren.



```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```



Herlaad dan je terminal om *NVM* te activeren:



```bash
source ~/.zshrc
```



Als je *bash* gebruikt in plaats van *zsh*, voer dan :



```bash
source ~/.bashrc
```



Controleer vervolgens of *NVM* is geïnstalleerd:



```bash
nvm --version
```



De terminal zou de versie van *NVM* moeten weergeven die op uw systeem is geïnstalleerd.



### 5.3. Node.js en npm installeren



Installeer vervolgens een stabiele versie van *Node.js* (bijvoorbeeld de huidige LTS):



```bash
nvm install --lts
```



Zodra de installatie is voltooid, controleert u de geïnstalleerde versies:



```bash
node -v
npm -v
```



Beide commando's moeten een versienummer teruggeven.



### 5.4 Peren installeren met npm



Zodra *npm* beschikbaar is, kun je Pears CLI globaal op je systeem installeren. Hierdoor kun je het `pear` commando vanuit elke map uitvoeren.



```bash
npm install -g pear
```



### 5.5. Peren initialiseren



Voer na de installatie gewoon het volgende commando uit in je terminal:



```bash
pear
```



Bij de eerste keer opstarten zal Pears verbinding maken met het peer-to-peer netwerk om de benodigde componenten te downloaden. Dit proces vereist geen centrale server: bestanden worden rechtstreeks verkregen van andere peers.



Zodra het downloaden is voltooid, voert u de opdracht opnieuw uit om te controleren of alles werkt:



```bash
pear
```



Als alles correct is geïnstalleerd, wordt Pears Help weergegeven met een lijst van beschikbare opdrachten.



### 5.6. Peren testen met Keet



Om te controleren of Pears volledig operationeel is, kun je een P2P applicatie starten die al beschikbaar is op het netwerk, zoals Keet, Holepunch's open-source messaging en videoconferencing software.



```bash
pear run pear://keet
```



Dit commando laadt de Keet-toepassing rechtstreeks vanaf het Pears-netwerk, zonder via een centrale server te gaan. Als Keet correct opstart, is je Pears installatie volledig functioneel.



Je macOS-systeem is nu klaar om peer-to-peer applicaties te draaien en te hosten met Pears.



## 6. Hoe gebruik ik een applicatie op Pears?



Als Pears eenmaal draait, kun je de applicatie van je keuze direct uitvoeren met het volgende commando:



```bash
pear run pear://[KEY]
```



Vervang simpelweg `[KEY]` door de applicatiesleutel die je wilt gebruiken.



![Image](assets/fr/13.webp)



Als je wilt leren hoe je ons Plan ₿ Academy-platform op Pears draait, bekijk dan deze uitgebreide tutorial:



https://planb.academy/tutorials/contribution/others/pears-plan-b-academy-77f0ae28-28fc-4465-a9f1-1c6654711770

En als je wilt weten hoe je de Keet-berichtenapplicatie gebruikt die je zojuist op Pears hebt gelanceerd, bekijk dan deze tutorial:



https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b