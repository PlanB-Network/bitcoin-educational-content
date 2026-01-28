---
name: ThunderHub
description: Interface Lightning node management web LND
---
![cover](assets/cover.webp)



## Innledning



ThunderHub er en **open source-manager for Lightning-noder (LND)**, som tilbyr en intuitiv Interface som er tilgjengelig fra alle enheter eller nettlesere.



**Hovedfunksjoner:**




- **Overvåking**: Global oversikt over saldoer, kanaler, transaksjoner og rutingstatistikk
- **Administrasjon**: Åpne/lukk kanaler, innkommende/utgående betalinger, kanalbalansering
- **Integrasjoner**: LNURL-støtte, bytter via Boltz, Amboss-sikkerhetskopiering
- **Interface responsiv**: Kompatibel med mobil, nettbrett og stasjonære enheter med mørke/lyse temaer



ThunderHub kan enkelt integreres med **Umbrel**, **Voltage**, **RaspiBlitz** og **MyNode**, noe som forenkler den daglige administrasjonen av noden din.



**ThunderHub er spesielt godt egnet for operatører som ønsker en ergonomisk Interface for å administrere kanalene sine, kontrollere likviditet (rebalansering), overvåke transaksjoner og integrere tredjepartstjenester som Amboss. Sikkerheten ivaretas via en lokal eller Tor-tilkobling.**



Hvis du ennå ikke har en Lightning-node, anbefaler vi at du følger vår LND Umbrel-veiledning:



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Installasjon



ThunderHub kan installeres på en rekke forskjellige måter, avhengig av ditt Lightning node-hostingmiljø. Enten du bruker en nøkkelferdig løsning (Umbrel, Voltage, RaspiBlitz, MyNode, Start9, etc.) eller en manuell installasjon, er ThunderHub ofte tilgjengelig uten større anstrengelser. Nedenfor beskriver vi to vanlige tilnærminger: via Umbrel App Store og via manuell installasjon (gjelder for en server eller en distribusjon på egen vert).



### Installasjon via Umbrel



Umbrel integrerer ThunderHub i sin **App Store**, noe som gjør installasjonen ekstremt enkel. Du trenger ingen kommandolinje eller manuell konfigurasjon: alt gjøres via Interface Umbrel. Bare følg disse trinnene:





- **Åpne Umbrel-dashbordet**: Koble til Interface-nettverket til Umbrel-noden din (f.eks. `http://umbrel.local` på ditt lokale nettverk, eller via Address Address `.onion` hvis du bruker Tor).
- Få tilgang til **App Store**: I Umbrels hovedmeny klikker du på "App Store" (eller "App"). Søk etter **ThunderHub** i listen over tilgjengelige applikasjoner.



![Écran d'installation de ThunderHub via Umbrel](assets/fr/01.webp)





- **Installer ThunderHub**: Klikk på ThunderHub-applikasjonen, og deretter på installasjonsknappen. Bekreft om nødvendig. Umbrel vil automatisk laste ned og distribuere ThunderHub på noden din.





- **Start applikasjonen**: Når installasjonen er fullført (noen titalls sekunder), vises ThunderHub på startsiden din. Klikk på ikonet for å åpne det. ThunderHub starter i nettleseren din.



![Identifiants par défaut pour ThunderHub](assets/fr/02.webp)



**Viktig: Når ThunderHub åpnes for første gang, vises automatisk standardpassordet som kreves for å logge inn. Med alternativet "Ikke vis dette igjen" kan du skjule denne visningen for fremtidige tilkoblinger. Vi anbefaler på det sterkeste at du:**




- **Lagre dette passordet umiddelbart** i passordbehandleren din
- Kopier den **for bruk i neste trinn**
- Merk av for "Ikke vis dette igjen" når passordet er lagret



![Page de connexion de ThunderHub](assets/fr/03.webp)



Du kommer da til påloggingssiden, der du må skrive inn passordet du kopierte i forrige trinn for å låse opp Interface.



![Interface de connexion complète à ThunderHub](assets/fr/04.webp)



Umbrel sørger for å gi ThunderHub informasjon om LND-tilkoblingen (TLS-sertifikat, administrasjonsmacaroon osv.) i bakgrunnen, slik at du ikke trenger å gjøre noen ekstra konfigurasjon. Med bare noen få klikk har du ThunderHub oppe og går på Umbrel-noden din.



### Manuell installasjon (selv-hostet, unntatt Umbrel)



For brukere utenfor Umbrel (f.eks. på en personlig server, en Raspberry Pi med RaspiBlitz eller en *stand-alone* installasjon), krever ThunderHub-installasjonen noen ekstra trinn. Nedenfor beskriver vi installasjonen fra kildekode og konfigurasjonen, i henhold til [den offisielle ThunderHub-dokumentasjonen](https://docs.thunderhub.io).



#### Installasjon



**Forutsetninger:** Sørg for at systemet ditt oppfyller minimumskravene i henhold til [documentation setup](https://docs.thunderhub.io/setup):




- **Node.js** versjon 18 eller nyere
- **npm** installert
- Tilgang til LND-godkjenningsfiler :
  - LND TLS-sertifikat (`tls.cert`)
  - LND administrasjonsmakron (`admin.macaroon`)
  - LND gRPC-tjeneste Address (vertsnavn:port) (standard `127.0.0.1:10009` lokalt)



**1. Hent ThunderHub-kode:** Klon prosjektets GitHub-repository som beskrevet i [installasjonsdokumentasjonen](https://docs.thunderhub.io/installation):



```bash
git clone https://github.com/apotdevin/thunderhub.git
cd thunderhub
```



**2. Installer avhengigheter og bygg applikasjonen**



```bash
npm install
npm run build
```



Disse kommandoene installerer alle de nødvendige modulene og kompilerer deretter applikasjonen (ThunderHub er skrevet i TypeScript/React).



**3. Oppdater senere:** ThunderHub tilbyr flere metoder for fremtidige oppdateringer:



```bash
# Méthode rapide
npm run update

# Ou méthode manuelle
git pull
npm install
npm run build
```



#### Konfigurasjon (oppsett)



**1. Hovedkonfigurasjonsfil:** Opprett en `.env.local`-fil i roten av ThunderHub-mappen for å tilpasse konfigurasjonen (dette forhindrer at innstillingene dine blir overskrevet under oppdateringer). Hovedvariabler i henhold til [setup documentation](https://docs.thunderhub.io/setup):



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



**2. Konfigurasjon av serverkontoer:** Opprett YAML-filen som er angitt i `ACCOUNT_CONFIG_PATH` :



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



**3. Ekstern tilgang:** For å koble til en ekstern LND-node, legg til i `LND.conf` :



```bash
# Option 1 : accès par IP
tlsextraip=<ip-externe-accessible>
rpclisten=0.0.0.0:10009

# Option 2 : accès par domaine
tlsextradomain=<domaine-externe-accessible>
rpclisten=0.0.0.0:10009
```



**4. Sikkerhet:** Ved første oppstart skjuler ThunderHub **automatisk** `masterPassword` og alle kontopassord i YAML-filen, for å unngå at passord ligger i klartekst på serveren.



**5. Start ThunderHub:**



```bash
npm start
```



Som standard lytter serveren på port 3000. Gå til `http://localhost:3000` (eller `http://ip-serveur:3000` fra det lokale nettverket).



**6. Docker-alternativ:** ThunderHub tilbyr offisielle Docker-bilder:



```bash
# Image standard
docker pull apotdevin/thunderhub:latest
docker run --rm -it -p 3000:3000/tcp apotdevin/thunderhub:latest

# Image avec base path /thub
docker pull apotdevin/thunderhub:base-v0.11.1
```



ThunderHub-påloggingssiden vises. Velg den konfigurerte kontoen og skriv inn passordet for å få tilgang til dashbordet.



**Installasjon på andre distribusjoner:** Ferdigpakkede node-distribusjoner (RaspiBlitz, MyNode, Start9 osv.) tilbyr vanligvis innebygd ThunderHub-støtte via sine respektive administrasjonsgrensesnitt.



**For mer informasjon:** Se den komplette offisielle dokumentasjonen :




- **Installasjon:** [docs.thunderhub.io/installation](https://docs.thunderhub.io/installation)
- **Konfigurasjon:** [docs.thunderhub.io/setup](https://docs.thunderhub.io/setup)



Disse ressursene beskriver avanserte alternativer som SSO-kontoer, krypterte makroner, TOR-konfigurasjon og mye mer.



Når ThunderHub er installert og tilgjengelig, er du klar til å utnytte alle funksjonene. I det følgende tar vi en titt på Interface ThunderHub og de ulike fanene for å veilede deg gjennom bruken av den.



## Interface-presentasjon



Interface ThunderHub er strukturert rundt en hovedmeny (vanligvis vist i kolonnen til venstre) som består av flere hovedseksjoner. Hver av dem tilsvarer et aspekt av administreringen av Lightning-noden. La oss gå gjennom dem én etter én:





- **Hjem** - Hjem-fanen med et generelt dashbord (oversikt over noden og raske handlinger).
- **Dashboard** - Tilpassbart dashboard med widgeter og avanserte beregninger.
- **Peers** - Lightning peer management (forbindelser til andre noder).
- **Channels** - Detaljert styring av Lightning-kanaler.
- **Rebalance** - verktøy for kanalbalansering (sirkulære betalinger).
- **Transaksjoner** - Lyn-betalingshistorikk (LN-transaksjoner).
- **Forwards** - Routing-statistikk (betalinger videresendt av noden din).
- **Chain** - Node's On-Chain-portefølje (On-Chain BTC: UTXOs, transaksjoner).
- **Amboss** - Integrasjon med Amboss (nodeovervåking, sikkerhetskopiering osv.).
- **Verktøy** - Diverse verktøy (sikkerhetskopier, signerte meldinger, makroner, rapporter osv.).
- **Swap** - On-Chain/Lightning-byttefunksjoner via Boltz.
- **Statistikk** - Avansert statistikk og beregninger av nodeytelse.



*(Merk: Avhengig av ThunderHub-versjonen kan enkelte seksjoner ha litt andre overskrifter eller tilleggsfunksjoner, men de generelle prinsippene er de samme)*



### Hjem (Generelt kontrollpanel)



ThunderHubs **Home**-fane er startsiden som vises etter at du har logget inn. Den inneholder **General Dashboard**, som gir en **global oversikt** over statusen til Lightning-noden din og foreslår **hurtige handlinger** for rutinemessige operasjoner. Her er hva du vanligvis finner:



![Tableau de bord principal de ThunderHub](assets/fr/05.webp)





- **Saldoer og kapasiteter:** Øverst på siden viser ThunderHub dine tilgjengelige saldoer. Her vil du vanligvis se On-Chain-saldoen (Bitcoin On-Chain i nodens Wallet, symbolisert med en Anchor ⚓) og Lightning-saldoen (kanalenes kapasitet, symbolisert med et lyn Bolt ⚡). Dette gir deg en umiddelbar oversikt over midlene du har i On-Chain og Lightning. Hvis du har flere kontoer eller kanaler, må du sørge for at du er på den riktige (f.eks. Mainnet vs Testnet).





- **Nøkkelstatistikk:** Dashbordet kan vise noen globale beregninger for noden din - for eksempel antall åpne kanaler, antall tilkoblede peers, opptjente rutingavgifter (hvis aktuelt) osv. Det er et sammendrag av nodens aktivitet og tilstand den siste tiden.





- **Hurtighandlinger:** Instrumentpanelet har knapper som gjør det mulig å utføre de vanligste oppgavene raskt, uten å måtte navigere gjennom menyer. Disse hurtighandlingene inkluderer :





- **Ghost**: Sett opp en tilpasset Lightning Address via Amboss.
- **Doner**: Gi en donasjon via Lightning.
- **Logg inn/Gå til**: Koble deg til Amboss-kontoen din (Quick Connect) og gå direkte til Amboss.space for å se informasjonen om noden din.
- **Address**: Angi en Lightning Address for å foreta en betaling.
- **Åpne**: Åpne en ny Lightning-kanal. Ved å klikke på åpnes et skjema for å angi URI-en til den eksterne noden som kanalen skal åpnes til, beløpet og, hvis det er aktuelt, den maksimale On-Chain-avgiften som skal brukes.
- **Dekod**: Dekod en Lightning Invoice eller LNURL for å se detaljer før betaling.
- **LNURL**: Behandle LNURL-er for Lightning-betalinger eller -uttak.
- **LnMarkets-pålogging**: Logg inn på LnMarkets for å handle.



Med disse hurtighandlingene kan du utføre de vanligste operasjonene direkte fra startsiden, uten å måtte navigere gjennom de ulike fanene i Interface.



Kort sagt gir ThunderHub-dashbordet deg en **rask titt** på noden din, og lar deg utføre de vanligste operasjonene (sende/motta, åpne en kanal) med ett enkelt klikk. Det er det ideelle utgangspunktet for den daglige administrasjonen.



### Dashbord



Seksjon **Dashboard** er atskilt fra Hjem-fanen og tilbyr et mer avansert, tilpassbart dashbord. Her kan du opprette en tilpasset visning med spesifikke widgeter i henhold til dine behov som nodeoperatør.





- **Tilpassbare widgeter:** I motsetning til startsiden, som har en fast layout, kan du på dashbordet velge nøyaktig hvilke Elements som skal vises, og hvordan de skal organiseres.



![Dashboard sans widgets activés](assets/fr/06.webp)



Hvis ingen widgeter er aktivert, vises meldingen "No Widgets Enabled!" med en "Settings"-knapp for å få tilgang til tilpasningsparametrene.



![Paramètres des widgets du Dashboard](assets/fr/07.webp)



I innstillingene kan du velge mellom et bredt utvalg av widgeter organisert i kategorier: "Lightning - Info", "Lightning - Tabell", "Lightning - Graf" og så videre. Hver widget kan aktiveres eller deaktiveres individuelt med knappene "Show/Hide".



![Bas de la page des paramètres](assets/fr/08.webp)



Nederst i innstillingene finner du knappen "Til dashbordet" for å gå tilbake til dashbordet, og knappen "Tilbakestill widgeter" for å tilbakestille standardvisningen.



![Dashboard personnalisé avec widgets](assets/fr/09.webp)



Når dashbordet er konfigurert, kan det vise ulike grafer og beregninger: Grafer for lynbetalinger, antall utstedte fakturaer, videresendingsstatistikk, detaljerte saldoer osv.





- **Avanserte beregninger:** Få tilgang til mer detaljert statistikk over nodens ytelse, med grafer og sanntidsdata.





- **Konfigurerbar oversikt:** Skreddersy skjermen slik at den passer enten du er en vanlig bruker eller en profesjonell operatør som administrerer flere rutingskanaler.





- **Modular Interface:** Legg til eller fjern widgeter etter behov: foroverdiagrammer, likviditetsmålinger, varsler om nodehelse osv.



Denne delen er spesielt nyttig for avanserte brukere som ønsker å overvåke spesifikke beregninger eller få en mer teknisk oversikt over Lightning-noden sin. Den utfyller Hjem-delen ved å tilby større fleksibilitet og kontroll over hvordan informasjonen vises.



### Likemenn



I **Peers**-delen vises alle Lightning-noder som for øyeblikket er koblet til din som peers. En **peer** er en direkte node-til-node-forbindelse på Lightning Network. Noden din kan være koblet til andre noder selv uten en åpen kanal (f.eks. bare til Exchange-sladderinformasjon i nettverket), eller selvfølgelig innebærer enhver åpen kanal automatisk en tilkoblet node.



![Vue de l'onglet Peers avec les pairs connectés](assets/fr/10.webp)



I fanen Peers ser du :





- **Informasjonskolonner:** Interface viser nyttige detaljer som synkroniseringsstatus, tilkoblingstype (clearnet eller Tor), ping, mottatte/sendte satoshis og datavolumet som utveksles.
- **Legg til en node:** ThunderHub lar deg manuelt koble til en ny node via **"Legg til"**-knappen øverst i høyre hjørne. Du må skrive inn nodens URI (format `<public_key>@<socket>`). Når den er validert, sender ThunderHub den tilsvarende `lncli connect`-kommandoen. Hvis noden er online og tilgjengelig, vil den bli lagt til i listen over jevnaldrende.



### Kanaler



Fanen **Kanaler** er hjertet i Lightning-kanaladministrasjonen. Det er sannsynligvis den delen du kommer til å bruke oftest. Her finner du **alle Lightning-kanalene** med informasjon om dem, og du kan utføre administrasjonshandlinger på disse kanalene.



![Vue d'ensemble des channels ouverts](assets/fr/11.webp)



Dette er hva du finner på Channels-siden:





- **Kanallistevisning:** Hver åpen (eller åpen/lukket) kanal vises i en liste, vanligvis med aliaset til den eksterne noden, den totale kanalkapasiteten og en farget stolpe som illustrerer fordelingen av lokal og ekstern likviditet. ThunderHub bruker en fargekode (ofte blå/Green) eller en prosentandel for å indikere kanalbalansen: for eksempel blå for din lokale andel, Green for den eksterne andelen. Hvis en kanal er perfekt balansert (50/50), vil stolpen være halvparten av hver farge. På denne måten kan du raskt se hvilke kanaler som er ubalanserte (alt blått = nesten alt lokalt, alt Green = nesten alt eksternt).





- **Informasjonskolonner:** Interface viser detaljerte kolonner, inkludert Status, Tilgjengelige handlinger, Peer Info, Kanal-ID, Kapasitet, Aktivitet, Gebyrer og Saldo med grafisk likviditetsvisning.





- **Displaykonfigurasjon:** Med et tannhjul øverst i høyre hjørne kan du tilpasse kanalvisningen slik at den passer til dine preferanser.





- **Status:** Du vil også se statusindikatorer - f.eks. `Aktiv` (kanalen er åpen og i drift), `Offline` (motparten er frakoblet, slik at kanalen for øyeblikket er ubrukelig), `Venter` (for åpninger eller stengninger som venter på bekreftelse fra On-Chain).





- **Handlinger på en kanal:** For hver kanal tilbyr ThunderHub handlingsknapper (ofte i form av ikoner):



![Actions de gestion des canaux - Modifier et Fermer](assets/fr/12.webp)





- Rediger avgifter: Interface "Oppdater kanalpolicy" lar deg justere alle kanalparametere: Basisavgift, avgiftssats (i ppm), CLTV-delta, maks HTLC og min HTLC. Dette gjør at du kan justere gebyrpolitikken individuelt per kanal, med sikte på å tiltrekke (eller motvirke) ruting av trafikk. *(Merk: ThunderHub er ikke en erstatning for et automatisk avgiftsstyringsverktøy, men for manuell justering er det svært effektivt)*
- Lukk kanal (**Lukk**): Interface "Avslutningskanal" gir deg valget mellom en **samarbeidsavslutning** (standard) eller en **tvangsavslutning** (**Tvangsavslutning**) ved å definere gebyrene (i Sats/vByte). **Viktig:** Foretrekk alltid kooperativ avslutning når det er mulig, for å unngå On-Chain-oppgjørsforsinkelser og høyere gebyrer. ThunderHub vil fortelle deg om motparten er online (samarbeid mulig) eller ikke. I tilfelle force close, må du sørge for å bekrefte, da dette er irreversibelt og vil utløse en feiende transaksjon med en tidslås (vanligvis 144 blokker eller ~ 1 dag på Bitcoin Mainnet).
- **Åpne en ny kanal:** For å åpne en ny kanal klikker du på tannhjulet øverst til høyre på Channels-siden, og velger deretter "Open". Deretter kan du starte en kanal til en ny eller eksisterende motpart. Fordelen med å bruke denne siden er at du har en liste over eksisterende kanaler foran deg, noe som kan hjelpe deg med å bestemme hvor du skal åpne en ny kanal.



Kort sagt gir Channels-delen deg **fin kontroll over hver enkelt kanal**. Det er her du styrer likviditetsallokeringen, bestemmer hvilke kanaler som skal beholdes eller stenges, og angir rutingsparametere per kanal. ThunderHub tilbyr en tydelig Interface for disse viktige nodeadministrasjonsoperasjonene.



### Ombalansering



Fanen **Rebalansering** er dedikert til **kanalbalansering**. Balansering (eller *rebalansering*) innebærer å justere fordelingen av midler mellom utgående og innkommende kanaler ved å foreta en **sirkulær betaling** fra en av kanalene dine til en annen av kanalene dine, via Lightning Network. På denne måten kan du, uten å tilføre nye midler, flytte likviditet fra en kanal som er for full til en som er for tom, noe som gjør kanalene dine mer nyttige (en balansert kanal kan både sende og motta betalinger).



![Interface de rebalance des canaux](assets/fr/13.webp)



ThunderHub gjør denne operasjonen mye enklere, noe som ellers ville vært kjedelig på kommandolinjen. Slik bruker du Rebalance-delen:





- **Første kanalvisning:** Når du går inn i Rebalance, viser ThunderHub en liste over kanalene dine, med en balanseindikator for hver av dem (på samme måte som på Channels-siden). Du kan med en gang se hvilke kanaler som er i ubalanse. ThunderHub kan sortere kanalene i rekkefølge etter økende balanse, slik at de mest ubalanserte kanalene står øverst på listen (0,0 betyr helt lokal eller ekstern).





- **Valg av motparter:** Interface gjør det enkelt å velge utgående og innkommende motparter for rebalansering.





- **Parameterinnstillinger:** Du kan stille inn :
  - Den **maksimale avgiften** (i Sats og ppm) du er villig til å betale
- Beløpet som skal rebalanseres med alternativet "Fast" eller "Mål"
- **Noder som skal unngås** ved ruting
- **Maksimal prøvetid** for rutesøking





- Velg **kilde kanal**: Velg først den **utgående (kilde)** kanalen, dvs. den kanalen som du har for mye lokal likviditet til å flytte fra. I praksis er dette en kanal der din lokale andel er høy (> 50 %). La oss tenke oss en A-kanal med 1 000 000 Satss, hvorav 900 000 er lokale - en god kandidat for å sende Satss andre steder. Ved å klikke på denne A-kanalen som "utgående", markerer ThunderHub den som en kilde.





- Velg **målkanal**: Deretter velger du den **innkommende (mål)** kanalen som trenger å motta likviditet. Vanligvis vil dette være en kanal der det er omvendt - de fleste midlene er på den andre siden (f.eks. bare 100 000 lokale Satss av 1 000 000). Når du har valgt kildekanalen, sorterer ThunderHub de andre kanalene i omvendt rekkefølge (avtagende balanse) for å hjelpe deg med å identifisere de mest komplementære kanalene. Velg en B-kanal som har plass på den lokale siden. ThunderHub vil da tydelig vise hvilke to kanaler som er valgt (kilde A og mål B).





- **Angi gebyrbeløp og toleranse:** Et skjema lar deg legge inn :





- **Beløpet** som skal rebalanseres (i Sats). Ofte velger vi et beløp som tilsvarer det som vil balansere begge kanalene ved \~50/50. ThunderHub kan for eksempel forhåndsfylle halvparten av den overskytende kapasiteten i kildekanalen.
  - Den **maksimale avgiften** du er villig til å betale for denne operasjonen (valgfritt). Denne avgiften uttrykkes i Sats (total kostnad for sirkulær ruting). Hvis du lar den stå tom, vil ThunderHub søke etter en bane uavhengig av kostnad, noe som vanligvis ikke er tilrådelig (det er bedre å angi en grense, f.eks. 10 Sats for en liten rebalansering, eller en maksimal ppm).





- **Finn rute:** Klikk på knappen for å finne en rute. ThunderHub spør LND for å beregne en rute fra kildekanalen din gjennom nettverket til din egen målkanal. Hvis den finner en mulig rute som oppfyller gebyrkriteriene dine, vises den med detaljer om hoppene og gebyrkostnaden. Den kan for eksempel indikere at den har funnet en rute med 3 hopp og totalt 2 Sats i avgifter.





- **Start rebalansering:** Hvis du er fornøyd med den foreslåtte ruten, klikker du på **Balanseringskanal**. ThunderHub vil deretter starte sirkulær betaling via LND. Hvis betalingen er vellykket, vil du se et varsel om suksess, og kanalene A og B vil få sine saldoer endret i sanntid. ThunderHub vil oppdatere saldoindikatoren for disse kanalene (ideelt sett vil de være grønnere enn før, noe som indikerer bedre saldo).





- **Justeringer og iterasjoner:** Hvis du ikke finner noen rute på første forsøk (eller hvis den er for dyr), kan du justere parametrene :





  - Prøv med et mindre beløp (noen ganger går en delvis rebalansering gjennom, mens en stor mengde mislykkes).
  - Øk maksimumsavgiften gradvis, men pass på at du ikke betaler mer i avgifter enn det er verdt.
  - Bruk knappen **Hent en annen rute**, hvis tilgjengelig, for å prøve et alternativ.
  - Prøv med et annet par kanaler hvis det virkelig blir vanskelig.



ThunderHub gjør prosessen veldig **intuitiv og visuell**. I bare fire trinn (velg utgående kanal, velg innkommende kanal, beløp, valider) kan du gjøre det som tidligere krevde komplekse manuelle kommandoer. Verktøyet er uvurderlig for å opprettholde en velbalansert node, forbedre rutingytelsen og -opplevelsen (enklere å sende og motta betalinger på tvers av alle kanalene dine).



Til slutt må du være oppmerksom på at en rebalansering medfører rutingskostnader (som betales til mellomliggende noder), så det er en **investering** for å gjøre noden din mer flytende. Bruk den med omhu, for eksempel for å støtte en kanal til en tjeneste du bruker ofte (inngående likviditet) eller for å balansere en stor rutingkanal. ThunderHub lar deg gjøre dette **enkelt og effektivt**.



### Transaksjoner



Avsnittet **Transaksjoner** i ThunderHub tilsvarer nodens **Lightning**-transaksjonshistorikk, dvs. betalinger og fakturaer som er betalt eller mottatt via kanalene. Det er en slags kontoutskrift for LN-operasjonene dine.



![Historique des transactions Lightning](assets/fr/14.webp)



I denne fanen finner du :





- **Invoice-graf:** Øverst i høyre hjørne viser en graf utviklingen av mottatte fakturaer over tid, slik at du kan visualisere aktiviteten i noden din.





- En kronologisk liste over alle Lightning-transaksjoner som er gjort *fra* eller *til* noden din. Hver oppføring kan vise :





  - Type operasjon: **sendt betaling** (utgående betaling) eller **mottatt betaling** (innkommende, via en betalt Invoice).
  - Beløpet i Sats.
  - Dato/klokkeslett
  - BetalingsID (Hash eller RHash pre-image) eller kommentar (hvis du har lagt til et memo i Invoice).
  - Status: **fullført**, eller muligens **pågående**/*feil* (f.eks. en betaling som venter på å bli løst, men generelt behandler LND dette raskt, så det er lite "ventende" her sammenlignet med On-Chain-transaksjoner).



Kort sagt fungerer Transactions-delen som din **LN-aktivitetslogg**. Den er veldig nyttig for å sjekke at en betaling har gått gjennom, hvor mange gebyrer den kostet, eller for å spore historikken til Lightning-utvekslingene dine. Sammen med Forwards-delen (som beskrives i neste avsnitt) får du en fullstendig oversikt over pengene som har gått gjennom noden din.



### Fremover



Fanen **Forwards** er dedikert til nodens **routing**-aktivitet, dvs. betalinger som **transiteres** gjennom kanalene dine (når du fungerer som en mellomliggende node på Lightning Network). Hvis du driver noden din som en rutingsnode, er dette en viktig del for å spore resultatene dine.



![Statistiques de routage Lightning](assets/fr/15.webp)



I Forwards presenterer ThunderHub :





- **Filtre og visningsalternativer:** Øverst til høyre finner du filtre som lar deg sortere data etter dag/uke/måned/år, og du kan velge mellom grafisk visning eller tabellvisning.





- **Aktivitetsmelding:** Hvis ingen ruting har blitt utført i løpet av den valgte perioden, viser Interface "Ingen viderekoblinger for denne perioden", som vist i dette eksempelet.





- En **tabell over nylige videresendinger**: Hver oppføring tilsvarer en betaling som har blitt **videresendt** gjennom noden din. For hver videresending ser vi vanligvis :





  - Timestamp,
  - beløpet som er rutet (i Sats),
  - den **opptjente** avgiften på denne videresendingen (i Sats er dette differansen mellom det du mottok på den innkommende kanalen og det du sendte på den utgående),
  - de innkommende og utgående kanalene som brukes (ofte identifisert av motpartens alias eller kanal-ID).
  - status (normalt *fullført*, eller feil hvis en videresending mislyktes underveis).





- **Aggregert statistikk**: ThunderHub beregner og viser øverst på siden totalsummer og statistikk over en gitt periode (f.eks. siste 24 timer, 7 dager osv., noen ganger konfigurerbar).



Kort sagt gir Forwards-delen en **oversikt i sanntid over Lightning-nodens rutingsaktivitet**. Sammen med seksjonene Channels og Rebalance utgjør dette en komplett pakke for optimalisering av noden din: Channels/Rebalance for likviditet, Forwards for å observere resultater (strømmer og fortjeneste).



### Kjede



Seksjonen **Chain** tilsvarer Bitcoin On-Chain-porteføljeadministrasjon av LND-noden din. Med denne Interface kan du vise og administrere Bitcoin-midler, som brukes til å åpne kanaler eller motta midler fra lukkede kanaler.



![Gestion du portefeuille on-chain](assets/fr/16.webp)



I Chain finner du :





- Balance On-Chain: Viser den totale BTC-saldoen som er tilgjengelig i Wallet LND.





- **Liste over UTXOer:** Vis alle ubrukte utganger (UTXO) med beløp, bekreftelser, Address og format for hver utgang.





- **Transaksjonshistorikk:** Detaljert tabell over alle Bitcoin-transaksjoner med type (inn/ut), dato, beløp, kostnader, bekreftelser, inkluderingsblokk, adresser og txid.



### Amboss



ThunderHub integreres med **Amboss**-plattformen (amboss.space), som tilbyr detaljert informasjon om Lightning-noder, en markedsplass for likviditet og nyttige funksjoner som sikkerhetskopiering av krypterte kanaler og overvåking av tilgjengelighet.



![Intégration Amboss avec ses options](assets/fr/17.webp)



I ThunderHub kan du i Amboss-delen **koble** noden din til Amboss-kontoen din:





- **Ghost Address:** Sett opp en **personlig Lightning Address** for noden din, for å forenkle innkommende betalinger.





- Automatisk sikkerhetskopiering av kanaler:** Flaggskipfunksjon for kryptert sikkerhetskopiering av kanaler** (SCB-filer) på Amboss. Aktiver **Amboss Auto Backup = Ja** i innstillingene for å automatisk sende krypterte sikkerhetskopieringsoppdateringer hver gang du bytter kanal. I tilfelle en feil, vil du kunne gjenopprette pengene dine takket være denne eksterne sikkerhetskopien.





- **Helsesjekker:** Aktiver **Amboss Healthcheck = Yes** for å få noden til å sende regelmessige pinger til Amboss. Du vil motta varsler hvis noden ser ut til å være frakoblet.





- Andre funksjoner: Automatisk saldopush, **Magma/Hydro**-integrasjon (likviditetsmarkedsplass) og tilgang til detaljert ytelsesstatistikk.



Amboss-integrering legger til en viktig **sikkerhets-Layer** med automatisk ekstern sikkerhetskopiering og tilgjengelighetsovervåking, som er tilgjengelig direkte fra ThunderHub.



### Verktøy



Avsnittet **Verktøy** samler ulike avanserte verktøy for administrasjon av noden. Her er de viktigste Elements:



![Interface des outils disponibles](assets/fr/18.webp)





- **Sikkerhetskopier:** Administrer sikkerhetskopier av kanalene dine manuelt (SCB). ThunderHub lar deg **laste ned den komplette sikkerhetskopifilen** av kanalene dine (alternativ "Backup all channels -> Download"). Oppbevar denne `channel-all.bak`-filen på et trygt sted - den er viktig for å gjenopprette pengene dine i tilfelle en krasj. Du kan også **importere** en sikkerhetskopifil når du omplasserer en node.





- **Regnskap:** Eksportverktøy for økonomiske rapporter, inkludert opptjente/betalte gebyrer og volumer som er rutet over en gitt periode.
- **Signerte meldinger:** Signer eller verifiser meldinger med noden din for å bevise Ownership fra Lightning-noden din via kryptografisk signatur.
- Makroner (Bakeri-seksjonen):** Administrer LND** makroner for å opprette tilpasset tilgang. Interface "Bakeri" lar deg velge nøyaktig hver tillatelse: "Legg til eller fjern jevnaldrende", "Opprett kjedeadresser", "Opprett fakturaer", "Opprett makroner", "Avled nøkler", "Hent tilgangsnøkler", "Hent kjedetransaksjoner", "Hent fakturaer", "Hent Wallet-info", "Hent betalinger", "Hent jevnaldrende", "Betal fakturaer", "Tilbakekall tilgangsadresser", "Send til kjedeadresser", "Signer byte", "Signer meldinger", "Stopp daemon", "Verifiser byte-signatur", "Verifiser meldinger" osv. Hver tillatelse kan aktiveres individuelt med "Ja/Nei"-knappene for å lage en skreddersydd makron.
- **Systeminformasjon:** Visning av Wallet-versjon og aktiverte RPC-er.



Kort sagt samler Tools-delen avanserte administrasjonsfunksjoner - sikkerhetskopiering, regnskap, sikkerhet og tilgangsstyring - i en samlet Interface.



### Bytte



ThunderHubs **Swap**-fane lar deg bytte Lightning-satoshier til Bitcoin On-Chain via Boltz-tjenesten. Denne funksjonen er nyttig for å "dumpe" overflødig Lightning-likviditet til kanalen uten å stenge en kanal.



![Interface de swap via Boltz](assets/fr/19.webp)



Prosessen er enkel:





- **Beløp**: Definer beløpet som skal byttes
- **Address**: Angi Bitcoin-mottak Address
- **Utførelse**: ThunderHub kommuniserer med Boltz for automatisk å behandle Exchange



**Fordeler:**




- Ikke-forvaringstjeneste (ingen kontantforvaring)
- Bevar de eksisterende kanalene dine
- Brukervennlig integrert Interface



Boltz tar en liten provisjon, og du betaler standard Bitcoin transaksjonsgebyr. ThunderHub viser alle kostnader før bekreftelse.



### Statistikk



ThunderHubs **Stats**-seksjon tilbyr **avansert statistikk** på Lightning-noden din for å analysere ytelse og optimalisere ruting.



![Statistiques du nœud via Amboss](assets/fr/20.webp)



Denne delen er viktig for å optimalisere kostnadene, identifisere vellykkede kanaler og planlegge utvidelsen av noden.



## Konklusjon



**ThunderHub** har etablert seg som det essensielle verktøyet for enkel administrasjon av en Lightning **LND** node. Denne moderne Interface tilbyr alle de viktigste funksjonene: kanaladministrasjon, betalinger, overvåking, med avanserte funksjoner som automatisert rebalansering og Amboss-integrasjon.



**Viktige fordeler:**




- Interface elegant og intuitiv
- Kraftige verktøy (rebalansering, Boltz-bytter, automatisk sikkerhetskopiering)
- Kompatibel med Umbrel, Voltage, RaspiBlitz og andre distribusjoner



ThunderHub demokratiserer avansert Lightning-nodeadministrasjon, og gjør tilgjengelig det som tidligere krevde komplekse tekniske kommandoer. Enten du er nybegynner eller erfaren operatør, lar ThunderHub deg effektivt administrere Lightning-noden din via en moderne, omfattende Interface.



## Ressurser



**Offisielle lenker:**




- **Offisiell nettside:** [thunderhub.io](https://thunderhub.io)
- **Dokumentasjon:** [docs.thunderhub.io](https://docs.thunderhub.io)
- **GitHub-kildekode:** [github.com/apotdevin/thunderhub](https://github.com/apotdevin/thunderhub)