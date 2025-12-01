---
name: Bisq 2
description: Complete gids voor het gebruik van Bisq 2 en het wisselen van bitcoins P2P
---
![cover](assets/cover.webp)


## Inleiding


KYC-vrije peer-to-peer (P2P) uitwisselingen zijn essentieel voor het behoud van de privacy en financiële autonomie van gebruikers. Ze maken directe transacties tussen individuen mogelijk zonder de noodzaak voor identiteitsverificatie, wat cruciaal is voor diegenen die waarde hechten aan privacy. Voor een meer diepgaand begrip van de theoretische concepten, bekijk de BTC204 cursus:


https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Wat is Bisq 2?


Bisq 2 is de nieuwe versie van de populaire gedecentraliseerde Bisq Exchange, gelanceerd in 2024. In tegenstelling tot zijn voorganger is Bisq 2 ontwikkeld om meerdere Exchange protocollen te ondersteunen, wat gebruikers meer flexibiliteit biedt.


**Belangrijkste nieuwe functies:**




- Ondersteuning voor meerdere privacynetwerken (Tor, I2P)
- Meerdere identiteiten voor meer privacy
- REST API voor handelsbots
- Ondersteuning voor meerdere Wallet types
- Rolsysteem met verplichte storting in BSQ


Deze gids richt zich uitsluitend op "Bisq Easy", het enige momenteel beschikbare protocol. Bisq Easy is speciaal ontworpen voor nieuwe Bitcoin-gebruikers. Dit protocol stelt gebruikers in staat bitcoins te kopen en verkopen tegen fiatvaluta's op een gedecentraliseerd peer-to-peer-platform. Transacties zijn beperkt tot het equivalent van 600 USD (met een minimum van 6 USD), en de veiligheid van de handel is gebaseerd op de reputatie van BTC-verkopers. Bisq Easy heeft geen handelskosten of borgvereisten. Verwacht wordt dat Bisq Easy Bisq 1 zal vervangen voor fiattransacties onder 600 USD (of equivalent).


**Belangrijkste kenmerken:**




- Desktopapplicatie voor meerdere platforms
- Verschillende Exchange protocollen beschikbaar
- Gedecentraliseerd P2P netwerk
- Focus op privacy (geen KYC, gebruik van Tor)
- Non-custodial (je behoudt de controle over je geld)
- Open bron (AGPL)


### Verschillen met Bisq 1


**Voor kopers:**




- Geen borg vereist
- Geen handelskosten
- Geen Mining kosten
- Beveiliging op basis van leveranciersreputatie
- Lagere handelslimieten (gelijk aan USD 600)


**Voor verkopers:**




- Geen borg vereist
- Een reputatie opbouwen
- Mogelijkheid om BSQ te verbranden of BSQ-bindingen te maken
- Potentieel hogere verkooppremie (10-15% boven de markt)


**Belangrijke opmerking:** Zodra het Bisq Multisig protocol is geïmplementeerd in Bisq 2, kan de oude versie van Bisq uitgefaseerd worden. Bisq 1 blijft echter in gebruik als beheertool voor de Bisq CAD en voor BSQ-BTC-uitwisselingen.


### Exchange proces




- De maker van de aanbieding bepaalt de voorwaarden van de Exchange
- Zodra de handelaren het eens zijn over de voorwaarden (betalingsmethode en prijs), begint de Exchange
- De verkoper stuurt zijn bankgegevens naar de koper en de koper stuurt zijn Bitcoin Address naar de verkoper
- De koper doet de betaling in fiatvaluta en stelt de verkoper op de hoogte
- Zodra de betaling is ontvangen, stuurt de verkoper de bitcoins naar de Address van de koper
- De Exchange is voltooid wanneer de koper de bitcoins ontvangt


### Belangrijke regels




- Voordat de betalingsgegevens worden uitgewisseld, kan de Exchange zonder reden worden geannuleerd
- Nadat details zijn uitgewisseld, kan het niet nakomen van verplichtingen leiden tot verbanning
- Gebruik bij bankoverschrijvingen **nooit de termen "Bisq" of "Bitcoin"** in de reden van betaling (dit kan ertoe leiden dat het geld wordt bevroren of zelfs dat de bankrekening van de ontvanger of betaler wordt geblokkeerd)
- Handelaren moeten minstens één keer per dag inloggen om het proces te volgen
- Bij problemen kunnen handelaars een beroep doen op de diensten van een bemiddelaar


## Installatie en configuratie


### 1. Bisq 2 downloaden en controleren


![Téléchargement de Bisq 2](assets/fr/01.webp)




- Ga naar [bisq.network](https://bisq.network/downloads/)
- Download de Bisq 2-versie die overeenkomt met uw besturingssysteem (scroll naar beneden op de pagina)
- Controleer de authenticiteit van het gedownloade bestand (sterk aanbevolen). Voor een gedetailleerde handleiding voor het verifiëren van handtekeningen, zie de volgende tutorial:


https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

### 2. Installatie volgens uw systeem


Volg de installatiestappen die geschikt zijn voor uw besturingssysteem. Als u problemen ondervindt tijdens de installatie, kunt u de gedetailleerde handleiding raadplegen op de [officiële Bisq wiki] (https://bisq.wiki/Downloading_and_installing).


### 3. Eerste opstart




- Start Bisq 2 en accepteer de gebruiksvoorwaarden


![Conditions d'utilisation](assets/fr/01.webp)




- Maak een nieuw profiel aan door een naam en avatar te kiezen


![Création du profil](assets/fr/02.webp)




- Vervolgens wordt u naar het hoofddashboard van de applicatie gebracht, waar u Bisq Easy kunt starten om uw eerste bitcoins te kopen of te verkopen


![Page d'accueil de Bisq 2](assets/fr/03.webp)


### 4. Betaalmethoden instellen




- Ga naar het gedeelte Betaalrekeningen in het hoofdmenu


![Liste des comptes de paiement](assets/fr/04.webp)




- Voeg een nieuwe betaalmethode toe door de vereiste informatie in te vullen


![Création d'un nouveau compte de paiement](assets/fr/05.webp)


Het vooraf configureren van betaalmethoden is optioneel, maar wordt aanbevolen om tijd te besparen tijdens het handelen. U kunt uw betaalmethoden ook direct tijdens een transactie configureren door contact op te nemen met uw Exchange partner.


### 5. Accountbeveiliging


**Data back-up:**


In tegenstelling tot Bisq 1 is er in Bisq 2 momenteel geen Bitcoin Wallet geïntegreerd: transacties worden dus uitgevoerd via uw eigen externe portemonnees. Desondanks raden we u aan regelmatig een back-up te maken van uw Bisq 2-gegevensmap. Raadpleeg de [officiële Bisq wiki] (https://bisq.wiki/Backing_up_application_data#Back_up_the_entire_Bisq_data_directory) om uw gegevensmap te vinden.


**Identiteitsbeheer:**


Met Bisq 2 kunt u meerdere identiteiten aanmaken. Elke identiteit kan worden gebruikt voor verschillende soorten transacties. Uw identiteiten worden opgeslagen in de gegevensmap.


## Bitcoins kopen en verkopen


### Hoe Bitcoins kopen


**Optie 1: Profiteer van een bestaande aanbieding**




- Selecteer in het hoofdscherm "Bisq Easy", tabblad "Aan de slag" en klik vervolgens op "Start handelsassistent"


![Lancer trade wizard](assets/fr/06.webp)




- Kies "Bitcoin kopen" en selecteer je valuta


![Sélection achat Bitcoin](assets/fr/07.webp)


![Choix de la devise](assets/fr/08.webp)




- Stel de betalingsmethode van je voorkeur in (SEPA, Revolut, enz.)


![Configuration méthodes de paiement](assets/fr/09.webp)




- Op dit punt heb je ofwel een lijst met aanbiedingen die overeenkomen met je vorige criteria, of je moet naar het "Offerteboek" gaan


![Liste des offres](assets/fr/10.webp)




- In het tweede geval kun je aanbiedingen weergeven en filteren met de knoppen rechtsboven op de Interface


![Filtres des offres](assets/fr/11.webp)




- Zodra je je aanbieding hebt gekozen, hoef je alleen nog maar je betaalmethode te kiezen en het transactieoverzicht te valideren


![Choix modalités de paiement](assets/fr/12.webp)


![Configuration du trade](assets/fr/13.webp)


![Récapitulatif du trade](assets/fr/14.webp)


**Optie 2: Maak je eigen aanbieding**




- Selecteer "Bisq Easy" en vervolgens "Offerteboek"
- Kies je handelspaar (bijv. BTC/EUR)
- Klik op "Offerte maken
- Volg de wizard voor het maken van een aanbieding: Definieer het bedrag (vast of bereik)


![Configuration du montant](assets/fr/20.webp)




- Selecteer geaccepteerde betalingsmethoden


![Sélection méthodes de paiement](assets/fr/21.webp)




  - Controleer de samenvatting en publiceer de aanbieding


![Récapitulatif et publication](assets/fr/22.webp)


Zodra de Exchange is opgestart:




- Stuur je Bitcoin Address of Lightning Invoice naar de verkoper


![Envoi adresse Bitcoin](assets/fr/15.webp)




- De bankgegevens van de verkoper ontvangen


![Réception coordonnées bancaires](assets/fr/16.webp)


![Détails coordonnées bancaires](assets/fr/17.webp)




- Voer de betaling uit (zonder "Bisq" of "Bitcoin" te vermelden)
- Stel de verkoper op de hoogte van je betaling


![Notification paiement](assets/fr/18.webp)




- Wacht tot de bitcoins arriveren


![Attente réception](assets/fr/19.webp)


### Hoe verkoop je Bitcoins?


Het verkoopproces op Bisq 2 volgt dezelfde logica als dat van kopen, met dezelfde hoofdstappen maar in omgekeerde volgorde. U kunt uw eigen verkoopbod maken of reageren op een bestaand koopbod. Hier volgt een overzicht van de verschillende opties en stappen in het proces:


**Optie 1: Maak een verkoopaanbod**




- Selecteer "Bisq Easy" en vervolgens "Offerteboek"
- Klik op "Maak aanbieding" en kies "Bitcoin verkopen"
- Configureer je aanbieding :
 - Selecteer valuta (EUR, USD, enz.)
 - Kies de geaccepteerde betaalmethoden
 - Stel het bedrag in (tussen 6 en 600 USD)
 - Bepaal je prijs (vast of % van de markt)
- Details controleren en het aanbod publiceren


**Optie 2: Neem een bestaand aanbod**




- Blader door aanbiedingen op het tabblad "Aanbiedingenboek
- Filter op valuta en betaalmethode
- Selecteer een aanbieding die bij je past
- Details controleren en het aanbod accepteren


**Verkoopproces:**


Zodra de Exchange is opgestart:




   - Stuur je bankgegevens naar de koper
   - Wacht op Bitcoin Address van de koper
   - Controleer of de Address geldig is


Na kennisgeving van betaling :




   - Controleer of de betaling op je account is ontvangen
   - Controleer of het bedrag en de details overeenkomen
   - Bitcoins verzenden naar de Address
   - Markeer de transactie als voltooid


Afronding :




   - Wacht op bevestiging van de koper
   - Laat feedback achter over de transactie
   - Bouw je reputatie op voor toekomstige verkopen


**Belangrijke opmerking:** Als verkoper moet je bijzonder alert zijn op het risico van terugboekingen. Geef de voorkeur aan veilige betalingsmethoden en controleer altijd of de betaling is ontvangen voordat je bitcoins verzendt.


## Goede praktijken en veiligheid


### Veiligheidstips


**Voor kopers:**




- Begin met kleine hoeveelheden
- Controleer de reputatie van verkopers (minimale score van 30.000)
- Gebruik alleen de voorgestelde betalingsmethoden
- Controleer of de verkoper actief is voordat je de betaling verstuurt
- Gebruik alleen de bankgegevens in de Exchange chat
- Communiceer nooit buiten het Bisq 2-platform
- Bewaar het betalingsbewijs
- Stuur nooit gevoelige informatie


**Voor verkopers:**




- Wees voorzichtig met nieuwe accounts
- Vermijd betaalmethoden die gevoelig zijn voor terugboekingen (PayPal, Venmo)
- Controleer of de accountgegevens overeenkomen met de koper
- Beperk communicatie tot chat Bisq 2
- Open een bemiddeling in geval van twijfel


### Reputatie opbouwen (voor verkopers)


Om je reputatie als verkoper op Bisq te verbeteren, moet je regelmatig transacties uitvoeren en professioneel communiceren met kopers. Reageer snel op verzoeken van kopers voor een positieve ervaring. Je kunt ook een BSQ-bond aanmaken om je Commitment aan het platform te laten zien. Deze acties zullen vertrouwen opbouwen en meer kopers aantrekken.


### Geschillenbeslechting




- Neem contact op met je tegenhanger via chat
- Open indien nodig een geschil
- Alle gevraagde bewijzen leveren
- Volg de instructies van de bemiddelaar


### Privacybeleid :




- Geen registratie of gecentraliseerde identiteitsverificatie vereist
- Alle verbindingen gaan via het Tor-netwerk (en binnenkort I2P)
- Geen centrale server om gegevens op te slaan
- Transactiegegevens zijn alleen leesbaar voor de betrokken partijen


### Bescherming tegen censuur :




- Volledig gedistribueerd P2P netwerk
- Het Tor-netwerk (en binnenkort I2P) gebruiken om censuur te weerstaan
- Open source project beheerd door een DAO, zonder gecentraliseerde juridische entiteit


## Voor- en nadelen


### Voordelen van Bisq 2




- **Maximale privacy**: Geen KYC, gebruik van Tor
- **Decentralisatie**: Geen centrale server
- **Beveiliging**: Open source, niet-custodiale code
- **Intuïtieve Interface**: eenvoudiger dan Bisq 1
- **Flexibiliteit**: Meerdere Exchange protocollen


### Bisq 2 nadelen




- **Beperkte liquiditeit** (op dit moment) :
 - Nieuw protocol in opstartfase
 - Weinig verkoopaanbiedingen beschikbaar
 - Potentieel lange wachttijden om een koper te vinden
- **Handelslimieten**: Maximaal USD 600 per transactie (met Bisq easy)
- **Alleen desktop**: Geen mobiele applicatie


## Toekomstige protocollen


Hoewel Bisq Easy momenteel het enige beschikbare protocol is, zijn er verschillende andere protocollen in ontwikkeling voor Bisq 2 :




- **Bisq Lightning**: Exchange protocol gebaseerd op een borgsysteem dat gebruik maakt van meerpartijenrekencryptografie op de Lightning Network.
- **Bisq MuSig**: Migratie van het hoofdprotocol van Bisq 1 naar Bisq 2, met behulp van een 2-op-2 Multisig met veiligheidsdeposito's.
- **BSQ Swaps**: Directe atomaire swaps tussen BSQ en BTC.
- **Liquid Swaps**: Exchange van activa op Liquid Network (USDT, BTC-L) via atomaire swaps.
- **Monero Swaps**: Atomaire uitwisselingen tussen Bitcoin en Monero.
- **Liquid MuSig**: Versie van het Multisig protocol met L-BTC voor lagere kosten en meer privacy.
- **Submarine Swaps**: Uitwisseling tussen Bitcoin op de Lightning Network en Bitcoin On-Chain.
- **Stablecoin Swaps**: Atomische uitwisselingen tussen Bitcoin en USD stablecoins.
- **Multisig Opties**: Creatie van P2P put- en callopties met BTC-blokkering in een On-Chain Multisig transactie.
- **Multisig Open Contracten**: Maakt het mogelijk om aangepaste voorwaardelijke contracten te maken met behulp van een 2-op-3 Multisig systeem met arbitrage.


Deze protocollen zijn momenteel in ontwikkeling en zullen geleidelijk worden geïntegreerd in Bisq 2, waardoor gebruikers meer flexibiliteit krijgen naargelang hun specifieke behoeften.


## Handige bronnen




- Officiële website: [bisq.network](https://bisq.network)
- Documentatie: [Bisq Wiki](https://bisq.wiki)
- Ondersteuning: [Forum Bisq](https://bisq.community)
- Broncode : [GitHub](https://github.com/bisq-network)