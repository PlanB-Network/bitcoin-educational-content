---
name: Phoenixd
description: Implementeer je eigen minimalistische Lightning-node met Phoenixd
---

![cover](assets/cover.webp)



Financiële autonomie betekent ook controle over uw Lightning-infrastructuur. Voor ontwikkelaars en bedrijven die Bitcoin Lightning in hun applicaties willen integreren, is **Phoenixd** de ideale oplossing: een minimalistisch, gespecialiseerd Lightning-knooppunt met automatisch liquiditeitsbeheer.



Phoenixd is een Lightning-server ontwikkeld door ACINQ, speciaal ontworpen voor het verzenden en ontvangen van Lightning-betalingen via een HTTP API. In tegenstelling tot volledige implementaties zoals LND of Core Lightning, abstraheert Phoenixd alle complexiteit van kanaalbeheer met behoud van de zelfbescherming van uw fondsen.



In deze tutorial bekijken we hoe je Phoenixd installeert, configureert en gebruikt om Lightning-toepassingen te ontwikkelen met een zelf gehoste infrastructuur en een gebruiksvriendelijke API.



## Wat is Phoenixd?



Phoenixd is een minimale, gespecialiseerde Lightning-node ontwikkeld door ACINQ. Het is een oplossing die is ontworpen voor ontwikkelaars en bedrijven die Lightning in hun applicaties willen integreren zonder de beheercomplexiteit van een Full node.



### Werkingsprincipe



**Fenixd is een minimaal Lightning-knooppunt dat ACINQ gebruikt als LSP (Lightning Service Provider) voor automatische liquiditeit. Wanneer je Lightning-betalingen ontvangt, opent het automatisch kanalen met ACINQ-knooppunten om de benodigde inkomende capaciteit toe te wijzen. Deze "on-the-fly" liquiditeit is onmiddellijk, maar wordt in rekening gebracht tegen exact **1% + Mining vergoedingen** van het ontvangen bedrag.



**Geautomatiseerd beheer:** Het systeem beheert drie belangrijke Elements:




- Lightning** kanalen: Naar behoefte automatisch openen, sluiten en beheren
- Inkomende/uitgaande liquiditeit**: Automatische bevoorrading via splicing en kanaalopening
- Tariefkrediet** : Kleine betalingen die onvoldoende zijn om een kanaal te rechtvaardigen, worden opgeslagen als voorziening voor toekomstige kosten



### Voordelen van Phoenixd



**Je beheert je privésleutels (12-woord seed) en fondsen. Phoenixd genereert je Wallet lokaal zonder ooit je sleutels te delen.



**Eigen infrastructuur:** Phoenixd draait op jouw server, waardoor je toegang hebt tot gedetailleerde logs, configuratie en API-controle. Je bent niet langer afhankelijk van een service van derden voor toegang tot je fondsen.



**Geïntegreerde API:** Phoenixd beschikt over een HTTP API voor integratie met andere services, native LNURL-ondersteuning en de ontwikkeling van toepassingen op maat.



**Gemakkelijke integratie:** Dankzij de eenvoudige REST API kan Phoenixd worden geïntegreerd in elke applicatie of service die Lightning-betalingen vereist.



**Belangrijke opmerking:** Automatische liquiditeit komt nog steeds van ACINQ als LSP (Lightning Service Provider). Phoenixd gebruikt hetzelfde mechanisme als Phoenix mobile voor automatisch kanaalbeheer.



## Phoenixd installeren



### Vereisten



Phoenixd vereist een Linux-omgeving (Ubuntu/Debian aanbevolen), met wat basis commandoregelvaardigheden. Voor optimale prestaties heb je :





- Linux server**: VPS of lokale machine met stabiele verbinding
- OpenJDK 21** : Java runtime-omgeving
- Stabiele internetverbinding**: Voor synchronisatie met de Lightning Network
- Domeinnaam** (optioneel) : Voor beveiligde HTTPS-toegang tot de API



### Downloaden en installeren



**1. Downloaden Phoenixd**



Ga naar de [GitHub releases] pagina (https://github.com/ACINQ/phoenixd/releases) en download de laatste versie voor jouw architectuur:



```bash
# For Linux x86_64
# Replace with the latest release
wget https://github.com/ACINQ/phoenixd/releases/download/v0.6.1/phoenixd-0.6.1-linux-x64.zip
unzip -j phoenixd-0.6.1-linux-x64.zip
chmod +x phoenixd phoenix-cli
```



**2. Eerste opstart



Start Phoenixd voor initialisatie:



```bash
./phoenixd
```



Bij de eerste keer opstarten wordt je gevraagd om twee belangrijke stappen te bevestigen door "Ik begrijp het" in te typen:



**Bericht 1 - Back-up:**


```
This software is self-custodial, you have full control and responsibility over your funds.
Your 12-words seed is located in /home/<user>/.phoenix, make sure to do a backup or you risk losing your funds.
Do not share the same seed with other phoenix instances (mobile or server), it will cause issues and channel force closes.
```



**Bewaar deze 12 woorden** - het is je enige garantie op herstel.



**Bericht 2 - Automatische liquiditeit:**


```
Continuous liquidity
Liquidity management is fully automated.
When receiving a Lightning payment that doesn't fit in your existing channel:
- If the payment amount is large enough to cover mining fees and service fees for automated liquidity,
then your channel will be created or enlarged right away.
- If the payment is too small, then the full amount is added to your fee credit,
and will be used later to pay for future fees. The fee credit is non-refundable.
```



Typ `Ik begrijp` voor elke bevestiging.



![Premier démarrage](assets/fr/01.webp)



*Phoenixd start voor het eerst op: back-upbevestigingen en automatische liquiditeit*



**3. Configuratie tijdens gebruik** (alleen in het Frans)



Voor continu gebruik maakt u een systemd :



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



*Phoenixd service actief en operationeel via systemd en `auto-liquidity` op 2m sat*



## Configuratie en beveiliging



### Configuratiebestand



Phoenixd maakt automatisch `~/.phoenix/phoenix.conf` aan met de essentiële parameters:



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



**Belangrijkste parameters:**




- `auto-liquiditeit`: Grootte van automatisch geopende kanalen (standaard: 2M Sats)
- http-wachtwoord`: Admin wachtwoord voor API (Invoice aanmaken EN betaling verzenden)
- http-wachtwoord-beperkte-toegang`: Beperkt wachtwoord (alleen aanmaak Invoice)



### Beveiligde toegang met HTTPS



Standaard is de Phoenixd API alleen toegankelijk via lokale HTTP (`http://127.0.0.1:9740`). Om je node van buitenaf te gebruiken (mobiele applicaties, andere servers, web integraties), moet je beveiligde HTTPS toegang configureren.



**Omgekeerd proxyprincipe:**


```
Internet → nginx (port 443 HTTPS) → Phoenixd (port 9740 HTTP local)
```



**Nginx** werkt als een **reverse proxy**: het luistert naar HTTPS-verzoeken van het internet op poort 443, stuurt ze lokaal door naar Phoenixd (poort 9740) en stuurt vervolgens versleutelde antwoorden terug naar de client.



**Het SSL/TLS**-certificaat is een digitaal bestand dat :




- De identiteit van je server bewijzen** (voorkomt man-in-the-middle-aanvallen)
- Maakt HTTPS**-encryptie mogelijk: alle gegevens, inclusief je API-wachtwoorden, worden tijdens het transport versleuteld
- Gratis** uitgegeven door Let's Encrypt via de certbot-tool



Met deze configuratie kun je :




- Beveiligde toegang tot de API vanaf het internet**
- Versleutel je API**-wachtwoorden tijdens het transport (om te voorkomen dat ze in onbewerkte tekst worden verzonden)
- Phoenixd** integreren in externe toepassingen die HTTPS vereisen
- Voldoen aan beveiligingsstandaarden** voor financiële API's



Configureer deze HTTPS reverse proxy met nginx :



**1. Nginx** configuratie



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



**2. SSL**-certificaat



```bash
sudo certbot --nginx -d phoenixd.your-domain.com
```



### Functietest



Controleer of Phoenixd goed werkt:



```bash
./phoenix-cli getinfo
./phoenix-cli getbalance
```



Deze commando's zouden JSON informatie moeten teruggeven over de status en balans van het knooppunt (in eerste instantie leeg).



![Commandes CLI](assets/fr/03.webp)



*Getinfo en getbalance commando's om de status van knooppunten te controleren*



## De API gebruiken



### Eerste ontvangsttest



**1. Maak een Lightning** Invoice



Gebruik de API om je eerste Invoice te maken:



```bash
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='First test' \
-d amountSat=100000
```



### Het automatische liquiditeitsmechanisme begrijpen



**Fundamenteel principe:** Wanneer je een Lightning-betaling ontvangt, moet Phoenixd soms een nieuw kanaal openen om het te kunnen ontvangen. Deze kanaalopening kost een vergoeding die **automatisch** wordt afgetrokken van het ontvangen bedrag.



**Concreet voorbeeld met 100.000 Sats:**



![Premier test de réception](assets/fr/04.webp)



*Eerste acceptatietest: Sats 100k ontvangen, eindsaldo Sats 75.561 na aftrek van liquiditeitskosten*



```bash
# Payment received: 100,000 sats
# Channel created: 2,115,000 sats total capacity
# Liquidity fee: 24,439 sats
# Final balance: 75,561 sats
```



**Tariefberekening:**




- Servicekosten**: 1% van kanaalcapaciteit (2.115.000 Sats) = 21.150 Sats
- Mining vergoedingen**: ~3.289 Sats (voor On-Chain transactie)
- Totaal**: 24.439 Sats automatisch afgetrokken



**Verificatie met CLI commando's:**


```bash
# View details of all channels
./phoenix-cli listchannels

# Important output:
# "toLocal": 75561000 (your balance in milli-sats)
# "toRemote": 2039439000 (ACINQ's balance)
# Total channel: 2,115,000 sats
```



![Nouveau solde après paiement](assets/fr/05.webp)



*Eindsaldo na betaling: 257 Sats resterend na Lightning-verzending*



**Geldkrediet voor kleine betalingen:** Als je betalingen ontvangt die te klein zijn om het openen van een kanaal te rechtvaardigen (< ca. 25k Sats), worden ze opgeslagen in een niet-terugbetaalbaar "vergoedingskrediet". Dit krediet wordt gebruikt om toekomstige kanaalkosten te betalen wanneer je een voldoende bedrag ontvangt.



**2. Volg kanaalopening**



Bekijk de logs van Phoenixd:



```bash
journalctl -u phoenixd -f
```



Je ziet de opening van het kanaal en de automatische aftrek van liquiditeitskosten. Vergoedingen variëren volgens Mempool Bitcoin voorwaarden, maar omvatten altijd 1% servicekosten plus de huidige Mining vergoeding.



**3. Controleer kanaal**



```bash
./phoenix-cli listchannels
```



Dit commando toont je actieve kanalen met hun status en balans.



### Volledige API-bewerkingen



Phoenixd stelt een REST API beschikbaar op poort 9740 waardoor :



**Basisbewerkingen:**


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



**Belangrijk voor de kosten:**




- Ontvangst**: 1% + Mining kosten voor automatische liquiditeit
- Verzending**: 0.4% routeringskosten op de Lightning Network



**Webhooks:** Webhooks stellen Phoenixd in staat om **automatisch** je applicaties op de hoogte te stellen wanneer zich een gebeurtenis voordoet (betaling ontvangen, Invoice betaald, kanaal geopend, etc.). In plaats van Phoenixd voortdurend om updates te vragen, ontvangt je applicatie een directe HTTP-melding.



**Je online winkel ontvangt automatisch een melding wanneer een klant voor een bestelling betaalt, zodat de transactie direct kan worden gevalideerd.



Configuratie in `phoenix.conf` :


```conf
webhook-url=https://your-app.com/webhook-phoenixd
webhook-secret=votre_secret_de_verification
```



## Geavanceerde toepassingen



### LNURL integraties



Phoenixd ondersteunt van nature LNURL-protocollen voor geavanceerde integratie:



**LNURL-Pay:** Betalen voor LNURL-compatibele diensten


```bash
curl -X POST http://localhost:9740/lnurlpay \
-u :your_password \
-d lnurl=LNURL1DP68GURN8GHJ7MRWW4EXCTN... \
-d amountSat=100
```



**LNURL-Withdraw :** Haal fondsen op bij LNURL-diensten


```bash
curl -X POST http://localhost:9740/lnurlwithdraw \
-u :your_password \
-d lnurl=lightning:LNURL1DP68GURN8GHJ7MRW...
```



**LNURL-Auth:** Authenticatie via Lightning om toegang te krijgen tot services


```bash
curl -X POST http://localhost:9740/lnurlauth \
-u :your_password \
-d lnurl=lnurl1dp68gurn8ghj7um5v93kket...
```



### Integratie met LNbits



LNbits kan Phoenixd gebruiken als financieringsbron volgens de [officiële documentatie] (https://docs.lnbits.org/guide/wallets.html):



**LNbits configuratie:**


```bash
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://localhost:9740/
PHOENIXD_API_PASSWORD=your_password_phoenixd
```



Met deze integratie kun je LNbits sub-accounts aanmaken die worden aangestuurd door je Phoenixd-node, waardoor je een webgebaseerde Interface krijgt voor het beheren van meerdere Lightning-portemonnees.



### Aangepaste toepassingen



Dankzij de uitgebreide REST API kun je :



**E-commerce:** Directe integratie van Lightning-betalingen in je winkel


**Donatiediensten:** Donatiesystemen met facturen en automatische webhooks


**Sociale netwerkbots:** Telegram/Discord-bots met tipfuncties


**Paywall Lightning:** Premium content beschikbaar tegen een Lightning vergoeding



## Veiligheid en best practices



### Toegangsbeveiliging



**API-wachtwoorden:** Automatisch gegenereerde wachtwoorden zijn de sleutels tot je Lightning-schatkist. Deel ze nooit en verander ze bij twijfel.



**Firewall:** Laat poort 9740 nooit rechtstreeks naar het internet openstaan. Gebruik altijd nginx met HTTPS.



**Geavanceerde verificatie:** Overweeg een VPN of Tailscale om de toegang tot je server te beperken tot alleen geautoriseerde apparaten.



### Essentiële back-ups



**seed herstel:** Bewaar je 12 woorden op een veilige plaats, buiten de server. Dit is je enige garantie op herstel.



*~/.phoenix directory:** Maak regelmatig een back-up van deze map (nadat Phoenixd is afgesloten) om de kanaalstatus te behouden en het herstel te versnellen.



**Service recovery codes:** Bewaar ook back-up codes voor alle diensten waarbij je 2FA activeert met je Phoenix.



### Bewaking en onderhoud



**Bewakingslogboeken:**


```bash
journalctl -u phoenixd -f  # Real-time logs
./phoenix-cli getinfo      # Node status
```



**Updates:** Bekijk [GitHub releases](https://github.com/ACINQ/phoenixd/releases) voor nieuwe versies. Updaten is zo simpel als het vervangen van de binary en het herstarten van de service.



## Vergelijking met alternatieven



### Phoenixd vs Phoenix standaard



**Phoenix standaard (mobiel) :**




- onmiddellijke installatie, nul configuratie
- gW-32 mobiel intuïtief
- zelfde auto-save als Phoenixd
- geen API voor ontwikkelaars
- geen toegang tot gedetailleerde logbestanden



**Phoenixd (server) :**




- hTTP API voor integraties
- ✅ Volledige toegang tot logboeken
- persoonlijke infrastructuur
- vereist technische vaardigheden
- serveronderhoud vereist



**Beide gebruiken ACINQ als hun LSP voor automatische liquiditeit.



### Phoenixd vs LND/Kernbliksem



**LND/kernbliksem :**




- totale controle, volledig Lightning-protocol
- grote gemeenschap, volwassen ecosysteem
- complex handmatig liquiditeitsbeheer
- grote leercurve



**Phoenixd :**




- automatisch liquiditeitsbeheer (zoals Phoenix mobile)
- aPI voor ontwikkelaars
- vereenvoudigde configuratie
- ❌ Gebruikt ACINQ als LSP (geen onafhankelijke routering)
- minder flexibel dan volledige knooppunten



## Veelvoorkomende problemen oplossen



### Problemen met API-toegang



**Authenticatie mislukt" fout:**


1. Controleer het wachtwoord in het bestand `~/.phoenix/phoenix.conf`


2. Authenticatie formaat `-u:wachtwoord` controleren


3. Zorg ervoor dat Phoenixd draait (`./phoenix-CLI getinfo`)



**Time-outs verbinding:**




- Controleer of Phoenixd luistert op de juiste poort (9740)
- Test lokale toegang voordat u HTTPS configureert
- Controleer de logboeken: `journalctl -u phoenixd -f`



### Liquiditeitsproblemen



**Betalingen komen niet aan :**


1. Controleer of het bedrag hoger is dan de minimumdrempel (~30k Sats)


2. Logboeken raadplegen om kanaalfouten te identificeren


3. Herstart Phoenixd indien nodig



**Saldo in "uitgavenkrediet":**


Kleine betalingen worden opgeslagen als provisie. Ontvang een groter bedrag om het kanaal te openen en deze fondsen vrij te geven.



## Conclusie



Phoenixd vertegenwoordigt een uitstekend compromis tussen gebruiksgemak en technische soevereiniteit voor ontwikkelaars. Het biedt een eenvoudige maar krachtige Lightning API met automatisch liquiditeitsbeheer, waardoor de complexiteit van traditionele Lightning nodes wegvalt.



Deze oplossing is bijzonder geschikt voor ontwikkelaars en bedrijven die :




- Bitcoin Lightning integreren in uw toepassingen
- Vermijd de complexiteit van het beheer van Lightning-kanalen
- Profiteer van een zelf gehoste infrastructuur
- Een eenvoudige, betrouwbare API



Met Phoenixd bouw je je eigen Lightning-infrastructuur met een moderne REST API en automatisch beheer van technische aspecten. Het is de ideale oplossing voor het democratiseren van Lightning-integratie in je projecten.



## Nuttige bronnen



### Officiële documentatie




- GitHub Phoenixd** : [github.com/ACINQ/phoenixd](https://github.com/ACINQ/phoenixd) - Broncode en releases
- Phoenix Server** site: [phoenix.acinq.co/server](https://phoenix.acinq.co/server) - Volledige documentatie
- FAQ Phoenixd** : [phoenix.acinq.co/server/faq](https://phoenix.acinq.co/server/faq) - Veelgestelde vragen



### Steun van de gemeenschap




- GitHub Issues** : [github.com/ACINQ/phoenixd/issues](https://github.com/ACINQ/phoenixd/issues) - Technische ondersteuning
- Twitter ACINQ** : [@ACINQ_co](https://twitter.com/ACINQ_co) - Nieuws en aankondigingen