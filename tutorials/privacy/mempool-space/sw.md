---
name: Mempool
description: Gundua mfumo mzima wa ikolojia wa Bitcoin.
---

![cover](assets/cover.webp)



Itifaki ya Bitcoin ni mtandao usiojulikana, uliogatuliwa ulio wazi kwa mashauriano. Wanachama (nodi), yaani kompyuta zilizo na mfano wa programu ya Bitcoin, zina ufikiaji usio na kikomo kwa data yote iliyochapishwa kwenye Bitcoin. Walakini, katika miaka ya mapema ya Bitcoin, itifaki haikuweza kupatikana kama ilivyo leo.


Katika siku za mwanzo za Bitcoin, ilikuwa ni lazima kuendesha node ya Bitcoin ili kufikia zana zinazofaa (bitcoin-cli) ili kuhoji mtandao kutoka kwa mistari ya amri.



https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.network/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

Kwa hivyo miradi imezinduliwa ili kupanua jumuiya ya Bitcoin, na kuifanya iweze kufikiwa zaidi na mtu yeyote ambaye hamiliki nodi na/au hana ujuzi wa kiufundi unaohitajika.



Katika somo hili, tutaangalia mradi wa **Mempool.space**, vipengele vyake na athari ambayo imekuwa nayo kwenye mfumo ikolojia wa Bitcoin.



## Mempool.space ni nini?



**Mempool.space** ni mgunduzi wa chanzo huria ambaye hutoa taarifa muhimu kuhusu miamala, ada za miamala, vizuizi na wachimbaji madini kwenye mitandao mbalimbali ya itifaki ya Bitcoin. Ilizinduliwa mnamo 2020, inaleta uboreshaji mkubwa katika uzoefu wa mtumiaji kupitia picha wakilishi, uhuishaji laini na miingiliano isiyo na vitu vingi.



Ili kuelewa mradi huo, Mempool (dimbwi la kumbukumbu) ni nafasi ya kawaida ambayo shughuli zote zinazosubiri uthibitisho kwenye mtandao wa Bitcoin huhifadhiwa. Mempool ni kama "chumba cha kusubiri" ambapo shughuli za Bitcoin zinasubiri kuthibitishwa. Kila kompyuta kwenye mtandao (node) ina chumba chake cha kusubiri, ambacho kinaelezea kwa nini si shughuli zote zinazoonekana kwa kila mtu kwa wakati mmoja.



Athari kuu ya jukwaa katika mfumo ikolojia wa Bitcoin ni kwamba hukuruhusu kufikia taarifa mbalimbali katika maeneo ya kumbukumbu ya nodi nyingi zilizopo kwenye Bitcoin bila kuhitaji kuendesha moja. Mempool.space ni hifadhi ya kutazama na kutafuta mitandao ya itifaki ya Bitcoin.



Kuongezeka kwa matumizi katika mfumo ikolojia na ukweli kwamba Mempool.space ni chanzo huria kumeiwezesha kuunganishwa katika mifumo zaidi na zaidi ya upangishaji wa kibinafsi. Sasa unaweza kuwa na mfano wako wa Mempool.space moja kwa moja kwenye nodi yako ya kibinafsi. Tazama mafunzo yetu juu ya kusanidi Mempool.space kwenye nodi yako ya Umbrel hapa chini.



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Misingi ya Mempool.space



Kama ilivyotajwa hapo juu, [Mempool.space](https://Mempool.space) ni kichunguzi cha itifaki cha Bitcoin ambacho hukuwezesha kufuatilia miamala yako na uenezi wake kwenye mtandao uliochaguliwa wa Bitcoin kwa wakati halisi, kutoka kwa mchoro wa Interface.



Mempool.space inasaidia mitandao mingi ya itifaki ya Bitcoin.


Kwenye upau wa menyu, utapata mitandao ifuatayo:




- Mainnet** : Mtandao mkuu wa Bitcoin ambapo miamala halisi ya Bitcoin hufanyika.
- Saini**: Mtandao wa majaribio unaotumia sahihi za kidijitali ili kuthibitisha vizuizi bila kuhitaji rasilimali zinazohitajika na mtandao mkuu.
- Testnet 3**: Jaribio lisilo na hatari na mtandao wa ukuzaji kwenye itifaki ya Bitcoin.
- Testnet 4** : Toleo jipya la Testnet 3 huleta uthabiti zaidi na sheria mpya za maafikiano kwa mazingira ya majaribio.



![reseaux](assets/fr/01.webp)



Kwenye ukurasa wa nyumbani, upande wa kushoto katika Green, utaona vizuizi vinavyowezekana vya siku zijazo (vikundi vya miamala) vilivyo tayari kuthibitishwa na kuunganishwa (kuchimbwa) kwenye mtandao wa Bitcoin. Kwa wastani, kizuizi huchimbwa kila baada ya dakika kumi: weka habari hii, kwani itakuja kwa manufaa baadaye katika maendeleo yetu.


Kwa purplish, upande wa kulia, utapata vitalu vya hivi majuzi vilivyochimbwa kwenye Bitcoin, huku idadi ya block ya mwisho iliyochimbwa ikiwakilisha urefu wa sasa wa mtandao.



![blocs](assets/fr/02.webp)



Sehemu ya **Ada za Muamala** ni mkadiriaji wa ada ya muamala. Kadiri ada zinazotolewa kwa muamala wako zilivyo juu, ndivyo uwezekano wa muamala wako utaongezwa kwenye kizuizi kinachofuata kilicho tayari kuchimbwa.


Ada za muamala zinawakilisha gharama ambayo Miner itachukua kutoka kwako ili kuingiza muamala wako kwenye kizuizi cha mteja cha Mining. Inafafanuliwa kwa uwiano wa sat/vB (Satoshi/Virtual Bytes) inayowakilisha idadi ya satoshi unazolipa kwa nafasi ambayo shughuli yako itachukua katika kizuizi cha mgombea.



⚠️ MUHIMU: Katika tukio la kueneza kwa Mempool, wachimbaji wanatoa kipaumbele kwa miamala inayotoa uwiano bora wa Satoshi/vByte. Kadiri shughuli yako inavyokuwa nzito (kubwa), ndivyo satoshi inavyohitaji kujumuishwa haraka.



![fees-visualizer](assets/fr/03.webp)



Sehemu ya **Mempool Goggles** inakuwezesha kuibua nafasi iliyochukuliwa na muamala.



![mempool](assets/fr/04.webp)



Kitalu huchimbwa takriban kila dakika kumi kutokana na ugumu wa Proof of Work ambayo wachimbaji wanapaswa kutoa ili kuongeza kizuizi cha wagombea wao kwenye mlolongo wa vitalu vya kuchimbwa. Ugumu huu hutofautiana kila **vitalu vya 2016**, sawa na takriban **wiki 2**. Unaweza kuona mabadiliko ya ugumu huu hapa.



![difficulty](assets/fr/05.webp)



Kuongezwa kwa kizuizi kipya kwenye msururu mkuu kunaipa Miner ya block iliyoidhinishwa kwa zawadi inayoundwa na sehemu isiyobadilika (iliyopunguzwa kwa nusu kila vitalu 210,000**, sawa na karibu miaka 4** wakati wa kupunguzwa kwa nusu) na ada za ununuzi.



![halving](assets/fr/06.webp)



## Fikia maelezo ya muamala wako



Katika upau wa utafutaji wa Mempool.space, unaweza kuingiza Bitcoin Address yako au transaction ID yako ili kujua zaidi kuhusu historia yako.



![search](assets/fr/07.webp)



Kwenye ukurasa wa maelezo ya muamala, utapata maelezo ya jumla kuhusu muamala wako:




- Hali**: Inathibitishwa inapoongezwa kwenye kizuizi, haijathibitishwa inaposubiri kwenye Mempool.
- Ada za muamala**.
- Muda uliokadiriwa wa kuwasili (ETA)** : Muda unaokadiriwa itachukua ili muamala wako uongezwe kwenye kizuizi. Inakokotolewa kulingana na uwiano unaojumuisha ada zinazohusiana na muamala huu.



![general-txinfo](assets/fr/08.webp)



Sehemu ya **Mtiririko** inaonyesha grafu ya vipengele vyako vya muamala.



Ingizo (UTXO iliyotangulia), iliyotumika kwa ununuzi wako, na matokeo yanayowapa wapokeaji haki ya kutumia bitcoins kutoka kwa kila pato kwa kuwasilisha sahihi inayohitajika kwa matumizi yao.



![flow](assets/fr/09.webp)



Maelezo zaidi kuhusu anwani zinazotumiwa yanaweza kupatikana katika sehemu ya **Inaingiza na Matokeo**.



![address](assets/fr/10.webp)



Gundua mipango tofauti ya miamala ya Bitcoin ili kuboresha usiri wako.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Ongeza kasi ya shughuli zako



Katika mfumo ikolojia wa Bitcoin, kipengele cha uthibitishaji wa miamala na wachimbaji kimeunganishwa kihalisi na ada za muamala zinazohusiana na shughuli hiyo. Wachimbaji hutanguliza malipo kwa uwiano wa juu wa ada (satoshis/vBytes), ambayo inaweza kuathiri uhalali wa shughuli yako ikiwa hutalipa ada zinazokubalika zinazokubaliwa na wachimbaji. Muamala wako utakwama katika Mempool ukingoja kizuizi kinachokubali uwiano wake wa ada.



Kwa bahati nzuri, kuna njia mbili zinazopatikana kwenye mtandao wa Bitcoin ili kuharakisha uthibitisho wa shughuli yako.





- RBF** - Kubadilisha Kwa Ada: Njia inayokuruhusu kutumia maingizo sawa na malipo yako ya ada ya chini, lakini wakati huu kwa kuongeza ada ya muamala ili kuharakisha uthibitishaji. Muamala wako mpya utathibitishwa kwa haraka zaidi na kujumuishwa kwenye kizuizi, na kubatilisha muamala wa ada ya chini.



Unaweza kutekeleza hatua ya kubadilisha ada na portfolios zinazokubali utaratibu huu. Kwa mfano, angalia nakala yetu kwenye kwingineko ya Bluu Wallet.



https://planb.network/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90



- CPFP** - Child pay for parent: Mbinu iliyoongozwa na RBF, lakini kwa upande wa mpokeaji. Wakati muamala ambao wewe ni mpokeaji umezuiwa katika Mempool, una chaguo la kutumia matokeo (UTXOs) ya muamala huu, licha ya ukweli kwamba bado haujathibitishwa, kwa kutenga ada zaidi kwa muamala huu mpya ili ada ya wastani - ya shughuli ambayo wewe ni mpokeaji kujumuisha katika muamala - kuhimiza wapokeaji katika muamala.



⚠️ Muamala wa kwanza lazima ujumuishwe kwenye kizuizi ili kuruhusu muamala wa pili kuthibitishwa.



Iwapo maneno haya yote yanaonekana kuwa ya kiufundi sana, ninapendekeza [upate faharasa yetu](https://planb.network/resources/glossary), ambayo ina ufafanuzi wa maneno yote ya kiufundi yanayohusiana na Bitcoin na mfumo wake wa ikolojia.



Mbali na mbinu hizi, Mempool.space, kutokana na miunganisho yake na zaidi ya 80% ya wachimba migodi waliopo kwenye mtandao wa Bitcoin, pia hukuruhusu kuharakisha shughuli zako zozote **zisizothibitishwa**, hata zile ambazo haziamilishi RBF, kwa kuzingatia wachimbaji katika Exchange kwa ajili ya kutayarisha muamala wako wa bei ya chini uliozuiwa.



Kwenye ukurasa wa maelezo ya muamala, bofya kitufe cha **Ongeza Kasi**, kisha uendelee kumlipa mshirika wako kwa wachimbaji.



![accelerate-section](assets/fr/11.webp)


## Watoto wadogo



Miner inarejelea mtu anayesimamia mgodi, yaani, kompyuta inayohusika na mchakato wa Mining, unaojumuisha kushiriki katika Proof-of-Work. Miner huweka pamoja shughuli zinazosubiri katika Mempool yake ili kuunda kizuizi cha wagombea. Kisha hutafuta Hash halali, chini ya au sawa na lengo, kwa kichwa cha kizuizi hiki kwa kurekebisha nonces mbalimbali. Ikiwa atapata Hash halali, anatangaza kizuizi chake kwenye mtandao wa Bitcoin na huweka thawabu ya pesa inayohusiana, inayoundwa na ruzuku ya kuzuia (kuundwa kwa bitcoins mpya ex-nihilo), na ada ya manunuzi.



https://planb.network/courses/ce272232-0d97-4482-884a-0f77a2ebc036

❗Wachimba madini ni kama "wathibitishaji" ambao huthibitisha na kupanga miamala katika vizuizi. Ili kuongeza kizuizi kipya kwenye mtandao wa Bitcoin, wanapaswa kutatua puzzle tata ya hisabati (Proof-of-Work). Miner ya kwanza ya kutatua fumbo itapata zawadi ya Bitcoin (ruzuku ya kuzuia + ada za miamala iliyojumuishwa kwenye kizuizi).



Ugumu wa Proof of Work hii inafuatiliwa, kukuwezesha kuibua mageuzi ya nguvu za kompyuta zinazohitajika kwa wachimbaji. Utapata katika sehemu zifuatazo:





- Makadirio ya jumla ya zawadi zilizovunwa na wachimbaji wakati wa marekebisho ya mwisho ya ugumu, pamoja na makadirio ya Halving inayofuata ya ruzuku ya vitalu, ambayo hutokea kila vitalu 210,000 (takriban miaka 04).



![rewards](assets/fr/12.webp)



Ugumu huu unarekebishwa kila vitalu vya 2016 (karibu wiki mbili). Inawiana kinyume na wastani wa muda unaochukuliwa na wachimbaji kwa Miner kila vitalu vya 2016.


Wakati wastani wa muda unaochukuliwa na wachimbaji ni chini ya dakika 10, ugumu huongezeka, na kuthibitisha kuwa ilikuwa rahisi kwa wachimbaji kuthibitisha vitalu vya Miner. Kinyume chake, wakati wastani unaochukuliwa ni mkubwa zaidi ya dakika 10, ugumu hupungua.



![mining-pool](assets/fr/13.webp)





- Vikundi vya wachimbaji madini: Kwa kuzingatia ugumu uliopo, kikundi cha wachimbaji hushirikiana kusaidia kutafuta Proof of Work kwenye Bitcoin, katika kile tunachokiita **bwawa**. Kizuizi kinapochimbwa na kikundi, malipo yanayopatikana husambazwa kulingana na asilimia ya mafanikio katika kila utafutaji wa ufumbuzi wa sehemu wa Miner, yaani, mchango katika nguvu za kompyuta katika utafutaji wa Proof-of-Work, au kulingana na mbinu ya malipo iliyokubaliwa na ushirikiano.





![mining](assets/fr/14.webp)



## Miundombinu ya Lightning Network



Mempool haitoi tu taarifa juu ya miundombinu ya mtandao ya Bitcoin (msururu mkuu). Pia inaunganisha zana za taswira na uchunguzi kwa ajili ya kuwekelea kwa Umeme wa Bitcoin.



Katika sehemu ya **Umeme**, unaweza kutazama miunganisho yote iliyopo kati ya nodi za Umeme.



![network-stats](assets/fr/15.webp)



Interface hii inatoa taarifa kuhusu:





- Takwimu za Lightning Network.



![distribution](assets/fr/16.webp)




⚠️ **MUHIMU**: Uwezo wa kituo cha malipo hubainisha kiwango cha juu zaidi ambacho nodi inaweza kutuma kwenye nodi nyingine wakati wa shughuli ya Umeme.





- Nodi za umeme zimetengwa kulingana na mtoa huduma wa mtandao (huduma ya mwenyeji) na kwa hiari kulingana na uwezo wa njia ya malipo.



![distribution](assets/fr/17.webp)





- Historia ya uwezo wa jumla wa Lightning Network.


Utapata pia nafasi ya nodi hizi kulingana na uwezo wa njia zao za malipo.



![ranking](assets/fr/18.webp)



## Michoro zaidi



Mempool.space ni jukwaa bora la kufurahia mwingiliano na mitandao ya itifaki ya Bitcoin. Grafu sio tu hutoa data ya kuona ili kukusaidia kuamua wakati wa kufanya miamala, lakini pia vigezo sahihi vinavyokuwezesha kuibua, kwa wakati halisi, nguvu na afya ya mtandao wa Bitcoin na miundomsingi inayohusika ya Umeme.



Katika sehemu ya **Michoro**, unaweza kuona data muhimu kuhusu mtandao wa Bitcoin:




- Mageuzi ya ukubwa wa Mempool: Unaweza kuona jinsi ukubwa wa Mempool unavyobadilika, ambayo inaweza kuonyesha vipindi vya shughuli za juu au za chini kwenye mtandao.



![graphs](assets/fr/19.webp)






- Mabadiliko ya miamala na ada za miamala kwenye mtandao uliochaguliwa: Kwa kufuatilia tofauti za miamala kwa sekunde, unaweza kutarajia vipindi vya msongamano au shughuli za chini, na uboreshe ada zako za muamala. Grafu hii inakupa mtazamo juu ya uwezo wa mtandao wa kushughulikia kiasi cha miamala.



![graphs](assets/fr/20.webp)



Kwa kuwa sasa umefika mwisho wa safari yako kwenye Mempool.space, kuwa mgunduzi wako mwenyewe na ufuatilie miamala yako kwa wakati halisi. Tafadhali pata chini ya nakala yetu juu ya mpelelezi wa Bitcoin **Public Pool**.



https://planb.network/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1