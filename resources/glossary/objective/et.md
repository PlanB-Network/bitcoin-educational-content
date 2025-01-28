---
term: OBJEKTIIV

---
Deterministlikes ja hierarhilistes (HD) rahakottides esindab BIP43 määratletud eesmärk (või inglise keeles _purpose_) konkreetset tuletamise taset. See indeks, mis asub tuletamispuu esimesel sügavusel (`m / purpose' /`), tähistab rahakoti poolt vastu võetud tuletamisstandardit, et hõlbustada erinevate rahakoti haldustarkvarade ühilduvust. Näiteks SegWit-aadresside (BIP84) puhul on eesmärk märgitud kui `/84'/`. See meetod võimaldab võtmete tõhusat korraldamist eri tüüpi aadresside vahel samas HD rahakotis. Kasutatakse järgmisi standardseid indekseid:


- P2PKH puhul: "44";
- P2WPKH-P2SH-siseselt: `49'`;
- P2WPKH puhul: `84'`;
- P2TR puhul: "86".

![](../../dictionnaire/assets/20.webp)