---
name: SwapMarket
description: Bitcoin en Lightning ruil diensten aggregator
---

![cover](assets/cover.webp)



Het overmaken van geld tussen Bitcoin on-chain en Lightning Network vereist over het algemeen ofwel het handmatig openen van Lightning-kanalen (technisch en duur), of het gebruik van gecentraliseerde swapplatforms met KYC. SwapMarket biedt een alternatief: atomaire swaps zonder vertrouwen via concurrerende aanbieders, zonder KYC.



Innovatie: hoewel aanbieders tussenpersonen zijn, garanderen HTLC (*Hash Time Locked Contracts*) wiskundig dat uw fondsen onder uw controle blijven. De samenvoeging van verschillende aanbieders (Boltz, ZEUS Swaps, Eldamar, Middle Way) creëert prijsconcurrentie. Interface web open-source zelf te hosten.



## Wat is SwapMarket?



SwapMarket, een open-source aggregator die in 2024 werd gelanceerd, functioneert als een vergelijker van Bitcoin/Lightning swapaanbieders. De gebruiker vergelijkt direct de voorwaarden (vergoedingen, liquiditeit, limieten) en selecteert de optimale aanbieder.



### Technische architectuur



**Frontend client-side**: 100% client-side applicatie (fork Boltz Web App) gehost op GitHub Pages. Code draait in browser zonder backend server. Geschiedenis lokaal opgeslagen (cookies/cache). Openbare en controleerbare broncode.



**Provider-ontdekking** : Hardcoded lijst in `src/configs/mainnet.ts`. Nieuwe providers toegevoegd via Pull Request of e-mail.



**Onafhankelijke backends**: Elke aanbieder heeft zijn eigen Boltz backend. De interface bevraagt de API's in realtime om offertes direct te vergelijken.



**HTLC Atomaire swaps**: Hash Time Locked Contracts garanderen atomiciteit: of de swap wordt uitgevoerd, of elke partij krijgt zijn geld terug. Tegenpartijrisico wiskundig geëlimineerd.



### Filosofie



SwapMarket vermindert centralisatie door concurrentie te creëren tussen aanbieders voor vergoedingen en liquiditeit. Geen KYC, open-source self-hostable code, vermenigvuldiging van onafhankelijke operators om single points of failure te voorkomen.



## Belangrijkste kenmerken



### Aanbieder Marktplaats



De interface toont alle actieve aanbieders: naam van de aanbieder, toegepaste kosten (percentage en/of vast), beschikbare minimum/maximumbedragen en ondersteunde swaptypes. De applicatie bevraagt direct de API's van elke aanbieder waarnaar in het configuratiebestand wordt verwezen om in realtime koersen op te halen. Concurrentie tussen aanbieders garandeert optimale tarieven, over het algemeen rond de 0,5% voor standaard swaps.



### Bidirectionele swaps



**Swap-in (on-chain → Lightning)**: on-chain BTC's omzetten in Lightning satoshis. Gebruiksmogelijkheid: een mobiele wallet Lightning van stroom voorzien, binnenkomende capaciteit op een node verkrijgen of onmiddellijke liquiditeit hebben.



**Swap-out (Lightning → on-chain)**: Lightning-satoshis omzetten in on-chain BTC. Use case: een wallet Lightning leegmaken naar koude opslag of liquiditeit tussen lagen opnieuw in evenwicht brengen.



### Veiligheid en herstel



**Trustless atomaire swaps**: HTLC's garanderen dat ofwel de ruil volledig wordt voltooid, ofwel elke partij haar inzet terugkrijgt. Het tegenpartijrisico wordt wiskundig geëlimineerd.



**Betalingsmechanisme**: Elke swap heeft een tijdslot. Als de swap mislukt, wordt het geld na afloop automatisch terugbetaald. De gebruiker behoudt altijd de optie om zijn bitcoins terug te vorderen.



**Herstelsleutels**: Met SwapMarket kunt u herstelsleutels voor lopende swaps exporteren. In het geval van een probleem kunnen deze sleutels worden gebruikt om een swap vanaf elk apparaat af te ronden of te annuleren.



## Installatie en toegang



### Interface web



SwapMarket vereist geen installatie. Toegang is via de browser door naar https://swapmarket.github.io te gaan. Gebruik voor maximale vertrouwelijkheid Brave, Firefox met anti-tracking extensies of LibreWolf. Tor Browser wordt aanbevolen voor netwerkanonimiteit.



Registratie, e-mail of identiteitscontrole zijn niet nodig.



### Zelf hosten (optioneel)



Voor technische gebruikers die niet afhankelijk willen zijn van het officiële GitHub Pages domein, kan SwapMarket lokaal draaien:



**Via npm** :


```
git clone https://github.com/SwapMarket/swapmarket.github.io.git
cd swapmarket.github.io
npm install
npm run dev
```



**Via Docker** :


```
docker run -p 3000:80 ghcr.io/swapmarket/swapmarket:latest
```



De applicatie zal toegankelijk zijn op `http://localhost:3000`. Zelf hosten garandeert totale controle over de interface, elimineert het risico van censuur van het officiële domein en maakt het mogelijk om de broncode te controleren voordat deze wordt uitgevoerd.



### Eerste configuratie



**Wallet Lightning**: Zorg ervoor dat je een operationele wallet Lightning hebt (Phoenix, Zeus, BlueWallet, enz.). Voor inruil krijgt u een generate Lightning-factuur. Voor ruilen betaalt u een Lightning-factuur.



**Wallet on-chain**: Voor swap-ins heb je een wallet Bitcoin on-chain nodig om geld te versturen. Voor swap-outs heb je een Bitcoin ontvangstadres nodig.



**Optionele configuratie**: SwapMarket slaat de ruilgeschiedenis en voorkeuren op in browsercookies. Er hoeft geen account te worden aangemaakt.



## Toegang tot instellingen en Rescue Key



Voordat je je eerste swaps uitvoert, raden we je ten zeerste aan om je **Rescue Key** te downloaden. Met deze noodsleutel kun je je tegoeden terughalen in het geval van een technisch probleem of als je geen toegang meer hebt tot je apparaat.



### Toegangsparameters



Klik op de hoofdpagina van SwapMarket op het tandwielpictogram (⚙️) rechtsboven in de interface, naast het ruilformulier.



![Accès aux paramètres](assets/fr/01.webp)



### Pagina-instellingen



De instellingenpagina wordt geopend en toont verschillende configuratieopties:





- Denominatie**: Keuze uit BTC of sats
- Decimaal scheidingsteken**: Decimaal scheidingsteken (, of .)
- Audio/Browsermeldingen**: Audio- en browsermeldingen
- Herstelsleutel** : De herstelsleutel downloaden
- Logs**: Logboeken bekijken, downloaden of verwijderen



![Page Settings](assets/fr/02.webp)



### Reddingssleutel downloaden



Klik op de knop **Download** naast "Rescue Key".



**Belangrijke punten** :




- De Rescue Key is een **one-stop noodsleutel** die werkt voor al je toekomstige swaps
- Bewaar deze sleutel op een **veilige en permanente** plaats (wachtwoordmanager, digitale kluis)
- In het geval van een wisselprobleem (time-out, technische storing) kun je met deze sleutel je geld terugkrijgen



## Stap voor stap een swap maken



### Omruilen: Bliksem → Bitcoin



Dit eerste voorbeeld laat zien hoe je Lightning-satoshi's omzet in on-chain bitcoins.



**Stap 1: Verwissel configuratie



Selecteer op de hoofdpagina het ruilformulier :




- LIGHTNING** (bovenste veld): Voer het bedrag in dat u in sats Lightning wilt verzenden (voorbeeld: 30.000 sats)
- BITCOIN** (onderste veld): Het bedrag dat je zult ontvangen wordt automatisch weergegeven nadat de kosten zijn afgetrokken (voorbeeld: 29.320 sats)



Plak in het onderste veld je **ontvangstadres Bitcoin** waar je het geld wilt ontvangen. Controleer dit adres zorgvuldig.



De standaard provider is meestal Boltz Exchange. Netwerkkosten en providerprijzen worden duidelijk weergegeven.



![Configuration swap-out](assets/fr/03.webp)



**Stap 2: Aanbiederselectie**



Klik op het dropdownmenu van de aanbieder (standaard: "Boltz Exchange") om alle beschikbare liquiditeitsproviders weer te geven.



Er wordt een modaal venster geopend met een vergelijkingstabel:




- Status**: Green indicator als de provider actief is
- Alias**: Naam aanbieder (Boltz Exchange, Middle Way, Eldamar, ZEUS Swaps)
- Vergoeding**: Kosten toegepast door de provider (over het algemeen tussen 0,49% en 0,5%)
- Max Swap**: Maximumbedrag dat wordt geaccepteerd voor een swap



Vergelijk vergoedingen en maximumbedragen en kies de aanbieder van je keuze.



**Let op**: De provider selectie interface toont niet de **minimumbedragen** voor elke provider. Deze informatie verschijnt alleen in de interface voor het aanmaken van swaps, nadat een provider is geselecteerd. Minimum- en maximumbedragen kunnen per aanbieder verschillen en kunnen na verloop van tijd veranderen. **Controleer deze limieten altijd op het moment van je swap**: als het bedrag dat je wilt ruilen buiten de limieten van een aanbieder valt, kun je een andere aanbieder selecteren die geschikter is voor je transactie.



![Sélection du provider](assets/fr/04.webp)



**Stap 3: Swap aanmaken en Lightning** betalen



Klik op de gele **"CREATE ATOMIC SWAP"** knop. SwapMarket zal generate een **Lightning-factuur** (BOLT11) maken die u kunt betalen vanaf uw wallet Lightning.



De pagina wordt weergegeven:




- Wissel-ID**: Unieke swap-ID (voorbeeld: J4ymFIMVR6Hm)
- Status**: "swap.created" (swap aangemaakt, wacht op betaling)
- QR-code**: Scan deze met uw wallet Lightning
- Invoice Bliksem**: Tekenreeks beginnend met "lnbc" (voorbeeld: lnbc300u1p50whiv...gn5dk2szgqkvfkzc)



Betaal deze factuur vanuit uw wallet Lightning (Phoenix, Zeus, BlueWallet, enz.). Het exacte bedrag dat moet worden betaald, wordt weergegeven (voorbeeld: 30.000 sats).



![Paiement Lightning](assets/fr/05.webp)



**Stap 4: Bevestiging en aanvaarding**



Zodra de Lightning-betaling is bevestigd, ontvangt SwapMarket onmiddellijk uw betaling en zendt de provider de Bitcoin transactie naar uw adres.



De status verandert in **"invoice.settled"** (factuur betaald) en er wordt een bevestigingsbericht weergegeven.



Uw on-chain bitcoins zijn beschikbaar zodra de transactie is bevestigd (meestal een paar minuten tot een paar uur, afhankelijk van de mining kosten die de provider heeft gekozen).



![Confirmation swap-out](assets/fr/06.webp)



U kunt klikken op **"OPEN CLAIM TRANSACTION"** om de Bitcoin transactie te bekijken op een blockchain browser.



### Inruil: Bitcoin → Bliksem



Dit tweede voorbeeld laat zien hoe je on-chain bitcoins omzet in Lightning satoshis.



**Stap 1: Verwissel configuratie



Selecteer op de hoofdpagina het ruilformulier :




- BITCOIN** (bovenste veld): Voer het bedrag in dat je wilt versturen in sats Bitcoin (voorbeeld: 63.400 sats)
- LIGHTNING** (onderste veld): Het bedrag dat je ontvangt wordt automatisch weergegeven na aftrek van kosten (voorbeeld: 62 884 sats)



Plak in het onderste veld een Lightning**-factuur (BOLT11) gegenereerd vanuit uw wallet Lightning, of gebruik uw LNURL-adres als uw wallet dit ondersteunt.



![Configuration swap-in](assets/fr/07.webp)



**Stap 2: Reddingssleutel controleren**



Nadat u op **"CREATE ATOMIC SWAP"** hebt geklikt, verschijnt er een modaal venster waarin u wordt gevraagd uw Rescue Key te verifiëren.



![Modal Rescue Key](assets/fr/08.webp)



**Boltz Reddingssleutel**: Aangezien u uw herstelsleutel al hebt geüpload tijdens de eerste configuratie (zie vorige sectie), klikt u op de knop **"VERIFY EXISTING KEY"** om de opgeslagen sleutel te importeren.



Selecteer het eerder gedownloade Rescue Key-bestand. Na een succesvolle verificatie schakelt de interface automatisch over naar de volgende stap.



**Stap 3: Bitcoin** depotadres



SwapMarket genereert nu een **uniek Bitcoin adres** met het HTLC contract dat gekoppeld is aan uw Lightning-factuur.



De pagina wordt weergegeven:




- Wissel-ID**: Unieke identificatie (voorbeeld: 1kGmB6JyGqU4)
- Status**: "invoice.set" (factuur ingesteld, in afwachting van betaling Bitcoin)
- QR-code**: Bitcoin depotadres
- Bitcoin** adres: Begint meestal met "bc1p..." (voorbeeld: bc1p5mvtwxapjkds...9d4n9f)
- Waarschuwing in geel** : "Zorg ervoor dat je transactie binnen ~24 uur na het aanmaken van deze swap bevestigt!"



Deze periode van ~24 uur is de **timeout** van het HTLC contract. Als uw Bitcoin transactie niet binnen deze periode wordt bevestigd, mislukt de swap en moet u uw Rescue Key gebruiken om uw geld terug te krijgen.



![Adresse de dépôt Bitcoin](assets/fr/09.webp)



Je kunt het adres kopiëren door op de knop **"ADRES"** te klikken, of scan de QR-code rechtstreeks vanaf je wallet on-chain.



**Stap 4: Bitcoins versturen**



Stuur **exact** het aangegeven bedrag (bijv. 63.400 sats) van je wallet Bitcoin on-chain naar het gegenereerde adres.



**Belangrijk**: Gebruik de juiste mining vergoedingen om een snelle bevestiging te garanderen. Als de vergoeding te laag is en de transactie langer dan de timeout (~24h) in de mempool blijft, zal de swap mislukken.



Zodra de transactie is verzonden, detecteert SwapMarket dat deze zich in de mempool bevindt en geeft :




- Status** : "transactie.mempool
- Bericht**: "Transactie is in mempool - Wachten op bevestiging om de swap te voltooien"



![Transaction en mempool](assets/fr/10.webp)



**Stap 5: Bevestiging en Bliksem** ontvangst



Zodra de Bitcoin-transactie de eerste bevestiging ontvangt, betaalt de provider automatisch uw Lightning-factuur. U ontvangt de satoshi's onmiddellijk op uw wallet Lightning.



De status verandert in **"transactie.claim.in behandeling"**, waarna een bevestigingsbericht wordt weergegeven:



![Confirmation swap-in](assets/fr/11.webp)



Je Lightning satoshis zijn onmiddellijk beschikbaar in je wallet.



## Voordelen en beperkingen



### Voordelen



**Tariefconcurrentie**: De samenvoeging van providers creëert een natuurlijke concurrentie die de tarieven naar beneden trekt (0,49% tot 0,5%).



**Vertrouwelijkheid**: Geen KYC, 100% client-side interface (geen overdracht van persoonlijke gegevens), compatibel met Tor Browser.



**Niet-vrijwillig**: HTLC garandeert wiskundig de exclusieve controle over uw fondsen. Of de swap slaagt, of je krijgt je bitcoins terug.



**Open-source self-hostable**: controleerbare openbare code, lokaal inzetbaar voor maximale weerstand tegen censuur.



### Beperkingen



**Beperkte liquiditeit**: Beperkt aantal actieve aanbieders (Boltz, Eldamar, MiddleWay afhankelijk van periode). Maximumbedragen kunnen beperkt zijn.



**Verlooptijd**: Time-out van 24 tot 48 uur. Als on-chain transactie niet bevestigd is voor afloop, is handmatig herstel vereist.



**Interface centralisatie**: Hoewel zelf te hosten, wordt de officiële interface gehost op GitHub Pages. Als GitHub de repo censureert, wordt de toegang via swapmarket.github.io geblokkeerd (oplossing: zelf hosten).



**on-chain Sporen**: HTLC scripts zijn potentieel identificeerbaar door geavanceerde blockchain analyse.



## Beste praktijken



### Beveiligde configuratie



**Download uw Rescue Key**: Download voor uw eerste swap uw Rescue Key via Instellingen (zie de speciale sectie hierboven). Deze unieke sleutel werkt voor al je toekomstige swaps en stelt je in staat om je geld terug te krijgen in het geval van een probleem.



**Gebruik Tor Browser**: Voor maximale vertrouwelijkheid opent u SwapMarket via Tor Browser om uw IP-adres te verbergen.



**Overweeg zelf hosten**: Voor technische gebruikers elimineert het draaien van je eigen SwapMarket instance de afhankelijkheid van het officiële GitHub Pages domein.



### Wisseloptimalisatie



**Let op de mempool**: Controleer mempool.space voor een swap-in. Kies tijden met weinig activiteit om mining kosten te minimaliseren.



**Controleer adressen**: Controleer bij ruilen zorgvuldig je ontvangstadres. Gebruik kopiëren en plakken en controleer de eerste 5 en laatste 5 tekens.



**Test met kleine hoeveelheden**: Begin met het minimaal toegestane (25.000 tot 50.000 sats). Verhoog geleidelijk als je het proces onder de knie hebt.



**Documenteer je swaps**: Noteer de ID, het aflossingsadres en de vervaldatum van elke swap. Deze informatie vergemakkelijkt het traceren en herstellen in het geval van een technisch probleem.



### Gebruiksstrategie



**Breng uw cashflow in balans**: Gebruik SwapMarket om uw verdeling tussen on-chain (sparen, zekerheid op lange termijn) en Lightning (dagelijkse uitgaven, directe betalingen) aan te passen aan uw werkelijke behoeften.



**Bereken de winstgevendheid**: Vergelijk voor permanente liquiditeitsbehoeften van Lightning de cumulatieve kosten van herhaalde swaps versus het rechtstreeks openen van een Lightning-kanaal. SwapMarket blinkt uit voor eenmalige aanpassingen, niet noodzakelijk voor grote regelmatige stromen.



## SwapMarkt vs Boltz: Wat is het verschil?



### Boltz: Technologie versus service



**Boltz is de open-source technologie** (`boltz-backend` op GitHub) die atomaire swaps via HTLC tussen Bitcoin, Lightning en Liquid implementeert.



**Kritisch punt**: Alle aanbieders van SwapMarket (Boltz Exchange, ZEUS Swaps, Eldamar, Middle Way) gebruiken hun eigen versie van de Boltz backend. De onderliggende technologie is daarom identiek. Een kwetsbaarheid in de Boltz backend zou mogelijk invloed hebben op alle aanbieders, maar het open-source karakter van het systeem maakt controle door de gemeenschap mogelijk.



**Boltz Exchange** is een enkele dienst die wordt beheerd door het Boltz-team, terwijl **SwapMarket** verschillende aanbieders samenbrengt die allemaal gebruik maken van de Boltz-technologie, waardoor een concurrerende prijsomgeving ontstaat.



Zie onze Boltz en Zeus Swap tutorials voor meer informatie:



https://planb.academy/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

https://planb.academy/tutorials/exchange/centralized/zeus-swap-b6732907-b5d8-43ea-85e3-9dcd6e6abe47

### Belangrijkste verschillen



| Aspect       | Boltz Exchange       | SwapMarket                           |
| ------------ | -------------------- | ------------------------------------ |
| Aard          | Unieke dienst        | Multi-provider-aggregator            |
| Aanbieders    | Alleen Boltz         | Boltz, ZEUS, Eldamar, Middle Way     |
| Concurrentie  | Vaste tarieven       | Vrije concurrentie                   |
| Interface     | boltz.exchange       | swapmarket.github.io (zelf hostbaar)  |
| Beveiliging   | Non-custodial (HTLC) | Non-custodial (HTLC)                 |

*voordelen van *SwapMarket**: Prijsconcurrentie, diversificatie van backend-instanties, real-time vergelijking.



**Technologische alternatieven** (niet compatibel met SwapMarket): Lightning Loop (Lightning Labs), Muun Wallet, NLoop, Breez Wallet. Deze oplossingen gebruiken hun eigen implementaties van onderzeese swaps.



**Aanbeveling**: Gebruik Boltz Exchange voor eenvoud of SwapMarket om de kosten te optimaliseren door concurrentie. Beide zijn gelijkwaardig in veiligheid (HTLC niet-custodiaal).



## Conclusie



SwapMarket faciliteert Bitcoin/Lightning uitwisselingen door meerdere aanbieders samen te voegen in een enkele interface. De HTLC architectuur garandeert de niet-custodiale aard van swaps, de afwezigheid van KYC beschermt de vertrouwelijkheid en de zelf te hosten open-source code versterkt de weerstand tegen censuur.



Concurrentie tussen aanbieders verbetert tarieven en vermenigvuldigt bronnen van liquiditeit. Om het beheer in twee lagen te optimaliseren (on-chain besparingen, Lightning-kosten), is SwapMarket een praktisch hulpmiddel dat de financiële soevereiniteit en vertrouwelijkheid behoudt.



## Bronnen



### Officiële documentatie




- [SwapMarket - Webtoepassing](https://swapmarket.github.io)
- [GitHub SwapMarket](https://github.com/SwapMarket/swapmarket.github.io)
- [Technische documentatie](https://docs.boltz.exchange/)
- [Gids zelf hosten](https://github.com/SwapMarket/swapmarket.github.io/blob/main/README.md)



### Verwante projecten




- [Boltz Exchange](https://boltz.exchange) - Originele atoomvervangingsdienst
- [ZEUS Swaps](https://zeusln.com) - Leverancier van bliksemswaps