---
name: Zeus Embedded - Geavanceerd
description: Multi-node zelfbewaarde Lightning-portemonnee
---

![Zeus](assets/cover.webp)


## Inleiding tot ZEUS Wallet


ZEUS is een mobiele Bitcoin Wallet en node management app met alle functionaliteiten van een Bitcoin Lightning Wallet die Bitcoin betalingen eenvoudig maakt, gebruikers volledige controle geeft over hun financiën en meer gevorderde gebruikers in staat stelt hun Lightning nodes te beheren vanuit de palm van hun hand.


### Voor wie is ZEUS?

Momenteel is ZEUS bedoeld voor mensen die hun eigen [Lightning Network Daemon (LND)](https://lightning.engineering/) of [Core Lightning (CLN)](https://blockstream.com/lightning/) thuis- / bedrijfsnodes draaien en deze op afstand beheren via Zeus.


Handelaars die [BTCPay](https://btcpayserver.org/), [LNBits](https://lnbits.com/) of [Alby](https://getalby.com/) (of een andere LNDhub-account) gebruiken, kunnen ook via ZEUS verbinding maken met, gebruiken en hun knooppunten / accounts beheren.


[Vanaf v0.8](https://blog.zeusln.com/zeus-v0-8-0-open-beta/) zal ZEUS zich richten op gemiddelde gebruikers die gewoon een eenvoudige manier willen om snelle en goedkope bitcoinbetalingen te doen vanaf hun mobiele apparaat, met een [ingebouwde mobiele Lightning-node](https://docs.zeusln.app/category/embedded-node) en een geïntegreerde [Lightning Service Provider (LSP)](https://docs.zeusln.app/lsp/intro).


### Belangrijke Zeus-bronnen:


- Officiële webpagina van Zeus - [https://zeusln.app/](https://zeusln.app/)
- Zeus Documentatie - [https://docs.zeusln.app/](https://docs.zeusln.app/)
- [Zeus Github-repository](https://github.com/ZeusLN/zeus)
- [Zeus Telegram-ondersteuningsgroep](https://t.me/ZeusLN)
- [Zeus op NOSTR](https://iris.to/zeus@zeusln.app)
- [Zeus Blog-aankondigingen](https://blog.zeusln.com)


### Zeus Kenmerken

#### Algemene kenmerken:


- Zelfbehoud, alleen Bitcoin en Lightning Wallet
- Geen verwerkingskosten, geen KYC
- Volledig open bron (APGLv3)
- Multi node / accounts ondersteund (je kunt je eigen home node(s) beheren, embedded LND node draaien, verbinding maken met meerdere LNDhub accounts)
- Gebruiksvriendelijk activiteitenmenu
- PIN- of passphrase-codering, Privacymodus - verberg je gevoelige gegevens
- Contactboek, meerdere thema's, meerdere talen


#### Technische kenmerken


- Verbinding maken via Tor
- Volledige LNURL-ondersteuning (betalen, opnemen, auth, kanaal), verzenden naar Lightning-adressen
- Gedetailleerd beheer van verlichtingskanalen, MPP/AMP-ondersteuning, Keysend, beheer van routeringskosten
- Replace-by-fee (RBF) en kind-voor-ouder (CPFP) ondersteuning
- NFC-betalingen en -verzoeken, Berichten ondertekenen en verifiëren
- Ondersteuning voor SegWit en Taproot
- Eenvoudige Taproot kanalen
- Zelfstandige bliksemadressen (@zeuspay.com)
- Point of Sale door Square (binnenkort open PoS)


### Handleidingen en video's

Om Zeus te kunnen gebruiken en de Lightning-kanalen, liquiditeit, vergoedingen enz. te beheren, is het beter om eerst enkele belangrijke gidsen over Lightning Network te lezen.


#### Gidsen:


- [LND - Lightning Network Daemon-documentatie](https://docs.lightning.engineering/)
- [CLN - Core Lightning-documentatie](https://lightning.readthedocs.io/index.html)
- [Lightning-gids voor beginners](https://bitcoiner.guide/lightning/) – door Bitcoin Q&A
- [Lightning-knooppuntbeheer](https://www.lightningnode.info/) – door openoms
- [Het Lightning Network en de luchthaven-analogie](https://darthcoin.substack.com/p/the-lightning-network-and-the-airport)
- [Beheer van Lightning Node-liquiditeit](https://darthcoin.substack.com/p/managing-lightning-node-liquidity)
- [Onderhoud van Lightning Node](https://darthcoin.substack.com/p/lightning-node-maintenance)


#### Videohandleiding door BTC Sessions


![Zeus Bitcoin Lightning Wallet - Mobile Node Management](https://youtu.be/hmmehTnV3ys)



## Een handleiding voor het gebruik van Zeus LN embedded node op je mobiele apparaat


![Image](assets/en/01.webp)


Ik draag deze gids op aan alle nieuwe Lightning Network (LN) gebruikers die een nieuwe soevereine reis willen beginnen met behulp van een self-custody node Wallet op hun mobiele apparaten.


Laten we eens bedenken dat je al door al die overvloed aan behouderde LN wallets heen bent, maar je bent nog niet klaar om een PUBLIC routing LN node te gaan runnen, je wilt gewoon meer Sats over LN stapelen op een meer self-custodial manier en je regelmatige betalingen over LN doen.


Hier komt Zeus, beginnend met [versie v0.8.0 aangekondigd op hun blog](https://blog.zeusln.com/new-release-zeus-v0-8-0/), dat nu een ingebedde LND-node in de app aanbiedt. Tot nu toe was Zeus een app voor het beheren van externe nodes + LNDhub-accounts. Maar nu… de node zit in de telefoon!


![Image](assets/en/02.webp)


### Een kort overzicht van de belangrijkste functies van Zeus Node:



- **Privé LND knooppunt** - Dat betekent dat dit knooppunt GEEN openbare routering van betalingen van anderen via jouw knooppunt zal doen. Het knooppunt en de kanalen zijn onaangekondigd (privé, niet zichtbaar op de openbare LN grafiek). Het ontvangen en doen van betalingen zal gebeuren via je verbonden LSP peers. Onthoud: Zeus Embedded Node zal GEEN publieke routering doen!
- **Persistente LND dienst** - de gebruiker kan deze functie activeren en de LND dienst continu actief houden, net als elk ander regulier LN knooppunt. De app hoeft niet open te zijn, de persistente dienst houdt alle communicatie online.
-   **Neutrino-blokfilters** - blokksynchronisatie gebeurt met behulp van [blokfilters en het Neutrino-protocol](https://bitcoinops.org/en/topics/compact-block-filters/) (zonder informatie te verstrekken over de on-chain fondsen van onze gebruikers). Herinnering: bij hoge latentie / trage internetverbindingen kan deze op Neutrino gebaseerde blokksynchronisatie soms mislukken. Proberen over te schakelen naar een nabijgelegen Neutrino-server kan helpen de synchronisatie te herstellen. Zonder deze synchronisatie kan uw LND-node niet starten!
- **Eenvoudige Taproot kanalen** - Bij het sluiten van deze kanalen hebben gebruikers minder kosten en krijgen ze meer privacy, omdat ze lijken op alle andere Taproot uitgaven bij het onderzoeken van hun On-Chain voetafdruk.
- **Geïntegreerde LSP** - Olympus is het nieuwe LSP-knooppunt voor Zeus. Gebruikers kunnen Sats direct ontvangen via LN, zonder eerst LN kanalen te moeten instellen. Ze hoeven alleen maar een LN Invoice aan te maken en te betalen vanaf elke andere LN Wallet, met Zeus 0-conf kanaalservice. Lees hier meer over Zeus LSP. De LSP biedt ook extra privacy aan onze gebruikers door ze te voorzien van ingepakte facturen die de publieke sleutels van hun nodes verbergen voor betalers.
- **Contactenboek** - je kunt handmatig contacten opslaan of importeren vanuit NOSTR, zodat je gemakkelijk betalingen kunt sturen naar je vaste bestemmingen.
- **Volledige ondersteuning voor LNURL, LN Address verzenden en ontvangen** - nu kun je zelf je eigen LN Address instellen met @zeuspay.com. Herinnering: Je kunt Zeus ook gebruiken voor LN-auth op sites waar je kunt inloggen met een LN authenticatie. Is erg handig.
- **Point of Sale** - Nu kunnen verkopers hun eigen productitems instellen en direct vanuit Zeus verkopen, met geïntegreerde PoS. Bevat op dit moment de basisbehoeften, maar zal in de toekomst uitgebreide functies bevatten.
- **LND logs** - de gebruiker kan in realtime de logs van de LND service lezen en ze gebruiken om mogelijke problemen op te lossen (voornamelijk slechte verbindingen)
- **Geautomatiseerde back-ups** - van de LN nodekanalen wordt automatisch een back-up gemaakt op de Olympus server. Deze geautomatiseerde back-up wordt versleuteld met uw node Wallet seed (zonder de seed is deze volledig onbruikbaar). De gebruiker kan ook handmatig een SCB (statische kanaalback-up) exporteren voor een noodherstel.


### Hoe aan boord te komen met Zeus LN Node (LND ingebed)


In deze handleiding zal ik alleen spreken over de ingebouwde LND-node en niet over de andere manieren om deze geweldige app te gebruiken (beheer van externe nodes en LNDhub-accounts). Voor de andere soorten verbindingen, raadpleeg de [Zeus-documentatiepagina](https://docs.zeusln.app/category/getting-started), die zeer goed is uitgelegd en waarvoor geen aparte handleiding nodig is.


#### STAP 1 - EERSTE INSTALLATIE


Omdat Zeus een volledig LND knooppunt is, heb ik een aantal eerste aanbevelingen:



- Gebruik geen oud apparaat, dat kan het gebruik van deze krachtige app beïnvloeden. Vooral in de synchronisatieperiode kan de app de CPU en het RAM intensief gebruiken. Het ontbreken hiervan kan het gebruik van de Zeus app zelfs onmogelijk maken.
- Gebruik ten minste Android 11 als mobiel besturingssysteem en werk zoveel mogelijk bij. Voor iOS geldt hetzelfde, probeer een veel hogere versie van OS te gebruiken.
- Je hebt minstens 1 GB schijfruimte nodig voor de gegevensopslag. Na verloop van tijd kan dit meer worden, maar er is een functionaliteit om de database te comprimeren tot een niveau van MB's.
- Het is NIET nodig om Zeus te gebruiken met Tor of Orbot service. Maak het alsjeblieft niet ingewikkelder dan nodig is. Tor biedt je in dit geval niet meer privacy, maar maakt het alleen maar erger voor de eerste synchronisatie. Wees ook voorzichtig met welke VPN's je gebruikt en controleer de latentie van de verbinding naar de Neutrino-servers. Houd in gedachten dat de Neutrino blokkeerfilter de identiteit van je apparaat niet lekt of traceert, maar alleen blokkades serveert. Het LN verkeer zit ook achter een LSP met privékanalen dus er komt maar weinig informatie vrij, er is geen reden om je zorgen te maken over privacy.
-   Heb geduld voor de initiële synchronisatie, dit kan enkele minuten duren. Probeer verbonden te zijn met een breedbandinternetverbinding met lage latentie. Als je je eigen Bitcoin-node draait, [kun je de neutrino-service activeren](https://docs.lightning.engineering/lightning-network-tools/lnd/enable-neutrino-mode-in-bitcoin-core) en je Zeus verbinden met je eigen node, zelfs met behulp van het interne LAN, zodat je maximale snelheid hebt.


Zodra je het verbindingstype "Embedded node" hebt ingesteld, begint de app even met synchroniseren. Wacht geduldig tot dat deel klaar is en ga dan naar de hoofdpagina Instellingen.


![Image](assets/en/03.webp)


Laten we kort in elk van de instellingensecties duiken en enkele van de belangrijkste functies begrijpen voordat je Zeus gaat gebruiken:


**A - INSTELLINGEN**


Dit is een sectie met algemene instellingen voor de hele app


**1 - Lightning Service Provider (LSP)**


Hier worden twee LSP-diensten gepresenteerd:



- _Just in time kanalen_ - wanneer je geen kanaal open of inkomende liquiditeit beschikbaar hebt, zal de service, wanneer deze geactiveerd is, on-the-fly een kanaal voor je openen. Deze optie kan worden uitgeschakeld als u niet meer van dit soort kanalen wilt openen.
- _Vroeg kanalen aan_ - u kunt inkomende kanalen van het Olympus LSP rechtstreeks in de app kopen met meerdere opties en bedragen (voor inkomend en uitgaand).


Het LSP helpt gebruikers verbinding te maken met het Lightning-netwerk door betalingskanalen naar hun nodes te openen. [Lees hier meer over LSP](https://medium.com/breez-technology/envisioning-lsps-in-the-lightning-economy-832b45871992). ZEUS heeft een nieuwe geïntegreerde LSP genaamd [OLYMPUS by ZEUS](https://mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581), die beschikbaar is voor alle gebruikers die de nieuwe ingebouwde node gebruiken.


In dit gedeelte staat standaard het Olympus LSP (https://0conf.lnolymp.us), maar binnenkort kunt u ook een ander 0conf LSP instellen dat dit protocol ondersteunt.


onthoud:_

wanneer u een kanaal opent met Olympus LSP met behulp van de verpakte LN facturen, krijgt u ook een 100k inkomende liquiditeit! Dit is echt een goede optie voor het geval u direct meer Sats wilt ontvangen._

voorbeeld: je stort 400k Sats om een LSP-kanaal te openen, dan opent het LSP een kanaal met een capaciteit van 500k Sats naar je Zeus-knooppunt en duwt de 400k Sats die je stort naar jouw kant

_"Inkomende liquiditeit" = meer "ruimte" in je kanaal om te ontvangen._


In de toekomst hopen we op vele andere LSP's die in Zeus kunnen worden geïntegreerd en elk als alternatief kunnen worden gebruikt. Het is slechts een kwestie van tijd totdat nieuwe LSP's een open standaard zullen adopteren voor dit soort 0conf-kanalen.


Als je niet "on the fly" nieuwe kanalen wilt openen, kun je deze optie uitschakelen.


In dezelfde sectie heb je ook de optie om te kiezen voor "Simple Taproot Channels aanvragen" wanneer het LSP een kanaal naar je Zeus-knooppunt opent. Deze Eenvoudige Taproot Kanalen bieden betere On-Chain privacy en lagere kosten bij kanaalsluiting. Er zijn slechts twee redenen waarom je ze niet zou willen gebruiken:



- Ze zijn nieuw en er kunnen nog bugs in LND zitten als je ze gebruikt.
- Je tegenpartij ondersteunt ze niet. Zelfs LND knooppunten moeten er voorlopig expliciet voor kiezen.


**2 - Betalingsinstellingen**


Deze functie biedt u de mogelijkheid om uw eigen voorkeurstarieven voor betalingen in te stellen, via LN of onchain. Ook kunt u de time-out voor uw facturen verhogen of verlagen.


Als sommige van je LN betalingen mislukken, kun je de vergoeding verhogen om een betere route te vinden. Ook als je onchain txs doet, kun je een specifieke vergoeding instellen, zodat je tx niet voor lange tijd vast komt te zitten in de Mempool, in het geval van hoge vergoedingen.


**3 - Factuurinstellingen**


In dit gedeelte staan enkele opties voor generate facturen:



- Stel een standaardmemo in die wordt weergegeven op de Invoice u generate
- Verlooptijd in seconden, voor het geval je een specifieke tijd wilt, langer of korter voor je Invoice om betaald te worden
- Neem route hints op - geef informatie om niet-aangeprezen, of privé, kanalen te vinden. Hierdoor kunnen betalingen worden gerouteerd naar knooppunten die niet publiek zichtbaar zijn op het netwerk. Een routehint geeft een gedeeltelijke route tussen het privéknooppunt van de ontvanger en een openbaar knooppunt. Deze routeringshint wordt dan opgenomen in de Invoice die door de ontvanger wordt gegenereerd en aan de betaler wordt verstrekt. Ik stel voor om dit standaard in te schakelen, anders kunnen inkomende betalingen mislukken (geen route gevonden).
- AMP Invoice - Atomic Multi-path Payments zijn een nieuw type Lightning-betalingen geïmplementeerd door LND, die het mogelijk maken Sats te ontvangen zonder een specifieke Invoice, met behulp van [Keysend](https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-Keysend). Is praktisch een statische betalingscode. [Lees hier meer](https://docs.lightning.engineering/lightning-network-tools/LND/amp).
- Toon aangepast preimage veld - gebruik deze optie alleen in zeer specifieke gevallen als je echt aangepaste velden in het preimage wilt gebruiken. [Lees hier meer](https://Bitcoin.stackexchange.com/questions/90797/how-can-i-generate-preimage-for-lightning-network-Invoice-should-i).


Een andere optie in deze sectie is het instellen van het type onchain Address dat je wilt gebruiken: SegWit genest, SegWit, Taproot.


![Image](assets/en/04.webp)


Klik op de bovenste wielknop en er verschijnt een pop-up scherm om het gewenste type Address te kiezen. Als je dat eenmaal hebt ingesteld, zal de volgende keer dat je op de ontvangstknop voor onchain drukt, Address het geselecteerde type Address zijn. Je kunt het op elk moment veranderen.


**4 - Kanaalinstellingen**


In dit gedeelte kun je een aantal openingskanalen vooraf instellen, zoals:



- aantal bevestigingen
- Kanaal aankondigen (standaard uitgeschakeld), dat betekent dat het onaangekondigde kanalen zullen zijn
- Eenvoudige Taproot kanalen
- Toon kanaal aankoopknop


**5 - Privacy-instellingen**


Hier vind je een aantal basisinstellingen om meer privacy toe te voegen met de Zeus app:



- Block explorer om tx-details te openen (Mempool.space, blockstream.info of aangepaste persoonlijke)
- Lees klembord - aan/uit om te schakelen als je wilt dat Zeus het klembord van je apparaat leest
- Lurker modus - aan/uit om te schakelen als je specifieke gevoelige info van je Zeus app wilt verbergen. Is een goede optie als je demo's of screenshots maakt.
- Mempool tariefsuggestie - activeer deze optie als je de aanbevolen tariefniveaus van [Mempool.space](https://Mempool.space/) wilt gebruiken


**6 - Beveiliging**


Dit gedeelte heeft slechts twee opties voor het beveiligen van de app bij het openen: een wachtwoord of een pincode instellen.


Zodra u een PIN-code hebt ingesteld om de app te openen, kunt u ook een "dwang-PIN-code" instellen. Deze geheime extra PIN-code wordt ALLEEN gebruikt in geval van bedreiging. Als u deze PIN-code invoert, wordt de configuratie volledig gewist. U kunt dus beter uw back-ups bijhouden. Geautomatiseerde back-ups staan standaard AAN, maar het is goed om ook je eigen back-ups te hebben, buiten het apparaat om.


**7 - Valuta**


Schakel de optie in of uit om een conversie van fiatvaluta weer te geven in het gebruik van de Zeus-app. Momenteel worden meer dan 30 fiatvaluta's wereldwijd ondersteund.


**8 - Taal**


Je kunt schakelen tussen meerdere vertaaltalen, beoordeeld door Zeus community met moedertaalsprekers.


**9 - Weergave**


In dit gedeelte kunt u uw Zeus-display personaliseren door verschillende kleurenthema's te selecteren, standaardscherm (toetsenbord of balans), uw knooppuntalias tonen, grote toetsen op het toetsenbord activeren, meer decimalen tonen.


**10 - Verkooppunt**


Dit is een speciale functie om een geïntegreerd PoS-systeem in Zeus in of uit te schakelen. Je kunt een standalone PoS draaien of gekoppeld aan een Square PoS-systeem. Momenteel ondersteunt het basisfunctionaliteiten als een PoS, maar genoeg voor een goede start en het zou kleine handelaars (bars/restaurants, kruidenierszaken) kunnen helpen om BTC te beginnen accepteren op een eigen manier.


In deze instellingen vindt u verschillende opties om uw PoS in te stellen:



- Type bevestiging betaling: Alleen LN, 0-conf, 1-conf
- Fooien in-/uitschakelen voor medewerkers die de PoS bedienen
- Toetsenbord tonen/verbergen
- Belastingpercentage op het ticket
- Producten en productcategorieën maken
- Een eenvoudige lijst van alle verkopen


Hier is een live demovideo over het gebruik van Zeus PoS:


**B - Back-up Wallet**


Het embedded knooppunt in ZEUS is gebaseerd op LND en gebruikt het [aezeed seed formaat](https://github.com/lightningnetwork/LND/blob/master/aezeed/README.md). Dit is anders dan het typische [BIP39 formaat](https://github.com/Bitcoin/bips/blob/master/bip-0039.mediawiki) dat je in de meeste Bitcoin wallets ziet, hoewel het erop lijkt. Aezeed bevat een aantal extra gegevens, waaronder de geboortedatum van de Wallet, die het opnieuw scannen tijdens het herstel efficiënter laten verlopen.


Het aezeed sleutelformaat zou compatibel moeten zijn met de volgende mobiele portemonnees: Blixt, BlueWallet en Breez. Merk op dat de seed alleen onvoldoende zal zijn om al je tegoeden te recupereren als je open of hangende sluitingskanalen hebt !


Leer meer over het back-up- en herstelproces op [Zeus Docs pagina](https://docs.zeusln.app/for-users/embedded-node/backup-and-recovery).


AANBEVELING: Wanneer je je seed opslaat, sla dan ook de node pubkey op! Soms is het goed om deze bij de hand te hebben, samen met je seed en SCB (Static Channels Backup) voor het geval je het herstel moet verifiëren.


SCB is alleen nodig als je LN kanalen open hebt. Als je alleen onchain fondsen hebt, is dit niet nodig.


Als je ziet dat na een lange tijd nog steeds niet de oude geschiedenis txs wordt weergegeven, ga dan naar Embedded node - Peers en schakel de optie uit om de lijst met geselecteerde peers te gebruiken (standaard is dit btcd.lnolymp.us). Dat zorgt voor een herstart en maakt verbinding met het eerste beschikbare neutrino-knooppunt met een betere tijdreactie. Of gebruik de hieronder genoemde andere bekende neutrino peers.


Als je meer herstelopties wilt zien voor een LND node, [lees dan mijn vorige gids](https://darth-Coin.github.io/nodes/shtf-restore-LND-node-en.html), waar je de stappen kunt vinden hoe je een seed met aeze kunt importeren in Sparrow wallet of andere methoden.


**C - Ingebed knooppunt**


In deze sectie vinden we enkele basistools om het geïntegreerde knooppunt te beheren:



- _Disaster Recovery_ - Geautomatiseerde en handmatige back-ups voor de LN kanalen. Lees meer over het gebruik van deze functie op de Zeus Docs pagina.
- express Graph Sync_ - Zeus app downloadt de LN roddelgegevens grafiek van een speciale server, voor snellere en betere synchronisatie. Je kunt er ook voor kiezen om vorige grafiekgegevens te wissen bij het opstarten.
- _Peers_ - sectie om de neutrino peers en 0-conf peers te beheren. Als je problemen hebt met de initiële synchronisatie, kanalen die niet online komen, komt dat omdat je apparaat een hoge latentie heeft met de geconfigureerde neutrino peer. Probeer de lijst met voorkeurspeers te wijzigen of voeg een specifieke peer toe waarvan je weet dat deze een betere latentie heeft voor synchronisatie. Bekende neutrino servers zijn:



 - btcd1.lnolymp.us | btcd2.lnolymp.us - voor regio VS
 - sg.lnolymp.us - voor de regio Azië
 - btcd-Mainnet.lightning.computer - voor regio VS
 - uswest.blixtwallet.com (Seattle) - voor de regio VS
 - europe.blixtwallet.com (Duitsland) - voor EU-regio
 - asia.blixtwallet.com - voor regio Azië
 - node.eldamar.icu - voor regio VS
 - noad.sathoarder.com - voor regio VS
 - bb1.breez.technology | bb2.breez.technology - voor regio VS
 - neutrino.shock.network - regio VS



- _LND logs_ - zeer nuttig gereedschap om problemen met uw LN knooppunt op te lossen en op een meer technisch niveau te controleren wat er aan de hand is.
- _Geavanceerde instellingen_ - meer tools om het gebruik van uw LND knooppunt te regelen:



 - padzoekmodus_ - bimodaal of apriori, manieren om een betere route te vinden voor uw LN betalingen en ook het resetten van de vorige route-informatie. Lees deze zeer goede gidsen over pathfinding: [Pathfinding](https://docs.lightning.engineering/lightning-network-tools/LND/pathfinding) - door Docs Lightning Engineering en [LN Betaling Pathfinding](https://voltage.cloud/blog/lightning-network-faq/understanding-payment-pathfinding-between-nodes-on-lightning-network/) - door Voltage
 - _Persistent LND_ - activeer deze modus als je wilt dat de LND service continu op de achtergrond draait en je node 24/7 online blijft. Dit is erg handig als je Zeus gebruikt als PoS in een kleine winkel of als je veel LN tips ontvangt over de LN Address.
 - _Rescan wallet_ - deze optie zal bij het herstarten een volledige scan van alle onchain txen van je Wallet activeren. Activeer deze optie alleen als u enkele txs in uw Wallet mist. De rescan taak zal tijd in beslag nemen, enkele minuten, dus wees geduldig en controleer altijd de logs om meer details over de voortgang te zien.
 - _Compact Database_ - deze optie is erg handig als je Zeus app veel apparaatruimte inneemt (zie app details in je apparaatinstellingen). Als je veel activiteit hebt met Zeus, zou ik aanraden om deze compactie vaker uit te voeren. Zodra je ziet dat je meer dan 1-1,5GB gegevens hebt voor de Zeus app, voer dan de verdichting uit. Het zal opnieuw opstarten en enige tijd duren, dus wees geduldig.
 - _Delete Neutrino files_ - deze optie om de neutrino-bestanden te verwijderen (met een herstart) zal het gebruik van gegevensopslag sterk verminderen. Het verminderen van het dataverbruik heeft ook een grote impact op het batterijverbruik, vooral als je Zeus in persistente modus gebruikt.


**D - Knooppuntinformatie**


In deze sectie vind je meer details over de status van je Zeus knooppunt zoals:



- Alias - korte knooppunt-ID
- Publieke sleutel - de volledige publieke sleutel voor jouw knooppunt die andere knooppunten nodig hebben om het pad naar jouw knooppunt te vinden. Onthoud dat deze pubkey NIET zichtbaar is op de reguliere LN Explorers (Mempool, Amboss, 1ML etc.). Deze pubkey is ALLEEN bereikbaar via de met jou verbonden LN peers en kanalen.
- LN implementatieversie
- Zeus app versie
- Status gesynchroniseerd met keten en Status gesynchroniseerd met grafiek - erg belangrijk om de juiste status van je knooppunt weer te geven. Als deze twee niet "true" worden weergegeven, betekent dit dat je node nog aan het synchroniseren is of problemen heeft met synchroniseren. Het is dus aan te raden om in je LND logs te kijken of nog even te wachten.
- Blokhoogte en Hash - toont het laatste blok en Hash dat je knooppunt zag en synchroniseerde.


**E - Netwerk Info**


Dit deel toont meer details over de algemene status van de Lightning Network, uit de synchronisatiegegevens van uw grafiek: aantal openbare kanalen beschikbaar, aantal knooppunten, aantal zombiekanalen (offline of dood), grafiekdiameter, gemiddelde en max. graad voor de grafiek.


Deze informatie kan nuttig zijn voor debuggen of gewoon worden gebruikt voor statistieken.


**F - Bliksem Address**


In dit gedeelte kan de gebruiker zijn eigen zelfbewaarplaats LN Address @zeuspay.com instellen.


ZEUS PAY maakt gebruik van door gebruikers gegenereerde preimage hashes, HODL facturen en het Zaplocker Nostr attestatieschema om gebruikers die misschien niet 24/7 online zijn, betalingen te laten ontvangen op een statische bliksem Address. Gebruikers hoeven alleen maar binnen 24 uur in te loggen op hun ZEUS wallets om de betalingen te claimen, anders worden ze teruggestuurd naar de afzender.


Als je de "persistente modus" activeert, worden alle betalingen naar je LN Address direct ontvangen.


Leer meer over hoe [Zaplocker](https://github.com/supertestnet/zaplocker#how-it-works) betalingen werken en meer over [ZeusPay Fees here](https://docs.zeusln.app/lightning-Address/fees).


**G - Onchain-adressen**


In deze sectie kunt u uw gegenereerde onchain-adressen raadplegen voor een betere Coin controle


**H - Contacten**


Een nieuw contactenboek werd geïntroduceerd in Zeus v 0.8.0 dat je kunt gebruiken om snel betalingen te sturen naar je vrienden en familie, ook met de mogelijkheid om je contacten te importeren vanuit Nostr.


Voer gewoon uw Nostr npub of menselijk leesbare NIP-05 Address in, en ZEUS zal Nostr om al uw contacten vragen. Van daaruit kunt u een snelle betaling naar een contact sturen, of alle of geselecteerde contacten importeren naar uw lokale contactboek./<


Hier is een korte video over het configureren en gebruiken van je Zeus-contacten:


**I - Gereedschap**


Hier hebben we verschillende subsecties met meer hulpmiddelen:



- _Accounts_ - hier kun je externe accounts / wallets importeren, Cold wallets, Hot wallets, om te controleren of te gebruiken als externe financieringsbron voor je Zeus node kanalen. Deze functie is nog experimenteel.
- transactie versnellen_ - Deze functie kan handig zijn als je een vastgelopen tx in Mempool hebt en de vergoeding wilt verhogen. Je moet de tx output opgeven van tx details en de gewenste nieuwe fee selecteren die je wilt gebruiken. Moet hoger zijn dan de vorige en vereist dat je meer geld beschikbaar hebt in je Wallet.


![Image](assets/en/05.webp)


Je moet naar je lopende tx gaan en het txid-uitgangspunt kopiëren. Ga dan naar dit gedeelte en plak het, selecteer dan de nieuwe vergoeding die je wilt gebruiken om de tx te stoten. Er verschijnt een nieuw scherm met aanbevolen vergoedingen op dat moment, of je kunt een aangepaste vergoeding instellen. Onthoud dat deze hoger MOET zijn dan de vorige.


Het is altijd beter om een UTXO met maximaal 100k Sats in je Zeus onchain Wallet te houden, zodat je die kunt gebruiken om vergoedingen te stoten als dat nodig is.



- _Tekenen of Verifiëren_ - Met deze functie kunt u een specifiek bericht ondertekenen met uw Wallet sleutels. Het kan ook gebruikt worden om een bericht te verifiëren om te bewijzen dat het van een specifieke Wallet sleutel komt.
- valuta omzetter_ - een eenvoudig hulpmiddel om de koers te berekenen tussen BTC en andere fiatvaluta's.


**J - Merch en ondersteuning**


Hier vind je meer info en links over Zeus, online shop, sponsors, sociale media.


**K - Help**


In deze laatste sectie vind je links naar de Zeus documentatiepagina, Github issues (als je een bug of verzoek direct bij de app-ontwikkelaars wilt plaatsen), e-mailondersteuning.



### STAP 2 - ZEUS NODE GAAN GEBRUIKEN



Vergeet niet dat Zeus voornamelijk gebruikt moet worden als een LN Wallet, voor gemakkelijke en snelle betalingen over LN. Zeker, het bevat ook een onchain Wallet, maar die moet uitsluitend gebruikt worden voor het openen/sluiten van LN kanalen en niet voor regelmatige betalingen van een koffie.


Lees mijn andere gids over [hoe je je eigen bank kunt zijn met behulp van de 3 niveaus van Stash](https://darth-Coin.github.io/beginner/be-your-own-bank-en.html).


Op dit moment heeft de gebruiker 2 manieren om Zeus te gebruiken:



- Rechtstreeks over LN, via het 0-conf kanaal van Olympus LSP
- Eerst storten in onchain Wallet en dan een normaal LN kanaal openen met de peer die je wenst.


#### Methode A - Olympus LSP gebruiken


Dit is een zeer gemakkelijke en eenvoudige manier om een nieuwe LN gebruiker in Zeus te laten instappen. Het kan een geheel nieuwe Bitcoin gebruiker zijn die nog geen Sats heeft, die door een vriend aan boord is gebracht, of een nieuwe handelaar die begint met zijn 1e LN betaling.


Standaard gebruikt Zeus zijn eigen LSP, Olympus. Maar later kunt u ook overschakelen naar andere LSP's die dit 0-conf protocol ondersteunen om kanalen te openen.


Door gewoon een Invoice aan te maken op je Zeus (vul het bedrag in en klik op de knop "aanvragen"), kun je die Sats meteen ontvangen.


De Invoice die je generate geeft, wordt [ingepakt](https://docs.zeusln.app/lsp/wrapped-invoices) en je krijgt de kosten te zien die bij de dienst horen als ze betaald zijn. Deze verpakte Invoice bevat route hints naar je Zeus knooppunt, zodat de LSP je nieuwe knooppunt kan vinden en een kanaal kan openen met de nieuwe fondsen die je stort.


![Image](assets/en/06.webp)


![Image](assets/en/07.webp)


Om een LN-kanaal van het LSP te krijgen met het geld dat je de eerste keer wilt ontvangen, moet deze Invoice betaald worden van een andere LN Wallet en een paar momenten wachten tot het LSP het kanaal opent naar jouw Zeus-knooppunt, de kosten aftrekken en het resterende bedrag van de betaling aan jouw kant van het kanaal duwen.


Het enige wat je hoeft te doen is de Invoice die voor je gegenereerd is in ZEUS te betalen met een andere bliksem Wallet, en je kanaal zal direct openen. [Raadpleeg de Zeus LSP tarieven](https://docs.zeusln.app/lsp/fees).


Een ander voordeel van betalen voor een kanaal is routing zonder kosten. Dat betekent dat bij het routeren van betalingen de eerste stap door OLYMPUS by ZEUS geen routeringskosten met zich meebrengt. Merk op dat hops voorbij OLYMPUS by ZEUS u nog steeds kosten in rekening brengen.


Zodra het kanaal klaar is, klik je op de rechterknop onderaan het scherm, die de Zeus-kanalen weergeeft.


![Image](assets/en/08.webp)


En je zult een kanaal als dit zien, dat jouw kant van de kanaalbalans laat zien:


![Image](assets/en/09.webp)


Hoe meer je zult uitgeven vanuit dit kanaal, hoe meer inkomende liquiditeit je zult hebben. Voor meer Sats die je ontvangt in dit kanaal, heb je minder inkomende liquiditeitsruimte.


Hier is een mooie eenvoudige visuele demonstratie (door Rene Pickhardt) over hoe LN kanalen werken:


Op dit moment, gezien het demoscherm voor kanalen, klik je op de kanaalnaam en zie je er meer details over.


Je hebt een enkel kanaal met Olympus, met een totale capaciteit van 490 000 Sats, met een saldo van 378k Sats aan jouw kant en 88k Sats aan de kant van Olympus. Dat betekent dat je maximaal 88k Sats meer zou kunnen ontvangen in hetzelfde kanaal.


Als je meer dan 88k Sats moet ontvangen (de beschikbare inkomende liquiditeit in dit geval), laten we zeggen nog eens 500k Sats, door eenvoudigweg een nieuwe LN Invoice met die hoeveelheid aan te maken, zal een nieuw kanaalverzoek naar het Olympus LSP worden getriggerd. Dus je krijgt een 2e kanaal.


Dat is waarom, om te voorkomen dat u meer kosten betaalt voor het openen van meerdere kanalen, het wordt aanbevolen om de eerste keer een groter kanaal te openen, laten we zeggen 1-2M Sats. Eenmaal open, kunt u een deel van die Sats, laten we zeggen 50%, omwisselen naar onchain, met behulp van een externe swap service zoals beschreven in deze gids.


Zodra je uit dat kanaal wisselt, laten we zeggen 50%, en de Sats terugkrijgt in je eigen Zeus onchain Wallet, ben je klaar om over te gaan naar de volgende methode om een nieuw kanaal te openen - vanuit onchain balans.


#### Methode B - Uw saldo op de ketting gebruiken


Met deze methode kunt u kanalen openen naar elk ander LN knooppunt, inclusief hetzelfde Olympus LSP. Maar als u al een kanaal met Olympus hebt, is het aan te raden om ook een kanaal met een ander knooppunt te hebben, voor meer betrouwbaarheid en ook om MPP (multi-part payment) te gebruiken.


![Image](assets/en/10.webp)


Hierboven zie je een voorbeeld van het betalen van een LN Invoice met MPP. Zoals je kunt zien heb je onderaan het scherm "instellingen" en opent een uitklappagina met meer details voor de betaling die je gaat doen. In dat scherm, als je minstens 2 kanalen open hebt, staat de MPP-functie standaard AAN. Je kunt ook AMP (atomic multi-path) activeren en specifieke onderdelen instellen. Dit is een krachtige functie!


Voor een privéknooppunt als Zeus zou ik aanraden om 2-3 goede kanalen te hebben (max. 4-5), met goede LSP's en een goede liquiditeit om aan al je behoeften te voldoen om Sats over LN te betalen of te ontvangen. [Zie meer LN node liquiditeitsadvies in deze gids](/nodes/managing-lightning-node-liquidity-en.html). Hier is ook een andere [algemene gids over LN liquiditeit](https://Bitcoin.design/guide/how-it-works/liquidity/) van het Bitcoin Ontwerpteam.


Ik weet dat het kiezen van de juiste peers geen gemakkelijke taak is, zelfs niet voor ervaren gebruikers. [Dus zal ik je enkele opties geven om te beginnen](https://github.com/ZeusLN/zeus/discussions/2265), dit zijn peer nodes die ik zelf getest heb met Zeus (ik probeerde alleen verbinding te maken met LND nodes om incompatibiliteitsproblemen te vermijden)


Hier is ook een lijst van betrouwbare knooppuntgenoten voor Zeus. Als je goede kent, ben je welkom om ze aan die lijst toe te voegen.


Je kunt een kanaal openen in Zeus door naar de Kanalenweergave te gaan door op het kanaalpictogram in de rechterbenedenhoek van de hoofdweergave te klikken en dan op het +-pictogram in de rechterbovenhoek.


![Image](assets/en/11.webp)


Als je een kanaal met een specifiek knooppunt wilt openen, klik dan op (A) in de bovenhoek om het QR-knooppuntID te scannen (op Mempool, Amboss, 1ML kun je die QR krijgen) en alle details van het knooppunt worden ingevuld.


HERINNERING:


- Zeus embedded node gebruikt geen Tor service! Dus probeer alsjeblieft geen kanalen te openen met nodes die onder Tor zitten! Je brengt jezelf meer schade toe dan dat je meer privacy krijgt. Tor voor LN biedt niet meer privacy maar meer problemen.
- kies je peers verstandig, het kunnen maar beter goede LSP's zijn, goede routing nodes, geen willekeurige pleb nodes die je kanalen kunnen sluiten en geen goede liquiditeit kunnen bieden. [Hier heb ik een speciale gids geschreven](https://darth-Coin.github.io/nodes/managing-lightning-node-liquidity-en.html) over liquiditeit en voorbeelden van knooppunten.


Als u direct op de knop "Kanaal naar Olympus openen" klikt, worden de vereiste velden ingevuld om een kanaal naar [OLYMPUS by ZEUS](https://Mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581) te openen.


In tegenstelling tot betaalde LSP kanalen, zal je kanaal een On-Chain bevestiging vereisen, gebruikmakend van je onchain fondsen (je kunt kiezen uit je UTXO's in de open kanaal weergave); het zal niet direct openen. Raadpleeg eerst de actuele Mempool kosten en pas deze aan, afhankelijk van hoe snel je het kanaal wilt openen.


Voordat je op de knop klikt om het kanaal te openen, schuif je de geavanceerde opties naar beneden:


![Image](assets/en/12.webp)


Je moet er ook voor zorgen dat het kanaal onaangekondigd (besloten) is. Standaard staat de optie uit voor aangekondigde kanalen. Deze optie wordt niet aangeraden om te activeren voor Zeus embedded node, het is alleen handig als je Zeus gebruikt met je remote node, als een publieke routing node.


In tegenstelling tot betaalde LSP-kanalen profiteer je bij het openen van kanalen met deze methode niet van routing zonder kosten.


En klaar, klik op de knop "Kanaal openen" en wacht tot de tx wordt bevestigd door de miners. Zodra het kanaal open is, kun je naar believen handelen met de Sats vanuit je kanalen.


Houd er rekening mee dat deze kanalen al het saldo aan JOUW kant hebben, dus je zult geen inkomende liquiditeit hebben. Zoals ik al eerder zei, ruil uit of besteed wat Sats aan het kopen van spullen over LN om "meer ruimte te maken" om te ontvangen.


Zie je LN kanalen als een glas water. Je giet wat water (Sats) in een leeg glas (je kanaal) totdat je het vult. Je kunt niet meer water gieten totdat je wat gedronken hebt (uitgeven/omruilen). Als het glas bijna leeg is, giet je er meer water (Sats) in met behulp van een swap-in. [Lees hier meer over externe wisseldiensten](https://darth-Coin.github.io/nodes/lightning-submarine-swaps-en.html).


Er zijn ook andere LSP-diensten die je inkomende kanalen verkopen: LNBig of Bitrefill. Ik denk dat er meer van dit soort diensten zijn, maar ik kan ze me nu niet herinneren.


Dus als je praktisch een leeg LN kanaal nodig hebt (het saldo is vanaf het begin 100% aan de peer kant), voor het ontvangen van meer betalingen dan je aankunt op je bestaande volle kanalen, kan dit een hele goede optie zijn. Je betaalt een specifieke vergoeding voor het openen van deze kanalen en je krijgt veel inkomende ruimte.



## TIPS EN TRUCS


### Inkomende reservelimieten


Op dit moment is het vanwege enkele LN codebeperkingen niet mogelijk om precies het bedrag te ontvangen dat wordt weergegeven in "Inkomend". Houd er altijd rekening mee dat je facturen moet maken met een iets lager bedrag, respectievelijk het bedrag van de "Kanaal Lokale Reserve".


![Image](assets/en/13.webp)


Zoals je kunt zien in de bovenstaande afbeelding, toont de "inkomende" dat ik nog steeds 5101 Sats kan ontvangen, maar in feite is het op dit moment onmogelijk om meer te ontvangen. En je kunt zien dat dit evenveel is als de "Lokale reserve".


Houd er dus rekening mee dat wanneer je facturen maakt om te ontvangen, je ook moet kijken naar de liquiditeit van je kanalen en de lokale reserve van dat bedrag moet aftrekken als je het te ontvangen bedrag tot het uiterste wilt drijven.


### Snel advies voor nieuwe gebruikers die beginnen met Zeus node:



- Benut je nieuwe kanalen op de juiste manier.


Als u bijvoorbeeld weet dat u over een week laten we zeggen 1M Sats zult ontvangen, open dan een 2M Sats kanaal en wissel 50-60% van uw uitgaande liquiditeit uit naar onchain Wallet of naar een andere (tijdelijke) bewaar LN rekening. Wees altijd voorbereid met meer liquiditeit. Zodra je meer liquiditeit nodig hebt in je Zeus kanalen, kun je het terugplaatsen van de custodial accounts.


Als je weet dat je laten we zeggen 500k Sats/week zult sturen, open dan een 1M Sats kanaal. Op deze manier heb je nog steeds een reserve totdat je die weer vult.



- Als je een handelaar bent en je ontvangt altijd meer dan je regelmatig uitgeeft, koop dan een speciaal inkomend kanaal. Dit is de goedkoopste manier. Je betaalt een minimale vergoeding en je krijgt een "leeg" kanaal.



- Open geen kleine betekenisloze kanalen van 50-100-300-500k Sats. Je zult ze binnen enkele dagen vullen, zelfs als je ze alleen voor zaps gebruikt. Open grotere en verschillende kanalen, NIET slechts één kanaal.


Zodra je een groter kanaal opent, kun je altijd externe onderzeese swaps gebruiken om Sats naar je onchain wallets te verplaatsen (inclusief terug naar Zeus onchain). Een balans houden tussen inkomende en uitgaande liquiditeit is goed en je kunt die Sats ook "hergebruiken" om meer kanalen te openen als je dat wilt.


### Gewikkeld Invoice


Als je meer privacy wilt bij het ontvangen, kun je de "gewikkelde Invoice" methode gebruiken. Herinnering: om dit te kunnen doen, heb je een kanaal met Olympus LSP nodig. Gewikkelde facturen "verbergen" de eindbestemming (uw Zeus-knooppunt) en tonen uw LSP-knooppunt als bestemming aan de betaler.


Om een gewikkelde Invoice te krijgen, ga je naar het hoofdscherm van het toetsenbord, voer je het bedrag in en druk je op aanvragen. Er verschijnt een normale QR-code voor je Invoice. Klik nu op de knop "X" rechtsboven en je wordt doorgestuurd naar meer opties voor de Invoice.


![Image](assets/en/14.webp)


Nu moet je de optie bovenaan "Enable LSP" activeren en op de knop "Create Invoice" drukken. Die optie zal de gewikkelde Invoice aanmaken en zal een kleine vergoeding vragen.


### Facturen met routehints


Dit is een erg handige functie als je meerdere inkomende kanalen liquide wilt beheren. In de praktijk kun je aangeven naar welk inkomend kanaal je de Sats van een Invoice wilt ontvangen.


Deze functie kan ook worden gebruikt voor circulaire rebalanacing, wanneer je liquiditeit wilt verplaatsen van een gevuld kanaal naar een ander leeg kanaal.


Hoe maak je een Invoice met routeaanwijzingen?



- Schuif op het hoofdscherm de LN-lade naar rechts en klik op "Ontvangen"
- Ga naar het onderste deel van de Invoice-instelling en activeer de knop "Routehints invoegen", kies daarna de tab "Aangepast". Er wordt een scherm geopend met alle beschikbare kanalen. Selecteer het kanaal dat je wilt ontvangen.
- Vul alle andere Invoice gegevens in, bedrag, memo enz. en klik op "Invoice aanmaken".
- Als je die Invoice betaalt, komt de Sats in het aangegeven kanaal.


Als je die Invoice (circulaire herbalancering) aan jezelf wilt betalen, selecteer dan in het betalingsscherm het uitgaande kanaal (één met meer liquiditeit) dat je wilt gebruiken om de betaling te verzenden.


### Betalen met Keysend


Keysend is een zeer onderschatte LN-functie en gebruikers zouden deze vaker moeten gebruiken.


[Keysend](https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-Keysend) staat gebruikers in de Lightning Network toe om betalingen naar anderen te sturen, direct naar hun publieke sleutel, zolang hun knooppunt publieke kanalen heeft en Keysend is ingeschakeld. Keysend vereist niet dat de begunstigde een Invoice uitgeeft.


Hoe kun je dat doen met Zeus?


Scan of kopieer gewoon de nodeID van de bestemming (of gebruik Zeus contacten om je reguliere bestemmingsknooppunten als contacten op te slaan) en klik dan in het hoofdscherm van Zeus op de knop "Verzenden". Plak in dat scherm de nodeID of selecteer deze uit je contacten.


Zet het bedrag van Sats, een bericht als dat nodig is (ja, je kunt het ook gebruiken als een geheime chat over LN) en klik op de knop "Verzenden". Klaar!


![Image](assets/en/15.webp)


Als je een direct kanaal hebt met de peer van bestemming, zijn er GEEN kosten aan verbonden.


Als je geen direct kanaal hebt met de bestemmingspeer, dan zal de Keysend betaling de vergoedingen betalen als een normale LN Invoice betaling, gerouteerd over een regulier pad zoals elke andere betaling. Onthoud alleen dat het geen enkel spoor zal achterlaten als een LN Invoice.


## Samenzwering


Ik raad aan om de vervolggids [Geavanceerd gebruik van Zeus](https://darth-Coin.github.io/wallets/zeus-node-advanced-usage-en.html) te lezen met meer instructies en gebruikssituaties.


En... dat is het! Vanaf nu gebruik je Zeus Node als een gewone BTC/LN Wallet op je mobiel. De UI is vrij rechttoe rechtaan en makkelijk te gebruiken, intuïtief voor elk type gebruiker, ik denk niet dat ik meer details hoef in te voeren over hoe je betalingen doet en ontvangt.


Tot slot volgt hier een vergelijkende privacytabel :


![Image](assets/en/16.webp)
