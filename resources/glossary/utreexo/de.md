---
term: UTREEXO
---

Protokoll, das von Tadge Dryja entworfen wurde, um das UTXO-Set der Bitcoin-Knoten mittels eines Akkumulators zu komprimieren, der auf Merkle-Bäumen basiert. Im Gegensatz zum klassischen UTXO-Set, das erheblichen Speicherplatz benötigt, reduziert Utreexo den benötigten Speicher drastisch, indem nur die Wurzeln der Merkle-Bäume gespeichert werden. Dies ermöglicht es dem Knoten, die Existenz von UTXOs, die in Transaktionseingaben verwendet werden, zu verifizieren, ohne das komplette Set von UTXOs speichern zu müssen. Durch die Verwendung von Utreexo behält jeder Knoten nur einen kryptografischen Fingerabdruck, genannt Merkle-Wurzel. Wenn eine Transaktion durchgeführt wird, liefert der Benutzer die Eigentumsnachweise der UTXOs und die entsprechenden Merkle-Pfade. So kann der Knoten Transaktionen verifizieren, ohne das gesamte UTXO-Set speichern zu müssen. Nehmen wir ein Beispiel mit einem Diagramm, um diesen Mechanismus zu verstehen:

![](../../dictionnaire/assets/15.png)

In diesem Beispiel habe ich das UTXO-Set absichtlich auf 4 UTXOs reduziert, um das Verständnis zu erleichtern. In Wirklichkeit ist es wichtig, sich vorzustellen, dass es zum Zeitpunkt des Schreibens dieser Zeilen fast 140 Millionen UTXOs bei Bitcoin gibt. In diesem Diagramm müsste der Utreexo-Knoten nur die Merkle-Wurzel im RAM behalten. Wenn er eine Transaktion erhält, die UTXO Nr. 3 (in Schwarz) ausgibt, würde der Nachweis aus den folgenden Elementen bestehen:
* UTXO 3;
* HASH 4;
* HASH 1-2.

Mit diesen Informationen, die vom Transaktionssender übermittelt wurden, führt der Utreexo-Knoten die folgenden Überprüfungen durch:
* Er berechnet den Abdruck von UTXO 3, was ihm HASH 3 ergibt;
* Er verknüpft HASH 3 mit HASH 4;
* Er berechnet deren Abdruck, was ihm HASH 3-4 ergibt;
* Er verknüpft HASH 3-4 mit HASH 1-2;
* Er berechnet deren Abdruck, was ihm die Merkle-Wurzel ergibt.

Wenn die Merkle-Wurzel, die er durch seinen Prozess erhält, dieselbe ist wie die Merkle-Wurzel, die er in seinem RAM gespeichert hat, dann ist er überzeugt, dass UTXO Nr. 3 tatsächlich Teil des UTXO-Sets ist.
Diese Methode reduziert die RAM-Anforderungen für Betreiber von Vollknoten. Allerdings hat Utreexo Einschränkungen, einschließlich einer Zunahme der Blockgröße aufgrund zusätzlicher Nachweise und der potenziellen Abhängigkeit von Utreexo-Knoten von Bridge Nodes, um fehlende Nachweise zu erhalten. Bridge Nodes sind traditionelle Vollknoten, die die notwendigen Nachweise für Utreexo-Knoten bereitstellen und so eine vollständige Verifizierung ermöglichen. Dieser Ansatz bietet einen Kompromiss zwischen Effizienz und Dezentralisierung und macht die Validierung von Transaktionen für Benutzer mit begrenzten Ressourcen zugänglicher.