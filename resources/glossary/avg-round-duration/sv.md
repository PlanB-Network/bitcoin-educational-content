---
term: Genomsnittlig runda varaktighet
definition: En indikator som uppskattar genomsnittlig tid som krävs för en gruvepool att hitta ett block, baserat på dess beräkningskraft och nätverkets svårighet.
---

Den genomsnittliga omgångstiden är en indikator som används för att uppskatta den tid det tar för en Mining pool att hitta ett block, baserat på nätverkets svårighetsgrad och poolens Hashrate. Den beräknas genom att ta antalet aktier som förväntas hitta ett block och dividera det med poolens Hashrate. Om en Mining pool till exempel har 200 miners, och var och en genererar i genomsnitt 4 aktier per sekund, är poolens totala beräkningskraft 800 aktier per sekund:


```text
200 * 4 = 800
```


Om man antar att det i genomsnitt tar 1 miljon aktier att hitta ett giltigt block, skulle poolens *Avg. Round Duration* vara 1 250 sekunder, eller cirka 21 minuter:


```text
1,000,000 / 800 = 1,250
```


I praktiken innebär det att Mining pool i genomsnitt bör hitta ett block ungefär var 21:a minut. Denna indikator fluktuerar med förändringar i poolens Hashrate: en ökning av Hashrate minskar *Avg. Round Duration*, medan en minskning förlänger den. Den kommer också att fluktuera med varje periodisk justering av svårighetsmålet Bitcoin (vart 2016:e block). Detta mått tar inte hänsyn till block som hittats av andra pooler och fokuserar enbart på den interna prestandan i den pool som studeras.