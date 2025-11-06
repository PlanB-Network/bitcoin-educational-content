---
name: Phoenixd
description: Tumia nodi yako ndogo ya Umeme na Phoenixd
---

![cover](assets/cover.webp)



Uhuru wa kifedha pia unamaanisha kudhibiti miundombinu yako ya Umeme. Kwa wasanidi programu na makampuni wanaotaka kujumuisha Umeme wa Bitcoin katika programu zao, **Phoenixd** inawakilisha suluhu bora: Nuru ya Umeme iliyobobea na yenye udhibiti wa moja kwa moja wa ukwasi.



Phoenixd ni seva ya Umeme iliyotengenezwa na ACINQ, iliyoundwa mahususi kwa ajili ya kutuma na kupokea malipo ya Umeme kupitia API ya HTTP. Tofauti na utekelezwaji kamili kama vile LND au Core Lightning, Phoenixd huondoa utata wote wa usimamizi wa kituo huku ikihifadhi ulinzi wa pesa zako.



Katika somo hili, tutaangalia jinsi ya kusakinisha, kusanidi na kutumia Phoenixd kutengeneza programu za Umeme na miundombinu inayojiendesha yenyewe na API iliyo rahisi kutumia.



## Phoenixd ni nini?



Phoenixd ni nodi ndogo, maalum ya Umeme iliyotengenezwa na ACINQ. Ni suluhisho iliyoundwa kwa ajili ya wasanidi programu na biashara zinazotaka kujumuisha Umeme katika programu zao bila utata wa usimamizi wa Full node.



### Kanuni ya uendeshaji



**Phoenixd ni sehemu ndogo ya Umeme inayotumia ACINQ kama LSP (Mtoa Huduma ya Umeme) kwa ukwasi kiotomatiki. Unapopokea malipo ya Radi, hufungua kiotomatiki chaneli zenye nodi za ACINQ ili kutenga uwezo unaohitajika unaoingia. Ukwasi huu wa "on-the-fly" ni wa papo hapo, lakini unatozwa kwa **1% + ada ya Mining** ya kiasi kilichopokelewa.



**Udhibiti wa kiotomatiki:** Mfumo unadhibiti vitu vitatu muhimu vya Elements:




- Vituo vya Umeme**: Fungua, funga na udhibiti kiotomatiki inavyohitajika
- Ukwasi unaoingia/unaotoka**: Utoaji kiotomatiki kupitia kuunganisha na kufungua chaneli
- Salio la ada** : Malipo madogo yasiyotosha kuhalalisha kituo huhifadhiwa kama kipengele cha malipo ya siku zijazo



### Faida za Phoenixd



**Unadhibiti funguo zako za faragha (maneno 12 seed) na fedha. Phoenixd hutengeneza Wallet yako ndani ya nchi bila kushiriki funguo zako.



**Miundombinu ya kibinafsi:** Phoenixd hutumika kwenye seva yako, kukupa ufikiaji wa kumbukumbu za kina, usanidi na udhibiti wa API. Hutegemei tena huduma ya watu wengine kupata pesa zako.



**API Iliyounganishwa:** Phoenixd ina API ya HTTP ili kuunganishwa na huduma zingine, usaidizi asilia wa LNURL na usanidi wa programu maalum.



**Urahisi wa kuunganishwa:** Shukrani kwa API yake rahisi ya REST, Phoenixd inaweza kuunganishwa kwenye programu au huduma yoyote inayohitaji malipo ya Umeme.



**Dokezo muhimu:** Malipo ya kiotomatiki bado yanatoka kwa ACINQ kama LSP (Mtoa Huduma ya Umeme). Phoenixd hutumia utaratibu sawa na Phoenix mobile kwa ajili ya usimamizi wa kituo kiotomatiki.



## Inasakinisha Phoenixd



### Masharti



Phoenixd inahitaji mazingira ya Linux (Ubuntu/Debian inapendekezwa), yenye ujuzi wa msingi wa mstari wa amri. Kwa utendaji bora, utahitaji:





- Seva ya Linux**: VPS au mashine ya ndani yenye muunganisho thabiti
- OpenJDK 21** : Mazingira ya wakati wa utekelezaji wa Java
- Muunganisho thabiti wa Mtandao**: Kwa ulandanishi na Lightning Network
- Jina la kikoa** (si lazima) : Kwa ufikiaji salama wa HTTPS kwa API



### Pakua na usakinishe



**1. Pakua Phoenixd**



Nenda kwenye ukurasa wa [GitHub releases] (https://github.com/ACINQ/phoenixd/releases) na upakue toleo jipya zaidi la usanifu wako:



```bash
# For Linux x86_64
# Replace with the latest release
wget https://github.com/ACINQ/phoenixd/releases/download/v0.6.1/phoenixd-0.6.1-linux-x64.zip
unzip -j phoenixd-0.6.1-linux-x64.zip
chmod +x phoenixd phoenix-cli
```



**2. Uzinduzi wa kwanza



Anzisha Phoenixd kwa kuanzishwa:



```bash
./phoenixd
```



Katika uzinduzi wa kwanza, utaombwa kuthibitisha hatua mbili muhimu kwa kuandika "Ninaelewa" :



**Ujumbe 1 - Hifadhi Nakala:**


```
This software is self-custodial, you have full control and responsibility over your funds.
Your 12-words seed is located in /home/<user>/.phoenix, make sure to do a backup or you risk losing your funds.
Do not share the same seed with other phoenix instances (mobile or server), it will cause issues and channel force closes.
```



**Hifadhi maneno haya 12** - ni dhamana yako pekee ya kupona.



**Ujumbe wa 2 - Ukwasi wa kiotomatiki:**


```
Continuous liquidity
Liquidity management is fully automated.
When receiving a Lightning payment that doesn't fit in your existing channel:
- If the payment amount is large enough to cover mining fees and service fees for automated liquidity,
then your channel will be created or enlarged right away.
- If the payment is too small, then the full amount is added to your fee credit,
and will be used later to pay for future fees. The fee credit is non-refundable.
```



Andika `Ninaelewa` kwa kila uthibitishaji.



![Premier démarrage](assets/fr/01.webp)



*Phoenixd inaanza kwa mara ya kwanza: uthibitisho wa chelezo na ukwasi kiotomatiki*



**3. Usanidi wa ndani ya huduma** (kwa Kifaransa pekee)



Kwa operesheni inayoendelea, tengeneza systemd :



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



*Huduma ya Phoenixd inatumika na inafanya kazi kupitia systemd na `auto-liquidity` saa 2m sat*



## Usanidi na usalama



### Faili ya usanidi



Phoenixd huunda `~/.phoenix/phoenix.conf` kiotomatiki kwa kutumia vigezo muhimu:



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



**Vigezo muhimu:**




- `uwezo wa otomatiki`: Ukubwa wa chaneli zinazofunguliwa kiotomatiki (chaguo-msingi: 2M Sats)
- http-nenosiri`: Nenosiri la msimamizi la API (uundaji wa Invoice NA utumaji malipo)
- http-password-limited-access`: Nenosiri lenye vikwazo (uundaji wa Invoice pekee)



### Salama ufikiaji ukitumia HTTPS



Kwa chaguo-msingi, API ya Phoenixd inapatikana tu kupitia HTTP ya ndani (`http://127.0.0.1:9740`). Ili kutumia nodi yako kutoka nje (programu za rununu, seva zingine, miunganisho ya wavuti), unahitaji kusanidi ufikiaji salama wa HTTPS.



**Kanuni ya ubadilishaji wa wakala:**


```
Internet → nginx (port 443 HTTPS) → Phoenixd (port 9740 HTTP local)
```



**Nginx** hufanya kazi kama **seva mbadala**: inasikiliza maombi ya HTTPS kutoka kwa Mtandao kwenye mlango wa 443, inawaelekeza kwenye Phoenixd ndani ya nchi (bandari 9740), kisha kutuma majibu yaliyosimbwa kwa njia fiche kwa mteja.



**Cheti cha SSL/TLS** ni faili ya dijitali ambayo :




- Thibitisha utambulisho wa seva yako** (huzuia mashambulizi ya mtu katikati)
- Huwasha usimbaji fiche wa HTTPS**: data zote, pamoja na manenosiri yako ya API, husimbwa kwa njia fiche wakati wa usafirishaji.
- Imetolewa bila malipo** na Let's Encrypt kupitia zana ya certbot



Mpangilio huu hukuruhusu:




- Ufikiaji salama wa API kutoka kwa Mtandao**
- Simba nenosiri lako la API** wakati wa usafiri (ili kuzuia kutumwa kwa maandishi wazi)
- Unganisha Phoenixd** katika programu za nje zinazohitaji HTTPS
- Kuzingatia viwango vya usalama** vya API za kifedha



Sanidi seva mbadala hii ya HTTPS ya kurudi nyuma na nginx :



**1. Usanidi wa Nginx**



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



**2. Cheti cha SSL**



```bash
sudo certbot --nginx -d phoenixd.your-domain.com
```



### Mtihani wa kazi



Angalia kuwa Phoenixd inafanya kazi vizuri:



```bash
./phoenix-cli getinfo
./phoenix-cli getbalance
```



Amri hizi zinapaswa kurudisha maelezo ya JSON juu ya hali ya nodi na salio (mwanzoni tupu).



![Commandes CLI](assets/fr/03.webp)



* Getinfo na getbalance amri kuangalia hali ya nodi *



## Kwa kutumia API



### Mtihani wa mapokezi ya kwanza



**1. Unda Umeme** Invoice



Tumia API kuunda Invoice yako ya kwanza:



```bash
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='First test' \
-d amountSat=100000
```



### Kuelewa utaratibu wa ukwasi otomatiki



**Kanuni ya msingi:** Unapopokea malipo ya Radi, wakati fulani Phoenixd inalazimika kufungua kituo kipya ili kuweza kuyapokea. Ufunguzi huu wa kituo hugharimu ada ambayo **hukatwa kiotomatiki** kutoka kwa kiasi kilichopokelewa.



**Mfano wa zege na 100,000 Sats:**



![Premier test de réception](assets/fr/04.webp)



*Jaribio la kwanza la kukubalika: Sats 100k imepokelewa, salio la mwisho la Sats 75.561 baada ya kukatwa kwa gharama za ukwasi*



```bash
# Payment received: 100,000 sats
# Channel created: 2,115,000 sats total capacity
# Liquidity fee: 24,439 sats
# Final balance: 75,561 sats
```



** Hesabu ya ada:**




- Ada ya huduma**: 1% ya uwezo wa chaneli (2,115,000 Sats) = 21,150 Sats
- Ada za Mining**: ~3,289 Sats (kwa muamala wa On-Chain)
- Jumla**: 24,439 Sats imekatwa kiotomatiki



**Uthibitishaji kwa amri za CLI:**


```bash
# View details of all channels
./phoenix-cli listchannels

# Important output:
# "toLocal": 75561000 (your balance in milli-sats)
# "toRemote": 2039439000 (ACINQ's balance)
# Total channel: 2,115,000 sats
```



![Nouveau solde après paiement](assets/fr/05.webp)



*Salio la mwisho baada ya malipo kutumwa: 257 Sats iliyobaki baada ya usafirishaji wa umeme*



**Salio la ada kwa malipo madogo:** Ukipokea malipo madogo mno kuweza kuhalalisha kufungua kituo (< takriban. 25k Sats), yanahifadhiwa katika "mkopo wa ada" usioweza kurejeshwa. Salio hili litatumika kulipa ada za kituo siku zijazo utakapopokea kiasi cha kutosha.



**2. Fuata ufunguzi wa kituo**



Tazama kumbukumbu za Phoenixd:



```bash
journalctl -u phoenixd -f
```



Utaona kufunguliwa kwa chaneli na kukatwa kiotomatiki kwa ada za ukwasi. Ada hutofautiana kulingana na masharti ya Mempool Bitcoin, lakini kila mara hujumuisha 1% ya malipo ya huduma pamoja na ada ya sasa ya Mining.



**3. Angalia kituo**



```bash
./phoenix-cli listchannels
```



Amri hii huonyesha chaneli zako zinazotumika pamoja na hali na salio lake.



### Kamilisha shughuli za API



Phoenixd inafichua API ya REST kwenye bandari 9740 inayowezesha :



**Shughuli za kimsingi:**


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



**Muhimu kwa gharama:**




- Risiti**: 1% + ada ya Mining kwa ukwasi otomatiki
- Usafirishaji**: Ada ya 0.4% ya uelekezaji kwenye Lightning Network



**Webhooks:** Webhooks huwezesha Phoenixd **kuarifu** maombi yako kiotomatiki tukio linapotokea (malipo yamepokelewa, Invoice kulipwa, kituo kufunguliwa, n.k.). Badala ya kuuliza Phoenixd masasisho kila mara, programu yako hupokea arifa ya HTTP papo hapo.



**Duka lako la mtandaoni hupokea arifa kiotomatiki mteja anapolipia agizo, kuwezesha uthibitishaji wa papo hapo wa muamala.



Usanidi katika `phoenix.conf` :


```conf
webhook-url=https://your-app.com/webhook-phoenixd
webhook-secret=votre_secret_de_verification
```



## Maombi ya hali ya juu



### Miunganisho ya LNURL



Phoenixd asilia inasaidia itifaki za LNURL kwa ujumuishaji wa hali ya juu:



**LNURL-Lipa:** Lipia huduma zinazooana na LNURL


```bash
curl -X POST http://localhost:9740/lnurlpay \
-u :your_password \
-d lnurl=LNURL1DP68GURN8GHJ7MRWW4EXCTN... \
-d amountSat=100
```



**LNURL-Withdraw :** Pata pesa kutoka kwa huduma za LNURL


```bash
curl -X POST http://localhost:9740/lnurlwithdraw \
-u :your_password \
-d lnurl=lightning:LNURL1DP68GURN8GHJ7MRW...
```



**LNURL-Auth:** Uthibitishaji kupitia Umeme ili kupata huduma


```bash
curl -X POST http://localhost:9740/lnurlauth \
-u :your_password \
-d lnurl=lnurl1dp68gurn8ghj7um5v93kket...
```



### Kuunganishwa na LNbits



LNbits inaweza kutumia Phoenixd kama chanzo cha ufadhili kulingana na [hati rasmi](https://docs.lnbits.org/guide/wallets.html):



**Usanidi wa LNbits:**


```bash
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://localhost:9740/
PHOENIXD_API_PASSWORD=your_password_phoenixd
```



Ujumuishaji huu hukuruhusu kuunda akaunti ndogo za LNbits zinazoendeshwa na nodi yako ya Phoenixd, ikitoa Interface inayotegemea wavuti kwa ajili ya kudhibiti pochi nyingi za Radi.



### Maombi maalum



Shukrani kwa API yake ya kina ya REST, unaweza kukuza:



**Biashara ya kielektroniki:** Ujumuishaji wa moja kwa moja wa malipo ya Umeme kwenye duka lako


**Huduma za uchangiaji:** Mifumo ya uchangiaji iliyo na ankara na vihifadhi otomatiki vya wavuti


**Vijibu vya roboti za mitandao jamii:** Telegram/Discord robots na vipengele vya vidokezo


**Umeme wa Paywall:** Maudhui ya kulipiwa yanapatikana kwa ada ya Umeme



## Usalama na mazoea bora



### Ulinzi wa ufikiaji



**Nenosiri za API:** Nywila zinazozalishwa kiotomatiki ndizo funguo za hazina yako ya Umeme. Usiwahi kuzishiriki, na zibadilishe ikiwa una shaka.



**Firewall:** Usiwahi kuondoka bandari 9740 wazi moja kwa moja kwenye Mtandao. Tumia nginx na HTTPS kila wakati.



**Uthibitishaji ulioimarishwa:** Zingatia VPN au Tailscale ili kudhibiti ufikiaji wa seva yako kwa vifaa vilivyoidhinishwa pekee.



### Backups muhimu



**seed ahueni:** Hifadhi maneno yako 12 mahali salama, nje ya seva. Hii ndiyo dhamana yako pekee ya kupona.



*~/.phoenix saraka:** Hifadhi nakala ya folda hii mara kwa mara (baada ya Phoenixd kuzimwa) ili kuhifadhi hali ya kituo na kuharakisha urejeshaji.



**Nambari za kurejesha huduma:** Pia weka misimbo mbadala kwa huduma zote ambapo unawasha 2FA ukitumia Phoenix yako.



### Ufuatiliaji na matengenezo



**Kumbukumbu za ufuatiliaji:**


```bash
journalctl -u phoenixd -f  # Real-time logs
./phoenix-cli getinfo      # Node status
```



**Sasisho:** Tazama [matoleo ya GitHub](https://github.com/ACINQ/phoenixd/releases) kwa matoleo mapya. Kusasisha ni rahisi kama kuchukua nafasi ya binary na kuanzisha upya huduma.



## Kulinganisha na njia mbadala



### Kiwango cha Phoenixd dhidi ya Phoenix



**Kiwango cha Phoenix (simu ya rununu) :**




- ✅ Ufungaji wa mara moja, usanidi wa sifuri
- ✅ Interface angavu ya rununu
- ✅ Hifadhi kiotomatiki sawa na Phoenixd
- ❌ Hakuna API ya wasanidi programu
- ❌ Hakuna ufikiaji wa kumbukumbu za kina



**Phoenixd (seva) :**




- ✅ HTTP API ya miunganisho
- ✅ Ufikiaji kamili wa kumbukumbu
- ✅ Miundombinu ya kibinafsi
- ❌ Inahitaji ujuzi wa kiufundi
- ❌ Matengenezo ya seva yanahitajika



**Wote wawili hutumia ACINQ kama LSP yao kwa ukwasi otomatiki.



### Phoenixd dhidi ya LND/Umeme wa Msingi



**LND/Umeme wa Msingi :**




- ✅ Udhibiti wa jumla, itifaki kamili ya Umeme
- ✅ Jamii kubwa, mfumo wa ikolojia uliokomaa
- ❌ Udhibiti tata wa ukwasi wa mikono
- ❌ Mkondo mkubwa wa kujifunza



**Phoenixd :**




- ✅ Usimamizi wa ukwasi otomatiki (kama simu ya Phoenix)
- ✅ API kwa watengenezaji
- ✅ Usanidi uliorahisishwa
- ❌ Hutumia ACINQ kama LSP (hakuna uelekezaji huru)
- ❌ Inayonyumbulika kidogo kuliko vifundo kamili



## Kutatua matatizo ya kawaida



### Matatizo ya ufikiaji wa API



**Uthibitishaji umeshindwa" hitilafu:**


1. Angalia nenosiri katika faili `~/.phoenix/phoenix.conf`


2. Angalia umbizo la uthibitishaji `-u:nenosiri`


3. Hakikisha Phoenixd inafanya kazi (`./phoenix-CLI getinfo`)



**Muda wa muunganisho umekwisha:**




- Angalia kuwa Phoenixd inasikiliza kwenye bandari sahihi (9740)
- Jaribu ufikiaji wa ndani kabla ya kusanidi HTTPS
- Angalia kumbukumbu: `journalctl -u phoenixd -f`



### Matatizo ya ukwasi



**Malipo hayajafika:**


1. Hakikisha kuwa kiasi kinazidi kiwango cha chini zaidi (~30k Sats)


2. Angalia kumbukumbu ili kutambua hitilafu za kituo


3. Anzisha tena Phoenixd ikiwa ni lazima



**Salio katika "mikopo ya gharama":**


Malipo madogo huhifadhiwa kama utoaji. Pokea kiasi kikubwa ili kuanzisha kituo na kutoa pesa hizi.



## Hitimisho



Phoenixd inawakilisha maelewano bora kati ya urahisi wa kutumia na uhuru wa kiufundi kwa wasanidi programu. Inatoa API rahisi lakini yenye nguvu ya Umeme yenye usimamizi wa ukwasi kiotomatiki, ikiondoa utata wa nodi za jadi za Umeme.



Suluhisho hili linafaa haswa kwa watengenezaji na kampuni zinazotaka:




- Unganisha Umeme wa Bitcoin kwenye programu zako
- Epuka utata wa usimamizi wa kituo cha Umeme
- Faidika na miundombinu inayojitegemea
- API rahisi na ya kuaminika



Ukiwa na Phoenixd, unaunda miundombinu yako ya kibinafsi ya Umeme kwa API ya kisasa ya REST na usimamizi wa kiotomatiki wa vipengele vya kiufundi. Ndilo suluhu bora la kuleta demokrasia ujumuishaji wa Umeme katika miradi yako.



## Rasilimali muhimu



### Nyaraka rasmi




- GitHub Phoenixd** : [github.com/ACINQ/phoenixd](https://github.com/ACINQ/phoenixd) - Msimbo wa chanzo na matoleo
- Tovuti ya Seva ya Phoenix**: [phoenix.acinq.co/server](https://phoenix.acinq.co/server) - Hati kamili
- Maswali Yanayoulizwa Mara kwa Mara** : [phoenix.acinq.co/server/faq](https://phoenix.acinq.co/server/faq) - Maswali yanayoulizwa sana



### Usaidizi wa jumuiya




- Masuala ya GitHub** : [github.com/ACINQ/phoenixd/issues](https://github.com/ACINQ/phoenixd/issues) - Usaidizi wa kiufundi
- Twitter ACINQ** : [@ACINQ_co](https://twitter.com/ACINQ_co) - Habari na matangazo