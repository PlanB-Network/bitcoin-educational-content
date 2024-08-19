---
term: P2WPKH
---

P2WPKH steht für *Pay to Witness Public Key Hash*. Es handelt sich um ein standardisiertes Skriptmodell, das verwendet wird, um Ausgabebedingungen für ein UTXO festzulegen. P2WPKH wurde mit der Implementierung von SegWit im August 2017 eingeführt.

Dieses Skript ähnelt P2PKH (*Pay to Public Key Hash*), da es ebenfalls Bitcoins basierend auf dem Hash eines öffentlichen Schlüssels, also einer Empfangsadresse, sperrt. Der Unterschied liegt darin, wie Signaturen und Skripte in die Transaktion einbezogen werden. Im Fall von P2WPKH werden die Informationen des Signaturskripts (`scriptSig`) von der traditionellen Transaktionsstruktur in einen separaten Abschnitt namens `Witness` verschoben. Diese Verschiebung ist ein Merkmal des SegWit (*Segregated Witness*) Updates, das dazu beiträgt, die Signaturveränderlichkeit zu verhindern. P2WPKH-Transaktionen sind im Allgemeinen kostengünstiger in Bezug auf die Gebühren im Vergleich zu Legacy-Transaktionen, da der Teil im Witness weniger kostet.

P2WPKH-Adressen werden unter Verwendung der `Bech32`-Kodierung mit einer Prüfsumme in Form des BCH-Codes geschrieben. Diese Adressen beginnen immer mit `bc1q`. P2WPKH ist eine Version 0 SegWit-Ausgabe.