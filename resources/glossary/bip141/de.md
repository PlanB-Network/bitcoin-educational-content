---
term: BIP141

---
Einführung des Konzepts von Segregated Witness (SegWit), das der SegWit-Soft-Fork ihren Namen gab. BIP141 führt eine wichtige Änderung des Bitcoin-Protokolls ein, um das Problem der Fälschbarkeit von Transaktionen zu lösen. SegWit trennt den Zeugen (Signaturdaten) vom Rest der Transaktionsdaten. Diese Trennung wird dadurch erreicht, dass die Zeugen in eine separate Datenstruktur eingefügt werden, die in einem neuen Merkle-Baum übertragen wird, auf den wiederum im Block über die Coinbase-Transaktion verwiesen wird, wodurch SegWit mit älteren Versionen des Protokolls kompatibel ist.