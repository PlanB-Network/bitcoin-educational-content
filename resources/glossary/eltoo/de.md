---
term: ELTOO
---

Ein allgemeines Protokoll für die zweiten Ebenen von Bitcoin, das definiert, wie das Eigentum an einem UTXO gemeinsam verwaltet wird. Eltoo wurde von Christian Decker, Rusty Russell und Olaoluwa Osuntokun entworfen, insbesondere um die Probleme zu lösen, die mit den Verhandlungsmechanismen von Lightning-Kanalzuständen verbunden sind, das heißt, zwischen Öffnen und Schließen. Die Eltoo-Architektur vereinfacht den Verhandlungsprozess, indem sie ein lineares Zustandsverwaltungssystem einführt und den etablierten strafbasierenden Ansatz durch eine flexiblere und weniger strafende Aktualisierungsmethode ersetzt. Dieses Protokoll erfordert die Verwendung eines neuen Typs von SigHash, der es ermöglicht, alle Eingaben in der Signatur einer Transaktion zu ignorieren. Dieser SigHash wurde zunächst `SIGHASH_NOINPUT` genannt, dann `SIGHASH_ANYPREVOUT` (*Any Previous Output*). Seine Implementierung ist in BIP118 geplant.

> ► *Eltoo wird manchmal auch als "LN-Symmetry" bezeichnet.*