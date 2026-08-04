---
name: Slipstream
description: Kurungika ihererekanya ryashizweko umukono imbonankubone ku mucukuzi ukoresheje Slipstream, utarisakaje ku muhora wa Bitcoin
---

![cover](assets/cover.webp)

Mu bisanzwe, iyo ushize umukono ku ihererekanya, rica risakazwa ubwaco kuri node zose za Bitcoin ziri ku muhora. Hanyuma ririndira ko ricukurwa.

Ariko rero, igihe cose ritari mu citunza, umugizi wa nabi yaronse urufunguzo rwawe rw'ibanga arashobora kurisubiriza n'irindi maze yibe amahera. Ni ivyo bisanzwe biba niba ukoresha hardware wallet ya ColdCard.

Igikoresho Slipstream c'isosiyete y'ugucukura MARA kikwemerera kwirengagiza ugusakaza ihererekanya ku muhora: rirungikwa imbonankubone ku mucukuzi (kandi kuri we gusa), ivyo bikarigumiza mu bwiherero kandi bikirinda kurishira ku mugaragaro ku muhora. Birashoboka ko ihererekanya rizotwara umwanya munini imbere y'uko ricukurwa, ariko rizoba rikingiwe ku gitero co kurisubiriza.

Hasi aha, turatanga inyigisho yemerera abakoresha [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04), be n'abakoresha agakofero [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d), gukoresha igikoresho Slipstream c'umucukuzi MARA biciye ku rupapuro [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

⚠️ **Icitonderwa**: iki gikoresho cagenewe gusa imiterere imwimwe, cane cane amakofero ya Liana, amakofero ya miniscript n'ubwoko bumwebumwe bwa multisig. Wizardsardine **irabuza mu majambo abonerana** ugukoresha ico gikoresho ku makofero amahera yayo asanzwe ari mu kaga gakomeye ko kwibwa, nk'akarorero ayo amajambo yayo yo gukira yakozwe ku gikoresho ca ColdCard cakozweko n'intege nke za random number generator. Muri ico kintu, isiganwa n'umugizi wa nabi ni ikibazo c'amasegonda, kandi ihererekanya rirungitswe ku mucukuzi umwe gusa ritwara umwanya munini cane kugira riremeshwe ugereranije n'iryasakajwe mu buryo busanzwe. Niba ivyo bikwerekeye, banza usome inyigisho yacu yihariye:

https://planb.academy/tutorials/wallet/hardware/coldcard-seed-vulnerability-1348b153-89db-429c-80af-b5d3d8506b9a

## Ku bakoresha Liana

Liana ibungabungwa na Wizardsardine, iyo nyene isohora urupapuro [outofband.wizardsardine.com](https://outofband.wizardsardine.com/), gutyo inzira iragororotse: ukura gusa dosiye ya PSBT yashizweko umukono aho kuyisakaza.

*Ivyo ukwiye kuba ufise: amahera mu gakofero kawe ka Liana.*

### Intambwe ya 1: Kora ihererekanya ryawe ukoresheje Liana

Nk'uko bisanzwe, ubaka ihererekanya ryawe wongeramwo aderesi y'aho urungika, insiguro, n'igitigiri c'amahera (aha, ni ico kinini kiboneka mu gakofero).

Kugira ushingire igipimo c'ikiguzi:

- hitamwo ama coins ushaka gukoresha ukanda ku gasandugu gatoyi kari epfo ibubamfu, munsi ya "Coins selection";
- hanyuma winjize igipimo c'ikiguzi. Wibuke gushinga ikiguzi kiri hejuru cane y'igipimo bagusaba, nk'uko bisiguwe kuri uru rupapuro: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Amaherezo, ukande kuri "Next".

![Ukubaka ihererekanya muri Liana](assets/fr/01.webp)

### Intambwe ya 2: Suzuma ibiranga ihererekanya ryawe

Imbere y'uko ukanda kuri "Sign", suzuma ibiranga ihererekanya ryawe; canecane:

- igitigiri c'amahera urungika;
- igitigiri ca satoshis ugeneye ikiguzi c'ihererekanya;
- ariko hejuru ya vyose, aderesi urungikako amahera (wibuke gusuzuma ibimenyetso 5/6 vya mbere, 5/6 vya nyuma, n'ibimenyetso 5/6 vyo hagati mu aderesi kugira wirinde ibitero vya "address poisoning").

![Ugusuzuma ibiranga ihererekanya](assets/fr/02.webp)

### Intambwe ya 3: Hitamwo amakofero ashira umukono

Ubukurikira, hitamwo amakofero ya porogaramu na/canke hardware wallets ukeneye kugira ushire umukono ku ihererekanya ryawe. Twokwibutsa mu makonjo: ku gakofero ka multisig ya 2-kuri-2, ukeneye imikono 2 kuri 2.

### Intambwe ya 4: Kura dosiye ya PSBT y'ihererekanya ryawe

Ihererekanya rya Bitcoin ubu rimaze gushirwako umukono n'imfunguruzo zibereye. Ntukande kuri "Broadcast", bitaba ivyo rizosangizwa umuhora wose kandi, niba ukoresha hardware wallet ya ColdCard, ihererekanya ryawe rizoshirwa ku mugaragaro maze amahera yawe abe mu kaga.

Ubu urashobora gukanda kuri "Export", hanyuma ubike dosiye ya PSBT kuri mudasobwa yawe.

![Ugukura dosiye ya PSBT muri Liana](assets/fr/03.webp)

### Intambwe ya 5: Rungika ihererekanya ku mucukuzi biciye kuri outofband.wizardsardine.com

Ubu turaje ku ntambwe za nyuma. Kugira urungike ihererekanya ku mucukuzi, ico gusa ukwiye gukora ni ukufata dosiye ya PSBT uyikwegere uyiterere mu kibanza cagenewe ivyo.

![Ugutereka dosiye ya PSBT kuri outofband.wizardsardine.com](assets/fr/04.webp)

Ihererekanya rica rigaragara nk'uko bibonwa hasi aha.

![Ihererekanya riri mu murongo w'ukurindira](assets/fr/05.webp)

### Intambwe ya 6: Rungika ihererekanya biciye kuri Slipstream

Amaherezo, ico gusa ukwiye gukora ni ugukanda kuri "Send" kugira ihererekanya rirungikwe kuri MARA biciye kuri Slipstream.

![Ukurungika ihererekanya biciye kuri Slipstream](assets/fr/06.webp)

Mu masegonda makeyi, ihererekanya rica rivuye kuri "Sending" rija kuri "Accepted":

![Ihererekanya ryemewe na Slipstream](assets/fr/07.webp)

Ibisigaye ni ugukoporora ikiranga ihererekanya (TXID), hanyuma ukiterere muri [mempool.space](https://mempool.space/) kugira urabe uko ricukurwa:

![Ugushakisha TXID kuri mempool.space](assets/fr/08.webp)

Ico ukwiye kumenya: ihererekanya rizogaragara nka "Transaction not found" gushika umucukuzi, MARA, acukura icitunza kandi ashiremwo ihererekanya ryawe. Ivyo birashobora gutwara mirongo mikeyi y'iminota, canke mbere amasaha, kuko MARA ifise gusa nka 4,5% vy'i hashrate y'umuhora wa Bitcoin. Ku wa 4 Myandagaro 2026, ivyo bihuye n'icitunza kimwe cicukurwa nka buri masaha 3 n'iminota 45.

## Ku bakoresha ayandi makofero

Niba udakoresha [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04) ariko ukagomba gukoresha ico gikoresho, ng'iyi inyigisho ikoresha agakofero ka multisig ya 2-kuri-2. Kugira ngo tubikore, tuzokoresha agakofero ka porogaramu [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d).

*Ivyo ukwiye kuba ufise: amahera mu gakofero kawe ka Sparrow.*

### Intambwe ya 1: Kora ihererekanya ryawe

Ukoresheje [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d), kora ihererekanya ku gakofero kawe ka multisig. Wibuke gushinga ikiguzi kiri hejuru cane y'igipimo bagusaba, nk'uko bisiguwe kuri uru rupapuro: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Umaze kurikora, ukande kuri "Create Transaction".

![Ugukora ihererekanya muri Sparrow](assets/fr/09.webp)

### Intambwe ya 2: Rangiza ihererekanya ryawe

Kugira urangize ihererekanya ryawe, ubu ukeneye kurishirako umukono. Kugira ubikore, ukande kuri "Finalize Transaction for Signing".

![Ukurangiza ihererekanya kugira rishirweko umukono](assets/fr/10.webp)

### Intambwe ya 3: Shira umukono ku ihererekanya ryawe ukoresheje imfunguruzo zawe zitandukanye

Ubu ni umwanya wo gushira umukono ku ihererekanya. Kugira ubikore, urishirako gusa umukono ukoresheje agakofero ka porogaramu canke hardware wallets ukoresha.

![Ugushira umukono ku ihererekanya ukoresheje imfunguruzo za multisig](assets/fr/11.webp)

### Intambwe ya 4: Kurura ihererekanya ryashizweko umukono, kandi ntuze urisakaze ku muhora

Ihererekanya rya Bitcoin ubu rimaze gushirwako umukono n'imfunguruzo zompi za multisig yacu ya 2-kuri-2. Ntukande kuri "Broadcast Transaction", bitaba ivyo rizosangizwa umuhora wose kandi, niba ukoresha hardware wallet ya ColdCard, ihererekanya ryawe rizoshirwa ku mugaragaro maze amahera yawe abe mu kaga.

![Ihererekanya ryashizweko umukono, ryiteguye ariko ritarasakazwa](assets/fr/12.webp)

### Intambwe ya 5: Garagaza script y'ihererekanya ryashizweko umukono, canke kurura dosiye ya PSBT

Kugira ugaragaze ihererekanya rya Bitcoin ryashizweko umukono, ubu ukande kuri "View Final Transaction". Uca ushobora gukoporora script y'ihererekanya rya Bitcoin ryashizweko umukono:

*02000000000101ade28cc43b2f51e09c88a87dfaeda8a601a78cddb458e47d99f0651020c1aaa60000000000fdffffff010b370000000000002200201810640a195e5a992d1f6da58a9781f77db47ac63a332b072580cc5b57dd1c2e04004730440220320777c52799cc8015be7c3f724a3d77906ce3d551205c893347910279ed796a02204ee45912623c1c45bf3d93d6558d878737f88f20dcbd152dc28fac80e788f2aa01473044022008bf6ea8432e3fee0eaa7edb923f60e44bb5eb37e52a93d8fdb4e30814340b0f0220473f8fcfbadda9c86fdfc4d3dd55c7883f62312794361e4d4d93f52964bce6520147522102bd28ad9b52829baf62621821abb49339262c7ef32f8adf15bf01b4d91fb5a9a72103ace1a518996275cbf9ebdbeaa4703318a50d5ab7f0fe22b9e566d2f2f644ed3752ae9fa90e00*

![Ukugaragaza script y'ihererekanya ryashizweko umukono](assets/fr/13.webp)

Niba ushaka kurura dosiye y'ihererekanya, urashobora:

- gukanda kuri "File", hanyuma kuri "Save transaction…";
- canke gukanda ku buto bw'ihuza ry'umuhora buri epfo iburyo (buto y'umuhondo), hanyuma ukande kuri "Save Final Transaction".

Ihererekanya rica ribikwa kuri mudasobwa yawe.

![Ugubika ihererekanya rya nyuma kuri mudasobwa](assets/fr/14.webp)

### Intambwe ya 6: Rungika ihererekanya ku mucukuzi biciye kuri outofband.wizardsardine.com

Ubu turaje ku ntambwe za nyuma. Kugira urungike ihererekanya ku mucukuzi, ico gusa ukwiye gukora ni:

- kuja kuri [outofband.wizardsardine.com](https://outofband.wizardsardine.com/);
- gutereramwo script y'ihererekanya ryashizweko umukono wakoporoye ku ntambwe iheze, hanyuma ukande kuri "ADD TO QUEUE" hasi aho;

![Ugutereramwo script y'ihererekanya mu gikoresho](assets/fr/15.webp)

- canke gufata dosiye uyikwegere uyiterere mu kibanza cagenewe ivyo.

![Ugutereka dosiye y'ihererekanya mu gikoresho](assets/fr/16.webp)

Ihererekanya rica rigaragara nk'uko bibonwa hasi aha.

![Ihererekanya riri mu murongo w'ukurindira](assets/fr/17.webp)

Niba ubutumwa bukubwiye ko igitigiri cose ca satoshis zinjira mu ihererekanya ryawe kitazwi (kandi ko, kubw'ivyo, igitigiri ca satoshis z'ikiguzi kidashobora guharurwa), ukeneye gusa kwinjiza n'ukuboko igitigiri cose ca satoshis zinjira. Kugira ukironke, ukande gusa ku kigaragaza ihererekanya ryawe muri Sparrow, hagati mu gishushanyo:

![Igitigiri cose cinjira nk'uko cigaragara muri Sparrow](assets/fr/18.webp)

Hanyuma winjize ico gitigiri (15 904 sats mu karorero kacu) mu gikoresho [outofband.wizardsardine.com](https://outofband.wizardsardine.com/):

![Ukwinjiza n'ukuboko igitigiri cose cinjira](assets/fr/19.webp)

Amaherezo, suzuma ko igipimo c'ikiguzi kiri kwo.

### Intambwe ya 7: Rungika ihererekanya biciye kuri Slipstream

Amaherezo, ico gusa ukwiye gukora ni ugukanda kuri "Send" kugira ihererekanya rirungikwe kuri MARA biciye kuri Slipstream.

![Ukurungika ihererekanya biciye kuri Slipstream](assets/fr/20.webp)

Mu masegonda makeyi, ihererekanya rica rivuye kuri "Sending" rija kuri "Accepted":

![Ihererekanya ryemewe na Slipstream](assets/fr/21.webp)

Ibisigaye ni ugukoporora ikiranga ihererekanya (TXID), hanyuma ukiterere muri [mempool.space](https://mempool.space/) kugira urabe uko ricukurwa:

![Ugushakisha TXID kuri mempool.space](assets/fr/22.webp)

Ico ukwiye kumenya: ihererekanya rizogaragara nka "Transaction not found" gushika umucukuzi, MARA, acukura icitunza kandi ashiremwo ihererekanya ryawe. Ivyo birashobora gutwara mirongo mikeyi y'iminota, canke mbere amasaha, kuko MARA ifise gusa nka 4,5% vy'i hashrate y'umuhora wa Bitcoin. Ku wa 4 Myandagaro 2026, ivyo bihuye n'icitunza kimwe cicukurwa nka buri masaha 3 n'iminota 45.
