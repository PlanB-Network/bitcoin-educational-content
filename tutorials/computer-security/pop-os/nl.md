---
name: Pop!_OS
description: Handleiding voor het installeren van Pop!_OS, een Linux-distributie
---

![cover](assets/cover.webp)



## Inleiding



Pop!OS is een op Linux gebaseerd besturingssysteem ontwikkeld door **System76**, een Amerikaanse fabrikant gespecialiseerd in machines voor ontwikkelaars, ontwerpers en gevorderde gebruikers.



Pop!OS is ontworpen om een moderne, stabiele, krachtige omgeving te bieden en onderscheidt zich door een eenvoudige ervaring, krachtige tools en een sterke focus op productiviteit.



### Wie is System76?



System76 is een Amerikaans bedrijf opgericht in 2005 en gevestigd in Denver, gespecialiseerd in de productie van notebooks, desktops en servers die speciaal ontworpen zijn voor Linux.



In tegenstelling tot traditionele fabrikanten ontwikkelt System76 machines die open en repareerbaar zijn en gericht op softwarevrijheid.



System76 maakt niet alleen computers.



Het bedrijf ontwikkelt ook :




- Pop!OS**, zijn eigen op Linux gebaseerde besturingssysteem;
- COSMIC**, de moderne, krachtige bureaubladomgeving die wordt gebruikt door Pop!OS ;
- Open Firmware**, een open-source firmware gebaseerd op Coreboot ;
- tools voor ontwikkelaars en ontwerpers.



Het doel is om hardware- en software-integratie van hoge kwaliteit te bieden, vergelijkbaar met het Apple ecosysteem, maar volledig open en gecentreerd op Linux.



## Een modern, stabiel en toegankelijk systeem



Pop!OS bouwt voort op de fundamenten van Ubuntu, waardoor het een uitstekende stabiliteit, brede hardwarecompatibiliteit en toegang tot een enorm software-ecosysteem heeft.


Het biedt een elegante interface, de COSMIC desktop, ontworpen om vloeiend, intuïtief en aanpasbaar te zijn, zelfs voor nieuwe gebruikers.



## Een ideale keuze voor ontwikkelaars, ontwerpers en veeleisende gebruikers



Pop!OS wordt vooral gewaardeerd door :





- ontwikkelaars (vooraf geïnstalleerde tools, geavanceerd tegelbeheer),
- gebruikers met een Nvidia of AMD grafische kaart,
- studenten en professionals die op zoek zijn naar een betrouwbaar systeem,
- windows-gebruikers die eenvoudig willen overstappen.



Het bevat automatische betegeling, een overzichtelijk softwarecentrum en geïntegreerde productiviteitstools om het dagelijkse gebruik te vereenvoudigen.



## Pop!OS hoogtepunten





- Geoptimaliseerde prestaties** dankzij regelmatige updates.
- Twee ISO-versies beschikbaar**: standaard en Nvidia-geoptimaliseerd.
- Verbeterde beveiliging** (LUKS-codering beschikbaar bij installatie).
- Interface COSMIC** ergonomisch en modern.
- Zeer compatibel** met Ubuntu en Flatpak software.



## POP!OS veilig downloaden



### 1. Vereisten



Voordat u POP!OS downloadt en installeert, zijn er een paar dingen die u moet doen om de installatieomgeving correct voor te bereiden.



### Benodigde apparatuur





- Een compatibele computer**: Intel- of AMD-processor, Intel / AMD / Nvidia GPU.
- Minimaal 4 GB RAM** (8 GB aanbevolen voor comfortabel gebruik).
- minimaal 20 GB vrije ruimte** (40 GB of meer aanbevolen).
- Een USB-sleutel** van minimaal 4 GB om de installatiemedia te maken.



### Internetverbinding



Een stabiele verbinding is handig voor :





- download het ISO-image,
- updates installeren na de installatie.



Pop!OS kan zonder verbinding worden uitgevoerd, maar de installatie verloopt veel soepeler via internet.



### Back-up van gegevens



Als Pop!OS een ander systeem (Windows, Ubuntu, enz.) moet vervangen of er naast moet bestaan, is het raadzaam om een back-up te maken van belangrijke bestanden voordat u verder gaat.



### Controleer op de aanwezigheid van een Nvidia GPU (indien van toepassing)



Voor computers met een Nvidia grafische kaart moet je het speciale ISO-image downloaden dat de Nvidia-stuurprogramma's bevat.


Deze controle is heel eenvoudig:





- door de specificaties van de pc te raadplegen,
- of door het model van de grafische kaart op te zoeken in de systeeminstellingen.



### Downloaden van de officiële website



Het Pop!OS ISO-image kan rechtstreeks van de officiële System76-pagina worden gedownload: [system76.com/pop](https://system76.com/pop/).



Deze pagina biedt altijd de meest recente versie, aangepast aan je hardware.



![capture](assets/fr/03.webp)



### Kies versie: Standaard of Nvidia, of Raspberry Pi (ARM64)



Pop!OS is verkrijgbaar in drie varianten:



### Standaard versie



Aanbevolen voor computers met :





- intel- of AMD-processor;
- een geïntegreerde GPU van Intel of AMD;
- een AMD Radeon grafische kaart.



![Utilisation de Balena Etcher](assets/fr/04.webp)



### Nvidia-versie



Aanbevolen voor computers met een Nvidia grafische kaart.


Deze image bevat al Nvidia-stuurprogramma's, wat de installatie eenvoudiger maakt en grafische problemen vermindert.



![Utilisation de Balena Etcher](assets/fr/05.webp)



### Versie Raspberry Pi (ARM64)



Voor Raspberry Pi 4 en 400 (ARM-processor).


Aangepast aan de ARM-architectuur is dit een specifieke versie voor deze minicomputers.



![Utilisation de Balena Etcher](assets/fr/06.webp)



## Een opstartbare USB-sleutel maken



Je kunt verschillende hulpmiddelen gebruiken, zoals Balena Etcher :





- Download en installeer [Balena Etcher](https://etcher.balena.io/).



![Page de téléchargement Balena Etcher](assets/fr/07.webp)



![Installation de Balena Etcher](assets/fr/08.webp)





- Open Balena Etcher en selecteer de Pop!OS ISO-image.
- Selecteer USB-stick als doelmedium.
- Klik op Flash en wacht tot het proces is voltooid.



![Utilisation de Balena Etcher](assets/fr/09.webp)



## Pop!OS installeren en beveiligen



### Opstarten vanaf USB-sleutel





- Schakel de computer uit.
- Sluit de USB-sleutel (met Pop!OS) aan.
- Zet je computer aan. Op recente PC's zou het systeem de USB opstartsleutel automatisch moeten herkennen. Als dit niet het geval is, start dan opnieuw op door de BIOS/UEFI-toegangstoets ingedrukt te houden (meestal F2, F12 of Delete, afhankelijk van het merk).
  - Selecteer in het BIOS/UEFI-menu je USB-sleutel als opstartapparaat.
  - Opslaan en opnieuw opstarten.



### De installatie starten



Nadat u uw opstartbare USB-stick als opstartapparaat hebt geselecteerd, start uw computer op in een Pop!OS Live-omgeving.



Selecteer je taal.



![Capture](assets/fr/10.webp)



Selecteer een locatie.



![Capture](assets/fr/11.webp)



Selecteer een taal voor toetsenbordinvoer.



![Capture](assets/fr/12.webp)



Selecteer een toetsenbordindeling.



![Capture](assets/fr/13.webp)



Kies de `Clean Install` optie voor een standaard installatie. Dit is de beste optie voor nieuwe Linux-gebruikers, maar houd er rekening mee dat dan alle inhoud van de doelschijf wordt verwijderd. Je kunt ook `Probeer demo-modus` kiezen om Pop!OS in de live-omgeving te blijven testen.



![Capture](assets/fr/14.webp)



Selecteer `Custom (Advanced)` om GParted te openen. Met deze tool kun je geavanceerde functies configureren zoals dual booting, een aparte `/home` partitie aanmaken of de `/tmp` partitie op een andere schijf plaatsen.



Klik op `Erase and Install` om Pop!OS op de geselecteerde schijf te installeren.



![Capture](assets/fr/15.webp)



### Configuratie gebruikersaccount



Het volgende deel van het installatieprogramma leidt je door het aanmaken van een gebruikersaccount, zodat je kunt inloggen op je nieuwe besturingssysteem.



Geef een volledige naam op (dit kan een tekst naar keuze zijn, hoofdletters of kleine letters), evenals een gebruikersnaam (die in kleine letters moet zijn) :



![Capture](assets/fr/16.webp)



Zodra de account is aangemaakt, wordt u gevraagd een nieuw wachtwoord in te stellen.



![Capture](assets/fr/17.webp)



### Volledige schijfversleuteling



Versleuteling van de systeemschijf is niet noodzakelijk, maar het garandeert wel de veiligheid van gebruikersgegevens in het geval dat iemand ongeautoriseerde fysieke toegang tot het apparaat krijgt.



De schijf kan worden versleuteld met uw aanmeldwachtwoord door `Sleutelwachtwoord is hetzelfde als gebruikersaccountwachtwoord` aan te vinken. U kunt dit vakje ook uitschakelen en onderaan `Wachtwoord instellen` selecteren. Selecteer `Niet coderen` om de schijfcodering te negeren.



![Capture](assets/fr/18.webp)



Als je de knop `Wachtwoord instellen` hebt gekozen, zie je een extra vraag om je coderingswachtwoord in te stellen.



Ga door naar de volgende stap in het installatieprogramma. Pop!OS begint nu met de installatie op de schijf.



![Capture](assets/fr/19.webp)



Zodra de installatie is voltooid, start u uw computer opnieuw op en logt u in om de configuratie van de gebruikersaccount te voltooien.



Als u de opstartvolgorde hebt gewijzigd om prioriteit te geven aan uw Live USB-stick bij het opstarten, schakel de computer dan volledig uit en verwijder de installatie-USB-stick. Als u in dual-boot modus bent, druk dan op de juiste toetsen om de configuratie te openen en selecteer de schijf met de Pop!OS-installatie.



![Capture](assets/fr/20.webp)



### NVIDIA-afbeeldingen



Als je hebt geïnstalleerd vanaf Intel/AMD ISO en je systeem heeft een discrete NVIDIA grafische kaart, of als je er later een hebt toegevoegd, moet je handmatig de stuurprogramma's voor je kaart installeren om optimale prestaties te bereiken. Voer de volgende opdracht uit in een opdrachtterminal om het stuurprogramma te installeren:



```bash
sudo apt install system76-driver-nvidia
```



Je kunt ook NVIDIA grafische stuurprogramma's installeren vanuit de Pop!_Shop.



![Capture](assets/fr/20.webp)



## Essentiële gereedschappen installeren



Pop!OS biedt een breed scala aan software via de Pop!Shop, maar veel essentiële tools kunnen ook via de terminal worden geïnstalleerd met `apt` of `flatpak`. Hier lees je hoe je de belangrijkste tools voor een complete werkomgeving installeert.



### Installatie aansluitklemmen



| Outil                        | Description                                | Commande d’installation                         |
| ---------------------------- | ------------------------------------------ | ----------------------------------------------- |
| Firefox                      | Navigateur web libre et populaire          | `sudo apt install firefox`                      |
| Brave                        | Navigateur web axé sur la confidentialité  | Installation via Pop!_Shop ou site officiel     |
| Visual Studio Code (VS Code) | Éditeur de code puissant pour développeurs | `flatpak install flathub com.visualstudio.code` |
| Git                          | Gestionnaire de versions                   | `sudo apt install git`                          |
| Flatpak                      | Gestionnaire de paquets alternatif         | `sudo apt install flatpak`                      |
| VLC                          | Lecteur multimédia polyvalent              | `sudo apt install vlc`                          |
| GNOME Terminal               | Terminal par défaut                        | Préinstallé sur Pop!OS                          |
| Curl                         | Outil de transfert de données en ligne     | `sudo apt install curl`                         |
| Wget                         | Téléchargement de fichiers via HTTP/FTP    | `sudo apt install wget`                         |
| Docker                       | Conteneurisation d’applications            | Installation via script officiel ou `apt`       |
| Node.js                      | Environnement JavaScript côté serveur      | Installation via `apt` ou NodeSource            |
| Python3                      | Langage de programmation                   | `sudo apt install python3 python3-pip`          |
| GIMP                         | Éditeur d’image avancé                     | `sudo apt install gimp`                         |
| Thunderbird                  | Client mail                                | `sudo apt install thunderbird`                  |
| Transmission                 | Client BitTorrent léger                    | `sudo apt install transmission-gtk`             |
| Htop                         | Moniteur de système interactif             | `sudo apt install htop`                         |

### Installatie via Pop! Shop (grafische interface)





- Open **Pop!_Shop** vanuit het hoofdmenu.
- Gebruik de zoekbalk om de gewenste applicaties te vinden (bijvoorbeeld "Brave").
- Klik op **Installeren** voor elke toepassing.
- Pop!_Shop beheert automatisch afhankelijkheden en updates.



## Systeem bijwerken



### Optie 1: Via grafische gebruikersinterface (GUI)



Pop!OS heeft een eenvoudige, intuïtieve grafische updatemanager.



1. Klik op het **hoofdmenu** (pictogram linksonder).


2. Open **"Pop!_Shop"**.


3. Klik in de Pop!_Shop op het tabblad **"Updates"**.


4. Het systeem controleert automatisch of er updates beschikbaar zijn.


5. Klik op **"Alles bijwerken"** om de installatie van updates te starten.


6. Voer uw wachtwoord in als daarom wordt gevraagd.


7. Laat het proces beëindigen en start indien nodig opnieuw op.



### Optie 2: Via terminal



Open een terminal en typ :



```bash
# Mettre à jour la liste des paquets et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyer les paquets inutiles
sudo apt autoremove -y && sudo apt autoclean
```



### Gebruikersbeheer



We raden aan om een standaard gebruikersaccount met sudo-rechten te gebruiken voor de dagelijkse werkzaamheden.



Een nieuwe gebruiker aanmaken :



```bash
sudo adduser votrenom && sudo usermod -aG sudo votrenom
```



Log uit en log weer in met deze nieuwe gebruiker.



### Beheer van grafische stuurprogramma's





- Controleer voor Nvidia-kaarten of de eigen stuurprogramma's zijn geïnstalleerd:



```bash
sudo apt install system76-driver-nvidia
```





- Voor AMD/Intel worden stuurprogramma's meestal standaard meegeleverd.



### Firewall activeren (UFW)



Pop!OS blokkeert standaard geen netwerkverkeer. Activeer UFW om de beveiliging te verbeteren:



```bash
sudo ufw enable && sudo ufw status verbose
```



### Automatische updates configureren



Het systeem up-to-date houden zonder handmatige tussenkomst:



```bash
sudo apt install unattended-upgrades && sudo dpkg-reconfigure --priority=low unattended-upgrades
```



### Uiterlijk en gedrag aanpassen





- Open **Systeeminstellingen** → **Uiterlijk** om een licht of donker thema te kiezen.
- Configureer actieve hoeken, animaties en uitbreidingen via de COSMIC-manager.
- Pas de bureaubladindeling aan om je workflow te optimaliseren.



### Automatische back-up configureren



Pop!OS integreert tools zoals Deja Dup voor back-ups:





- Start **Backup** vanuit het menu.
- Kies een externe schijf of een netwerklocatie.
- Plan regelmatige back-ups.



### Nuttige GNOME/COSMIC-uitbreidingen installeren



Hier zijn een paar aanbevolen extensies om de gebruikerservaring te verbeteren:





- Dash to Dock**: toepassingsbalk altijd zichtbaar.
- GSConnect**: synchronisatie met Android.
- Klembordindicator**: geavanceerd klembordbeheer.



Installeer ze via :



```bash
sudo apt install gnome-shell-extensions
```



Activeer ze vervolgens in de instellingen.



### Geheugen- en swapbeheer optimaliseren



Controleer je ruilstatus:



```bash
swapon --show
```



Vergroot indien nodig de swapgrootte of configureer een wisselbestand:



```bash
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```



Voeg het toe aan het `/etc/fstab` bestand voor automatisch mounten.



## Beheer van pakketten en opslagplaatsen



### Pakketbronnen begrijpen



Pop!OS, gebaseerd op Ubuntu, gebruikt voornamelijk :





- Officiële Ubuntu** repositories: voor de meeste stabiele software.
- System76** repositories: voor stuurprogramma's, firmware en specifieke tools.
- Flatpak**: toegang tot een groot aantal sandboxed applicaties.
- Snap** (optioneel): een ander universeel pakketformaat.



---

### PPA-repositories toevoegen en beheren



Om vaak bijgewerkte software te installeren, kunnen bepaalde PPA's (Personal Package Archives) worden toegevoegd:



```bash
sudo add-apt-repository ppa:nom/ppa
sudo apt update
```



## Conclusie



Pop!OS is een moderne, stabiele Linux-distributie die geschikt is voor zowel beginners als gevorderden.



Dankzij de intuïtieve COSMIC interface en geïntegreerde tools biedt het een vloeiende en productieve ervaring, zowel voor ontwikkeling, creatie als dagelijks gebruik.



Deze handleiding behandelt de belangrijkste stappen: voorbereiding, downloaden, installatie, eerste instellingen en essentiële tools.



Voel je vrij om Pop!OS verder te verkennen en je omgeving aan te passen om er het meeste uit te halen.