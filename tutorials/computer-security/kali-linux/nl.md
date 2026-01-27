---
name: Kali
description: Kali Linux installeren op VirtualBox, als opstartbare USB-stick of als dual boot, stap voor stap.
---

![cover-kali](assets/cover.webp)



## Inleiding



### Waarom Kali Linux?



**Kali Linux** is een Linux-distributie gespecialiseerd in IT-beveiliging.


Dit is waarom we Kali Linux gebruiken:





- Het is vooraf geconfigureerd met een breed scala aan pentesting tools (systeem- en netwerkbeveiligingstests).
- Het is **open source en vrij**, dus je kunt het vrij gebruiken en aanpassen.
- Het is **betrouwbaar en veilig**, ideaal om te leren over cyberbeveiliging.
- Hiermee kun je Linux leren gebruiken in een testklare omgeving.
- Het kan op verschillende manieren worden geïnstalleerd: **VirtualBox**, **opstartbare USB-sleutel**, of **dual boot**.



## Installatie en configuratie



### 1. Vereisten



**vereiste uitrusting:**





- 64-bits processor** (Intel of AMD).
- minimaal 8 GB RAM** (4 GB kan voldoende zijn voor een lichte installatie of VM).
- 50 GB vrije schijfruimte** om Kali Linux te installeren.
- Internetverbinding** om ISO image en updates te downloaden.
- Een USB-sleutel van minimaal 8 GB** om opstartbare media te maken (als je Kali op een PC wilt installeren of wilt testen op Live USB).



Het is belangrijk om een back-up van je gegevens te maken voordat je op een bestaande pc installeert.



### 2. Downloaden





- Ga naar [kali.org/get-kali](https://www.kali.org/get-kali/#kali-platforms)
- Selecteer het ISO-image voor je toepassing:
  - Install Image** : voor installatie op de pc.
  - Virtual Image**: om Kali op VirtualBox of VMware te installeren.
- Download de ISO-afbeelding.



![Page de téléchargement Kali](assets/fr/01.webp)



![Sélection de la version Kali](assets/fr/02.webp)



### 3. Een opstartbare USB-sleutel maken



Je kunt verschillende hulpmiddelen gebruiken, zoals Balena Etcher :





- Download en installeer [Balena Etcher](https://etcher.balena.io/).



![Page de téléchargement Balena Etcher](assets/fr/03.webp)



![Installation de Balena Etcher](assets/fr/04.webp)





- Open Balena Etcher en selecteer de Kali ISO image.
- Selecteer USB-stick als doelmedium.
- Klik op Flash en wacht tot het proces is voltooid.



![Utilisation de Balena Etcher](assets/fr/05.webp)



### 4. Kali Linux installeren en beveiligen



#### 4.1 Opstarten op de USB-stick





- Schakel de computer uit.
- Sluit de USB-sleutel aan (met Kali Linux).
- Zet je computer aan. Op recente PC's zou het systeem de USB opstartsleutel automatisch moeten herkennen. Als dit niet het geval is, start dan opnieuw op door de BIOS/UEFI-toegangstoets ingedrukt te houden (meestal F2, F12 of Delete, afhankelijk van het merk).
  - Selecteer in het BIOS/UEFI-menu je USB-sleutel als opstartapparaat.
  - Opslaan en opnieuw opstarten.



#### 4.2 De installatie starten



##### Opstartscherm



Bij het opstarten vanaf de USB-stick zou het Kali Linux opstartscherm moeten verschijnen. Kies tussen **grafische installatie** en **tekstinstallatie**. In dit voorbeeld hebben we gekozen voor grafische installatie.



![capture](assets/fr/06.webp)



Als je de **Live** image gebruikt, zie je een andere modus, **Live**, die ook de standaard opstartoptie is.



![Mode Live](assets/fr/07.webp)



##### Taalkeuze



Kies de taal van je voorkeur voor de installatie en het systeem.



![Sélection de la langue](assets/fr/08.webp)



Geef uw geografische locatie aan.



![Options d'accessibilité](assets/fr/09.webp)



##### Configuratie toetsenbord



Selecteer je toetsenbordindeling. Er is een testveld beschikbaar om te controleren of de toetsen overeenkomen met je configuratie.



![Configuration du clavier](assets/fr/10.webp)



##### Netwerkverbinding



De installatie scant nu je netwerkinterfaces, zoekt naar een DHCP-service en vraagt je dan om een hostnaam voor je systeem in te voeren. In het onderstaande voorbeeld hebben we **"kali"** als hostnaam ingevoerd.



![Configuration réseau](assets/fr/11.webp)



Je kunt optioneel een standaard domeinnaam opgeven die dit systeem zal gebruiken (waarden kunnen worden opgehaald bij DHCP of als er een bestaand besturingssysteem is).



![Choix du type d'installation](assets/fr/12.webp)



##### Gebruikersaccounts



Maak vervolgens de gebruikersaccount voor het systeem aan (volledige naam, gebruikersnaam en een sterk wachtwoord).



![Création d'un utilisateur](assets/fr/13.webp)



![Mode d'installation](assets/fr/14.webp)



![Sélection des applications](assets/fr/15.webp)



##### Tijdzone



Selecteer je geografische gebied om de systeemtijd in te stellen.



![Sélection du fuseau horaire](assets/fr/16.webp)



##### Type partitionering



Het installatieprogramma scant vervolgens je schijven en geeft verschillende opties weer, afhankelijk van je configuratie.



In deze handleiding beginnen we met een **blanke schijf**, wat **vier mogelijke keuzes** oplevert.


We gaan **Geleid - gebruik gehele schijf** selecteren, omdat we hier een eenmalige installatie van Kali Linux uitvoeren (single boot). Dit betekent dat er geen ander besturingssysteem wordt bewaard en dat de hele schijf kan worden gewist.



Als uw schijf al gegevens bevat, kan een extra optie **Geleid - gebruik de grootste aaneengesloten vrije ruimte** worden weergegeven.



Met dit alternatief kun je Kali Linux installeren zonder bestaande gegevens te verwijderen, waardoor het ideaal is voor dual booting met een ander systeem.



In ons geval is de schijf leeg, dus deze optie verschijnt niet.



![Choix du partitionnement](assets/fr/17.webp)



Selecteer de schijf die moet worden gepartitioneerd.



![capture](assets/fr/18.webp)



Afhankelijk van je behoeften kun je ervoor kiezen om al je bestanden in één partitie te houden (standaard gedrag) of aparte partities te hebben voor één of meer mappen op het hoogste niveau.



Als je niet zeker weet wat je wilt, kies dan de optie **Alle bestanden op één partitie**.



![capture](assets/fr/19.webp)



![capture](assets/fr/20.webp)



Je krijgt dan nog een laatste kans om je schijfconfiguratie te controleren voordat het installatieprogramma onomkeerbare wijzigingen aanbrengt. Zodra je op _Continue_ hebt geklikt, start het installatieprogramma en is de installatie bijna voltooid.



![capture](assets/fr/21.webp)



##### Versleuteld LVM



Als deze optie was ingeschakeld in de vorige stap, zal Kali Linux nu een beveiligde harde schijf wissen voordat je om een LVM wachtwoord wordt gevraagd.



Gebruik een sterk wachtwoord, anders verschijnt er een waarschuwing over een zwakke passphrase.



##### Volmacht informatie



Kali Linux gebruikt repositories om applicaties te distribueren. Je moet de nodige proxy-informatie invoeren als je omgeving er een gebruikt.



Als je **niet zeker** weet of je een proxy moet gebruiken, **laat dan leeg**. Als je onjuiste informatie invoert, kun je geen verbinding maken met de archieven.



![capture](assets/fr/22.webp)



##### Metapets



Als de netwerktoegang niet is geconfigureerd, moet u **verdere configuratie** uitvoeren wanneer daarom wordt gevraagd.



Als u de **Live** afbeelding gebruikt, wordt de volgende stap niet weergegeven.



Je kunt dan de [metapackages](https://www.kali.org/docs/general-use/metapackages/) selecteren die je wilt installeren. De standaardopties installeren een standaard Kali Linux systeem, dus je hoeft niets aan te passen.



![capture](assets/fr/23.webp)



#### Opstartinformatie



Bevestig vervolgens de installatie van de GRUB bootloader.



![capture](assets/fr/24.webp)



##### Herstart



Klik ten slotte op Doorgaan om je nieuwe Kali Linux installatie opnieuw op te starten.



![capture](assets/fr/25.webp)



#### 4.3 Kali Linux bijwerken en configureren na de installatie



Je systeem updaten is een belangrijke stap na een nieuwe installatie. Je hebt twee opties:



##### Optie 1: Via grafische gebruikersinterface (GUI)



Kali biedt net als Debian/Ubuntu een geïntegreerde grafische updatemanager.



1. Klik op het **hoofdmenu** (linksboven of onderaan, afhankelijk van je bureaublad).


2. Open **"Software Updater"**.


3. Het gereedschap zal :




    - Controleer de pakketten die moeten worden bijgewerkt.
    - Je ziet een lijst (met maten en versies).
    - Hiermee kun je de update starten met één klik.


4. Voer uw beheerderswachtwoord (`sudo`) in wanneer daarom wordt gevraagd.


5. Laat het installeren en herstart indien nodig.



##### Optie 2: Via terminal



Open een terminal en voer :



```bash
# Mettre à jour les dépôts et le système
sudo apt update && sudo apt full-upgrade -y

# Nettoyage
sudo apt autoremove -y && sudo apt autoclean
```



Het is niet aan te raden om de **root** account te gebruiken voor dagelijks werk; maak in plaats daarvan een niet-root gebruiker aan.



Typ deze commando's in uw terminal:



```bash
sudo adduser yourname
sudo usermod -aG sudo yourname
```



Log uit en log opnieuw in met de nieuwe gebruiker.



Laten we een aantal basistaken van Kali Linux samenvatten in een tabel.



### Basistaken onder Kali Linux




| **Categorie** | **Basistaak** | **Beschrijving / Doel** | **Hoofdmethode** |
| -------------------------- | -------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| **Systeemnavigatie** | Terminal openen | Toegang krijgen tot de belangrijkste commandoregel van Kali | Klik op het terminalpictogram of gebruik `Ctrl + Alt + T` |
| | Mappen doorzoeken | Navigeren door de directorystructuur van het systeem | `cd /pad/naar/map`, `ls` om bestanden op te sommen |
| | Map aanmaken / verwijderen | Bestanden organiseren | `mkdir mapnaam`, `rm -r mapnaam` |
| **Bestandsbeheer** | Bestand kopiëren / verplaatsen | Bestanden manipuleren in de terminal | `cp bestand bestemming`, `mv bestand bestemming` |
| | Bestand verwijderen | Schijfruimte vrijmaken | `rm bestandsnaam` |
| | Inhoud van een tekstbestand tonen | Snel een bestand lezen | `cat bestand.txt`, `less bestand.txt` |
| **Systeembeheer** | Kali Linux bijwerken | Installeer de laatste versies en beveiligingspatches | `sudo apt update && sudo apt full-upgrade -y` |
| | Software installeren | Een nieuwe tool of hulpprogramma toevoegen | `sudo apt install pakketnaam` |
| | Software verwijderen | Het systeem opschonen | `sudo apt remove pakketnaam` |
| | Onnodige afhankelijkheden opschonen | Schijfruimte winnen | `sudo apt autoremove` |
| **Netwerk en Internet** | Netwerkverbinding controleren | Toegang tot internet testen | `ping google.com` |
| | IP-adres identificeren | Uw netwerkconfiguratie kennen | `ip a` of `ifconfig` |
| | Van Wi-Fi-netwerk wisselen | Verbinden met een ander toegangspunt | Netwerkpictogram → Selecteer de gewenste Wi-Fi |
| **Accounts en machtigingen** | Een beheerderscommando uitvoeren | Tijdelijk root-rechten verkrijgen | `sudo commando` |
| | Nieuwe gebruiker aanmaken | Een lokaal account toevoegen | `sudo adduser gebruikersnaam` |
| | Wachtwoord wijzigen | Een account beveiligen | `passwd` |
| **Uiterlijk en comfort** | Achtergrond wijzigen | Het bureaublad personaliseren | Rechtermuisklik op het bureaublad → **Bureaubladinstellingen** |
| | Thema / pictogrammen wijzigen | Leesbaarheid en esthetiek verbeteren | Instellingen → Uiterlijk / Thema's |
| **Kali Tools** | Toolmenu openen | Test- en beveiligingstools verkennen | Menu **Toepassingen → Kali Linux** |
| | Een tool starten (bijv: nmap, wireshark) | Praktische ontdekking van beveiligingshulpprogramma's | `sudo nmap`, `wireshark`, enz. |
| **Hulp en documentatie** | Hulp krijgen bij een commando | Een commando begrijpen voordat u het gebruikt | `man commando` of `commando --help` |

## Conclusie



Het installeren van Kali Linux is slechts de eerste stap in het ontdekken van deze krachtige omgeving gewijd aan cyberbeveiliging. Door de basistaken en het systeembeheer onder de knie te krijgen, kan iedereen beginnen met het verkennen van de ingebouwde tools en de innerlijke werking van een Linux-systeem begrijpen. Kali biedt een uitstekend leerplatform, zowel voor het versterken van technische vaardigheden als voor het ontwikkelen van een echte cultuur van IT-beveiliging.