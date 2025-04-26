---
term: MTP (MEDIAN DER VERGANGENEN ZEIT)

---
Dieses Konzept wird im Bitcoin-Protokoll verwendet, um eine Marge auf den Konsenszeitstempel des Netzwerks zu bestimmen. MTP ist definiert als der Median der Zeitstempel der letzten 11 geminten Blöcke. Die Verwendung dieses Indikators hilft, Unstimmigkeiten zwischen den Knoten über die genaue Zeit im Falle von Diskrepanzen zu vermeiden. MTP wurde ursprünglich verwendet, um die Gültigkeit der Zeitstempel von Blöcken im Vergleich zur Vergangenheit zu überprüfen. Seit BIP113 wird es auch als Referenz für die Netzwerkzeit verwendet, um die Gültigkeit von Time-Lock-Transaktionen zu überprüfen (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence` und `OP_CHECKSEQUENCEVERIFY`).