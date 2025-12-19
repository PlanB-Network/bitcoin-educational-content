---
name: Ride The Lightning (RTL)
description: Bruk Ride The Lightning (RTL) til å administrere Lightning-noden din
---
![cover](assets/cover.webp)


## 1. Innledning



**Ride The Lightning (RTL)** er en komplett Interface-nettapplikasjon for administrasjon av en Lightning Network-node. Denne selvbetjente webapplikasjonen tilbyr en Lightning-**"cockpit"** som er tilgjengelig fra nettleseren din. RTL fungerer med alle større Lightning-implementeringer (LND, Core Lightning/CLN og Eclair) og gir deg full kontroll over noden og kanalene dine. RTL er gratis og har åpen kildekode (MIT-lisens) og er integrert som standard i mange nøkkelferdige nodeløsninger (RaspiBlitz, MyNode, Umbrel osv.).



**Uten en grafisk Interface kan Lightning-noder kun administreres via brukervennlige CLI-kommandoer. RTL forenkler disse operasjonene med en ergonomisk Interface. Her er de viktigste bruksområdene:**





- Se kanalene og noden - Dashbordet viser On-Chain-saldo, Lightning-likviditet (lokal/fjern), synkroniseringsstatus, nodealias og mer. Du kan se kanallisten, kapasitet, lokal/fjerndistribusjon og status. RTL tilbyr kontekstsensitive dashbord for å analysere aktivitet fra ulike vinkler.





- **Lynrask kanaladministrasjon** - åpne/lukk kanaler med noen få klikk. Med RTL kan du koble deg til en motpart og åpne en kanal uten en kommando. Du kan justere rutingavgifter, se saldoscore eller starte en sirkulær rebalansering for å rebalansere midler mellom kanaler.





- **Spor og utfør betalinger** - RTL håndterer Lightning-transaksjoner: send betalinger via fakturaer, generate-fakturaer for mottak, spor transaksjoner (betalinger, ruting) med detaljert historikk. Interface analyserer også ruting for å se hvilke betalinger som går gjennom noden din.





- **Wallet On-Chain-administrasjon og sikkerhetskopiering** - On-Chain-fanen lar deg generate-adresser og sende transaksjoner. RTL gjør det enkelt å lagre kanaler ved å eksportere SCB-filen for LND, med automatisk oppdatering for hver kanalendring.



Kort sagt er RTL et **kraftig dashbord for Lightning Network**, som tilbyr en pedagogisk Interface for daglig styring av noden din. Denne veiledningen vil veilede deg gjennom installasjon og bruk for å administrere kanalene og betalingene dine.



## 2. Teknisk drift av RTL



![Schéma de l'architecture RTL : interface responsive compatible avec tous les appareils, frontend Angular, serveur Node (port 3000), connecté aux API REST de LND](assets/fr/01.webp)



Før vi går i gang med det praktiske, er det nyttig å forstå **hvordan RTL samhandler med Lightning-noden** på et teknisk nivå.



**Generell arkitektur:** RTL er en webapplikasjon bygget med Node.js (backend) og Angular (frontend). Konkret kjører RTL som en liten lokal webserver (på port 3000 som standard) som kommuniserer med Lightning-implementeringen din via API-ene. Avhengig av hvilken type :





- Med **LND** bruker RTL LNDs REST API (port 8080) til å utføre Lightning-kommandoer. Tilkoblingen er sikret med TLS og krever LNDs **admin macaroon**-fil for autentisering.





- Med **Core Lightning (CLN)** bruker RTL enten REST API som leveres av *c-lightning-REST*, eller en **access rune** via `commando`-plugin. Løsninger som Umbrel konfigurerer automatisk disse Elements.





- Med **Eclair** kobler RTL seg til Eclair REST API ved hjelp av det konfigurerte autentiseringspassordet.



**Konfigurasjon og sikkerhet:** RTL konfigureres via en JSON-fil (`RTL-Config.json`) der du definerer nettporten, tilgangspassordet og tilkoblingsinformasjon til noden din. Interface-nettverket er beskyttet av en innlogging/passord (standard `passord` som kan endres) og støtter 2FA. Som standard kjører RTL som lokal HTTP (`http://localhost:3000`), men for ekstern tilgang må du alltid bruke en sikker tilkobling (HTTPS via reverse-proxy, Tor eller VPN).



Kort sagt er RTL en tilleggskomponent som kobles til noden din via sikre API-er, krever passende tilgangstokener og tilbyr sin egen sikkerhet Layer. Denne modulære arkitekturen gjør at du til og med kan administrere **flere Lightning-noder med én enkelt RTL-instans**.



## 3. RTL-installasjon



Siden RTL distribueres som programvare med åpen kildekode, finnes det flere måter å installere det på systemet ditt på. I dette avsnittet tar vi for oss to hovedmetoder: manuell installasjon og installasjon via Umbrel.



### Manuell metode



Manuell installasjon er egnet hvis du ønsker å beholde finkornet kontroll, eller hvis du integrerer RTL i en tilpasset konfigurasjon. Fremgangsmåten nedenfor gjelder for en LND-node som kjører Linux (f.eks. Raspberry Pi eller VPS som kjører Ubuntu/Debian), men er lik for CLN/Eclair.



**Forutsetning:** sørg for at du har en **synkronisert** Bitcoin-node og en fungerende Lightning-node (LND, CLN eller Eclair) på maskinen. RTL inneholder ikke en Lightning-node i seg selv, men kobler seg til en eksisterende node. Du trenger også **Node.js** installert (versjon 14+ anbefales). Du kan sjekke med `node -v` eller installere Node fra det offisielle nettstedet (https://nodejs.org/en/download/) eller pakkebehandleren din.



De viktigste installasjonsfasene er :



**Last ned RTL-kode**: Klon det offisielle RTL GitHub-depotet i katalogen du ønsker. For eksempel



```bash
git clone https://github.com/Ride-The-Lightning/RTL.git
cd RTL
```



**Installer avhengigheter**: RTL er en Node.js-applikasjon, så du må installere de nødvendige modulene. I RTL-mappen kjører du :



```bash
npm install --omit=dev --legacy-peer-deps
```



Denne kommandoen installerer de nødvendige NPM-pakkene (ignorerer utviklingsavhengigheter). Alternativet `--legacy-peer-deps` anbefales for å unngå mulige Node-avhengighetskonflikter.



**RTL-Config**: Når avhengighetene er på plass, klargjør du konfigurasjonsfilen. Kopier/gi nytt navn til filen `Sample-RTL-Config.json` i prosjektets rot til `RTL-Config.json`. Åpne den i :





- **UI-passord**: Velg et sikkert passord og skriv det inn i `multiPass` (i stedet for standard `"passord"`).
- **Port**: standard `3000`. Du kan endre den hvis denne porten allerede er opptatt på maskinen din.
- **Node**: I delen `nodes[0]` justerer du parametrene for noden din:
     - `lnNode`: et beskrivende navn for noden (f.eks. `"LND Node Maison"`).
     - lnImplementation`: `"LND"` (eller `"CLN"`/`"ECL"` etter behov).
     - Under `autentisering`:
       - macaroonPath`: angi den fullstendige banen til mappen som inneholder LNDs macaroon-administrator.
       - `configPath`: sti til nodens konfigurasjonsfil (`LND.conf` for LND).
     - Under `innstillinger`:
       - `fiatConversion`: Sett til `true` hvis du ønsker konvertering av fiat-valuta.
       - `unannouncedChannels`: Sett til `true` for å se uanmeldte kanaler.
       - themeColor` og `themeMode`: Interface-tilpasning.
       - channelBackupPath`: bane for sikkerhetskopiering av LND-kanaler.
       - `lnServerUrl`: URL-adressen til Lightning-noden (f.eks. `https://127.0.0.1:8080`).



**Start RTL-serveren**: I RTL-mappen kjører du :



```bash
node rtl
```



Programmet starter opp og kan nås på `http://localhost:3000`.



**(Valgfritt) Kjør RTL som en tjeneste**: For automatisk oppstart oppretter du en systemd :



For å gjøre dette:




- Åpne en terminal på maskinen din.
- Opprett en ny servicefil med følgende kommando (erstatt `nano` med din foretrukne editor):


```bash
sudo nano /etc/systemd/system/RTL.service
```




- Kopier og lim inn innholdet nedenfor i denne filen:



```ini
[Unit]
Description=Ride The Lightning web UI
Wants=lnd.service
After=lnd.service

[Service]
ExecStart=/usr/bin/node /chemin/vers/RTL/rtl
User=<votre_user>
Restart=always
TimeoutSec=120
RestartSec=30

[Install]
WantedBy=multi-user.target
```





- Erstatt `/path/to/RTL/rtl` med den faktiske banen til `rtl`-filen på maskinen din, og `<your_user>` med Linux-brukernavnet ditt.
- Lagre og lukk filen.
- Last inn systemd-konfigurasjonen på nytt:


```bash
sudo systemctl daemon-reload
```




- Aktiver og start RTL-tjenesten:


```bash
sudo systemctl enable RTL
sudo systemctl start RTL
```



RTL vil nå starte automatisk hver gang maskinen startes på nytt. Du kan sjekke statusen med :


```bash
sudo systemctl status RTL
```



### Installasjon via Umbrel



Hvis du bruker [Umbrel] (https://getumbrel.com), er RTL-installasjonen mye enklere:





- Få tilgang til Interface Umbrel (vanligvis via `http://umbrel.local`)
- Gå til **App Store**
- Søk etter "Ride The Lightning"



**Viktig merknad: Det finnes to separate RTL-applikasjoner i Umbrel App Store:**




- **Ride The Lightning** (for LND): for bruk med Umbrels standard Lightning-node (LND).
- **Ride The Lightning (Core Lightning)**: brukes bare hvis du har installert *Core Lightning*-applikasjonen på Umbrel og ønsker å administrere denne noden med RTL.



*Hver RTL-versjon er forhåndskonfigurert for dialog med den tilsvarende implementasjonen (LND eller Core Lightning). Hvis du ikke har endret Lightning-noden din, velger du bare den klassiske LND-versjonen*



![Fiche de l'application Ride The Lightning dans Umbrel : présentation de l'app avec captures d'écran et bouton violet "Install" en haut à droite](assets/fr/02.webp)





- Klikk på **Install**



![Fenêtre d'affichage du mot de passe par défaut après installation de RTL dans Umbrel, avec bouton "Open Ride The Lightning"](assets/fr/03.webp)



**Viktig:** Etter installasjonen viser RTL et skjermbilde med standardpassordet. **Kopier og lagre dette passordet** - du trenger det for å logge på Interface RTL. Dette passordet vises hver gang RTL starter opp, helt til du merker av for alternativet "Don't show it again" (ikke vis det igjen).



Umbrel tar seg automatisk av :




- Last ned og konfigurer RTL
- Konfigurere tilgang til Lightning-noden
- Administrer oppdateringer
- Sikre tilgangen til Interface



Når applikasjonen er installert, vises den i *Apps*-menyen på Umbrel. Klikk på **Ride The Lightning** for å starte den.



![Écran de connexion RTL via Umbrel : champ de mot de passe avec logo du cheval en haut à gauche, bouton "Login"](assets/fr/04.webp)



På påloggingsskjermen skriver du inn passordet du kopierte tidligere. Når du er logget inn, vil Interface web RTL være tilgjengelig direkte fra Umbrel-dashbordet, uten behov for ytterligere konfigurasjon!



## 4. Introduksjon og bruk av Interface RTL



Nå som RTL er oppe og går, skal vi se nærmere på Interface-nettverket og de viktigste funksjonene. Vi går gjennom de ulike delene av applikasjonen for å gi deg en fullstendig oversikt.



### Hovedkontrollpanelet



![Tableau de bord RTL : solde Lightning, solde on-chain, capacité de liquidité entrante/sortante et création de facture](assets/fr/05.webp)



Så snart du logger deg på, får du tilgang til **hovedinstrumentbordet**, som gir deg en oversikt over Lightning-noden din. Denne siden samler viktig informasjon:




- Din totale Lightning-saldo
- On-Chain-saldo tilgjengelig
- Fordelingen av likviditeten din (innkommende/utgående)
- Rask tilgang til å sende og motta Satss via Lightning-noden din



### Fondsforvaltning On-Chain



![Onglet "On-chain" actif dans RTL : solde Bitcoin (en sats, BTC, USD), et liste des transactions avec type d'adresse Taproot](assets/fr/06.webp)



Med **On-Chain**-fanen kan du administrere bitcoinsene dine direkte i hovedkjeden:




- Saldo vises i ulike enheter (Sats, BTC, USD)
- Fullstendig liste over transaksjoner
- Address generasjon Taproot (P2TR), P2SH (NP2WKH) eller Bech32 (P2WKH)
- UTXO-administrasjon, mottak og sending av bitcoins



### Lightning: detaljert presentasjon av undermenyer



Interface RTL har en sidemeny dedikert til Lightning Network, som samler alle de viktigste funksjonene for å administrere noden din. Her er detaljene for hver undermeny, i samme rekkefølge som på skjermbildet:



#### 1. Kolleger/kanaler



![Vue de gestion des canaux Lightning (onglet "Peers/Channels" ouvert)](assets/fr/07.webp)



Denne undermenyen gir deg mulighet til å :




- Se listen over tilkoblede kolleger og Lightning-kanaler som er åpne eller venter.
- Legg til en ny peer (koble til en annen Lightning-node).
- Åpne, lukk eller administrer eksisterende kanaler.
- Se detaljer om hver kanal: kapasitet, lokale/fjerne saldoer, status, handelshistorikk, saldoscore osv.



#### 2. Transaksjoner



![Historique des transactions Lightning (onglet "Transactions" > "Payments")](assets/fr/08.webp)



I denne undermenyen kan du :




- Send Lightning-betalinger (via Invoice).
- generate og administrer fakturaer for å motta betalinger.
- Se hele historikken over sendte og mottatte betalinger, med detaljer (beløp, dato, status, gebyrer, antall overhoppinger osv.).



#### 3. Ruting



Denne undermenyen viser :




- Betalinger som videresendes av noden din til andre Lightning Network-brukere.
- Routing-statistikk: antall videresendte transaksjoner, opptjente gebyrer, oppståtte feil.
- Eksporterbar historikk for avansert analyse.



#### 4. Utsettelser



Denne undermenyen tilbyr :




- Detaljerte rapporter om aktiviteten til Lightning-noden din.
- Diagrammer og tabeller over kanaler, betalinger, avgifter, kapasitet osv.
- Verktøy for bedre forståelse av nodens ytelse.



#### 5. Grafoppslag



Denne undermenyen gir deg mulighet til å :




- Utforsk topologien til Lightning Network.
- Søk etter bestemte noder eller kanaler.
- Innhent informasjon om tilkoblingsmuligheter og generell nettverkskapasitet.



#### 6. Signer/bekreft



Denne undermenyen tilbyr :




- Muligheten til å signere en melding med nodens nøkkel (bevis på Ownership).
- Signaturverifisering for å autentisere meldinger fra andre noder.



#### 7. Sikkerhetskopiering



Denne undermenyen er dedikert til sikkerhetskopiering:




- Eksporter sikkerhetskopifil for kanal (SCB for LND).
- Gjenopprett konfigurasjon eller kanaler om nødvendig.
- Tips for å sikre sikkerhetskopiene dine.



#### 8. Knutepunkt/nettverk



![Vue d'ensemble du nœud Lightning (onglet "Node/Network")](assets/fr/09.webp)



I denne undermenyen finner du :




- En fullstendig oversikt over Lightning-nodens status: alias, versjon, farge, synkroniseringsstatus.
- Statistikk over kanaler (aktive, ventende, stengte), total kapasitet, tilkobling.
- Informasjon om den globale Lightning Network og din nodes posisjon i den.



### Tjenester: Boltz Swaps



![Interface de gestion des swaps avec Boltz (onglet "Services" > "Boltz")](assets/fr/10.webp)



Boltz er en personvernvennlig, ikke-frihetsberøvende Exchange-tjeneste som konverterer bitcoins mellom Lightning Network og Blockchain Bitcoin (On-Chain). Den tilbyr to typer operasjoner: Omvendt Submarine Swap (**Swap Out**) og Submarine Swap (**Swap In**).



#### Bytte ut (omvendt ubåtbytte)



Swap Out konverterer tilgjengelige Satss på Lightning Network til On-Chain bitcoins. Denne mekanismen er nyttig når en node går tom for innkommende kapasitet, eller når du ønsker å få tilbake midler fra en On-Chain Address. Prosessen fungerer som følger:




- Brukeren velger et beløp som skal veksles
- Noden sender en Lightning-betaling til Boltz
- I Exchange blokkerer Boltz et tilsvarende beløp i On-Chain bitcoins
- Når transaksjonen er bekreftet, kan brukeren gjøre krav på pengene ved å avsløre en hemmelighet som ble brukt i byttehandelen



Denne prosessen er ikke frihetsberøvende, og Boltz oppbevarer aldri brukerens midler.


![Double capture des étapes de configuration d'un swap-out](assets/fr/11.webp)



#### Swap In (Submarine Swap)



Swap In, derimot, gjør det mulig å tilbakeføre On-Chain-midler til Lightning Network. Dette er spesielt nyttig for å gjenopprette utgangskapasiteten på kanalene dine. Fremgangsmåten er som følger:




- Brukeren sender bitcoins til en spesifikk Address generert av Boltz
- Disse midlene kan bare frigjøres av Boltz hvis han betaler en Lightning Invoice generert av brukerens node
- Når Invoice er betalt, er midlene tilgjengelige på Lightning-kanalen, noe som øker nodens utgangskapasitet



![Configuration d'un swap-in](assets/fr/12.webp)



Disse to mekanismene gjør det mulig å styre likviditeten i Lightning-kanalen på en effektiv måte, samtidig som brukeren beholder råderetten over midlene sine.



### Konfigurasjon og tilpasning



![Écran de configuration du nœud (onglet "Node Config")](assets/fr/13.webp)



I **Node Config**-fanen kan du tilpasse opplevelsen din:




- Aktivering av uannonserte kanaler
- Tilpass salgsdisplayet
- Block explorer-konfigurasjon
- Justering av Interface



### Dokumentasjon og hjelp



![Section d'aide de RTL (onglet "Help")](assets/fr/14.webp)



Til slutt tilbyr **Hjelp**-delen omfattende dokumentasjon om :




- Opprinnelig konfigurasjon
- Ledelse av kolleger og kanaler
- Betalinger og transaksjoner
- Sikkerhetskopiering og gjenoppretting
- Rapporter og statistikk
- Underskrifter og bekreftelser
- Node- og applikasjonsparametere



Med denne omfattende Interface kan du administrere Lightning-noden effektivt, fra grunnleggende operasjoner til avanserte funksjoner, alt i en intuitiv og velorganisert Interface.



## 5. Avanserte brukstilfeller og sikkerhet



I denne delen får du vite hva du trenger å vite for å gå videre med RTL og sikre Lightning-noden:



### Overvåking og feilsøking



For å overvåke noden din kan du eksportere RTL-data (logger, CSV) og vise dem i verktøy som Grafana. Hvis det oppstår et problem (blokkert betaling, inaktiv kanal), kan du se i LND/CLN-loggene og bruke diagnosekommandoene (`lncli listchannels`, `lncli pendingchannels` osv.). RTL tilbyr også Interface-logger for overvåking av rutinghendelser.



### Sikker ekstern tilgang



Utsett aldri RTL direkte på Internett. Gi preferanse til :




- **VPN** (f.eks. Tailscale) for privat, kryptert tilgang
- **Tor** for sikker, anonym tilgang
- Omvendt proxy **HTTPS** (Nginx/Caddy) bare hvis du vet hvordan du konfigurerer den



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### God sikkerhetspraksis





- **Beskytt tilgangen din**: Del aldri admin.macaroon eller RTL-passordet ditt. Begrens tillatelser på sensitive filer.
- **Regelmessig sikkerhetskopiering**: Eksporter kanalens sikkerhetskopifil (SCB) etter hver endring, og lagre den utenfor noden.
- **Oppdateringer**: Hold RTL, noden din og Umbrel oppdatert med de nyeste sikkerhetsoppdateringene.
- **Konfidensialitet**: anonymiser logger og skjermbilder før du deler dem. Del aldri saldoer eller peer-lister offentlig.
- **Enkel tilgang**: RTL er ikke flerbruker. Ikke del administratortilgang. For skrivebeskyttet tilgang, bruk en dedikert macaroon om nødvendig.



Ved å følge disse prinsippene kan du begrense risikoen og beholde kontrollen over Lightning-noden.



## 7. Konklusjon



**Ride The Lightning** er et viktig verktøy for effektiv administrasjon av en Bitcoin/Lightning-node, enten du er nybegynner eller en avansert bruker. Det gir en tydelig Interface for å kontrollere kanaler, betalinger og nodehelse, samtidig som det gir deg en dypere forståelse av Lightning Network.



RTL skiller seg ut med sin kompatibilitet med flere implementeringer, sine avanserte funksjoner (rebalansering, swaps, rapporter) og sin pedagogiske tilnærming. For enkle behov er Interface Umbrel eller en Wallet mobil tilstrekkelig, men RTL er perfekt for aktiv, optimalisert nodeadministrasjon.



For å finne ut mer :




- Offisielt nettsted for RTL: https://www.ridethelightning.info/
- GitHub RTL: https://github.com/Ride-The-Lightning/RTL
- **Reddit r/lightningnetwork**: [r/lightningnetwork](https://www.reddit.com/r/lightningnetwork) - Tekniske diskusjoner, prosjektannonseringer, tilbakemeldinger og utdanningsressurser
- **Umbrel Community Forum**: [community.getumbrel.com](https://community.getumbrel.com) - Offisielt forum med egen Bitcoin/Lightning-seksjon, guider og løsninger på vanlige problemer
- **Lightning Network-utviklere**: [github.com/lightning](https://github.com/lightning) - Offisielt GitHub-depot for å følge utviklingen og bidra med kildekode
- Stack Exchange **Bitcoin**: [Bitcoin.stackexchange.com](https://Bitcoin.stackexchange.com) - Tekniske spørsmål og svar med utviklere og avanserte brukere



Kort sagt gir RTL deg full kontroll over Lightning-noden din, i en moderne Interface med alle funksjoner.



**Kilder :** RTLs offisielle nettsted; RTL GitHub; Umbrel App Store; Umbrel Community; Plan ₿ Academy-ressurser.



For å få en dypere forståelse av hvordan Lightning Network fungerer, anbefaler jeg også at du tar dette gratiskurset:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb