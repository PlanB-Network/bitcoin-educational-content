---
term: VEREINFACHTE ZAHLUNGSPRÜFUNG

---
Methode, die es Light-Clients ermöglicht, Bitcoin-Transaktionen zu überprüfen, ohne die gesamte Blockchain herunterzuladen. Ein Knoten, der SPV verwendet, lädt nur die Blockheader herunter, die viel leichter sind als die vollständigen Blöcke. Wenn er eine Transaktion verifizieren muss, fordert der SPV-Knoten einen Merkle-Beweis von vollständigen Knoten an, um zu bestätigen, dass die Transaktion in einem bestimmten Block enthalten ist. Dieser Ansatz ist effizient für Geräte mit begrenzten Ressourcen, wie z. B. Smartphones, aber er impliziert eine Abhängigkeit von vollständigen Knoten, was die Sicherheit verringern und das erforderliche Vertrauen erhöhen kann.

> ► *Die Abkürzung "SPV" wird häufig für diese Methode verwendet