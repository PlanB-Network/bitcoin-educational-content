---
term: ELTOO

---
Ein allgemeines Protokoll für die zweiten Bitcoin-Schichten, das definiert, wie das Eigentum an einem UTXO gemeinsam verwaltet werden kann. Eltoo wurde von Christian Decker, Rusty Russell und Olaoluwa Osuntokun entwickelt, um insbesondere die Probleme zu lösen, die mit den Verhandlungsmechanismen der Lightning-Kanalzustände, d.h. zwischen Öffnen und Schließen, verbunden sind. Die Eltoo-Architektur vereinfacht den Verhandlungsprozess durch die Einführung eines linearen Zustandsverwaltungssystems, das den etablierten, auf Strafen basierenden Ansatz durch eine flexiblere und weniger strafende Aktualisierungsmethode ersetzt. Dieses Protokoll erfordert die Verwendung einer neuen Art von SigHash, die es erlaubt, alle Eingaben in der Signatur einer Transaktion zu ignorieren. Dieser SigHash wurde zunächst `SIGHASH_NOINPUT` genannt, dann `SIGHASH_ANYPREVOUT` (*Any Previous Output*). Seine Implementierung ist in BIP118 geplant.

> ► *Eltoo wird manchmal auch als "LN-Symmetrie" bezeichnet