---
name: LNbits
description: Plattform for handelsregnskap
---
![presentation](assets/lnbits-intro.webp)

# Regnskapssystem

LNbits er fullpakket med mange verktøy for å kontrollere og kanalisere innkommende og utgående midler, koble til nettbutikken din eller til og med enheter som en maskinvarelommebok eller en minibank som du har bygget selv. Brukertyper inkluderer:


- Lommebankeiere som ønsker å bruke LNbits som et grensesnitt for forvaltningen av midlene sine, samt ekstrafunksjonene.
- Nettbutikker og tjenesteleverandører som ønsker å akseptere Bitcoin onchain- og Lightning Network-betalinger.
- Utviklere som ønsker å bygge Lightning Network-applikasjoner.
- Nodeoperatører som ønsker å integrere noden sin med LNbits-systemet for regnskapsformål.
- Alle disse har forskjellige behov. Vi bygger LNbits modulært, slik at alle brukere kan bruke funksjonene våre på den måten som passer dem best.

# Lommebokansvarlig

LNbits er et gratis regnskapssystem med åpen kildekode - ikke en nodeadministrator. Kanaladministrasjon er domenet til Lightning-noden som er koblet til LNbits som en finansieringskilde, slik som LND eller c-lightning. Superbrukeren eller administratorbrukerne i LNbits-systemet er ansvarlige for å administrere den generelle tilgjengeligheten og konfigurasjonen av regnskapsfunksjonene og interne utvidelser.

LNbits fungerer som et grensesnitt mellom brukeren og Lightning-noden, og tilbyr en enkel og brukervennlig måte å administrere og samhandle med betalingsnettverket på.

Tenk på LNbits som et "modulært Wordpress-rammeverk" for noden din. En plattform som er enkel å administrere, basert på utvidelser som du kan kombinere for en rekke bruksområder.

Tenk på LNbits som din egen banks programvare for økonomistyring. Noden din tilbyr kanaler du kan betale gjennom, og LNbits utvider noden din til å kunne kjøre mer enn én lynlommebok som noden din kommer med. Disse lommebøkene trenger ikke nødvendigvis å tilhøre deg selv. La oss si at du, som driver LN-noden, allerede har nok kanallikviditet og midler, og at du nå ønsker å tilby noen bitcoin-banktjenester til venner, familie, din egen butikk eller andre vanlige selgere.

Du vil tilby en enkel måte for dem å åpne en "bankkonto" på noden din uten å ha tilgang til andre lommebøker på noden din og til all nodelikviditeten, men bare deres del. Noden din (banken) fungerer kun som en transportleverandør for deres betalinger (inn/ut).

MERK: Alle midler som "kundene" dine setter inn på LNbits-bankkontoene sine på noden din, vil gå rett inn i LN-kanalene på noden din. Det betyr at DU faktisk er den virkelige eieren av disse midlene. Du vil ha et stort ansvar for deres midler. Ikke vær ond og stikk av med midlene, ikke vær ond og ta høye gebyrer. Vi ønsker å knulle fiat-banksterne, ikke å knulle hverandre (bitcoin-brukere).

# Demoplattform

Demoen finner du på [https://legend.lnbits.com](https://legend.lnbits.com). Den er fullt funksjonell og kan brukes til å lære om Lightning Network og funksjonene i LNbits og LNURL generelt. Selv om vi ikke kan hindre deg i å bruke den, vil vi be deg om å ikke bruke den til produksjonsoppsettet ditt. Ikke bare jobber vi ofte på serverne for å teste nye funksjoner, men vi vil også oppfordre deg til å kjøre din egen node og LNbits på en suveren måte. Hvis du synes det er for mye å kjøre en node for øyeblikket, kan du koble LNbits til en depotfinansieringstjeneste i skyen som Opennode, Luna eller Votage eller til Lightning Tipbot på Telegram, bare for å nevne noen.

# LNbits-flygeblad

Vil du overlevere litt grunnleggende informasjon til en kjøpmann eller en byggevenn av deg? Vi er veldig glade for å kunne presentere vår første flyer som alle kan bruke. Størrelsen er et globalt typisk flyerformat med 6 sider (2 bretter) og en bredde på 3508 og en høyde på 2480px.

LNbits for selgere: [EN](/assets/lnbits-merchants-en.pdf) | [DE](/assets/lnbits-merchants-de.pdf) | [ES](/assets/lnbits-merchants-es.pdf) | [IT](/assets/lnbits-merchants-it.pdf) | [PL](/assets/lnbits-merchants-pl.pdf)

LNbits for byggherrer: [EN](/assets/lnbits-builders-en.pdf) | [DE](/assets/lnbits-builders-de.pdf) | [ES](/assets/lnbits-builders-es.pdf) | [IT](/assets/lnbits-builders-it.pdf) | [PL](/assets/lnbits-builders-pl.pdf)

# Noen grunnleggende ting

LNbits fungerer basert på LNURL-protokollen, noe som betyr at forespørsler er gyldige i to former: enten som https:// clearnet-link (ingen selvsignerte sertifikater tillatt) eller som http:// v2/v3 onion-link. For å tilby LNbits-tjenester som LNURLp/w QR-koder eller NFC-kort, som kan brukes i naturen, må du åpne LNbits for clearnet (https).

Før du installerer LNbits, må du sørge for å ha lest og forstått følgende generelle veiledning om hva LNbits er og hvilke muligheter det gir deg.


- [LND Guide] (https://docs.lightning.engineering/) | Installere LND
- [Eksempel på LND-konfigurasjon] (https://github.com/lightningnetwork/lnd/blob/master/sample-lnd.conf) | LND-innstillinger
- [CLN-veiledning] (https://docs.corelightning.org/docs/installation) | Installere CLN
- [LUDs](https://github.com/lnurl/luds) LNURL Spec | [NIPs](https://github.com/nostr-protocol/nips) Nostr Spec
- [Kjør et vakttårn] (https://docs.lightning.engineering/lightning-network-tools/lnd/watchtower) | Veldig viktig!

Mer detaljerte veiledninger om bruk av LNbits i spesifikke bruksscenarioer her:


- [Komme i gang med LNbits] (https://darthcoin.substack.com/p/getting-started-lnbits) | Substack-veiledning
- [ToDos for din sikkerhet med LNbits] (https://youtu.be/i5FQf96e6zg) | Youtube Video
- [Private banker på Lightning Network] (https://darthcoin.substack.com/p/bitcoin-private-banks-over-lightning) | Substack guide
- [Kjør depotlommebøker til venner og familie] (https://darthcoin.substack.com/p/the-bank-of-lnbits) | Substack guide
- [LNbits for en liten restaurant/hotell](https://darthcoin.substack.com/p/lnbits-for-small-merchants) | Substack guide
- [Bruke LNbits Streamer copilot] (https://darthcoin.substack.com/p/lnbits-streamer-copilot) | Substack guide
- [Start ditt NOSTR-marked med LNbits] (https://darthcoin.substack.com/p/lnbits-nostr-market) | Substack-guide
- [Bruk av LNbits til skoleprosjekter eller festivalarrangementer] (https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools) Substack guide

# Installer LNbits

## Grunnleggende installasjonsveiledning

LNbits kan installeres på alle Linux OS-maskiner. Det krever ikke en kraftig maskin eller server, bare nok RAM-minne og litt diskplass for databasen. Det kan kjøres separat fra en BTC/LN-node (lokal PC eller ekstern VPS) eller sammen på samme maskin som noden, eller allerede installert i en pakke med nodeprogramvare.

Du kan velge mellom de vanligste pakkebehandlerne som poetry og nix. Som standard vil LNbits bruke SQLite som database. Du kan også bruke PostgreSQL, som anbefales for applikasjoner med høy belastning. [Her er en veiledning for grunnleggende installasjon ved hjelp av poetry eller nix] (https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md).

For alle som er nye på dette området, finner du mer detaljerte trinn-for-trinn-veiledninger for hvordan du får LNbits til å kjøre i bestemte miljøer:


- [LNbits på clearnet](https://ereignishorizont.xyz/lnbits-server/en/) av Axel
- [LNbits på en VPS] (https://github.com/TrezorHannes/vps-lnbits) av Hannes
- [LNbits på cloudflare] (https://www.nodeacademy.org/lnbits) av Leo

Du kan også finne en video på [dockerisert oppsett på en VPS med PostgreSQ, LightningTipBot som finansieringskilde ved hjelp av nginx] (https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/).

[Flere installasjonsscenarier her] (https://darthcoin.substack.com/p/build-your-own-lnbits-app-server).

For programvarepakker, se deres spesifikke dokumentasjon om LNbits: [Citadel](https://runcitadel.space) | [Umbrel](https://umbrel.com) | [MyNode](https://mynodebtc.com) | [RaspiBlitz](https://raspiblitz.org/) | [RaspiBolt](https://raspibolt.org)

## LNbits SaaS

Når du ikke er interessert i det tekniske og verken vil være vert for finansieringskilden eller LNbits selv, finnes det en [LNbits SaaS-versjon] (https://saas.lnbits.com) (Software-as-a-service) du kan bruke. Det er i utgangspunktet som LNbits i en sky, men du kan definere finansieringskilden (f.eks. noden din, en LNbits-lommebok, LNtipbot, fakewallet osv.) og miljøvariabler selv - noe som stort sett ikke er tilfelle på andre skyløsninger.

[Her er en detaljert veiledning om hvordan du bruker LNbits SaaS for spesifikke bruksområder] (https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools).

## Finansieringskilder

LNbits er ikke en nodeadministrasjonsprogramvare, men et LN-fokusert regnskapssystem på toppen av en LND- eller CLN-finansieringskilde. Etter den første installasjonen kan du besøke LNbits på http://localhost:5000/.

For å endre finansieringskilden, gå til superbruker-URL-en din og velg en finansieringskilde i "Manage Server" eller rediger .env-filen ved å endre `LNBITS_BACKEND_WALLET_CLASS` til den nødvendige kilden hvis du angir `adminUI=TRUE` i `.env`.

Du finner .env-filen i mappen lnbits/ eller lnbits/apps/data ved å utvide kommandoen til å liste opp filer i katalogen din med `ls -a`.

Det kan også hende at du må installere flere pakker eller utføre flere oppsettstrinn ved å velge ønsket finansieringskilde. Etter en omstart vil det nye oppsettet være aktivt.

Hvilke finansieringskilder kan jeg bruke for LNbits?

LNbits kan kjøre på toppen av mange finansieringskilder for lynnettverk. For øyeblikket er det støtte for CoreLightning, LND, LNbits, LNPay, OpenNode, og flere blir lagt til regelmessig.

Det er viktig å velge en kilde som har god likviditet og gode peers tilkoblet. Hvis du bruker LNbits for offentlige tjenester, kan brukernes betalinger bare flyte i begge retninger.

En backend-lommebok (finansieringskilde) kan konfigureres ved hjelp av følgende LNbits-miljøvariabler i filen `.env` eller i superbrukerkontoen din under Administrer-server-delen.

Hvis du ønsker å bruke .env-versjonen, finner du parametrene her:

### CoreLightning


- CLN
  - `LNBITS_BACKEND_WALLET_CLASS`: **CoreLightningWallet**
  - `CORELIGHTNING_RPC`: /file/path/lightning-rpc
- Gnist (c-lyn)
  - `LNBITS_BACKEND_WALLET_CLASS`: **SparkWallet**
  - `SPARK_URL`: http://10.147.17.230:9737/rpc
   - `SPARK_TOKEN`: secret_access_key

### Lightning Network Daemon


- LND (REST)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LndRestWallet**
  - `LND_REST_ENDPOINT`: http://10.147.17.230:8080/
  - `LND_REST_CERT`: /file/path/tls.cert
  - `LND_REST_MACAROON`: /file/path/admin.macaroon eller Bech64/Hex
  - `LND_REST_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn
- LND (gRPC)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LndWallet**
  - `LND_GRPC_ENDPOINT`: ip_address
  - `LND_GRPC_PORT`: port
  - `LND_GRPC_CERT`: /file/path/tls.cert
  - `LND_GRPC_MACAROON`: /file/path/admin.macaroon eller Bech64/Hex

Du kan også bruke en AES-kryptert makron (mer info) i stedet ved å bruke


  - `LND_GRPC_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn

For å kryptere macaroon kjører du `./venv/bin/python lnbits/wallets/macaroon/macaroon/macaroon.py`.

### LNbits (en annen LNbits-instans)


- LNbits-instans på en skyserver eller din egen hjemmeserver
  - `LNBITS_BACKEND_WALLET_CLASS`: **LNbitsWallet**
  - `LNBITS_ENDPOINT`: https://lnbits.mydomain.com
  - `LNBITS_KEY`: my-lnbits-AdminKey
- LNbits Legend Demo Server (!!! Ikke bruk denne til produksjon / kommersielle formål, bare for testing !!!)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LNbitsWallet**
  - `LNBITS_ENDPOINT`: https://legend.lnbits.com
  - `LNBITS_KEY`: legend-lnbits-AdminKey

### Lightning TipBot

For å koble din [Lightning Tipbot] (https://t.me/LightningTipBot) fra Telegram må du angi følgende parameter:


  - `LNBITS_BACKEND_WALLET_CLASS`: **LnTipsWallet**
  - `LNBITS_ENDPOINT`: https://ln.tips
  - `LNBITS_KEY`: For å få nøkkelen må du kjøre /api i en privat chat med LightningTipbot på Telegram en gang.

Se også denne veiledningen om hvordan du installerer [LNbits med LightningTipBot via vps] (https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/)

### IBEX HUB

Registrer deg [her] (https://ibexpay.ibexmercado.com/onboard) og hent nøklene/tokenene dine derfra, endepunktet er https://ibexpay-api.ibexmercado.com.

For mer informasjon, se [IBEX API-Documentation] (https://ibexpay-api.readme.io/reference/getting-started-with-your-api).

### LNPay

For at fakturalytteren skal fungere, må du ha en offentlig tilgjengelig URL i LNbits og sette opp en [LNPay webhook] (https://dashboard.lnpay.co/webhook/) som peker til `<din LNbits-vert>/wallet/webhook` med "Wallet Receive"-hendelsen og ingen hemmelighet gitt. Innstillingen `https://mylnbits/wallet/webhook` vil være endepunkt-URL-en som blir varslet om enhver betaling.


  - `LNBITS_BACKEND_WALLET_CLASS`: **LNPayWallet**
  - `LNPAY_API_ENDPOINT`: https://api.lnpay.co/v1/
  - `LNPAY_API_KEY`: sak_apiKey
  - `LNPAY_WALLET_KEY`: waka_apiKey

### OpenNode

For at fakturaen skal fungere, må du ha en offentlig tilgjengelig URL i LNbits. Webhook-innstillingen er valgfri.


  - `LNBITS_BACKEND_WALLET_CLASS`: **OpenNodeWallet**
  - `OPENNODE_API_ENDPOINT`: https://api.opennode.com/
  - `OPENNODE_KEY`: opennodeAdminApiKey

### Alby

Alby er en nettleserutvidelse med LN-lommebokfunksjoner og LNDHUB-konto som kan brukes som finansieringskilde for LNbits. [Mer informasjon her] (https://getalby.com/).

For at fakturaen skal fungere, må du ha en offentlig tilgjengelig URL i LNbits. Ingen manuell innstilling av webhook er nødvendig. Du kan generere et Alby-tilgangstoken her: https://getalby.com/developer/access_tokens/new


- `LNBITS_BACKEND_WALLET_CLASS`: AlbyWallet
- `ALBY_API_ENDPOINT`: https://api.getalby.com/
- `ALBY_ACCESS_TOKEN`: AlbyAccessToken

## Ytterligere / Feilsøkingsveiledninger

Her er noen ekstra instruksjoner i tilfelle du skulle trenge dem. Klikk på pilen for å utvide beskrivelsen.

### The Killswitch 🚨

Det har vært så mange farlige feil i det siste, ikke bare i hele verden, men også i LNbits, at vi bestemte oss for å gjøre noe med det. Du kan nå velge å motta advarsler og/eller iverksette direkte tiltak når en sårbarhet eller en feil som kan føre til tap av penger, oppstår igjen.

![killswitchn](assets/lnbits-killswitch.webp)

Hvis du bytter til void-lommebok, vil alle brukertyper på instansen se et gult banner der du normalt finner "LNbits er i beta"-varselet ved siden av tema-/språkområdet oppe til høyre - og er det mest åpenbare hintet om at noe har skjedd. Ta en titt på den nye server-fanen som er uthevet i grønt i venstre del av vinduet.

Hvordan fungerer det? Når killswitch er aktivert, vil et hemmelig github-depot som kun er tilgjengelig for LNbits kjerneteam, bli sjekket med et intervall på X minutter (som kan spesifiseres). Hvis en sårbar feil blir publisert i dette depotet, fungerer det som et signal som utløser killswitch på alle installasjoner som abonnerer og overfører lnbits-forekomsten din til å bruke den tomme lommeboken. Hvis skyene har fjernet seg og du har installert sikkerhetsoppdateringen, kan du angi finansieringskilden din til noden, lommeboken eller hva du bruker igjen, også via Manage Server-delen. Denne wikien har en seksjon om hvordan du bytter finansieringskilde hvis du ikke vet hva du skal konfigurere.

### Forskjellen mellom admin og superbruker

LNbits Admin UI lar deg endre LNbits-innstillinger via LNbits frontend. Det er deaktivert som standard, og første gang du angir miljøvariabelen `LNBITS_ADMIN_UI=true` i filen `.env`, blir innstillingene initialisert og vil bli brukt. Deretter brukes innstillingene fra databasen i stedet for innstillingene i .env-filen.

### Superbruker

Med admin-brukergrensesnittet introduserte vi superbrukeren som har tilgang til serveren, slik at den kan endre innstillinger som kan få serveren til å krasje eller gjøre at den ikke svarer via frontend og api, som f.eks. å endre finansieringskilden. Superbrukeren er bare lagret i innstillingstabellen i databasen. Etter at innstillingene er "tilbakestilt til standardinnstillingene" og startet på nytt, opprettes en ny superbruker. Vi har også lagt til en dekorator for API-rutene for å sjekke om det finnes en superbruker. ID-en sendes aldri over API-et og frontend, og mottar bare en bool (ja/nei) om du er superbruker eller ikke.

Det er bare superbrukeren som har lov til å overføre satoshier til forskjellige lommebøker via "Top Up"-delen.

Du kan også sende superbrukeren via webhook til en annen tjeneste når den opprettes. Mer info her https://github.com/lnbits/lnbits/blob/main/lnbits/settings.py `class SaaSSettings`

I frontend finner du også muligheten til å endre butikkbildet som vises på "opprett lommebok"-siden ved å åpne Manage Server-delen og velge Theme -> Custom Logo.

### Admin-brukere

Omgivelsesvariabel: `LNBITS_ADMIN_USERS`, kommaseparert liste over bruker-ID-er. Admin-brukere kan endre innstillinger i admin-brukergrensesnittet - med unntak av innstillinger for finansieringskilder, fordi dette vil kreve en omstart av serveren og potensielt kan gjøre serveren utilgjengelig. De har også tilgang til alle utvidelsene som er dedikert til dem i `LNBITS_ADMIN_EXTENSIONS`.

### Tillatte brukere

Omgivelsesvariabel: `LNBITS_ALLOWED_USERS`, kommaseparert liste over bruker-ID-er. Ved å definere disse brukerne vil LNbits ikke lenger kunne brukes av allmennheten. Bare definerte brukere og administratorer har da tilgang til LNbits-frontenden.

#### Oppdater LNbits

En normal oppdatering av din lokale LNbits-instans gjøres ganske enkelt ved å kopiere og lime inn følgende CLI-kommandoer:

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

Hvis du kjører Raspiblitz eller MyNode, kan du i tillegg trenge en

```
sudo systemctl restart lnbits
```

på slutten, fordi den kjører LNbits som en tjeneste.

På Umbrel/Citadel vil kommandoene være

```
cd ~/apps/lnbits
git pull upstream main
sudo ~/scripts/app start lnbits
```

#### Migrering fra SQLite til PostgreSQL

Hvis du allerede har LNbits installert og kjører på en SQLite-database, anbefaler vi på det sterkeste at du migrerer til postgres hvis du planlegger å kjøre LNbits i stor skala.

Det følger med et skript som enkelt kan gjøre migreringen. Du må ha Postgres installert, og det bør finnes et passord for brukeren (se installasjonsveiledningen for Postgres ovenfor). I tillegg må LNbits-instansen din kjøre én gang på Postgres for å implementere databaseskjemaet før migreringen kan fungere:

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

Forhåpentligvis fungerer alt nå og blir migrert ... Start LNbits igjen og sjekk om alt fungerer som det skal.

#### Sikkerhetskopiering og gjenoppretting av databasen

Se [denne svært detaljerte veiledningen om sikkerhetskopierings- og gjenopprettingsprosessen] (https://ereignishorizont.xyz/lnbits-server/en/#94_LNbits_-_Databases_Backup_Restore).

#### Finansiering av LNbits-lommeboken min fra noden min fungerer ikke

Hvis du vil sende sats fra den samme noden som er finansieringskilden til LNbits, må du redigere filen lnd.conf.

Parametrene som skal inkluderes er: `allow-circular-route=1`

Gjør dette i avsnittet Application options i lnd.conf. På noen bundle-noder kan starten av LND mislykkes ellers.

MERK: Vi anbefaler at du i stedet bruker den nye adminUI-utvidelsen med alternativet "TopUp" for å legge til penger på en LNbits-konto.

#### Feil 426

Jeg fikk en feilmelding: "lnurl må leveres over offentlig tilgjengelig https-domene eller tor. 426 oppgradering kreves"</summary>

Denne feilen skyldes vanligvis at LNbits bak en ngnix-tunnel ikke videresender LNURL-adressen riktig. Stopp LNbits og rediger .env-filen ved å legge til denne linjen:

`FORWARDED_ALLOW_IPS=*``

Hvis du bruker et ngnix-oppsett, må du også sørge for at du har disse overskriftene i ngnix-konfigurasjonen:

```
RequestHeader set "X-Forwarded-Proto" expr=%{REQUEST_SCHEME}
RequestHeader set "X-Forwarded-SSL" expr=%{HTTPS}
```

#### Nettverksfeil

Jeg fikk "https-feil", nettverksfeil" eller annet når jeg skannet en QR</summary>

Dårlige nyheter, dette er en rutingsfeil som kan ha ganske mange grunner. Sjekk først QRs LNURL med [Lightning Decoder] (https://lightningdecoder.com/) hvis du kan finne noe rart der. La oss prøve noen av de mest mulige problemene og deres løsninger.

LNbits kjører kun via Tor, du kan ikke åpne det på et offentlig domene som lnbits.yourdomain.com


- Gitt at du vil at oppsettet ditt skal forbli slik, åpner du LNbits-lommeboken din ved hjelp av .onion URI og oppretter den på nytt. På denne måten genereres QR-en slik at den er tilgjengelig via denne .onion URI-en, altså kun via tor. Ikke generer QR-en fra en .local URI, fordi den ikke vil være tilgjengelig via internett - bare fra ditt hjemme-LAN.
- Åpne LN-lommebokappen som du brukte til å skanne QR-koden, og denne gangen ved å bruke tor (se innstillinger for lommebokappen). Hvis appen ikke tilbyr tor, kan du bruke Orbot (Android) i stedet. Se installasjonsdelen for detaljerte instruksjoner om hvordan du åpner LNbits for clearnet/https.

#### Hindre andre i å generere lommebøker på mine LNbits

Når du kjører LNbits i clearnet, kan i utgangspunktet alle generere en lommebok på den. Siden midlene til noden din er bundet til disse lommebøkene, kan det være lurt å forhindre dette. Det er to måter å gjøre det på:

Konfigurer tillatte brukere og utvidelser i filen `.env` ([se env-eksempelet her](https://github.com/lnbits/lnbits/blob/main/.env.example)). Dette fungerer bare hvis du bruker innstillingen `adminUI=FALSE` i .env, ellers må du gjøre det i Manage Server-seksjonen -> Users -> Allowed Users. Alle andre vil ikke bli tillatt etterpå.

#### Tilpass tidsrammen for utløp av fakturaen

Nå kan du generere fakturaer med egendefinert utløpsdato. Kompatibel med backends: LndRestWallet, LndWallet, CoreLightningWallet, EclairWallet, LnbitsWallet, SparkWallet så langt!

Du kan angi `LIGHTNING_INVOICE_EXPIRY` i .env-filen eller bruke AdminUI til å endre standardverdien for alle fakturaer. Det er også et nytt felt i /api/v1/payments-endepunktet der du kan angi utløp i JSON-dataene.

## Wallet-URL slettet

### Lommebok på demo-server legend.lnbits

Lagre alltid en kopi av wallet-URL, Export2phone-QR eller LNDhub for dine egne lommebøker på et trygt sted. LNbits kan IKKE hjelpe deg med å gjenopprette dem når du mister dem.

### Lommebok på egen finansieringskilde/node

Lagre alltid en kopi av wallet-URL, Export2phone-QR eller LNDhub for dine egne lommebøker på et trygt sted. Du finner alle LNbits-brukere og lommebok-ID-er i LNbits-brukeradministratorutvidelsen eller i sqlite-databasen din. For å redigere eller lese LNbits-databasen, går du til LNbits /data-mappen og ser etter filen som heter sqlite.db. Du kan åpne og redigere den med Excel eller med en dedikert SQL-Editor som [SQLite browser] (https://sqlitebrowser.org/).

Du kan også dumpe lommebøkene via cli og se hver lommebok i databasen din.

```
cd ~/app-data/lnbits/data
sqlite3 database.sqlite3
.dump wallets
```

Utdataene vil se omtrent slik ut

```
INSERT INTO wallets VALUES('f8a43fc363ea428db5c53b3559935f1f','NAME OF WALLET','1280ff5910a9c485a782a2376f338b6c','33b95b099ce848e3b484124373f681e5','2cca208ae6d94d438227b9487ff216f9');
```

og du vil legge disse verdiene inn i en url slik

```
https://your.lnbits.com/wallet?usr=1280ff5910a9c485a782a2376f338b6c&wal=f8a43fc363ea428db5c53b3559935f1f
```

Hvor du erstatter f8a43fc363ea428db5c53b3559935f1f med verdien som kommer før navnet (i vårt eksempel f8a43fc363ea428db5c53b3559935f1f) og 1280ff5910a9c485a782a2376f338b6c er din bruker og skal bli verdien som vises etter navnet. For å avslutte sqlite3 skriver du inn

```
.quit
```

#### LNURL for en lyn-adresse og omvendt

Prøv denne [encoder](https://lnurl-codec.netlify.app/) fra fiatjaf eller [denne](https://lightningdecoder.com/). For å betale eller sjekke en LNURLp kan du også bruke [LNurlpay](https://wwww.lnurlpay.com/). Det skal stå HTTPS IKKE HTTP.

#### Konfigurer en kommentar som folk ser når de betaler til min LNURLp QR

Når du oppretter en LNURL-p, er kommentarfeltet som standard ikke fylt ut. Det betyr at det ikke er tillatt å legge til kommentarer til betalinger.

For å tillate kommentarer, legg til tegnlengden i boksen, fra 1 til 250. Når du har lagt inn et tall der, vises kommentarfeltet i betalingsprosessen. Du kan også redigere en LNURL-p som allerede er opprettet og legge til det nummeret.

![lnbits comments](assets/lnbits-comments.webp)

#### Innskudd onchain BTC til LNbits

Det er to måter å veksle sats fra onchain BTC til LN BTC (hhv. til LNbits).

##### Via en ekstern byttetjeneste.

Andre brukere som ikke har tilgang til LNb its kan bruke en byttetjeneste som [Boltz] (https://boltz.exchange/), [FixedFloat] (https://fixedfloat.com/), [DiamondHands] (https://swap.diamondhands.technology/) eller [ZigZag] (https://zigzag.io/). Dette er nyttig hvis du bare leverer LNURL/LN-fakturaer fra LNbits-instansen din, men en betaler bare har onchain-satser, så de må bytte disse satsene først på sin side. Fremgangsmåten er enkel: brukeren sender onchain btc til byttetjenesten og oppgir LNURL/LN-fakturaen fra LNbits som destinasjon for byttet.

##### Bruk av Onchain og Boltz LNbits-utvidelsen.

Husk at dette er en separat lommebok, ikke LN btc-lommeboken som er representert av LNbits som "lommeboken din" på LN-finansieringskilden din. Denne onchain-lommeboken kan også brukes til å bytte LN btc til (f.eks. maskinvarelommeboken din) ved å bruke LNbits Boltz- eller Deezy-utvidelsen. Hvis du driver en nettbutikk som er koblet til LNbits for LN-betalinger, er det veldig praktisk å regelmessig tømme alle satsene fra LN til onchain. Dette fører til mer plass i LN-kanalene dine for å kunne motta nye, ferske sats.

Prosedyre for de som ikke har en bitcoin-maskinvarelommebok:


- Bruk Electrum- eller Sparrow-lommeboken til å opprette en ny lommebok i kjeden, og lagre sikkerhetskopien på et trygt sted.
- Gå til lommebokinformasjon og kopier xpuben.
- Gå til LNbits - Onchain-utvidelse og opprett en ny lommebok kun for klokker med den xpuben.
- Gå til LNbits - Tipjar-utvidelse og opprett en ny Tipjar. Velg også onchain-alternativet i tillegg til LN-lommeboken.
- Valgfritt - Gå til LNbits - SatsPay-utvidelse og opprett en ny belastning for onchain btc. Du kan velge mellom onchain og LN eller begge. Det vil da opprettes en faktura som kan deles.
- Valgfritt - Hvis du bruker LNbits knyttet til en Wordpress + Woocommerce-side, vil kunden ha begge alternativene for å betale på samme skjermbilde når du oppretter / kobler en lommebok for kun klokker til LN btc-lommeboken.

Når du mottar en betaling i LNbits, vil transaksjonsloggen kun vise en gjenopptatt type av transaksjonen.

![lnbits payment details](assets/lnbits-payment-details.webp)

I transaksjonsoversikten finner du en liten grønn pil for mottatt og en rød pil for midler som er sendt.

Hvis du klikker på disse pilene, får du opp et popup-vindu som viser vedlagte meldinger samt avsenderens navn, hvis det er oppgitt.

For å konfigurere et navn som skal vises i betalinger, er dette for øyeblikket ikke mulig å gjøre i LNbits - men å motta. Dette er bare mulig hvis avsenderens LN-lommebok støtter [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (nameDesc) som [OBW, Blixt, Alby, ZBD, BitBanana](https://github.com/lnurl/luds?tab=readme-ov-file#lnurl-documents).

Du vil da se et alias/pseudonym i detaljdelen av LNbits-transaksjonene dine (klikk på pilene). Merk at du kan oppgi hvilket som helst navn der, og det er ikke sikkert at det er relatert til den virkelige avsenderens navn hvis du mottar et slikt.

![lnbits namedesc](assets/lnbits-namedesc.webp)

For å importere LNbits-kontoen din i en lommebok-app, åpner du LNbits med kontoen/lommeboken du vil bruke, går til "administrer utvidelser" og aktiverer LNDHUB-utvidelsen. Åpne LNDHUB-utvidelsen, velg lommeboken du vil bruke, og skann enten QR-koden "admin" eller "kun faktura", avhengig av sikkerhetsnivået du vil ha for den lommeboken.

Du kan bruke [Zeus] (https://zeusln.app/) eller [Bluewallet] (https://bluewallet.io/) som lommebokapper for en lndhub-konto, der BW støtter mer enn én slik lommebok.

Når du gjør dette, anbefaler vi at du også setter LN-nettverks-URI-en til din egen node. Hvis LNbits-instansen din kun er Tor, må du også bruke disse appene med Tor aktivert. Også i dette tilfellet må du åpne LNbits-siden gjennom Tor .onion-adressen din.

Hvis du har en feil "unsupported hash type" når du bruker en ypub i On-chain extension, sjekk om LNbits-instansen din bruker python 3.10, det kan være påvirket av [dette problemet] (https://stackoverflow.com/questions/72409563/unsupported-hash-type-ripemd160-with-hashlib-in-python). Rediger openssl.cnf som beskrevet i stackoverflow-svaret, og start LNbits på nytt.

## Verktøy og bygging med LNbits

LNbits har alle slags [åpne API-er] (https://legend.lnbits.com/docs) og verktøy for å programmere og koble til mange forskjellige enheter for en mengde ulike bruksområder.

Hvis du er nybegynner, kan du starte med denne [MakerBits-presentasjonen] (https://www.youtube.com/channel/UCZhKfzK6_KWZ-CFC2wXQVBw/videos) fra Ben Arc om å bygge gadgets basert på LNbits.

### VIKTIG:


- LNbits fungerer basert på LNURL-protokollen som forespørsler er gyldige i to former: enten som https:// clearnet link (ingen selvsignerte sertifikater tillatt) eller som http:// v2/v3 onion link. For å tilby LNbits-tjenester som LNURLp/w QR-koder eller NFC-kort, som kan brukes i naturen, må du åpne LNbits til clearnet (https).
- Bruk bare DATA-kabler til å drive esp32. Ikke alle kabler støtter data i tillegg til å drive esp. Du ville ikke være den første hvis kabelen som fulgte med esp er en ren strømkabel
- Pass på at du ikke bruker en USB-Hub med andre enheter tilkoblet. Dette kan føre til merkelige effekter som er vanskelige å feilsøke (f.eks. at den ikke starter eller stopper).
- For å realisere esp-prosjekter med MacOS trenger du en UART Bridge Driver. Hvis du har problemer med driveren på Mac- eller Linux-systemer, kan du finne dem her eller, hvis en TTGO-skjerm er involvert, denne. Hvis du bruker Windows og har problemer med å koble til, må du sørge for å laste ned den GAMLE versjonen 11.1.0 fordi den nyere ikke fungerer! Du kan også finne en seriell terminal her for å sjekke tilkoblingen din - sett til baudrate 115200.
- Selv om det er mye mer komfortabelt å bruke Platform.io (f.eks. installeres avhengigheter automatisk), anbefaler vi å bruke Arduino for alle som ikke er vant til å bygge.
- TT-Go Display S3: Fargen på fanen på skjermbeskyttelsesfilmen forteller deg nøyaktig hvilken kontroller (ST7735_redtab, ST7735_blacktag, ST7735_greetab, greentab128, ...) som har blitt brukt til å bygge den. Behold den for å kunne feilsøke hvis du programmerer deg selv og skjermen ikke viser grafikk riktig, f.eks. feil farger, speilvendte bilder eller bortkomne piksler i kantene. Hvis du noen gang trenger å gjøre dette, finnes det en episk guide om hvordan du justerer for ulike skjermer
- Bruk alltid små bokstaver lnurl239xx i stedet for LNURLl239xx
- Hvis du legger til lightning:lnurl1234xyz, opprettes en QR som ber om å åpne brukerens lommebok for denne fakturaen ved skanning (sist installerte lightning-app på iOS, innstilling i Android)
- Hvis du blinker en esp32 via nettet, vil den bare fungere med disse nettleserne (TL:DR Chrome, Edge og Opera).
- Vær oppmerksom på denne PIN-OUT-referansen for esp
- Når du bruker FOSSoftware eller FOSGuides, må du alltid lenke til forfatteren. Alle elsker å se barnet sitt vokse, og det setter også i gang en byggekjede som er ganske fantastisk å se på :)

Kom til [Makerbits Telegram Group] (https://t.me/makerbits) hvis du trenger hjelp med et prosjekt - vi har deg!

![lnbits hackathlon](assets/lnbits-hackathlon.webp)

Her er noen prosjektkategorier du kan bygge med LNbits:


- [Nostr Signing Device] (https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#nostr-signing-device)
- [Archade Machine] (https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#arcade-machine)
- [Gerty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#gerty)
- [Nostr Zap-lampe] (https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#zap-lamp)
- [BTC/LN ATM] (https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#atm)
- [LNPoS](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lnpos-terminal)
- [Lightning Piggy] (https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lightning-piggy)
- [Hardware Wallet] (https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#hardware-wallet)
- [Bitcoin Switch] (https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bitcoin-switch)
- [Salgsautomat] (https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#vending-machine)
- [Bolty] (https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bolty)
- [Nerdminer](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Nerdminer)
- [Bitcoin Ticker] (https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bitcoin-ticker)
- [BTClock](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#btclock)
- [Lora og Mesh-nettverk] (https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lora)
- [HJELPERE OG RESSURSER](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#resources)
- [Flere eksempler på prosjekter "Powered by LNbits" her] (https://github.com/lnbits/lnbits/wiki/Powered-by-LNbits).
- [Brukstilfeller for LNbits] (https://github.com/lnbits/lnbits/wiki/Use-Cases-of-LNbits)