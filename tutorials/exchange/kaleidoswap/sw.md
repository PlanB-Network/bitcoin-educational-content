---
name: KaleidoSwap
description: Mwongozo wa kina wa biashara ya mali ya RGB kwenye Lightning Network ukitumia KaleidoSwap
---

![cover](assets/cover.webp)


KaleidoSwap ni programu ya kisasa ya eneo-kazi ya chanzo huria ambayo huunganisha pengo kati ya Itifaki ya RGB na Lightning Network. Inatumika kama kiolesura kamili cha kudhibiti Nodi za Umeme za RGB, ikiingiliana na Watoa Huduma za Umeme za RGB (LSPs) kupitia vipimo vya LSPS1, na kutekeleza ubadilishaji wa atomiki wa mali za RGB.


Kama suluhisho lisilo la kuhifadhi, KaleidoSwap inawawezesha watumiaji kudumisha udhibiti kamili wa funguo na data zao. Kwa kutumia mfumo wa uthibitishaji wa upande wa mteja wa RGB, inawezesha mikataba mahiri ya kibinafsi na inayoweza kupanuliwa juu ya Bitcoin. Mafunzo haya yanaangazia vipengele vya hali ya juu vya KaleidoSwap, ikikuongoza kupitia ugumu wa usimamizi wa "Rangi" UTXO, ukwasi wa njia kwa mali maalum, na mfumo wa biashara wa mpokeaji, kuhakikisha unaweza kutumia kikamilifu itifaki hii yenye nguvu ya kubadilishana iliyogawanywa.


## Usakinishaji


KaleidoSwap hutoa jozi zilizojengwa tayari kwa mifumo mikubwa ya uendeshaji, lakini kwa watumiaji wa hali ya juu, kujenga kutoka chanzo huhakikisha unaendesha msimbo mpya zaidi na usanidi wako maalum.


### Pakua Pacha


Unaweza kupakua toleo jipya zaidi la mfumo wako wa uendeshaji kutoka [tovuti rasmi](https://kaleidoswap.com/) au [ukurasa wa matoleo ya GitHub](https://github.com/kaleidoswap/desktop-app/releases).


### Mbinu za Ufungaji


1. **Windows**: Pakua kisakinishi cha `.exe` na ukiendeshe.

2. **macOS**: Pakua faili ya `.dmg`, ifungue, na uburute KaleidoSwap hadi kwenye folda yako ya Programu.

3. **Linux**: Pakua faili ya `.AppImage` au `.deb` na usakinishe/uendeshe.



## Chaguo za Usanidi wa Nodi


Unapozindua KaleidoSwap kwa mara ya kwanza, utaonyeshwa **Skrini ya Muunganisho**. Hii ni hatua ya kwanza katika kusanidi mazingira yako.


![Node Selection Screen](assets/en/01.webp)


Lazima uchague jinsi ya kuunganisha kwenye RGB Lightning Network. Chaguo hili linaathiri kiwango chako cha udhibiti na faragha.


### Chaguo la 1: Nodi ya Eneo (Inapendekezwa kwa Utunzaji wa Mwenyewe)


**Kwa udhibiti kamili na faragha**, endesha nodi moja kwa moja kwenye mashine yako, tazama faida zilizo hapa chini:


- Kujitunza**: Una funguo. Hakuna mtu wa tatu anayeweza kusimamisha pesa zako au kudhibiti miamala yako.
- Faragha**: Data yako inabaki kwenye kifaa chako.
- Uhuru**: Hakuna kutegemea watoa huduma wa nje.


Ukichagua **Node ya Eneo**, utaelekezwa kwenye skrini ya usanidi ambapo unaweza kuunda wallet mpya au kurejesha iliyopo.


![Local Node Setup Screen](assets/en/02.webp)


### Chaguo la 2: Nodi ya Mbali


Unganisha kwenye RGB Lightning Node ya mbali (inayojiendesha yenyewe kwenye VPS au mtoa huduma anayepangishwa).


- Faida**: Hakuna matumizi ya rasilimali za ndani, upatikanaji wa saa 24 kwa siku, siku 7 kwa wiki.
- Kubadilishana**: Inahitaji kumwamini mwenyeji au kudhibiti seva ya mbali.


![Remote Node Setup Screen](assets/en/03.webp)


**KaleidoSwap imeundwa ili kuwezesha uangalizi wa kibinafsi.** Tunapendekeza sana kuendesha nodi yako mwenyewe—iwe ndani ya eneo lako (Chaguo la 1) au kwa kujipangia nodi ya mbali—ili kutumia kikamilifu sifa zinazostahimili udhibiti za Bitcoin na RGB.


## Kuunda Wallet


KaleidoSwap husimamia mali za Bitcoin na RGB. Mchakato wa kuunda wallet huanzisha duka la funguo linalolinda fedha zako za on-chain na hali ya chaneli yako ya Lightning.


Hapa kuna mchakato wa kina:

1. Fungua KaleidoSwap na uchague **Node ya Eneo**.

2. Bonyeza **Unda Wallet Mpya**.

3. **Usanidi wa Akaunti**: Ingiza **Jina la Akaunti** na uchague **Mtandao** (k.m., Bitcoin Mainnet, Testnet, Saini).

4. **Usanidi wa Kina** (Si lazima): Ikiwa wewe ni mtumiaji wa umeme, unaweza kusanidi sehemu maalum za mwisho za RPC, URL za Kielezo, au mipangilio ya Proksi chini ya "Mipangilio ya Kina".

5. Bonyeza **Endelea**.

6. **Nenosiri**: Weka nenosiri thabiti ili kusimba faili yako ya wallet kwa njia fiche ndani ya eneo lako.

7. **Kifungu cha Urejeshaji**: Andika kifungu chako cha seed na ukihifadhi kwa usalama.


    - Muhimu**: Kifungu hiki kinahitajika ili kurejesha fedha zako za on-chain na utambulisho wa nodi.
    - Onyo**: **Hali za chaneli za umeme haziwezi kurejeshwa kikamilifu kutoka kwa seed pekee**. Lazima pia uendelee na Hifadhi Nakala za Chaneli Tuli (SCB) ili kurejesha pesa zilizofungwa kwenye chaneli.


![Wallet Creation Screen](assets/en/04.webp)



## Muhtasari wa Dashibodi


Mara tu wallet yako itakapoundwa, utaelekezwa kwenye **Dashibodi** kuu.


![KaleidoSwap Dashboard](assets/en/05.webp)


_Kumbuka: Picha ya skrini hapo juu inaonyesha wallet ambayo tayari imefadhiliwa na ina njia zinazotumika. wallet mpya itaonyesha salio sifuri na hakuna njia zinazotumika hadi utakapoifadhili._


## Kufadhili Wallet yako


Ili kufanya kazi na mali za RGB, unahitaji kufadhili wallet yako. KaleidoSwap inasaidia kuweka mali za Bitcoin na RGB kupitia miamala ya on-chain au Lightning Network.


### Kuweka Bitcoin


1. Bonyeza **Weka** kwenye menyu ya Vitendo vya Haraka.

2. Chagua **BTC** kutoka kwenye orodha ya mali.


![Select BTC Asset](assets/en/06.webp)


3. Chagua njia yako ya kuweka pesa: **Inapowekwa kwenye mnyororo** au **Umeme**.


![BTC Deposit Options](assets/en/07.webp)



- Kwenye mnyororo**: Changanua msimbo wa QR au nakili anwani ili kutuma Bitcoin kutoka kwa wallet nyingine.
- Umeme**: Tengeneza ankara ya kiasi unachotaka.


![BTC On-chain Deposit](assets/en/08.webp)


### Kuweka Mali za RGB na UTXO za Rangi


Ili kupokea mali za RGB (kama vile USDT), unahitaji UTXO maalum zinazopatikana ili "zipakwe rangi" (zipewe mali).


1. Bofya **Amana** na uchague kipengee cha RGB (k.m., USDT). **Muhimu**: Ikiwa hii ni mara ya kwanza kipengee chako kupokea kipengee hiki mahususi, **acha sehemu ya Kitambulisho cha Kipengee tupu**. Kuingiza Kitambulisho cha kipengee kisichojulikana kutasababisha kipengee hicho kurudisha hitilafu kwani hakijakitambua bado.

2. Chagua **Imo kwenye mnyororo** au **Umeme**.


![USDT Deposit Options](assets/en/09.webp)


#### Njia za Kupokea Zilizopo Kwenye Mnyororo: Shahidi dhidi ya Kupofushwa


Unapopokea vipengee vya RGB on-chain, una njia mbili za faragha:



- Kupokea Kipofu (Inapendekezwa kwa Faragha)**: Unampa mtumaji "blinded" UTXO. Unamwomba mtumaji atume mali kwa UTXO iliyopo ambayo unamiliki, lakini unaficha kitambulisho halisi cha UTXO. Hii inatoa faragha bora.
- Shahidi Anapokea**: Unatoa anwani ya kawaida ya Bitcoin. Unamwomba mtumaji akutengenezee UTXO *mpya* kwa kutuma mali kwenye anwani hiyo. Hii inaruhusu mali za RGB kuunganishwa moja kwa moja na UTXO mpya iliyoundwa na muamala.


#### Amana ya Umeme


Kwa amana za umeme, tumia ankara ya generate tu. Mali ya RGB itakufikia kupitia njia zako zilizo wazi.


![USDT Lightning Invoice](assets/en/10.webp)



## Kufungua Njia zenye Mali za RGB


Ili kuhamisha mali za RGB juu ya Lightning Network, unahitaji njia yenye ukwasi wa kutosha na mgao wa mali. Njia rahisi zaidi ya kuanza ni **Kununua Njia** kutoka kwa LSP (Mtoa Huduma wa Umeme).


### Kununua Kituo kutoka Kaleido LSP


1. Nenda kwenye kichupo cha **Chaneli**. Utaona chaguo za "Fungua Chaneli" (kwa mkono) au "Nunua Chaneli" (LSP).

2. Bonyeza **Nunua Kituo**.


![Channels Dashboard](assets/en/11.webp)


3. **Unganisha kwenye LSP**: Programu itaunganishwa kwenye Kaleido LSP chaguo-msingi. Mtoa huduma huyu hutoa ukwasi unaoingia na anaunga mkono uelekezaji wa mali wa RGB.


![Connect to LSP](assets/en/12.webp)


4. **Sanidi Kituo**:


    - Uwezo**: Chagua jumla ya uwezo wa Bitcoin kwa chaneli.
    - Mgawanyo wa RGB**: Chagua mali ya RGB (k.m., USDT) unayotaka kuweza kupokea au kutuma. LSP itahakikisha kuwa kituo kimeundwa ili kuunga mkono mali hii.


![Configure Channel](assets/en/13.webp)



    - Mgao wa RGB**: Chagua kipengee cha RGB (k.m., USDT) unachotaka kipokee au kutuma. LSP itahakikisha kuwa kituo kimeundwa ili kuunga mkono kipengee hiki.


![RGB Allocation](assets/en/14.webp)


5. **Malipo**: Lazima ulipe ada kwa LSP kwa kufungua chaneli na kutoa ukwasi. Unaweza kulipa kwa kutumia **Umeme** au **On-chain** Bitcoin. Malipo yanaweza kufanywa kutoka KaleidoSwap wallet yako ya ndani au wallet ya nje.


![Complete Payment](assets/en/15.webp)


6. Mara tu malipo yatakapothibitishwa, LSP itaanzisha muamala wa kufungua chaneli. Utaona skrini ya **Agizo Lililokamilika**.


![Order Completed](assets/en/16.webp)


7. Baada ya uthibitisho kwenye blockchain, chaneli yako itakuwa hai na tayari kwa uhamisho wa RGB.



## Biashara: Mfano wa Mtengenezaji-Mwenye Kuchukua


Injini ya biashara ya KaleidoSwap inafanya kazi kwenye modeli ya **Taker-Maker**. Unaweza kubadilisha mali mwenyewe na rika au kutumia Market Maker (LSP).


### Kubadilishana na Mtengenezaji wa Soko (LSP)


Hii ndiyo njia ya kawaida ya kufanya biashara. Unafanya kazi kama **Mpokeaji**, ukitekeleza maagizo dhidi ya ukwasi unaopatikana unaotolewa na LSP (**Mtengenezaji**).


1. Nenda kwenye kichupo cha **Biashara** na uchague **Soko la Kutengeneza**.

2. **Ingiza Kiasi**: Ingiza kiasi cha Bitcoin unachotaka kutuma (au mali unayotaka kupokea). Kiolesura kitaonyesha kiwango cha ubadilishaji na ada zinazokadiriwa.


![Market Maker Swap](assets/en/17.webp)


3. **Thibitisha Kubadilishana**: Kagua maelezo, ikiwa ni pamoja na kiwango cha ubadilishaji na kiasi halisi utakachopokea. Bonyeza **Thibitisha Kubadilishana**.


![Confirm Swap](assets/en/18.webp)


4. **Uchakataji**: Ubadilishaji unatekelezwa kwa atomiki kwenye Lightning Network. Utaona skrini ya hali inayoonyesha kuwa ubadilishaji unasubiri.


![Swap Pending](assets/en/19.webp)


5. **Mafanikio**: Mara tu HTLC zitakapokamilika, ubadilishaji umekamilika, na mali ziko kwenye kituo chako.


![Swap Success](assets/en/20.webp)



## Msanidi Programu API


Kwa watengenezaji wanaojenga juu ya KaleidoSwap, programu hii inaonyesha API inayounga mkono:



- RGB LSPS1**: Kwa huduma za ukwasi otomatiki.
- Badilisha API**: Kwa biashara ya kiprogramu na utengenezaji wa soko.
- WebSocket**: Kwa usajili wa data ya soko kwa wakati halisi.


Rejelea [Nyaraka za API](https://docs.kaleidoswap.com/api/introduction) kwa vidokezo kamili na vipimo.


## Hitimisho


KaleidoSwap inakuwezesha kutumia faragha na uwezo wa kupanuka wa mali za RGB kwenye Lightning Network. Kwa kuelewa UTXO za Rangi na ugawaji wa mali za njia, unaweza kutumia kikamilifu itifaki hii yenye nguvu ya ubadilishanaji wa rasilimali.