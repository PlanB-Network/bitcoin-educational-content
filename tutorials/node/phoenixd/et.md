---
name: Phoenixd
description: Võtke oma minimalistlik Lightning-sõlm kasutusele koos Phoenixd-ga
---

![cover](assets/cover.webp)



Finantsautonoomia tähendab ka oma Lightning-infrastruktuuri kontrollimist. Arendajatele ja ettevõtetele, kes soovivad integreerida Bitcoin Lightningi oma rakendustesse, on **Phoenixd** ideaalne lahendus: minimalistlik, spetsialiseeritud Lightning-sõlm koos automaatse likviidsuse juhtimisega.



Phoenixd on ACINQ poolt välja töötatud Lightning server, mis on loodud spetsiaalselt Lightning maksete saatmiseks ja vastuvõtmiseks HTTP API kaudu. Erinevalt täisfunktsionaalsetest rakendustest, nagu LND või Core Lightning, abstraheerib Phoenixd kogu kanalihalduse keerukuse, säilitades samal ajal teie rahaliste vahendite enesekaitsmise.



Selles õpetuses vaatleme, kuidas paigaldada, konfigureerida ja kasutada Phoenixd, et arendada Lightning rakendusi isehostitava infrastruktuuri ja lihtsa APIga.



## Mis on Phoenixd?



Phoenixd on ACINQ poolt välja töötatud minimaalne, spetsialiseeritud Lightning-sõlm. See on lahendus, mis on mõeldud arendajatele ja ettevõtetele, kes soovivad Lightningut oma rakendustesse integreerida ilma Full node halduskompleksita.



### Tööpõhimõte



**Phoenixd on minimaalne Lightning-sõlm, mis kasutab automaatseks likviidsuseks ACINQ-d kui LSP-d (Lightning Service Provider). Kui saate Lightning-makseid, avab see automaatselt kanalid ACINQ-sõlmedega, et eraldada vajalikku sissetulevat võimsust. See "jooksev" likviidsus on kohene, kuid selle eest tuleb tasuda täpselt **1% + Mining tasud** saadud summast.



**Automaatne juhtimine:** Süsteem haldab kolme peamist Elements:




- Välk** kanalid: Avage, sulgege ja haldage automaatselt vastavalt vajadusele
- Sissetulev/väljaminev likviidsus**: Automaatne varustamine ühendamise ja kanali avamise kaudu
- Tasu krediit** : Väikesed maksed, mis ei ole piisavad kanali õigustamiseks, salvestatakse tulevaste tasude katteks



### Phoenixd eelised



**Sina kontrollid oma isiklikke võtmeid (12-sõnaline seed) ja raha. Phoenixd genereerib teie Wallet kohalikult, ilma et te kunagi oma võtmeid jagaksite.



**Personaalne infrastruktuur:** Phoenixd töötab teie serveris, andes teile juurdepääsu üksikasjalikele logidele, konfiguratsioonile ja API kontrollile. Te ei ole enam sõltuvuses kolmanda osapoole teenusest, et pääseda ligi oma rahalistele vahenditele.



**Integreeritud API:** Phoenixd omab HTTP API-d teiste teenustega integreerimiseks, LNURL-i emakeeleks ja kohandatud rakenduste arendamiseks.



**Lihtne integreerimine:** Tänu lihtsale REST API-le saab Phoenixd integreerida mis tahes rakendusse või teenusesse, mis nõuab Lightning-makseid.



**Tähtis märkus:** Automaatne likviidsus tuleb endiselt ACINQ-lt kui LSP-lt (Lightning Service Provider). Phoenixd kasutab automaatseks kanalihalduseks sama mehhanismi nagu Phoenix mobile.



## Phoenixd paigaldamine



### Eeltingimused



Phoenixd nõuab Linuxi keskkonda (soovitatav on Ubuntu/Debian) ja mõningaid põhilisi käsurea oskusi. Optimaalse jõudluse saavutamiseks on vaja :





- Linuxi server**: VPS või kohalik masin stabiilse ühendusega
- OpenJDK 21** : Java jooksutuskeskkond
- Stabiilne internetiühendus**: Lightning Network-ga sünkroniseerimiseks
- Domeeninimi** (vabatahtlik) : Turvalise HTTPS-juurdepääsu jaoks API-le



### Allalaadimine ja paigaldamine



**1. Lae alla Phoenixd**



Mine [GitHub releases] lehele (https://github.com/ACINQ/phoenixd/releases) ja lae alla uusim versioon oma arhitektuuri jaoks:



```bash
# For Linux x86_64
# Replace with the latest release
wget https://github.com/ACINQ/phoenixd/releases/download/v0.6.1/phoenixd-0.6.1-linux-x64.zip
unzip -j phoenixd-0.6.1-linux-x64.zip
chmod +x phoenixd phoenix-cli
```



**2. Esimene käivitamine



Käivitage Phoenixd initsialiseerimiseks:



```bash
./phoenixd
```



Esimesel käivitamisel palutakse teil kinnitada kaks olulist sammu, kirjutades "ma saan aru" :



**Sõnum 1 - Varukoopia:**


```
This software is self-custodial, you have full control and responsibility over your funds.
Your 12-words seed is located in /home/<user>/.phoenix, make sure to do a backup or you risk losing your funds.
Do not share the same seed with other phoenix instances (mobile or server), it will cause issues and channel force closes.
```



**Säilitage need 12 sõna** - see on teie ainus garantii taastumiseks.



**Sõnum 2 - Automaatne likviidsus:**


```
Continuous liquidity
Liquidity management is fully automated.
When receiving a Lightning payment that doesn't fit in your existing channel:
- If the payment amount is large enough to cover mining fees and service fees for automated liquidity,
then your channel will be created or enlarged right away.
- If the payment is too small, then the full amount is added to your fee credit,
and will be used later to pay for future fees. The fee credit is non-refundable.
```



Kirjutage iga kinnituse puhul "ma saan aru".



![Premier démarrage](assets/fr/01.webp)



*Phoenixd käivitub esimest korda: varukoopia kinnitused ja automaatne likviidsus*



**3. Kasutusel olev konfiguratsioon** (ainult prantsuse keeles)



Pidevaks tööks looge systemd :



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



*Phoenixd teenus aktiivne ja toimiv systemd ja `auto-liquidity` kaudu 2m sat* juures



## Konfiguratsioon ja turvalisus



### Konfiguratsioonifail



Phoenixd loob automaatselt faili `~/.phoenix/phoenix.conf` koos oluliste parameetritega:



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



**Väikeparameetrid:**




- "Automaatne likviidsus": Automaatselt avatud kanalite suurus (vaikimisi: 2M Sats)
- http-password`: Administraatori parool API jaoks (Invoice loomine JA maksete saatmine)
- http-password-limited-access`: Piiratud parool (ainult Invoice loomine)



### Turvaline juurdepääs HTTPS-i abil



Vaikimisi on Phoenixd API kättesaadav ainult kohaliku HTTP kaudu (`http://127.0.0.1:9740`). Kui soovite oma sõlme kasutada väljastpoolt (mobiilirakendused, muud serverid, veebiintegratsioonid), peate seadistama turvalise HTTPS-juurdepääsu.



**Pöördvolituse põhimõte:**


```
Internet → nginx (port 443 HTTPS) → Phoenixd (port 9740 HTTP local)
```



**Nginx** toimib **pöördproxy'na**: ta võtab vastu HTTPS päringuid internetist pordist 443, suunab need ümber Phoenixd'ile lokaalselt (port 9740) ja saadab seejärel krüpteeritud vastused kliendile tagasi.



**SSL/TLS** sertifikaat on digitaalne fail, mis :




- Tõendab teie serveri identiteeti** (takistab man-in-the-middle rünnakuid)
- Võimaldab HTTPS** krüpteerimist: kõik andmed, sealhulgas teie API paroolid, on transpordi ajal krüpteeritud
- Väljastatakse tasuta** Let's Encrypt'i poolt certbot tööriista kaudu



See konfiguratsioon võimaldab teil :




- Turvaline juurdepääs API-le internetist**
- Krüpteerige oma API** paroolid transpordi ajal (et vältida nende edastamist selge tekstina)
- Integreerida Phoenixd** välistesse rakendustesse, mis nõuavad HTTPS-i
- Vastavus finants-APIde turvastandarditele**



Konfigureerige see HTTPS pöördproxy koos nginxiga :



**1. Nginx** konfiguratsioon



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



**2. SSL** sertifikaat



```bash
sudo certbot --nginx -d phoenixd.your-domain.com
```



### Funktsiooni test



Kontrollige, et Phoenixd töötab korralikult:



```bash
./phoenix-cli getinfo
./phoenix-cli getbalance
```



Need käsud peaksid tagastama JSON-teavet sõlme staatuse ja saldo kohta (esialgu tühja).



![Commandes CLI](assets/fr/03.webp)



*Getinfo ja getbalance käsud sõlme oleku kontrollimiseks*



## API kasutamine



### Esimene vastuvõtukatsetus



**1. Looge välk** Invoice



Kasutage API-d oma esimese Invoice loomiseks:



```bash
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='First test' \
-d amountSat=100000
```



### Automaatse likviidsusmehhanismi mõistmine



**Põhimõte:** Kui saate välkmakse, peab Phoenixd mõnikord avama uue kanali, et seda vastu võtta. See kanali avamine maksab tasu, mis **automaatselt** saadavast summast maha arvestatakse.



**Konkreetne näide 100 000 Sats:**



![Premier test de réception](assets/fr/04.webp)



*Esimene vastuvõtutest: Sats 100k saadud, Sats lõppsaldo 75.561 pärast likviidsuskulude mahaarvamist*



```bash
# Payment received: 100,000 sats
# Channel created: 2,115,000 sats total capacity
# Liquidity fee: 24,439 sats
# Final balance: 75,561 sats
```



**Tasu arvutamine:**




- Teenustasu**: 1% kanali võimsusest (2,115,000 Sats) = 21,150 Sats
- Mining tasud**: ~3,289 Sats (On-Chain tehingu puhul)
- Kokku**: 24,439 Sats automaatselt maha arvatud



**Kontroll CLI käskudega:**


```bash
# View details of all channels
./phoenix-cli listchannels

# Important output:
# "toLocal": 75561000 (your balance in milli-sats)
# "toRemote": 2039439000 (ACINQ's balance)
# Total channel: 2,115,000 sats
```



![Nouveau solde après paiement](assets/fr/05.webp)



*Lõppsaldo pärast makse saatmist: 257 Sats, mis on jäänud pärast Lightning-saadetist*



**Tasu krediit väikeste maksete puhul:** Kui saad makseid, mis on liiga väikesed, et õigustada kanali avamist (< u. 25k Sats), salvestatakse need tagastamatu "tasu krediidina". Seda krediiti kasutatakse tulevaste kanalitasude maksmiseks, kui saate piisava summa.



**2. Järgige kanali avanemist**



Vaadake Phoenixdi logisid:



```bash
journalctl -u phoenixd -f
```



Näete kanali avamist ja likviidsustasu automaatset mahaarvamist. Tasud varieeruvad vastavalt Mempool Bitcoin tingimustele, kuid sisaldavad alati 1% teenustasu pluss jooksev Mining tasu.



**3. Kontrollige kanalit**



```bash
./phoenix-cli listchannels
```



See käsk näitab teie aktiivseid kanaleid koos nende staatuse ja saldoga.



### Täielikud API toimingud



Phoenixd pakub REST API-d pordil 9740, mis võimaldab :



**Baasilised toimingud:**


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



**Kuludest oluline:**




- Kviitung**: 1% + Mining tasu automaatse likviidsuse eest
- Laevandus**: 0.4% marsruutimistasu Lightning Network puhul



**Webhooks:** Webhooks võimaldavad Phoenixdil **automaatselt teavitada** teie rakendusi, kui mingi sündmus (makse saabunud, Invoice makstud, kanal avatud jne). Selle asemel, et pidevalt Phoenixdilt uuendusi küsida, saab teie rakendus kohese HTTP-teate.



** Teie veebipood saab automaatselt teate, kui klient maksab tellimuse eest, võimaldades tehingu kohese kinnitamise.



Konfiguratsioon failis `phoenix.conf` :


```conf
webhook-url=https://your-app.com/webhook-phoenixd
webhook-secret=votre_secret_de_verification
```



## Täiustatud rakendused



### LNURL integratsioonid



Phoenixd toetab algselt LNURL-protokolle täiustatud integratsiooni jaoks:



**LNURL-Pay:** Tasu LNURL-ühilduvate teenuste eest


```bash
curl -X POST http://localhost:9740/lnurlpay \
-u :your_password \
-d lnurl=LNURL1DP68GURN8GHJ7MRWW4EXCTN... \
-d amountSat=100
```



**LNURL-Withdraw :** Rahaliste vahendite hankimine LNURL-teenustest


```bash
curl -X POST http://localhost:9740/lnurlwithdraw \
-u :your_password \
-d lnurl=lightning:LNURL1DP68GURN8GHJ7MRW...
```



**LNURL-Auth:** Autentimine Lightning'i kaudu teenustele juurdepääsuks


```bash
curl -X POST http://localhost:9740/lnurlauth \
-u :your_password \
-d lnurl=lnurl1dp68gurn8ghj7um5v93kket...
```



### Integratsioon LNbitsiga



LNbits võib vastavalt oma [ametlikule dokumentatsioonile](https://docs.lnbits.org/guide/wallets.html) kasutada rahastamisallikana Phoenixd:



**LNbits konfiguratsioon:**


```bash
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://localhost:9740/
PHOENIXD_API_PASSWORD=your_password_phoenixd
```



See integratsioon võimaldab teil luua LNbits'i alamkontosid, mis töötavad teie Phoenixd-sõlme kaudu, pakkudes veebipõhist Interface mitmete Lightning-rahakottide haldamiseks.



### Kohandatud rakendused



Tänu selle põhjalikule REST API-le saate arendada :



**E-kaubandus:** Lightning-maksete otsene integreerimine teie poodi


**Doonorlusteenused:** Annetussüsteemid koos arvete ja automaatsete veebikonksudega


**Sotsiaalvõrgustike robotid:** Telegram/Discord robotid koos vihjefunktsioonidega


**Paywall Lightning:** Premium-sisu on saadaval Lightning-tasu eest



## Ohutus ja parimad tavad



### Juurdepääsukaitse



**API paroolid:** Automaatselt genereeritud paroolid on teie Lightning'i varakambri võtmed. Ärge kunagi jagage neid ja muutke neid kahtluse korral.



**Firewall:** Ärge kunagi jätke port 9740 otse internetti avatuks. Kasutage alati nginx'i koos HTTPS-iga.



**Tihedam autentimine:** Kaaluge VPN-i või Tailscale'i kasutamist, et piirata juurdepääsu serverile ainult volitatud seadmetele.



### Olulised varukoopiad



**seed taastamine:** Salvesta oma 12 sõna turvalisse kohta väljaspool serverit. See on teie ainus tagatis taastumiseks.



*~/.phoenix kataloog:** Varundage seda kausta regulaarselt (pärast Phoenixd-i sulgemist), et säilitada kanali olek ja kiirendada taastamist.



**teenuste taastamise koodid:** Hoidke ka kõigi teenuste varakoodid, mille puhul te aktiveerite 2FA oma Phoenixiga.



### Järelevalve ja hooldus



**Monitooring logid:**


```bash
journalctl -u phoenixd -f  # Real-time logs
./phoenix-cli getinfo      # Node status
```



**Updates:** Jälgige [GitHub releases](https://github.com/ACINQ/phoenixd/releases) uute versioonide jaoks. Uuendamine on nii lihtne kui binaarsüsteemi asendamine ja teenuse taaskäivitamine.



## Võrdlus alternatiividega



### Phoenixd vs Phoenix standard



**Foenix standard (mobiilne) :**




- ✅ Kohene paigaldus, nullkonfiguratsioon
- ✅ Interface mobiilne intuitiivne
- ✅ Sama automaatne salvestamine nagu Phoenixd
- ❌ API puudub arendajatele
- ❌ Puudub juurdepääs üksikasjalikele logidele



**Phoenixd (server) :**




- ✅ HTTP API integratsioonide jaoks
- ✅ Täielik juurdepääs logidele
- ✅ Isiklik infrastruktuur
- ❌ Nõuab tehnilisi oskusi
- ❌ Vajalik serveri hooldus



**Kumbki kasutab automaatseks likviidsuseks ACINQ-d kui LSP-d.



### Phoenixd vs LND/Core Lightning



**LND/Core Lightning :**




- ✅ Täielik kontroll, täielik välkprotokoll
- ✅ Suur kogukond, küps ökosüsteem
- ❌ Keeruline likviidsuse käsitsi juhtimine
- ❌ Suur õppimiskõver



**Phoenixd :**




- ✅ Automaatne likviidsuse juhtimine (nagu Phoenix mobile)
- ✅ API arendajatele
- ✅ Lihtsustatud konfiguratsioon
- ❌ Kasutab ACINQ-d kui LSP-d (ei ole sõltumatut marsruutimist)
- ❌ Vähem paindlik kui täielikud sõlmed ❌ Vähem paindlik kui täielikud sõlmed



## Ühiste probleemide lahendamine



### API juurdepääsu probleemid



**Autentimine ebaõnnestus" viga:**


1. Kontrollida parooli failis `~/.phoenix/phoenix.conf`


2. Kontrolli autentimisformaat `-u:password`


3. Veenduge, et Phoenixd töötab (`./phoenix-CLI getinfo`)



**Võimaluste aegumine:**




- Kontrolli, et Phoenixd kuulab õiget porti (9740)
- Enne HTTPS-i konfigureerimist testige kohalikku juurdepääsu
- Kontrollige logisid: `journalctl -u phoenixd -f`



### Likviidsusprobleemid



**Maksed ei laeku :**


1. Kontrollida, et summa ületab miinimumkünnise (~30k Sats)


2. Kanalivigade tuvastamiseks konsulteeri logidega


3. Vajaduse korral taaskäivitage Phoenixd



**Saldo "kulukrediit":**


Väikesed maksed salvestatakse eraldisena. Saate suurema summa, et käivitada kanali avamine ja vabastada need vahendid.



## Kokkuvõte



Phoenixd on suurepärane kompromiss arendajate jaoks kasutusmugavuse ja tehnilise sõltumatuse vahel. See pakub lihtsat, kuid võimsat Lightning API-d koos automaatse likviidsuse juhtimisega, kõrvaldades traditsiooniliste Lightning-sõlmede keerukuse.



See lahendus sobib eriti hästi arendajatele ja ettevõtetele, kes soovivad :




- Integreerige Bitcoin Lightning oma rakendustesse
- Vältige välgukanali juhtimise keerukust
- Kasu iseteenindatavast infrastruktuurist
- Lihtne ja usaldusväärne API



Phoenixdiga ehitate omaenda erasektori Lightning-infrastruktuuri, millel on kaasaegne REST API ja tehniliste aspektide automaatne haldamine. See on ideaalne lahendus Lightningi integreerimise demokratiseerimiseks teie projektides.



## Kasulikud ressursid



### Ametlikud dokumendid




- GitHub Phoenixd** : [github.com/ACINQ/phoenixd](https://github.com/ACINQ/phoenixd) - lähtekood ja versioonid
- Phoenix Server** sait: [phoenix.acinq.co/server](https://phoenix.acinq.co/server) - Täielik dokumentatsioon
- KKK Phoenixd** : [phoenix.acinq.co/server/faq](https://phoenix.acinq.co/server/faq) - Korduma kippuvad küsimused



### Ühenduse toetus




- GitHubi probleemid** : [github.com/ACINQ/phoenixd/issues](https://github.com/ACINQ/phoenixd/issues) - Tehniline tugi
- Twitter ACINQ** : [@ACINQ_co](https://twitter.com/ACINQ_co) - Uudised ja teadaanded