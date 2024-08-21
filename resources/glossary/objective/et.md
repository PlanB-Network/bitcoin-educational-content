---
term: EESMÄRK
---

Deterministlikes ja hierarhilistes (HD) rahakottides tähistab eesmärk (või _otstarve_ inglise keeles), mille on määratlenud BIP43, konkreetset tuletustaset. See indeks, mis asub tuletuspuu esimesel tasemel (`m / otstarve' /`), identifitseerib rahakoti poolt omaks võetud tuletusstandardi, et hõlbustada erinevate rahakotihaldustarkvarade vahelist ühilduvust. Näiteks SegWiti aadresside (BIP84) puhul märgitakse eesmärk kui `/84'/`. See meetod võimaldab erinevat tüüpi aadresside võtmete tõhusat korraldamist samas HD rahakotis. Standardseid indekseid kasutatakse järgmiselt:
* P2PKH jaoks: `44'`;
* P2WPKH-nested-in-P2SH jaoks: `49'`;
* P2WPKH jaoks: `84'`;
* P2TR jaoks: `86'`.

![](../../dictionnaire/assets/20.png)