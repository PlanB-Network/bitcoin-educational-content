---
name: Debian
description: Een Linux-distributie die bekend staat om zijn stabiliteit, robuustheid en compatibiliteit.
---

![cover](assets/cover.webp)



Debian is een vrije GNU/Linux-distributie die bekend staat om zijn robuustheid en betrouwbaarheid. De Linux-kernel en alle pakketten zijn uitvoerig getest om een rotsvaste stabiliteit en een hoog beveiligingsniveau te garanderen. Debian is geschikt voor zowel servers als werkstations en biedt een gebruiksvriendelijke ervaring en een uitgebreide softwarecatalogus. Of u nu op zoek bent naar een veilig systeem voor dagelijks gebruik of voor een productieomgeving, Debian is de juiste keuze.



## Waarom Debian kiezen?





- Gratis en open**: Debian is volledig open source, waardoor transparantie en geen licentiekosten gegarandeerd zijn.
- Stabiliteit en veiligheid**: elke release ondergaat een grondig testproces, waardoor Debian een van de meest betrouwbare en veilige distributies op de markt is.
- Actieve community**: een uitgebreide community en uitgebreide documentatie zijn beschikbaar om je te ondersteunen wanneer je dat nodig hebt.
- Lichtgewicht en schaalbaar**: u kunt Debian installeren op machines met bescheiden middelen met behoud van goede prestaties.
- Uitgebreide software catalogus**: meer dan 50.000 officiële pakketten zijn beschikbaar via de repositories.



## Kies een Interface grafiek



Debian biedt verschillende bureaubladomgevingen die aan uw wensen voldoen:





- GNOME**: moderne, intuïtieve Interface, ideaal voor beginners. Het biedt een vloeiend, eenvoudig te gebruiken grafisch menu voor toegang tot toepassingen.
- XFCE**: licht en snel, perfect voor minder krachtige machines.
- KDE Plasma**: zeer aanpasbaar, met een Windows-achtig uiterlijk.
- Cinnamon**: eenvoudige, elegante Interface, geïnspireerd op Windows.
- LXDE / LXQt**: ultralicht, geschikt voor oudere computers.
- MATE**: eenvoudig en klassiek, dicht bij het oude GNOME.



💡 Voor een comfortabele, gemakkelijk vast te houden ervaring wordt **GNOME sterk aanbevolen**.



## Debian installeren en configureren


### Hardwarevereisten



Controleer voordat u met de installatie begint of u over de volgende apparatuur beschikt:





- USB-sleutel**: minimaal 8 GB voor het opstartbare ISO-image.
- Random Access Memory (RAM)**: 4 GB voor probleemloze installatie en werking.
- Schijfruimte**: minstens 15 GB vrije ruimte voor het systeem en updates.



### Downloaden



De keuze van het Debian image hangt af van de architectuur van uw processor:





- AMD64**: download de "live hybride" editie van de [download] lijst (https://debian.obspm.fr/debian-cd/12.11.0-live/amd64/iso-hybrid/).
- ARM64**: haal het DVD-image van de officiële [Debian] website (https://debian.obspm.fr/debian-cd/12.11.0/arm64/iso-dvd/).
- Andere architecturen**: zoek de ISO die overeenkomt met jouw architectuur [hier] (https://debian.obspm.fr/debian-cd/12.11.0/).



![download](assets/fr/01.webp)



### Een opstartbare USB-sleutel maken



Zodra je de juiste ISO-image hebt gedownload, kun je doorgaan met het maken van je installatiemedia:




- Download Balena Etcher** van de [officiële website] (https://etcher.balena.io/), haal dan de binary voor jouw systeem op en installeer het.



![etcher](assets/fr/02.webp)





- Start Etcher**: open de software en selecteer het eerder gedownloade Debian ISO-image.
- Kies de USB-sleutel**: geef je sleutel (8 GB+) op als doel.
- Start flash**: klik op **Flash!** en wacht tot het proces is voltooid.



![flash](assets/fr/03.webp)



Uw USB-stick is nu klaar om Debian te installeren.



## Debian installeren op uw systeem



### Opstarten vanaf USB-sleutel



Om de installatie vanaf uw USB-sleutel te starten:




- Schakel** de computer volledig uit.
- Herstart** en open BIOS/UEFI door onmiddellijk op `ESC`, `F2`, `F11` te drukken (of de speciale toets afhankelijk van je merk).
- Selecteer in het opstartmenu **uw USB-sleutel** als opstartapparaat.
- Bevestig** met de Enter-toets om het Debian-image te starten: dit brengt u naar het welkomstscherm van het installatieprogramma.



### De installatie starten



Startscherm:



![starting](assets/fr/04.webp)



Bij het opstarten vanaf de USB-stick biedt het welkomstscherm van Debian verschillende opties:




- Live Systeem**: start Debian op zonder het te installeren, ideaal om de omgeving te testen.
- Start Installer**: start de installatie direct op de Hard schijf.
- Geavanceerde installatieopties**: geeft je toegang tot aangepaste installatiemodi.



Om Debian in live modus te verkennen, selecteert u **Live System** en bevestigt u met **Enter**. Vervolgens kunt u de installatie starten door te klikken op **Installeer Debian** in de live omgeving.



![system](assets/fr/05.webp)





- Taalkeuze** (optioneel)



Selecteer de hoofdtaal van uw Debian-systeem uit de lijst en klik op OK.



![language](assets/fr/06.webp)





- Tijdzone** (GMT)



Kies je geografische zone om automatisch de datum en tijd in te stellen.



![timezone](assets/fr/07.webp)





- Toetsenbordindeling



Selecteer de taal en indeling van je toetsenbord. Gebruik het ingebouwde testveld om te controleren of elke toets het verwachte teken produceert.



![keyboard](assets/fr/08.webp)



### Schijfpartitionering





- Schijf wissen**: als u een speciale partitie hebt, verwijdert deze optie alle inhoud.
- Handmatig partitioneren**: kies deze optie om naar wens partities aan te maken, te verkleinen of te verwijderen.



![disk](assets/fr/09.webp)





- Een gebruikersaccount maken



Voer je volledige naam, accountnaam en een sterk wachtwoord in om ervoor te zorgen dat je sessie veilig is.



![user](assets/fr/10.webp)





- Parameteroverzicht**



Er wordt een overzicht van uw keuzes weergegeven: controleer elk item en ga terug om te wijzigen indien nodig.



![settings](assets/fr/11.webp)





- De installatie starten



Klik op **Installeren** om te beginnen met het kopiëren van bestanden en het configureren van het systeem.



![install](assets/fr/12.webp)





- Herstart**



Zodra de installatie is voltooid, herstart u de computer om alle configuraties toe te passen en toegang te krijgen tot uw nieuwe Debian-systeem.



![restart](assets/fr/13.webp)



Voer bij het opstarten de gebruikersnaam en het wachtwoord in om toegang te krijgen tot het systeem.



![login](assets/fr/14.webp)



## Systeem bijwerken



Voordat je je systeem gaat gebruiken, is het essentieel om het bij te werken. Hierdoor kun je profiteren van de nieuwste softwarepatches, bijgewerkte repositories en in sommige gevallen beveiligingspatches voor het besturingssysteem zelf.



### Optie 1: Bijwerken via grafische Interface (GNOME)



Als u Debian heeft geïnstalleerd met de GNOME desktopomgeving, kunt u updates grafisch uitvoeren. Open hiervoor het programma **Software** en ga naar het tabblad **Updates**. Klik vervolgens op **Opnieuw opstarten en bijwerken** om het proces te starten.



### Optie 2: Update via terminal (aanbevolen)



Deze methode biedt meer volledige controle. Je kunt repositories, softwarepakketten en, indien nodig, de kernel bijwerken.




- Open de terminal met de sneltoets `Ctrl + Alt + T`.
- Werk de lijst met beschikbare pakketten bij met het volgende commando:



```shell
sudo apt update
```



Voer je wachtwoord in wanneer daarom wordt gevraagd (merk op dat er geen tekens worden weergegeven terwijl je typt - dit is normaal).





- Beschikbare updates installeren:



```shell
sudo apt full-upgrade
```



## Ontdek de basistaken



### Surfen op internet



De standaard webbrowser op Debian is **Firefox**. Als u de voorkeur geeft aan een andere browser, kunt u een andere installeren, mits deze beschikbaar is in de Debian repositories (zoals Chromium, Brave...).



### Tekstverwerking



De **LibreOffice** suite is standaard geïnstalleerd op Debian.





- Om documenten te schrijven gebruik je **LibreOffice Writer**, het equivalent van Microsoft Word.
- Voor spreadsheets werkt **LibreOffice Calc** als een alternatief voor Excel.
- Tot slot kun je met **LibreOffice Impress** presentaties maken, net als PowerPoint.



## Toepassingen installeren



Er zijn twee manieren om applicaties te installeren op Debian:



### Grafische methode:



Je kunt de **software manager** (toegankelijk via de grafische Interface) gebruiken om eenvoudig toepassingen te zoeken en te installeren.



### Opdrachtregelmethode:



Als de toepassing die je zoekt niet verschijnt in de grafische Interface, of als je de voorkeur geeft aan de terminal, gebruik dan het volgende commando:



```shell
sudo apt install <name>
```



Vervang `<name>` door de naam van het pakket. Om bijvoorbeeld `curl` te installeren:



```shell
sudo apt install curl
```



### Een handmatig gedownload pakket installeren:



Als je een `.deb` bestand (Debian pakket) hebt gedownload, kun je het installeren met het volgende commando:



```shell
sudo apt install ./name.deb
```



https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af

Uw Debian-systeem is nu geïnstalleerd en klaar voor gebruik voor uw dagelijkse taken.


Dankzij de **GNOME** bureaubladomgeving heb je toegang tot een groot aantal toepassingen via een gebruiksvriendelijke grafische Interface, ideaal voor zowel beginners als gevorderden.



Het is ook mogelijk om uw bureaubladomgeving te veranderen (bijvoorbeeld naar XFCE, KDE, etc.) zonder Debian opnieuw te installeren. Om dit te doen, gebruikt u gewoon de terminal en installeert u de nieuwe omgeving van uw keuze.



Om meer te leren over Debian, en meer in het algemeen over GNU/Linux distributies, raad ik je aan deze cursus te raadplegen:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1