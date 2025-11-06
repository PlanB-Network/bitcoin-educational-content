---
name: ThunderHub
description: Interface Web voor beheer van bliksemknooppunten LND
---
![cover](assets/cover.webp)



## Inleiding



ThunderHub is een **open-source manager voor Lightning nodes (LND)**, die een intuïtieve Interface biedt die toegankelijk is vanaf elk apparaat of browser.



**Belangrijkste kenmerken:**




- **Bewaking**: Globaal overzicht van saldi, kanalen, transacties, routingstatistieken
- **Beheer**: Kanalen openen/sluiten, inkomende/uitgaande betalingen, kanaalbalancering
- **Integraties**: LNURL ondersteuning, swaps via Boltz, Amboss back-up
- **Interface responsief**: Compatibel met mobiele, tablet- en desktopapparaten met donkere/lichte thema's



ThunderHub integreert eenvoudig met **Umbrel**, **Voltage**, **RaspiBlitz** en **MyNode**, waardoor het dagelijkse beheer van uw node vereenvoudigd wordt.



**ThunderHub is met name geschikt voor operators die op zoek zijn naar een ergonomische Interface om hun kanalen te beheren, liquiditeit (rebalancing) te controleren, transacties te monitoren en diensten van derden zoals Amboss te integreren. Beveiliging is verzekerd via een lokale of Tor-verbinding.**



Als je nog geen Lightning node hebt, raden we je aan onze LND Umbrel tutorial te volgen:



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Installatie



ThunderHub kan op een aantal verschillende manieren worden geïnstalleerd, afhankelijk van uw Lightning node hosting omgeving. Of u nu een kant-en-klare oplossing gebruikt (Umbrel, Voltage, RaspiBlitz, MyNode, Start9, etc.) of een handmatige installatie, ThunderHub is vaak beschikbaar zonder al te veel moeite. Hieronder beschrijven we twee veelgebruikte benaderingen: via de Umbrel App Store en via handmatige installatie (van toepassing op een server of zelf gehoste distributie).



### Installatie via Umbrel



Umbrel integreert ThunderHub in zijn **App Store**, waardoor installatie extreem eenvoudig is. Je hebt geen opdrachtregel of handmatige configuratie nodig: alles gebeurt via Interface Umbrel. Volg gewoon deze stappen:





- **Open het Umbrel dashboard**: Maak verbinding met het Interface web van je Umbrel knooppunt (bijvoorbeeld `http://umbrel.local` op je lokale netwerk, of via zijn `.onion` Address als je Tor gebruikt).
- Ga naar de **App Store**: Klik in het hoofdmenu van Umbrel op "App Store" (of "App"). Zoek naar **ThunderHub** in de lijst met beschikbare applicaties.



![Écran d'installation de ThunderHub via Umbrel](assets/fr/01.webp)





- **Installeer ThunderHub**: Klik op de ThunderHub-toepassing en vervolgens op de knop Installeren. Bevestig indien nodig. Umbrel zal ThunderHub automatisch downloaden en implementeren op uw knooppunt.





- **Start de toepassing**: Zodra de installatie is voltooid (enkele tientallen seconden), verschijnt ThunderHub op uw startpagina. Klik op het pictogram om het te openen. ThunderHub wordt gestart in uw browser.



![Identifiants par défaut pour ThunderHub](assets/fr/02.webp)



**Belangrijk:** Wanneer ThunderHub voor het eerst wordt geopend, wordt automatisch het **standaard wachtwoord** weergegeven dat nodig is om in te loggen. Met de optie "Dit niet meer tonen" kunt u deze weergave verbergen voor toekomstige verbindingen. **We raden u sterk aan om:**




- Sla dit wachtwoord **onmiddellijk** op in uw wachtwoordmanager
- Kopieer het **voor gebruik in de volgende stap**
- Vink "Dit niet meer tonen" aan zodra het wachtwoord is opgeslagen



![Page de connexion de ThunderHub](assets/fr/03.webp)



Je komt dan op de inlogpagina, waar je het wachtwoord moet invoeren dat je in de vorige stap hebt gekopieerd om de Interface te ontgrendelen.



![Interface de connexion complète à ThunderHub](assets/fr/04.webp)



Umbrel zorgt ervoor dat ThunderHub op de achtergrond wordt voorzien van LND verbindingsinformatie (TLS certificaat, administratie macaroon, etc.), zodat u geen extra configuratie hoeft te doen. In slechts een paar klikken hebt u ThunderHub aan de gang op uw Umbrel knooppunt.



### Handmatige installatie (zelf gehost, exclusief Umbrel)



Voor gebruikers buiten Umbrel (bijvoorbeeld op een persoonlijke server, een Raspberry Pi met RaspiBlitz of een *stand-alone* installatie), vereist de installatie van ThunderHub een paar extra stappen. Hieronder beschrijven we de installatie vanaf broncode en de configuratie, volgens de [officiële ThunderHub documentatie](https://docs.thunderhub.io).



#### Installatie



**vereisten:** Zorg ervoor dat uw systeem voldoet aan de minimale vereisten volgens [documentatie setup] (https://docs.thunderhub.io/setup):




- **Node.js** versie 18 of hoger
- **npm** geïnstalleerd
- Toegang tot LND authenticatiebestanden :
  - LND TLS-certificaat (`tls.cert`)
  - LND administratiemacaron (`admin.macaroon`)
  - LND gRPC service Address (hostnaam:poort) (standaard `127.0.0.1:10009` lokaal)



**1. ThunderHub code ophalen:** Kloon de GitHub repository van het project zoals beschreven in de [installatie documentatie](https://docs.thunderhub.io/installation):



```bash
git clone https://github.com/apotdevin/thunderhub.git
cd thunderhub
```



**2. Installeer de afhankelijkheden en bouw de applicatie:**



```bash
npm install
npm run build
```



Deze commando's installeren alle benodigde modules en compileren vervolgens de applicatie (ThunderHub is geschreven in TypeScript/React).



**3. Later bijwerken:** ThunderHub biedt verschillende methoden voor toekomstige updates:



```bash
# Méthode rapide
npm run update

# Ou méthode manuelle
git pull
npm install
npm run build
```



#### Configuratie (instelling)



**1. Hoofdconfiguratiebestand:** Maak een `.env.local` bestand aan in de root van de ThunderHub map om de configuratie aan te passen (dit voorkomt dat uw instellingen worden overschreven tijdens updates). Hoofdvariabelen zoals in [setup documentatie](https://docs.thunderhub.io/setup):



```bash
# -----------
# Server Configs
# -----------
LOG_LEVEL='info' # 'error' | 'warn' | 'info' | 'http' | 'verbose' | 'debug' | 'silly'
PORT=3000
NODE_ENV=production

# -----------
# Interface Configs
# -----------
THEME='dark' # 'dark' | 'light' | 'night'
CURRENCY='sat' # 'sat' | 'btc' | 'fiat'

# -----------
# Privacy Configs
# -----------
FETCH_PRICES=true # Récupération des prix BTC/fiat depuis Blockchain.com
FETCH_FEES=true # Récupération des frais on-chain depuis Earn.com
DISABLE_LINKS=false # Liens vers 1ml.com et Blockchain.com
NO_VERSION_CHECK=false # Vérification de version depuis GitHub

# -----------
# TOR (optionnel)
# -----------
TOR_PROXY_SERVER='socks://127.0.0.1:9050' # Pour proxifier via TOR

# -----------
# Account Configs
# -----------
ACCOUNT_CONFIG_PATH='/chemin/vers/thubConfig.yaml' # Fichier de comptes
```



**2. Serveraccounts configureren:** Maak het YAML-bestand aan dat is opgegeven in `ACCOUNT_CONFIG_PATH` :



```yaml
masterPassword: 'votre_mot_de_passe_principal'
accounts:
- name: 'Mon Nœud LND'
serverUrl: '127.0.0.1:10009'
macaroonPath: '/home/user/.lnd/data/chain/bitcoin/mainnet/admin.macaroon'
certificatePath: '/home/user/.lnd/tls.cert'
password: 'mot_de_passe_compte_specifique'
# Optionnel : compte avec macaroon en hexadécimal
- name: 'Nœud Distant'
serverUrl: 'ip.distante:10009'
macaroon: '0201056c6e6402f8...' # Macaroon en HEX ou Base64
certificate: '0202045c7365...' # Certificat en HEX ou Base64
```



**3. Toegang op afstand:** Om verbinding te maken met een LND knooppunt op afstand, voeg je aan `LND.conf` toe:



```bash
# Option 1 : accès par IP
tlsextraip=<ip-externe-accessible>
rpclisten=0.0.0.0:10009

# Option 2 : accès par domaine
tlsextradomain=<domaine-externe-accessible>
rpclisten=0.0.0.0:10009
```



**4. Beveiliging:** Bij de eerste keer opstarten verbergt ThunderHub **automatisch** het `masterPassword` en alle accountwachtwoorden in het YAML-bestand, om te voorkomen dat wachtwoorden in duidelijke tekst op de server staan.



**5. ThunderHub starten:**



```bash
npm start
```



Standaard luistert de server op poort 3000. Ga naar `http://localhost:3000` (of `http://ip-serveur:3000` vanaf het lokale netwerk).



**6. Docker-alternatief:** ThunderHub biedt officiële Docker-images:



```bash
# Image standard
docker pull apotdevin/thunderhub:latest
docker run --rm -it -p 3000:3000/tcp apotdevin/thunderhub:latest

# Image avec base path /thub
docker pull apotdevin/thunderhub:base-v0.11.1
```



De ThunderHub aanmeldpagina verschijnt. Selecteer de geconfigureerde account en voer het wachtwoord in om toegang te krijgen tot het dashboard.



**Installatie op andere distributies:** Voorverpakte node distributies (RaspiBlitz, MyNode, Start9, etc.) bieden over het algemeen eigen ThunderHub ondersteuning via hun respectievelijke beheerinterfaces.



**Voor meer informatie:** Raadpleeg de volledige officiële documentatie :




- **Installatie:** [docs.thunderhub.io/installatie](https://docs.thunderhub.io/installation)
- **Configuratie:** [docs.thunderhub.io/setup](https://docs.thunderhub.io/setup)



Deze bronnen beschrijven geavanceerde opties zoals SSO-accounts, versleutelde macarons, TOR-configuratie en nog veel meer.



Zodra ThunderHub geïnstalleerd en toegankelijk is, ben je klaar om alle functies te gebruiken. In het volgende gedeelte bekijken we de Interface ThunderHub en de verschillende tabbladen, om u door het gebruik ervan te leiden.



## Presentatie Interface



Interface ThunderHub is opgebouwd rond een hoofdmenu (meestal weergegeven in de linkerkolom) met verschillende hoofdsecties. Elk onderdeel komt overeen met een aspect van het beheren van je Lightning-node. Laten we ze een voor een doorlopen:





- **Home** - tabblad Home met een algemeen dashboard (overzicht van je knooppunt en snelle acties).
- **Dashboard** - Aanpasbaar dashboard met widgets en geavanceerde statistieken.
- **Peers** - Bliksem peer management (verbindingen met andere nodes).
- **Kanalen** - Gedetailleerd beheer van Lightning-kanalen.
- **Rebalance** - tool voor kanaalbalancering (circulaire betalingen).
- **Transacties** - Bliksem betalingsgeschiedenis (LN transacties).
- **Forwards** - Routingstatistieken (betalingen doorgegeven door je knooppunt).
- **Chain** - Node's On-Chain Wallet (On-Chain BTC: UTXO's, transacties).
- **Amboss** - Integratie met Amboss (nodebewaking, back-ups, enz.).
- **Tools** - Diverse tools (back-ups, ondertekende berichten, macarons, rapporten, etc.).
- **Wissel** - On-Chain/Lightning wisselfuncties via Boltz.
- **Stats** - Geavanceerde statistieken en statistieken over knooppuntprestaties.



*(Opmerking: Afhankelijk van de ThunderHub versie kunnen sommige secties iets andere kopjes of extra functies hebben, maar de algemene principes blijven hetzelfde)*



### Home (Algemeen bedieningspaneel)



Het tabblad **Home** van ThunderHub is de startpagina die verschijnt nadat u bent ingelogd. Het bevat het **Algemene Dashboard**, dat een **globaal overzicht** biedt van de status van uw Lightning knooppunt en **snelle acties** voorstelt voor routinematige bewerkingen. Dit is wat je er meestal aantreft:



![Tableau de bord principal de ThunderHub](assets/fr/05.webp)





- **Saldi en capaciteiten:** Bovenaan de pagina toont ThunderHub je beschikbare saldi. Hier zie je meestal het On-Chain saldo (Bitcoin On-Chain in de Wallet van het knooppunt, gesymboliseerd door een Anchor ⚓) en het Lightning saldo (de capaciteiten van je kanalen, gesymboliseerd door een Bolt ⚡ bliksemschicht). Dit geeft je direct een idee van de fondsen die je hebt in On-Chain en Lightning. Als je meerdere accounts of kanalen hebt, controleer dan of je op de juiste zit (bijvoorbeeld Mainnet vs Testnet).





- **Belangrijkste statistieken:** Het dashboard kan een aantal globale statistieken voor je knooppunt laten zien - bijvoorbeeld het aantal open kanalen, het aantal verbonden peers, verdiende routing fees (indien van toepassing), enz. Het is een samenvatting van de recente activiteit en gezondheid van het knooppunt.





- **Snelle acties:** Het dashboard bevat knoppen om de meest voorkomende taken snel uit te voeren, zonder door menu's te hoeven navigeren. Deze snelle acties omvatten :





- **Ghost**: Stel een aangepaste Lightning Address in via Amboss.
- **Doneren**: Doe een donatie via Lightning.
- **Inloggen/Ga naar**: Maak verbinding met uw Amboss account (Quick Connect) en ga direct naar Amboss.space om de informatie van uw node te bekijken.
- **Address**: Voer een Lightning Address in om een betaling te doen.
- **Openen**: Open een nieuw Lightning-kanaal. Klikken opent een formulier voor het invoeren van de URI van het externe knooppunt waarnaar de chatroom moet worden geopend, het bedrag en, indien van toepassing, de maximale On-Chain-vergoeding die moet worden gebruikt.
- **Decode**: Decodeer een Lightning Invoice of LNURL om details te bekijken voor betaling.
- **LNURL**: LNURL's verwerken voor Lightning-betalingen of -opnames.
- **Inloggen bij LnMarkets**: Log in bij LnMarkets om te handelen.



Met deze snelle acties kun je de meest voorkomende handelingen direct vanaf de startpagina uitvoeren, zonder door de verschillende tabbladen van Interface te hoeven navigeren.



In het kort geeft het ThunderHub dashboard je een **snelle blik** op je node en kun je de meest voorkomende handelingen (verzenden/ontvangen, een kanaal openen) met één klik uitvoeren. Het is het ideale startpunt voor dagelijks beheer.



### Dashboard



Het **Dashboard** gedeelte staat los van het tabblad Home en biedt een geavanceerder, aanpasbaar dashboard. Met dit gedeelte kun je een aangepaste weergave maken met specifieke widgets die voldoen aan jouw behoeften als knooppuntbeheerder.





- **Aanpasbare widgets:** In tegenstelling tot de startpagina, die een vaste lay-out heeft, kun je in het Dashboard precies kiezen welke Elements je wilt weergeven en hoe je ze wilt organiseren.



![Dashboard sans widgets activés](assets/fr/06.webp)



Als er geen widgets zijn ingeschakeld, zie je een bericht "Geen widgets ingeschakeld!" met een knop "Instellingen" om toegang te krijgen tot de aanpassingsparameters.



![Paramètres des widgets du Dashboard](assets/fr/07.webp)



In de instellingen kun je kiezen uit een groot aantal widgets die zijn onderverdeeld in categorieën: "Lightning - Info", "Lightning - Tabel", "Lightning - Grafiek", enzovoort. Elke widget kan afzonderlijk worden geactiveerd of gedeactiveerd met de knoppen "Weergeven/Verbergen".



![Bas de la page des paramètres](assets/fr/08.webp)



Onderaan de instellingen vind je de knop "Naar dashboard" om terug te keren naar het dashboard en de knop "Widgets resetten" om de standaardweergave te resetten.



![Dashboard personnalisé avec widgets](assets/fr/09.webp)



Eenmaal geconfigureerd kan je dashboard verschillende grafieken en statistieken weergeven: Lightning betalingsgrafieken, aantal uitgegeven facturen, statistieken over vooruitbetalingen, gedetailleerde saldi, enz.





- **Geavanceerde statistieken:** Krijg toegang tot meer gedetailleerde statistieken over de prestaties van je node, met grafieken en realtime gegevens.





- **Configureerbaar overzicht:** Pas het display aan je wensen aan, of je nu een gewone gebruiker bent of een professionele operator die meerdere routingkanalen beheert.





- **Modulaire Interface:** Voeg naar behoefte widgets toe of verwijder ze: voorwaartse grafieken, liquiditeitsmetriek, node gezondheidswaarschuwingen, enz.



Dit gedeelte is vooral handig voor gevorderde gebruikers die specifieke statistieken willen controleren of een meer technisch overzicht van hun Lightning-knooppunt willen krijgen. Het is een aanvulling op het Home-gedeelte en biedt meer flexibiliteit en controle over de manier waarop informatie wordt weergegeven.



### Peers



De **Peers** sectie toont alle Lightning nodes die op dit moment verbonden zijn met de jouwe als peers. Een **peer** is een directe node-naar-node verbinding op de Lightning Network. Uw knooppunt kan verbonden zijn met peers, zelfs zonder een open kanaal (bijvoorbeeld alleen om Exchange roddelinformatie over het netwerk te geven), of natuurlijk impliceert elk open kanaal automatisch een verbonden peer.



![Vue de l'onglet Peers avec les pairs connectés](assets/fr/10.webp)



Op het tabblad Peers zie je :





- **Informatiekolommen:** De Interface toont nuttige details zoals synchronisatiestatus, verbindingstype (clearnet of Tor), ping, ontvangen/verzonden satoshi's en volume van de uitgewisselde gegevens.
- Een peer toevoegen: Met ThunderHub kun je handmatig verbinding maken met een nieuwe peer via de **"Add"** knop in de rechterbovenhoek. Je moet de URI van het knooppunt invoeren (formaat `<public_key>@<socket>`). Eenmaal gevalideerd, stuurt ThunderHub het bijbehorende `lncli connect` commando. Als het knooppunt online en toegankelijk is, wordt het toegevoegd aan je lijst met peers.



### Kanalen



Het tabblad **Kanalen** is het hart van het kanaalbeheer van Lightning. Het is waarschijnlijk de sectie die je het vaakst zult raadplegen. Het toont **alle Lightning-kanalen** met hun details, en stelt je in staat om beheeracties uit te voeren op deze kanalen.



![Vue d'ensemble des channels ouverts](assets/fr/11.webp)



Dit is wat je kunt vinden op de Kanalen-pagina:





- **Kanaallijstweergave:** Elk open (of openend/sluitend) kanaal wordt weergegeven, meestal met de alias van het externe knooppunt, de totale kanaalcapaciteit en een gekleurde balk die de verdeling van lokale vs. externe liquiditeit illustreert. ThunderHub gebruikt een kleurcode (vaak blauw/Green) of percentage om de kanaalbalans aan te geven: bijvoorbeeld blauw voor het lokale aandeel, Green voor het aandeel op afstand. Als een kanaal perfect in balans is (50/50), zal de balk de helft van elke kleur zijn. Zo kun je in één oogopslag zien welke kanalen uit balans zijn (helemaal blauw = bijna helemaal lokaal, helemaal Green = bijna helemaal op afstand).





- **Informatiekolommen:** De Interface toont gedetailleerde kolommen waaronder Status, Beschikbare acties, Peerinfo, Kanaal-ID, Capaciteit, Activiteit, Kosten en Saldo met grafische liquiditeitsweergave.





- **Weergaveconfiguratie:** Met een tandwiel in de rechterbovenhoek kun je de kanaalweergave aan je voorkeuren aanpassen.





- **Status:** Je ziet ook statusindicatoren - bijvoorbeeld `Actief` (het kanaal is open en operationeel), `Offline` (de verbinding met de peer is verbroken, dus het kanaal is tijdelijk onbruikbaar), `Pending` (voor openingen of sluitingen die wachten op On-Chain bevestiging).





- **Acties op een kanaal:** Voor elk kanaal biedt ThunderHub actieknoppen (vaak in de vorm van pictogrammen):



![Actions de gestion des canaux - Modifier et Fermer](assets/fr/12.webp)





- **Vergoedingen bewerken:** Met Interface "Kanaalbeleid bijwerken" kun je alle kanaalparameters aanpassen: Base Fee, Fee Rate (in ppm), CLTV Delta, Max HTLC en Min HTLC. Hierdoor kunt u uw vergoedingenbeleid individueel per kanaal aanpassen, met als doel routeringsverkeer aan te trekken (of te ontmoedigen). *(Opmerking: ThunderHub is geen vervanging voor een automatische fee management tool, maar voor handmatige aanpassing is het zeer effectief)*
- Kanaal sluiten (*Sluiten*): Het Interface "Close Channel" geeft u de keuze tussen een **coöperatieve afsluiting** (standaard) of een **geforceerde afsluiting** (*Force Close*) door de kosten te definiëren (in Sats/vByte). **Belangrijk:** geef altijd de voorkeur aan een coöperatieve afsluiting wanneer mogelijk, om On-Chain vertragingen in de afhandeling en hogere kosten te voorkomen. ThunderHub zal je vertellen of de peer online is (coöperatief mogelijk) of niet. In het geval van een geforceerde sluiting, moet je bevestigen, want dit is onomkeerbaar en zal een vegende transactie met een tijdslot veroorzaken (over het algemeen 144 blokken of ~1 dag op Bitcoin Mainnet).
- Een nieuwe chatroom openen: Om een nieuwe chatroom te openen, klik je op het tandwiel rechtsboven op de chatroompagina en selecteer je "Openen". Je kunt dan een chatroom starten naar een nieuwe of bestaande leeftijdsgenoot. Het voordeel van het gebruik van deze pagina is dat je een lijst van je bestaande chatrooms voor je hebt, wat je kan helpen beslissen waar je een nieuwe chatroom wilt openen.



Kortom, de Kanalen sectie geeft je **fijne controle over elk kanaal**. Hier bepaal je de liquiditeitstoewijzing, beslis je welke kanalen je wilt behouden of sluiten en stel je de routingparameters per kanaal in. ThunderHub biedt een duidelijke Interface voor deze cruciale operaties voor knooppuntbeheer.



### Herbalanceren



Het tabblad **Rebalans** is gewijd aan het **kanalen balanceren**. Balanceren (of *herbalanceren*) houdt in dat je de verdeling van fondsen tussen je uitgaande en inkomende kanalen aanpast, door een **circulaire betaling** te doen van een van je kanalen naar een ander kanaal, via de Lightning Network. Hierdoor kun je, zonder nieuwe fondsen in te brengen, liquiditeit verschuiven van een kanaal dat te vol is naar een kanaal dat te leeg is. Hierdoor kun je, zonder nieuwe fondsen in te brengen, liquiditeit verschuiven van een kanaal dat te vol is naar een kanaal dat te leeg is, waardoor je kanalen nuttiger worden (een gebalanceerd kanaal kan zowel betalingen verzenden als ontvangen).



![Interface de rebalance des canaux](assets/fr/13.webp)



ThunderHub maakt deze handeling, die anders vervelend zou zijn op de opdrachtregel, een stuk eenvoudiger. Hier lees je hoe je de Rebalance sectie gebruikt:





- **Oorspronkelijke kanaalweergave:** Bij het openen van Rebalance toont ThunderHub een lijst van je kanalen, met een balansindicator voor elk kanaal (vergelijkbaar met de indicator op de Kanalen pagina). Je kunt meteen zien welke kanalen uit balans zijn. ThunderHub kan kanalen sorteren in volgorde van toenemende balans, zodat de kanalen met de meeste onbalans bovenaan de lijst staan (0.0 betekent volledig lokaal of op afstand).





- **Peer selectie:** De Interface maakt het eenvoudig om uitgaande en inkomende peers te selecteren voor rebalancing.





- **Parameterinstellingen:** U kunt :
  - De **maximale vergoeding** (in Sats en ppm) die je bereid bent te betalen
  - Het **bedrag om opnieuw in evenwicht te brengen** met de optie "Vast" of "Doel
- Te vermijden **knooppunten** bij het routeren
- **Maximale proeftijd** voor routebepaling





- Selecteer **bron kanaal**: Selecteer eerst het **uitgaande (bron)** kanaal, d.w.z. het kanaal waarvan je te veel lokale liquiditeit hebt om te verplaatsen. In de praktijk is dit een kanaal waar je lokale aandeel hoog is (> 50%). Stel je een A-kanaal voor met 1.000.000 Satss, waarvan er 900.000 lokaal zijn - een goede kandidaat om Satss naar elders te sturen. Door op dit A-kanaal te klikken als "uitgaand", markeert ThunderHub het als een bron.





- Kies **doelkanaal**: Kies vervolgens het **inkomende (doel)** kanaal dat liquiditeit moet ontvangen. Meestal zal dit een kanaal zijn waar het andersom is - de meeste fondsen zijn aan de lage kant (bijv. slechts 100.000 lokale Satss van de 1.000.000). ThunderHub zal, zodra het bronkanaal is geselecteerd, de andere kanalen in omgekeerde volgorde sorteren (afnemende balans) om te helpen bij het identificeren van de meest complementaire kanalen. Selecteer een B-kanaal dat ruimte heeft aan de lokale kant. ThunderHub geeft dan duidelijk weer welke twee kanalen zijn geselecteerd (bron A en doel B).





- **Tariefbedrag en tolerantie instellen:** Via een formulier kun je :





  - De **hoeveelheid** die opnieuw gebalanceerd moet worden (in Sats). Vaak kiezen we een hoeveelheid die gelijk is aan wat beide kanalen in balans zou brengen bij 50/50. ThunderHub kan bijvoorbeeld de helft van de overcapaciteit van het bronkanaal voorvullen. ThunderHub kan bijvoorbeeld de helft van de overtollige capaciteit van het bronkanaal voorvullen.
  - De **maximale vergoeding** die je bereid bent te betalen voor deze bewerking (optioneel). Deze vergoeding wordt uitgedrukt in Sats (totale kosten van circulaire routering). Als je dit leeg laat, zal ThunderHub zoeken naar een pad ongeacht de kosten, wat over het algemeen niet aan te raden is (het is beter om een limiet in te stellen, bijv. 10 Sats voor een kleine herbalancering, of een maximum ppm).





- **Route zoeken:** Klik op de knop om een route te vinden. ThunderHub bevraagt LND om een route te berekenen van uw bronkanaal door het netwerk naar uw eigen doelkanaal. Als er een mogelijke route wordt gevonden die voldoet aan uw tariefcriteria, wordt deze weergegeven met details van de hops en de tariefkosten. Het kan bijvoorbeeld aangeven dat het een 3-hop pad heeft gevonden met in totaal 2 Sats aan kosten.





- Start rebalance: Als u tevreden bent met de voorgestelde route, klikt u op **Balanceer kanaal**. ThunderHub zal dan de circulaire betaling starten via LND. Als de betaling succesvol is, zie je een melding van het succes en worden de saldi van kanaal A en B in realtime aangepast. ThunderHub zal de balansindicator voor deze kanalen bijwerken (idealiter zullen ze groener zijn dan voorheen, wat duidt op een betere balans).





- **Aanpassingen en iteraties:** Als er bij de eerste poging geen route wordt gevonden (of als deze te duur is), kun je de parameters aanpassen :





  - Probeer een kleinere hoeveelheid (soms wordt een gedeeltelijke herbalancering doorgevoerd terwijl een grote hoeveelheid mislukt).
  - Verhoog de maximale vergoeding geleidelijk, maar pas op dat je niet meer betaalt dan het waard is.
  - Gebruik de knop **Een andere route verkrijgen**, indien beschikbaar, om een alternatief te proberen.
  - Probeer een ander paar kanalen als het echt gaat knellen.



ThunderHub maakt het proces zeer **intuïtief en visueel**. In slechts 4 stappen (selecteer uitgaand kanaal, selecteer inkomend kanaal, bedrag, valideren) kunt u doen wat vroeger complexe handmatige opdrachten vereiste. De tool is van onschatbare waarde voor het onderhouden van een goed gebalanceerd knooppunt, het verbeteren van je routingprestaties en -ervaring (eenvoudiger betalingen verzenden en ontvangen via al je kanalen).



Merk tenslotte op dat een rebalance routeringskosten verbruikt (betaald aan tussenliggende knooppunten), dus het is een **investering** om je knooppunt vloeiender te maken. Gebruik het verstandig, bijvoorbeeld om een kanaal te ondersteunen naar een service die u vaak gebruikt (inkomende liquiditeit) of om een groot routeringskanaal in balans te brengen. Met ThunderHub kunt u dit **simpel en efficiënt** doen.



### Transacties



De **Transacties** sectie in ThunderHub komt overeen met de **Lightning** transactiegeschiedenis van uw node, dat wil zeggen betalingen en facturen die betaald of ontvangen zijn via de kanalen. Het is een soort rekeningoverzicht voor uw LN activiteiten.



![Historique des transactions Lightning](assets/fr/14.webp)



In dit tabblad vindt u :





- **Invoice grafiek:** In de rechterbovenhoek toont een grafiek de ontwikkeling van de ontvangen facturen in de loop van de tijd, zodat je de activiteit van je knooppunt kunt visualiseren.





- Een chronologische lijst van alle Lightning-transacties die *vanaf* of *naar* je knooppunt zijn gemaakt. Elk item kan :





  - Type bewerking: **verzonden betaling** (uitgaande betaling) of **ontvangen betaling** (inkomend, via een betaalde Invoice).
  - Het bedrag in Sats.
  - Datum/tijd.
  - Betalings-ID (Hash of RHash pre-image) of opmerking (als je een memo hebt toegevoegd aan Invoice).
  - Status: **voltooid**, of mogelijk **in behandeling**/* mislukt* (bijvoorbeeld een betaling die nog moet worden afgehandeld, maar over het algemeen verwerkt LND dit snel, dus er is hier weinig "in behandeling" vergeleken met On-Chain transacties).



Kortom, het gedeelte Transacties dient als uw **LN activiteitenlogboek**. Het is erg handig om te controleren of een betaling is gelukt, hoeveel kosten het heeft gekost of om de geschiedenis van je Lightning-uitwisselingen te volgen. In combinatie met het gedeelte Forwards (dat hierna wordt beschreven) heb je een volledig overzicht van het geld dat door je knooppunt is gepasseerd.



### Voorwaartsen



De **Forwards** tab is gewijd aan de **routing** activiteit van je node, d.w.z. betalingen die **doorgaan** via je kanalen (wanneer je optreedt als een tussenliggend knooppunt op de Lightning Network). Als u uw node als routeringsnode gebruikt, is dit een belangrijk onderdeel om uw prestaties bij te houden.



![Statistiques de routage Lightning](assets/fr/15.webp)



In Forwards presenteert ThunderHub :





- **Filters en weergaveopties:** Rechtsboven kun je met filters gegevens sorteren op dag/week/maand/jaar en kiezen tussen grafische weergave of weergave in tabelvorm.





- **Activiteitsbericht:** Als er geen routering is uitgevoerd tijdens de geselecteerde periode, geeft de Interface "No forwards for this period" weer, zoals in dit voorbeeld.





- Een **tabel met recente doorsturen**: elk item komt overeen met een betaling die **doorgestuurd** is via je knooppunt. Voor elk doorsturen zien we over het algemeen :





  - Timestamp,
  - de gerouteerde hoeveelheid (in Sats),
  - de **vergoeding die is verdiend** op dit doorsturen (in Sats is dit het verschil tussen wat je hebt ontvangen op het inkomende kanaal en verzonden op het uitgaande kanaal),
  - de gebruikte inkomende en uitgaande kanalen (vaak geïdentificeerd door de peer alias of kanaal ID).
  - status (normaal gesproken *voltooid*, of mislukt als een doorsturing onderweg is mislukt).





- **Samengevoegde statistieken**: ThunderHub berekent en toont bovenaan de pagina totalen en statistieken over een bepaalde periode (bijv. de laatste 24 uur, of 7 dagen, etc., soms instelbaar).



Kortom, de sectie Forwards biedt een **real-time overzicht van de routeringsactiviteit van je Lightning-knooppunt**. In combinatie met de secties Kanalen en Rebalance vormt dit een compleet pakket om je knooppunt te optimaliseren: Kanalen/Rebalans voor liquiditeit, Forwards voor het observeren van resultaten (stromen en winsten).



### Ketting



Het **Keten** gedeelte komt overeen met het Bitcoin On-Chain Wallet beheer van je LND knooppunt. Met deze Interface kun je Bitcoin fondsen bekijken en beheren, die worden gebruikt om kanalen te openen of fondsen te ontvangen van gesloten kanalen.



![Gestion du portefeuille on-chain](assets/fr/16.webp)



In Chain vindt u :





- Balans On-Chain: Toont het totale BTC-saldo beschikbaar in Wallet LND.





- **Lijst van UTXO's:** Bekijk alle onbestede uitgaven (UTXO) met bedrag, bevestigingen, Address en formaat voor elke uitgave.





- **Transactiegeschiedenis:** Gedetailleerde tabel van alle Bitcoin transacties met type (in/uit), datum, bedrag, kosten, bevestigingen, inclusieblok, adressen en txid.



### Amboss



ThunderHub integreert met het **Amboss** platform (amboss.space), dat gedetailleerde informatie biedt over Lightning nodes, een liquiditeitenmarktplaats en handige functies zoals versleutelde kanaalback-up en beschikbaarheidsbewaking.



![Intégration Amboss avec ses options](assets/fr/17.webp)



In ThunderHub kun je in het Amboss gedeelte je node **linken** aan je Amboss account:





- **Ghost Address:** Zet een **persoonlijke Lightning Address** op voor je node, om inkomende betalingen te vergemakkelijken.





- Automatische kanaalback-ups:** Vlaggenschipfunctie voor versleutelde kanaalback-ups** (SCB-bestanden) op Amboss. Activeer **Amboss Auto Backup = Ja** in de instellingen om automatisch versleutelde back-upupdates te verzenden telkens wanneer u van kanaal verandert. In het geval van een storing kunt u uw fondsen herstellen dankzij deze externe back-up.





- **Health Checks:** Activeer **Amboss Healthcheck = Yes** om je node regelmatig pings te laten sturen naar Amboss. Je ontvangt waarschuwingen als je node offline lijkt te zijn.





- **Andere functies:** Automatische balans push, **Magma/Hydro** integratie (liquiditeitenmarktplaats) en toegang tot gedetailleerde prestatiestatistieken.



Amboss integratie voegt een essentiële **beveiliging Layer** toe met automatische externe back-up en beschikbaarheidsbewaking, direct toegankelijk vanuit ThunderHub.



### Gereedschap



De **Tools** sectie groepeert verschillende geavanceerde gereedschappen voor het beheren van je node. Hier zijn de belangrijkste Elements:



![Interface des outils disponibles](assets/fr/18.webp)





- **Back-ups:** Beheer handmatig uw kanaalback-ups (SCB). ThunderHub laat je **het complete back-up bestand** van je kanalen downloaden (optie "Back-up van alle kanalen -> Downloaden"). Bewaar dit `kanaal-all.bak` bestand op een veilige plek - het is essentieel voor het herstellen van je fondsen in het geval van een crash. Je kunt ook een back-upbestand **importeren** wanneer je een node opnieuw installeert.





- **Boekhouding:** Exporttool voor financiële rapporten, inclusief verdiende/betaalde vergoedingen en gerouteerde volumes over een bepaalde periode.
- **Ondertekende berichten:** Teken of verifieer berichten met uw knooppunt om Ownership van uw Lightning-knooppunt aan te tonen via een cryptografische handtekening.
- Macarons (Bakkerijgedeelte):** Beheer LND** macarons om aangepaste toegang te creëren. In de Interface "Bakkerij" kun je elke toestemming precies selecteren: "Peers toevoegen of verwijderen", "Ketenadressen aanmaken", "Facturen aanmaken", "Macarons aanmaken", "Sleutels afleiden", "Toegangssleutels ophalen", "Kettingtransacties ophalen", "Facturen ophalen", "Wallet-info ophalen", "Get Payments", "Get Peers", "Pay Invoices", "Revoke Access Ids", "Send to Chain Addresses", "Sign bytes", "Sign Messages", "Stop daemon", "Verify bytes signature", "Verify messages", enzovoort. Elke toestemming kan afzonderlijk worden geactiveerd met de knoppen "Ja/Nee" om een macaron op maat te maken.
- **Systeeminformatie:** Weergave van Wallet versie en geactiveerde RPC's.



Kortom, de Tools sectie brengt geavanceerde beheerfuncties - back-ups, boekhouding, beveiliging en toegangsbeheer - samen in één Interface.



### Wissel



Met het tabblad **Swap** van ThunderHub kun je Lightning-satoshis omwisselen naar Bitcoin On-Chain via de Boltz-service. Deze functie is handig voor het "dumpen" van overtollige Lightning liquiditeit naar het kanaal zonder een kanaal te sluiten.



![Interface de swap via Boltz](assets/fr/19.webp)



Het proces is eenvoudig:





- **Bedrag**: Definieer het in te ruilen bedrag
- **Address**: Bitcoin ontvangst Address invoeren
- **Uitvoering**: ThunderHub communiceert met Boltz om automatisch de Exchange te verwerken



**Voordelen:**




- Niet-bewarende dienst (geen contante bewaring)
- Behoud uw bestaande kanalen
- Gebruiksvriendelijke geïntegreerde Interface



Boltz rekent een kleine commissie en jij betaalt de standaard Bitcoin transactiekosten. ThunderHub toont alle kosten voor bevestiging.



### Stats



De sectie **Stats** van ThunderHub biedt **geavanceerde statistieken** over uw Lightning-node om de prestaties te analyseren en de routering te optimaliseren.



![Statistiques du nœud via Amboss](assets/fr/20.webp)



Dit gedeelte is essentieel voor het optimaliseren van je kosten, het identificeren van succesvolle kanalen en het plannen van de uitbreiding van je knooppunt.



## Conclusie



**ThunderHub** heeft zich gevestigd als de essentiële tool voor eenvoudig beheer van een Lightning **LND** knooppunt. Deze moderne Interface biedt alle essentiële functies: kanaalbeheer, betalingen, monitoring, met geavanceerde functies zoals geautomatiseerde herbalancering en Amboss-integratie.



**Belangrijkste voordelen:**




- Interface gestroomlijnd en intuïtief
- Krachtige tools (herbalanceren, Boltz-swaps, automatische back-ups)
- Compatibel met Umbrel, Voltage, RaspiBlitz en andere distributies



ThunderHub democratiseert geavanceerd beheer van Lightning-knooppunten en maakt toegankelijk wat voorheen complexe technische commando's vereiste. Of u nu een beginner of een ervaren operator bent, met ThunderHub kunt u uw Lightning-node efficiënt beheren via een moderne, uitgebreide Interface.



## Bronnen



**Officiële links:**




- **Officiële website:** [thunderhub.io](https://thunderhub.io)
- **Documentatie:** [docs.thunderhub.io](https://docs.thunderhub.io)
- GitHub broncode: **[github.com/apotdevin/thunderhub](https://github.com/apotdevin/thunderhub)**