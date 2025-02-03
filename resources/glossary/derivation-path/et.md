---
term: TULETAMISE TEE

---
Hierarhilise deterministliku (HD) rahakoti kontekstis viitab tuletamise tee indeksite jadale, mida kasutatakse peavõti alamvõtmete tuletamiseks. BIP32-s kirjeldatud tee määrab kindlaks puu struktuuri, mille abil tuletatakse allvõtmed. Tuletamise teed kujutatakse kaldkriipsudega eraldatud indeksite jadana ja see algab alati peavõti (tähistatud kui "m/"). Näiteks võib tüüpiline tee olla `m/84'/0'/0'/0'/0/0`. Iga tuletamistasand on seotud konkreetse sügavusega:


- `m /` tähistab peamise isikliku võtme. See on rahakoti jaoks ainulaadne ja tal ei saa olla sama sügavusega õdesid. Peavõti tuletatakse otse seemnest;
- `m / purpose' /` näitab tuletamise eesmärki, mis aitab tuvastada järgitavat standardit. See väli on kirjeldatud BIP43-s. Näiteks kui rahakott järgib BIP84 standardit (SegWit V0), siis on indeks `84'`;
- `m / purpose' / coin-type' /` näitab krüptoraha tüüpi. See võimaldab selgelt eristada ühele krüptovaluutale pühendatud filiaale ja mitmele muule rahakotile pühendatud filiaale. Bitcoinile pühendatud indeks on `0'`;
- `m / eesmärk' / mündi tüüp' / konto' /` tähistab kontonumbrit. See sügavus teeb rahakoti eristamise ja organiseerimise erinevateks kontodeks lihtsaks. Need kontod on nummerdatud alates `0'`. Laiendatud võtmed (`xpub`, `xprv`...) asuvad sellel sügavustasemel;
- `m / eesmärk' / mündi tüüp' / konto' / muutus /` näitab teed. Igal 3. sügavusel määratletud kontol on 4. sügavusel kaks teed: väline ahel ja sisemine ahel (mida nimetatakse ka "muutus"). Väline ahel tuleneb aadressidest, mis on mõeldud avalikult jagamiseks, st aadressidest, mida meile pakutakse, kui me vajutame rahakoti tarkvaras nupule "saada". Sisemine ahel tuleneb aadressidest, mis ei ole mõeldud avalikuks vahetamiseks, peamiselt muutmisaadressidest. Väline ahel on identifitseeritud indeksiga `0` ja sisemine ahel on identifitseeritud indeksiga `1`. Te märkate, et sellest sügavusest alates ei tee me enam karastatud tuletamist, vaid tavalist tuletamist (puudub alistus). Tänu sellele mehhanismile saame tuletada kõik laps-avalikud võtmed nende `xpub`-st;
- `m / eesmärk' / mündi tüüp' / konto' / muutus / aadressi-indeks` näitab lihtsalt vastuvõtva aadressi numbrit ja selle võtmepaari, et eristada seda sama haru samal sügavusel asuvatest vendadest. Näiteks esimesel tuletatud aadressil on indeks `0`, teisel aadressil on indeks `1` ja nii edasi...

Näiteks, kui minu vastuvõtva aadressi tuletamise tee on `m / 86' / 0' / 0' / 0 / 5`, saame tuletada järgmise teabe:


- `86'` näitab, et me järgime BIP86 (Taproot / SegWit V1) tuletamisstandardit;
- `0'` näitab, et tegemist on Bitcoini aadressiga;
- "0" näitab, et oleme rahakoti esimesel kontol;
- "0" näitab, et tegemist on välise aadressiga;
- "5" näitab, et see on selle konto kuues väline aadress.

![](../../dictionnaire/assets/18.webp)