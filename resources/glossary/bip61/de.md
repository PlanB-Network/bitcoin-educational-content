---
term: BIP61

---
Einführung einer Ablehnungsnachricht in das Kommunikationsprotokoll zwischen den Knoten. Das Ziel von BIP61 ist es, einen Feedback-Mechanismus einzuführen, wenn ein Knoten eine Transaktion oder einen Block von einem anderen Knoten erhält, den er für ungültig hält. Diese Ablehnungsnachricht würde es einem Knoten ermöglichen, dem Absender den Grund für die Ablehnung mitzuteilen. Diese Art der Kommunikation sollte die Interoperabilität zwischen verschiedenen Clients und die Kommunikation zwischen Vollknoten und SPV-Clients verbessern. Die von BIP61 eingebrachten Funktionalitäten wurden schließlich ab Version 0.20.0 von Bitcoin Core aufgegeben, da sie als unnötig angesehen wurden, da sie einen erhöhten Bandbreitenbedarf mit sich brachten.