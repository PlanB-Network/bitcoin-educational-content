---
name: Ashigaru - Stonewall x2
description: Kuelewa na kutumia miamala ya Stonewall x2 kwenye Ashigaru
---
![cover stonewall x2](assets/cover.webp)



> *Fanya kila matumizi kwa coinjoin

## Muamala wa Stonewall x2 ni nini?



Stonewall x2 ni aina mahususi ya muamala wa Bitcoin iliyoundwa ili kuongeza usiri wa mtumiaji wakati wa kutumia, kwa kushirikiana na mtu mwingine asiyehusika katika matumizi. Njia hii inaiga muunganisho mdogo wa sarafu kati ya washiriki wawili, huku ukifanya malipo kwa wahusika wengine. Shughuli za Stonewall x2 zinapatikana kwenye programu ya Ashigaru, fork kutoka Samourai Wallet (timu iliyoanzisha aina hii ya shughuli).



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Jinsi inavyofanya kazi ni rahisi kiasi: unatumia UTXO uliyo nayo kufanya malipo, na kuomba usaidizi wa wahusika wengine ambao pia huchangia kwa UTXO yao wenyewe. Muamala unaishia na matokeo manne: mawili kati ya hayo kwa kiasi sawa, moja kwa ajili ya anwani ya anayelipwa, nyingine kwa anwani ya mshirika. UTXO ya tatu inarejeshwa kwa anwani nyingine ya mshirika, na kumwezesha kurejesha kiasi cha awali (hatua ya upande wowote kwake, modulo ya gharama za mining), na UTXO ya mwisho inarudi kwa anwani yetu, ambayo inajumuisha ubadilishaji wa malipo.



Kwa hivyo majukumu matatu tofauti yanafafanuliwa katika shughuli za Stonewall x2:




- Mtoaji, ambaye hufanya malipo halisi;
- Mshiriki, ambaye hufanya bitcoins kupatikana ili kuboresha kutokujulikana kwa shughuli hiyo, wakati wa kurejesha fedha zake kwa ukamilifu mwishoni (hatua ya neutral kwa ajili yake, modulo ya gharama za mining);
- Mpokeaji, ambaye huenda hajui aina mahususi ya muamala na anatarajia tu malipo kutoka kwa mtumaji.



Hebu tuchukue mfano. Alice iko kwa mwokaji ili kununua baguette yake, ambayo inagharimu `4,000 sats`. Anataka kulipa kwa bitcoins, huku akihifadhi usiri fulani kuhusu malipo yake. Kwa hiyo anampigia simu rafiki yake Bob, ambaye atamsaidia kwa hili.



![image](assets/fr/01.webp)



Kuchanganua muamala huu, tunaweza kuona kwamba mwokaji alipokea `4,000 sats` kama malipo ya baguette. Alice ilitumia `10,000 sats` katika ingizo na kurejesha `6,000 sats` katika pato, ikitoa salio halisi la `-4,000 sats`, ambalo linalingana na bei ya baguette. Kuhusu Bob, ilitoa `15,000 sats` katika ingizo na kupokea matokeo mawili: moja ya `4,000 sats` na lingine la `11,000 sats`, na kufanya salio la `0`.



Katika mfano huu, nimepuuza kwa makusudi ada za mining ili kurahisisha kueleweka. Kwa kweli, ada za miamala hushirikiwa kwa usawa kati ya mtoaji malipo na mshirika.



## Kuna tofauti gani kati ya Stonewall na Stonewall x2?



Muamala wa StonewallX2 hufanya kazi kwa njia sawa kabisa na muamala wa Stonewall, isipokuwa kwamba ule wa kwanza unashirikiana, ilhali ule wa mwisho haufanyi kazi. Kama tulivyoona, muamala wa Stonewall x2 unahusisha ushiriki wa mtu wa tatu, ambaye yuko nje ya malipo, na ambaye atafanya bitcoins zake zipatikane ili kuimarisha usiri wa muamala. Katika shughuli ya kawaida ya Stonewall, jukumu la mshirika linachukuliwa na mtumaji.



Wacha turudi kwenye mfano wetu wa Alice kwenye duka la mkate. Ikiwa hangeweza kupata mtu kama Bob wa kuandamana naye kwenye matumizi yake ya pesa, angeweza kufanya Ukuta wa Stonewall peke yake. Kwa njia hiyo, UTXO mbili zilizokuwa njiani zingekuwa zake, na angechukua 3 wakati wa kutoka.



![image](assets/fr/02.webp)




Kwa mtazamo wa mtu wa nje, shughuli hiyo ingebaki vile vile.



![image](assets/fr/05.webp)



Kwa hivyo mantiki inapaswa kuwa kama ifuatavyo unapotaka kutumia zana ya matumizi ya Ashigaru:




- Ikiwa mfanyabiashara hatumii Payjoin Stowaway, unaweza kufanya muamala shirikishi na mtu mwingine nje ya malipo ya shukrani kwa Stonewall x2 ;
- Ikiwa huwezi kupata mtu yeyote wa kufanya muamala wa Stonewall x2, unaweza kufanya muamala wa Stonewall pekee, ambao utaiga tabia ya muamala wa Stonewall x2.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-033daa45-d42c-40e1-9511-cea89751c3d4

## Ni nini maana ya muamala wa Stonewall x2?



Muundo wa Stonewall x2 huongeza kiasi kikubwa cha entropy kwenye shughuli, na kutatanisha uchanganuzi wa mnyororo. Ikionekana kutoka nje, shughuli kama hiyo inaweza kufasiriwa kama Coinjoin ndogo kati ya watu wawili. Lakini kwa kweli, ni malipo. Kwa hiyo njia hii inajenga kutokuwa na uhakika katika uchanganuzi wa minyororo, au hata kusababisha miongozo ya uwongo.



Hebu tuchukue mfano wa Alice, Bob na Boulanger. Shughuli kwenye blockchain ingeonekana kama hii:



![image](assets/fr/03.webp)



Mtazamaji wa nje anayetegemea heuristics ya uchanganuzi wa mnyororo wa kawaida anaweza kuhitimisha kimakosa kwamba "*Alice na Bob zimeungana kidogo, zikiwa na UTXO moja ndani na UTXO mbili kila moja nje*".



![image](assets/fr/04.webp)



Ufafanuzi huu sio sahihi kwa sababu, kama unavyojua, UTXO ilitumwa kwa Boulanger, Alice ina pato moja tu la kubadilishana, na Bob ina mbili.



![image](assets/fr/01.webp)



Hata kama mwangalizi wa nje ataweza kutambua paterne wa shughuli ya Stonewall x2, hatakuwa na taarifa zote. Hataweza kubainisha ni UTXO gani kati ya hizo mbili za kiasi sawa kinacholingana na malipo. Wala hataweza kubaini ikiwa Alice au Bob ilifanya malipo. Hatimaye, hataweza kubainisha ikiwa UTXO mbili zilizoingizwa zimetoka kwa watu wawili tofauti, au kama ni za mtu mmoja ambaye ameziunganisha. Hoja hii ya mwisho ni kwa sababu ya ukweli kwamba shughuli za kawaida za Stonewall, zilizojadiliwa hapo juu, zinafuata sawa sawa na shughuli za Stonewall x2. Ikionekana kutoka nje na bila maelezo ya ziada ya muktadha, haiwezekani kutofautisha muamala wa Stonewall na muamala wa Stonewall x2. Ya awali si shughuli shirikishi, ambapo ya mwisho ni. Hii inaongeza shaka zaidi kwa gharama.



![image](assets/fr/05.webp)




## Je, ninawezaje kuanzisha muunganisho kati ya Paynyms?



Kama ilivyo kwa miamala mingine shirikishi kwenye Ashigaru (*Cahoots*), Stonewall x2 inahusisha ubadilishanaji wa miamala ambayo haijatiwa saini kati ya mtumaji na mshirika. Ubadilishanaji huu unaweza kufanywa wewe mwenyewe, ikiwa uko pamoja na mshirika wako, au ukitumia kiotomatiki itifaki ya mawasiliano ya Soroban.



Ukichagua chaguo la pili, utahitaji kuanzisha muunganisho kati ya Paynyms kabla ya kutekeleza Stonewall x2. Ili kufanya hivyo, Paynym yako lazima "*ifuate*" Paynym ya mshirika wako, na kinyume chake. Ili kujua jinsi ya kufanya hivyo, unaweza kufuata mwanzo wa mafunzo haya mengine:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## Ninawezaje kufanya muamala wa Stonewall x2 kwenye Ashigaru?



Ili kutekeleza muamala wa Stonewall x2, bofya kwenye picha ya Paynym yako katika kona ya juu kushoto ya skrini, kisha ufungue menyu ya `Shirikiana`. Mtu anayeshiriki katika shughuli na wewe lazima afanye vivyo hivyo, isipokuwa kama unabadilishana misimbo ya QR ana kwa ana.



![Image](assets/fr/06.webp)



Una chaguo mbili: chagua `Anzisha` ikiwa wewe ndiwe mtumaji wa malipo, au `Shiriki` ikiwa wewe ndiye mtu unayeshirikiana katika muamala lakini si mlipaji wala mpokeaji halisi.



![Image](assets/fr/07.webp)



Ikiwa una jukumu la mshiriki, utaratibu ni rahisi sana. Kwa ushirikiano wa mbali kupitia mtandao wa Soroban, bofya `Shiriki`, chagua akaunti unayotaka kutumia, kisha ubofye `SIKILIZA KWA MAOMBI YA CAHOOTS` ili kusubiri ombi lililotumwa na mlipaji.



![Image](assets/fr/08.webp)



Kwa upande mwingine, kwa ushirikiano wa ana kwa ana kupitia kuchanganua msimbo wa QR, nenda kwenye ukurasa wa nyumbani wa wallet yako, bonyeza aikoni ya msimbo wa QR juu ya skrini, kisha uchanganue msimbo wa QR uliotolewa na mlipaji anayeanzisha muamala.



![Image](assets/fr/09.webp)



Ikiwa uko katika jukumu la mlipaji, yaani, anayeanzisha muamala, nenda kwenye menyu ya `Shirikiana`, kisha uchague `Anzisha`.



![Image](assets/fr/10.webp)



Kwa aina ya muamala, kwa kuwa tunataka kutekeleza Stonewall x2, chagua chaguo hili.



![Image](assets/fr/11.webp)



Kisha unaweza kuchagua kati ya ushirikiano wa mtandaoni (*Cahoots* kupitia *Soroban*) au ushirikiano wa ana kwa ana, kwa kubadilishana misimbo ya QR.



![Image](assets/fr/12.webp)



### Cahoots mtandaoni



Ikiwa umechagua chaguo la `Mkondoni`, basi chagua mshirika wako kutoka kwa Paynyms unazofuata.



![Image](assets/fr/13.webp)



Bofya kwenye `Sanidi muamala`, kisha uchague akaunti ambayo ungependa kufanya matumizi.



![Image](assets/fr/14.webp)



Kwenye ukurasa unaofuata, ingiza maelezo ya shughuli: anwani ya mpokeaji halisi wa malipo, kiasi cha kutumwa na kiwango cha malipo. Kisha bofya kwenye `Kagua usanidi wa muamala`.



![Image](assets/fr/15.webp)



Angalia maelezo kwa makini, hakikisha kuwa mshirika wako anasikiliza maombi ya *Cahoots*, kisha ubofye kitufe cha kijani `BEGIN BEGIN TRANSACTION` ili kuanzisha ubadilishanaji wa PSBTs kupitia Soroban.



![Image](assets/fr/16.webp)



Subiri hadi washiriki wote wawili wawe wametia saini muamala, kisha uyatangaze kwenye mtandao wa Bitcoin.



![Image](assets/fr/17.webp)



### Majadiliano ya ana kwa ana



Iwapo ungependa kufanya ubadilishanaji ana kwa ana, chagua aina ya muamala ya `STONEWALL X2`, kisha uchague chaguo la `Katika Mtu / Mwongozo`.



![Image](assets/fr/18.webp)



Bofya kwenye `Sanidi muamala`, kisha uchague akaunti ambayo ungependa kufanya matumizi.



![Image](assets/fr/19.webp)



Kwenye ukurasa unaofuata, ingiza maelezo ya shughuli: anwani ya mpokeaji halisi wa malipo, kiasi cha kutumwa na kiwango cha malipo. Kisha bofya kwenye `Kagua usanidi wa muamala`.



![Image](assets/fr/20.webp)



Angalia maelezo, kisha ubonyeze kitufe cha kijani `BEGIN BEGIN TRANSACTION` ili kuanza kubadilishana PSBT kupitia kuchanganua msimbo wa QR.



![Image](assets/fr/21.webp)



Ubadilishanaji unafanywa kwa kubadilisha uchanganuzi na mshirika: bofya kwenye `ONYESHA Msimbo wa QR` ili kuonyesha msimbo wako wa QR kwa mshirika wako, ambaye ataichanganua. Kisha atabofya `SHOW QR CODE` ili kuonyesha yake, na utaichanganua kwa `LAUNCH QR Scanner`. Rudia utaratibu huu hadi hatua zote tano za kubadilishana zimekamilika.



![Image](assets/fr/22.webp)



Mara ubadilishanaji wote utakapokamilika, angalia maelezo ya muamala, kisha uachilie kwa kuburuta kishale cha kijani kibichi chini ya skrini.



![Image](assets/fr/23.webp)



[Muamala umechapishwa](https://mempool.space/testnet4/tx/9082f3d989728aacd290535a1ac374ab8c04a241a1d798b378db626dabea7a24). Muundo wake ni kama ifuatavyo:



![Image](assets/fr/24.webp)



*Mikopo: [mempool.space](https://mempool.space/)*



Tunaweza kuchunguza michango miwili kutoka kwa jalada langu, mtawalia `91,869 sats` na `64,823 sats`, huku pembejeo zingine mbili zinatoka kwa wallet ya mshiriki wangu. Kwa upande wa matokeo, UTXO moja ya `100,000 sats` inatumwa kwa anayelipwa, na UTXO mbili za `100,000 sats` na `159,578 sats` zinarudi kwenye jalada la mshirika wangu. Kwake, operesheni hiyo haina upande wowote, kwani anarejesha kiasi kamili cha fedha alizowekeza kwenye pembejeo (bila kujumuisha gharama za mining ambazo alichangia). Hatimaye, ninapokea ubadilishaji wa UTXO wa `56,270 sats`, unaolingana na tofauti kati ya pembejeo zangu zote na malipo ya `100,000 sats` yaliyotumwa kwa mpokeaji.



Ni wazi, naweza kuelezea muundo huu kwa sababu nilijenga shughuli mwenyewe. Lakini kwa mtazamaji wa nje, kwa ujumla haiwezekani kuamua ni UTXO zipi ni za mshiriki yupi, ama katika pembejeo au matokeo.



Ili kuongeza ujuzi wako wa usimamizi wa faragha wa onchain kwenye Bitcoin, ninapendekeza uchukue mafunzo yangu ya BTC 204 kuhusu Mpango ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c