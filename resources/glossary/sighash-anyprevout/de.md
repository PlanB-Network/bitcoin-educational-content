---
term: SIGHASH_ANYPREVOUT
---

Vorschlag für die Implementierung eines neuen SigHash-Flag-Modifiers in Bitcoin, eingeführt mit BIP118. `SIGHASH_ANYPREVOUT` ermöglicht eine größere Flexibilität im Transaktionsmanagement, insbesondere für fortgeschrittene Anwendungen wie Zahlungskanäle im Lightning Network und das Eltoo-Update. Der `SIGHASH_ANYPREVOUT` ermöglicht es, dass die Signatur nicht an einen spezifischen vorherigen UTXO (*Any Previous Output*) gebunden ist. In Kombination mit `SIGHASH_ALL` verwendet, würde es erlauben, alle Ausgaben einer Transaktion zu signieren, aber keine der Eingaben. Dies würde die Wiederverwendung der Signatur für verschiedene Transaktionen ermöglichen, solange bestimmte festgelegte Bedingungen erfüllt sind.

> ► *Dieser SigHash-Modifier SIGHASH_ANYPREVOUT basiert auf der Idee von SIGHASH_NOINPUT, die ursprünglich 2016 von Joseph Poon vorgeschlagen wurde, um sein Konzept des Lightning Networks zu verbessern.*