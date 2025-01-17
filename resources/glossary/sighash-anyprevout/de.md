---
term: SIGHASH_ANYPREVOUT

---
Vorschlag für die Implementierung eines neuen SigHash Flag Modifiers in Bitcoin, eingeführt mit BIP118. sIGHASH_ANYPREVOUT" ermöglicht eine größere Flexibilität im Transaktionsmanagement, insbesondere für fortgeschrittene Anwendungen wie Zahlungskanäle im Lightning Network und das Eltoo-Update. Mit `SIGHASH_ANYPREVOUT` kann die Signatur nicht an einen bestimmten vorherigen UTXO (*Any Previous Output*) gebunden werden. In Kombination mit `SIGHASH_ALL` würde dies das Signieren aller Ausgaben einer Transaktion ermöglichen, aber keine der Eingaben. Dies würde die Wiederverwendung der Signatur für verschiedene Transaktionen ermöglichen, sofern bestimmte Bedingungen erfüllt sind.

> ► *Dieser SigHash-Modifikator SIGHASH_ANYPREVOUT ist von der Idee von SIGHASH_NOINPUT abgeleitet, die ursprünglich von Joseph Poon 2016 vorgeschlagen wurde, um sein Konzept des Lightning Network zu verbessern