---
term: ÜMBERMAKSE

---
Bitcoini ahelate analüüsi sisemine heuristika, mis võimaldab hüpoteesi tehingu väljundite olemuse kohta, mis põhineb ümmargustel summadel. Üldiselt, kui lihtsa maksemustri (1 sisend ja 2 väljundit) puhul kulutab üks väljunditest ümmarguse summa, siis kujutab see endast makset. Kui üks väljund esindab makse, siis teine väljund esindab muutust. Seega võib tõlgendada, et tõenäoliselt on tehingu sisestanud kasutaja käsutuses ikka veel väljund, mis on identifitseeritud kui muutus.

Tuleb märkida, et see heuristika ei ole alati kohaldatav, sest enamik makseid tehakse ikka veel fiat-valuutaühikutes. Tõepoolest, kui kaupmees Prantsusmaal aktsepteerib bitcoin'i, ei näita nad üldiselt stabiilset hinda satsides. Nad valivad pigem eurodes väljendatud hinna ja bitcoinides väljendatud summa konverteerimise, mida makstakse nende kassasüsteemi kaudu (näiteks BTCPay Server). Seetõttu ei tohiks tehingu väljundis olla ümmargune number. Sellegipoolest võiks analüütik üritada seda ümberarvestust teha, võttes arvesse tehingu võrgus edastamise ajal kehtinud vahetuskurssi. Kui ühel päeval muutub bitcoin meie börsidel eelistatud arvestusühikuks, võib see heuristika muutuda analüüside jaoks veelgi kasulikumaks.

![](../../dictionnaire/assets/11.webp)