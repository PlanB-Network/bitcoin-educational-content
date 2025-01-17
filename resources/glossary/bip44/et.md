---
term: BIP44

---
Parandusettepanek, millega võetakse kasutusele standardne hierarhiline tuletamisstruktuur HD-kassade jaoks. BIP44 tugineb põhimõtetele, mis on kehtestatud BIP32ga võtme tuletamise kohta ja BIP43ga "purpose" välja kasutamise kohta. Sellega võetakse kasutusele viietasandiline tuletamisstruktuur: `m / eesmärk' / coin_type' / account' / change / address_index`. Siin on iga sügavuse üksikasjad:


- `m /` tähistab peamise isikliku võtme. See on rahakoti jaoks ainulaadne ja tal ei saa olla sama sügavusega õdesid. Peavõti tuletatakse otse rahakoti seemnest;
- `m / purpose' /` näitab tuletamise eesmärki, mis aitab tuvastada järgitavat standardit. See väli on kirjeldatud BIP43-s. Näiteks kui rahakott järgib BIP84 (SegWit V0) standardit, siis on indeks `84'`;
- `m / purpose' / coin-type' /` näitab krüptoraha tüüpi. See võimaldab selgelt eristada ühele krüptovaluutale ja teisele krüptovaluutale pühendatud filiaalid mitme mündi rahakotis. Bitcoinile pühendatud indeks on `0'`;
- `m / eesmärk' / mündi tüüp' / konto' /` tähistab kontonumbrit. See sügavus võimaldab rahakoti lihtsat eristamist ja organiseerimist erinevateks kontodeks. Need kontod on nummerdatud alates `0'`. Laiendatud võtmed (`xpub`, `xprv`...) asuvad sellel sügavusel;
- `m / eesmärk' / mündi tüüp' / konto' / vahetus /` tähistab ahelat. Igal kontol, nagu on määratletud sügavuses 3, on sügavuses 4 kaks ahelat: väline ahel ja sisemine ahel (mida nimetatakse ka "muutus"). Väline ahel tuleneb aadressidest, mis on mõeldud avalikuks edastamiseks, st aadressidest, mida pakutakse meile, kui me vajutame rahakoti tarkvaras nupule "saada". Sisemine ahel tuletab aadressid, mis ei ole mõeldud avalikuks vahetuseks, st peamiselt muutmisaadressid. Väline ahel on tähistatud indeksiga `0` ja sisemine ahel on tähistatud indeksiga `1`. Te märkate, et sellest sügavusest alates ei tee me enam karastatud tuletamist, vaid tavalist tuletamist (puudub alistus). Tänu sellele mehhanismile oleme võimelised tuletama kõik laps-avalikud võtmed nende `xpub`-st;
- `m / eesmärk' / mündi tüüp' / konto' / muutus / aadressi-indeks` näitab lihtsalt vastuvõtva aadressi numbrit ja selle võtmepaari, et eristada seda sama haru samal sügavusel asuvatest vendadest. Näiteks esimesel tuletatud aadressil on indeks `0`, teisel aadressil on indeks `1` ja nii edasi...

Näiteks, kui minu vastuvõtva aadressi tuletamise tee on `m / 86' / 0' / 0' / 0 / 5`, saame tuletada järgmise teabe:


- `86'` näitab, et me järgime BIP86 tuletamisstandardit (Taproot või SegWitV1);
- `0'` näitab, et tegemist on Bitcoini aadressiga;
- "0" näitab, et oleme rahakoti esimesel kontol;
- "0" näitab, et tegemist on välise aadressiga;
- "5" näitab, et see on selle konto kuues väline aadress.

![](../../dictionnaire/assets/18.webp)