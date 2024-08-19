---
term: SCHWIERIGKEITSZIEL
---

Der Schwierigkeitsfaktor, auch bekannt als Schwierigkeitsziel, ist ein Parameter, der im Konsensmechanismus durch Proof of Work (Proof of Work, PoW) bei Bitcoin verwendet wird. Das Ziel stellt einen numerischen Wert dar, der die Schwierigkeit für Miner bestimmt, ein spezifisches kryptografisches Problem, genannt Proof of Work, beim Erstellen eines neuen Blocks auf der Blockchain zu lösen.

Das Schwierigkeitsziel ist eine anpassbare 256-Bit (64 Bytes) Zahl, die eine Akzeptanzgrenze für das Hashing von Blockheadern bestimmt. Mit anderen Worten, damit ein Block gültig ist, muss der Hash seines Headers mit `SHA256d` (doppeltes `SHA256`) numerisch niedriger oder gleich dem Schwierigkeitsziel sein. Der Proof of Work besteht darin, das `Nonce`-Feld des Blockheaders oder die Coinbase-Transaktion so lange zu modifizieren, bis der resultierende Hash niedriger als der Zielwert ist.

Dieses Ziel wird alle 2016 Blöcke (ungefähr alle zwei Wochen) während eines Ereignisses namens "Anpassung" justiert. Der Schwierigkeitsfaktor wird basierend auf der Zeit, die es brauchte, um die vorherigen 2016 Blöcke zu minen, neu berechnet. Wenn die Gesamtzeit weniger als zwei Wochen beträgt, erhöht sich die Schwierigkeit, indem das Ziel nach unten angepasst wird. Wenn die Gesamtzeit mehr als zwei Wochen beträgt, verringert sich die Schwierigkeit, indem das Ziel nach oben angepasst wird. Das Ziel ist es, eine durchschnittliche Mining-Zeit von 10 Minuten pro Block zu halten. Diese Zeit zwischen jedem Block hilft, Teilungen des Bitcoin-Netzwerks zu verhindern, was zu einer Verschwendung von Rechenleistung führen würde. Das Schwierigkeitsziel findet sich in jedem Blockheader, innerhalb des `nBits`-Feldes. Da dieses Feld auf 32 Bits reduziert ist und das Ziel tatsächlich 256 Bits beträgt, wird das Ziel in ein weniger präzises wissenschaftliches Format komprimiert.

![](../../dictionnaire/assets/34.png)

> ► *Das Schwierigkeitsziel wird manchmal auch als "Schwierigkeitsfaktor" bezeichnet. In Erweiterung kann es mit seiner Kodierung in den Blockheadern mit dem Begriff "nBits" bezeichnet werden.*