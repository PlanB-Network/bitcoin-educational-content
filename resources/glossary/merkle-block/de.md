---
term: MERKLE BLOCK

---
Eine Datenstruktur, die im Zusammenhang mit BIP37 (*Transaction Bloom Filtering*) verwendet wird, um einen kompakten Nachweis für die Aufnahme bestimmter Transaktionen in einen Block zu liefern. Sie wird vor allem für SPV-Wallets verwendet. Der Merkle-Block enthält die Block-Header, gefilterte Transaktionen und einen partiellen Merkle-Baum, so dass Light-Clients schnell überprüfen können, ob eine Transaktion zu einem Block gehört, ohne alle Transaktionen herunterladen zu müssen.