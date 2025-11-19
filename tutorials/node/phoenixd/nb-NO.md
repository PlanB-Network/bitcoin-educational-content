---
name: Phoenixd
description: Distribuer din egen minimalistiske Lightning-node med Phoenixd
---

![cover](assets/cover.webp)



Økonomisk autonomi betyr også kontroll over Lightning-infrastrukturen. For utviklere og selskaper som ønsker å integrere Bitcoin Lightning i applikasjonene sine, representerer **Phoenixd** den ideelle løsningen: en minimalistisk, spesialisert Lightning-node med automatisk likviditetsstyring.



Phoenixd er en Lightning-server utviklet av ACINQ, designet spesielt for å sende og motta Lightning-betalinger via et HTTP-API. I motsetning til fullverdige implementeringer som LND eller Core Lightning, abstraherer Phoenixd all kompleksiteten ved kanaladministrasjon, samtidig som midlene dine er selvbeskyttet.



I denne veiledningen ser vi på hvordan du installerer, konfigurerer og bruker Phoenixd til å utvikle Lightning-applikasjoner med en selvdrevet infrastruktur og et brukervennlig API.



## Hva er Phoenixd?



Phoenixd er en minimal, spesialisert Lightning-node utviklet av ACINQ. Det er en løsning for utviklere og bedrifter som ønsker å integrere Lightning i applikasjonene sine uten å måtte forholde seg til den komplekse administrasjonen av en Full node.



### Driftsprinsipp



**Phoenixd er en minimal Lightning-node som bruker ACINQ som LSP (Lightning Service Provider) for automatisk likviditet. Når du mottar Lightning-betalinger, åpner den automatisk kanaler med ACINQ-noder for å tildele nødvendig innkommende kapasitet. Denne "on-the-fly"-likviditeten er øyeblikkelig, men belastes med nøyaktig **1 % + Mining-gebyr** av det mottatte beløpet.



**Automatisert administrasjon:** Systemet administrerer tre viktige Elements:




- Lightning**-kanaler: Åpne, lukk og administrer automatisk etter behov
- Innkommende/utgående likviditet**: Automatisk tilførsel via spleising og kanalåpning
- Avgiftskreditt** : Små betalinger som ikke er tilstrekkelige til å rettferdiggjøre en kanal, lagres som en avsetning for fremtidige gebyrer



### Phoenixd fordeler



**Du kontrollerer dine private nøkler (12-ord seed) og midler. Phoenixd genererer Wallet lokalt uten å dele nøklene dine.



**Personlig infrastruktur:** Phoenixd kjører på din server, noe som gir deg tilgang til detaljerte logger, konfigurasjon og API-kontroll. Du er ikke lenger avhengig av en tredjepartstjeneste for å få tilgang til midlene dine.



**Integrert API:** Phoenixd har et HTTP-API for integrasjon med andre tjenester, innebygd LNURL-støtte og utvikling av tilpassede applikasjoner.



**Enkel integrering:** Takket være det enkle REST API-et kan Phoenixd integreres i alle applikasjoner eller tjenester som krever lynbetalinger.



**Viktig merknad:** Automatisk likviditet kommer fortsatt fra ACINQ som LSP (Lightning Service Provider). Phoenixd bruker samme mekanisme som Phoenix mobile for automatisk kanaladministrasjon.



## Installere Phoenixd



### Forutsetninger



Phoenixd krever et Linux-miljø (Ubuntu/Debian anbefales), med noen grunnleggende kommandolinjeferdigheter. For optimal ytelse trenger du :





- Linux-server**: VPS eller lokal maskin med stabil tilkobling
- OpenJDK 21** : Java-kjøretidsmiljø
- Stabil Internett-tilkobling**: For synkronisering med Lightning Network
- Domenenavn** (valgfritt) : For sikker HTTPS-tilgang til API-et



### Nedlasting og installasjon



**1. Last ned Phoenixd**



Gå til [GitHub releases]-siden (https://github.com/ACINQ/phoenixd/releases) og last ned den nyeste versjonen for din arkitektur:



```bash
# For Linux x86_64
# Replace with the latest release
wget https://github.com/ACINQ/phoenixd/releases/download/v0.6.1/phoenixd-0.6.1-linux-x64.zip
unzip -j phoenixd-0.6.1-linux-x64.zip
chmod +x phoenixd phoenix-cli
```



**2. Første oppstart



Start Phoenixd for initialisering:



```bash
./phoenixd
```



Ved første oppstart vil du bli bedt om å bekrefte to viktige trinn ved å skrive "Jeg forstår" :



**Melding 1 - Sikkerhetskopiering:**


```
This software is self-custodial, you have full control and responsibility over your funds.
Your 12-words seed is located in /home/<user>/.phoenix, make sure to do a backup or you risk losing your funds.
Do not share the same seed with other phoenix instances (mobile or server), it will cause issues and channel force closes.
```



**Spar på disse 12 ordene** - det er din eneste garanti for å bli frisk.



**Melding 2 - Automatisk likviditet:**


```
Continuous liquidity
Liquidity management is fully automated.
When receiving a Lightning payment that doesn't fit in your existing channel:
- If the payment amount is large enough to cover mining fees and service fees for automated liquidity,
then your channel will be created or enlarged right away.
- If the payment is too small, then the full amount is added to your fee credit,
and will be used later to pay for future fees. The fee credit is non-refundable.
```



Skriv `Jeg forstår` for hver bekreftelse.



![Premier démarrage](assets/fr/01.webp)



*Phoenixd starter opp for første gang: backupbekreftelser og automatisk likviditet*



**3. Konfigurasjon i drift** (kun på fransk)



For kontinuerlig drift oppretter du en systemd :



```bash
sudo nano /etc/systemd/system/phoenixd.service
```



```ini
[Unit]
Description=Phoenixd - Minimalist Lightning node
After=network.target

[Service]
User=your_user
WorkingDirectory=/home/your_user
ExecStart=/home/your_user/phoenixd
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```



```bash
sudo systemctl daemon-reload
sudo systemctl enable phoenixd
sudo systemctl start phoenixd
```



![Service systemd](assets/fr/02.webp)



*Phoenixd-tjenesten aktiv og operativ via systemd og `auto-liquidity` på 2m sat*



## Konfigurasjon og sikkerhet



### Konfigurasjonsfil



Phoenixd oppretter automatisk `~/.phoenix/phoenix.conf` med de viktigste parameterne:



```conf
# Network (mainnet by default)
chain=mainnet

# Size of automatic channels and requested liquidity amount (in satoshis)
auto-liquidity=2000000

# API configuration
http-bind-address=127.0.0.1
http-bind-port=9740
http-password=auto_generated_password
http-password-limited-access=limited_password
```



**Nøkkelparametere:**




- `auto-likviditet`: Størrelse på automatisk åpnede kanaler (standard: 2M Sats)
- http-passord`: Administratorpassord for API (opprettelse av Invoice OG utsendelse av betaling)
- http-passord-begrenset-tilgang`: Begrenset passord (kun ved opprettelse av Invoice)



### Sikker tilgang med HTTPS



Som standard er Phoenixd API bare tilgjengelig via lokal HTTP (`http://127.0.0.1:9740`). Hvis du vil bruke noden din utenfra (mobilapplikasjoner, andre servere, webintegrasjoner), må du konfigurere sikker HTTPS-tilgang.



**Reverse proxy-prinsippet:**


```
Internet → nginx (port 443 HTTPS) → Phoenixd (port 9740 HTTP local)
```



**Nginx** fungerer som en **omvendt proxy**: Den lytter til HTTPS-forespørsler fra Internett på port 443, omdirigerer dem til Phoenixd lokalt (port 9740), og sender deretter krypterte svar tilbake til klienten.



**SSL/TLS-sertifikatet** er en digital fil som :




- Bevis serverens identitet** (forhindrer "man-in-the-middle"-angrep)
- Aktiverer HTTPS**-kryptering: alle data, inkludert API-passordene dine, krypteres under transport
- Utstedt gratis** av Let's Encrypt via certbot-verktøyet



Denne konfigurasjonen lar deg :




- Sikker tilgang til API-et fra Internett**
- Krypter API**-passordene dine under transport (for å hindre at de overføres i klartekst)
- Integrer Phoenixd** i eksterne applikasjoner som krever HTTPS
- Overholdelse av sikkerhetsstandarder** for finansielle API-er



Konfigurer denne HTTPS reverse proxy med nginx :



**1. Nginx**-konfigurasjon



```bash
sudo apt install nginx certbot python3-certbot-nginx
sudo nano /etc/nginx/sites-available/phoenixd.conf
```



```nginx
server {
listen 80;
server_name phoenixd.your-domain.com;

location / {
proxy_pass http://127.0.0.1:9740;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header Host $host;
}
}
```



```bash
sudo ln -s /etc/nginx/sites-available/phoenixd.conf /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```



**2. SSL**-sertifikat



```bash
sudo certbot --nginx -d phoenixd.your-domain.com
```



### Funksjonstest



Kontroller at Phoenixd fungerer som den skal:



```bash
./phoenix-cli getinfo
./phoenix-cli getbalance
```



Disse kommandoene skal returnere JSON-informasjon om nodens status og saldo (i utgangspunktet tom).



![Commandes CLI](assets/fr/03.webp)



*Kommandoene getinfo og getbalance for å sjekke nodenes status*



## Bruke API-et



### Første mottakstest



**1. Opprett en Lightning** Invoice



Bruk API-et til å opprette din første Invoice:



```bash
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='First test' \
-d amountSat=100000
```



### Forståelse av den automatiske likviditetsmekanismen



**Grunnprinsipp:** Når du mottar en lynbetaling, må Phoenixd noen ganger åpne en ny kanal for å kunne motta den. Denne kanalåpningen koster et gebyr som **automatisk** trekkes fra det mottatte beløpet.



**Konkret eksempel med 100 000 Sats:**



![Premier test de réception](assets/fr/04.webp)



*Første akseptansetest: Sats 100k mottatt, endelig saldo på Sats 75.561 etter fradrag av likviditetskostnader*



```bash
# Payment received: 100,000 sats
# Channel created: 2,115,000 sats total capacity
# Liquidity fee: 24,439 sats
# Final balance: 75,561 sats
```



**Beregning av gebyr:**




- Serviceavgift**: 1 % av kanalkapasiteten (2 115 000 Sats) = 21 150 Sats
- Mining-avgifter**: ~3 289 Sats (for On-Chain-transaksjon)
- Totalt**: 24 439 Sats trekkes automatisk fra



**Verifisering med CLI-kommandoer:**


```bash
# View details of all channels
./phoenix-cli listchannels

# Important output:
# "toLocal": 75561000 (your balance in milli-sats)
# "toRemote": 2039439000 (ACINQ's balance)
# Total channel: 2,115,000 sats
```



![Nouveau solde après paiement](assets/fr/05.webp)



*Sluttsaldo etter at betalingen er sendt: 257 Sats gjenstår etter Lightning-forsendelsen*



**Avgiftskreditt for små betalinger:** Hvis du mottar betalinger som er for små til å rettferdiggjøre åpning av en kanal (< ca. 25 000 Sats), lagres de i en ikke-refunderbar "avgiftskreditt". Denne kreditten vil bli brukt til å betale fremtidige kanalavgifter når du mottar et tilstrekkelig beløp.



**2. Følg kanalåpningen**



Følg med på Phoenixd-loggene:



```bash
journalctl -u phoenixd -f
```



Du vil se åpningen av kanalen og det automatiske trekket av likviditetsgebyrer. Gebyrene varierer i henhold til Mempool Bitcoin-betingelsene, men inkluderer alltid 1 % servicegebyr pluss gjeldende Mining-gebyr.



**3. Sjekk kanalen**



```bash
./phoenix-cli listchannels
```



Denne kommandoen viser de aktive kanalene dine med status og saldo.



### Fullstendige API-operasjoner



Phoenixd eksponerer et REST API på port 9740 som muliggjør :



**Grunnleggende operasjoner:**


```bash
# Create an invoice
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='Test payment' \
-d amountSat=100000

# Send a payment (routing fee 0.4%)
curl -X POST http://localhost:9740/payinvoice \
-u :your_password \
-d invoice='lnbc...'

# Check balance
curl http://localhost:9740/getbalance \
-u :your_password

# Send on-chain funds (in case of channel closure)
./phoenix-cli sendtoaddress \
--address bc1q... \
--amountSat 50000 \
--feerateSatByte 12
```



**Viktig for kostnadene:**




- Kvittering**: 1 % + Mining-gebyr for automatisk likviditet
- Frakt**: 0.4 % rutinggebyr på Lightning Network



**Webhooks:** Webhooks gjør det mulig for Phoenixd å **automatisk varsle** applikasjonene dine når en hendelse inntreffer (betaling mottatt, Invoice betalt, kanal åpnet osv.). I stedet for å stadig be Phoenixd om oppdateringer, mottar applikasjonen din et øyeblikkelig HTTP-varsel.



**Nettbutikken din mottar automatisk et varsel når en kunde betaler for en bestilling, slik at transaksjonen kan valideres umiddelbart.



Konfigurasjon i `phoenix.conf` :


```conf
webhook-url=https://your-app.com/webhook-phoenixd
webhook-secret=votre_secret_de_verification
```



## Avanserte applikasjoner



### LNURL-integrasjoner



Phoenixd støtter LNURL-protokoller for avansert integrering:



**LNURL-Pay:** Betal for LNURL-kompatible tjenester


```bash
curl -X POST http://localhost:9740/lnurlpay \
-u :your_password \
-d lnurl=LNURL1DP68GURN8GHJ7MRWW4EXCTN... \
-d amountSat=100
```



**LNURL-Withdraw :** Hente midler fra LNURL-tjenester


```bash
curl -X POST http://localhost:9740/lnurlwithdraw \
-u :your_password \
-d lnurl=lightning:LNURL1DP68GURN8GHJ7MRW...
```



**LNURL-Auth:** Autentisering via Lightning for å få tilgang til tjenester


```bash
curl -X POST http://localhost:9740/lnurlauth \
-u :your_password \
-d lnurl=lnurl1dp68gurn8ghj7um5v93kket...
```



### Integrering med LNbits



LNbits kan bruke Phoenixd som finansieringskilde i henhold til [offisiell dokumentasjon] (https://docs.lnbits.org/guide/wallets.html):



**LNbits-konfigurasjon:**


```bash
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://localhost:9740/
PHOENIXD_API_PASSWORD=your_password_phoenixd
```



Denne integrasjonen lar deg opprette LNbits-underkontoer drevet av Phoenixd-noden din, og gir deg en nettbasert Interface for administrasjon av flere Lightning-lommebøker.



### Tilpassede applikasjoner



Takket være det omfattende REST API-et kan du utvikle :



**E-handel:** Direkte integrering av Lightning-betalinger i butikken din


**Donasjonstjenester:** Donasjonssystemer med fakturaer og automatiske webhooks


**Bots for sosiale nettverk:** Telegram/Discord-bots med tipsfunksjoner


**Premium-innhold tilgjengelig mot en Lightning-avgift



## Sikkerhet og beste praksis



### Tilgangsbeskyttelse



**API-passord:** Automatisk genererte passord er nøklene til Lightning-skattkammeret ditt. Del dem aldri, og endre dem hvis du er i tvil.



**Brannmur:** La aldri port 9740 være åpen direkte mot Internett. Bruk alltid nginx med HTTPS.



**Utvidet autentisering:** Vurder VPN eller Tailscale for å begrense tilgangen til serveren din til kun autoriserte enheter.



### Viktige sikkerhetskopier



**Gjenoppretting av seed:** Lagre de 12 ordene dine på et trygt sted utenfor serveren. Dette er din eneste garanti for gjenoppretting.



*~/.phoenix-katalogen:** Sikkerhetskopier denne mappen regelmessig (etter at Phoenixd har blitt stengt ned) for å bevare kanalstatusen og gjøre gjenopprettingen raskere.



**Gjenopprettingskoder for tjenester:** Ta også vare på sikkerhetskopikoder for alle tjenester der du aktiverer 2FA med Phoenix.



### Overvåking og vedlikehold



**Overvåkingslogger:**


```bash
journalctl -u phoenixd -f  # Real-time logs
./phoenix-cli getinfo      # Node status
```



**Oppdateringer:** Se [GitHub releases] (https://github.com/ACINQ/phoenixd/releases) for nye versjoner. Oppdatering er så enkelt som å bytte ut binærfilen og starte tjenesten på nytt.



## Sammenligning med alternativer



### Phoenixd vs Phoenix standard



**Phoenix standard (mobil) :**




- ✅ Umiddelbar installasjon, ingen konfigurasjon
- ✅ Interface mobil intuitiv
- ✅ Samme automatisk lagring som Phoenixd
- ❌ Ingen API for utviklere
- ❌ Ingen tilgang til detaljerte logger



**Phoenixd (server) :**




- ✅ HTTP API for integrasjoner
- ✅ Full tilgang til logger
- ✅ Personlig infrastruktur
- ❌ Krever tekniske ferdigheter
- ❌ Servervedlikehold kreves



**Begge bruker ACINQ som LSP for automatisk likviditet.



### Phoenixd vs LND/Core Lightning



**LND/Core Lightning :**




- ✅ Total kontroll, full Lightning-protokoll
- ✅ Stort samfunn, modent økosystem
- ❌ Kompleks manuell likviditetsstyring
- ❌ Stor læringskurve



**Phoenixd :**




- ✅ Automatisk likviditetsstyring (som Phoenix mobile)
- ✅ API for utviklere
- ✅ Forenklet konfigurasjon
- ❌ Bruker ACINQ som LSP (ingen uavhengig ruting)
- ❌ Mindre fleksibel enn komplette noder



## Løsning av vanlige problemer



### Problemer med API-tilgang



*feilen "*Autentifisering mislyktes":**


1. Sjekk passordet i filen `~/.phoenix/phoenix.conf`


2. Kontroller autentiseringsformatet `-u:password`


3. Kontroller at Phoenixd kjører (`./phoenix-CLI getinfo`)



**Tidsavbrudd i tilkoblingen:**




- Kontroller at Phoenixd lytter på riktig port (9740)
- Test lokal tilgang før du konfigurerer HTTPS
- Sjekk loggene: `journalctl -u phoenixd -f`



### Likviditetsproblemer



**Betalinger kommer ikke frem :**


1. Kontroller at beløpet overstiger minimumsgrensen (~30 000 Sats)


2. Se logger for å identifisere kanalfeil


3. Start Phoenixd på nytt om nødvendig



**Saldo i "utgiftskreditt":**


Små betalinger lagres som en avsetning. Motta et større beløp for å utløse kanalåpning og frigjøre disse midlene.



## Konklusjon



Phoenixd representerer et utmerket kompromiss mellom brukervennlighet og teknisk suverenitet for utviklere. Det tilbyr et enkelt, men kraftig Lightning API med automatisk likviditetsstyring, noe som eliminerer kompleksiteten til tradisjonelle Lightning-noder.



Denne løsningen egner seg spesielt godt for utviklere og selskaper som ønsker å :




- Integrer Bitcoin Lightning i applikasjonene dine
- Unngå kompleksiteten ved styring av Lightning-kanaler
- Dra nytte av en infrastruktur med egen drift
- Et enkelt og pålitelig API



Med Phoenixd bygger du din egen private Lightning-infrastruktur med et moderne REST API og automatisk håndtering av tekniske aspekter. Det er den ideelle løsningen for å demokratisere Lightning-integrering i prosjektene dine.



## Nyttige ressurser



### Offisiell dokumentasjon




- GitHub Phoenixd** : [github.com/ACINQ/phoenixd](https://github.com/ACINQ/phoenixd) - Kildekode og utgivelser
- Phoenix Server**-nettstedet: [phoenix.acinq.co/server](https://phoenix.acinq.co/server) - Fullstendig dokumentasjon
- FAQ Phoenixd** : [phoenix.acinq.co/server/faq](https://phoenix.acinq.co/server/faq) - Ofte stilte spørsmål



### Støtte fra fellesskapet




- GitHub-problemer** : [github.com/ACINQ/phoenixd/issues](https://github.com/ACINQ/phoenixd/issues) - Teknisk støtte
- Twitter ACINQ** : [@ACINQ_co](https://twitter.com/ACINQ_co) - Nyheter og kunngjøringer