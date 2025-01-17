---
term: AVG. RINGI KESTUS

---
Keskmine vooru kestus on näitaja, mida kasutatakse selleks, et hinnata aega, mis kulub kaevandamisbasseinil ploki leidmiseks, tuginedes võrgu raskusastmele ja basseini hashrate'ile. See arvutatakse, võttes ploki leidmiseks oodatavate aktsiate arvu ja jagades selle basseini hashrate'iga. Näiteks kui kaevandamisbasseinil on 200 kaevurit ja igaüks neist toodab keskmiselt 4 aktsiat sekundis, on basseini kogu arvutusvõimsus 800 aktsiat sekundis:

```text
200 * 4 = 800
```

Eeldades, et keskmiselt kulub 1 miljon aktsiat kehtiva ploki leidmiseks, on koondis *Avg. Round Duration* oleks 1250 sekundit ehk umbes 21 minutit:

```text
1,000,000 / 800 = 1,250
```

Praktikas tähendab see, et keskmiselt peaks kaevandamisbassein leidma ploki umbes iga 21 minuti tagant. See näitaja kõigub vastavalt basseini hashrate'i muutustele: hashrate suurenemine vähendab *Avg. Round Duration*, samas kui vähenemine pikendab seda. Samuti kõigub see näitaja iga Bitcoini raskusastme eesmärgi perioodilise kohandamise korral (iga 2016 ploki järel). See näitaja ei võta arvesse teiste basseinide leitud plokke ja keskendub ainult uuritava basseini sisemisele jõudlusele.