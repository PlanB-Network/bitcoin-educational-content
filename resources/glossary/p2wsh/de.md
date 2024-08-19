---
term: P2WSH
---

P2WSH steht für *Pay to Witness Script Hash*. Es handelt sich um ein standardisiertes Skriptmodell, das verwendet wird, um Ausgabebedingungen für ein UTXO festzulegen. P2WSH wurde mit der Implementierung von SegWit im August 2017 eingeführt.

Dieses Skript ist ähnlich wie P2SH (*Pay to Public Script Hash*), da es ebenfalls Bitcoins auf Basis des Hashs eines Skripts sperrt. Der Unterschied liegt darin, wie Signaturen und Skripte in die Transaktion einbezogen werden. Um die Bitcoins auf diesem Skripttyp auszugeben, muss der Empfänger das ursprüngliche Skript, genannt `witnessScript` (entspricht `redeemScript`), zusammen mit den erforderlichen Signaturen bereitstellen. Dieser Mechanismus ermöglicht die Implementierung von komplexeren Ausgabebedingungen, wie z.B. Multisigs.

Im Kontext von P2WSH wird die Signaturskriptinformation (das `scriptWitness`, entspricht `scriptSig`) von der traditionellen Transaktionsstruktur in einen separaten Abschnitt namens `Witness` verschoben. Diese Verschiebung ist ein Merkmal des SegWit (*Segregated Witness*) Updates, das dazu beiträgt, die Signaturveränderlichkeit zu verhindern. P2WSH-Transaktionen sind im Allgemeinen kostengünstiger in Bezug auf Gebühren im Vergleich zu Legacy-Transaktionen, da der Teil im Witness weniger kostet.

P2WSH-Adressen werden unter Verwendung der `Bech32`-Kodierung mit einer Prüfsumme in Form des BCH-Codes geschrieben. Diese Adressen beginnen immer mit `bc1q`. P2WSH ist eine Version 0 SegWit-Ausgabe.