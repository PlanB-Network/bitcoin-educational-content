---
term: MTP (MEDIAN TIME PAST)
---

Dieses Konzept wird im Bitcoin-Protokoll verwendet, um eine Marge beim Konsens-Zeitstempel des Netzwerks zu bestimmen. MTP wird definiert als der Median der Zeitstempel der letzten 11 abgebauten Blöcke. Die Verwendung dieses Indikators hilft, Meinungsverschiedenheiten zwischen Knoten über die genaue Zeit im Falle von Diskrepanzen zu vermeiden. MTP wurde ursprünglich verwendet, um die Gültigkeit von Blockzeitstempeln gegenüber der Vergangenheit zu überprüfen. Seit BIP113 wird es auch als Referenz für die Netzwerkzeit verwendet, um die Gültigkeit von Zeit-Schloss-Transaktionen (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence` und `OP_CHECKSEQUENCEVERIFY`) zu überprüfen.