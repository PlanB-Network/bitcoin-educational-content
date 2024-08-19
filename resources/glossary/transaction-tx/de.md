---
term: TRANSACTION (TX)
---

Im Kontext von Bitcoin ist eine Transaktion (abgekürzt als "TX") eine auf der Blockchain aufgezeichnete Operation, die das Eigentum an Bitcoins von einem oder mehreren Eingängen (Inputs) auf einen oder mehrere Ausgänge (Outputs) überträgt. Jede Transaktion verbraucht nicht ausgegebene Transaktionsausgänge (Unspent Transaction Outputs, UTXOs) als Eingänge, die Ausgänge aus vorherigen Transaktionen sind, und erzeugt neue UTXOs als Ausgänge, die in zukünftigen Transaktionen als Eingänge verwendet werden können.

Jeder Eingang enthält einen Verweis auf einen bestehenden Ausgang zusammen mit einem Signaturskript (`scriptSig`), das die durch den Ausgang, auf den er sich bezieht, festgelegten Ausgabebedingungen (`scriptPubKey`) erfüllt. Dies ermöglicht es, Bitcoins freizuschalten. Die Ausgänge definieren neue Ausgabebedingungen (`scriptPubKey`) für die übertragenen Bitcoins, oft in Form eines öffentlichen Schlüssels oder einer Adresse, mit der die Bitcoins nun assoziiert sind.