---
term: AVG. RUNDENDAUER

---
Die durchschnittliche Rundendauer ist ein Indikator, mit dem die Zeit geschätzt wird, die ein Mining-Pool benötigt, um einen Block zu finden, basierend auf der Schwierigkeit des Netzwerks und der Hash-Rate des Pools. Sie wird berechnet, indem die Anzahl der Anteile, die zum Finden eines Blocks erwartet werden, durch die Hash-Rate des Pools geteilt wird. Wenn ein Mining-Pool beispielsweise 200 Miner hat und jeder durchschnittlich 4 Shares pro Sekunde erzeugt, beträgt die gesamte Rechenleistung des Pools 800 Shares pro Sekunde:

```text
200 * 4 = 800
```

Unter der Annahme, dass es im Durchschnitt 1 Million Aktien braucht, um einen gültigen Block zu finden, würde die *Avg. Round Duration* des Pools 1.250 Sekunden oder etwa 21 Minuten betragen:

```text
1,000,000 / 800 = 1,250
```

In der Praxis bedeutet dies, dass der Mining-Pool im Durchschnitt etwa alle 21 Minuten einen Block finden sollte. Dieser Indikator schwankt mit Änderungen der Hashrate des Pools: Ein Anstieg der Hashrate reduziert die *Avg. Round Duration*, während eine Verringerung sie verlängert. Sie schwankt auch bei jeder periodischen Anpassung des Bitcoin-Schwierigkeitsziels (alle 2016 Blöcke). Dieses Maß berücksichtigt keine von anderen Pools gefundenen Blöcke und konzentriert sich ausschließlich auf die interne Leistung des untersuchten Pools.