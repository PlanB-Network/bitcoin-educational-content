---
term: UTREEXO

---
Von Tadge Dryja entwickeltes Protokoll zur Verdichtung der UTXO-Menge der Bitcoin-Knoten mithilfe eines auf Merkle-Bäumen basierenden Akkumulators. Im Gegensatz zum klassischen UTXO-Set, das viel Speicherplatz benötigt, reduziert Utreexo den benötigten Speicherplatz drastisch, indem nur die Wurzeln des Merkle-Baums gespeichert werden. Dadurch kann der Knoten das Vorhandensein von UTXOs, die in den Transaktionsinputs verwendet werden, verifizieren, ohne den kompletten Satz von UTXOs aufbewahren zu müssen. Durch die Verwendung von Utreexo speichert jeder Knoten nur einen kryptografischen Fingerabdruck, die sogenannte Merkle-Wurzel. Bei einer Transaktion liefert der Nutzer die Eigentumsnachweise für die UTXOs und die entsprechenden Merkle-Pfade. So kann der Knoten Transaktionen verifizieren, ohne den gesamten UTXO-Satz zu speichern. Nehmen wir ein Beispiel mit einem Diagramm, um diesen Mechanismus zu verstehen:

![](../../dictionnaire/assets/15.webp)

In diesem Beispiel habe ich den UTXO-Satz absichtlich auf 4 UTXOs reduziert, um das Verständnis zu erleichtern. In Wirklichkeit ist es wichtig, sich vorzustellen, dass es zum Zeitpunkt des Schreibens dieser Zeilen fast 140 Millionen UTXOs auf Bitcoin gibt. In diesem Diagramm müsste der Utreexo-Knoten nur die Merkle-Wurzel im RAM halten. Wenn er eine Transaktion erhält, die UTXO Nr. 3 (in schwarz) ausgibt, würde der Beweis aus den folgenden Elementen bestehen:


- UTXO 3;
- HASH 4;
- HASH 1-2.

Mit diesen vom Transaktionsabsender übermittelten Informationen führt der Utreexo-Knoten die folgenden Überprüfungen durch:


- Er berechnet den Abdruck von UTXO 3, was ihm HASH 3 gibt;
- Er verkettet HASH 3 mit HASH 4;
- Es errechnet ihr Impressum, das ihr HASH 3-4 gibt;
- Er verkettet HASH 3-4 mit HASH 1-2;
- Sie berechnet ihren Abdruck, der ihr die Merkle-Wurzel gibt.

Wenn die Merkle-Wurzel, die er durch seinen Prozess erhält, mit der Merkle-Wurzel übereinstimmt, die er in seinem RAM gespeichert hat, dann ist er davon überzeugt, dass UTXO Nr. 3 tatsächlich Teil des UTXO-Sets ist.

Diese Methode verringert die Anforderungen an den Arbeitsspeicher für vollständige Knotenbetreiber. Utreexo hat jedoch Einschränkungen, darunter eine Zunahme der Blockgröße aufgrund zusätzlicher Beweise und die potenzielle Abhängigkeit der Utreexo-Knoten von Bridge Nodes, um fehlende Beweise zu erhalten. Brückenknoten sind herkömmliche Vollknoten, die Utreexo-Knoten die erforderlichen Beweise liefern und so eine vollständige Überprüfung ermöglichen. Dieser Ansatz bietet einen Kompromiss zwischen Effizienz und Dezentralisierung und macht die Transaktionsvalidierung für Nutzer mit begrenzten Ressourcen leichter zugänglich.