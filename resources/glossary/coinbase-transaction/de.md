---
term: COINBASE (TRANSAKTION)
---

Die Coinbase-Transaktion ist eine spezielle und einzigartige Transaktion, die in jedem Block der Bitcoin-Blockchain enthalten ist. Sie stellt die erste Transaktion eines Blocks dar und wird von dem Miner erstellt, der erfolgreich einen Header gefunden hat, der den Proof-of-Work (*Proof-of-Work*) validiert, das heißt, er ist kleiner oder gleich dem Zielwert.

Die Coinbase-Transaktion erfüllt hauptsächlich zwei Zwecke: Sie vergibt die Blockbelohnung an den Miner und fügt neue Einheiten von Bitcoins dem umlaufenden Geldangebot hinzu. Die Blockbelohnung, die den wirtschaftlichen Anreiz für Miner darstellt, sich am Proof-of-Work zu beteiligen, umfasst die angesammelten Gebühren für die Transaktionen, die im Block enthalten sind, und eine bestimmte Menge an neu geschaffenen Bitcoins ex nihilo (Blocksubvention). Diese Menge, die ursprünglich 2009 auf 50 Bitcoins pro Block festgelegt wurde, halbiert sich alle 210.000 Blöcke (ungefähr alle 4 Jahre) während eines Ereignisses, das als "Halving" bezeichnet wird.

Die Coinbase-Transaktion unterscheidet sich in mehrerer Hinsicht von regulären Transaktionen. Erstens hat sie keine Eingabe, was bedeutet, dass kein existierender Transaktionsausgang (UTXO) von ihr verbraucht wird. Weiterhin enthält das Signaturskript (`scriptSig`) für die Coinbase-Transaktion typischerweise ein beliebiges Feld, das die Einbindung zusätzlicher Daten, wie benutzerdefinierte Nachrichten oder Informationen zur Version der Mining-Software, ermöglicht. Schließlich unterliegen die durch die Coinbase-Transaktion generierten Bitcoins einer Reifezeit von 100 Blöcken (101 Bestätigungen), bevor sie ausgegeben werden können, um das potenzielle Ausgeben von nicht existenten Bitcoins im Falle einer Kettenreorganisation zu verhindern.

> ► *Es gibt keine Übersetzung für "Coinbase" auf Deutsch. Daher ist es akzeptiert, diesen Begriff direkt zu verwenden.*