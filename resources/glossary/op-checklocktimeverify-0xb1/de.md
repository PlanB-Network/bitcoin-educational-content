---
term: OP_CHECKLOCKTIMEVERIFY (0XB1)
---

Macht die Transaktion ungültig, es sei denn, alle diese Bedingungen sind erfüllt:
* Der Stack ist nicht leer;
* Der Wert an der Spitze des Stacks ist größer oder gleich `0`;
* Der Typ des Zeitlocks ist zwischen dem `nLockTime`-Feld und dem Wert an der Spitze des Stacks gleich (Echtzeit oder Blocknummer);
* Das `nSequence`-Feld des Inputs ist nicht gleich `0xffffffff`;
* Der Wert an der Spitze des Stacks ist größer oder gleich dem Wert des `nLockTime`-Feldes der Transaktion.

Wenn eine dieser Bedingungen nicht erfüllt ist, kann das Skript, das `OP_CHECKLOCKTIMEVERIFY` enthält, nicht erfüllt werden. Wenn alle diese Bedingungen gültig sind, dann wirkt `OP_CHECKLOCKTIMEVERIFY` wie ein `OP_NOP`, was bedeutet, dass es keine Aktion im Skript ausführt. Es ist, als ob es verschwindet. `OP_CHECKLOCKTIMEVERIFY` legt somit eine Zeitbeschränkung für die Ausgabe des UTXO fest, der mit dem Skript gesichert ist, das es enthält. Dies kann entweder in Form eines Unix-Zeitdatums oder als Blocknummer geschehen. Dazu beschränkt es die möglichen Werte für das `nLockTime`-Feld der Transaktion, die es ausgibt, und dieses `nLockTime`-Feld selbst beschränkt, wann die Transaktion in einem Block enthalten sein kann.

> ► *Dieser Opcode ist ein Ersatz für `OP_NOP`. Er wurde auf `OP_NOP2` platziert. Er wird oft mit seinem Akronym "CLTV" bezeichnet. Beachten Sie, `OP_CLTV` sollte nicht mit dem `nLockTime`-Feld einer Transaktion verwechselt werden. Der erstere verwendet den letzteren, aber ihre Naturen und Aktionen sind unterschiedlich.*