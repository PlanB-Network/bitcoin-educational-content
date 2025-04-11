---
term: BLOCK/REV*.DAT

---
Name der Dateien in Bitcoin Core, in denen die Informationen gespeichert sind, die benötigt werden, um die Änderungen, die durch zuvor hinzugefügte Blöcke am UTXO-Set vorgenommen wurden, potenziell rückgängig zu machen. Jede Datei wird durch eine eindeutige Nummer identifiziert, die die gleiche ist wie die blk*.dat-Datei, der sie entspricht. Die rev*.dat-Dateien enthalten die Umkehrdaten, die den in den blk*.dat-Dateien gespeicherten Blöcken entsprechen. Diese Daten sind im Wesentlichen eine Liste aller UTXOs, die als Eingänge in einem Block verwendet werden. Diese Umkehrdateien ermöglichen es dem Knoten, zu einem früheren Zustand zurückzukehren, falls eine Blockchain-Umstrukturierung dazu führt, dass zuvor validierte Blöcke verworfen werden.