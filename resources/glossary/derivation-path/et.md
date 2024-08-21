---
term: TULETUSTEE
---

Hierarhiliste Deterministlike (HD) rahakottide kontekstis viitab tuletustee indeksite jadale, mida kasutatakse lapsevõtmete tuletamiseks peavõtmest. BIP32-s kirjeldatud tee identifitseerib puustruktuuri lapsevõtmete tuletamiseks. Tuletustee on esitatud indeksite jadana, mis on eraldatud kaldkriipsudega, ja algab alati peavõtmega (tähistatud kui `m/`). Näiteks tüüpiline tee võiks olla `m/84'/0'/0'/0/0`. Iga tuletustasand on seotud kindla sügavusega:
* `m /` tähistab peamist privaatvõtit. See on rahakotile ainulaadne ja samal sügavusel ei saa olla õdesid-vendi. Peavõti tuletatakse otse seemnest;
* `m / purpose' /` tähistab tuletuse eesmärki, mis aitab tuvastada järgitud standardit. See väli on kirjeldatud BIP43-s. Näiteks, kui rahakott järgib BIP84 standardit (SegWit V0), siis indeks oleks `84'`;
* `m / purpose' / coin-type' /` tähistab krüptoraha tüüpi. See võimaldab selgelt eristada ühele krüptorahale pühendatud harusid teistele pühendatud harudest mitme mündiga rahakotis. Bitcoinile pühendatud indeks on `0'`;
* `m / purpose' / coin-type' / account' /` tähistab konto numbrit. See sügavus teeb lihtsaks rahakoti erinevatesse kontodesse jaotamise ja organiseerimise. Need kontod on nummerdatud alates `0'`. Laiendatud võtmed (`xpub`, `xprv`...) asuvad sellel sügavusel;
* `m / purpose' / coin-type' / account' / change /` tähistab teed. Nagu sügavusel 3 määratletud iga konto puhul, on sügavusel 4 kaks teed: väline ahel ja sisemine ahel (mida nimetatakse ka "vahetus"). Väline ahel tuletatakse aadresse, mida on kavas jagada avalikult, st aadresse, mis pakutakse meile, kui klõpsame oma rahakotitarkvaras "vasta". Sisemine ahel tuletatakse aadresse, mida ei ole ette nähtud avalikult vahetamiseks, peamiselt vahetusaadresse. Väline ahel on identifitseeritud indeksiga `0` ja sisemine ahel indeksiga `1`. Märkate, et alates sellest sügavusest ei toimu enam kõvastatud tuletust, vaid tavalist tuletust (pole apostroofi). Tänu sellele mehhanismile suudame tuletada kõik lapse avalikud võtmed nende `xpub` alusel;

* `m / purpose' / coin-type' / account' / change / address-index` tähistab lihtsalt vastuvõtva aadressi numbrit ja selle võtmepaari, et eristada seda samal harul samal sügavusel asuvatest õdedest-vendadest. Näiteks esimesel tuletatud aadressil on indeks `0`, teisel aadressil on indeks `1` ja nii edasi...

Näiteks, kui minu vastuvõtva aadressi tuletustee on `m / 86' / 0' / 0' / 0 / 5`, võime järeldada järgmist teavet:
* `86'` näitab, et järgime BIP86 (Taproot / SegWit V1) tuletusstandardit;
* `0'` näitab, et tegemist on Bitcoin aadressiga;
* `0'` näitab, et oleme rahakoti esimesel kontol;
* `0` näitab, et tegemist on välise aadressiga;
* `5` näitab, et see on selle konto kuues väline aadress.

![](../../dictionnaire/assets/18.png)