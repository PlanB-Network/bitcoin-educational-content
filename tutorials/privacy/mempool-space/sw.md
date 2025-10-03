---
name: Mempool
description: Gundua mfumo mzima wa ikolojia wa Bitcoin.
---

![cover](assets/cover.webp)



protocol ya Bitcoin ni mtandao usiojulikana, uliogatuliwa ulio wazi kwa mashauriano. Wanachama (node), yaani kompyuta zilizo na mfano wa programu ya Bitcoin, zina ufikiaji usio na kikomo kwa data yote iliyochapishwa kwenye Bitcoin. Walakini, katika miaka ya mapema ya Bitcoin, protocol haikuweza kupatikana kama ilivyo leo.


Katika siku za mwanzo za Bitcoin, ilikuwa ni lazima kuendesha node ya Bitcoin ili kufikia zana zinazofaa (bitcoin-cli) ili kuhoji mtandao kutoka kwa mistari ya amri.



https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.network/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

Kwa hivyo miradi imezinduliwa ili kupanua jumuiya ya Bitcoin, na kuifanya iweze kufikiwa zaidi na mtu yeyote ambaye hamiliki node na/au hana ujuzi wa kiufundi unaohitajika.



Katika somo hili, tutaangalia mradi wa **Mempool.space**, vipengele vyake na athari ambayo imekuwa nayo kwenye mfumo ikolojia wa Bitcoin.



## Mempool.space ni nini?



**Mempool.space** ni mgunduzi wa chanzo huria ambaye hutoa taarifa muhimu kuhusu miamala, ada za miamala, block na miners kwenye mitandao mbalimbali ya protocol ya Bitcoin. Ilizinduliwa mnamo 2020, inaleta uboreshaji mkubwa katika uzoefu wa mtumiaji kupitia picha wakilishi, uhuishaji laini na miingiliano isiyo na vitu vingi.



Ili kuelewa mradi huo, Mempool (dimbwi la kumbukumbu) ni nafasi ya kawaida ambayo muamala zote zinazosubiri uthibitisho kwenye mtandao wa Bitcoin huhifadhiwa. Mempool ni kama "chumba cha kusubiri" ambapo miamala ya Bitcoin zinasubiri kuthibitishwa. Kila kompyuta kwenye mtandao (node) ina chumba chake cha kusubiri, ambacho kinaelezea kwa nini si muamala zote zinazoonekana kwa kila mtu kwa wakati mmoja.



Athari kuu ya jukwaa katika mfumo ikolojia wa Bitcoin ni kwamba hukuruhusu kufikia taarifa mbalimbali katika maeneo ya kumbukumbu ya node nyingi zilizopo kwenye Bitcoin bila kuhitaji kuendesha moja. Mempool.space ni hifadhi ya kutazama na kutafuta mitandao ya protocol ya Bitcoin.



Kuongezeka kwa matumizi katika mfumo ikolojia na ukweli kwamba Mempool.space ni chanzo huria kumeiwezesha kuunganishwa katika mifumo zaidi na zaidi ya upangishaji wa kibinafsi. Sasa unaweza kuwa na mfano wako wa Mempool.space moja kwa moja kwenye node yako ya kibinafsi. Tazama mafunzo yetu juu ya kusanidi Mempool.space kwenye node yako ya Umbrel hapa chini.



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Misingi ya Mempool.space



Kama ilivyotajwa hapo juu, [Mempool.space](https://Mempool.space) ni kichunguzi cha protocol cha Bitcoin ambacho hukuwezesha kufuatilia miamala yako na uenezi wake kwenye mtandao uliochaguliwa wa Bitcoin kwa wakati halisi, kutoka kwa mchoro wa Interface.



Mempool.space inasaidia mitandao mingi ya protocol ya Bitcoin.


Kwenye upau wa menyu, utapata mitandao ifuatayo:




- **Mainnet** : Mtandao mkuu wa Bitcoin ambapo miamala halisi ya Bitcoin hufanyika.
- **Saini**: Mtandao wa majaribio unaotumia sahihi za kidijitali ili kuthibitisha vizuizi bila kuhitaji rasilimali zinazohitajika na mtandao mkuu.
- **Testnet 3**: Jaribio lisilo na hatari na mtandao wa ukuzaji kwenye protocol ya Bitcoin.
- **Testnet 4** : Toleo jipya la Testnet 3 huleta uthabiti zaidi na sheria mpya za maafikiano kwa mazingira ya majaribio.



![reseaux](assets/fr/01.webp)



Kwenye ukurasa wa nyumbani, upande wa kushoto katika Green, utaona blocks zinaxowezeksna za siku zijazo (vikundi vya miamala) vilivyo tayari kuthibitishwa na kuunganishwa (kuchimbwa) kwenye mtandao wa Bitcoin. Kwa wastani, block huchimbwa kila baada ya dakika kumi: weka habari hii, kwani itakuja kwa manufaa baadaye katika maendeleo yetu.


Kwa purplish, upande wa kulia, utapata block ya hivi majuzi vilivyochimbwa kwenye Bitcoin, huku idadi ya block ya mwisho iliyochimbwa ikiwakilisha urefu wa sasa wa mtandao.



![blocs](assets/fr/02.webp)



Sehemu ya **Ada za Muamala** ni mkadiriaji wa ada ya muamala. Kadiri ada zinazotolewa kwa muamala wako zilivyo juu, ndivyo uwezekano wa muamala wako utaongezwa kwenye block inachofuata ilicho tayari kuchimbwa.


Ada za muamala zinawakilisha gharama ambayo Miner itachukua kutoka kwako ili kuingiza muamala wako kwenye block ya mteja cha Mining. Inafafanuliwa kwa uwiano wa sat/vB (Satoshi/Virtual Bytes) inayowakilisha idadi ya satoshi unazolipa kwa nafasi ambayo muamala yako itachukua katika block ya mgombea.



⚠️ MUHIMU: Katika tukio la kueneza kwa Mempool, wachimbaji wanatoa kipaumbele kwa miamala inayotoa uwiano bora wa Satoshi/vByte. Kadiri muamala yako inavyokuwa nzito (kubwa), ndivyo satoshi inavyohitaji kujumuishwa haraka.



![fees-visualizer](assets/fr/03.webp)



Sehemu ya **Mempool Goggles** inakuwezesha kuibua nafasi iliyochukuliwa na muamala.



![mempool](assets/fr/04.webp)



block huchimbwa takriban kila dakika kumi kutokana na ugumu wa Proof of Work ambayo miners wanapaswa kutoa ili kuongeza block ya wagombea wao kwenye mlolongo wa block wa kuchimbwa. Ugumu huu hutofautiana kila **block ya 2016**, sawa na takriban **wiki 2**. Unaweza kuona mabadiliko ya ugumu huu hapa.



![difficulty](assets/fr/05.webp)



Kuongezwa kwa block kipya kwenye msururu mkuu kunaipa Miner ya block iliyoidhinishwa kwa zawadi inayoundwa na sehemu isiyobadilika (iliyopunguzwa kwa nusu kila block 210,000**, sawa na karibu miaka 4** wakati wa kupunguzwa kwa nusu) na ada za ununuzi.



![halving](assets/fr/06.webp)



## Fikia maelezo ya muamala wako



Katika upau wa utafutaji wa Mempool.space, unaweza kuingiza Bitcoin Address yako au transaction ID yako ili kujua zaidi kuhusu historia yako.



![search](assets/fr/07.webp)



Kwenye ukurasa wa maelezo ya muamala, utapata maelezo ya jumla kuhusu muamala wako:




- **Hali**: Inathibitishwa inapoongezwa kwenye block, haijathibitishwa inaposubiri kwenye Mempool.
- **Ada za muamala**.
- **Muda uliokadiriwa wa kuwasili (ETA)** : Muda unaokadiriwa itachukua ili muamala wako uongezwe kwenye block. Inakokotolewa kulingana na uwiano unaojumuisha ada zinazohusiana na muamala huu.



![general-txinfo](assets/fr/08.webp)



Sehemu ya **Mtiririko** inaonyesha grafu ya Elements zako za muamala.



Ingizo (UTXO iliyotangulia), iliyotumika kwa ununuzi wako, na matokeo yanayowapa wapokeaji haki ya kutumia bitcoins kutoka kwa kila toleo kwa kuwasilisha sahihi inayohitajika kwa matumizi yao.



![flow](assets/fr/09.webp)



Maelezo zaidi kuhusu address zinazotumiwa yanaweza kupatikana katika sehemu ya **Inaingiza na Matokeo**.



![address](assets/fr/10.webp)



Gundua mipango tofauti ya miamala ya Bitcoin ili kuboresha usiri wako.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Ongeza kasi ya muamala zako



Katika mfumo ikolojia wa Bitcoin, kipengele cha uthibitishaji wa miamala na wachimbaji kimeunganishwa kihalisi na ada za muamala zinazohusiana na muamala hiyo. Wachimbaji hutanguliza malipo kwa uwiano wa juu wa ada (satoshis/vBytes), ambayo inaweza kuathiri uhalali wa muamala yako ikiwa hutalipa ada zinazokubalika zinazokubaliwa na wachimbaji. Muamala wako utakwama katika Mempool ukingoja block kinachokubali uwiano wake wa ada.



Kwa bahati nzuri, kuna njia mbili zinazopatikana kwenye mtandao wa Bitcoin ili kuharakisha uthibitisho wa muamala yako.





- **RBF** - Kubadilisha Kwa Ada: Njia inayokuruhusu kutumia maingizo sawa na malipo yako ya ada ya chini, lakini wakati huu kwa kuongeza ada ya muamala ili kuharakisha uthibitishaji. Muamala wako mpya utathibitishwa kwa haraka zaidi na kujumuishwa kwenye block, na kubatilisha muamala wa ada ya chini.



Unaweza kutekeleza hatua ya Exchange ada na portfolios zinazokubali utaratibu huu. Kwa mfano, angalia nakala yetu kwenye kwingineko ya Bluu 

https://planb.network/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90



- **CPFP** - Child pay for parent: Mbinu iliyoongozwa na RBF, lakini kwa upande wa mpokeaji. Wakati muamala ambao wewe ni mpokeaji umezuiwa katika Mempool, una chaguo la kutumia matokeo (UTXOs) ya muamala huu, licha ya ukweli kwamba bado haujathibitishwa, kwa kutenga ada zaidi kwa muamala huu mpya ili ada ya wastani - ya muamala ambayo wewe ni mpokeaji kujumuisha katika muamala - kuhimiza wapokeaji katika muamala.



⚠️ Muamala wa kwanza lazima ujumuishwe kwenye block ili kuruhusu muamala wa pili kuthibitishwa.



Iwapo maneno haya yote yanaonekana kuwa ya kiufundi sana, ninapendekeza [upate faharasa yetu](https://planb.network/resources/glossary.) ambayo ina ufafanuzi wa maneno yote ya kiufundi yanayohusiana na Bitcoin na mfumo wake wa ikolojia.



Mbali na mbinu hizi, Mempool.space, kutokana na miunganisho yake na zaidi ya 80% ya miners waliopo kwenye mtandao wa Bitcoin, pia hukuruhusu kuharakisha muamala zako zozote **zisizothibitishwa**, hata zile ambazo haziamilishi RBF, kwa kuzingatia wachimbaji katika Exchange kwa ajili ya kutayarisha muamala wako wa bei ya chini uliozuiwa.



Kwenye ukurasa wa maelezo ya muamala, bofya kitufe cha **Ongeza Kasi**, kisha uendelee kumlipa mshirika wako kwa wachimbaji.



![accelerate-section](assets/fr/11.webp)


## Watoto wadogo



Miner inarejelea mtu anayesimamia mgodi, yaani, kompyuta inayohusika na mchakato wa Mining, unaojumuisha kushiriki katika Proof-of-Work. Miner huweka pamoja muamala zinazosubiri katika Mempool yake ili kuunda block cha wagombea. Kisha hutafuta Hash halali, chini ya au sawa na lengo, kwa kichwa cha block hii kwa kurekebisha nonces mbalimbali. Ikiwa atapata Hash halali, anatangaza block yake kwenye mtandao wa Bitcoin na huweka thawabu ya pesa inayohusiana, inayoundwa na ruzuku ya block (kuundwa kwa bitcoins mpya ex-nihilo), na ada 

https://planb.network/courses/ce272232-0d97-4482-884a-0f77a2ebc036

❗Miners ni kama "wathibitishaji" ambao huthibitisha na kupanga miamala katika block. Ili kuongeza block kipya kwenye mtandao wa Bitcoin, wanapaswa kutatua puzzle tata ya hisabati (Proof-of-Work). Miner wa kwanza ya kutatua fumbo itapata zawadi ya Bitcoin (ruzuku ya kuzuia + ada za miamala iliyojumuishwa kwenye block).



Ugumu wa Proof of Work hii inafuatiliwa, kukuwezesha kuibua mageuzi ya nguvu za kompyuta zinazohitajika kwa wachimbaji. Utapata katika sehemu zifuatazo:





- Makadirio ya jumla ya zawadi zilizovunwa na wachimbaji wakati wa marekebisho ya mwisho ya ugumu, pamoja na makadirio ya Halving inayofuata ya ruzuku ya block, ambayo hutokea kila block 210,000 (takriban miaka 04).



![rewards](assets/fr/12.webp)



Ugumu huu unarekebishwa kila block vya 2016 (karibu wiki mbili). Inawiana kinyume na wastani wa muda unaochukuliwa na miners kwa Miner kila block ya 2016.


Wakati wastani wa muda unaochukuliwa na miners ni chini ya dakika 10, ugumu huongezeka, na kuthibitisha kuwa ilikuwa rahisi kwa wachimbaji kuthibitisha block ya Miner. Kinyume chake, wakati wastani unaochukuliwa ni mkubwa zaidi ya dakika 10, ugumu hupungua.



![mining-pool](assets/fr/13.webp)





- Vikundi vya wachimbaji madini: Kwa kuzingatia ugumu uliopo, Pool cha miners hushirikiana kusaidia kutafuta Proof of Work kwenye Bitcoin, katika kile tunachokiita **pool**. block kinawalletmbwa na Pool, malipo yanayopatikana husambazwa kulingana na asilimia ya mafanikio katika kila utafutaji wa ufumbuzi wa sehemu wa Miner, yaani, mchango katika nguvu za kompyuta katika utafutaji wa Proof-of-Work, au kulingana na mbinu ya malipo iliyokubaliwa na ushirikiano.





![mining](assets/fr/14.webp)



## Miundombinu ya Lightning Network



Mempool haitoi tu taarifa juu ya miundombinu ya mtandao ya Bitcoin (msururu mkuu). Pia inaunganisha zana za taswira na uchunguzi kwa ajili ya kuwekelea kwa Lightning ya Bitcoin.



Katika sehemu ya **Lightning**, unaweza kutazama miunganisho yote iliyopo kati ya node za Lightning.



![network-stats](assets/fr/15.webp)



Interface hii inatoa taarifa kuhusu:

- Takwimu za Lightning Network.

![distribution](assets/fr/16.webp)




⚠️**MUHIMU**: Uwezo wa kituo cha malipo hubainisha kiwango cha juu zaidi ambacho node inaweza kutuma kwenye node nyingine wakati wa muamala wa Lightning.



- node za Lightning Network zimetengwa kulingana na mtoa huduma wa mtandao (hosting service) na kwa hiari kulingana na uwezo wa njia ya malipo.

![distribution](assets/fr/17.webp)

- Historia ya uwezo wa jumla wa Lightning Network.


Utapata pia nafasi ya node hizi kulingana na uwezo wa njia zao za malipo.



![ranking](assets/fr/18.webp)



## Grafu zaidi



Mempool.space ni jukwaa bora la kufurahia mwingiliano na mitandao ya protocol ya Bitcoin. Grafu sio tu hutoa data ya kuona ili kukusaidia kuamua wakati wa kufanya miamala, lakini pia vigezo sahihi vinavyokuwezesha kuibua, kwa wakati halisi, nguvu na afya ya mtandao wa Bitcoin na miundomsingi inayohusika ya Lightning.



Katika sehemu ya **Michoro**, unaweza kuona data muhimu kuhusu mtandao wa Bitcoin:




- Mageuzi ya ukubwa wa Mempool: Unaweza kuona jinsi ukubwa wa Mempool unavyobadilika, ambayo inaweza kuonyesha vipindi vya miamala ya juu au za chini kwenye mtandao.



![graphs](assets/fr/19.webp)






- Mabadiliko ya miamala na ada za miamala kwenye mtandao uliochaguliwa: Kwa kufuatilia tofauti za miamala kwa sekunde, unaweza kutarajia vipindi vya msongamano au miamala ya chini, na uboreshe ada zako za muamala. Grafu hii inakupa mtazamo juu ya uwezo wa mtandao wa kumuamalakia kiasi cha miamala.



![graphs](assets/fr/20.webp)



Kwa kuwa sasa umefika mwisho wa safari yako kwenye Mempool.space, kuwa mgunduzi wako mwenyewe na ufuatilie miamala yako kwa wakati halisi. Tafadhali pata chini ya nakala yetu juu ya mpelelezi wa Bitcoin **Public Pool**.



https://planb.network/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1
