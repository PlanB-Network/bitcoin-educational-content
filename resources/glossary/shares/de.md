---
term: ANTEILE

---
Im Zusammenhang mit Mining-Pools ist ein Anteil ein Indikator, der verwendet wird, um den Beitrag eines einzelnen Miners innerhalb des Pools zu quantifizieren. Dieses Maß dient als Grundlage für die Berechnung der Belohnung, die der Pool an jeden Schürfer weiterverteilt. Jeder Anteil entspricht einem Hash, der ein Schwierigkeitsziel erfüllt, das unter dem des Bitcoin-Netzwerks liegt.

Um dies mit einer Analogie zu erklären, betrachten Sie einen 20-seitigen Würfel. Nehmen wir an, dass bei Bitcoin der Arbeitsnachweis erfordert, eine Zahl kleiner als 3 zu würfeln, um einen Block zu validieren (d. h. ein Ergebnis von 1 oder 2 zu erzielen). Stellen Sie sich nun vor, dass innerhalb eines Mining-Pools das Schwierigkeitsziel für einen Anteil auf 10 festgelegt ist. Somit zählt für einen einzelnen Schürfer im Pool jeder Würfelwurf, der eine Zahl kleiner als 10 ergibt, als gültiger Anteil. Diese Anteile werden dann vom Schürfer an den Pool übermittelt, damit er seine Belohnung einfordern kann, auch wenn sie nicht einem gültigen Ergebnis für einen Bitcoin-Block entsprechen.

Für jeden berechneten Hash kann ein einzelner Schürfer in einem Pool drei verschiedene Szenarien erleben:


- Wenn der Hash-Wert größer oder gleich dem vom Pool festgelegten Schwierigkeitsziel für einen Anteil ist, dann ist dieser Hash-Wert unbrauchbar. Der Schürfer ändert dann seine Nonce, um einen neuen Hash zu versuchen: hash > Aktie > Block".
- Wenn der Hash niedriger ist als das Schwierigkeitsziel des Anteils, aber größer oder gleich dem Schwierigkeitsziel von Bitcoin, dann stellt dieser Hash einen gültigen Anteil dar, der jedoch nicht ausreicht, um einen Block zu validieren. Der Miner kann diesen Hash an seinen Pool senden, um die mit der Aktie verbundene Belohnung einzufordern: anteil > Hash > Block".
- Wenn der Hash niedriger ist als das Schwierigkeitsziel des Bitcoin-Netzwerks, wird er sowohl als gültiger Anteil als auch als gültiger Block betrachtet. Der Miner sendet diesen Hash an seinen Pool, der sich beeilt, ihn im Bitcoin-Netzwerk zu verbreiten. Dieser Hash wird auch als gültiger Anteil für den Miner gezählt: "Anteil > Block > Hash".

![](../../dictionnaire/assets/32.webp)

Dieses Anteilssystem wird verwendet, um die von jedem einzelnen Schürfer innerhalb eines Pools geleistete Arbeit zu schätzen, ohne dass alle von einem Schürfer generierten Hashes einzeln neu berechnet werden müssen, was für den Pool völlig ineffizient wäre.

Mining-Pools passen die Schwierigkeit der Anteile an, um die Verifizierungslast auszugleichen und sicherzustellen, dass jeder Schürfer, ob klein oder groß, etwa alle paar Sekunden Anteile einreicht. Dies ermöglicht eine genaue Berechnung der Hashrate jedes Schürfers und die Verteilung der Belohnungen entsprechend der gewählten Methode der Entschädigungsberechnung (PPS, PPLNS, TIDES...).

> ► *Im Französischen kann "shares" mit "Teil" übersetzt werden.*