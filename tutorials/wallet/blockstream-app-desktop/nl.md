---
name: Blockstream App - Desktop
description: Hoe gebruik je de Hardware Wallet met Blockstream App op een computer?
---
![cover](assets/cover.webp)



## 1. Inleiding



### 1.1 Lesdoel





- Deze tutorial legt uit hoe je de **Blockstream App** op een computer kunt gebruiken om een Bitcoin **onchain** Wallet met een **Hardware Wallet** te beheren, waardoor veilige transacties mogelijk zijn die op de hoofd-Blockchain Bitcoin zijn geregistreerd.
- Het behandelt de installatie, de initiële configuratie, het aansluiten van een Hardware Wallet en het ontvangen en versturen van onchain bitcoins.
- Opmerking: Andere tutorials in de bijlagen behandelen Liquid, Watch-Only en de mobiele applicatie.



### 1.2 Doelgroep





- **Beginners**: Gebruikers die hun bitcoins willen beheren met veilige desktopsoftware en een Hardware Wallet.
- **Intermediaire gebruikers**: Mensen die willen begrijpen hoe ze een Hardware Wallet moeten gebruiken voor onchain transacties en privacy opties zoals Tor of SPV.



### 1.3. Achtergrond over hardware wallets





- **Hardware Wallet**, **Cold Wallet**: Een fysiek apparaat dat privésleutels offline opslaat en een hoog beveiligingsniveau biedt tegen cyberaanvallen, in tegenstelling tot **Hot wallets** (softwarematige wallets op aangesloten apparaten).
- **Aanbevolen gebruik**:
    - Ideaal om grote bedragen of langetermijnsparen veilig te stellen.
    - Geschikt voor beveiligingsgerichte gebruikers die hun geld willen beschermen tegen de risico's van verbonden apparaten.
- **Beperkingen**: Vereist software zoals Blockstream App om saldi en generate adressen te bekijken en Hardware Wallet ondertekende transacties uit te zenden.



## 2. Introductie van Blockstream App





- **Blockstream App** is een mobiele (iOS, Android) en desktop applicatie voor het beheren van Bitcoin wallets en activa op de Liquid Network. In 2016 overgenomen door Blockstream, heette het *GreenAddress*, werd het omgedoopt tot *Blockstream Green* (2019) en heet het nu *Blockstream app* (2025).
- **Belangrijkste kenmerken**:
- **Onchain** transacties op Blockchain Bitcoin.
    - Transacties op het **Liquid** netwerk (Sidechain voor snelle, vertrouwelijke uitwisselingen).
- **Watch-only** portefeuilles voor het monitoren van fondsen zonder toegang tot sleutels.
    - Privacyopties: verbinding via **Tor**, verbinding met een **persoonlijk knooppunt** via Electrum, of **SPV** verificatie om de afhankelijkheid van knooppunten van derden te verminderen.
    - Functies **Replace-by-fee (RBF)** om onbevestigde transacties te versnellen.
- **Compatibiliteit**: Integreert hardware wallets zoals **Blockstream Jade**.
- **Interface**: Intuïtief voor beginners, met geavanceerde opties voor experts.
- **Opmerking**: Deze handleiding richt zich op het gebruik van onchain met een Hardware Wallet op de desktopversie. Andere tutorials in de bijlagen gaan over het gebruik op mobiele toepassingen, voor onchain, Liquid en Watch-Only functies.



## 3. Blockstream App Desktop installeren en instellen



### 3.1. downloaden





- Ga naar de [officiële website](https://blockstream.com/app/) en klik op "_Download Now_". Download de versie die overeenkomt met je besturingssysteem (Windows, macOS, Linux).
- **Opmerking**: Zorg ervoor dat je downloadt van de officiële bron om frauduleuze software te vermijden.



### 3.2. initiële configuratie





- **Beginscherm**: Wanneer de toepassing voor het eerst wordt geopend, toont het een scherm zonder een geconfigureerde Wallet. Aangemaakt of geïmporteerd portfolio zal hier later verschijnen. Aangemaakte of geïmporteerde portfolio's zullen hier later verschijnen.



![image](assets/fr/02.webp)





- **Instellingen aanpassen**: Klik op het instellingenpictogram linksonder, pas de onderstaande opties aan en verlaat dan de Interface om verder te gaan.



![image](assets/fr/03.webp)



#### 3.2.1. Algemene parameters





- Klik in het menu Instellingen op "**Algemeen**".
- **Functie**: Wijzig de softwaretaal en activeer experimentele functies indien nodig.



![image](assets/fr/04.webp)



#### 3.2.2. Verbinding via Tor





- Klik in het menu Instellingen op "**Netwerk**".
- **Functie**: Routeer netwerkverkeer via **Tor**, een anoniem netwerk dat je verbindingen versleutelt.
- **Waarom?**: Verberg je IP Address en bescherm je privacy, ideaal als je je netwerk niet vertrouwt (openbare Wi-Fi, bijvoorbeeld).
- **Nadeel**: Kan de toepassing vertragen door versleuteling.
- **Aanbeveling**: Activeer Tor als vertrouwelijkheid een prioriteit is, maar test de verbindingssnelheid.



![image](assets/fr/05.webp)



#### 3.2.3. Verbinding maken met een persoonlijk knooppunt





- Klik in het menu Instellingen op "**Aangepaste servers en validatie**".
- **Functie**: Verbindt de applicatie met je eigen **complete Bitcoin node** via een **Electrum server**.
- **Waarom?**: Biedt totale controle over Blockchain gegevens, waardoor u niet langer afhankelijk bent van Blockstream-servers.
- **Vereiste**: Een geconfigureerd Bitcoin knooppunt.
- **Aanbeveling**: Gevorderde gebruikers die maximale soevereiniteit willen.



![image](assets/fr/06.webp)



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

#### 3.2.4. SPV-verificatie





- Klik in het menu Instellingen op "**Aangepaste servers en validatie**".
- **Functie**: Gebruikt **Simplified Payment Verification (SPV)** die block headers downloadt en je transacties verifieert door middel van proof of inclusion (Merkle), zonder de volledige Blockchain op te slaan.
- **Waarom?**: Vermindert de afhankelijkheid van Blockstream's standaard node, terwijl het lichtgewicht blijft voor apparaten.
- **Nadeel**: Minder veilig dan een Full node, omdat het voor sommige informatie afhankelijk is van knooppunten van derden.
- **Aanbeveling**: Activeer SPV als u geen persoonlijk knooppunt kunt gebruiken, maar de voorkeur geeft aan een Full node voor optimale beveiliging.



![image](assets/fr/07.webp)



## 4. Een Hardware Wallet aansluiten op de Blockstream App



### 4.1. Inleidende overwegingen



#### 4.1.1. Voor Ledger gebruikers





- Blockstream Green ondersteunt alleen de **Bitcoin Legacy** toepassing op Ledger apparaten (Nano S, Nano X).
- Stappen die u moet volgen in **Ledger Live** voordat u uw apparaat aansluit:


1. Ga naar **"Instellingen"** → **"Experimentele functies"** en activeer **ontwikkelmodus**.


2. Ga naar **"Mijn Ledger"** → **"App Catalogus"**, installeer dan de **Bitcoin Legacy** toepassing


3. Open de **Bitcoin Legacy**-toepassing op uw Ledger voordat u Blockstream Green opstart om de verbinding tot stand te brengen.




- **Opmerking**: Zorg ervoor dat uw Ledger ontgrendeld is met uw PIN-code en dat de Bitcoin Legacy-toepassing actief is wanneer u verbinding maakt.



#### 4.1.2 Een Hardware Wallet initialiseren





- Als uw Hardware Wallet (Ledger, Trezor of Blockstream Jade) nog nooit is gebruikt (met Blockstream Green of met andere software zoals Ledger Live), moet u deze eerst initialiseren. Deze stap vindt plaats in een veilige omgeving, zonder camera's of waarnemers:


1. **seed zin generatie / Mnemonic zin** (12, 18 of 24 woorden): Schrijf het zorgvuldig op een stuk papier.


2. **seed zinsverificatie**: Test de Wallet invoer van de genoteerde woorden, bijvoorbeeld door de uitgebreide publieke sleutel te verifiëren. Uit te voeren voordat geld naar Wallet wordt gestuurd en de seed frase permanent wordt beveiligd.


3. **De seed-zin beveiligen**: Bewaar de zin op een fysieke drager (papier of metaal) en op een veilige plaats. Sla het nooit digitaal op (geen screenshots, cloud of e-mail).




- **Belangrijk**: De seed zin is uw enige manier om uw fondsen terug te krijgen als het apparaat verloren raakt of defect raakt. Iedereen met toegang kan uw bitcoins stelen.
- **Bronnen** voor back-up en controle van de seed zin :



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

#### 4.1.3. Configuratie voor deze tutorial :





- We gaan ervan uit dat de Hardware Wallet al geïnitialiseerd is met een seed zin en een pincode voor vergrendeling.
- We gaan ervan uit dat de Hardware Wallet nog nooit verbonden is geweest met Blockstream App, waarvoor een nieuw account moet worden aangemaakt. Als de Hardware Wallet al gebruikt is met Blockstream App, zal het account automatisch verschijnen wanneer de applicatie geopend wordt.



### 4.2. Verbinding starten





- Klik in het beginscherm op "**Setup a New Wallet**", bevestig de voorwaarden en klik op "**Get Started**":



![image](assets/fr/08.webp)





- Selecteer de optie "**Op Hardware Wallet**":



![image](assets/fr/09.webp)





- Als je een **Blockstream Jade** gebruikt, klik dan op de bijbehorende knop. Selecteer anders "**Een ander hardwareapparaat aansluiten**":



![image](assets/fr/10.webp)





- Sluit uw Hardware Wallet via USB aan op de computer en selecteer deze in Blockstream App :



![image](assets/fr/22.webp)





- Wacht alstublieft terwijl Blockstream App uw portefeuille-informatie importeert:



![image](assets/fr/23.webp)



### 4.3. Maak een account aan





- Als je Hardware Wallet al gebruikt is met Blockstream App, zal je account automatisch verschijnen in de Interface na het importeren. Maak anders een account aan door op "**Create Account**" te klikken:



![image](assets/fr/24.webp)





- Kies "**Standaard**" om een klassiek Bitcoin portfolio te configureren:



![image](assets/fr/25.webp)





- Zodra je account is aangemaakt, heb je toegang tot je Interface portfolio:



![image](assets/fr/26.webp)





## 5. De onchain Wallet gebruiken met een Hardware Wallet



### 5.1. Bitcoins ontvangen





- Klik in het hoofdscherm van je portfolio op "**Ontvangen**" :



![image](assets/fr/27.webp)





- De applicatie toont een **blanco ontvangst Address**. Het gebruik van een nieuwe Address voor elke ontvangst verbetert je vertrouwelijkheid. Klik op "**Kopieer Address**" om de Address te kopiëren, of laat de verzender de getoonde QR-code scannen:



![image](assets/fr/12.webp)



**Opties** :




- (1) Klik op de pijltjes om generate een nieuwe Address aan je portefeuille te koppelen.
- (2) Om een specifiek bedrag aan te vragen, klik op "**Meer opties**" en dan op "**Aanvragen bedrag**". De QR wordt bijgewerkt en de Address wordt vervangen door een Bitcoin betalings-URI zoals: `Bitcoin:bc1q...?amount=0.00001`



![image](assets/fr/13.webp)





- (3) Om een vorige Address opnieuw te gebruiken, klik op "**Meer opties**" en vervolgens op "**Lijst van adressen**" :



![image](assets/fr/14.webp)





- **Verificatie**: Controleer zorgvuldig het gedeelde Address om fouten of aanvallen te voorkomen (bijv. malware die het klembord wijzigt).
- Zodra de transactie is uitgezonden op het netwerk, verschijnt deze in je Wallet. Wacht 1 tot 6 bevestigingen om de transactie als onveranderbaar te beschouwen.



![image](assets/fr/28.webp)



### 5.2. bitcoins versturen





- Klik in het hoofdscherm van je portfolio op "**Versturen**".



![image](assets/fr/29.webp)





- **Vul gegevens in**:
    - (1) Controleer of het geselecteerde onderdeel **Bitcoin** (onchain) is.
    - (2) Voer de **Address van de ontvanger** in door deze te plakken of een QR-code te scannen met je webcam.
    - (3) Geef het **bedrag** aan dat moet worden verzonden (in BTC, satoshis of andere eenheden).




![image](assets/fr/16.webp)





- Selecteer **transactiekosten** (optioneel) :
 - Kies uit de voorgestelde opties (snel, gemiddeld, langzaam) op basis van urgentie, met een geschatte bevestigingstijd.
 - Voor aangepaste kosten pas je handmatig het aantal satoshi's per vbyte aan. Deze worden weergegeven op het beginscherm. Zie ook [Mempool.space](https://Mempool.space/).



![image](assets/fr/17.webp)





- **Handmatige selectie van UTXO's** (optioneel): Klik op "**Handmatige Coin selectie**" om de specifieke UTXO's te kiezen die in de transactie moeten worden gebruikt.



![image](assets/fr/18.webp)





- **Voorafgaande verificatie**: Controleer de Address, het bedrag en de kosten op het overzichtsscherm en klik dan op "**Transactie bevestigen**". In werkelijkheid wordt de transactie pas vrijgegeven aan het netwerk als je hem hebt ondertekend met je Hardware Wallet, die als enige de geheime sleutels heeft die verbonden zijn met de adressen waarvan UTXO's (satoshis) zullen worden afgeschreven.



![image](assets/fr/19.webp)





- **Laatste controle en ondertekening**: Controleer of alle transactieparameters correct zijn **op uw Hardware Wallet** scherm en onderteken de transactie ermee. Een Address fout kan leiden tot onomkeerbaar verlies van geld.





- **Uitzending**: Eenmaal ondertekend, zendt Blockstream App de transactie automatisch uit op het Bitcoin netwerk.



![image](assets/fr/20.webp)





- **Follow-up**:
 - De transactie verschijnt in het Wallet beginscherm als "in behandeling" totdat deze is bevestigd.
 - Zolang de transactie niet is bevestigd, kan de functie **Replace-by-fee (RBF)** worden gebruikt om de bevestiging te versnellen door de vergoeding te verhogen (zie Appendix).



![image](assets/fr/21.webp)



## Bijlagen



### A1. Andere Blockstream-tutorials





- De Liquid Network gebruiken :



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a



- Importeer en volg een portfolio in "Watch-Only" :



https://planb.network/tutorials/wallet/mobile/blockstream-app-watch-only-66c3bc5a-5fa1-40ef-9998-6d6f7f2810fb



- De Blockstream-app gebruiken op mobiele telefoons (Hot Wallet) :



https://planb.network/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

### A2. Uitleg van Replace-by-fee (RBF)





- **Definitie**: Replace-by-fee (RBF) is een functie van het Bitcoin netwerk waarmee de verzender de bevestiging van een **onchain** transactie kan versnellen door de vergoeding te verhogen.
- **Grenzen**:
    - RBF is niet beschikbaar voor Liquid of Lightning-transacties.
    - De initiële transactie moet gemarkeerd worden als RBF-compatibel, wat Blockstream App automatisch doet.
- Zie voor meer informatie [onze woordenlijst](https://planb.network/resources/glossary/rbf-replacebyfee).



### A3. Beste praktijken





- **Beveilig je herstelzin**:
    - Bewaar je Hardware Wallet's Mnemonic zin op een fysieke drager (papier, metaal) op een veilige plaats.
    - Sla het nooit digitaal op (cloud, e-mail, screenshot).
    - Tutorial : Sla uw Mnemonic zin op:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- **Bescherm uw privacy** :





    - generate een nieuwe Address voor elke ontvangst aan de ketting.
    - Activeer **Tor** of **SPV** om het volgen te beperken.
    - Maak verbinding met je eigen Bitcoin knooppunt via Electrum voor maximale soevereiniteit.
- Controleer altijd de **verzendadressen**:





    - Controleer de Address op je Hardware Wallet scherm voordat je tekent.
    - Gebruik kopiëren/plakken of een QR-code om handmatige fouten te voorkomen.
- **Kosten optimaliseren**:





    - Pas de kosten aan op basis van urgentie en netwerkcongestie (zie [Mempool.space](https://Mempool.space/)).
    - Gebruik Liquid of Lightning voor snelle, goedkope transacties waarvoor geen onchain beveiliging nodig is.
- **Werk de software bij**:





    - Houd uw Blockstream App en Hardware Wallet firmware up-to-date met de nieuwste functies en beveiligingspatches.



### A4. Extra middelen





- **Officiële links**:
    - [Officiële website](https://blockstream.com/)
    - [Ondersteuning voor Blockstream App](https://help.blockstream.com/hc/en-us/categories/900000056183-Blockstream-Green/): documentatie en chat
    - [GitHub](https://github.com/Blockstream/green_qt)





- **Blokverkenners**:
    - Onchain : [Mempool.space](https://Mempool.space/)
    - Liquid : [Informatie over blokstroom] (https://blockstream.info/Liquid)
    - Bliksem : [1ML (Lightning Network)](https://1ml.com/)





- **Uw herstelzin beveiligen:**



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f



- **Liquid Network** :



[Woordenlijst](https://planb.network/fr/resources/glossary/liquid-network)



https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727



- **Lightning Network**:



[Woordenlijst](https://planb.network/fr/resources/glossary/lightning-network)



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb