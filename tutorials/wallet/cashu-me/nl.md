---
name: Cashu.me
description: Cashu.me gids voor het gebruik van ecash
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=LIPw1c74LBU)


*Hier is een video tutorial van BTC Sessions, een video gids die je begeleidt bij het opzetten en gebruiken van de Cashu.me Bitcoin Wallet, die je toegang geeft tot eenvoudige, goedkope en private Bitcoin transacties - zonder dat je een app store nodig hebt!


In deze tutorial verkennen we Cashu.me, een browsergebaseerde Wallet voor private Bitcoin betalingen met Chaumian ecash. Voordat we beginnen, eerst een korte introductie van ecash en hoe het werkt.


## Inleiding tot ecash


Stel je voor dat je digitaal geld hebt dat precies zo werkt als fysieke biljetten in je zak - privé, direct en peer-to-peer bruikbaar zonder tussenpersonen. Dat is wat ecash mogelijk maakt: een digitale betaalmethode die de privacy van fysiek geld terugbrengt in de digitale wereld. In tegenstelling tot onchain-Bitcoin, dat elke transactie vastlegt op een openbare Ledger die voor iedereen zichtbaar is, creëert ecash privé-tokens die echte Bitcoin waarde vertegenwoordigen terwijl uw uitgavengedrag vertrouwelijk blijft.


Denk aan ecash als digitale instrumenten aan toonder die op je apparaat zijn opgeslagen - als je ze in je bezit hebt, bezit je ze, net als fysiek geld. Deze tokens worden uitgegeven door vertrouwde diensten genaamd `Mints` die de onderliggende Bitcoin reserves aanhouden. Als je ecash gebruikt, zend je je transacties niet uit naar het hele netwerk. In plaats daarvan wissel je privétokens direct uit met anderen, waardoor je een betaalervaring creëert die meer aanvoelt alsof je iemand contant geld overhandigt dan wanneer je een traditionele digitale betaling doet.


Cashu is een vrij en open-source Chaumian ecash protocol gebouwd voor Bitcoin. De technologie bouwt voort op het baanbrekende cryptografische onderzoek van David Chaum uit de jaren '80, waarbij `blinde handtekeningen` worden gebruikt om privacy te garanderen. Wanneer je ecash tokens ontvangt, ondertekent de munt ze zonder te weten waar ze vervolgens zullen worden uitgegeven - een cruciale functie die het traceren van transacties voorkomt. Belangrijk is dat ecash Bitcoin niet vervangt, maar aanvult door enkele kritieke problemen aan te pakken die komen kijken bij de vereisten van de Bitcoin architectuur. Het biedt de privacy die fysiek geld biedt (wat Bitcoin's transparante Ledger ontbeert) en maakt directe microtransacties mogelijk zonder Blockchain kosten of vertragingen in de bevestiging.


Ecash integreert naadloos met de Lightning Network. Je gebruikt Lightning om Bitcoin te storten in een munt (waarbij je Bitcoin waarde wordt omgezet in ecash tokens) en om deze later weer op te nemen (waarbij de tokens weer worden omgezet in besteedbaar Lightning saldo). Samen vormen ze een krachtige combinatie: Bitcoin biedt de veilige afwikkeling Layer, Lightning maakt snelle transacties en netwerkinteroperabiliteit mogelijk en ecash voegt de privacy Layer toe waardoor digitale betalingen weer echt privé aanvoelen.


## Cashu.me


Cashu.me is een `Progressive Web App (PWA)` die het Cashu protocol implementeert - een specifieke implementatie van Chaumian ecash ontworpen voor Bitcoin. Als PWA werkt het direct in je browser zonder installatie in app stores, maar je kunt het wel `installeren` op je apparaat voor eenvoudigere toegang. Deze webgebaseerde aanpak zorgt voor brede compatibiliteit tussen besturingssystemen, terwijl de veiligheid wordt behouden door cryptografische protocollen in plaats van platformbeperkingen.


## belangrijkste kenmerken


Laten we eens duiken in de functies en ontdekken wat Cashu.me te bieden heeft:



- Chaumian ecash op Lightning**: Gebruikt blinde handtekeningen zodat munten gebruikerssaldi of transactiegeschiedenis niet kunnen achterhalen
- Zelfbeheer van tokens**: Je beheert ecash tokens lokaal met je seed zin
- seed zin back-ups**: 12-woord herstelzin voor Wallet herstel
- Onafhankelijkheid van muntsystemen**: Werkt met meerdere onafhankelijke muntsoorten-je bent niet gebonden aan één aanbieder
- Directe, gratis transacties**: Binnen dezelfde munt worden betalingen binnen enkele seconden afgerond zonder kosten
- Privacybehoudende architectuur**: Munten kunnen niet zien wie transacties doet met wie
- Offline ecash**: Munten verzenden/ontvangen via een lokaal transmissieprotocol, zoals NFC, QR-code, Bluetooth, enz. zonder internetverbinding
- Ontdek ecash-munten via Nostr**: Vind en verifieer betrouwbare munten via het Nostr-protocol
- Wissel ecash tussen munten**: Alle munten spreken Lightning, wat betekent dat je waarde tussen hen kunt overdragen.
- Bedien je Wallet op afstand met Nostr Wallet Connect (NWC)**: Maak verbinding met andere apps zoals Nostr Client en begin te zappen via NWC


De kritieke afweging is `trust`: terwijl je de controle hebt over de tokens zelf, moet je munten vertrouwen om de onderliggende Bitcoin reserves te bewaren. Zoals de documentatie van Cashu stelt:


> ...de Munt beheert de Lightning-infrastructuur en bewaart de satoshi's voor de gebruikers van de Munt ecash. Gebruikers moeten de munt vertrouwen om hun ecash te Redeem zodra ze willen overstappen op Lightning.

- Cashu Documentatie, [Algemene veiligheids- en privacyvragen] (https://docs.cashu.space/faq#general-safety-and-privacy-questions)


Dit maakt ecash een bewaaroplossing voor de Bitcoin zelf, hoewel u de volledige controle over de tokens behoudt.


## 1️⃣ Eerste installatie


① Begin met het bezoeken van [Wallet.cashu.me](https://Wallet.cashu.me) in je browser. Omdat Cashu.me een `PWA` is, hoef je het niet te downloaden van app stores, maar open je de site rechtstreeks in je browser. Je kunt de site ook installeren op het startscherm van je apparaat, zodat je er makkelijker bij kunt.


② Om de PWA te installeren, tik je op de ⋮ menuknop in je browser en selecteer je `Toevoegen aan beginscherm`. Sluit na de installatie de browsertab en start Cashu.me vanaf het beginscherm van je toestel. Tik op het welkomstscherm op `Volgende` om verder te gaan.


beveiliging is cruciaal. Sla uw seed zin veilig op in een wachtwoordmanager of, nog beter, schrijf hem op papier. Deze 12-woorden herstelzin is de enige manier om geld terug te krijgen als u de toegang tot dit apparaat verliest. Tik op het 👁️ icoon om uw seed zin te onthullen, schrijf zorgvuldig alle 12 woorden in volgorde op en vink dan het vakje `Ik heb het opgeschreven` aan. Tik op `Volgende` om verder te gaan en vink het vakje aan om te bevestigen dat u de `voorwaarden` op het volgende scherm accepteert.


![image](assets/en/01.webp)


Na het voltooien van de installatie moet je verbinding maken met een `Mint`. Tik op `ADD MINT` gevolgd door `DISCOVER MINTS` om mints te bekijken die worden aanbevolen door de Nostr-community. Voor extra verificatie kunt u muntbeoordelingen bekijken op [bitcoinmints.com](bitcoinmints.com).


Tik vervolgens op `Klik om door mints te bladeren` om de volledige lijst te zien. Selecteer een munt door de URL te kopiëren, in het URL-veld te plakken en een herkenbare naam te geven. Voor dit voorbeeld gebruiken we:


URL: `https://mint.minibits.cash/Bitcoin`

Naam: minibits


![image](assets/en/02.webp)


Tik op `ADD MINT` om het proces te voltooien. Controleer in het bevestigingsscherm of je de operator van deze munt vertrouwt en tik dan opnieuw op `ADD MINT`. De Minibits mint verschijnt nu op je startscherm. Zodra je Wallet is ingesteld, moet je er geld op storten voordat je transacties kunt doen.


![image](assets/en/03.webp)


## 2️⃣ Uw Wallet financieren


Cashu.me biedt twee verschillende methoden om je Wallet te financieren. Wanneer je op `Ontvangen` op het beginscherm tikt, zie je opties om geld te ontvangen via `ECASH` of via `LIGHTNING.` Laten we beide opties bekijken.


![image](assets/en/04.webp)


### Financiering via LIGHTNING


De eerste optie is om de Wallet via Lightning Invoice te financieren. selecteer een munt als je verschillende munten hebt toegevoegd en bepaal het `bedrag (Sats)` dat je wilt ontvangen. Tik dan op `CREËER Invoice.` Nu krijg je een QR-code te zien die je kunt scannen met een andere Lightning Wallet of je kunt gewoon de Invoice `kopiëren` en in een andere Wallet plakken om je cashu.me Wallet te betalen en te financieren.


![image](assets/en/05.webp)


### E-cash ontvangen


Met de ecash-methode kunt u tokens rechtstreeks van een andere ecash Wallet ontvangen. Begin met het aantikken van de knop `Ontvangen` en selecteer de optie `ECASH`. Je kunt een Cashu token van een andere Wallet plakken, scannen of `NFC` gebruiken. Als je voor plakken kiest, voer dan de token string in die je van een andere Wallet hebt gekopieerd, het `bedrag` en de `munt` worden automatisch getoond. Tik op `RECEIVE` om de transactie te voltooien, en de Sats verschijnt in jouw Wallet. Merk op dat je saldo nu verdeeld is over meerdere munten. Je hebt bijvoorbeeld 1.000 Sats in je Minibits `Mint` en nog eens 1.000 Sats in een Coinos `Mint`. Deze verdeling over verschillende munten is een belangrijk aspect van Cashu's architectuur.


![image](assets/en/06.webp)


### Wisselen tussen pepermuntjes


Als je een bepaalde munt die je hebt toegevoegd niet meer vertrouwt, biedt cashu.me een functie om `geld te ruilen` van de ene munt naar de andere. Navigeer naar de mints tab en scroll naar beneden totdat je `Multimint Swaps` ziet. Selecteer de munt `VAN` en `Tot` in de vervolgkeuzemenu's en voer het bedrag in dat je wilt overmaken. Tik op `SWAP` om de munten tussen munten te verplaatsen. Dit wordt uitgevoerd via een Lightning-transactie, dus je moet ruimte overlaten voor mogelijke Lightning-kosten. In mijn voorbeeld was 1 zat voldoende.


![image](assets/en/07.webp)


## 3️⃣ Geld versturen


Om Sats te versturen, biedt Cashu.me twee opties. Om te versturen via `ecash` of via `lightning`. Laten we beide opties eens bekijken.


### Verzenden via Lightning


Volg deze stappen om via Lightning te verzenden:


1. Tik op `Verstuur` in het Beginscherm en selecteer `Bliksem`

2. De app vraagt je om een `Lightning Invoice` of `-Address` in te voeren. Je kunt de Invoice/Address direct plakken, of de scan QR code optie gebruiken om het visueel vast te leggen, bevestig dan met `ENTER`

3. Selecteer de Mint waarvan je wilt betalen met behulp van het dropdown veld en tik op `PAY` om te bevestigen. **Note**: er is ook een optie om `Multinut` te gebruiken onder `Instellingen` -> `Experimenteel` waarmee je facturen van meerdere mints tegelijk kunt betalen.

4. Na succesvolle afronding zie je een betalingsbevestiging en het bedrag dat van je saldo is afgetrokken.


![image](assets/en/08.webp)


### Verzenden via ecash


Het versturen van ecash is net zo eenvoudig.


1. Tik op `Verstuur` en selecteer deze keer de optie `ECASH`.

2. `Selecteer een munt` en voer het `bedrag` in dat je wilt versturen in Sats en tik op `Verstuur` om te bevestigen

3. Dit creëert een `Animated QR Code` die je kunt aanpassen door de Snelheid en Grootte parameters aan te passen. Iedereen kan deze QR Code scannen om de Sats direct te Redeemen, of je kunt op COPY tikken om de token string naar iemand anders te sturen via alternatieve kanalen zoals Bluetooth, NFC of standaard berichten.

4. Ik open een andere Wallet. Plak van het klembord en selecteer `Kasgeld ontvangen` in de andere Wallet.


![image](assets/en/09.webp)


## 4️⃣ Extra functies


Naast de kernfunctionaliteit voor verzenden en ontvangen, biedt Cashu.me krachtige extra functies die uw Bitcoin ervaring binnen het Nostr ecosysteem verbeteren.


### Nostr Wallet aansluiten


Nostr Wallet Connect (`NWC`) verandert de manier waarop u met Nostr-toepassingen communiceert door een naadloze verbinding tussen uw Wallet en sociale apps te creëren. Met dit protocol kunnen toepassingen zoals [Damus](https://damus.io/) of [Primal](https://primal.net/home) direct betalingen aanvragen via Nostr relais, zonder dat je de app hoeft te verlaten.


Om `NWC` in Cashu.me in te stellen:


1. Ga naar `Instellingen` linksboven in het hamburgermenu

2. Ga naar het gedeelte `NOSTR Wallet CONNECT` en tik op de knop `Enable`

3. Vervolgens stel je een toelage in om het maximale bedrag vast te stellen dat applicaties van je Wallet kunnen uitgeven.

4. Eenmaal geconfigureerd kun je de verbindingsstring kopiëren en plakken in elke Nostr-client die `NWC` ondersteunt, waardoor je direct kunt zappen en tippen.


![image](assets/en/10.webp)


### Bliksem Address via npub.nl


Cashu.me integreert met [npub.cash](https://npub.cash/) om je een Lightning Address aan te bieden die naadloos samenwerkt met het Nostr-protocol. Hier kun je je aanmelden en je gebruikersnaam claimen door je Nostr `nsec` te geven, die 5.000 Sats kost en het npub.cash project ondersteunt, of je kunt een willekeurige Nostr publieke sleutel (`npub`) gebruiken zonder registratie.


Ga eerst naar `Instellingen` en tik op `Inschakelen` Bliksem Address met npub.cash. Dit zal generate een npub.cash Address met behulp van een `npub` string afgeleid van uw Wallet seed zinsdeel standaard.


Je kunt ook naar [deze webpagina](https://npub.cash/username) gaan om een aangepaste gebruikersnaam te claimen met je eigen Nostr `nsec`, waardoor je een gepersonaliseerde Lightning Address krijgt zoals username@npub.cash.


![image](assets/en/11.webp)


## conclusie


Cashu.me levert privé Bitcoin betalingen die functioneren als fysiek geld - direct en peer-to-peer zonder je transactiegeschiedenis bloot te geven. Persoonlijk waardeer ik de PWA architectuur omdat het vrij werkt van app store beperkingen. Door de veiligheid van Bitcoin, de snelheid van Lightning en de privacy van ecash te combineren, biedt Wallet gebruiksmogelijkheden die het dagelijkse gebruik van Bitcoin kunnen verbeteren.


Hoewel u volledige controle hebt over uw ecash tokens via zelfbewaarneming, moet u niet vergeten dat munten fungeren als vertrouwde derde partijen die de onderliggende Bitcoin reserves bezitten. De mogelijkheid om meerdere munten te gebruiken en tussen hen te wisselen biedt flexibiliteit met behoud van privacy.


Dankzij functies als NWC en npub.cash adressen is Cashu.me een aantrekkelijke Wallet optie voor sociale klanten die privacy en soevereiniteit belangrijker vinden dan de beperkingen van het grote technologiebeleid.


## hulpbronnen


[https://github.com/cashubtc/cashu.me](https://github.com/cashubtc/cashu.me)


[https://github.com/cashubtc](https://github.com/cashubtc)


[https://github.com/cashubtc/awesome-cashu](https://github.com/cashubtc/awesome-cashu)


[https://cashu.space/](https://cashu.space/)