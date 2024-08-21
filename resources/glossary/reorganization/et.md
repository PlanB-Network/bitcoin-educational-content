---
term: REORGANISEERIMINE
---

Viitab nähtusele, kus plokiahel läbib oma struktuuri muudatuse konkureerivate plokkide olemasolu tõttu samal kõrgusel. See juhtub, kui osa plokiahelast asendatakse teise ahelaga, millel on suurem kogunenud töö hulk.

Need reorganiseerimised on Bitcoini loomuliku toimimise osa, kus erinevad kaevurid võivad leida uusi plokke peaaegu samaaegselt, jagades seeläbi Bitcoini võrgu kaheks. Sellistel juhtudel võib võrk ajutiselt jaguneda konkureerivateks ahelateks. Lõpuks, kui üks neist ahelatest kogub rohkem tööd, hülgavad noodid teised ahelad ja nende plokid muutuvad nn "vananenud plokkideks" või "orbudeks plokkideks". Ühe ahela asendamise protsess teisega on reorganiseerimine.

![](../../dictionnaire/assets/9.png)

Reorganiseerimisel võib olla mitmesuguseid tagajärgi. Esiteks, kui kasutajal oli tehing kinnitatud plokis, mis osutub hüljatuks, kuid see tehing ei ilmu lõpuks kehtivasse ahelasse, siis muutub nende tehing taas kinnitamata olekuks. Seetõttu soovitatakse alati oodata vähemalt 6 kinnitust, et pidada tehingut tõeliselt muutumatuks. Pärast 6 plokki sügavust on reorganiseerimised nii ebatõenäolised, et nende toimumise võimalust võib pidada praktiliselt olematuks.

Lisaks, ülemaailmsel süsteemi tasandil tähendavad reorganiseerimised kaevurite arvutusvõimsuse raiskamist. Tõepoolest, kui lõhe tekib, siis mõned kaevurid on ahelas `A` ja teised ahelas `B`. Kui ahel `B` lõpuks reorganiseerimise käigus hüljatakse, siis on sellel ahelal töötanud kaevurite arvutusvõimsus definitsiooni järgi raisatud. Kui Bitcoini võrgus toimub liiga palju reorganiseerimisi, väheneb selle üldine turvalisus. See on osaliselt põhjus, miks ploki suuruse suurendamine või iga ploki vahelise intervalli (10 minutit) vähendamine võib olla ohtlik.

> ► *Mõned bitcoini kasutajad eelistavad kasutada terminit "orbuks jäänud plokk" viitamaks aegunud plokile. Samuti, üldkõnepruugis kasutatakse "reorg" terminit viitamaks "reorganiseerimisele". Termin "reorganiseerimine" on anglicism. Täpsemalt võiks rääkida "resünkroniseerimisest".*