---
name: BIP47 - PayNym

description: Jinsi PayNyms hufanya kazi
---
***ONYO:** Kufuatia kukamatwa kwa waanzilishi wa Samourai Wallet na kunaswa seva zao tarehe 24 Aprili, programu haiwezi kutumiwa tena na watumiaji ambao hawana Dojo yao wenyewe. BIP47 inasalia kutumika kwenye Sparrow Wallet kwa watumiaji wote na **kwenye Samourai Wallet kwa watumiaji walio na Dojo** pekee.*


_Tunafuatilia kwa karibu maendeleo ya kesi hii pamoja na maendeleo kuhusu zana zinazohusiana. Uwe na uhakika kwamba tutasasisha mafunzo haya kadiri habari mpya zinavyopatikana._


_Mafunzo haya yametolewa kwa madhumuni ya elimu na habari pekee. Hatuidhinishi au kuhimiza matumizi ya zana hizi kwa madhumuni ya uhalifu. Ni wajibu wa kila mtumiaji kutii sheria katika eneo la mamlaka yake._


---

> "Yeye ni mkubwa sana," wote walisema, na jogoo wa Uturuki, ambaye alizaliwa na spurs na alifikiri kuwa ni mfalme, alivimba kama meli iliyo na matanga yote, na akaenda moja kwa moja kwake kwa hasira kali, macho yake nyekundu kama moto. Bata maskini hakujua ikiwa atasimama au kukimbia, na hakuwa na furaha sana kwa sababu alidharauliwa na bata wote kwenye ua.

![BIP47, the ugly duckling illustration](assets/1.webp)


Mojawapo ya masuala muhimu zaidi kwenye itifaki ya Bitcoin ni kutumia tena Address. Uwazi na usambazaji wa mtandao hufanya mazoezi haya kuwa hatari kwa faragha ya mtumiaji. Ili kuepuka matatizo yanayohusiana na hili, inashauriwa kutumia tupu mpya ya kupokea Address kwa kila malipo mapya yanayoingia kwa Wallet, ambayo inaweza kuwa ngumu kufikia katika baadhi ya matukio.


Maelewano haya ni ya zamani kama White Paper. Satoshi tayari ilituonya juu ya hatari hii katika kazi yake iliyochapishwa mwishoni mwa 2008:


> Kama ngome ya ziada, jozi mpya ya funguo inapaswa kutumika kwa kila shughuli ili kuwazuia kuunganishwa na mmiliki wa kawaida.

Kuna masuluhisho mengi yanayopatikana ili kupokea malipo mengi bila kutumia tena Address. Kila mmoja wao ana maelewano yake na vikwazo. Miongoni mwa suluhu hizi zote, kuna [BIP47](https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki), pendekezo lililoundwa na Justus Ranvier na kuchapishwa mwaka wa 2015, ambalo linaruhusu uundaji wa misimbo ya malipo inayoweza kutumika tena. Lengo lake ni kuwezesha miamala mingi kufanywa kwa mtu yule yule bila kutumia tena Address.


Hapo awali, pendekezo hili lilipokelewa kwa dharau na sehemu ya jamii, na halikuongezwa kamwe kwa Bitcoin Core. Walakini, programu zingine bado zilichagua kuitekeleza peke yao. Kwa mfano, Samourai Wallet ilitengeneza utekelezaji wake wa BIP47: PayNym. Leo, utekelezaji huu unapatikana kwenye Samourai Wallet kwa simu mahiri, na pia kwenye [Sparrow Wallet](https://sparrowwallet.com/) kwa Kompyuta.


Baada ya muda, Samourai imepanga vipengele vipya vinavyohusiana moja kwa moja na PayNym. Sasa, kuna mfumo mzima wa zana unaopatikana ili kuboresha faragha ya mtumiaji kulingana na PayNym na BIP47.

Katika makala haya, utagundua kanuni ya BIP47 na PayNym, taratibu za itifaki hizi, na matumizi ya vitendo yanayotokana nayo. Nitatumia Address pekee toleo la kwanza la BIP47, ambalo kwa sasa linatumika kwa PayNym, lakini matoleo ya 2, 3, na 4 yanafanya kazi kwa njia sawa.


**Kumbuka** kuwa tofauti kuu pekee inapatikana katika shughuli ya arifa:


- Toleo la 1 hutumia Address rahisi na OP_RETURN kwa arifa,
- Toleo la 2 linatumia hati ya Multisig (bloom-Multisig) yenye OP_RETURN,
- Na matoleo ya 3 na 4 hutumia tu hati ya Multisig (cfilter-Multisig).


Taratibu zilizojadiliwa katika nakala hii, pamoja na njia za kriptografia zilizosomwa, kwa hivyo zinatumika kwa matoleo yote manne. Kufikia sasa, utekelezaji wa PayNym kwenye Samourai Wallet na Sparrow hutumia toleo la kwanza la BIP47.


## Muhtasari:


1- Tatizo la kutumia tena Address.


2- Kanuni za BIP47 na PayNym.


3- Mafunzo: Kutumia PayNym.



- Kujenga muamala wa BIP47 na Samourai Wallet.
- Kujenga muamala wa BIP47 na Sparrow Wallet.


4- Utendaji wa BIP47.



- Nambari ya malipo inayoweza kutumika tena.
- Mbinu ya kriptografia: Kitufe cha Diffie-Hellman Exchange kilichoanzishwa kwenye mikondo ya duaradufu (ECDH).
- Shughuli ya arifa.
- Kuunda shughuli ya arifa.
- Inapokea muamala wa arifa.
- Shughuli ya malipo ya BIP47.
- Kupokea malipo ya BIP47 na kupata ufunguo wa faragha.
- Kurejesha malipo ya BIP47.


5- Matumizi yanayotokana na PayNym.


6- Maoni yangu ya kibinafsi juu ya BIP47.


## Tatizo la kutumia tena Address.


Address inayopokea hutumiwa kupokea bitcoins. Inatolewa kutoka kwa ufunguo wa umma kwa kuharakisha na kutumia umbizo maalum. Kwa hivyo, inaruhusu kuundwa kwa hali mpya ya matumizi kwenye sarafu ili kubadilisha mmiliki wake.


Ili kupata maelezo zaidi kuhusu kutengeneza Address inayopokea, ninapendekeza usome sehemu ya mwisho ya makala haya: **The Bitcoin Wallet - dondoo kutoka** [ebook Bitcoin Démocratisé 2](https://www.pandul.fr/post/le-portefeuille-Bitcoin-extrait-ebook-Bitcoin-d%C3%A9mocratis%C3%A9-2#viewer-epio7).


Zaidi ya hayo, pengine tayari umesikia kutoka kwa bitcoiner mwenye ujuzi kwamba anwani za kupokea ni za matumizi ya mara moja, na kwamba unapaswa generate mpya kwa kila malipo mapya yanayoingia kwa Wallet yako. Sawa, lakini kwa nini?


Kimsingi, kutumia tena Address hakuhatarishi pesa zako moja kwa moja. Utumiaji wa kriptografia kwenye mikunjo ya duaradufu hukuruhusu kudhibitisha kwa mtandao kuwa una ufunguo wa kibinafsi bila kufichua ufunguo huo. Kwa hivyo, unaweza kufunga UTXO nyingi tofauti (Matokeo ya Shughuli Zisizotumika) kwenye Address sawa na kuzitumia kwa nyakati tofauti. Ikiwa hutafichua ufunguo wa faragha unaohusishwa na Address hiyo, hakuna mtu anayeweza kufikia pesa zako. Suala la kutumia tena Address linahusiana zaidi na faragha.


Kama ilivyoelezwa katika utangulizi, uwazi na usambazaji wa mtandao wa Bitcoin unamaanisha kwamba mtumiaji yeyote anayeweza kufikia nodi anaweza kuchunguza shughuli za mfumo wa malipo. Matokeo yake, wanaweza kuona mizani tofauti ya anwani. Satoshi Nakamoto kisha ilitaja uwezekano wa kuzalisha jozi mpya muhimu, na hivyo anwani mpya, kwa kila malipo mapya yanayoingia kwa Wallet. Lengo litakuwa kuwa na ngome ya ziada ikiwa kuna uhusiano kati ya utambulisho wa mtumiaji na mojawapo ya jozi zao muhimu.


Leo, pamoja na kuwepo kwa makampuni ya uchambuzi wa mnyororo na maendeleo ya KYC (Jua Mteja Wako), matumizi ya anwani tupu sio firewall ya ziada, lakini ni wajibu kwa mtu yeyote anayejali hata kidogo kuhusu faragha yao.


Kutafuta faragha sio faraja au ndoto ya Maximalist Bitcoiners. Ni kigezo maalum ambacho kinaathiri moja kwa moja usalama wako wa kibinafsi na usalama wa pesa zako. Ili kukusaidia kuelewa hili, hapa kuna mfano halisi:



- Bob hununua Bitcoin kupitia Dollar Cost Averaging (DCA), kumaanisha kwamba anapata kiasi kidogo cha Bitcoin kwa vipindi vya kawaida ili wastani wa bei yake ya kuingia. Bob hutuma pesa zilizonunuliwa kwa utaratibu sawa kupokea Address. Ananunua 0.01 Bitcoin kila wiki na kuituma kwa Address hii hiyo. Baada ya miaka miwili, Bob amekusanya Bitcoin nzima kwenye Address hii.
- Mwokaji kwenye kona anakubali malipo ya Bitcoin. Akiwa na furaha ya kutumia Bitcoin, Bob anaenda kununua baguette yake katika satoshis. Ili kulipa, anatumia pesa zilizofungwa na Address yake. Mwokaji wake sasa anajua kwamba anamiliki Bitcoin. Kiasi hiki kikubwa kinaweza kuvutia wivu, na Bob anaweza kuhatarisha shambulio la kimwili katika siku zijazo.


Utumiaji tena wa Address huruhusu mtazamaji kutengeneza kiungo kisichoweza kukanushwa kati ya UTXO zako tofauti na wakati mwingine kati ya utambulisho wako na Wallet yako yote.

Hii ndiyo sababu programu nyingi za Bitcoin Wallet huzalisha kiotomatiki Address mpya ya kupokea unapobofya kitufe cha "Pokea". Kwa watumiaji wa kawaida, kupata mazoea ya kutumia anwani mpya sio usumbufu mkubwa. Hata hivyo, kwa biashara ya mtandaoni, Exchange, au kampeni ya mchango, kikwazo hiki kinaweza kushindwa kudhibitiwa haraka.

Kuna suluhisho nyingi kwa mashirika haya. Kila moja yao ina faida na hasara zake, lakini hadi sasa, na kama tutakavyoona baadaye, BIP47 inasimama kweli kutoka kwa wengine.


Toleo hili la utumiaji tena wa Address liko mbali na kupuuzwa katika Bitcoin. Kama unavyoona kwenye grafu iliyo hapa chini iliyochukuliwa kutoka kwa tovuti ya oxt.me, kiwango cha jumla cha matumizi ya Address na watumiaji wa Bitcoin kwa sasa ni 52%:

Grafu kutoka OXT.me inayoonyesha mabadiliko ya kiwango cha jumla cha matumizi ya Address kwenye mtandao wa Bitcoin.


![image](assets/2.webp)

_Mikopo: OXT_


Wengi wa utumiaji huu tena hutoka kwa kubadilishana, ambayo, kwa sababu za ufanisi na urahisi, hutumia tena Address sawa mara nyingi. Hadi sasa, BIP47 itakuwa suluhu bora ya kukomesha jambo hili kati ya kubadilishana. Hili lingesaidia kupunguza kiwango cha jumla cha matumizi ya Address bila kusababisha msuguano mwingi kwa huluki hizi.


Kipimo hiki cha kimataifa katika mtandao mzima kinafaa hasa katika kesi hii. Hakika, kutumia tena Address si tatizo kwa mtu anayejihusisha na mazoezi haya tu, bali pia kwa yeyote anayefanya miamala naye. Kupotea kwa faragha kwenye Bitcoin hufanya kama virusi, kuenea kutoka kwa mtumiaji hadi kwa mtumiaji. Kusoma kipimo cha kimataifa kwenye miamala yote ya mtandao huturuhusu kuelewa ukubwa wa jambo hili.


## Kanuni za BIP47 na PayNym.


BIP47 inalenga kutoa njia rahisi ya kupokea malipo mengi bila kutumia tena Address. Uendeshaji wake unategemea matumizi ya nambari ya malipo inayoweza kutumika tena.


Kwa hivyo, watumaji wengi wanaweza kutuma malipo mengi kwa msimbo mmoja wa malipo unaoweza kutumika tena wa mtumiaji mwingine, bila mpokeaji kuhitaji kutoa Address mpya isiyo na kitu kwa kila muamala mpya.


Mtumiaji anaweza kushiriki kwa uhuru msimbo wake wa malipo (kwenye mitandao ya kijamii, kwenye tovuti...) bila hatari ya kupoteza faragha, tofauti na kupokea kwa kawaida Address au ufunguo wa umma.

Ili kutekeleza Exchange, watumiaji wote wawili lazima wawe na Bitcoin Wallet yenye utekelezaji wa BIP47, kama vile PayNym kwenye Samourai Wallet au Sparrow Wallet. Kuunganishwa kwa misimbo ya malipo ya watumiaji hao wawili kutaanzisha chaneli ya siri kati yao. Ili kuanzisha idhaa hii ipasavyo, mtumaji lazima afanye shughuli kwenye Bitcoin Blockchain: shughuli ya arifa (Nitaelezea zaidi kuhusu hili baadaye).


Uhusiano wa misimbo ya malipo ya watumiaji hao wawili hutoa siri zilizoshirikiwa ambazo wao wenyewe generate idadi kubwa ya anwani za kipekee za Bitcoin zinazopokea (haswa 2^32). Kwa hiyo, kwa kweli, malipo na BIP47 haitumwa kwa msimbo wa malipo, lakini kwa anwani za kawaida kabisa, zinazotokana na kanuni za malipo za wahusika wanaohusika.


Nambari ya malipo hutumika kama kitambulisho pepe, kinachotokana na Wallet seed. Katika muundo wa derivation wa HD Wallet, msimbo wa malipo iko katika kina cha 3, katika ngazi ya akaunti ya Wallet.


![image](assets/3.webp)


Madhumuni ya utoaji wake yamebainishwa kama 47' (0x8000002F) kwa kurejelea BIP47. Kwa mfano, njia ya kupata nambari ya malipo inayoweza kutumika tena itakuwa: ** m/47'/0'/0'/**


Ili kukupa wazo la jinsi nambari ya malipo inavyoonekana, hii ndio yangu: **PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qDudE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j5j2nr*


Inaweza pia kusimba kama msimbo wa QR ili kuwezesha mawasiliano:


![image](assets/4.webp)


Kuhusu PayNym Boti, roboti hizo unazoona kwenye Twitter, ni viwakilishi tu vya kuona vya msimbo wako wa malipo, iliyoundwa na Samourai Wallet. Wao huzalishwa kwa kutumia kazi ya Hash, ambayo inawafanya kuwa karibu kipekee. Hii hapa yangu na kitambulisho chake: **+throbbingpond8B1**


![image](assets/5.webp)


Boti hizi hazina matumizi halisi ya kiufundi. Badala yake, hurahisisha mwingiliano kati ya watumiaji kwa kuunda utambulisho pepe wa kuona.


Kwa mtumiaji, mchakato wa kufanya malipo ya BIP47 kwa utekelezaji wa PayNym ni rahisi sana. Wacha tufikirie kuwa Alice anataka kutuma malipo kwa Bob:


1. Bob anashiriki msimbo wake wa QR au moja kwa moja msimbo wake wa malipo unaoweza kutumika tena. Anaweza kuiweka kwenye tovuti yake, kwenye mitandao yake mbalimbali ya kijamii ya umma, au kuituma kwa Alice kupitia njia nyingine ya mawasiliano.

2. Alice hufungua programu yake ya Samourai au Sparrow na kuchanganua au kubandika msimbo wa malipo wa Bob.

3. Alice anaunganisha PayNym yake na Bob ("Fuata" kwa Kiingereza). Operesheni hii inafanywa off-chain na inabaki bure kabisa.

4. Alice anaunganisha PayNym yake na Bob ("Connect" kwa Kiingereza). Operesheni hii inafanywa "On-Chain". Ni lazima Alice alipe ada za ununuzi wa Mining pamoja na ada isiyobadilika ya 15,000 Sats kwa huduma ya Samourai. Ada za huduma zitaondolewa kwa Sparrow. Hatua hii ndiyo tunaita muamala wa arifa.

5. Baada ya shughuli ya arifa kuthibitishwa, Alice anaweza kuunda muamala wa malipo wa BIP47 kwa Bob. Wallet yake ita generate kiotomatiki tupu mpya ikipokea Address ambayo ni Bob pekee ndiye aliye na ufunguo wa faragha.


Kufanya shughuli ya arifa, yaani, kuunganisha PayNym yake, ni sharti la lazima ili kufanya malipo ya BIP47. Hata hivyo, hili likifanywa, mtumaji anaweza kufanya malipo mengi kwa mpokeaji (haswa 2^32) bila kuhitaji kufanya shughuli mpya ya arifa.


Huenda umegundua kuwa kuna shughuli mbili tofauti za kuunganisha PayNyms pamoja: "fuata" na "unganisha". Operesheni ya uunganisho ("kontakt") inalingana na shughuli ya arifa ya BIP47, ambayo ni shughuli ya Bitcoin tu na habari fulani inayopitishwa kupitia pato la OP_RETURN. Kwa hivyo, inasaidia kuanzisha mawasiliano yaliyosimbwa kwa njia fiche kati ya watumiaji hao wawili ili kutoa siri za pamoja zinazohitajika ili kutoa anwani mpya tupu za kupokea.


Kwa upande mwingine, operesheni ya kuunganisha ("fuata" au "relier") inaruhusu kiungo kwenye Soroban, itifaki ya mawasiliano iliyosimbwa kwa msingi wa Tor, iliyotengenezwa mahususi na timu za Samourai.


Kwa muhtasari:



- Kuunganisha PayNyms mbili ("kufuata") ni bure kabisa. Husaidia kuanzisha mawasiliano yaliyosimbwa kwa njia fiche ya off-chain, hasa kwa kutumia zana shirikishi za shughuli za Samourai (Stowaway au StonewallX2). Operesheni hii ni maalum kwa PayNym na haijafafanuliwa katika BIP47.
- Kuunganisha PayNyms mbili hugharimu. Hii inahusisha kufanya shughuli ya arifa ili kuanzisha muunganisho. Gharama inajumuisha ada zozote za huduma, ada za muamala za Mining, na 546 Sats zilizotumwa kwa arifa ya mpokeaji Address ili kuwaarifu kuhusu kufunguliwa kwa njia. Operesheni hii inahusiana na BIP47. Baada ya kukamilika, mtumaji anaweza kufanya malipo mengi ya BIP47 kwa mpokeaji.


Ili kuunganisha PayNym mbili, lazima tayari zimeunganishwa.


## Mafunzo: Kwa kutumia PayNym.


Sasa kwa kuwa tumeona nadharia, hebu tujifunze mazoezi pamoja. Wazo la mafunzo yaliyo hapa chini ni kuunganisha PayNym yangu kwenye Sparrow yangu Wallet na PayNym yangu kwenye Samourai Wallet yangu. Mafunzo ya kwanza yanakuonyesha jinsi ya kufanya muamala kwa kutumia msimbo wa malipo unaoweza kutumika tena kutoka Samourai hadi Sparrow, na somo la pili linaeleza utaratibu sawa kutoka Sparrow hadi Samourai.


**Kumbuka:** Nilitekeleza mafunzo haya kwenye Testnet. Hizi sio bitcoins halisi.


### Kujenga muamala wa BIP47 na Samourai Wallet.


Ili kuanza, ni wazi unahitaji programu ya Samourai Wallet. Unaweza kuipakua moja kwa moja kutoka kwa Google Play Store au kwa faili ya APK inayopatikana kwenye tovuti rasmi ya Samourai.


Mara tu Wallet inapoanzishwa, ikiwa bado hujatuma ombi la PayNym yako kwa kubofya nyongeza (+) iliyo chini kulia, kisha kwenye "PayNym".


Hatua ya kwanza ya kufanya malipo ya BIP47 ni kupata msimbo wa malipo unaoweza kutumika tena kutoka kwa mpokeaji wetu. Kisha, tutaweza kuungana nao na baadaye kuunganisha:


![video](assets/6.mp4)


Mara tu shughuli ya arifa itakapothibitishwa, ninaweza kutuma malipo mengi kwa mpokeaji wangu. Kila muamala utafanywa kiotomatiki na Address mpya tupu ambayo mpokeaji ana funguo zake. Mpokeaji haitaji kuchukua hatua yoyote, kila kitu kinahesabiwa kwa upande wangu.


Hivi ndivyo jinsi ya kufanya muamala wa BIP47 kwenye Samourai Wallet:


![video](assets/7.mp4)


### Kujenga muamala wa BIP47 na Sparrow Wallet.


Kama ilivyo kwa Samourai, ni wazi unahitaji kuwa na programu ya Sparrow. Hii inapatikana kwenye kompyuta yako. Unaweza kuipakua kutoka kwa [tovuti rasmi](https://sparrowwallet.com/).


Hakikisha umethibitisha sahihi ya msanidi programu na uadilifu wa programu iliyopakuliwa kabla ya kuisakinisha kwenye mashine yako.


Unda Wallet na uombe PayNym yako kwa kubofya "Onyesha PayNym" kutoka kwenye menyu ya "Zana" kwenye upau wa juu:


![image](assets/8.webp)


Kisha, utahitaji kuunganisha na kuunganisha PayNym yako na ile ya mpokeaji wako. Ili kufanya hivyo, weka msimbo wao wa malipo unaoweza kutumika tena kwenye dirisha la "Tafuta Anwani", uwafuate, kisha ufanye shughuli ya arifa kwa kubofya "Unganisha Anwani":


![image](assets/9.webp)


Baada ya shughuli ya arifa kuthibitishwa, unaweza kutuma malipo kwa nambari ya malipo inayoweza kutumika tena. Hapa ni jinsi ya kufanya hivyo:


![video](assets/10.mp4)


Sasa kwa kuwa tumeweza kusoma kipengele cha vitendo cha utekelezaji wa PayNym wa BIP47, hebu tuone jinsi mifumo hii yote inavyofanya kazi na ni mbinu gani za siri zinazotumiwa.


## Utendaji wa ndani wa BIP47.


Ili kusoma mifumo ya BIP47, ni muhimu kuelewa muundo wa kiambishi cha kihierarkia (HD) Wallet, mifumo ya kupata jozi muhimu za watoto, pamoja na kanuni za kriptografia ya curve elliptic. Kwa bahati nzuri, unaweza kupata habari zote muhimu ili kuelewa sehemu hii kwenye blogi yangu:



- [Kuelewa njia za kupata Bitcoin Wallet](https://www.pandul.fr/post/comprendre-les-chemins-de-d%C3%A9rivation-d-un-portefeuille-Bitcoin)



- [Bitcoin Wallet - nukuu kutoka kwa kitabu pepe Bitcoin Democratized 2](https://www.pandul.fr/post/le-portefeuille-Bitcoin-extrait-ebook-Bitcoin-d%C3%A9mocratis%C3%A9-2)


### Nambari ya malipo inayoweza kutumika tena.


Kama ilivyoelezwa katika sehemu ya pili ya karatasi hii, nambari ya malipo inayoweza kutumika tena iko katika kina cha tatu cha HD Wallet. Kwa kiasi fulani inalinganishwa na xpub, katika uwekaji na muundo wake, na pia katika jukumu lake.


Hapa kuna sehemu tofauti zinazounda nambari ya malipo ya baiti 80:



- _Byte 0_: Toleo. Ikiwa unatumia toleo la kwanza la BIP47, byte hii itakuwa sawa na 0x01.
- _Byte 1_: Sehemu ndogo. Nafasi hii imehifadhiwa kwa ajili ya kutoa dalili za ziada katika kesi ya matumizi maalum. Ukitumia PayNym tu, baiti hii itakuwa sawa na 0x00.
- _Byte 2_: Usawa wa y. Baiti hii inaonyesha 0x02 au 0x03 kulingana na usawa (hata au nambari isiyo ya kawaida) ya thamani ya kiratibu y cha ufunguo wetu wa umma. Kwa maelezo zaidi kuhusu mazoezi haya, tafadhali soma hatua ya 1 ya sehemu ya "Address derivation" ya makala haya.
- _Kutoka kwa baiti 3 hadi baiti 34_: Thamani ya x. Baiti hizi zinaonyesha uratibu wa x wa ufunguo wetu wa umma. Muunganisho wa x na usawa wa y hutupa ufunguo wetu wa umma uliobanwa.
- _Kutoka kwa byte 35 hadi byte 66_: Msimbo wa mnyororo. Nafasi hii imehifadhiwa kwa msimbo wa mnyororo unaohusishwa na ufunguo wa umma uliotajwa hapo juu.
- _Kutoka kwa byte 67 hadi 79_: Padding. Nafasi hii imehifadhiwa kwa maendeleo yanayowezekana ya siku zijazo. Kwa toleo la 1, tunaijaza tu na sufuri ili kufikia baiti 80, ambayo ni saizi ya data ya pato la OP_RETURN.


Huu hapa ni uwakilishi wa heksadesimali wa nambari yangu ya malipo inayoweza kutumika tena, iliyowasilishwa katika sehemu iliyotangulia, yenye rangi zinazolingana na baiti zilizowasilishwa hapo juu:

Kisha, unahitaji pia kuongeza kiambishi awali "P" ili kutambua kwa haraka kuwa tunashughulikia msimbo wa malipo. Baiti hii ni 0x47.


**0x47010002a0716529bae6b36c5c9aa518a52f9c828b46ad8d907747f0d09dcd4d9a39e97c3c5f37c4 70c390d842f364086362f6122f412e2b0c7e7fc6e32287e364a7a36a00000000000000000000000000000000000.


Hatimaye, tunakokotoa hesabu ya hundi ya msimbo huu wa malipo kwa kutumia HASH256, ambayo ina maana ya kuharakisha mara mbili kwa chaguo za kukokotoa za SHA256. Tunapata baiti nne za kwanza za digest hii na kuziunganisha mwishoni (kwa waridi).


**0x47010002a0716529bae6b36c5c9aa518a52f9c828b46ad8d907747f0d09dcd4d9a39e97c3c5f37c470c3 90d842f364086362f6122f412e2b0c7e7fc6e32287e364a7a36a00000000000000000000000000000000000567080c4**


Nambari ya malipo iko tayari, sasa tunahitaji tu kuibadilisha kuwa Base 58:


**PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qDudE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j5j2nr*


Kama unaweza kuona, ujenzi huu unafanana kwa karibu na muundo wa ufunguo wa umma uliopanuliwa wa aina ya "xpub".


Wakati wa mchakato huu wa kupata nambari yetu ya malipo, tulitumia ufunguo wa umma uliobanwa na msimbo wa mnyororo. Elements hizi mbili ni matokeo ya utohozi wa kiama na kidaraja kutoka kwa Wallet seed, kufuatia njia ifuatayo ya utoho: m/47'/0'/0'/


Kwa maneno madhubuti, ili kupata ufunguo wa umma na msimbo wa msimbo wa msimbo wa malipo unaoweza kutumika tena, tutakokotoa ufunguo mkuu wa kibinafsi kutoka kwa seed, kisha tupate jozi ya watoto na fahirisi 47 + 2^31 (derivation ngumu). Kisha, tunapata jozi mbili zaidi za watoto kwa index 2^31 (derivation ngumu).


**Kumbuka:** ikiwa ungependa kupata maelezo zaidi kuhusu kupata jozi za funguo za mtoto ndani ya uamuzi wa ngazi ya Bitcoin Wallet, ninapendekeza utumie CRYPTO301.


### Mbinu ya kriptografia: Kitufe cha Elliptic Curve Diffie-Hellman Exchange (ECDH).


Mbinu ya kriptografia inayotumika katika msingi wa BIP47 ni ECDH (Elliptic-Curve Diffie-Hellman). Itifaki hii ni lahaja ya ufunguo wa kawaida wa Diffie-Hellman Exchange.


Diffie-Hellman, katika toleo lake la kwanza, ni itifaki kuu ya makubaliano iliyowasilishwa mnamo 1976 ambayo inaruhusu pande mbili, kila moja ikiwa na jozi ya funguo za umma na za kibinafsi, kuamua siri iliyoshirikiwa kwa kubadilishana habari juu ya njia isiyo salama ya mawasiliano.


![image](assets/11.webp)


Siri hii iliyoshirikiwa (ufunguo nyekundu) inaweza kisha kutumika kwa kazi zingine. Kwa kawaida, siri hii iliyoshirikiwa inaweza kutumika kusimba na kusimbua mawasiliano kupitia mtandao usio salama:


![image](assets/12.webp)


Ili kufikia Exchange hii, Diffie-Hellman hutumia hesabu ya moduli kukokotoa siri iliyoshirikiwa. Hapa kuna maelezo rahisi ya jinsi inavyofanya kazi:



- Alice na Bob wanakubaliana juu ya rangi ya kawaida, katika kesi hii, njano. Rangi hii inajulikana kwa kila mtu. Ni taarifa za umma.
- Alice anachagua rangi ya siri, katika kesi hii, nyekundu. Anachanganya rangi mbili, na kusababisha machungwa.
- Bob huchagua rangi ya siri, katika kesi hii, bluu ya teal. Anachanganya rangi mbili, na kusababisha anga ya bluu.
- Alice na Bob wanaweza Exchange rangi walizopata: machungwa na anga bluu. Exchange hii inaweza kutokea kwenye mtandao usio salama na inaweza kuzingatiwa na washambuliaji.
- Alice huchanganya rangi ya samawati iliyopokelewa kutoka kwa Bob na rangi yake ya siri (nyekundu). Anapata kahawia.
- Bob huchanganya rangi ya chungwa iliyopokelewa kutoka kwa Alice na rangi yake ya siri (teal blue). Pia hupata kahawia.


![image](assets/13.webp)


**Mikopo:** Wazo asilia: A.J. Toleo la Han VinckVector: FlugaalTafsiri: Dereckson, Kikoa cha Umma, kupitia Wikimedia Commons. https://commons.wikimedia.org/wiki/File:Diffie-Hellman_Key_Exchange_(fr).svg


Katika kurahisisha huku, rangi ya kahawia inawakilisha siri iliyoshirikiwa kati ya Alice na Bob. Inapaswa kufikiriwa kuwa kwa kweli, haiwezekani kwa mshambuliaji kutenganisha rangi ya machungwa na anga ya bluu ili kurejesha Alice au rangi za siri za Bob.


Sasa, hebu tujifunze utendakazi wake halisi. Kwa mtazamo wa kwanza, Diffie-Hellman inaweza kuonekana kuwa ngumu kufahamu. Kwa kweli, kanuni ya uendeshaji ni karibu kama mtoto. Kabla ya kuelezea utaratibu wake, nitakukumbusha haraka dhana mbili za hisabati ambazo tutahitaji (na kwa bahati mbaya, pia hutumiwa katika njia zingine nyingi za kriptografia).


1. Nambari kuu ni nambari asilia ambayo ina vigawanyiko viwili tu: 1 na yenyewe. Kwa mfano, nambari ya 7 ni ya msingi kwa sababu inaweza tu kugawanywa na 1 na 7 (yenyewe). Kwa upande mwingine, nambari ya 8 sio ya msingi kwa sababu inaweza kugawanywa na 1, 2, 4, na 8. Kwa hiyo ina si tu vigawanyiko viwili, lakini vigawanyiko vinne na vyema.

2. "Modulo" (inayoashiria "mod" au "%") ni operesheni ya hisabati ambayo inaruhusu nambari mbili kamili kurudisha sehemu iliyobaki ya mgawanyiko wa Euclidean wa nambari ya kwanza kwa nambari ya pili. Kwa mfano, 16 mod 5 ni sawa na 1.


Kitufe cha Diffie-Hellman Exchange kati ya Alice na Bob hufanya kazi kama ifuatavyo:



- Alice na Bob huamua nambari mbili za kawaida: p na g. p ni nambari kuu. Kadiri nambari hii p inavyokuwa kubwa, ndivyo Diffie-Hellman atakavyokuwa salama zaidi. g ni mzizi wa awali wa uk. Nambari hizi mbili zinaweza kuwasilishwa kwa maandishi wazi juu ya mtandao usio salama, ni sawa na rangi ya njano katika kurahisisha hapo juu. Alice na Bob wanahitaji tu kuwa na maadili sawa ya p na g.
- Mara tu vigezo vimechaguliwa, Alice na Bob kila mmoja huamua nambari ya siri ya nasibu peke yao. Nambari ya nasibu iliyopatikana na Alice inaitwa (sawa na rangi nyekundu) na nambari nasibu iliyopatikana na Bob inaitwa b (sawa na rangi ya teal). Nambari hizi mbili lazima zibaki siri.
- Badala ya kubadilishana nambari hizi a na b, kila mhusika atakokotoa A (herufi kubwa) na B (herufi kubwa) hivi kwamba:


A ni sawa na g iliyoinuliwa kwa nguvu ya modulo p:

**A = g^a % p**


B ni sawa na g iliyoinuliwa kwa nguvu ya b modulo p:

**B = g^b % p**



- Nambari hizi A (sawa na rangi ya machungwa) na B (sawa na rangi ya bluu ya anga) zitabadilishwa kati ya pande hizo mbili. Exchange inaweza kufanywa kwa maandishi wazi juu ya mtandao usio salama.
- Alice, ambaye sasa anajua B, atahesabu thamani ya z hivi kwamba:


z ni sawa na B iliyoinuliwa kwa nguvu ya modulo p:

**z = B^a % p**



- Kama ukumbusho, B = g^b % p. Kwa hivyo:

**z = B^a % p**

**z = (g^b)^a % p**


Kulingana na sheria za uwasilishaji:

**(x^n)^m = x^nm**


Kwa hivyo:

**z = g^ba % p**



- Bob, ambaye sasa anajua A, pia atahesabu thamani ya z kama ifuatavyo:


z ni sawa na A iliyoinuliwa kwa uwezo wa b modulo p:

**z = A^b % p**


Kwa hivyo:

**z = (g^a)^b % p**

**z = g^ab % p**

**z = g^ba % p**


Shukrani kwa usambazaji wa opereta wa modulo, Alice na Bob wanapata thamani sawa kabisa ya z. Nambari hii inawakilisha siri yao iliyoshirikiwa, ambayo ni sawa na rangi ya kahawia katika maelezo ya awali. Wanaweza kutumia siri hii iliyoshirikiwa kusimba kwa njia fiche mawasiliano kati yao kwenye mtandao usio salama.


![Diffie-Hellman Technical Operation Diagram](assets/14.webp)


Mshambulizi anayemiliki p, g, A, na B hataweza kukokotoa a, b, au z. Kutekeleza utendakazi huu kutahitaji kugeuza ubainishaji, jambo ambalo haliwezekani kufanyika isipokuwa kwa kujaribu uwezekano wote mmoja baada ya mwingine kwa kuwa tunafanya kazi na uga wenye kikomo. Hii itakuwa sawa na kukokotoa logarithmu bainifu, ambayo ni ulinganifu wa ufafanuzi katika kikundi chenye kikomo cha mzunguko.


Kwa hivyo, mradi tunachagua thamani kubwa za kutosha za a, b, na p, Diffie-Hellman ni salama. Kwa kawaida, na vigezo vya biti 2,048 (nambari yenye tarakimu 600 katika desimali), kupima uwezekano wote wa a na b hakutakuwa na maana. Hadi sasa, kwa nambari za ukubwa huu, algorithm inachukuliwa kuwa salama.


Hapa ndipo haswa ambapo kasoro kuu ya itifaki ya Diffie-Hellman iko. Ili kuwa salama, algorithm lazima itumie nambari kubwa. Kwa hivyo, algoriti ya ECDH sasa inapendelewa, ambayo ni lahaja ya Diffie-Hellman inayotumia mkunjo wa aljebra, hasa mkunjo wa duaradufu. Hii huturuhusu kufanya kazi na nambari ndogo zaidi huku tukidumisha usalama sawa, na hivyo kupunguza rasilimali za kukokotoa na kuhifadhi zinazohitajika.


Kanuni ya jumla ya algorithm inabaki sawa. Hata hivyo, badala ya kutumia nambari nasibu A na nambari A iliyokokotwa kutoka kwa upanuzi wa moduli, tutatumia jozi ya vitufe vilivyowekwa kwenye mkunjo wa duaradufu. Badala ya kutegemea usambaaji wa mwendeshaji wa modulo, tutatumia sheria ya kikundi kwenye mikunjo ya duaradufu, haswa ushirika wa sheria hii.

Ikiwa huna ujuzi wa jinsi funguo za kibinafsi na za umma zinavyofanya kazi kwenye mviringo wa mviringo, nitaelezea misingi ya njia hii katika sehemu sita za kwanza za makala hii.


Kwa muhtasari wa takriban, ufunguo wa kibinafsi ni nambari ya nasibu kati ya 1 na n-1 (ambapo n ni mpangilio wa curve), na ufunguo wa umma ni sehemu ya kipekee kwenye curve iliyoamuliwa na ufunguo wa kibinafsi kupitia nyongeza ya nukta na kurudia mara mbili kutoka kwa sehemu ya jenereta, kama ifuatavyo.


**K = k·G**


Ambapo K ni ufunguo wa umma, k ni ufunguo wa kibinafsi, na G ni sehemu ya jenereta.


Moja ya sifa za jozi hii muhimu ni kwamba ni rahisi sana kuamua K ikiwa unajua k na G, lakini kwa sasa haiwezekani kuamua k ikiwa unajua K na G. Ni kazi ya njia moja.


Kwa maneno mengine, unaweza kuhesabu ufunguo wa umma kwa urahisi ikiwa unajua ufunguo wa faragha, lakini haiwezekani kuhesabu ufunguo wa faragha ikiwa unajua ufunguo wa umma. Usalama huu kwa mara nyingine tena unatokana na kutowezekana kwa kukokotoa logarithm tofauti.


Tutatumia mali hii kurekebisha algoriti yetu ya Diffie-Hellman. Kwa hivyo, kanuni ya uendeshaji wa ECDH ni kama ifuatavyo.



- Alice na Bob wanakubaliana kuhusu mkunjo wa duaradufu ulio salama kwa njia fiche na vigezo vyake. Habari hii ni ya umma.
- Alice hutoa nambari ya nasibu ka, ambayo itakuwa ufunguo wake wa kibinafsi. Ufunguo huu wa faragha lazima ubaki kuwa siri. Anaamua ufunguo wake wa umma Ka kwa kuongeza na kuzidisha alama maradufu kwenye mduara uliochaguliwa wa duaradufu.


**Ka = ka·G**



- Bob pia hutoa nambari ya nasibu kb, ambayo itakuwa ufunguo wake wa kibinafsi. Anakokotoa ufunguo wa umma unaohusishwa Kb.


**Kb = kb·G**



- Alice na Bob Exchange funguo zao za umma za Ka na Kb kwenye mtandao wa umma usio salama.
- Alice anakokotoa pointi (x, y) kwenye mkunjo kwa kutumia ufunguo wake wa faragha ka kwenye ufunguo wa umma wa Bob Kb.


**(x, y) = ka·Kb**



- Bob anakokotoa pointi (x, y) kwenye mkunjo kwa kutumia ufunguo wake wa faragha kb kwenye ufunguo wa umma wa Alice Ka.


**(x, y) = kb·Ka**



- Alice na Bob wanapata sehemu sawa kwenye curve ya duaradufu. Siri iliyoshirikiwa itakuwa uratibu wa x wa hatua hii.


Wanapata siri ile ile iliyoshirikiwa kwa sababu:


**(x, y) = ka·Kb = ka·kb·G = kb·ka·G = kb·Ka**


Mshambulizi anayewezekana akiangalia mtandao wa umma usio salama anaweza tu kupata funguo za umma za kila mhusika na vigezo vilivyochaguliwa vya mkunjo. Kama ilivyoelezwa hapo awali, habari hizi mbili pekee haziruhusu uamuzi wa funguo za kibinafsi, hivyo mshambuliaji hawezi kufikia siri.

ECDH ni algorithm inayoruhusu ufunguo wa Exchange. Mara nyingi hutumiwa pamoja na njia zingine za kriptografia kufafanua itifaki. Kwa mfano, ECDH hutumiwa katika msingi wa TLS (Usafiri wa Layer Usalama), itifaki ya usimbaji na uthibitishaji inayotumika kwa usafiri wa mtandao wa Layer. TLS hutumia ECDHE kwa ufunguo wa Exchange, kibadala cha ECDH ambapo funguo ni za muda mfupi ili kutoa usiri unaoendelea. Kando na ECDHE, TLS pia hutumia algoriti ya uthibitishaji kama vile ECDSA, algoriti ya usimbaji fiche kama AES, na kazi ya Hash kama SHA256.


TLS inafafanua "s" katika "https" na ikoni ndogo ya kufunga unayoona kwenye kivinjari chako cha wavuti kwenye kona ya juu kushoto, ambayo inahakikisha mawasiliano yaliyosimbwa. Kwa hivyo, kwa sasa unatumia ECDH kwa kusoma makala hii, na pengine unaitumia kila siku bila kujua.


### Shughuli ya arifa


Kama tulivyogundua katika sehemu iliyotangulia, ECDH ni lahaja ya Diffie-Hellman Exchange inayohusisha jozi muhimu zilizoanzishwa kwenye mkunjo wa duaradufu. Kwa bahati nzuri, tuna jozi nyingi muhimu zinazofikia kiwango hiki katika pochi zetu za Bitcoin!


Wazo ni kutumia jozi muhimu kutoka kwa pochi za kidaraja za Bitcoin za pande zote mbili ili kuanzisha siri za pamoja na za muda mfupi kati yao. Ndani ya BIP47, ECDHE (Elliptic Curve Diffie-Hellman Ephemeral) inatumika badala yake.


ECDHE inatumika mwanzoni katika BIP47 kutuma msimbo wa malipo wa mtumaji kwa mpokeaji. Huu ndio shughuli maarufu ya arifa. Ili BIP47 itumike, pande zote mbili (mtumaji anayetuma malipo na mpokeaji anayepokea malipo) wanahitaji kufahamu msimbo wa malipo wa kila mmoja wao. Hii ni muhimu ili kupata funguo za muda mfupi za umma na kwa hivyo anwani maalum za kupokea.


Kabla ya Exchange hii, mtumaji tayari anajua nambari ya malipo ya mpokeaji kwa kuwa angeweza kuipata off-chain, kwa mfano, kutoka kwa tovuti yao au mitandao ya kijamii. Hata hivyo, huenda mpokeaji hajui nambari ya malipo ya mtumaji. Inahitaji kupitishwa kwao, vinginevyo hawataweza kupata funguo zao za ephemeral na kwa hiyo hawataweza kujua wapi bitcoins zao na kufungua fedha zao. Inaweza kupitishwa kwao off-chain, kwa kutumia mfumo mwingine wa mawasiliano, lakini hii inaweza kusababisha tatizo ikiwa Wallet itapatikana kutoka kwa seed.

Hakika, kama nilivyokwisha sema, anwani za BIP47 hazitolewi kutoka kwa seed ya mpokeaji (vinginevyo, itakuwa bora kutumia moja ya xpub zao moja kwa moja), lakini ni matokeo ya hesabu inayohusisha nambari ya malipo ya mpokeaji na nambari ya malipo ya mtumaji. Kwa hiyo, ikiwa mpokeaji hupoteza Wallet yao na anajaribu kurejesha kutoka kwa seed yao, watahitaji lazima kuwa na kanuni zote za malipo za watu ambao wamewatuma bitcoins kupitia BIP47.


Itawezekana kutumia BIP47 bila muamala huu wa arifa, lakini kila mtumiaji atahitaji kuhifadhi nakala za misimbo ya malipo ya wenzao. Hali hii itasalia kuwa ngumu kudhibitiwa hadi njia rahisi na thabiti ya kuunda, kuhifadhi na kusasisha nakala hizi ipatikane. Kwa hivyo shughuli ya arifa ni karibu lazima katika hali ya sasa ya mambo.


Kando na jukumu lake la kuhifadhi misimbo ya malipo, kama jina lake linavyopendekeza, muamala huu pia hutumika kama arifa kwa mpokeaji. Inamfahamisha mteja wao kwamba handaki limefunguliwa hivi punde.


Kabla ya kueleza kwa undani zaidi utendakazi wa kiufundi wa shughuli ya arifa, ningependa kuzungumza kidogo kuhusu mtindo wa faragha. Hakika, mtindo wa faragha wa BIP47 unahalalisha tahadhari fulani zilizochukuliwa wakati wa kuunda muamala huu wa awali.


Nambari ya malipo yenyewe haileti hatari moja kwa moja kwa faragha. Tofauti na muundo wa kawaida wa Bitcoin, unaoruhusu kuvunja mtiririko wa taarifa kati ya utambulisho wa mtumiaji na miamala, hasa kwa kutoweka funguo za umma bila majina, msimbo wa malipo unaweza kuhusishwa moja kwa moja na utambulisho. Hii sio lazima, lakini kiunga hiki sio hatari.


Hakika, msimbo wa malipo haupati moja kwa moja anwani zinazotumiwa kupokea malipo ya BIP47. Badala yake, anwani zinapatikana kwa kutumia ECDHE kati ya funguo za watoto za misimbo ya malipo ya pande zote mbili.


Kwa hivyo, msimbo wa malipo pekee hauleti hatari ya moja kwa moja kwa faragha kwa kuwa ni arifa ya Address pekee inayotokana nayo. Baadhi ya taarifa zinaweza kudhaniwa kutoka kwayo, lakini kwa kawaida mtu hawezi kujua unafanya naye miamala na nani.


Kwa hivyo ni muhimu kudumisha utengano mkali kati ya misimbo ya malipo ya watumiaji. Katika suala hili, hatua ya awali ya mawasiliano ya msimbo ni wakati muhimu kwa faragha ya malipo, na bado ni lazima kwa utendaji mzuri wa itifaki. Ikiwa mojawapo ya misimbo ya malipo inaweza kurejeshwa hadharani (kwa mfano, kutoka kwa tovuti), msimbo wa pili, yaani, msimbo wa mtumaji, haupaswi kuhusishwa na wa kwanza.


Kwa mfano, hebu tufikirie kuwa ninataka kutoa mchango kwa BIP47 kwa vuguvugu la amani la maandamano nchini Kanada:



- Shirika hili limechapisha nambari yake ya malipo moja kwa moja kwenye tovuti yake au majukwaa ya mitandao ya kijamii.
- Kwa hivyo kanuni hii inahusishwa na harakati.
- Narejesha nambari hii ya malipo.
- Kabla ya kuwatumia muamala, ni lazima nihakikishe kuwa wanafahamu msimbo wangu wa malipo wa kibinafsi, ambao pia unahusishwa na utambulisho wangu kwa vile ninautumia kupokea miamala kutoka kwa mitandao yangu ya kijamii.


Ninawezaje kuisambaza kwao? Nikituma kwao kwa kutumia njia ya kawaida ya mawasiliano, maelezo yanaweza kuvuja, na ninaweza kutambuliwa kama mtu anayeunga mkono harakati za amani.


Muamala wa arifa kwa hakika si suluhisho pekee la kutuma kwa siri msimbo wa malipo wa mtumaji, lakini kwa sasa unatimiza jukumu hili kikamilifu kwa kutumia safu nyingi za usalama.


Katika mchoro ulio hapa chini, mistari nyekundu inawakilisha wakati ambapo mtiririko wa habari lazima uvunjwe, na mishale nyeusi inawakilisha viungo visivyoweza kukataliwa ambavyo vinaweza kufanywa na mwangalizi wa nje:


![Privacy model diagram for reusable payment code](assets/15.webp)


Kwa kweli, kwa mfano wa faragha wa Bitcoin, mara nyingi ni vigumu kuvunja kabisa mtiririko wa habari kati ya jozi muhimu na mtumiaji, hasa wakati wa kufanya shughuli za mbali. Kwa mfano, katika kesi ya kampeni ya mchango, mpokeaji atahitajika kufichua Address au ufunguo wa umma kwenye tovuti yao au majukwaa ya mitandao ya kijamii. Matumizi sahihi ya BIP47, yaani, pamoja na shughuli ya arifa, hutatua suala hili kupitia ECDHE na usimbaji fiche Layer ambayo tutajifunza.


Ni wazi, mtindo wa kawaida wa faragha wa Bitcoin bado unazingatiwa katika kiwango cha funguo za muda mfupi za umma zinazotokana na uhusiano wa misimbo miwili ya malipo. Mifano mbili zinategemeana. Ningependa kuangazia hapa kwamba, tofauti na matumizi ya kawaida ya ufunguo wa umma kupokea bitcoins, nambari ya malipo inaweza kuhusishwa na utambulisho kwa sababu maelezo "Bob anafanya muamala na Alice" yamevunjwa wakati mwingine. Nambari ya malipo hutumiwa kwa anwani za malipo za generate, lakini kwa kuzingatia tu Blockchain, haiwezekani kuhusisha shughuli ya malipo ya BIP47 na nambari za malipo zilizotumiwa kuifanya.


### Ujenzi wa shughuli ya arifa


Sasa, hebu tuone jinsi shughuli hii ya arifa inavyofanya kazi. Hebu tufikirie kwamba Alice anataka kutuma pesa kwa Bob kwa kutumia BIP47. Katika mfano wangu, Alice anafanya kama mtumaji na Bob kama mpokeaji. Bob tayari amechapisha nambari yake ya malipo kwenye tovuti yake, kwa hivyo Alice tayari anafahamu msimbo wa malipo wa Bob.


1- Alice anakokotoa siri iliyoshirikiwa na ECDH:



- Yeye huchagua jozi ya funguo kutoka kwa HD Wallet yake iliyoko kwenye tawi tofauti na msimbo wake wa malipo. Kumbuka kwamba jozi hizi hazipaswi kuhusishwa kwa urahisi na arifa ya Alice Address au utambulisho wa Alice (angalia sehemu iliyotangulia).
- Alice anachagua ufunguo wa faragha kutoka kwa jozi hii. Tutaiita **a** (herufi ndogo).



- Alice anapata ufunguo wa umma unaohusishwa na arifa ya Bob Address. Ufunguo huu ni mtoto wa kwanza anayetokana na msimbo wa malipo wa Bob (faharasa 0). Tutaita ufunguo huu wa umma "B" (herufi kubwa). Ufunguo wa faragha unaohusishwa na ufunguo huu wa umma unaitwa "b" (herufi ndogo). "B" imedhamiriwa na kuongeza kwa uhakika na kurudia mara mbili kwenye curve ya mviringo kutoka "G" (kiini cha jenereta) na "b" (ufunguo wa kibinafsi).

**B = b·G**



- Alice anakokotoa sehemu ya siri "S" (herufi kubwa) kwenye mkunjo wa duaradufu kwa kuongeza nukta na kurudia maradufu, akitumia ufunguo wake wa kibinafsi "a" kwenye ufunguo wa umma wa Bob "B".

**S = a·B**



- Alice anakokotoa kipengele cha upofu "f" ambacho kitatumika kusimba msimbo wake wa malipo. Ili kufanya hivyo, atatumia generate nambari isiyo ya kawaida kwa kutumia kazi ya HMAC-SHA512. Kama ingizo la pili la chaguo hili la kukokotoa, anatumia thamani ambayo ni Bob pekee ataweza kupata: (x), ambayo ni kiratibu cha x cha sehemu ya siri iliyokokotwa hapo awali. Ingizo la kwanza ni (o), ambayo ni UTXO inayotumiwa kama ingizo la muamala huu (outpoint).

**f = HMAC-SHA512(o, x)**


2- Alice anabadilisha nambari yake ya malipo ya kibinafsi kuwa msingi wa 2 (binary).


3- Anatumia kipengele hiki cha upofu kama ufunguo wa kutekeleza usimbaji fiche linganifu kwenye mzigo wa malipo ya msimbo wake wa malipo. Algorithm ya usimbaji fiche inayotumika ni XOR tu. Operesheni iliyofanywa ni sawa na cipher ya Vernam, inayojulikana pia kama "pedi ya wakati mmoja":



- Alice kwanza anagawanya kipengele chake cha upofu katika sehemu mbili: byte 32 za kwanza zinaitwa "f1" na byte 32 za mwisho zinaitwa "f2". Kwa hivyo tunayo:

**f = f1 || f2**



- Alice hukokotoa maandishi ya sifuri (x') ya kiratibu cha x cha ufunguo wa umma (x) wa msimbo wake wa malipo, na kukokotoa maandishi ya siri (c') ya msimbo wake (c) kando. "f1" na "f2" hufanya kama funguo za usimbuaji, na operesheni ya XOR inatumiwa.

**x' = x XOR f1**

**c' = c XOR f2**



- Alice anabadilisha thamani halisi za abscissa ya ufunguo wa umma (x) na msimbo wa mnyororo (c) katika msimbo wake wa malipo na thamani zilizosimbwa (x') na (c').


Kabla ya kuendelea na maelezo ya kiufundi ya shughuli hii ya arifa, hebu tuchukue muda kujadili utendakazi wa XOR. XOR ni opereta mwenye busara kidogo kulingana na aljebra ya Boolean. Kwa kuzingatia uendeshaji wa bits mbili, inarudisha 1 ikiwa bits zinazolingana ni tofauti, na inarudi 0 ikiwa bits zinazolingana ni sawa. Hapa kuna jedwali la ukweli la XOR kulingana na maadili ya operesheni D na E:


| D   | E   | D XOR E |
| --- | --- | ------- |
| 0   | 0   | 0       |
| 0   | 1   | 1       |
| 1   | 0   | 1       |
| 1   | 1   | 0       |

Kwa mfano:


**0110 XOR 1110 = 1000**


Au:


**010011 XOR 110110 = 100101**


Kwa ECDH, matumizi ya XOR kama usimbaji fiche Layer yanashikamana haswa. Kwanza, shukrani kwa mwendeshaji huyu, usimbaji fiche ni wa ulinganifu. Hii humruhusu mpokeaji kusimbua msimbo wa malipo kwa ufunguo ule ule unaotumika kwa usimbaji fiche. Ufunguo wa usimbaji na usimbuaji hukokotolewa kutoka kwa siri iliyoshirikiwa kwa kutumia ECDH.


Ulinganifu huu unawezeshwa na sifa za mawasiliano na ushirika za opereta wa XOR:



- Tabia zingine:

-> D ⊕ D = 0

-> D ⊕ 0 = D



- Mawasiliano:

D ⊕ E = E ⊕ D



- Ushirika:

D ⊕ (E ⊕ Z) = (D ⊕ E) ⊕ Z = D ⊕ E ⊕ Z



- Ulinganifu:

Kama: D ⊕ E = L

Kisha: D ⊕ L = D ⊕ (D ⊕ E) = D ⊕ D ⊕ E = 0 ⊕ E = E

-> D ⊕ L = E

Kisha, mbinu hii ya usimbaji fiche inafanana sana na cipher ya Vernam (Padi ya Wakati Mmoja), algoriti pekee inayojulikana hadi sasa ambayo ina usalama usio na masharti (au kabisa). Ili sifa ya Vernam iwe na sifa hii, ufunguo wa usimbaji lazima uwe nasibu kabisa, uwe na ukubwa sawa na ujumbe, na utumike mara moja tu. Katika mbinu ya usimbaji fiche inayotumika hapa kwa BIP47, ufunguo hakika una ukubwa sawa na ujumbe, kipengele cha kupofusha ni sawa kabisa na upatanisho wa x-coordinate ya ufunguo wa umma na msimbo wa msimbo wa malipo. Ufunguo huu wa usimbaji hutumika mara moja tu. Walakini, ufunguo huu hautolewi kutoka kwa chanzo kamili bila mpangilio kwani ni HMAC. Ni badala ya pseudo-random. Kwa hiyo, sio cipher ya Vernam, lakini njia ni sawa.


Wacha turudi kwenye muundo wetu wa muamala wa arifa:


4- Kwa sasa Alice ana msimbo wake wa malipo na mzigo uliosimbwa kwa njia fiche. Ataunda na kutangaza muamala unaohusisha ufunguo wake wa umma "A" kama ingizo, matokeo ya arifa ya Bob Address, na toleo la OP_RETURN linalojumuisha msimbo wake wa malipo pamoja na mzigo uliosimbwa kwa njia fiche. Muamala huu ni shughuli ya arifa.


OP_RETURN ni Opcode, ambayo ni hati inayoashiria matokeo ya muamala wa Bitcoin kuwa batili. Leo, inatumika kutangaza au habari ya Anchor kwenye Bitcoin Blockchain. Inaweza kuhifadhi hadi baiti 80 za data ambazo zimerekodiwa kwenye mnyororo na hivyo kuonekana kwa watumiaji wengine wote.


Kama tulivyoona katika sehemu iliyotangulia, Diffie-Hellman inatumika kwa generate siri iliyoshirikiwa kati ya watumiaji wawili wanaowasiliana kupitia mtandao usio salama, ambayo inaweza kuzingatiwa na washambuliaji. Katika BIP47, ECDH hutumiwa kuwasiliana kwenye mtandao wa Bitcoin, ambao kwa asili ni mtandao wa mawasiliano wa uwazi unaozingatiwa na washambuliaji wengi. Siri iliyoshirikiwa inayokokotolewa kupitia ufunguo wa Diffie-Hellman Exchange kwenye kona ya duaradufu kisha hutumika kusimba maelezo ya siri yatakayotumwa: msimbo wa malipo wa mtumaji (Alice).


Hapa kuna mchoro uliotolewa kutoka kwa BIP47 ambao unaonyesha kile tulichoelezea hivi punde:


![Diagram Alice sends her masked payment code to Bob's notification address](assets/16.webp)


Mkopo: Misimbo ya Malipo Inayoweza Kutumika tena kwa Pochi za Kihierarkia, Justus Ranvier. https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki


Ikiwa tutalinganisha mchoro huu na kile nilichoelezea hapo awali:



- "Wallet Priv-Key" kwa upande wa Alice inalingana na: a.
- "Child Pub-Key 0" kwa upande wa Bob inalingana na: B.
- "Arifa ya Siri ya Pamoja" inalingana na: f.
- "Nambari ya Malipo Iliyofichwa" inalingana na msimbo wa malipo uliosimbwa kwa njia fiche, yaani, na mzigo uliosimbwa kwa njia fiche: x' na c'.
- "Muamala wa Arifa" ni muamala ambao una OP_RETURN.


Wacha turudie hatua ambazo tumepitia ili kufanya shughuli ya arifa:



- Alice anarejesha nambari ya malipo ya Bob na arifa Address.
- Alice anachagua UTXO ambayo ni yake katika HD yake Wallet na jozi za funguo zinazolingana.
- Anakokotoa sehemu ya siri kwenye curve ya duaradufu kwa kutumia ECDH.
- Anatumia sehemu hii ya siri kukokotoa HMAC, ambayo ni sababu inayopofusha.
- Anatumia kipengele hiki cha upofu ili kusimba kwa njia fiche mzigo wa malipo ya nambari yake ya malipo ya kibinafsi.
- Anatumia pato la muamala la OP_RETURN kuhamisha nambari ya malipo iliyofichwa kwa Bob.


Ili kuelewa vyema utendakazi wake, hasa utumiaji wa OP_RETURN, hebu tuchunguze shughuli ya arifa halisi pamoja. Nilifanya muamala wa aina hii kwenye Testnet, ambayo unaweza kuipata kwa kubofya hapa:


https://Mempool.space/fr/Testnet/tx/0e2e4695a3c49272ef631426a9fd2dae6ec3a469e3a39a3db51aa476cd09de2e


txid: **0e2e4695a3c49272ef631426a9fd2dae6ec3a469e3a39a3db51aa476cd09de2e**


![BIP47 Notification Transaction](assets/17.webp)


Mkopo: https://blockstream.info/


Kwa kutazama muamala huu, tunaweza kuona tayari kuwa ina ingizo moja na matokeo 4:



- Matokeo ya kwanza ni OP_RETURN ambayo ina nambari yangu ya malipo iliyofichwa.
- Toleo la pili la 546 Sats linaelekeza kwa arifa ya mpokeaji Address.
- Pato la tatu la 15,000 Sats linawakilisha ada ya huduma, kwani nilitumia Samourai Wallet kuunda muamala huu.
- Pato la nne la milioni mbili la Sats linawakilisha mabadiliko, yaani, tofauti iliyobaki kutoka kwa pembejeo yangu ambayo inarudi kwa Address nyingine iliyo yangu.


Kinachovutia zaidi kusoma ni dhahiri pato 0 kwa kutumia OP_RETURN. Wacha tuangalie kwa undani kile kilichomo:


![OP_RETURN Output of Notification Transaction BIP47](assets/18.webp)


Mkopo: https://blockstream.info/


Tunagundua hati ya hexadecimal ya pato: **6a4c50010002b13b2911719409d704ecc69f74fa315a6cb20fdd6ee39bc9874667703d67b164927b0e8 8f89f3f8b963549eab2533b5d7ed481a3bea7e953b546b4e91b6f50d80000000000000000000000000**


Katika hati hii, tunaweza kugawanya sehemu kadhaa:

Miongoni mwa opcodes, tunaweza kutambua 0x6a ambayo inarejelea OP_RETURN na 0x4c ambayo inarejelea OP_PUSHDATA1. Baiti inayofuata opcode hii inaonyesha ukubwa wa mzigo unaofuata. Inaonyesha 0x50, ambayo ni 80 byte.


Inayofuata inakuja nambari ya malipo iliyo na mzigo uliosimbwa kwa njia fiche.


Huu hapa ni msimbo wangu wa malipo uliotumika katika muamala huu:


Katika msingi wa 58: **PM8TJQCyt6ovbozreUCBrfKqmSVmTzJ5vjqse58LnBzKFFZTwny3KfCDdwTqAEYVasn11tTMPc2FJsFygFd3YzsHvwNXLEQNADgxeGn6MKTZ8Ugmin*


Katika msingi wa 16 (HEX): **4701000277507c9c17a89cfca2d3af554745d6c2db0e7f6b2721a3941a504933103cc42add94881210d6e 752a9abc8a9fa0070e85184993c4f643f1121dd807dd556d1dc00000000000000000000000008604e4db**


Tukilinganisha msimbo wangu wa malipo na OP_RETURN, tunaweza kuona kwamba HRP (ya kahawia) na hundi (ya rangi ya waridi) hazisambazwi. Hii ni kawaida, kwani habari hii imekusudiwa wanadamu.

Ifuatayo, tunaweza kutambua (katika Green) toleo (0x01), sehemu ndogo (0x00), na usawa wa ufunguo wa umma (0x02). Na, mwishoni mwa msimbo wa malipo, baiti tupu za rangi nyeusi (0x00) ambazo huruhusu pedi kufikia jumla ya baiti 80. Metadata hii yote inatumwa kwa maandishi wazi (haijasimbwa).

Hatimaye, tunaweza kuona kwamba x-coordinate ya ufunguo wa umma (katika bluu) na msimbo wa mnyororo (katika nyekundu) zimesimbwa kwa njia fiche. Hii inajumuisha mzigo wa malipo ya msimbo wa malipo.


### Inapokea muamala wa arifa.


Sasa kwa kuwa Alice ametuma muamala wa arifa kwa Bob, hebu tuone jinsi anavyoitafsiri.


Kama ukumbusho, ni lazima Bob aweze kufikia nambari ya malipo ya Alice. Bila habari hii, kama tutakavyoona katika sehemu inayofuata, hataweza kupata jozi muhimu zilizoundwa na Alice, na kwa hiyo, hawezi kufikia bitcoins zake zilizopokelewa na BIP47. Kwa sasa, upakiaji wa msimbo wa malipo wa Alice umesimbwa kwa njia fiche. Hebu tuone pamoja jinsi Bob anavyoichambua.


1- Bob hufuatilia shughuli zinazounda matokeo kwa arifa yake Address.

2- Wakati muamala una matokeo ya arifa yake Address, Bob huichanganua ili kuona ikiwa ina matokeo ya OP_RETURN ambayo yanatii kiwango cha BIP47.

3- Ikiwa baiti ya kwanza ya upakiaji wa OP_RETURN ni 0x01, Bob anaanza utafutaji wake wa siri inayowezekana iliyoshirikiwa na ECDH:



- Bob huchagua ufunguo wa umma katika ingizo la muamala. Hiyo ni, ufunguo wa umma wa Alice unaoitwa "A" na: **A = a·G**
- Bob anachagua ufunguo wa faragha "b" unaohusishwa na arifa yake ya kibinafsi Address: **b**
- Bob anakokotoa sehemu ya siri "S" (ECDH iliyoshirikiwa siri) kwenye mkunjo wa duaradufu kwa kuongeza na kurudia pointi, akitumia ufunguo wake wa kibinafsi "b" kwenye ufunguo wa umma wa Alice "A": **S = b·A**
- Bob huamua kipengele cha kupofusha "f" ambacho kitamruhusu kusimbua upakiaji wa msimbo wa malipo wa Alice. Kwa njia ile ile Alice aliihesabu hapo awali, Bob atapata "f" kwa kutumia HMAC-SHA512 hadi (x) thamani ya x ya kuratibu ya sehemu ya siri "S", na (o) UTXO inayotumiwa kama ingizo katika shughuli hii ya arifa: **f = HMAC-SHA512(o, x)**


4- Bob anatafsiri data katika OP_RETURN ya shughuli ya arifa kama msimbo wa malipo. Anasimbua tu upakiaji wa msimbo huu unaowezekana wa malipo kwa kutumia kipengele cha upofu "f".



- Bob hutenganisha kipengele cha upofu "f" katika sehemu mbili: byte 32 za kwanza za "f" zitakuwa "f1" na byte 32 za mwisho zitakuwa "f2".
- Bob anasimbua thamani iliyosimbwa ya x-coordinate (x') ya ufunguo wa umma wa msimbo wa malipo wa Alice:


**x = x' XOR f1**



- Bob anasimbua thamani ya msimbo uliosimbwa (c') wa msimbo wa malipo wa Alice:


**c = c' XOR f2**


5- Bob huangalia ikiwa thamani ya msimbo wa malipo wa Alice ni sehemu ya kikundi cha secp256k1. Ikiwa ndivyo, anaifasiri kama msimbo halali wa malipo. Vinginevyo, anapuuza shughuli hiyo.


Kwa kuwa sasa Bob anajua nambari ya malipo ya Alice, anaweza kumtumia hadi malipo 2^32 bila kuhitaji kufanya shughuli ya arifa kama hii tena.


Kwa nini hii inafanya kazi? Je, Bob anawezaje kubaini kigezo sawa na cha Alice na kusimbue msimbo wake wa malipo? Hebu tuchunguze mchakato wa ECDH kwa undani zaidi kulingana na kile tulichoelezea hivi punde.


Kwanza, tunashughulika na usimbaji fiche linganifu. Hii ina maana kwamba ufunguo wa usimbaji fiche na ufunguo wa kusimbua ni thamani sawa. Katika kesi hii, ufunguo katika shughuli ya arifa ni sababu ya upofu (f = f1 || f2). Alice na Bob wanahitaji kupata thamani sawa ya f bila kuisambaza moja kwa moja, kwani mshambulizi anaweza kuizuia na kusimbua maelezo ya siri.


Kipengele hiki cha upofu kinapatikana kwa kutumia HMAC-SHA512 kwa maadili mawili: x-kuratibu ya uhakika wa siri na UTXO inayotumiwa katika pembejeo ya shughuli. Kwa hivyo, Bob anahitaji kuwa na taarifa hizi mbili ili kusimbua upakiaji wa msimbo wa malipo wa Alice.


Kwa ingizo la UTXO, Bob anaweza kuipata kwa kutazama shughuli ya arifa. Kwa hatua ya siri, Bob atalazimika kutumia ECDH.


Kama inavyoonekana katika sehemu ya Diffie-Hellman, kwa kubadilishana funguo zao za umma na kutumia kwa siri funguo zao za faragha kwenye ufunguo wa umma wa wengine, Alice na Bob wanaweza kupata sehemu mahususi na ya siri kwenye kona ya duaradufu. Shughuli ya arifa inategemea utaratibu huu:


Jozi muhimu za Bob: **B = b·G**


Jozi muhimu ya Alice: **A = a·G**


Kwa sehemu ya siri S (x,y): **S = a·B = a·b·G = b·a·G = b·A**


![Diagram of generating a shared secret with ECDHE](assets/19.webp)

Kwa kuwa sasa Bob anajua nambari ya malipo ya Alice, ataweza kugundua malipo yake ya BIP47 na kupata funguo za faragha zinazozuia bitcoins zilizopokelewa.

![Bob interprets Alice's notification transaction](assets/20.webp)


Mkopo: Misimbo ya Malipo Inayoweza Kutumika tena kwa Pochi za Kihierarkia, Justus Ranvier. https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki


Ikiwa tutalinganisha mchoro huu na kile nilichokuelezea hapo awali:



- "Wallet Pub-Key" kwa upande wa Alice inalingana na: A.
- "Child Priv-Key 0" kwa upande wa Bob inalingana na: b.
- "Arifa ya Siri ya Pamoja" inalingana na: f.
- "Nambari ya Malipo Iliyofichwa" inalingana na msimbo wa malipo uliofichwa wa Alice, yaani, na mzigo uliosimbwa kwa njia fiche: x' na c'.
- "Muamala wa Arifa" ni muamala ambao una OP_RETURN.


Acha nifanye muhtasari wa hatua ambazo tumeziona kwa pamoja ili kupokea na kutafsiri shughuli ya arifa:



- Bob hufuatilia matokeo ya muamala kwa arifa yake Address.
- Anapogundua moja, anapata habari iliyo katika OP_RETURN.
- Bob huchagua ufunguo wa umma wa kuingiza na kukokotoa sehemu ya siri kwa kutumia ECDH.
- Anatumia hatua hii ya siri kuhesabu HMAC, ambayo ni sababu ya upofu.
- Anatumia kipengele hiki cha upofu ili kusimbua upakiaji wa msimbo wa malipo wa Alice ulio katika OP_RETURN.


### Shughuli ya malipo ya BIP47.


Hebu sasa tujifunze mchakato wa malipo na BIP47. Ili kukukumbusha hali ya sasa ya hali:



- Alice anafahamu msimbo wa malipo wa Bob, ambao aliupata kutoka kwa tovuti yake.



- Bob anafahamu msimbo wa malipo wa Alice kutokana na shughuli ya arifa.



- Alice atafanya malipo ya awali kwa Bob. Anaweza kutengeneza nyingi zaidi kwa njia ile ile.


Kabla ya kukuelezea mchakato huu, nadhani ni muhimu kukukumbusha ni faharasa zipi tunazoshughulikia kwa sasa:


Tunaelezea njia ya kupata msimbo wa malipo kama ifuatavyo: m/47'/0'/0'/.


Kina kinachofuata kinasambaza faharisi kama ifuatavyo:



- Jozi ya kwanza ya watoto wa kawaida (isiyo ngumu) hutumiwa kwa generate arifa Address tuliyojadili katika sehemu iliyotangulia: m/47'/0'/0'/0/.



- Jozi za funguo za watoto za kawaida hutumiwa ndani ya ECDH hadi generate BIP47 anwani za kupokea malipo, kama tutakavyoona katika sehemu hii: m/47'/0'/0'/ kutoka 0 hadi 2,147,483,647/.



- Jozi za funguo ngumu za watoto ni misimbo ya malipo ya muda mfupi: m/47'/0'/0'/ kutoka 0' hadi 2,147,483,647'/.

Kila wakati Alice anapotaka kutuma malipo kwa Bob, yeye hupata Address mpya ya kipekee, kwa mara nyingine tena kutokana na itifaki ya ECDH:


- Alice anachagua ufunguo wa kwanza wa faragha unaotokana na msimbo wake wa malipo unaoweza kutumika tena: **a**



- Alice anachagua ufunguo wa kwanza wa umma ambao haujatumika unaotokana na msimbo wa malipo wa Bob. Ufunguo huu wa umma, tutauita "B". Inahusishwa na ufunguo wa faragha "b" ambao ni Bob pekee anajua.

**B = b·G**



- Alice anakokotoa sehemu ya siri "S" kwenye mduara wa duaradufu kwa kuongeza na kurudisha pointi, akitumia ufunguo wake wa kibinafsi "a" kwenye ufunguo wa umma wa Bob "B":

**S = a·B**



- Kutoka kwa hatua hii ya siri, Alice atahesabu siri iliyoshirikiwa "s" (herufi ndogo). Ili kufanya hivyo, anachagua x-kuratibu ya hatua ya siri "S" inayoitwa "Sx", na hupitisha thamani hii kwenye kazi ya SHA256 Hash.

**s = SHA256(Sx)**


Usiamini. Thibitisha! Ikiwa unataka kuelewa kanuni za msingi za kazi ya Hash, utapata kile unachohitaji katika makala hii. Na ikiwa huamini NIST (uko sawa), na unataka kuelewa kwa undani jinsi SHA256 inavyofanya kazi, ninaelezea kila kitu katika makala hii kwa Kifaransa.



- Alice anatumia siri hizi za pamoja kukokotoa malipo ya Bitcoin inayopokea Address. Kwanza, anaangalia kuwa "s" iko ndani ya mpangilio wa secp256k1 curve. Ikiwa sivyo, anaongeza faharasa ya ufunguo wa umma wa Bob ili kupata siri nyingine iliyoshirikiwa.



- Pili, yeye hukokotoa kitufe cha umma "K0" kwa kuongeza alama "B" na "s·G" kwenye mduara wa duaradufu. Kwa maneno mengine, Alice anaongeza ufunguo wa umma unaotokana na msimbo wa malipo wa Bob "B" na pointi nyingine iliyohesabiwa kwenye mviringo wa mviringo kwa kuongeza na pointi mbili na "s" za siri zilizoshirikiwa kutoka kwa sehemu ya jenereta ya secp256k1 curve "G". Hoja hii mpya inawakilisha ufunguo wa umma, na tunaiita "K0":

**K0 = B + s·G**



- Kwa ufunguo huu wa umma "K0", Alice anaweza kupata tupu kupokea Address kwa njia ya kawaida (kwa mfano, SegWit V0 katika Bech32).


Alice akishapokea Address "K0" hii ya Bob, anaweza kutengeneza muamala wa kawaida wa Bitcoin kwa kuchagua UTXO ambayo ni yake kwenye tawi lingine la HD Wallet yake, na kuitumia kwa "K0" Address ya Bob.


![Alice sends bitcoins with BIP47 to Bob](assets/21.webp)


Mkopo: Misimbo ya Malipo Inayoweza Kutumika tena kwa Pochi za Kihierarkia, Justus Ranvier. https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki

Ikiwa tutalinganisha mchoro huu na kile nilichokuelezea hapo awali:



- "Child Priv-Key" kwa upande wa Alice inalingana na: a.
- "Child Pub-Key 0" kwa upande wa Bob inalingana na: B.
- "Siri ya Malipo 0" inalingana na: s.
- "Payment Pub-Key 0" inalingana na: K0.


Acha nifanye muhtasari wa hatua ambazo tumepitia pamoja kutuma malipo ya BIP47:



- Alice huchagua ufunguo wa kibinafsi wa mtoto kutoka kwa nambari yake ya malipo ya kibinafsi.
- Anakokotoa sehemu ya siri kwenye kona ya duaradufu kwa kutumia ECDH kutoka kwa ufunguo wa kwanza wa umma wa mtoto kutoka kwa msimbo wa malipo wa Bob.
- Anatumia sehemu hii ya siri kukokotoa siri iliyoshirikiwa na SHA256.
- Anatumia siri hii iliyoshirikiwa kukokotoa sehemu mpya ya siri kwenye mkunjo wa duaradufu.
- Anaongeza sehemu hii mpya ya siri kwa ufunguo wa umma wa Bob.
- Anapata ufunguo mpya wa umma wa muda mfupi ambao ni Bob pekee aliye na ufunguo wa faragha unaohusishwa.
- Alice anaweza kutuma muamala wa kawaida kwa Bob na ephemeral inayotokana na kupokea Address.


Ikiwa anataka kufanya malipo ya pili, atarudia hatua zilizo hapo juu, isipokuwa atachagua ufunguo wa pili unaotokana na umma kutoka kwa msimbo wa malipo wa Bob. Hiyo ni, ufunguo unaofuata ambao haujatumiwa. Kisha atakuwa na ya pili kupokea Address mali ya Bob, "K1".


![Alice derives three BIP47 receiving addresses for Bob](assets/22.webp)


Mkopo: Misimbo ya Malipo Inayoweza Kutumika tena kwa Pochi za Kihierarkia, Justus Ranvier. https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki


Anaweza kuendelea hivi na kupata hadi 2^32 anwani tupu za Bob.


Kwa mtazamo wa nje, kwa kuzingatia Bitcoin Blockchain, haiwezekani kinadharia kutofautisha malipo ya BIP47 kutoka kwa malipo ya kawaida. Huu hapa ni mfano wa malipo ya BIP47 kwenye Testnet:


https://blockstream.info/Testnet/tx/94b2e59510f2e1fa78411634c98a77bbb638e28fb2da00c9f359cd5fc8f87254


txid: **94b2e59510f2e1fa78411634c98a77bbb638e28fb2da00c9f359cd5fc8f87254**


Inaonekana kama muamala wa kawaida na ingizo lililotumika, pato la malipo la 210,000 Sats, na mabadiliko.


![Bitcoin payment transaction with BIP47](assets/23.webp)


Mkopo: https://blockstream.info/


### Kupokea malipo ya BIP47 na kupata ufunguo wa faragha.


Alice ametoka kufanya malipo yake ya kwanza kwa BIP47 Address tupu inayomilikiwa na Bob. Sasa hebu tuone jinsi Bob anavyopokea malipo haya. Pia tutaona ni kwa nini Alice hana uwezo wa kufikia ufunguo wa faragha wa Address ambao ametengeneza hivi punde, na jinsi Bob anavyopata ufunguo huu ili kutumia bitcoins ambazo amepokea hivi punde.


Mara tu Bob anapopokea muamala wa arifa kutoka kwa Alice, anapata kitufe cha umma cha BIP47 "K0" hata kabla hajatuma malipo yoyote kwake. Kwa hivyo anaangalia malipo yoyote kwa Address inayohusika. Kwa hakika, mara moja hupata anwani kadhaa ambazo atazingatia (K0, K1, K2, K3 ...). Hivi ndivyo anavyopata ufunguo huu wa umma "K0":



- Bob huchagua ufunguo wa kibinafsi wa mtoto wa kwanza unaotokana na msimbo wake wa malipo. Ufunguo huu wa kibinafsi unaitwa "b". Inahusishwa na kitufe cha umma "B" ambacho Alice alitumia katika hatua ya awali: **b**



- Bob anachagua ufunguo wa kwanza wa umma unaotokana na Alice kutoka kwa msimbo wake wa malipo. Ufunguo huu unaitwa "A". Inahusishwa na ufunguo wa faragha "a" ambao Alice alitumia katika hesabu zake, na ni Alice pekee anayefahamu. Bob anaweza kutekeleza mchakato huu kwa sababu anajua msimbo wa malipo wa Alice ambao ulitumwa kwake pamoja na shughuli ya arifa.

**A = a·G**



- Bob anakokotoa sehemu ya siri ya "S" kwa kuongeza na kuzidisha pointi maradufu kwenye mviringo wa mviringo, akitumia ufunguo wake wa kibinafsi "b" kwenye ufunguo wa umma wa Alice "A". Hapa tunatumia ECDH, ambayo inathibitisha kwamba hatua hii "S" itakuwa sawa kwa Bob na Alice.

**S = b·A**



- Kama vile Alice alivyofanya, Bob hutenganisha kiratibu cha x cha nukta hii "S". Tumeiita thamani hii "Sx". Anapitisha thamani hii kupitia kazi ya SHA256 ili kupata "s" za siri zilizoshirikiwa (herufi ndogo).

**s = SHA256(Sx)**



- Kwa njia sawa na Alice, Bob anakokotoa nukta "s·G" kwenye mkunjo wa duaradufu. Kisha, anaongeza sehemu hii ya siri kwa ufunguo wake wa umma "B". Kisha anapata nukta mpya kwenye curve ya mviringo ambayo anaitafsiri kama ufunguo wa umma "K0":

**K0 = B + s·G**


Mara tu Bob ana ufunguo huu wa umma "K0", anaweza kupata ufunguo wa kibinafsi unaohusishwa ili kutumia bitcoins zake. Yeye ndiye pekee anayeweza generate nambari hii.



- Bob anaongeza ufunguo wa faragha wa mtoto wake "b" kutoka kwa nambari yake ya malipo ya kibinafsi. Ni yeye pekee anayeweza kupata thamani ya "b". Kisha, anaongeza "b" kwa siri iliyoshirikiwa "s" ili kupata k0, ufunguo wa kibinafsi wa K0: ** k0 = b + s**



- Shukrani kwa sheria ya kikundi ya curve ya mviringo, Bob anapata ufunguo wa faragha unaolingana na ufunguo wa umma unaotumiwa na Alice. Kwa hivyo tunayo: **K0 = k0·G**


![Bob generates his BIP47 receiving addresses](assets/24.webp)


Mkopo: Misimbo ya Malipo Inayoweza Kutumika tena kwa Pochi za Kihierarkia, Justus Ranvier. https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki


Ikiwa tutalinganisha mchoro huu na kile nilichokuelezea hapo awali:



- "Child Priv-Key 0" kwa upande wa Bob inalingana na: b.



- "Child Pub-Key 0" kwa upande wa Alice inalingana na: A.



- "Siri ya Malipo 0" inalingana na: s.



- "Payment Pub-Key 0" inalingana na: K0.



- "Malipo ya Priv-Ufunguo 0" inalingana na: k0.


Acha nifanye muhtasari wa hatua ambazo tumeona pamoja ili kupokea malipo ya BIP47 na kukokotoa ufunguo wa faragha unaolingana:



- Bob huchagua ufunguo wa kwanza wa kibinafsi wa mtoto kutoka kwa nambari yake ya malipo ya kibinafsi.



- Anakokotoa sehemu ya siri kwenye mkunjo wa duaradufu kwa kutumia ECDH kutoka kwa ufunguo wa kwanza wa umma wa mtoto kutoka kwa msimbo wa mnyororo wa Alice.



- Anatumia sehemu hii ya siri kukokotoa siri iliyoshirikiwa na SHA256.



- Anatumia siri hii iliyoshirikiwa kukokotoa sehemu mpya ya siri kwenye curve ya duaradufu.



- Anaongeza sehemu hii mpya ya siri kwa ufunguo wake wa kibinafsi wa umma.



- Anapata ufunguo mpya wa umma wa muda mfupi, ambao Alice atamtumia malipo ya kwanza.



- Bob hukokotoa ufunguo wa faragha unaohusishwa na ufunguo huu wa umma wa muda mfupi kwa kuongeza ufunguo wa faragha wa mtoto wake kutoka kwa nambari yake ya malipo na siri iliyoshirikiwa.


Kwa kuwa Alice hawezi kupata "b," ufunguo wa faragha wa Bob, hawezi kubainisha k0, ufunguo wa faragha unaohusishwa na BIP47 ya Bob kupokea Address.


Kwa utaratibu, tunaweza kuwakilisha hesabu ya siri iliyoshirikiwa "S" kama ifuatavyo:


![Calculation of the shared secret with ECDHE](assets/25.webp)


Siri iliyoshirikiwa inapopatikana kwa ECDH, Alice na Bob wanakokotoa ufunguo wa umma wa malipo wa BIP47 "K0," na Bob pia anakokotoa ufunguo wa faragha unaohusishwa "k0":


![Derivation of the BIP47 receiving address from the shared secret](assets/26.webp)


### Kurejesha malipo ya BIP47.


Kwa kuwa Bob anafahamu msimbo wa malipo unaoweza kutumika tena wa Alice, tayari ana taarifa zote muhimu za kumrejeshea pesa. Hatakuwa na haja ya kuwasiliana na Alice ili kuuliza maelezo yoyote. Atamjulisha kwa urahisi na shughuli ya arifa, hasa ili aweze kurejesha anwani zake za BIP47 kwenye seed yake, na kisha anaweza pia kumtumia hadi malipo 2^32.

Kisha Bob anaweza kumlipa Alice kama vile alivyomtumia malipo. Majukumu yamebadilishwa:


![Bob sends a refund to Alice with BIP47](assets/27.webp)


Mkopo: Misimbo ya Malipo Inayoweza Kutumika tena kwa Pochi za Kihierarkia, Justus Ranvier. https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki


Sasa unajua ins na nje ya suluhisho hili nzuri ambalo BIP47 inawakilisha.


## Matumizi yanayotokana na PayNym.


Utekelezaji wa BIP47 hii kwenye Samourai Wallet umesababisha PayNyms, vitambulishi vinavyokokotolewa kutoka kwa misimbo ya malipo ya watumiaji. Leo, manufaa yao huenda mbali zaidi ya matumizi ya BIP47.


Timu ya Samourai inaendeleza taratibu mfumo mzima wa zana na huduma kulingana na PayNym ya mtumiaji. Miongoni mwa hizi, ni dhahiri kuna zana zote za matumizi zinazoruhusu kuboresha faragha ya mtumiaji kwa kuongeza entropy kwenye shughuli, na hivyo kuongeza ukanushaji unaokubalika.


Matumizi ya pamoja ya Soroban, mtandao wa mawasiliano uliosimbwa kwa njia fiche kulingana na Tor, na PayNyms yameboresha sana matumizi ya mtumiaji wakati wa kuunda miamala shirikishi, huku tukidumisha kiwango kizuri cha usalama. Kwa hivyo, ni rahisi kufanya shughuli za Stowaway (PayJoin) na StonewallX2 bila kufanya ubadilishanaji mwingi wa miamala ambayo haijasainiwa inayohitajika kuanzisha shughuli kama hiyo ya ushirikiano.


Tofauti na matumizi ya BIP47, kwa kuwa miamala hii shirikishi haihitaji muamala wa arifa, inatosha kuunganisha PayNyms ili kutumia zana hizi. Hakuna haja ya kuwaunganisha.


Ikiwa unataka kujifunza zaidi kuhusu shughuli za ushirikiano, na kwa upana zaidi kuhusu zana zote za matumizi za Samourai Wallet, unaweza kusoma sehemu ya "Zana za Kutumia" katika makala hii. Utapata maelezo ya kiufundi na mafunzo ya kina kwa kila chombo.


Kando na miamala hii shirikishi, imeonekana hivi majuzi kuwa timu ya Samourai inashughulikia itifaki ya uthibitishaji iliyounganishwa na PayNym: Auth47. Zana hii tayari imetekelezwa na inaruhusu, kwa mfano, uthibitishaji na PayNym kwenye tovuti inayokubali njia hii. Katika siku zijazo, nadhani kuwa zaidi ya uwezekano huu wa uthibitishaji kwenye wavuti, Auth47 itakuwa sehemu ya mradi mkubwa karibu na mfumo ikolojia wa BIP47/PayNym/Samourai. Labda itifaki hii itatumika kuboresha zaidi uzoefu wa mtumiaji wa Samourai Wallet, hasa katika matumizi ya zana za matumizi. Inabakia kuonekana ...


## Maoni yangu ya kibinafsi juu ya BIP47.


Kwa wazi, hasara kuu ya BIP47 ni shughuli ya arifa. Inapelekea mtumiaji kulazimika kutumia ada kwa Mining yake, ambayo inaweza kuwaudhi baadhi. Walakini, hoja ya "spam" kwenye Bitcoin Blockchain haikubaliki kabisa. Yeyote anayelipa ada za muamala wake lazima aweze kuirekodi kwenye Ledger, bila kujali madhumuni yake. Kudai vinginevyo ni kutetea udhibiti.


Inawezekana kwamba katika siku zijazo, suluhu zingine za bei nafuu zitapatikana ili kuwasiliana na msimbo wa malipo wa mtumaji kwa mpokeaji, na kwa mpokeaji kuihifadhi kwa usalama. Lakini kwa sasa, shughuli ya arifa inasalia kuwa suluhisho na maelewano machache zaidi.


Hasara hii inasalia kuwa kidogo wakati wa kuzingatia faida zote za BIP47. Miongoni mwa mapendekezo yote yaliyopo ya kutatua tatizo hili la utumiaji tena wa Address, inaonekana kwangu kama suluhisho bora zaidi.


Kama ilivyoelezwa hapo awali, matumizi mengi ya Address yanatokana na kubadilishana. BIP47 ndio suluhisho pekee la busara ambalo hutatua shida hii kwenye chanzo chake. Pendekezo lolote linalolenga kupunguza idadi ya matumizi tena ya Address linapaswa kuzingatia kipengele hiki na kurekebisha suluhisho kwa chanzo kikuu cha tatizo.


Kwa upande wa utumiaji, ingawa kazi zake za ndani ni ngumu sana, utaratibu wa malipo wa BIP47 ni wa moja kwa moja. Kwa hivyo, misimbo ya malipo inayoweza kutumika tena inaweza kupitishwa kwa urahisi, hata na watumiaji wapya.


Kwa upande wa faragha, BIP47 inavutia sana. Kama nilivyoeleza katika sehemu ya shughuli ya arifa, msimbo wa malipo hauonyeshi taarifa yoyote kuhusu anwani za muda mfupi zinazotolewa. Kwa hivyo huvunja mtiririko wa maelezo kati ya shughuli ya Bitcoin na kitambulisho cha mpokeaji, tofauti na matumizi ya jadi ya Address inayopokea.


Na zaidi ya yote, utekelezaji wa PayNym wa BIP47 hufanya kazi! Imepatikana kwenye Samourai Wallet tangu 2016 na kwenye Sparrow Wallet tangu mwanzoni mwa mwaka huu. Sio mradi wa kisayansi, lakini suluhisho ambalo limejaribiwa jana na linafanya kazi kikamilifu leo.


Tunatumahi, katika siku zijazo, misimbo hii ya malipo inayoweza kutumika tena itapitishwa na watendaji wa mfumo ikolojia, kutekelezwa katika programu ya Wallet, na kutumiwa na Bitcoiners.


Suluhisho lolote chanya la ufaragha wa mtumiaji lazima lijadiliwe, lisukumwe na kulindwa, ili Bitcoin isiwe uwanja wa michezo wa CA na zana ya ufuatiliaji ya serikali.

Alifikiria jinsi alivyokuwa akiteswa na kutukanwa kila mahali, na sasa akasikia kila mtu akisema kwamba yeye ndiye mrembo zaidi ya ndege hao wote warembo! Na hata elderberry akainamisha matawi yake kwake, na jua likaeneza mwanga wa joto na mzuri! Kisha manyoya yake yakavimba, shingo yake nyembamba ikanyooka, na akasema kwa moyo wote, "Ningewezaje kuota furaha nyingi wakati nilikuwa bata mdogo tu mbaya."


## Ili kwenda zaidi:



- Kuelewa na kutumia CoinJoin kwenye Bitcoin.



- Kuelewa njia za kupatikana kwa Bitcoin Wallet.



- Inasakinisha na kutumia nodi yako ya RoninDojo Bitcoin.


### Rasilimali za nje na shukrani:


Shukrani kwa LaurentMT na Théo Pantamis kwa dhana nyingi walizonieleza, ambazo nilitumia katika makala hii. Natumai nimewafikisha kwa usahihi.


Asante kwa Fanis Michalakis kwa kusahihisha maandishi haya na ushauri wake wa kitaalamu.



- https://bitcoiner.guide/paynym/
- https://github.com/Bitcoin/bips/blob/master/bip-0047.mediawiki
- https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman
- https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman_bas%C3%A9_sur_les_courbes_elliptiques
- https://security.stackexchange.com/questions/46802/what-is-the-difference-between-dhe-and-ecdh#:~:text=The%20difference%20between%20DHE%20and%20ECDH%20in%20two%20bullet%2020type2020type20bullet%2020type20020020120120120,ge20bullet%20type2020020202020DHE20between%.
- https://commandlinefanatic.com/cgi-bin/showarticle.cgi?article=art060
- https://ee.stanford.edu/~hellman/publications/24.pdf
- https://www.researchgate.net/publication/317339928_A_study_on_diffie-hellman_key_exchange_protocols