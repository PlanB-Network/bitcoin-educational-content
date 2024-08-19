---
term: SHARES
---

Im Kontext von Mining-Pools ist ein Share (Anteil) ein Indikator, der verwendet wird, um den Beitrag eines einzelnen Miners innerhalb des Pools zu quantifizieren. Dieses Maß dient als Grundlage für die Berechnung der Belohnung, die der Pool an jeden Miner redistribuiert. Jeder Share entspricht einem Hash, der ein Schwierigkeitsziel erfüllt, das niedriger ist als das der Bitcoin-Netzwerk.

Um dies mit einer Analogie zu erklären, betrachten Sie einen 20-seitigen Würfel. Bei Bitcoin, nehmen wir an, dass der Proof of Work erfordert, eine Zahl kleiner als 3 zu würfeln, um einen Block zu validieren (das heißt, ein Ergebnis von 1 oder 2 zu erzielen). Stellen Sie sich nun vor, dass innerhalb eines Mining-Pools das Schwierigkeitsziel für einen Share auf 10 gesetzt ist. Somit zählt für einen einzelnen Miner im Pool jeder Würfelwurf, der eine Zahl kleiner als 10 ergibt, als ein gültiger Share. Diese Shares werden dann vom Miner an den Pool übermittelt, um ihre Belohnung zu beanspruchen, auch wenn sie kein gültiges Ergebnis für einen Block auf Bitcoin entsprechen.

Für jeden berechneten Hash kann ein einzelner Miner in einem Pool drei verschiedene Szenarien erleben:
* Wenn der Hashwert größer oder gleich dem vom Pool festgelegten Schwierigkeitsziel für einen Share ist, dann ist dieser Hash nutzlos. Der Miner ändert dann seinen Nonce, um einen neuen Hash zu versuchen: `hash > share > block`.
* Wenn der Hash niedriger als das Schwierigkeitsziel des Shares, aber größer oder gleich dem Schwierigkeitsziel von Bitcoin ist, dann stellt dieser Hash einen gültigen Share dar, der jedoch nicht ausreicht, um einen Block zu validieren. Der Miner kann diesen Hash an seinen Pool senden, um die mit dem Share verbundene Belohnung zu beanspruchen: `share > hash > block`.
* Wenn der Hash niedriger als das Schwierigkeitsziel des Bitcoin-Netzwerks ist, wird er sowohl als gültiger Share als auch als gültiger Block betrachtet. Der Miner übermittelt diesen Hash an seinen Pool, der sich beeilt, ihn im Bitcoin-Netzwerk zu verbreiten. Dieser Hash wird auch als gültiger Share für den Miner gezählt: `share > block > hash`.

![](../../dictionnaire/assets/32.png)

Dieses Share-System wird verwendet, um die von jedem einzelnen Miner innerhalb eines Pools geleistete Arbeit zu schätzen, ohne alle vom Miner generierten Hashes einzeln neu berechnen zu müssen, was für den Pool völlig ineffizient wäre.

Mining-Pools passen die Schwierigkeit von Shares an, um die Verifizierungslast auszugleichen und sicherzustellen, dass jeder Miner, ob klein oder groß, ungefähr alle paar Sekunden Shares einreicht. Dies ermöglicht eine genaue Berechnung der Hashrate jedes Miners und die Verteilung der Belohnungen gemäß der gewählten Methode der Entschädigungsberechnung (PPS, PPLNS, TIDES...).

> ► *Auf Französisch können "shares" als "part" übersetzt werden.*