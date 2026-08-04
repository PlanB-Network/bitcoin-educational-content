---
name: Slipstream
description: Kutuma muamala uliotiwa saini moja kwa moja kwa mchimbaji kupitia Slipstream, bila kuutangaza kwenye mtandao wa Bitcoin
---

![jalada](assets/cover.webp)

Kwa kawaida, unapoutia saini muamala, unatangazwa kiotomatiki kwa kila nodi ya Bitcoin kwenye mtandao. Kisha unasubiri kuchimbwa.

Hata hivyo, kwa muda wote ambao haujajumuishwa kwenye kitalu, mshambuliaji aliyepata ufunguo wako wa faragha anaweza kuubadilisha na kuiba fedha. Hii ndiyo hali ya kawaida ikiwa unatumia ColdCard hardware wallet.

Zana ya Slipstream kutoka kampuni ya uchimbaji MARA hukuruhusu kuepuka kutangaza muamala kwenye mtandao: unatumwa moja kwa moja (na pekee) kwa mchimbaji, ambaye huuweka faragha na huepuka kuufichua kwenye mtandao. Huenda muamala ukachukua muda mrefu zaidi kuchimbwa, lakini utalindwa dhidi ya shambulio la kubadilisha muamala.

Hapa chini, tunatoa mafunzo yanayowaruhusu watumiaji wa [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04), pamoja na watumiaji wa wallet ya [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d), kutumia zana ya Slipstream ya mchimbaji MARA kupitia ukurasa wa [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

⚠️ **Onyo**: zana hii imekusudiwa tu kwa wasifu fulani, hasa wallet za Liana, wallet za miniscript na aina fulani za multisig. Wizardsardine **inashauri waziwazi dhidi ya** kuitumia kwa wallet ambazo fedha zake tayari ziko katika hatari kubwa ya kuibwa, kwa mfano zile ambazo maneno yake ya kurejesha yalitengenezwa kwenye kifaa cha ColdCard kilichoathiriwa na udhaifu wa generator ya nambari nasibu. Katika hali hiyo, mbio dhidi ya mshambuliaji ni suala la sekunde, na muamala uliotumwa kwa mchimbaji mmoja huchukua muda mrefu zaidi kuthibitishwa kuliko ule uliotangazwa kawaida. Ikiwa hili linakuhusu, soma kwanza mafunzo yetu maalum:

https://planb.academy/tutorials/wallet/hardware/coldcard-seed-vulnerability-1348b153-89db-429c-80af-b5d3d8506b9a

## Kwa watumiaji wa Liana

Liana inadumishwa na Wizardsardine, mchapishaji wa ukurasa wa [outofband.wizardsardine.com](https://outofband.wizardsardine.com/), kwa hiyo njia ni ya moja kwa moja: unahamisha tu faili ya PSBT iliyotiwa saini badala ya kuitangaza.

*Sharti la awali: uwe na fedha kwenye wallet yako ya Liana.*

### Hatua ya 1: Unda muamala wako kwa Liana

Kama kawaida, jenga muamala wako kwa kuongeza anwani ya lengwa, maelezo, na kiasi (hapa, kiwango cha juu kinachopatikana kwenye wallet).

Ili kuweka fee rate:

- chagua coins unazotaka kutumia kwa kubofya kisanduku kidogo chini kushoto, chini ya "Uteuzi wa coins";
- kisha weka fee rate. Kumbuka kuweka ada juu zaidi kuliko kiwango kilichopendekezwa, kama ilivyoelezwa kwenye ukurasa huu: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Hatimaye, bofya "Ifuatayo".

![Kujenga muamala katika Liana](assets/fr/01.webp)

### Hatua ya 2: Kagua maelezo ya muamala wako

Kabla ya kubofya "Tia saini", kagua maelezo ya muamala wako; hasa:

- kiasi kinachotumwa;
- idadi ya satoshis zilizotengwa kwa ada za muamala;
- lakini zaidi ya yote, anwani unayotumia kutuma fedha (kumbuka kukagua herufi 5/6 za kwanza, 5/6 za mwisho, na herufi 5/6 katikati ya anwani ili kuepuka mashambulio ya "address poisoning").

![Kukagua maelezo ya muamala](assets/fr/02.webp)

### Hatua ya 3: Chagua wallet za kutia saini

Kisha, chagua software na/au hardware wallets unazohitaji kutumia kutia saini muamala wako. Ukumbusho mfupi: katika wallet ya multisig ya 2-of-2, unahitaji saini 2 kati ya 2.

### Hatua ya 4: Hamisha faili ya PSBT ya muamala wako

Muamala wa Bitcoin sasa umetiwa saini na funguo zinazofaa. Usibofye "Tangaza", vinginevyo utasambazwa kwa mtandao wote na, ikiwa unatumia ColdCard hardware wallet, muamala wako utawekwa wazi hadharani na fedha zako zitakuwa hatarini.

Sasa unaweza kubofya "Hamisha", kisha uhifadhi faili ya PSBT ndani ya kompyuta yako.

![Kuhamisha faili ya PSBT kutoka Liana](assets/fr/03.webp)

### Hatua ya 5: Tuma muamala kwa mchimbaji kupitia outofband.wizardsardine.com

Sasa kwa hatua za mwisho. Ili kutuma muamala kwa mchimbaji, unachopaswa kufanya ni kuchukua faili ya PSBT na kuivuta na kuidondosha katika eneo lililotengwa.

![Kudondosha faili ya PSBT kwenye outofband.wizardsardine.com](assets/fr/04.webp)

Kisha muamala unaonyeshwa kama ilivyo hapa chini.

![Muamala kwenye foleni](assets/fr/05.webp)

### Hatua ya 6: Tuma muamala kupitia Slipstream

Hatimaye, unachopaswa kufanya ni kubofya "Tuma" ili muamala utumwe kwa MARA kupitia Slipstream.

![Kutuma muamala kupitia Slipstream](assets/fr/06.webp)

Ndani ya sekunde chache, muamala kisha hubadilika kutoka "Inatuma" hadi "Imekubaliwa":

![Muamala umekubaliwa na Slipstream](assets/fr/07.webp)

Kilichobaki ni kunakili kitambulisho cha muamala (TXID), kisha kukibandika kwenye [mempool.space](https://mempool.space/) ili kutazama ukichimbwa:

![Kutafuta TXID kwenye mempool.space](assets/fr/08.webp)

Tafadhali kumbuka: muamala utaonekana kama "Muamala haukupatikana" hadi mchimbaji, MARA, achimbe kitalu na kujumuisha muamala wako humo. Hili linaweza kuchukua makumi kadhaa ya dakika, au hata saa, kwa sababu MARA inashikilia tu takriban 4.5% ya hash rate ya mtandao wa Bitcoin. Kufikia 4 Agosti 2026, hii inalingana takriban na kitalu kimoja kuchimbwa kila saa 3 na dakika 45.

## Kwa watumiaji wa wallet nyingine

Ikiwa hutumii [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04) lakini bado unataka kutumia zana hii, hapa kuna mafunzo yanayotumia wallet ya multisig ya 2-of-2. Ili kufanya hivyo, tutatumia software wallet ya [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d).

*Sharti la awali: uwe na fedha kwenye wallet yako ya Sparrow.*

### Hatua ya 1: Unda muamala wako

Kwa [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d), unda muamala kwenye wallet yako ya multisig. Kumbuka kuweka ada juu zaidi kuliko kiwango kilichopendekezwa, kama ilivyoelezwa kwenye ukurasa huu: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Baada ya kuundwa, bofya "Unda Muamala".

![Kuunda muamala katika Sparrow](assets/fr/09.webp)

### Hatua ya 2: Kamilisha muamala wako

Ili kukamilisha muamala wako, sasa unahitaji kuutia saini. Ili kufanya hivyo, bofya "Kamilisha Muamala kwa ajili ya Kutia Saini".

![Kukamilisha muamala kwa ajili ya kutia saini](assets/fr/10.webp)

### Hatua ya 3: Tia saini muamala wako kwa funguo zako tofauti

Sasa umefika wakati wa kutia saini muamala. Ili kufanya hivyo, utie saini tu kwa software au hardware wallet(s) unazotumia.

![Kutia saini muamala kwa funguo za multisig](assets/fr/11.webp)

### Hatua ya 4: Pakua muamala uliotiwa saini, na usiutangaze kwenye mtandao

Muamala wa Bitcoin sasa umetiwa saini na funguo zote mbili za multisig yetu ya 2-of-2. Usibofye "Tangaza Muamala", vinginevyo utasambazwa kwa mtandao wote na, ikiwa unatumia ColdCard hardware wallet, muamala wako utawekwa wazi hadharani na fedha zako zitakuwa hatarini.

![Muamala uliotiwa saini, uko tayari lakini haujatangazwa](assets/fr/12.webp)

### Hatua ya 5: Onyesha script ya muamala uliotiwa saini, au pakua faili ya PSBT

Ili kuonyesha muamala wa Bitcoin uliotiwa saini, sasa bofya "Tazama Muamala wa Mwisho". Kisha unaweza kunakili script ya muamala wa Bitcoin uliotiwa saini:

*02000000000101ade28cc43b2f51e09c88a87dfaeda8a601a78cddb458e47d99f0651020c1aaa60000000000fdffffff010b370000000000002200201810640a195e5a992d1f6da58a9781f77db47ac63a332b072580cc5b57dd1c2e04004730440220320777c52799cc8015be7c3f724a3d77906ce3d551205c893347910279ed796a02204ee45912623c1c45bf3d93d6558d878737f88f20dcbd152dc28fac80e788f2aa01473044022008bf6ea8432e3fee0eaa7edb923f60e44bb5eb37e52a93d8fdb4e30814340b0f0220473f8fcfbadda9c86fdfc4d3dd55c7883f62312794361e4d4d93f52964bce6520147522102bd28ad9b52829baf62621821abb49339262c7ef32f8adf15bf01b4d91fb5a9a72103ace1a518996275cbf9ebdbeaa4703318a50d5ab7f0fe22b9e566d2f2f644ed3752ae9fa90e00*

![Kuonyesha script ya muamala uliotiwa saini](assets/fr/13.webp)

Ikiwa unataka kupakua faili ya muamala, unaweza aidha:

- kubofya "Faili", kisha "Hifadhi muamala…";
- au kubofya kitufe cha muunganisho wa mtandao chini kulia (kitufe cha manjano), kisha ubofye "Hifadhi Muamala wa Mwisho".

Kisha muamala utahifadhiwa ndani ya kompyuta yako.

![Kuhifadhi muamala wa mwisho ndani ya kompyuta](assets/fr/14.webp)

### Hatua ya 6: Tuma muamala kwa mchimbaji kupitia outofband.wizardsardine.com

Sasa kwa hatua za mwisho. Ili kutuma muamala kwa mchimbaji, unachopaswa kufanya ni:

- kwenda kwenye [outofband.wizardsardine.com](https://outofband.wizardsardine.com/);
- kubandika script ya muamala uliotiwa saini iliyonakiliwa katika hatua iliyotangulia, kisha ubofye "ONGEZA KWENYE FOLENI" hapa chini;

![Kubandika script ya muamala kwenye zana](assets/fr/15.webp)

- au kuchukua faili na kuivuta na kuidondosha kwenye eneo lililotengwa.

![Kudondosha faili ya muamala kwenye zana](assets/fr/16.webp)

Kisha muamala unaonyeshwa kama ilivyo hapa chini.

![Muamala kwenye foleni](assets/fr/17.webp)

Ikiwa ujumbe unakuambia kwamba jumla ya kiasi cha input cha satoshis katika muamala wako hakijulikani (na kwamba, kwa sababu hiyo, idadi ya satoshis kwa ajili ya ada haiwezi kukokotolewa), unahitaji tu kuingiza jumla ya kiasi cha input cha satoshis mwenyewe. Ili kukipata, bonyeza tu kwenye onyesho la muamala wako katika Sparrow, katikati ya mchoro:

![Jumla ya kiasi cha input kinachoonyeshwa katika Sparrow](assets/fr/18.webp)

Kisha ingiza kiasi hicho (15,904 sats katika mfano wetu) kwenye zana ya [outofband.wizardsardine.com](https://outofband.wizardsardine.com/):

![Kuingiza kwa mkono jumla ya kiasi cha input](assets/fr/19.webp)

Hatimaye, kagua kwamba fee rate ni sahihi.

### Hatua ya 7: Tuma muamala kupitia Slipstream

Hatimaye, unachopaswa kufanya ni kubofya "Tuma" ili muamala utumwe kwa MARA kupitia Slipstream.

![Kutuma muamala kupitia Slipstream](assets/fr/20.webp)

Ndani ya sekunde chache, muamala kisha hubadilika kutoka "Inatuma" hadi "Imekubaliwa":

![Muamala umekubaliwa na Slipstream](assets/fr/21.webp)

Kilichobaki ni kunakili kitambulisho cha muamala (TXID), kisha kukibandika kwenye [mempool.space](https://mempool.space/) ili kutazama ukichimbwa:

![Kutafuta TXID kwenye mempool.space](assets/fr/22.webp)

Tafadhali kumbuka: muamala utaonekana kama "Muamala haukupatikana" hadi mchimbaji, MARA, achimbe kitalu na kujumuisha muamala wako humo. Hili linaweza kuchukua makumi kadhaa ya dakika, au hata saa, kwa sababu MARA inashikilia tu takriban 4.5% ya hash rate ya mtandao wa Bitcoin. Kufikia 4 Agosti 2026, hii inalingana takriban na kitalu kimoja kuchimbwa kila saa 3 na dakika 45.
