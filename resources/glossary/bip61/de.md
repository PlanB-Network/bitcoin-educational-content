---
term: BIP61
---

Führte eine Ablehnungsnachricht im Kommunikationsprotokoll zwischen Knoten ein. Das Ziel von BIP61 ist es, einen Feedbackmechanismus hinzuzufügen, wenn ein Knoten eine Transaktion oder einen Block von einem anderen Knoten erhält, den er für ungültig hält. Diese Ablehnungsnachricht würde es einem Knoten ermöglichen, dem Sender den Grund für die Ablehnung zu signalisieren. Diese Art der Kommunikation sollte die Interoperabilität zwischen verschiedenen Clients und die Kommunikation zwischen Vollknoten und SPV-Clients verbessern. Die durch BIP61 eingeführten Funktionalitäten wurden jedoch ab der Version 0.20.0 von Bitcoin Core schließlich aufgegeben, da sie als unnötig angesehen wurden, während sie einen erhöhten Bandbreitenbedarf mit sich brachten.