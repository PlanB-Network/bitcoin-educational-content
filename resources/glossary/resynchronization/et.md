---
term: RESÜNKRONISEERIMINE
---

Viitab nähtusele, kus plokiahel läbib oma struktuuri muudatuse konkureerivate plokkide olemasolu tõttu samal kõrgusel. See juhtub, kui osa plokiahelast asendatakse teise ahelaga, millel on suurem kogunenud töö hulk.

Need resünkroniseerimised on Bitcoini loomuliku toimimise osa, kus erinevad kaevurid võivad peaaegu samaaegselt leida uusi plokke, jagades seeläbi Bitcoini võrgu kaheks. Sellistel juhtudel võib võrk ajutiselt jaguneda konkureerivateks ahelateks. Lõpuks, kui üks neist ahelatest kogub rohkem tööd, hülgavad noodid teised ahelad ja nende plokid muutuvad nn "vananenud plokkideks" või "orbudeks plokkideks". Ühe ahela asendamine teisega on resünkroniseerimine.

![](../../dictionnaire/assets/9.png)

Resünkroniseerimisel võib olla mitmesuguseid tagajärgi. Esiteks, kui kasutaja tehing kinnitati plokis, mis osutub hüljatuks, kuid seda tehingut ei leita lõpuks kehtivast ahelast, siis muutub nende tehing taas kinnitamata olekuks. Seetõttu soovitatakse alati oodata vähemalt 6 kinnitust, et pidada tehingut tõeliselt muutumatuks. Pärast 6 plokki sügavust on resünkroniseerimised nii ebatõenäolised, et nende toimumise võimalust võib pidada praktiliselt olematuks.

Lisaks, ülemaailmsel süsteemi tasandil tähendavad resünkroniseerimised kaevurite arvutusvõimsuse raiskamist. Tõepoolest, kui lõhe tekib, siis mõned kaevurid on ahelas `A` ja teised ahelas `B`. Kui ahel `B` resünkroniseerimise käigus lõpuks hüljatakse, siis on sellel ahelal töötanud kaevurite poolt rakendatud arvutusvõimsus definitsiooni järgi raisatud. Kui Bitcoini võrgus toimub liiga palju resünkroniseerimisi, väheneb seega võrgu üldine turvalisus. See on osaliselt põhjus, miks ploki suuruse suurendamine või iga ploki vahelise intervalli (10 minutit) vähendamine võib olla ohtlik.

> ► *Mõned bitcoini kasutajad eelistavad kasutada terminit "orbuks jäänud plokk" viitamaks aegunud plokile. Samuti, kuigi see on anglicism, eelistatakse tavakeeles sageli "reorganiseerimist" või "reorgi" termini "resünkroniseerimine" asemel.*