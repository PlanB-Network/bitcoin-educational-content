---
term: ÜMAR MAKSE
---

Sisemine heuristika Bitcoin'i ahela analüüsiks, mis võimaldab teha hüpoteesi tehingu väljundite olemuse kohta, lähtudes ümmargustest summadest. Üldiselt, kui on tegemist lihtsa maksemustriga (1 sisend ja 2 väljundit), kui üks väljunditest kasutab ümmargust summat, siis see esindab makset. Elimineerimise teel, kui üks väljund esindab makset, siis teine esindab vahetusraha. Seega võib tõlgendada, et tõenäoliselt omab tehingu sisestaja endiselt väljundit, mis on identifitseeritud kui vahetusraha.

Tuleb märkida, et see heuristika ei ole alati kohaldatav, kuna enamik makseid tehakse endiselt fiat valuuta ühikutes. Tõepoolest, kui Prantsusmaal asuv kaupmees aktsepteerib bitcoini, üldiselt ei kuvata stabiilseid hindu satsides. Nad eelistaksid pigem konversiooni eurodes näidatud hinna ja bitcoini kaudu makstava summa vahel läbi nende POS-i (näiteks BTCPay Server). Seetõttu ei tohiks tehingu väljundis olla ümmargust numbrit. Siiski võiks analüütik üritada teha seda konversiooni, võttes arvesse vahetuskurssi, mis kehtis tehingu võrgus levitamise ajal. Kui ühel päeval muutub bitcoin meie vahetuste eelistatud arvestusühikuks, võib see heuristika muutuda analüüside jaoks veelgi kasulikumaks.

![](../../dictionnaire/assets/11.png)