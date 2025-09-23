---
name: RoninDojo v2
description: Kufunga nodi yako ya RoninDojo v2 Bitcoin kwenye Raspberry Pi
---
![cover RoninDojo v2](assets/cover.webp)


**ONYO:** Kufuatia kukamatwa kwa waanzilishi wa Samourai Wallet na kunaswa kwa seva zao mnamo Aprili 24, vipengele fulani vya RoninDojo, kama vile Whirlpool, havifanyi kazi tena. Hata hivyo, kuna uwezekano kwamba zana hizi zinaweza kurejeshwa au kuzinduliwa upya kwa njia tofauti katika wiki zijazo. Zaidi ya hayo, kwa kuwa msimbo wa RoninDojo ulipangishwa kwenye GitLab ya Samourai, ambayo pia ilichukuliwa, kwa sasa haiwezekani kupakua msimbo kwa mbali. Timu za RoninDojo huenda zinashughulikia kuchapisha upya msimbo.*


_Tunafuatilia kwa karibu maendeleo ya kesi hii pamoja na maendeleo kuhusu zana zinazohusiana. Uwe na uhakika kwamba tutasasisha mafunzo haya kadiri habari mpya zinavyopatikana._


_Mafunzo haya yametolewa kwa madhumuni ya elimu na habari pekee. Hatuidhinishi au kuhimiza matumizi ya zana hizi kwa madhumuni ya uhalifu. Ni wajibu wa kila mtumiaji kutii sheria katika eneo la mamlaka yake._


---

> Tumia Bitcoin na faragha.

Katika somo lililopita, tulikuwa tayari tumeelezea utaratibu wa kusakinisha na kutumia RoninDojo v1. Hata hivyo, zaidi ya mwaka jana, timu za RoninDojo zimezindua toleo la 2 la utekelezaji wao, ambalo liliashiria mabadiliko makubwa katika usanifu wa programu. Hakika, walihama kutoka kwa usambazaji wa Linux Manjaro kwa niaba ya Debian. Kwa hivyo, hawatoi tena picha iliyosanidiwa mapema kwa usakinishaji wa kiotomatiki kwenye Raspberry Pi. Lakini bado kuna njia ya kuendelea na ufungaji wa mwongozo. Hili ndilo nililotumia kwa nodi yangu mwenyewe, na tangu wakati huo, RoninDojo v2 imekuwa ikifanya kazi kwa ajabu kwenye Raspberry Pi 4 yangu. Kwa hiyo ninatoa mafunzo mapya kuhusu namna ya kusakinisha RoninDojo v2 kwa Raspberry Pi.

https://planb.network/tutorials/node/bitcoin/ronin-dojo-31d96647-029b-43e8-9fb5-95ec5dde72b0

## Jedwali la Yaliyomo:


- RoninDojo ni nini?
- Ni maunzi gani ya kuchagua kwa kusakinisha RoninDojo v2?
- Jinsi ya kukusanyika Raspberry Pi 4?
- Jinsi ya kufunga RoninDojo v2 kwenye Raspberry Pi 4?
- Jinsi ya kutumia nodi yako ya RoninDojo v2?


## RoninDojo ni nini?

Hapo awali Dojo ni utekelezaji kamili wa nodi za Bitcoin, kulingana na Bitcoin Core, na kuendelezwa na timu za Samourai Wallet. Suluhisho hili linaweza kusanikishwa kwenye kifaa chochote. Tofauti na utekelezaji mwingine wa Core, Dojo imeboreshwa mahususi ili kuunganishwa na mazingira ya utumizi wa Android ya Samourai Wallet. Kuhusu RoninDojo, ni shirika lililoundwa ili kuwezesha usakinishaji na usimamizi wa Dojo, pamoja na zana zingine mbalimbali za ziada. Kwa kifupi, RoninDojo inaboresha utekelezaji wa msingi wa Dojo kwa kuunganisha wingi wa zana za ziada, huku ikirahisisha usakinishaji na usimamizi wake.


Ronin pia hutoa [suluhisho la nodi ndani ya kisanduku, linaloitwa "*Tanto*"](https://ronindojo.io/en/products), kifaa ambacho RoninDojo tayari kimesakinishwa kwenye mfumo uliounganishwa na timu yao. Tanto ni chaguo la kulipwa, ambalo linaweza kuvutia kwa wale wanaopendelea kuepuka matatizo ya kiufundi. Lakini kwa kuwa msimbo wa chanzo wa RoninDojo umefunguliwa, inawezekana pia kuipeleka kwenye vifaa vyako mwenyewe. Hii mbadala, ya kiuchumi zaidi, hata hivyo inahitaji ujanja wa ziada, ambao tutashughulikia katika somo hili.

RoninDojo ni Dojo, kwa hivyo inaruhusu ujumuishaji rahisi wa Whirlpool CLI kwenye nodi yako ya Bitcoin ili kutoa matumizi bora zaidi ya CoinJoin. Ukiwa na Whirlpool CLI, inakuwa rahisi kuendelea kuchanganya bitcoins zako, saa 24 kwa siku, siku 7 kwa wiki, bila kuhitaji kompyuta yako ya kibinafsi iendelee kuwashwa.


Zaidi ya Whirlpool CLI, RoninDojo inajumuisha zana mbalimbali ili kuboresha utendakazi wa Dojo yako. Kati ya hizi, kikokotoo cha Boltzmann huchanganua kiwango cha faragha cha miamala yako, seva ya Electrum inaruhusu uunganisho wa pochi zako za Bitcoin kwenye nodi yako, na seva ya Mempool hukuwezesha kutazama miamala yako ndani ya nchi, bila kuvuja taarifa.


Ikilinganishwa na suluhu zingine za nodi kama Umbrel, RoninDojo inalenga kwa uwazi suluhisho ya On-Chain na zana za faragha. Tofauti na Umbrel, RoninDojo haitumii kusanidi nodi ya Umeme wala ujumuishaji wa programu-tumizi zaidi za seva za jumla. Ingawa RoninDojo inatoa zana chache zinazoweza kutumika kuliko Umbrel, ina vipengele vyote muhimu vya kudhibiti shughuli yako ya On-Chain.


Ikiwa hauitaji utendaji wa kiujumla au zile zinazohusiana na Lightning Network kama inavyotolewa na Umbrel, na unatafuta nodi rahisi, thabiti yenye zana muhimu kama vile Whirlpool au Mempool, RoninDojo inaweza kuwa suluhisho bora. Ingawa Umbrel inaelekea kuwa seva ndogo ya kufanya kazi nyingi zinayoelekezwa kuelekea kwa Lightning Network na matumizi mengi, RoninDojo, kulingana na falsafa ya Samourai Wallet, inazingatia zana za kimsingi za faragha ya mtumiaji.


Sasa kwa kuwa tumeelezea RoninDojo, hebu tuone pamoja jinsi ya kusanidi nodi hii.


## Ni vifaa gani vya kuchagua kwa kusakinisha RoninDojo v2?

RoninDojo inatoa picha ya usakinishaji kiotomatiki wa programu yake kwenye [RockPro64](https://ronindojo.io/en/download). Hata hivyo, somo letu linaangazia utaratibu wa usakinishaji wa mwongozo kwenye Raspberry Pi 4. Ingawa Raspberry Pi 5 imezinduliwa hivi majuzi, na mafunzo haya yanafaa kinadharia kuendana na mtindo huu mpya, bado sijapata fursa ya kukijaribu kibinafsi, na sijapata maoni yoyote kutoka kwa jumuiya. Mara tu nitakapopata Pi 5 na vipengee vinavyotumika, nitasasisha mafunzo haya ili kukufahamisha. Wakati huo huo, ninapendekeza kuweka kipaumbele kwa Pi 4, kwani inafanya kazi kikamilifu kwa nodi yangu.

Kwa upande wangu, ninaendesha RoninDojo kwenye Raspberry Pi iliyo na 8 GB ya RAM. Ingawa baadhi ya wanajamii wameweza kuifanya ifanye kazi kwenye vifaa vilivyo na RAM ya GB 4 pekee, sijajaribu usanidi huu mimi mwenyewe. Kwa kuzingatia tofauti ndogo ya bei, inaonekana kuwa busara kuchagua toleo la 8 GB la RAM. Hii inaweza pia kuwa muhimu ikiwa unapanga kutumia tena Raspberry Pi yako kwa matumizi mengine katika siku zijazo.

Ni muhimu kutambua kwamba timu za RoninDojo zimeripoti masuala ya mara kwa mara kuhusiana na kesi na adapta ya SSD. Nimekumbana na masuala haya mimi mwenyewe. **Kwa hivyo, inashauriwa sana kuepuka kesi zilizo na kebo ya USB ya SSD ya nodi yako.** Badala yake, pendelea kadi ya upanuzi ya hifadhi iliyoundwa mahususi kwa Raspberry Pi yako:


![storage expansion card RPI4](assets/notext/1.webp)


Ili kuhifadhi Bitcoin Blockchain, utahitaji SSD inayoendana na kadi ya upanuzi ya hifadhi uliyochagua. Kwa sasa (Februari 2024), tuko katika awamu ya mpito. Inatarajiwa kwamba, katika miezi michache, disks 1 za TB hazitatosha tena kuwa na ukubwa unaoongezeka wa Blockchain, hasa kwa kuzingatia maombi mbalimbali unayopanga kuunganisha kwenye node yako. Kwa hivyo wengine wanapendekeza kuwekeza kwenye SSD ya TB 2 kwa amani ya akili kwa muda mrefu. Hata hivyo, kwa hali ya kushuka kwa bei za SSD mwaka baada ya mwaka, wengine wanapendekeza kutatua kwa diski 1 ya TB, ambayo inapaswa kutosha kwa mwaka mmoja au miwili, wakisema kwamba wakati inakuwa kizamani, gharama ya mifano 2 ya TB labda itapungua. Chaguo kwa hivyo inategemea upendeleo wako wa kibinafsi. Ikiwa unapanga kuweka RoninDojo yako kwa muda mrefu na ungependa kuepuka ushughulikiaji wowote wa kiufundi katika miaka ijayo, chaguo la 2 TB SSD linaonekana kuwa la busara zaidi, kwani hukupa ukingo mzuri kwa siku zijazo.


Kwa kuongeza, utahitaji vipengele vidogo vidogo:


- Kipochi kilicho na feni cha kuweka Raspberry Pi yako na kadi yako ya upanuzi ya hifadhi. Seti zinazojumuisha kadi ya upanuzi ya SSD na kipochi kinachooana zinapatikana mtandaoni;
- Kebo ya nguvu ya Raspberry Pi yako;
- Kadi ndogo ya SD ya angalau GB 16 (ingawa GB 8 inaweza kutosha kiufundi, tofauti ya bei kati ya kadi za GB 8 na 16 mara nyingi haitumiki);
- Kebo ya Ethaneti ya RJ45 kwa muunganisho wa mtandao.


![node material](assets/notext/2.webp)


## Jinsi ya kukusanyika Raspberry Pi 4?

Mkusanyiko wa nodi yako itatofautiana kulingana na vifaa vilivyochaguliwa, hasa aina ya kesi. Walakini, muhtasari wa jumla wa hatua za kufuata unabaki sawa katika mkutano.

Anza kwa kusakinisha SSD yako kwenye kadi ya upanuzi wa hifadhi, ukitunza kulinda skrubu mbili za kufunga zilizo nyuma.


![assembly1](assets/notext/3.webp)


Kisha ambatisha Raspberry Pi yako kwenye kadi ya upanuzi.


![assembly2](assets/notext/4.webp)


Pia, ambatisha shabiki kwa Raspberry Pi.


![assembly3](assets/notext/5.webp)


Unganisha vipengele mbalimbali, ukizingatia kutumia pini sahihi, ukirejelea mwongozo wa kesi yako. Watengenezaji wa kesi mara nyingi hutoa mafunzo ya video ili kukusaidia katika mkusanyiko. Kwa upande wangu, nina kadi ya upanuzi ya ziada iliyo na kitufe cha kuwasha/kuzima. Hii sio muhimu kwa kutengeneza nodi ya Bitcoin. Ninaitumia sana kwa kuwa na kitufe cha kuwasha.


Ikiwa, kama mimi, una kadi ya upanuzi iliyo na kitufe cha kuwasha/kuzima, usisahau kusakinisha jumper ndogo ya "Auto Power On". Hii itaruhusu nodi yako kuanza kiotomatiki mara tu inapowashwa. Kipengele hiki ni muhimu sana katika tukio la kukatika kwa umeme, kwani inaruhusu nodi yako kuanza upya yenyewe, bila uingiliaji wa mwongozo kwa upande wako.


![assembly4](assets/notext/6.webp)


Kabla ya kuingiza maunzi yote kwenye kipochi, ni muhimu kuangalia utendakazi sahihi wa Raspberry Pi yako, kadi ya upanuzi ya hifadhi, na feni kwa kuwasha.


![assembly5](assets/notext/7.webp)


Mwishowe, sasisha Raspberry Pi yako katika kesi yake. Fahamu, hatua ya baadaye itahitaji kuongeza kadi ndogo ya SD kwenye bandari inayofaa kwenye Raspberry Pi. Ikiwa kipochi chako kimewekwa na fursa ambayo hukuruhusu kuingiza kadi ya SD bila kuifungua (kama ilivyo kwa mgodi ulioonyeshwa kwenye picha), unaweza kuendelea na kufunga kesi sasa. Hata hivyo, ikiwa kipochi chako hakina ufikiaji wa moja kwa moja kwa mlango mdogo wa SD, utahitaji kusubiri hadi uwe umetayarisha kadi ndogo ya SD ili kuiingiza kabla ya kukamilisha mkusanyiko.


![assembly6](assets/notext/8.webp)


## Jinsi ya kufunga RoninDojo v2 kwenye Raspberry Pi 4?


### Hatua ya 1: Tayarisha SD ndogo inayoweza kuwashwa

Baada ya kukusanya vifaa vyako, hatua inayofuata ni kusakinisha RoninDojo. Kwa hili, tutatayarisha kadi ndogo ya SD ya bootable kutoka kwa kompyuta yako, kwa kuchoma picha sahihi ya disk juu yake.

Utahitaji kutumia _**Raspberry Pi Imager**_ programu, iliyoundwa ili kukuwezesha kupakua, kusanidi, na kuandika mifumo ya uendeshaji kwenye kadi ndogo ya SD kwa matumizi na Raspberry Pi. Anza kwa kusakinisha programu hii kwenye Kompyuta yako ya kibinafsi:


- Kwa Ubuntu/Debian: https://downloads.raspberrypi.org/imager/imager_latest_amd64.deb
- Kwa Windows: https://downloads.raspberrypi.org/imager/imager_latest.exe
- Kwa Mac: https://downloads.raspberrypi.org/imager/imager_latest.dmg


Mara baada ya programu kusakinishwa, ifungue, na uingize kadi yako ndogo ya SD kwenye kompyuta yako ya kibinafsi. Kutoka kwa Raspberry Pi Imager Interface, chagua `CHAGUA OS`:


![choose OS](assets/notext/9.webp)


Ifuatayo, nenda kwenye menyu ya `Raspberry Pi OS (nyingine)`:


![choose OS others](assets/notext/10.webp)


Chagua mfumo wa uendeshaji unaoitwa `Raspberry Pi OS (Legacy, 64-bit) Lite`, ambayo ni `0.3 GB` kwa ukubwa:


![choose OS Legacy Lite](assets/notext/11.webp)


Baada ya kuchagua mfumo wa uendeshaji, utaelekezwa kwenye menyu kuu ya Raspberry Pi Imager. Bofya kwenye `CHAGUA HIFADHI`:


![choose storage](assets/notext/12.webp)


Chagua kadi yako ndogo ya SD:


![choose micro sd](assets/notext/13.webp)


Baada ya kuchagua mfumo wa uendeshaji na kadi ndogo ya SD, bonyeza `NEXT`:


![choose next](assets/notext/14.webp)


Dirisha jipya litaonekana. Chagua `BARILISHA UWEKEAJI`:


![edit settings](assets/notext/15.webp)


Katika dirisha hili, nenda kwenye kichupo cha `GENERAL` na ufanye mipangilio ifuatayo (ambayo ni muhimu sana kwake kufanya kazi):


- Washa chaguo na ukabidhi `RoninDojo` kama jina la mpangishaji;
- Wezesha `Weka jina la mtumiaji na nenosiri`, ingiza `pi` kama jina la mtumiaji, chagua nenosiri, na kumbuka maelezo haya, kama yatakavyohitajika baadaye. Vitambulisho hivi ni vya muda na vitafutwa baadaye;
- Zima `Sanidi Wi-Fi`;
- Washa `Weka mipangilio ya eneo` na uchague saa za eneo lako pamoja na aina ya kibodi inayolingana na kompyuta yako;


![general settings](assets/notext/16.webp)


Katika kichupo cha HUDUMA, bofya kwenye kisanduku cha `Wezesha SSH` na uchague `Tumia nenosiri kwa uthibitishaji`:


![services settings](assets/notext/17.webp)


Pia, hakikisha kuwa katika kichupo cha `OPTIONS`, telemetry imezimwa:


![options settings](assets/notext/18.webp)


Bofya kwenye `HIFADHI`:


![settings save](assets/notext/19.webp)

Thibitisha kwa kubofya `NDIYO` ili kuanza kuunda kadi ndogo ya SD inayoweza kuwasha:

![settings yes](assets/notext/20.webp)


Ujumbe utakujulisha kuwa data yote kwenye kadi ndogo ya SD itafutwa. Thibitisha kwa kubofya `NDIYO` ili kuanza mchakato:


![overwrite micro SD](assets/notext/21.webp)


Subiri hadi programu ikamilishe kuandaa kadi yako ndogo ya SD:


![writing micro SD](assets/notext/22.webp)


Wakati ujumbe unaoonyesha mwisho wa mchakato unaonekana, unaweza kuondoa kadi ndogo ya SD kutoka kwa kompyuta yako:


![writing micro SD completed](assets/notext/23.webp)


### Hatua ya 2: Kamilisha Mkutano wa Nodi

Sasa unaweza kuingiza kadi ndogo ya SD kwenye bandari inayofaa ya Raspberry Pi yako.


![micro SD](assets/notext/24.webp)


Kisha unganisha Raspberry Pi yako kwenye kipanga njia chako kwa kutumia kebo ya Ethernet. Hatimaye, washa nodi yako kwa kuunganisha kebo ya umeme na kubofya kitufe cha kuwasha/kuzima (ikiwa usanidi wako unajumuisha moja).


### Hatua ya 3: Anzisha Muunganisho wa SSH na Nodi

Kwanza, ni muhimu kupata IP Address ya node yako. Una chaguo la kutumia zana kama vile _[Advanced IP Scanner](https://www.advanced-ip-scanner.com/)_ au _[Hasira IP Scanner](https://angryip.org/)_, au angalia usimamizi Interface wa kipanga njia chako. IP Address inapaswa kuwa katika fomu `192.168.1.??`. **Kwa amri zote zifuatazo, badilisha `[IP]` na IP halisi Address ya nodi yako**, (kuondoa mabano).


Zindua terminal.


Ili kuondoa ufunguo unaowezekana ambao tayari unahusishwa na IP Address ya nodi yako, tekeleza amri:

`ssh-keygen -R [IP]`.


Hitilafu kufuatia amri hii si mbaya; inamaanisha kuwa ufunguo haupo katika orodha yako ya wapangishi wanaojulikana (ambayo inawezekana). Kwa mfano, ikiwa IP ya nodi yako ni `192.168.1.40`, amri inakuwa: `ssh-keygen -R 192.168.1.40`.


Ifuatayo, anzisha muunganisho wa SSH na nodi yako kwa kutekeleza amri:

`ssh pi@[IP]`.

Ujumbe utaonekana kuhusu uhalisi wa mwenyeji: `Ukweli wa seva pangishi '[IP]' hauwezi kuthibitishwa.` Hii inaonyesha kuwa uhalisi wa kifaa unachojaribu kuunganisha nacho hauwezi kuthibitishwa kwa sababu ya ukosefu wa ufunguo wa umma unaojulikana. Unapounganisha kupitia SSH kwa seva pangishi mpya kwa mara ya kwanza, ujumbe huu utaonekana kila wakati. Lazima ujibu `ndiyo` ili kuongeza ufunguo wake wa umma kwenye saraka yako ya karibu, ambayo itazuia ujumbe huu wa onyo usionekane wakati wa miunganisho ya SSH ya siku zijazo kwenye nodi hii. Kwa hivyo, chapa `ndiyo` na ubonyeze `ingiza` ili kuthibitisha.

Kisha utaombwa kuingiza nenosiri lako, lile lililowekwa hapo awali kama la muda katika hatua ya 1. Thibitisha kwa `ingiza`. Kisha utaunganishwa kwenye nodi yako kupitia SSH.


Kwa muhtasari, hapa kuna amri za kutekeleza:


- `ssh-keygen -R [IP]`
- `ssh pi@[IP]`
- `ndio`
- Ingiza nenosiri la muda na uthibitishe.


### Hatua ya 4: Sasisha na Maandalizi

Sasa umeunganishwa kwenye nodi yako kupitia kipindi cha SSH. Kwenye terminal yako, haraka ya amri inapaswa kuwa: `pi@RoninDojo:~ $`. Ili kuanza, sasisha orodha ya vifurushi vinavyopatikana na usakinishe masasisho ya vifurushi vilivyopo kwa amri ifuatayo:

`sudo apt update && sudo apt upgrade -y`


Mara tu sasisho zimekamilika, endelea kusakinisha *Git* na *Dialog* kwa kutumia amri:

`sudo apt install git dialog -y`


Ifuatayo, fanya tawi la `master` la hazina ya _RoninOS_ Git kwa kutekeleza:

`sudo git clone --branch master https://code.samourai.io/ronindojo/RoninOS.git /opt/RoninOS`


Endesha hati `Customize-image.sh` kwa amri:

`cd /opt/RoninOS/ && sudo ./customize-image.sh`


**Ni muhimu kuruhusu hati iendeshe bila kukatizwa na kungoja kwa subira hadi mwisho wa mchakato wake**, ambao huchukua kama dakika 10. Wakati ujumbe `Usanidi umekamilika` unaonekana, unaweza kuendelea hadi hatua inayofuata.


### Hatua ya 5: Kuzindua RoninOS

Zindua RoninOS kwa amri:

`sudo systemctl anzisha usanidi wa ronin`


Onyesha mistari ya faili ya logi na amri:

`mkia -f /home/ronindojo/.logs/setup.logs`


Katika hatua hii, **ni muhimu kuiruhusu RoninOS izinduliwe na kungojea** imalize kukimbia. Hii inachukua kama dakika 40. Wakati `Usakinishaji wa vipengele vyote vya RoninDojo utakapokamilika!` inaonekana, unaweza kuendelea hadi hatua ya 6.


### Hatua ya 6: Kufikia RoninUI na Kubadilisha Kitambulisho

Baada ya kukamilisha usakinishaji, ili kuunganisha kwenye nodi yako kupitia kivinjari, hakikisha kwamba kompyuta yako ya kibinafsi imeunganishwa kwenye mtandao wa ndani sawa na nodi yako. Ikiwa unatumia VPN kwenye mashine yako, izima kwa muda. Ili kufikia nodi ya Interface kwenye kivinjari chako, ingiza kwenye upau wa URL:


- Moja kwa moja IP Address ya nodi yako, kwa mfano, `192.168.1.??`;
- Au, chapa `ronindojo.local`.


Mara moja kwenye ukurasa wa nyumbani wa RoninUI, utaulizwa kuanza usanidi. Ili kufanya hivyo, bofya kitufe cha `Hebu tuanze`.


![lets start](assets/notext/25.webp)


Katika hatua hii, RoninUI inakuletea nenosiri lako la `root`. Ni muhimu kuiweka salama. Unaweza kuchagua kupata nakala halisi, kwenye karatasi, au kuihifadhi katika [kidhibiti nenosiri](https://planb.network/courses/99c46148-7080-4915-a7e0-9df0e145cd47/0b3c69b2-522c-56c8-9fb8-155).


![root password](assets/notext/26.webp)


Baada ya kuhifadhi neno la siri la `mzizi`, chagua kisanduku `Nimeweka nakala rudufu za mtumiaji wa Root` na ubofye `Endelea` ili kuendelea.


![confirm root password](assets/notext/27.webp)


Hatua inayofuata inahusisha kuunda nenosiri la mtumiaji, ambalo litatumika kufikia mtandao wa RoninUI Interface na kuanzisha vipindi vya SSH na nodi yako. Chagua nenosiri dhabiti na uhakikishe kulihifadhi kwa usalama. Utahitaji kuingiza nenosiri hili mara mbili kabla ya kubofya `Maliza` ili kuhalalisha. Kuhusu jina la mtumiaji, inashauriwa kuweka chaguo-msingi, `ronindojo`. Ukiamua kulibadilisha, kumbuka kurekebisha amri katika hatua zifuatazo ipasavyo.


![user credentials](assets/notext/28.webp)


Mara tu vitendo hivi vimekamilika, subiri nodi yako ianzishwe. Kisha utafikia mtandao wa RoninUI Interface. Uko karibu mwisho wa mchakato, umesalia hatua chache tu!

![Ronin UI](assets/notext/29.webp)


### Hatua ya 7: Ondoa Kitambulisho cha Muda

Fungua terminal mpya kwenye kompyuta yako ya kibinafsi na uanzishe muunganisho wa SSH na nodi yako kwa kutumia amri ifuatayo:

`SSH ronindojo@[IP]`


Ikiwa, kwa mfano, IP Address ya nodi yako ni `192.168.1.40`, amri inayofaa itakuwa:

`SSH ronindojo@192.168.1.40`


Ikiwa ulibadilisha jina lako la mtumiaji wakati wa hatua ya awali, ukibadilisha jina la mtumiaji chaguo-msingi (`ronindojo`) na lingine, hakikisha unatumia jina hili jipya katika amri. Kwa mfano, ukichagua `planb` kama jina la mtumiaji na IP Address ni `192.168.1.40`, amri ya kuingia itakuwa:

`SSH planb@192.168.1.40`

Utaulizwa kuingiza nenosiri la mtumiaji. Ingiza na kisha ubonyeze `enter` ili kuhalalisha. Kisha utafikia RoninCLI Interface. Tumia vitufe vya vishale kwenye kibodi yako ili kuabiri hadi kwenye chaguo la `Toka RoninDojo` na ubonyeze `ingia` ili kuichagua.

![RoninCLI](assets/notext/30.webp)


Kwa wakati huu, uko kwenye terminal ya nodi yako, na haraka ya amri sawa na: `ronindojo@RoninDojo:~ $`. Ili kuondoa mtumiaji wa muda aliyeundwa wakati wa usanidi wa kadi ndogo ya SD inayoweza kuwasha, ingiza amri ifuatayo na ubonyeze `ingia`:

`sudo deluser --remove-home pi`


Utaulizwa kuthibitisha nenosiri lako la mtumiaji. Ingize na uthibitishe kwa kubonyeza `ingiza`. Subiri operesheni ikamilike, kisha utumie amri ya `toka` ili kuondoka kwenye terminal.


Hongera! Njia yako ya RoninDojo v2 sasa imesanidiwa na iko tayari kutumika. Itaanza IBD yake (*Upakuaji wa Kizuizi cha Awali*), ikiendelea kupakua na kuthibitisha Bitcoin Blockchain kutoka kwa kizuizi cha Genesis. Hatua hii inahusisha kurejesha miamala yote ya Bitcoin iliyofanywa tangu Januari 3, 2009, na inachukua muda. Mara baada ya Blockchain kupakuliwa kikamilifu, indexer itaendelea kubana hifadhidata. Muda wa IBD unaweza kutofautiana sana. Nodi yako ya RoninDojo itafanya kazi kikamilifu mara tu mchakato huu utakapokamilika.


**Ikiwa unahama kutoka nodi ya zamani ya RoninDojo v1** hadi toleo hili jipya na mafunzo haya huku ukihifadhi SSD sawa, nodi yako inapaswa kutambua kiotomatiki na kutumia tena data iliyopo kwenye diski, kukuepusha na umuhimu wa kutekeleza IBD tena. Katika kesi hii, utahitaji tu kusubiri nodi yako ili kusawazisha na vitalu vya hivi karibuni.


### Hatua ya 8: "veth fix"

Ikiwa unakutana na mdudu na RoninDojo v2 yako kwenye Raspberry Pi, ambapo baada ya usakinishaji usio na shida, nodi yako ghafla haipatikani kupitia SSH lakini inapona baada ya kuanzisha upya rahisi, basi unahitaji kufuata hatua hii ya 8. Hitilafu hii ya kawaida inaweza kurekebishwa kwa urahisi na ufumbuzi uliotengenezwa na jumuiya: "_veth fix_". Usahihishaji huu mdogo husuluhisha kukatika kwa ghafla. Hapa ni jinsi ya kuitumia.


Fungua terminal mpya kwenye kompyuta yako ya kibinafsi na uanzishe muunganisho wa SSH na nodi yako kwa kutumia amri ifuatayo:

`SSH ronindojo@[IP]`


Ikiwa, kwa mfano, IP Address ya nodi yako ni `192.168.1.40`, amri inayofaa itakuwa:

`SSH ronindojo@192.168.1.40`


Utaulizwa kuingiza nenosiri la mtumiaji. Ingiza na ubonyeze `enter` ili kuhalalisha. Kisha utafikia RoninCLI Interface. Tumia vishale vya kibodi yako kwenda kwenye chaguo la `Toka RoninDojo` na ubonyeze `ingia` ili kuichagua.


Kwa wakati huu, uko kwenye terminal ya nodi yako, na upesi wa amri sawa na: `ronindojo@RoninDojo:~ $`. Ili kutumia urekebishaji wa **veth**, chapa amri ifuatayo na ubonyeze `ingia`:

`sudo nano /etc/dhcpcd.conf`


Thibitisha nenosiri lako tena na ubonyeze `ingiza`.


Utafika kwenye faili ya `dhcpcd.conf`. Unahitaji kunakili maandishi yafuatayo, ukihakikisha kuwa unajumuisha nyota, na kuiongeza chini ya faili:

`nyingi za nyuso veth`


Ili kufanya hivyo, nenda chini ya faili kwa kutumia mshale wa chini kwenye kibodi yako, kisha ubofye kulia kwa kipanya chako ili kubandika maandishi kwenye mstari unaojitegemea.


Baada ya kuongeza maandishi, bonyeza `ctrl X` ili kuanza kuondoka, ikifuatiwa na `ctrl Y` ili kuthibitisha kuhifadhi mabadiliko, na ubonyeze `enter` ili kukamilisha na kurudi kwenye kidokezo cha amri. Ili kuhakikisha kuwa urekebishaji umetumika ipasavyo, fungua upya faili ya `dhcpcd.conf` kwa kutumia amri inayofaa.


Ili kukamilisha utumizi wa urekebishaji, anzisha upya nodi yako kwa kutekeleza:

`sudo washa upya sasa`


Katika hatua hii, unaweza kufunga terminal yako. Ruhusu muda unaohitajika ili RoninDojo yako iwake upya, kisha utaweza kuunganisha upya kupitia mchoro wa kivinjari chako wa Interface. Utaratibu huu unapaswa kurekebisha hitilafu iliyokutana.


## Jinsi ya kutumia nodi yako ya RoninDojo v2?


### Kuunganisha programu yako ya Wallet kwa Electrs

Matumizi ya kwanza ya nodi yako mpya iliyosakinishwa na iliyosawazishwa itakuwa kutangaza miamala yako kwa mtandao wa Bitcoin. Labda utataka kuunganisha pochi zako mbalimbali kwenye nodi yako ili kutangaza shughuli zako kwa siri. Unaweza kufanya hivyo kupitia Electrum Rust Server (elektroni). Programu hii kwa kawaida husakinishwa awali kwenye nodi yako ya RoninDojo. Ikiwa sivyo, unaweza kuisakinisha wewe mwenyewe kupitia RoninCLI Interface katika `Programu > Dhibiti Programu > Sakinisha Seva ya Electrum`.


Ili kupata Tor Address ya Seva yako ya Electrum, kutoka kwa mtandao wa RoninUI Interface, nenda kwa:

`Kuoanisha > Seva ya umeme > Oanisha sasa`

![Pairing](assets/notext/31.webp)

![Electrs](assets/notext/32.webp)

Kisha utahitaji kuingiza `Jina la mpangishaji` Address linaloisha kwa `.onion` katika programu yako ya Wallet, ikiambatana na port `50001`. ![jina la mwenyeji](assets/notext/33.webp)

Kwa mfano, kwenye Sparrow Wallet, nenda tu kwenye kichupo:

`Faili > Mapendeleo > Seva > Private Electrum`


![Sparrow](assets/notext/34.webp)


### Inaunganisha programu yako ya Wallet kwenye Samourai Dojo

Kama njia mbadala ya kutumia Electrs, Dojo hukuruhusu kuunganisha Software Wallet yako inayooana moja kwa moja kwenye nodi yako ya RoninDojo. Pochi kama vile Samourai Wallet na Sentinel hutoa utendakazi huu.


Ili kuanzisha muunganisho, utahitaji tu kuchanganua msimbo wa QR wa Dojo yako. Ili kufikia msimbo huu wa QR kupitia RoninUI, nenda kwa:

`Inaoanisha > Samourai Dojo > Oanisha sasa`

![Samourai Dojo](assets/notext/35.webp)

Ili kuunganisha Samourai Wallet yako kwenye Dojo yako, changanua tu msimbo huu wa QR wakati wa kusakinisha programu:


![Samourai Wallet connection](assets/notext/36.webp)


Ikiwa tayari ulikuwa na Samourai Wallet kabla ya kusanidi Ronin Dojo yako, ni muhimu kuhifadhi nakala ya Wallet yako, kufuta na kusakinisha tena programu ya Samourai Wallet, kabla ya kurejesha Wallet yako. Baada ya kuzindua programu iliyosakinishwa upya, utakuwa na chaguo la kuunganisha kwenye Dojo mpya. **Kuwa mwangalifu, mchakato huu una hatari ya kupoteza bitcoins zako ikiwa hautatekelezwa ipasavyo!** Hakikisha una nakala rudufu ya Samourai Wallet yako kwenye faili zako na uthibitishe uhalali wa passphrase yako kupitia `Mipangilio > Tatua matatizo > passphrase`. Pia ni muhimu kuwa na nakala inayoweza kusomeka ya maneno yako ya kurejesha uwezo wa kufikia akaunti na passphrase yako. Kwa usahihi zaidi katika operesheni hii, inashauriwa kufuata mafunzo haya ya kina: [https://wiki.ronindojo.io/en/setup/v2_0_0-upgrade/reconnectsamourai](https://wiki.ronindojo.io/en/setup/v2_0_0-upgrade/reconnectsamourai).


### Kwa kutumia Mempool.space yako mwenyewe Block explorer

Block explorer hubadilisha taarifa ghafi kutoka Bitcoin Blockchain hadi umbizo lililoundwa na kusomeka kwa urahisi. Kwa kutumia zana kama vile *Mempool.space*, inawezekana kuchanganua miamala, kutafuta anwani mahususi, au hata kushauriana na viwango vya wastani vya ada za mempools za mtandao kwa wakati halisi.


Hata hivyo, kutumia vichunguzi vya kuzuia mtandaoni kunaleta hatari kwa faragha yako na inahusisha uaminifu katika data iliyotolewa na wahusika wengine. Hakika, kwa kutumia huduma hizi bila kupitia nodi yako mwenyewe, unaweza kufichua habari kuhusu miamala yako bila kukusudia na lazima utegemee usahihi wa maelezo yaliyowasilishwa na mmiliki wa tovuti.

Ili kupunguza hatari hizi, inashauriwa kutumia mfano wako mwenyewe wa *Mempool.space* kupitia mtandao wa Tor, unaopangishwa moja kwa moja kwenye nodi yako. Suluhisho hili huhakikisha uhifadhi wa faragha yako na uhuru wa data yako.

Ili kufanya hivyo, anza kwa kusakinisha *Mempool Space Visualizer* kutoka RoninUI. Kwenye wavuti Interface, nenda kwenye kichupo cha `Dashibodi` na ubofye `Dhibiti` chini ya `Mempool Space`:

`Dashibodi > Nafasi ya Mempool > Dhibiti`

![Manage mempool](assets/notext/37.webp)

Kisha bofya kitufe cha `Sakinisha kitazamaji cha Mempool`:

![install mempool](assets/notext/38.webp)

Thibitisha nenosiri lako la mtumiaji:

![password mempool](assets/notext/39.webp)

Subiri usakinishaji ukamilike, kisha ubofye tena kitufe cha `Dhibiti`:

![Mempool Manage](assets/notext/40.webp)

Utapata kiungo cha `.onion` ili kufikia mfano wako mwenyewe wa *Mempool.space* kupitia mtandao wa Tor.

![Mempool link](assets/notext/41.webp)

Ninakushauri uhifadhi kiungo hiki katika vipendwa vyako kwenye kivinjari cha Tor au uongeze kwenye programu ya Tor Browser kwenye simu yako mahiri kwa ufikiaji rahisi na salama kutoka mahali popote. Ikiwa bado huna kivinjari cha Tor, unaweza kuipakua hapa: [https://www.torproject.org/download/](https://www.torproject.org/download/)

![Mempool Tor](assets/notext/42.webp)


### Kutumia Whirlpool kuchanganya bitcoins zako

Nodi yako ya RoninDojo pia inaunganisha _WhirlpoolCLI_, safu ya amri ya Interface inayowezesha uwekaji otomatiki wa viunganishi vya Whirlpool, na _WhirlpoolGUI_, mchoro wa Interface iliyoundwa kuingiliana na _WhirlpoolCLI_.


Kufanya CoinJoin kupitia Whirlpool kunahitaji kwamba programu inayotumika itumike kutekeleza michanganyiko. Hali hii inaweza kuwa kizuizi kwa wale wanaotaka kufikia viwango vya juu vya anonsets. Hakika, kifaa kinachopangisha programu inayounganisha Whirlpool lazima kiendelee kuwashwa. Hii ina maana kwamba ili kushiriki katika michanganyiko saa 24 kwa siku, kompyuta au simu yako mahiri lazima ibaki imewashwa huku Samourai au Sparrow zikiwa zimefunguliwa kila wakati. Suluhisho la kikwazo hiki ni kutumia _WhirlpoolCLI_ kwenye mashine ambayo huwashwa kila wakati, kama vile nodi ya Bitcoin, kuruhusu sarafu zako kuchanganyika bila kukatizwa, na bila hitaji la kuwasha kifaa kingine.


Mafunzo ya kina yako katika maandalizi ya kukuongoza hatua kwa hatua katika mchakato wa kuungana na Samourai Wallet na RoninDojo v2, kutoka A hadi Z.


Kwa ufahamu wa kina wa CoinJoin na matumizi yake kwenye Bitcoin, ninakualika pia kushauriana na makala haya mengine: Kuelewa na kutumia CoinJoin kwenye Bitcoin, ambapo ninaelezea kila kitu unachohitaji kujua kuhusu mbinu hii.




### Kwa kutumia Whirlpool Stat Tool (WST)


Baada ya kutekeleza sanjari na Whirlpool, ni muhimu kutathmini kwa usahihi kiwango cha faragha kilichofikiwa kwa UTXO zako mchanganyiko. Ili kufanya hivyo, unaweza kutumia zana ya Python *Whirlpool Stat Tool*. Zana hii inakuruhusu kupima alama zinazotarajiwa na rejea za UTXO zako, huku ukichanganua kiwango chao cha usambazaji kwenye bwawa.


Ili kuimarisha uelewa wako na taratibu za hesabu za anonsets hizi, napendekeza kusoma makala: REMIX - Whirlpool, ambayo inaelezea utendaji wa fahirisi hizi.


https://planb.network/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa



Ili kufikia zana ya WST, nenda kwa RoninCLI. Ili kufanya hivyo, fungua terminal kwenye kompyuta yako ya kibinafsi na uanzishe muunganisho wa SSH na nodi yako kwa kutumia amri ifuatayo:

`SSH ronindojo@[IP]`


Ikiwa, kwa mfano, IP Address ya nodi yako ni `192.168.1.40`, amri inayofaa itakuwa:

`SSH ronindojo@192.168.1.40`


Ikiwa ulibadilisha jina lako la mtumiaji wakati wa hatua ya 6, ukibadilisha jina la mtumiaji chaguo-msingi (`ronindojo`) na lingine, hakikisha unatumia jina hili jipya katika amri. Kwa mfano, ukichagua `planb` kama jina lako la mtumiaji na IP Address ni `192.168.1.40`, amri ya kuingia itakuwa:

`SSH planb@192.168.1.40`


Utaulizwa kuingiza nenosiri la mtumiaji. Ingiza na ubonyeze `enter` ili kuhalalisha. Kisha utafikia RoninCLI Interface. Tumia vitufe vya vishale kwenye kibodi chako ili kuelekea kwenye menyu ya `Zana ya Samourai` na ubonyeze `ingia` ili kuichagua:


![Samourai Toolkit](assets/notext/43.webp)


Kisha chagua `Whirlpool Stat Tool`:


![WST](assets/notext/44.webp)


Baada ya kuanzisha WST, chombo kitaendelea na usakinishaji wake otomatiki. Subiri wakati wa hatua hii. Maagizo ya matumizi yatapitia. Mara usakinishaji utakapokamilika, bonyeza kitufe chochote ili kufikia terminal ya WST:


![WST commands](assets/notext/45.webp)


Amri ifuatayo itaonyeshwa:

`wst#/tmp>`


Ikiwa ungependa kuondoka kwenye Interface hii na kurudi kwenye menyu ya RoninCLI, ingiza tu:

`acha`


Kwanza, ni muhimu kusanidi seva mbadala kutumia Tor, ili kuhakikisha usiri wakati wa kutoa data kutoka kwa OXT. Ingiza amri:

`soksi5 127.0.0.1:9050`


Baadaye, endelea kupakua maelezo ya pamoja yaliyo na muamala wako:

`Pakua 0001`

Badilisha `0001` na msimbo wa dhehebu wa bwawa unalopenda. Misimbo ya madhehebu ni kama ifuatavyo kwenye WST:


- Dimbwi la bitcoins 0.5: `05`
- Dimbwi la bitcoins 0.05: `005`
- Dimbwi la bitcoins 0.01: `001`
- Dimbwi la bitcoins 0.001: `0001`


Baada ya kupakua, pakia data kwa kubadilisha `0001` na msimbo wa bwawa lako katika amri hii: `load 0001`


![WST loading](assets/notext/46.webp)


Subiri hadi upakiaji ukamilike, ambao unaweza kuchukua dakika chache. Mara tu data inapopakiwa, ili kujua alama za anonset za sarafu yako, tekeleza amri `alama` ikifuatiwa na txid yako (bila mabano):

`alama [txid]`


![WST score](assets/notext/47.webp)


WST kisha itaonyesha alama ya rejea (_vipimo vinavyoonekana nyuma_), ikifuatwa na alama tarajiwa (_Vipimo vinavyotazama Mbele_). Kando na alama za kukosekana kwa mpangilio, WST pia itaonyesha kiwango cha usambazaji wa shughuli zako ya ununuzi ndani ya bwawa, ikilinganishwa na kutokujali kwake.


**Ni muhimu kutambua kwamba alama zinazotarajiwa za sarafu yako zinapaswa kuhesabiwa kutoka kwa txid ya mchanganyiko wako wa awali, na si kutoka kwa mchanganyiko wako wa hivi karibuni. Kinyume chake, alama ya retrospective ya UTXO inakokotolewa kutoka txid ya mzunguko wa mwisho.**


### Kwa kutumia Calculator ya Boltzmann

Kikokotoo cha Boltzmann ni zana ya kuchanganua muamala wa Bitcoin, ikitoa uwezo wa kupima kiwango chake cha entropy kati ya vipimo vingine vya juu. Data hizi hutoa tathmini iliyoidhinishwa ya faragha ya shughuli na kusaidia kutambua dosari zinazoweza kutokea. Zana hii tayari imeunganishwa kwenye nodi yako ya RoninDojo, na kuifanya iwe rahisi kufikia na kutumia.


Kabla ya kuelezea utaratibu wa kutumia Kikokotoo cha Boltzmann, ni muhimu kuelewa maana ya viashiria hivi, njia yao ya kuhesabu, na matumizi yao. Ingawa inatumika kwa shughuli yoyote ya Bitcoin, viashirio hivi ni muhimu sana katika kutathmini ubora wa shughuli ya CoinJoin.


**Kiashirio cha kwanza** ambacho programu huhesabu ni jumla ya idadi ya michanganyiko inayowezekana, iliyoonyeshwa chini ya `michanganyiko ya nb` kwenye zana. Kulingana na maadili ya UTXO zinazohusika, kiashiria hiki kinahesabu idadi ya njia ambazo pembejeo zinaweza kuhusishwa na matokeo. Kwa maneno mengine, huamua idadi ya tafsiri zinazokubalika ambazo shughuli inaweza generate. Kwa mfano, CoinJoin iliyoundwa kulingana na modeli ya Whirlpool 5x5 inatoa `1496` mchanganyiko unaowezekana:

![combinations](assets/notext/50.webp)

Mkopo: KYCP


**Kiashirio cha pili** kilichokokotolewa ni entropy ya muamala, iliyoteuliwa na `Entropy`. Wakati muamala una idadi kubwa ya michanganyiko inayowezekana, mara nyingi inafaa zaidi kurejelea entropy yake. Hii inafafanuliwa kama logarithm ya binary ya idadi ya michanganyiko inayowezekana. Hapa kuna fomula iliyotumiwa:


- $E$: entropy ya shughuli;
- $C$: idadi ya michanganyiko inayowezekana ya shughuli hiyo.

$$E = \log_2(C)$$


Katika hisabati, logarithm binary (msingi 2 logarithm) inalingana na uendeshaji kinyume cha kuongeza 2 kwa nguvu. Kwa maneno mengine, logariti ya binary ya $x$ ni kipeo ambacho 2 lazima iongezwe ili kupata $x$. Kwa hiyo, kiashiria hiki kinaonyeshwa kwa bits. Wacha tuchukue mfano wa kuhesabu entropy kwa shughuli ya CoinJoin iliyoundwa kulingana na muundo wa Whirlpool 5x5, ambayo, kama ilivyotajwa hapo awali, inatoa idadi ya mchanganyiko unaowezekana wa `1496`:

$$ C = 1496 $$

$$ E = \log_2(1496) $$

$$ E \takriban 10.5469 \text{ bits}$$


Kwa hivyo, shughuli hii ya CoinJoin inaonyesha entropy ya bits 10.5469, ambayo inachukuliwa kuwa ya kuridhisha sana. Kadiri thamani hii inavyokuwa juu, ndivyo tafsiri tofauti zaidi ya shughuli inavyokubali, na hivyo kuimarisha kiwango chake cha faragha.


Wacha tuchukue mfano wa ziada na shughuli ya kawaida zaidi, inayojumuisha ingizo moja na matokeo mawili: [1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://GW-9 6.space/en/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce)

Kwa upande wa muamala huu, tafsiri pekee inayowezekana ni: `(inp 0) > (Outp 0 ; Outp 1)`. Kwa hivyo, entropy yake imeanzishwa kwa `0`:

$$ C = 1 $$

$$ E = \log_2(1) $$

$$ E \takriban 0 \text{ bits}$$

**Kiashiria cha tatu** kinachotolewa na Kikokotoo cha Boltzmann kinaitwa `Ufanisi wa Wallet`. Kiashirio hiki hutathmini ufanisi wa shughuli kwa kuilinganisha na muamala bora unaowezekana katika usanidi unaofanana. Hii inatuongoza kujadili dhana ya entropy ya juu zaidi, ambayo inalingana na entropy ya juu zaidi muundo maalum wa shughuli unaoweza kufikia kinadharia. Kwa hivyo, kwa muundo wa Whirlpool 5x5 CoinJoin, entropy ya juu imewekwa kwenye `10.5469`. Ufanisi wa muamala kisha unakokotolewa kwa kukabili entropy hii ya juu zaidi na entropy halisi ya shughuli iliyochanganuliwa. Formula inayotumika ni kama ifuatavyo:


- $ER$: entropy halisi ya shughuli, iliyoonyeshwa kwa bits;
- $EM$: kiwango cha juu kinachowezekana cha entropy kwa muundo fulani wa ununuzi, pia katika bits;
- $Ef$: ufanisi wa shughuli, katika biti.

$$Ef = ER - EM$$ $$Ef = 10.5469 - 10.5469$$

$$Ef = 0 \text{ bits}$$


Kiashiria hiki pia kinaonyeshwa kama asilimia, formula yake ni basi:


- $CR$: idadi ya mchanganyiko halisi unaowezekana;
- $CM$: idadi ya juu ya mchanganyiko unaowezekana na muundo sawa;
- $Ef$: ufanisi ulioonyeshwa kama asilimia.

$$Ef = \frac{CR}{CM}$$

$$Ef = \frac{1496}{1496}$$

$$Ef = 100\%$$


Ufanisi wa `100%` kwa hivyo unaonyesha kuwa muamala huongeza uwezekano wake wa faragha kulingana na muundo wake.


**Kiashirio cha nne**, msongamano wa entropy, au `Uzito wa Entropy`, hutoa mtazamo kuhusu entropy kuhusiana na kila ingizo au matokeo ya muamala. Kiashiria hiki kinathibitisha kuwa cha muhimu kwa kutathmini na kulinganisha ufanisi wa shughuli za ukubwa tofauti. Ili kuihesabu, gawanya tu jumla ya entropi ya muamala kwa jumla ya idadi ya pembejeo na matokeo yanayohusika. Kwa kuchukua mfano wa Whirlpool 5x5 CoinJoin:


- $ED$: msongamano wa entropy ulioonyeshwa kwa bits;
- $E$: entropy ya shughuli iliyoonyeshwa kwa bits;
- $T$: jumla ya idadi ya pembejeo na matokeo katika muamala.

$$T = 5 + 5 = 10$$

$$ED = \frac{E}{T}$$

$$ED = \frac{10.5469}{10}$$

$$ED = 1.054 \text{ bits}$$

**Taarifa ya tano** iliyotolewa na Kikokotoo cha Boltzmann ni jedwali la uwezekano wa kulinganisha kati ya ingizo na matokeo. Jedwali hili linaonyesha, kupitia `alama ya Boltzmann`, uwezekano kwamba ingizo mahususi limeunganishwa kwa matokeo fulani. Kwa kuchukua mfano wa Whirlpool CoinJoin, jedwali la uwezekano lingeangazia uwezekano wa uhusiano kati ya kila ingizo na pato, likitoa kipimo cha kiasi cha utata au kutabirika kwa vyama katika shughuli ya ununuzi:


| %       | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |
|---------|----------|----------|----------|----------|----------|
| Input 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 4 | 34%      | 34%      | 34%      | 34%      | 34%      |


Hapa, ni wazi kwamba kila pembejeo lina nafasi sawa ya kuhusishwa na matokeo yoyote, ambayo huimarisha utata na usiri wa shughuli. Walakini, katika kesi ya shughuli rahisi na pembejeo moja na matokeo mawili, hali ni tofauti:


| %       | Output 0 | Output 1 |
|---------|----------|----------|
| Input 0 | 100%     | 100%     |

Hapa, tunaona kwamba uwezekano wa kila pato kutoka kwa pembejeo 0 ni 100%. Kwa hivyo, uwezekano mdogo hutafsiri kuwa usiri mkubwa zaidi, kwa kupunguza viungo vya moja kwa moja kati ya pembejeo na matokeo.


**Taarifa ya sita** iliyotolewa ni idadi ya viungo vya kubainisha, vinavyokamilishwa na uwiano wa viungo hivi. Kiashiria hiki kinaonyesha ni miunganisho mingapi kati ya pembejeo na matokeo katika shughuli iliyochanganuliwa ambayo haiwezi kupingwa, na uwezekano wa 100%. Uwiano, kwa upande wake, unatoa mtazamo juu ya uzito wa viungo hivi vya kuamua ndani ya viungo vya jumla vya ununuzi.


Kwa mfano, shughuli ya Whirlpool ya aina ya CoinJoin haitoi viungo vya kuamua, na kwa hiyo inaonyesha kiashirio na uwiano wa 0%. Kwa upande mwingine, katika shughuli yetu ya pili iliyochunguzwa (kwa pembejeo moja na matokeo mawili), kiashiria kinawekwa kwa 2 na uwiano unafikia 100%. Kwa hivyo, kiashiria kisicho na maana kinaashiria shukrani bora ya usiri kwa kukosekana kwa viungo vya moja kwa moja na visivyoweza kupingwa kati ya pembejeo na matokeo.


**Jinsi ya kufikia Kikokotoo cha Boltzmann kwenye RoninDojo?**

Ili kufikia zana ya *Boltzmann Calculator*, nenda kwa RoninCLI. Ili kufanya hivyo, fungua terminal kwenye kompyuta yako ya kibinafsi na uanzishe muunganisho wa SSH na nodi yako kwa kutumia amri ifuatayo: `SSH ronindojo@[IP]`


Ikiwa, kwa mfano, IP Address ya nodi yako ni `192.168.1.40`, amri inayofaa itakuwa:

`SSH ronindojo@192.168.1.40`


Ikiwa ulibadilisha jina lako la mtumiaji wakati wa hatua ya 6, ukibadilisha jina la mtumiaji chaguo-msingi (`ronindojo`) na lingine, hakikisha unatumia jina hili jipya katika amri. Kwa mfano, ukichagua `planb` kama jina lako la mtumiaji na IP Address ni `192.168.1.40`, amri ya kuingia itakuwa:

`SSH planb@192.168.1.40`


Utaulizwa kuingiza nenosiri la mtumiaji. Ingiza na kisha ubonyeze `enter` ili kuhalalisha. Kisha utafikia RoninCLI Interface. Tumia vishale kwenye kibodi yako kwenda kwenye menyu ya `Samourai Toolkit` na ubonyeze `enter` ili kuichagua:


![Samourai Toolkit](assets/notext/43.webp)


Kisha chagua `Kikokotoo cha Boltzmann`:


![boltzmann](assets/notext/49.webp)


Utafika kwenye ukurasa wa nyumbani wa programu:


![boltzmann home](assets/notext/51.webp)


Ingiza txid ya muamala unaotaka kusoma na ubonyeze kitufe cha `ingiza`:


![boltzmann txid](assets/notext/52.webp)


Kikokotoo kisha hukupa viashiria vyote ambavyo tumejadili hapo awali:


![boltzmann result](assets/notext/53.webp)


### Vipengele vingine vya RoninDojo v2

Nodi yako ya RoninDojo inaunganisha vipengele vingine mbalimbali. Hasa, una uwezo wa kuchambua habari maalum ili kuzingatia. Kwa mfano, wakati mwingine Samourai Wallet yako, iliyounganishwa na RoninDojo, inaweza isionyeshe bitcoins unazoshikilia. Ikiwa salio linaonyesha 0 huku una uhakika wa kuwa na bitcoins katika Wallet hii, sababu kadhaa zinaweza kueleza hali hii, kama vile hitilafu katika njia za utokaji. Lakini moja ya sababu inaweza pia kuwa kwamba nodi yako haifuatilii vizuri anwani zako. Ili kutatua tatizo hili, unaweza kuhakikisha kwamba nodi yako inafuata `xpub` yako kwa kutumia _xpub tool_. Ili kupata zana hii kupitia RoninUI, fuata njia:

`Matengenezo > Zana ya XPUB`


Ingiza `xpub` inayosababisha tatizo na ubofye kitufe cha `Angalia` ili kuthibitisha maelezo haya:

![xpub tool](assets/notext/54.webp)

Hakikisha kwamba miamala yote imeorodheshwa ipasavyo. Ni muhimu pia kuthibitisha kuwa aina ya utokezi inayotumika inalingana na Wallet yako. Ikiwa sivyo, bofya `Chapa upya`, kisha uchague kutoka `BIP44`, `BIP49`, au `BIP84` kulingana na mahitaji yako.

Zaidi ya zana hii, kichupo cha `Matengenezo` cha RoninUI kimejaa vipengele vingine muhimu:


- **Zana ya Muamala**: Huruhusu kuchunguza maelezo ya shughuli fulani;
- **Zana ya Address**: Inaruhusu kuthibitisha ufuatiliaji wa Address iliyotolewa na Dojo yako;
- Changanua upya Vitalu: Hulazimisha nodi yako kufanya uchanganuzi mpya wa safu maalum ya kuzuia.


Kichupo cha `Push Tx` ni kipengele kingine cha kuvutia cha RoninUI, ambacho huwezesha utangazaji wa shughuli iliyosainiwa kwenye mtandao wa Bitcoin. Muamala lazima uingizwe katika fomu ya hexadecimal.


Kuhusu vichupo vingine vinavyopatikana kwenye dashibodi yako ya RoninUI:


- `Programu`: Hupangisha programu ya Whirlpool, na hakika itatumika kuunganisha programu mpya katika siku zijazo;
- `Kumbukumbu`: Hutoa ufikiaji wa wakati halisi kwa kumbukumbu za matukio ya programu yako;
- `Maelezo ya Mfumo`: Hutoa maelezo ya jumla kuhusu nodi yako, kama vile halijoto ya CPU, matumizi ya nafasi ya kuhifadhi, au data ya RAM. Pia utapata chaguo za `Reboot` na `Shut down` ili kuanzisha upya au kuzima nodi yako;
- `Mipangilio`: Hukuruhusu kubadilisha nenosiri lako la mtumiaji.


Hapo unayo! Asante kwa kufuatilia mafunzo haya hadi mwisho. Ikiwa uliyafurahia, nakuhimiza kushiriki kwenye mitandao ya kijamii. Zaidi ya hayo, ikiwa una fursa, zingatia kuunga mkono wasanidi programu wanaofanya programu hizi huria na huria kupatikana kwa jumuiya yetu kwa mchango: [https://donate.ronindojo.io/](https://donate.ronindojo.io/). Ili kuongeza ujuzi wako wa RoninDojo na kugundua rasilimali zaidi, ninapendekeza sana kushauriana na viungo vya rasilimali za nje zilizotajwa hapa chini.


**Nyenzo za nje:**


- [https://ronindojo.io/index.html](https://ronindojo.io/index.html)
- [https://wiki.ronindojo.io/en/home](https://wiki.ronindojo.io/en/home)
- [https://gist.github.com/LaurentMT/e758767ca4038ac40aaf](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [https://medium.com/@laurentmt/introducing-boltzmann-85930984a159](https://medium.com/@laurentmt/introducing-boltzmann-85930984a159)
- [https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry](https://wiki.ronindojo.io/en/setup/V2_0_0-upgrade-raspberry)

