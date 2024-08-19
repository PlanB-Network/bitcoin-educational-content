---
term: OP_CHECKSEQUENCEVERIFY (0XB2)
---

Macht die Transaktion ungültig, wenn eine dieser Eigenschaften beobachtet wird:
* Der Stapel ist leer;
* Der Wert an der Spitze des Stapels ist kleiner als `0`;
* Das Deaktivierungsflag für den Wert an der Spitze des Stapels ist undefiniert und; Die Transaktionsversion ist kleiner als `2` oder; Das Deaktivierungsflag für das `nSequence`-Feld des Eingangs ist gesetzt oder; Der Zeitverriegelungstyp ist nicht derselbe zwischen dem `nSequence`-Feld und dem Wert an der Spitze des Stapels (Echtzeit oder Anzahl der Blöcke) oder; Der Wert an der Spitze des Stapels ist größer als der Wert des `nSequence`-Feldes des Eingangs.

Wenn eine oder mehrere dieser Eigenschaften beobachtet werden, kann das Skript, das das `OP_CHECKSEQUENCEVERIFY` enthält, nicht erfüllt werden. Wenn alle Bedingungen gültig sind, dann wirkt `OP_CHECKSEQUENCEVERIFY` wie ein `OP_NOP`, was bedeutet, dass es keine Aktion im Skript durchführt. Es ist, als ob es verschwindet. `OP_CHECKSEQUENCEVERIFY` legt somit eine relative Zeitbeschränkung für die Ausgabe des UTXO fest, das mit dem Skript gesichert ist, das es enthält. Dies kann entweder in Form von Echtzeit oder als Anzahl von Blöcken geschehen. Dazu beschränkt es die möglichen Werte für das `nSequence`-Feld des Eingangs, der es ausgibt, und dieses `nSequence`-Feld selbst beschränkt, wann die Transaktion, die diesen Eingang enthält, in einem Block aufgenommen werden kann.

> ► *Dieser Opcode ist ein Ersatz für `OP_NOP`. Er wurde auf `OP_NOP3` platziert. Oft wird er mit seinem Akronym "CSV" bezeichnet. Beachten Sie, `OP_CSV` sollte nicht mit dem `nSequence`-Feld einer Transaktion verwechselt werden. Das Erstere verwendet das Letztere, aber ihre Naturen und Aktionen sind unterschiedlich.*