---
name: Phoenixd
description: Distribuera din egen minimalistiska Lightning-nod med Phoenixd
---

![cover](assets/cover.webp)



Finansiell autonomi innebär också att kontrollera din Lightning-infrastruktur. För utvecklare och företag som vill integrera Bitcoin Lightning i sina applikationer utgör **Phoenixd** den perfekta lösningen: en minimalistisk, specialiserad Lightning-nod med automatisk likviditetshantering.



Phoenixd är en Lightning-server som utvecklats av ACINQ, speciellt utformad för att skicka och ta emot Lightning-betalningar via ett HTTP API. Till skillnad från fullfjädrade implementeringar som LND eller Core Lightning abstraherar Phoenixd all komplexitet i kanalhanteringen samtidigt som självskyddet för dina medel bevaras.



I den här handledningen går vi igenom hur du installerar, konfigurerar och använder Phoenixd för att utveckla Lightning-applikationer med en egen infrastruktur och ett lättanvänt API.



## Vad är Phoenixd?



Phoenixd är en minimal, specialiserad Lightning-nod som utvecklats av ACINQ. Det är en lösning som är utformad för utvecklare och företag som vill integrera Lightning i sina applikationer utan att behöva hantera komplexiteten hos en Full node.



### Funktionsprincip



**Phoenixd är en minimal Lightning-nod som använder ACINQ som sin LSP (Lightning Service Provider) för automatisk likviditet. När du får Lightning-betalningar öppnar den automatiskt kanaler med ACINQ-noder för att tilldela den nödvändiga inkommande kapaciteten. Denna "on-the-fly"-likviditet är omedelbar, men debiteras med exakt **1% + Mining-avgifter** av det mottagna beloppet.



**Automatiserad hantering:** Systemet hanterar tre viktiga Elements:




- Blixtsnabba** kanaler: Öppna, stäng och hantera automatiskt efter behov
- Inkommande/utgående likviditet**: Automatisk försörjning via splicing och kanalöppning
- Avgiftskredit** : Små betalningar som inte räcker för att motivera en kanal lagras som en avsättning för framtida avgifter



### Phoenixd förmåner



**Du kontrollerar dina privata nycklar (12-ord seed) och medel. Phoenixd genererar din Wallet lokalt utan att någonsin dela dina nycklar.



**Personlig infrastruktur:** Phoenixd körs på din server, vilket ger dig tillgång till detaljerade loggar, konfiguration och API-kontroll. Du är inte längre beroende av en tredjepartstjänst för att få tillgång till dina pengar.



**Integrerat API:** Phoenixd har ett HTTP API för integration med andra tjänster, inbyggt LNURL-stöd och utveckling av anpassade applikationer.



**Enkel integration: ** Tack vare sitt enkla REST API kan Phoenixd integreras i alla applikationer eller tjänster som kräver Lightning-betalningar.



**Viktigt att notera:** Automatisk likviditet kommer fortfarande från ACINQ som LSP (Lightning Service Provider). Phoenixd använder samma mekanism som Phoenix mobile för automatisk kanalhantering.



## Installera Phoenixd



### Förkunskapskrav



Phoenixd kräver en Linux-miljö (Ubuntu/Debian rekommenderas), med vissa grundläggande kommandoradsfärdigheter. För optimal prestanda behöver du :





- Linux-server**: VPS eller lokal maskin med stabil anslutning
- OpenJDK 21** : Java runtime-miljö
- Stabil internetanslutning**: För synkronisering med Lightning Network
- Domännamn** (valfritt) : För säker HTTPS-åtkomst till API:et



### Nedladdning och installation



**1. Ladda ner Phoenixd**



Gå till sidan [GitHub releases] (https://github.com/ACINQ/phoenixd/releases) och ladda ner den senaste versionen för din arkitektur:



```bash
# For Linux x86_64
# Replace with the latest release
wget https://github.com/ACINQ/phoenixd/releases/download/v0.6.1/phoenixd-0.6.1-linux-x64.zip
unzip -j phoenixd-0.6.1-linux-x64.zip
chmod +x phoenixd phoenix-cli
```



**2. Första uppstarten



Starta Phoenixd för initialisering:



```bash
./phoenixd
```



Vid första lanseringen ombeds du att bekräfta två viktiga steg genom att skriva "Jag förstår" :



**Meddelande 1 - Backup:**


```
This software is self-custodial, you have full control and responsibility over your funds.
Your 12-words seed is located in /home/<user>/.phoenix, make sure to do a backup or you risk losing your funds.
Do not share the same seed with other phoenix instances (mobile or server), it will cause issues and channel force closes.
```



**Spara dessa 12 ord** - det är din enda garanti för tillfrisknande.



**Meddelande 2 - Automatisk likviditet:**


```
Continuous liquidity
Liquidity management is fully automated.
When receiving a Lightning payment that doesn't fit in your existing channel:
- If the payment amount is large enough to cover mining fees and service fees for automated liquidity,
then your channel will be created or enlarged right away.
- If the payment is too small, then the full amount is added to your fee credit,
and will be used later to pay for future fees. The fee credit is non-refundable.
```



Skriv "Jag förstår" för varje bekräftelse.



![Premier démarrage](assets/fr/01.webp)



*Phoenixd startar upp för första gången: backupbekräftelser och automatisk likviditet*



**3. Konfiguration vid drift** (endast på franska)



För kontinuerlig drift, skapa en systemd :



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



*Phoenixd-tjänsten aktiv och i drift via systemd och `auto-liquidity` på 2m sat*



## Konfiguration och säkerhet



### Konfigurationsfil



Phoenixd skapar automatiskt `~/.phoenix/phoenix.conf` med de viktigaste parametrarna:



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



**Nyckelparametrar: **




- `auto-likviditet`: Storlek på automatiskt öppnade kanaler (standard: 2M Sats)
- http-lösenord`: Administratörslösenord för API (skapande av Invoice OCH betalningsutskick)
- http-lösenord-begränsad-åtkomst`: Begränsat lösenord (endast vid skapande av Invoice)



### Säker åtkomst med HTTPS



Som standard är Phoenixd API endast tillgängligt via lokal HTTP (`http://127.0.0.1:9740`). Om du vill använda din nod från utsidan (mobila applikationer, andra servrar, webbintegrationer) måste du konfigurera säker HTTPS-åtkomst.



**Omvänd proxyprincip:**


```
Internet → nginx (port 443 HTTPS) → Phoenixd (port 9740 HTTP local)
```



**Nginx** fungerar som en **reverse proxy**: den lyssnar på HTTPS-förfrågningar från Internet på port 443, omdirigerar dem till Phoenixd lokalt (port 9740) och skickar sedan krypterade svar tillbaka till klienten.



**SSL/TLS**-certifikatet är en digital fil som :




- Bevisa din servers identitet** (förhindrar man-in-the-middle-attacker)
- Aktiverar HTTPS**-kryptering: alla data, inklusive dina API-lösenord, krypteras under transport
- Utfärdas kostnadsfritt** av Let's Encrypt via verktyget certbot



Denna konfiguration gör att du kan :




- Säker åtkomst till API:et från Internet**
- Kryptera dina API**-lösenord under transport (för att förhindra att de överförs i klartext)
- Integrera Phoenixd** i externa applikationer som kräver HTTPS
- Överensstämmelse med säkerhetsstandarder** för finansiella API:er



Konfigurera denna omvända HTTPS-proxy med nginx :



**1. Nginx**-konfiguration



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



**2. SSL**-certifikat



```bash
sudo certbot --nginx -d phoenixd.your-domain.com
```



### Funktionstest



Kontrollera att Phoenixd fungerar som det ska:



```bash
./phoenix-cli getinfo
./phoenix-cli getbalance
```



Dessa kommandon ska returnera JSON-information om nodens status och saldo (initialt tom).



![Commandes CLI](assets/fr/03.webp)



*Kommandona getinfo och getbalance för att kontrollera nodstatus*



## Använda API:et



### Första mottagningstestet



**1. Skapa en blixt** Invoice



Använd API:et för att skapa din första Invoice:



```bash
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='First test' \
-d amountSat=100000
```



### Förståelse för den automatiska likviditetsmekanismen



**Grundläggande princip:** När du tar emot en blixtbetalning måste Phoenixd ibland öppna en ny kanal för att kunna ta emot den. Denna kanalöppning kostar en avgift som **automatiskt** dras av från det mottagna beloppet.



**Konkret exempel med 100.000 Sats:**



![Premier test de réception](assets/fr/04.webp)



*Första acceptanstestet: Sats 100k mottaget, slutligt saldo för Sats 75.561 efter avdrag för likviditetskostnader*



```bash
# Payment received: 100,000 sats
# Channel created: 2,115,000 sats total capacity
# Liquidity fee: 24,439 sats
# Final balance: 75,561 sats
```



**Beräkning av avgift:**




- Serviceavgift**: 1% av kanalens kapacitet (2 115 000 Sats) = 21 150 Sats
- Mining avgifter**: ~3.289 Sats (för On-Chain-transaktion)
- Totalt**: 24.439 Sats dras av automatiskt



**Verifiering med CLI-kommandon:**


```bash
# View details of all channels
./phoenix-cli listchannels

# Important output:
# "toLocal": 75561000 (your balance in milli-sats)
# "toRemote": 2039439000 (ACINQ's balance)
# Total channel: 2,115,000 sats
```



![Nouveau solde après paiement](assets/fr/05.webp)



*Slutligt saldo efter skickad betalning: 257 Sats kvar efter Lightning-försändelsen*



**Avgiftskredit för små betalningar:** Om du får betalningar som är för små för att motivera att en kanal öppnas (< ca 25k Sats), lagras de i en icke-återbetalningsbar "avgiftskredit". Detta tillgodohavande kommer att användas för att betala framtida kanalavgifter när du får en tillräckligt stor summa.



**2. Följ kanalöppningen**



Titta på Phoenixd-loggen:



```bash
journalctl -u phoenixd -f
```



Du kommer att se öppnandet av kanalen och det automatiska avdraget av likviditetsavgifter. Avgifterna varierar beroende på Mempool Bitcoin villkor, men inkluderar alltid 1% serviceavgift plus aktuell Mining avgift.



**3. Kontrollera kanal**



```bash
./phoenix-cli listchannels
```



Detta kommando visar dina aktiva kanaler med deras status och balans.



### Komplett API-verksamhet



Phoenixd exponerar ett REST API på port 9740 som möjliggör :



**Grundläggande verksamhet:**


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



**Viktigt om kostnader:**




- Kvitto**: 1% + Mining avgift för automatisk likviditet
- Frakt**: 0.4% routningsavgift på Lightning Network



**Webhooks: ** Webhooks gör det möjligt för Phoenixd att **automatiskt meddela** dina applikationer när en händelse inträffar (betalning mottagen, Invoice betald, kanal öppnad etc.). Istället för att ständigt be Phoenixd om uppdateringar får din applikation en omedelbar HTTP-notifiering.



**Din webbutik får automatiskt ett meddelande när en kund betalar för en order, vilket möjliggör omedelbar validering av transaktionen.



Konfiguration i `phoenix.conf` :


```conf
webhook-url=https://your-app.com/webhook-phoenixd
webhook-secret=votre_secret_de_verification
```



## Avancerade tillämpningar



### LNURL-integrationer



Phoenixd har inbyggt stöd för LNURL-protokoll för avancerad integration:



**LNURL-Pay:** Betala för LNURL-kompatibla tjänster


```bash
curl -X POST http://localhost:9740/lnurlpay \
-u :your_password \
-d lnurl=LNURL1DP68GURN8GHJ7MRWW4EXCTN... \
-d amountSat=100
```



**LNURL-Withdraw :** Hämta medel från LNURL-tjänster


```bash
curl -X POST http://localhost:9740/lnurlwithdraw \
-u :your_password \
-d lnurl=lightning:LNURL1DP68GURN8GHJ7MRW...
```



**LNURL-Auth:** Autentisering via Lightning för åtkomst till tjänster


```bash
curl -X POST http://localhost:9740/lnurlauth \
-u :your_password \
-d lnurl=lnurl1dp68gurn8ghj7um5v93kket...
```



### Integration med LNbits



LNbits kan använda Phoenixd som finansieringskälla enligt dess [officiella dokumentation] (https://docs.lnbits.org/guide/wallets.html):



**LNbits konfiguration:**


```bash
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://localhost:9740/
PHOENIXD_API_PASSWORD=your_password_phoenixd
```



Denna integration gör att du kan skapa LNbits-underkonton som drivs av din Phoenixd-nod, vilket ger en webbaserad Interface för hantering av flera Lightning-plånböcker.



### Anpassade applikationer



Tack vare det omfattande REST API:et kan du utveckla :



**E-handel:** Direkt integration av Lightning-betalningar i din butik


**Donationstjänster:** Donationssystem med fakturor och automatiska webhooks


**Botar för sociala nätverk:** Telegram/Discord-botar med tipsfunktioner


**Betalvägg Lightning:** Premiuminnehåll tillgängligt mot en Lightning-avgift



## Säkerhet och bästa praxis



### Åtkomstskydd



**API-lösenord:** Automatiskt genererade lösenord är nycklarna till din Lightning-skattkammare. Dela aldrig med dig av dem och ändra dem om du är osäker.



**Brandvägg:** Lämna aldrig port 9740 öppen direkt mot Internet. Använd alltid nginx med HTTPS.



**Förbättrad autentisering:** Överväg ett VPN eller Tailscale för att begränsa åtkomsten till din server till endast auktoriserade enheter.



### Viktiga säkerhetskopior



**seed återställning:** Spara dina 12 ord på en säker plats, utanför servern. Detta är din enda garanti för återhämtning.



*~/.phoenix directory:** Säkerhetskopiera den här mappen regelbundet (efter att Phoenixd har stängts av) för att bevara kanalstatus och påskynda återställningen.



**Återställningskoder för tjänster:** Spara även säkerhetskopieringskoder för alla tjänster där du aktiverar 2FA med din Phoenix.



### Övervakning och underhåll



**Övervakningsloggar:**


```bash
journalctl -u phoenixd -f  # Real-time logs
./phoenix-cli getinfo      # Node status
```



**Uppdateringar:** Se [GitHub releases](https://github.com/ACINQ/phoenixd/releases) för nya versioner. Uppdatering är så enkelt som att byta ut binärfilen och starta om tjänsten.



## Jämförelse med alternativ



### Phoenixd vs Phoenix standard



**Phoenix standard (mobil) :**




- ✅ Omedelbar installation, ingen konfiguration
- ✅ Interface mobil intuitiv
- ✅ Samma autosparande som Phoenixd
- ❌ Inget API för utvecklare
- ❌ Ingen tillgång till detaljerade loggar



**Phoenixd (server) :**




- ✅ HTTP API för integrationer
- ✅ Full tillgång till loggar
- ✅ Personlig infrastruktur
- ❌ Kräver tekniska färdigheter
- ❌ Underhåll av server krävs



**Båda använder ACINQ som sin LSP för automatisk likviditet.



### Phoenixd vs LND/Core Lightning



**LND/Core Lightning :**




- ✅ Total kontroll, fullständigt Lightning-protokoll
- ✅ Stort samhälle, moget ekosystem
- ❌ Komplex manuell likviditetshantering
- ❌ Stor inlärningskurva



**Phoenixd :**




- ✅ Automatisk likviditetshantering (som Phoenix mobile)
- ✅ API för utvecklare
- ✅ Förenklad konfiguration
- ❌ Använder ACINQ som LSP (ingen oberoende routing)
- ❌ Mindre flexibel än kompletta noder



## Lösning av vanliga problem



### Problem med API-åtkomst



**Autenticering misslyckades" fel:**


1. Kontrollera lösenordet i filen `~/.phoenix/phoenix.conf`


2. Kontrollera autentiseringsformatet `-u:lösenord`


3. Kontrollera att Phoenixd körs (`./phoenix-CLI getinfo`)



**Tidsgränser för anslutning:**




- Kontrollera att Phoenixd lyssnar på rätt port (9740)
- Testa lokal åtkomst innan du konfigurerar HTTPS
- Kontrollera loggar: `journalctl -u phoenixd -f`



### Likviditetsproblem



**Betalningar har inte kommit in :**


1. Kontrollera att beloppet överstiger minimitröskeln (~30k Sats)


2. Konsultera loggar för att identifiera kanalfel


3. Starta om Phoenixd om det behövs



**Saldo i "kostnadskredit":**


Små betalningar lagras som en avsättning. Ta emot ett större belopp för att utlösa kanalöppning och frigöra dessa medel.



## Slutsats



Phoenixd representerar en utmärkt kompromiss mellan användarvänlighet och teknisk suveränitet för utvecklare. Det erbjuder ett enkelt men ändå kraftfullt Lightning API med automatisk likviditetshantering, vilket eliminerar komplexiteten hos traditionella Lightning-noder.



Denna lösning lämpar sig särskilt väl för utvecklare och företag som vill :




- Integrera Bitcoin Lightning i dina applikationer
- Undvik komplexiteten i hanteringen av blixtkanaler
- Dra nytta av en infrastruktur med egen drift
- Ett enkelt och tillförlitligt API



Med Phoenixd bygger du din egen privata Lightning-infrastruktur med ett modernt REST API och automatisk hantering av tekniska aspekter. Det är den perfekta lösningen för att demokratisera Lightning-integrationen i dina projekt.



## Användbara resurser



### Officiell dokumentation




- GitHub Phoenixd** : [github.com/ACINQ/phoenixd](https://github.com/ACINQ/phoenixd) - Källkod och releaser
- Phoenix Server** webbplats: [phoenix.acinq.co/server](https://phoenix.acinq.co/server) - Fullständig dokumentation
- FAQ Phoenixd** : [phoenix.acinq.co/server/faq](https://phoenix.acinq.co/server/faq) - Vanliga frågor och svar



### Stöd från gemenskapen




- GitHub-problem** : [github.com/ACINQ/phoenixd/issues](https://github.com/ACINQ/phoenixd/issues) - Teknisk support
- Twitter ACINQ** : [@ACINQ_co](https://twitter.com/ACINQ_co) - Nyheter och tillkännagivanden