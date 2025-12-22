---
name: Phoenixd
description: Implementirajte svoj minimalistički Lightning čvor sa Phoenixd
---

![cover](assets/cover.webp)



Finansijska autonomija takođe znači kontrolu nad vašom Lightning infrastrukturom. Za programere i kompanije koje žele da integrišu Bitcoin Lightning u svoje aplikacije, **Phoenixd** predstavlja idealno rešenje: minimalistički, specijalizovani Lightning čvor sa automatskim upravljanjem likvidnošću.



Phoenixd je Lightning server koji je razvio ACINQ, dizajniran posebno za slanje i primanje Lightning uplata putem HTTP API-ja. Za razliku od implementacija sa punim funkcijama kao što su LND ili Core Lightning, Phoenixd apstrahuje svu složenost upravljanja kanalima dok čuva samostalnu zaštitu vaših sredstava.



U ovom vodiču ćemo pogledati kako instalirati, konfigurisati i koristiti Phoenixd za razvoj Lightning aplikacija sa samostalno hostovanom infrastrukturom i jednostavnim API-jem za korišćenje.



## Šta je Phoenixd?



Phoenixd je minimalan, specijalizovan Lightning čvor razvijen od strane ACINQ-a. To je rešenje dizajnirano za programere i preduzeća koja žele da integrišu Lightning u svoje aplikacije bez složenosti upravljanja Full node.



### Princip rada



**Phoenixd je minimalni Lightning čvor koji koristi ACINQ kao svoj LSP (pružalac Lightning usluga) za automatsku likvidnost. Kada primate Lightning uplate, automatski otvara kanale sa ACINQ čvorovima kako bi alocirao potrebni dolazni kapacitet. Ova likvidnost "u hodu" je trenutna, ali se naplaćuje tačno **1% + Mining naknade** od primljenog iznosa.**



**Automatizovano upravljanje:** Sistem upravlja sa tri ključna Elements:




- Lightning** kanali: Otvaraj, zatvaraj i upravljaj automatski po potrebi
- Dolazna/odlazna likvidnost**: Automatsko obezbeđivanje putem spajanja i otvaranja kanala
- Kredit za naknadu** : Mala plaćanja koja nisu dovoljna da opravdaju kanal čuvaju se kao rezerva za buduće troškove



### Phoenixd pogodnosti



**Vi kontrolišete svoje privatne ključeve (12-reči seed) i sredstva. Phoenixd generiše vaš Wallet lokalno bez ikakvog deljenja vaših ključeva.



**Lična infrastruktura:** Phoenixd radi na vašem serveru, pružajući vam pristup detaljnim zapisima, konfiguraciji i API kontroli. Više niste zavisni od usluge treće strane za pristup vašim sredstvima.



**Integrisani API:** Phoenixd ima HTTP API za integraciju sa drugim uslugama, nativnu podršku za LNURL i razvoj prilagođenih aplikacija.



**Jednostavnost integracije:** Zahvaljujući svom jednostavnom REST API-ju, Phoenixd se može integrisati u bilo koju aplikaciju ili uslugu koja zahteva Lightning plaćanja.



**Važna napomena:** Automatska likvidnost i dalje dolazi od ACINQ kao LSP (Lightning Service Provider). Phoenixd koristi isti mehanizam kao Phoenix mobilni za automatsko upravljanje kanalima.



## Instaliranje Phoenixd



### Preduslovi



Phoenixd zahteva Linux okruženje (preporučuje se Ubuntu/Debian), sa osnovnim veštinama rada u komandnoj liniji. Za optimalne performanse, biće vam potrebno:





- Linux server**: VPS ili lokalna mašina sa stabilnom vezom
- OpenJDK 21** : Java runtime okruženje
- Stabilna internet konekcija**: Za sinhronizaciju sa Lightning Network
- Naziv domena** (opciono) : Za siguran HTTPS pristup API-ju



### Preuzimanje i instalacija



**1. Preuzmi Phoenixd**



Idite na stranicu [GitHub releases](https://github.com/ACINQ/phoenixd/releases) i preuzmite najnoviju verziju za vašu arhitekturu:



```bash
# For Linux x86_64
# Replace with the latest release
wget https://github.com/ACINQ/phoenixd/releases/download/v0.6.1/phoenixd-0.6.1-linux-x64.zip
unzip -j phoenixd-0.6.1-linux-x64.zip
chmod +x phoenixd phoenix-cli
```



**2. Prvo pokretanje



Pokreni Phoenixd za inicijalizaciju:



```bash
./phoenixd
```



Prilikom prvog pokretanja, od vas će se tražiti da potvrdite dva važna koraka upisivanjem "Razumem" :



**Poruka 1 - Rezerva:**


```
This software is self-custodial, you have full control and responsibility over your funds.
Your 12-words seed is located in /home/<user>/.phoenix, make sure to do a backup or you risk losing your funds.
Do not share the same seed with other phoenix instances (mobile or server), it will cause issues and channel force closes.
```



**Sačuvaj ovih 12 reči** - to je tvoja jedina garancija za oporavak.



**Poruka 2 - Automatska likvidnost:**


```
Continuous liquidity
Liquidity management is fully automated.
When receiving a Lightning payment that doesn't fit in your existing channel:
- If the payment amount is large enough to cover mining fees and service fees for automated liquidity,
then your channel will be created or enlarged right away.
- If the payment is too small, then the full amount is added to your fee credit,
and will be used later to pay for future fees. The fee credit is non-refundable.
```



Ukucajte `Razumem` za svaku potvrdu.



![Premier démarrage](assets/fr/01.webp)



*Phoenixd se pokreće prvi put: potvrde rezervnih kopija i automatska likvidnost*



**3. Konfiguracija u radu** (samo na francuskom)



Za kontinuirani rad, kreirajte systemd:



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



*Phoenixd servis aktivan i operativan putem systemd i `auto-liquidity` na 2m sat*



## Konfiguracija i sigurnost



### Konfiguraciona datoteka



Phoenixd automatski kreira `~/.phoenix/phoenix.conf` sa osnovnim parametrima:



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



**Ključni parametri:**




- `auto-liquidity`: Veličina automatski otvorenih kanala (podrazumevano: 2M Sats)
- http-password`: Admin lozinka za API (Invoice kreiranje I slanje plaćanja)
- http-password-limited-access`: Ograničena lozinka (samo za kreiranje Invoice)



### Siguran pristup sa HTTPS



Podrazumevano, Phoenixd API je dostupan samo putem lokalnog HTTP-a (`http://127.0.0.1:9740`). Da biste koristili svoj čvor spolja (mobilne aplikacije, drugi serveri, web integracije), potrebno je da konfigurišete siguran HTTPS pristup.



**Princip reverznog proxy-ja:**


```
Internet → nginx (port 443 HTTPS) → Phoenixd (port 9740 HTTP local)
```



**Nginx** deluje kao **reverse proxy**: sluša HTTPS zahteve sa Interneta na portu 443, preusmerava ih lokalno na Phoenixd (port 9740), zatim šalje enkriptovane odgovore nazad klijentu.



**SSL/TLS** sertifikat je digitalna datoteka koja :




- Dokaži identitet svog servera** (sprečava napade posrednika)
- Omogućava HTTPS** enkripciju: svi podaci, uključujući vaše API lozinke, su šifrovani tokom prenosa
- Izdato besplatno** od strane Let's Encrypt putem alata certbot



Ova konfiguracija vam omogućava da :




- Osigurajte pristup API-ju sa Interneta**
- Šifrujte svoje API** lozinke tokom prenosa (da biste sprečili njihovo prenošenje u čistom tekstu)
- Integrisati Phoenixd** u eksterne aplikacije koje zahtevaju HTTPS
- Usklađenost sa sigurnosnim standardima** za finansijske API-je



Konfigurišite ovaj HTTPS obrnuti proxy sa nginx-om:



**1. Nginx** konfiguracija



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



**2. SSL** sertifikat



```bash
sudo certbot --nginx -d phoenixd.your-domain.com
```



### Funkcija test



Proverite da Phoenixd radi ispravno:



```bash
./phoenix-cli getinfo
./phoenix-cli getbalance
```



Ove komande treba da vrate JSON informacije o statusu čvora i stanju (u početku prazno).



![Commandes CLI](assets/fr/03.webp)



*Getinfo i getbalance komande za proveru statusa čvora*



## Korišćenje API-ja



### Prvi test prijema



**1. Kreiraj Lightning** Invoice



Koristite API da kreirate svoj prvi Invoice:



```bash
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='First test' \
-d amountSat=100000
```



### Razumevanje automatskog mehanizma likvidnosti



**Osnovni princip:** Kada primite Lightning uplatu, Phoenixd ponekad mora da otvori novi kanal kako bi mogao da je primi. Otvaranje ovog kanala nosi trošak koji se **automatski oduzima** od primljenog iznosa.



**Konkretan primer sa 100.000 Sats:**



![Premier test de réception](assets/fr/04.webp)



*Prvi test prihvatanja: Sats 100k primljeno, konačno stanje Sats 75.561 nakon odbitka troškova likvidnosti*



```bash
# Payment received: 100,000 sats
# Channel created: 2,115,000 sats total capacity
# Liquidity fee: 24,439 sats
# Final balance: 75,561 sats
```



**Izračun naknade:**




- Naknada za uslugu**: 1% kapaciteta kanala (2,115,000 Sats) = 21,150 Sats
- Mining naknade**: ~3,289 Sats (za On-Chain transakciju)
- Ukupno**: 24,439 Sats automatski odbijeno



**Verifikacija sa CLI komandama:**


```bash
# View details of all channels
./phoenix-cli listchannels

# Important output:
# "toLocal": 75561000 (your balance in milli-sats)
# "toRemote": 2039439000 (ACINQ's balance)
# Total channel: 2,115,000 sats
```



![Nouveau solde après paiement](assets/fr/05.webp)



*Konačno stanje nakon poslatog plaćanja: 257 Sats preostalo nakon Lightning isporuke*



**Kredit za naknade za male uplate:** Ako primite uplate koje su premale da bi opravdale otvaranje kanala (< otprilike 25k Sats), one se čuvaju u nepovratnom "kreditu za naknade". Ovaj kredit će se koristiti za plaćanje budućih naknada za kanale kada primite dovoljan iznos.



**2. Prati otvaranje kanala**



Gledajte Phoenixd dnevnike:



```bash
journalctl -u phoenixd -f
```



Videćete otvaranje kanala i automatsko odbijanje naknada za likvidnost. Naknade variraju u skladu sa uslovima Mempool Bitcoin, ali uvek uključuju 1% naknade za uslugu plus trenutnu Mining naknadu.



**3. Proveri kanal**



```bash
./phoenix-cli listchannels
```



Ova komanda prikazuje vaše aktivne kanale sa njihovim statusom i stanjem.



### Dovršite API operacije



Phoenixd izlaže REST API na portu 9740 omogućavajući:



**Osnovne operacije:**


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



**Važno o troškovima:**




- Račun**: 1% + Mining naknada za automatsku likvidnost
- Dostava**: 0,4% naknada za usmeravanje na Lightning Network



**Webhooks:** Webhooks omogućavaju Phoenixd-u da **automatski obavesti** vaše aplikacije kada se dogodi neki događaj (primljena uplata, Invoice plaćen, kanal otvoren, itd.). Umesto da konstantno pitate Phoenixd za ažuriranja, vaša aplikacija prima trenutnu HTTP notifikaciju.



**Vaša online prodavnica automatski prima obaveštenje kada kupac plati porudžbinu, omogućavajući trenutnu validaciju transakcije.



Konfiguracija u `phoenix.conf` :


```conf
webhook-url=https://your-app.com/webhook-phoenixd
webhook-secret=votre_secret_de_verification
```



## Napredne aplikacije



### LNURL integracije



Phoenixd natively supports LNURL protocols for advanced integration:



**LNURL-Pay:** Platite za usluge kompatibilne sa LNURL


```bash
curl -X POST http://localhost:9740/lnurlpay \
-u :your_password \
-d lnurl=LNURL1DP68GURN8GHJ7MRWW4EXCTN... \
-d amountSat=100
```



**LNURL-Withdraw :** Preuzimanje sredstava sa LNURL usluga


```bash
curl -X POST http://localhost:9740/lnurlwithdraw \
-u :your_password \
-d lnurl=lightning:LNURL1DP68GURN8GHJ7MRW...
```



**LNURL-Auth:** Autentifikacija putem Lightning-a za pristup uslugama


```bash
curl -X POST http://localhost:9740/lnurlauth \
-u :your_password \
-d lnurl=lnurl1dp68gurn8ghj7um5v93kket...
```



### Integracija sa LNbits



LNbits može koristiti Phoenixd kao izvor finansiranja prema svojoj [zvaničnoj dokumentaciji](https://docs.lnbits.org/guide/wallets.html):



**LNbits konfiguracija:**


```bash
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://localhost:9740/
PHOENIXD_API_PASSWORD=your_password_phoenixd
```



Ova integracija vam omogućava kreiranje LNbits podračuna koje pokreće vaš Phoenixd čvor, pružajući web-bazirani Interface za upravljanje višestrukim Lightning novčanicima.



### Prilagođene aplikacije



Zahvaljujući svom sveobuhvatnom REST API-ju, možete razviti :



**E-commerce:** Direktna integracija Lightning plaćanja u vašu prodavnicu


**Donatorske usluge:** Sistemi za donacije sa fakturama i automatskim webhook-ovima


**Botovi za društvene mreže:** Telegram/Discord botovi sa funkcijama napojnica


**Paywall Lightning:** Premium sadržaj dostupan uz Lightning naknadu



## Bezbednost i najbolje prakse



### Zaštita pristupa



**API lozinke:** Automatski generisane lozinke su ključevi vašeg Lightning trezora. Nikada ih ne delite i promenite ih ako ste u nedoumici.



**Firewall:** Nikada ne ostavljajte port 9740 otvoren direktno prema Internetu. Uvek koristite nginx sa HTTPS.



**Poboljšana autentifikacija:** Razmislite o korišćenju VPN-a ili Tailscale-a kako biste ograničili pristup vašem serveru samo na autorizovane uređaje.



### Osnovne sigurnosne kopije



**seed oporavak:** Sačuvajte svojih 12 reči na sigurnom mestu, van servera. Ovo je vaša jedina garancija za oporavak.



*~/.phoenix direktorijum:** Redovno pravite rezervne kopije ove fascikle (nakon što je Phoenixd isključen) kako biste sačuvali status kanala i ubrzali obnavljanje.



**Kodovi za oporavak usluge:** Takođe čuvajte rezervne kodove za sve usluge gde aktivirate 2FA sa vašim Phoenixom.



### Praćenje i održavanje



**Praćenje logova:**


```bash
journalctl -u phoenixd -f  # Real-time logs
./phoenix-cli getinfo      # Node status
```



**Ažuriranja:** Pratite [GitHub izdanja](https://github.com/ACINQ/phoenixd/releases) za nove verzije. Ažuriranje je jednostavno kao zamena binarne datoteke i ponovno pokretanje usluge.



## Poređenje sa alternativama



### Phoenixd vs Phoenix standard



**Phoenix standard (mobilni) :**




- ✅ Neposredna instalacija, nulta konfiguracija
- ✅ Interface mobilni intuitivan
- ✅ Ista automatska pohrana kao Phoenixd
- ❌ Nema API-ja za programere
- ❌ Nema pristupa detaljnim zapisima



**Phoenixd (server) :**




- ✅ HTTP API za integracije
- ✅ Potpun pristup logovima
- ✅ Lična infrastruktura
- ❌ Zahteva tehničke veštine
- ❌ Potrebno održavanje servera



**Oboje koriste ACINQ kao svoj LSP za automatsku likvidnost.



### Phoenixd vs LND/Core Lightning



**LND/Core Lightning :**




- ✅ Totalna kontrola, potpuni Lightning protokol
- ✅ Velika zajednica, zreo ekosistem
- ❌ Kompleksno ručno upravljanje likvidnošću
- ❌ Velika kriva učenja



**Phoenixd :**




- ✅ Automatsko upravljanje likvidnošću (kao Phoenix mobilni)
- ✅ API za developere
- ✅ Pojednostavljena konfiguracija
- ❌ Koristi ACINQ kao LSP (nema nezavisnog rutiranja)
- ❌ Manje fleksibilan od kompletnih čvorova



## Rešavanje uobičajenih problema



### Problemi sa pristupom API-ju



**Greška "Autentifikacija nije uspela":**


1. Proverite lozinku u datoteci `~/.phoenix/phoenix.conf`


2. Proveri format autentifikacije `-u:password`


3. Uverite se da Phoenixd radi (`./phoenix-CLI getinfo`)



**Vremenska ograničenja za povezivanje:**




- Proverite da li Phoenixd sluša na ispravnom portu (9740)
- Testirajte lokalni pristup pre nego što konfigurišete HTTPS
- Proveri logove: `journalctl -u phoenixd -f`



### Problemi sa likvidnošću



**Uplate ne stižu :**


1. Proverite da iznos prelazi minimalni prag (~30k Sats)


2. Konsultujte dnevnike kako biste identifikovali greške kanala


3. Ponovo pokreni Phoenixd ako je potrebno



**Stanje u "trošku kredita":**


Mala plaćanja se čuvaju kao rezerva. Primite veći iznos da biste pokrenuli otvaranje kanala i oslobodili ova sredstva.



## Zaključak



Phoenixd predstavlja odličan kompromis između jednostavnosti korišćenja i tehničkog suvereniteta za programere. Nudi jednostavan, ali moćan Lightning API sa automatskim upravljanjem likvidnošću, eliminišući složenost tradicionalnih Lightning čvorova.



Ovo rešenje je posebno pogodno za programere i kompanije koje žele da :




- Integrisati Bitcoin Lightning u vaše aplikacije
- Izbegnite složenost upravljanja Lightning kanalima
- Koristite prednosti samostalno hostovane infrastrukture
- Jednostavan, pouzdan API



Sa Phoenixd-om, izgradite sopstvenu privatnu Lightning infrastrukturu sa modernim REST API-jem i automatskim upravljanjem tehničkim aspektima. To je idealno rešenje za demokratizaciju Lightning integracije u vašim projektima.



## Korisni resursi



### Zvanična dokumentacija




- GitHub Phoenixd** : [github.com/ACINQ/phoenixd](https://github.com/ACINQ/phoenixd) - Izvorni kod i izdanja
- Phoenix Server** sajt: [phoenix.acinq.co/server](https://phoenix.acinq.co/server) - Kompletna dokumentacija
- FAQ Phoenixd** : [phoenix.acinq.co/server/faq](https://phoenix.acinq.co/server/faq) - Često postavljana pitanja



### Podrška zajednice




- GitHub Issues** : [github.com/ACINQ/phoenixd/issues](https://github.com/ACINQ/phoenixd/issues) - Tehnička podrška
- Twitter ACINQ** : [@ACINQ_co](https://twitter.com/ACINQ_co) - Vesti i najave