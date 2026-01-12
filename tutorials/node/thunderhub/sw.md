---
name: ThunderHub
description: Interface Mtandao wa usimamizi wa nodi za umeme LND
---
![cover](assets/cover.webp)



## Utangulizi



ThunderHub ni **kidhibiti chanzo huria cha nodi za Radi (LND)**, inayotoa Interface angavu inayoweza kufikiwa kutoka kwa kifaa au kivinjari chochote.



**Sifa kuu:**




- **Ufuatiliaji**: Mtazamo wa kimataifa wa salio, chaneli, miamala, takwimu za uelekezaji
- **Usimamizi**: Fungua/funga chaneli, malipo yanayoingia/yanayotoka, kusawazisha chaneli
- **Miunganisho**: Usaidizi wa LNURL, hubadilishana kupitia Boltz, chelezo ya Amboss
- **Interface inayoitikia**: Inaoana na vifaa vya mkononi, kompyuta ya mkononi na kompyuta ya mezani vilivyo na mandhari meusi/nyepesi



ThunderHub inaunganishwa kwa urahisi na **Mwavuli**, **Voltage**, **RaspiBlitz** na **MyNode**, ikirahisisha usimamizi wa kila siku wa nodi yako.



**ThunderHub inafaa hasa kwa waendeshaji wanaotafuta Interface ergonomic ili kudhibiti chaneli zao, kudhibiti ukwasi (kusawazisha upya)**, kufuatilia miamala na kuunganisha huduma za watu wengine kama vile Amboss. Usalama umehakikishwa kupitia muunganisho wa ndani au Tor.



Ikiwa bado huna nodi ya Umeme, tunapendekeza ufuate mafunzo yetu ya LND Umbrel:



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Ufungaji



ThunderHub inaweza kusakinishwa kwa njia tofauti, kulingana na mazingira yako ya upangishaji wa nodi ya Umeme. Ikiwa unatumia suluhisho la turnkey (Umbrel, Voltage, RaspiBlitz, MyNode, Start9, nk.) au usakinishaji wa mwongozo, ThunderHub inapatikana mara nyingi bila juhudi kubwa. Hapo chini, tunaelezea mbinu mbili za kawaida: kupitia Hifadhi ya Programu ya Umbrel, na kupitia usakinishaji wa mwongozo (unaotumika kwa seva au usambazaji wa kibinafsi).



### Ufungaji kupitia Umbrel



Mwavuli huunganisha ThunderHub kwenye **Duka la Programu**, na kufanya usakinishaji kuwa rahisi sana. Hakuna haja ya mstari wa amri au usanidi wa mwongozo: kila kitu kinafanywa kupitia Interface Umbrel. Fuata tu hatua hizi:





- **Fungua dashibodi ya Umbrel**: Unganisha kwenye wavuti ya Interface ya nodi yako ya Umbrel (k.m. `http://umbrel.local` kwenye mtandao wako wa karibu, au kupitia `.onion` yake Address ikiwa unatumia Tor).
- **Fikia Duka la Programu**: Katika menyu kuu ya Umbrel, bofya "Duka la Programu" (au "Programu"). Tafuta **ThunderHub** katika orodha ya programu zinazopatikana.



![Écran d'installation de ThunderHub via Umbrel](assets/fr/01.webp)





- **Sakinisha ThunderHub**: Bofya kwenye programu ya ThunderHub, kisha kwenye kitufe cha kusakinisha. Thibitisha ikiwa ni lazima. Umbrel itapakua kiotomatiki na kupeleka ThunderHub kwenye nodi yako.





- **Fungua programu**: Mara usakinishaji utakapokamilika (makumi kadhaa ya sekunde), ThunderHub inaonekana kwenye ukurasa wako wa nyumbani. Bofya kwenye ikoni ili kuifungua. ThunderHub inazinduliwa kwenye kivinjari chako.



![Identifiants par défaut pour ThunderHub](assets/fr/02.webp)



**Muhimu:** ThunderHub inapofunguliwa mara ya kwanza, huonyesha kiotomatiki **nenosiri chaguomsingi** linalohitajika ili kuingia. Chaguo la "Usionyeshe hili tena" hukuwezesha kuficha onyesho hili kwa miunganisho ya siku zijazo. **Tunakushauri sana:**




- **Hifadhi nenosiri hili mara moja** katika kidhibiti chako cha nenosiri
- **Nakili** kwa matumizi katika hatua inayofuata
- **Angalia** "Usionyeshe hii tena" mara tu nenosiri limehifadhiwa



![Page de connexion de ThunderHub](assets/fr/03.webp)



Kisha utachukuliwa kwenye ukurasa wa kuingia, ambapo lazima uweke nenosiri ulilonakili katika hatua ya awali ili kufungua Interface.



![Interface de connexion complète à ThunderHub](assets/fr/04.webp)



Umbrel hutunza kutoa ThunderHub na maelezo ya muunganisho wa LND (cheti cha TLS, macaroon ya usimamizi, n.k.) chinichini, kwa hivyo huhitaji kufanya usanidi wowote wa ziada. Kwa kubofya mara chache tu, utakuwa na ThunderHub juu na kufanya kazi kwenye nodi yako ya Umbrel.



### Ufungaji wa mwongozo (mwenyeji wa kujitegemea, ukiondoa Umbrel)



Kwa watumiaji walio nje ya Umbrel (k.m. kwenye seva ya kibinafsi, Raspberry Pi iliyo na RaspiBlitz au usakinishaji wa *kusimama pekee*), usakinishaji wa ThunderHub unahitaji hatua chache za ziada. Hapa chini tunaelezea usakinishaji kutoka chanzo na usanidi, kulingana na [hati rasmi ya ThunderHub](https://docs.thunderhub.io).



#### Ufungaji



**Masharti:** Hakikisha kuwa mfumo wako unatimiza mahitaji ya chini kabisa kulingana na [usanidi wa hati](https://docs.thunderhub.io/setup):




- **Node.js** toleo la 18 au la juu zaidi
- **npm** imewekwa
- Ufikiaji wa faili za uthibitishaji za LND :
  - Cheti cha LND TLS (`tls.cert`)
  - LND macaroon ya utawala (`admin.macaroon`)
  - Huduma ya LND gRPC Address (jina la mpangishaji: bandari) (chaguo-msingi `127.0.0.1:10009` ndani ya nchi)



**1. Rejesha msimbo wa ThunderHub:** Weka hazina ya GitHub ya mradi kama ilivyofafanuliwa katika [hati za usakinishaji](https://docs.thunderhub.io/installation):



```bash
git clone https://github.com/apotdevin/thunderhub.git
cd thunderhub
```



**2. sasisha utegemezi na ujenge programu:**



```bash
npm install
npm run build
```



Amri hizi husakinisha moduli zote zinazohitajika na kisha kukusanya programu (ThunderHub imeandikwa katika TypeScript/React).



**3. Sasisha baadaye:** ThunderHub inatoa mbinu kadhaa kwa masasisho yajayo:



```bash
# Méthode rapide
npm run update

# Ou méthode manuelle
git pull
npm install
npm run build
```



#### Usanidi (Mipangilio)



**1. Faili kuu ya usanidi:** Unda faili ya `.env.local` kwenye mzizi wa folda ya ThunderHub ili kubinafsisha usanidi (hii itazuia mipangilio yako kufutwa wakati wa masasisho). Vigezo kuu kulingana na [hati za usanidi](https://docs.thunderhub.io/setup):



```bash
# -----------
# Server Configs
# -----------
LOG_LEVEL='info' # 'error' | 'warn' | 'info' | 'http' | 'verbose' | 'debug' | 'silly'
PORT=3000
NODE_ENV=production

# -----------
# Interface Configs
# -----------
THEME='dark' # 'dark' | 'light' | 'night'
CURRENCY='sat' # 'sat' | 'btc' | 'fiat'

# -----------
# Privacy Configs
# -----------
FETCH_PRICES=true # Récupération des prix BTC/fiat depuis Blockchain.com
FETCH_FEES=true # Récupération des frais on-chain depuis Earn.com
DISABLE_LINKS=false # Liens vers 1ml.com et Blockchain.com
NO_VERSION_CHECK=false # Vérification de version depuis GitHub

# -----------
# TOR (optionnel)
# -----------
TOR_PROXY_SERVER='socks://127.0.0.1:9050' # Pour proxifier via TOR

# -----------
# Account Configs
# -----------
ACCOUNT_CONFIG_PATH='/chemin/vers/thubConfig.yaml' # Fichier de comptes
```



**2. Usanidi wa Akaunti za Seva:** Unda faili ya YAML iliyobainishwa katika `ACCOUNT_CONFIG_PATH` :



```yaml
masterPassword: 'votre_mot_de_passe_principal'
accounts:
- name: 'Mon Nœud LND'
serverUrl: '127.0.0.1:10009'
macaroonPath: '/home/user/.lnd/data/chain/bitcoin/mainnet/admin.macaroon'
certificatePath: '/home/user/.lnd/tls.cert'
password: 'mot_de_passe_compte_specifique'
# Optionnel : compte avec macaroon en hexadécimal
- name: 'Nœud Distant'
serverUrl: 'ip.distante:10009'
macaroon: '0201056c6e6402f8...' # Macaroon en HEX ou Base64
certificate: '0202045c7365...' # Certificat en HEX ou Base64
```



**3. Ufikiaji wa Mbali:** Ili kuunganisha kwa nodi ya mbali ya LND, ongeza kwenye `LND.conf` :



```bash
# Option 1 : accès par IP
tlsextraip=<ip-externe-accessible>
rpclisten=0.0.0.0:10009

# Option 2 : accès par domaine
tlsextradomain=<domaine-externe-accessible>
rpclisten=0.0.0.0:10009
```



**4. Usalama:** Inapowasha mara ya kwanza, ThunderHub **otomatiki** huficha `masterPassword` na manenosiri yote ya akaunti katika faili ya YAML, ili kuepuka kuwa na manenosiri katika maandishi wazi kwenye seva.



**5. Anzisha ThunderHub:**



```bash
npm start
```



Kwa chaguo-msingi, seva husikiliza kwenye lango 3000. Fikia `http://localhost:3000` (au `http://ip-serveur:3000` kutoka kwa mtandao wa ndani).



**6. Mbadala wa Docker:** ThunderHub hutoa picha rasmi za Docker:



```bash
# Image standard
docker pull apotdevin/thunderhub:latest
docker run --rm -it -p 3000:3000/tcp apotdevin/thunderhub:latest

# Image avec base path /thub
docker pull apotdevin/thunderhub:base-v0.11.1
```



Ukurasa wa kuingia kwa ThunderHub unaonekana. Chagua akaunti iliyosanidiwa na ingiza nenosiri ili kufikia dashibodi.



**Usakinishaji kwenye usambaaji mwingine:** Usambazaji wa nodi zilizopakiwa mapema (RaspiBlitz, MyNode, Start9, n.k.) kwa ujumla hutoa usaidizi asilia wa ThunderHub kupitia violesura vyao vya usimamizi.



**Kwa habari zaidi:** Angalia hati rasmi kamili :




- **Usakinishaji:** [docs.thunderhub.io/installation](https://docs.thunderhub.io/installation)
- **Usanidi:** [docs.thunderhub.io/setup](https://docs.thunderhub.io/setup)



Nyenzo hizi kwa undani zaidi chaguo za kina kama vile akaunti za SSO, macaroons zilizosimbwa kwa njia fiche, usanidi wa TOR na mengi zaidi.



Mara tu ThunderHub itakaposakinishwa na kufikiwa, uko tayari kutumia vipengele vyake vyote. Katika sehemu ifuatayo, tutaangalia Interface ThunderHub na vichupo vyake mbalimbali, ili kukuongoza katika matumizi yake.



## wasilisho la Interface



Interface ThunderHub imeundwa kuzunguka menyu kuu (kawaida huonyeshwa kwenye safu wima ya upande wa kushoto) inayojumuisha sehemu muhimu kadhaa. Kila moja inalingana na kipengele cha kudhibiti nodi yako ya Umeme. Wacha tupitie moja baada ya nyingine:





- **Nyumbani** - Kichupo cha Nyumbani chenye dashibodi ya jumla (muhtasari wa nodi yako na vitendo vya haraka).
- **Dashibodi** - Dashibodi inayoweza kubinafsishwa yenye wijeti na vipimo vya hali ya juu.
- **Wenzake** - Udhibiti wa rika wa umeme (viunganisho kwa nodi zingine).
- **Vituo** - Udhibiti wa kina wa chaneli za Umeme.
- **Usawazishaji** - Chombo cha kusawazisha chaneli (malipo ya mduara).
- **Shughuli** - Historia ya malipo ya umeme (shughuli za LN).
- **Wasambazaji** - Takwimu za uelekezaji (malipo yanayotumwa na nodi yako).
- **Mlolongo** - kwingineko ya On-Chain ya Node (On-Chain BTC: UTXOs, shughuli).
- **Amboss** - Ushirikiano na Amboss (ufuatiliaji wa nodi, chelezo, nk).
- **Zana** - Zana Nyingine (chelezo, ujumbe uliotiwa sahihi, macaroons, ripoti, n.k.).
- **Badili** - On-Chain/vitendaji vya kubadilisha umeme kupitia Boltz.
- **Takwimu** - Takwimu za kina na vipimo vya utendaji wa nodi.



*(Kumbuka: Kulingana na toleo la ThunderHub, baadhi ya sehemu zinaweza kuwa na vichwa tofauti kidogo au vipengele vya ziada, lakini kanuni za jumla zinasalia zile zile)*



### Nyumbani (Jopo la udhibiti wa jumla)



Kichupo cha **Nyumbani** cha ThunderHub ni ukurasa wa nyumbani unaoonekana baada ya kuingia. Ina **Dashibodi ya Jumla**, ambayo inatoa **muhtasari wa kimataifa** wa hali ya eneo lako la Umeme na kupendekeza **hatua za haraka** kwa shughuli za kawaida. Hivi ndivyo utapata kwa kawaida:



![Tableau de bord principal de ThunderHub](assets/fr/05.webp)





- **Salio na uwezo:** Katika sehemu ya juu ya ukurasa, ThunderHub huonyesha salio lako linalopatikana. Hapa kwa kawaida utaona salio la On-Chain (Bitcoin On-Chain katika nodi ya Wallet, inayoashiriwa na Anchor ⚓) na salio la Radi (uwezo wa mikondo yako, inayoashiriwa na Bolt ⚡). Hii inakupa wazo la haraka la pesa ulizo nazo katika On-Chain na Umeme. Iwapo una akaunti au vituo kadhaa, hakikisha kuwa uko kwenye njia sahihi (k.m. Mainnet vs Testnet).





- **Takwimu muhimu:** Dashibodi inaweza kuonyesha baadhi ya vipimo vya kimataifa vya nodi yako - kwa mfano, idadi ya vituo vilivyofunguliwa, idadi ya programu zingine zilizounganishwa, ada za uelekezaji zilizopatikana (ikiwa zinatumika), n.k. Ni muhtasari wa shughuli na afya ya hivi majuzi ya nodi.





- **Vitendo vya Haraka:** Dashibodi ina vitufe vya kutekeleza kwa haraka kazi zinazojulikana zaidi, bila kulazimika kupitia menyu. Hatua hizi za haraka ni pamoja na:





  - **Ghost**: Sanidi Umeme maalum wa Address kupitia Amboss.
  - **Changia**: Toa mchango kupitia Umeme.
  - **Ingia/Nenda kwa**: Unganisha kwenye akaunti yako ya Amboss (Unganisha Haraka) na uende moja kwa moja kwa Amboss.space ili kuona maelezo ya nodi yako.
  - **Address** : Weka Address ya umeme ili kufanya malipo.
  - **Fungua**: Fungua chaneli mpya ya Umeme. Kubofya kunafungua fomu ya kuingiza URI ya nodi ya mbali ambayo itafungua chaneli, kiasi na, ikiwezekana, ada ya juu zaidi ya On-Chain itatumika.
  - **Simbua**: Simbua Umeme Invoice au LNURL ili kuona maelezo kabla ya malipo.
  - **LNURL**: Mchakato wa LNURL kwa malipo ya umeme au uondoaji.
  - **Kuingia kwa LnMarkets**: Ingia kwa LnMarkets kwa biashara.



Vitendo hivi vya haraka hukuruhusu kufanya shughuli za mara kwa mara moja kwa moja kutoka kwa ukurasa wa nyumbani, bila kulazimika kupitia tabo mbalimbali za Interface.



Kwa kifupi, dashibodi ya ThunderHub hukupa **mwonekano wa haraka** kwenye nodi yako na hukuruhusu kufanya shughuli za mara kwa mara (tuma/pokea, fungua kituo) kwa mbofyo mmoja. Ni mahali pazuri pa kuanzia kwa utawala wa kila siku.



### Dashibodi



Sehemu ya **Dashibodi** ni tofauti na kichupo cha Nyumbani na inatoa dashibodi ya hali ya juu zaidi, inayoweza kugeuzwa kukufaa. Sehemu hii hukuruhusu kuunda mwonekano uliobinafsishwa na wijeti maalum kulingana na mahitaji yako kama opereta wa nodi.





- **Wijeti zinazoweza kugeuzwa kukufaa:** Tofauti na ukurasa wa Nyumbani, ambao una mpangilio usiobadilika, Dashibodi hukuruhusu kuchagua ni Elements ipi hasa ya kuonyesha na jinsi ya kuzipanga.



![Dashboard sans widgets activés](assets/fr/06.webp)



Ikiwa hakuna wijeti zimewezeshwa, utaona "Hakuna Wijeti Imewezeshwa!" ujumbe na kitufe cha "Mipangilio" ili kufikia vigezo vya ubinafsishaji.



![Paramètres des widgets du Dashboard](assets/fr/07.webp)



Katika mipangilio, unaweza kuchagua kutoka kwa wijeti mbalimbali zilizopangwa katika makundi: "Umeme - Maelezo", "Umeme - Jedwali", "Umeme - Grafu", na kadhalika. Kila wijeti inaweza kuwashwa kibinafsi au kuzimwa kwa vitufe vya "Onyesha/Ficha".



![Bas de la page des paramètres](assets/fr/08.webp)



Katika sehemu ya chini ya mipangilio, utapata kitufe cha "Kwa Dashibodi" ili kurudi kwenye dashibodi na kitufe cha "Rudisha Wijeti" ili kuweka upya onyesho chaguomsingi.



![Dashboard personnalisé avec widgets](assets/fr/09.webp)



Baada ya kusanidiwa, dashibodi yako inaweza kuonyesha grafu na vipimo mbalimbali: Grafu za malipo ya umeme, idadi ya ankara zilizotolewa, takwimu za mbele, salio la kina, n.k.





- **Vipimo vya hali ya juu:** Fikia takwimu za kina zaidi za utendakazi wa nodi yako, kwa kutumia grafu na data ya wakati halisi.





- **Muhtasari unaoweza kusanidiwa:** Tengeneza onyesho likufae kama wewe ni mtumiaji wa kawaida au opereta mtaalamu anayedhibiti chaneli nyingi za kuelekeza.





- **Interface ya kawaida:** Ongeza au uondoe wijeti inavyohitajika: chati za mbele, vipimo vya ukwasi, arifa za afya za nodi, n.k.



Sehemu hii ni muhimu sana kwa watumiaji wa hali ya juu wanaotaka kufuatilia vipimo mahususi au kupata muhtasari wa kiufundi zaidi wa nodi zao za Umeme. Inakamilisha sehemu ya Mwanzo kwa kutoa unyumbulifu zaidi na udhibiti wa jinsi maelezo yanavyoonyeshwa.



### Wenzake



Sehemu ya **Rika** huorodhesha sehemu zote za Mwangaza ambazo kwa sasa zimeunganishwa na zako kama programu zingine. **rika** ni muunganisho wa moja kwa moja wa nodi hadi nodi kwenye Lightning Network. Nodi yako inaweza kuunganishwa kwa wenzao hata bila chaneli iliyo wazi (kwa mfano, tu kwa taarifa za uvumi za Exchange kwenye mtandao), au bila shaka kila chaneli iliyo wazi inaashiria kiotomatiki rika lililounganishwa.



![Vue de l'onglet Peers avec les pairs connectés](assets/fr/10.webp)



Katika kichupo cha Rika, utaona:





- **Safu wima za taarifa:** Interface inaonyesha maelezo muhimu kama vile hali ya ulandanishi, aina ya muunganisho (clearnet au Tor), ping, satoshis zilizopokelewa/kutumwa na kiasi cha data iliyobadilishwa.
- **Ongeza programu rika:** ThunderHub hukuruhusu kuunganishwa na mwenzi mwingine mwenyewe kupitia kitufe cha **"Ongeza "** katika kona ya juu kulia. Utahitaji kuingiza URI ya nodi (umbizo `<public_key>@<socket>`). Baada ya kuthibitishwa, ThunderHub hutuma amri inayolingana ya `lncli connect`. Ikiwa nodi iko mtandaoni na inapatikana, itaongezwa kwenye orodha ya wenzako.



### Vituo



Kichupo cha **Vituo** ndicho kiini cha usimamizi wa chaneli ya Umeme. Pengine ni sehemu ambayo utashauriana mara kwa mara. Inawasilisha **vituo vyako vyote vya Umeme** na maelezo yake, na hukuruhusu kutekeleza vitendo vya usimamizi kwenye vituo hivi.



![Vue d'ensemble des channels ouverts](assets/fr/11.webp)



Hivi ndivyo utakavyopata kwenye ukurasa wa Vituo:





- **Mwonekano wa orodha ya idhaa:** Kila chaneli iliyofunguliwa (au inayofungua/kufunga) imeorodheshwa, kwa kawaida na lakabu ya nodi ya mbali, jumla ya uwezo wa kituo, na upau wa rangi unaoonyesha usambazaji wa ukwasi wa ndani dhidi ya kijijini. ThunderHub hutumia msimbo wa rangi (mara nyingi bluu/Green) au asilimia ili kuonyesha salio la kituo: kwa mfano, bluu kwa sehemu yako ya ndani, Green kwa sehemu ya mbali. Ikiwa kituo kina usawa (50/50), bar itakuwa nusu ya kila rangi. Hii hukuruhusu kutambua mara moja ni njia zipi hazina usawa (zote za bluu = karibu zote za ndani, zote Green = karibu zote za mbali).





- **Safu wima za taarifa:** Interface inaonyesha safu wima za kina ikijumuisha Hali, Vitendo Vinavyopatikana, Maelezo ya Rika, Kitambulisho cha Kituo, Uwezo, Shughuli, Ada na Salio zenye onyesho la mchoro la ukwasi.





- **Usanidi wa onyesho:** Gurudumu la gombo katika kona ya juu kulia hukuruhusu kubinafsisha onyesho la kituo ili kukidhi mapendeleo yako.





- **Hali:** Pia utaona viashirio vya hali - k.m. `Inatumika` (kituo kimefunguliwa na kinafanya kazi), `Nje ya Mtandao` (kishirika kimetenganishwa, kwa hivyo chaneli haiwezi kutumika kwa muda), `Inasubiri` (kwa fursa au kufungwa kunangoja uthibitisho wa On-Chain).





- **Vitendo kwenye kituo:** Kwa kila kituo, ThunderHub hutoa vitufe vya kutenda (mara nyingi katika mfumo wa aikoni):



![Actions de gestion des canaux - Modifier et Fermer](assets/fr/12.webp)





  - **Ada za kubadilisha:** "Sera ya Kusasisha Kituo" ya Interface hukuwezesha kurekebisha vigezo vyote vya kituo: Ada ya Msingi, Kiwango cha Ada (katika ppm), CLTV Delta, Max HTLC na Min HTLC. Hii hukuruhusu kurekebisha sera zako za ada kibinafsi kwa kila kituo, kwa lengo la kuvutia (au kukatisha tamaa) trafiki ya uelekezaji. *(Kumbuka: ThunderHub si mbadala wa zana ya kiotomatiki ya kudhibiti ada, lakini kwa urekebishaji wa mikono ni mzuri sana)*
  - **Funga Kituo (*Funga*)**: "Mkondo wa Kufunga" wa Interface hukupa chaguo kati ya **kufunga kwa ushirika** (chaguo-msingi) au **kufunga kwa lazima** (*Lazimisha Kufunga*) kwa kufafanua gharama (katika Sats/vByte). **Muhimu:** kila mara hupendelea ushirika wa karibu inapowezekana, ili kuepuka ucheleweshaji wa makazi wa On-Chain na ada za juu. ThunderHub itakuambia ikiwa mwenzi huyo yuko mtandaoni (ushirikiano unawezekana) au la. Katika tukio la kufungwa kwa nguvu, hakikisha umethibitisha kwa kuwa hii haiwezi kutenduliwa na itaanzisha muamala mkubwa kwa kufunga saa (kwa ujumla vitalu 144 au ~ siku 1 kwenye Bitcoin Mainnet).
  - **Fungua kituo kipya:** Ili kufungua chaneli mpya, bofya kwenye cogwheel iliyo upande wa juu kulia wa ukurasa wa Vituo, kisha uchague "Fungua". Kisha unaweza kuanzisha kituo kwa programu rika mpya au iliyopo. Faida ya kutumia ukurasa huu ni kwamba una orodha ya chaneli zako zilizopo mbele yako, ambayo inaweza kukusaidia kuamua mahali pa kufungua kituo kipya.



Kwa kifupi, sehemu ya Vituo hukupa **udhibiti mzuri wa kila kituo**. Hapa ndipo unapoendesha mgao wa ukwasi, amua ni njia zipi za kuweka au kufunga, na kuweka vigezo vya uelekezaji wa kila kituo. ThunderHub inatoa Interface wazi kwa shughuli hizi muhimu za usimamizi wa nodi.



### Usawazishaji



Kichupo cha **Rebalance** kimejitolea kwa **kusawazisha kituo**. Kusawazisha (au *kusawazisha upya*) kunahusisha kurekebisha mgawanyo wa fedha kati ya chaneli zako zinazotoka na zinazoingia, kwa kufanya **malipo ya mduara** kutoka kwa mojawapo ya vituo vyako hadi vingine vya vituo vyako, kupitia Lightning Network. Hii hukuruhusu, bila kuleta pesa mpya, kuhamisha ukwasi kutoka kwa chaneli iliyojaa kupita kiasi hadi kwa ambayo haina chochote, na kufanya vituo vyako kuwa muhimu zaidi (kituo kilichosawazishwa kinaweza kutuma na kupokea malipo).



![Interface de rebalance des canaux](assets/fr/13.webp)



ThunderHub inawezesha sana operesheni hii, ambayo ingekuwa ya kuchosha kwenye safu ya amri. Hapa kuna jinsi ya kutumia sehemu ya Usawazishaji:





- **Mwonekano wa awali wa kituo:** Unapoingiza Usawazishaji, ThunderHub huonyesha orodha ya chaneli zako, ikiwa na kiashirio cha usawa kwa kila moja (sawa na ile iliyo kwenye ukurasa wa Vituo). Unaweza kuona mara moja ni njia zipi ambazo hazijasawazishwa. ThunderHub inaweza kupanga chaneli ili kuongeza usawa, ili chaneli zisizo na usawa zitokee juu ya orodha (0.0 ikimaanisha ya ndani au ya mbali kabisa).





- **Uchaguzi wa rika:** Interface hurahisisha kuchagua wenzao wanaotoka na wanaoingia ili kusawazisha upya.





- **Mipangilio ya kigezo:** Unaweza kuweka :
  - **ada ya juu zaidi** (katika Sats na ppm) ambayo uko tayari kulipa
  - **kiasi cha kusawazisha** na chaguo la "Zisizohamishika" au "Lengo".
  - **Nodi za kuepuka** wakati wa kuelekeza
  - **Muda wa juu zaidi wa majaribio** wa kutafuta njia





- Chagua **chanzo chaneli**: Kwanza chagua **kituo (chanzo)** kinachotoka, yaani, kituo ambacho una ukwasi mwingi wa ndani wa kuhamisha. Kwa vitendo, hiki ni chaneli ambapo hisa yako ya karibu ni ya juu (> 50%). Wacha tufikirie chaneli A iliyo na Satss 1,000,000, 900,000 ambazo ni za ndani - mgombea mzuri wa kutuma Satss mahali pengine. Kwa kubofya kituo hiki A kama "kinachotoka", ThunderHub inakiweka alama kama chanzo.





- Chagua **kituo lengwa**: Kisha, chagua chaneli **inayoingia (lengwa)** ambayo inahitaji kupokea ukwasi. Kwa kawaida, hii itakuwa njia ambayo ni kinyume chake - pesa nyingi ziko upande wa mbali (k.m. Satss 100,000 pekee kati ya 1,000,000). ThunderHub, mara baada ya kituo cha chanzo kuchaguliwa, itapanga vituo vingine kwa mpangilio wa nyuma (kupungua kwa salio) ili kusaidia kutambua chaneli zinazosaidiana zaidi. Chagua kituo B ambacho kina nafasi upande wa karibu. Kisha ThunderHub itaonyesha kwa uwazi ni njia gani mbili zimechaguliwa (chanzo A na lengwa B).





- **Weka kiasi cha ada na uvumilivu:** Fomu hukuruhusu kuingiza :





  - **kiasi** cha kusawazishwa upya (katika Sats). Mara nyingi, tunachagua kiasi sawa na kile ambacho kingesawazisha chaneli zote mbili kwa \~50/50. ThunderHub inaweza kujaza nusu ya uwezo wa ziada wa chaneli ya chanzo, kwa mfano.
  - **ada ya juu zaidi** ambayo uko tayari kulipa kwa operesheni hii (si lazima). Ada hii inaonyeshwa katika Sats (gharama ya jumla ya uelekezaji wa mzunguko). Ukiiacha wazi, ThunderHub itatafuta njia bila kujali gharama, ambayo kwa ujumla haifai (ni bora kuweka kikomo, k.m. 10 Sats kwa usawazishaji mdogo, au upeo wa juu wa ppm).





- **Tafuta Njia:** Bofya kitufe ili kupata njia. ThunderHub inaulizia LND ili kukokotoa njia kutoka kwa chanzo cha chanzo kupitia mtandao hadi kwenye kituo chako unacholenga. Ikipata njia inayowezekana ambayo inakidhi vigezo vya ada yako, huionyesha ikiwa na maelezo ya humle na gharama ya ada. Kwa mfano, inaweza kuonyesha kuwa imepata njia ya 3-hop yenye jumla ya 2 Sats katika malipo.





- **Anza kusawazisha:** Iwapo umefurahishwa na njia inayopendekezwa, bofya kwenye **Mkondo wa Salio**. Kisha ThunderHub itaanzisha malipo ya mduara kupitia LND. Malipo yakifanikiwa, utaona arifa ya kufaulu, na salio A na B zitarekebishwa kwa wakati halisi. ThunderHub itasasisha kiashirio cha usawa cha chaneli hizi (ikiwezekana zitakuwa kijani kibichi zaidi kuliko hapo awali, ikionyesha usawa bora).





- **Marekebisho na marudio:** Ikiwa hakuna njia inayopatikana kwenye jaribio la kwanza (au ikiwa ni ghali sana), unaweza kurekebisha vigezo :





  - Jaribu kiasi kidogo (wakati mwingine usawa wa sehemu hupitia wakati kiasi kikubwa kinashindwa).
  - Ongeza ada ya juu hatua kwa hatua, lakini kuwa mwangalifu usilipe ada zaidi kuliko inavyostahili.
  - Tumia kitufe cha **Pata Njia Nyingine**, ikiwa inapatikana, ili kujaribu njia mbadala.
  - Jaribu jozi nyingine ya chaneli ikiwa mambo yanata.



ThunderHub hufanya mchakato kuwa **angavu na wa kuona** sana. Katika hatua 4 tu (chagua chaneli inayotoka, chagua chaneli inayoingia, kiasi, dhibitisha), unaweza kufanya kile kilichotumika kuhitaji amri ngumu za mwongozo. Zana hii ni muhimu sana kwa kudumisha hali iliyosawazishwa vizuri, kuboresha utendakazi wako wa uelekezaji na matumizi (rahisi kutuma na kupokea malipo kwenye vituo vyako vyote).



Mwishowe, kumbuka kuwa salio linatumia gharama za uelekezaji (zinazolipwa kwa nodi za kati), kwa hivyo ni **uwekezaji** kufanya nodi yako iwe maji zaidi. Itumie kwa busara, kwa mfano kusaidia kituo kwa huduma unayotumia mara kwa mara (ukwasi unaoingia) au kusawazisha chaneli kubwa ya kuelekeza. ThunderHub hukuruhusu kufanya hivi **kwa urahisi na kwa ufanisi**.



### Shughuli



Sehemu ya **Miamala** katika ThunderHub inalingana na historia ya miamala ya nodi ya **Lightning**, yaani, malipo na ankara zinazolipwa au kupokewa kupitia vituo. Ni aina ya taarifa ya akaunti kwa ajili ya shughuli zako za LN.



![Historique des transactions Lightning](assets/fr/14.webp)



Katika tabo hii utapata:





- **Grafu ya Invoice:** Katika kona ya juu upande wa kulia, grafu inaonyesha mabadiliko ya ankara zilizopokelewa kwa muda, hivyo kukuruhusu kuibua shughuli za nodi yako.





- Orodha ya mpangilio wa miamala yote ya Umeme iliyofanywa *kutoka* au *kwenda* nodi yako. Kila kiingilio kinaweza kuonyesha:





  - Aina ya operesheni: **malipo yaliyotumwa** (malipo yanayotoka) au **malipo yaliyopokelewa** (yanayoingia, kupitia Invoice inayolipiwa).
  - Kiasi cha Sats.
  - Tarehe/saa.
  - Kitambulisho cha Malipo (Hash au picha ya awali ya RHash) au toa maoni (ikiwa umeongeza memo kwenye Invoice).
  - Hali: **imekamilishwa**, au ikiwezekana **inaendelea**/*imeshindwa* (k.m. malipo yanayosubiri kusuluhishwa, lakini kwa ujumla LND huchakata hili haraka, kwa hivyo kuna "inasubiri" kidogo hapa ikilinganishwa na miamala ya On-Chain).



Kwa kifupi, sehemu ya Miamala hutumika kama kumbukumbu ya shughuli ya **LN**. Ni muhimu sana kwa kuangalia kama malipo yamefanyika, ni ada ngapi, au kufuatilia historia ya ubadilishaji wako wa umeme. Kwa kushirikiana na sehemu ya Forwards (iliyoelezewa ijayo), utakuwa na mtazamo kamili wa pesa ambazo zimepitia nodi yako.



### Washambuliaji



Kichupo cha **Wasambazaji** kimejitolea kwa shughuli za **kuelekeza** kwenye nodi yako, yaani, malipo ambayo **yanapitia** kupitia vituo vyako (unapofanya kazi kama nodi ya kati kwenye Lightning Network). Ikiwa utatumia nodi yako kama nodi ya kuelekeza, hii ni sehemu muhimu ya kufuatilia utendaji wako.



![Statistiques de routage Lightning](assets/fr/15.webp)



Katika Forwards, ThunderHub inatoa:





- **Vichujio na chaguo za kuonyesha:** Katika sehemu ya juu kulia, vichujio hukuruhusu kupanga data kwa siku/wiki/mwezi/mwaka, na uchague kati ya onyesho la mchoro au la jedwali.





- **Ujumbe wa shughuli:** Ikiwa hakuna uelekezaji umefanywa katika kipindi kilichochaguliwa, Interface itaonyesha "Hakuna mbele kwa kipindi hiki", kama inavyoonyeshwa katika mfano huu.





- **Jedwali la washambuliaji wa hivi majuzi**: kila ingizo linalingana na malipo ambayo **yametumwa** kupitia nodi yako. Kwa kila mbele, kwa ujumla tunaona:





  - Timestamp,
  - kiasi kilichopitishwa (katika Sats),
  - **ada iliyopatikana** kwa msambazaji huyu (katika Sats, hii ndiyo tofauti kati ya ulichopokea kwenye chaneli inayoingia na kutuma kwa kinachotoka),
  - njia zinazoingia na zinazotoka zinazotumiwa (mara nyingi hutambuliwa na lakabu rika au kitambulisho cha kituo).
  - hali (kawaida *imekamilishwa*, au kutofaulu ikiwa usambazaji wa mbele haukufaulu kwenye njia).





- **Takwimu zilizojumlishwa**: ThunderHub hukokotoa na kuonyeshwa juu ya jumla ya ukurasa na takwimu katika kipindi fulani (k.m. saa 24 zilizopita, au siku 7, n.k., wakati mwingine zinaweza kusanidiwa).



Kwa kifupi, sehemu ya Mbele inatoa **muhtasari wa wakati halisi wa shughuli za uelekezaji za nodi yako ya Umeme**. Sambamba na sehemu za Vituo na Usawazishaji, hii inaunda kifurushi kamili cha kuboresha nodi yako: Vituo/ Usawa upya kwa ukwasi, Usambazaji kwa kuangalia matokeo (mitiririko na faida).



### Mnyororo



Sehemu ya **Chain** inalingana na usimamizi wa kwingineko wa Bitcoin On-Chain wa nodi yako ya LND. Interface hii hukuruhusu kutazama na kudhibiti fedha za Bitcoin, ambazo hutumika kufungua vituo au kupokea pesa kutoka kwa vituo vilivyofungwa.



![Gestion du portefeuille on-chain](assets/fr/16.webp)



Katika Chain, utapata:





- **Salio On-Chain :** Huonyesha jumla ya salio la BTC linalopatikana katika Wallet LND.





- **Orodha ya UTXO:** Tazama matokeo yote ambayo hayajatumika (UTXO) yenye kiasi, uthibitisho, Address na umbizo la kila towe.





- **Historia ya muamala:** Jedwali la kina la miamala yote ya Bitcoin yenye aina ya (kuingia/kutoka), tarehe, kiasi, gharama, uthibitisho, kizuizi cha kujumuishwa, anwani na txid.



### Amboss



ThunderHub inaunganishwa na jukwaa la **Amboss** (amboss.space), ambalo hutoa maelezo ya kina kuhusu sehemu za Umeme, soko la ukwasi, na vipengele muhimu kama vile hifadhi rudufu ya njia iliyosimbwa kwa njia fiche na ufuatiliaji wa upatikanaji.



![Intégration Amboss avec ses options](assets/fr/17.webp)



Katika ThunderHub, sehemu ya Amboss hukuruhusu **kuunganisha** nodi yako kwa akaunti yako ya Amboss:





- **Ghost Address:** Sanidi **Umeme uliobinafsishwa wa Address** kwa nodi yako, kuwezesha malipo yanayokuja.





- **Hifadhi rudufu za kiotomatiki:** Kipengele kinachoangazia kwa chelezo zilizosimbwa kwa njia fiche **(faili za SCB)** kwenye Amboss. Washa **Hifadhi Nakala Kiotomatiki ya Amboss = Ndiyo** katika mipangilio ili kutuma kiotomatiki masasisho ya nakala rudufu yaliyosimbwa kwa njia fiche kila unapobadilisha chaneli. Ikitokea kushindwa, utaweza kurejesha pesa zako kutokana na hifadhi hii ya nje.





- **Ukaguzi wa Afya:** Washa **Amboss Healthcheck = Ndiyo** ili nodi yako itume pings za kawaida kwa Amboss. Utapokea arifa ikiwa nodi yako itaonekana kuwa nje ya mtandao.





- **Vipengele vingine:** Kushinikiza kusawazisha kiotomatiki, muunganisho wa **Magma/Hydro** (soko la ukwasi), na ufikiaji wa takwimu za kina za utendakazi.



Ujumuishaji wa Amboss huongeza **usalama Layer** muhimu iliyo na nakala kiotomatiki ya nje na ufuatiliaji wa upatikanaji, unaoweza kufikiwa moja kwa moja kutoka ThunderHub.



### Zana



Sehemu ya **Zana** hukusanya pamoja zana mbalimbali za kina za kudhibiti nodi yako. Hapa kuna Elements kuu:



![Interface des outils disponibles](assets/fr/18.webp)





- **Hifadhi rudufu:** Dhibiti wewe mwenyewe hifadhi rudufu za kituo chako (SCB). ThunderHub hukuruhusu **kupakua faili kamili ya chelezo** ya vituo vyako (chaguo "Hifadhi nakala za vituo vyote -> Pakua"). Weka faili hii ya `channel-all.bak` mahali salama - ni muhimu ili kurejesha pesa zako iwapo kutatokea ajali. Unaweza pia **kuagiza** faili chelezo wakati wa kupeleka upya nodi.





- **Uhasibu:** Zana ya kuuza nje ya ripoti za fedha ikiwa ni pamoja na ada zinazopatikana/kulipwa na kiasi kilichopitishwa kwa muda fulani.
- **Ujumbe uliotiwa saini:** **Weka au uthibitishe ujumbe** ukitumia nodi yako ili kuthibitisha Ownership ya nodi yako ya Umeme kupitia sahihi ya kriptografia.
- **Makaroni (sehemu ya mkate):** Dhibiti macaroons ya LND ili kuunda ufikiaji uliobinafsishwa. Interface "Bakery" hukuruhusu kuchagua kila ruhusa kwa usahihi: "Ongeza au ondoa Wenzake", "Unda Anwani za Msururu", "Unda Ankara", "Unda Macaroons", "Funguo za Pata", "Pata Vifunguo vya Ufikiaji", "Pata Miamala", "Pata Ankara", "Pata GW-Pat Info" Ankara", "Batilisha Vitambulisho vya Ufikiaji", "Tuma kwa Anwani za Msururu", "Baiti za Saini", "Ujumbe wa Saini", "Acha daemon", "Thibitisha saini ya baiti", "Thibitisha ujumbe", na kadhalika. Kila ruhusa inaweza kuamilishwa kibinafsi kwa vitufe vya "Ndiyo/Hapana" ili kuunda macaroon iliyoundwa maalum.
- **Taarifa ya mfumo:** Onyesho la toleo la Wallet na RPC zilizoamilishwa.



Kwa kifupi, sehemu ya Zana huleta pamoja utendaji wa juu wa usimamizi - chelezo, uhasibu, usalama na usimamizi wa ufikiaji - katika Interface iliyounganishwa.



### Badili



Kichupo cha **Swap** cha ThunderHub hukuwezesha kubadilisha satoshi za Lightning hadi Bitcoin On-Chain kupitia huduma ya Boltz. Kipengele hiki ni muhimu kwa "kutupa" ziada ya ukwasi wa Umeme kwenye chaneli bila kufunga chaneli.



![Interface de swap via Boltz](assets/fr/19.webp)



Mchakato ni rahisi:





- **Kiasi**: Bainisha kiasi kitakachobadilishwa
- **Address** : Ingiza Bitcoin mapokezi Address
- **Utekelezaji**: ThunderHub huwasiliana na Boltz ili kuchakata kiotomatiki Exchange



**Faida:**




- Huduma isiyo ya ulezi (hakuna uhifadhi wa pesa)
- Hifadhi chaneli zako zilizopo
- Rahisi kutumia Interface iliyojumuishwa



Boltz inatoza kamisheni ndogo na unalipa ada ya kawaida ya ununuzi ya Bitcoin. ThunderHub huonyesha gharama zote kabla ya uthibitisho.



### Takwimu



Sehemu ya **Takwimu** ya ThunderHub inatoa **takwimu za kina** kwenye nodi yako ya Umeme ili kuchanganua utendakazi na kuboresha uelekezaji.



![Statistiques du nœud via Amboss](assets/fr/20.webp)



Sehemu hii ni muhimu kwa ajili ya kuboresha gharama zako, kutambua njia zilizofanikiwa na kupanga upanuzi wa nodi yako.



## Hitimisho



**ThunderHub** imejitambulisha kama zana muhimu ya usimamizi rahisi wa nodi ya Umeme **LND**. Interface hii ya kisasa inatoa vipengele vyote muhimu: usimamizi wa kituo, malipo, ufuatiliaji, na vipengele vya juu kama vile kusawazisha upya kiotomatiki na uunganishaji wa Amboss.



**Faida kuu:**




- Interface maridadi na angavu
- Zana zenye nguvu (kusawazisha, kubadilishana kwa Boltz, chelezo otomatiki)
- Inapatana na Umbrel, Voltage, RaspiBlitz na usambazaji mwingine



ThunderHub huweka kidemokrasia usimamizi wa hali ya juu wa nodi ya Umeme, na kufanya kufikiwa kwa kile kilichohitaji amri changamano za kiufundi hapo awali. Iwe wewe ni mwanzilishi au mhudumu mwenye uzoefu, ThunderHub hukuruhusu kudhibiti vyema nodi yako ya Umeme kupitia Interface ya kisasa na ya kina.



## Rasilimali



**Viungo rasmi:**




- **Tovuti rasmi:** [thunderhub.io](https://thunderhub.io)
- **Hati:** [docs.thunderhub.io](https://docs.thunderhub.io)
- **Msimbo wa chanzo wa GitHub:** [github.com/apotdevin/thunderhub](https://github.com/apotdevin/thunderhub)