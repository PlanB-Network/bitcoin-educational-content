---
name: Umbrel LND
description: Gevorderde tutorial over het installeren en configureren van Lightning Network Daemon (LND) op Umbrel
---
![cover](assets/cover.webp)




## Inleiding



Deze geavanceerde tutorial neemt je stap-voor-stap mee door de installatie, configuratie en het gebruik van de Lightning Node (LND) applicatie op je Umbrel node. Je leert hoe je kanalen opent, je liquiditeit beheert en je node synchroniseert met een mobiele applicatie.



## 1. Voorwaarde: functioneel Bitcoin Umbrel knooppunt



Voordat je Lightning kunt inzetten, moet je een volledig operationeel Bitcoin knooppunt op Umbrel hebben. Hiervoor moet Umbrel geïnstalleerd worden (op Raspberry Pi, NAS of een andere machine) en moet Blockchain Bitcoin volledig gesynchroniseerd worden.



Om Umbrel te installeren en uw Bitcoin node te configureren, raden we u aan onze speciale tutorial te volgen:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Zorg ervoor dat je Bitcoin node up-to-date is en goed werkt, want Lightning Network vertrouwt erop voor alle off-chain transacties.



## 2. Inleiding tot Lightning Network



Lightning Network is een tweede Layer protocol, ontworpen om Bitcoin transacties te versnellen en goedkoper te maken door ze buiten de hoofd-Blockchain om uit te voeren.



Concreet maakt Lightning gebruik van een netwerk van betalingskanalen tussen knooppunten: twee gebruikers openen een kanaal door On-Chain BTC te blokkeren (initiële transactie), en kunnen dan onmiddellijk Exchange betalingen doen binnen dit kanaal. Deze off-chain transacties worden niet geregistreerd op de Blockchain, vandaar hun snelheid en vrijwel geen kosten.



Betalingen kunnen via meerdere kanalen worden gerouteerd (dankzij tussenliggende nodes) om elke ontvanger op het netwerk te bereiken, waardoor een bijna onbeperkte schaal van onmiddellijke transacties mogelijk is. Lightning biedt dus zeer snelle, goedkope transacties, ideaal voor alledaagse betalingen of microtransacties, terwijl het de Blockchain Bitcoin ontlast.



Om te kunnen werken, moet een Lightning-knooppunt permanent verbonden zijn met het netwerk en communiceren met andere Lightning-knooppunten. Er bestaan verschillende software-implementaties (LND, Core Lightning, Eclair, enz.), die allemaal compatibel zijn met elkaar. Umbrel gebruikt LND (Lightning Network Daemon) als onderdeel van zijn officiële Lightning Node toepassing. Deze tutorial richt zich op LND.



Voor een volledige theoretische inleiding tot Lightning Network raden we je aan onze speciale cursus te volgen:



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Deze cursus geeft je een grondige basis in de fundamentele concepten van Lightning Network, voordat je verder gaat met oefenen met je LND node.



## 3. Waarom LND zelf hosten?



Als u uw eigen Lightning-node (LND) op Umbrel beheert, hebt u volledige soevereiniteit over uw fondsen en kanalen, in vergelijking met custodial of semi-custodial oplossingen.



### Vergelijking van bliksemoplossingen :



**Solutions custodiales (ex: Wallet of Satoshi)** :




- Uw Lightning-bitcoins worden beheerd door een vertrouwde derde partij
- Gebruiksvriendelijk, geen technische complexiteit
- De operator bewaart uw geld en kan uw transacties traceren
- Je offert controle en privacy op



**Niet-goederen consumentenportemonnees (bijv. Phoenix, Breez)** :




- Gebruikers behouden hun privésleutels en dus Ownership van hun BTC
- Geen volledig knooppuntbeheer - applicatie beheert kanalen op de achtergrond
- Compromis tussen eenvoud en soevereiniteit
- Afhankelijkheid van leveranciersinfrastructuur voor liquiditeit
- Technische beperkingen (één smartphone kan geen betalingen voor anderen routeren)



**Zelf gehoste LND knoop (Umbrel)** :




- Maximale soevereiniteit: je On-Chain en off-chain BTC's staan volledig onder jouw controle
- Er zijn geen derde partijen betrokken bij het openen van kanalen of het beheren van je betalingen
- Meer privacy (je kanalen en transacties zijn alleen bekend bij jou en je directe peers)
- Gebruiksvrijheid: maak verbinding met je eigen diensten en portemonnees
- Mogelijkheid om transacties voor anderen te routeren (microvergoeding)
- Meer technische verantwoordelijkheden (onderhoud, liquiditeitsbeheer, back-ups)



Kortom, zelf LND hosten geeft u maximale controle, maar vereist meer technische vaardigheden. Het is een afweging tussen gemak en soevereiniteit.



## 4. Stap-voor-stap uitleg



### 4.1 De Lightning Node-toepassing installeren en configureren op Umbrel



Zodra uw Umbrel-knooppunt (Bitcoin) is gesynchroniseerd, volgt u deze stappen :



![Installation de Lightning Node depuis l'App Store Umbrel](assets/fr/01.webp)



Installeer de Lightning Node-toepassing uit de sectie "App Store" van de Interface Umbrel.



![Avertissement sur la nature expérimentale de Lightning](assets/fr/02.webp)



LND (Lightning Network Daemon) wordt op je Umbrel geïnstalleerd als een toepassing. Als je het voor het eerst opent, zie je een waarschuwing dat Lightning een experimentele technologie is.



![Création ou restauration d'un nœud LND](assets/fr/03.webp)



Je kunt kiezen tussen het aanmaken van een nieuw knooppunt of het herstellen van een knooppunt vanaf een back-up/seed. Voor een eerste installatie kies je voor het maken van een nieuw knooppunt. De Lightning Node app zal generate een 24-woorden Mnemonic zin (uw seed Lightning): schrijf het heel zorgvuldig op (idealiter offline, op papier), want het zal worden gebruikt om uw Lightning-middelen te herstellen indien nodig.



**Noot:** Op recente versies van Umbrel levert de installatie van de Lightning app dit 24-woord seed (het Bitcoin Umbrel knooppunt zelf niet).



![Interface principale de Lightning Node](assets/fr/04.webp)



Na initialisatie krijg je toegang tot de hoofd Interface van Lightning Node.



![Paramètres de l'application](assets/fr/05.webp)



In de applicatie-instellingen vind je een aantal belangrijke opties:




   - Raadpleeg je Node ID (de unieke identificatiecode van je knooppunt)
   - Een externe Wallet aansluiten (Wallet aansluiten)
   - Geheime woorden bekijken
   - Toegang tot geavanceerde instellingen
   - Kanalen herstellen
   - Back-upbestand van kanaal downloaden
   - Automatische back-ups inschakelen
   - Back-up via Tor configureren (Backup over Tor)



Deze opties zijn essentieel voor de beveiliging en het beheer van je Lightning-node. Zorg ervoor dat je automatische back-ups activeert en je geheime woorden veilig bewaart.



**Nuttige bronnen:**




- [Umbrel Gemeenschap](https://community.umbrel.com) - Discussieforum voor gebruikers om problemen en oplossingen te delen met betrekking tot Umbrel en haar ecosysteem


> - [Umbrel App Store - Lightning Node (LND)](https://apps.umbrel.com/app/lightning) - Beschrijving van Lightning Node app functies op Umbrel
> - [LND Docs - Quickstart](https://docs.lightning.engineering/lightning-network-tools/LND/run-LND) - Officiële LND documentatie

### 4.2 Een Lightning-kanaal openen



Zodra LND draait, kun je je eerste Lightning-kanaal openen. Om kwaliteitsknooppunten te vinden waarmee je verbinding kunt maken:



![Page d'accueil Amboss.space](assets/fr/06.webp)



[Amboss.space](https://amboss.space/) is een verkenner voor het vinden van betrouwbare knooppunten om kanalen te openen.



![Exemple de nœud ACINQ sur Amboss](assets/fr/07.webp)



Het [ACINQ knooppunt](https://amboss.space/node/03864ef025fde8fb587d989186ce6a4a186895ee44a926bfc370e2c366597a3f8f) is bijvoorbeeld een erkend knooppunt met uitstekende beschikbaarheids- en liquiditeitsstatistieken.



![Informations de connexion Swiss Bitcoin Pay](assets/fr/08.webp)



Voor deze tutorial openen we een kanaal met [Swiss Bitcoin Pay](https://amboss.space/node/03c181e13a09a649c13f60ea3ddbeefc66123c43280da8eebc19f54445f35173ca). De informatie die nodig is voor de verbinding (pubkey@ip:port) wordt gegeven op hun Amboss pagina.



Het kanaal openen :



![Bouton d'ouverture de canal](assets/fr/09.webp)



Klik op de startpagina van de Lightning Node op de knop "+ OPEN CHANNEL



![Configuration du canal](assets/fr/10.webp)



In de kanaalconfiguratiepagina :




   - Plak de knooppunt-ID die is gekopieerd van Amboss (formaat: pubkey@ip:port)
   - Bepaal de hoeveelheid kanaalcapaciteit (sommige knooppunten zoals ACINQ hebben minima, bijv. 400k Sats)
   - Pas indien nodig de kosten voor openingstransacties aan



![Canal en cours d'ouverture](assets/fr/11.webp)



Zodra de transactie is verzonden, verschijnt het kanaal als "geopend" op de startpagina. Wacht op de bevestiging van de On-Chain transactie.



![Détails du canal](assets/fr/12.webp)



Klik op het kanaal om de details te bekijken:




   - Huidige status
   - Totale capaciteit
   - Uitsplitsing van liquiditeit (inkomend/uitgaand)
   - Openbare sleutel van knooppunt op afstand
   - En andere technische informatie



### Lightning Network+ gebruiken om inkomende liquiditeit te verkrijgen



![Lightning Network+ dans l'App Store](assets/fr/13.webp)



Lightning Network+ is beschikbaar in de Umbrel App Store om het verkrijgen van inkomend geld te vergemakkelijken.



![Interface principale de LN+](assets/fr/14.webp)



De belangrijkste Interface biedt drie belangrijke opties:




- "Liquiditeitsswaps: verken de beschikbare swapaanbiedingen
- "Open voor mij": filter de swaps waarvoor je in aanmerking komt
- "Naar Documenten": toegang tot documentatie



![Message d'erreur LN+](assets/fr/15.webp)



Opmerking: Als je nog geen kanaal open hebt staan, krijg je deze foutmelding te zien als je op "Open For Me" klikt.



![Liste des swaps disponibles](assets/fr/16.webp)



De pagina "Liquiditeitsswaps" toont alle swapaanbiedingen die beschikbaar zijn op het netwerk.



![Swaps éligibles](assets/fr/17.webp)



"Open voor mij" filtert alleen de swaps waarvoor je knooppunt aan de vereiste voorwaarden voldoet.



![Détails d'un swap](assets/fr/18.webp)



Voorbeeld van ruilgegevens :




- Pentagon configuratie (5 deelnemers)
- Capaciteit van 300k Sats per kanaal
- Voorwaarde: minimaal 10 open kanalen met 1M Sats totale capaciteit
- Plaatsen beschikbaar: 4/5



### 4.3 Synchronisatie met een mobiele toepassing (Zeus)



Om je Lightning-node op afstand (smartphone) te bedienen, kun je Zeus gebruiken (open-source applicatie beschikbaar op iOS/Android).



**Zeus configuratie met Umbrel :**



![Bouton "Connect Wallet" dans l'interface LND](assets/fr/19.webp)



Zorg ervoor dat je Umbrel-node toegankelijk is (standaard via Tor).


Open de Lightning Node-app in de Interface Umbrel en klik vervolgens op de knop "Connect Wallet", zoals aangegeven door de pijl.



![Page de connexion avec QR code](assets/fr/20.webp)



Er verschijnt een QR code met je LND toegangsgegevens in lndconnect formaat. Deze QR code bevat bijzonder veel informatie, dus aarzel niet om hem te vergroten om het lezen te vergemakkelijken.



![Configuration initiale de Zeus](assets/fr/21.webp)



Op uw telefoon:




   - Open Zeus
   - Klik op de startpagina op "Geavanceerde instellingen" om uw eigen Lightning-knooppunt aan te sluiten
   - Selecteer in de parameters "Een Wallet maken of aansluiten"



![Configuration de la connexion LND dans Zeus](assets/fr/22.webp)



In Zeus:




   - Kies "LND (REST)" als verbindingstype
   - Je kunt de QR-code scannen (aanbevolen methode) of de informatie handmatig invoeren. (Aarzel niet om in te zoomen op de Umbrel QR code, want deze is erg dicht)
   - Belangrijk: activeer de optie "Tor gebruiken" als uw Umbrel alleen toegankelijk is via Tor (de standaardinstelling)
   - Configuratie opslaan



Je Zeus is nu verbonden met je Umbrel-knooppunt en stelt je in staat om Lightning-betalingen te doen, je kanalen, saldi, enz. te bekijken, terwijl je volledig zelf blijft beheren.



**Geavanceerde verbindingsopties:**



Standaard verloopt de Zeus ↔ Umbrel verbinding via Tor. Voor een snellere verbinding zijn er twee alternatieven:



**Lightning Node Connect (LNC)** :




   - Gecodeerd verbindingsmechanisme van Lightning Labs
   - Installeer de Lightning Terminal-app op Umbrel (inclusief LNC-toegang)
   - generate een verbinding QR code in Lightning Terminal (Verbinden → Verbind Zeus via LNC)
   - Scan het in Zeus (kies "LNC" als verbindingstype)



**VPN Tailscale**:




   - Eenvoudig te configureren mesh VPN
   - Installeer Tailscale op Umbrel (App Store) en op je mobiele telefoon
   - Verbind Zeus via Tailscale privé IP in plaats van Tor Address



Deze opties zijn niet verplicht en de Tor + Zeus oplossing werkt in de meeste gevallen goed.



> **Nuttige bronnen:**
> - [Zeus Documentatie - Umbrel Verbinding](https://community.umbrel.com/t/zeus-LN-mobile/7619) - Officiële gids voor het verbinden van Zeus met Umbrel
> - [Zeus GitHub](https://github.com/ZeusLN/zeus) - Zeus open-source project
> - [Umbrel Gemeenschap - Zeus verbinden via Tailscale](https://community.umbrel.com/t/how-to-use-tailscale-with-umbrel/6782) - Gids voor het verbinden van Zeus met Umbrel met behulp van Tailscale

## 5. Veiligheid en best practices



Het beheren van een zelf gehost Lightning knooppunt vereist speciale aandacht voor beveiliging.



### Back-up en beveiliging voor je node



**Essentiële soorten back-ups**



Voor uw Lightning Umbrel knooppunt zijn twee soorten back-ups nodig:



**De seed zin (24 woorden)**




- Vordert On-Chain fondsen
- Nodig om je Wallet Lightning na te maken
- Voor ultraveilige opslag (offline, op papier)



**Static Channel Backup (SCB)** bestand




- Bevat informatie over het Lightning-kanaal
- Maakt geforceerde kanaalsluiting mogelijk in het geval van een crash
- **Belangrijk:** Sla het `channel.db` bestand nooit handmatig op (risico op boetes)



**Handmatige back-upprocedure**



Uw kanalen handmatig opslaan :


1. Ga naar het Lightning Node-menu (drie puntjes "⋮" naast "+ Open Channel")


2. Het back-upbestand van het kanaal downloaden


3. Een nieuwe SCB exporteren na elke kanaalwijziging


4. SCB veilig opslaan (versleutelde media, off-site kopie)



**Umbrel** automatisch back-upsysteem



Umbrel heeft een geavanceerd automatisch back-upsysteem dat ervoor zorgt dat :



*Gegevensbescherming:*




- Encryptie aan clientzijde vóór verzending
- Versturen via het Tor-netwerk
- Gegevens aangevuld met willekeurige vulling
- Encryptiesleutel die uniek is voor uw apparaat



*Verbeterde beveiliging:*




- Directe back-ups bij statuswijzigingen
- Decoy" back-ups op willekeurige intervallen
- Verberg veranderingen in de back-upgrootte
- Bescherming tegen tijdsanalyse



*Restauratieproces:*




- Identificatiecode en sleutel afgeleid van uw seed Umbrel
- Volledige restauratie alleen mogelijk met Mnemonic zinnen
- Automatisch herstel van de laatste back-ups
- Kanaalinstellingen en gegevens herstellen



### Crashherstel



Als je knooppunt verloren is gegaan (hardwarestoring, beschadigde SD-kaart) :




- Paraplu opnieuw installeren
- Voer uw seed van 24 woorden in de Lightning-app in
- Het SCB-bestand importeren tijdens het herstel



LND zal contact opnemen met elke partner van uw oude kanalen om ze te sluiten en uw aandeel in de On-Chain fondsen terug te krijgen. De kanalen worden permanent gesloten (en indien nodig heropend).



### Beschikbaarheid en bescherming tegen fraude



Ideaal is om je knoop zo vaak mogelijk online te laten. Bij langdurige afwezigheid:




- Een kwaadwillende peer kan proberen een oude kanaalstatus uit te zenden
- Bliksem voorziet in een "protestperiode" (ongeveer 2 weken voor LND)
- Als je voor langere tijd weggaat, stel dan een Watchtower in



**Watchtower configuratie:**




- Voeg in de LND geavanceerde instellingen de URL van een vertrouwde Watchtower server toe
- Je kunt een openbare dienst gebruiken of je eigen Watchtower installeren




Om meer te weten te komen over het configureren en gebruiken van uitkijktorens, raden we je aan onze speciale tutorial te bekijken:



https://planb.network/tutorials/node/lightning-network/watch-tower-26937006-dfe5-404e-9ee4-e82e422c5cf2
### Andere best practices





- **Software-updates:** Umbrel en LND up-to-date houden (beveiligingsfixes)
- **Hardwarebescherming:** Gebruik een stabiel systeem (Raspberry Pi met SSD, mini-PC) en een UPS
- **Netwerkbeveiliging:** Behoud de standaard Tor-configuratie, wijzig het Umbrel admin-wachtwoord (standaard: "moneyprintergobrrr")
- **Versleuteling:** Schakel indien mogelijk schijfversleuteling in



## 6. Extra hulpmiddelen



Umbrel's Lightning Node app biedt de essentie voor het beheren van je kanalen, maar tools van derden bieden geavanceerde functionaliteit.



### ThunderHub



Interface modern webgebaseerd Lightning-nodebeheersysteem dat installeerbaar is via de Umbrel App Store.



**Features:**




- Real-time visualisatie van kanalen (capaciteiten, balansen)
- Geïntegreerde herschikkingstools
- Ondersteuning voor MPP (multi-path billing)
- QR code genereren LNURL
- Transactiebeheer On-Chain



ThunderHub is ideaal voor het bewaken van een actief routeringsknooppunt en het uitvoeren van eenvoudige rebalancing.



### Rijd de bliksem (RTL)



Interface webcompatibel met verschillende Lightning-implementaties (LND, Core Lightning, Eclair).



**Highlights:**




- Beheer van meerdere knooppunten
- Contextgevoelige dashboards
- Ondersteuning voor onderzeese swaps (Lightning Loop)
- 2-factor authenticatie
- Back-ups van kanalen exporteren/importeren



RTL is een compleet "Zwitsers zakmes" voor het beheren van een Lightning-node met een meer expertgeoriënteerde aanpak.



### Andere nuttige hulpmiddelen





- **Lightning Shell**: Opdrachtregel (lncli) via browser
- **BTC RPC Verkenner & Mempool**: Controle Blockchain
- **LNmetrics & Torq**: Analyse van routeprestaties
- **Amboss & 1ML**: "Sociaal" beheer van uw knooppunt (aliassen, contacten, netwerkanalyse)



Deze tools kunnen met een paar klikken worden geïnstalleerd via de Umbrel App Store, zonder complexe configuratie.



**Toegevoegde hulpmiddelen:**




- [ThunderHub.io - Functies](https://thunderhub.io) - Overzicht van de functies van ThunderHub
- [Ride The Lightning (RTL) info](https://www.ridethelightning.info/) - RTL-documentatie
- [David Kaspar - Herbalanceren via ThunderHub](https://blog.davidkaspar.com) - Een praktische gids voor herbalanceren
- [Guide "Managing Lightning Nodes"](https://github.com/openoms/lightning-node-management) - Geavanceerde documentatie voor power-users



## Conclusie



Uw eigen LND node op Umbrel draaien is een belangrijke stap in de richting van financiële soevereiniteit. Hoewel het meer technische betrokkenheid vereist dan een custodial oplossing, zijn de voordelen in termen van controle, privacy en actieve deelname aan de Lightning Network aanzienlijk.



Door deze gids te volgen, zou je nu LND moeten kunnen installeren, kanalen openen, je liquiditeit beheren en op afstand toegang krijgen tot je knooppunt. Voel je vrij om geleidelijk geavanceerde functies en aanvullende tools te verkennen naarmate je meer bekend raakt met het ecosysteem.



Vergeet niet dat de veiligheid van je fondsen afhangt van je veiligheidsmaatregelen en praktijken. Neem de tijd om elk aspect te begrijpen voordat je grote bedragen vastlegt.