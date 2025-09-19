---
name: Boltzmann Calculator
description: Kuelewa dhana ya Entropy na jinsi ya kutumia Boltzmann
---
![cover](assets/cover.webp)


**ONYO**: Kufuatia kukamatwa kwa waanzilishi wa Samourai Wallet na kunaswa kwa seva zao mnamo Aprili 24, tovuti ya KYCP.org haipatikani kwa sasa. Gitlab inayopangisha nambari ya Calculator ya Python Boltzmann pia imekamatwa. Kufikia sasa, haiwezekani tena kupakua zana hii. Hata hivyo, kuna uwezekano kwamba msimbo huo unaweza kuchapishwa tena na wengine katika wiki zijazo. Kwa sasa, bado unaweza kufaidika na mafunzo haya ili kuelewa utendakazi wa Calculator ya Boltzmann. Viashirio vilivyotolewa na zana hii vinatumika kwa muamala yoyote ya Bitcoin na vinaweza pia kuhesabiwa kwa mikono. Nitatoa mahesabu yote muhimu katika somo hili. Ikiwa tayari ulikuwa umepakua zana ya Python kwenye mashine yako au ikiwa unatumia RoninDojo, unaweza kuen


_Tunafuatilia kwa karibu maendeleo ya kesi hii pamoja na maendeleo kuhusu zana zinazohusiana. Uwe na uhakika kwamba tutasasisha mafunzo haya kadiri habari mpya zinavyopatikana._


_Mafunzo haya yametolewa kwa madhumuni ya elimu na habari pekee. Hatuidhinishi au kuhimiza matumizi ya zana hizi kwa madhumuni ya uhalifu. Ni wajibu wa kila mtumiaji kutii sheria katika eneo la mamlaka yake._


---

Calculator ya Boltzmann ni zana ya kuchanganua muamala wa Bitcoin kwa kupima kiwango chake cha Entropy pamoja na vipimo vingine vya juu. Inatoa maarifa katika miunganisho kati ya ingizo na matokeo ya muamala. Viashirio hivi vinatoa tathmini iliyoidhinishwa ya faragha ya muamala na kusaidia kutambua makosa yanayoweza kutokea.


Zana hii ya Python ilitengenezwa na timu za Samourai Wallet na OXT, lakini inaweza kutumika kwenye muamala wowote wa Bitcoin.


## Jinsi ya kutumia Calculator ya Boltzmann?

Ili kutumia Calculator ya Boltzmann, chaguzi mbili zinapatikana kwako. Ya kwanza ni kusanikisha zana ya Python moja kwa moja kwenye mashine yako. Vinginevyo, unaweza kuchagua tovuti ya KYCP.org (_Jua Faragha ya Sarafu Yako_), ambayo hutoa jukwaa la matumizi lililorahisishwa. Kwa watumiaji wa RoninDojo, kumbuka kuwa chombo hiki tayari kimeunganishwa kwenye nodi yako.


Kutumia tovuti ya KYCP ni rahisi sana: ingiza tu kitambulisho cha muamala (txid) unachotaka kuchanganua kwenye upau wa kutafutia na ubonyeze `ENTER`.

![KYCP](assets/1.webp)

Kisha utapata taarifa tofauti kuhusu muamala, ikijumuisha viungo kati ya ingizo na matokeo. Bofya kwenye `viungo vinavyoamua`.

![KYCP](assets/2.webp)

Utafika kwenye ukurasa uliowekwa kwa viashiria vya Calculator ya Boltzmann.

![KYCP](assets/3.webp)

Kwa wale wanaopendelea kutumia zana moja kwa moja kutoka kwa nodi yao ya RoninDojo, inaweza kufikiwa kupitia `RoninCLI > Samourai Toolkit > Boltzmann Calculator`.


Kama ilivyo kwa tovuti ya KYCP.org, zana ya Python ikishasakinishwa, utahitaji tu kubandika txid ya muamala unayotaka kuchambua.


![KYCP](assets/7.webp)


Kisha, bonyeza kitufe cha `ENTER` ili kupata matokeo.


![KYCP](assets/8.webp)


## Je, ni viashiria vipi vya Calculator ya Boltzmann?

### Mchanganyiko / Tafsiri:

Kiashirio cha kwanza ambacho programu huhesabu ni jumla ya idadi ya michanganyiko inayowezekana, iliyoonyeshwa chini ya `mchanganyiko wa nb` au `fasiri` kwenye zana.


Kwa kuzingatia maadili ya UTXOs zinazohusika katika muamala, kiashiria hiki kinahesabu idadi ya njia ambazo pembejeo zinaweza kuhusishwa na matokeo. Kwa maneno mengine, huamua idadi ya tafsiri zinazokubalika ambazo muamala inaweza kupata kutoka kwa mtazamo wa mwangalizi wa nje anayeichambua.

Kwa mfano, CoinJoin iliyoundwa kulingana na muundo wa Whirlpool 5x5 inatoa `1,496` michanganyiko inayowezekana: ![KYCP](asset/4.webp)

Whirlpool Surge Cycle 8x8 CoinJoin, kwa upande mwingine, inatoa `9,934,563` tafsiri zinazowezekana: ![KYCP](assets/5.webp)

Kinyume chake, muamala wa kitamaduni wenye ingizo 1 na matokeo 2 utawasilisha tafsiri moja tu: ![KYCP](assets/6.webp)


### Entropy:

Kiashirio cha pili kilichokokotolewa ni Entropy ya muamala, iliyoteuliwa na `Entropy`.


Katika muktadha wa jumla wa kriptografia na maelezo, Entropy ni kipimo cha kiasi cha kutokuwa na uhakika au kutotabirika kuhusishwa na chanzo cha data au mchakato wa nasibu. Kwa maneno mengine, Entropy ni njia ya kupima jinsi habari ilivyo ngumu kutabiri au kukisia.


Katika muktadha mahususi wa uchanganuzi wa msururu, Entropy pia ni jina la kiashirio, linalotokana na Shannon Entropy na [iliyovumbuliwa na LaurentMT](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf), ambayo inakokotolewa kwa zana ya Boltzmann.


Wakati muamala unawasilisha idadi kubwa ya michanganyiko inayowezekana, mara nyingi inafaa zaidi kurejelea Entropy yake. Kiashiria hiki kinaruhusu kupima ukosefu wa ujuzi wa wachambuzi kuhusu usanidi halisi wa muamala. Kwa maneno mengine, juu ya Entropy, kazi ngumu zaidi ya kutambua harakati za Bitcoin kati ya pembejeo na matokeo inakuwa kwa wachambuzi.


Katika mazoezi, Entropy inaonyesha kama, kutoka kwa mtazamo wa mwangalizi wa nje, muamala inawasilisha tafsiri nyingi zinazowezekana, kulingana na kiasi cha pembejeo na matokeo, bila kuzingatia mifumo mingine ya nje au ya ndani na heuristics. Entropy ya juu basi ni sawa na usiri bora zaidi wa muamala.


Entropy inafafanuliwa kama logarithm ya binary ya idadi ya michanganyiko inayowezekana. Hapa kuna fomula iliyotumiwa:

```plaintext
E: the Entropy of the transaction
C: the number of possible combinations for the transaction

E = log2(C)
```


Katika hisabati, logarithmu ya binary (logarithm msingi-2) inalingana na utendakazi kinyume wa kubainisha 2. Kwa maneno mengine, logariti binary ya `x` ni kipeo ambacho `2` lazima iinulishwe ili kupata `x`. Kwa hivyo kiashiria hiki kinaonyeshwa kwa bits.


Wacha tuchukue mfano wa kuhesabu Entropy kwa muamala ya CoinJoin iliyoundwa kulingana na muundo wa Whirlpool 5x5, ambayo, kama ilivyotajwa hapo awali, inatoa idadi ya mchanganyiko unaowezekana wa `1,496`:

```plaintext
C = 1,496
E = log2(1,496)
E = 10.5469 bits
```

Kwa hivyo, muamala huu wa CoinJoin unaonyesha Entropy ya `10.5469 bits`, ambayo inachukuliwa kuwa ya kuridhisha sana. Kadiri thamani hii inavyokuwa juu, ndivyo tafsiri tofauti zaidi muamala inavyokubali, na hivyo kuimarisha kiwango chake cha faragha.

Kwa muamala wa 8x8 CoinJoin unaowasilisha tafsiri za `9,934,563`, Entropy itakuwa:

```plaintext
C = 9,934,563
E = log2(9,934,563)
E = 23.244 bits
```


Wacha tuchukue mfano mwingine na muamala ya kawaida zaidi, iliyo na ingizo moja na matokeo mawili: [1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://GW -16.space/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce) Kwa upande wa muamala huu, tafsiri pekee inayowezekana ni: `(In.0) > (Out.0 ; Out.1)`. Kwa hivyo, Entropy yake imeanzishwa kwa `0`:

```plaintext
C = 1
E = log2(1)
E = 0 bits
```


### Ufanisi:

Kiashiria cha tatu kinachotolewa na Calculator ya Boltzmann kinaitwa `Ufanisi wa Wallet`. Kiashirio hiki hutathmini ufanisi wa muamala kwa kuilinganisha na muamala bora unaowezekana katika usanidi unaofanana.


Hii inatuongoza kujadili dhana ya Entropy ya juu zaidi, ambayo inalingana na Entropy ya juu zaidi muundo maalum wa muamala unaweza kufikia kinadharia. Ufanisi wa muamala kisha unakokotolewa kwa kukabili Entropy hii ya juu zaidi na Entropy halisi ya muamala iliyochanganuliwa.


Formula inayotumika ni kama ifuatavyo:

```plaintext
ER: the actual Entropy of the transaction expressed in bits
EM: the maximum possible Entropy for a given transaction structure expressed in bits
Ef: the efficiency of the transaction in bits

Ef = ER - EM
```


Kwa mfano, kwa muundo wa Whirlpool 5x5 aina ya CoinJoin, kiwango cha juu cha Entropy kimewekwa kuwa `10.5469`:

```plaintext
ER = 10.5469
EM = 10.5469
Ef = 10.5469 - 10.5469 = 0 bits
```


Kiashiria hiki pia kinaonyeshwa kama asilimia, formula yake ni basi:

```plaintext
CR: the actual number of possible combinations
CM: the maximum number of possible combinations with the same structure
Ef: the efficiency expressed as a percentage

Ef = CR / CM
Ef = 1,496 / 1,496
Ef = 100%
```


Ufanisi wa `100%` kwa hivyo unaonyesha kuwa muamala huongeza uwezekano wake wa faragha kulingana na muundo wake.


### Msongamano wa Entropy:

Kiashiria cha nne ni msongamano wa Entropy, uliobainishwa kwenye zana ya `Entropy Density`. Inatoa mtazamo juu ya Entropy jamaa kwa kila pembejeo au matokeo ya muamala. Kiashiria hiki kinathibitisha kuwa muhimu kwa kutathmini na kulinganisha ufanisi wa muamala za ukubwa tofauti. Ili kuihesabu, gawanya tu jumla ya Entropy ya muamala kwa jumla ya idadi ya pembejeo na matokeo yanayohusika:

```plaintext
ED: the Entropy density expressed in bits
E: the Entropy of the transaction expressed in bits
T: the total number of inputs and outputs in the transaction

ED = E / T
```


Wacha tuchukue mfano wa Whirlpool 5x5 CoinJoin:

```plaintext
T = 5 + 5 = 10
E = 10.5469
ED = 10.5469 / 10 = 1.054 bits
```


Wacha pia tuhesabu msongamano wa Entropy kwa Whirlpool 8x8 CoinJoin:

```plaintext
T = 8 + 8 = 16
E = 23.244
ED = 23.244 / 16 = 1.453 bits
```


### Alama ya Boltzmann:

Sehemu ya tano ya taarifa iliyotolewa na Calculator ya Boltzmann ni jedwali la uwezekano wa kulinganisha kati ya ingizo na matokeo. Jedwali hili linaonyesha, kupitia alama ya Boltzmann, uwezekano wa masharti kwamba ingizo maalum linahusiana na matokeo fulani.


Kwa hivyo ni kipimo cha kiasi cha uwezekano wa masharti kwamba uhusiano kati ya ingizo na matokeo katika muamala hutokea, kulingana na uwiano wa idadi ya matukio mazuri ya tukio hili kwa jumla ya idadi ya matukio iwezekanavyo, katika seti ya tafsiri.


Kwa kuchukua mfano wa Whirlpool CoinJoin tena, jedwali la uwezekano wa masharti lingeangazia nafasi za uhusiano kati ya kila pembejeo na matokeo, ikitoa kipimo cha kiasi cha utata wa vyama katika muamala ya ununuzi:


| %       | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |
| ------- | -------- | -------- | -------- | -------- | -------- |
| Input 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 4 | 34%      | 34%      | 34%      | 34%      | 34%      |

Hapa, tunaweza kuona wazi kwamba kila ingizo lina nafasi sawa ya kuhusishwa na matokeo yoyote, ambayo huongeza usiri wa muamala.

Kuhesabu alama ya Boltzmann kunahusisha kugawanya idadi ya tafsiri ambapo tukio fulani hutokea kwa jumla ya idadi ya tafsiri zilizopo. Kwa hivyo, ili kuamua alama inayohusisha ingizo Nambari 0 na towe Nambari 3 (`512` tafsiri), utaratibu ufuatao unatumika:

```plaintext
Interpretations (IN.0 > OUT.3) = 512
Total Interpretations = 1496
Score = 512 / 1496 = 34%
```


Kwa kuchukua mfano wa Whirlpool 8x8 CoinJoin , jedwali la Boltzmann lingeonekana kama hii:


|       | OUT.0 | OUT.1 | OUT.2 | OUT.3 | OUT.4 | OUT.5 | OUT.6 | OUT.7 |
|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| IN.0  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.1  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.2  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.3  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.4  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.5  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.6  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.7  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |

Walakini, katika kesi ya muamala rahisi na pembejeo moja na matokeo mawili, hali ni tofauti:


| %       | Output 0 | Output 1 |
|---------|----------|----------|
| Input 0 | 100%     | 100%     |

Hapa, inazingatiwa kuwa uwezekano wa kila matokeo kutoka kwa ingizo Nambari 0 ni `100%`. Kwa hivyo, uwezekano mdogo hutafsiri kuwa faragha zaidi kwa kupunguza viungo vya moja kwa moja kati ya ingizo na matokeo.


### Viungo vya Kuamua:

Sehemu ya sita ya habari iliyotolewa ni idadi ya viungo vya kuamua, vinavyokamilishwa na uwiano wa viungo hivi. Kiashiria hiki kinaonyesha ni miunganisho mingapi kati ya ingizo na matokeo katika muamala iliyochanganuliwa ambayo haiwezi kupingwa, na uwezekano wa `100%`. Uwiano, kwa upande mwingine, unatoa mtazamo juu ya uzito wa viungo hivi vya kuamua ndani ya seti nzima ya viungo vya muamala.

Kwa mfano, muamala wa aina ya Whirlpool wa CoinJoin hauna viungo vya kubainisha, na kwa hivyo huonyesha kiashirio na uwiano wa `0%`. Kinyume chake, katika muamala yetu ya pili rahisi iliyochunguzwa (kwa ingizo moja na matokeo mawili), kiashirio kimewekwa kwa `2` na uwiano unafikia `100%`. Kwa hivyo, kiashiria kisicho na maana kinaashiria usiri bora kwa sababu ya kukosekana kwa viungo vya moja kwa moja na visivyoweza kupingwa kati ya pembejeo na matokeo.


**Nyenzo za Nje:**



- Msimbo wa Boltzmann kwenye Samourai
- [Miamala na Faragha ya Bitcoin (Sehemu ya I) na Laurent MT](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [Miamala na Faragha ya Bitcoin (Sehemu ya II) na Laurent MT](https://gist.github.com/LaurentMT/d361bca6dc52868573a2)
- [Miamala na Faragha ya Bitcoin (Sehemu ya III) na Laurent MT](https://gist.github.com/LaurentMT/e8644d5bc903f02613c6)
- Tovuti ya KYCP
- [Kifungu cha Kati kuhusu Utangulizi wa Hati ya Boltzmann na Laurent MT](https://medium.com/@laurentmt/introducing-Boltzmann-85930984a159)