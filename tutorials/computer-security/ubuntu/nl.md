---
name: Ubuntu
description: Complete handleiding voor het installeren en gebruiken van Ubuntu als alternatief voor Windows
---
![cover](assets/cover.webp)


## Inleiding


Een besturingssysteem (OS) is de belangrijkste software die alle bronnen van je computer beheert. Kiezen voor een alternatief besturingssysteem zoals Ubuntu kan veel voordelen bieden op het gebied van veiligheid, kosten en privacy.


### Waarom Ubuntu?




- Verbeterde beveiliging**: Linux-distributies staan bekend om hun veiligheid en robuustheid
- Geen kosten**: Ubuntu en de meeste Linux-distributies zijn gratis
- Grote gemeenschap**: Een gemeenschap van gebruikers die klaar staan om te helpen via forums en tutorials
- Respect voor privacy**: Open source systeem voor meer transparantie
- Eenvoud**: Gebruiksvriendelijke Interface en gebruiksgemak
- Rijk ecosysteem**: Uitgebreide catalogus van open source software
- Regelmatige ondersteuning**: Veilige updates van Canonical


## Installatie en configuratie


### 1. Vereisten


**vereiste uitrusting:**




- Een USB-sleutel van minstens 12 GB
- Een computer met minimaal 25 GB beschikbaar


### 2. Downloaden




- Ga naar [ubuntu.nl/download] (https://ubuntu.com/download)
- Kies de stabiele versie (LTS aanbevolen)
- ISO-afbeelding downloaden


![Page de téléchargement Ubuntu](assets/fr/01.webp)


![Sélection de la version Ubuntu](assets/fr/02.webp)


### 3. Een opstartbare USB-sleutel maken


Je kunt verschillende hulpmiddelen gebruiken, zoals Balena Etcher:




- Download en installeer [Balena Etcher] (https://etcher.balena.io/)


![Page de téléchargement Balena Etcher](assets/fr/03.webp)


![Installation de Balena Etcher](assets/fr/04.webp)




- Open Balena Etcher en selecteer de Ubuntu ISO-afbeelding
- Selecteer USB-stick als doelmedium
- Klik op Flash en wacht tot het proces is voltooid


![Utilisation de Balena Etcher](assets/fr/05.webp)


### 4. Ubuntu installeren en beveiligen


**4.1 Opstarten vanaf USB-geheugenstick** (in het Frans)




- Schakel de computer uit
- Sluit de USB-sleutel aan (met Ubuntu)
- Zet je computer aan. Op recente PC's zou het systeem de USB opstartsleutel automatisch moeten herkennen. Als dit niet het geval is, start dan opnieuw op door de BIOS/UEFI-toegangstoets ingedrukt te houden (meestal F2, F12 of Delete, afhankelijk van het merk)
 - Selecteer in het BIOS/UEFI-menu je USB-sleutel als opstartapparaat
 - Opslaan en opnieuw opstarten


**4.2 De installatie starten** (in het Frans)


**Opstartscherm**


Bij het opstarten vanaf de USB-sleutel zie je dit scherm, waarmee je Ubuntu kunt starten.


![Écran de démarrage Ubuntu](assets/fr/06.webp)


**Keuze van taal


Kies de taal van je voorkeur voor de installatie en het systeem.


![Sélection de la langue](assets/fr/07.webp)


**Toegankelijkheidsopties


Configureer toegankelijkheidsopties indien nodig (schermlezer, hoog contrast, enz.).


![Options d'accessibilité](assets/fr/08.webp)


**Configuratie toetsenbord


Selecteer je toetsenbordindeling. Er is een testveld beschikbaar om te controleren of de toetsen overeenkomen met je configuratie.


![Configuration du clavier](assets/fr/09.webp)


**Netwerkverbinding**


Maak verbinding met je Wi-Fi- of bekabelde netwerk om updates te downloaden tijdens de installatie.


![Configuration réseau](assets/fr/10.webp)


**Type installatie


Kies tussen "Ubuntu proberen" (om te testen zonder te installeren) of "Ubuntu installeren".


![Choix du type d'installation](assets/fr/11.webp)


**Installatiemethode


Selecteer interactieve installatie.


![Mode d'installation](assets/fr/12.webp)


**Toepassingsselectie


Kies tussen de standaardinstallatie of een uitgebreide selectie van applicaties.


![Sélection des applications](assets/fr/13.webp)


**Toepassingen van derden


Beslis of je wel of geen extra stuurprogramma's en bedrijfseigen software wilt installeren.


![Installation applications tierces](assets/fr/14.webp)


**Type partitionering


Je hebt twee opties:




- "Wis schijf en installeer Ubuntu": gebruikt de hele schijf voor Ubuntu
- "Handmatige installatie: maak een dual boot met Windows of pas je partities aan


![Choix du partitionnement](assets/fr/15.webp)


**Account aanmaken


Stel je gebruikersnaam en wachtwoord in voor je Ubuntu-account.


![Création du compte](assets/fr/16.webp)


**Tijdzone


Selecteer je geografische gebied om de systeemtijd in te stellen.


![Sélection du fuseau horaire](assets/fr/17.webp)


**Installatieoverzicht**


Controleer al je keuzes voordat je de uiteindelijke installatie start. Zodra je op "Installeren" klikt, begint het proces.


![Résumé de l'installation](assets/fr/18.webp)


**4.3 Ubuntu upgraden na installatie** (in het Frans)


Je systeem updaten is een belangrijke stap na een nieuwe installatie. Je hebt twee opties:


**Optie 1: Via de grafische gebruiker Interface**




- Zoek naar "Software en updates" in het menu Toepassingen
- De applicatie controleert automatisch op beschikbare updates
- Volg de instructies op het scherm om de updates te installeren


**Optie 2: Via terminal




- Terminal openen (Ctrl + Alt + T)
- Typ de volgende opdracht om te controleren op beschikbare updates:


```bash
sudo apt update
```




- Voer je wachtwoord in wanneer daarom wordt gevraagd
- Om updates te installeren, typt u:


```bash
sudo apt upgrade
```




- Bevestig de installatie door 'Y' te typen en vervolgens Enter


### 5. Basistaken ontdekken


**5.1 Surfen op internet


Standaard staat Firefox vaak in de startbalk.


Start Firefox en begin met browsen.


Andere browsers (Chrome, Brave, enz.) kunnen worden geïnstalleerd via de Software Manager of via .deb-pakketten.


**5.2 Tekstverwerking


Ubuntu wordt geleverd met de LibreOffice-suite (Writer voor tekstverwerking).


Om het te openen: Activiteiten > Zoeken naar "LibreOffice Writer" of klik op het pictogram als het in de balk verschijnt.


Je kunt documenten in verschillende indelingen (waaronder .docx) maken, bewerken en opslaan.


**5.3 Toepassingen installeren


Software manager (genaamd "Ubuntu Software"): grafische Interface voor het zoeken en installeren van applicaties.


Gebruik in Terminal het commando:


```bash
sudo apt install nom-du-paquet
```


Voorbeeld:


```bash
sudo apt install vlc
```


### 6. Conclusie en aanvullende bronnen


Nu ben je klaar om Ubuntu dagelijks te gebruiken: je systeem beveiligen, browsen, kantoorwerk doen, software installeren en je OS up-to-date houden!


Om de veiligheid van je digitale leven een stap verder te brengen, raden we je aan om eens te kijken naar onze versleutelde berichtendienst, die perfect geschikt is om je privacy te beschermen en je Ubuntu-installatie aanvult:


https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2