---
name: Seva ya LNbits
description: Ufungaji na usanidi wa seva ya LNbits inayojiendesha yenyewe kwenye Ubuntu VPS na PHOENIXD au kwenye Umbrel.
---

![cover](assets/cover.webp)



LNbits ni programu huria ya wavuti ya Interface ambayo inabadilisha mandharinyuma yoyote ya Umeme (LND, Core Lightning, PHOENIXD) kuwa jukwaa kamili la huduma. Suluhisho hili linalojipangia mwenyewe hukuwezesha kudhibiti jalada nyingi za Umeme ukiwa umejitenga, kusambaza sehemu za mauzo, kuunda mifumo ya uchangiaji au huduma za bili, huku ukihifadhi udhibiti kamili wa pesa zako.



Mafunzo haya yanashughulikia mbinu mbili za usakinishaji: **VPS Ubuntu iliyo na PHOENIXD** (suluhisho jepesi bila nodi kamili ya Bitcoin) na **Mwavuli** (muunganisho na nodi yako iliyopo ya LND). Tofauti na mafunzo ya jumla ya LNbits ya Mtandao wa Plan B, ambayo yanashughulikia dhana na viendelezi, mwongozo huu unaangazia taratibu za kiufundi za hatua kwa hatua za usakinishaji.



## LNbits ni nini?



LNbits ni mfumo wa uhasibu wa Umeme uliotengenezwa katika Python (FastAPI) unaounganishwa na mazingira ya nyuma yaliyopo (LND, Core Lightning, PHOENIXD). Tofauti na nodi za kawaida za Umeme, LNbits hutoa Interface inayoweza kufikiwa, kukuwezesha kudhibiti portfolio kadhaa zilizojitenga kwa funguo zao za API. Unaweza kuunda akaunti ndogo za familia yako, wafanyikazi au miradi, bila kuwapa ufikiaji wa pesa zako zote.



Usanifu uliotenganishwa huhifadhi maelezo katika SQLite (chaguo-msingi) au PostgreSQL (uzalishaji), huku pesa zikisalia kusimamiwa na mazingira yako ya nyuma ya Umeme. Utengano huu unahakikisha kubebeka: unaweza kuhama kutoka PHOENIXD hadi LND bila kupoteza data yako ya mtumiaji.



## Vipengele muhimu



LNbits inatoa **mfumo wa upanuzi** unaoweza kutumika tofauti: TPoS (mauzo), Paywall (uchumaji wa maudhui), Matukio (tiketi), LndHub (seva ya BlueWallet), Kadi za Bolt (malipo ya NFC), Malipo ya Gawanya (usambazaji wa kiotomatiki), na Kidhibiti cha Mtumiaji (udhibiti wa mtumiaji na uthibitishaji).



**dashibodi** huonyesha salio la wakati halisi, historia ya miamala na zana za kulipa. Kila Wallet ina URL ya kipekee iliyo na funguo zake za API, kuruhusu ufikiaji bila kuingia kwa kawaida. Mfumo wa ufunguo wa ngazi tatu wa API** (msimamizi, Invoice, wa kusoma tu) hutoa udhibiti wa punjepunje wa ruhusa kwa miunganisho salama.



LNbits hutekeleza **LNURL** (LNURL-pay, LNURL-Withdraw, LNURL-auth) na inasaidia **Lightning Address**, ikihakikisha utangamano na pochi za kisasa za Umeme na kuwezesha utumaji wa huduma za kitaalamu.



## Mifumo inayotumika



**Ubuntu VPS**: Suluhisho nyepesi bila nodi kamili ya Bitcoin. Masharti: 1 vCPU, RAM ya GB 1-2, Ubuntu 22.04 LTS, Python 3.10+, Git, UV. HTTPS + jina la kikoa linahitajika kwa kufichuliwa kwa umma (huduma za LNURL).



**Mwavuli**: Usakinishaji kwa urahisi kutoka kwa Duka la Programu. Sharti: nodi ya Umbrel inayofanya kazi na LND iliyosawazishwa na chaneli wazi. Usanidi otomatiki.



Hapo chini kuna viungo vya mafunzo yetu ya Umbrel na Umbrel LND:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Inasakinisha kwenye Ubuntu VPS na PHOENIXD



### Hatua ya 1: Kulinda seva ya VPS



**Kabla ya usakinishaji wowote **, unahitaji kulinda seva yako ya Ubuntu VPS kulingana na sheria za sanaa. Hatua hii ni **muhimu** ili kulinda miundombinu yako na fedha zako za Umeme.



Huu hapa ni mwongozo wa kina wa kukusaidia kuanza: **[Usanidi wa awali wa seva ya Ubuntu - Mwongozo wa hatua kwa hatua](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/)** na Daniel P. Costas.



Mwongozo huu unashughulikia usanidi wa mtumiaji, SSH salama, ngome (UFW), fail2ban, masasisho ya kiotomatiki, na mbinu bora za usalama za mfumo.



### Hatua ya 2: Kusakinisha PHOENIXD



Mara seva yako ikiwa salama, unahitaji kusakinisha na kusanidi PHOENIXD. Mpango wa Mtandao wa B unatoa usakinishaji kamili wa kufunika mafunzo, kizazi cha seed na usanidi wa huduma ya mfumo:



https://planb.academy/tutorials/node/lightning-network/phoenixd-beb86edd-f9c0-4bec-ad36-db234c88e7b1

Mara tu PHOENIXD inapoanza kutumika (angalia kwa `./Phoenix-CLI getinfo`), kumbuka **nenosiri la HTTP** katika `~/.Phoenix/Phoenix.conf` - utahitaji ili kuunganisha LNbits kwenye PHOENIXD.



### Usambazaji wa LNbits



Sakinisha UV na clone LNbits :


```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
git clone https://github.com/lnbits/lnbits.git && cd lnbits
uv sync --all-extras
```



Sanidi mazingira ya nyuma ya PHOENIXD:


```bash
cp .env.example .env && nano .env
```



Ongeza kwa `.env` :


```
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://127.0.0.1:9740
PHOENIXD_API_PASSWORD=<mot-de-passe-phoenix.conf>
```



Jaribu kwa `uv run lnbits --host 0.0.0.0 --port 5000` kisha uunde huduma ya mfumo kwa `Wants=PHOENIXD.service`.



## Usanidi wa awali na matumizi ya kwanza



### Uanzishaji wa SuperUser



Washa msimamizi wa Interface katika `.env` :


```
LNBITS_ADMIN_UI=true
```



Anzisha tena LNbits (`sudo systemctl anzisha tena lnbits`) na urejeshe Kitambulisho cha SuperUser:


```bash
cat ~/lnbits/data/.super_user
```



Nenda kwa `http://<IP-VPS>:5000/Wallet?usr=<SuperUserID>` kwa paneli ya usimamizi. Menyu ya "Seva" inakuwezesha kusanidi vyanzo vya ufadhili, viendelezi na akaunti za mtumiaji.



### Salama uundaji wa akaunti



**Muhimu kwa kufichuliwa kwa umma**: Ikiwa unaonyesha mfano wako wa LNbits kwenye jina la kikoa cha umma linaloweza kufikiwa kutoka kwa Mtandao, ni **muhimu** kuzima uundaji wa akaunti za watumiaji bila malipo.



Kutoka kwa utawala wa SuperUser Interface, nenda kwenye "Mipangilio" na kisha kwenye sehemu ya "Usimamizi wa Mtumiaji". Utapata chaguo la "Ruhusu uundaji wa watumiaji wapya".



![Gestion des utilisateurs - Sécurité](assets/fr/17.webp)



**Kwa maonyesho ya umma yenye jina la kikoa** :




- Lazima uzime** chaguo la "Ruhusu uundaji wa watumiaji wapya".
- Bila ulinzi huu, mtu yeyote kwenye Mtandao anaweza kufungua akaunti kwa mfano wako
- Mshambulizi anaweza kuunda akaunti na kutumia ukwasi wa LIGHTNING NODE yako bila wewe kujua
- Utahitaji kuunda akaunti za mtumiaji wewe mwenyewe kutoka kwa Interface SuperUser



**Kwa matumizi ya ndani pekee** :




- Chaguo hili sio muhimu sana ikiwa mfano wako unapatikana ndani ya nchi pekee (http://localhost:5000)
- Walakini, kuzima chaguo hili ni mazoezi mazuri ya usalama wa jumla



Baada ya kusanidiwa, msimamizi wa SuperUser pekee ndiye anayeweza kuunda akaunti mpya za watumiaji kupitia "Watumiaji" wa Interface. Mbinu hii inahakikisha udhibiti kamili juu ya nani anaweza kufikia miundombinu yako ya Umeme na kutumia pesa zako.



### Kufungua kituo cha kwanza



PHOENIXD inadhibiti chaneli kiotomatiki kupitia uwekaji maji kiotomatiki. generate a Lightning Invoice ya ~30,000 Sats kutoka LNbits na kuilipa kutoka Wallet nyingine. PHOENIXD hufungua kituo kiotomatiki kwa ACINQ. Ada ya ufunguzi (~ 20-23k Sats) inatolewa, salio iliyobaki (~ 7-10k Sats) inaonekana baada ya uthibitisho wa On-Chain.



Angalia hali kwa `./Phoenix-CLI getinfo`. Kisha zingatia kuzima uwazi wa kiotomatiki (`auto-liquidity=off` katika `Phoenix.conf`) ili kudhibiti fursa za vituo.



### Onyesho la umma na HTTPS



**Muhimu**: HTTPS lazima ionekane hadharani (ufunguo wa usalama wa API + uoanifu wa LNURL). Ruka hatua hii kwa matumizi ya ndani pekee.



**Caddy (inapendekezwa)**: SSL otomatiki. `sudo apt install -y caddy`, hariri `/etc/caddy/Caddyfile` :


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


Washa: `sudo LN -s /etc/nginx/sites-available/lnbits /etc/nginx/sites-enabled/ && sudo nginx -t && sudo systemctl pakia tena nginx && sudo certbot --nginx -d your-domain.com`



Ongeza kwa `.env`: `FORWARDED_ALLOW_IPS=*`



## Ufungaji wa mwavuli



### Usambazaji kutoka kwa Duka la Programu



Nenda kwenye Duka la Programu ya Umbrel, tafuta "LNbits", na ubofye "Sakinisha".



![Installation LNbits Umbrel](assets/fr/01.webp)



Umbrel hukagua kiotomatiki vitegemezi vinavyohitajika. LNbits inahitaji LIGHTNING NODE (LND) ili kuendesha. Ikiwa LIGHTNING NODE yako tayari inafanya kazi, bofya kwenye "Sakinisha LNbits" ili kuthibitisha.



![Dépendances LNbits](assets/fr/02.webp)



Umbrel hupakua picha ya Docker, husanidi miunganisho kiotomatiki na LND, na kuwasha chombo (dakika 2-5). Ufungaji unafanyika kabisa nyuma.



### Usanidi wa awali wa SuperUser



Wakati wa uzinduzi wa kwanza, LNbits hukuhimiza kuunda akaunti ya msimamizi wa SuperUser. Ingiza jina la mtumiaji na uweke nenosiri salama ili kulinda ufikiaji wa mfumo wa utawala wa Interface.



![Configuration SuperUser](assets/fr/03.webp)



**Muhimu**: Akaunti hii ya SuperUser ina haki kamili kwenye mfano wako wa LNbits. Chagua nenosiri dhabiti na uliweke salama.



Ukishafungua akaunti, utachukuliwa kiotomatiki hadi eneo kuu la utawala la Interface. Umbrel tayari imeweka LND kama chanzo chako cha ufadhili - malipo yote ya Radi yatapitia chaneli zako zilizopo.



### Ufikiaji wa msimamizi wa Interface



Katika menyu ya upande wa kushoto, bofya "Mipangilio" ili kufikia paneli kamili ya usimamizi.



![Interface Settings](assets/fr/04.webp)



Sehemu ya "Usimamizi wa Pochi" huonyesha taarifa muhimu kuhusu usanidi wako:




- Chanzo cha Ufadhili** : LndBtcRestWallet (muunganisho wa moja kwa moja kwenye nodi yako ya Mwavuli ya LND)
- Salio la Nodi** : Jumla ya ukwasi unaopatikana katika chaneli zako za Umeme
- Salio la LNbits**: Fedha zilizotengwa kwa mfumo wa LNbits (mwanzoni 0 Sats)



Sasa unaweza kutumia moja kwa moja ukwasi wa nodi yako ya Umbrel kwa pochi zote za LNbits unazounda. Hakuna usanidi wa ziada unaohitajika - LNbits iko na inafanya kazi.



### Usimamizi wa mtumiaji



Moja ya vipengele vya nguvu zaidi vya LNbits ni uwezo wake wa kuunda watumiaji wengi huru, kila moja ikiwa na uthibitishaji wa nenosiri na pochi zilizotengwa. Usanifu huu hufanya iwezekane kuchukua fursa ya ukwasi wa nodi yako ya Umbrel huku ukitoa akaunti ndogo zilizotengwa kwa matumizi tofauti: biashara, familia, wafanyikazi, miradi, n.k.



Katika menyu ya kando, bofya "Watumiaji" ili kufikia usimamizi wa mtumiaji. Bofya kwenye "CREATE ACCOUNT" ili kuongeza mtumiaji mpya.



![Gestion des utilisateurs](assets/fr/05.webp)



Jaza fomu ya kuunda mtumiaji:




- Jina la mtumiaji**: Ingia jina la mtumiaji (mfano: "Satoshi")
- Weka Nenosiri**: Amilisha chaguo hili ili kuweka nenosiri la uthibitishaji
- Nenosiri** na **Nenosiri kurudia**: Weka nenosiri la mtumiaji huyu



![Création utilisateur satoshi](assets/fr/06.webp)



Sehemu za hiari (Ufunguo wa Umma wa Nostr, Barua pepe, Jina la Kwanza, Jina la Mwisho) zinaweza kuachwa wazi kwa usanidi mdogo. Bofya kwenye "CREATE ACCOUNT" ili kuthibitisha.



![Confirmation utilisateur créé](assets/fr/07.webp)



Mtumiaji wako mpya sasa anaonekana katika orodha ya watumiaji na kitambulisho chake cha kipekee na jina la mtumiaji.



![Liste des utilisateurs](assets/fr/08.webp)



**Hoja muhimu**: Kila mtumiaji anaweza kuingia kwa kujitegemea kabisa na nenosiri lake mwenyewe. Msimamizi wa SuperUser huhifadhi udhibiti kamili kupitia zana ya usimamizi ya Interface.



### Mtumiaji Wallet usimamizi



Sasa kwa kuwa mtumiaji wa "Satoshi" ameundwa, unahitaji kumpa Umeme wa Wallet. Bofya kwenye ikoni ya Wallet (ikoni ya pili) kwa mtumiaji anayehusika, kisha kwenye "UNDA Wallet MPYA".



![Gestion des wallets](assets/fr/09.webp)



Kisanduku cha mazungumzo kinakuhimiza kutaja Wallet. Weka jina la maelezo (k.m. "Wallet Of Satoshi") na uchague sarafu ya kuonyesha (CUC, USD, EUR, n.k.).



![Création wallet](assets/fr/10.webp)



Bonyeza "CREATE". LNbits hutengeneza umeme wa Wallet papo hapo kwa mtumiaji huyu.



![Confirmation wallet créé](assets/fr/11.webp)



Sasa unaona pochi mbili zilizopo: chaguo-msingi Wallet "LNbits Wallet" iliyoundwa moja kwa moja, na mpya "Wallet Ya Satoshi". Ili kurahisisha matumizi ya mtumiaji, unaweza kufuta chaguomsingi la Wallet kwa kubofya aikoni ya kufuta (tupio nyekundu).



![Wallet final unique](assets/fr/12.webp)



Mtumiaji wa "Satoshi" sasa ana Wallet moja, iliyotambuliwa wazi. Kila mtumiaji Wallet hufanya kazi kwa uhuru kabisa, huku akitumia ukwasi wa nodi yako ya msingi ya LND.



**Dhana kuu**: Pochi hizi zote hushiriki ukwasi wa kimataifa wa nodi yako ya Umbrel. Hauundi chaneli mpya za Radi kwa kila Wallet - LNbits hufanya kazi kama hesabu mahiri ya Layer ambayo inadhibiti ugawaji wa fedha ndani ya miundombinu yako iliyopo ya Umeme. Hiyo ndiyo nguvu ya mfumo wa Wallet wa LNbits.



### Kuingia kwa mtumiaji



Toka kwenye akaunti ya SuperUser (ikoni ya juu kulia) na urudi kwenye ukurasa wa kuingia wa LNbits. Sasa unaweza kuingia kwa kutumia kitambulisho cha mtumiaji mpya.



![Connexion utilisateur satoshi](assets/fr/13.webp)



Ingiza jina la mtumiaji ("Satoshi") na nenosiri lililoelezwa hapo awali, kisha ubofye "INGIA". Mtumiaji anapata ufikiaji wa moja kwa moja kwa Wallet yake ya kibinafsi, iliyotengwa kabisa na utawala wa Interface.



### Interface kutoka kwa mtumiaji wa Wallet



Mara tu imeunganishwa, mtumiaji anapata Interface yake kutoka kwa Umeme wa Wallet.



![Interface wallet utilisateur](assets/fr/14.webp)



Vipengele vya Interface:




- Salio la sasa**: Imeonyeshwa katika Sats na katika sarafu iliyochaguliwa (CUC katika mfano huu)
- Vitendo vikuu**: "BEKA OMBI" (bandika bili ili kulipa), "UNDA Invoice" (generate risiti), ikoni ya QR (changanua haraka)
- Historia ya muamala** : Kamilisha orodha ya malipo na risiti zote
- Paneli ya upande wa kulia**: Chaguo za usanidi na ufikiaji



### Ufikiaji wa simu ya Wallet



Paneli ya upande wa kulia inatoa kipengele cha vitendo hasa: ufikiaji wa simu kwa Wallet. Fungua sehemu ya "Ufikiaji wa Simu" ili kugundua chaguo zinazopatikana.



![Mobile Access](assets/fr/15.webp)



LNbits inatoa njia kadhaa za kutumia Wallet hii kwenye simu mahiri:



**Chaguo la 1: Programu zinazooana za simu




- Pakua **Zeus** au **BlueWallet** kutoka kwa App Store au Google Play
- Washa kiendelezi cha **LndHub** katika LNbits kwa Wallet hii
- Changanua msimbo wa QR wa LndHub ukitumia programu ya simu ili kuunganisha Wallet



**Chaguo la 2: Ufikiaji wa moja kwa moja kupitia kivinjari cha rununu**




- Msimbo wa QR unaoonyeshwa katika "Hamisha kwa Simu ukitumia Msimbo wa QR" una URL kamili ya Wallet yenye uthibitishaji jumuishi.
- Changanua msimbo huu wa QR kutoka kwa simu yako mahiri ili kufungua Wallet moja kwa moja kwenye kivinjari chako cha rununu
- Ongeza ukurasa kwenye skrini ya kwanza kwa ufikiaji wa haraka



**Usalama muhimu**: URL hii ina funguo za API kwa ufikiaji kamili wa Wallet. Usiwahi kuishiriki hadharani. Tumia msimbo huu wa QR jinsi ungefanya funguo zako za faragha za Bitcoin - mtu yeyote anayechanganua msimbo huu wa QR anapata ufikiaji kamili wa Wallet.



Kipengele hiki cha rununu hugeuza kielelezo chako cha Umbrel cha LNbits kuwa seva halisi ya Lightning Wallet kwa ajili yako na marafiki zako, huku kikihifadhi mamlaka kamili juu ya fedha zako kwa shukrani kwa nodi yako inayojiendesha.



### Kushiriki ufikiaji wa mtumiaji



Kesi kuu ya utumiaji wa usanidi huu wa watumiaji wengi ni **kushiriki pochi na familia yako au mduara wa karibu**. Mara tu unapounda mtumiaji aliye na Wallet maalum (kama vile "Satoshi" katika mfano wetu), unaweza kushiriki vitambulisho hivi vya kuingia na wanafamilia wako unaowaamini.



**Usalama wa ufikiaji kwenye Mwavuli**: Ufikiaji wa mfano wako wa LNbits kwenye Umbrel unalindwa kwa kawaida, kwani unaweza kufikiwa tu :




- Kwenye mtandao wa ndani** : Wanafamilia wako waliounganishwa kwenye mtandao sawa wa WiFi/Ethernet wanaweza kufikia mfano huo
- Kupitia VPN**: Ikiwa unatumia VPN kama vile Tailscale iliyosanidiwa kwenye seva yako ya Umbrel, watumiaji walioidhinishwa wanaweza kupata ufikiaji salama wa mbali.



Layer hii maradufu ya ulinzi (ufikiaji wa mtandao + uthibitishaji wa mtumiaji) hufanya chaguo la "Ruhusu uundaji wa watumiaji wapya" kuwa muhimu sana kwenye Umbrel. Watu ambao tayari wana ufikiaji wa mtandao wako au VPN wanaweza kufikia kuingia kwa Interface.



**Hali ya kawaida**: Unafungua akaunti ya "baba", akaunti ya "mama", akaunti ya "biashara" na kadhalika. Kila mwanafamilia ana Umeme wake wa pekee wa Wallet, huku akinufaika na ukwasi ulioshirikiwa wa nodi yako ya Umbrel. Shiriki kwa urahisi jina la mtumiaji na nenosiri - mtumiaji anaweza kisha kuunganisha kutoka kwa kifaa chochote kwenye mtandao wako wa karibu au kupitia Tailscale VPN yako. Tafadhali tazama mafunzo yetu yaliyojitolea ya Tailscale kwa habari zaidi:



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Chunguza viendelezi vinavyopatikana



Rudi kwa Interface SuperUser na ufikie menyu ya "Viendelezi" katika paneli ya upande wa kushoto ili kugundua mfumo kamili wa kiendelezi wa LNbits.



![Extensions disponibles](assets/fr/16.webp)



LNbits inatoa katalogi tajiri ya viendelezi ambavyo hubadilisha mfano wako kuwa jukwaa la huduma za Umeme halisi:





- Jukebox**: Mfumo wa jukebox unaoendeshwa na Sats (malipo ya Spotify)
- Tiketi za Usaidizi**: Mfumo wa usaidizi unaolipishwa (pokea Satss kujibu maswali)
- TPoS**: Kituo salama, cha kuuza cha simu kwa wauzaji reja reja
- Kidhibiti cha Mtumiaji**: mtumiaji wa hali ya juu na usimamizi wa Wallet (ambao tumetumia hivi punde)
- Matukio**: Uuzaji na uthibitishaji wa tikiti za hafla
- LNURLDevices**: Usimamizi wa sehemu ya mauzo, ATM, swichi zilizounganishwa
- SMTP**: Wezesha watumiaji kutuma barua pepe na kupata Satss
- Boltcards**: Kupanga kadi za NFC kwa malipo ya umeme ya bomba-ili-kulipa
- NostrNip5**: Unda anwani za NIP5 za vikoa vyako
- Malipo ya kugawanyika**: Usambazaji wa malipo kiotomatiki kati ya pochi nyingi



Kila kiendelezi huwashwa kwa mbofyo mmoja kutoka kwa Interface hii. Viendelezi vilivyowekewa alama ya "BURE" havilipishwi, ilhali vingine vinapatikana kama matoleo "INAYOLIPIWA". Kagua katalogi ili kubaini zile zinazolingana na mahitaji yako - iwe kwa biashara, usimamizi wa familia, au kufanya majaribio ya uwezo wa Lightning Network.



## Faida na mapungufu



**Manufaa**: Mamlaka ya kifedha (udhibiti kamili wa fedha/funguo/data), kubadilika kwa usanifu (uhamiaji usio na hasara wa VPS→Full node), mfumo wa upanuzi wa kitaalamu, Interface angavu.



**Mapungufu** : Programu katika beta (tahadhari juu ya kiasi), usalama chini ya wajibu wa msimamizi, URL zilizo na funguo nyeti za API (lazima ya HTTPS), usimamizi wa watumiaji wengi unamaanisha wajibu wa ulezi.



## Mbinu bora



**Hifadhi rudufu**: seed PHOENIXD/vitambulisho LND, hifadhidata ya LNbits, faili za `.env`. Weka otomatiki kila siku, weka mbali na seva ya uzalishaji, iliyosimbwa. Mtihani hurejesha mara kwa mara.



**Matengenezo**: Angalia mara kwa mara masasisho (LNbits, nyuma ya umeme, mfumo wa uendeshaji). Angalia vidokezo vya toleo kila wakati kabla ya sasisho kuu.





- Kwenye Umbrel**: Duka la Programu hukuarifu kiotomatiki matoleo mapya. Sawazisha viendelezi kupitia "Dhibiti Viendelezi" > "Sasisha Vyote". Angalia ujumuishaji wa hifadhidata ya SQLite kwenye chelezo otomatiki za Umbrel.
- Kwenye VPS**: Sasisha wewe mwenyewe ukitumia `cd lnbits && git pull && uv sync --all-extras && sudo systemctl anzisha upya lnbits`. Fuatilia kumbukumbu za mfumo: `sudo journalctl -u lnbits -f`.



## Hitimisho



Upangishaji wa kibinafsi wa LNbits hutoa njia thabiti ya uhuru wa kifedha wa Umeme. VPS+PHOENIXD inatoa suluhisho nyepesi kwa huduma za haraka, ushirikiano kamili wa Umbrel na nodi iliyopo ya Bitcoin. Usanifu unaoweza kuenea huwezesha mageuzi kutoka kwa watumiaji wengi wa Wallet hadi kesi za matumizi ya biashara ya kisasa.



Kujikaribisha mwenyewe kunamaanisha kuwajibika: kuhifadhi nakala za mbegu, linda ufikiaji, anza na viwango vya kawaida. Kwa tahadhari hizi, LNbits inakuwa suluhisho thabiti kwa uchumi wa Umeme, huku ikihifadhi ugatuaji na uhuru.



## Rasilimali



### Nyaraka rasmi




- [Hati za LNbits](https://docs.lnbits.org)
- [LNbits GitHub](https://github.com/lnbits/lnbits)
- [PHOENIXD GitHub](https://github.com/ACINQ/PHOENIXD)
- [Mwongozo rasmi wa usakinishaji](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md)



### Miongozo ya jumuiya




- [Usanidi wa awali wa seva ya Ubuntu](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/) na Daniel P. Costas (usalama wa hatua kwa hatua wa VPS)
- [LNbits + PHOENIXD usakinishaji kwenye Ubuntu VPS](https://danielpcostas.dev/install-lnbits-PHOENIXD-vps-ubuntu/) na Daniel P. Costas (mwongozo kamili)
- [Seva ya LNbits kwenye Clearnet](https://ereignishorizont.xyz/lnbits-server/en/) na Axel
- [LNbits kwenye VPS](https://github.com/TrezorHannes/vps-lnbits) na Hannes