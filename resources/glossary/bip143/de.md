---
term: BIP143
---

Führt eine neue Methode des Hashings der Transaktion für die Signaturverifizierung in Post-SegWit-Skripten ein. Das Ziel ist es, redundante Operationen während der Verifizierung zu minimieren und den Wert der UTXOs im Input in die Signatur einzubeziehen. Dies löst zwei große Probleme mit dem ursprünglichen Transaktions-Hashing-Algorithmus:
* Das quadratische Wachstum des Datenhashings mit der Anzahl der Signaturen;
* Das Fehlen der Einbeziehung des Input-Wertes in die Signatur, was ein Risiko für Hardware-Wallets darstellte, insbesondere in Bezug auf das Wissen über die entstandenen Transaktionsgebühren.
Seit dem SegWit-Update, erklärt in BIP141, wird eine neue Form von Transaktionen eingeführt, deren Skript von alten Knoten nicht verifiziert wird, nutzt BIP143 diese Gelegenheit, um dieses Problem zu adressieren, ohne einen Hard Fork zu benötigen. Daher ist BIP143 Teil des SegWit-Soft-Forks.