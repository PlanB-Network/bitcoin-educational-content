---
term: BIP143

---
Führt eine neue Methode zum Hashing der Transaktion für die Signaturprüfung in Post-SegWit-Skripten ein. Ziel ist es, redundante Operationen während der Überprüfung zu minimieren und den Wert der UTXOs in der Eingabe in die Signatur aufzunehmen. Damit werden zwei wesentliche Probleme des ursprünglichen Transaktions-Hashing-Algorithmus gelöst:


- Das quadratische Wachstum des Datenhashings mit der Anzahl der Unterschriften;
- Das Fehlen der Einbeziehung des Eingabewertes in die Signatur, was ein Risiko für Hardware-Wallets darstellte, insbesondere im Hinblick auf die Kenntnis der anfallenden Transaktionsgebühren.

Da das in BIP141 erläuterte SegWit-Update eine neue Form von Transaktionen einführt, deren Skript von alten Nodes nicht verifiziert wird, nutzt BIP143 die Gelegenheit, dieses Problem zu beheben, ohne dass eine Hard Fork erforderlich ist. Daher ist BIP143 Teil des SegWit Soft Forks.