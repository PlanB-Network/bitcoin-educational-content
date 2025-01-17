---
term: SCHWIERIGKEITSZIEL

---
Der Schwierigkeitsfaktor, auch bekannt als Schwierigkeitsziel, ist ein Parameter, der im Konsensmechanismus des Arbeitsnachweises (Proof of Work, PoW) auf Bitcoin verwendet wird. Das Ziel stellt einen numerischen Wert dar, der die Schwierigkeit für Miner bestimmt, ein bestimmtes kryptographisches Problem, genannt Proof of Work, zu lösen, wenn ein neuer Block auf der Blockchain erstellt wird.

Das Schwierigkeitsziel ist eine einstellbare 256-Bit-Zahl (64 Bytes), die eine Akzeptanzgrenze für das Hashing von Block-Headern festlegt. Mit anderen Worten, damit ein Block gültig ist, muss der Hash seines Headers mit `SHA256d` (doppelter `SHA256`) numerisch kleiner oder gleich dem Schwierigkeitsziel sein. Der Arbeitsnachweis besteht darin, das Feld `nonce` des Block-Headers oder der Coinbase-Transaktion so lange zu verändern, bis der resultierende Hash-Wert kleiner als der Zielwert ist.

Dieses Ziel wird alle 2016er Blöcke (etwa alle zwei Wochen) während eines Ereignisses namens "Anpassung" angepasst Der Schwierigkeitsfaktor wird auf der Grundlage der Zeit, die für den Abbau der vorherigen 2016er Blöcke benötigt wurde, neu errechnet. Beträgt die Gesamtzeit weniger als zwei Wochen, erhöht sich der Schwierigkeitsgrad, indem das Ziel nach unten angepasst wird. Beträgt die Gesamtzeit mehr als zwei Wochen, sinkt die Schwierigkeit, indem der Zielwert nach oben angepasst wird. Ziel ist es, eine durchschnittliche Abbauzeit von 10 Minuten pro Block einzuhalten. Diese Zeit zwischen den einzelnen Blöcken hilft zu verhindern, dass das Bitcoin-Netzwerk geteilt wird, was eine Verschwendung von Rechenleistung zur Folge hätte. Das Schwierigkeitsziel befindet sich in jedem Block-Header im Feld "nBits". Da dieses Feld auf 32 Bits reduziert ist und das Ziel eigentlich 256 Bits beträgt, wird das Ziel in ein weniger präzises wissenschaftliches Format verdichtet.

![](../../dictionnaire/assets/34.webp)

> ► *Das Schwierigkeitsziel wird manchmal auch als "Schwierigkeitsfaktor" bezeichnet Im weiteren Sinne kann es mit seiner Kodierung in den Blockheadern mit dem Begriff "nBits" bezeichnet werden