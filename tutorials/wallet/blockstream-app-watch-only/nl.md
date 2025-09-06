---
name: Blockstream App - Alleen kijken
description: Hoe configureer ik een Watch-only wallet op de Blockstream App?
---

![cover](assets/cover.webp)


## 1. Inleiding


### 1.1 Doel van de zelfstudie





- Deze tutorial legt uit hoe je de **Watch-Only** functie van de **Blockstream App** mobiele applicatie kunt instellen en gebruiken om een Bitcoin Wallet te monitoren zonder toegang tot de private sleutels.
- Het behandelt de installatie, de initiële configuratie, het importeren van een uitgebreide publieke sleutel en het gebruik ervan om saldi en generate ontvangstadressen bij te houden.
- Opmerking: Andere tutorials, in de bijlage, behandelen Onchain, Liquid en de desktopversie.



### 1.2. Doelgroep





- Beginners**: Gebruikers die een Bitcoin portefeuille (vaak gekoppeld aan een Hardware Wallet) willen bewaken via een intuïtieve mobiele applicatie.
- Gemiddelde gebruikers**: Mensen die alleen-lezen portefeuilles willen beheren terwijl ze privacyopties gebruiken zoals Tor of SPV.
- Hardware Wallet eigenaren**: Om hun saldo en generate adressen te controleren zonder hun apparaat aan te sluiten.
- Bedrijven en winkels** :
 - Traceer je transacties voor boekhoudkundige doeleinden zonder je privésleutels bloot te geven.
 - Verifieer ontvangen transacties zonder hun privésleutels in te voeren in online betaalsystemen.
 - Medewerkers in staat stellen om generate nieuwe ontvangstadressen te geven zonder toegang te hebben tot privésleutels.
- Organisaties en crowdfunding**: Geef het saldo transparant weer aan donateurs zonder toegang te geven tot fondsen.



### 1.3. Watch-Only introduceren



Met een **Watch-Only** Wallet kun je de transacties en het saldo van een Bitcoin Wallet controleren zonder toegang te hebben tot de private sleutels. In tegenstelling tot een conventionele Wallet, slaat het alleen openbare gegevens op, zoals de **uitgebreide **publieke sleutel** (die aanleiding gaf tot "**xpub**", daarna "zpub", "ypub", etc.), die het mogelijk maakt om ontvangstadressen te verkrijgen en de transactiegeschiedenis op de Blockchain Bitcoin bij te houden. De afwezigheid van privésleutels maakt het onmogelijk om geld uit te betalen vanuit de applicatie, wat de veiligheid ten goede komt.



![image](assets/fr/10.webp)



**Waarom een Watch-only wallet gebruiken?





- Beveiliging**: Ideaal voor het bewaken van een portfolio beveiligd door een **Hardware Wallet** zonder privé-sleutels op een aangesloten apparaat bloot te leggen.
- Gemak**: Hiermee kunt u het saldo controleren en generate nieuwe ontvangstadressen geven zonder de Hardware Wallet aan te sluiten.
- Vertrouwelijkheid**: Compatibel met opties zoals **Tor** of **SPV** om afhankelijkheid van servers van derden te beperken.
- Gebruikscases**: Onderweg geld traceren, adressen genereren om betalingen te ontvangen of transacties verifiëren zonder het risico van privésleutels.



![image](assets/fr/01.webp)



### 1.4. Uitgebreide openbare sleutels



Een **extended public key** (xpub, ypub, zpub, enz.) is een stuk data afgeleid van een Bitcoin Wallet dat alle child public keys en hun geassocieerde ontvangstadressen genereert, zonder toegang te geven tot de private keys.





- Hoe het werkt** : De uitgebreide openbare sleutel wordt gegenereerd uit de seed frase via een deterministisch proces (BIP-32). Het creëert een hiërarchische boom van child public keys, die elk omgezet kunnen worden in een ontvangen Address. Door gebruik te maken van hetzelfde afleidingspad (bijv. `m/44'/0'/0'`) als de bekeken Wallet, genereert de Watch-only wallet dezelfde adressen, waardoor fondsen kunnen worden getraceerd en nieuwe ontvangstadressen kunnen worden aangemaakt.



![image](assets/fr/11.webp)





- Uitgebreide openbare sleutel typen
 - xpub**: Gebruikt voor legacy portfolio's (adressen beginnend met "1", BIP-44) en Taproot portfolio's (adressen beginnend met "bc1p", BIP-86).
 - ypub**: Ontworpen voor compatibele SegWit portemonnees (adressen beginnend met "3", BIP-49).
 - zpub**: Gekoppeld aan native SegWit portefeuilles (adressen beginnend met "bc1q", BIP-84).
 - Andere (tpub, upub, vpub, enz.)**: Gebruikt voor alternatieve netwerken (zoals Testnet) of specifieke standaarden. Bijvoorbeeld, tpub is voor het Testnet netwerk.





- Onderscheid** : De keuze tussen xpub, ypub of zpub hangt af van het Address type (legacy, SegWit, Taproot of genest SegWit) en de BIP standaard die door de Wallet gebruikt wordt. Controleer het formaat dat vereist is door je bronportfolio om compatibiliteit met Blockstream App te garanderen.





- Veiligheid en vertrouwelijkheid** : De uitgebreide openbare sleutel is niet gevoelig in termen van veiligheid, omdat er geen geld mee kan worden uitgegeven (geen toegang tot privésleutels). Het is echter wel gevoelig in termen van vertrouwelijkheid, omdat het alle openbare adressen en de bijbehorende transactiegeschiedenis onthult.



**Aanbeveling**: Bescherm uw uitgebreide openbare sleutel als gevoelige informatie.



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 1.5. Hot Wallet herinnering





- Hot Wallet**, **Software Wallet**, **Wallet mobile**, **Software Wallet**: alle benamingen voor een applicatie die geïnstalleerd is op een smartphone, computer of elk ander apparaat dat verbonden is met het internet, waarmee privésleutels van een Bitcoin Wallet beheerd en beveiligd kunnen worden.
- In tegenstelling tot **hardware wallets**, ook bekend als **Cold wallets**, die sleutels offline isoleren, werken software wallets in een verbonden omgeving, waardoor ze kwetsbaarder zijn voor cyberaanvallen.





- Aanbevolen gebruik** :
    - Ideaal voor het beheren van gemiddelde hoeveelheden Bitcoin, vooral voor dagelijkse transacties.
    - Geschikt voor beginners of gebruikers met beperkte middelen, voor wie een Hardware Wallet misschien overbodig lijkt.





- Beperkingen**: Minder veilig voor het opslaan van grote bedragen of langetermijnsparen. Kies in dit geval voor een Hardware Wallet.




## 2. Introductie van Blockstream App





- Blockstream App** is een mobiele (iOS, Android) en desktop applicatie voor het beheren van Bitcoin portefeuilles en activa op de Liquid Network. Het werd in 2016 overgenomen door [Blockstream](https://blockstream.com/) en heette eerder *Green Address* en daarna *Blockstream Green*.
- Belangrijkste kenmerken** :
    - Onchain** transacties op Blockchain Bitcoin.
    - Transacties op het **Liquid** netwerk (Sidechain voor snelle, vertrouwelijke uitwisselingen).
    - Watch-only** portefeuilles voor het monitoren van fondsen zonder toegang tot sleutels.
    - Privacyopties: verbinding via **Tor**, verbinding met een **persoonlijk knooppunt** via Electrum, of **SPV** verificatie om de afhankelijkheid van knooppunten van derden te verminderen.
    - Functies **Replace-by-fee (RBF)** om onbevestigde transacties te versnellen.
- Compatibiliteit**: Integreert hardware wallets zoals **Blockstream Jade**.
- Interface**: Intuïtief voor beginners, met geavanceerde opties voor experts.
- Opmerking**: Deze handleiding richt zich op het gebruik van Onchain. Andere tutorials in de bijlagen behandelen Onchain, Watch-Only en de desktopversie.




## 3. De Blockstream App installeren en configureren



### 3.1. downloaden





- Voor Android** :
    - Download [Blockstream App] (https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet) uit de Google Play Store.
    - Alternatief: Installeer via het APK-bestand dat beschikbaar is op [Blockstream's officiële GitHub] (https://github.com/Blockstream/green_android).
- Voor iOS** :
    - Download [Blockstream App] (https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590) van de App Store.
- Opmerking**: Zorg ervoor dat je downloadt van officiële bronnen om frauduleuze toepassingen te voorkomen.



### 3.2. initiële configuratie





- Beginscherm**: Bij de eerste keer openen toont de toepassing een scherm zonder een geconfigureerd Wallet. Aangemaakte of geïmporteerde portfolio's zullen hier later verschijnen.



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





- Functie**: Verbindt de applicatie met je eigen **complete Bitcoin node** via een **Electrum server**.
- Waarom?**: Biedt totale controle over Blockchain gegevens, waardoor u niet meer afhankelijk bent van Blockstream servers.
- Vereiste**: Een geconfigureerd Bitcoin knooppunt.
- Aanbeveling**: Gevorderde gebruikers die maximale soevereiniteit willen.



#### 3.2.4. SPV-verificatie





- Functie**: Gebruikt **Simplified Payment Verification (SPV)** om bepaalde Blockchain gegevens direct te verifiëren zonder de hele keten te downloaden.
- Waarom?**: Vermindert de afhankelijkheid van Blockstream's standaard node, terwijl het lichtgewicht blijft voor mobiele apparaten.
- Nadeel**: Minder veilig dan een Full node, omdat het voor sommige informatie afhankelijk is van knooppunten van derden.
- Aanbeveling**: Activeer SPV als je geen persoonlijk knooppunt kunt gebruiken, maar de voorkeur geeft aan een Full node voor optimale beveiliging.





## 4. Een Bitcoin "Watch-only" portefeuille creëren



### 4.1. Uitgebreide openbare sleutel herstellen



Om een Watch-only wallet in te stellen, moet je eerst de uitgebreide publieke sleutel (xpub, ypub, zpub, enz.) van de Wallet die je wilt bewaken verkrijgen. Deze informatie is meestal beschikbaar in de instellingen of "Wallet informatie" sectie van je software of Hardware Wallet.





- Voorbeeld met Blockstream App: Vanaf het Wallet startscherm, ga naar "Instellingen", dan "Wallet Details", en kopieer de zpub :



![image](assets/fr/09.webp)





- Alternatief 1: generate een QR-code met de uitgebreide openbare sleutel om in de volgende stap te scannen.
- Alternatief 2: Gebruik een output descriptor als je Wallet die biedt.



### 4.2. Wallet Watch-only importeren





- Let op**: Stel je portfolio op in een privéomgeving, zonder camera's of toeschouwers.
- Klik in het beginscherm op "Een nieuwe portefeuille aanmaken" en vervolgens op "Aan de slag" :



![image](assets/fr/04.webp)





- Het volgende scherm verschijnt:



![image](assets/fr/06.webp)






- (1) **"Instelling Mobile Wallet"** : Maak een nieuwe Hot Wallet. Zie de "Blockstream App - Onchain" tutorial in de bijlage.
- (2) **"Herstellen vanaf back-up"**: Importeer een bestaande portefeuille met behulp van een Mnemonic-zin (12 of 24 woorden). Let op: Importeer geen zinsdeel van een Cold Wallet, omdat het zal worden blootgesteld op een aangesloten apparaat, waardoor de beveiliging ongeldig wordt.
- (3) **"Watch-Only"**: de optie waarin we geïnteresseerd zijn voor deze tutorial.





- Selecteer vervolgens "**Enkel handtekening**" en het "**Bitcoin**" netwerk:



![image](assets/fr/12.webp)





- Plak de uitgebreide openbare sleutel (xpub, ypub, zpub, enz.), scan de bijbehorende QR-code of voer een output descriptor in. Zelfs als de toepassing "xpub" specificeert, zijn de sleutels ypub, zpub, enz. ook geautoriseerd. Klik vervolgens op "Verbinden":



![image](assets/fr/13.webp)




### 4.3. De Wallet Watch-only gebruiken



Eenmaal geïmporteerd, toont de Watch-only wallet het totale saldo en de transactiegeschiedenis van adressen afgeleid van de uitgebreide publieke sleutel. Alleen onchain transacties zijn zichtbaar (Liquid transacties worden genegeerd). Om een Liquid Wallet te controleren, herhaalt u het importeren door "Liquid" te selecteren in de vorige stap.





- Bekijk saldo en geschiedenis**: bekijk vanaf het beginscherm het totale saldo en de transactiegeschiedenis van de ketting:



![image](assets/fr/14.webp)





- generate een ontvangende Address**: Klik op "Transactie", dan op "Ontvangen", om een nieuwe Address op de ketting te creëren. Deel het via QR-code of kopieer het om fondsen te ontvangen:



![image](assets/fr/15.webp)





- Geld verzenden**: Klik op **"Transactie"** en vervolgens op **"Verzenden"**. U kunt :
 - De Address van de ontvanger.
 - Het bedrag van de transactie.
 - Transactiekosten.



Omdat de Watch-only wallet echter niet over de private sleutels beschikt, kunt u niet direct geld versturen. Om de transactie te ondertekenen, sluit je je Hardware Wallet of Exchange PSBT's aan door de QR-codes te scannen (een optie die bijvoorbeeld beschikbaar is op de Coldcard Q).



![image](assets/fr/16.webp)





- Opmerking**: Controleer altijd de ontvangende Address en transactiegegevens om fouten te voorkomen. Fondsen die naar de verkeerde Address worden gestuurd, kunnen niet worden teruggevorderd.




## Bijlagen



### A1. Andere Blockstream App tutorials





- Het Onchain-netwerk gebruiken :



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143



- De Liquid Network gebruiken :



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- Desktop versie :



https://planb.network/tutorials/wallet/desktop/blockstream-app-desktop-c1503adf-1404-4328-b814-aa97fcf0d5da


### A2. Uitgebreide openbare sleutels





- Woordenlijst :
 - [Uitgebreide openbare sleutels](https://planb.network/fr/resources/glossary/extended-key)
 - [xpub](https://planb.network/fr/resources/glossary/xpub)
 - [ypub](https://planb.network/fr/resources/glossary/ypub)
 - [zpub](https://planb.network/fr/resources/glossary/zpub)
- Cursus :
 - [Les clés publiques étendues](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f)




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
 - Voor maximale vertrouwelijkheid verbindt u uw Wallet met uw eigen Bitcoin knooppunt via een Electrum-server in plaats van het openbare knooppunt te gebruiken





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





- Officiële Blockstream links:**
 - [Officiële website](https://blockstream.com/)**
 - [Ondersteuning voor de mobiele toepassing](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/)** : documentatie en chat
 - [GitHub](https://github.com/Blockstream/green_android)**





- Blokverkenners :**
 - Onchain: **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Informatie blokstroom](https://blockstream.info/Liquid)**
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
