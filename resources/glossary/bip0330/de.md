---
term: BIP0330
---

Ein als "*Erlay*" bekannter Vorschlag, der darauf abzielt, die Weiterleitung unbestätigter Transaktionen im Bitcoin-Netz zu optimieren. Derzeit werden Transaktionen an alle Peers eines Knotens gesendet, was zu Redundanz und übermäßiger Bandbreitennutzung führt. BIP330 schlägt vor, diese Übertragung standardmäßig auf 8 Peers zu beschränken und dann einen Versöhnungsmechanismus zu verwenden, um fehlende Transaktionen effizient zu teilen. Erlay reduziert den Bandbreitenverbrauch um etwa 40 %. Es vermeidet auch einen linearen Anstieg des Bandbreitenverbrauchs mit der Anzahl der mit dem Knoten verbundenen Peers.