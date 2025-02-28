---
term: SCHWIERIGKEITSANPASSUNG

---
Die Schwierigkeitsanpassung ist ein periodischer Prozess, der das Schwierigkeitsziel für den Proof-of-Work-Mechanismus (Mining) von Bitcoin neu definiert. Dieses Ereignis findet alle 2016 Blöcke (etwa alle zwei Wochen) statt. Es dient dazu, den Schwierigkeitsfaktor (auch Schwierigkeitsziel genannt) zu erhöhen oder zu senken, je nachdem, wie schnell die letzten 2016er Blöcke gefunden wurden. Die Anpassung zielt darauf ab, eine stabile und vorhersehbare Blockproduktionsrate aufrechtzuerhalten, mit einer Frequenz von einem Block alle 10 Minuten, trotz Schwankungen in der von den Minern eingesetzten Rechenleistung. Die Änderung der Schwierigkeit während der Anpassung ist auf einen Faktor von 4 begrenzt. Die Formel, die von den Knoten ausgeführt wird, um das neue Ziel zu berechnen, lautet wie folgt:

$$N = A \cdot \left(\frac{T}{1,209,600}\right)$$

&nbsp;

Wo:


- $N$: Das neue Ziel;
- $A$: Das alte Ziel der letzten 2016er Blöcke;
- $T$: Die tatsächliche Gesamtzeit der letzten 2016 Blöcke in Sekunden;
- $1,209,600$: Die Zielzeit in Sekunden für die Produktion von 2016 Blöcken mit einem Abstand von 10 Minuten.

> ► *Im Französischen wird der Begriff "reciblage" manchmal auch für die Anpassung verwendet. Im Englischen wird es als "Difficulty Adjustment" bezeichnet.*