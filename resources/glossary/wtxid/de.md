---
term: WTXID

---
Eine Erweiterung der traditionellen TXID, einschließlich der mit SegWit eingeführten Zeugendaten. Während die TXID ein Hash der Transaktionsdaten ohne den Zeugen ist, ist die WTXID der `SHA256d` der gesamten Transaktionsdaten, einschließlich des Zeugen. WTXIDs werden in einem separaten Merkle-Baum gespeichert, dessen Wurzel sich in der Coinbase-Transaktion befindet. Diese Trennung ermöglicht die Beseitigung der Transaktionsveränderlichkeit der TXID.