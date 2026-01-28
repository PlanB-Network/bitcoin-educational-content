---
term: Sperre (.lock)

definition: Eine Datei, die verhindert, dass mehrere Instanzen von Bitcoin Core gleichzeitig auf dasselbe Verzeichnis zugreifen.
---
Datei, die in Bitcoin Core zum Sperren des Datenverzeichnisses verwendet wird. Sie wird beim Start von bitcoind oder Bitcoin-qt erstellt, um zu verhindern, dass mehrere Instanzen der Software gleichzeitig auf dasselbe Datenverzeichnis zugreifen. Das Ziel ist es, Konflikte und Datenkorruption zu verhindern. Wenn die Software unerwartet gestoppt wird, kann die .lock-Datei bestehen bleiben und muss manuell gelöscht werden, bevor Bitcoin Core neu gestartet wird.