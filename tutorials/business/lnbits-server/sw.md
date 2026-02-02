---
name: LNbits Server
description: Ufungaji na usanidi wa seva ya LNbits inayojiendesha yenyewe kwenye Ubuntu VPS na Phoenixd au kwenye Umbrel.
---

![cover](assets/cover.webp)



LNbits ni kiolesura cha tovuti huria kinachobadilisha mandharinyuma yoyote ya Lightning (kama LND, Core Lightning, au Phoenixd) kuwa jukwaa kamili la huduma. Suluhisho hili la kujipangia mwenyewe hukuwezesha kudhibiti wallet nyingi za Lightning kwa kujitegemea, kusambaza sehemu za mauzo, kuunda mifumo ya michango au huduma za utozaji, huku ukiendelea kuhifadhi udhibiti kamili wa pesa zako.



Mafunzo haya yanashughulikia mbinu mbili za usakinishaji: **VPS Ubuntu iliyo na Phoenixd** (suluhisho jepesi bila  Full Node ya Bitcoin) na **Umbrel** (muunganisho na node yako iliyopo ya LND). Tofauti na mafunzo ya jumla ya LNbits ya Chuo cha Plan ₿, ambayo yanashughulikia dhana na viendelezi, mwongozo huu unaangazia taratibu za kiufundi za hatua kwa hatua za usakinishaji.



## LNbits ni nini?



LNbits ni mfumo wa uhasibu wa Lightning uliotengenezwa katika Python (FastAPI) unaounganishwa na mazingira ya nyuma yaliyopo (LND, Core Lightning, Phoenixd). Tofauti na node za jadi za Lightning, LNbits hutoa kiolesura kinachoweza kufikiwa kwa ajili ya kudhibiti portfolios kadhaa zilizotengwa na funguo zao za API. Unaweza kuunda akaunti ndogo za familia yako, wafanyikazi au miradi, bila kuwapa ufikiaji wa pesa zako zote.



Usanifu uliotenganishwa huhifadhi maelezo katika SQLite (chaguo-msingi) au PostgreSQL (uzalishaji), huku pesa zikisalia kusimamiwa na mazingira yako ya nyuma ya Lightning. Utengano huu unahakikisha kubebeka: unaweza kuhama kutoka Phoenixd hadi LND bila kupoteza data yako ya mtumiaji.



## Vipengele muhimu



LNbits inatoa **mfumo wa upanuzi** unaoweza kutumika tofauti: TPoS (maeneo ya kuuza), Paywall (uchumaji wa maudhui), Matukio (tiketi), LndHub (server ya BlueWallet), Kadi za Bolt (malipo ya NFC), Malipo ya Gawanya (usambazaji otomatiki), na Kidhibiti cha Mtumiaji (udhibiti wa mtumiaji na uthibitishaji).



**dashibodi** huonyesha salio la wakati halisi, historia ya miamala na zana za kulipa. Kila wallet ina URL ya kipekee iliyo na funguo zake za API, kuruhusu ufikiaji bila kuingia kwa kawaida. Mfumo wa ufunguo wa ngazi tatu wa APIUmbrel (msimamizi, ankara, kusoma tu) hutoa udhibiti wa punjepunje wa ruhusa kwa miunganisho salama.



LNbits hutekeleza **LNURL** (LNURL-pay, LNURL-withdraw, LNURL-auth) na inaauni **Lightning Address**, kuhakikisha utangamano na pochi za kisasa za Radi na kuwezesha utumaji wa huduma za kitaalamu.



## Mifumo inayotumika



**Ubuntu VPS**: Suluhisho nyepesi bila  Full Node ya Bitcoin. Masharti: 1 vCPU, RAM ya GB 1-2, Ubuntu 22.04 LTS, Python 3.10+, Git, UV. HTTPS + jina la kikoa linahitajika kwa kufichuliwa kwa umma (huduma za LNURL).



**Umbrel**: Usakinishaji kwa urahisi kutoka kwa Duka la Programu. Sharti: node ya Umbrel inayofanya kazi na LND iliyosawazishwa na chaneli wazi. Usanidi otomatiki.



Hapo chini kuna viungo vya mafunzo yetu ya Umbrel na Umbrel LND:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Ufungaji kwenye Ubuntu VPS na Phoenixd



### Hatua ya 1: Kulinda server ya VPS



**Kabla ya usakinishaji wowote**, unahitaji kulinda server yako ya Ubuntu VPS kulingana na sheria za sanaa. Hatua hii ni **muhimu** ili kulinda miundombinu yako na fedha zako za Lightning.



Huu hapa ni mwongozo wa kina wa kukusaidia kuanza: **[Usanidi wa awali wa server ya Ubuntu - Mwongozo wa hatua kwa hatua](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/)** na Daniel P. Costas.



Mwongozo huu unashughulikia usanidi wa mtumiaji, SSH salama, firewall (UFW), fail2ban, masasisho ya kiotomatiki, na mbinu bora za usalama wa mfumo.



### Hatua ya 2: Kusakinisha Phoenixd



Mara server yako ikiwa salama, unahitaji kusakinisha na kusanidi Phoenixd. Plan ₿ Academy inatoa usakinishaji wa kina wa kufunika mafunzo, kizazi cha seed na usanidi wa huduma ya mfumo :



https://planb.academy/tutorials/node/lightning-network/phoenixd-beb86edd-f9c0-4bec-ad36-db234c88e7b1

Mara tu Phoenixd inapoanza kufanya kazi (angalia na `./phoenix-cli getinfo`), andika neno siri la HTTP** katika `~/.phoenix/phoenix.conf` - utahitaji ili kuunganisha LNbits kwenye Phoenixd.



### Usambazaji wa LNbits



Sakinisha UV na clone LNbits :


```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
git clone https://github.com/lnbits/lnbits.git && cd lnbits
uv sync --all-extras
```



Sanidi mandharinyuma ya Phoenixd:


```bash
cp .env.example .env && nano .env
```



Ongeza kwa `.env` :


```
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://127.0.0.1:9740
PHOENIXD_API_PASSWORD=<mot-de-passe-phoenix.conf>
```



Jaribu kwa `uv run lnbits --host 0.0.0.0 --port 5000` kisha uunde huduma ya mfumo kwa `Wants=phoenixd.service`.



## Usanidi wa awali na matumizi ya kwanza



### Uanzishaji wa SuperUser



Washa kiolesura cha msimamizi katika `.env` :


```
LNBITS_ADMIN_UI=true
```



Anzisha tena LNbits (`sudo systemctl anzisha tena lnbits`) na urejeshe Kitambulisho cha SuperUser:


```bash
cat ~/lnbits/data/.super_user
```



Nenda kwa `http://<IP-VPS>:5000/wallet?usr=<SuperUserID>` kwa paneli ya usimamizi. Menyu ya "server" inakuwezesha kusanidi vyanzo vya ufadhili, viendelezi na akaunti za mtumiaji.



### Salama uundaji wa akaunti



**Muhimu kwa kufichuliwa kwa umma**: Ikiwa unaonyesha mfano wako wa LNbits kwenye jina la kikoa cha umma linaloweza kufikiwa kutoka kwa Mtandao, ni **muhimu** kuzima uundaji wa akaunti za watumiaji bila malipo.



Kutoka kwa kiolesura cha usimamizi wa SuperUser, nenda kwa "Mipangilio" na kisha kwenye sehemu ya "Usimamizi wa Mtumiaji". Huko utapata chaguo "Ruhusu uundaji wa watumiaji wapya".



![Gestion des utilisateurs - Sécurité](assets/fr/17.webp)



**Kwa maonyesho ya umma yenye jina la kikoa** :




- Lazima uzime chaguo la "Ruhusu uundaji wa watumiaji wapya".
- Bila ulinzi huu, mtu yeyote kwenye Mtandao anaweza kufungua akaunti kwa mfano wako
- Mshambulizi anaweza kuunda akaunti na kutumia ukwasi wa node yako ya Lightning bila wewe kujua
- Utahitaji kuunda akaunti za mtumiaji mwenyewe kutoka kwa kiolesura cha SuperUser



**Kwa matumizi ya ndani pekee** :




- Chaguo hili sio muhimu sana ikiwa mfano wako unapatikana ndani ya nchi pekee (http://localhost:5000)
- Walakini, kuzima chaguo hili ni mazoezi mazuri ya usalama wa jumla



Baada ya kusanidiwa, msimamizi wa SuperUser pekee ndiye anayeweza kuunda akaunti mpya za watumiaji kupitia kiolesura cha "Watumiaji". Mbinu hii inahakikisha udhibiti kamili juu ya nani anaweza kufikia miundombinu yako ya Lightning na kutumia pesa zako.



### Kufungua kituo cha kwanza



Phoenixd inadhibiti chaneli kiotomatiki kupitia uwazi kiotomatiki. Tengeneza lightning invoice  ya ~30,000 sats kutoka LNbits na ulipe kutoka kwa wallet nyingine. Phoenixd hufungua kituo kiotomatiki kwa ACINQ. Ada ya ufunguzi (~ 20-23k sats) inatolewa, salio iliyobaki (~ 7-10k sats) inaonekana baada ya uthibitisho wa on-chain.



Angalia hali na `./phoenix-cli getinfo`. Kisha zingatia kuzima uwazi wa kiotomatiki (`auto-liquidity=off` katika `phoenix.conf`) ili kudhibiti fursa za vituo.



### Onyesho la umma na HTTPS



**Muhimu**: HTTPS lazima ionekane hadharani (ufunguo wa usalama wa API + uoanifu wa LNURL). Ruka hatua hii kwa matumizi ya ndani pekee.



**Caddy (inapendekezwa)**: SSL automatic. `sudo apt install -y caddy`, hariri `/etc/caddy/Caddyfile` :


```
votre-domaine.com {
reverse_proxy 127.0.0.1:5000
}
```


Anzisha tena: `sudo systemctl anzisha tena caddy`.



**Nginx** : Udhibiti zaidi. Sakinisha `nginx certbot python3-certbot-nginx`, unda `/etc/nginx/sites-available/lnbits` :


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


Washa: `sudo ln -s /etc/nginx/sites-available/lnbits /etc/nginx/sites-enabled/ && sudo nginx -t && sudo systemctl pakia tena nginx && sudo certbot --nginx -d your-domain.com`



Ongeza kwa `.env`: `FORWARDED_ALLOW_IPS=*`



## Ufungaji wa Umbrel



### Usambazaji kutoka Hifadhi ya Programu



Nenda kwenye Duka la Programu ya Umbrel, tafuta "LNbits", na ubofye "Sakinisha".



![Installation LNbits Umbrel](assets/fr/01.webp)



Umbrel hukagua kiotomatiki vitegemezi vinavyohitajika. LNbits inahitaji Lightning node (LND) kufanya kazi. Ikiwa node yako ya Lightning tayari inafanya kazi, bofya kwenye "Sakinisha LNbits" ili kuthibitisha.



![Dépendances LNbits](assets/fr/02.webp)



Umbrel hupakua picha ya Docker, husanidi miunganisho kiotomatiki na LND, na kuwasha chombo (dakika 2-5). Ufungaji unafanyika kabisa nyuma.



### Usanidi wa awali wa SuperUser



Wakati wa uzinduzi wa kwanza, LNbits hukuhimiza kuunda akaunti ya msimamizi wa SuperUser. Ingiza jina la mtumiaji na nenosiri salama ili kulinda ufikiaji wa kiolesura cha utawala.



![Configuration SuperUser](assets/fr/03.webp)



**Muhimu**: Akaunti hii ya SuperUser ina haki kamili kwenye mfano wako wa LNbits. Chagua nenosiri dhabiti na uliweke salama.



Mara baada ya kuunda akaunti, unachukuliwa kiotomatiki kwenye kiolesura kikuu cha utawala. Umbrel tayari imeanzisha LND kama chanzo chako cha ufadhili - malipo yote ya Lightning yatapitia chaneli zako zilizopo.



### Ufikiaji wa kiolesura cha msimamizi



Katika menyu ya upande wa kushoto, bofya "Mipangilio" ili kufikia paneli kamili ya usimamizi.



![Interface Settings](assets/fr/04.webp)



Sehemu ya "Usimamizi wa Pochi" huonyesha taarifa muhimu kuhusu usanidi wako:




- Chanzo cha Ufadhili** : LndBtcRestWallet (muunganisho wa moja kwa moja kwenye node yako ya Umbrel ya LND)
- Salio la node** : Jumla ya ukwasi unaopatikana katika chaneli zako za Lightning
- Salio la LNbits**: Fedha zilizotengwa kwa mfumo wa LNbits (mwanzoni 0 sats)



Sasa unaweza kutumia moja kwa moja ukwasi wa node yako ya Umbrel kwa pochi zote za LNbits unazounda. Hakuna usanidi wa ziada unaohitajika - LNbits iko na inafanya kazi.



### Usimamizi wa mtumiaji



Moja ya vipengele vya nguvu zaidi vya LNbits ni uwezo wake wa kuunda watumiaji wengi huru, kila moja ikiwa na uthibitishaji wa nenosiri na pochi zilizotengwa. Usanifu huu hufanya iwezekane kuchukua fursa ya ukwasi wa node yako ya Umbrel huku ukitoa akaunti ndogo zilizotengwa kwa matumizi tofauti: biashara, familia, wafanyikazi, miradi, n.k.



Katika menyu ya kando, bofya "Watumiaji" ili kufikia usimamizi wa mtumiaji. Bofya kwenye "CREATE ACCOUNT" ili kuongeza mtumiaji mpya.



![Gestion des utilisateurs](assets/fr/05.webp)



Jaza fomu ya kuunda mtumiaji:




- Jina la mtumiaji**: Ingia jina la mtumiaji (mfano: "satoshi")
- Weka Nenosiri**: Amilisha chaguo hili ili kuweka nenosiri la uthibitishaji
- Nenosiri** na **Nenosiri kurudia**: Weka nenosiri la mtumiaji huyu



![Création utilisateur satoshi](assets/fr/06.webp)



Sehemu za hiari (Ufunguo wa Umma wa Nostr, Barua pepe, Jina la Kwanza, Jina la Mwisho) zinaweza kuachwa wazi kwa usanidi mdogo. Bofya kwenye "CREATE ACCOUNT" ili kuthibitisha.



![Confirmation utilisateur créé](assets/fr/07.webp)



Mtumiaji wako mpya sasa anaonekana katika orodha ya watumiaji na kitambulisho chake cha kipekee na jina la mtumiaji.



![Liste des utilisateurs](assets/fr/08.webp)



**Hoja muhimu**: Kila mtumiaji anaweza kuingia kwa kujitegemea kabisa na nenosiri lake mwenyewe. Msimamizi wa SuperUser huhifadhi udhibiti kamili kupitia kiolesura cha utawala.



### Mtumiaji wallet usimamizi



Sasa kwa kuwa mtumiaji wa "satoshi" ameundwa, unahitaji kumpa Lightning wallet. Bofya kwenye ikoni ya wallet (ikoni ya pili) kwa mtumiaji husika, kisha kwenye "UNDA WALLET MPYA".



![Gestion des wallets](assets/fr/09.webp)



Kisanduku cha mazungumzo kinakuhimiza kutaja wallet. Weka jina la maelezo (k.m. "Wallet Of Satoshi") na uchague sarafu ya kuonyesha (CUC, USD, EUR, n.k.).



![Création wallet](assets/fr/10.webp)

wa

Bonyeza "CREATE". LNbits hutengeneza Lightning  wallet papo hapo kwa mtumiaji huyu.



![Confirmation wallet créé](assets/fr/11.webp)



Sasa unaona pochi mbili zilizopo: chaguo-msingi wallet "LNbits wallet" iliyoundwa moja kwa moja, na mpya "Wallet Ya Satoshi". Ili kurahisisha matumizi ya mtumiaji, unaweza kufuta chaguomsingi la wallet kwa kubofya aikoni ya kufuta (tupio nyekundu).



![Wallet final unique](assets/fr/12.webp)



Mtumiaji wa "satoshi" sasa ana wallet moja, iliyotambuliwa wazi. Kila mtumiaji wa wallet anafanya kazi kwa uhuru huku akitumia ukwasi wa node yako ya msingi ya LND.



**Dhana kuu**: Pochi hizi zote hushiriki ukwasi wa kimataifa wa node yako ya Umbrel. Hutengenezi chaneli mpya za Radi kwa kila wallet - LNbits hufanya kazi kama safu mahiri ya uhasibu ambayo inadhibiti ugawaji wa fedha ndani ya miundombinu yako iliyopo ya Lightning. Hiyo ndiyo nguvu ya mfumo wa wallet wa LNbits.



### Kuingia kwa mtumiaji



Toka kwenye akaunti ya SuperUser (ikoni iliyo juu kulia) na urudi kwenye ukurasa wa kuingia wa LNbits. Sasa unaweza kuingia kwa kutumia kitambulisho cha mtumiaji mpya.



![Connexion utilisateur satoshi](assets/fr/13.webp)



Ingiza jina la mtumiaji ("satoshi") na nenosiri lililoelezwa hapo awali, kisha ubofye "INGIA". Mtumiaji anapata ufikiaji wa moja kwa moja kwa wallet yake ya kibinafsi, iliyotengwa kabisa na kiolesura cha utawala.



### Interface kutoka kwa mtumiaji wa wallet



Mara baada ya kuingia, mtumiaji hufikia kiolesura chake kamili cha Lightning wallet.



![Interface wallet utilisateur](assets/fr/14.webp)



Vipengele vya interface:




- **Salio la sasa**: Imeonyeshwa katika sats na katika sarafu iliyochaguliwa (CUC katika mfano huu)
- **Vitendo vikuu**: BANDIKIA OMBI, UNDA ankara, ikoni ya QR (changanuzi haraka)
- **Historia ya muamala** : Kamilisha orodha ya malipo na risiti zote
- **Paneli ya upande wa kulia**: Chaguo za usanidi na ufikiaji



### Ufikiaji wa rununu kwa wallet



Paneli ya upande wa kulia inatoa kipengele cha vitendo hasa: ufikiaji wa simu kwa wallet. Fungua sehemu ya "Ufikiaji wa Simu" ili kugundua chaguo zinazopatikana.



![Mobile Access](assets/fr/15.webp)



LNbits inatoa njia kadhaa za kutumia wallet hii kwenye simu mahiri:



**Chaguo la 1: Programu zinazooana za simu




- Pakua **Zeus** au **BlueWallet** kutoka kwa App Store au Google Play
- Washa kiendelezi cha **LndHub** katika LNbits kwa wallet hii
- Changanua msimbo wa QR wa LndHub ukitumia programu ya simu ili kuunganisha wallet



**Chaguo la 2: Ufikiaji wa moja kwa moja kupitia kivinjari cha rununu**




- Msimbo wa QR unaoonyeshwa katika "Hamisha kwa Simu ukitumia Msimbo wa QR" una URL kamili ya wallet yenye uthibitishaji jumuishi.
- Changanua msimbo huu wa QR kutoka kwa simu yako mahiri ili kufungua wallet moja kwa moja kwenye kivinjari chako cha rununu
- Ongeza ukurasa kwenye skrini ya kwanza kwa ufikiaji wa haraka



**Usalama muhimu**: URL hii ina funguo za API kwa ufikiaji kamili wa wallet. Usiwahi kuishiriki hadharani. Tumia msimbo huu wa QR jinsi ungefanya funguo zako za faragha za Bitcoin - mtu yeyote anayechanganua msimbo huu wa QR anapata ufikiaji kamili wa wallet.



Kipengele hiki cha rununu hubadilisha mfano wako wa Umbrel wa LNbits kuwa server halisi ya Lightning wallet kwa ajili yako na marafiki zako, huku ukihifadhi mamlaka kamili juu ya fedha zako kupitia node yako inayojitegemea.



### Kushiriki ufikiaji wa mtumiaji



Kesi kuu ya matumizi ya usanidi huu wa watumiaji wengi ni kushiriki pochi na familia yako au mduara wa karibu. Mara tu unapounda mtumiaji mwenye wallet maalum (kama "satoshi" katika mfano wetu), unaweza kushiriki vitambulisho vya kuingia na wanafamilia wako unaowaamini.



**Usalama wa ufikiaji kwenye Umbrel**: Ufikiaji wa mfano wako wa LNbits kwenye Umbrel unalindwa kwa kawaida, kwani unaweza kufikiwa tu :




- **Kwenye mtandao wa ndani** : Wanafamilia wako waliounganishwa kwenye mtandao sawa wa WiFi/Ethernet wanaweza kufikia mfano huo
- **Kupitia VPN**: Ikiwa unatumia VPN kama vile Tailscale iliyosanidiwa kwenye server yako ya Umbrel, watumiaji walioidhinishwa wanaweza kupata ufikiaji salama wa mbali.



Safu hii mbili ya ulinzi (ufikiaji wa mtandao + uthibitishaji wa mtumiaji) hufanya chaguo la "Ruhusu uundaji wa watumiaji wapya" kuwa muhimu sana kwenye Umbrel. Watu ambao tayari wana ufikiaji wa mtandao wako au VPN wanaweza kufikia kiolesura cha kuingia.



**Hali ya kawaida**: Unafungua akaunti ya "baba", akaunti ya "mama", akaunti ya "biashara" na kadhalika. Kila mwanafamilia ana Lightning yake ya pekee wa yallet, huku akinufaika na ukwasi ulioshirikiwa wa node yako ya Umbrel. Shiriki kwa urahisi jina la mtumiaji na nenosiri - mtumiaji anaweza kisha kuunganisha kutoka kwa kifaa chochote kwenye mtandao wako wa karibu au kupitia Tailscale VPN yako. Tafadhali tazama mafunzo yetu yaliyojitolea ya Tailscale kwa habari zaidi:



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Chunguza viendelezi vinavyopatikana



Rudi kwenye kiolesura cha SuperUser na ufikie menyu ya "Viendelezi" katika paneli ya upande wa kushoto ili kugundua mfumo kamili wa kiendelezi wa LNbits.



![Extensions disponibles](assets/fr/16.webp)



LNbits inatoa katalogi nono ya viendelezi vinavyobadilisha mfano wako kuwa jukwaa la huduma za Lightning halisi:





- **Jukebox**: Mfumo wa jukebox unaoendeshwa na sats (malipo ya Spotify)
- **Tiketi za Usaidizi**: Mfumo wa usaidizi unaolipishwa (pokea satss kujibu maswali)
- **TPoS**: Salama, kituo cha mauzo cha simu kwa wauzaji reja reja
- **Kidhibiti cha Mtumiaji**: mtumiaji wa hali ya juu na usimamizi wa wallet (ambao tumetumia hivi punde)
-**Matukio**: Uuzaji na uthibitishaji wa tikiti za hafla
- **LNURLDevices**: Usimamizi wa sehemu ya mauzo, ATM, swichi zilizounganishwa
- **SMTP**: Wezesha watumiaji kutuma barua pepe na kupata sats
- **Boltcards**: Kupanga kadi za NFC kwa malipo ya Lightning ya bomba-ili-kulipa
- **NostrNip5**: Unda anwani za NIP5 za vikoa vyako
- **Malipo ya kugawanyika**: Usambazaji wa malipo kiotomatiki kati ya pochi nyingi



Kila kiendelezi kinaamilishwa kwa mbofyo mmoja kutoka kwenye kiolesura hiki. Viendelezi vilivyowekewa alama ya "BURE" havilipishwi, wakati vingine vinapatikana kama matoleo "YANAYOLIPIWA". Kagua katalogi ili kubaini zile zinazokidhi mahitaji yako—iwe kwa biashara, usimamizi wa familia, au kufanya majaribio na uwezo wa Lightning Network.



## Faida na mapungufu



**Manufaa**: Mamlaka ya kifedha (jumla ya udhibiti wa fedha/funguo/data), kubadilika kwa usanifu (uhamiaji usio na hasara wa VPS→full node), mfumo wa upanuzi wa kitaalamu, kiolesura angavu.



**Mapungufu** : Programu katika beta (tahadhari juu ya kiasi), usalama chini ya wajibu wa msimamizi, URL zilizo na funguo nyeti za API (lazima ya HTTPS), usimamizi wa watumiaji wengi unamaanisha jukumu la ulezi.



## Mbinu bora



**Hifadhi rudufu**: Vitambulisho vya Phoenixd Seed/LND, hifadhidata ya LNbits, faili za .env. Weka otomatiki kila siku, weka mbali na server ya uzalishaji, iliyosimbwa. Mtihani hurejesha mara kwa mara.



**Matengenezo**: Angalia mara kwa mara masasisho (LNbits, nyuma ya Lightning, mfumo wa uendeshaji). Angalia vidokezo vya toleo kila wakati kabla ya sasisho kuu.





- **Kwenye Umbrel**: Duka la Programu hukuarifu kiotomatiki matoleo mapya. Sawazisha viendelezi kupitia "Dhibiti Viendelezi" > "Sasisha Vyote". Angalia ujumuishaji wa hifadhidata ya SQLite kwenye chelezo otomatiki za Umbrel.
- **Kwenye VPS**: Sasisha wewe mwenyewe ukitumia `cd lnbits && git pull && uv sync --all-extras && sudo systemctl anzisha upya lnbits`. Fuatilia kumbukumbu za mfumo: `sudo journalctl -u lnbits -f`.



## Hitimisho



Upangishaji wa kibinafsi wa LNbits hutoa njia thabiti ya uhuru wa kifedha wa Lightning. VPS + Phoenixd inatoa suluhisho nyepesi kwa huduma za haraka, ujumuishaji kamili wa Umbrel na node iliyopo ya Bitcoin. Usanifu unaoweza kuenea huwezesha mageuzi kutoka kwa watumiaji wengi wa wallet hadi kesi za matumizi ya biashara ya kisasa.



Kujikaribisha mwenyewe kunamaanisha kuwajibika: kuhifadhi nakala za seed, linda ufikiaji, anza na viwango vya kawaida. Kwa tahadhari hizi, LNbits inakuwa suluhisho thabiti kwa uchumi wa Lightning, huku ikihifadhi ugatuaji na uhuru.



## Rasilimali



### Nyaraka rasmi




- [Hati za LNbits](https://docs.lnbits.org)
- [LNbits GitHub](https://github.com/lnbits/lnbits)
- [Phoenixd GitHub](https://github.com/ACINQ/phoenixd)
- [Mwongozo rasmi wa usakinishaji](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md)



### Miongozo ya jumuiya




- [Usanidi wa awali wa server ya Ubuntu](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/) na Daniel P. Costas (usalama wa hatua kwa hatua wa VPS)
- [LNbits + Phoenixd usakinishaji kwenye Ubuntu VPS](https://danielpcostas.dev/install-lnbits-phoenixd-vps-ubuntu/) na Daniel P. Costas (mwongozo kamili)
- [server ya LNbits kwenye Clearnet](https://ereignishorizont.xyz/lnbits-server/en/) na Axel
- [LNbits kwenye VPS](https://github.com/TrezorHannes/vps-lnbits) na Hannes
