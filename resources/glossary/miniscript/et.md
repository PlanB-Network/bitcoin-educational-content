---
term: MINISCRIPT
---

Raamistik, mis on loodud selleks, et pakkuda turvalist viisi skriptide programmeerimiseks Bitcoinil. Bitcoini emakeelt nimetatakse skriptiks. Praktikas on seda eriti keeruline kasutada, eriti keerukate ja kohandatud rakenduste jaoks. Mis veelgi olulisem, skripti piirangute kontrollimine on väga keeruline. Miniscript kasutab Bitcoini skriptide alamhulka, et lihtsustada nende loomist, analüüsi ja kontrollimist. Iga miniscript vastab üks-ühele emakeelsele skriptile. Kasutatakse kasutajasõbralikku poliitikakeelt, mis seejärel kompileeritakse miniscriptiks, et lõpuks vastata emakeelsele skriptile.

![](../../dictionnaire/assets/30.png)

Miniscript võimaldab seega arendajatel luua keerukaid skripte turvalisemal ja usaldusväärsemal viisil. Miniscripti olulised omadused on järgmised:
* See võimaldab skripti staatilist analüüsi, sealhulgas selle lubatud kulutamistingimusi ja ressursside kulu;
* See võimaldab luua skripte, mis vastavad konsensusele;
* See võimaldab analüüsida, kas erinevad kulutamisteed vastavad sõlmede standardreeglitele;
* See kehtestab üldise standardi, mis on arusaadav ja komponeeritav, kõigile rahakottide tarkvarale ja riistvarale.

Miniscripti projekt käivitati 2018. aastal Peter Wuille, Andrew Poelstra ja Sanket Kanjalkari poolt ettevõtte Blockstream kaudu. Miniscript lisati Bitcoin Core rahakotti ainult vaatamisrežiimis detsembris 2022 versiooniga 24.0 ja seejärel täielikult mais 2023 versiooniga 25.0.