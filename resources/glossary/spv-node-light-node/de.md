---
term: SPV-KNOTEN (LICHTKNOTEN)

---
Ein SPV-Knoten (*Simple Payment Verification*), manchmal auch "Light Node" genannt, ist ein leichtgewichtiger Client eines Bitcoin-Knotens, der es Nutzern ermöglicht, Transaktionen zu überprüfen, ohne die gesamte Blockchain speichern zu müssen. Stattdessen speichert ein SPV-Knoten nur die Blockheader und erhält Informationen über bestimmte Transaktionen, indem er bei Bedarf vollständige Knoten abfragt. Dieses Überprüfungsprinzip wird durch die Struktur der Transaktionen in Bitcoin-Blöcken ermöglicht, die in einem kryptografischen Akkumulator (Merkle-Baum) organisiert sind.

Dieser Ansatz ist vorteilhaft für Geräte mit begrenzten Ressourcen, wie z. B. Mobiltelefone. Allerdings sind SPV-Knoten bei der Verfügbarkeit von Informationen auf Vollknoten angewiesen, was ein zusätzliches Maß an Vertrauen und folglich eine geringere Sicherheit im Vergleich zu Vollknoten mit sich bringt. SPV-Knoten können Transaktionen nicht eigenständig validieren, aber sie können anhand von Merkle-Beweisen überprüfen, ob eine Transaktion in einem Block enthalten ist.