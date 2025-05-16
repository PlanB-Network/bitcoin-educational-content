---
name: Zana za Takwimu za Whirlpool - Anonsets
description: Kuelewa dhana ya anoset na jinsi ya kuihesabu na WST
---
![cover](assets/cover.webp)


***ONYO:** Kufuatia kukamatwa kwa waanzilishi wa Samourai Wallet na kunaswa kwa seva zao mnamo Aprili 24, Zana ya Takwimu ya Whirlpool haipatikani tena kupakuliwa, kwa kuwa ilipangishwa kwenye Gitlab ya Samourai. Hata kama ulikuwa umepakua zana hii kwenye mashine yako hapo awali, au ilisakinishwa kwenye nodi yako ya RoninDojo, WST haitafanya kazi kwa wakati huu. Ilitegemea data iliyotolewa na OXT.me kwa uendeshaji wake, na tovuti hii haipatikani tena. Kwa sasa, WST sio muhimu sana kwani itifaki ya Whirlpool haifanyi kazi. Walakini, bado inawezekana kwamba programu hizi zinaweza kurejeshwa katika wiki zijazo. Zaidi ya hayo, sehemu ya kinadharia ya kifungu hiki inabaki kuwa muhimu kwa kuelewa kanuni na malengo ya coinjoins kwa ujumla (sio tu Whirlpool), na pia kuelewa ufanisi wa mfano wa Whirlpool. Unaweza pia kujifunza jinsi ya kukadiria faragha inayotolewa na mizunguko ya CoinJoin.*


_Tunafuatilia kwa karibu maendeleo ya kesi hii pamoja na maendeleo kuhusu zana zinazohusiana. Uwe na uhakika kwamba tutasasisha mafunzo haya kadiri habari mpya zinavyopatikana._


_Mafunzo haya yametolewa kwa madhumuni ya elimu na habari pekee. Hatuidhinishi au kuhimiza matumizi ya zana hizi kwa madhumuni ya uhalifu. Ni wajibu wa kila mtumiaji kutii sheria katika eneo la mamlaka yake._


---

> *Vunja kiunga ambacho sarafu zako huacha nyuma*

Katika somo hili, tutajifunza dhana ya anonsets, viashiria vinavyotuwezesha kukadiria ubora wa mchakato wa CoinJoin kwenye Whirlpool. Tutashughulikia njia ya hesabu na tafsiri ya viashiria hivi. Kufuatia sehemu ya kinadharia, tutaendelea kufanya mazoezi kwa kujifunza kukokotoa anonsets za shughuli mahususi kwa kutumia zana ya Python *Whirlpool Stats Tools* (WST).


## CoinJoin kwenye Bitcoin ni nini?

**CoinJoin ni mbinu inayovunja ufuatiliaji wa bitcoins kwenye Blockchain**. Inategemea shughuli ya ushirikiano na muundo maalum wa jina moja: shughuli ya CoinJoin.


Shughuli za CoinJoin huongeza faragha ya watumiaji wa Bitcoin kwa kutatiza uchanganuzi wa msururu kwa waangalizi wa nje. Muundo wao unaruhusu kuunganisha sarafu nyingi kutoka kwa watumiaji tofauti katika shughuli moja, hivyo basi kuficha njia na kufanya iwe vigumu kubainisha viungo kati ya anwani za kuingiza na kutoa.


Kanuni ya CoinJoin inategemea mbinu ya ushirikiano: watumiaji kadhaa ambao wangependa kuchanganya bitcoins zao huweka kiasi sawa kama pembejeo za muamala sawa. Kiasi hiki kisha kusambazwa upya katika matokeo ya thamani sawa. Mwishoni mwa muamala, inakuwa vigumu kuhusisha pato mahususi na mtumiaji fulani. Hakuna kiungo cha moja kwa moja kilichopo kati ya pembejeo na matokeo, na hivyo kuvunja uhusiano kati ya watumiaji na UTXO yao, pamoja na historia ya kila sarafu.


![coinjoin](assets/notext/1.webp)


Mfano wa shughuli ya CoinJoin:

[323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://GW -15.space/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)


Ili kutekeleza CoinJoin huku ukihakikisha kwamba kila mtumiaji anaendelea kudhibiti fedha zake wakati wote, mchakato huanza na ujenzi wa shughuli na mratibu, ambaye kisha anaipeleka kwa kila mshiriki. Kila mtumiaji basi hutia saini muamala baada ya kuthibitisha kuwa inamfaa. Saini zote zilizokusanywa hatimaye zimeunganishwa kwenye shughuli. Iwapo jaribio la kubadilisha fedha litafanywa na mtumiaji au mratibu, kwa kurekebisha matokeo ya muamala wa CoinJoin, sahihi zitathibitisha kuwa si sahihi, na hivyo kusababisha kukataliwa kwa shughuli hiyo na nodi.


Kuna utekelezaji kadhaa wa CoinJoin, kama vile Whirlpool, JoinMarket, au Wabisabi, kila moja ikilenga kudhibiti uratibu kati ya washiriki na kuongeza ufanisi wa miamala ya CoinJoin.

Katika somo hili, tutazingatia utekelezaji ninaopenda zaidi: Whirlpool, ambayo inapatikana kwenye Samourai Wallet na Sparrow Wallet. Kwa maoni yangu, ni utekelezaji bora zaidi kwa coinjoins kwenye Bitcoin.


## Je! ni matumizi gani ya CoinJoin kwenye Bitcoin?


Umuhimu wa CoinJoin upo katika uwezo wake wa kutokeza ukanushaji unaokubalika, kwa kuzamisha sarafu yako ndani ya kundi la sarafu zisizoweza kutofautishwa. Lengo la hatua hii ni kuvunja viungo vya ufuatiliaji, kutoka zamani hadi sasa na kutoka sasa hadi siku za nyuma.


Kwa maneno mengine, mchambuzi anayejua shughuli yako ya awali wakati wa kuingia kwa mizunguko ya CoinJoin hapaswi kuwa na uwezo wa kutambua kwa uhakika UTXO yako wakati wa kuondoka kwa mizunguko ya remix (uchambuzi kutoka kwa kuingia kwa mzunguko hadi kuondoka kwa mzunguko).


![coinjoin](assets/en/2.webp)


Kinyume chake, mchambuzi anayejua UTXO yako wakati wa kuondoka kwa mizunguko ya CoinJoin anapaswa kushindwa kubainisha shughuli ya awali wakati wa kuingiza mizunguko (uchambuzi kutoka kwa njia ya kutoka kwa mzunguko hadi kuingia kwa mzunguko).


![coinjoin](assets/en/3.webp)


Ili kutathmini ugumu wa mchambuzi kuunganisha yaliyopita na ya sasa na kinyume chake, ni muhimu kubainisha ukubwa wa vikundi ambamo sarafu yako imefichwa. Hatua hii inatuambia idadi ya uchanganuzi kuwa na uwezekano sawa. Kwa hivyo, ikiwa uchanganuzi sahihi umezama kati ya uchanganuzi mwingine 3 wa uwezekano sawa, kiwango chako cha ufichaji ni cha chini sana. Kwa upande mwingine, ikiwa uchanganuzi sahihi uko ndani ya seti ya uchanganuzi 20,000 zote zinazowezekana kwa usawa, sarafu yako imefichwa vizuri sana.


Na kwa usahihi, saizi ya vikundi hivi inawakilisha viashiria vinavyoitwa "anonsets".


## Kuelewa anonsets

Anonsets hutumika kama viashirio vya kutathmini kiwango cha faragha cha UTXO fulani. Hasa zaidi, wanapima idadi ya UTXO zisizoweza kutofautishwa ndani ya seti inayojumuisha sarafu iliyosomwa. Mahitaji ya seti ya UTXO yenye homogeneous inamaanisha kuwa anonsets kawaida huhesabiwa kwa mizunguko ya CoinJoin. Utumiaji wa viashiria hivi ni muhimu sana kwa miunganisho ya Whirlpool kwa sababu ya usawa wao.


Anonsets huruhusu, inapofaa, kuhukumu ubora wa coinjoins. Ukubwa mkubwa wa anoset unamaanisha kiwango cha kuongezeka kwa kutokujulikana, kwani inakuwa vigumu kutofautisha UTXO maalum ndani ya kuweka.


Kuna aina mbili za anonsets:


- Seti inayotarajiwa ya kutokujulikana;**
- Mtazamo wa kutokujulikana umewekwa.**

Kiashiria cha kwanza kinaonyesha ukubwa wa kikundi kati ya ambayo UTXO iliyojifunza imefichwa mwishoni mwa mzunguko, kujua UTXO kwenye kuingia, yaani, idadi ya sarafu zisizojulikana zilizopo ndani ya kikundi hiki. Kiashiria hiki kinaruhusu kupima upinzani wa usiri wa sarafu dhidi ya uchambuzi kutoka zamani hadi sasa (kuingia kwa kuondoka). Kwa Kiingereza, jina la kiashirio hiki ni "*forward anonse*", au "*vipimo vya kuangalia mbele*".

![coinjoin](assets/en/4.webp)


Kipimo hiki kinakadiria kiwango ambacho UTXO yako inalindwa dhidi ya majaribio ya kuunda upya historia yake kutoka mahali pake pa kuingilia hadi mahali pake pa kutokea katika mchakato wa CoinJoin.


Kwa mfano, ikiwa muamala wako ulishiriki katika mzunguko wake wa kwanza wa CoinJoin na mizunguko mingine miwili ya ukoo ikakamilika, uondoaji unaotarajiwa wa sarafu yako utakuwa `13`:


![coinjoin](assets/en/5.webp)


Kiashiria cha pili kinaonyesha idadi ya vyanzo vinavyowezekana kwa sarafu fulani, kujua UTXO mwishoni mwa mzunguko. Kiashiria hiki kinapima upinzani wa usiri wa sarafu dhidi ya uchambuzi kutoka sasa hadi uliopita (kutoka hadi kuingia), yaani, jinsi ilivyo vigumu kwa mchambuzi kufuatilia asili ya sarafu yako, kabla ya mizunguko ya CoinJoin. Kwa Kiingereza, jina la kiashirio hiki ni "*backward anonse*", au "*metrics zinazoangalia nyuma*".


![coinjoin](assets/en/6.webp)


Kwa kujua UTXO yako wakati wa kuondoka kwa mizunguko, uwekaji upyaji wa mipangilio ya nyuma huamua idadi ya miamala ya Tx0 inayoweza kujumuisha kuingia kwako kwenye mizunguko ya CoinJoin. Katika mchoro hapa chini, hii inalingana na jumla ya Bubbles zote za machungwa.


![coinjoin](assets/en/7.webp)


## Kukokotoa utatuzi kwa kutumia Zana za Takwimu za Whirlpool (WST)

Ili kukokotoa viashirio hivi kwenye sarafu zako mwenyewe ambazo zimepitia mizunguko ya CoinJoin, unaweza kutumia zana iliyotengenezwa mahususi na Samourai Wallet: *Whirlpool Stats Tools*.


Ikiwa una RoninDojo, WST imesakinishwa awali kwenye nodi yako. Kwa hiyo unaweza kuruka hatua za usakinishaji na kufuata moja kwa moja hatua za utumiaji. Kwa wale ambao hawana node ya RoninDojo, hebu tuone jinsi ya kuendelea na ufungaji wa chombo hiki kwenye kompyuta.


Utahitaji: Kivinjari cha Tor (au Tor), Python 3.4.4 au zaidi, git, na bomba. Fungua terminal. Ili kuangalia uwepo na toleo la programu hizi kwenye mfumo wako, ingiza amri zifuatazo:

```plaintext
python --version
git --version
pip --version
```


Ikihitajika, unaweza kuzipakua kutoka kwa tovuti zao husika:


- https://www.python.org/downloads/ (bomba inakuja moja kwa moja na Python tangu toleo la 3.4);
- https://www.torproject.org/download/;
- https://git-scm.com/downloads.

Mara programu hizi zote zikisanikishwa, kutoka kwa terminal, tengeneza hazina ya WST:

```plaintext
git clone https://code.samourai.io/whirlpool/whirlpool_stats.git
```


![WST](assets/notext/8.webp)


Nenda kwenye saraka ya WST:

```plaintext
cd whirlpool_stats
```


Sakinisha utegemezi:

```plaintext
pip3 install -r ./requirements.txt
```


![WST](assets/notext/9.webp)


Unaweza pia kuzisakinisha mwenyewe (si lazima):

```plaintext
pip install PySocks
pip install requests[socks]
pip install plotly
pip install datasketch
pip install numpy
pip install python-bitcoinrpc
```


Nenda kwenye folda ya `/whirlpool_stats`:

```plaintext
cd whirlpool_stats
```


Anzisha WST:

```plaintext
python3 wst.py
```


![WST](assets/notext/10.webp)


Zindua Tor au Kivinjari cha Tor nyuma.


**-> Kwa watumiaji wa RoninDojo, unaweza kuendelea na mafunzo moja kwa moja hapa.**


Weka proksi kwa Tor (RoninDojo),

```plaintext
socks5 127.0.0.1:9050
```


au kwa Kivinjari cha Tor kulingana na kile unachotumia:

```plaintext
socks5 127.0.0.1:9150
```


Udanganyifu huu utakuruhusu kupakua data kwenye OXT kupitia Tor, ili usivujishe maelezo kuhusu miamala yako. Ikiwa wewe ni novice na hatua hii inaonekana ngumu, ujue kwamba inahusisha tu kuelekeza trafiki yako ya mtandao kupitia Tor. Njia rahisi zaidi ni kuzindua Kivinjari cha Tor chinichini kwenye kompyuta yako, kisha utekeleze amri ya pili pekee ya kuunganisha kupitia kivinjari hiki (`soksi5 127.0.0.1:9150`).


![WST](assets/notext/11.webp)


Ifuatayo, nenda kwenye saraka ya kufanya kazi ambayo unakusudia kupakua data ya WST kwa kutumia amri ya `workdir`. Folda hii itatumika kuhifadhi data ya muamala ambayo utapata kutoka kwa OXT katika mfumo wa faili za `.csv`. Taarifa hii ni muhimu kwa kukokotoa viashirio unavyotafuta kupata. Uko huru kuchagua eneo la saraka hii. Inaweza kuwa busara kuunda folda haswa kwa data ya WST. Kwa mfano, wacha tuchague folda ya upakuaji. Ikiwa unatumia RoninDojo, hatua hii sio lazima:

```plaintext
workdir path/to/your/directory
```


Uhakika wa amri unapaswa kuwa umebadilika ili kuonyesha saraka yako ya kufanya kazi.


![WST](assets/notext/12.webp)


Kisha pakua data kutoka kwa bwawa iliyo na muamala wako. Kwa mfano, ikiwa niko kwenye dimbwi la `100,000 Sats`, amri ni:

```plaintext
download 0001
```


![WST](assets/notext/13.webp)


Nambari za madhehebu kwenye WST ni kama ifuatavyo:


- Dimbwi la bitcoins 0.5: `05`
- Dimbwi la bitcoins 0.05: `005`
- Dimbwi la bitcoins 0.01: `001`
- Dimbwi la bitcoins 0.001: `0001`

Mara baada ya data kupakuliwa, pakia. Kwa mfano, ikiwa niko kwenye dimbwi la `100,000 Sats`, amri ni:

```plaintext
load 0001
```


Hatua hii inachukua dakika chache kulingana na kompyuta yako. Sasa ni wakati mzuri wa kujitengenezea kahawa! :)


![WST](assets/notext/14.webp)


Baada ya kupakia data, charaza amri ya `alama` ikifuatiwa na txid yako (kitambulisho cha muamala) ili kupata majibu yake:

```plaintext
score TXID
```


**Tahadhari:** chaguo la txid la kutumia hutofautiana kulingana na urejeshi unaotaka kukokotoa. Ili kutathmini uwezekano wa kutoweka kwa sarafu, ni muhimu kuingiza, kupitia amri ya `alama`, txid inayolingana na CoinJoin yake ya kwanza, ambayo ni mchanganyiko wa awali unaofanywa na UTXO hii. Kwa upande mwingine, ili kuamua anoset ya nyuma, lazima uweke txid ya CoinJoin ya mwisho iliyofanywa. Kwa muhtasari, anoset tarajiwa huhesabiwa kutoka kwa txid ya mchanganyiko wa kwanza, wakati anoset ya kurudi nyuma inakokotolewa kutoka kwa txid ya mchanganyiko wa mwisho.


Kisha WST huonyesha alama za rejea (*Vipimo vinavyoonekana nyuma*) na alama zinazotarajiwa (*Vipimo vya kuangalia Mbele*). Kwa mfano, nilichukua txid ya sarafu isiyo ya kawaida kwenye Whirlpool ambayo si yangu.


![WST](assets/notext/15.webp)


Muamala unaohusika: [7fe6081fa4f4382be629fb2ef59029d058a22b6fd59cb31d1511fe9e0e7f32be](https://GW -53.space/tx/7fe6081fa4f4382be629fb2ef59029d058a22b6fd59cb31d1511fe9e0e7f32be)


Ikiwa tutazingatia muamala huu kama CoinJoin ya kwanza iliyotekelezwa kwa sarafu inayohusika, basi itanufaika kutokana na uwezekano wa kutoweka kwa `86,871`. Hii inamaanisha kuwa imefichwa kati ya sarafu `86,871` zisizoweza kutofautishwa. Kwa mtazamaji wa nje ambaye anajua sarafu hii mwanzoni mwa mizunguko ya CoinJoin na kujaribu kufuatilia matokeo yake, watakabiliwa na `86,871` zinazowezekana za UTXO, kila moja ikiwa na uwezekano sawa wa kuwa sarafu inayotafutwa.


Iwapo tutazingatia muamala huu kama CoinJoin ya mwisho ya sarafu, basi ina urejeshi usiofaa wa `42,185`. Hii inamaanisha kuwa kuna `42,185` vyanzo vinavyowezekana vya UTXO hii. Ikiwa mwangalizi wa nje atatambua sarafu hii mwishoni mwa mizunguko na kutafuta kufuatilia asili yake, atakabiliwa na `42,185` vyanzo vinavyowezekana, vyote vikiwa na uwezekano sawa wa kuwa asili inayotafutwa.

Kando na alama za kukosekana kwa mpangilio, WST pia hukupa kiwango cha uenezaji wa pato lako ndani ya hifadhi kulingana na kutoweka. Kiashiria hiki kingine hukuruhusu kutathmini uwezekano wa uboreshaji wa kipande chako. Kiwango hiki ni muhimu hasa kwa anayetarajiwa kutoweka. Hakika, ikiwa kipande chako kina kiwango cha kuenea kwa 15%, inamaanisha inaweza kuchanganyikiwa na 15% ya vipande kwenye bwawa. Hiyo ni nzuri, lakini bado una ukingo mkubwa sana wa kuboreshwa kwa kuendelea kuiga. Kwa upande mwingine, ikiwa kipande chako kina kiwango cha kueneza cha 95%, basi unakaribia mipaka ya bwawa. Unaweza kuendelea kuchanganya, lakini anonse yako haitaongezeka sana.


Ni muhimu kutambua kwamba anonsets zilizohesabiwa na WST sio sahihi kabisa. Kwa kuzingatia idadi kubwa ya data ya kuchakatwa, WST hutumia algoriti ya *HyperLogLogPlusPlus* ili kupunguza kwa kiasi kikubwa mzigo unaohusishwa na uchakataji wa data ya ndani na kumbukumbu muhimu. Hii ni algoriti inayoruhusu kukadiria idadi ya thamani tofauti katika seti kubwa za data huku ikidumisha usahihi wa juu wa matokeo. Kwa hivyo, alama zinazotolewa ni nzuri za kutosha kutumika katika uchanganuzi wako, kwani ni makadirio ya karibu sana na ukweli, lakini hazipaswi kufasiriwa kama maadili kamili kwa kitengo.


Kwa kumalizia, kumbuka kwamba sio lazima kuhesabu kwa utaratibu anonsets kwa kila kipande chako kwa coinjoins. Muundo wenyewe wa Whirlpool tayari hutoa dhamana. Hakika, anonseti ya nyuma mara chache huwa ya wasiwasi. Kutoka kwa mchanganyiko wako wa awali, unapata alama ya juu zaidi ya retrospective kutokana na urithi wa michanganyiko ya awali tangu Genesis CoinJoin. Kuhusu hali ya kutokujali inayotarajiwa, inatosha kuweka kipande chako kwenye akaunti ya baada ya mchanganyiko kwa kipindi kirefu cha kutosha.


Hii ndiyo sababu ninaona matumizi ya Whirlpool kuwa yanafaa hasa katika mkakati wa *HODL -> Mchanganyiko -> Tumia -> Badilisha* mkakati. Kwa maoni yangu, mbinu ya kimantiki zaidi ni kuweka akiba kubwa ya Bitcoin ya mtu kwenye Cold Wallet, huku ukiendelea kudumisha idadi fulani ya vipande kwa sanjari kwenye Samourai ili kufidia gharama za kila siku. Mara tu bitcoins kutoka kwa sarafu zinatumiwa, hubadilishwa na mpya, ili kurudi kwenye kizingiti kilichoelezwa cha vipande vilivyochanganywa. Njia hii inaruhusu mtu kujiondoa kutoka kwa wasiwasi wa anonsets wetu wa UTXO, huku akifanya wakati muhimu kwa ufanisi wa coinjoins kuwa ngumu sana.


**Nyenzo za Nje:**



- [Podcast katika Uchambuzi wa on chain ya Kifaransa](https://fountain.fm/episode/6nNoQEUHBCQR8hAXAkEx)
- [Makala ya Wikipedia kuhusu HyperLogLog](https://en.wikipedia.org/wiki/HyperLogLog)
- Hazina ya Samourai ya Takwimu za Whirlpool
- Tovuti ya Whirlpool na Samourai
- [Makala ya wastani katika Kiingereza kuhusu faragha na Bitcoin ya Samourai](https://medium.com/oxt-research/understanding-Bitcoin-privacy-with-oxt-part-1-4-8177a40a5923)
- [Makala ya wastani katika Kiingereza kuhusu dhana ya kutokujulikana iliyowekwa na Samourai](https://medium.com/samourai-Wallet/diving-head-first-into-Whirlpool-anonymity-sets-4156a54b0bc7)