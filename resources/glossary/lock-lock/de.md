---
term: LOCK (.LOCK)
---

Datei, die in Bitcoin Core verwendet wird, um das Datenverzeichnis zu sperren. Sie wird erstellt, wenn bitcoind oder Bitcoin-qt startet, um zu verhindern, dass mehrere Instanzen der Software gleichzeitig auf dasselbe Datenverzeichnis zugreifen. Das Ziel ist, Konflikte und Datenkorruption zu verhindern. Wenn die Software unerwartet stoppt, kann die .lock-Datei verbleiben und muss manuell gelöscht werden, bevor Bitcoin Core neu gestartet wird.