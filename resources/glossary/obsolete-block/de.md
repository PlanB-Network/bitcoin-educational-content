---
term: OBSOLETE (BLOCK)
---

Bezieht sich auf einen Block ohne Kinder: ein gültiger Block, der jedoch aus der Haupt-Bitcoin-Kette ausgeschlossen ist. Dies tritt auf, wenn zwei Miner innerhalb eines kurzen Zeitraums einen gültigen Block auf derselben Kettenhöhe finden und im Netzwerk verbreiten. Knoten wählen letztendlich nur einen Block zur Aufnahme in die Kette aus, gemäß dem Prinzip der Kette mit der meisten angesammelten Arbeit, wodurch der andere "obsolet" wird. Der Prozess, der zur Produktion eines obsoleten Blocks führt, ist wie folgt:
* Zwei Miner finden innerhalb eines kurzen Zeitintervalls einen gültigen Block auf derselben Kettenhöhe. Nennen wir sie `Block A` und `Block B`;
* Jeder verbreitet seinen Block im Bitcoin-Knotennetzwerk. Jeder Knoten hat nun 2 Blöcke auf derselben Höhe. Daher gibt es zwei gültige Ketten;
* Miner setzen die Suche nach Arbeitsnachweisen für die folgenden Blöcke fort, müssen dazu aber notwendigerweise nur einen Block zwischen `Block A` und `Block B` wählen, auf dem sie minen werden;
* Ein Miner findet schließlich einen gültigen Block über `Block B`. Nennen wir ihn `Block B+1`;
* Sie verbreiten `Block B+1` an die Netzwerkknoten;
* Da die Knoten der längsten Kette folgen (mit der meisten angesammelten Arbeit), werden sie schätzen, dass die `Kette B` die zu verfolgende ist;
* Sie werden `Block A` aufgeben, der nicht länger Teil der Hauptkette ist. Er ist somit zu einem obsoleten Block geworden.

![](../../dictionnaire/assets/9.png)

> ► *Im Englischen wird dies als "Stale Block" bezeichnet. Im Französischen kann es auch "bloc périmé" oder "bloc abandonné" genannt werden. Obwohl ich dieser Verwendung nicht zustimme, verwenden einige Bitcoiner den Begriff "bloc orphelin", um das zu bezeichnen, was tatsächlich ein obsoleter Block ist.*