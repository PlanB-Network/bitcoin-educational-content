---
term: BLOCKS/REV*.DAT
---

Name der Dateien in Bitcoin Core, die die Informationen speichern, die benötigt werden, um die Änderungen am UTXO-Set, die durch zuvor hinzugefügte Blöcke gemacht wurden, potenziell rückgängig zu machen. Jede Datei wird durch eine einzigartige Nummer identifiziert, die der des entsprechenden blk*.dat-Files gleicht. Die rev*.dat-Dateien enthalten die Umkehrdaten, die den in den blk*.dat-Dateien gespeicherten Blöcken entsprechen. Diese Daten sind im Wesentlichen eine Liste aller UTXOs, die als Eingaben in einem Block ausgegeben wurden. Diese Umkehrdateien ermöglichen es dem Knoten, zu einem früheren Zustand zurückzukehren, falls es zu einer Blockchain-Reorganisation kommt, die dazu führt, dass zuvor validierte Blöcke verworfen werden.