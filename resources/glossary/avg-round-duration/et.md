---
term: KESKMINE RINGI KESTUS
---

Keskmine ringi kestus on näitaja, mida kasutatakse hinnangu andmiseks ajale, mis kulub kaevandusbasseinil ploki leidmiseks, lähtudes võrgu raskusastmest ja basseini hashrate'ist. See arvutatakse, võttes arvesse oodatavate osakute arvu, mis on vajalik ploki leidmiseks, ja jagades selle basseini hashrate'iga. Näiteks, kui kaevandusbasseinil on 200 kaevurit ja igaüks genereerib keskmiselt 4 osakut sekundis, on basseini kogu arvutusvõimsus 800 osakut sekundis:

```text
200 * 4 = 800
```

Eeldades, et keskmiselt on vaja leida kehtiv plokk 1 miljon osakut, oleks basseini *Keskmine Ringi Kestus* 1,250 sekundit ehk umbes 21 minutit:

```text
1,000,000 / 800 = 1,250
```

Praktilises mõttes tähendab see, et keskmiselt peaks kaevandusbassein leidma ploki iga 21 minuti järel. See näitaja kõigub koos muutustega basseini hashrate'is: hashrate'i suurenemine vähendab *Keskmine Ringi Kestus*t, samas kui vähenemine pikendab seda. Samuti kõigub see iga Bitcoin'i raskusastme perioodilise kohandamisega (iga 2016 ploki järel). See mõõdik ei võta arvesse teiste basseinide poolt leitud plokke ja keskendub ainult uuritava basseini sisemisele sooritusele.