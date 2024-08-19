---
term: BIP141
---

Führte das Konzept von Segregated Witness (SegWit) ein, welches dem SegWit-Soft-Fork seinen Namen gab. BIP141 führt eine bedeutende Änderung im Bitcoin-Protokoll ein, die darauf abzielt, das Problem der Transaktionsmanipulierbarkeit zu lösen. SegWit trennt die Zeugendaten (Signaturdaten) vom Rest der Transaktionsdaten. Diese Trennung wird erreicht, indem die Zeugen in eine separate Datenstruktur eingefügt werden, die in einem neuen Merkle-Baum festgehalten wird, welcher selbst über die Coinbase-Transaktion im Block referenziert wird, wodurch SegWit mit älteren Versionen des Protokolls kompatibel ist.