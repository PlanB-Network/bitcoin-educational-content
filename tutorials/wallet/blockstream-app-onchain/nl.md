---
name: Blockstream-app - Onchain
description: Blockstream App instellen op mobiel en onchain-transacties beheren
---
![cover](assets/cover.webp)


## 1. Inleiding


### 1.1 Lesdoel





- Deze tutorial legt uit hoe je de **Blockstream App** mobiele applicatie kunt gebruiken om een Bitcoin **onchain** Wallet te beheren, d.w.z. transacties die direct op de hoofd Blockchain Bitcoin zijn geregistreerd.
- Het behandelt de installatie, de initiële configuratie, het aanmaken van een Software Wallet en handelingen voor het ontvangen en verzenden van bitcoins.
- Opmerking: Andere tutorials in de bijlagen behandelen Liquid, Watch-Only en de desktopversie.



![image](assets/fr/01.webp)



### 1.2 Doelgroep





- Beginners**: Gebruikers die hun bitcoins willen beheren met een intuïtieve mobiele applicatie.
- Intermediaire gebruikers**: Mensen die de onchain-functionaliteiten en privacyopties zoals Tor of SPV willen begrijpen.



### 1.3. Herinneringen over Hot portefeuilles





- Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: alle namen voor een applicatie die geïnstalleerd is op een smartphone, computer of een ander apparaat met internetverbinding, waarmee privésleutels van een Bitcoin Wallet beheerd en beveiligd kunnen worden.
- In tegenstelling tot **hardware wallets**, ook bekend als **Cold wallets**, die sleutels offline isoleren, werken software wallets in een verbonden omgeving, waardoor ze kwetsbaarder zijn voor cyberaanvallen.





- Aanbevolen gebruik** :
    - Ideaal voor het beheren van gemiddelde hoeveelheden Bitcoin, vooral voor dagelijkse transacties.
    - Geschikt voor beginners of gebruikers met beperkte middelen, voor wie een Hardware Wallet overbodig lijkt.





- Beperkingen**: Minder veilig voor het opslaan van grote bedragen of langetermijnsparen. Kies in dit geval voor een Hardware Wallet.




## 2. Introductie van Blockstream App





- Blockstream App** is een mobiele (iOS, Android) en desktop applicatie voor het beheren van Bitcoin portefeuilles en activa op de Liquid Network. Het werd in 2016 overgenomen door [Blockstream](https://blockstream.com/) en heette eerder *Green Address* en daarna *Blockstream Green*.
- Belangrijkste kenmerken** :
    - Onchain** transacties op Blockchain Bitcoin.
    - Netwerktransacties **Liquid** (Sidechain voor snelle, vertrouwelijke uitwisselingen).
    - Watch-only** portefeuilles voor het monitoren van fondsen zonder toegang tot sleutels.
    - Privacyopties: verbinding via **Tor**, verbinding met een **persoonlijk knooppunt** via Electrum, of **SPV** verificatie om de afhankelijkheid van knooppunten van derden te verminderen.
    - Functies **Replace-by-fee (RBF)** om onbevestigde transacties te versnellen.
- Compatibiliteit**: Integreert hardware wallets zoals **Blockstream Jade**.
- Interface**: Intuïtief voor beginners, met geavanceerde opties voor experts.
- Opmerking**: Deze handleiding richt zich op het gebruik van de onchain. Andere tutorials in de bijlagen behandelen Liquid, Watch-Only en de desktopversie.



## 3. De Blockstream App installeren en configureren



### 3.1. downloaden





- Voor Android** :
    - Download [Blockstream App] (https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet) uit de Google Play Store.
    - Alternatief: Installeer via het APK-bestand dat beschikbaar is op [Blockstream's officiële GitHub] (https://github.com/Blockstream/green_android).
- Voor iOS** :
    - Download [Blockstream App] (https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590) van de App Store.
- Opmerking**: Zorg ervoor dat je downloadt van officiële bronnen om frauduleuze toepassingen te voorkomen.



### 3.2. initiële configuratie





- Beginscherm**: Wanneer de toepassing voor het eerst wordt geopend, toont het een scherm zonder een geconfigureerde Wallet. Aangemaakt of geïmporteerd portfolio zal hier later verschijnen. Aangemaakte of geïmporteerde portfolio's zullen hier later verschijnen.



![image](assets/fr/02.webp)





- Instellingen aanpassen**: Klik op "Toepassingsinstellingen", pas de onderstaande opties aan, klik op "Opslaan", start de toepassing opnieuw en maak je portfolio aan.



![image](assets/fr/03.webp)



#### 3.2.1. Verbeterde privacy (alleen Android)





- Functie**: Schakelt schermafbeeldingen uit, verbergt toepassingsvoorbeelden in het taakbeheer en vergrendelt de toegang wanneer de telefoon is vergrendeld.
- Waarom?** : Beschermt uw gegevens tegen onbevoegde fysieke toegang of malware die het scherm buitmaakt.


#### 3.2.2. Verbinding via Tor





- Functie**: Routeer netwerkverkeer via **Tor**, een anoniem netwerk dat je verbindingen versleutelt.
- Waarom?**: Verberg je IP Address en bescherm je privacy, ideaal als je je netwerk niet vertrouwt (openbare Wi-Fi, bijvoorbeeld).
- Nadeel**: Kan de toepassing vertragen door versleuteling.
- Aanbeveling**: Activeer Tor als vertrouwelijkheid een prioriteit is, maar test de verbindingssnelheid.


#### 3.2.3. Verbinding maken met een persoonlijk knooppunt





- Functie**: Verbindt de applicatie met je eigen **complete Bitcoin node** via een **Electrum** server.
- Waarom?**: Biedt totale controle over Blockchain gegevens, waardoor u niet meer afhankelijk bent van Blockstream servers.
- Vereiste**: Een geconfigureerd Bitcoin knooppunt.
- Aanbeveling**: Gevorderde gebruikers die maximale soevereiniteit zoeken.


#### 3.2.4. SPV-verificatie





- Functie**: Gebruikt **Simplified Payment Verification (SPV)** om bepaalde Blockchain gegevens direct te verifiëren zonder de hele keten te downloaden.
- Waarom?**: Vermindert de afhankelijkheid van Blockstream's standaard node, terwijl het lichtgewicht blijft voor mobiele apparaten.
- Nadeel**: Minder veilig dan een Full node, omdat het voor sommige informatie afhankelijk is van knooppunten van derden.
- Aanbeveling**: Activeer SPV als u geen persoonlijk knooppunt kunt gebruiken, maar de voorkeur geeft aan een Full node voor optimale beveiliging.





## 4. Een Bitcoin-ketenportefeuille creëren



### 4.1. Begin met creëren





- Let op**: Stel je portfolio op in een privéomgeving, zonder camera's of toeschouwers.
- Klik in het beginscherm op "Aan de slag" :



![image](assets/fr/04.webp)





- Als je een **Cold Wallet** (offline Wallet) wilt beheren: klik op **"Connect Jade"** om de Hardware Wallet Blockstream Jade of andere compatibele Cold wallets te gebruiken.



![image](assets/fr/05.webp)





- Het volgende scherm verschijnt:



![image](assets/fr/06.webp)





- (1) **"Setup Mobile Wallet"** : Maak een nieuwe Hot Wallet (Hot Wallet).
- (2) **"Herstellen vanaf back-up"**: Importeer een bestaande portefeuille met behulp van een Mnemonic-zin (12 of 24 woorden). Let op: Importeer geen Cold Wallet zinsdeel, omdat het op een aangesloten apparaat wordt weergegeven, waardoor de beveiliging ongeldig wordt.
- (3) **"Alleen kijken"**: Importeer een bestaande alleen-lezen portefeuille, om het saldo te bekijken (bijvoorbeeld van je Cold Wallet) zonder de Mnemonic zin bloot te leggen. Zie de Watch Only tutorial in de bijlage.



**In deze tutorial**: Klik op **"Instelling Mobiele Wallet"** om een Hot Wallet aan te maken.


Uw Wallet wordt automatisch aangemaakt en de Wallet-startpagina, hier 'Mijn Wallet 5' genoemd, wordt weergegeven:



![image](assets/fr/07.webp)



**Belangrijk**: Blockstream App heeft het aanmaken van een Wallet vereenvoudigd door de seed zin van 12 woorden niet automatisch weer te geven. *Hoewel de portefeuille nu met één klik wordt aangemaakt, riskeert u de toegang tot uw fondsen te verliezen als u uw seed zin niet opslaat*.



### 4.2. seed zin opslaan





- Klik op het Wallet startscherm op het tabblad "Beveiliging" en vervolgens op de prompt "Back-up" of het menu "Herstelzin":



![image](assets/fr/08.webp)



De seed 12-woordzin wordt weergegeven zodat je deze kunt opslaan.





- Schrijf je herstelzin met de grootste zorg op. Schrijf het op papier of metaal en bewaar het op een veilige plaats (veilige, offline locatie). Deze zin is je enige manier om toegang te krijgen tot je bitcoins in het geval van verlies van je apparaat of verwijdering van de applicatie.
- Het is ook belangrijk om te weten dat iedereen met deze zin al je bitcoins kan stelen. Sla het nooit digitaal op:
 - Geen screenshot
 - Geen cloud-, e-mail- of berichtenback-ups
 - Geen kopiëren/plakken (risico van opslaan op klembord)



**! Dit punt is kritiek**. Voor meer informatie over back-up :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 4.3. seed zin bevestigen



Voordat je geld naar een Address stuurt die verbonden is met deze seed zin, moet je de back-up van je 12 woorden testen.



Om dit te doen, schrijven we een referentie op, verwijderen de Wallet, herstellen deze met de back-up en controleren of de referentie ongewijzigd is.





- Klik op het beginscherm van de Wallet op het tabblad 'Instellingen', vervolgens op 'Wallet Details' en kopieer de zPub ([extended public key](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/8dcffce1-31bd-5e0b-965b-735f5f9e4602):



![image](assets/fr/09.webp)



Opmerking: een zpub Address kan in uw Blockstream-toepassing worden geïmporteerd voor de "Watch Only" functie (zie Appendix).





- Verwijder de applicatie, herstel dan de Wallet via **"Restore from Backup"** door de Mnemonic zin in te voeren, en controleer of de zpub ongewijzigd is. Zo ja, dan is je back-up correct en kun je geld naar de Wallet sturen.





- Om meer te leren over hoe je een hersteltest uitvoert, is hier een speciale tutorial :



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 4.5. Toegang tot de applicatie beveiligen



Vergrendel de toegang tot de applicatie met een sterke PIN-code:




- Ga in het Wallet startscherm naar **"Beveiliging"** en klik vervolgens op **"PIN"**
- Voer **een willekeurige PIN-code van 6 cijfers** in en bevestig deze.



**Biometrische optie**: Beschikbaar voor extra gemak, maar minder veilig dan een robuuste PIN-code (risico op onbevoegde toegang, bijv. vingerafdruk of gezichtsscan tijdens slaap).



**Noot**: De PIN beveiligt het apparaat, maar alleen de seed zin kan worden gebruikt om geld op te halen.





## 5. De Wallet op de ketting gebruiken



### 5.1. Bitcoins ontvangen





- Klik in het beginscherm van je portfolio op '"**Transact**" en vervolgens op **"Ontvangen"**.



![image](assets/fr/10.webp)





- De applicatie toont een **blanke ontvangst Address** (SegWit v0 formaat, beginnend met `bc1q...`). Het gebruik van een nieuwe Address elke keer dat je Bitcoin ontvangt, verbetert je vertrouwelijkheid.





- Opties** :
    - (1) "Bitcoin": klik om een onchain of Liquid zending te selecteren en kies het goed.
    - (2) Klik op de pijlen om een andere nieuwe Address te selecteren die is gekoppeld aan deze seed zin.
    - (3) U kunt ook een Address kiezen uit de reeds gebruikte/getoonde adressen, door te klikken op de drie puntjes rechtsboven en dan op "Lijst van adressen"
    - (4) Om een specifiek bedrag aan te vragen, klik op de drie puntjes rechtsboven, selecteer "Bedrag aanvragen" en voer het gewenste bedrag in. De QR wordt bijgewerkt en de Address wordt vervangen door een Bitcoin betalings-URI.




![image](assets/fr/11.webp)





- Deel de Address/URI door op "**Share**" te klikken, de tekst te kopiëren of de QR-code te scannen.
- Verificatie**: Controleer de Address die met de ontvanger is gedeeld zo goed mogelijk om fouten of aanvallen te voorkomen (bijv. malware die het klembord wijzigt).



### 5.2. bitcoins versturen





- Klik in het beginscherm van je portfolio op "**Transact**" en vervolgens op **"Verzenden"** :



![image](assets/fr/12.webp)





- Vul gegevens in** :
    - (1) Voer de **Address van de ontvanger** in door deze op te plakken of een QR-code te scannen.
    - (2) Controleer de activa en de rekening waarvan het geld wordt verstuurd.
    - (3) Geef het **bedrag** aan dat moet worden verzonden. Je kunt de eenheid kiezen: BTC, satoshis, USD, ...


Het minimumbedrag (dush-limiet) op 03/08/2025 is 546 Sats.




    - (4) Selecteer **transactiekosten** :
        - Kies uit de voorgestelde opties (bijv. snel, medium, langzaam) afhankelijk van de urgentie en er wordt een geschatte overdrachtstijd weergegeven.
        - Pas voor aangepaste kosten handmatig het aantal Satoshi per vbytes aan (zie [Mempool.space](https://Mempool.space/) voor markttarieven).




![image](assets/fr/13.webp)





- Check** :
    - Controleer de Address, het bedrag en de kosten op het overzichtsscherm.
    - Een Address fout kan leiden tot onomkeerbaar verlies van geld. Pas op voor malware die het klembord wijzigt.



![image](assets/fr/14.webp)





- Bevestiging**: Schuif op de knop "Verzenden" om de transactie te ondertekenen en te distribueren.
- Follow-up**: In het tabblad "Transactie" van Wallet verschijnt de transactie als "in behandeling" tot de bevestiging (1 tot 6 bevestigingen):



![image](assets/fr/15.webp)





- Zolang de transactie niet is bevestigd, kun je met de functie "Replace by fee" (zie Appendix) de afhandeling versnellen door de transactiekosten te verhogen:



![image](assets/fr/16.webp)




## Bijlagen



### A1. Andere Blockstream-tutorials



De Liquid Network gebruiken



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

Een Wallet importeren en volgen in de modus Alleen kijken



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb

Desktop versie



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da


### A2. Uitleg van Replace-by-fee (RBF)



**Definitie**: Replace-by-fee (RBF) is een functie van het Bitcoin netwerk die de verzender toestaat om de bevestiging van een **onchain** transactie te versnellen door akkoord te gaan met het betalen van een hogere vergoeding.



**Limieten** :




- RBF is niet beschikbaar voor Liquid of Lightning-transacties.
- De initiële transactie moet gemarkeerd worden als RBF-compatibel wanneer het aangemaakt wordt, wat Blockstream App automatisch doet.



**Meer info:**




- [Woordenlijst](https://planb.network/fr/resources/glossary/rbf-replacebyfee)




### A3. Beste praktijken



Volg deze aanbevelingen om **Blockstream App** veilig en efficiënt te gebruiken. Ze zullen u helpen uw geld te beschermen, uw transacties te optimaliseren en uw vertrouwelijkheid te bewaren op de **Bitcoin (onchain)**, **Liquid** en **Lightning** netwerken.





- Beveilig je herstelzin** :
 - Handleiding: Uw Mnemonic zin opslaan



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Gebruik beveiligde verificatie** :
 - Activeer een **sterke PIN** of **biometrische verificatie** (vingerafdruk of gezichtsherkenning) om de toegang tot de applicatie te beveiligen.
 - Deel nooit uw PIN- of biometrische gegevens.





- Bescherm uw privacy** :
 - generate een nieuwe Address voor elke onchain of Liquid ontvangst om traceren op de Blockchain te beperken.
 - Activeer de functies "Verbeterde privacy", "Tor" en "SPV".
 - Voor maximale vertrouwelijkheid verbindt u uw Wallet met uw eigen Bitcoin knooppunt via een Electrum server in plaats van het openbare knooppunt te gebruiken





- Kies het netwerk dat het beste bij uw behoeften past** :
 - Onchain**: Voorkeur voor langetermijnbewaring of transacties met een grote waarde (kosten te verwaarlozen in verhouding tot het bedrag).
 - Liquid**: Gebruik voor snelle, goedkope overdrachten met verbeterde vertrouwelijkheid.
 - Lightning**: Kies voor directe, goedkope overschrijvingen voor kleine bedragen.





- Controleer altijd de verzendadressen** :
 - Controleer de Address zorgvuldig voordat je geld verstuurt. Geld dat naar de verkeerde Address wordt gestuurd, is voor altijd verloren. Gebruik kopiëren/plakken of QR-code scannen, kopieer/wijzig nooit een Address met de hand.





- Kosten optimaliseren** :
 - Kies voor onchain transacties de juiste tarieven (langzaam, gemiddeld, snel) op basis van urgentie en netwerkcongestie.
 - Gebruik Liquid of Lightning voor kleine hoeveelheden.





- Houd de applicatie up-to-date




### A4. Extra middelen





- Officiële links:**
 - [Officiële website](https://blockstream.com/)**
 - [Ondersteuning voor de mobiele toepassing](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/)** : documentatie en chat
 - [GitHub](https://github.com/Blockstream/green_android)**





- Blokverkenners :**
 - on chain : **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Bliksem: **[1ML (Lightning Network)](https://1ml.com/)**





- Leren en tutorials:** **[Plan ₿ Network](https://planb.network/)** :
 - Je herstelzin beveiligen



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Liquid Network** :
 - [Woordenlijst](https://planb.network/fr/resources/glossary/liquid-network)**



https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727




- Lightning Network** :
 - [Woordenlijst](https://planb.network/fr/resources/glossary/lightning-network)**



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb