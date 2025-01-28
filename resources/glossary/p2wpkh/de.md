---
term: P2WPKH

---
P2WPKH steht für *Pay to Witness Public Key Hash*. Es ist ein Standard-Skriptmodell, das verwendet wird, um die Ausgabenbedingungen auf einem UTXO festzulegen. P2WPKH wurde mit der Einführung von SegWit im August 2017 eingeführt.

Dieses Skript ähnelt P2PKH (*Pay to Public Key Hash*), da es ebenfalls Bitcoins auf der Grundlage des Hashes eines öffentlichen Schlüssels, d. h. einer Empfängeradresse, sperrt. Der Unterschied liegt darin, wie Signaturen und Skripte in die Transaktion einbezogen werden. Im Fall von P2WPKH werden die Informationen zum Signaturskript (`scriptSig`) aus der traditionellen Transaktionsstruktur in einen separaten Abschnitt namens `Witness` verschoben. Diese Verschiebung ist ein Merkmal des SegWit (*Segregated Witness*) Updates, das dazu beiträgt, die Verfälschung von Signaturen zu verhindern. P2WPKH-Transaktionen sind im Allgemeinen billiger als Legacy-Transaktionen, da der Teil des Zeugen weniger kostet.

P2WPKH-Adressen werden in "Bech32"-Kodierung mit einer Prüfsumme in Form von BCH-Code geschrieben. Diese Adressen beginnen immer mit "bc1q". P2WPKH ist eine SegWit-Ausgabe der Version 0.