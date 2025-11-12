---
name: Seedkeeper - Wachtwoordmanager
description: Hoe sla je wachtwoorden op met de Seedkeeper smartcard?
---

![cover](assets/cover.webp)



De Seedkeeper is een smartcard ontwikkeld door Satochip, een Belgisch bedrijf gespecialiseerd in hardware-oplossingen voor het beheren en beschermen van digitale geheimen. Satochip, bekend om zijn reeks smartcards voor het Bitcoin ecosysteem, bedacht de Seedkeeper als alternatief voor traditionele methodes om geheugenzinnen en andere digitale geheimen op te slaan.



Concreet heeft de Seedkeeper de vorm van een multifunctionele, EAL6-gecertificeerde smartcard met een beveiligde processor en een fraudebestendig geheugen (een zogenaamd "Secure Element"). Zoals de naam al doet vermoeden, is het de taak van de Seedkeeper om Bitcoin portfoliomemonie en wachtwoorden versleuteld en beschermd op te slaan. Met Seedkeeper kun je generate, importeren, organiseren en je geheimen direct opslaan in het beveiligde component van de kaart.



Naar mijn mening heeft Seedkeeper twee belangrijke toepassingen, die we in 2 aparte tutorials zullen verkennen:




- Bitcoin** geheugensteuntjes: in plaats van je 12 of 24 woorden op papier te zetten, kun je ze importeren in de smartcard en beschermen met een pincode.
- Wachtwoordbeheer**: je kunt generate sterke wachtwoorden genereren via de Seedkeeper-toepassing en ze direct op de smartcard opslaan, zodat je een handige, gebruiksvriendelijke offline wachtwoordbeheerder hebt.



Technisch gezien heeft Seedkeeper een capaciteit van 8192 bytes, waardoor het minimaal 50 afzonderlijke geheimen kan opslaan (het exacte aantal hangt af van hun grootte en de metadata die bij elk geheim hoort). Seedkeeper is toegankelijk [via een smartcardlezer die is aangesloten](https://satochip.io/accessories/) op een computer, of via de mobiele applicatie met NFC-verbinding. Het hele systeem werkt in offline modus, zonder internetverbinding, wat een beperkt aanvalsoppervlak garandeert.



![Image](assets/fr/001.webp)



Een bijzonder interessante functie is de mogelijkheid om de inhoud van een Seedkeeper te dupliceren naar een andere om een back-up te maken. In deze tutorial laten we je zien hoe je dat doet.



In deze tutorial behandelen we alleen het gebruik van SeedKeeper voor traditionele wachtwoorden, op de manier van een wachtwoordmanager. Als je SeedKeeper wilt gebruiken om Bitcoin wallet geheugenzinnen op te slaan, bekijk dan deze andere tutorial:



https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

## 1. Hoe krijg ik een Seedkeeper?



Er zijn twee manieren om aan je Seedkeeper te komen. Je kunt [het direct kopen bij de officiële winkel van Satochip](https://satochip.io/product/seedkeeper/) of bij een erkende wederverkoper. Maar omdat [de Seedkeeper applet open-source is](https://github.com/Toporin/Seedkeeper-Applet), heb je ook de mogelijkheid om het zelf te installeren op [een lege smartcard](https://satochip.io/product/blank-javacard-for-diy-project/).



Als je de back-upfunctie van Seedkeeper wilt gebruiken, moet je uiteraard twee smartcards aanschaffen.



## 2. De Seedkeeper-client installeren



De eerste stap is het installeren van de software op je computer of smartphone. Op een pc moet je [de nieuwste versie van Satochip-Utils downloaden](https://github.com/Toporin/Satochip-Utils/releases). Op mobiele telefoons is de Seedkeeper-applicatie beschikbaar in de [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) en in de [Apple App Store](https://apps.apple.com/be/app/seedkeeper/id6502836060).



![Image](assets/fr/002.webp)



## 3. Seedkeeper initialisatie



Start de toepassing en klik op de knop "*Klik & Scan*".



![Image](assets/fr/003.webp)



Er wordt om een pincode voor je Seedkeeper gevraagd. Omdat dit een nieuwe kaart is, is er nog geen PIN-code gedefinieerd. Voer een willekeurige code in om deze stap over te slaan en klik vervolgens op "*Volgende*".



![Image](assets/fr/004.webp)



Plaats de kaart vervolgens op de achterkant van je smartphone. De applicatie detecteert dat Seedkeeper nog niet is geïnitialiseerd en vraagt je om de pincode van je smartcard in te stellen, die tussen de 4 en 16 tekens lang is. Voor optimale veiligheid kies je een robuuste pincode die zo lang mogelijk is, willekeurig is en uit veel verschillende tekens bestaat. Deze PIN-code is de enige barrière tegen fysieke toegang tot je wachtwoorden.



**Vergeet niet om deze pincode nu ook te bewaren**, bijvoorbeeld in een wachtwoordmanager, of op een aparte fysieke drager. Bewaar in het laatste geval het medium met de pincode nooit op dezelfde plek als je Seedkeeper, anders is deze beveiliging nutteloos. Het is belangrijk om een betrouwbare back-up te hebben: zonder de PIN-code kun je de geheimen die op je Seedkeeper zijn opgeslagen niet terughalen.



![Image](assets/fr/005.webp)



Bevestig uw pincode een tweede keer.



![Image](assets/fr/006.webp)



Je Seedkeeper is nu geïnitialiseerd. Je kunt hem ontgrendelen door de pincode in te voeren die je zojuist hebt ingesteld.



![Image](assets/fr/007.webp)



Je komt nu op de beheerpagina van je smartcard.



![Image](assets/fr/008.webp)



## 4. Wachtwoorden opslaan op Seedkeeper



Zodra je Seedkeeper is ontgrendeld, klik je op de knop "*+*".



![Image](assets/fr/009.webp)



Selecteer "Genereer geheim*". Met de optie "*Een geheim importeren*" kun je een bestaand geheim opslaan (bijvoorbeeld een wachtwoord dat je in het verleden hebt aangemaakt).



![Image](assets/fr/010.webp)



In ons geval willen we een wachtwoord opslaan. Klik op "*Wachtwoord*".



![Image](assets/fr/011.webp)



Wijs een "*Label*" toe aan dit geheim, zodat het gemakkelijk kan worden geïdentificeerd als je meerdere gegevens in je Seedkeeper opslaat. Je kunt ook een identifier toevoegen die is gekoppeld aan het wachtwoord en de URL van de site.



![Image](assets/fr/012.webp)



Kies de lengte en parameters van je wachtwoord, klik dan op "*Generate*" en vervolgens op "*Import*".



![Image](assets/fr/013.webp)



Plaats je Seedkeeper op de achterkant van je smartphone.



![Image](assets/fr/014.webp)



Je wachtwoord is geregistreerd.



![Image](assets/fr/015.webp)



## 5. Toegang tot je Seedkeeper-wachtwoord



Als je je wachtwoord wilt controleren, pak dan je Seedkeeper en klik op de knop "*Klik & Scan*".



![Image](assets/fr/016.webp)



Voer uw PIN-code in en druk vervolgens op "*Next*".



![Image](assets/fr/017.webp)



Plaats je Seedkeeper op de achterkant van je smartphone.



![Image](assets/fr/018.webp)



Dit brengt je naar een lijst met al je geregistreerde geheimen. In dit voorbeeld wil ik het wachtwoord voor mijn Plan ₿ Academy-account weergeven, dus klik ik erop.



![Image](assets/fr/019.webp)



Druk op de knop "*Reveal*".



![Image](assets/fr/020.webp)



Scan je Seedkeeper opnieuw.



![Image](assets/fr/021.webp)



Uw eerder opgeslagen wachtwoord verschijnt nu op het scherm. Je kunt het kopiëren en gebruiken op de desbetreffende website.



![Image](assets/fr/022.webp)



## 6. Een back-up maken van Seedkeeper



We gaan nu een back-up maken van mijn Seedkeeper op een tweede Seedkeeper, zodat we twee kopieën hebben. Deze redundantie kan deel uitmaken van een strategie om je belangrijkste wachtwoorden te beveiligen: bijvoorbeeld door je Seedkeepers op 2 verschillende locaties op te slaan om fysieke risico's te beperken, of een kopie toe te vertrouwen aan een vertrouwd familielid.



Neem hiervoor je tweede Seedkeeper mee (vergeet niet om één van de twee te identificeren met een merkteken om verwarring te voorkomen). Begin met initialiseren, zoals beschreven in stap 3 van deze handleiding. Kies opnieuw een sterke PIN-code. Afhankelijk van je strategie kun je voor een andere pincode kiezen of dezelfde houden.



![Image](assets/fr/023.webp)



Open de applicatie, klik op "*Klik & Scan*", voer de PIN-code van je Seedkeeper n°1 (bron) in en scan deze.



![Image](assets/fr/024.webp)



Dit brengt je naar de startpagina, met een lijst van je geheimen. Klik op de drie kleine puntjes rechtsboven in de interface.



![Image](assets/fr/025.webp)



Selecteer "*Een back-up maken*" en druk vervolgens op "*Start*".



![Image](assets/fr/026.webp)



Voer de pincode van uw back-upkaart in (Seedkeeper nr. 2).



![Image](assets/fr/027.webp)



Scan vervolgens de kaart.



![Image](assets/fr/028.webp)



Doe hetzelfde met de hoofdkaart (Seedkeeper nr. 1) en klik vervolgens op "*Make a backup*".



![Image](assets/fr/029.webp)



Je Seedkeeper n°2 bevat nu alle geheimen die op Seedkeeper n°1 zijn opgeslagen.



![Image](assets/fr/030.webp)



Je kunt je Seedkeeper n°2 scannen om te controleren of de geheimen zijn gekopieerd.



![Image](assets/fr/031.webp)



Dat is alles! Nu weet je hoe je Seedkeeper kunt gebruiken om je wachtwoorden op te slaan. In een toekomstige tutorial zullen we kijken hoe je Seedkeeper kunt gebruiken om een Bitcoin wallet te back-uppen. Ik nodig je ook uit om het gecombineerde gebruik met SeedSigner te ontdekken:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356