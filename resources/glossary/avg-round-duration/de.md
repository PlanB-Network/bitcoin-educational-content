---
term: AVG. ROUND DURATION
---

Die durchschnittliche Rundendauer ist ein Indikator, der verwendet wird, um die Zeit zu schätzen, die ein Mining-Pool benötigt, um einen Block zu finden, basierend auf der Schwierigkeit des Netzwerks und der Hashrate des Pools. Sie wird berechnet, indem die Anzahl der Shares, die erwartet werden, um einen Block zu finden, durch die Hashrate des Pools geteilt wird. Zum Beispiel, wenn ein Mining-Pool 200 Miner hat und jeder durchschnittlich 4 Shares pro Sekunde generiert, ist die gesamte Rechenleistung des Pools 800 Shares pro Sekunde:

```text
200 * 4 = 800
```

Unter der Annahme, dass es im Durchschnitt 1 Million Shares benötigt, um einen gültigen Block zu finden, wäre die *Avg. Round Duration* des Pools 1.250 Sekunden oder etwa 21 Minuten:

```text
1,000,000 / 800 = 1,250
```

In praktischen Begriffen bedeutet dies, dass der Mining-Pool im Durchschnitt alle 21 Minuten oder so einen Block finden sollte. Dieser Indikator schwankt mit Veränderungen in der Hashrate des Pools: Eine Erhöhung der Hashrate reduziert die *Avg. Round Duration*, während eine Verringerung sie verlängert. Sie wird auch mit jeder periodischen Anpassung des Bitcoin-Schwierigkeitsziels (alle 2016 Blöcke) schwanken. Diese Maßnahme berücksichtigt nicht die von anderen Pools gefundenen Blöcke und konzentriert sich ausschließlich auf die interne Leistung des untersuchten Pools.