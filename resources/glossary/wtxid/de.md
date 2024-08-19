---
term: WTXID
---

Eine Erweiterung der traditionellen TXID, einschließlich Zeugendaten, die mit SegWit eingeführt wurden. Während die TXID ein Hash der Transaktionsdaten ohne den Zeugen ist, ist die WTXID der `SHA256d` der gesamten Transaktionsdaten, einschließlich des Zeugen. WTXIDs werden in einem separaten Merkle-Baum gespeichert, dessen Wurzel in der Coinbase-Transaktion platziert wird. Diese Trennung ermöglicht die Entfernung der Transaktionsveränderlichkeit der TXID.