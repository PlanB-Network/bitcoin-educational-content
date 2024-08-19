---
term: MERKLE BLOCK
---

Eine Datenstruktur, die im Kontext von BIP37 (*Transaction Bloom Filtering*) verwendet wird, um einen kompakten Nachweis der Einbeziehung spezifischer Transaktionen in einen Block zu liefern. Sie wird insbesondere für SPV-Wallets verwendet. Der Merkle Block enthält die Blockheader, gefilterte Transaktionen und einen partiellen Merkle-Baum, der es Leichtgewicht-Clients ermöglicht, schnell zu überprüfen, ob eine Transaktion zu einem Block gehört, ohne alle Transaktionen herunterladen zu müssen.