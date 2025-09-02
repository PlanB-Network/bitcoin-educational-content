---
name: Fedora
description: De Linux-distributie die je voorziet van een gratis, complete en veilige werkruimte.
---


![cover](assets/cover.webp)





Fedora is een vrij, open-source Linux-gebaseerd besturingssysteem gelanceerd in 2003, ontwikkeld door de **Fedora Project** gemeenschap en ondersteund door **Red Hat Linux**. Het staat bekend om zijn stabiliteit, goede prestaties en gebruiksgemak, waardoor het een uitstekende keuze is voor zowel beginners als gevorderde gebruikers. Het systeem draait op de meeste moderne processor architecturen, waardoor het gemakkelijk te installeren is op vrijwel elke computer. Fedora is ook beschikbaar in verschillende voorgeconfigureerde edities, genaamd "Fedora Spins" of "Fedora Editions", ontworpen voor specifieke behoeften (videospellen, astronomie, ontwikkeling...).



## Fedora Linux architectuur



Zoals je eerder hebt gelezen, is Fedora een vrij besturingssysteem gebaseerd op de Linux kernel. De Linux kernel is het deel van het besturingssysteem dat communiceert met de computer hardware en systeembronnen zoals geheugen en rekenkracht beheert.



Fedora Linux bevat een verscheidenheid aan software gereedschappen en applicaties die nodig zijn om het besturingssysteem bovenop de Linux kernel te draaien. Fedora's modulaire architectuur betekent dat het voornamelijk bestaat uit een verzameling van individuele componenten die gemakkelijk kunnen worden toegevoegd, verwijderd of vervangen als dat nodig is. Hierdoor kun je het besturingssysteem vormgeven met alleen de middelen die je nodig hebt.



Fedora bevat ook een desktop omgeving, dat is de Interface waarmee gebruikers taken uitvoeren en toegang hebben tot applicaties. Fedora's standaard bureaublad omgeving is GNOME, een gebruikersvriendelijke, eenvoudig te gebruiken en zeer aanpasbare bureaublad omgeving.



## Waarom kiezen voor Fedora?



Onder de vele Linux distributies die beschikbaar zijn, valt Fedora in het bijzonder op door:





- Modulariteit**: Fedora is compatibel met verschillende processor architecturen en kan geïnstalleerd worden op de meeste computers, zelfs computers met weinig vermogen, en past zich perfect aan aan je behoeften.





- Een eenvoudige, intuïtieve Interface**: Fedora combineert een moderne grafische Interface met een krachtige opdrachtregel Interface, waardoor het eenvoudig te gebruiken is voor alle profielen.





- Kernel stabiliteit**: Fedora is gebaseerd op Red Hat en staat bekend om de betrouwbaarheid van zijn updates, vooral kernel updates, die zonder grote bugs worden uitgevoerd dankzij gratis bijdragen van een grote gemeenschap.





- Snelle, eenvoudige installatie**: met een image van slechts 3 GB is de installatie snel en eenvoudig, zelfs op machines met beperkte bronnen.



## Fedora edities



Afhankelijk van je profiel en gebruik, biedt Fedora edities die passen bij je behoeften. Je zult voornamelijk:





- Fedora Workstation**: Ideaal voor persoonlijk en/of professioneel gebruik op uw computers, deze editie is geïnstalleerd met algemene hulpprogramma's zoals browsers, een kantoorpakket (tekstverwerkers) en software voor het afspelen van media.





- Fedora Server**: Deze editie is gewijd aan server management. Fedora Server bevat een verscheidenheid aan gereedschappen om je te helpen servers op je eigen schaal in te zetten en te beheren.





- Fedora CoreOS**: Wil je eenvoudig cloud applicaties draaien en inzetten? Fedora CoreOS is de editie die je de tools geeft om images te maken en te beheren met bijvoorbeeld Docker en Kubernets.



In deze tutorial nemen we de Fedora Workstation editie voor onze rekening. Echter, de hieronder beschreven processen zijn vergelijkbaar voor de andere edities.



## Fedora Workstation installeren en configureren



Het installeren van Fedora Workstation vereist de volgende hardware configuratie:




- Een USB-sleutel van minstens **8 GB** om het besturingssysteem op te starten.
- Ten minste **40 GB vrije ruimte** op de Hard schijf van je computer.
- 4 GB RAM** voor een soepele ervaring.



### Fedora Werkstation downloaden



Je kunt de [Fedora Workstation] editie (https://fedoraproject.org/fr/workstation/download) downloaden van de officiële Fedora project website. Selecteer dan de versie die overeenkomt met je processorarchitectuur (32-bit - 64-bit) en klik op het **Download** icoon.



![download](assets/fr/01.webp)



![telecharger](assets/fr/02.webp)


### Een opstartbare USB-sleutel maken



Om Fedora te installeren, moet je een opstartbare USB sleutel maken met software zoals [Balena Etcher](https://etcher.balena.io/).



![flashOs](assets/fr/03.webp)



![flash](assets/fr/04.webp)



Zodra je klaar bent met de installatie van Balena Etcher, open de applicatie en selecteer de gedownloade Fedora Workspace ISO image. Selecteer je USB sleutel als doelmedium en klik op de **Flash** knop om te beginnen met het maken van de opstartbare sleutel.



![boot](assets/fr/05.webp)


### Fedora installeren



Schakel de computer uit wanneer u klaar bent met het opstarten van de USB-stick.


Schakel je computer in en open het BIOS tijdens het opstarten door op de `F2`, `F12` of `ESC` toets te drukken, afhankelijk van je computer.



Selecteer in de opstartopties je USB-sleutel als het primaire opstartapparaat. Door deze keuze te bevestigen, zal je computer herstarten en automatisch het Fedora installatieprogramma** starten dat op de USB-sleutel staat.



Zodra de computer is opgestart vanaf de USB-stick, verschijnt het **GRUB-scherm**.



In dit stadium heb je de volgende opties:




- Test media**: Met deze optie kunt u de integriteit van de USB-stick controleren en ervoor zorgen dat alle afhankelijkheden die nodig zijn voor een correcte installatie aanwezig zijn. Dit is een optionele stap, maar aanbevolen als u twijfels hebt over de USB-stick.



![install](assets/fr/06.webp)



![testing](assets/fr/07.webp)





- Start Fedora**: Dit start Fedora in "live" modus, zonder installatie.



Op het Fedora bureaublad (live modus), klik op **Installeer Fedora** (of Installeer op Hard schijf) om het installatieproces te starten. Je kunt ervoor kiezen om later te installeren en Fedora te testen zonder het te installeren.



![install-live](assets/fr/08.webp)



De eerste stap is het selecteren van Fedora's **installatietaal** en **toetsenbordindeling**



![language](assets/fr/10.webp)





- De installatieschijf selecteren:



Kies de Hard schijf waarop je Fedora wilt installeren.



Als de schijf leeg is, zal Fedora automatisch alle beschikbare ruimte gebruiken. Anders kun je de partitionering aanpassen (handmatig of automatisch).



![disk](assets/fr/11.webp)





- Encryptie:



In dit stadium stelt Fedora voor om je schijf te vercijferen om een extra Layer van beveiliging toe te voegen. Dit zorgt ervoor dat je gegevens alleen door je Fedora systeem gelezen kunnen worden.



![chiffrement](assets/fr/12.webp)



Alvorens de installatie te starten, toont Fedora een samenvatting van je keuzes. Bevestig en klik op de installatie knop om de Fedora installatie te starten.



![resume](assets/fr/13.webp)



Tijdens de installatie kopieert Fedora bestanden en configureert het systeem. Als het klaar is, start de computer automatisch opnieuw op.



![installation](assets/fr/14.webp)



### Basisconfiguratie


Bij het eerste gebruik moet je een paar instellingen aanpassen:




- Wijzig indien nodig de systeemtaal.



![language](assets/fr/15.webp)





- Selecteer een toetsenbordindeling die aan je voorkeuren voldoet.



![keyboard](assets/fr/16.webp)





- Kies je tijdzone door de naam van je stad in de zoekbalk te typen en klik vervolgens op de bijbehorende suggestie.



![timezone](assets/fr/17.webp)





 - Toegang tot je positie in- of uitschakelen voor applicaties die dat nodig hebben, evenals het automatisch verzenden van bugrapporten.



![location](assets/fr/18.webp)





- Beslis of je softwareopslagplaatsen van derden wilt inschakelen.



![logs](assets/fr/19.webp)





- Voer je volledige naam in en definieer een gebruikersnaam voor je account.



![name](assets/fr/20.webp)





- Maak een veilig wachtwoord voor je sessie: zo lang mogelijk (minimaal 20 tekens), zo willekeurig mogelijk en met verschillende tekens (kleine letters, hoofdletters, cijfers en symbolen). Vergeet niet je wachtwoord op te slaan.



![mdp](assets/fr/21.webp)



Zodra al deze stappen zijn voltooid, start Fedora en begin het onmiddellijk te gebruiken, zonder verder opnieuw op te starten.



![welcome](assets/fr/22.webp)



![start](assets/fr/23.webp)



Zodra je installatie voltooid is, kun je je Interface thuis raadplegen met een paar voorgeïnstalleerde hulpprogramma's.



![install-now](assets/fr/09.webp)



## Ontdek de basistaken



### Surfen op internet


Fedora's standaard browser is **Firefox**. Het is makkelijk te gebruiken en geschikt voor de meeste behoeften.


Als je de voorkeur geeft aan een andere browser, kun je deze installeren via **softwarebeheer** of via de **terminal**.


### Tekstverwerking


Fedora bevat standaard de **LibreOffice** office suite, die verschillende nuttige gereedschappen biedt:




- Writer** voor tekstverwerking.
- Calc** voor spreadsheets.
- Impress** om presentaties te maken.


## Toepassingen installeren


Om nieuwe applicaties te installeren kun je Fedora's **software manager** gebruiken (genaamd _Software_), die de installatie eenvoudig en visueel maakt.  Echter, het gebruik van de **terminal** is vaak sneller en nauwkeuriger.



Voordat je software installeert, moet je altijd de **repositories** bijwerken om er zeker van te zijn dat je toegang hebt tot de nieuwste versies.



Gebruik vervolgens de volgende opdracht om de installatie van de gewenste toepassing te starten:


sudo dnf installeer software_naam`


## Je besturingssysteem bijwerken


Na de installatie is het belangrijk om Fedora bij te werken om te profiteren van de laatste beveiligingspatches en software updates.


### Optie 1: Via Interface grafiek




- Open Fedora **Instellingen**, ga dan naar de **Systeem** sectie.
- Klik op **Software-update**.
- Begin met het downloaden van updates en wacht tot het proces is voltooid.



Een **herstart** kan nodig zijn nadat de updates zijn geïnstalleerd.


### Optie 2: Via terminal




- Open een terminal en begin met het bijwerken van de **repositories** om er zeker van te zijn dat je de laatste versies hebt van:



```shell
sudo dnf check-update
```





- Werk vervolgens alle geïnstalleerde software bij met het volgende commando:



```shell
sudo dnf upgrade
```



Nu is je Fedora systeem up-to-date en klaar voor gebruik voor al je dagelijkse taken. Ontdek onze tutorial over Linux Mint, een andere Linux distributie, en hoe je een gezonde en veilige omgeving opzet voor je Bitcoin transacties.



https://planb.network/tutorials/computer-security/operating-system/linux-mint-da44852e-513f-4004-949a-8fde60c1bca5