---
term: COINBASE (TRANSAKTION)

---
Die Coinbase-Transaktion ist eine spezielle und einzigartige Transaktion, die in jedem Block der Bitcoin-Blockchain enthalten ist. Sie stellt die erste Transaktion eines Blocks dar und wird von dem Miner erstellt, der erfolgreich einen Header gefunden hat, der den Proof of Work (*Proof-of-Work*) validiert, d.h. kleiner oder gleich dem Zielwert ist.

Die Coinbase-Transaktion dient in erster Linie zwei Zwecken: der Vergabe der Blockbelohnung an den Miner und der Zuführung neuer Bitcoin-Einheiten zur zirkulierenden Geldmenge. Die Blockbelohnung, die den wirtschaftlichen Anreiz für Miner darstellt, sich am Proof of Work zu beteiligen, umfasst die kumulierten Gebühren für die im Block enthaltenen Transaktionen und eine bestimmte Menge neu geschaffener Bitcoins ex nihilo (Blocksubvention). Dieser Betrag, der 2009 ursprünglich auf 50 Bitcoins pro Block festgesetzt wurde, wird alle 210.000 Blöcke (etwa alle 4 Jahre) im Rahmen eines "Halving" genannten Ereignisses halbiert

Die Coinbase-Transaktion unterscheidet sich in mehrfacher Hinsicht von regulären Transaktionen. Erstens hat sie keinen Input, d.h. es wird kein bestehender Transaktions-Output (UTXO) von ihr verbraucht. Zum anderen enthält das Signaturskript (`scriptSig`) für die coinbase-Transaktion in der Regel ein beliebiges Feld, in das zusätzliche Daten, wie z. B. benutzerdefinierte Nachrichten oder Versionsinformationen der Mining-Software, eingefügt werden können. Schließlich unterliegen die durch die coinbase-Transaktion generierten Bitcoins einer Reifezeit von 100 Blöcken (101 Bestätigungen), bevor sie ausgegeben werden können, um zu verhindern, dass im Falle einer Reorganisation der Kette möglicherweise nicht vorhandene Bitcoins ausgegeben werden.

> *Es gibt keine Übersetzung für "Coinbase" im Französischen. Daher ist es zulässig, diesen Begriff direkt zu verwenden.*