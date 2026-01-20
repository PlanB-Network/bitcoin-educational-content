---
term: LOCK (.LOCK)

---
Datei, die in Bitcoin Core zum Sperren des Datenverzeichnisses verwendet wird. Sie wird beim Start von bitcoind oder Bitcoin-qt erstellt, um zu verhindern, dass mehrere Instanzen der Software gleichzeitig auf dasselbe Datenverzeichnis zugreifen. Das Ziel ist es, Konflikte und Datenkorruption zu verhindern. Wenn die Software unerwartet gestoppt wird, kann die .lock-Datei bestehen bleiben und muss manuell gelöscht werden, bevor Bitcoin Core neu gestartet wird.