---
name: Ukuta wa mawe x2
description: Kuelewa na kutumia miamala ya Stonewall x2
---
![cover stonewall x2](assets/cover.webp)


***ONYO:** Kufuatia kukamatwa kwa waanzilishi wa Samourai Wallet na kunaswa kwa seva zao tarehe 24 Aprili, miamala ya Stonewallx2 hufanya kazi tu kwa kubadilishana PSBTs kati ya wahusika husika, mradi watumiaji wote wawili wameunganishwa kwenye Dojo yao wenyewe. Hata hivyo, inawezekana kwamba zana hizi zinaweza kuzinduliwa tena katika wiki zijazo. Kwa sasa, bado unaweza kushauriana na makala haya ili kuelewa utendakazi wa kinadharia wa Stonewallx2 na ujifunze jinsi ya kuyafanya wewe mwenyewe.*


_Ikiwa unazingatia kutekeleza Stonewallx2 wewe mwenyewe, utaratibu unafanana sana na ule ulioelezewa katika mafunzo haya. Tofauti kuu iko katika uchaguzi wa aina ya muamala wa Stonewallx2: badala ya kuchagua `Mkondoni`, bofya `Katika Mtu / Mwongozo`. Kisha, utahitaji wewe mwenyewe Exchange PSBTs kuunda muamala wa Stonewallx2. Ikiwa uko karibu na mshirika wako, unaweza kuchanganua misimbo ya QR mfululizo. Ikiwa uko mbali, faili za JSON zinaweza kubadilishwa kupitia njia salama ya mawasiliano. Mafunzo mengine bado hayajabadilika._


_Tunafuatilia kwa karibu maendeleo ya kesi hii pamoja na maendeleo kuhusu zana zinazohusiana. Uwe na uhakika kwamba tutasasisha mafunzo haya kadiri habari mpya zinavyopatikana._


_Mafunzo haya yametolewa kwa madhumuni ya elimu na habari pekee. Hatuidhinishi au kuhimiza matumizi ya zana hizi kwa madhumuni ya uhalifu. Ni wajibu wa kila mtumiaji kutii sheria katika eneo la mamlaka yake._


---

> *Fanya kila utumie CoinJoin.*

## Muamala wa Stonewall x2 ni nini?


Stonewall x2 ni aina mahususi ya muamala wa Bitcoin unaolenga kuongeza faragha ya mtumiaji wakati wa matumizi, kwa kushirikiana na mtu mwingine asiyehusika katika matumizi hayo. Njia hii inaiga mini-CoinJoin kati ya washiriki wawili, huku ukifanya malipo kwa wahusika wengine. Miamala ya Stonewall x2 inapatikana kwenye programu ya Samourai Wallet na programu ya Sparrow Wallet. Zote mbili zinaingiliana.


Uendeshaji wake ni rahisi kiasi: tunatumia UTXO tuliyo nayo kufanya malipo na kutafuta usaidizi wa wahusika wengine ambao pia huchangia na UTXO yao wenyewe. Muamala huo unasababisha matokeo manne: mawili kati ya hayo yakiwa na kiasi sawa, moja kwa ajili ya Address ya mpokeaji malipo, nyingine kwa Address inayomilikiwa na mshirika. UTXO ya tatu inarejeshwa kwa Address nyingine ya mshirika, na kuwaruhusu kupata kiasi cha awali (hatua isiyopendelea upande wowote, ada za modulo za Mining), na UTXO ya mwisho inarudi kwa Address yetu, ambayo inajumuisha mabadiliko kutoka kwa malipo.


Kwa hivyo, majukumu matatu tofauti yanafafanuliwa katika shughuli za Stonewall x2:


- Mtumaji, ambaye hufanya malipo halisi;
- Mshiriki, ambaye hutoa bitcoins ili kuboresha kutokujulikana kwa jumla kwa shughuli, huku akipata kikamilifu fedha zao mwishoni (hatua ya neutral kwao, ada za modulo za Mining);
- Mpokeaji, ambaye huenda hajui aina mahususi ya muamala na anatarajia tu malipo kutoka kwa mtumaji.


Hebu tuchukue mfano ili kuelewa zaidi. Alice yuko dukani kununua baguette yake, ambayo inagharimu `4,000 Sats`. Anataka kulipa kwa bitcoins huku akidumisha kiwango fulani cha faragha kwa malipo yake. Kwa hivyo anamwita rafiki yake Bob, ambaye atamsaidia katika mchakato huu.

![schema stonewall x2](assets/en/1.webp)

Kwa kuchanganua muamala huu, tunaweza kuona kwamba mwokaji alipokea `4,000 Sats` kama malipo ya baguette. Alice alitumia `10,000 Sats` kama ingizo na akapokea `6,000 Sats` kama pato, na kusababisha salio halisi la `-4,000 Sats`, ambalo linalingana na bei ya baguette. Kuhusu Bob, alitoa `15,000 Sats` kama pembejeo na akapokea matokeo mawili: moja ya `4,000 Sats` na nyingine `11,000 Sats`, na kusababisha salio la `0`.

Katika mfano huu, nilipuuza ada za Mining kimakusudi ili kuwezesha kuelewana. Kwa kweli, ada za miamala hushirikiwa kwa usawa kati ya mtumaji malipo na mshirika.


## Kuna tofauti gani kati ya Stonewall na Stonewall x2?


Muamala wa StonewallX2 hufanya kazi sawasawa kabisa na muamala wa Stonewall, isipokuwa ule wa kwanza unashirikiana ilhali wa pili haufanyi kazi. Kama tulivyoona, muamala wa Stonewall x2 unahusisha ushiriki wa mtu wa tatu, ambaye yuko nje ya malipo, na ambaye atatoa bitcoins zao ili kuimarisha faragha ya ununuzi. Katika shughuli ya kawaida ya Stonewall, jukumu la mshirika linachukuliwa na mtumaji.


Wacha tuangalie tena mfano wetu wa Alice kwenye duka la mkate. Ikiwa hangeweza kupata mtu kama Bob wa kuandamana naye kwa gharama zake, angeweza kufanya shughuli ya Stonewall peke yake. Kwa hivyo, UTXO mbili za pembejeo zingekuwa zake, na angepokea 3 kwenye pato.

![transaction stonewall](assets/en/2.webp)


Kwa mtazamo wa nje, muundo wa muamala ungebaki vile vile.

![Stonewall or Stonewall x2?](assets/en/5.webp)

Kwa hivyo, mantiki inapaswa kuwa kama ifuatavyo wakati wa kutumia zana ya matumizi ya Samourai:


- Ikiwa mfanyabiashara hatatumia PayJoin Stowaway, muamala shirikishi unaweza kufanywa na mtu mwingine nje ya malipo kwa kutumia Stonewall x2.
- Ikiwa hakuna mtu anayepatikana kufanya shughuli ya Stonewall x2, muamala wa Stonewall unaweza kufanywa peke yake, kuiga tabia ya muamala wa Stonewall x2.
- Hatimaye, chaguo la mwisho litakuwa kufanya muamala na JoinBot, seva inayodumishwa na Samourai, ambayo inaweza, kwa ombi, kufanya kama mshiriki katika shughuli ya Stonewall x2.


Iwapo ungependa kupata mshirika ambaye yuko tayari kukusaidia katika muamala wa Stonewall X2, unaweza pia kutembelea kikundi hiki cha Telegram (kisicho rasmi) kinachodumishwa na watumiaji wa Samourai ili kuunganisha watumaji na washirika: [Make Every Spend a CoinJoin](https://t.me/EverySpendACoinjoin).


[**-> Pata maelezo zaidi kuhusu shughuli za Stonewall**](https://planb.network/tutorials/privacy/On-Chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)


## Madhumuni ya muamala wa Stonewall x2 ni nini?


Muundo wa Stonewall x2 huongeza kiasi kikubwa cha entropy kwenye shughuli na huchanganya uchanganuzi wa mnyororo. Kutoka nje, shughuli kama hiyo inaweza kufasiriwa kama CoinJoin ndogo kati ya watu wawili. Lakini kwa kweli, ni malipo. Njia hii inazalisha kutokuwa na uhakika katika uchanganuzi wa mnyororo, na hata husababisha miongozo ya uwongo.


Hebu turudi kwenye mfano wa Alice, Bob, na Baker. Shughuli kwenye Blockchain ingeonekana kama hii:

![stonewall x2 public](assets/en/3.webp)

Mtazamaji wa nje anayetegemea heuristic ya uchanganuzi wa kawaida anaweza kuhitimisha kimakosa kwamba "Alice na Bob walifanya CoinJoin ndogo, na UTXO moja kila moja kama ingizo na UTXO mbili kila moja kama matokeo."![misinterpretation stonewall x2](assets/en/4.webp)

Ufafanuzi huu sio sahihi kwa sababu, kama unavyojua, UTXO ilitumwa kwa Baker, Alice ana pato moja tu la mabadiliko, na Bob ana mbili.

![transaction stonewall x2](assets/en/1.webp)

Hata kama mwangalizi wa nje ataweza kutambua muundo wa shughuli ya Stonewall x2, hatakuwa na taarifa zote. Hawataweza kubainisha ni ipi kati ya UTXO mbili za kiasi sawa inalingana na malipo. Zaidi ya hayo, hawataweza kujua ikiwa ni Alice au Bob waliofanya malipo hayo. Hatimaye, hawataweza kubainisha ikiwa UTXO mbili za pembejeo zinatoka kwa watu wawili tofauti au kama ni za mtu mmoja aliyeziunganisha. Hoja hii ya mwisho ni kwa sababu ya ukweli kwamba shughuli za kawaida za Stonewall, ambazo tulijadili hapo juu, zinafuata muundo sawa na shughuli za Stonewall x2. Kutoka nje na bila maelezo ya ziada kuhusu muktadha, haiwezekani kutofautisha muamala wa Stonewall kutoka kwa shughuli ya Stonewall x2. Walakini, za kwanza sio shughuli shirikishi, wakati za mwisho ni. Hii inaongeza mashaka zaidi kuhusu gharama hii.

![Stonewall or Stonewall x2 ?](assets/en/5.webp)



## Jinsi ya kuanzisha muunganisho kati ya Paynyms ili kuweza kushirikiana kupitia Soroban?


Kama ilivyo kwa miamala mingine ya ushirikiano kwenye Samourai (*Cahoots*), kutekeleza Stonewall x2 inahusisha Exchange ya miamala iliyotiwa saini kiasi kati ya mtumaji na mshirika. Exchange hii inaweza kufanywa wewe mwenyewe, ikiwa uko pamoja na mshirika wako, au kiotomatiki kupitia itifaki ya mawasiliano ya Soroban.


Ukichagua chaguo la pili, utahitaji kuanzisha muunganisho kati ya Paynyms kabla ya kuweza kutekeleza Stonewall x2. Ili kufanya hivyo, Paynym yako lazima "ifuate" Paynym ya mshirika wako, na kinyume chake.


**Kufikia Paynym ya mshirika:**


Ili kuanza, ni muhimu kupata nambari ya malipo ya Paynym ya mshirika wako. Katika programu ya Samourai Wallet, mshirika wako lazima abonyeze aikoni ya Paynym yao (roboti ndogo) iliyo sehemu ya juu kushoto ya skrini, kisha ubofye jina la utani la Paynym, akianza na `+...`. Kwa mfano, yangu ni `+namelessmode0aF`.


![samourai paynym](assets/notext/6.webp)

Ikiwa mshirika wako anatumia Sparrow Wallet, wanapaswa kubofya kichupo cha 'Zana', kisha kwenye 'Onyesha PayNym'.![paynym sparrow](assets/notext/7.webp)

**Kufuata PayNym ya mshirika wako kutoka Samourai Wallet:**


Ikiwa unatumia Samourai Wallet, zindua programu na ufikie menyu ya 'PayNyms' kwa njia ile ile. Ikiwa hii ni mara yako ya kwanza kutumia PayNym yako, utahitaji kupata kitambulisho chake.


![request paynym samourai](assets/notext/8.webp)


Kisha ubofye bluu '+' chini kulia mwa skrini.

![add collaborator paynym](assets/notext/9.webp)

Kisha unaweza kubandika msimbo wa malipo wa mshirika wako kwa kuchagua 'BEKA MSIMBO WA MALIPO', au ufungue kamera ili kuchanganua msimbo wake wa QR kwa kubofya 'SCAN QR CODE'.

![paste paynym identifier](assets/notext/10.webp)


Bonyeza kitufe cha 'FUATA'.

![follow paynym](assets/notext/11.webp)

Thibitisha kwa kubofya 'NDIYO'.

![confirm follow paynym](assets/notext/12.webp)

Programu itakupa kitufe cha 'CONNECT'. Sio lazima kubofya kitufe hiki kwa mafunzo yetu. Hatua hii inahitajika tu ikiwa unapanga kufanya malipo kwa PayNym nyingine kama sehemu ya BIP47, ambayo haihusiani na mafunzo yetu.

![connect paynym](assets/notext/13.webp)

Mara tu PayNym yako inapofuata PayNym ya mshirika wako, rudia mchakato huu kinyume chake ili mshiriki wako pia aweze kukufuata. Kisha unaweza kufanya shughuli ya Stonewall x2.


**Kufuata PayNym ya mshirika wako kutoka Sparrow Wallet:**


Ikiwa unatumia Sparrow Wallet, fungua Wallet yako na ufikie menyu ya 'Onyesha PayNym'. Ikiwa unatumia PayNym yako kwa mara ya kwanza, utahitaji kupata kitambulisho kwa kubofya 'Rejesha PayNym'.

![request paynym sparrow](assets/notext/14.webp)

Kisha weka kitambulisho cha PayNym cha mshirika wako (ama jina la utani la '+...' au msimbo wake wa malipo 'PM...') katika kisanduku cha 'Tafuta Anwani', na ubofye kitufe cha 'Ongeza Anwani'.

![add contact paynym](assets/notext/15.webp)

Programu itakupa kitufe cha 'Unganisha Anwani'. Sio lazima kubofya kitufe hiki kwa mafunzo yetu. Hatua hii inahitajika tu ikiwa unapanga kufanya malipo kwa PayNym iliyoonyeshwa kama sehemu ya BIP47, ambayo haihusiani na mafunzo yetu.


Mara tu PayNym yako inapofuata PayNym ya mshirika wako, rudia mchakato huu kinyume chake ili mshiriki wako pia aweze kukufuata. Kisha unaweza kufanya shughuli ya Stonewall x2.

## Jinsi ya kufanya shughuli ya Stonewall x2 kwenye Samourai Wallet?


Ikiwa umekamilisha hatua za awali za kuunganisha Paynyms, hatimaye uko tayari kufanya muamala wa Stonewall x2! Ili kufanya hivyo, fuata mafunzo yetu ya video kwenye Samourai Wallet:

![Stonewall x2 Tutorial - Samourai Wallet](https://youtu.be/89oYE1Hw3Fk?si=QTqUZ6IypiR6PPMr)


## Jinsi ya kufanya shughuli ya Stonewall x2 kwenye Sparrow Wallet?


Ikiwa umekamilisha hatua za awali za kuunganisha Paynyms, hatimaye uko tayari kufanya muamala wa Stonewall x2! Ili kufanya hivyo, fuata mafunzo yetu ya video kwenye Sparrow Wallet:

![Stonewall x2 Tutorial - Sparrow Wallet](https://youtu.be/mO3Xpp34Hhk?si=bfYiTl0Gxjs9sNQq)


**Nyenzo za nje:**


- https://sparrowwallet.com/docs/spending-privately.html;
- https://docs.samourai.io/en/spend-tools#stonewallx2.