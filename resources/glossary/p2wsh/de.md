---
term: P2WSH

---
P2WSH steht für *Pay to Witness Script Hash*. Es ist ein Standard-Skriptmodell, das verwendet wird, um Ausgabenbedingungen für einen UTXO festzulegen. P2WSH wurde mit der Einführung von SegWit im August 2017 eingeführt.

Dieses Skript ähnelt P2SH (*Pay to Public Script Hash*), da es ebenfalls Bitcoins auf der Grundlage des Hashes eines Skripts sperrt. Der Unterschied liegt darin, wie Signaturen und Skripte in die Transaktion einbezogen werden. Um die Bitcoins für diese Art von Skript auszugeben, muss der Empfänger das ursprüngliche Skript, genannt `witnessScript` (entspricht `redeemScript`), zusammen mit den erforderlichen Signaturen bereitstellen. Dieser Mechanismus ermöglicht die Implementierung von anspruchsvolleren Ausgabenbedingungen, wie z.B. Multisigs.

Im Zusammenhang mit P2WSH wird die Information über das Signaturskript (`scriptWitness`, äquivalent zu `scriptSig`) von der traditionellen Transaktionsstruktur in einen separaten Abschnitt namens `Witness` verschoben. Diese Verlagerung ist ein Merkmal des SegWit (*Segregated Witness*) Updates, das hilft, die Verfälschung von Signaturen zu verhindern. P2WSH-Transaktionen sind im Allgemeinen billiger als Legacy-Transaktionen, da der Teil des Zeugen weniger kostet.

P2WSH-Adressen werden in der Kodierung "Bech32" mit einer Prüfsumme in Form von BCH-Code geschrieben. Diese Adressen beginnen immer mit "bc1q". P2WSH ist eine SegWit-Ausgabe der Version 0.