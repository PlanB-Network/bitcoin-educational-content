---
name: Ashigaru - Whirlpool Coinjoin
description: Je, ninawezaje kufanya coinjoins kwenye programu ya Ashigaru?
---

![cover](assets/cover.webp)



"*wallet ya bitcoin ya mitaani*"



Katika somo hili, utajifunza coinjoin ni nini na jinsi ya kutengeneza moja kwa kutumia Ashigaru Terminal application na utekelezaji wa Whirlpool, itifaki sanjari iliyorithiwa kutoka Samourai Wallet.



## Jinsi viunganishi vya Whirlpool hufanya kazi



Katika somo hili, sitarudi nyuma kuhusu dhana ya sanjari, manufaa yake au utendakazi wa kinadharia wa Whirlpool, kwa kuwa mada hizi tayari zimefafanuliwa kwa kina katika Sehemu ya 5 ya kozi ya mafunzo ya BTC 204 kuhusu Mpango ₿ Academy. Iwapo bado hujafahamu utendakazi wa Whirlpool au kanuni ya sanjari, ninapendekeza kwa dhati kwamba uwasiliane na sehemu hii ya 5 kabla ya kuendelea :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Hata hivyo, hapa kuna mambo machache ya haraka na takwimu ambazo zinaweza kuja kwa manufaa.



Kwingineko zinazooana za Whirlpool hutumia akaunti 4 tofauti ili kukidhi mahitaji ya mchakato wa sanjari:




- Akaunti ya **Amana**, iliyotambuliwa kwa faharasa `0'` ;
- Akaunti **Bad Bank** (au *doxxic exchange*), iliyotambuliwa kwa faharasa `2,147,483,644'` ;
- Akaunti ya **Premix**, iliyotambuliwa na fahirisi `2 147 483 645'` ;
- Akaunti ya **Mchanganyiko wa Posta**, iliyotambuliwa na faharasa `2 147 483 646'`.



Mnamo mwezi wa Novemba 2025, Ashigaru, madhehebu mawili ya kuogelea yanapatikana (orodha hii huenda ikabadilika katika miezi ijayo: kwa hivyo kumbuka kuangalia maadili unaposoma):




- 0.25 BTC`, na ada ya kuingia ya `0.0125 BTC`;
- 0.025 BTC, na ada ya kuingia ya 0.00125 BTC.



Kila mzunguko wa kuchanganya unaweza kuhusisha kati ya 5 na 10 UTXO katika pembejeo na pato.



![Image](assets/fr/01.webp)



## Mahitaji ya programu



Ili kutengeneza sanjari na Whirlpool, utahitaji programu tatu tofauti:





- Ashigaru Terminal**, ambayo inakuwezesha kudhibiti coinjoins zako moja kwa moja kutoka kwa kompyuta yako;



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add



- Ashigaru Wallet**, programu kwenye simu yako mahiri ambayo unaweza kutumia bitcoins zako katika *mchanganyiko wa posta* kutoka mahali popote ;



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f



- Dojo**, utekelezaji wa nodi ya Bitcoin inayokuhakikishia muunganisho huru kwenye mtandao, bila kutegemea seva ya watu wengine.



https://planb.academy/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Sakinisha kila moja ya zana hizi kwa kufuata mafunzo yao husika, kisha unaweza kuanza kutengeneza coinjoins zako za kwanza.



## Pokea bitcoins



Baada ya kuunda kwingineko yako, utaanza na akaunti moja, iliyotambuliwa na faharasa `0'`. Hii ni akaunti ya `Amana`. Ni kwa akaunti hii ambapo utatuma bitcoins zinazolengwa kuunganishwa. Unaweza kuzipokea kupitia programu ya Ashigaru (angalia sehemu ya 5 ya mafunzo maalum), au kupitia Kituo cha Ashigaru (pia kimefafanuliwa katika sehemu ya 5 ya mafunzo maalum).



Pindi tu akaunti yako ya amana inapokuwa na angalau kiasi kinachohitajika ili kushiriki katika hifadhi ndogo zaidi (pamoja na gharama za huduma na kima cha chini kabisa kinachohitajika ili kulipia gharama za mining) utakuwa tayari kuanzisha miunganisho yako ya kwanza.



![Image](assets/fr/02.webp)



## Fanya Tx0



Pesa zikishafika katika akaunti yako ya amana na muamala umethibitishwa, unaweza kuanza mchakato wa sanjari. Ili kufanya hivyo, kwenye Kituo cha Ashigaru, fungua menyu ya `Pochi`, kisha uchague wallet yako. Ikiwa wallet yako imefungwa, programu itakuuliza nenosiri lako na passphrase.



![Image](assets/fr/03.webp)



Kisha chagua akaunti ya `Amana`.



![Image](assets/fr/04.webp)



Nenda kwenye menyu ya `UTXOs`.



![Image](assets/fr/05.webp)



Hapa utaona orodha ya UTXO zote kwenye akaunti yako ya amana. Chagua zile unazotaka kutuma katika mizunguko ya sanjari.



Kwa usiri zaidi na kuepuka *Ingizo la Kawaida Ownership Heuristic (CIOH)*, inashauriwa kutumia UTXO moja tu kwa kila ingizo katika Whirlpool (ufafanuzi wa kina wa kanuni hii unaweza kupatikana katika BTC 204).



Bonyeza kitufe cha `ENTER` kwenye kibodi yako ili kuchagua UTXO: nyota `(*)` itaonekana kando yake ili kuonyesha kuwa imechaguliwa.



![Image](assets/fr/06.webp)



Kisha bonyeza kitufe cha `Changanya Uliochaguliwa`.



![Image](assets/fr/07.webp)



Ikiwa una UTXO kubwa ya kutosha kushiriki katika mojawapo ya madimbwi mawili yanayopatikana, unaweza kuchagua bwawa lengwa kwa kutumia mishale. Kwenye ukurasa huu, utaona maelezo ya Tx0 yako:




- idadi ya UTXO ambazo zitaingia kwenye bwawa;
- ada mbalimbali zinazotumika (ada za huduma na ada za mining);
- kiasi cha mabadiliko ya *doxxic*.



Angalia maelezo kwa makini, kisha ubofye `Broadcast` ili kutangaza Tx0.



![Image](assets/fr/08.webp)



Kisha Ashigaru itaonyesha TXID ya Tx0 yako, ikithibitisha kwamba muamala umetangazwa kwenye mtandao.



![Image](assets/fr/09.webp)



## Kufanya coinjoins



Baada ya Tx0 kutangazwa, rudi kwenye ukurasa wa nyumbani wa akaunti yako ya amana, kisha ubofye `Akaunti` na uchague akaunti ya `Premix`.



![Image](assets/fr/10.webp)



Katika menyu ya `UTXOs`, utaona sehemu mbalimbali zilizosawazishwa, tayari kuingiza mizunguko ya sanjari. Mara tu Tx0 itakapothibitishwa, Kituo cha Ashigaru kitaanzisha kiotomatiki mzunguko wao wa kwanza wa kuchanganya.



![Image](assets/fr/11.webp)



Baada ya Tx0 kuthibitishwa, muamala wa kwanza wa pamoja utaundwa na kutangazwa kiotomatiki na Kituo cha Ashigaru. Kwa kwenda kwenye `Akaunti > Postmix > UTXOs`, unaweza kutazama UTXO zako zilizosawazishwa, ukingoja uthibitisho wa mzunguko wao wa kwanza.



![Image](assets/fr/12.webp)



Sasa unaweza kuondoka kwenye Kituo cha Ashigaru kikiendelea chinichini: kitaendelea kuchanganya na kuchanganya nyimbo zako kiotomatiki.



## Kumaliza coinjoins



Sasa unaweza kuruhusu sarafu zako zijichanganye zenyewe kiotomatiki. Muundo wa Whirlpool unamaanisha kuwa hakuna gharama za ziada za kuchanganya tena: hakuna ada za huduma, hakuna ada za mining. Kwa hivyo kuruhusu sarafu zako kushiriki katika mizunguko zaidi ya kuchanganya kunaweza kufaidi usiri wako pekee.



Kwa ufahamu bora wa utaratibu huu na ni mizunguko ngapi inafaa kungojea, napendekeza kusoma nakala hii:



https://planb.academy/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

Ili kuona idadi ya michanganyiko iliyofanywa na kila moja ya vipande vyako, fungua menyu ya `UTXOs` katika akaunti ya `Postmix`.



![Image](assets/fr/13.webp)



Ili kutumia sarafu zako zilizochanganywa, nenda kwenye programu ya Ashigaru, inayotumia wallet sawa na programu yako ya Kituo cha Ashigaru. wallet inayoonyeshwa kwenye ufunguzi inalingana na akaunti yako ya `Amana`. Ili kufikia akaunti ya `Postmix`, iliyo na UTXO zako mchanganyiko, bofya alama ya Whirlpool katika kona ya juu kulia.



![Image](assets/fr/14.webp)



Katika akaunti hii, utaona sarafu zako zote zinazochanganywa kwa sasa. Ili kuzitumia, bonyeza `+` ishara iliyo chini kulia mwa skrini, kisha uchague `Tuma`.



![Image](assets/fr/15.webp)



Jaza maelezo ya muamala wako: anwani ya mpokeaji, kiasi kitakachotumwa, na, ukipenda, chagua muundo mahususi wa muamala ili kuboresha zaidi usiri wako (angalia mafunzo yanayolingana).



![Image](assets/fr/16.webp)



Angalia kwa uangalifu maelezo ya muamala, kisha uburute mshale chini ya skrini ili kuthibitisha usafirishaji.



![Image](assets/fr/17.webp)



Muamala wako umetiwa saini na kutangazwa kwenye mtandao wa Bitcoin.



![Image](assets/fr/18.webp)



## Tumia Mabadiliko ya Doxxic



Kumbuka: Muundo wa Whirlpool unatokana na kusawazisha vipande vyako kwenye Tx0, kabla havijaingia kwenye madimbwi. Ni utaratibu huu ambao unavunja ufuatiliaji wa UTXO. Kwa maoni yangu, huu ndio mfano bora zaidi wa coinjoin, lakini ina drawback moja: hutoa *mabadiliko* ambayo hayapitii mchakato wa coinjoin.



Mabadiliko haya yanalingana na UTXO iliyoundwa kwa kila Tx0. Imetengwa katika akaunti mahususi iitwayo `Doxxic Change` au `Bad Bank`, kulingana na programu, ili kuepuka kuitumia pamoja na UTXO zako zingine. Hii ni muhimu sana, kwa sababu UTXO hizi hazijachanganyika: viungo vyake vya ufuatiliaji hubakia sawa, na wanaweza kuhatarisha usiri wako kwa kuanzisha muunganisho kati yako na shughuli yako ya sanjari. Kwa hivyo zishughulikie kwa uangalifu na **usizitumie kamwe na UTXO zingine**, iwe zimechanganywa au la. Kuchanganya UTXO yenye sumu na UTXO iliyochanganywa itafuta faida zote za faragha ambazo umepata kutokana na kuungana.



Kwa sasa, Ashigaru haitoi ufikiaji wa moja kwa moja kwa akaunti hii ya `Doxxic Change` (angalau, sijaipata). Kipengele hiki labda kitaongezwa katika sasisho la baadaye. Wakati huo huo, njia pekee ya kupata pesa hizi ni kuagiza seed yako kwenye Sparrow Wallet. Ya pili itagundua kiotomatiki kuwa hii ni wallet inayotumiwa na Whirlpool na kukupa ufikiaji wa akaunti zote nne, pamoja na akaunti ya `Doxxic Change`. Kisha unaweza kutumia UTXO hizi kama bitcoins za kawaida kutoka Sparrow.



Hapa kuna mikakati kadhaa inayowezekana ya kudhibiti UTXO zako za ubadilishaji wa fedha za kigeni kutoka kwa coinjoins bila kuathiri faragha yako:





- Kuzichanganya kwenye madimbwi madogo:** Ikiwa UTXO yako yenye sumu ni kubwa vya kutosha kujiunga na bwawa dogo, kwa ujumla hili ndilo chaguo bora zaidi. Kuwa mwangalifu, hata hivyo, usiwahi kuunganisha UTXO kadhaa zenye sumu ili kufikia hili, kwani hii itaunda kiunganishi kati ya maingizo yako mbalimbali katika Whirlpool.





- Ziweke alama kama zisizoweza kutegemewa:** Mbinu nyingine ya busara ni kuwaweka tu jinsi walivyo katika akaunti yao tofauti na kuwaacha bila kuguswa. Hii itakuzuia kuzitumia kwa bahati mbaya. Ikiwa thamani ya bitcoin itaongezeka, mabwawa mapya yaliyochukuliwa kwa ukubwa wao yanaweza kufunguliwa.





- Toa michango:** Unaweza kuchagua kugeuza UTXO hizi zenye sumu kuwa michango kwa wasanidi wa Bitcoin, miradi huria au vyama vinavyokubali BTC. Hii hukuruhusu kuzitupa kwa manufaa huku ukisaidia mfumo ikolojia.





- Nunua kadi za zawadi za kulipia kabla au kadi za Visa:** Mifumo kama vile [Bitrefill](https://www.bitrefill.com/) hukuruhusu kubadilisha bitcoins zako kwa kadi za zawadi au kadi za Visa zinazoweza kupakiwa tena ambazo zinaweza kutumika madukani. Hii inaweza kuwa njia rahisi na ya busara ya kutumia UTXO zako zenye sumu.





- Zibadilishe kwa Monero:** Samourai Wallet ilitumika kutoa huduma ambayo sasa haitumiki ya ubadilishaji wa atomiki ya BTC/XMR. Ikiwa huduma kama hiyo ipo (sijui yoyote ya kibinafsi), ni suluhisho bora la kutenga UTXO hizi, kuzibadilisha kuwa Monero, na kisha kuzirudisha kwa Bitcoin. Walakini, njia hii ilikuwa ghali na inategemea ukwasi uliopatikana.





- Zihamishe hadi Lightning Network:** Kuhamisha UTXO hizi kwa Lightning Network ili kufaidika na ada zilizopunguzwa za muamala ni chaguo linaloweza kuvutia. Walakini, njia hii inaweza kufichua habari fulani kulingana na utumiaji wako wa Umeme, na kwa hivyo inapaswa kutumiwa kwa tahadhari.



## Ninawezaje kujua kuhusu ubora wa mizunguko yetu ya sati?



Ili coinjoin iwe na ufanisi wa kweli, lazima iwasilishe kiwango cha juu cha usawa kati ya kiasi cha kuingiza na kutoa. Usawa huu huongeza idadi ya tafsiri zinazowezekana kwa mwangalizi wa nje, ambayo huongeza kutokuwa na uhakika kuhusu shughuli. Kupima kutokuwa na uhakika huku, tunatumia dhana ya entropy inayotumika kwa muamala. Mfano wa Whirlpool unatambuliwa kama mojawapo ya ufanisi zaidi katika suala hili, kwani inahakikisha usawa bora kati ya washiriki. Kwa mtazamo wa kina zaidi wa kanuni hii, ninapendekeza uangalie sura ya mwisho ya Sehemu ya 5 ya kozi ya mafunzo ya BTC 204.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Utendaji wa mizunguko kadhaa ya coinjoin hupimwa kwa saizi ya seti ambazo sarafu imefichwa. Seti hizi hufafanua kile kinachojulikana kama *anonsets*. Kuna aina mbili: hatua ya kwanza ya usiri katika uso wa uchambuzi wa retrospective (kutoka sasa hadi siku za nyuma), na pili hupima upinzani dhidi ya uchambuzi unaotarajiwa (kutoka zamani hadi sasa). Kwa maelezo kamili ya viashiria hivi viwili, tafadhali soma mafunzo yafuatayo (au, kwa mara nyingine, kozi ya mafunzo ya BTC 204):



https://planb.academy/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

## Jinsi ya kusimamia mchanganyiko wa posta?



Baada ya kuendesha mizunguko kadhaa ya satifu, mkakati bora ni kuweka UTXO zako kwenye akaunti ya `Postmix`, ukiziruhusu zichanganywe tena kwa muda usiojulikana hadi utakapohitaji kuzitumia.



Watumiaji wengine wanapendelea kuhamisha bitcoins zao zilizochanganywa kwenye wallet iliyolindwa na vifaa vya wallet. Chaguo hili linawezekana, lakini linahitaji kiasi fulani cha ukali ili kuhakikisha kuwa usiri unaopatikana kwa coinjoins hauathiriwi.



Kuunganisha UTXO ndio kosa la mara kwa mara. Ni muhimu kamwe usichanganye UTXO zilizochanganywa na UTXO ambazo hazijachanganywa katika shughuli hiyo hiyo, vinginevyo unaweza kuhatarisha kuanzisha *Ingizo ya Kawaida ya Ownership Heuristic (CIOH)*. Hii inamaanisha usimamizi mkali wa UTXO zako, haswa kupitia uwekaji lebo wazi na sahihi. Kwa ujumla, kuunganisha UTXOs ni mazoea mabaya ambayo mara nyingi husababisha upotezaji wa usiri wakati unasimamiwa vibaya.



https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Unapaswa pia kuwa mwangalifu juu ya kuunganisha UTXO zilizochanganywa. Uunganisho mdogo unaweza kuzingatiwa ikiwa UTXO zina matatizo muhimu, lakini bila shaka hupunguza kiwango chako cha usiri. Epuka uunganisho mkubwa au wa haraka, unaofanywa kabla ya idadi ya kutosha ya mchanganyiko, kwa kuwa unaweza kuanzisha viungo visivyo na maana kati ya vipande vyako vya kabla na baada ya mchanganyiko. Katika hali ya shaka, ni vyema kutounganisha UTXO zako za posta na kuzihamisha moja baada ya nyingine hadi kwenye maunzi yako ya wallet, na kutengeneza anwani mpya ya mapokezi tupu kila wakati. Usisahau kuweka lebo kwa kila UTXO iliyohamishwa.



Tunashauri sana dhidi ya kuhamisha UTXO zako za posta hadi kwenye jalada kwa kutumia hati za wachache. Kwa mfano, ikiwa ulishiriki katika Whirlpool kutoka kwa jalada la multi-sig katika `P2WSH`, kutakuwa na wachache wenu wanaoshiriki aina hii ya hati. Kwa kutuma UTXO za mchanganyiko wako kwa aina hii ya hati, unapunguza sana kutokujulikana kwako. Zaidi ya aina ya hati, alama zingine maalum za vidole za wallet zinaweza kuhatarisha usiri wako, kwa hivyo jambo bora zaidi kufanya ni kuzitumia kutoka kwa programu ya Ashigaru.



Hatimaye, kama ilivyo kwa miamala yote ya Bitcoin, usiwahi kutumia tena anwani ya kupokea. Kila malipo lazima yatumwe kwa anwani mpya, ya kipekee, isiyo na kitu.



Njia rahisi na salama zaidi ni kuruhusu UTXO zako zilizochanganyika zitulie kwenye akaunti zao za `Postmix`, ziruhusu zichanganyike kawaida, na uzitumie tu inapohitajika kutoka kwa Ashigaru.



Pochi za Ashigaru na Sparrow hujumuisha ulinzi wa ziada dhidi ya makosa ya kawaida yanayohusiana na uchanganuzi wa blockchain, kukusaidia kuhifadhi usiri wa miamala yako.