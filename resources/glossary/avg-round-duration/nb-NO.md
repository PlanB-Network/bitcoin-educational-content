---
term: AVG. RUNDE VARIGHET

---
Gjennomsnittlig rundevarighet er en indikator som brukes til å estimere hvor lang tid det tar for en utvinningspool å finne en blokk, basert på nettverkets vanskelighetsgrad og poolens hashrate. Den beregnes ved å ta antall aksjer som forventes å finne en blokk, og dividere det med poolens hashrate. Hvis en utvinningspool for eksempel har 200 utvinnere, og hver av dem i gjennomsnitt genererer fire aksjer per sekund, er poolens totale regnekraft 800 aksjer per sekund:

```text
200 * 4 = 800
```

Hvis vi antar at det i gjennomsnitt tar 1 million aksjer å finne en gyldig blokk, vil bassengets *Vg. Round Duration* være 1 250 sekunder, eller omtrent 21 minutter:

```text
1,000,000 / 800 = 1,250
```

I praksis betyr dette at utvinningsbassenget i gjennomsnitt bør finne en blokk omtrent hvert 21. minutt. Denne indikatoren svinger med endringer i bassengets hashrate: en økning i hashrate reduserer *Avg. Round Duration*, mens en reduksjon forlenger den. Den vil også svinge med hver periodiske justering av Bitcoin-svårighetsmålet (hver 2016. blokk). Dette målet tar ikke hensyn til blokker som er funnet av andre bassenger, og fokuserer utelukkende på den interne ytelsen til bassenget som studeres.