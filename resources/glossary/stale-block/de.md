---
term: Stale Block

definition: Gültiger Block, der jedoch aus der Hauptkette ausgeschlossen wird, wenn zwei Miner gleichzeitig einen Block auf derselben Höhe finden.
---
Bezieht sich auf einen Block ohne Kinder: ein gültiger Block, der aber von der Haupt-Bitcoin-Kette ausgeschlossen ist. Er entsteht, wenn zwei Miner innerhalb kurzer Zeit einen gültigen Block auf der gleichen Kettenhöhe finden und ihn über das Netzwerk verbreiten. Die Knoten wählen schließlich nur einen Block aus, der in die Kette aufgenommen wird, nach dem Prinzip der Kette mit der meisten angesammelten Arbeit, wodurch der andere "obsolet" wird. Der Prozess, der zur Erzeugung eines veralteten Blocks führt, ist folgendermaßen:


- Zwei Schürfer finden innerhalb eines kurzen Zeitintervalls einen gültigen Block auf der gleichen Kettenhöhe. Nennen wir sie `Block A` und `Block B`;
- Jeder sendet seinen Block an das Bitcoin-Knotennetzwerk. Jeder Knoten hat nun 2 Blöcke in der gleichen Höhe. Daher gibt es zwei gültige Ketten;
- Die Schürfer suchen weiter nach Arbeitsnachweisen für die folgenden Blöcke, müssen aber zwangsläufig nur einen Block zwischen Block A und Block B auswählen, auf dem sie schürfen;
- Ein Schürfer findet schließlich einen gültigen Block oberhalb von "Block B". Nennen wir ihn `Block B+1`;
- Sie senden "Block B+1" an die Netzknoten;
- Da die Knoten der längsten Kette (mit der meisten angesammelten Arbeit) folgen, schätzen sie, dass die "Kette B" diejenige ist, der man folgen sollte;
- Sie werden Block A aufgeben, der nicht mehr Teil der Hauptkette ist. Er ist somit ein veralteter Block geworden.



