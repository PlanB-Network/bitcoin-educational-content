---
term: BIP44
---

Ettepanek täiustuseks, mis tutvustab standardset hierarhilist tuletusstruktuuri HD rahakottidele. BIP44 tugineb BIP32 poolt võtmete tuletamiseks loodud põhimõtetele ja BIP43 kasutusele "eesmärgi" väljal. See tutvustab viie taseme tuletusstruktuuri: `m / eesmärk' / mündi_tüüp' / konto' / muutus / aadressi_indeks`. Siin on iga sügavuse detailid:
* `m /` tähistab peamist privaatvõtit. See on rahakotile ainulaadne ja samal sügavusel ei saa olla õdesid-vendi. Peamine võti on otseselt tuletatud rahakoti seemnest;
* `m / eesmärk' /` tähistab tuletuse eesmärki, mis aitab tuvastada järgitud standardit. See väli on kirjeldatud BIP43-s. Näiteks, kui rahakott järgib BIP84 (SegWit V0) standardit, oleks indeks `84'`;
* `m / eesmärk' / mündi_tüüp' /` tähistab krüptoraha tüüpi. See võimaldab selget eristamist ühele krüptorahale pühendatud harude ja teisele krüptorahale pühendatud harude vahel mitme mündi rahakotis. Bitcoinile pühendatud indeks on `0'`;
* `m / eesmärk' / mündi_tüüp' / konto' /` tähistab konto numbrit. See sügavus võimaldab rahakoti lihtsat eristamist ja korraldamist erinevateks kontodeks. Need kontod on nummerdatud alates `0'`. Laiendatud võtmed (`xpub`, `xprv`...) asuvad selles sügavuses;
* `m / eesmärk' / mündi_tüüp' / konto' / muutus /` tähistab ahelat. Nagu sügavuses 3 määratletud, on igal kontol sügavusel 4 kaks ahelat: väline ahel ja sisemine ahel (mida nimetatakse ka “muutuseks”). Väline ahel tuletatakse aadresse, mida on kavas avalikult kommunikeerida, st aadresse, mida pakutakse meile, kui klõpsame oma rahakotitarkvaras nupul “vasta”. Sisemine ahel tuletatakse aadresse, mida ei ole kavas avalikult vahetada, st peamiselt muutuse aadresse. Väline ahel on identifitseeritud indeksiga `0` ja sisemine ahel indeksiga `1`. Märkate, et alates sellest sügavusest ei teosta me enam kõvastatud tuletust, vaid tavalist tuletust (ei ole apostroofi). Tänu sellele mehhanismile oleme võimelised tuletama kõik laste avalikud võtmed nende `xpub`-st;
* `m / eesmärk' / mündi_tüüp' / konto' / muutus / aadressi-indeks` lihtsalt tähistab vastuvõtva aadressi numbrit ja selle võtmepaari, et eristada seda oma õdedest-vendadest samal sügavusel samal harul. Näiteks esimese tuletatud aadressi indeks on `0`, teise aadressi indeks on `1` ja nii edasi...
Näiteks, kui minu vastuvõtva aadressi tuletustee on `m / 86' / 0' / 0' / 0 / 5`, võime järeldada järgmist teavet:
* `86'` näitab, et järgime BIP86 (Taproot või SegWitV1) tuletusstandardit;
* `0'` näitab, et tegemist on Bitcoin aadressiga;
* `0'` näitab, et oleme rahakoti esimesel kontol;
* `0` näitab, et tegemist on välise aadressiga;
* `5` näitab, et see on selle konto kuues väline aadress.

![](../../dictionnaire/assets/18.png)