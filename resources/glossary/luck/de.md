---
term: LUCK
---

Ein Indikator, der in Mining-Pools verwendet wird, um die Leistung eines Pools im Verhältnis zu seinen theoretischen Erwartungen zu messen. Wie der Name schon sagt, bewertet er das Glück des Pools, einen Block zu finden. Glück wird berechnet, indem die theoretisch benötigte Anzahl an Shares, basierend auf der aktuellen Schwierigkeit von Bitcoin, mit der tatsächlich produzierten Anzahl an Shares verglichen wird, um diesen Block zu finden. Eine Anzahl an Shares, die niedriger als erwartet ist, deutet auf gutes Glück hin, während eine höhere Zahl auf schlechtes Glück hindeutet.

Indem die Schwierigkeit bei Bitcoin mit seiner Anzahl an pro Sekunde produzierten Shares und der Schwierigkeit jeder Share korreliert wird, kann der Pool die Anzahl an Shares berechnen, die theoretisch notwendig sind, um einen gültigen Block zu finden. Angenommen, theoretisch benötigt ein Pool 100.000 Shares, um einen Block zu finden. Wenn der Pool tatsächlich 200.000 produziert, bevor er einen Block findet, beträgt sein Glück 50%:

```text
100.000 / 200.000 = 0,5 = 50%
```

Umgekehrt, wenn dieser Pool einen gültigen Block findet, nachdem er nur 50.000 Shares produziert hat, dann beträgt sein Glück 200%:

```text
100.000 / 50.000 = 2 = 200%
```

Glück ist ein Indikator, der nur aktualisiert werden kann, nachdem ein Block vom Pool entdeckt wurde, was ihn zu einem statischen Indikator macht, der periodisch aktualisiert wird.