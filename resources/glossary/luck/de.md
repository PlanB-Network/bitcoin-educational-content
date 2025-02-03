---
term: LUCK

---
Ein Indikator, der in Mining-Pools verwendet wird, um die Leistung eines Pools im Vergleich zu seinen theoretischen Erwartungen zu messen. Wie der Name schon sagt, bewertet er das Glück des Pools beim Finden eines Blocks. Das Glück wird berechnet, indem die Anzahl der Anteile, die theoretisch benötigt werden, um einen gültigen Block zu finden, basierend auf der aktuellen Schwierigkeit von Bitcoin, mit der tatsächlichen Anzahl der Anteile verglichen wird, die produziert wurden, um diesen Block zu finden. Eine geringere Anzahl von Anteilen als erwartet deutet auf Glück hin, während eine höhere Anzahl auf Pech hinweist.

Indem die Schwierigkeit von Bitcoin mit der Anzahl der pro Sekunde produzierten Anteile und der Schwierigkeit jedes Anteils korreliert wird, kann der Pool die Anzahl der Anteile berechnen, die theoretisch notwendig sind, um einen gültigen Block zu finden. Nehmen wir zum Beispiel an, dass ein Pool theoretisch 100.000 Anteile braucht, um einen Block zu finden. Wenn der Pool tatsächlich 200.000 produziert, bevor er einen Block findet, beträgt sein Glück 50%:

```text
100,000 / 200,000 = 0.5 = 50%
```

Umgekehrt, wenn dieser Pool einen gültigen Block gefunden hat, nachdem er nur 50.000 Anteile produziert hat, dann ist sein Glück 200%:

```text
100,000 / 50,000 = 2 = 200%
```

Glück ist ein Indikator, der nur aktualisiert werden kann, nachdem ein Block vom Pool entdeckt wurde, so dass es sich um einen statischen Indikator handelt, der in regelmäßigen Abständen aktualisiert wird.