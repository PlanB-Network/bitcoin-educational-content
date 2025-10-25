---
name: Phoenixd
description: Gushiraho urudodo rwawe rw'umuravyo rutoyi cane na Phoenixd
---

![cover](assets/cover.webp)



Ukwigenga mu vy’amahera bisigura kandi kugenzura ibikorwa remezo vyawe vya Lightning. Ku bahinga n’amashirahamwe yipfuza gushiramwo Bitcoin Lightning mu bikorwa vyabo, **Phoenixd** iserukira umuti mwiza: urudodo rw’umuravyo rutoyi, rwihariye rufise uburongozi bw’amahera bwikora.



Phoenixd ni server ya Lightning yateguwe na ACINQ, yagenewe canecane kohereza no kwakira amafaranga y’umuravyo biciye kuri HTTP API. Udakunze gushirwa mu ngiro kwuzuye nka LND canke Core Lightning, Phoenixd ikuramwo ibibazo vyose vy’uburongozi bw’imirongo mu gihe izigama ukwirinda kw’amahera yawe.



Muri iyi nyigisho, turaza kuraba ingene twoshiramwo, gutunganya no gukoresha Phoenixd kugira ngo dutegure porogarama za Lightning zifise ibikorwa remezo vy’ubwakiranyi n’ivyo gukoresha API yoroshe.



## None Fenikisi ni iki?



Phoenixd ni umurongo mutoyi, wihariye w’umuravyo wakozwe na ACINQ. Ni umuti wagenewe abahinguzi n'ibigo bipfuza kwinjiza Lightning mu bikorwa vyabo ata n'uburongozi bugoranye bwa Full node.



### Ingingo ngenderwako



**Phoenixd ni urudodo rutoyi rw’umuravyo rukoresha ACINQ nk’umurongo wa LSP (Umutanga Serivisi z’Umuravyo) kugira ngo rubone amahera yihuta. Iyo uronse amahera ya Lightning, ihita ifungura imirongo ifise ama node ya ACINQ kugira ngo itange ubushobozi bukenewe bwo kwinjira. Ivyo bihembo "on-the-fly" biraheza bikaja mu kanya nk'ako gukubita, ariko bifatwa ku giciro nyaco **1% + amafaranga Mining** y'amahera umuntu yaronse.



**Uburongozi bwikora:** Ubuhinga burongora urufunguzo rutatu Elements:




- Imirongo y'umuravyo**: Gufungura, gufunga no gucunga ubwavyo nk'uko bikenewe
- Amafaranga yinjira/asohoka**: Gutanga ubwavyo biciye mu gukoranya no gufungura umuyoboro
- Fee credit** : Amahera mato mato adahagije kugira ngo umuntu ashobore gushingira intahe umurongo abikwa nk'ingingo y'amahera azokwishurwa muri kazoza



### Inyungu za Phoenixd



**Ugenzura imfunguruzo zawe z’ibanga (amajambo 12 seed) n’amahera. Phoenixd itanga Wallet yawe mu karere ataco wigeze usangira imfunguruzo zawe.



**Ibikorwa remezo vy’umuntu ku giti ciwe:** Phoenixd ikora kuri server yawe, ikaguha uburenganzira bwo kuronka amakuru arambuye, imiterere n’ubugenzuzi bwa API. Ntugishingiye ku wundi muntu kugira ngo ubone amahera yawe.



**API yunze ubumwe:** Phoenixd ifise API ya HTTP yo gufatanya n'izindi serivisi, gufasha LNURL kavukire n'ugutegura porogarama zisanzwe.



**Ukworohereza gushiramwo:** Kubera REST API yayo yoroshe, Phoenixd ishobora kwinjira mu gikorwa cose canke mu gikorwa cose gisaba ko Lightning yishurwa.



**Iciyumviro gihambaye:** Amafaranga yihuta aracari muri ACINQ nk’uko LSP (Umutanga Serivisi y’Umuravyo). Phoenixd ikoresha uburyo bumwe na Phoenix mobile ku bijanye n’ugucungera imirongo yikora.



## Gushiramwo Phoenixd



### Ibisabwa



Phoenixd isaba ibidukikije vya Linux (Ubuntu/Debian birasabwa), n'ubuhinga bumwe bumwe bw'ishimikiro bwo gukoresha umurongo w'amabwirizwa. Kugira ngo ukore neza, uzokenera :





- Server ya Linux**: VPS canke imashini yo mu karere ifise ubufatanye buhamye
- GufunguraJDK 21** : Ibidukikije vy'igihe c'ibikorwa vya Java
- Ihuriro rya Internet rihamye**: Kugira ngo rihuzwe na Lightning Network.
- Izina ry'indangarubuga** (ubusabe) : Kugira ngo HTTPS igere kuri API



### Gukuraho no gushiramwo



**1. Gukuraho Phoenixd**



Genda kuri [ibisohoka vya GitHub] kuri paji (https://github.com/ACINQ/phoenixd/ibisohoka) maze ushiremwo verisiyo nshasha y'ubwubatsi bwawe:



```bash
# For Linux x86_64
# Replace with the latest release
wget https://github.com/ACINQ/phoenixd/releases/download/v0.6.1/phoenixd-0.6.1-linux-x64.zip
unzip -j phoenixd-0.6.1-linux-x64.zip
chmod +x phoenixd phoenix-cli
```



**2. Itanguriro rya mbere



Tangira Phoenixd kugira ngo utangure:



```bash
./phoenixd
```



Ku gutangura kwa mbere, uzosabwa kwemeza intambwe zibiri zihambaye wanditse "Ndatahura" :



**Ubutumwa bwa 1 - Gusubiza inyuma:**


```
This software is self-custodial, you have full control and responsibility over your funds.
Your 12-words seed is located in /home/<user>/.phoenix, make sure to do a backup or you risk losing your funds.
Do not share the same seed with other phoenix instances (mobile or server), it will cause issues and channel force closes.
```



**Bika aya majambo 12** - ni co kigufasha gukira.



**Ubutumwa bwa 2 - Uguhinduka kw'amahera:**


```
Continuous liquidity
Liquidity management is fully automated.
When receiving a Lightning payment that doesn't fit in your existing channel:
- If the payment amount is large enough to cover mining fees and service fees for automated liquidity,
then your channel will be created or enlarged right away.
- If the payment is too small, then the full amount is added to your fee credit,
and will be used later to pay for future fees. The fee credit is non-refundable.
```



Andika `Ndatahura` ku kwemeza kwose.



![Premier démarrage](assets/fr/01.webp)



*Phoenixd itanguye ku ncuro ya mbere: ivyemezo vy'ububiko n'amahera yihuta*



**3. Itunganywa ry'ibikorwa** (mu gifaransa gusa)



Kugira ngo ukomeze gukora, rema systemd :



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



*Serivisi ya Phoenixd irakora kandi irakora biciye kuri systemd na `ugutanga amahera` ku 2m sat*



## Gutunganya n'umutekano



### Dosiye y'imiterere



Phoenixd ihita irema `~/.phoenix/phoenix.conf` n'ibigenderwako vy'ingenzi:



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



**Ivyagezwe vy'ingenzi:**




- `ukwihindura`: Ubwinshi bw'imirongo yuguruye ubwayo (ivya kera: 2M Sats)
- http-ijambobanga`: Ijambobanga ry'umuyobozi wa API (Invoice kurema NO gutanga kwishura)
- http-ijambobanga-ribujijwe-kuronka`: Ijambobanga ribujijwe (Invoice kurema gusa)



### Ukwinjira mu mutekano na HTTPS



Ku mburabuzi, API ya Phoenixd ishobora gushikwako gusa biciye kuri HTTP yo mu karere (`http://127.0.0.1:9740`). Kugira ngo ukoreshe node yawe uvuye hanze (ibikoresho vy’amatelefone ngendanwa, izindi serveri, ubufatanye bw’urubuga), ukeneye gutunganya uburyo bwo gushika ku HTTPS butekanye.



**Ingingo ngenderwako y'uburenganzira bwo guhindura:**


```
Internet → nginx (port 443 HTTPS) → Phoenixd (port 9740 HTTP local)
```



**Nginx** ikora nk’**reverse proxy**: yumviriza ibisabwa vya HTTPS biva kuri Internet ku kivuko 443, ikabirungika kuri Phoenixd mu karere (icuma 9740), hanyuma ikarungika inyishu zifise amakuru apfutse ku mukiriya.



**Icemezo ca SSL/TLS** ni dosiye y'ubuhinga bwa none :




- Erekana akaranga ka server yawe** (ibuza ibitero vy'umuntu wo hagati)
- Bishoboza HTTPS** gupfuka: amakuru yose, harimwo n'amajambobanga yawe ya API, apfutse mu gihe co gutwara
- Isohowe ku buntu** na Let's Encrypt biciye ku gikoresho ca certbot



Iyi ntunganyo iraguha uburenganzira bwo :




- Ushobora gushika kuri API ukoresheje Internet**
- Gushiramwo amajambobanga yawe ya API** mu gihe co gutwara (kugira ngo ntamenyekane mu nyandiko itomoye)
- Kwinjiza Phoenixd** mu bikorwa vyo hanze bisaba HTTPS
- Kubahiriza ingingo ngenderwako z'umutekano** ku ma API y'ivy'amahera



Kugena iyi HTTPS ihindura proxy na nginx :



**1. Nginx** imiterere



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



**2. SSL** icemeza



```bash
sudo certbot --nginx -d phoenixd.your-domain.com
```



### Igerageza ry'imikorere



Suzuma ko Phoenixd ikora neza:



```bash
./phoenix-cli getinfo
./phoenix-cli getbalance
```



Aya mategeko akwiye kugarura amakuru ya JSON ku bijanye n'imimerere n'uburinganire bw'uruzitiro (mu ntango rwari ubusa).



![Commandes CLI](assets/fr/03.webp)



*Amabwirizwa ya Getinfo na getbalance kugira ngo usuzume uko urudodo rumeze*



## Gukoresha API



### Ikigeragezo ca mbere co kwakira



**1. Rema Umuravyo** Invoice



Koresha API kugira ngo ureme Invoice yawe yambere:



```bash
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='First test' \
-d amountSat=100000
```



### Gutahura uburyo bwo gutanga amahera



**Ingingo y'ishimikiro:** Iyo uronse amahera ya Lightning, rimwe na rimwe Phoenixd itegerezwa gufungura umurongo mushasha kugira ngo ishobore kuyaronka. Ukwo gufungura umurongo bitwara amahera **akurwako** ku mafaranga umuntu aronka.



**Akarorero nyako gafise Sats 100.000:**



![Premier test de réception](assets/fr/04.webp)



*Ikigeragezo ca mbere co kwemera: Sats 100k zaronswe, umusaruro wa nyuma wa Sats 75.561 inyuma yo gukuraho amafaranga y'amahera*



```bash
# Payment received: 100,000 sats
# Channel created: 2,115,000 sats total capacity
# Liquidity fee: 24,439 sats
# Final balance: 75,561 sats
```



**Ibara ry'amafaranga:**




- Igiciro c'ibikorwa**: 1% y'ubushobozi bw'umuyoboro (2.115.000 Sats) = 21.150 Sats
- Amafaranga y'ama Mining**: ~3.289 Sats (ku bijanye n'ugucuruza ama On-Chain)
- Igitigiri cose**: 24.439 Sats zica zikurwako



**Igenzura n'amabwirizwa ya CLI:**


```bash
# View details of all channels
./phoenix-cli listchannels

# Important output:
# "toLocal": 75561000 (your balance in milli-sats)
# "toRemote": 2039439000 (ACINQ's balance)
# Total channel: 2,115,000 sats
```



![Nouveau solde après paiement](assets/fr/05.webp)



*Igiciro ca nyuma gisigaye inyuma yo kwishura: 257 Sats zisigaye inyuma yo gutuma Lightning irungikwa*



**Inguzanyo y'amahera y'amahera make:** Iyo uronse amahera make cane ku buryo udashobora gufungura umurongo (< hafi 25k Sats), abikwa mu "nguzanyo y'amahera" idashobora gusubirwamwo. Iyi ngurane izokoreshwa mu kwishura amafaranga y’umurongo wo muri kazoza igihe uzoba uronse amahera ahagije.



**2. Kurikirana ugufungura umurongo**



Raba ibitabo vya Phoenixd:



```bash
journalctl -u phoenixd -f
```



Uzobona ugufungura umuyoboro n’ugukuraho amafaranga y’amahera. Amafaranga aratandukanye bivanye n’ivyo Mempool Bitcoin ivuga, ariko yama harimwo 1% y’amahera y’ibikorwa hamwe n’amahera ya Mining ariho ubu.



**3. Suzuma umurongo**



```bash
./phoenix-cli listchannels
```



Iri tegeko ryerekana imirongo yawe ikora n'aho iri n'uburinganire bwayo.



### Kuzuza ibikorwa vya API



Phoenixd yerekana REST API ku cambu 9740 ishoboza :



**Ibikorwa vy'ishimikiro:**


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



**Igihambaye kugiciro:**




- Inyishu**: 1% + amafaranga Mining y'amahera yihuta
- Ugutwara**: 0.4% y'amahera yo gutwara ku Lightning Network



**Webhooks:** Webhooks zituma Phoenixd **imenyesha ubwo nyene** ibisabwa vyawe iyo habaye ikintu (amahera yaronse, Invoice yishuwe, umurongo wafunguwe, n'ibindi). Aho kwama usaba Phoenixd ivyahinduwe, porogaramu yawe iraronka itangazo rya HTTP ry’aho nyene.



**Iduka ryawe ryo kuri internet rihita rironka itangazo iyo umukiriya yishuye ivyo yasavye, bikaba bituma ivyo yasavye bishobora kwemezwa ubwo nyene.



Itunganywa muri 'phoenix.conf` :


```conf
webhook-url=https://your-app.com/webhook-phoenixd
webhook-secret=votre_secret_de_verification
```



## Ibikoresho biteye imbere



### Ubufatanye bwa LNURL



Phoenixd ishigikira amasezerano ya LNURL ku bijanye n'ubufatanye buteye imbere:



**LNURL-Ishura:** Ishura ibikorwa bihuye na LNURL


```bash
curl -X POST http://localhost:9740/lnurlpay \
-u :your_password \
-d lnurl=LNURL1DP68GURN8GHJ7MRWW4EXCTN... \
-d amountSat=100
```



**LNURL-Withdraw :** Gukura amafranga mu bikorwa vya LNURL


```bash
curl -X POST http://localhost:9740/lnurlwithdraw \
-u :your_password \
-d lnurl=lightning:LNURL1DP68GURN8GHJ7MRW...
```



**LNURL-Auth:** Kwemeza biciye ku Muravyo kugira ngo ushikire ibikorwa


```bash
curl -X POST http://localhost:9740/lnurlauth \
-u :your_password \
-d lnurl=lnurl1dp68gurn8ghj7um5v93kket...
```



### Ukwinjizwa na LNbits



LNbits ishobora gukoresha Phoenixd nk’isoko y’amahera hakurikijwe [inyandiko zemewe] zayo(https://inyandiko.lnbits.org/uburongozi/amasakoshi.html):



**Imiterere y'ibice vya LN:**


```bash
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://localhost:9740/
PHOENIXD_API_PASSWORD=your_password_phoenixd
```



Ubu bufatanye buragufasha gukora amakonti mato mato ya LNbits akoreshwa n’uruzitiro rwawe rwa Phoenixd, utanga Interface ishingiye ku rubuga yo gucunga amasakoshi menshi ya Lightning.



### Ibikoresho vy'umuntu ku giti ciwe



Ushimiye REST API yayo, ushobora gutegura :



**Ubucuruzi bwo kuri interineti:** Gushiramwo amafaranga y'umuravyo mu iduka ryawe


**Ibikorwa vy'impano:** Uburyo bwo gutanga impanuro bufise amafagitire n'ibikoresho vy'urubuga vyikora


**Ivyuma vy'imigenderanire:** Ivyuma vy'amatelegaramu/Discord bifise ibikorwa vy'impanuro


**Paywall Lightning:** Ibirimwo vyiza cane biraboneka ku mafaranga y'umuravyo



## Umutekano n'ibikorwa vyiza



### Uburinzi bwo kuronka



**Amajambo y'ibanga ya API:** Amajambo y'ibanga yibonekeza ni yo mfunguruzo z'itunga ryawe rya Lightning. Ntukigere ubisangira, kandi ubihindure nimba ufise amakenga.



**Firewall:** Ntukigere usiga port 9740 yuguruye kuri Internet. Igihe cose ukoreshe nginx na HTTPS.



**Ivyemezo vy’ukuri:** Niwiyumvire VPN canke Tailscale kugira ngo uhagarike uburenganzira bwo gukoresha server yawe ku bikoresho vyemewe gusa.



### Ububiko bw'ingenzi



**seed recovery:** Bika amajambo yawe 12 ahantu hatagira umutekano, hanze ya server. Ivyo ni vyo vyonyene biguha icemezo co gukira.



*~/.phoenix directory:** Gusubiza inyuma iyi dosiye ubudasiba (inyuma y'aho Phoenixd ipfungiwe) kugira ngo uzigame ikibanza c'umurongo no kwihutisha gusubirana.



**Amakode yo gusubizaho ibikorwa:** Kandi ubike amakode y'ububiko y'ibikorwa vyose aho ukoresha 2FA na Phoenix yawe.



### Gukurikirana no gucungera



**Ivyanditswe vyo kugenzura:**


```bash
journalctl -u phoenixd -f  # Real-time logs
./phoenix-cli getinfo      # Node status
```



**Ivyashizwe ku rubuga:** Raba [ivyasohotse kuri GitHub](ivyo vyasohotse) kugira ngo ubone verisiyo nshasha. Guhindura ibintu bishasha biroroshe nk’ugusubirira binary no gusubira gutangura service.



## Kugereranya n'ubundi buryo



### Fenikisi n'itegeko rya Fenikisi



**Ikigereranyo ca Phoenix (igendagenda) :**




- ✅ Gushiramwo ubwo nyene, nta gutunganya
- ✅ Interface telefone ngendanwa
- ✅ Ivyo nyene bizigama ubwavyo nka Phoenixd
- ❌ Nta API y'abahinguzi
- ❌ Nta gushika ku bitabo vy'ido n'ido



**Fonikisi (umukozi) :**




- ✅ HTTP API y'ubufatanye
- ✅ Ushobora gushika ku bitabo vyose
- ✅ Ibikorwa remezo vy'umuntu ku giti ciwe
- ❌ Bisaba ubuhinga bw'ubuhinga
- ❌ Gucungera server birakenewe



**Bompi bakoresha ACINQ nka LSP yabo kugira ngo bashobore gutanga amahera.



### Phoenixd na LND/Umuravyo



**LND/Umuravyo w'Ishingiro :**




- ✅ Igenzura ryose, umurongo wuzuye w'umuravyo
- ✅ Umuryango munini, ibidukikije bikomeye
- ❌ Uburyo bugoye bwo gucunga amafaranga y'amaboko
- ❌ Inyigisho nini



**Fenikisi :**




- ✅ Ubuyobozi bw'amahera bwikora (nk'uko Phoenix igendagenda)
- ✅ API y'abahinguzi
- ✅ Gutunganya vyoroshe
- ❌ Ikoresha ACINQ nka LSP (nta nzira yigenga)
- ❌ Bidahinduka bike kuruta utugingo ngengabuzima twuzuye



## Gutorera umuti ibibazo rusangi



### Ingorane zo kuronka API



**Ivyemezo vyananiwe" ikosa:**


1. Suzuma ijambobanga riri muri dosiye `~/.phoenix/phoenix.conf`


2. Suzuma uburyo bwo kwemeza `-u:ijambobanga`


3. Raba neza ko Phoenixd iriko irakora (`./Phoenix-CLI kuronka amakuru`)



**Igihe co guhuza caraheze:**




- Suzuma ko Phoenixd iriko iratega yompi ku nzira ibereye (9740)
- Gerageza ukwinjira mu karere imbere yo gutunganya HTTPS
- Suzuma inyandiko: `ikinyamakuructl -u phoenixd -f`



### Ibibazo vy'amahera



**Ivyishurwa ntibishika :**


1. Suzuma ko amafaranga arenga urugero rwo hasi (~30k Sats)


2. Raba ibitabo kugira ngo umenye amakosa y'umurongo


3. Subiramwo Phoenixd nimba bikenewe



**Ibisigaye mu "nguzanyo y'amafaranga":**


Ivyishyurwa bitobito birabikwa nk’ivyo umuntu atanga. Kwakira amahera menshi kugira ngo uvyure ugufungura imihora maze urekure ayo mahera.



## Iciyumviro



Phoenixd igereranya ugusenyera ku mugozi umwe neza cane hagati y’ukworohereza gukoresha n’ubusegaba bw’ubuhinga ku bategura. Itanga API yoroshe ariko ikomeye ya Lightning n’uburongozi bw’amahera bwikora, ikuraho ubugoyagoye bw’ibihimba vya kera vy’umuravyo.



Uyu muti urabereye cane cane abahinguzi n'amashirahamwe yipfuza :




- Injiza Bitcoin Umuravyo mu bikorwa vyawe
- Irinde ubugoyagoye bw'uburongozi bw'umurongo w'umuravyo
- Inyungu z'ibikorwa remezo vy'ubwakiranyi
- API yoroshe kandi yizewe



Na Phoenixd, wubaka ibikorwa remezo vyawe vy’ibanga vy’umuravyo ufise REST API y’ubuhinga bwa none n’uburongozi bwikora bw’imice y’ubuhinga. Ni umuti mwiza wo gutuma demokarasi y’ugushiramwo Lightning mu migambi yawe.



## Ibikoresho vy'ingirakamaro



### Inyandiko zemewe




- - Kode y'inkomoko n'ibisohoka
- Urubuga rwa Phoenix Server**: [umukozi wa Phoenix) - Inyandiko zose
- Ibibazo bikunze kwibazwa Phoenixd** : [Ibibazo bikunze kwibazwa) - Ibibazo bikunze kubazwa



### Infashanyo y'abanyagihugu




- Ibibazo vya GitHub** : [ibibazo] (ibibazo) - Ubufasha mu vy'ubuhinga
- Twitter ACINQ** : [@ACINQ_co](https://twitter.com/ACINQ_co) - Amakuru n'amatangazo