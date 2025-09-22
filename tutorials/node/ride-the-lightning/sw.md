---
name: Ride The Lightning (RTL)
description: Tumia Ride The Lightning (RTL) kudhibiti eneo lako la Umeme
---
![cover](assets/cover.webp)


## 1. Utangulizi



**Ride The Lightning (RTL)** ni programu kamili ya wavuti ya Interface ya kudhibiti nodi ya Lightning Network. Programu hii ya wavuti inayojiendesha yenyewe hutoa **"cockpit" ya Umeme** inayopatikana kutoka kwa kivinjari chako. RTL hufanya kazi na utekelezaji wote mkuu wa Umeme (LND, Core Lightning/CLN na Eclair) na hukupa udhibiti kamili wa nodi na chaneli zako. Chanzo-wazi (leseni ya MIT) na bila malipo, RTL imeunganishwa kwa chaguo-msingi katika suluhu nyingi za nodi za turnkey (RaspiBlitz, MyNode, Umbrel, nk.).



**Bila Interface ya picha**, nodi za Umeme zinaweza kudhibitiwa tu kupitia amri za CLI zinazofaa mtumiaji. RTL hurahisisha shughuli hizi kwa kutumia Interface ya ergonomic. Hapa kuna **matumizi makuu**:





- **Tazama vituo na nodi zako** - Dashibodi inaonyesha salio la On-Chain, ukwasi wa umeme (ya karibu/mbali), hali ya ulandanishi, lakabu za nodi na zaidi. Unaweza kutazama orodha ya kituo chako, uwezo, usambazaji wa ndani/mbali na hali. RTL hutoa dashibodi zinazozingatia muktadha ili kuchanganua shughuli kutoka pembe tofauti.





- **Udhibiti wa njia za umeme** - Fungua/funga chaneli kwa mibofyo michache. RTL hukuruhusu kuungana na mwenzi wako na kufungua kituo bila amri. Unaweza kurekebisha ada za uelekezaji, kuangalia alama ya salio, au kuanzisha salio la mduara ili kusawazisha fedha kati ya vituo.





- **Fuatilia na ufanye malipo** - RTL hudhibiti miamala ya umeme: tuma malipo kupitia ankara, ankara za generate za kupokea, fuatilia miamala (malipo, uelekezaji) na historia ya kina. Interface pia huchanganua uelekezaji ili kuona ni malipo gani yanapitia nodi yako.





- **Usimamizi na uhifadhi wa Wallet On-Chain** - Kichupo cha On-Chain hukuwezesha anwani za generate na kutuma miamala. RTL hurahisisha kuhifadhi chaneli kwa kusafirisha faili ya SCB ya LND, ikiwa na sasisho la kiotomatiki kwa kila urekebishaji wa kituo.



Kwa kifupi, RTL ni **dashibodi yenye nguvu ya Lightning Network**, inayotoa Interface ya kielimu kwa ajili ya kujaribu nodi yako kila siku. Mafunzo haya yatakuongoza katika usakinishaji na matumizi yake kudhibiti vituo na malipo yako.



## 2. Uendeshaji wa kiufundi wa RTL



![Schéma de l'architecture RTL : interface responsive compatible avec tous les appareils, frontend Angular, serveur Node (port 3000), connecté aux API REST de LND](assets/fr/01.webp)



Kabla ya kupata maelezo ya nitty-gritty, ni muhimu kuelewa kwa ufupi **jinsi RTL inavyoingiliana na nodi yako ya Umeme** katika kiwango cha kiufundi.



**Usanifu wa jumla:** RTL ni programu ya wavuti iliyojengwa kwa Node.js (backend) na Angular (mbele). Kwa maneno madhubuti, RTL hufanya kazi kama seva ndogo ya wavuti ya ndani (kwenye bandari 3000 kwa chaguo-msingi) ambayo hujadiliana na utekelezaji wako wa Umeme kupitia API zake. Kulingana na aina ya:





- Kwa **LND**, RTL hutumia LND's REST API (bandari 8080) kutekeleza amri za Umeme. Muunganisho umelindwa na TLS na unahitaji faili ya **admin macaroon** ya LND kwa uthibitishaji.





- Kwa **Umeme wa Msingi (CLN)**, RTL hutumia ama REST API iliyotolewa na *c-umeme-REST*, au njia ya **ufikiaji** kupitia programu-jalizi ya `commando`. Suluhu kama vile Umbrel husanidi kiotomatiki hizi Elements.





- Kwa **Eclair**, RTL inaunganisha kwenye API ya Eclair REST kwa kutumia nenosiri la uthibitishaji lililowekwa.



**Usanidi na usalama:** RTL imesanidiwa kupitia faili ya JSON (`RTL-Config.json`) ambapo unafafanua mlango wa wavuti, nenosiri la kufikia, na maelezo ya muunganisho kwenye nodi yako. Wavuti ya Interface inalindwa na kuingia/nenosiri (chaguo-msingi `nenosiri` ya kubadilishwa) na inaauni 2FA. Kwa chaguo-msingi, RTL hutumika kama HTTP ya ndani (`http://localhost:3000`), lakini kwa ufikiaji wa mbali, tumia muunganisho salama kila wakati (HTTPS kupitia seva mbadala, Tor, au VPN).



Kwa kifupi, RTL ni sehemu ya ziada inayounganishwa kwenye nodi yako kupitia API salama, inahitaji tokeni zinazofaa za ufikiaji, na inatoa usalama wake wa Layer. Usanifu huu wa kawaida hata hukuruhusu kudhibiti **nodi kadhaa za Umeme kwa mfano mmoja wa RTL**.



## 3. Ufungaji wa RTL



RTL inavyosambazwa kama programu huria, kuna njia kadhaa za kuisakinisha kwenye mfumo wako. Katika sehemu hii, tutashughulikia mbinu mbili kuu: ufungaji wa mwongozo na ufungaji kupitia Umbrel.



### Njia ya mwongozo



Usakinishaji wa kibinafsi unafaa ikiwa ungependa kuweka udhibiti ulioboreshwa, au ikiwa unaunganisha RTL kwenye usanidi maalum. Hatua zilizo hapa chini ni za nodi ya LND inayoendesha Linux (k.m. Raspberry Pi au VPS inayoendesha Ubuntu/Debian), lakini ni sawa kwa CLN/Eclair.



**Sharti:** hakikisha kuwa una nodi **iliyosawazishwa** ya Bitcoin na nodi ya Umeme inayofanya kazi (LND, CLN au Eclair) kwenye mashine. RTL haina nodi ya Umeme kwa kila sekunde, inayounganisha kwa nodi iliyopo. Pia unahitaji **Node.js** kusakinishwa (toleo la 14+ linapendekezwa). Unaweza kuangalia na `node -v` au kusakinisha Node kutoka kwa tovuti rasmi (https://nodejs.org/en/download/) au msimamizi wa kifurushi chako.



Hatua kuu za ufungaji ni:



**Pakua msimbo wa RTL**: Weka hazina rasmi ya RTL GitHub katika saraka uliyochagua. Kwa mfano:



```bash
git clone https://github.com/Ride-The-Lightning/RTL.git
cd RTL
```



**Vitegemezi vya kusakinisha**: RTL ni programu ya Node.js, kwa hivyo unahitaji kusakinisha moduli zake zinazohitajika. Kwenye folda ya RTL, endesha:



```bash
npm install --omit=dev --legacy-peer-deps
```



Amri hii husakinisha vifurushi muhimu vya NPM (kupuuza utegemezi wa maendeleo). Chaguo la `--legacy-peer-deps` linapendekezwa ili kuepuka mizozo inayowezekana ya utegemezi wa Node.



**RTL-Config**: Mara tu vitegemezi vimewekwa, tayarisha faili ya usanidi. Nakili/badilisha jina la faili ya `Sampuli-RTL-Config.json` katika mzizi wa mradi kuwa `RTL-Config.json`. Fungua katika yako:





   - **Nenosiri la UI**: chagua nenosiri salama na uliweke katika `multiPass` (badala ya `"nenosiri"` chaguo-msingi).
   - **Mlango**: chaguo-msingi `3000`. Unaweza kuibadilisha ikiwa mlango huu tayari umechukuliwa kwenye mashine yako.
   - **Nodi**: katika sehemu ya `nodi[0]`, rekebisha vigezo vya nodi yako:
     - `lnNode`: jina la maelezo la nodi yako (k.m. `"LND Node Maison"`).
     - lnUtekelezaji`: `"LND"` (au `"CLN"`/`"ECL"` inavyofaa).
     - Chini ya `uthibitishaji`:
       - macaroonPath`: taja njia kamili ya folda iliyo na msimamizi wa macaroon wa LND.
       - `configPath`: njia ya faili ya usanidi ya nodi (`LND.conf` kwa LND).
     - Chini ya `mipangilio`:
       - `fiatConversion`: weka kuwa `kweli` ikiwa unataka ubadilishaji wa sarafu ya fiat.
       - `Vituo visivyotangazwa`: weka `true` ili kuona vituo ambavyo havijatangazwa.
       - mandhariColor` na `themeMode`: ubinafsishaji wa Interface.
       - channelBackupPath`: njia ya chelezo za kituo cha LND.
       - `lnServerUrl`: URL ya nodi yako ya Umeme (k.m. `https://127.0.0.1:8080`).



**Anzisha seva ya RTL**: Katika folda ya RTL, endesha :



```bash
node rtl
```



Programu huanza na inaweza kufikiwa katika `http://localhost:3000`.



**(Si lazima) Endesha RTL kama huduma**: Kwa uanzishaji kiotomatiki, unda systemd :



Ili kufanya hivi:




- Fungua terminal kwenye mashine yako.
- Unda faili mpya ya huduma kwa amri ifuatayo (Badilisha `nano` na kihariri unachopenda):


```bash
sudo nano /etc/systemd/system/RTL.service
```




- Nakili na ubandike yaliyomo hapa chini kwenye faili hii:



```ini
[Unit]
Description=Ride The Lightning web UI
Wants=lnd.service
After=lnd.service

[Service]
ExecStart=/usr/bin/node /chemin/vers/RTL/rtl
User=<votre_user>
Restart=always
TimeoutSec=120
RestartSec=30

[Install]
WantedBy=multi-user.target
```





- Badilisha `/path/to/RTL/rtl` na njia halisi ya faili ya `rtl` kwenye mashine yako, na `<your_user>` na jina lako la mtumiaji la Linux.
- Hifadhi na funga faili.
- Pakia upya usanidi wa mfumo:


```bash
sudo systemctl daemon-reload
```




- Washa na anza huduma ya RTL:


```bash
sudo systemctl enable RTL
sudo systemctl start RTL
```



RTL sasa itaanza kiotomatiki kila wakati mashine inapowashwa upya. Unaweza kuangalia hali yake na:


```bash
sudo systemctl status RTL
```



### Ufungaji kupitia Umbrel



Ukitumia [Umbrel](https://getumbrel.com), usakinishaji wa RTL ni rahisi zaidi:





- Fikia Mwavuli wa Interface (kawaida kupitia `http://umbrel.local`)
- Nenda kwa **Duka la Programu**
- Tafuta "Panda Umeme"



**Dokezo muhimu: kuna programu mbili tofauti za RTL katika Duka la Programu la Umbrel:**




- **Ride The Lightning** (kwa LND): kwa matumizi na nodi chaguo-msingi ya Umeme ya Umbrel (LND).
- **Panda Umeme (Umeme wa Msingi)**: tumia tu ikiwa umesakinisha programu ya *Umeme wa Msingi* kwenye Umbrel na ungependa kudhibiti nodi hii kwa RTL.



*Kila toleo la RTL limesanidiwa awali ili kujadiliana na utekelezaji unaolingana (LND au Umeme wa Msingi). Ikiwa haujabadilisha nodi yako ya Umeme, chagua toleo la kawaida la LND*



![Fiche de l'application Ride The Lightning dans Umbrel : présentation de l'app avec captures d'écran et bouton violet "Install" en haut à droite](assets/fr/02.webp)





- Bonyeza **Sakinisha**



![Fenêtre d'affichage du mot de passe par défaut après installation de RTL dans Umbrel, avec bouton "Open Ride The Lightning"](assets/fr/03.webp)



**Muhimu:** Baada ya kusakinisha, RTL huonyesha skrini yenye nenosiri chaguo-msingi. **Nakili na uhifadhi nenosiri hili** - utalihitaji ili uingie kwenye Interface RTL. Nenosiri hili litaonyeshwa kila wakati RTL inapoanza hadi uangalie chaguo la "Usionyeshe tena".



Umbrel hutunza kiotomatiki:




- Pakua na usanidi RTL
- Inasanidi ufikiaji wa nodi ya Umeme
- Dhibiti masasisho
- Inalinda ufikiaji wa Interface



Baada ya kusakinishwa, programu inaonekana katika menyu yako ya *Programu* kwenye Umbrel. Bofya kwenye **Panda Umeme** ili kuizindua.



![Écran de connexion RTL via Umbrel : champ de mot de passe avec logo du cheval en haut à gauche, bouton "Login"](assets/fr/04.webp)



Kwenye skrini ya kuingia, weka nenosiri ulilonakili mapema. Baada ya kuingia, mtandao wa Interface RTL utapatikana moja kwa moja kutoka kwa dashibodi ya Umbrel, bila usanidi wa ziada unaohitajika!



## 4. Utangulizi na matumizi ya Interface RTL



Kwa kuwa sasa RTL inatumika, hebu tuchunguze mtandao wake wa Interface na vipengele vyake muhimu. Tutapitia sehemu tofauti za programu ili kukupa muhtasari kamili.



### Jopo kuu la kudhibiti



![Tableau de bord RTL : solde Lightning, solde on-chain, capacité de liquidité entrante/sortante et création de facture](assets/fr/05.webp)



Mara tu unapoingia, unafikia **dashibodi kuu**, ambayo inakupa muhtasari wa nodi yako ya Umeme. Ukurasa huu unaweka habari muhimu katikati:




- Jumla ya salio lako la Umeme
- Salio la On-Chain linapatikana
- Mchanganuo wa ukwasi wako (zinazoingia/zinazotoka)
- Ufikiaji wa haraka wa kutuma na kupokea Satss kupitia nodi yako ya Umeme



### Usimamizi wa Mfuko On-Chain



![Onglet "On-chain" actif dans RTL : solde Bitcoin (en sats, BTC, USD), et liste des transactions avec type d'adresse Taproot](assets/fr/06.webp)



Kichupo cha **On-Chain** hukuwezesha kudhibiti bitcoins zako moja kwa moja kwenye msururu mkuu:




- Onyesho la salio katika vitengo tofauti (Sats, BTC, USD)
- Orodha kamili ya miamala
- Kizazi cha Address Taproot (P2TR), P2SH (NP2WKH) au Bech32 (P2WKH)
- Usimamizi wa UTXO, kupokea na kutuma bitcoins



### Umeme: uwasilishaji wa kina wa menyu ndogo



Interface RTL ina menyu ya kando iliyowekwa kwa Lightning Network, inayoleta pamoja vipengele vyote muhimu vya kudhibiti nodi yako. Hapa kuna maelezo ya kila menyu ndogo, kwa mpangilio wa picha ya skrini:



#### 1. Rika/Chaneli



![Vue de gestion des canaux Lightning (onglet "Peers/Channels" ouvert)](assets/fr/07.webp)



Menyu ndogo hii hukuruhusu:




- Tazama orodha ya wenzako waliounganishwa na vituo vya Umeme vilivyo wazi au vinavyosubiri.
- Ongeza rika mpya (unganisha kwa nodi nyingine ya Umeme).
- Fungua, funga au udhibiti vituo vilivyopo.
- Tazama maelezo ya kila kituo: uwezo, salio za ndani/mbali, hali, historia ya biashara, alama ya salio, n.k.



#### 2. Miamala



![Historique des transactions Lightning (onglet "Transactions" > "Payments")](assets/fr/08.webp)



Katika menyu ndogo hii, unaweza:




- Tuma malipo ya umeme (kupitia Invoice).
- generate na udhibiti ankara za kupokea malipo.
- Tazama historia kamili ya malipo yaliyotumwa na kupokewa, pamoja na maelezo (kiasi, tarehe, hali, gharama, idadi ya kurukwa, n.k.).



#### 3. Kuelekeza



Menyu ndogo hii inaonyesha:




- Malipo yanayoendeshwa na nodi yako kwa watumiaji wengine wa Lightning Network.
- Takwimu za uelekezaji: idadi ya miamala iliyotumwa, ada zilizopatikana, hitilafu zilizojitokeza.
- Historia inayoweza kuhamishwa kwa uchanganuzi wa hali ya juu.



#### 4. Kuahirishwa



Menyu ndogo hii inatoa:




- Ripoti za kina juu ya shughuli ya nodi yako ya Umeme.
- Chati na majedwali kwenye chaneli, malipo, ada, uwezo n.k.
- Zana za kuelewa vyema utendaji wa nodi yako.



#### 5. Kutafuta Grafu



Menyu ndogo hii hukuruhusu:




- Chunguza topolojia ya Lightning Network.
- Tafuta nodi au vituo maalum.
- Pata habari juu ya muunganisho na uwezo wa jumla wa mtandao.



#### 6. Saini/Thibitisha



Menyu ndogo hii inatoa:




- Uwezo wa kusaini ujumbe kwa ufunguo wa nodi yako (uthibitisho wa Ownership).
- Uthibitishaji wa saini ili kuthibitisha ujumbe kutoka nodi nyingine.



#### 7. Hifadhi nakala



Menyu ndogo hii imejitolea kuhifadhi nakala:




- Hamisha faili ya chelezo ya kituo (SCB kwa LND).
- Rejesha usanidi au chaneli ikiwa ni lazima.
- Vidokezo vya kulinda nakala zako.



#### 8. Node/Mtandao



![Vue d'ensemble du nœud Lightning (onglet "Node/Network")](assets/fr/09.webp)



Katika submenu hii utapata:




- Muhtasari kamili wa hali ya nodi yako ya Umeme: lakabu, toleo, rangi, hali ya ulandanishi.
- Takwimu kwenye chaneli (zinazotumika, zinazosubiri, zimefungwa), jumla ya uwezo, muunganisho.
- Taarifa kuhusu Lightning Network ya kimataifa na nafasi ya nodi yako ndani yake.



### Huduma: Mabadiliko ya Boltz



![Interface de gestion des swaps avec Boltz (onglet "Services" > "Boltz")](assets/fr/10.webp)



Boltz ni huduma ya faragha, isiyo ya ulinzi ya Exchange ambayo inabadilisha bitcoins kati ya Lightning Network na Blockchain Bitcoin (On-Chain). Inatoa aina mbili za operesheni: Badilisha Ubadilishanaji wa Nyambizi (**Swap Out**) na Ubadilishanaji wa Nyambizi (**Swap In**).



#### Badilisha (Ubadilishanaji wa Nyambizi ya Nyuma)



Badilisha hubadilisha Satss inayopatikana kwenye Lightning Network hadi bitcoins za On-Chain. Utaratibu huu ni muhimu wakati nodi inapoishiwa na uwezo unaoingia, au unapotaka kurejesha fedha kutoka kwa On-Chain Address. Mchakato huo unafanya kazi kama ifuatavyo:




- Mtumiaji huchagua kiasi cha kubadilishana
- Nodi hutuma malipo ya Umeme kwa Boltz
- Katika Exchange, Boltz huzuia kiasi sawa katika bitcoins za On-Chain
- Baada ya muamala kuthibitishwa, mtumiaji anaweza kudai pesa kwa kufichua siri iliyotumika katika kubadilishana



Mchakato huu hauzuiliwi, huku Boltz akiwa hashiki pesa za mtumiaji.


![Double capture des étapes de configuration d'un swap-out](assets/fr/11.webp)



#### Badilisha (Ubadilishanaji wa Nyambizi)



Swap In, kwa upande mwingine, inaruhusu fedha za On-Chain kurejeshwa kwenye Lightning Network. Hii ni muhimu sana kwa kurejesha uwezo wa kutoa matokeo kwenye chaneli zako. Utaratibu ni kama ufuatao:




- Mtumiaji hutuma bitcoins kwa Address maalum inayozalishwa na Boltz
- Fedha hizi zinaweza tu kutolewa na Boltz ikiwa atalipa Umeme Invoice inayozalishwa na nodi ya mtumiaji.
- Mara baada ya Invoice kulipwa, fedha zinapatikana kwenye chaneli ya Umeme, na kuongeza uwezo wa pato la nodi.



![Configuration d'un swap-in](assets/fr/12.webp)



Taratibu hizi mbili huwezesha ukwasi wa chaneli ya Umeme kudhibitiwa kwa ufanisi, huku kikidumisha mamlaka ya mtumiaji juu ya fedha zake.



### Usanidi na ubinafsishaji



![Écran de configuration du nœud (onglet "Node Config")](assets/fr/13.webp)



Kichupo cha **Usanidi wa Nodi** hukuwezesha kubinafsisha matumizi yako:




- Uwezeshaji wa vituo ambavyo havijatangazwa
- Badilisha onyesho la mauzo kukufaa
- Mpangilio wa Block explorer
- Kurekebisha Interface



### Nyaraka na usaidizi



![Section d'aide de RTL (onglet "Help")](assets/fr/14.webp)



Hatimaye, sehemu ya **Msaada** inatoa hati za kina kuhusu:




- Usanidi wa awali
- Usimamizi wa rika na kituo
- Malipo na miamala
- Hifadhi nakala na kurejesha
- Ripoti na takwimu
- Sahihi na uthibitishaji
- Node na vigezo vya maombi



Interface hii ya kina hukuruhusu kudhibiti eneo lako la Umeme kwa njia ifaayo, kuanzia utendakazi wa kimsingi hadi vipengele vya juu, vyote katika Interface angavu, iliyopangwa vyema.



## 5. Kesi za utumiaji wa hali ya juu na usalama



Katika sehemu hii, haya ndio unayohitaji kujua ili kwenda mbali zaidi na RTL na kulinda nodi yako ya Umeme:



### Ufuatiliaji na utatuzi wa shida



Ili kufuatilia nodi yako, unaweza kuhamisha data ya RTL (kumbukumbu, CSV) na kuzitazama katika zana kama vile Grafana. Kukitokea tatizo (malipo yaliyozuiwa, kituo kisichotumika), wasiliana na kumbukumbu za LND/CLN na utumie amri za uchunguzi (`lncli listchannels`, `lncli pendingchannels`, n.k.). RTL pia hutoa kumbukumbu za Interface kwa ufuatiliaji wa matukio ya uelekezaji.



### Salama ufikiaji wa mbali



Usiwahi kufichua RTL moja kwa moja kwenye Mtandao. Toa upendeleo kwa:




- **VPN** (k.m. Tailscale) kwa ufikiaji wa faragha, uliosimbwa
- **Tor** kwa ufikiaji salama, usiojulikana
- **Badilisha HTTPS ya seva mbadala** (Nginx/Caddy) ikiwa tu unajua jinsi ya kuisanidi



https://planb.network/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Mazoea mazuri ya usalama





- **Linda ufikiaji wako**: usishiriki kamwe admin.macaroon au nenosiri lako la RTL. Weka kikomo ruhusa kwenye faili nyeti.
- **Hifadhi rudufu za mara kwa mara**: hamisha faili ya chelezo ya kituo (SCB) baada ya kila urekebishaji na uihifadhi nje ya nodi.
- **Masasisho**: sasisha RTL, nodi yako na Umbrel na masahihisho mapya zaidi ya usalama.
- **Usiri**: ficha kumbukumbu na picha za skrini kabla ya kuzishiriki. Kamwe usishiriki salio lako au orodha za wenzako hadharani.
- **Ufikiaji mmoja**: RTL sio watumiaji wengi. Usishiriki ufikiaji wa msimamizi. Kwa ufikiaji wa kusoma tu, tumia macaroon maalum ikiwa ni lazima.



Kwa kutumia kanuni hizi, unapunguza kwa kiasi kikubwa hatari na kuhifadhi udhibiti wa nodi yako ya Umeme.



## 7. Hitimisho



**Ride The Lightning** ni zana muhimu ya kudhibiti vyema eneo la Bitcoin/Lightning, iwe wewe ni mwanzilishi au mtumiaji wa hali ya juu. Inatoa Interface ya wazi ya kudhibiti chaneli zako, malipo na afya ya nodi, huku ikikuza uelewa wako wa Lightning Network.



RTL inajitokeza kwa upatanifu wake wa utekelezaji mwingi, utendakazi wake wa hali ya juu (kusawazisha upya, kubadilishana, ripoti) na mbinu yake ya ufundishaji. Kwa mahitaji rahisi, Mwavuli wa Interface au simu ya mkononi ya Wallet itatosha, lakini RTL ina mantiki kamili kwa usimamizi amilifu, ulioboreshwa wa nodi.



Ili kujua zaidi:




- Tovuti rasmi ya RTL: https://www.ridethelightning.info/
- GitHub RTL: https://github.com/Ride-The-Lightning/RTL
- Reddit r/lightningnetwork**: [r/lightningnetwork](https://www.reddit.com/r/lightningnetwork) - Majadiliano ya kiufundi, matangazo ya mradi, maoni na rasilimali za elimu
- Jukwaa la Jumuiya ya Umbrel**: [community.getumbrel.com](https://community.getumbrel.com) - Jukwaa rasmi lenye sehemu maalum ya Bitcoin/Lightning, miongozo na masuluhisho ya matatizo ya kawaida
- Wasanidi wa Lightning Network**: [github.com/lightning](https://github.com/lightning) - Hazina Rasmi ya GitHub kwa kufuata usanidi na kuchangia msimbo wa chanzo
- Stack Exchange Bitcoin** : [Bitcoin.stackexchange.com](https://Bitcoin.stackexchange.com) - Maswali na Majibu ya Kiufundi pamoja na wasanidi programu na watumiaji wa hali ya juu



Kwa kifupi, RTL hukupa udhibiti kamili wa nodi yako ya Umeme, katika Interface ya kisasa, yenye sifa kamili.



**Vyanzo :** Tovuti rasmi ya RTL; RTL GitHub; Hifadhi ya Programu ya Umbrel; Jumuiya ya Umbrel; Mpango B Rasilimali za Mtandao.



Ili kuongeza uelewa wako wa jinsi Lightning Network inavyofanya kazi, ninapendekeza pia uchukue kozi hii isiyolipishwa:



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
