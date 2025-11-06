---
name: LNbits

description: Boekhoudplatform voor verkopers
---

![presentation](assets/lnbits-intro.webp)

# Boekhoudsysteem


LNbits zit boordevol tools om je inkomende en uitgaande geldstromen te beheren en te kanaliseren, je webwinkel aan te sluiten of zelfs apparaten zoals een Hardware Wallet of een geldautomaat die je zelf hebt gebouwd. Gebruikerstypes zijn onder andere:


- Wallet eigenaren die LNbits willen gebruiken als een Interface voor hun geldbeheer en de extra functies.
- Online en offline handelaren of dienstverleners die Bitcoin onchain en Lightning Network betalingen willen accepteren.
- Ontwikkelaars die Lightning Network toepassingen willen bouwen.
- Knooppuntbeheerders die hun knooppunt met het LNbits-systeem willen integreren voor boekhoudkundige doeleinden.
- Die hebben allemaal verschillende behoeften. We bouwen LNbits modulair op zodat elke gebruiker onze functies kan gebruiken op de manier die het beste bij hem past.


# Wallet manager


LNbits is een gratis en open-source boekhoudsysteem - geen knooppuntmanager. Kanaalbeheer is het domein van het Lightning knooppunt dat verbonden is met LNbits als een financieringsbron zoals LND of c-lightning. De Superuser of Admin Gebruikers in het LNbits systeem zijn verantwoordelijk voor het beheer van de algemene toegankelijkheid en configuratie van de boekhoudfuncties en interne uitbreidingen.


LNbits fungeert als een Interface tussen de gebruiker en het Lightning-knooppunt en biedt een eenvoudige, gebruiksvriendelijke manier om het betalingsnetwerk te beheren en ermee te communiceren.


Zie LNbits als een "wordpress modulair framework" voor je node. Een eenvoudig te beheren platform, gebaseerd op uitbreidingen die je kunt combineren voor talloze gebruikssituaties.


Zie LNbits als de software voor financieel beheer van je eigen bank. Je node biedt kanalen aan om via te betalen en LNbits breidt je node uit zodat je meer dan één bliksem Wallet kunt draaien waar je node mee wordt geleverd. Deze wallets hoeven niet noodzakelijk van jezelf te zijn. Laten we zeggen dat jij, als de LN node runner, al genoeg kanaalliquiditeit en fondsen hebt en nu wil je wat Bitcoin bankdiensten aanbieden aan je vrienden, familie, eigen winkel of andere reguliere handelaars.


Je biedt hen een eenvoudige manier om een "bankrekening" op jouw node te openen zonder toegang te hebben tot andere wallets op jouw node en tot al je node-liquiditeit, maar alleen tot hun deel. Jouw node (de bank) fungeert alleen als een transportprovider voor hun betalingen (in/uit).


OPMERKING: al het geld dat jouw "klanten" storten op hun LNbits bankrekeningen op jouw node, gaat rechtstreeks naar de LN kanalen van jouw node. Dat betekent dat JIJ de echte eigenaar van die fondsen bent. Je hebt een grote verantwoordelijkheid voor hun fondsen. Wees niet slecht en loop niet weg met het geld, wees niet slecht en reken hoge kosten. We willen de fiat banksters naaien, niet elkaar (Bitcoin gebruikers).


# Demoplatform


De demo kan worden gevonden op [https://legend.lnbits.com](https://legend.lnbits.com). Hij is volledig functioneel en kan gebruikt worden om de Lightning Network en mogelijkheden van LNbits en LNURL in het algemeen te leren kennen. Hoewel we je er niet van kunnen weerhouden, willen we je vragen om het niet te gebruiken voor je productie setup. Niet alleen werken we vaak aan de servers om nieuwe functies te testen, maar we willen je ook aanmoedigen om je eigen node en LNbits op een soevereine manier te draaien. Als je denkt dat het runnen van een node op dit moment te veel gevraagd is, kun je LNbits verbinden met een custodian funding service in de cloud zoals Opennode, Luna of Votage of met de Lightning Tipbot op Telegram om er maar een paar te noemen.


# LNbits flyer


Wil je wat basisinformatie overhandigen aan een handelaar of een bevriende bouwer? We zijn erg blij om onze eerste flyer aan te kondigen die iedereen kan gebruiken. Het formaat is een typisch flyerformaat met 6 pagina's (2 vouwen) en een breedte van 3508 en een hoogte van 2480px.


LNbits voor kooplieden: [EN](/assets/lnbits-merchants-en.pdf) | [DE](/assets/lnbits-merchants-de.pdf) | [ES](/assets/lnbits-merchants-es.pdf) | [IT](/assets/lnbits-merchants-it.pdf) | [PL](/assets/lnbits-merchants-pl.pdf)


LNbits voor bouwers: [EN](/assets/lnbits-builders-en.pdf) | [DE](/assets/lnbits-builders-de.pdf) | [ES](/assets/lnbits-builders-es.pdf) | [IT](/assets/lnbits-builders-it.pdf) | [PL](/assets/lnbits-builders-pl.pdf)


# Enkele basisprincipes


LNbits werkt op basis van het LNURL protocol wat betekent dat verzoeken geldig zijn in twee vormen: ofwel als https:// clearnet link (geen zelfondertekende certificaten toegestaan) of als http:// v2/v3 onion link. Om LNbits diensten aan te bieden zoals LNURLp/w QR codes of NFC kaarten, die in het wild gebruikt kunnen worden, moet je LNbits openstellen voor clearnet (https).


Voordat je LNbits installeert, moet je eerst de volgende algemene gidsen hebben gelezen en begrepen over wat LNbits is en welke mogelijkheden het voor je ontketent.



- [LND Gids](https://docs.lightning.engineering/) | LND installeren
- [LND Configuratievoorbeeld] (https://github.com/lightningnetwork/LND/blob/master/sample-LND.conf) | LND Instellingen
- [CLN gids](https://docs.corelightning.org/docs/installation) | CLN installeren
- [LUDs](https://github.com/lnurl/luds) LNURL Spec | [NIPs](https://github.com/nostr-protocol/nips) Nostr Spec
- [Voer een Watchtower uit (https://docs.lightning.engineering/lightning-network-tools/LND/Watchtower) | Zeer belangrijk!


Meer gedetailleerde gidsen over het gebruik van LNbits in specifieke gebruiksscenario's vindt u hier:



- [Aan de slag met LNbits](https://darthcoin.substack.com/p/getting-started-lnbits) | Substack-gids
- [ToDos voor uw veiligheid met LNbits](https://youtu.be/i5FQf96e6zg) | Youtube Video
- [Private Banken op Lightning Network](https://darthcoin.substack.com/p/Bitcoin-private-banks-over-lightning) | Substack gids
- [Bewaarportemonnees uitvoeren voor je vrienden & familie](https://darthcoin.substack.com/p/the-bank-of-lnbits) | Substack-gids
- [LNbits voor een klein restaurant / hotel](https://darthcoin.substack.com/p/lnbits-for-small-merchants) | Substack gids
- [LNbits Streamer copilot gebruiken](https://darthcoin.substack.com/p/lnbits-streamer-copilot) | Substack-gids
- [Start uw NOSTR-markt met LNbits](https://darthcoin.substack.com/p/lnbits-nostr-market) | Substack-gids
- [LNbits gebruiken voor schoolprojecten of festivalevenementen](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools) Substackgids



# LNbits installeren


## Basis installatiegids


LNbits kan op elke Linux OS-machine geïnstalleerd worden. Er is geen krachtige machine of server voor nodig, alleen voldoende RAM-geheugen en wat schijfruimte voor de database. Het kan afzonderlijk van een BTC/LN knooppunt (lokale pc of VPS op afstand) worden uitgevoerd of samen op dezelfde machine met het knooppunt of al geïnstalleerd in een bundel knooppuntsoftwaremachine.


Je kunt kiezen tussen de meest gebruikte pakketbeheerders zoals poetry en nix. Standaard gebruikt LNbits SQLite als database. Je kunt ook PostgreSQL gebruiken, wat wordt aanbevolen voor toepassingen met een hoge belasting. [Hier is een handleiding voor een basisinstallatie met poetry of nix](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md).


Voor iedereen die hier nieuw in is, vind je hier meer gedetailleerde stap-voor-stap handleidingen om je LNbits in specifieke omgevingen te laten werken:


- [LNbits op clearnet](https://ereignishorizont.xyz/lnbits-server/en/) door Axel
- [LNbits op een VPS](https://github.com/TrezorHannes/vps-lnbits) door Hannes
- [LNbits op cloudflare](https://www.nodeacademy.org/lnbits) door Leo


Je kunt ook een video vinden op de [dockerised Setup op een VPS met PostgreSQ, LightningTipBot als financieringsbron met nginx](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/).


[Meer installatiescenario's hier](https://darthcoin.substack.com/p/build-your-own-lnbits-app-server).


Raadpleeg voor bundelsoftware nodes hun specifieke documentatie over LNbits: [Citadel](https://runcitadel.space) | [Umbrel](https://umbrel.com) | [MyNode](https://mynodebtc.com) | [RaspiBlitz](https://raspiblitz.org/) | [RaspiBolt](https://raspibolt.org)


## LNbits SaaS


Als je niet zo technisch bent en je financieringsbron of je lnbits niet zelf wilt hosten, is er een [LNbits SaaS-versie](https://saas.lnbits.com) (Software-as-a-service) die je kunt gebruiken. Het is eigenlijk net als LNbits in een cloud, maar je kunt de financieringsbron (bijv. je Node, een LNbits Wallet, de LNtipbot, fakewallet enz.) en omgevingsvariabelen zelf definiëren - wat meestal niet het geval is bij andere cloud-oplossingen.


[Hier is een gedetailleerde handleiding hoe LNbits SaaS te gebruiken voor specifieke use cases] (https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools).


## Financieringsbronnen


LNbits is geen software voor knooppuntbeheer, maar een op LN gericht boekhoudsysteem bovenop een LND of CLN financieringsbron. Na de eerste installatie kun je je LNbits bezoeken op http://localhost:5000/.


Om de financieringsbron aan te passen ga je naar je super-user-URL en selecteer je een financieringsbron binnen "Server beheren" of bewerk je het .env bestand door `LNBITS_BACKEND_WALLET_CLASS` aan te passen naar de bron die je nodig hebt als je `adminUI=TRUE` in de `.env` instelt.


U vindt het .env-bestand in uw map lnbits/ of lnbits/apps/data door het commando uit te breiden om bestanden in uw map op te sommen met `ls -a`.


Het kan ook zijn dat je extra pakketten moet installeren of extra installatiestappen moet uitvoeren. Na een herstart is uw nieuwe installatie actief.


Welke financieringsbronnen kan ik gebruiken voor LNbits?


LNbits kan bovenop veel financieringsbronnen voor Lightning-netwerken draaien. Momenteel is er ondersteuning voor CoreLightning, LND, LNbits, LNPay, OpenNode, en er worden er regelmatig meer toegevoegd.

Het is belangrijk om een bron te kiezen met een goede liquiditeit en goede verbonden peers. Als je LNbits gebruikt voor publieke diensten, kunnen de betalingen van je gebruikers alleen maar goed stromen in beide richtingen.


Een backend Wallet (funding source) kan worden geconfigureerd met de volgende LNbits omgevingsvariabelen in het `.env` bestand of binnen je superuser account onder Manage-Server sectie.

Als je de .env-versie wilt gebruiken, kun je de parameters hier vinden:



### CoreLightning


- CLN
  - `LNBITS_BACKEND_WALLET_CLASS`: **CoreLightningWallet**
  - `CORELIGHTNING_RPC`: /bestand/pad/verlichting-RPC
- Vonk (c-bliksem)
  - `LNBITS_BACKEND_WALLET_CLASS`: **SparkWallet**
  - `SPARK_URL`: http://10.147.17.230:9737/RPC
   - `SPARK_TOKEN`: geheime_toegangssleutel

### Lightning Network Daemon


- LND (REST)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LndRestWallet**
  - `LND_REST_ENDPOINT`: http://10.147.17.230:8080/
  - `LND_REST_CERT`: /bestand/path/tls.cert
  - `LND_REST_MACAROON`: /file/path/admin.macaroon of Bech64/Hex
  - `LND_REST_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn
- LND (gRPC)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LndWallet**
  - lND_GRPC_ENDPOINT`: ip_adres
  - `LND_GRPC_PORT`: poort
  - `LND_GRPC_CERT`: /bestand/path/tls.cert
  - `LND_GRPC_MACAROON`: /file/path/admin.macaroon of Bech64/Hex

Je kunt in plaats daarvan ook een met AES versleutelde macaron (meer info) gebruiken met


  - `LND_GRPC_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn

Om je macaron te versleutelen, voer je `./venv/bin/python lnbits/wallets/macaroon/macaroon.py` uit.


### LNbits (een andere LNbits-instantie)



- LNbits instance gehost op een cloud server of je eigen server thuis
  - `LNBITS_BACKEND_WALLET_CLASS`: **LNbitsWallet**
  - `LNBITS_ENDPOINT`: https://lnbits.mydomain.com
  - `LNBITS_KEY`: my-lnbits-AdminKey
- LNbits Legend Demo Server (!! Gebruik deze NIET voor productie / commerciële doeleinden, alleen om te testen !!)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LNbitsWallet**
  - `LNBITS_ENDPOINT`: https://legend.lnbits.com
  - `LNBITS_KEY`: legend-lnbits-AdminKey

### Bliksem TipBot


Om je [Lightning Tipbot] (https://t.me/LightningTipBot) vanuit Telegram te verbinden, moet je de volgende parameter instellen:


  - `LNBITS_BACKEND_WALLET_CLASS`: **LnTipsWallet**
  - `LNBITS_ENDPOINT`: https://LN.tips
  - `LNBITS_KEY`: Om de sleutel te krijgen moet je eenmaal /api uitvoeren in een privéchat met de LightningTipbot op Telegram.


Bekijk ook deze tutorial over het installeren van [LNbits met LightningTipBot via vps] (https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/)


### IBEX HUB


Registreer [hier] (https://ibexpay.ibexmercado.com/onboard) en haal daar je sleutels/tokens vandaan, het eindpunt is https://ibexpay-api.ibexmercado.com.

Voor meer informatie zie [IBEX API-Documentatie](https://ibexpay-api.readme.io/reference/getting-started-with-your-api).


### LNPay

Om de Invoice listener te laten werken heb je een publiek toegankelijke URL in je LNbits en moet je een [LNPay webhook](https://dashboard.lnpay.co/webhook/) instellen die wijst naar `<je LNbits host>/Wallet/webhook` met de "Wallet ontvangen" gebeurtenis en geen geheim gegeven. De instelling `https://mylnbits/Wallet/webhook` zal de endpoint url zijn die op de hoogte wordt gebracht van een betaling.


  - `LNBITS_BACKEND_WALLET_CLASS`: **LNPayWallet**
  - `LNPAY_API_ENDPOINT`: https://api.lnpay.co/v1/
  - `LNPAY_API_KEY`: sak_apiKey
  - `LNPAY_WALLET_KEY`: waka_apiKey


### OpenNode

Om de Invoice te laten werken, moet je een publiek toegankelijke URL in je LNbits hebben. De webhook-instelling is optioneel.


  - `LNBITS_BACKEND_WALLET_CLASS`: **OpenNodeWallet**
  - `OPENNODE_API_ENDPOINT`: https://api.opennode.com/
  - `OPENNODE_KEY`: opennodeAdminApiKey


### Alby


Alby is een browserextensie met LN Wallet functionaliteiten en LNDHUB account die gebruikt kan worden als financieringsbron voor LNbits. [Meer details hier](https://getalby.com/).


Om de Invoice te laten werken moet je een publiek toegankelijke URL in je LNbits hebben. Er is geen handmatige webhook instelling nodig. Je kunt generate en Alby toegang geven tot token hier: https://getalby.com/developer/access_tokens/new



- `LNBITS_BACKEND_WALLET_CLASS`: AlbyWallet
- `ALBY_API_ENDPOINT`: https://api.getalby.com/
- `ALBY_ACCESS_TOKEN`: AlbyAccessToken


## Extra / Probleemoplossingsgidsen


Hier zijn wat extra instructies voor het geval je ze nodig hebt. Klik op de pijl om de beschrijving uit te breiden.


### The Killswitch 🚨


Er zijn de laatste tijd zoveel gevaarlijke bugs geweest, niet alleen in de hele wereld maar ook in LNbits, dat we besloten hebben er iets aan te doen. Je kunt je nu aanmelden voor waarschuwingen en/of directe actie ondernemen wanneer zich weer een kwetsbaarheid of bug voordoet die kan leiden tot het verlies van fondsen.


![killswitchn](assets/lnbits-killswitch.webp)


Als je overschakelt naar void-Wallet zullen alle gebruikerstypes op de instantie een gele banner zien waar je normaal de "LNbits is in Beta" melding vindt naast het thema/taal gebied aan de rechterkant - en dit is de meest voor de hand liggende hint dat er iets is gebeurd. Kijk eens naar je nieuwe server-tab in Green aan de linkerkant van het venster.


Hoe werkt het? Wanneer de killswitch is ingeschakeld, wordt een geheime github repository die alleen beschikbaar is voor het kernteam van LNbits gecontroleerd met een interval van X minuten (die kan worden opgegeven). Als er een kwetsbare bug wordt gepubliceerd in deze repository, dient dit als een signaal dat de killswitch activeert op alle installaties die zich hebben geabonneerd en je lnbits instance overzet om de lege Wallet te gebruiken. Als de wolken zijn verdwenen en je de beveiligingsupdate hebt geïnstalleerd, kun je je financieringsbron weer instellen op je node, Wallet of wat je dan ook gebruikt, ook via de sectie Server Beheren. Deze wiki heeft een sectie over het wisselen van financieringsbron als je niet weet wat je moet configureren.



### Verschil tussen admin en superuser


Met de LNbits Admin UI kun je LNbits instellingen wijzigen via de LNbits frontend. Het is standaard uitgeschakeld en de eerste keer dat je de omgevingsvariabele `LNBITS_ADMIN_UI=true` in het `.env` bestand instelt, worden de instellingen geïnitialiseerd en gebruikt. Vanaf dan worden de overeenkomende instellingen van de database gebruikt in plaats van die van het .env bestand.


### Supergebruiker


Met de beheerinterface hebben we de supergebruiker geïntroduceerd die toegang heeft tot de server en dus instellingen kan wijzigen die de server kunnen laten crashen of onresponsief maken via frontend en api, zoals het wijzigen van de financieringsbron. De supergebruiker wordt alleen opgeslagen in de instellingentabel van de database. Nadat de instellingen zijn "gereset naar standaardwaarden" en opnieuw zijn opgestart, wordt een nieuwe supergebruiker aangemaakt. We hebben ook een decorator toegevoegd voor de API-routes om het bestaan van een supergebruiker te controleren. Zijn ID wordt nooit verzonden via de api en de frontend en ontvangt alleen een bool (ja/nee) of je supergebruiker bent of niet.


Alleen de supergebruiker mag satoshis naar verschillende portemonnees brrrrren via de "Opwaarderen" sectie.


Je kunt de supergebruiker ook via een webhook naar een andere service sturen wanneer deze is aangemaakt. Meer informatie vind je hier https://github.com/lnbits/lnbits/blob/main/lnbits/settings.py `class SaaSSettings`


In de frontend vind je ook de mogelijkheid om de shop-afbeelding te wijzigen die wordt getoond op de "maak Wallet" pagina door de sectie Server beheren te openen en Thema -> Aangepast logo te kiezen.


### Admin-gebruikers


Omgevingsvariabele: `LNBITS_ADMIN_USERS`, een door komma's gescheiden lijst van gebruikers-ID's. Admin gebruikers kunnen instellingen wijzigen in de admin ui - met uitzondering van de financieringsbron instellingen, omdat dit een server herstart zou vereisen en de server ontoegankelijk zou kunnen maken. Ze hebben ook toegang tot alle extensies die aan hen zijn toegewezen in `LNBITS_ADMIN_EXTENSIONS`.


### Toegestane gebruikers


Omgevingsvariabele: `LNBITS_ALLOWED_USERS`, een door komma's gescheiden lijst met gebruikers-ID's. Door deze gebruikers te definiëren is LNbits niet langer te gebruiken door het publiek. Alleen gedefinieerde gebruikers en admins hebben dan toegang tot de LNbits frontend.




#### LNbits bijwerken

Een normale update van je LNbits lokale instantie doe je door simpelweg de volgende CLI commando's te kopiëren en te plakken:


```
cd lnbits
## Stop LNbits with `ctrl + x`
git pull
## Keep your poetry install up to date, this can be done with
poetry self update
poetry install --only main
## or
git checkout main && git pull && poetry install
## Start LNbits with
poetry run lnbits
```


Als je Raspiblitz of MyNode draait, heb je misschien ook een

```
sudo systemctl restart lnbits
```

aan het einde, omdat het LNbits als een service uitvoert.


Op Umbrel/Citadel zouden de commando's zijn

```
cd ~/apps/lnbits
git pull upstream main
sudo ~/scripts/app start lnbits
```


#### Migratie van SQLite naar PostgreSQL


Als je LNbits al op een SQLite database hebt geïnstalleerd en draaien, raden we je sterk aan om te migreren naar postgres als je van plan bent om LNbits op schaal te draaien.


Er is een script meegeleverd dat de migratie eenvoudig kan uitvoeren. Je moet Postgres al geïnstalleerd hebben en er moet een wachtwoord zijn voor de gebruiker (zie Postgres installatiegids hierboven). Daarnaast moet je LNbits instantie een keer draaien op postgres om de database Schema te implementeren voordat de migratie kan werken:


```
# STOP LNbits

# add the database connection string to .env 'nano .env' LNBITS_DATABASE_URL=
# postgres://<user>:<password>@<host>/<database> - alter line bellow with your user, password and db name
LNBITS_DATABASE_URL="postgres://postgres:postgres@localhost/lnbits"
# save and exit

# START LNbits
# STOP LNbits
poetry run python tools/conv.py
# or
make migration
```

Hopelijk werkt alles nu en wordt het gemigreerd... Start LNbits opnieuw en controleer of alles goed werkt.



#### Back-up en herstel van de database


Raadpleeg [deze zeer gedetailleerde handleiding over het back-up & herstelproces] (https://ereignishorizont.xyz/lnbits-server/en/#94_LNbits_-_Databases_Backup_Restore).



#### Mijn LNbits Wallet financieren vanaf mijn knooppunt werkt niet


Als je Sats wilt versturen vanaf hetzelfde knooppunt dat de financieringsbron is van je LNbits, dan moet je het LND.conf bestand bewerken.


De parameters die moeten worden opgenomen zijn: `allow-circular-route=1`


Doe dat in de sectie Application options van uw LND.conf. Op sommige bundelknooppunten kan het starten van LND anders mislukken.


OPMERKING: Het wordt aanbevolen om in plaats daarvan de nieuwe adminUI extensie met de "TopUp" optie te gebruiken om geld toe te voegen aan een LNbits account.


#### Fout 426

Ik kreeg de foutmelding: "lnurl moet worden geleverd via publiek toegankelijk https-domein of tor. 426 upgrade vereist"</summary>


Deze fout komt meestal omdat je LNbits achter een ngnix tunnel de LNURL Address niet correct doorstuurt. Stop je LNbits en bewerk het .env bestand door deze regel toe te voegen:

`FORWARDED_ALLOW_IPS=*`


Als je een ngnix setup gebruikt, zorg er dan voor dat deze headers in de ngnix configuratie staan:


```
RequestHeader set "X-Forwarded-Proto" expr=%{REQUEST_SCHEME}
RequestHeader set "X-Forwarded-SSL" expr=%{HTTPS}
```


#### Netwerkfout

Ik kreeg "https error", netwerkfout" of anderen bij het scannen van een QR</summary>


Slecht nieuws, dit is een routeringsfout die verschillende redenen kan hebben. Controleer eerst de LNURL van de QR met de [Lightning Decoder] (https://lightningdecoder.com/) of je daar iets vreemds in kunt vinden. Laten we een paar van de meest mogelijke problemen en hun oplossingen proberen.


LNbits draait alleen via Tor, je kunt het niet openen op een openbaar domein zoals lnbits.yourdomain.com



- Aangezien je wilt dat je setup zo blijft, open je LNbits Wallet met de .onion URI en maak je deze opnieuw aan. Op deze manier wordt de QR gegenereerd om bereikbaar te zijn via deze .onion URI dus alleen via tor. generate die QR niet van een .local URI, want het zal niet bereikbaar zijn via internet - alleen van binnen uw home-LAN.
- Open je LN Wallet app die je gebruikte om die QR te scannen en gebruik deze keer tor (zie instellingen Wallet app). Als de app geen tor biedt, kun je in plaats daarvan Orbot (Android) gebruiken. Zie installatiesectie voor gedetailleerde instructies over hoe je je LNbits opent voor clearnet/https.



#### Voorkomen dat anderen wallets genereren op mijn LNbits


Als je LNbits in clearnet draaien, kan in principe iedereen er generate en Wallet op zetten. Aangezien de fondsen van je node gebonden zijn aan deze wallets, wil je dat misschien voorkomen. Er zijn twee manieren om dat te doen:


Configureer toegestane gebruikers en extensies in het `.env` bestand ([zie het env voorbeeld hier](https://github.com/lnbits/lnbits/blob/main/.env.example)). Dit werkt alleen als je de instelling `adminUI=FALSE` in de .env gebruikt, anders moet je dat doen in de sectie Server beheren -> Gebruikers -> Toegestane gebruikers. Alle anderen worden daarna niet meer toegelaten.




#### De vervaldatum van Invoice aanpassen


Nu kun je generate facturen met een aangepaste vervaldatum. Compatibel met backends: LndRestWallet, LndWallet, CoreLightningWallet, EclairWallet, LnbitsWallet, SparkWallet tot nu toe!


Je kunt `LIGHTNING_INVOICE_EXPIRY` instellen in je .env-bestand of de AdminUI gebruiken om de standaardwaarde voor alle facturen te wijzigen. Er is ook een nieuw veld in het eindpunt /api/v1/payments waarmee je de vervaldatum kunt instellen in de JSON-gegevens.




## Wallet-URL verwijderd


### Wallet op demoserver legend.lnbits


Bewaar altijd een kopie van uw Wallet-URL, Export2phone-QR of LNDhub voor uw eigen portemonnees op een veilige plaats. LNbits KAN u NIET helpen deze terug te vinden als u ze kwijtraakt.


### Wallet op uw eigen financieringsbron/knooppunt

Bewaar altijd een kopie van uw Wallet-URL, Export2phone-QR of LNDhub voor uw eigen portemonnees op een veilige plaats. Je kunt alle LNbits gebruikers en Wallet-ID's vinden in je LNbits user manager extensie of in je sqlite database. Om de LNbits database te bewerken of te lezen, ga je naar de LNbits /data map en zoek je naar het bestand sqlite.db. U kunt het openen en bewerken met Excel of met een speciale SQL-editor zoals [SQLite browser] (https://sqlitebrowser.org/).


Je kunt ook de portemonnees dumpen via CLI en elke Wallet in je database bekijken.


```
cd ~/app-data/lnbits/data
sqlite3 database.sqlite3
.dump wallets
```


De uitvoer ziet er ongeveer zo uit


```
INSERT INTO wallets VALUES('f8a43fc363ea428db5c53b3559935f1f','NAME OF WALLET','1280ff5910a9c485a782a2376f338b6c','33b95b099ce848e3b484124373f681e5','2cca208ae6d94d438227b9487ff216f9');
```

en je wilt deze waarden in een url zetten zoals deze


```
https://your.lnbits.com/wallet?usr=1280ff5910a9c485a782a2376f338b6c&wal=f8a43fc363ea428db5c53b3559935f1f
```


Hierbij vervang je f8a43fc363ea428db5c53b3559935f1f door de waarde die voor de naam staat (in ons voorbeeld f8a43fc363ea428db5c53b3559935f1f) en 1280ff5910a9c485a782a2376f338b6c is je gebruiker en zou de waarde moeten worden die achter de naam staat. Om sqlite3 af te sluiten voer je in


```
.quit
```

#### LNURL voor een bliksem-Address vice versa


Probeer deze [encoder](https://lnurl-codec.netlify.app/) van fiatjaf of [deze](https://lightningdecoder.com/). Voor het betalen of controleren van een LNURLp kun je ook [LNurlpay](https://wwww.lnurlpay.com/) gebruiken. Er moet HTTPS op staan NIET HTTP.



#### Een commentaar configureren dat mensen zien wanneer ze betalen naar mijn LNURLp QR

Wanneer je een LNURL-p aanmaakt, is het commentaarvak standaard niet gevuld. Dat betekent dat commentaar niet mag worden gekoppeld aan betalingen.


Om commentaar toe te staan, voeg je de lengte van het vak toe, van 1 tot 250 tekens. Zodra je een getal hebt ingevoerd, wordt het commentaarvak weergegeven tijdens het betalingsproces. Je kunt ook een LNURL-p bewerken die al is gemaakt en dat nummer toevoegen.


![lnbits comments](assets/lnbits-comments.webp)


#### Stort onchain BTC naar LNbits

Er zijn twee manieren om Exchange Sats van onchain BTC naar LN BTC (resp. naar LNbits).


##### Via een externe swapservice.


Andere gebruikers die geen toegang hebben tot jouw LNb its kunnen een swap service gebruiken zoals [Boltz](https://boltz.Exchange/), [FixedFloat](https://fixedfloat.com/), [DiamondHands](https://swap.diamondhands.technology/) of [ZigZag](https://zigzag.io/). Dit is handig als je alleen LNURL/LN facturen verstrekt vanuit je LNbits instantie, maar een betaler heeft alleen onchain Sats, dus ze zullen die Sats eerst aan hun kant moeten omwisselen. De procedure is eenvoudig: gebruiker stuurt onchain btc naar de swap service en geeft de LNURL / LN Invoice van LNbits als bestemming van de swap.


##### Gebruik van de Onchain en Boltz LNbits uitbreiding.


Houd in gedachten dat dit een aparte Wallet is, niet de LN btc die door LNbits wordt voorgesteld als "jouw Wallet" op jouw LN financieringsbron. Deze onchain Wallet kan ook worden gebruikt om LN btc te wisselen naar (bijvoorbeeld je hardwarewallet) door gebruik te maken van de LNbits Boltz of Deezy extensie. Als je een webshop hebt die gekoppeld is aan je LNbits voor LN betalingen, is het erg handig om regelmatig alle Sats van LN af te tappen naar onchain. Dit leidt tot meer ruimte in uw LN kanalen om nieuwe verse Sats te kunnen ontvangen.


Procedure voor mensen zonder Bitcoin Hardware Wallet:



- Gebruik Electrum of Sparrow wallet om een nieuwe onchain Wallet te maken en bewaar de back-up seed op een veilige plaats.
- Ga naar Wallet informatie en kopieer de xpub.
- Ga naar LNbits - Onchain extensie en maak een nieuwe Watch-only wallet met die xpub.
- Ga naar LNbits - Tipjar extensie en maak een nieuwe Tipjar aan. Selecteer naast de LN Wallet ook de optie onchain.
- Optioneel - Ga naar LNbits - SatsPay extensie en maak een nieuwe lading voor onchain btc. Je kunt kiezen tussen onchain en LN of beide. Het zal dan een Invoice aanmaken die gedeeld kan worden.
- Optioneel - Als je LNbits koppelt aan een Wordpress + Woocommerce pagina, maak/koppel je een Watch-only wallet aan je LN btc shop Wallet, dan heeft de klant beide opties om te betalen op hetzelfde scherm.


Wanneer je een betaling ontvangt in LNbits, zal het transactielogboek alleen een hervat type van de transactie weergeven.


![lnbits payment details](assets/lnbits-payment-details.webp)


In je transactieoverzicht zie je een kleine Green pijl voor ontvangen en een rode pijl voor het geld dat is verzonden.


Als je op die pijlen klikt, verschijnt er een pop-up met details over de bijgevoegde berichten en de naam van de afzender als die is gegeven.


Een naam configureren om te verschijnen binnen betalingen, in LNbits is dit momenteel niet mogelijk om te doen - maar om te ontvangen. Dit is alleen mogelijk als de LN Wallet van de verzender [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (nameDesc) ondersteunt, zoals [OBW, Blixt, Alby, ZBD, BitBanana](https://github.com/lnurl/luds?tab=readme-ov-file#lnurl-documents).


Je ziet dan een alias/pseudoniem in de detailssectie van je LNbits-transacties (klik op de pijltjes). Houd er rekening mee dat je elke naam kunt opgeven en dat deze mogelijk niet overeenkomt met de echte naam van de afzender als je deze ontvangt.


![lnbits namedesc](assets/lnbits-namedesc.webp)


Om je LNbits account in een Wallet app te importeren, open je LNbits met het account / Wallet dat je wilt gebruiken, ga naar "beheer extensies" en activeer de LNDHUB extensie. Open de LNDHUB extensie, kies de Wallet die je wilt gebruiken en scan de "admin" of "Invoice only" QR, afhankelijk van het beveiligingsniveau dat je wilt voor die Wallet.


Je kunt [Zeus](https://zeusln.app/) of [Bluewallet](https://bluewallet.io/) gebruiken als Wallet apps voor een lndhub account waarbij BW meer dan één Wallet ondersteunt.


Als je dit doet, raden we je aan om ook de LN netwerk URI in te stellen op die van je eigen node. Als je LNbits instantie alleen Tor is, moet je deze apps ook gebruiken met Tor geactiveerd. Ook in dit geval moet je de LNbits pagina openen via je Tor .onion Address.


Als je een Error "unsupported Hash type" hebt bij het gebruik van een ypub in On-Chain extensie, controleer dan of je LNbits instance python 3.10 gebruikt. Dit probleem kan van invloed zijn op [dit probleem] (https://stackoverflow.com/questions/72409563/unsupported-Hash-type-ripemd160-with-hashlib-in-python). Bewerk de openssl.cnf zoals beschreven in het stackoverflow antwoord en herstart je LNbits.



## Gereedschap maken en bouwen met LNbits


LNbits heeft allerlei [open API's] (https://legend.lnbits.com/docs) en tools om te programmeren en verbinding te maken met een heleboel verschillende apparaten voor een heleboel verschillende gebruikssituaties.


Als je nieuw bent met bouwen, begin dan met deze [MakerBits presentaties](https://www.youtube.com/channel/UCZhKfzK6_KWZ-CFC2wXQVBw/videos) van Ben Arc over het bouwen van gadgets gebaseerd op LNbits.


### BELANGRIJK:


- LNbits werkt op basis van het LNURL protocol waarbij verzoeken in twee vormen geldig zijn: als https:// clearnet link (geen zelfondertekende certificaten toegestaan) of als http:// v2/v3 onion link. Om LNbits diensten aan te bieden zoals LNURLp/w QR codes of NFC kaarten, die in het wild gebruikt kunnen worden, moet je LNbits openen naar clearnet (https).
- Gebruik alleen DATA-kabels om je esp32 van stroom te voorzien. Niet alle kabels ondersteunen data naast het voeden van de esp. Je zou niet de eerste zijn als de kabel die bij de esp is geleverd alleen een voedingskabel is
- Zorg ervoor dat u geen USB-Hub gebruikt waaraan andere apparaten zijn aangesloten. Dit kan leiden tot vreemde effecten die Hard zijn om te debuggen (bijvoorbeeld niet starten of stoppen).
- Om esp projecten te realiseren met een MacOS heb je een UART Bridge Driver nodig. Als je problemen hebt met het stuurprogramma op Mac- of Linux-systemen, kun je die hier vinden of, als het om een TTGO Display gaat, deze. Als je Windows gebruikt en problemen hebt met de verbinding, zorg er dan voor dat je de oude versie 11.1.0 downloadt, want de nieuwere versie werkt niet! Je kunt hier ook een seriële terminal vinden om je verbinding te controleren - stel deze in op baudrate 115200.
- Hoewel het veel comfortabeler is om Platform.io te gebruiken (afhankelijkheden worden bijvoorbeeld automatisch geïnstalleerd) raden we iedereen die nieuw is met bouwen aan om Arduino te gebruiken.
- TT-Go Display S3: De kleur van het lipje van de screen protector film vertelt je welke controller precies (ST7735_redtab, ST7735_blacktag, ST7735_greetab, greentab128, ..) is gebruikt om het te bouwen. Bewaar het om te kunnen debuggen als je zelf programmeert en het scherm geeft afbeeldingen niet correct weer, bijvoorbeeld verkeerde kleuren, gespiegelde afbeeldingen of verdwaalde pixels aan de randen. Als je dit ooit moet doen, is er een epische gids over het aanpassen voor verschillende schermen
- Gebruik altijd kleine letters lnurl239xx in plaats van LNURLl239xx
- Het toevoegen van lightning:lnurl1234xyz zal een QR creëren die vraagt om de gebruikers Wallet te openen voor deze Invoice bij het scannen (laatst geïnstalleerde lightning app op iOS, instelling in Android)
- Als je een esp32 flasht via het web, werkt dit alleen met deze browsers (TL:DR Chrome, Edge & Opera).
- Let op deze PIN-OUT referentie voor de esp
- Als je FOSSoftware of FOSGuides gebruikt, plaats dan altijd een link naar de auteur. Iedereen vindt het leuk om hun baby te zien groeien en het brengt ook een bouwketen op gang die geweldig is om te zien:)


Kom naar de [Makerbits Telegram Group](https://t.me/makerbits) als je hulp nodig hebt met een project - we hebben je!


![lnbits hackathlon](assets/lnbits-hackathlon.webp)


Hier zijn enkele projectcategorieën die je kunt bouwen met LNbits:



- [Nostr Ondertekeningsapparaat] (https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#nostr-signing-device)
- [Archade Machine](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#arcade-machine)
- [Gerty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#gerty)
- [Nostr Zap Lamp](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#zap-lamp)
- [BTC/LN ATM](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#atm)
- [LNPoS](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lnpos-terminal)
- [Bliksemschicht Piggy](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lightning-piggy)
- [Hardware Wallet] (https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#hardware-Wallet)
- [Bitcoin Schakelaar] (https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Bitcoin-switch)
- [Automaat](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#vending-machine)
- [Bolty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bolty)
- [Nerdminer](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Nerdminer)
- [Bitcoin Ticker](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Bitcoin-ticker)
- [BTClock](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#btclock)
- [Lora en netwerken](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lora)



- [HELPERS & BRONNEN](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#resources)
- [Meer voorbeelden van projecten "Powered by LNbits" hier](https://github.com/lnbits/lnbits/wiki/Powered-by-LNbits).
- [Gebruikscases voor LNbits](https://github.com/lnbits/lnbits/wiki/Use-Cases-of-LNbits)