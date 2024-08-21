---
term: AEGUNUD (PLOKK)
---

Viitab plokile ilma alamplokkideta: kehtiv plokk, kuid välja jäetud peamisest Bitcoin'i ahelast. See juhtub, kui kaks kaevurit leiavad kehtiva ploki samal ahela kõrgusel lühikese aja jooksul ja edastavad selle võrku. Noodid valivad lõpuks ainult ühe ploki, mida ahelasse lisada, lähtudes kõige rohkem kogunenud töö põhimõttest, muutes teise "aegunuks". Aegunud ploki tootmise protsess on järgmine:
* Kaks kaevurit leiavad kehtiva ploki samal ahela kõrgusel lühikese ajavahemiku jooksul. Nimetagem neid `Plokk A` ja `Plokk B`;
* Igaüks edastab oma ploki Bitcoin'i noodivõrku. Igal noodil on nüüd 2 plokki samal kõrgusel. Seega on olemas kaks kehtivat ahelat;
* Kaevurid jätkavad järgmiste plokkide töötõendite otsimist, kuid selleks peavad nad tingimata valima ainult ühe ploki `Plokk A` ja `Plokk B` vahel, millel nad kaevandavad;
* Kaevur leiab lõpuks kehtiva ploki `Plokk B` kohal. Nimetagem seda `Plokk B+1`;
* Nad edastavad `Plokk B+1` võrgu noodidele;
* Kuna noodid järgivad pikimat ahelat (kõige rohkem kogunenud tööga), hindavad nad, et `Ahel B` on see, mida järgida;
* Nad hülgavad `Plokk A`, mis ei ole enam peamise ahela osa. See on seega muutunud aegunuks plokiks.

![](../../dictionnaire/assets/9.png)

> ► *Inglise keeles nimetatakse seda "Stale Block" (vananenud plokk). Prantsuse keeles võib seda nimetada ka "bloc périmé" (aegunud plokk) või "bloc abandonné" (hüljatud plokk). Kuigi ma ei nõustu selle kasutusega, kasutavad mõned bitcoinerid terminit "bloc orphelin" (orvuplokk), viidates tegelikult aegunud plokile.*