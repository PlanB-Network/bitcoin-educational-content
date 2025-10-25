---
name: Blockstream App - Liquid
description: Hoe Blockstream App configureren en de Liquid Network gebruiken
---
![cover](assets/cover.webp)


## 1. Inleiding


### 1.1 Lesdoel





- Deze tutorial legt uit hoe je de **Blockstream App** mobiele applicatie kunt gebruiken om een **Bitcoin Liquid** portefeuille te beheren, d.w.z. transacties die rechtstreeks op de Bitcoin "Liquid" zijketen zijn geregistreerd.
- Het behandelt de installatie, initiële configuratie, het aanmaken van een Software Wallet, en handelingen voor het ontvangen en verzenden van bitcoins op Liquid.
- Opmerking: Andere tutorials in de bijlagen behandelen Onchain, Watch-Only en de desktopversie.



### 1.2 Doelgroep





- **Beginners**: Gebruikers die hun bitcoins willen beheren met een intuïtieve mobiele applicatie die de Liquid Network integreert.
- **Intermediaire gebruikers**: Mensen die de onchain-functionaliteiten en privacyopties zoals Tor of SPV willen begrijpen.



### 1.3 Kennismaking met Liquid



**Liquid** is een **Sidechain** van Bitcoin, ontwikkeld door **[Blockstream](https://blockstream.com/Liquid/)**, ontworpen om sneller, meer Confidential Transactions en geavanceerde functionaliteit te bieden, terwijl het verbonden blijft met de hoofd Blockchain Bitcoin.



Een Sidechain is een onafhankelijke Blockchain die parallel werkt met Bitcoin, met behulp van een mechanisme dat bekend staat als **two-way peg**. Dit systeem vergrendelt bitcoins op de hoofd-Blockchain om **Liquid-Bitcoins (L-BTC)** te creëren, tokens die circuleren op Liquid Network, terwijl de waarde gelijk blijft aan die van de originele bitcoins. Fondsen kunnen op elk moment worden teruggegeven aan Blockchain Bitcoin.



![image](assets/fr/17.webp)






- (1) **Peg-in**: Bitcoins (BTC) worden door de Liquid federatie vastgezet op de Blockchain hoofdketen. In ruil daarvoor wordt een gelijkwaardige hoeveelheid Liquid-Bitcoins (L-BTC), die pariteit tussen de twee ketens garandeert, uitgegeven op Blockchain Liquid en naar de gebruiker gestuurd.





- (2) **Onafhankelijke transacties**: Transacties kunnen gelijktijdig en onafhankelijk draaien op de hoofd Blockchain (BTC) en Sidechain Liquid (L-BTC), afhankelijk van de vereisten van de gebruiker.





- (3) **Peg-out**: De gebruiker stuurt Liquid-bitcoins (L-BTC) terug naar de Liquid federatie. De federatie ontgrendelt dan een gelijkwaardige hoeveelheid bitcoins (BTC) op het hoofd Blockchain en draagt ze over aan de gebruiker.



Liquid vertrouwt op een **federatie** van vertrouwde deelnemers (exchanges, erkende Bitcoin bedrijven) die de blokvalidatie en bilaterale verankering beheren. In tegenstelling tot Blockchain Bitcoin, dat gedecentraliseerd is en afhankelijk van miners, is Liquid een **federated** netwerk, wat betekent dat de veiligheid en het bestuur afhangen van deze deelnemers. Hoewel dit een compromis betekent voor de decentralisatie, maakt het optimale prestaties en geavanceerde functionaliteit mogelijk.



![image](assets/fr/18.webp)



##### Waarom Liquid gebruiken?





- **Snelheid**: Transacties op Liquid worden bevestigd in ongeveer **1 minuut**, vergeleken met 10 minuten of meer voor onchain transacties, dankzij blokken die elke minuut worden gegenereerd door een federatie van validators.
- **Verbeterde vertrouwelijkheid**: Liquid gebruikt **Confidential Transactions**, dat de hoeveelheid en het type overgedragen activa verbergt, waardoor transacties meer privé worden (hoewel adressen zichtbaar blijven).
- **Lage kosten**: Transacties op Liquid zijn over het algemeen goedkoper, waardoor ze ideaal zijn voor frequente overschrijvingen of kleine bedragen.
- **Meerdere activa**: Naast L-BTC's ondersteunt Liquid de uitgifte van andere digitale activa, zoals stablecoins of tokens, voor gebruik in specifieke toepassingen.
- **Gebruikscases**: Liquid is bijzonder geschikt voor platformoverkoepelende uitwisselingen, snelle betalingen of toepassingen die slimme contracten vereisen, terwijl het gekoppeld blijft aan de beveiliging van Bitcoin.



**Opmerking: Deze tutorial richt zich op het gebruik van de Liquid via de Blockstream App. Voor een diepgaand begrip van de Liquid Network, vind je bronnen in de bijlage.**



### 1.4. Hot Wallet herinnering





- **Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: alle benamingen voor een applicatie die geïnstalleerd is op een smartphone, computer of elk ander apparaat dat verbonden is met het internet, waarmee privésleutels van een Bitcoin Wallet beheerd en beveiligd kunnen worden.
- In tegenstelling tot **hardware wallets**, ook bekend als **Cold wallets**, die sleutels offline isoleren, werken software wallets in een verbonden omgeving, waardoor ze kwetsbaarder zijn voor cyberaanvallen.





- **Aanbevolen gebruik**:
    - Ideaal voor het beheren van gemiddelde hoeveelheden Bitcoin, vooral voor dagelijkse transacties.
    - Geschikt voor beginners of gebruikers met beperkte middelen, voor wie een Hardware Wallet overbodig lijkt.





- **Beperkingen**: Minder veilig voor het opslaan van grote bedragen of langetermijnsparen. Kies in dit geval voor een Hardware Wallet.




## 2. Introductie van Blockstream App





- **Blockstream App** is een mobiele (iOS, Android) en desktop applicatie voor het beheren van Bitcoin wallets en activa op de Liquid Network. Het werd in 2016 overgenomen door [Blockstream](https://blockstream.com/) en heette eerder *Green Address* en daarna *Blockstream Green*.
- **Belangrijkste kenmerken**:
- **Onchain** transacties op Blockchain Bitcoin.
    - Transacties op het **Liquid** netwerk (Sidechain voor snelle, vertrouwelijke uitwisselingen).
- **Watch-only** portefeuilles voor het monitoren van fondsen zonder toegang tot sleutels.
    - Privacyopties: verbinding via **Tor**, verbinding met een **persoonlijk knooppunt** via Electrum, of **SPV** verificatie om de afhankelijkheid van knooppunten van derden te verminderen.
    - Functies **Replace-by-fee (RBF)** om onbevestigde transacties te versnellen.
- **Compatibiliteit**: Integreert hardware wallets zoals **Blockstream Jade**.
- **Interface**: Intuïtief voor beginners, met geavanceerde opties voor experts.
- **Opmerking**: Deze handleiding richt zich op het gebruik van Onchain. Andere tutorials in de bijlagen behandelen Onchain, Watch-Only en de desktopversie.




## 3. De Blockstream App installeren en configureren



### 3.1. downloaden





- Voor **Android**:
    - Download [Blockstream App] (https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet) uit de Google Play Store.
    - Alternatief: Installeer via het APK-bestand dat beschikbaar is op [Blockstream's officiële GitHub] (https://github.com/Blockstream/green_android).
- Voor **iOS**:
    - Download [Blockstream App] (https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590) van de App Store.
- **Opmerking**: Zorg ervoor dat je downloadt van officiële bronnen om frauduleuze toepassingen te voorkomen.



### 3.2. initiële configuratie





- **Beginscherm**: Bij de eerste keer openen toont de applicatie een scherm zonder een geconfigureerde Wallet. Aangemaakte of geïmporteerde portfolio's zullen hier later verschijnen.



![image](assets/fr/02.webp)





- **Instellingen aanpassen**: Klik op "Toepassingsinstellingen", pas de onderstaande opties aan, klik op "Opslaan", start de toepassing opnieuw en maak je portfolio aan.



![image](assets/fr/03.webp)



#### 3.2.1. Verbeterde privacy (alleen Android)





- **Functie**: Schakelt schermafbeeldingen uit, verbergt toepassingsvoorbeelden in het taakbeheer en vergrendelt de toegang wanneer de telefoon is vergrendeld.
- **Waarom?**: Beschermt uw gegevens tegen onbevoegde fysieke toegang of malware die het scherm buitmaakt.



#### 3.2.2. Verbinding via Tor





- **Functie**: Routeer netwerkverkeer via **Tor**, een anoniem netwerk dat je verbindingen versleutelt.
- **Waarom?**: Verberg je IP Address en bescherm je privacy, ideaal als je je netwerk niet vertrouwt (openbare Wi-Fi, bijvoorbeeld).
- **Nadeel**: Kan de toepassing vertragen door versleuteling.
- **Aanbeveling**: Activeer Tor als vertrouwelijkheid een prioriteit is, maar test de verbindingssnelheid.



#### 3.2.3. Verbinding maken met een persoonlijk knooppunt





- **Functie**: Verbindt de applicatie met je eigen **complete Bitcoin node** via een **Electrum server**.
- **Waarom?**: Biedt totale controle over Blockchain gegevens, waardoor u niet meer afhankelijk bent van Blockstream servers.
- **Vereiste**: Een geconfigureerd Bitcoin knooppunt.
- **Aanbeveling**: Gevorderde gebruikers die maximale soevereiniteit willen.



#### 3.2.4. SPV-verificatie





- **Functie**: Gebruikt **Simplified Payment Verification (SPV)** om bepaalde Blockchain gegevens direct te verifiëren zonder de hele keten te downloaden.
- **Waarom?**: Vermindert de afhankelijkheid van Blockstream's standaard node, terwijl het lichtgewicht blijft voor mobiele apparaten.
- **Nadeel**: Minder veilig dan een Full node, omdat het voor sommige informatie afhankelijk is van knooppunten van derden.
- **Aanbeveling**: Activeer SPV als je geen persoonlijk knooppunt kunt gebruiken, maar de voorkeur geeft aan een Full node voor optimale beveiliging.





## 4. Een Bitcoin-ketenportefeuille creëren



### 4.1. Begin met creëren





- **Let op**: Stel je portfolio op in een privéomgeving, zonder camera's of toeschouwers.
- Klik in het beginscherm op "Aan de slag" :



![image](assets/fr/04.webp)





- Als je een **Cold Wallet** (offline Wallet) wilt beheren: klik op **"Connect Jade"** om de Hardware Wallet Blockstream Jade of andere compatibele Cold wallets te gebruiken.



![image](assets/fr/05.webp)






- Het volgende scherm verschijnt:



![image](assets/fr/06.webp)






- (1) **"Instelling Mobiele Wallet"** : Maak een nieuwe Hot Wallet aan.
- (2) **"Herstellen vanaf back-up"**: Importeer een bestaande portefeuille met behulp van een Mnemonic-zin (12 of 24 woorden). Waarschuwing: Importeer de zin niet uit een Cold Wallet, omdat deze dan wordt blootgesteld op een aangesloten apparaat, waardoor de beveiliging ongeldig wordt.
- (3) **"Alleen kijken"**: Importeer een bestaande alleen-lezen portefeuille, om het saldo te bekijken (bijvoorbeeld van je Cold Wallet) zonder de Mnemonic zin bloot te leggen. Zie de "Watch Only" tutorial in de bijlage.



**In deze tutorial**: Klik op **"Setup Mobile Wallet"** om een Hot Wallet aan te maken.


Uw Wallet wordt automatisch aangemaakt en de Wallet startpagina, hier 'Mijn Wallet 5' genoemd, wordt weergegeven:



![image](assets/fr/07.webp)



**Belangrijk**: Blockstream App heeft het aanmaken van een Wallet vereenvoudigd door de seed zin van 12 woorden niet automatisch weer te geven. *Hoewel de portefeuille nu met één klik wordt aangemaakt, riskeert u de toegang tot uw fondsen te verliezen als u uw seed zin niet opslaat*.



### 4.2. seed zin opslaan





- Klik op het Wallet startscherm op het tabblad "Beveiliging" en vervolgens op de prompt "Back-up" of het menu "Herstelzin":



![image](assets/fr/08.webp)



De seed zin van 12 woorden wordt weergegeven zodat je deze kunt opslaan.





- Schrijf je herstelzin met de grootste zorg op. Schrijf het op papier of metaal en bewaar het op een veilige plaats (veilige, offline locatie). Deze zin is je enige manier om toegang te krijgen tot je bitcoins in het geval van verlies van je apparaat of verwijdering van de applicatie.
- Het is ook belangrijk om te weten dat iedereen met deze zin al je bitcoins kan stelen. Sla het nooit digitaal op:
 - Geen screenshot
 - Geen cloud-, e-mail- of berichtenback-ups
 - Geen kopiëren/plakken (risico van opslaan op klembord)



**! Dit punt is kritiek**. Voor meer informatie over back-up :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 4.3. Controleer seed zin



Voordat je geld verstuurt naar een Address die gekoppeld is aan deze seed zin, moet je de back-up van je 12 woorden testen.


Om dit te doen, schrijven we een referentie op, verwijderen de Wallet, herstellen deze met de back-up en controleren of de referentie ongewijzigd is.





- Klik op het Wallet startscherm op het tabblad "Instellingen", dan op "Wallet Details", en kopieer de zPub ([extended public key](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f):



![image](assets/fr/09.webp)



Opmerking: een zpub Address kan worden geïmporteerd in uw Blockstream-toepassing voor de functie "Alleen kijken" (zie Appendix).





- Verwijder de applicatie, herstel dan de Wallet via **"Restore from Backup"** door de Mnemonic zin in te voeren, en controleer of de zpub ongewijzigd is. Zo ja, dan is je back-up correct, en kun je geld naar de Wallet sturen.





- Om meer te leren over hoe je een hersteltest uitvoert, is hier een speciale tutorial :



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 4.4. Toegang tot de applicatie beveiligen



Vergrendel de toegang tot de applicatie met een sterke PIN-code:




- Ga in het Wallet startscherm naar **"Beveiliging"** en klik vervolgens op **"PIN"**
- Voer **een willekeurige PIN-code van 6 cijfers** in en bevestig deze.



**Biometrische optie**: Beschikbaar voor extra gemak, maar minder veilig dan een robuuste PIN-code (risico op onbevoegde toegang, bijv. vingerafdruk of gezichtsscan tijdens slaap).



**Noot**: De PIN beveiligt het apparaat, maar alleen de seed zin kan worden gebruikt om geld terug te krijgen.





## 5. De Liquid Wallet gebruiken



### 5.1. Bitcoins "L-BTC" ontvangen



Om Liquid-Bitcoins (L-BTC) te ontvangen, zijn er verschillende opties beschikbaar. Je kunt iemand vragen je direct wat te sturen door een Liquid te delen die Address ontvangt, wat hieronder wordt uitgelegd.



Als alternatief, Exchange uw bitcoins onchain of via de Lightning Network voor L-BTC met behulp van [een bridge zoals Boltz](https://boltz.Exchange/): voer uw Liquid in die Address ontvangt, doe de betaling zoals u verkiest, en ontvang uw L-BTC.





- Klik in het beginscherm van je portfolio op '"**Transact**" en vervolgens op **"Ontvangen"**.



![image](assets/fr/19.webp)





- Standaard toont de applicatie een lege **ontvangst Address, onchain** (SegWit v0 formaat, beginnend met `bc1q...`). Klik op "Bitcoin" om **Liquid Bitcoin** te selecteren:



![image](assets/fr/20.webp)





- **Opties**:
 - (1) Klik op de pijlen om nog een nieuwe Address te selecteren die aan deze seed zin is gekoppeld.
    - (2) Je kunt ook een Address kiezen uit de reeds gebruikte/weergegeven adressen, door te klikken op de drie puntjes rechtsboven en dan op "Lijst van adressen"
    - (3) Om een specifiek bedrag aan te vragen, klik op de drie puntjes rechtsboven, selecteer "Bedrag aanvragen" en voer het gewenste bedrag in. De QR wordt bijgewerkt en de Address wordt vervangen door een Bitcoin betalings-URI.



![image](assets/fr/21.webp)





- Deel de Address/URI door op "**Share**" te klikken, de tekst te kopiëren of de QR-code te scannen.
- **Verificatie**: Controleer de Address die gedeeld is met de ontvanger zoveel mogelijk om fouten of aanvallen te voorkomen (bijv. malware die het klembord wijzigt).



### 5.2. bitcoins versturen





- Klik in het beginscherm van je portfolio op "**Transact**" en vervolgens op **"Verzenden"** :



![image](assets/fr/22.webp)





- **Vul gegevens in**:
    - (1) Voer de **Address van de ontvanger** in door deze op te plakken of een QR-code te scannen.
    - (2) Controleer de activa en de rekening waarvan het geld wordt verstuurd.
    - (3) Geef het **bedrag** aan dat moet worden verzonden. Je kunt de eenheid kiezen: L-BTC, L-satoshis, USD, ...



![image](assets/fr/23.webp)





- **Check**:
    - Controleer de Address, het bedrag en de kosten op het overzichtsscherm.
    - Een Address fout kan leiden tot onomkeerbaar verlies van geld. Pas op voor malware die het klembord wijzigt.



![image](assets/fr/24.webp)





- **Bevestiging**: Schuif op de knop "Verzenden" om de transactie te ondertekenen en te distribueren.
- **Follow-up**: In het tabblad "Transactie" van Wallet verschijnt de transactie als "Onbevestigd", dan "Bevestigd", dan "Voltooid":



![image](assets/fr/25.webp)





- De tijd tussen 2 blokken is 1 minuut op Liquid, dus de transactie wordt snel bevestigd en voltooid.




## Bijlagen



### A1. Andere Blockstream App tutorials



Het Onchain netwerk gebruiken



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

Een Wallet importeren en volgen in de modus Alleen kijken



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

Desktop versie



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da



### A2. Beste praktijken



Volg deze aanbevelingen om **Blockstream App** veilig en efficiënt te gebruiken. Ze zullen u helpen uw geld te beschermen, uw transacties te optimaliseren en uw vertrouwelijkheid te bewaren op de **Bitcoin (onchain)**, **Liquid** en **Lightning** netwerken.





- **Beveilig je herstelzin**:
 - Handleiding: Uw Mnemonic zin opslaan



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Gebruik **beveiligde verificatie**:
 - Activeer een **sterke PIN** of **biometrische verificatie** (vingerafdruk of gezichtsherkenning) om de toegang tot de applicatie te beveiligen.
 - Deel nooit uw PIN- of biometrische gegevens.





- **Bescherm uw privacy** :
 - generate een nieuwe Address voor elke ontvangst aan de ketting of Liquid om het traceren op de Blockchain te beperken.
 - Activeer de functies "Verbeterde privacy", "Tor" en "SPV".
 - Voor maximale vertrouwelijkheid verbindt u uw Wallet met uw eigen Bitcoin knooppunt via een Electrum-server in plaats van het openbare knooppunt te gebruiken





- **Kies het netwerk dat het beste bij uw behoeften past**:
- **Onchain**: Voorkeur voor langetermijnbewaring of transacties met een grote waarde (kosten te verwaarlozen in verhouding tot het bedrag).
- **Liquid**: Voor snelle, goedkope overdrachten met verbeterde vertrouwelijkheid.
- **Lightning**: Kies voor directe, goedkope overschrijvingen voor kleine bedragen.





- Controleer altijd de **verzendadressen**:
 - Controleer de Address zorgvuldig voordat je geld verstuurt. Geld dat naar de verkeerde Address wordt gestuurd, is voor altijd verloren. Gebruik kopiëren/plakken of QR-code scannen, kopieer/wijzig nooit een Address met de hand.





- **Kosten optimaliseren**:
 - Kies voor onchain transacties de juiste tarieven (langzaam, gemiddeld, snel) op basis van urgentie en netwerkcongestie.
 - Gebruik Liquid of Lightning voor kleine hoeveelheden.





- Houd de applicatie up-to-date




### A3. Extra middelen





- **Officiële links:**
- [Officiële website](https://blockstream.com/)
- [Ondersteuning voor de mobiele toepassing](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/): documentatie en chat
- [GitHub](https://github.com/Blockstream/green_android)





- **Blokverkenners:**
 - on chain : **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Bliksem: **[1ML (Lightning Network)](https://1ml.com/)**





- **Leren en tutorials:** **[Plan ₿ Network](https://planb.network/)**:
 - Je herstelzin beveiligen



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- **Liquid Network** :
- [Woordenlijst](https://planb.network/fr/resources/glossary/liquid-network)




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727




- **Lightning Network**:
- [Woordenlijst](https://planb.network/fr/resources/glossary/lightning-network)



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb