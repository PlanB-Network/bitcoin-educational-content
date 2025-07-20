---
name: RoninDojo

description: Kusakinisha na kutumia nodi yako ya RoninDojo Bitcoin.
---
***ONYO:** Kufuatia kukamatwa kwa waanzilishi wa Samourai Wallet na kunaswa kwa seva zao mnamo Aprili 24, vipengele fulani vya RoninDojo, kama vile Whirlpool, havifanyi kazi tena. Hata hivyo, kuna uwezekano kwamba zana hizi zinaweza kurejeshwa au kuzinduliwa upya kwa njia tofauti katika wiki zijazo. Zaidi ya hayo, kwa kuwa msimbo wa RoninDojo ulipangishwa kwenye GitLab ya Samourai, ambayo pia ilichukuliwa, kwa sasa haiwezekani kupakua msimbo kwa mbali. Timu za RoninDojo huenda zinashughulikia kuchapisha upya msimbo.*


_Tunafuatilia kwa karibu maendeleo ya kesi hii pamoja na maendeleo kuhusu zana zinazohusiana. Uwe na uhakika kwamba tutasasisha mafunzo haya kadiri habari mpya zinavyopatikana._


_Mafunzo haya yametolewa kwa madhumuni ya elimu na habari pekee. Hatuidhinishi au kuhimiza matumizi ya zana hizi kwa madhumuni ya uhalifu. Ni wajibu wa kila mtumiaji kutii sheria katika eneo la mamlaka yake._


_Mafunzo haya yamejitolea kwa usakinishaji wa RoninDojo v1. Ili kuchukua fursa ya uboreshaji na vipengele vya hivi karibuni, ninapendekeza sana kushauriana na mafunzo yetu yaliyotolewa kwa usakinishaji wa moja kwa moja wa RoninDojo v2 kwenye Raspberry Pi yako:_

https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8

---

Kukimbia na kutumia nodi yako mwenyewe ni muhimu ili kushiriki kikweli katika mtandao wa Bitcoin. Ingawa kuendesha nodi ya Bitcoin hakuleti manufaa yoyote ya kifedha kwa mtumiaji, kunamruhusu kuhifadhi faragha yake, kutenda kwa kujitegemea, na kuwa na udhibiti wa imani yao katika mtandao.


Katika makala hii, tutaangalia kwa kina RoninDojo, suluhisho kubwa la kuendesha node yako ya Bitcoin.


### Jedwali la Yaliyomo:



- RoninDojo ni nini?
- Ni vifaa gani vya kuchagua?
- Jinsi ya kufunga RoninDojo?
- Jinsi ya kutumia RoninDojo?
- Hitimisho


Ikiwa hujui jinsi node ya Bitcoin inavyofanya kazi na jukumu lake, napendekeza kuanza kwa kusoma makala hii: Node ya Bitcoin - Sehemu ya 1/2: Dhana za Kiufundi.


![Samourai](assets/1.webp)


## RoninDojo ni nini?


Dojo ni seva kamili ya nodi ya Bitcoin iliyotengenezwa na timu ya Samourai Wallet. Unaweza kuiweka kwa uhuru kwenye mashine yoyote.


RoninDojo ni msaidizi wa usakinishaji na zana ya usimamizi ya Dojo na zana zingine mbali mbali. RoninDojo inachukua utekelezaji wa awali wa Dojo na kuongeza zana nyingine nyingi kwake, huku pia ikifanya usakinishaji na usimamizi kuwa rahisi.


Pia hutoa maunzi ya "plug-and-play", RoninDojo Tanto, huku RoninDojo ikiwa imesakinishwa awali kwenye mashine iliyounganishwa na timu yao. Tanto ni suluhisho la kulipwa, linafaa kwa wale ambao hawataki kupata mikono yao chafu.


Nambari ya RoninDojo ni chanzo-wazi, kwa hivyo inawezekana pia kusakinisha suluhisho hili kwenye maunzi yako mwenyewe. Chaguo hili ni la gharama nafuu lakini linahitaji udanganyifu zaidi, ambayo ni nini tutafanya katika makala hii.


RoninDojo ni Dojo, kwa hivyo inaruhusu kuunganishwa kwa urahisi kwa Whirlpool CLI kwenye nodi yako ya Bitcoin ili kuwa na matumizi bora zaidi ya CoinJoin. Ukiwa na Whirlpool CLI, si tu kwamba unaweza kuruhusu bitcoins remix yako 24/7 bila kuhitaji kuwasha kompyuta yako ya kibinafsi, lakini pia unaweza kuboresha faragha yako kwa kiasi kikubwa.


RoninDojo huunganisha zana zingine nyingi zinazotegemea Dojo yako, kama vile kikokotoo cha Boltzmann, ambacho huamua kiwango cha faragha cha muamala, seva ya Electrum ili kuunganisha pochi zako tofauti za Bitcoin kwenye nodi yako, au seva ya Mempool ili kuchunguza shughuli zako kwa faragha.

Ikilinganishwa na suluhisho lingine la nodi kama Umbrel, ambayo niliwasilisha kwako katika nakala hii, RoninDojo inalenga sana suluhisho na zana za "on chain" zinazoboresha ufaragha wa mtumiaji. Kwa hiyo, RoninDojo hairuhusu mwingiliano na Lightning Network.

RoninDojo inatoa zana chache ikilinganishwa na Umbrel, lakini vipengele vichache muhimu kwa Bitcoiner aliyepo kwenye Ronin ni thabiti sana.


Kwa hivyo ikiwa huhitaji vipengele vyote vya seva ya Umbrel na unataka tu nodi rahisi na dhabiti yenye zana chache muhimu kama Whirlpool au Mempool, basi RoninDojo labda ni suluhisho zuri kwako.


Kwa maoni yangu, mwelekeo wa ukuzaji wa Umbrel unategemea sana Lightning Network na zana nyingi. Bado ni nodi ya Bitcoin, lakini lengo ni kuifanya iwe seva ndogo ya multitasking. Kinyume chake, mwelekeo wa maendeleo wa RoninDojo unalingana zaidi na timu za Samourai Wallet na inaangazia zana muhimu kwa Bitcoiner, kuruhusu uhuru kamili na usimamizi bora wa faragha kwenye Bitcoin.


Tafadhali kumbuka kuwa kusanidi nodi ya RoninDojo ni ngumu zaidi kuliko nodi ya Umbrel.


Sasa kwa kuwa tumeweza kuchora picha ya RoninDojo, hebu tuone jinsi ya kusanidi nodi hii pamoja.


## Ni vifaa gani vya kuchagua?


Ili kuchagua mashine inayopangisha na kuendesha RoninDojo, una chaguo kadhaa.


Kama ilivyoelezwa hapo awali, chaguo rahisi zaidi ni kuagiza Tanto, mashine ya kuziba-na-kucheza iliyoundwa mahsusi kwa madhumuni haya. Ili kuagiza yako, nenda hapa: [link](https://shop.ronindojo.io/product-category/nodes/).


Kwa kuwa timu za RoninDojo hutoa msimbo wa chanzo huria, inawezekana pia kutekeleza RoninDojo kwenye mashine zingine. Unaweza kupata matoleo mapya zaidi ya kichawi cha usakinishaji kwenye ukurasa huu: [link](https://ronindojo.io/en/downloads.html), na matoleo mapya zaidi ya msimbo kwenye ukurasa huu: [link](https://code.samourai.io/ronindojo/RoninDojo).


Binafsi, niliiweka kwenye Raspberry Pi 4 8GB na kila kitu hufanya kazi kikamilifu.


Hata hivyo, tafadhali kumbuka kuwa timu za RoninDojo zinaonyesha kuwa mara nyingi kuna matatizo na kesi na adapta ya SSD. Kwa hivyo haipendekezi kutumia kesi na kebo kwa SSD ya mashine yako. Badala yake, ni vyema kutumia kadi ya upanuzi wa hifadhi iliyoundwa mahsusi kwa ubao wako wa mama, kama hii: Kadi ya Upanuzi ya Hifadhi ya Raspberry Pi 4.


Hapa kuna mfano wa jinsi ya kusanidi nodi yako ya RoninDojo:



- Raspberry Pi 4.
- Kesi na shabiki.
- Kadi ya upanuzi wa hifadhi inayolingana.
- Kebo ya nguvu.
- Kadi ndogo ya SD ya viwanda ya 16GB au zaidi.
- SSD yenye TB 1 au zaidi.
- Kebo ya Ethaneti ya RJ45, kitengo cha 8 kinapendekezwa.


## Jinsi ya kufunga RoninDojo?


### Hatua ya 1: Tayarisha kadi ndogo ya SD inayoweza kuwashwa.


Mara baada ya kukusanya mashine yako, unaweza kuanza usakinishaji wa RoninDojo. Ili kufanya hivyo, anza kwa kuunda kadi ndogo ya SD ya bootable kwa kuchoma picha sahihi ya diski juu yake.


Ingiza kadi yako ndogo ya SD kwenye kompyuta yako ya kibinafsi, kisha uende kwenye tovuti rasmi ya RoninDojo ili kupakua picha ya diski ya RoninOS: https://ronindojo.io/en/downloads.html.


Pakua picha ya diski inayolingana na maunzi yako. Katika kesi yangu, nilipakua picha ya "MANJARO-ARM-RONINOS-RPI4-22.03.IMG.XZ":


![Download RoninOS disk image](assets/2.webp)


Mara tu picha inapopakuliwa, thibitisha uadilifu wake kwa kutumia faili inayolingana ya .SHA256. Nitaelezea kwa undani jinsi ya kufanya hivyo katika makala hii: Jinsi ya kuthibitisha uadilifu wa programu ya Bitcoin kwenye Windows?


Maagizo mahususi ya kuthibitisha uadilifu wa RoninOS yanapatikana pia kwenye ukurasa huu: https://wiki.ronindojo.io/en/extras/verify.


Ili kuchoma picha hii kwenye kadi yako ndogo ya SD, unaweza kutumia programu kama vile Balena Etcher, ambayo unaweza kuipakua hapa: https://www.balena.io/etcher/.


Ili kufanya hivyo, chagua picha kwenye Etcher na uangaze kwenye kadi ndogo ya SD:


![Burn disk image with Etcher](assets/3.webp)


Operesheni ikishakamilika, unaweza kuingiza kadi ndogo ya SD inayoweza kuwashwa kwenye Raspberry Pi na kuwasha mashine.


### Hatua ya 2: Sanidi RoninOS.


RoninOS ni mfumo wa uendeshaji wa nodi yako ya RoninDojo. Ni toleo lililobadilishwa la Manjaro, usambazaji wa Linux. Baada ya kuanza mashine yako na kusubiri dakika chache, unaweza kuanza usanidi wake.


Ili kuunganisha kwayo kwa mbali, utahitaji kupata IP Address ya mashine yako ya RoninDojo. Ili kufanya hivyo, unaweza, kwa mfano, kuunganisha kwenye paneli ya usimamizi ya kisanduku chako cha intaneti, au unaweza pia kupakua programu kama vile https://angryip.org/ ili kuchanganua mtandao wako wa karibu na kupata IP ya mashine.


Mara tu unapopata IP, unaweza kuchukua udhibiti wa mashine yako kutoka kwa kompyuta nyingine iliyounganishwa kwa mtandao huo wa ndani kwa kutumia SSH.


Kutoka kwa kompyuta inayoendesha macOS au Linux, fungua tu terminal. Kutoka kwa kompyuta inayoendesha Windows, unaweza kutumia zana maalum kama Putty au kutumia Windows PowerShell moja kwa moja.


Mara tu terminal imefunguliwa, chapa amri ifuatayo:

```
ssh root@192.168.?.?
```


Badilisha tu alama mbili za swali na IP ya RoninDojo yako iliyopatikana hapo awali.

Kidokezo: Katika Shell, bofya kulia ili kubandika kipengee.


Kisha, utafika kwenye paneli dhibiti ya Manjaro. Chagua mpangilio sahihi wa kibodi kwa kutumia vishale ili kubadilisha lengo katika orodha kunjuzi.


![Manjaro Keyboard Configuration](assets/4.webp)


Chagua jina la mtumiaji na nenosiri kwa kipindi chako. Tumia nenosiri dhabiti na uhifadhi nakala salama. Unaweza kutumia kwa hiari nenosiri dhaifu wakati wa usakinishaji, na baadaye ubadilishe kwa urahisi kwa "kubandika" kuwa RoninUI. Hii itakuruhusu kutumia nenosiri kali sana bila kutumia muda mwingi kuliandika mwenyewe wakati wa kusanidi Manjaro.


![Manjaro Username Configuration](assets/5.webp)


Ifuatayo, utaulizwa pia kuchagua nenosiri la mizizi. Kwa nenosiri la mizizi, ingiza nenosiri kali moja kwa moja. Hutaweza kuibadilisha kutoka kwa RoninUI. Pia, kumbuka kuweka salama nenosiri hili la msingi.


Kisha ingiza eneo lako na saa za eneo.


![Manjaro Time Zone Configuration](assets/6.webp)


![Manjaro Location Configuration](assets/7.webp)


Ifuatayo, chagua jina la mpangishaji.


![Manjaro Hostname Configuration](assets/8.webp)


Hatimaye, thibitisha maelezo ya usanidi wa Manjaro na uthibitishe.


![Verification of ManjaroOS Configuration Information](assets/9.webp)


### Hatua ya 3: Pakua RoninDojo.


Usanidi wa awali wa RoninOS utafanywa. Mara baada ya kumaliza, kama inavyoonyeshwa kwenye skrini hapo juu, mashine itaanza upya. Subiri kidogo, kisha ingiza amri ifuatayo ili kuunganisha tena kwenye mashine yako ya RoninDojo:

```
ssh username@192.168.?.?
```


Badilisha tu "jina la mtumiaji" na jina la mtumiaji ulilochagua hapo awali, na ubadilishe alama za swali na IP ya RoninDojo yako.


Kisha ingiza nenosiri lako la mtumiaji.


Katika terminal, itaonekana kama hii:


![SSH Connection to RoninOS](assets/10.webp)


Sasa umeunganishwa kwenye mashine yako, ambayo kwa sasa ina RoninOS pekee. Sasa unahitaji kusakinisha RoninDojo juu yake.


Pakua toleo la hivi karibuni la RoninDojo kwa kuingiza amri ifuatayo:

```
git clone https://code.samourai.io/ronindojo/RoninDojo
```


Upakuaji utakuwa haraka. Katika terminal, utaona hii:


![Cloning RoninDojo](assets/11.webp)


Subiri upakuaji ukamilike, kisha usakinishe na ufikie mtumiaji wa RoninDojo Interface kwa kutumia amri ifuatayo:

```
~/RoninDojo/ronin
```


Utaulizwa kuingiza nenosiri lako la mtumiaji:


![Bitcoin Node Password Verification](assets/12.webp)


Amri hii ni muhimu mara ya kwanza tu unapofikia RoninDojo yako. Baadaye, ili kufikia RoninCLI kupitia SSH, utahitaji tu kuingiza amri [SSH username@192.168.?.?] ikibadilisha "jina la mtumiaji" na jina lako la mtumiaji na kuingiza IP Address ya nodi yako. Utaulizwa nenosiri lako la mtumiaji.


Ifuatayo, utaona uhuishaji huu mzuri:


![RoninCLI launch animation](assets/13.webp)


Kisha hatimaye utafika kwa mtumiaji wa RoninDojo CLI Interface.


### Hatua ya 4: Sakinisha RoninDojo.


Kutoka kwa menyu kuu, nenda kwenye menyu ya "Mfumo" kwa kutumia vitufe vya vishale kwenye kibodi yako. Bonyeza kitufe cha Ingiza ili kuthibitisha chaguo lako.


![RoninCLI navigation menu to System](assets/14.webp)


Kisha nenda kwenye menyu ya "Mipangilio ya Mfumo na Usakinishe".


![RoninCLI navigation menu to RoninDojo system installation](assets/15.webp)


Hatimaye, angalia "Mpangilio wa Mfumo" na "Sakinisha RoninDojo" ukitumia upau wa nafasi, kisha uchague "Kubali" ili kuanza usakinishaji.


![RoninDojo installation confirmation](assets/16.webp)


Acha ufungaji uendelee kimya kimya. Kwa upande wangu, ilichukua kama masaa 2. Weka terminal yako wazi wakati wa mchakato.


Mara kwa mara angalia terminal yako, kwani utaulizwa kubonyeza kitufe katika hatua fulani za usakinishaji, kama hapa kwa mfano:


![RoninDojo installation in progress](assets/17.webp)


Mwishoni mwa usakinishaji, utaona vyombo tofauti vinaanza:


![Node container startup](assets/18.webp)


Kisha nodi yako itaanza tena. Unganisha tena kwa RoninCLI kwa hatua inayofuata.


![Bitcoin node restart](assets/19.webp)


### Hatua ya 5: Pakua msururu wa Proof-of-Work na ufikie RoninUI.


Mara tu usakinishaji utakapokamilika, nodi yako itaanza kupakua mnyororo wa Bitcoin Proof-of-Work. Hii inaitwa Upakuaji wa Kizuizi cha Awali (IBD). Kwa kawaida huchukua kati ya siku 2 hadi 14 kulingana na muunganisho wako wa intaneti na kifaa.


Unaweza kufuatilia maendeleo ya upakuaji wa mnyororo kwa kufikia mtandao wa RoninUI Interface.


Ili kuipata kutoka kwa mtandao wa ndani, andika yafuatayo kwenye upau wa Address wa kivinjari chako:



- Ingiza moja kwa moja IP Address ya mashine yako (192.168.?.?)
- Au ingiza: ronindojo.local


Kumbuka kuzima VPN yako ikiwa unatumia moja.


### Iwezekanavyo twist


Ikiwa huwezi kuunganisha kwa RoninUI kutoka kwa kivinjari chako, angalia utendakazi sahihi wa programu kutoka kwa Kituo chako kilichounganishwa kwenye nodi yako kupitia SSH. Unganisha kwenye menyu kuu kwa kufuata hatua zilizopita:



- Aina: Jina la mtumiaji la SSH@192.168.?.? kubadilisha na sifa zako.



- Weka nenosiri lako la mtumiaji.


Mara moja kwenye menyu kuu, nenda kwa: ** RoninUI > Anzisha upya **


Ikiwa programu itaanza upya kwa usahihi, ni tatizo na muunganisho kutoka kwa kivinjari chako. Hakikisha kuwa hutumii VPN na uhakikishe kuwa umeunganishwa kwenye mtandao sawa na nodi yako.


Ikiwa kuanzisha upya hutoa hitilafu, jaribu kusasisha mfumo wa uendeshaji na kisha usakinishe tena RoninUI. Kusasisha Mfumo wa Uendeshaji: **Mfumo > Masasisho ya Programu > Sasisha Mfumo wa Uendeshaji**


Mara tu sasisho na kuanzisha upya kukamilika, unganisha tena kwenye nodi yako kupitia SSH na usakinishe upya RoninUI: **RoninUI > Sakinisha upya**


Baada ya kupakua RoninUI tena, jaribu kuunganisha kwa RoninUI kupitia kivinjari chako.


**Kidokezo:** Ukitoka kwenye RoninCLI kimakosa na ukajipata kwenye terminal ya Manjaro, weka tu amri "ronin" ili kurudi moja kwa moja kwenye menyu kuu ya RoninCLI.


### Ingia kwenye wavuti


Unaweza pia kuingia kwenye mtandao wa RoninUI Interface kutoka kwa mtandao wowote kwa kutumia Tor. Ili kufanya hivyo, rudisha Tor Address ya RoninUI yako kutoka RoninCLI: **Sifa > Ronin UI**


Rejesha Tor Address inayoishia kwa .onion na kisha ingia kwenye Ronin UI kwa kuingiza Address hii kwenye kivinjari chako cha Tor. Kuwa mwangalifu usivujishe sifa zako mbalimbali, kwani ni habari nyeti.


![RoninUI web login interface](assets/20.webp)


Mara tu umeingia, utaulizwa nenosiri lako la mtumiaji. Ni nenosiri lile lile unalotumia kuingia kupitia SSH.


![RoninUI web interface management panel](assets/21.webp)


Tunaweza kuona maendeleo ya IBD (Upakuaji wa Kizuizi cha Awali) hapa. Kuwa mvumilivu, unarejesha miamala yote iliyofanywa kwenye Bitcoin tangu tarehe 3 Januari 2009.


Baada ya kupakua Blockchain nzima, indexer itaunganisha hifadhidata. Operesheni hii inachukua kama masaa 12. Unaweza pia kufuatilia maendeleo yake chini ya "Indexer" kwenye RoninUI.


Nodi yako ya RoninDojo itafanya kazi kikamilifu baada ya hii:


![Indexer synchronized at 100% functional node](assets/22.webp)


Ikiwa unataka kubadilisha nenosiri la mtumiaji kuwa lenye nguvu zaidi, unaweza kufanya hivyo sasa kutoka kwenye kichupo cha "Mipangilio". Kwenye RoninDojo, hakuna usalama wa ziada wa Layer, kwa hivyo ninapendekeza uchague nenosiri thabiti na kutunza nakala yake.


## Jinsi ya kutumia RoninDojo?


Msururu ukishapakuliwa na kuunganishwa, unaweza kuanza kufurahia huduma zinazotolewa na nodi yako mpya ya RoninDojo. Hebu tuone jinsi ya kuzitumia.


### Kuunganisha programu ya Wallet kwa elektroniki.


Huduma ya kwanza ya nodi yako mpya iliyosakinishwa na iliyosawazishwa itakuwa kutangaza miamala yako kwa mtandao wa Bitcoin. Kwa hivyo, kuna uwezekano utataka kuunganisha programu yako tofauti ya usimamizi ya Wallet nayo.


Unaweza kufanya hivyo kwa kutumia Electrum Rust Server (elektroni). Programu kwa kawaida husakinishwa awali kwenye nodi yako ya RoninDojo. Ikiwa sivyo, unaweza kuisanikisha kwa mikono kutoka kwa RoninCLI Interface.


Nenda kwa: **Programu > Dhibiti Programu > Sakinisha Seva ya Electrum**


Ili kupata Tor Address ya Seva yako ya Electrum, kutoka kwa menyu ya RoninCLI, nenda kwa:

**Vitambulisho > Wateule**


Lazima tu uweke kiungo cha .onion kwenye programu yako ya Wallet. Kwa mfano, katika Sparrow Wallet, nenda kwenye kichupo:

**Faili > Mapendeleo > Seva**


Katika aina ya seva, chagua `Electrum ya Kibinafsi`, kisha ingiza Tor Address ya Seva yako ya Electrum katika sehemu inayolingana. Hatimaye, bofya "Jaribio la Muunganisho" ili kujaribu na kuhifadhi muunganisho wako.


![Sparrow Wallet connection interface to an electrs](assets/23.webp)


### Inaunganisha programu ya Wallet kwenye Samourai Dojo.


Badala ya kutumia Electrs, unaweza pia kutumia Samourai Dojo kuunganisha Software Wallet yako inayooana na nodi yako ya RoninDojo. Kwa mfano, Samourai Wallet inatoa chaguo hili.


Ili kufanya hivyo, changanua tu msimbo wa QR wa muunganisho wa Dojo yako. Ili kuipata kutoka kwa RoninUI, bofya kichupo cha "Dashibodi" na kisha kwenye kitufe cha "Dhibiti" kwenye kisanduku cha Dojo yako. Kisha utaweza kuona misimbo ya QR ya muunganisho ya Dojo yako na BTC-RPC Explorer. Ili kuzionyesha, bofya kwenye "Onyesha maadili".


![Retrieving the connection QR code to Dojo](assets/24.webp)


Ili kuunganisha Samourai Wallet yako kwenye Dojo yako, utahitaji kuchanganua msimbo huu wa QR wakati wa kusakinisha programu:


![Connecting to Dojo from the Samourai Wallet application](assets/25.webp)


### Kwa kutumia Mempool Explorer yako mwenyewe.


Chombo muhimu kwa Bitcoiners, mchunguzi hukuruhusu kuangalia habari mbalimbali kuhusu mlolongo wa Bitcoin. Ukiwa na Mempool, kwa mfano, unaweza kuangalia katika muda halisi ada zinazotumika na watumiaji wengine ili kurekebisha yako ipasavyo. Unaweza pia kuangalia hali ya uthibitishaji wa mojawapo ya miamala yako au kuangalia salio la Address.


Zana hizi za wachunguzi zinaweza kukuweka kwenye hatari za faragha na kukuhitaji uamini hifadhidata ya watu wengine. Unapotumia zana hii mkondoni bila kupitia nodi yako mwenyewe:



- Una hatari ya kuvuja taarifa kuhusu Wallet yako.



- Unamwamini msimamizi wa tovuti kwa msururu wa Proof-of-Work wanaopangisha.


Ili kuepuka hatari hizi, unaweza kutumia mfano wako wa Mempool kwenye nodi yako kupitia mtandao wa Tor. Kwa suluhisho hili, sio tu kwamba unahifadhi faragha yako wakati wa kutumia huduma, lakini pia huhitaji tena kumwamini mtoa huduma kwa kuwa unauliza hifadhidata yako mwenyewe.


Ili kufanya hivyo, anza kwa kusakinisha Mempool Space Visualizer kutoka RoninCLI:


**Programu > Dhibiti Programu > Sakinisha Mempool Space Visualizer**


Mara baada ya kusakinishwa, rudisha kiungo kwa Mempool yako. Tor Address itawawezesha kuipata kutoka kwa mtandao wowote. Vile vile, tunapata kiunga hiki kupitia RoninCLI:


**Kitambulisho > Mempool**


![Retrieve Tor Mempool address](assets/26.webp)


Ingiza tu Mempool Tor Address yako kwenye kivinjari cha Tor ili kufurahia mfano wako wa Mempool, kulingana na data yako mwenyewe. Ninapendekeza uongeze Tor Address hii kwa vipendwa vyako kwa ufikiaji wa haraka. Unaweza pia kuunda njia ya mkato kwenye eneo-kazi lako.


![Mempool Space interface](assets/27.webp)


Ikiwa bado huna kivinjari cha Tor, unaweza kuipakua hapa: https://www.torproject.org/download/


Unaweza pia kuipata kutoka kwa smartphone yako kwa kusakinisha Kivinjari cha Tor na kuingiza Address sawa. Ukiwa mahali popote, unaweza kutazama hali ya mnyororo wa Bitcoin ukitumia nodi yako mwenyewe.


### Kwa kutumia Whirlpool CLI.


Nodi yako ya RoninDojo pia inajumuisha WhirlpoolCLI, mstari wa amri wa mbali wa Interface wa kufanyia michanganyiko ya Whirlpool kiotomatiki.


Unapotekeleza CoinJoin na utekelezaji wa Whirlpool, programu unayotumia lazima ibaki wazi ili kutekeleza michanganyiko na michanganyiko. Mchakato huu unaweza kuwa wa kuchosha watumiaji ambao wanataka kuwa na seti nyingi za anon, kwani kifaa kinachopangisha programu kwa Whirlpool lazima kiendelee kuwashwa kila mara. Kwa maneno ya kiutendaji, hii inamaanisha kwamba ikiwa unataka kushirikisha UTXO zako katika michanganyiko ya 24/7, utahitaji kuweka kompyuta yako ya kibinafsi au simu kila mara huku programu ikifunguliwa.


Suluhisho moja la kizuizi hiki ni kutumia WhirlpoolCLI kwenye mashine ambayo inakusudiwa kuwashwa kila wakati, kama vile nodi ya Bitcoin. Kwa hili, UTXO zetu zinaweza kuchanganywa 24/7 bila hitaji la kuweka mashine nyingine isipokuwa nodi yetu ya Bitcoin inayofanya kazi.

WhirlpoolCLI inatumiwa na WhirlpoolGUI, Interface ya picha itakayosakinishwa kwenye kompyuta ya kibinafsi kwa usimamizi rahisi wa Coinjoins. Nitaelezea kwa undani jinsi ya kusanidi Whirlpool CLI na dojo yako mwenyewe katika nakala hii: [kiungo](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin#:~:text=dans%20cette%20p artie.-,Tutoriel%20%3A%20Whirpool%20CLI%20sur%20Dojo%20et%20Whirlpool%20GUI.,-Si%20vous%20souhaitez).


Ili kupata maelezo zaidi kuhusu CoinJoin kwa ujumla, ninaeleza kila kitu katika makala haya: [link](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin).


### Kwa kutumia Whirlpool Stat Tool.


Baada ya kufanya CoinJoins na Whirlpool, unaweza kutaka kujua kiwango halisi cha faragha ya UTXO zako zilizochanganywa. Whirlpool Stat Tool hukuruhusu kufanya hivi kwa urahisi. Ukiwa na zana hii, unaweza kukokotoa alama tarajiwa na alama ya nyuma ya UTXO zako zilizochanganywa. Ili kujifunza zaidi kuhusu kuhesabu Seti hizi za Anon na jinsi zinavyofanya kazi, ninapendekeza usome sehemu hii: [kiungo](https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%rcdeC3%A9%ment%3%A9).


Zana imesakinishwa awali kwenye RoninDojo yako. Kwa sasa, inapatikana tu kutoka kwa RoninCLI. Ili kuizindua kutoka kwa menyu kuu, nenda kwa:

**Zana za Samourai > Zana ya Takwimu ya Whirlpool**


Maagizo ya matumizi yataonekana. Mara baada ya kumaliza, bonyeza kitufe chochote ili kufikia mistari ya amri:


![Whirlpool Stats Tool software home](assets/28.webp)


Terminal itaonyesha:

**wst#/tmp>**


Ili kutoka kwa Interface hii na kurudi kwenye menyu ya RoninCLI, ingiza tu amri:

```
quit
```


Kuanza, tutaweka seva mbadala kwenye Tor ili kutoa data ya OXT kwa faragha kamili. Ingiza amri:

```
socks5 127.0.0.1:9050
```


Kisha pakua data kutoka kwa bwawa ambayo ina shughuli yako:

```
download 0001
```


**Kumbuka:** badilisha `0001` na msimbo wa kundi la madhehebu unaokuvutia.


Nambari za madhehebu ni kama ifuatavyo kwenye WST:



- Dimbwi la bitcoins 0.5: 05
- Dimbwi la bitcoins 0.05: 005
- Dimbwi la bitcoins 0.01: 001
- Dimbwi la bitcoins 0.001: 0001


![Downloading data from pool 0001 from OXT](assets/29.webp)


Mara tu data inapopakuliwa, pakia kwa amri:

```
load 0001
```


**Kumbuka:** badilisha `0001` na msimbo wa kundi la madhehebu unaokuvutia.


![Loading data from pool 0001](assets/30.webp)

Acha mchakato wa upakiaji ufanyike, inaweza kuchukua dakika chache. Baada ya kupakia data, chapa amri ya alama ikifuatiwa na txid yako (kitambulisho cha muamala) ili kupata Anon Sets zake:

```
score TXID
```


**Kumbuka:** badilisha `txid` na kitambulisho cha muamala wako.


![Printing the prospective and retrospective scores of the given TXID](assets/31.webp)


WST kisha itaonyesha alama ya rejea (metriki zinazoonekana Nyuma) ikifuatwa na alama zinazotarajiwa (Vipimo vya kuangalia Mbele). Kando na alama za Anon Sets, WST pia hukupa kiwango cha usambaaji wa pato lako kwenye hifadhi kulingana na seti ya anon.


Tafadhali kumbuka kuwa alama tarajiwa ya UTXO yako inakokotolewa kulingana na txid ya mchanganyiko wako wa awali, si mchanganyiko wako wa mwisho. Kinyume chake, alama ya retrospective ya UTXO inahesabiwa kulingana na txid ya mzunguko wa mwisho.


Kwa mara nyingine tena, ikiwa huelewi dhana hizi za Anon Sets, ninapendekeza kusoma sehemu hii ya makala yangu kwenye CoinJoin ambapo ninaelezea kila kitu kwa undani na michoro: [https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%Ac%deCm%3%3%A9%Ac9%20p% (https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%Ac%CdeC3%20p%Ac9%20p%


### Kwa kutumia kikokotoo cha Boltzmann.


Kikokotoo cha Boltzmann ni chombo kinachokuwezesha kuhesabu kwa urahisi metriki mbalimbali za hali ya juu kwenye muamala wa Bitcoin, ikijumuisha kiwango chake cha entropy. Data hii yote itakuruhusu kukadiria kiwango cha faragha ya muamala na kugundua hitilafu zozote zinazoweza kutokea. Zana hii imesakinishwa awali kwenye nodi yako ya RoninDojo.


Ili kuipata kutoka kwa RoninCLI, unganisha kupitia SSH, kisha uende kwenye menyu:

**Zana za Samourai> Kikokotoo cha Boltzmann**


Kabla ya kueleza jinsi ya kuitumia kwenye RoninDojo, nitaeleza ni nini metriki hizi zinawakilisha, jinsi zinavyokokotolewa, na zinatumika kwa matumizi gani.


Viashiria hivi vinaweza kutumika kwa shughuli yoyote ya Bitcoin, lakini ni ya kuvutia hasa kwa kusoma ubora wa shughuli ya CoinJoin.


1. Kiashiria cha kwanza kilichohesabiwa na programu hii ni idadi ya mchanganyiko iwezekanavyo. Imebainishwa kwenye kikokotoo kama "mchanganyiko wa nb". Kwa kuzingatia maadili ya UTXOs, kiashirio hiki kinawakilisha idadi ya upangaji unaowezekana kutoka kwa pembejeo hadi matokeo.


**kumbuka:** ikiwa hujui neno `UTXO`, ninapendekeza usome nakala hii fupi:


> Utaratibu wa shughuli ya Bitcoin: UTXO, pembejeo, na matokeo.

Kwa maneno mengine, kiashiria hiki kinawakilisha idadi ya tafsiri zinazowezekana kwa shughuli fulani. Kwa mfano, muundo wa Whirlpool 5x5 CoinJoin utakuwa na idadi ya mchanganyiko unaowezekana sawa na 1496:


![Schema of a Coinjoin transaction on kycp.org](assets/32.webp)


Mkopo: KYCP


2. Kiashiria cha pili kilichohesabiwa ni entropy ya shughuli. Kwa kuwa idadi ya michanganyiko inayowezekana inaweza kuwa ya juu sana kwa shughuli, mtu anaweza kuchagua kutumia entropy badala yake. Entropy inawakilisha logarithm ya binary ya idadi ya michanganyiko inayowezekana. Formula yake ni kama ifuatavyo:



- E: entropy ya shughuli.
- C: idadi ya michanganyiko inayowezekana kwa shughuli hiyo.


**E = logi2(C)**


Katika hisabati, logarithm ya binary (msingi 2) ni chaguo la kukokotoa kinyume cha nguvu ya chaguo 2. Kwa maneno mengine, logaritimu ya binary ya x ni nguvu ambayo nambari 2 lazima ipandishwe ili kupata thamani x.


Hivyo:


**E = logi2(C)**


**C = 2^E**


Kiashiria hiki kinaonyeshwa kwa bits. Kwa mfano, hapa kuna hesabu ya entropy ya shughuli ya Whirlpool 5x5 CoinJoin, na idadi iliyotajwa hapo awali ya mchanganyiko unaowezekana sawa na 1496:


**C = 1496**


**E = logi2(1496)**


**E = biti 10.5469**


Kwa hiyo, shughuli hii ya CoinJoin ina entropy ya bits 10.5469, ambayo ni nzuri sana.


Kadiri kiashiria hiki kilivyo juu, ndivyo tafsiri tofauti zaidi za shughuli zilivyo, na kwa hivyo ndivyo shughuli hiyo inavyokuwa ya siri zaidi.


Hebu tuchukue mfano mwingine. Hapa kuna shughuli ya "classic" ambayo ina pembejeo moja na matokeo mawili:


![Bitcoin transaction schema on oxt.me](assets/34.webp)


Mkopo: OXT


Muamala huu una tafsiri moja tu inayowezekana:


**[(inp 0) > (Outp 0 ; Outp 1)]**


Kwa hivyo entropy yake itakuwa sawa na 0:


**C = 1**,

**E = logi2(C)**,

**E = 0**


3. Kiashiria cha tatu kilichorejeshwa na calculator ya Boltzmann ni ufanisi wa Tx inayoitwa "Ufanisi wa Wallet". Kiashiria hiki kinaruhusu tu kulinganisha shughuli ya uingizaji na shughuli bora zaidi katika usanidi sawa.


Sasa tutaanzisha dhana ya entropy ya juu zaidi, ambayo inawakilisha entropy ya juu zaidi inayoweza kufikiwa kwa muundo fulani wa ununuzi. Kwa mfano, muundo wa Whirlpool 5x5 CoinJoin utakuwa na entropy ya juu ya 10.5469. Kiashiria cha ufanisi kinalinganisha entropy hii ya juu na entropy halisi ya shughuli ya uingizaji. Formula yake ni kama ifuatavyo:



- ER: Entropy halisi imeonyeshwa kwa bits.
- EM: Upeo wa entropy na muundo sawa ulioonyeshwa kwa biti.
- Ef: Ufanisi ulioonyeshwa kwa bits.


**Ef = ER - EM**


**Ef = 10.5469 - 10.5469**


**Ef = biti 0**


Kiashiria hiki pia kinaonyeshwa kama asilimia, kwa hivyo formula inakuwa:



- CR: Idadi halisi ya michanganyiko inayowezekana.
- CM: Idadi ya juu zaidi ya michanganyiko inayowezekana na muundo sawa.
- Ef: Ufanisi unaoonyeshwa kama asilimia.


**Ef = CR/CM**


**Ef = 1496/1496**


**Ef = 100%**


Ufanisi wa 100% unamaanisha kuwa shughuli hii ina faragha ya juu kabisa inayowezekana kulingana na muundo wake.


4. Kiashiria cha nne kilichohesabiwa ni wiani wa entropy. Inaturuhusu kuhusisha entropy kwa kila ingizo au pato. Kiashiria hiki kinaweza kutumika kulinganisha ufanisi kati ya shughuli za ukubwa tofauti.


Hesabu yake ni rahisi sana: tunagawanya entropy ya muamala kwa idadi ya pembejeo na matokeo yaliyopo. Kwa mfano, kwa Whirlpool 5x5 CoinJoin, tungekuwa na:


ED: Msongamano wa Entropy umeonyeshwa kwa biti.

E: Entropy ya muamala imeonyeshwa kwa biti.

T: Jumla ya idadi ya pembejeo na matokeo katika muamala.


T = 5 + 5 = 10

ED = E / T

ED = 10.5469 / 10

ED = 1.054 bits


Sehemu ya tano ya taarifa iliyotolewa na kikokotoo cha Boltzmann ni jedwali la uwezekano wa viungo kati ya ingizo na matokeo. Jedwali hili hukupa tu uwezekano (alama ya Boltzmann) kwamba ingizo fulani linalingana na matokeo fulani.


Ikiwa tutachukua mfano wetu na Whirlpool CoinJoin, jedwali la uwezekano litakuwa:


| %       | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |
|---------|----------|----------|----------|----------|----------|
| Input 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 4 | 34%      | 34%      | 34%      | 34%      | 34%      |


Hapa tunaweza kuona kwamba kila pembejeo ina uwezekano sawa wa kuunganishwa kwa kila pato.


Walakini, ikiwa tutachukua mfano wa ununuzi na ingizo moja na matokeo mawili, itaonekana kama hii:


| Input | Output 0 | Output 1 |
| ----- | -------- | -------- |
| 0     | 100%     | 100%     |

Katika mfano huu, tunaweza kuona kwamba uwezekano wa kila pato kutoka kwa pembejeo 0 ni 100%.


Kadiri uwezekano huu unavyopungua, ndivyo kiwango cha usiri kinavyoongezeka.


6. Sehemu ya sita ya habari ambayo imehesabiwa ni idadi ya viungo vya kuamua. Uwiano wa viungo vya kuamua pia utatolewa. Kiashiria hiki huangazia idadi ya viunganishi kati ya pembejeo na matokeo ya shughuli uliyopewa ambayo yana uwezekano wa 100%, kumaanisha kuwa hayawezi kukanushwa.


Uwiano unaonyesha idadi ya viungo vya kuamua katika shughuli ya ununuzi ikilinganishwa na jumla ya idadi ya viungo.


Kwa mfano, muamala wa CoinJoin Whirlpool hauna viungo vya kuamua kati ya pembejeo na matokeo. Kiashiria kitakuwa sifuri na uwiano pia utakuwa 0%.


Hata hivyo, kwa shughuli ya pili iliyojifunza (pembejeo 1 na matokeo 2), kiashiria ni 2 na uwiano ni 100%.


Kwa hiyo, ikiwa kiashiria hiki ni sifuri, kinaonyesha usiri mzuri.


Sasa kwa kuwa tumejifunza viashiria, hebu tuone jinsi ya kuhesabu kwa kutumia programu hii. Kutoka RoninCLI, nenda kwenye menyu:

**Zana za Samourai> Kikokotoo cha Boltzmann**


![Boltzmann Calculator software homepage](assets/35.webp)


Mara tu programu inapozinduliwa, ingiza transaction ID unayotaka kusoma. Unaweza kuingiza shughuli nyingi kwa wakati mmoja kwa kuzitenganisha kwa koma, kisha ubonyeze ingiza:


![Enter a TXID to study on Boltzmann Calculator](assets/36.webp)


Kikokotoo kitarudisha viashiria vyote ambavyo tumeona hapo awali:


![Printing of Boltzmann Calculator data for this TXID](assets/37.webp)


Andika amri "Kuacha" ili kuondoka kwenye programu na kurudi kwenye orodha ya RoninCLI.


Ili kujifunza zaidi juu ya kikokotoo cha Boltzmann, napendekeza kusoma nakala hizi:



- https://medium.com/@laurentmt/introducing-boltzmann-85930984a159



- https://gist.github.com/LaurentMT/e758767ca4038ac40aaf


### Kuunganisha Bisq.


Bisq ni jukwaa la rika-kwa-rika la Exchange linalokuruhusu kununua na kuuza bitcoins. Inatumika na programu ya eneo-kazi inayotumika kwenye Tor na hukuruhusu kutumia bitcoins za Exchange bila kuhitaji kutoa utambulisho wako.

Bisq hulinda ubadilishanaji wa rika-kwa-rika kupitia mfumo wa 2/2 wa saini nyingi. Unaweza kutumia programu hii na nodi yako ya RoninDojo ili kuboresha faragha ya mabadilishano yako na kuamini data kutoka kwa nodi yako ya Blockchain.


Ili kupakua programu ya Bisq, nenda kwa tovuti yao rasmi: https://bisq.network/


Ili kuanza na programu, napendekeza kusoma ukurasa huu: https://bisq.network/getting-started/


Ili kupata kiunga cha muunganisho kutoka kwa RoninDojo yako, utahitaji kuunganisha kwa RoninCLI kupitia SSH. Kisha nenda kwenye menyu:

**Programu > Dhibiti Programu**


Weka nenosiri lako, kisha uteue kisanduku chenye kitufe cha nafasi:

**[ ] Washa Muunganisho wa Bisq**


Thibitisha chaguo lako. Acha nodi yako isanikishe, kisha upate Tor V3 Address kutoka:

**Kitambulisho > bitcoind**


Nakili Address chini ya "Bitcoin daemon".


Unaweza pia kuepua bitcoind Tor V3 Address yako kutoka kwa RoninUI Interface kwa kubofya tu "Dhibiti" katika kisanduku cha "Bitcoin Core" kwenye "Dashibodi":


![Retrieve TorV3 Bitcoin Daemon address on RoninUI](assets/38.webp)


Ili kuunganisha nodi yako kutoka Bisq, nenda kwenye menyu:

**Mipangilio > Maelezo ya Mtandao**


![Access the node connection interface from the Bisq software](assets/39.webp)


Bofya kwenye Bubble "Tumia nodi za Msingi za Bitcoin". Kisha ingiza Bitcoin TorV3 Address yako kwenye kisanduku kilichoteuliwa, na ".onion" lakini bila "http://".


![Box to enter the TorV3 address of your node in the Bisq software](assets/40.webp)


Anzisha tena programu ya Bisq. Nodi yako sasa imeunganishwa kwenye Bisq yako.


### Vipengele vingine.


Nodi yako ya RoninDojo pia inajumuisha vipengele vingine vya msingi. Una uwezo wa kuchanganua maelezo mahususi ili kuhakikisha kuwa yanazingatiwa.


Kwa mfano, wakati mwingine inawezekana kwamba Wallet yako iliyounganishwa na RoninDojo haipati bitcoins ambazo ni zako. Salio ni 0 ingawa una uhakika kuwa una Bitcoin katika Wallet hii. Kuna sababu nyingi zinazowezekana za kuzingatia, pamoja na hitilafu katika njia za utokaji, na kati yao, inawezekana pia kwamba nodi yako haizingatii anwani zako.


Ili kurekebisha hili, unaweza kuangalia kuwa nodi yako inafuatilia xpub yako na "zana ya xpub". Ili kuipata kutoka kwa RoninUI, nenda kwenye menyu:

**Matengenezo > Zana ya XPUB**


Ingiza xpub yenye matatizo na ubofye "Angalia" ili kuthibitisha maelezo haya.


![XPUB Tool from RoninUI](assets/41.webp)


Ikiwa xpub yako inafuatiliwa na nodi, utaona hii ikitokea:


![XPUB Tool result showing successful analysis](assets/42.webp)


Hakikisha kwamba shughuli zote zinaonekana kwa usahihi. Pia, thibitisha kuwa aina ya uasilia inalingana na Wallet yako. Hapa tunaweza kuona kwamba nodi inatafsiri xpub hii kama derivation ya BIP44. Iwapo aina hii ya utokaji hailingani na ile ya Wallet yako, bofya kitufe cha "Chapa upya", kisha uchague BIP44/BIP49/BIP84 kulingana na chaguo lako:


![Change the derivation type of the studied xpub from RoninUI](assets/43.webp)


Ikiwa xpub yako haijafuatiliwa na nodi yako, utaona skrini hii inakualika kuiingiza:


![Import an xpub with XPUB Tool on RoninUI](assets/44.webp)


Unaweza pia kutumia zana zingine za matengenezo:



- Zana ya Muamala: Hukuruhusu kutazama maelezo ya shughuli mahususi.
- Zana ya Address: Hukuruhusu kuthibitisha kuwa Address mahususi inafuatiliwa na Dojo yako.
- Vitalu vya Changanua upya: Hulazimisha nodi yako kuchambua tena safu iliyochaguliwa ya vizuizi.


Utapata pia zana ya "Push Tx" kwenye RoninUI. Inakuruhusu kutangaza shughuli iliyosainiwa kwa mtandao wa Bitcoin. Lazima iingizwe katika umbizo la hexadecimal:


![Tool for broadcasting a signed transaction from RoninUI](assets/45.webp)


## Hitimisho.


Tumeona jinsi ya kusakinisha na kuanza kutumia zana hii nzuri ambayo ni RoninDojo. Ni chaguo bora kwa kuendesha nodi yako ya Bitcoin. Ni suluhisho thabiti linalojumuisha na kusasisha zana zote muhimu kwa Bitcoiner.


Ikiwa kutumia terminal hakuogopi na ikiwa hauitaji zana zinazohusiana na Lightning Network, basi RoninDojo inaweza kukuvutia.


Ukiweza, zingatia kuchangia wasanidi programu wanaokutengenezea programu hizi za programu huria: https://donate.ronindojo.io/


Ili kujifunza zaidi kuhusu RoninDojo, ninapendekeza uangalie viungo kwenye rasilimali zangu za nje hapa chini.


### Kusoma zaidi:



- Kuelewa na kutumia CoinJoin kwenye Bitcoin.
- Vitendaji vya Hash - nukuu kutoka kwa kitabu pepe Bitcoin Démocratisé 1.
- Kila kitu unachohitaji kujua kuhusu Bitcoin passphrase.


### Rasilimali za nje:



- https://ronindojo.io/index.html
- https://wiki.ronindojo.io/en/home
- https://gist.github.com/LaurentMT/e758767ca4038ac40aaf
- https://medium.com/@laurentmt/introducing-boltzmann-85930984a159
- https://en.wikipedia.org/wiki/Boltzmann_formula
- https://wiki.ronindojo.io/en/setup/bisq
- https://bisq.network/