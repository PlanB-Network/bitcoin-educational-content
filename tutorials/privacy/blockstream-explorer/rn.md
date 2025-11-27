---
name: Umugenzuzi w'umugezi
description: Gutohoza igice nyamukuru ca Bitcoin na Liquid Network.
---

![cover](assets/cover.webp)



Blockstream Explorer ni umugambi worohereza ugutohoza ibikorwa vy’ubudandaji n’ingene amasezerano ya Bitcoin ameze kw’isi yose, hamwe n’itegeko rya Liquid ryateguwe n’ishirahamwe rya Blockstream.



Yatangujwe mu 2014 na Blockstream, ishirahamwe ryashinzwe na Adam Back, [blockstream.info](https://blockstream.info) ubushakashatsi bufise intumbero yo gutanga ibikorwa remezo bikomeye vya Bitcoin, bigatuma habaho ugukorana n’ugukurikirana ibikorwa hagati y’ibice (on-chain na Liquid), mu gihe enhan.



Muri iyi nyigisho, turaza kuraba ikiyitandukanya, ibikorwa vyayo, n’ingene itanga ubugenzuzi butagira umurongo bw’ibikorwa n’imimerere y’ibice vya Bitcoin vya on-chain na Liquid.



## Gutangura n'umugenzuzi wa Blockstream



### Kugendera ku muhora nyamukuru



Iyo uja ku mushakashatsi wa Blockstream.info, kuri "**Dashboard**", uruhererekane rwa Bitcoin rutorwa ku buryo busanzwe. Kuva kuri iyi interface, ufise icegeranyo ca :





- Ingano y’uruzitiro nyamukuru: Amabuye aherutse gucukurwa.



![blocks](assets/fr/01.webp)



Iki gice kiratanga amakuru ku mabuye aherutse gucukurwa, ikidodo c’igihe, umubare w’ibikorwa vy’ubudandaji biri muri buri butaka, ubunini mu kilobytes (kB) n’ingero y’ubutaka bumwe bumwe mu bipimo vy’uburemere (**WU** = *Ibipimo vy’uburemere*). Iryo ngero rya nyuma riraryoshe, kuko ridushoboza gusuzuma ukuntu igice cose gikora neza, kubera ko igice cose c’uruzitiro rukuru gifise ubushobozi bwo gukora `4.000.000 WU`, canke `4.000 kWU`.





- Ivyo gucuruza vuba.



![transactions](assets/fr/02.webp)



Igice c’ugucuruza gitanga amakuru ku kimenyetso kidasanzwe c’ugucuruza, agaciro ka bitcoin karimwo, ubunini mu bytes vy’ukuri (vB) - bigereranya umubare w’amakuru yose (injizwa n’isohoka) - n’igipimo c’amahera ajanye. Nk’akarorero, igikorwa gifise ubunini bwa `153 vB` ku rugero rwa `2 sat/vB` kizotwara amahera `306 satoshis`.



### Gutohoza amazi



Kuva ku rutonde rwa "**Blocks**", ushobora gukurikirana amateka y'uruzitiro rwose rwo gusubira ku bubiko bwa nyuma bwacukuwe.



![blocs](assets/fr/03.webp)



Niwafyonda ku gice kinaka, urashobora kuronka ibindi bisobanuro ku bijanye n’amakuru be n’ibikorwa biri muri co. Nk'akarorero, ku gice 919330: uzobona hash y'igice. Ushobora kandi kuja ku gice c’imbere, kuko igice cose c’amabuye y’agaciro (uretse Genesis) gifatanye n’igice c’imbere, kigakomeza hash y’igice ca mbere.



![metadata](assets/fr/04.webp)



Mu gufyonda kuri buto **"Ibisobanuro "**, ushobora kuronka amakuru menshi ku bijanye n'iri bubiko, nk'aho riri, ryemeza ko ryongewe ku ruhererekane nyamukuru rwagumye kandi rwakwiragijwe. Ufise kandi ingorane iyo block icukurwamwo: iyo ngorane igereranya ububasha bwo gukoresha ubuhinga bwa none busabwa kugira ngo umuntu atore umuti w’ingorane y’ubuhinga bwa cryptography ya mining kandi irahindurwa buri block ya 2016 (nk’indwi 2).



![details](assets/fr/05.webp)



Munsi y’iki gice c’ido n’ido, turabona amafaranga yose akoreshwa muri iki gice.



Igikoresho ca mbere nyene mu gice citwa **isoko coinbase**. Ikoreshwa mu gutanga impembo y’umucukuzi w’amabuye y’agaciro mining (amahera yose ajanye n’ibikorwa biri muri block n’infashanyo ya block). Ivyo bikoresho vy’ubuhinga bwa none (bitcoins) vyaremwe n’iyi nzira bishobora gukoreshwa gusa iyo haciye hacukurwa ibindi bice 100 bikurikiranye. Mu yandi majambo, kugira ngo ashobore kubikoresha, umucukuzi azobwirizwa kurindira ko hakorwa block **919430**. Ivyo bizwi kw'izina rya [*"igihe co gukura "*](https://planb.academy/fr/ibikoresho/urutonde rw'amajambo/igihe-co gukura).



Coinbase ni igikorwa kidasanzwe: ni co conyene kitagira inyungu nyayo, kuko nta bitcoins zikoresha zivuye mu gicuruzwa ca kera.




![coinbase](assets/fr/06.webp)



Ibindi bikorwa vyose bigabanywamwo ibice bibiri: ivyo kwinjira n’ivyo gusohoka.



Kugira ngo bitcoins zikoreshwe nk’ibintu vyinjizwa mu bikorwa bishasha, uwutanguje ivyo bikorwa ategerezwa kwemeza ko ari vyo afise mu gutanga umukono uhuye n’inyandiko yihariye. Igipande cose c’ama bitcoins (UTXO) kirimwo inyandiko muri rusangi isaba umukono wihariye urufunguzo rw’ibanga rw’uwufise gusa rushobora gutanga. Izo nyandiko ni ***scriptSig*** (mu rurimi rwa ASM), zanditswe mu rurimi rwa Bitcoin, kandi zishobora kuba z’ubwoko butandukanye. Muri aka karorero, turashobora kubona ko ama UTXO yakoreshejwe yari ay’ubwoko bwa P2SH gushika ku gisohoka c’ubwoko bwa P2WPKH (*Pay-to-Witness-Public-Key-Hash*).



Ushobora gukurikirana amateka ya UTXO yihariye ukoresheje ubuhinga bwa heuristics. Turagutumiye kumenya ubuhinga butandukanye bwa Bitcoin n'uburyo bwo gukomeza ibanga ry'ibikorwa vyawe kuri Bitcoin :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



Reka dufate akarorero k’amahera asohoka y’iyi nzira. Mu gufyonda ku kimenyetso c'ibikorwa, duca tuja ku gice ca **Ibikorwa** kiri kuri paji y'ibisobanuro vy'ibikorwa.



![transaction](assets/fr/08.webp)



Kuri iyi paji, urashobora kumenya block iyo transaction yashizwemwo.Bivanye n’ubwoko bw’aderesi yakoreshejwe, transaction irashobora gutuma amakuru yayo agenda neza (*virtual bytes*) bigatuma wishura amafaranga make y’ugusaba. Nk'akarorero, iyo nzira yazigamye 53% vy'amahera hakoreshejwe uburyo bw'aderesi SegWit Bech32 butangura na `bc1q`.



![trx_details](assets/fr/09.webp)



## Liquid uruhande



Liquid Network ni [*uruhererekane rw'inyuma*](https://planb.academy/ru/ibikoresho/urutonde rw'amajambo/uruhererekane rw'inyuma) n'umuti w'urugero rwa 2 rw'inkomoko yuguruye ku bijanye n'umurongo wa Bitcoin. Cane cane, bishoboza gukoresha amafaranga yihuta kandi y’ibanga.



Ku rubuga rwa Blockstream.info, fyonda ku buto **"Liquid"** kugira ngo uhindukire ku rubuga rwa Liquid.



![liquid](assets/fr/10.webp)



Dufyondeye kuri kimwe mu bikorwa dushaka gukurikirana, turabona ko amafaranga y'ibice vya bitcoin asubirizwa n'amajambo "**Ibanga**". Kuri uru rubuga, amafaranga ashobora kuba ay’ibanga, rero ntidushobora kubona amafaranga y’ama UTXO yose, yaba ari mu mafaranga canke hanze y’amafaranga.



![liquid_trx](assets/fr/11.webp)



Ariko rero, turabona ko ingingo ngenderwako n’uburyo biri ku rugero nyamukuru rw’umurongo wa Bitcoin ari kimwe: inyandiko zo gufunga bitcoin n’ugukurikirana kwa UTXO.



![liquid_details](assets/fr/12.webp)



Liquid Network kandi itanga ivy’ubuhinga bwa none bitagiramwo ububiko bishobora gukoreshwa n’amashirahamwe. Mu **"Itunga "**, uzosanga urutonde rw'itunga ryanditswe, umubare waryo wose hamwe n'itongo rifitaniye isano.



![assets](assets/fr/13.webp)



Ku mutungo wose, urashobora gukurikirana amateka y’ugusohoka no guturira amafaranga (ugukuraho umubare wose uriko urakoreshwa).



![assets_trxs](assets/fr/14.webp)




## Ibindi bihitamwo



Igikoresho co gutohoza amakuru ca Blockstream.info kandi kirimwo ivyerekanwa n'ugukurikirana amafaranga akoreshwa kuri Testnet, Bitcoin, on-chain na Liquid Network.



![testnet](assets/fr/15.webp)



Iyo uja ku rubuga rwa Testnet, ntukoresha ama bitcoins nyayo, ariko ufise ibintu vyose vyavuzwe haruguru.



![liquid_testnet](assets/fr/16.webp)



Iyi nzira ifise uburebure bw’uruzitiro butandukanye, ushobora kuyifatanya no kugerageza ingene ubuhinga bwa Bitcoin na Liquid bukora.





- Igice ca API kigenewe umuntu wese yipfuza kwinjiza ibikorwa bimwebimwe vya Explorer mu gikorwa ciwe bwite. Biciye muri iyi API urashobora kubaza uruhererekane nyamukuru rw’ibice bitandukanye (on-chain na Liquid), gukurikirana ibikorwa no kumenya amafaranga y’ibikorwa mu gice, nk’akarorero.



![api](assets/fr/17.webp)



Ubu rero witeguye gukoresha ubushobozi bwose bwa Blockstream Explorer bwo kubaza amabarabara ku bice vya on-chain na Liquid. Twizeye ko mwabonye iyi nyigisho ari ngirakamaro, kandi muzogusaba inyigisho yacu ku yindi nzira ya Bitcoin:



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f