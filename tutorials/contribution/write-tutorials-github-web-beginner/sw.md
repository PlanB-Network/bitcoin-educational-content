---
name: Mchango - Mafunzo ya Wavuti ya GitHub (mwanzo)
description: Mwongozo kamili wa mafunzo ya Plan ₿ Network na GitHub Web
---
![cover](assets/cover.webp)


Kabla ya kufuata mafunzo haya juu ya kuongeza mafunzo mapya, unahitaji kuwa umekamilisha hatua chache za awali. Ikiwa bado hujafanya hivyo, tafadhali angalia mafunzo haya ya utangulizi kwanza, kisha urudi hapa:


https://planb.network/tutorials/contribution/content/write-tutorials-4d142a6a-9127-4ffb-9e0a-5aba29f169e2

Tayari unayo:




- Chagua mada ya mafunzo yako;
- Iliwasiliana na timu ya Plan ₿ Network kupitia [Telegram group](https://t.me/PlanBNetwork_ContentBuilder) au paolo@planb.network ;
- Chagua zana zako za mchango.


Katika somo hili, tutaangalia jinsi ya kuongeza mafunzo yako kwa Plan ₿ Network kwa kutumia toleo la wavuti la GitHub. Ikiwa tayari umeijua Git, mafunzo haya ya kina yanaweza kuwa sio lazima kwako. Badala yake, ninapendekeza uangalie moja ya mafunzo haya mengine 2, ambapo ninaelezea miongozo ya kufuata na hatua za kufanya mabadiliko kutoka kwa local:




- **Watumiaji wenye uzoefu**:


https://planb.network/tutorials/contribution/content/write-tutorials-git-expert-0ce1e490-c28f-4c51-b7e0-9a6ac9728410


- **Ya kati (Desktop ya GitHub)**:


https://planb.network/tutorials/contribution/content/write-tutorials-github-desktop-intermediate-4a36a052-1000-4191-890a-9a1dc65f8957

## Masharti


Masharti kabla ya kuanza mafunzo:




- Kuwa na [akaunti ya GitHub](https://github.com/signup);
- Kuwa na Fork ya [Plan ₿ Network chanzo hazina](https://github.com/PlanB-Network/Bitcoin-educational-content);
- Kuwa na [wasifu wa mwalimu kwenye Plan ₿ Network](https://planb.network/professors) (ikiwa tu utatoa mafunzo kamili).


Ikiwa unahitaji usaidizi kupata mahitaji haya, mafunzo yangu mengine yatasaidia:



https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c

https://planb.network/tutorials/contribution/others/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba

https://planb.network/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

Mara tu kila kitu kitakapowekwa na unayo Fork yako ya hazina ya Plan ₿ Network, unaweza kuanza kuongeza mafunzo.


## 1 - Unda tawi jipya


Fungua kivinjari chako na uende kwenye ukurasa wako wa Fork kwenye hazina ya Plan ₿ Network. Hii ndiyo Fork uliyoanzisha kwenye GitHub. URL ya Fork yako inapaswa kuonekana hivi: `https://github.com/[your-username]/Bitcoin-educational-content`:


![GITHUB](assets/fr/01.webp)


Hakikisha uko kwenye tawi kuu la `dev`, kisha ubofye kitufe cha "*Sync Fork*". Ikiwa Fork yako haijasasishwa, GitHub itakuuliza usasishe tawi lako. Endelea na sasisho hili:


![GITHUB](assets/fr/02.webp)


Bofya kwenye tawi la `dev`, kisha ulipe tawi lako linalofanya kazi ili jina lake lionyeshe waziwazi madhumuni yake, kwa kutumia vistari kutenganisha maneno. Kwa mfano, ikiwa lengo letu ni kuandika mafunzo kuhusu kutumia Green Wallet, tawi linaweza kuitwa: `tuto-Green-Wallet-loic`. Baada ya kuingiza jina linalofaa, bofya "*Unda tawi*" ili kuthibitisha kuundwa kwa tawi lako jipya kulingana na `dev`:


![GITHUB](assets/fr/03.webp)


Unapaswa sasa kuwa kwenye tawi lako jipya la kazi:


![GITHUB](assets/fr/04.webp)


Hii inamaanisha kuwa mabadiliko yoyote utakayofanya yatahifadhiwa kwenye tawi hilo mahususi pekee.


Kwa kila makala mapya unayopanga kuchapisha, unda tawi jipya kutoka `dev`.


Tawi katika Git linawakilisha toleo sambamba la mradi, hukuruhusu kufanya kazi kwenye marekebisho bila kuathiri tawi kuu, hadi kazi yako iko tayari kuunganishwa.


## 2 - Ongeza faili za mafunzo


Kwa kuwa sasa tawi la kufanya kazi limeundwa, ni wakati wa kuunganisha mafunzo yako mapya.


Ndani ya faili zako za tawi, utahitaji kupata folda ndogo inayofaa kwa uwekaji wa mafunzo yako. Mpangilio wa folda huonyesha sehemu tofauti za tovuti ya Plan ₿ Network. Katika mfano wetu, kwa kuwa tunaongeza mafunzo kwenye Green Wallet, nenda kwa njia ifuatayo: `Bitcoin-maudhui-ya-elimu\tutorials\Wallet` ambayo inalingana na sehemu ya `Wallet` ya tovuti:


![GITHUB](assets/fr/05.webp)


Katika folda ya `Wallet`, unda saraka mpya iliyoundwa mahususi kwa mafunzo yako. Jina la folda hii linapaswa kuonyesha wazi programu iliyofunikwa kwenye mafunzo, kwa kutumia vistari kuunganisha maneno. Kwa mfano wangu, folda itaitwa `Green-Wallet`. Bofya kwenye "*Ongeza Faili*" kisha kwenye "*Unda faili mpya*":


![GITHUB](assets/fr/06.webp)


Ingiza jina la folda na kufyeka `/` ili kuthibitisha uundaji wake kama folda.


![GITHUB](assets/fr/07.webp)


Katika folda hii ndogo iliyotolewa kwa mafunzo yako, unahitaji kuongeza vitu kadhaa:




- Unda folda ya `asethi` ili kushikilia vielelezo vyote vinavyohitajika kwa mafunzo yako;
- Ndani ya folda hii ya `mali`, unda folda ndogo inayoitwa kulingana na msimbo wa lugha asilia wa mafunzo. Kwa mfano, ikiwa mafunzo yameandikwa kwa Kiingereza, folda hii inapaswa kupewa jina `en`. Weka taswira zote za mafunzo (michoro, picha, picha za skrini, n.k.) kwenye folda hii.
- Faili ya `tutorial.yml` lazima iundwe ili kurekodi maelezo ya mafunzo yako;
- Faili ya alama lazima iundwe ili kuandika maudhui halisi ya mafunzo yako. Faili hii lazima ipewe jina kulingana na msimbo wa lugha ambayo imeandikwa. Kwa mfano, kwa mafunzo yaliyoandikwa kwa Kifaransa, faili inapaswa kuitwa `fr.md`.


Kwa muhtasari, hapa kuna safu ya faili (tutaendelea kuziunda katika sehemu inayofuata):


```
bitcoin-educational-content/
└── tutorials/
└── wallet/ (à modifier avec la bonne catégorie)
└── green-wallet/ (à modifier avec le nom du tuto)
├── assets/
│   ├── fr/ (à modifier selon le code de langue approprié)
├── tutorial.yml
└── fr.md (à modifier selon le code de langue approprié)
```


## 3 - Jaza faili ya YAML


Hebu tuanze na faili ya YAML. Katika kisanduku cha kuunda faili mpya, ingiza `tutorial.yml`:


![GITHUB](assets/fr/08.webp)


Jaza faili `tutorial.yml` kwa kunakili kiolezo kifuatacho:


```
id:

project_id:

tags:
-
-
-

category:

level:

professor_id:

# Proofreading metadata

original_language:
proofreading:
- language:
last_contribution_date:
urgency:
contributor_names:
-
reward:
```


Hapa kuna sehemu zinazohitajika:



- **id**: UUID (_Kitambulisho cha Kipekee cha Universally_) ambacho hutambulisha mafunzo kwa njia ya kipekee. Unaweza generate kwa kutumia [zana ya mtandaoni](https://www.uuidgenerator.net/version4). Sharti pekee ni kwamba UUID hii ni ya nasibu ili kuepusha migongano na UUID nyingine kwenye jukwaa;



- **project_id**: UUID ya kampuni au shirika nyuma ya zana iliyowasilishwa kwenye mafunzo [kutoka kwenye orodha ya mradi](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/resources/projects). Kwa mfano, ikiwa unaunda mafunzo kuhusu programu ya Green Wallet, unaweza kupata `project_id` hii katika faili ifuatayo: `Bitcoin-educational-content/resources/projects/blockstream/project.yml`. Maelezo haya yanaongezwa kwenye faili ya mafunzo yako ya YAML kwa sababu Plan ₿ Network ina hifadhidata ya makampuni na mashirika yote yanayofanya kazi kwenye Bitcoin au miradi inayohusiana. Kwa kuongeza `project_id` ya huluki iliyounganishwa kwenye mafunzo yako, unaunda kiungo kati ya Elements mbili;



- **tags**: Maneno muhimu 2 au 3 yanayohusiana na maudhui ya mafunzo, yaliyochaguliwa pekee [kutoka kwa orodha ya lebo za Plan ₿ Network](https://github.com/PlanB-Network/Bitcoin-educational-content/blob/dev/docs/50-planb-tags.md);



- **kategoria**: Kitengo kidogo kinacholingana na maudhui ya mafunzo, kulingana na muundo wa tovuti ya Plan ₿ Network (kwa mfano, kwa pochi: `desktop`, `hardware`, `mobile`, `chelezo`);



- **kiwango**: Kiwango cha ugumu cha mafunzo, kilichochaguliwa kutoka:
    - `Mwanzo`
    - `katikati`
    - `advanced`
    - `mtaalam`



- **professor_id**: `professor_id` (UUID) yako kama inavyoonyeshwa kwenye [wasifu wako wa profesa](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/professors);



- **lugha_asilia**: Lugha asilia ya mafunzo (k.m., `fr`, `en`, n.k.);



- **kusahihisha**: Taarifa kuhusu mchakato wa kusahihisha. Kamilisha sehemu ya kwanza, kwani kusahihisha mafunzo yako mwenyewe kunahesabiwa kama uthibitisho wa kwanza:
    - **lugha**: Msimbo wa lugha wa kusahihisha (k.m., `fr`, `en`, n.k.).
    - **tarehe_ya_mwisho_mchango**: Tarehe ya siku.
    - **dharura**: 1
    - **contributor_names**: Kitambulisho chako cha GitHub.
    - **malipo**: 0


Kwa maelezo zaidi kuhusu kitambulisho chako cha ualimu, tafadhali rejelea mafunzo yanayolingana:


https://planb.network/tutorials/contribution/others/create-teacher-profile-8ba9ba49-8fac-437a-a435-c38eebc8f8a4

```
id: e84edaa9-fb65-48c1-a357-8a5f27996143

project_id: 3b2f45e6-d612-412c-95ba-cf65b49aa5b8

tags:
- wallets
- software
- keys

category: mobile

level: beginner

professor_id: 6516474c-c190-41f2-b2ab-3d452ce7bdf0

# Proofreading metadata

original_language: fr
proofreading:
- language: fr
last_contribution_date: 2024-11-20
urgency: 1
contributor_names:
- LoicPandul
reward: 0
```


Mara tu unapomaliza kurekebisha faili yako ya `tutorial.yml`, hifadhi hati yako kwa kubofya kitufe cha "*Fanya mabadiliko...*":


![GITHUB](assets/fr/09.webp)


Ongeza kichwa na maelezo, na uhakikishe kuwa ahadi imefanywa kwa tawi ulilounda mwanzoni mwa mafunzo haya. Kisha thibitisha kwa kubofya "*Fanya mabadiliko*".


![GITHUB](assets/fr/10.webp)


## 4 - Kuunda folda ndogo za picha


Bonyeza "*Ongeza Faili*" tena kisha kwenye "*Unda faili mpya*":


![GITHUB](assets/fr/11.webp)


Ingiza `mali` ikifuatiwa na kufyeka `/` ili kuunda folda:


![GITHUB](assets/fr/12.webp)


Rudia hatua hii katika folda ya `/assets` ili kuunda folda ndogo ya lugha, kwa mfano `fr` ikiwa somo lako ni la Kifaransa:


![GITHUB](assets/fr/13.webp)


Kwenye folda hii, tengeneza faili ya dummy ili kulazimisha GitHub kuweka folda yako (ambayo ingekuwa tupu). Ipe faili hii jina `.gitkeep`. Kisha bonyeza "*Fanya mabadiliko...*".


![GITHUB](assets/fr/14.webp)


Angalia tena kuwa uko kwenye tawi sahihi, kisha ubofye "*Fanya mabadiliko*".


![GITHUB](assets/fr/15.webp)


## 5 - Kuunda faili ya Markdown


Sasa tutaunda faili ambayo itakuwa mwenyeji wa mafunzo yako, yaliyopewa jina kulingana na msimbo wa lugha yako, kwa mfano `fr.md` ikiwa tunaandika kwa Kifaransa. Nenda kwenye folda yako ya mafunzo:


![GITHUB](assets/fr/16.webp)


Bonyeza "Ongeza faili *", kisha kwenye "Unda faili mpya *".


![GITHUB](assets/fr/17.webp)


Taja faili kwa kutumia msimbo wa lugha yako. Kwa upande wangu, jinsi mafunzo yanavyoandikwa kwa Kifaransa, mimi huita faili yangu `fr.md`. Kiendelezi `.md` kinaonyesha kuwa faili iko katika umbizo la Markdown.


![GITHUB](assets/fr/18.webp)


Tunaanza kwa kujaza sehemu ya `Mali` juu ya hati. Ongeza mwenyewe na ujaze kizuizi kifuatacho cha msimbo (vifunguo vya `jina:` na `maelezo:` lazima vihifadhiwe kwa Kiingereza, lakini thamani zao lazima ziandikwe katika lugha iliyotumiwa kwa mafunzo yako):


```
---
name: [Titre]
description: [Description]
---
```


![GITHUB](assets/fr/19.webp)


Jaza jina la mafunzo yako na maelezo mafupi:


![GITHUB](assets/fr/20.webp)


Kisha ongeza njia ya picha ya jalada mwanzoni mwa mafunzo yako. Ili kufanya hivyo, kumbuka:


```
![cover-green](assets/cover.webp)
```


Sintaksia hii itakusaidia wakati wowote unapohitaji kuongeza picha kwenye mafunzo yako. Alama ya mshangao huonyesha picha, ambayo maandishi yake mbadala (alt) yamebainishwa kati ya mabano ya mraba. Njia ya picha imeonyeshwa kati ya mabano:


![GITHUB](assets/fr/21.webp)


Bofya kitufe cha "*Fanya mabadiliko...*" ili kuhifadhi faili hii.


![GITHUB](assets/fr/22.webp)


Angalia kuwa uko kwenye tawi linalofaa, kisha uthibitishe ahadi hiyo.


![GITHUB](assets/fr/23.webp)


Folda yako ya mafunzo inapaswa sasa kuonekana kama hii, kulingana na nambari yako ya lugha:


![GITHUB](assets/fr/24.webp)


## 6 - Ongeza nembo na kifuniko


Ndani ya folda ya `asethi`, unahitaji kuongeza faili iitwayo `logo.webp`, ambayo itakuwa kama kijipicha cha makala yako. Picha hii lazima iwe katika umbizo la `.webp`, na lazima iwe na ukubwa wa mraba ili ilingane na mtumiaji Interface.


Uko huru kuchagua nembo ya programu iliyotumika kwenye mafunzo, au picha nyingine yoyote inayofaa, mradi tu haina mrahaba. Kwa kuongeza, ongeza picha yenye mada `cover.webp` katika sehemu moja. Hii itaonyeshwa juu ya mafunzo yako. Hakikisha kuwa picha hii, kama nembo, inaheshimu haki za matumizi na inafaa kwa muktadha wa mafunzo yako.


Ili kuongeza picha kwenye folda ya `/assets`, unaweza kuziburuta na kuzidondosha kutoka kwa faili zako za karibu. Hakikisha uko kwenye folda ya `/assets` na kwenye tawi la kulia, kisha ubofye "*Fanya mabadiliko*".


![GITHUB](assets/fr/26.webp)


Unapaswa sasa kuona picha zinaonekana kwenye folda.


![GITHUB](assets/fr/27.webp)


## 7 - Kuandika mafunzo


Endelea kuandika mafunzo yako kwa kubainisha maudhui yako katika faili ya Markdown na msimbo wa lugha (kwa mfano wangu, kwa Kifaransa, ni faili ya `fr.md`). Nenda kwa faili na ubonyeze ikoni ya penseli:


![GITHUB](assets/fr/28.webp)


Anza kuandika mafunzo yako. Unapoongeza manukuu, tumia umbizo la Markdown linalofaa kwa kuweka maandishi kwa `##`:


![GITHUB](assets/fr/29.webp)


Mbadala kati ya mionekano ya "*Hariri*" na "*Onyesha Hakiki*" ili kuibua vyema utoaji.


![GITHUB](assets/fr/30.webp)


Ili kuhifadhi kazi yako, bofya "*Fanya Mabadiliko...*", hakikisha uko kwenye tawi linalofaa, kisha uthibitishe kwa kubofya "*Fanya Mabadiliko*" tena.


![GITHUB](assets/fr/31.webp)


## 8 - Ongeza taswira


Folda ndogo ya lugha katika folda ya `/assets` (katika mfano wangu: `/assets/en`) inatumika kuhifadhi michoro na taswira ambazo zitaambatana na mafunzo yako. Kadiri uwezavyo, epuka kujumuisha maandishi katika picha zako ili kufanya maudhui yako kufikiwa na hadhira ya kimataifa. Bila shaka, programu iliyowasilishwa itakuwa na maandishi, lakini ikiwa unaongeza schematics au dalili za ziada kwenye picha za skrini za programu, fanya hivyo bila maandishi au, ikiwa ni lazima, tumia Kiingereza.


Ili kutaja picha zako, tumia tu nambari zinazolingana na mpangilio wao wa kuonekana kwenye somo, zilizoumbizwa kama tarakimu mbili (au tarakimu tatu ikiwa somo lako lina zaidi ya picha 99). Kwa mfano, taja picha yako ya kwanza `01.webp`, `02.webp` yako ya pili, na kadhalika.


Picha zako lazima ziwe katika umbizo la `.webp` pekee. Ikihitajika, unaweza kutumia [programu yangu ya kubadilisha picha](https://github.com/LoicPandul/ImagesConverter).


![GITHUB](assets/fr/32.webp)


Kwa kuwa sasa umeongeza picha zako kwenye folda ndogo, unaweza kufuta faili dummy `.gitkeep`. Fungua faili hii, bofya kwenye vitone vitatu vidogo kwenye kona ya juu ya mkono wa kulia, kisha kwenye "*Futa faili*".


![GITHUB](assets/fr/33.webp)


Hifadhi mabadiliko yako kwa kubofya "*Fanya mabadiliko...*".


![GITHUB](assets/fr/34.webp)


Ili kuingiza mchoro kutoka kwa folda yako ndogo kwenye hati yako ya uhariri, tumia amri ifuatayo ya Markdown, kwa uangalifu kubainisha maandishi mbadala yanayofaa na njia sahihi ya picha ya lugha yako:


```
![green](assets/fr/01.webp)
```


Alama ya mshangao mwanzoni inaonyesha picha. Maandishi mbadala, ambayo husaidia kwa ufikivu na kurejelea, yanawekwa kati ya mabano ya mraba. Hatimaye, njia ya picha imeonyeshwa kati ya mabano.


![GITHUB](assets/fr/35.webp)


Ikiwa ungependa kuunda michoro yako mwenyewe, hakikisha unafuata miongozo ya picha ya Plan ₿ Network ili kuhakikisha uthabiti wa kuona:




- **Fonti**: Tumia [IBM Plex Sans](https://fonts.google.com/specimen/IBM+Plex+Sans);
- **Rangi**:
 - Chungwa: #FF5C00
 - Nyeusi: #000000
 - Nyeupe: #FFFFFF


**Ni muhimu kwamba taswira zote zilizojumuishwa katika mafunzo yako hazina hakimiliki au ziheshimu leseni ya faili chanzo**. Kwa hiyo, michoro zote zilizochapishwa kwenye Plan ₿ Network zinapatikana chini ya leseni ya CC-BY-SA, kwa njia sawa na maandishi.


**-> Kidokezo:** Unaposhiriki faili hadharani, kama vile picha, ni muhimu kuondoa metadata isiyo ya kawaida. Hii inaweza kuwa na taarifa nyeti, kama vile data ya eneo, tarehe za kuundwa na maelezo ya mwandishi. Ili kulinda faragha yako, ni vyema uondoe metadata hii. Ili kurahisisha utendakazi huu, unaweza kutumia zana maalum kama vile [Exif Cleaner](https://exifcleaner.com/), ambayo hukuwezesha kusafisha metadata ya hati kwa kuburuta na kudondosha rahisi.


## 9 - Pendekeza mafunzo


Mara tu unapomaliza kuandika mafunzo yako katika lugha unayochagua, hatua inayofuata ni kuwasilisha **Ombi la Kuvuta**. Kisha msimamizi ataongeza tafsiri zinazokosekana kwenye mafunzo yako, kwa kutumia mbinu yetu ya kutafsiri kiotomatiki na kusahihisha kibinadamu.


Ili kuendelea na Ombi la Kuvuta, baada ya kuhifadhi mabadiliko yako yote, bofya kitufe cha "*Changia*", kisha kwenye "*Fungua ombi la kuvuta*":


![GITHUB](assets/fr/36.webp)


Ombi la Kuvuta ni ombi linalofanywa ili kujumuisha mabadiliko kutoka kwa tawi lako hadi tawi kuu la hazina ya Plan ₿ Network, ambayo inaruhusu ukaguzi na majadiliano ya mabadiliko kabla ya kuunganishwa.


Kabla ya kuendelea, angalia kwa makini chini ya Interface kwamba mabadiliko haya ndiyo uliyotarajia:


![GITHUB](assets/fr/37.webp)


Hakikisha, katika sehemu ya juu ya Interface, kwamba tawi lako la kazi limeunganishwa kwenye tawi la `dev` la hazina ya Plan ₿ Network (ambalo ndilo tawi kuu).


Weka jina ambalo linatoa muhtasari wa mabadiliko unayotaka kuunganisha na hazina ya chanzo. Ongeza maoni mafupi yanayoelezea mabadiliko haya (ikiwa una nambari ya toleo inayohusishwa na uundaji wa mafunzo yako, kumbuka kukumbuka `Hufunga #{nambari ya toleo}` kama maoni), kisha ubofye kitufe cha Green "*Tengeneza ombi la kuvuta*" ili kuthibitisha ombi la kuunganisha:


![GITHUB](assets/fr/38.webp)


PR yako kisha itaonekana kwenye kichupo cha "*Vuta Ombi*" cha hazina kuu ya Plan ₿ Network. Unachohitajika kufanya sasa ni kusubiri hadi msimamizi awasiliane nawe ili kuthibitisha kuwa mchango wako umeunganishwa, au kuomba marekebisho mengine.


![GITHUB](assets/fr/39.webp)


Baada ya kuunganisha PR yako na tawi kuu, tunapendekeza ufute tawi lako linalofanya kazi (katika mfano wangu: `tuto-Green-Wallet`) ili kudumisha historia safi ya Fork yako. GitHub itakupa chaguo hili kiotomatiki kwenye ukurasa wako wa PR:


![GITHUB](assets/fr/40.webp)


Ikiwa ungependa kufanya mabadiliko kwenye mchango wako baada ya kuwa tayari kuwasilisha PR yako, hatua za kufuata zinategemea hali ya sasa ya PR yako:




- Ikiwa PR yako bado imefunguliwa na bado haijaunganishwa, fanya mabadiliko kwenye tawi la kazi sawa. Mabadiliko ya ahadi yataongezwa kwa PR yako ambayo bado imefunguliwa;
- Katika tukio ambalo PR yako tayari imeunganishwa na tawi kuu, utahitaji kufanya upya mchakato tangu mwanzo kwa kuunda tawi jipya, kisha kuwasilisha PR mpya. Hakikisha Fork yako imelandanishwa na hazina ya chanzo cha Plan ₿ Network kwenye tawi la `dev` kabla ya kuendelea.


Iwapo una matatizo ya kiufundi kuwasilisha mafunzo yako, tafadhali usisite kuomba usaidizi kwenye [kikundi chetu maalum cha Telegram kwa michango](https://t.me/PlanBNetwork_ContentBuilder). Asante sana!
