---
name: SeedSigner
description: DIY, stateloze, betaalbare en volledig air-gapped wallet hardware
---

![cover](assets/cover.webp)



De SeedSigner is een open-source wallet Bitcoin hardware die iedereen zelf kan bouwen met goedkope elektronische componenten voor algemeen gebruik. In tegenstelling tot commerciële producten zoals de Ledger, Coldcard of Trezor, is dit geen kant-en-klaar apparaat gemaakt door een bedrijf: het is een gemeenschapsproject waarmee iedereen zijn eigen apparaat kan maken en elke stap kan controleren.



De SeedSigner is ontworpen om 100% ***air-gapped*** te zijn: het maakt nooit verbinding met het internet, heeft geen Wi-Fi of Bluetooth (in het geval van de Raspberry Pi Zero v1.3) en is nooit verbonden met een computer om gegevens uit te wisselen. De communicatie verloopt uitsluitend via een QR-code uitwisselingssysteem. Concreet geeft je portfoliobeheersoftware (zoals Sparrow Wallet) de te ondertekenen transactie weer in de vorm van QR-codes; jij scant ze met de camera van de SeedSigner, waarna het apparaat de transactie ondertekent met behulp van jouw privésleutels die tijdelijk in zijn RAM zijn opgeslagen. Tot slot genereert het QR-codes die de ondertekende transactie bevatten, die je scant met je software om het naar het Bitcoin netwerk te sturen.



![Image](assets/fr/001.webp)



SeedSigner is ook ***stateless***. Met andere woorden, het slaat je seed of je privésleutels niet permanent op, in tegenstelling tot andere hardware wallets. Elke keer dat je herstart, is het geheugen helemaal leeg, tenzij je het apparaat zo configureert dat het je instellingen opslaat op een microSD-kaart. Daarom moet je je seed elke keer dat je het gebruikt opnieuw invoeren, de meest praktische methode is om het op te slaan in de vorm van een QR-code, die bij het opstarten gescand moet worden met de camera van de SeedSigner. Deze manier van werken vermindert het aanvalsoppervlak aanzienlijk: zelfs als een dief je apparaat steelt, zal hij er geen informatie op vinden, omdat het standaard altijd leeg is.



Een andere optie om je seed op te slaan en te gebruiken met de SeedSigner is het gebruik van een *SeedKeeper* smartcard in combinatie met een compatibele lezer. Dit geeft je een zeer robuust *Secure Element* om je seed op te slaan, terwijl je het SeedSigner scherm gebruikt om transacties te ondertekenen. Maar deze specifieke configuratie is het onderwerp van een andere tutorial. Hier concentreren we ons op het basisgebruik van de SeedSigner:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

Het SeedSigner-project neemt een belangrijke plaats in het Bitcoin ecosysteem in, omdat het iedereen, overal ter wereld, de mogelijkheid biedt om te profiteren van geavanceerde beveiliging om hun bitcoins te beschermen. Het belangrijkste voordeel is de toegankelijkheid: de benodigde hardware kan voor minder dan $50 worden aangeschaft. Bovendien kunnen mensen in landen met beperkte toegang hun eigen wallet hardware bouwen met standaard computeronderdelen, die gemakkelijk te vinden zijn en minder onderhevig aan wettelijke beperkingen.



Maar zelfs buiten deze specifieke contexten kan SeedSigner een interessante optie voor je zijn: het is open-source, werkt stateless en airgapped en vermindert de aanvalsvectoren die gekoppeld zijn aan de toeleveringsketen van je wallet hardware.



## 1. Benodigde uitrusting



Om je SeedSigner te bouwen, heb je de volgende onderdelen nodig:





- Raspberry Pi Zero
    - Versie 1.3 wordt aanbevolen omdat deze geen Wi-Fi of Bluetooth heeft, waardoor volledige isolatie gegarandeerd is.
 - De W- en v2-versies zijn ook compatibel, maar bevatten een Wi-Fi/Bluetooth-chip. Het is daarom aan te raden om deze fysiek te deactiveren door de radiomodule van de kaart te verwijderen. De handeling is relatief eenvoudig, maar vereist precisie (een fijne tang is voldoende voor de Zero W, terwijl een hete pen nodig is voor de v2 om het metalen plaatje dat de module verbergt te verwijderen). Ik ga in deze tutorial niet in op de details, maar je vindt alle instructies in dit document: *[WiFi/Bluetooth uitschakelen via hardware](https://github.com/DesobedienteTecnologico/rpi_disable_wifi_and_bt_by_hardware)*.
 - Let op: sommige Raspberry Pi Zero-modellen worden verkocht zonder voorgesoldeerde GPIO-pinnen. Je kunt direct een versie met geïntegreerde pinnen kopen (eenvoudigste oplossing), of de pinnen apart kopen en ze zelf solderen (complexere oplossing).
 - Vergeet niet een micro-USB-voeding mee te nemen.



![Image](assets/fr/002.webp)





- Waveshare 1,3" scherm (240×240 px)** (in het Frans)
    - Het is essentieel om dit specifieke model te kiezen: er bestaan ook andere soortgelijke schermen, maar met een andere resolutie. Zonder 240×240 px definitie is het scherm onbruikbaar.
    - Het scherm heeft drie knoppen en een mini-joystick voor de gebruikersinterface.



![Image](assets/fr/003.webp)





- Raspberry Pi Zero**-compatibele camera
    - Optie 1: de standaardcamera met een brede gouden mat (controleer de compatibiliteit met je behuizing).
    - Optie 2: de compactere "*Zero*" camera, speciaal ontworpen voor de Pi Zero.



![Image](assets/fr/004.webp)





- MicroSD**-kaart
    - Aanbevolen capaciteit: tussen 4 en 32 GB.





- Huisvesting (optioneel maar aanbevolen)** (optioneel maar aanbevolen)** (optioneel maar aanbevolen)** (optioneel maar aanbevolen)**)
    - Beschermt het apparaat en maakt het gebruiksvriendelijk.
    - Het populairste model is de "*Orange Pill Case*", waarvoor [open-source STL-bestanden beschikbaar zijn voor 3D-printing](https://github.com/SeedSigner/seedsigner/tree/dev/enclosureshttps://github.com/SeedSigner/seedsigner/tree/dev/enclosures).
    - Dozen zijn ook verkrijgbaar bij [onafhankelijke wederverkopers die verbonden zijn aan het project](https://seedsigner.com/hardware/).



![Image](assets/fr/005.webp)



Je kunt deze componenten apart kopen of, voor meer eenvoud, kiezen voor kant-en-klare pakketten die alle benodigde hardware bevatten. Persoonlijk heb ik mijn pakket besteld [op deze Franse site](https://bitcoinbazar.fr/), maar je vindt ook een lijst van verkopers voor elke regio van de wereld op [de SeedSigner project hardware pagina](https://seedsigner.com/hardware/). Als je de componenten liever afzonderlijk koopt, zijn ze verkrijgbaar op de grote e-commerce platforms of in gespecialiseerde winkels.



## 2. De software voorbereiden



Zodra je je hardware bij elkaar hebt, moet je de microSD-kaart voorbereiden door het SeedSigner-systeem erop te installeren. Om dit te doen, ga je naar je gewone computer en sluit je je microSD aan die bedoeld is voor SeedSigner.



### 2.1. Downloaden



Ga naar [de officiële GitHub repository van het project](https://github.com/SeedSigner/seedsigner/releases). Download de nieuwste versie van de software:




- De `.img` image die overeenkomt met uw Pi model.
- Het bestand `.sha256.txt`.
- Het bestand `.sha256.txt.sig`.



![Image](assets/fr/006.webp)



Laten we eerst de software controleren voordat we met de installatie beginnen.



### 2.2 Verificatie onder Linux en macOS



Begin met het importeren van de officiële publieke sleutel van het SeedSigner-project rechtstreeks vanuit Keybase :



```
gpg --fetch-keys https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/007.webp)



De terminal zou je moeten vertellen dat er een sleutel geïmporteerd of bijgewerkt is. Voer vervolgens het verificatiecommando uit op het handtekeningenbestand (vergeet niet om het commando aan te passen aan je versie, hier `0.8.6.`):



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/008.webp)



Als alles correct is, zou de uitvoer `Goede handtekening` moeten zijn. Dit betekent dat het bestand `.sha256.txt` is ondertekend door de sleutel die u zojuist hebt geïmporteerd en dat de handtekening geldig is. Negeer de waarschuwing `WARNING: Deze sleutel is niet gecertificeerd met een vertrouwde handtekening`: dit is normaal, omdat het nu aan jou is om te controleren of de gebruikte sleutel bij het SeedSigner project hoort.



Om dit te doen, vergelijk je de laatste 16 karakters van de weergegeven vingerafdruk met die beschikbaar op [Keybase.io/SeedSigner](https://keybase.io/seedsigner), op hun [officiële Twitter](https://twitter.com/SeedSigner/status/1530555252373704707), of in het bestand gepubliceerd op [SeedSigner.com](https://seedsigner.com/keybase.txt). Als deze identifiers exact overeenkomen, kun je er zeker van zijn dat de sleutel inderdaad van het project is. Als je twijfelt, stop dan onmiddellijk en vraag de SeedSigner gemeenschap (Telegram, X, GitHub...) om hulp.



Wanneer de sleutel is gevalideerd, kun je controleren of de gedownloade afbeelding niet is gewijzigd (vergeet niet om het commando aan te passen aan je versie, hier `0.8.6.`):



```
shasum -a 256 --ignore-missing --check seedsigner.0.8.6.sha256.txt
```



![Image](assets/fr/009.webp)





- Onder Linux is dit commando ingebouwd.
- Waarschuwing: macOS versies voorafgaand aan `Big Sur (11)` herkennen de `--ignore-missing` optie niet. Verwijder deze in dit geval en negeer waarschuwingen over ontbrekende bestanden.



Het verwachte resultaat is een `OK` naast het `.img` bestand. Dit bevestigt dat de geüploade afbeelding identiek is aan de afbeelding die door het project is gepubliceerd en niet is gewijzigd.



### 2.3 Windows-verificatie



Op Windows is de procedure vergelijkbaar, maar de commando's zijn anders. Begin met het installeren van [Gpg4win](https://www.gpg4win.org/) en open de *Kleopatra* applicatie. Importeer de publieke sleutel van het SeedSigner project van de URL Keybase :



```
https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/010.webp)



Open vervolgens PowerShell in de map waar je gedownloade bestanden staan (`Shift` + rechtermuisknop > `Open PowerShell here`). Voer de volgende opdracht uit om de handtekening van het manifest te controleren (vergeet niet de opdracht aan te passen aan je versie, hier `0.8.6.`):



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/011.webp)



Als alles correct is, zou de uitvoer `Goede handtekening` moeten zijn. Dit betekent dat het bestand `.sha256.txt` is ondertekend door de sleutel die u zojuist hebt geïmporteerd en dat de handtekening geldig is. Negeer de waarschuwing `WARNING: Deze sleutel is niet gecertificeerd met een vertrouwde handtekening`: dit is normaal, omdat het nu aan jou is om te controleren of de gebruikte sleutel bij het SeedSigner project hoort.



Om dit te doen, vergelijk je de laatste 16 karakters van de weergegeven vingerafdruk met die beschikbaar op [Keybase.io/SeedSigner](https://keybase.io/seedsigner), op hun [officiële Twitter](https://twitter.com/SeedSigner/status/1530555252373704707), of in het bestand gepubliceerd op [SeedSigner.com](https://seedsigner.com/keybase.txt). Als deze identifiers exact overeenkomen, kun je er zeker van zijn dat de sleutel inderdaad van het project is. Als je twijfelt, stop dan onmiddellijk en vraag de SeedSigner gemeenschap (Telegram, X, GitHub...) om hulp.



Zodra de sleutel is gevalideerd, moet je controleren of het imagebestand niet is beschadigd. Gebruik hiervoor de volgende opdracht in PowerShell :



```
CertUtil -hashfile seedsigner_os.0.8.6.[your-Pi-model].img SHA256
```



Voorbeeld voor een Raspberry Pi Zero 2 (vergeet niet om het commando aan te passen aan je versie, hier `0.8.6.`):



```
CertUtil -hashfile seedsigner_os.0.8.6.pi02w.img SHA256
```



![Image](assets/fr/012.webp)



PowerShell berekent dan de SHA256 hash van je image-bestand. Vergelijk deze hash met de corresponderende waarde in `seedsigner.0.8.6.sha256.txt`.




- Als de twee waarden strikt identiek zijn, is de controle geslaagd en kun je doorgaan.
- Als ze verschillen, is het bestand corrupt of beschadigd. Gebruik het niet en start de download opnieuw.



![Image](assets/fr/013.webp)



Een succesvolle verificatie garandeert dat uw `.img` bestand zowel authentiek (ondertekend door SeedSigner) als ongewijzigd (ongewijzigd) is. U kunt dan veilig doorgaan naar de volgende stap.



### 2.4. Flash de afbeelding



Als je die nog niet hebt, download dan de [Balena Etcher] software (https://etcher.balena.io/), en vervolgens :




- Plaats de microSD-kaart in uw computer.
- Lanceer Etcher.
- Selecteer het gedownloade en geverifieerde `.img` bestand.
- Selecteer microSD-kaart als doel.
- Klik op `Flash!`.



![Image](assets/fr/014.webp)



Wacht tot het proces is voltooid: je microSD is klaar voor gebruik. Nu is het tijd voor de montage!



## 3. SeedSigner montage



Zodra je microSD-kaart is voorbereid en geflasht met SeedSigner software, kun je verder gaan met de uiteindelijke assemblage. Neem de tijd, want sommige onderdelen zijn kwetsbaar (met name het tafelkleed, de camera en de GPIO-pinnen).



### 3.1 De behuizing voorbereiden



Open eerst je behuizing. Controleer of hij schoon is en of er geen resten 3D-printplastic in de weg zitten van de interne bevestigingsmiddelen. Kijk uit voor :




- Locatie van de camera (klein rond gat aan de voorkant).
- De opening voor het scherm.
- De uitsparingen voor de micro-USB-poorten en het microSD-slot van de Raspberry Pi Zero.



### 3.2 Camera-installatie



Zoek de lintconnector van de camera op de Raspberry Pi Zero: het is een dunne zwarte strip aan de zijkant van het bord die je lichtjes kan optillen om hem te openen. Til het voorzichtig op, zonder te forceren: het moet gewoon een paar millimeter kantelen.



![Image](assets/fr/015.webp)



Plaats de cameradeksel. Het bruine/koper gedeelte moet naar beneden wijzen. Zorg ervoor dat het stevig vastzit in de connector, zonder te draaien.



![Image](assets/fr/016.webp)



Sluit de zwarte balk om het tafelkleed te vergrendelen (je voelt een lichte klik). Controleer voorzichtig of het op zijn plaats blijft en niet verschuift.



![Image](assets/fr/017.webp)



Plaats vervolgens de cameramodule in het daarvoor bestemde gat in de behuizing. Afhankelijk van het model kan de module direct vastklikken of is er een kleine plakstrip nodig om de module op zijn plaats te houden. De lens moet perfect uitgelijnd zijn, naar buiten gericht.



### 3.3 De Raspberry Pi Zero installeren



Als je een behuizing gebruikt, plaats dan het Raspberry Pi Zero bord erin. Lijn de poorten voorzichtig uit met de voorziene openingen.



Plaats vervolgens het Waveshare-display bovenop de Raspberry Pi Zero. De GPIO pinnen van de Pi moeten perfect in lijn liggen met de vrouwelijke connector van het display. Druk het display langzaam op de pinnen en oefen gelijkmatige druk uit aan elke kant om te voorkomen dat ze verbuigen.



![Image](assets/fr/018.webp)



Als je een behuizing hebt, voltooi dan de montage door het voorpaneel en de joystick toe te voegen.



Plaats tenslotte de microSD-kaart met de geflashte software in de sleuf aan de rand van de Raspberry Pi Zero. Zorg ervoor dat het op zijn plaats klikt.



### 3.4 Eerste opstart



Sluit een micro-USB-stroomkabel aan op de daarvoor bestemde poort. Wacht ongeveer een minuut. Het SeedSigner logo zou moeten verschijnen, gevolgd door het beginscherm.



![Image](assets/fr/019.webp)



Controleer om te beginnen of de verschillende componenten goed werken door naar het menu `Instellingen > I/O-test` te gaan.



![Image](assets/fr/020.webp)



Test alle knoppen en controleer of ze correct reageren. Klik vervolgens op de `KEY1` knop om te controleren of de camera werkt zoals verwacht. Nu wordt er een foto gemaakt.



![Image](assets/fr/021.webp)



### 3.5 Camera instellen



Afhankelijk van hoe je je SeedSigner hebt gemonteerd, kan de camera een omgekeerd beeld weergeven. Om dit te corrigeren, ga je naar `Instellingen > Geavanceerd > Camerarotatie` en selecteer je indien nodig een rotatie van 180°.



![Image](assets/fr/022.webp)



Als je de camerastand hebt gewijzigd of andere instellingen (zoals de interfacetaal) op een later tijdstip wilt wijzigen, moet je de instellingen op de microSD laten behouden. Anders zullen je instellingen bij elke herstart terugvallen op de standaardinstellingen, omdat de Raspberry Pi Zero geen permanent geheugen heeft.



Open hiervoor het menu `Instellingen > Persistente instellingen` en selecteer vervolgens `Ingeschakeld`.



![Image](assets/fr/023.webp)



Als alles werkt, is je SeedSigner nu klaar voor gebruik!



## 4. SeedSigner instellingen



Voordat je je Bitcoin wallet aanmaakt, moeten we de SeedSigner configureren. Omdat het draait op een Raspberry Pi Zero zonder permanent geheugen, worden de instellingen niet automatisch opgeslagen, tenzij je ze opslaat op de microSD-kaart. Zorg er dus voor dat je deze optie hebt ingeschakeld, anders gaan deze instellingen verloren bij het opnieuw opstarten (zie stap 3.5).



### 4.1 Toegang tot parametermenu



Start je SeedSigner en wacht tot het beginscherm verschijnt. Navigeer met de joystick naar de optie `Instellingen` en bevestig deze door op de draaiknop te drukken. U komt nu in het hoofdmenu met instellingen.



![Image](assets/fr/024.webp)



### 4.2 Portfoliomanagementsoftware kiezen



Open vervolgens het menu `Coördinatorsoftware`.



![Image](assets/fr/025.webp)



De `Coordinator` verwijst naar de software voor portefeuillebeheer waarmee uw SeedSigner zal communiceren via QR-codes. Deze software wordt geïnstalleerd op je computer of op je smartphone. Hiermee kunt u uw bitcoins beheren, maar zonder ooit toegang te hebben tot uw privésleutels. De SeedSigner blijft het enige apparaat dat uw transacties kan ondertekenen.



De huidige firmwareversie ondersteunt verschillende programma's: Sparrow, Specter, BlueWallet, Nunchuk en Keeper. In mijn geval gebruik ik **Sparrow Wallet**, die ik vooral aanbeveel vanwege zijn eenvoud en rijke functionaliteit.



Als je niet weet hoe je het moet installeren, kun je deze tutorial volgen:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Selecteer gewoon de software van je keuze in het menu.



![Image](assets/fr/026.webp)



### 4.3 Weergave van eenheden en hoeveelheid



In het menu `Denominatieweergave` kun je de eenheid kiezen waarin de bedragen worden weergegeven:




- `BTC`
- mBTC` (milli-bitcoin, of 0,001 BTC)
- gW-15 (satoshis, of 1/100.000.000 BTC)



De **sats** is over het algemeen het meest praktisch voor kleine hoeveelheden.



![Image](assets/fr/027.webp)



### 4.4 Geavanceerde instellingen



Ga nu naar het menu `Geavanceerd`. Hier vind je verschillende handige opties:




- gW-17 network`: alleen aan te passen als je de SeedSigner op Testnet wilt gebruiken.
- qR code density`: past de hoeveelheid informatie in elke QR code aan. Je kunt de standaardwaarde laten staan, tenzij je het moeilijk vindt om te lezen tijdens het scannen.
- `Xpub export`: in- of uitschakelen van de export van je uitgebreide publieke sleutel (`xpub`, `ypub`, `zpub`) naar portfoliobeheersoftware via QR-code (een functie die we later zullen gebruiken, dus laat deze voorlopig ingeschakeld).
- `Script types`: definieert de scripttypes die toegestaan zijn om je bitcoins te vergrendelen. Je hoeft deze parameter niet aan te passen, omdat het scripttype direct op Sparrow wordt gezet. Hier gaat het alleen om scripts die de SeedSigner mag manipuleren.



### 4.5 Taalkeuze



Tot slot kun je in het menu `Taal` de interfacetaal aanpassen aan je voorkeur.



![Image](assets/fr/028.webp)



## 5. seed aanmaken en opslaan



De seed (of mnemonische zin) vormt de basis van je Bitcoin portfolio. Het wordt gebruikt om je privésleutels en adressen af te leiden, en geeft toegang tot je fondsen. SeedSigner biedt verschillende methodes om het te genereren, die we in deze sectie zullen bekijken.



Voordat we beginnen, een paar essentiële herinneringen:




- Deze zin geeft volledige, onbeperkte toegang tot al je bitcoins.** Iedereen die in het bezit is van deze zin kan je geld stelen, zelfs zonder fysieke toegang tot je SeedSigner ;
- Gewoonlijk wordt een 12-woorden zin gebruikt om een wallet te herstellen in geval van verlies of diefstal van wallet hardware. Maar omdat de SeedSigner een *statloos* apparaat is, registreert het nooit jouw seed. Dus je fysieke back-ups zijn niet zomaar reservekopieën, maar **de enige manier om je wallet te gebruiken**. Als je deze back-ups verliest, zijn je bitcoins voorgoed verloren. Maak dus zorgvuldig back-ups, op verschillende media en op veilige plaatsen;
- Als je net begint, raad ik je aan om deze tutorial te lezen voor een gedetailleerd begrip van de risico's die gepaard gaan met het beheren van een mnemonische zin:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.1 De tool voor het aanmaken van seed openen



Ga in het beginscherm van SeedSigner naar het menu `Tools`.



![Image](assets/fr/029.webp)



Je generate zal nu je seed zijn. Een seed is gewoon een groot willekeurig getal. Hoe willekeuriger het wordt gegenereerd, hoe veiliger het is. SeedSigner biedt twee manieren om dit te doen:




- camera": seed wordt gegenereerd uit de visuele ruis van een foto. Je neemt een afbeelding van een willekeurige omgeving (voorwerp, landschap, gezicht, enz.) waarvan de pixelvariaties gebruikt worden om generate entropie te genereren. Het is een snelle methode, maar niet reproduceerbaar.
- dobbelen": je gooit met dobbelstenen om de nodige entropie te creëren. Het is tijdrovender, maar reproduceerbaar en dus controleerbaar. Als je voor deze methode kiest, volg dan het advies in deze tutorial (je hoeft hier geen checksum te berekenen, dat doet de SeedSigner):



https://planb.academy/tutorials/wallet/backup/generate-mnemonic-phrase-47507d90-e6af-4cac-b01b-01a14d7a8228

### 5.2 De seed met de foto maken



Als je de fotomethode kiest, klik dan op `Nieuw seed` (met het camerapictogram), neem een foto en valideer. Selecteer dan de lengte van je zin (12 of 24 woorden), die op het scherm verschijnt om op te slaan. De volgende stappen zijn identiek aan deel 5.3.



### 5.3 seed maken met dobbelstenen



In deze tutorial gebruiken we de **Dice Rolls** methode. Klik op `New seed` (met het dobbelicoon).



![Image](assets/fr/030.webp)



Kies vervolgens de lengte van je geheugensteunzin. 12 woorden bieden al voldoende zekerheid, dus dit is de keuze die ik aanraad.



![Image](assets/fr/031.webp)



Gooi met de dobbelstenen en voer de resulterende getallen in met de cursor. Druk op de middelste knop om elke invoer te valideren. Als je een fout maakt, kun je teruggaan. Gebruik verschillende dobbelstenen om de invloed van ongebalanceerde dobbelstenen te verminderen. Zorg ervoor dat je niet in de gaten wordt gehouden tijdens deze handeling.



![Image](assets/fr/032.webp)



Zodra je je 50 worpen hebt ingevoerd, genereert de SeedSigner je zin. **Volg de instructies in deze tutorial zorgvuldig op als je net begint:**



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.4 De seed weergeven en opslaan



Schrijf de woorden van je mnemonische zin zorgvuldig op een geschikte fysieke drager (papier of metaal).



![Image](assets/fr/033.webp)



### 5.5 De back-up controleren



Om fouten in de back-up te voorkomen, vraagt SeedSigner je om je back-up te verifiëren. Klik op `Verifiëren`.



![Image](assets/fr/034.webp)



Voer dan het gevraagde woord in volgens de volgorde in de zin. Hier moet ik bijvoorbeeld het derde woord in mijn zin kiezen.



![Image](assets/fr/035.webp)



Als je een fout maakt, zal de SeedSigner je verwittigen en moet je opnieuw beginnen. Zorg ervoor dat je je geheugensteuntje noteert wanneer je het krijgt. Deze verificatiestap zorgt ervoor dat uw back-up correct en volledig is. Eenmaal gevalideerd zal het scherm `Backup geverifieerd` weergeven.



![Image](assets/fr/036.webp)



Volg deze tutorial voor een meer volledige hersteltest:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 5.6 Het concept van "stateless device" begrijpen



De SeedSigner is een apparaat zonder permanent geheugen. Dit betekent dat uw seed nooit wordt opgeslagen in het apparaat (in tegenstelling tot bijvoorbeeld een Ledger, Trezor of Coldcard). Zodra u de stroom uitschakelt, verdwijnt de seed volledig uit het RAM-geheugen. Als je opnieuw opstart, keert de SeedSigner terug naar een lege staat: je moet hem dan opnieuw jouw seed geven, zodat hij jouw transacties kan ondertekenen.



Dit biedt essentiële bescherming. In tegenstelling tot andere hardware wallets, is SeedSigner gebaseerd op een Raspberry Pi Zero, die geen fysieke bescherming heeft, inclusief *Secure Element*. Maar omdat er geen gevoelige gegevens worden opgeslagen, zou zelfs een fysiek gecompromitteerd apparaat een aanvaller niet in staat stellen om je privésleutels te ontfutselen of je bitcoins uit te geven.



Aan de andere kant brengt deze architectuur een extra verantwoordelijkheid met zich mee: zonder back-up zijn je fondsen definitief verloren. Daarom raad ik een **dubbele back-up** aan. Je hebt je herstelzin al: dit is je belangrijkste back-up op lange termijn, die je op een veilige plaats bewaart. Nu gaan we een kopie van deze zin maken in de vorm van **QR-code**.



Elke keer dat je de SeedSigner gebruikt, scan je deze QR-code met de camera van het apparaat zodat het tijdelijk je seed in zijn geheugen laadt terwijl jij je transacties ondertekent. Deze tweede back-up, bedoeld voor dagelijks gebruik, moet ook met de grootste zorg bewaard worden: iedereen die in het bezit is van deze QR-code heeft volledige toegang tot jouw bitcoins.


Ik raad je ook aan om je QR-code en je geheugensteuntje op twee verschillende locaties op te slaan, om te voorkomen dat je alles kwijtraakt in het geval van een claim.



Een geavanceerder en veiliger alternatief is het gebruik van de SeedSigner met een **SeedKeeper**, die de seed opslaat in een secure element. Bekijk deze tutorial voor meer informatie:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

### 5.7 Master key fingerprint schrijven



Zodra de verificatie voltooid is, toont SeedSigner de vingerafdruk van de hoofdsleutel van uw wallet. Deze vingerafdruk identificeert uw wallet en zorgt ervoor dat u in de toekomst de juiste herstelzin gebruikt. Deze vingerafdruk identificeert jouw wallet en zorgt ervoor dat je in de toekomst de juiste herstelzin gebruikt. Het geeft geen informatie over je privésleutels, dus je kunt het veilig op een digitaal medium opslaan. Zorg er wel voor dat je een toegankelijke kopie bewaart en deze nooit kwijtraakt.



![Image](assets/fr/037.webp)



Het is ook in dit stadium dat je een **passphrase BIP39** kunt toevoegen om de veiligheid van je wallet te versterken. Afhankelijk van je back-upstrategie kan deze optie de moeite waard zijn, maar het brengt ook risico's met zich mee: als je de passphrase verliest, ben je de toegang tot je bitcoins voorgoed kwijt.



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

Als je nog niet bekend bent met het passphrase concept, nodig ik je uit om deze uitgebreide tutorial over dit onderwerp te lezen:



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

![Image](assets/fr/038.webp)



### 5.8 seed opslaan in QR formaat (*SeedQR*)



Met SeedSigner kun je je seed omzetten in een papieren QR code, genaamd *SeedQR*. Deze methode vereenvoudigt het herladen van je wallet, omdat je niet elk woord handmatig hoeft over te typen.



Hiervoor heb je een blanco papieren of metalen QR code nodig die overeenkomt met de lengte van jouw mnemonische zin. Als je een compleet pakket voor je SeedSigner hebt gekocht, zijn de sjablonen meestal inbegrepen. Zo niet, dan kun je ze hier downloaden en afdrukken (of met de hand reproduceren):




- [12-woord formaat](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)
- [24-woord formaat](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_29x29.pdf)
- [Compact formaat 12 woorden](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_21x21.pdf)
- [Compact formaat 24 woorden](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)



Selecteer `Backup zaad` op het seed scherm.



![Image](assets/fr/039.webp)



Kies dan `Export als SeedQR`.



![Image](assets/fr/040.webp)



Selecteer vervolgens het gewenste formaat (normaal of compact) op basis van de beschikbare papiersjabloon.



![Image](assets/fr/041.webp)



Klik op `Begin` om te beginnen met het maken van de *SeedQR*. De SeedSigner toont dan een reeks rasters (A1, A2, B1, enz.), die elk overeenkomen met een deel van de code.



![Image](assets/fr/042.webp)



Reproduceer zorgvuldig elke zwarte stip op je saveblad en gebruik dan de joystick om naar het volgende blok te gaan. Neem de tijd: een simpele verkeerde uitlijning kan de QR-code onbruikbaar maken.



Een paar tips:




- Begin met een potlood zodat je eventuele fouten kunt corrigeren, en ga dan terug naar een fijne zwarte pen als je klaar bent;
- Een goed gecentreerd punt in het midden van het vierkant is alles wat je nodig hebt, je hoeft het niet helemaal op te vullen.



![Image](assets/fr/043.webp)



Klik dan op `Confirm SeedQR` en scan je QR code om te controleren of deze correct werkt.



![Image](assets/fr/044.webp)



Als het bericht `Succes` wordt weergegeven, is uw *SeedQR* geldig: u kunt doorgaan met de volgende stap.



![Image](assets/fr/045.webp)



**Bewaar dit blad net zo goed als je herstelzin. Iedereen die in het bezit is van deze QR-code kan je privésleutels reconstrueren en je bitcoins stelen.**



Gefeliciteerd, je Bitcoin portfolio werkt nu! We importeren nu de publieke componenten in **Sparrow Wallet** om het gemakkelijk te beheren.



## 6. wallet importeren in Sparrow



Zodra uw SeedSigner is ingesteld en uw seed correct is aangemaakt en opgeslagen, is de volgende stap om deze portefeuille te koppelen aan beheersoftware zoals Sparrow Wallet. Uw seed blijft altijd offline, omdat alleen het openbare deel van uw portefeuille naar Sparrow wordt verzonden. Hierdoor kan de software je adressen en transacties weergeven en nieuwe transacties opbouwen, zonder ooit je bitcoins te kunnen uitgeven. Om je bitcoins uit te geven, moet je SeedSigner altijd de transactie ondertekenen die door Sparrow is voorbereid.



### 6.1 De SeedSigner voorbereiden



Plaats de microSD met het besturingssysteem, zet je SeedSigner aan en laad de seed die je net hebt gemaakt van je back-up QR code. Selecteer op het beginscherm `Scan` en scan vervolgens je SeedQR met de SeedSigner.



![Image](assets/fr/046.webp)



Controleer of de vingerafdruk op je master key overeenkomt met de vingerafdruk op je wallet. Als je een passphrase gebruikt, voer die dan in dit stadium in.



![Image](assets/fr/047.webp)



Dit brengt je naar het menu voor je portfolio, in mijn geval genaamd `d4149b27`. Als je terug bent op het beginscherm, selecteer je `Zaden` en kies je de afdruk die overeenkomt met je portfolio. Klik dan op `Export Xpub`.



![Image](assets/fr/048.webp)



Selecteer het type portefeuille. In ons geval is het een enkele portefeuille: selecteer `Single Sig`.



![Image](assets/fr/049.webp)



Vervolgens komt de keuze van de scriptingstandaard. De nieuwste en meest voordelige in termen van transactiekosten is `Taproot`. Ik raad je daarom aan deze standaard te kiezen.



![Image](assets/fr/050.webp)



Er verschijnt een waarschuwingsbericht. Dit is normaal: met deze uitgebreide publieke sleutel (`xpub`) kun je alle adressen bekijken die zijn afgeleid van je seed (op de eerste rekening). Je kunt er je geld niet mee uitgeven, maar het laat wel de structuur van je portefeuille zien. Als het ooit uitlekt, is dat een probleem voor je privacy, maar niet voor de veiligheid van je bitcoins: je kunt ze zien, maar niet uitgeven.



Klik op `Ik begrijp het` en vervolgens op `Export Xpub` als u tevreden bent met de weergegeven informatie.



De SeedSigner genereert dan je xpub in de vorm van een dynamische QR-code met alle gegevens die je nodig hebt om je portfolio in Sparrow Wallet te beheren.



![Image](assets/fr/051.webp)



Je kunt de joystick gebruiken om de helderheid van het scherm aan te passen zodat je gemakkelijker QR-codes kunt scannen.



### 6.2 Een nieuw portfolio importeren in Sparrow Wallet



Zorg ervoor dat je de Sparrow Wallet software op je computer geïnstalleerd hebt. Als je niet weet hoe je de software moet downloaden, controleren en installeren, raadpleeg dan onze volledige tutorial over dit onderwerp:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Open op je computer Sparrow Wallet, klik dan in de menubalk op `Bestand → Wallet importeren`.



![Image](assets/fr/052.webp)



Scroll naar beneden naar `SeedSigner` en selecteer vervolgens `Scan...`. Uw webcam wordt geopend: scan de dynamische QR-code die op uw SeedSigner-scherm wordt weergegeven.



![Image](assets/fr/053.webp)



Geef je portfolio een naam en klik dan op `Creëer Wallet`. Sparrow zal je dan vragen een wachtwoord in te stellen om de lokale toegang tot deze wallet te vergrendelen. Kies een sterk wachtwoord: het beschermt de toegang tot uw portefeuillegegevens in Sparrow (openbare sleutels, adressen, labels en transactiegeschiedenis). Dit wachtwoord is niet nodig om de portefeuille op een later tijdstip te herstellen: alleen je geheugensteuntje (en mogelijk je passphrase) is hiervoor nodig.



Ik raad je aan om dit wachtwoord op te slaan in een wachtwoordmanager om te voorkomen dat je het kwijtraakt.



![Image](assets/fr/054.webp)



Je sleutelbewaarplaats is nu succesvol geïmporteerd.



![Image](assets/fr/055.webp)



Controleer dan of de `Master fingerprint` die in Sparrow wordt weergegeven, overeenkomt met de vingerafdruk die eerder in uw SeedSigner werd genoteerd.



Uw SeedSigner en Sparrow Wallet zijn nu veilig met elkaar verbonden. De Sparrow fungeert als volledige beheerinterface, terwijl de SeedSigner het enige apparaat blijft dat uw transacties kan ondertekenen. U bent nu klaar om bitcoins te ontvangen en te verzenden in een volledig air-gapped configuratie.



## 7. Bitcoins ontvangen en versturen



Je SeedSigner en Sparrow Wallet zijn nu geconfigureerd om samen te werken. In dit laatste gedeelte bekijken we hoe we bitcoins kunnen ontvangen en verzenden met deze configuratie.



### 7.1 Bitcoins ontvangen



#### 7.1.1 Een ontvangstadres genereren



Open Sparrow Wallet op je computer en ontgrendel je SeedSigner wallet met je wachtwoord. Zorg ervoor dat de software verbonden is met een server (inkeping rechtsonder). Klik in de zijbalk op `Ontvangen`.



![Image](assets/fr/056.webp)



Een nieuw Bitcoin adres wordt weergegeven. U ziet :




- Het tekstadres (beginnend met `bc1p...` als je P2TR gebruikt zoals ik),
- De bijbehorende QR-code,
- Een `Label` veld voor het bijhouden van je transacties.



Ik raad je sterk aan om een label toe te voegen aan elke bitcoin-ontvangst op je wallet. Zo kun je gemakkelijk de herkomst van elke UTXO identificeren en je privacybeheer verbeteren. Om dieper op dit belangrijke onderwerp in te gaan, kun je de speciale training op Plan ₿ Academy bekijken:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Als u een label wilt toevoegen, voert u een naam in het veld `Label` in en bevestigt u.



Bijvoorbeeld:



```txt
Label : Sale of the Raspberry Pi Zero
```



Je adres is nu gekoppeld aan dit label in alle Sparrow-secties.



![Image](assets/fr/057.webp)



#### 7.1.2 Address verificatie op de SeedSigner



Voordat u uw ontvangstadres deelt, is het erg belangrijk om te controleren of het bij uw seed hoort. Deze stap zorgt ervoor dat uw SeedSigner transacties kan ondertekenen die aan dit adres zijn gekoppeld. Het beschermt ook tegen mogelijke aanvallen waarbij Sparrow een frauduleus adres weergeeft. Vergeet niet dat Sparrow draait op een onveilige omgeving (uw computer), die een veel groter aanvalsoppervlak heeft dan uw SeedSigner, die volledig geïsoleerd is. Daarom moet je nooit blindelings de ontvangstadressen geloven die Sparrow weergeeft, totdat je ze hebt geverifieerd met je wallet hardware.



Klik op Sparrow op de QR-code van het adres om het te vergroten: het wordt dan schermvullend weergegeven.



![Image](assets/fr/058.webp)



Kies `scannen` in het hoofdmenu van je SeedSigner. Scan de QR-code op je computerscherm en kies de seed die overeenkomt met jouw wallet (in mijn geval de `d4149b27` vingerafdruk).



![Image](assets/fr/059.webp)



Als het gescande adres overeenkomt met het adres van jouw seed, dan zal het SeedSigner scherm het bericht weergeven: `Address geverifieerd`.



![Image](assets/fr/060.webp)



Dit bevestigt dat het adres bij jouw wallet hoort en dat je er met een gerust hart bitcoins van kunt ontvangen.



#### 7.1.3 Ontvangst van fondsen



Je kunt dit adres nu doorgeven (in de vorm van tekst of QR-code) aan de persoon of afdeling die je satss moet sturen. Zodra de transactie is uitgezonden op het netwerk, verschijnt deze op het tabblad `Transacties` van Sparrow Wallet.



![Image](assets/fr/061.webp)



### 7.2 Bitcoins versturen



Bitcoins versturen met een SeedSigner gaat in 3 stappen:




- Transactie creëren in Sparrow ;
- Handtekening van de transactie op de SeedSigner ;
- Definitieve verdeling van de transactie via Sparrow.



Alle uitwisselingen tussen de twee apparaten gebeuren uitsluitend via QR-codes.



#### 7.2.1 De transactie aanmaken in Sparrow



In Sparrow Wallet kun je klikken op de `Verstuur` tab in de linker zijbalk. Ik gebruik echter liever het tabblad `UTXO's`, waarmee je "*Coin Controle*" kunt oefenen. Deze methode geeft je precieze controle over de gebruikte UTXO's, zodat je zelf kunt bepalen welke informatie je tijdens de transactie vrijgeeft.



Selecteer in het tabblad `UTXO's` de munten die u wilt uitgeven en klik vervolgens op `Verstuur Geselecteerd`.



![Image](assets/fr/062.webp)



Vul vervolgens de transactievelden in:




- Plak in `Betalen aan` het adres van de ontvanger of klik op het camerapictogram om de QR-code te scannen;
- Voeg in `Label` een label toe om deze uitgave bij te houden;
- Voer in `Bedrag` het bedrag in dat moet worden verzonden;
- Selecteer ten slotte het tarief op basis van de huidige marktomstandigheden (schattingen zijn beschikbaar op [mempool.space](https://mempool.space/)).



Zodra de velden zijn ingevuld, controleer je de informatie zorgvuldig en klik je op `Transactie maken >>`.



![Image](assets/fr/063.webp)



Controleer de transactiegegevens om er zeker van te zijn dat alles correct is en klik vervolgens op `Transactie voltooien voor ondertekening`.



![Image](assets/fr/064.webp)



De transactie is nu klaar, maar nog niet ondertekend. Om de [PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/psbt) als QR code weer te geven, klik op `Show QR`.



![Image](assets/fr/065.webp)



#### 7.2.2 De transactie ondertekenen met de SeedSigner



Zet je SeedSigner aan en scan je SeedQR om toegang te krijgen tot je portefeuille, zoals gewoonlijk. Selecteer op het beginscherm `Scan` en scan de QR-code die op de Sparrow staat.



![Image](assets/fr/066.webp)



Kies dan de seed die bij jouw portfolio past.



![Image](assets/fr/067.webp)



De SeedSigner detecteert automatisch dat dit een PSBT is en toont een samenvatting van de transactie:




   - Het verzonden bedrag,
   - Uitvoeradressen,
   - Gerelateerde transactiekosten.



Klik op `Bekijk Details` en controleer alle informatie direct op het scherm van SeedSigner. De belangrijkste items om te controleren zijn het verzonden bedrag, het adres van de ontvanger en het bedrag aan kosten dat in rekening is gebracht.



![Image](assets/fr/068.webp)



Als alles correct is, selecteer dan `Approveer PSBT` om de transactie te ondertekenen met de bijbehorende private sleutel(s).



![Image](assets/fr/069.webp)



Na ondertekening genereert de SeedSigner een nieuwe QR-code met de ondertekende transactie, klaar om gescand te worden door Sparrow.



![Image](assets/fr/070.webp)



#### 7.2.3 De transactie uitzenden vanaf Sparrow



Nu de transactie geldig is, moet ze worden uitgezonden op het Bitcoin netwerk, zodat ze een miner bereikt die ze toevoegt aan een blok.



Klik op Sparrow op `QR Scan`.



![Image](assets/fr/071.webp)



Presenteer de QR-code die wordt weergegeven door je SeedSigner (die van de ondertekende transactie) aan de webcam. Sparrow zal de handtekening decoderen en de volledige transactiedetails weergeven. Controleer nog een laatste keer of alle informatie correct is en klik dan op Transactie uitzenden om het uit te zenden op het Bitcoin netwerk.



![Image](assets/fr/072.webp)



Je transactie is nu verzonden naar het Bitcoin netwerk. U kunt de voortgang volgen op het tabblad `Transacties` van Sparrow Wallet.



![Image](assets/fr/073.webp)



Je hebt nu de basisbeginselen van SeedSigner onder de knie. Om je kennis te verdiepen en meer geavanceerde toepassingen te verkennen, nodig ik je uit om de volgende tutorial te raadplegen:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

**[Je kunt de ontwikkeling van het SeedSigner open-source project ook steunen door een donatie te doen in bitcoins!](https://seedsigner.com/donate/)**



*Krediet: sommige afbeeldingen in deze handleiding komen van de [officiële SeedSigner projectwebsite](https://seedsigner.com/) en [GitHub repository](https://github.com/SeedSigner/seedsigner).*