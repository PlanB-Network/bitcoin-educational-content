---
name: COLDCARD Q - Key Teleport
description: Teleport muhimu ni nini na ninaitumiaje?
---

![cover](assets/cover.webp)




![video](https://www.youtube.com/watch?v=Bg0r0DQVcDg)




![video](https://www.youtube.com/watch?v=BRpBiK-F8VU)



Je, ni kipengele cha **Muhimu Teleport** kinachotolewa na Coinkite iliyo na kifaa chake kikuu cha ColdCardQ?



**Muhimu Teleport** hukuwezesha kuhamisha kwa usalama data ya siri kati ya 2 ColdCardQs. Njia ya usambazaji haihitaji hata kusimbwa kwa njia fiche, na inaweza kuwa ya umma.



Hii inaweza kutumika kuhamisha:





- Vifungu vya maneno vya **gW-0** (Nyimbo kuu ya seed ya ColdCard Q au siri zilizohifadhiwa katika [seed Vault] ya ColdCardQ)(https://coldcard.com/docs/temporary-seeds/#seed-vault).
- **madokezo ya siri na manenosiri**: hii inaweza kuwa siri yoyote au saraka nzima ya [Vidokezo Salama na Manenosiri] (https://coldcard.com/docs/secure_notes/) kwenye ColdCardQ yako.
- **chelezo ya ColdCardQ yako yote**: ColdCardQ inayopokea nakala hii lazima isiwe na seed Master ili hii ifanye kazi.
- gW-3 (**Miamala ya Bitcoin Iliyotiwa Saini kwa Kiasi**) kama sehemu ya mpango wa sahihi nyingi.



Hii inakuhitaji usasishe [kidhibiti kifaa chako hadi toleo la v1.3.2Q](https://coldcard.com/docs/upgrade/) au toleo jipya zaidi.



## Ninawezaje kutumia Key Teleport?



### 1- Kuhamisha aina yoyote ya data



Hapa, tutaangalia uhamisho wa sentensi za seed, madokezo, manenosiri, au uhamisho mzima wa chelezo ya ColdCardQ. Kesi ya uhamisho wa PSBT kwa miamala ya saini nyingi itashughulikiwa baadaye.



#### Tayarisha kifaa kupokea siri



Katika menyu **"Zana/Zana**" kwenye ColdCardQ yako, chagua **"Ufunguo wa Teleport (anza) "**.


Kwenye skrini inayofuata, nenosiri la tarakimu 8 linapendekezwa, hapa "20420219". Utahitaji kuwasiliana nenosiri hili kwa mtumaji. Tumia sms, kwa mfano, kutuma nenosiri hili, au mfumo wako salama wa ujumbe, au hata simu ya sauti.



Kisha ubofye kitufe cha **"Ingiza**" kwenye ColdCardQ yako ili kuendelea na hatua inayofuata.




![CCQ-key-teleport](assets/fr/01.webp)




Msimbo wa QR unatolewa kwenye skrini. Kwa mara nyingine tena, utahitaji kuwasiliana na msimbo huu wa QR kwa "mtumaji" wa ColdCardQ. Njia rahisi zaidi ya kufanya hivyo ni kupitia Hangout ya Video.



**USITUMIE MSIMBO HII WA QR KUPITIA KITUO ILE kile kile ILICHOTUMIA KUTUMA NENOSIRI ILIYOPITA YENYE TATU 8**.



![CCQ-key-teleport](assets/fr/02.webp)



*Kwa wale ambao mna nia, hebu jaribu kuelewa utaratibu wa msingi unaoruhusu siri kuhamishwa kwenye chaneli zisizo salama*



*Tunachofanya hapa ni kuanzisha uhamishaji wa siri kupitia mbinu ya Diffie-Hellman, iliyojumuishwa katika kozi ya BTC204 ambayo nimejumuisha hapa chini*



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

*Kwa sasa tunayo:*




- ilizalisha jozi za vitufe vya muda mfupi (ya umma/faragha mtawalia Ka na ka na Ka=G.ka, G ikiwa sehemu ya jenereta ya ECDH), na nenosiri la tarakimu **8**.
- alitumia nenosiri hili kusimba ufunguo wa umma (Ka) kupitia AES-256-CTR, kisha akasambaza nenosiri hili kupitia njia ya mawasiliano A hadi "kutuma" **ColdCardQ**.
- hatimaye, tulituma pakiti iliyosimbwa kwa njia fiche kwa mtumaji kupitia msimbo wa QR ulio hapo juu, kwa kutumia chaneli ya pili ya mawasiliano **B** tofauti na ya **1**.



#### Andaa kifaa kitakachotuma siri



Kutoka kwenye kifaa kinachotuma, bofya kitufe cha **"QR "** ili kuchanganua msimbo wa QR uliotumwa kwako na kifaa kinachopokea, kisha uweke nenosiri la tarakimu 8 ulilopokea katika hatua ya awali kupitia kituo tofauti. Sasa tuko tayari kuanza kutuma data kutoka kwa kifaa cha "kutuma".



**Tafadhali usiingize nenosiri lenye tarakimu 8 kimakosa, kwani hakuna ujumbe wa hitilafu utakaoonyeshwa na mchakato utaendelea. Hata hivyo, uhamishaji wa mwisho wa data utashindwa na itabidi uanze tena**.



![CCQ-key-teleport](assets/fr/03.webp)



*Kwa wanaotaka kujua zaidi miongoni mwenu, hebu tuangalie tena kile tunachofanya kuhusu mfumo wa siri na uhamisho wa siri:*




- tuliingiza data iliyosimbwa kwa kuchanganua msimbo wa QR kwenye kifaa kinachopokea.
- kisha tukasimbua kwa kutumia nenosiri la tarakimu 8 lililotumwa kwetu kupitia kituo cha pili.
- kwa hivyo tunamiliki ufunguo wa umma (Ka) uliotolewa na mpokeaji mwanzoni.
- Kisha tunagenerate jozi mpya ya vitufe vya muda mfupi (Kb/kb, na Kb=G.kb) kwenye kifaa cha kutuma, ambacho tunatumia kutumia ECDH kwa Ka. Kwa hivyo tunafanya operesheni kb.Ka=Ks , ambapo Ks inaitwa **"Ufunguo wa Kipindi"**.




Sasa unaombwa kuchagua asili ya siri zitakazotumwa kati ya 2 ColdCardQs (maelezo ya siri, nenosiri, chelezo kamili, mbegu zilizo kwenye kuba yako, bwana wa kifaa cha seed).



![CCQ-key-teleport](assets/fr/04.webp)



Hapa siri yetu itakuwa ujumbe mfupi kwa kuchagua **"Ujumbe wa Maandishi ya Haraka "**. Andika ujumbe wako (kwetu "PlanB Network rocks") kisha ubonyeze **"INGIA "**.


Kisha kifaa hutoa nenosiri jipya lisilo la kawaida linaloitwa **"Nenosiri la Teleport "** , katika mfano "NE XG BT SK".



![CCQ-key-teleport](assets/fr/05.webp)



Bonyeza **"ENTER "** na utawasilishwa na msimbo mpya wa QR. Ichanganue na kifaa kinachopokea. Na kwenye njia tofauti ya mawasiliano, sambaza **"Nenosiri la Simu "** kwa mpokeaji.



![CCQ-key-teleport](assets/fr/06.webp)



*Hapa tena, kwa wadadisi, katika hatua hii:*




- baada ya kuchagua siri za kutumwa, tuna generate nenosiri jipya la random linaloitwa **"Nenosiri la Teleport"**.
- kisha tunasimba siri kupitia AES-256-CTR kwa kutumia **"Ufunguo wa Kipindi"**, "Ks", uliotolewa katika hatua ya awali.
- tunaweka kiambishi awali pakiti ambayo tayari imesimbwa kwa njia fiche kwa **"Ufunguo wa Kipindi "** kwa ufunguo wetu wa umma wa Kb, kisha uongeze usimbaji zaidi wa Layer wa AES-256-CTR kwa **"Nenosiri la Simu "**. Jambo zima basi limesimbwa kama msimbo wa QR




#### Maliza uhamishaji wa siri kwa kifaa kinachopokea



Bonyeza kitufe cha **"QR "** ili kuchanganua msimbo wa QR unaowasilishwa na kifaa kinachotuma kupitia kituo cha visio. Utaulizwa kuingiza **"Nenosiri la Teleport "** kwetu" NE XG BT SK ".



![CCQ-key-teleport](assets/fr/07.webp)





Kisha data hutambulishwa na kufanywa ieleweke kwa kifaa kinachopokea. Ujumbe uliopokelewa kwa hakika ni "PlanB Network rocks". Ni hayo tu.



![CCQ-key-teleport](assets/fr/08.webp)



*Ni nini hasa kilifanyika katika hatua hii ya mwisho :*?




- tumesimbua data inayotumwa na mtumaji kwa kutumia **"Nenosiri la Simu"**.
- kwa hivyo tuna ufunguo wa umma Kb na ujumbe wetu wa siri uliosimbwa kwa njia fiche na **"Ufunguo wa Kipindi "**, "Ks". Lakini tunawezaje kufanya hivi kwani, kama mpokeaji, hatujui Ks, ambayo iliundwa na mtumaji?
- Tunahitaji kutumia ufunguo wetu wa faragha "ka" kutoka hatua ya awali **"Andaa kifaa kitakachopokea data"** kwa ufunguo wa umma Kb.
- Kwa kweli, kwa kuhesabu ka.Kb = ka.kb.G=kb.ka.G=kb.Ka=Ks, tunapata Ks. Ambayo hatimaye inatumiwa kufafanua ujumbe wa siri.



### 2- Kuhamisha PSBT hadi Multisig (ya hali ya juu)



Hii inadhania kuwa Wallet Multisig yako tayari imeundwa na kwamba kifaa chako cha ColdCardQ tayari kimewekwa upya ili kuweza kufanya miamala ya sahihi nyingi. Ikiwa sivyo hivyo, maelezo yanapatikana [hapa](https://coldcard.com/docs/Multisig/) kwenye tovuti ya Coinkite.



Kikumbusho cha haraka cha saini nyingi za Wallet (Multisig) ni.



Kwa kawaida, ili kutumia pesa zako za Wallet, ufunguo mmoja tu wa faragha unahitajika ili kufungua UTXO zinazohusishwa na anwani zako.


Kwa upande wa Wallet Multisig, hadi funguo za faragha 15 na kwa hiyo saini 15 zinaweza kuhitajika ili kutumia fedha. Hii inajulikana kama jalada la "M kati ya N", huku N kati ya 1 na 15 na M idadi ya sahihi zinazohitajika ili pesa zitumike. Kwa mfano, Wallet Multisig 3 kati ya 5 itahitaji angalau sahihi 3 kati ya 5 zinazowezekana.



Changamoto basi ni kuratibu kati ya watia saini kutia saini "PSBT" ya "Partially Signed Bitcoin Transaction" kwa zamu. Katika muktadha huu, "**Muhimu Teleport**" inaweza kutumika kusambaza PSBT kati ya watia saini wenza kwa njia rahisi na ya siri. Simu rahisi ya video kati ya watia saini wenza itafanya ujanja.



Hivi ndivyo inavyofanywa kwenye Multisig 3 kati ya 4.



**Mtia saini 1:**



Mtia saini 1 anaagiza na kusaini PSBT. Hatimaye, anabofya **"T "** ili kutumia **"Muhimu Teleport "** kusambaza PSBT kwa mtiaji saini 2.



![CCQ-key-teleport](assets/fr/09.webp)




Baada ya kumteua aliyetia saini 2 kwa kubofya kwenye **"INGIA "**, "NENOSIRI YA TELEPORT" (hapa JJ YC AB 6A) imetolewa, ambayo lazima isambazwe kwa mtiaji saini 2 kupitia njia nyingine ya mawasiliano. Kwa mfano, SMS au simu ya sauti, lakini **si** simu ya video.



Bonyeza **"INGIA "** tena na msimbo wa QR unaowakilisha PSBT iliyotiwa saini na 1 kisha iliyosimbwa kwa "TELEPORT PASSWORD" inaonekana.



![CCQ-key-teleport](assets/fr/10.webp)



**Mtia saini 2:**



Mtia saini 2 huchanganua msimbo wa QR uliowasilishwa kwake na mtiaji saini 1. Kisha huingiza "TELEPORT PASSWORD" inayotumwa kwenye kituo cha pili cha mawasiliano ili kusimbua data iliyotumwa.



Mtia saini 2 anasaini muamala na kisha kubofya **"T "** ili kusambaza PSBT kwa mtiaji saini 3 kupitia "Teleport muhimu".


Ni wazi, sahihi 2 tayari zimetumika. Kinachokosekana ni yule aliyetia saini 3 ili shughuli hiyo iwe halali. Chagua mtiaji saini 3 kwa kubofya kwenye **"INGIA "**.



![CCQ-key-teleport](assets/fr/11.webp)



Na "TELEPORT PASSWORD" mpya imeundwa, ikifuatiwa tena na msimbo wa QR unaosimba PSBT iliyotiwa saini na 1 na 2 na kisha kusimbwa kwa "TELEPORT PASSWORD" hii mpya (GW YQ K3 LL).



![CCQ-key-teleport](assets/fr/12.webp)



**Mtia saini 3:**



Rudia hatua sawa na hapo juu.


Mtia saini 3 huchanganua msimbo wa QR uliowasilishwa kwake na mtiaji saini 2. Kisha huingiza "TELEPORT PASSWORD" inayotumwa na njia ya pili ya mawasiliano.



Mtia saini 3 hutia saini shughuli hiyo na wakati huu, kwa kuwa saini 3 kati ya 4 zimetumika, shughuli hiyo imeonyeshwa kama imekamilika, na iko tayari kusambazwa kupitia vyombo vya habari mbalimbali (Kadi ya SD, NFC, QR n.k.).



![CCQ-key-teleport](assets/fr/13.webp)



Ikiwa kipengele chako cha "Push Tx" cha ColdCardQ kimewashwa, bandika ColdCardQ yako nyuma ya kifaa chochote kilichounganishwa kwenye Intaneti (simu mahiri/kompyuta kibao) kilicho na NFC (simu mahiri/kompyuta kibao) ili kutangaza muamala kwenye mtandao wa Bitcoin.



![CCQ-key-teleport](assets/fr/14.webp)



*Kwa uhamishaji wa PSBT kutoka kwa mtiaji saini mmoja hadi mwingine, "Key Teleport" inatumiwa tu kupitia "Nenosiri la Teleport" katika kila hatua, ambayo husimba kwa njia fiche PSBT inapohamishwa kutoka kwa mtiaji saini mmoja hadi mwingine. Kwa vile data iliyotumwa haiwezi kutumika kuiba fedha, hakuna haja ya Diffie-Hellman kama ilivyo wakati wa kutuma siri za siri sana (seed, nenosiri n.k...)*.



![CCQ-key-teleport](assets/fr/15.webp)



*Chanzo: [Tovuti rasmi ya ColdCard](https://coldcard.com/)*