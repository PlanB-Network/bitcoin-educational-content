---
name: LNbits Server
description: Installasjon og konfigurasjon av en LNbits-server på Ubuntu VPS med PHOENIXD eller på Umbrel
---

![cover](assets/cover.webp)



LNbits er en Interface-nettapplikasjon med åpen kildekode som forvandler enhver Lightning-backend (LND, Core Lightning, PHOENIXD) til en komplett tjenesteplattform. Med denne selvbetjente løsningen kan du administrere flere Lightning-porteføljer isolert, distribuere salgssteder, opprette donasjonssystemer eller faktureringstjenester, samtidig som du beholder full kontroll over midlene dine.



Denne veiledningen dekker to installasjonsmetoder: **VPS Ubuntu med PHOENIXD** (lettvektsløsning uten en full Bitcoin-node) og **Umbrel** (integrering med din eksisterende LND-node). I motsetning til Plan B Networks generelle LNbits-veiledning, som dekker konsepter og utvidelser, fokuserer denne veiledningen på trinnvise tekniske installasjonsprosedyrer.



## Hva er LNbits?



LNbits er et Lightning-regnskapssystem utviklet i Python (FastAPI) som kobles til en eksisterende backend (LND, Core Lightning, PHOENIXD). I motsetning til tradisjonelle Lightning-noder tilbyr LNbits en tilgjengelig Interface, slik at du kan administrere flere isolerte porteføljer med egne API-nøkler. Du kan opprette underkontoer for familien, ansatte eller prosjekter, uten å gi dem tilgang til alle midlene dine.



Den frikoblede arkitekturen lagrer informasjon i SQLite (standard) eller PostgreSQL (produksjon), mens midlene fortsatt administreres av Lightning-backend. Denne separasjonen garanterer portabilitet: Du kan migrere fra PHOENIXD til LND uten å miste brukerdataene dine.



## Viktige funksjoner



LNbits tilbyr et allsidig **utvidelsessystem**: TPoS (salgssted), Paywall (inntektsgenerering av innhold), Events (billettering), LndHub (server for BlueWallet), Bolt Cards (NFC-betalinger), Split Payments (automatisk distribusjon) og User Manager (brukeradministrasjon med autentisering).



Dashbordet** viser saldoer i sanntid, transaksjonshistorikk og faktureringsverktøy. Hver Wallet har en unik URL som inneholder API-nøklene, noe som gir tilgang uten tradisjonell innlogging. API-nøkkelsystemet** med tre nivåer (admin, Invoice, skrivebeskyttet) gir detaljert kontroll over tillatelser for sikre integrasjoner.



LNbits implementerer **LNURL** (LNURL-pay, LNURL-Withdraw, LNURL-auth) og støtter **Lightning Address**, noe som garanterer kompatibilitet med moderne Lightning-lommebøker og gjør det enklere å distribuere profesjonelle tjenester.



## Støttede plattformer



**Ubuntu VPS**: Lettvektsløsning uten full Bitcoin node. Forutsetninger: 1 vCPU, 1-2 GB RAM, Ubuntu 22.04 LTS, Python 3.10+, Git, UV. HTTPS + domenenavn kreves for offentlig eksponering (LNURL-tjenester).



**Umbrel**: Enkel installasjon fra App Store. Forutsetning: funksjonell Umbrel-node med synkronisert LND og åpne kanaler. Automatisk konfigurasjon.



Nedenfor finner du lenker til våre veiledninger for Umbrel og Umbrel LND:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Installasjon på Ubuntu VPS med PHOENIXD



### Trinn 1: Sikring av VPS-serveren



**Før du installerer *, må du sikre Ubuntu VPS-serveren din i henhold til alle kunstens regler. Dette trinnet er **kritisk** for å beskytte infrastrukturen din og dine Lightning-midler.



Her er en detaljert veiledning som hjelper deg med å komme i gang: **[Initial Ubuntu server configuration - Step-by-step guide](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/)** av Daniel P. Costas.



Denne veiledningen dekker brukerkonfigurasjon, sikker SSH, brannmur (UFW), fail2ban, automatiske oppdateringer og god praksis for systemsikkerhet.



### Trinn 2: Installere PHOENIXD



Når serveren din er sikret, må du installere og konfigurere PHOENIXD. Plan B Network tilbyr en komplett veiledning som dekker installasjon, generering av seed og konfigurasjon av systemd-tjenesten:



https://planb.academy/tutorials/node/lightning-network/phoenixd-beb86edd-f9c0-4bec-ad36-db234c88e7b1

Når PHOENIXD er oppe og går (sjekk med `./Phoenix-CLI getinfo`), legg merke til **HTTP-passordet** i `~/.Phoenix/Phoenix.conf` - du trenger det for å koble LNbits til PHOENIXD.



### LNbits-distribusjon



Installer UV og klon LNbits :


```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
git clone https://github.com/lnbits/lnbits.git && cd lnbits
uv sync --all-extras
```



Konfigurer PHOENIXD-backenden:


```bash
cp .env.example .env && nano .env
```



Legg til i `.env` :


```
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://127.0.0.1:9740
PHOENIXD_API_PASSWORD=<mot-de-passe-phoenix.conf>
```



Test med `uv run lnbits --host 0.0.0.0 --port 5000` og opprett deretter en systemd-tjeneste med `Wants=PHOENIXD.service`.



## Førstegangsoppsett og første gangs bruk



### Aktivering av SuperUser



Aktiver Interface-administratoren i `.env` :


```
LNBITS_ADMIN_UI=true
```



Start LNbits på nytt (`sudo systemctl restart lnbits`) og hent SuperUser-ID-en:


```bash
cat ~/lnbits/data/.super_user
```



Gå til `http://<IP-VPS>:5000/Wallet?usr=<SuperUserID>` for administrasjonspanelet. I menyen "Server" kan du konfigurere finansieringskilder, utvidelser og brukerkontoer.



### Sikker kontoopprettelse



**Viktig for offentlig eksponering**: Hvis du eksponerer LNbits-instansen din på et offentlig domenenavn som er tilgjengelig fra Internett, er det **kritisk** å deaktivere fri opprettelse av brukerkontoer.



Fra SuperUser-administrasjonen Interface går du til "Innstillinger" og deretter til delen "Brukeradministrasjon". Her finner du alternativet "Tillat opprettelse av nye brukere".



![Gestion des utilisateurs - Sécurité](assets/fr/17.webp)



**For en offentlig utstilling med domenenavn** :




- Du må deaktivere** alternativet "Tillat opprettelse av nye brukere"
- Uten denne beskyttelsen kan hvem som helst på Internett opprette en konto på din instans
- En angriper kan opprette kontoer og bruke likviditeten til LIGHTNING NODE uten at du vet om det
- Du må opprette brukerkontoer manuelt fra Interface SuperUser



**Kun til lokal bruk** :




- Dette alternativet er mindre kritisk hvis forekomsten bare er tilgjengelig lokalt (http://localhost:5000)
- Det er imidlertid en god sikkerhetsrutine å deaktivere dette alternativet



Når konfigurasjonen er klar, er det bare SuperUser-administratoren som kan opprette nye brukerkontoer via Interface "Users". Denne tilnærmingen garanterer total kontroll over hvem som har tilgang til Lightning-infrastrukturen og hvem som kan bruke midlene dine.



### Åpne den første kanalen



PHOENIXD administrerer automatisk kanaler via automatisk likviditet. generate en Lightning Invoice på ~ 30 000 Sats fra LNbits og betaler den fra en annen Wallet. PHOENIXD åpner automatisk en kanal til ACINQ. Åpningsgebyret (~20-23k Sats) trekkes fra, den gjenværende saldoen (~7-10k Sats) vises etter bekreftelse fra On-Chain.



Sjekk status med `./Phoenix-CLI getinfo`. Vurder deretter å deaktivere auto-liquidity (`auto-liquidity=off` i `Phoenix.conf`) for å kontrollere kanalåpninger.



### Offentlig visning og HTTPS



**Viktig**: HTTPS er obligatorisk for offentlig visning (API-nøkkelsikkerhet + LNURL-kompatibilitet). Hopp over dette trinnet kun for lokal bruk.



**Caddy (anbefalt)**: automatisk SSL. `sudo apt install -y caddy`, rediger `/etc/caddy/Caddyfile` :


```
votre-domaine.com {
reverse_proxy 127.0.0.1:5000
}
```


Start på nytt: `sudo systemctl restart caddy`.



**Nginx** : Mer kontroll. Installer `nginx certbot python3-certbot-nginx`, opprett `/etc/nginx/sites-available/lnbits` :


```nginx
server {
listen 80;
server_name votre-domaine.com;
location / {
proxy_pass http://127.0.0.1:5000;
proxy_set_header Host $host;
proxy_set_header X-Forwarded-Proto $scheme;
}
}
```


Aktiver: `sudo LN -s /etc/nginx/sites-available/lnbits /etc/nginx/sites-enabled/ && sudo nginx -t && sudo systemctl reload nginx && sudo certbot --nginx -d your-domain.com`



Legg til i `.env`: `FORWARDED_ALLOW_IPS=*`



## Installasjon av paraply



### Distribusjon fra App Store



Gå til Umbrel App Store, søk etter "LNbits", og klikk på "Install".



![Installation LNbits Umbrel](assets/fr/01.webp)



Umbrel sjekker automatisk for nødvendige avhengigheter. LNbits krever LIGHTNING NODE (LND) for å kjøre. Hvis LIGHTNING NODE allerede er i drift, klikker du på "Installer LNbits" for å bekrefte.



![Dépendances LNbits](assets/fr/02.webp)



Umbrel laster ned Docker-imaget, konfigurerer automatisk tilkoblinger med LND og starter containeren (2-5 minutter). Installasjonen foregår helt og holdent i bakgrunnen.



### Innledende SuperUser-konfigurasjon



Ved første oppstart ber LNbits deg om å opprette SuperUser-administratorkontoen. Skriv inn et brukernavn og angi et sikkert passord for å beskytte tilgangen til Interface-administrasjonssystemet.



![Configuration SuperUser](assets/fr/03.webp)



**Viktig**: Denne SuperUser-kontoen har fulle rettigheter på LNbits-forekomsten din. Velg et sterkt passord og oppbevar det trygt.



Når du har opprettet en konto, blir du automatisk ført til hovedadministrasjonsområdet for Interface. Umbrel har allerede satt opp LND som din finansieringskilde - alle Lyn-betalinger vil gå gjennom dine eksisterende kanaler.



### Tilgang til Interface-administrator



I menyen til venstre klikker du på "Innstillinger" for å få tilgang til hele administrasjonspanelet.



![Interface Settings](assets/fr/04.webp)



I delen "Wallets Management" vises nøkkelinformasjon om konfigurasjonen din:




- Finansieringskilde** : LndBtcRestWallet (direkte tilkobling til din LND Umbrel-node)
- Node-saldo** : Total likviditet tilgjengelig i Lightning-kanalene dine
- LNbits-saldo**: Midler allokert til LNbits-systemet (opprinnelig 0 Sats)



Du kan nå utnytte likviditeten til Umbrel-noden din direkte for alle LNbits-lommebøkene du oppretter. Ingen ekstra konfigurasjon er nødvendig - LNbits er oppe og går.



### Brukeradministrasjon



En av LNbits' kraftigste funksjoner er muligheten til å opprette flere uavhengige brukere, hver med passordautentisering og isolerte lommebøker. Denne arkitekturen gjør det mulig å dra nytte av likviditeten til Umbrel-noden din, samtidig som du kan tilby helt isolerte underkontoer for ulike bruksområder: bedrift, familie, ansatte, prosjekter osv.



Klikk på "Brukere" i sidemenyen for å få tilgang til brukeradministrasjon. Klikk på "CREATE ACCOUNT" for å legge til en ny bruker.



![Gestion des utilisateurs](assets/fr/05.webp)



Fyll ut skjemaet for brukeropprettelse:




- Brukernavn**: Innloggingsbrukernavn (eksempel: "Satoshi")
- Angi passord**: Aktiver dette alternativet for å angi et autentiseringspassord
- Passord** og **Passord gjenta**: Angi passordet for denne brukeren



![Création utilisateur satoshi](assets/fr/06.webp)



Valgfrie felt (offentlig nøkkel, e-post, fornavn, etternavn) kan stå tomme for minimal konfigurasjon. Klikk på "CREATE ACCOUNT" for å bekrefte.



![Confirmation utilisateur créé](assets/fr/07.webp)



Den nye brukeren vises nå i listen over brukere med sin unike identifikator og sitt brukernavn.



![Liste des utilisateurs](assets/fr/08.webp)



**Viktig poeng**: Hver bruker kan logge på helt uavhengig av hverandre med sitt eget passord. SuperUser-administratoren beholder full kontroll via Interface-administrasjonsverktøyet.



### Brukeradministrasjon Wallet



Nå som "Satoshi"-brukeren er opprettet, må du tildele ham en Wallet Lightning. Klikk på Wallet-ikonet (det andre ikonet) for den aktuelle brukeren, og deretter på "CREATE NEW Wallet".



![Gestion des wallets](assets/fr/09.webp)



En dialogboks ber deg om å gi Wallet et navn. Skriv inn et beskrivende navn (f.eks. "Wallet Of Satoshi"), og velg visningsvaluta (CUC, USD, EUR osv.).



![Création wallet](assets/fr/10.webp)



Klikk på "CREATE". LNbits genererer øyeblikkelig en fungerende Wallet Lightning for denne brukeren.



![Confirmation wallet créé](assets/fr/11.webp)



Du ser nå de to eksisterende lommebøkene: standard Wallet "LNbits Wallet" som opprettes automatisk, og den nye "Wallet Of Satoshi". For å forenkle brukeropplevelsen kan du slette standard Wallet ved å klikke på sletteikonet (rød søppelbøtte).



![Wallet final unique](assets/fr/12.webp)



"Satoshi"-brukeren har nå en enkelt, tydelig identifisert Wallet. Hver Wallet-bruker opererer helt autonomt, samtidig som den bruker likviditeten til den underliggende LND-noden.



**Nøkkelkonsept**: Alle disse lommebøkene deler den globale likviditeten til Umbrel-noden din. Du oppretter ikke nye Lightning-kanaler for hver Wallet - LNbits fungerer som en intelligent regnskapsmessig Layer som administrerer allokeringen av midler innenfor din eksisterende Lightning-infrastruktur. Det er kraften i LNbits' multi-Wallet-system.



### Brukerinnlogging



Logg ut av SuperUser-kontoen (ikonet øverst til høyre) og gå tilbake til LNbits-påloggingssiden. Du kan nå logge inn med den nye brukerens påloggingsinformasjon.



![Connexion utilisateur satoshi](assets/fr/13.webp)



Skriv inn brukernavnet ("Satoshi") og passordet som er definert på forhånd, og klikk deretter på "LOGIN". Brukeren får direkte tilgang til sin personlige Wallet, helt isolert fra administrasjons-Interface.



### Interface fra Wallet-bruker



Når brukeren er tilkoblet, får han eller hun tilgang til Interface fra Wallet Lightning.



![Interface wallet utilisateur](assets/fr/14.webp)



Interface har følgende funksjoner :




- Gjeldende saldo**: Vises i Sats og i den valgte valutaen (CUC i dette eksempelet)
- Hovedhandlinger**: "PASTE REQUEST" (lim inn en regning som skal betales), "CREATE Invoice" (generate en kvittering), QR-ikon (hurtigskanning)
- Transaksjonshistorikk** : Komplett liste over alle betalinger og kvitteringer
- Høyre sidepanel**: Konfigurasjon og tilgangsalternativer



### Wallet mobil tilgang



Det høyre sidepanelet tilbyr en spesielt praktisk funksjon: mobil tilgang til Wallet. Brett ut "Mobile Access"-delen for å oppdage de tilgjengelige alternativene.



![Mobile Access](assets/fr/15.webp)



LNbits tilbyr flere måter å bruke denne Wallet på en smarttelefon:



**Alternativ 1: Kompatible mobilapplikasjoner




- Last ned **Zeus** eller **BlueWallet** fra App Store eller Google Play
- Aktiver **LndHub**-utvidelsen i LNbits for denne Wallet
- Skann LndHub QR-koden med mobilappen for å koble til Wallet



**Alternativ 2: Direkte tilgang via mobil nettleser**




- QR-koden som vises i "Eksporter til telefon med QR-kode", inneholder den fullstendige URL-en til Wallet med integrert autentisering
- Skann denne QR-koden fra smarttelefonen din for å åpne Wallet direkte i mobilnettleseren din
- Legg til side på startskjermen for rask tilgang



**Viktig sikkerhetsinformasjon**: Denne URL-en inneholder API-nøklene for full tilgang til Wallet. Del den aldri offentlig. Behandle denne QR-koden på samme måte som de private nøklene til Bitcoin - alle som skanner denne QR-koden får full tilgang til Wallet.



Denne mobilfunksjonen gjør LNbits Umbrel-forekomsten din til en veritabel Lightning Wallet-server for deg og vennene dine, samtidig som du beholder full suverenitet over pengene dine takket være din egen node.



### Deling av brukertilgang



Det viktigste bruksområdet for denne flerbrukerkonfigurasjonen er **deling av lommebøker med familien eller den nærmeste kretsen**. Når du har opprettet en bruker med en dedikert Wallet (for eksempel "Satoshi" i vårt eksempel), kan du dele disse innloggingsopplysningene med betrodde medlemmer av husstanden din.



**Tilgangssikkerhet på Umbrel**: Tilgang til LNbits-instansen din på Umbrel er naturligvis beskyttet, ettersom den bare kan nås :




- På ditt lokale nettverk** : Medlemmer av husstanden din som er koblet til samme WiFi-/Ethernet-nettverk, kan få tilgang til forekomsten
- Via VPN**: Hvis du bruker et VPN som Tailscale konfigurert på Umbrel-serveren din, kan autoriserte brukere få sikker ekstern tilgang



Denne doble Layer-beskyttelsen (nettverkstilgang + brukerautentisering) gjør alternativet "Tillat opprettelse av nye brukere" mindre kritisk på Umbrel. Bare personer som allerede har tilgang til nettverket eller VPN-et ditt, kan nå Interface-påloggingen.



**Typisk scenario**: Du oppretter en "pappa"-konto, en "mamma"-konto, en "bedriftskonto" og så videre. Hvert familiemedlem har sin egen isolerte Wallet Lightning, samtidig som de drar nytte av den delte likviditeten til Umbrel-noden din. Det er bare å dele brukernavn og passord - brukeren kan deretter koble seg til fra en hvilken som helst enhet i ditt lokale nettverk eller via Tailscale VPN. Se vår dedikerte Tailscale-veiledning for mer informasjon:



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Utforsk tilgjengelige utvidelser



Gå tilbake til Interface SuperUser og åpne "Extensions"-menyen i venstre sidepanel for å oppdage hele LNbits' økosystem av utvidelser.



![Extensions disponibles](assets/fr/16.webp)



LNbits tilbyr en rikholdig katalog med utvidelser som forvandler instansen din til en veritabel Lightning-tjenesteplattform:





- Jukeboks**: Sats-drevet jukeboksystem (Spotify-betalinger)
- Supportbilletter**: Betalt supportsystem (motta svar på spørsmål via SMS)
- TPoS**: Sikker, mobil kasseterminal for forhandlere
- User Manager**: avansert bruker- og Wallet-administrasjon (som vi nettopp har brukt)
- Arrangementer**: Salg og validering av billetter til arrangementer
- LNURLDevices**: Administrasjon av utsalgssteder, minibanker, tilkoblede brytere
- SMTP**: Gjør det mulig for brukere å sende e-post og tjene penger på Satss
- Boltcards**: Programmering av NFC-kort for lynraske tap-to-pay-betalinger
- NostrNip5**: Opprett NIP5-adresser for domenene dine
- Delte betalinger**: Automatisk fordeling av betalinger mellom flere lommebøker



Hver utvidelse aktiveres med ett enkelt klikk fra denne Interface. Utvidelser merket med "FREE" er gratis, mens noen er tilgjengelige som "PAID"-versjoner. Utforsk katalogen for å finne de som passer til dine behov - enten det gjelder forretningsvirksomhet, familieadministrasjon eller eksperimentering med Lightning Networks muligheter.



## Fordeler og begrensninger



**Fordeler**: Økonomisk suverenitet (full kontroll over midler/nøkler/data), arkitektonisk fleksibilitet (tapsfri VPS→Full node-migrering), profesjonelt utvidelsessystem, intuitiv Interface.



**Begrensninger** : Programvare i betaversjon (forsiktighet med mengder), sikkerhet under administratorens ansvar, nettadresser som inneholder sensitive API-nøkler (HTTPS obligatorisk), administrasjon av flere brukere innebærer forvalteransvar.



## Beste praksis



**Backups**: seed PHOENIXD/legitimasjon LND, LNbits-database, `.env`-filer. Automatiser daglig, hold utenfor produksjonsserveren, kryptert. Test gjenopprettinger regelmessig.



**Vedlikehold**: Se jevnlig etter oppdateringer (LNbits, Lightning backend, operativsystem). Sjekk alltid utgivelsesmerknader før større oppdateringer.





- På Umbrel**: App Store varsler deg automatisk om nye versjoner. Synkroniser utvidelser via "Administrer utvidelser" > "Oppdater alle". Sjekk at SQLite-databasen er inkludert i Umbrels automatiske sikkerhetskopier.
- På VPS**: Oppdater manuelt med `cd lnbits && git pull && uv sync --all-extras && sudo systemctl restart lnbits`. Overvåk systemlogger: `sudo journalctl -u lnbits -f`.



## Konklusjon



LNbits selvhosting tilbyr en konkret vei til Lightning økonomisk suverenitet. VPS+PHOENIXD tilbyr en lettvektsløsning for raske tjenester, med full integrering med eksisterende Bitcoin-node. Den skalerbare arkitekturen muliggjør utvikling fra enkle flerbruker-Wallet til sofistikerte forretningsbrukssaker.



Selvhosting innebærer ansvar: sikkerhetskopier frø, beskytt tilgangen, start med beskjedne beløp. Med disse forholdsreglene blir LNbits en robust løsning for lynøkonomien, samtidig som desentralisering og autonomi bevares.



## Ressurser



### Offisiell dokumentasjon




- [LNbits-dokumentasjon](https://docs.lnbits.org)
- [LNbits GitHub] (https://github.com/lnbits/lnbits)
- [PHOENIXD GitHub] (https://github.com/ACINQ/PHOENIXD)
- [Offisiell installasjonsveiledning] (https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md)



### Fellesskapets guider




- [Innledende Ubuntu-serverkonfigurasjon] (https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/) av Daniel P. Costas (trinnvis VPS-sikkerhet)
- [LNbits + PHOENIXD-installasjon på Ubuntu VPS] (https://danielpcostas.dev/install-lnbits-PHOENIXD-vps-ubuntu/) av Daniel P. Costas (komplett guide)
- [LNbits Server på Clearnet] (https://ereignishorizont.xyz/lnbits-server/en/) av Axel
- [LNbits på VPS](https://github.com/TrezorHannes/vps-lnbits) av Hannes