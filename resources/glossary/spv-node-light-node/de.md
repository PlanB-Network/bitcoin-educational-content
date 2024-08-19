---
term: SPV NODE (LIGHT NODE)
---

Ein SPV (*Simple Payment Verification*) Node, manchmal auch "Light Node" genannt, ist ein leichtgewichtiger Client eines Bitcoin-Nodes, der es Benutzern ermöglicht, Transaktionen zu validieren, ohne die gesamte Blockchain speichern zu müssen. Stattdessen speichert ein SPV-Node nur die Blockheader und erhält Informationen über spezifische Transaktionen, indem er bei Bedarf vollständige Nodes abfragt. Dieses Verifizierungsprinzip wird durch die Struktur der Transaktionen in Bitcoin-Blöcken ermöglicht, die innerhalb eines kryptografischen Akkumulators (Merkle-Baum) organisiert sind.

Dieser Ansatz ist vorteilhaft für Geräte mit begrenzten Ressourcen, wie zum Beispiel Mobiltelefone. Allerdings sind SPV-Nodes auf vollständige Nodes für die Verfügbarkeit von Informationen angewiesen, was ein zusätzliches Vertrauensniveau impliziert und folglich weniger Sicherheit im Vergleich zu vollständigen Nodes bietet. SPV-Nodes können Transaktionen nicht autonom validieren, aber sie können überprüfen, ob eine Transaktion in einem Block enthalten ist, indem sie Merkle-Beweise konsultieren.