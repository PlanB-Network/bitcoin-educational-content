---
term: OP_ROLL (0X7A)
---

Verschiebt ein Element vom Stapel an die Spitze des Stapels, basierend auf der Tiefe, die durch den Wert an der Spitze des Stapels vor der Operation angegeben wird. Wenn beispielsweise der Wert an der Spitze des Stapels `4` ist, wird `OP_ROLL` das vierte Element von oben auf dem Stapel auswählen und diesen Wert an die Spitze verschieben. `OP_ROLL` erfüllt die gleiche Funktion wie `OP_PICK`, entfernt jedoch das Element aus seiner ursprünglichen Position.