---
name: Seedkeeper
description: Hoe maak ik een back-up van mijn wallet Bitcoin met de Seedkeeper smartcard?
---

![cover](assets/cover.webp)



De Seedkeeper is een smartcard ontwikkeld door Satochip, een Belgisch bedrijf gespecialiseerd in hardware-oplossingen voor het beheren en beschermen van digitale geheimen. Satochip, bekend om zijn reeks smartcards voor het Bitcoin ecosysteem, ontwierp de Seedkeeper als alternatief voor traditionele methodes om geheugenzinnen op te slaan.



Concreet heeft de Seedkeeper de vorm van een multifunctionele, EAL6-gecertificeerde smartcard met een beveiligde processor en een fraudebestendig geheugen (een zogenaamd "Secure Element"). Zoals de naam al zegt, is het de taak van de Seedkeeper om Bitcoin wallet mnemonics en wachtwoorden versleuteld en beschermd op te slaan. Met Seedkeeper kun je je geheimen generate importeren, organiseren en direct opslaan in het beveiligde component van de kaart.



Naar mijn mening heeft Seedkeeper twee belangrijke toepassingen, die we in 2 aparte tutorials zullen verkennen:




- Bitcoin** geheugensteuntjes: in plaats van je 12 of 24 woorden op papier te zetten, kun je ze importeren in de smartcard en beschermen met een pincode.
- Wachtwoordbeheer**: je kunt generate sterke wachtwoorden genereren via de Seedkeeper-toepassing en ze direct op de smartcard opslaan, zodat je een handige, gebruiksvriendelijke offline wachtwoordbeheerder hebt.



Technisch gezien heeft Seedkeeper een capaciteit van 8192 bytes, waardoor het minimaal 50 afzonderlijke geheimen kan opslaan (het exacte aantal hangt af van hun grootte en de metadata die bij elk geheim hoort). Seedkeeper is toegankelijk [via een smartcardlezer die is aangesloten](https://satochip.io/accessories/) op een computer, of via de mobiele applicatie met NFC-verbinding. Het hele systeem werkt in offline modus, zonder internetverbinding, wat een beperkt aanvalsoppervlak garandeert.



![Image](assets/fr/001.webp)



Een bijzonder interessante functie is de mogelijkheid om de inhoud van een Seedkeeper te dupliceren naar een andere om een back-up te maken. In deze tutorial laten we je zien hoe je dat doet.



Seedkeeper is ook erg interessant in combinatie met wallet stateloze hardware zoals SeedSigner of Specter DIY. In dit geval is het niet nodig om de Satochip client op de computer of mobiele telefoon te gebruiken. De Seedkeeper houdt de seed in zijn secure element en kan direct met het ondertekeningsapparaat worden gebruikt, waardoor er geen papieren QR-code meer nodig is. Ik zal deze specifieke use case niet in deze tutorial behandelen, omdat deze het onderwerp is van een andere tutorial:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 1. Welke use case voor Seedkeeper?



In deze tutorial ga ik alleen in op use cases die te maken hebben met Bitcoin, want daar gaat deze tutorial over. We gaan niet in op de functionaliteit voor wachtwoordbeheer, dat is het onderwerp van een andere tutorial.



Vergeleken met een eenvoudige papieren back-up van de mnemonische zin, heeft het gebruik van een Seedkeeper verschillende voordelen:





- Diefstalbestendig:** De seed in je wallet is niet toegankelijk in duidelijke tekst. Om hem eruit te halen, moet je de Seedkeeper PIN kennen. Een dief die het apparaat in handen krijgt, kan er niets mee doen zonder deze code.





- Risico verdelen over twee factoren:** Je kunt de beveiliging verdelen over een digitale en een fysieke factor. Als je de Seedkeeper PIN bijvoorbeeld opslaat in je wachtwoordmanager, heb je zowel toegang tot deze manager als fysiek bezit van de smartcard nodig om de seed te verkrijgen (een aanzienlijk kleinere aanvalskans).





- Gecentraliseerd beheer:** Seedkeeper vergemakkelijkt het beheer van meerdere zaden uit verschillende portefeuilles.





- Eenvoudige back-ups:** dupliceer eenvoudig versleutelde back-ups naar andere SeedKeepers.



Er zijn echter een aantal nadelen vergeleken met een eenvoudige papieren back-up van je seed:





- De prijs:** is weliswaar bescheiden (ongeveer €25), maar nog altijd hoger dan die van een vel papier.





- Afhankelijkheid van een general-purpose computing device:** voor het invoeren en beheren van seed is een computer of smartphone nodig, wat betekent dat je mnemonic een machine passeert met een veel breder aanvalsoppervlak dan wallet hardware. Dit kan een risico vormen als de machine gecompromitteerd is. Daarom adviseer ik niet om Seedkeeper te gebruiken om de seed van een wallet hardware op te slaan (behalve in stateless gebruik zonder computer, zoals met SeedSigner). De rol van wallet hardware is juist om de seed op te slaan in een minimalistische, zeer veilige omgeving. Door je seed handmatig in te voeren op je gebruikelijke computer, is het niet langer beperkt tot de wallet hardware: het komt ook terecht op een algemene machine, blootgesteld aan meerdere aanvalsvectoren. Het is dus beter om Seedkeeper te gebruiken voor een warme wallet dan voor een koude (behalve SeedSigner / stateless wallet hardware).





- Het risico op verlies gekoppeld aan de PIN:** de directe ontoegankelijkheid van de seed biedt, in tegenstelling tot een papieren back-up, inderdaad bescherming tegen fysieke diefstal. Maar zoals altijd is beveiliging een evenwichtsoefening tussen het risico op diefstal en het risico op verlies. Als uw back-up een PIN vereist, zal het verlies van deze code het onmogelijk maken om uw geheugensteuntje terug te vinden en dus toegang te krijgen tot uw bitcoins.



Met het oog op deze voor- en nadelen ben ik van mening dat de beste toepassingen voor Seedkeeper (afgezien van de wachtwoordbeheerfunctie) aan de ene kant het opslaan van zaden uit je **software portfolio's** zijn, aangezien deze al op je telefoon of computer staan, of van je schermloze wallet hardware zoals de Satochip, en aan de andere kant het gebruik in combinatie met stateless wallet hardware zoals de SeedSigner, waar het echt tot zijn recht komt.



Een andere bijzonder interessante use case voor Seedkeeper is de mogelijkheid om een veilige en betrouwbare back-up te maken van de *Descriptors* van je portefeuilles.



## 2. Hoe krijg ik een Seedkeeper?



Er zijn twee manieren om aan je Seedkeeper te komen. Je kunt [het direct kopen bij de officiële winkel van Satochip](https://satochip.io/product/seedkeeper/) of bij een erkende wederverkoper. Maar omdat [de Seedkeeper applet open-source is](https://github.com/Toporin/Seedkeeper-Applet), heb je ook de mogelijkheid om het zelf te installeren op [een lege smartcard](https://satochip.io/product/blank-javacard-for-diy-project/).



Als je de back-upfunctie van Seedkeeper wilt gebruiken, moet je uiteraard twee smartcards aanschaffen.



## 3. De Seedkeeper-client installeren



In deze tutorial maken we een back-up van onze seed portfolio op onze Seedkeeper. De eerste stap is het installeren van de software op je computer of smartphone. Op een PC moet je [de laatste versie van Satochip-Utils downloaden](https://github.com/Toporin/Satochip-Utils/releases). Op een mobiele telefoon is de Seedkeeper-applicatie beschikbaar in de [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) en in de [Apple App Store](https://apps.apple.com/be/app/seedkeeper/id6502836060).



![Image](assets/fr/002.webp)



## 4. Seedkeeper initialisatie



Start de toepassing en klik op de knop "*Klik & Scan*".



![Image](assets/fr/003.webp)



Er wordt om een pincode voor je Seedkeeper gevraagd. Omdat dit een nieuwe kaart is, is er nog geen PIN-code gedefinieerd. Voer een willekeurige code in om deze stap over te slaan en klik vervolgens op "*Volgende*".



![Image](assets/fr/004.webp)



Plaats de kaart vervolgens op de achterkant van je smartphone. De applicatie detecteert dat Seedkeeper nog niet is geïnitialiseerd en vraagt je om de pincode van je smartcard in te stellen, die tussen de 4 en 16 tekens lang is. Voor optimale veiligheid kies je een sterk wachtwoord dat zo lang mogelijk is, willekeurig is en uit veel verschillende tekens bestaat. Deze PIN-code is de enige barrière tegen fysieke toegang tot je herstelzin.



**Vergeet niet om deze pincode nu ook te bewaren**, bijvoorbeeld in een wachtwoordmanager, of op een aparte fysieke drager. Bewaar in het laatste geval het medium met de pincode nooit op dezelfde plek als je Seedkeeper, anders is deze beveiliging nutteloos. Het is belangrijk om een betrouwbare back-up te hebben: zonder de PIN-code kun je de geheimen die op je Seedkeeper zijn opgeslagen niet terughalen.



![Image](assets/fr/005.webp)



Bevestig uw pincode een tweede keer.



![Image](assets/fr/006.webp)



Je Seedkeeper is nu geïnitialiseerd. Je kunt hem ontgrendelen door de pincode in te voeren die je zojuist hebt ingesteld.



![Image](assets/fr/007.webp)



Je komt nu op de beheerpagina van je smartcard.



![Image](assets/fr/008.webp)



## 5. Registreer een seed op Seedkeeper



Zodra je Seedkeeper is ontgrendeld, klik je op de knop "*+*".



![Image](assets/fr/009.webp)



Selecteer "Importeer geheim*". Met de optie "*Generate secret*" kun je direct vanuit de applicatie een nieuwe geheugenzin maken.



![Image](assets/fr/010.webp)



In ons geval willen we de seed opslaan in onze portfolio. Klik op "*Mnemonic*".



![Image](assets/fr/011.webp)



Wijs een "*Label*" toe aan dit geheim, zodat het gemakkelijk kan worden geïdentificeerd als je meerdere stukken informatie in je Seedkeeper opslaat.



![Image](assets/fr/012.webp)



Voer dan je herstelzin in het daarvoor bestemde veld in. Als je wilt, kun je ook een passphrase BIP39 of je *Descriptors* toevoegen. Klik dan op "Importeren*".



![Image](assets/fr/013.webp)



*Het ezelsbruggetje in deze afbeelding is fictief en is van niemand. Het is slechts een voorbeeld. Onthul nooit je eigen mnemonic aan iemand, anders worden je bitcoins gestolen



Plaats je Seedkeeper op de achterkant van je smartphone.



![Image](assets/fr/014.webp)



Je seed is geregistreerd.



![Image](assets/fr/015.webp)



## 6. Toegang tot je seed op Seedkeeper



Als je je geheugensteuntje wilt controleren, pak dan je Seedkeeper en klik op de knop "*Klik & Scan*".



![Image](assets/fr/016.webp)



Voer uw PIN-code in en druk vervolgens op "*Next*".



![Image](assets/fr/017.webp)



Plaats je Seedkeeper op de achterkant van je smartphone.



![Image](assets/fr/018.webp)



Dit brengt je naar een lijst van al je geregistreerde geheimen. In dit voorbeeld wil ik de seed van mijn "*Blockstream App*" portfolio weergeven, dus klik ik erop.



![Image](assets/fr/019.webp)



Druk op de knop "*Reveal*".



![Image](assets/fr/020.webp)



Scan je Seedkeeper opnieuw.



![Image](assets/fr/021.webp)



Uw eerder opgenomen geheugensteunzin wordt nu op het scherm weergegeven.



![Image](assets/fr/022.webp)



## 7. Een back-up maken van Seedkeeper



We gaan nu een back-up maken van mijn Seedkeeper op een tweede Seedkeeper zodat we twee kopieën hebben. Deze redundantie kan deel uitmaken van een strategie om je bitcoins te beveiligen: bijvoorbeeld door je zinnen op twee verschillende locaties op te slaan om fysieke risico's te beperken, of door een kopie toe te vertrouwen aan een vertrouwd familielid als onderdeel van een erfenisplan.



Neem hiervoor je tweede Seedkeeper mee (vergeet niet om één van de twee te identificeren met een merkteken om verwarring te voorkomen). Begin met initialiseren, zoals beschreven in stap 4 van deze tutorial. Kies opnieuw een sterk wachtwoord. Afhankelijk van je strategie, kun je kiezen voor een ander wachtwoord of hetzelfde houden.



![Image](assets/fr/023.webp)



Open de applicatie, klik op "*Klik & Scan*", voer het wachtwoord van je Seedkeeper n°1 (bron) in en scan het.



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



Dat is alles! Nu weet je hoe je Seedkeeper kunt gebruiken om de mnemonische zin van een Bitcoin wallet op te slaan. In een volgende tutorial zullen we kijken hoe je Seedkeeper kunt gebruiken om je wachtwoorden op te slaan. Ik nodig je ook uit om het gecombineerde gebruik met SeedSigner te ontdekken:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

In deze tutorial hebben we het verschillende keren gehad over de ***Descriptors*** in je Bitcoin portfolio. Weet je niet wat ze zijn? In dat geval raad ik je aan onze gratis CYP 201 training te volgen, die dieper ingaat op alle mechanismen die betrokken zijn bij de werking van HD-portefeuilles!



https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f