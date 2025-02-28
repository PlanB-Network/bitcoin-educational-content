---
term: TRANSAKTION (TX)

---
Im Zusammenhang mit Bitcoin ist eine Transaktion (abgekürzt "TX") ein in der Blockchain aufgezeichneter Vorgang, der das Eigentum an Bitcoins von einem oder mehreren Inputs auf einen oder mehrere Outputs überträgt. Jede Transaktion verbraucht Unspent Transaction Outputs (UTXOs) als Inputs, d. h. Outputs aus früheren Transaktionen, und erzeugt neue UTXOs als Outputs, die als Inputs in zukünftigen Transaktionen verwendet werden können.

Jede Eingabe enthält einen Verweis auf eine bestehende Ausgabe zusammen mit einem Signaturskript (`scriptSig`), das die Ausgabebedingungen (`scriptPubKey`) erfüllt, die durch die Ausgabe, auf die es verweist, festgelegt wurden. Dadurch können Bitcoins freigeschaltet werden. Die Ausgaben definieren neue Ausgabebedingungen (`scriptPubKey`) für die übertragenen Bitcoins, oft in Form eines öffentlichen Schlüssels oder einer Adresse, mit der die Bitcoins nun verbunden sind.