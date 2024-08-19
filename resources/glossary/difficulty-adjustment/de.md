---
term: SCHWIERIGKEITSANPASSUNG
---

Die Schwierigkeitsanpassung ist ein periodischer Prozess, der das Schwierigkeitsziel für den Proof-of-Work-Mechanismus (Mining) bei Bitcoin neu definiert. Dieses Ereignis tritt alle 2016 Blöcke auf (ungefähr alle zwei Wochen). Es dient dazu, den Schwierigkeitsfaktor (auch Schwierigkeitsziel genannt) zu erhöhen oder zu verringern, abhängig davon, wie schnell die letzten 2016 Blöcke gefunden wurden. Die Anpassung zielt darauf ab, eine stabile und vorhersehbare Blockproduktionsrate zu erhalten, bei einer Frequenz von einem Block alle 10 Minuten, trotz Schwankungen in der von den Minern eingesetzten Rechenleistung. Die Änderung der Schwierigkeit während der Anpassung ist auf einen Faktor von 4 begrenzt. Die von den Knoten ausgeführte Formel zur Berechnung des neuen Ziels lautet wie folgt:
$$N = A \cdot \left(\frac{T}{1,209,600}\right)$$
&nbsp;
Wo:
* $N$: Das neue Ziel;
* $A$: Das alte Ziel der letzten 2016 Blöcke;
* $T$: Die gesamte tatsächliche Zeit der letzten 2016 Blöcke in Sekunden;
* $1,209,600$: Die Zielzeit in Sekunden, um 2016 Blöcke mit einem 10-Minuten-Intervall zwischen jedem zu produzieren.

> ► *Im Französischen wird manchmal auch der Begriff "reciblage" verwendet, um sich auf die Anpassung zu beziehen. Im Englischen wird es als "Difficulty Adjustment" bezeichnet.*