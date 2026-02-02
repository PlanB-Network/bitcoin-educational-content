---
name: Phoenixd
description: Ota käyttöön oma minimalistinen Lightning-solmusi Phoenixd:n avulla
---

![cover](assets/cover.webp)



Taloudellinen riippumattomuus tarkoittaa myös Lightning-infrastruktuurin hallintaa. Kehittäjille ja yrityksille, jotka haluavat integroida Bitcoin Lightningin sovelluksiinsa, **Phoenixd** on ihanteellinen ratkaisu: minimalistinen, erikoistunut Lightning-solmu, jossa on automaattinen likviditeetinhallinta.



Phoenixd on ACINQ:n kehittämä Lightning-palvelin, joka on suunniteltu erityisesti Lightning-maksujen lähettämiseen ja vastaanottamiseen HTTP-API:n kautta. Toisin kuin LND:n tai Core Lightningin kaltaiset täysimittaiset toteutukset, Phoenixd abstrahoi kaiken kanavanhallinnan monimutkaisuuden säilyttäen samalla varojen itsesuojelun.



Tässä oppaassa tarkastelemme, miten Phoenixd asennetaan, konfiguroidaan ja käytetään Lightning-sovellusten kehittämiseen itse isännöidyn infrastruktuurin ja helppokäyttöisen API:n avulla.



## Mikä on Phoenixd?



Phoenixd on ACINQ:n kehittämä minimaalinen, erikoistunut Lightning-solmu. Se on ratkaisu, joka on suunniteltu kehittäjille ja yrityksille, jotka haluavat integroida Lightningin sovelluksiinsa ilman Full node:n hallinnoinnin monimutkaisuutta.



### Toimintaperiaate



**Phoenixd on minimaalinen Lightning-solmu, joka käyttää ACINQ:ta LSP:nä (Lightning Service Provider) automaattiseen likviditeettiin. Kun vastaanotat Lightning-maksuja, se avaa automaattisesti kanavia ACINQ-solmujen kanssa tarvittavan saapuvan kapasiteetin jakamiseksi. Tämä "lennossa oleva" likviditeetti on välitöntä, mutta siitä veloitetaan tasan **1 % + Mining-maksut** vastaanotetusta summasta.



**Automaattinen hallinta:** Järjestelmä hallinnoi kolmea keskeistä Elements:




- Salama**-kanavat: Avaa, sulje ja hallitse automaattisesti tarpeen mukaan
- Saapuva/lähtevä likviditeetti**: Automaattinen tarjoaminen liittämisen ja kanavien avaamisen avulla
- Maksuhyvitys** : Pienet maksut, jotka eivät riitä oikeuttamaan kanavaa, tallennetaan varaukseksi tulevia maksuja varten



### Phoenixd-edut



**Hallitset yksityiset avaimesi (12-sanainen seed) ja varasi. Phoenixd luo Wallet:n paikallisesti jakamatta avaimiasi.



**Henkilökohtainen infrastruktuuri:** Phoenixd toimii palvelimellasi, jolloin saat käyttöösi yksityiskohtaiset lokit, konfiguraation ja API:n hallinnan. Et ole enää riippuvainen kolmannen osapuolen palvelusta, kun pääset käsiksi varoihisi.



**Integroitu API:** Phoenixd:ssä on HTTP-API, joka mahdollistaa integroinnin muihin palveluihin, natiivin LNURL-tuen ja mukautetun sovelluskehityksen.



**Helppo integroitavuus:** Yksinkertaisen REST API:nsa ansiosta Phoenixd voidaan integroida mihin tahansa sovellukseen tai palveluun, joka vaatii Lightning-maksuja.



**Tärkeä huomautus:** Automaattinen likviditeetti tulee edelleen ACINQ:lta LSP:nä (Lightning Service Provider). Phoenixd käyttää automaattiseen kanavanhallintaan samaa mekanismia kuin Phoenix mobile.



## Phoenixd:n asentaminen



### Edellytykset



Phoenixd vaatii Linux-ympäristön (Ubuntu/Debian suositeltava) ja joitakin peruskomentorivitaitoja. Optimaalisen suorituskyvyn saavuttamiseksi tarvitset :





- Linux-palvelin**: VPS tai paikallinen kone, jossa on vakaa yhteys
- OpenJDK 21** : Java-ajoympäristö
- Vakaa Internet-yhteys**: Synkronointia varten Lightning Network:n kanssa
- Verkkotunnus** (valinnainen) : API:n suojattua HTTPS-yhteyttä varten



### Lataa ja asenna



**1. Lataa Phoenixd**



Siirry [GitHub releases] -sivulle (https://github.com/ACINQ/phoenixd/releases) ja lataa uusin versio arkkitehtuurillesi:



```bash
# For Linux x86_64
# Replace with the latest release
wget https://github.com/ACINQ/phoenixd/releases/download/v0.6.1/phoenixd-0.6.1-linux-x64.zip
unzip -j phoenixd-0.6.1-linux-x64.zip
chmod +x phoenixd phoenix-cli
```



**2. Ensimmäinen käynnistys



Käynnistä Phoenixd alustusta varten:



```bash
./phoenixd
```



Ensimmäisellä käynnistyskerralla sinua pyydetään vahvistamaan kaksi tärkeää vaihetta kirjoittamalla "I understand" :



**Viesti 1 - Varmuuskopiointi:**


```
This software is self-custodial, you have full control and responsibility over your funds.
Your 12-words seed is located in /home/<user>/.phoenix, make sure to do a backup or you risk losing your funds.
Do not share the same seed with other phoenix instances (mobile or server), it will cause issues and channel force closes.
```



**Säilytä nämä 12 sanaa** - se on ainoa tae toipumisesta.



**Viesti 2 - Automaattinen maksuvalmius:**


```
Continuous liquidity
Liquidity management is fully automated.
When receiving a Lightning payment that doesn't fit in your existing channel:
- If the payment amount is large enough to cover mining fees and service fees for automated liquidity,
then your channel will be created or enlarged right away.
- If the payment is too small, then the full amount is added to your fee credit,
and will be used later to pay for future fees. The fee credit is non-refundable.
```



Kirjoita `I understand` jokaisen vahvistuksen kohdalla.



![Premier démarrage](assets/fr/01.webp)



*Phoenixd käynnistyy ensimmäistä kertaa: varmuuskopiointivahvistukset ja automaattinen likviditeetti*



**3. Käytössä oleva kokoonpano** (vain ranskaksi)



Jatkuvaa toimintaa varten luo systemd :



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



*Phoenixd-palvelu aktiivinen ja toiminnassa systemd:n ja "automaattisen likviditeetin" kautta 2m sat*:ssa



## Konfigurointi ja turvallisuus



### Konfiguraatiotiedosto



Phoenixd luo automaattisesti tiedoston `~/.phoenix/phoenix.conf`, jossa on keskeiset parametrit:



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



**Keskeiset parametrit:**




- "automaattinen maksuvalmius": Automaattisesti avattujen kanavien koko (oletus: 2M Sats)
- http-password`: Admin-salasana API:lle (Invoice luominen JA maksujen lähettäminen)
- http-password-limited-access`: Rajoitettu salasana (vain Invoice:n luomisessa)



### Turvallinen pääsy HTTPS:n avulla



Oletusarvoisesti Phoenixd API on käytettävissä vain paikallisen HTTP:n kautta (`http://127.0.0.1:9740`). Jos haluat käyttää solmua ulkopuolelta (mobiilisovellukset, muut palvelimet, web-integraatiot), sinun on määritettävä suojattu HTTPS-yhteys.



**Käänteinen proxy-periaate:**


```
Internet → nginx (port 443 HTTPS) → Phoenixd (port 9740 HTTP local)
```



**Nginx** toimii **käännettynä välityspalvelimena**: se kuuntelee HTTPS-pyyntöjä Internetistä portista 443, ohjaa ne paikallisesti Phoenixd:hen (portti 9740) ja lähettää sitten salatut vastaukset takaisin asiakkaalle.



**S SSL/TLS**-varmenne on digitaalinen tiedosto, joka :




- Todistaa palvelimen henkilöllisyyden** (estää välikäsien välityksellä tapahtuvat hyökkäykset)
- Ottaa käyttöön HTTPS**-salauksen: kaikki tiedot, myös API-salasanat, salataan siirron aikana
- Let's Encrypt myöntää maksutta** certbot-työkalun kautta



Tämän kokoonpanon avulla voit :




- Turvallinen pääsy API:han Internetistä**
- Salaa API**-salasanasi kuljetuksen aikana (jotta ne eivät välity selvänä tekstinä)
- Integroi Phoenixd** ulkoisiin sovelluksiin, jotka vaativat HTTPS:ää
- Rahoitusalan sovellusliittymien turvallisuusstandardien** noudattaminen



Määritä tämä HTTPS-käänteinen välityspalvelin nginxin kanssa :



**1. Nginx**-konfiguraatio



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



**2. SSL**-sertifikaatti



```bash
sudo certbot --nginx -d phoenixd.your-domain.com
```



### Toimintatesti



Tarkista, että Phoenixd toimii oikein:



```bash
./phoenix-cli getinfo
./phoenix-cli getbalance
```



Näiden komentojen pitäisi palauttaa JSON-tiedot solmun tilasta ja saldosta (aluksi tyhjä).



![Commandes CLI](assets/fr/03.webp)



*Getinfo ja getbalance-komennot solmun tilan tarkistamiseksi*



## API:n käyttäminen



### Ensimmäinen vastaanottotesti



**1. Luo salama** Invoice



Luo ensimmäinen Invoice API:n avulla:



```bash
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='First test' \
-d amountSat=100000
```



### Automaattisen likviditeettimekanismin ymmärtäminen



**Perusperiaate:** Kun saat Lightning-maksun, Phoenixd joutuu joskus avaamaan uuden kanavan voidakseen vastaanottaa sen. Tämä kanavan avaaminen maksaa maksun, joka **automaattisesti vähennetään** vastaanotetusta summasta.



**Konkreettinen esimerkki 100 000 Sats:**



![Premier test de réception](assets/fr/04.webp)



*Ensimmäinen hyväksymistesti: Sats 100k vastaanotettu, Sats:n lopullinen saldo 75.561 likviditeettikustannusten vähentämisen jälkeen*



```bash
# Payment received: 100,000 sats
# Channel created: 2,115,000 sats total capacity
# Liquidity fee: 24,439 sats
# Final balance: 75,561 sats
```



**Palkkion laskeminen:**




- Palvelumaksu**: 1 % kanavan kapasiteetista (2,115,000 Sats) = 21,150 Sats
- Mining-maksut**: ~3,289 Sats (On-Chain-tapahtuman osalta)
- Yhteensä**: 24,439 Sats automaattisesti vähennetty



**Varmennus CLI-komennoilla:**


```bash
# View details of all channels
./phoenix-cli listchannels

# Important output:
# "toLocal": 75561000 (your balance in milli-sats)
# "toRemote": 2039439000 (ACINQ's balance)
# Total channel: 2,115,000 sats
```



![Nouveau solde après paiement](assets/fr/05.webp)



*Loppusaldo maksun lähettämisen jälkeen: 257 Sats jäljellä Lightning-lähetyksen jälkeen*



**Pienten maksujen maksuhyvitys:** Jos saat maksuja, jotka ovat liian pieniä kanavan avaamiseen (< n. 25k Sats), ne tallennetaan "maksuhyvitykseen", jota ei voi palauttaa. Tätä luottoa käytetään tulevien kanavamaksujen maksamiseen, kun saat riittävän määrän.



**2. Seuraa kanavan avautumista**



Tarkkaile Phoenixdin lokitietoja:



```bash
journalctl -u phoenixd -f
```



Näet kanavan avautumisen ja likviditeettimaksujen automaattisen vähentämisen. Maksut vaihtelevat Mempool Bitcoin-ehtojen mukaan, mutta ne sisältävät aina 1 prosentin palvelumaksun sekä voimassa olevan Mining-maksun.



**3. Tarkista kanava**



```bash
./phoenix-cli listchannels
```



Tämä komento näyttää aktiiviset kanavasi sekä niiden tilan ja saldon.



### Täydelliset API-toiminnot



Phoenixd tarjoaa REST API:n portissa 9740, joka mahdollistaa :



**Basistoiminnot:**


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



**Kustannusten kannalta tärkeää:**




- Kuitti**: 1% + Mining maksu automaattisesta likviditeetistä
- Toimitus**: 0.4% reititysmaksu Lightning Network:lle



**Webhooks:** Webhooksin avulla Phoenixd voi **automaattisesti ilmoittaa** sovelluksillesi, kun jokin tapahtuma tapahtuu (maksu vastaanotettu, Invoice maksettu, kanava avattu jne.). Sen sijaan, että pyytäisit Phoenixd:ltä jatkuvasti päivityksiä, sovelluksesi saa välittömän HTTP-ilmoituksen.



**Verkkokauppasi saa automaattisesti ilmoituksen, kun asiakas maksaa tilauksen, mikä mahdollistaa tapahtuman välittömän validoinnin.



Konfigurointi tiedostossa `phoenix.conf` :


```conf
webhook-url=https://your-app.com/webhook-phoenixd
webhook-secret=votre_secret_de_verification
```



## Edistyneet sovellukset



### LNURL-integraatiot



Phoenixd tukee natiivisti LNURL-protokollia kehittynyttä integrointia varten:



**LNURL-Pay:** Maksa LNURL-yhteensopivista palveluista


```bash
curl -X POST http://localhost:9740/lnurlpay \
-u :your_password \
-d lnurl=LNURL1DP68GURN8GHJ7MRWW4EXCTN... \
-d amountSat=100
```



**LNURL-Withdraw :** Varojen haku LNURL-palveluista


```bash
curl -X POST http://localhost:9740/lnurlwithdraw \
-u :your_password \
-d lnurl=lightning:LNURL1DP68GURN8GHJ7MRW...
```



**LNURL-Auth:** Tunnistautuminen Lightningin kautta palveluiden käyttämiseksi


```bash
curl -X POST http://localhost:9740/lnurlauth \
-u :your_password \
-d lnurl=lnurl1dp68gurn8ghj7um5v93kket...
```



### Integrointi LNbitsin kanssa



LNbits voi käyttää Phoenixd:tä rahoituslähteenä [virallisen dokumentaation](https://docs.lnbits.org/guide/wallets.html) mukaan:



**LNbits-konfiguraatio:**


```bash
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://localhost:9740/
PHOENIXD_API_PASSWORD=your_password_phoenixd
```



Tämän integraation avulla voit luoda LNbits-alitilejä, jotka toimivat Phoenixd-solmun kautta, ja tarjota verkkopohjaisen Interface:n useiden Lightning-lompakoiden hallintaan.



### Mukautetut sovellukset



Sen kattavan REST API:n ansiosta voit kehittää :



**E-commerce:** Lightning-maksujen suora integrointi myymälääsi


**Lahjoituspalvelut:** Lahjoitusjärjestelmät laskuineen ja automaattisine verkkokoukkuineen


**Sosiaalisen verkostoitumisen botit:** Telegram/Discord-botit, joissa on vinkkitoimintoja


**Paywall Lightning:** Premium-sisältö saatavilla Lightning-maksua vastaan



## Turvallisuus ja parhaat käytännöt



### Pääsysuojaus



**API-salasanat:** Automaattisesti luodut salasanat ovat avaimet Lightning-varastoosi. Älä koskaan jaa niitä, ja vaihda ne, jos olet epävarma.



**Palomuuri:** Älä koskaan jätä porttia 9740 auki suoraan Internetiin. Käytä aina nginxiä HTTPS:n kanssa.



**Vahvistettu todennus:** Harkitse VPN:ää tai Tailscalea rajoittaaksesi pääsyn palvelimelle vain valtuutetuille laitteille.



### Olennaiset varmuuskopiot



**seed palautus:** Tallenna 12 sanaa turvalliseen paikkaan, pois palvelimelta. Tämä on ainoa takuu palautumisesta.



*~/.phoenix-hakemisto:** Varmuuskopioi tämä kansio säännöllisesti (Phoenixd:n sammuttamisen jälkeen) kanavan tilan säilyttämiseksi ja palauttamisen nopeuttamiseksi.



**Palveluiden palautuskoodit:** Säilytä myös varmuuskopiokoodit kaikista palveluista, joissa aktivoit 2FA:n Phoenixin avulla.



### Seuranta ja ylläpito



**Valvontalokit:**


```bash
journalctl -u phoenixd -f  # Real-time logs
./phoenix-cli getinfo      # Node status
```



**Päivitykset:** Tarkkaile [GitHub releases](https://github.com/ACINQ/phoenixd/releases) uusia versioita varten. Päivittäminen on yhtä yksinkertaista kuin binäärin vaihtaminen ja palvelun uudelleenkäynnistäminen.



## Vertailu vaihtoehtoihin



### Phoenixd vs Phoenix standard



**Phoenix-standardi (mobiili) :**




- ✅ Välitön asennus, ei lainkaan konfigurointia
- ✅ Interface mobiili intuitiivinen
- ✅ Sama automaattinen tallennus kuin Phoenixd:ssä
- ❌ Ei API:ta kehittäjille
- ❌ Ei pääsyä yksityiskohtaisiin lokitietoihin



**Phoenixd (palvelin) :**




- ✅ HTTP API integraatioita varten
- ✅ Täysi pääsy lokitietoihin
- ✅ Henkilökohtainen infrastruktuuri
- ❌ Vaatii teknisiä taitoja
- ❌ Palvelimen ylläpito vaaditaan



**Kumpikin käyttää ACINQ:ta automaattisen likviditeetin LSP:nä.



### Phoenixd vs LND/Core Lightning



**LND/Core Lightning :**




- ✅ Täydellinen valvonta, täysi salamaprotokolla
- ✅ Suuri yhteisö, kypsä ekosysteemi
- ❌ Monimutkainen manuaalinen likviditeetin hallinta
- ❌ Suuri oppimiskäyrä



**Phoenixd :**




- ✅ Automaattinen likviditeetin hallinta (kuten Phoenix mobile)
- ✅ API kehittäjille
- ✅ Yksinkertaistettu kokoonpano
- ❌ Käyttää ACINQ:ta LSP:nä (ei itsenäistä reititystä)
- ❌ Vähemmän joustava kuin täydelliset solmut



## Yleisten ongelmien ratkaiseminen



### API-käytön ongelmat



**Authentication failed" virhe:**


1. Tarkista salasana tiedostosta `~/.phoenix/phoenix.conf`


2. Tarkista todennusmuoto `-u:salasana`


3. Varmista, että Phoenixd on käynnissä (`./phoenix-CLI getinfo`)



**Yhteyden aikakatkaisut:**




- Tarkista, että Phoenixd kuuntelee oikeaa porttia (9740)
- Testaa paikallinen pääsy ennen HTTPS:n määrittämistä
- Tarkista lokit: `journalctl -u phoenixd -f`



### Maksuvalmiusongelmat



**Maksuja ei ole saapunut :**


1. Tarkista, että määrä ylittää vähimmäismäärän (~30k Sats)


2. Tutustu lokitietoihin kanavavirheiden tunnistamiseksi


3. Käynnistä Phoenixd tarvittaessa uudelleen



**Kuluhyvityksen saldo:**


Pienet maksut tallennetaan varauksena. Suuremman summan vastaanottaminen käynnistää kanavan avaamisen ja vapauttaa nämä varat.



## Päätelmä



Phoenixd on erinomainen kompromissi helppokäyttöisyyden ja kehittäjien teknisen riippumattomuuden välillä. Se tarjoaa yksinkertaisen mutta tehokkaan Lightning API:n, jossa on automaattinen likviditeetinhallinta ja joka poistaa perinteisten Lightning-solmujen monimutkaisuuden.



Tämä ratkaisu sopii erityisen hyvin kehittäjille ja yrityksille, jotka haluavat :




- Integroi Bitcoin Lightning sovelluksiisi
- Vältä Lightning-kanavien hallinnan monimutkaisuus
- Hyödy itse isännöidystä infrastruktuurista
- Yksinkertainen, luotettava API



Phoenixd:n avulla voit rakentaa oman yksityisen Lightning-infrastruktuurin, jossa on moderni REST API ja automaattinen teknisten näkökohtien hallinta. Se on ihanteellinen ratkaisu Lightning-integraation demokratisointiin projekteissasi.



## Hyödyllisiä resursseja



### Viralliset asiakirjat




- GitHub Phoenixd** : [github.com/ACINQ/phoenixd](https://github.com/ACINQ/phoenixd) - Lähdekoodi ja julkaisut
- Phoenix Server**-sivusto: [phoenix.acinq.co/server](https://phoenix.acinq.co/server) - Täydellinen dokumentaatio
- FAQ Phoenixd** : [phoenix.acinq.co/server/faq](https://phoenix.acinq.co/server/faq) - Usein kysytyt kysymykset



### Yhteisön tuki




- GitHub Issues** : [github.com/ACINQ/phoenixd/issues](https://github.com/ACINQ/phoenixd/issues) - Tekninen tuki
- Twitter ACINQ** : [@ACINQ_co](https://twitter.com/ACINQ_co) - Uutiset ja ilmoitukset