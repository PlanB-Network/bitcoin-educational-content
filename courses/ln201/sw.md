---
name: Utangulizi wa Nadharia kuhusu Mtandao wa Lightning
goal: Kugundua Mtandao wa Lightning kutoka mtazamo wa kiufundi
objectives:
  - Kuelewa jinsi njia za mtandao zinafanya kazi.
  - Kujifunza maneno kama HTLC, LNURL, na UTXO.
  - Kuelewa usimamizi wa likiditi na ada katika LNN.
  - Kutambua Mtandao wa Lightning kama mtandao.
  - Kuelewa matumizi ya nadharia ya Mtandao wa Lightning.
---

# Safari kuelekea Tabaka la Pili la Bitcoin

Kozi hii ni somo la nadharia kuhusu jinsi Mtandao wa Lightning unavyofanya kazi kiufundi.

Karibu katika ulimwengu wa kusisimua wa Mtandao wa Lightning, tabaka la pili la Bitcoin ambalo ni tata na lina uwezo mkubwa. Tunakusudia kuingia kwenye undani wa kiufundi wa teknolojia hii, bila kuzingatia mafunzo maalum au mifano ya matumizi. Ili kupata faida kubwa kutoka kwenye kozi hii, ni muhimu kuwa na uelewa thabiti wa Bitcoin. Hii ni uzoefu ambao unahitaji mtazamo wa kujituma na umakini. Pia unaweza kuzingatia kuchukua kozi ya LN 202 kwa wakati mmoja, ambayo inatoa upande zaidi wa vitendo katika uchunguzi huu. Jiandae kuanza safari ambayo inaweza kubadilisha mtazamo wako wa mazingira ya Bitcoin.

Furahia ugunduzi!

+++

# Misingi
 
## Kuelewa Mtandao wa Lightning

![Kuelewa Mtandao wa Lightning](https://youtu.be/PszWk046x-I)

Mtandao wa Lightning ni miundombinu ya malipo ya tabaka la pili iliyojengwa kwenye mtandao wa Bitcoin ambayo inawezesha malipo ya haraka na ya gharama nafuu. Ili kuelewa kabisa jinsi Mtandao wa Lightning unavyofanya kazi, ni muhimu kuelewa ni nini njia za malipo na jinsi zinavyofanya kazi.

Njia ya malipo ya Lightning ni aina ya "njia ya faragha" kati ya watumiaji wawili ambayo inaruhusu malipo ya Bitcoin haraka na yanayorudiwa. Wakati njia inapofunguliwa, inapewa uwezo uliowekwa, ambao unatangazwa mapema na watumiaji. Uwezo huu unawakilisha kiasi kikubwa cha Bitcoin kinachoweza kuhamishwa kwenye njia wakati wowote.

Njia za malipo ni za pande mbili, maana yake zina "upande" mbili. Kwa mfano, ikiwa Alice na Bob wanafungua njia ya malipo, Alice anaweza kutuma Bitcoin kwa Bob, na Bob anaweza kutuma Bitcoin kwa Alice. Miamala ndani ya njia haiathiri uwezo wa jumla wa njia, lakini inabadilisha ugawaji wa uwezo huo kati ya Alice na Bob.

![maelezo](assets/chapitre1/0.JPG)

Ili miamala iwezekane kwenye njia ya malipo ya Lightning, mtumiaji anayetuma fedha lazima awe na kiasi cha kutosha cha Bitcoin upande wake wa njia. Ikiwa Alice anataka kutuma Bitcoin 1 kwa Bob kupitia njia yao, lazima awe na angalau Bitcoin 1 upande wake wa njia.
Vikwazo na Uendeshaji wa Njia za Malipo kwenye Lightning.
Ingawa uwezo wa njia ya malipo ya Lightning ni uliowekwa, hii haimaanishi kuwa idadi ya jumla ya miamala au kiasi cha jumla cha Bitcoin kinachoweza kuhamishwa kupitia njia hiyo ni mdogo. Kwa mfano, ikiwa Alice na Bob wana njia yenye uwezo wa Bitcoin 1, wanaweza kufanya mamia ya miamala ya Bitcoin 0.01 au maelfu ya miamala ya Bitcoin 0.001, mradi uwezo wa jumla wa njia hautazidi wakati wowote.

Licha ya vikwazo hivi, njia za malipo za Lightning ni njia yenye ufanisi ya kufanya miamala ya Bitcoin haraka na isiyo na gharama kubwa. Zinaruhusu watumiaji kutuma na kupokea Bitcoin bila kulipa ada kubwa za miamala au kusubiri muda mrefu wa uthibitisho kwenye mtandao wa Bitcoin.

Kwa muhtasari, njia za malipo za Lightning zinatoa suluhisho lenye nguvu kwa wale wanaotaka kufanya miamala ya Bitcoin haraka na isiyo na gharama kubwa. Hata hivyo, ni muhimu kuelewa jinsi wanavyofanya kazi na vikwazo vyao ili kufaidika kabisa nao.

![maelezo](assets/chapitre1/1.JPG)

Mfano:

- Alice ana SAT 100,000
- Bob ana SAT 30,000
Hii ndio hali ya sasa ya channel. Wakati wa muamala, Alice anachagua kutuma 40,000 SAT kwa Bob. Anaweza kufanya hivyo kwa sababu 40,000 < 100,000.
Hali mpya ya channel ni kama ifuatavyo:

- Alice 60,000 SAT
- Bob 70,000 SAT

```
Hali ya awali ya channel:
Alice (100,000 SAT) ============== Bob (30,000 SAT)

Baada ya uhamisho wa Alice kwa Bob wa 40,000 SAT:
Alice (60,000 SAT) ============== Bob (70,000 SAT)

```
![maelezo](assets/chapitre1/2.JPG)

Sasa, Bob anataka kutuma 80,000 SAT kwa Alice. Kwa kutokuwa na likiditi, hawezi kufanya hivyo. Uwezo mkubwa wa channel ni 130,000 SAT, na matumizi yanayowezekana hadi 60,000 SAT kwa Alice na 70,000 SAT kwa Bob.

![maelezo](assets/chapitre1/3.JPG)

## Bitcoin, anwani, UTXO na muamala

![bitcoin, anwani, utxo na muamala](https://youtu.be/cadCJ2V7zTg)

Katika sura hii ya pili, tunachukua muda wa kuchunguza jinsi muamala wa Bitcoin unavyofanya kazi, ambayo itakuwa muhimu sana kwa kuelewa Lightning. Pia tunajadili kwa kifupi dhana ya anwani za multi-saini, ambayo ni muhimu kwa kuelewa sura inayofuata juu ya kufungua channel kwenye Mtandao wa Lightning.

- Private key > Public key > Anwani: Wakati wa muamala, Alice anatuma pesa kwa Bob. Huyu wa mwisho anatoa anwani iliyotolewa na muamala wake wa umma. Alice, ambaye yeye mwenyewe alipokea pesa kwenye anwani kupitia muamala wake wa umma, sasa anatumia ufunguo wake wa kibinafsi kusaini muamala na hivyo kufungua bitcoins kutoka kwenye anwani.
- Katika muamala wa Bitcoin, bitcoins zote lazima zisonge. Zinaitwa UTXO (Unspend Transaction Output), vipande vya bitcoin vitatoka kwa mmiliki tu kurudi kwake baadaye.
  Alice ana 0.002 BTC, Bob hana BTC. Alice anachagua kutuma 0.0015 BTC kwa Bob. Atasaini muamala wa 0.002 BTC ambapo 0.0015 itakwenda kwa Bob na 0.0005 itarudi kwenye mkoba wake.

![maelezo](assets/chapitre2/0.JPG)

Hapa, kutoka kwa UTXO moja (Alice ana 0.0002 BTC kwenye anwani), tumetengeneza UTXOs 2 (Bob ana 0.0015 na Alice ana UTXO mpya (isiyohusiana na ile ya awali) ya 0.0005 BTC).

```
Alice (0.002 BTC)
  |
  V
Muamala wa Bitcoin (0.002 BTC)
  |
  |----> Bob (0.0015 BTC)
  |
  V
Alice (UTXO mpya: 0.0005 BTC)
```

Katika Mtandao wa Lightning, anwani za multi-saini hutumiwa. Kwa hivyo, saini 2 zinahitajika kufungua pesa, yaani, ufunguo wa kibinafsi wa saini 2 kuhamisha pesa. Hii inaweza kuwa Alice na Bob ambao, pamoja, lazima wakubaliane kufungua pesa (UTXO). Kwenye LN kwa kusisitiza, ni muamala wa 2/2, kwa hivyo saini zote mbili ni muhimu kabisa, tofauti na anwani za multi-saini za 2/3 au 3/5 ambapo inahitajika tu mchanganyiko wa idadi kamili ya ufunguo.

![maelezo](assets/chapitre2/1.JPG)

# Kufungua na kufunga channel

## Kufungua Channel

![fungua channel](https://youtu.be/B2caBC0Rxko)

Sasa, tutachunguza kwa karibu kufungua channel na jinsi inavyofanywa kupitia muamala wa Bitcoin.
Mtandao wa Lightning una viwango tofauti vya mawasiliano:
- Mawasiliano ya P2P (itifaki ya Mtandao wa Lightning)
- Kituo cha malipo (itifaki ya Mtandao wa Lightning)
- Muamala wa Bitcoin (itifaki ya Bitcoin)

![maelezo](assets/chapitre3/0.JPG)

Kuweka kituo, wenzake wawili wanawasiliana kupitia kituo cha mawasiliano:

- Alice: "Halo, nataka kuweka kituo!"
- Bob: "Sawa, hapa ni anwani yangu ya umma."

![maelezo](assets/chapitre3/1.JPG)

Sasa Alice ana anwani 2 za umma ili kuunda anwani ya 2/2 ya multi-sig. Sasa anaweza kufanya muamala wa Bitcoin kuutumia pesa.

Tuseme Alice ana UTXO ya 0.002 BTC na anataka kuweka kituo na Bob wa 0.0013 BTC. Ataunda muamala na UTXO 2 kama pato:

- UTXO ya 0.0013 kwa anwani ya multi-sig ya 2/2
- UTXO ya 0.0007 kwa moja ya anwani zake za kubadilisha (kurudisha UTXOs).

Muamala huu bado haujulikani kwa umma kwa sababu kwa hatua hii, anamwamini Bob aweze kufungua pesa kutoka kwenye multi-sig.

Lakini basi jinsi ya kuendelea?

Alice ataunda muamala wa pili unaoitwa "muamala wa kujiondoa" kabla ya kuchapisha amana ya pesa kwenye multi-sig.

![maelezo](assets/chapitre3/2.JPG)

Muamala wa kujiondoa utatumia pesa kutoka kwenye anwani ya multi-sig hadi anwani yake (hii inafanyika kabla ya kuchapisha kila kitu).
Baada ya muamala zote mbili kuundwa, Alice anamwambia Bob kuwa imekamilika na kumwomba saini yake na muamala huo kwa kutumia funguo zake za umma, akimweleza kuwa njia hii anaweza kurejesha pesa zake ikiwa kitu kitakwenda vibaya. Bob anakubali kwa sababu hana nia mbaya.

Sasa Alice anaweza kurejesha pesa peke yake, kwani tayari ana saini ya Bob. Anachapisha muamala. Kituo sasa kimefunguliwa na kuna 0.0013 BTC (130,000 SAT) upande wa Alice.

![maelezo](assets/chapitre3/3.JPG)

## Muamala wa Lightning na Muamala wa Ahadi

![Muamala wa Lightning na Muamala wa Ahadi](https://youtu.be/aPqI34tpypM)

![jalada](assets/chapitre4/1.JPG)

Sasa tuchambue kinachotokea nyuma ya pazia wakati wa kuhamisha pesa kutoka upande mmoja hadi mwingine wa kituo kwenye Mtandao wa Lightning, na dhana ya muamala wa ahadi. Muamala wa kufunga/kufunga kwenye mtandao wa msingi unaonyesha hali ya kituo, ikithibitisha ni nani anamiliki pesa baada ya kila uhamisho. Kwa hivyo baada ya uhamisho wa Mtandao wa Lightning, kuna sasisho la muamala/ mkataba huu ambao haujatekelezwa kati ya wenzake wawili, Alice na Bob, ambao wanajenga muamala sawa na hali ya sasa ya kituo ikiwa kuna kufunga:

- Alice anaanza kituo na Bob na 130,000 SAT upande wake. Muamala wa kujiondoa unaokubaliwa na wote kwa kufunga unaonyesha kuwa 130,000 SAT zitamwendea Alice wakati wa kufunga, na Bob anakubaliana kwa sababu ni haki.

![jalada](assets/chapitre4/2.JPG)

- Alice anatuma 30,000 SAT kwa Bob. Sasa kuna muamala mpya wa kujiondoa unaosema kuwa wakati wa kufunga, Alice atapokea 100,000 SAT na Bob 30,000 SAT. Wote wanaafikiana kwa sababu ni haki.

![jalada](assets/chapitre4/3.JPG)

- Alice anatuma 10,000 SAT kwa Bob, na muamala mpya wa kujiondoa unajengwa ukisema kuwa Alice atapokea 90,000 SAT na Bob 40,000 SAT wakati wa kufunga. Wote wanaafikiana kwa sababu ni haki.
![cover](assets/chapitre4/4.JPG)

```
Hali ya awali ya channeli:
Alice (130,000 SAT) =============== Bob (0 SAT)

Baada ya uhamisho wa kwanza:
Alice (100,000 SAT) =============== Bob (30,000 SAT)

Baada ya uhamisho wa pili:
Alice (90,000 SAT) =============== Bob (40,000 SAT)

```

Fedha hazisogei kamwe, lakini salio la mwisho linasasishwa kupitia shughuli iliyosainiwa lakini haijasajiliwa kwenye mlolongo. Kwa hivyo, shughuli ya kutoa ni shughuli ya ahadi. Uhamisho wa satoshi ni shughuli nyingine ya ahadi ambayo inasasisha salio.

## Shughuli za Ahadi

![shughuli sehemu ya 2](https://youtu.be/RRvoVTLRJ84)

Ikiwa shughuli za ahadi zinaamua hali ya channeli na ukwasi wakati X, je, tunaweza kudanganya kwa kuchapisha hali ya zamani? Jibu ni ndio, kwa sababu tayari tuna saini ya awali ya washiriki wote katika shughuli isiyosajiliwa.

![maagizo](assets/Chapitre5/0.JPG)

Ili kutatua tatizo hili, tutazidisha utata:

- Timelock = fedha zilizofungwa hadi kufikia kizuizi N
- Funguo la kufuta = siri ya Alice na siri ya Bob

Vitu hivi viwili vinaongezwa kwenye shughuli ya ahadi. Kama matokeo, Alice lazima asubiri kumalizika kwa Timelock, na yeyote anayeshikilia funguo la kufuta anaweza kuhamisha fedha bila kusubiri kumalizika kwa Timelock. Ikiwa Alice anajaribu kudanganya, Bob anatumia funguo la kufuta kuiba na kuadhibu Alice.

![maagizo](assets/Chapitre5/1.JPG)

Sasa (na kwa kweli) shughuli ya ahadi sio sawa kwa Alice na Bob, zinafanana lakini kila moja na vikwazo tofauti, wanapeana siri zao ili kuunda funguo la kufuta la shughuli ya ahadi ya awali. Kwa hivyo wakati wa uundaji, Alice anaunda channeli na Bob, 130,000 SAT upande wake, ana Timelock ambayo inamzuia kupata pesa yake mara moja, lazima asubiri kidogo. Funguo la kufuta linaweza kufungua pesa lakini Alice pekee ndiye anaye nalo (shughuli ya ahadi ya Alice). Mara tu kuna uhamisho, Alice atatoa siri yake ya zamani kwa Bob na kwa hivyo huyu wa mwisho ataweza kufuta channeli hadi hali ya awali ikiwa Alice anajaribu kudanganya (Alice anapata adhabu).

![maagizo](assets/Chapitre5/2.JPG)

Vivyo hivyo, Bob atatoa siri yake kwa Alice. Kwa hivyo ikiwa anajaribu kudanganya, Alice anaweza kumwadhibu. Uendeshaji huu unarudiwa kwa kila shughuli mpya ya ahadi. Siri mpya inaamuliwa na funguo mpya la kufuta. Kwa hivyo kwa kila shughuli mpya, shughuli ya ahadi ya awali lazima iharibiwe kwa kutoa siri ya kufuta. Kwa hivyo ikiwa Alice au Bob anajaribu kudanganya, mwingine anaweza kuchukua hatua kabla (kutokana na Timelock) na hivyo kuepuka udanganyifu. Wakati wa shughuli #3, siri ya shughuli #2 kwa hivyo inatolewa ili kuruhusu Alice na Bob kujilinda dhidi ya Alice au Bob.

![maagizo](assets/Chapitre5/3.JPG)

Mtu anayeanzisha shughuli na Timelock (yule anayetuma pesa) anaweza kutumia funguo la kufuta baada ya Timelock. Walakini, mtu anayepokea pesa anaweza kuitumia kabla ya Timelock ikiwa kuna udanganyifu kutoka upande mmoja hadi mwingine wa channeli kwenye Mtandao wa Lightning. Hasa, tunaelezea mifumo inayoturuhusu kujilinda dhidi ya udanganyifu wowote kutoka kwa mshirika wetu ndani ya channeli.

## Kufunga Channeli

![funga channeli](https://youtu.be/FVmQvNpVW8Y)
Tunavutiwa na kufunga kituo kupitia shughuli ya Bitcoin, ambayo inaweza kuchukua fomu tofauti kulingana na kesi. Kuna aina 3 za kufunga kituo:
- Iliyo nzuri: kufunga kwa ushirikiano
- Iliyo nguvu: kufunga kwa kulazimishwa (isiyo ya ushirikiano)
- Iliyo hila: kufunga kwa mlaghai

![maelekezo](assets/chapitre6/1.JPG)
![maelekezo](assets/chapitre6/0.JPG)


### Iliyo nzuri

Washiriki wawili wanawasiliana na kukubaliana kufunga kituo. Wanakomesha shughuli zote na kuthibitisha hali ya mwisho ya kituo. Wanakubaliana juu ya ada za mtandao (mtu ambaye alifungua kituo anachukua ada za kufunga). Sasa wanatengeneza shughuli ya kufunga. Kuna shughuli ya kufunga, tofauti na shughuli za ahadi kwa sababu hakuna Timelock na ufunguo wa kufuta. Shughuli hiyo kisha inachapishwa na Alice na Bob wanapokea salio lao kwa mtiririko huo. Aina hii ya kufunga ni haraka (kwa sababu hakuna Timelock) na kwa ujumla ni gharama nafuu.

![maelekezo](assets/chapitre6/3.JPG)


### Iliyo nguvu

Alice anataka kufunga kituo, lakini Bob hajibu kwa sababu yuko nje ya mtandao (kukatika kwa mtandao au umeme). Alice kisha atachapisha shughuli ya ahadi ya hivi karibuni zaidi (ya mwisho). Shughuli hiyo inachapishwa na Timelock inaanzishwa. Kisha, ada ziliamuliwa wakati shughuli hii iliumbwa X wakati uliopita! MemPool ni mtandao ambao umebadilika tangu wakati huo, kwa hivyo itifaki inarudi kwa ada mara 5 zaidi ya sasa wakati shughuli iliumbwa. Ada ya uundaji ni SAT 10, kwa hivyo shughuli inachukuliwa kuwa SAT 50. Wakati wa kufunga kwa kulazimishwa, mtandao ni:

- 1 SAT = imezidiwa na 50\*
- 100 SAT = imepungukiwa na 2\*

Hii inafanya kufunga kwa kulazimishwa kuwa mrefu (Timelock) na haswa hatari zaidi kwa ada na uthibitisho unaowezekana na wachimbaji.

![maelekezo](assets/chapitre6/4.JPG)

### Iliyo hila

Alice anajaribu kudanganya kwa kuchapisha shughuli ya ahadi ya zamani. Lakini Bob anafuatilia MemPool na anatazama shughuli ambazo zinajaribu kuchapisha za zamani. Ikiwa anapata yoyote, anatumia ufunguo wa kufuta kuadhibu Alice na kuchukua SAT zote kutoka kwenye kituo.

![maelekezo](assets/chapitre6/5.JPG)

Kwa hitimisho, kufunga kituo katika Mtandao wa Lightning ni hatua muhimu ambayo inaweza kuchukua fomu tofauti. Katika kufunga kwa ushirikiano, pande zote mbili zinawasiliana na kukubaliana juu ya hali ya mwisho ya kituo. Hii ni chaguo haraka zaidi na gharama nafuu. Kwa upande mwingine, kufunga kwa kulazimishwa hutokea wakati moja ya pande haijibu. Hii ni hali ghali zaidi na ya muda mrefu kutokana na ada za shughuli zisizotabirika na kuanzishwa kwa Timelock. Hatimaye, ikiwa mshiriki anajaribu kudanganya kwa kuchapisha shughuli ya ahadi ya zamani, mlaghai anaweza kuadhibiwa kwa kupoteza SAT zote kutoka kwenye kituo. Ni muhimu kuelewa mifumo hii kwa matumizi yenye ufanisi na ya haki ya Mtandao wa Lightning.

# Mtandao wa likiditi

## Mtandao wa Lightning

![Mtandao wa Lightning](https://youtu.be/RAZAa3v41DM)

Katika sura hii ya saba, tunachunguza jinsi Lightning inavyofanya kazi kama mtandao wa vituo na jinsi malipo yanavyotumwa kutoka chanzo hadi marudio yao.

![jalada](assets/Chapitre7/0.JPG)
![jalada](assets/Chapitre7/1.JPG)

Lightning ni mtandao wa vituo vya malipo. Maelfu ya washiriki na vituo vyao vya likiditi wameunganishwa na kila mmoja, na hivyo kujitumia kufanya shughuli kati ya washiriki ambao hawajaunganishwa. Likiditi ya vituo hivi haiwezi kuhamishiwa kwa vituo vingine vya likiditi.
Alice -> Eden -> Bob`. Satoshis have not moved from `Alice -> Bob`, but from `Alice -> Eden`and from`Eden -> Bob`.
So each person and channel has different liquidity. To make payments, you need to find a route in the network with enough liquidity. If there isn't enough, the payment won't go through.

Consider the following network:

```
Hali ya awali ya mtandao:
Alice (130 SAT) ==== (0 SAT) Susie (90 SAT) ==== (200 SAT) Eden (150 SAT) ==== (100 SAT) Bob
```
![cover](assets/Chapitre7/2.JPG)

Ikiwa Alice anataka kuhamisha 40 SAT kwa Bob, basi likizo itagawanywa upya kwenye njia kati ya pande mbili.

```
Baada ya Alice kuhamisha 40 SAT kwa Bob:
Alice (90 SAT) ==== (40 SAT) Susie (50 SAT) ==== (240 SAT) Eden (110 SAT) ==== (140 SAT) Bob
```

![cover](assets/Chapitre7/4.JPG)

Hata hivyo, katika hali ya awali, Bob hawezi kutuma 40 SAT kwa Alice kwa sababu Susie hana likizo yoyote na Alice ya kutuma 40 SAT, kwa hivyo malipo hayawezekani kupitia njia hii. Kwa hivyo tunahitaji njia nyingine ambapo shughuli hiyo ni haiwezekani.

Katika mfano wa kwanza, ni wazi kwamba Susie na Eden hawajapoteza kitu na hawajapata kitu. Nodes za Lightning Network hutoza ada kwa kukubali kutumika kama njia ya kusafirisha shughuli!

Kuna ada tofauti kulingana na mahali likizo inapatikana

Alice - Bob

- Ada ya Alice = Alice -> Bob
- Ada ya Bob = Bob -> Alice

![cover](assets/Chapitre7/5.JPG)

Kuna aina mbili za ada:

- ada ya kudumu bila kujali kiasi: 1 SAT (chaguo-msingi lakini inaweza kubadilishwa)
- ada inayoweza kubadilika (0.01% kwa chaguo-msingi)

Mfano wa ada:

- Alice - Susie; 1/1 (gharama ya kudumu na gharama inayoweza kubadilika)
- Susie - Eden; 0/200
- Eden - Bob; 1/1

Kwa hivyo:

- Ada 1: (ililipwa na Alice kwake mwenyewe) 1 + (40,000 * 0.000001)
- Ada 2: 0 + 40,000 * 0.0002 = 8 SAT
- Ada 3: 1 + 40,000 * 0.000001 = 0.4 SAT

![cover](assets/Chapitre7/6.JPG)

Usafirishaji:

1. Usafirishaji wa 40,009.04 Alice -> Susie; Alice anagharamia gharama zake mwenyewe kwa hivyo hazihesabiwi
2. Susie anafanya Eden kufanya kibali cha 40,001.04; anachukua tume hii ya 8 SAT
3. Eden anafanya huduma ya kutuma 40,000 kwa Bob, anachukua ada yake ya 1.04 SAT.

Alice alilipa ada ya 9.04 SAT na Bob alipokea 40,000 SAT.

![cover](assets/Chapitre7/7.JPG)

Katika Lightning Network, ni node ya Alice ambayo inaamua njia kabla ya kutuma malipo. Kwa hivyo, kuna utafutaji wa njia bora na Alice ndiye pekee anayejua njia na bei. Malipo yanasafirishwa, lakini Susie hana habari.

![cover](assets/Chapitre7/9.JPG)
Kwa Susie au Eden: hawajui ni nani mpokeaji wa mwisho, wala ni nani anayetuma malipo. Hii ni njia ya vitunguu. Node lazima iwe na mpango wa mtandao ili kupata njia yake, lakini hakuna mmoja wa wapatanishi ana habari yoyote.

## HTLC - Mkataba wa Muda Uliofungwa kwa Kutumia Hash

![HTLC](https://youtu.be/-JC4mkq7H48)

Katika mfumo wa kawaida wa usambazaji, tunawezaje kuhakikisha kuwa Eden haibi na anaheshimu sehemu yake ya mkataba?

HTLC ni mkataba wa malipo ambao unaweza kufunguliwa tu kwa kutumia siri. Ikiwa siri haijafichuliwa, basi mkataba unakwisha muda wake. Kwa hivyo ni malipo yanayotegemea hali. Jinsi gani hutumiwa?

![maagizo](assets/chapitre8/0.JPG)

Fikiria hali ifuatayo:

`Alice (100,000 SAT) ==== (30,000 SAT) Susie (250,000 SAT) ==== (0 SAT) Bob`

- Bob anazalisha siri S (preimage) na kuhesabu hash r = hash(s)
- Bob anatuma ankara kwa Alice na "r" imejumuishwa
- Alice anatuma HTLC ya 40,000 SAT kwa Susie na hali ya kufichua "s'" ambayo hash(s') = r
- Susie anatuma HTLC sawa kwa Bob
- Bob anafungua HTLC ya Susie kwa kumwonyesha "s"
- Susie anafungua HTLC ya Alice kwa kumwonyesha "S"

Ikiwa Bob hayupo mtandaoni na kamwe hajapata siri ambayo inampa uhalali wa kupokea pesa, basi HTLC itakwisha muda wake baada ya idadi fulani ya vitalu.

![maagizo](assets/chapitre8/1.JPG)

HTLCs hukwisha muda wake kwa utaratibu wa kurudi: kwanza ni HTLC ya Susie-Bob, kisha HTLC ya Alice-Susie. Kwa njia hii, ikiwa Bob anarudi, haitabadilisha chochote. Vinginevyo, ikiwa Alice anafuta wakati Bob anarudi, itakuwa fujo na watu wanaweza kuwa wamefanya kazi bure.

Kwa hivyo, nini kinatokea katika kufunga? Kwa kweli, shughuli zetu za ahadi ni ngumu zaidi. Tunahitaji kuwakilisha salio la kati ikiwa njia imefungwa.

Kwa hivyo, kuna HTLC ya 40,000 satoshi (na vikwazo vilivyotajwa hapo awali) katika shughuli ya ahadi kupitia pato #3.

![maagizo](assets/chapitre8/2.JPG)

Alice ana katika shughuli ya ahadi:

- Pato #1: 60,000 SAT kwa Alice kupitia Timelock na ufunguo wa kufuta (kile kinachobaki kwake)
- Pato #2: 30,000 ambazo tayari ni mali ya Susie
- Pato #3: 40,000 katika HTLC

Shughuli ya ahadi ya Alice ina HTLC-out kwa sababu anatuma HTLC-in kwa mpokeaji, Susie.

![maagizo](assets/chapitre8/3.JPG)

Kwa hivyo, ikiwa tunachapisha shughuli hii ya ahadi, Susie anaweza kupata pesa za HTCL na "s" picha. Ikiwa hana pre-image, Alice anapata pesa baada ya HTCL kumalizika muda wake. Fikiria pato (UTXO) kama malipo tofauti na hali tofauti.
Baada ya malipo kufanyika (kumalizika muda wake au utekelezaji), hali ya njia inabadilika na shughuli na HTCL haipo tena. Tunarudi kwenye kitu cha kawaida.
Katika kufunga kwa ushirikiano: tunasitisha malipo na kusubiri utekelezaji wa uhamisho / HTCL, shughuli ni nyepesi kwa hivyo gharama ni ndogo kwa sababu kuna pato la 1 au 2 kwa kiwango cha juu.
Ikiwa kufunga kwa kulazimishwa: tunachapisha na HTLC zote zilizoendelea, kwa hivyo inakuwa nzito sana na ghali sana. Na ni fujo.
Kwa muhtasari, mfumo wa usambazaji wa Lightning Network hutumia Mikataba ya Hash Time-Locked (HTLC) ili kuhakikisha malipo salama na yanayoweza kuthibitishwa. HTLC huruhusu malipo ya masharti ambapo pesa zinaweza kufunguliwa tu kwa siri, hivyo kuhakikisha washiriki wanatimiza ahadi zao. Katika mfano uliowasilishwa, Alice anataka kutuma SAT kwa Bob kupitia Susie. Bob anazalisha siri, anaunda hash yake, na kuituma kwa Alice. Alice na Susie wanaweka HTLC kulingana na hash hii. Mara Bob anapofungua HTLC ya Susie kwa kumwonyesha siri, Susie anaweza kisha kufungua HTLC ya Alice.

Katika tukio ambalo Bob haifunui siri ndani ya kipindi fulani cha wakati, HTLC inakwisha muda wake. Ukwishaji unatokea kwa mpangilio wa nyuma, kuhakikisha kuwa ikiwa Bob anarudi mtandaoni, hakuna matokeo yasiyotarajiwa.

Wakati wa kufunga kituo, ikiwa ni kufunga kwa ushirikiano, malipo yanakatishwa na HTLC zinafanyiwa utatuzi, ambao kwa ujumla ni gharama ndogo. Ikiwa kufunga ni kwa nguvu, shughuli zote za HTLC zinazofanyika zinachapishwa, ambayo inaweza kuwa ghali na yenye fujo.

Kwa muhtasari, mfumo wa HTLC unaongeza safu ya ziada ya usalama kwa Lightning Network, kuhakikisha kuwa malipo yanatekelezwa kwa usahihi na watumiaji wanatimiza ahadi zao.

## Kupata njia yako

![kupata njia yako](https://youtu.be/wnUGJjOxd9Q)

Data pekee ya umma ni uwezo wa jumla wa kituo (Alice + Bob) lakini hatujui wapi likizo iko.
Ili kupata habari zaidi, nodi yetu inasikiliza kituo cha mawasiliano cha LN kwa matangazo ya njia mpya na sasisho za ada ya njia. Nodi yako pia inatazama blockchain kwa kufunga kwa kituo.

Kwa kuwa hatuna habari yote, lazima tafute grafu/njia na habari tunayo (uwezo wa juu wa kituo na sio wapi likizo iko).

Vigezo:

- Uwezekano wa mafanikio - Ada
- Muda wa ukomo wa HTLC
- Idadi ya nodi za kati
- Bahati nasibu

![grafu](assets/chapitre9/1.JPG)

Kwa hivyo ikiwa kuna njia 3 zinazowezekana:

- Alice > 1 > 2 > 5 > Bob
- Alice > 1 > 2 > 4 > 5 > Bob
- Alice 1 > 2 > 3 > Bob

Tunatafuta njia bora kwa nadharia na ada ya chini na nafasi kubwa ya mafanikio: likizo kubwa na hatua chache iwezekanavyo.

Kwa mfano, ikiwa 2-3 ina uwezo wa 130,000 SAT tu, kutuma 100,000 ni jambo lisilowezekana sana, kwa hivyo chaguo #3 hakuna nafasi ya mafanikio.

![grafu](assets/chapitre9/2.JPG)

Sasa algorithm imefanya chaguzi zake 3 na itajaribu ya kwanza:

Chaguo 1:

- Alice anatuma HTLC ya 100,000 SAT kwa 1;
- 1 anafanya HTLC ya 100,000 SAT kwa 2;
- 2 anafanya HTLC ya 100,000 SAT kwa 5, lakini 5 hawezi kufanya hivyo, kwa hivyo anatangaza.

Taarifa inatumwa nyuma, kwa hivyo Alice anachagua kujaribu njia ya pili:

- Alice anatuma HTLC ya 100,000 kwa 1;
- 1 anafanya HTLC ya 100,000 kwa 2;
- 2 anafanya HTLC ya 100,000 kwa 4;
- 4 anafanya HTLC ya 100,000 kwa Bob. Bob ana likizo, kwa hivyo ni sawa.
- Bob anatumia preimage (hash) ya HTLC na hivyo anatumia siri kuokoa 100,000 SAT
- Sasa 5 ana siri ya HTLC kuokoa HTLC iliyozuiliwa kutoka kwa 4
- 4 sasa ana siri ya HTLC ya kupata HTLC iliyozuiliwa kutoka 2- 2 sasa ana siri ya HTLC ya kupata HTLC iliyozuiliwa kutoka 1
- 1 sasa ana siri ya HTLC ya kupata HTLC iliyozuiliwa ya Alice

Alice hakuyaona kushindwa kwa njia 1, alisubiri tu sekunde moja zaidi. Kukosekana kwa malipo hutokea wakati hakuna njia inayowezekana. Ili kurahisisha utafutaji wa njia, Bob anaweza kutoa habari kwa Alice ili kumsaidia na ankara yake:

- Kiasi
- Anwani yake
- Hash ya preimage ili Alice aweze kuunda HTLC
- Maelezo juu ya njia za Bob

Bob anajua upatikanaji wa njia 5 na 3 kwa sababu yeye anaunganishwa moja kwa moja nao, anaweza kumwambia Alice hii. Anamwonya Alice kuwa node 3 haina maana, ambayo inazuia Alice kutumia njia yake.
Elementingine ni njia za kibinafsi (kwa hivyo hazijachapishwa kwenye mtandao) ambazo Bob anaweza kuwa nazo. Ikiwa Bob ana njia ya kibinafsi na 1, anaweza kumwambia Alice itumie na itampa Alice > 1 > Bob'.

![graph](assets/chapitre9/3.JPG)

Kwa hitimisho, kusafirisha shughuli kwenye Mtandao wa Lightning ni mchakato mgumu ambao unahitaji kuzingatia mambo mbalimbali. Ingawa uwezo wa jumla wa njia unajulikana, usambazaji sahihi wa upatikanaji wa njia haupatikani moja kwa moja. Hii inalazimisha nodi kuthibitisha njia za mafanikio zaidi, kwa kuzingatia vigezo kama ada, muda wa kumalizika kwa HTLC, idadi ya nodi za kati, na kipengele cha nasibu. Wakati njia nyingi zinawezekana, nodi zinatafuta kupunguza ada na kuongeza nafasi za mafanikio kwa kuchagua njia zenye upatikanaji wa kutosha na idadi ya hops ya chini. Ikiwa jaribio la shughuli linashindwa kutokana na upatikanaji wa kutosha, njia nyingine inajaribiwa hadi shughuli inafanikiwa.

Zaidi ya hayo, ili kurahisisha utafutaji wa njia, mpokeaji anaweza kutoa habari zaidi kama anwani, kiasi, hash ya preimage, na maelezo juu ya njia zao. Hii inaweza kusaidia kutambua njia zenye upatikanaji wa kutosha na kuepuka jaribio lisilo la lazima la shughuli. Hatimaye, mfumo wa usafirishaji wa Mtandao wa Lightning umebuniwa ili kuboresha kasi, usalama, na ufanisi wa shughuli wakati unahifadhi faragha ya mtumiaji.

# Vifaa vya Mtandao wa Lightning

## Ankara, LNURL, Keysend

![ankara, LNURL, Keysend](https://youtu.be/CHnXJuZTarU)

![cover](assets/chapitre10/0.JPG)

Ankara ya LN (au ankara) ni ndefu na haifurahishi kusoma, lakini inaruhusu uwakilishi mzito wa ombi la malipo.

Mfano:
lnbc1m1pskuawzpp5qeuuva2txazy5g483tuv9pznn9ft8l5e49s5dndj2pqq0ptyn8msdqqcqzpgxqrrsssp5v4s00u579atm0em6eqm9nr7d0vr64z5j2sm5s33x3r9m4lgfdueq9qyyssqxkjzzgx5ef7ez3dks0laxayx4grrw7j22ppgzyhpydtv6hmc39skf9hjxn5yd3kvv7zpjdxd2s7crcnemh2fz26mnr6zu83w0a2fwxcqnvujl3

- lnbc1m = sehemu inayoweza kusomwa
- 1 = utenganisho kutoka sehemu iliyobaki
- Kisha sehemu iliyobaki
- Bc1 = uandishi wa Bech32 (msingi 32), kwa hivyo wahusika 32 hutumiwa.
- 10 = 1.2.3.4.5.6.7.8.9.0- 26 = abcdefghijklmnopqrstuvwxyz
- 32 = sio "b-i-o" na sio "1"

### lnbc1m

- ln = Lightning
- Bc = bitcoin (mainnet)
- 1 = kiasi
- M = milli (10*-3 / u = micro 10*-6 / n = nano 10*-9 / p = pico 10*-12'
  Hapa 1m = 1 \* 0.0001btc = 100,000 BTC
  "Tafadhali lipa 100,000 SAT kwenye mtandao wa Lightning wa Bitcoin mainnet kwa pskuawzpp5qeuuva2txazy5g483tuv9pznn9ft8l5e49s5dndj2pqq0ptyn8msdqqcqzpgxqrrsssp5v4s00u579atm0em6eqm9nr7d0vr64z5j2sm5s33x3r9m4lgfdueq9qyyssqxkjzzgx5ef7ez3dks0laxayx4grrw7j22ppgzyhpydtv6hmc39skf9hjxn5yd3kvv7zpjdxd2s7crcnemh2fz26mnr6zu83w0a2fwxcqnvujl3"

### Muda (wakati iliumbwa)

Ina sehemu 0 au zaidi:

- Hash ya preimage
- Siri ya malipo (onion routing)
- Data isiyo na kikomo
- LN muhimu ya umma ya mpokeaji
- Muda wa kumalizika (chaguo-msingi saa 1)
- Vidokezo vya njia
- Saini ya yote

Kuna aina nyingine za ankara. Meta-protoksi ya LNURL inaruhusu kutoa kiasi cha satoshi moja kwa moja badala ya kufanya ombi. Hii ni ya kubadilika sana na inaruhusu uboreshaji mwingi kwa upande wa uzoefu wa mtumiaji.

![cover](assets/chapitre10/2.JPG)

Keysend inaruhusu Alice kutuma pesa kwa Bob bila kuwa na ombi la Bob. Alice anapata Kitambulisho cha Bob, anaunda preimage bila kuuliza Bob, na kuichukua katika malipo yake. Kwa hivyo, Bob atapokea ombi la kushangaza ambapo anaweza kufungua pesa kwa sababu Alice tayari amefanya kazi.

![cover](assets/chapitre10/3.JPG)

Kwa hitimisho, ankara ya Lightning Network, ingawa ngumu kwa mtazamo wa kwanza, inakodisha kwa ufanisi ombi la malipo. Kila sehemu ya ankara ina habari muhimu, ikiwa ni pamoja na kiasi cha kulipwa, mpokeaji, muda wa kuundwa, na habari nyingine kama vile hash ya preimage, siri ya malipo, vidokezo vya njia, na muda wa kumalizika. Itifaki kama LNURL na Keysend zinaleta uboreshaji mkubwa kwa upande wa kubadilika na uzoefu wa mtumiaji, kuruhusu, kwa mfano, kutuma fedha bila ombi la awali kutoka kwa upande mwingine. Teknolojia hizi zinafanya mchakato wa malipo kuwa laini na ufanisi zaidi kwenye Lightning Network.

## Kusimamia Urahisi

![kusimamia urahisi](https://youtu.be/YuPrbhEJXbg)

![maagizo](assets/chapitre11/0.JPG)


Tunatoa mwongozo wa jumla kujibu swali la kudumu la kusimamia urahisi kwenye Lightning.

Katika LN, kuna aina 3 za watu:

- Wanunuzi: wana uwezo wa kutuma pesa, ambayo ni rahisi zaidi kwa sababu wanahitaji tu kufungua njia
- Wafanyabiashara: ni ngumu zaidi kwa sababu wanahitaji uwezo wa kupokea pesa kutoka kwa nodi na wahusika wengine. Lazima wawe na watu waliounganishwa nao
- Nodes za Routing: wanataka kuwa na usawa na likiditi kwa pande zote na kuwa na uhusiano mzuri na nodes nyingi ili kutumika kadri iwezekanavyo
Kwa hivyo, ikiwa unahitaji likiditi ya kuingia, unaweza kununua kutoka kwa huduma.

![maagizo](assets/chapitre11/1.JPG)

Alice ananunua channel na Susie kwa 1 milioni satoshis, kwa hivyo anafungua channel na moja kwa moja 1,000,000 SAT kwenye upande wa kuingia. Kisha anaweza kukubali hadi 1 milioni SAT kama malipo kutoka kwa wateja ambao wameunganishwa na Susie (ambaye ana uhusiano mzuri).

Suluhisho lingine litakuwa kufanya malipo; unalipa 100,000 kwa sababu X, sasa unaweza kupokea 100,000.

![maagizo](assets/chapitre11/2.JPG)

### Suluhisho la Loop Out: Atomic swap LN - BTC

Alice 2 milioni - Susie 0

![maagizo](assets/chapitre11/3.JPG)

Alice anataka kutuma likiditi kwa Susie, kwa hivyo anafanya Loop out (node maalum inayotoa huduma ya pro ya kurekebisha LN/BTC).
Alice anatuma 1 milioni kwa Loop kupitia node ya Susie, kwa hivyo Susie ana likiditi na Loop anatuma usawa wa on-chain nyuma kwenye node ya Alice.

![maagizo](assets/chapitre11/4.JPG)

Kwa hivyo milioni 1 inakwenda kwa Susie, Susie anatuma milioni 1 kwa Loop, Loop anatuma milioni 1 kwa Alice. Kwa hivyo Alice amehamisha likiditi kwa Susie kwa gharama ya ada fulani zilizolipwa kwa Loop kwa huduma.

Jambo gumu zaidi katika LN ni kudumisha likiditi.

![maagizo](assets/chapitre11/5.JPG)

Kwa hitimisho, usimamizi wa likiditi kwenye Lightning Network ni suala muhimu ambalo linategemea aina ya mtumiaji: mnunuzi, muuzaji, au node ya routing. Wanunuzi, ambao wanahitaji likiditi ya kutoka, wana kazi rahisi: wanafungua tu channels. Wafanyabiashara, ambao wanahitaji likiditi ya kuingia, lazima wawe na uhusiano na nodes na wahusika wengine. Nodes za routing, kwa upande mwingine, wanatafuta kudumisha usawa wa likiditi kwa pande zote. Suluhisho kadhaa zipo kwa usimamizi wa likiditi, kama kununua channels au kulipa kuongeza uwezo wa kupokea. Chaguo la "Loop Out", kuruhusu Atomic Swap kati ya LN na BTC, linaleta suluhisho la kuvutia kwa kurekebisha likiditi. Licha ya mikakati hii, kudumisha likiditi kwenye Lightning Network bado ni changamoto ngumu.

# Endelea zaidi
## Muhtasari wa kozi

![hitimisho](https://youtu.be/MaWpD0rbkVo)

Lengo letu lilikuwa kuelezea jinsi Lightning Network inavyofanya kazi na jinsi inavyotegemea Bitcoin ili kufanya kazi.

Lightning Network ni mtandao wa channels za malipo. Tumeona jinsi channel ya malipo inavyofanya kazi kati ya wadau wawili, lakini pia tumepanua maono yetu kwa mtandao mzima, kwa dhana ya mtandao wa channels za malipo.

![maagizo](assets/chapitre12/0.JPG)

Channels zinafunguliwa kupitia shughuli ya Bitcoin na zinaweza kuhifadhi shughuli nyingi iwezekanavyo. Hali ya channel inawakilishwa na shughuli ya ahadi ambayo inawapelekea kila mshiriki kile wanacho upande wao wa channel. Wakati shughuli inatokea ndani ya channel, wadau wanajitolea kwa hali mpya kwa kufuta hali ya zamani na kujenga shughuli mpya ya ahadi.

![maagizo](assets/chapitre12/1.JPG)

Washirika wanajilinda kutokana na udanganyifu na funguo za kufuta na kufunga wakati. Kufunga kwa makubaliano ya pande zote kunapendelewa kufunga channel. Kwa kufunga kwa kulazimishwa, shughuli ya ahadi ya mwisho inachapishwa.
Malipo yanaweza kukopa njia kutoka kwa nodi za kati zingine. Malipo ya masharti kwenye kufunga wakati wa kufunga (HTLC) huruhusu fedha kufungwa hadi malipo yatatuliwe kabisa. Onion routing hutumiwa kwenye Mtandao wa Lightning. Nodi za kati hazijui marudio ya mwisho ya malipo. Alice lazima ihesabu njia ya malipo, lakini hana habari yote juu ya likiditi katika njia za kati.
![maagizo](mali/chapitre12/4.JPG)

Kuna sehemu ya uwezekano wakati wa kutuma malipo kupitia Mtandao wa Lightning.

![maagizo](mali/chapitre12/5.JPG)

Ili kupokea malipo, likiditi lazima lisimamiwe katika njia, ambayo inaweza kufanywa kwa kuomba wengine wafungue njia kwetu, kufungua njia wenyewe, na kutumia zana kama Loop au kununua/kukodisha njia kwenye masoko.


## Mahojiano ya Fanis

![Mahojiano ya Fanis](https://youtu.be/VeJ4oJIXo9k)

Hapa kuna muhtasari wa mahojiano:

Mtandao wa Lightning ni suluhisho la malipo la haraka sana kwenye Bitcoin ambalo huruhusu kuepuka vizuizi vinavyohusiana na uwezo wa mtandao. Walakini, bitcoins kwenye Lightning sio salama kama zile kwenye mnyororo wa Bitcoin kwa sababu decentralization na usalama vinapewa kipaumbele kuliko uwezo wa kupanua.

Ongezeko kubwa la ukubwa wa kizuizi sio suluhisho nzuri kwani inahatarisha nodi na uwezo wa data. Badala yake, Mtandao wa Lightning huruhusu kuunda njia za malipo kati ya watumiaji wawili wa Bitcoin bila kuonyesha shughuli kwenye blockchain, kuokoa nafasi kwenye vitalu na kuruhusu Bitcoin kupanuka leo.

Walakini, kuna ukosoaji kuhusu uwezo wa kupanua na kuzingatia Mtandao wa Lightning, na masuala yanayowezekana yanayohusiana na kufunga njia na ada kubwa za shughuli. Kwa kutatua matatizo haya, inapendekezwa kuepuka kufungua njia ndogo ili kuepuka matatizo ya baadaye na kuongeza ada za shughuli na Child Pay for Parent.

Suluhisho zinazofikiriwa kwa siku zijazo za Mtandao wa Lightning ni kuchanganya na kuunda njia kwa vikundi ili kupunguza ada za shughuli, pamoja na kuongeza ukubwa wa kizuizi kwa muda mrefu. Walakini, ni muhimu kuzingatia kuwa bitcoins kwenye Lightning sio salama kama bitcoins kwenye mnyororo wa Bitcoin.

Faragha kwenye Bitcoin na Lightning zimeunganishwa, na onion routing ikitoa kiwango fulani cha faragha kwa shughuli. Walakini, kwenye Bitcoin, kila kitu ni wazi kwa chaguo-msingi, na heuristics hutumiwa kufuatilia Bitcoins kutoka anwani hadi anwani kwenye mnyororo wa Bitcoin.

Kununua Bitcoins na KYC kunaruhusu ubadilishaji kujua shughuli za kutoa, wakati kiasi cha pande zote na anwani za mabadiliko huwezesha kujua sehemu gani ya shughuli inalenga kwa mtu mwingine na sehemu gani inalenga kwa mtu binafsi.

Kuboresha faragha, hatua za pamoja na coinjoins huruhusu kuvunja hesabu za uwezekano kwa kufanya shughuli ambapo watu wengi wanafanya shughuli pamoja. Kampuni za uchambuzi wa mnyororo zina wakati mgumu kujua unachofanya na bitcoins yako kwa kufuata.

Kwenye Lightning, watu wawili tu wanajua shughuli, na ni ya siri zaidi kuliko Bitcoin. Onion routing inamaanisha kuwa nodi ya kati haijui mtumaji na mpokeaji wa malipo.

Ili kutumia Mtandao wa Lightning, inapendekezwa kufuata mafunzo kwenye kituo chako cha YouTube au moja kwa moja kwenye wavuti ya kugundua Bitcoin, au kutumia mafunzo kwenye Umbrell. Pia, ni muhimu kutambua kuwa nodi za usambazaji wa Lightning zinaweza kudhibitiwa katika siku zijazo, na baadhi ya nchi zinajaribu kudhibiti nodi za usambazaji. Kwa wafanyabiashara, ni muhimu kusimamia likiditi ili kukubali malipo kwenye Mtandao wa Lightning, na vizuizi vya sasa vinaweza kushindwa na suluhisho sahihi.

Hatimaye, siku zijazo za Bitcoin ni za kusisimua na uwezekano wa upeo wa milioni moja katika miaka mitano. Ili kuhakikisha kitaalamu wa tasnia na uumbaji wa mfumo mbadala kwa mfumo wa benki uliopo, ni muhimu kuchangia kwenye mtandao na kuacha kuiamini. 

## Shukrani na endelea kuchimba shimo la sungura
Hongera! 🎉 Umeisha mafunzo ya LN 201 - Utangulizi wa Lightning Network!
Unaweza kujivunia mwenyewe kwa sababu si rahisi. Jua kuwa watu wachache sana wanakwenda kirefu katika shimo la Bitcoin.

Kwanza kabisa, shukrani kubwa kwa Fanis Makalakis kwa kutupatia kozi hii nzuri na ya bure kuhusu upande wa kikabila zaidi wa Lightning. Usisite kumfuata kwenye Twitter, kwenye blogu yake, au kupitia kazi yake kwenye LN market.

Kisha, ikiwa unataka kusaidia mradi huu, usisite kutusaidia kwa kusaidia kupitia Patreon. Michango yako itatumika kuzalisha maudhui kwa kozi mpya za mafunzo na bila shaka, utakuwa wa kwanza kuambiwa habari (ikiwa ni pamoja na ya Fanis inayokuja ambayo inafanyiwa kazi!).

Makala ya Lightning Network inaendelea na mafunzo ya Umbrel na utekelezaji wa kifaa cha Lightning Network. Nadharia imekwisha na sasa ni wakati wa mazoezi na mafunzo ya LN 202!

Busu na tutaonana hivi karibuni!

Rogzy'
