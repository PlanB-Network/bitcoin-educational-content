---
term: MINISCRIPT

---
Raamistik, mille eesmärk on pakkuda raamistikku skriptide turvaliseks programmeerimiseks Bitcoinis. Bitcoini emakeeleks nimetatakse skripti. Seda on praktikas üsna keeruline kasutada, eriti keerukate ja kohandatud rakenduste puhul. Ennekõike on väga raske kontrollida skripti piiranguid. Miniscript kasutab Bitcoini skriptide alamhulka, et lihtsustada nende loomist, analüüsi ja kontrollimist. Iga miniskript on 1:1 samaväärne algupärase skriptiga. Kasutatakse kasutajasõbralikku poliitikakeelt, mis kompileeritakse seejärel miniscriptiks, et lõpuks vastata emakeelsele skriptile.

![](../../dictionnaire/assets/30.webp)

Miniscript võimaldab seega arendajatel ehitada keerulisi skripte turvalisemalt ja usaldusväärsemalt. Miniscripti olulised omadused on järgmised:


- See võimaldab skripti staatilist analüüsi, sealhulgas selle lubatud kulutustingimusi ja selle ressursikulusid;
- See võimaldab luua konsensust järgivaid skripte;
- See võimaldab analüüsida, kas erinevad kuluread vastavad sõlmede standardreeglitele või mitte;
- Sellega kehtestatakse üldine, arusaadav ja koostatav standard kogu rahakoti tarkvara ja riistvara jaoks.

Miniscripti projekti käivitasid 2018. aastal Peter Wuille, Andrew Poelstra ja Sanket Kanjalkar ettevõtte Blockstream kaudu. Miniscript lisati Bitcoin Core'i rahakotti ainult jälgimisrežiimis 2022. aasta detsembris versiooniga 24.0 ja seejärel täielikult 2023. aasta mais versiooniga 25.0.