---
term: OP_CHECKSEQUENCEVERIFY (0XB2)

---
Macht die Transaktion ungültig, wenn eines dieser Merkmale beobachtet wird:


- Der Stapel ist leer;
- Der Wert an der Spitze des Stapels ist kleiner als "0";
- Das Sperrkennzeichen für den Wert an der Spitze des Stapels ist undefiniert und; Die Transaktionsversion ist kleiner als "2" oder; Das Sperrkennzeichen für das Feld "nSequence" des Eingangs ist gesetzt oder; Der Zeitsperrtyp ist nicht derselbe wie der des Feldes "nSequence" und des Wertes an der Spitze des Stapels (Echtzeit oder Anzahl der Blöcke) oder; Der Wert an der Spitze des Stapels ist größer als der Wert des Feldes "nSequence" des Eingangs.

Wenn eine oder mehrere dieser Bedingungen erfüllt sind, kann das Skript, das den `OP_CHECKSEQUENCEVERIFY` enthält, nicht erfüllt werden. Wenn alle Bedingungen erfüllt sind, verhält sich `OP_CHECKSEQUENCEVERIFY` wie ein `OP_NOP`, d.h. es führt keine Aktion an dem Skript aus. Es ist so, als ob es verschwindet. `OP_CHECKSEQUENCEVERIFY` erlegt also eine relative Zeitbeschränkung für die Ausgaben des UTXO auf, der mit dem Skript, das ihn enthält, gesichert ist. Dies kann entweder in Form von Echtzeit oder in Form einer Anzahl von Blöcken geschehen. Zu diesem Zweck schränkt es die möglichen Werte für das Feld "nSequence" der Eingabe ein, die es ausgibt, und dieses Feld "nSequence" selbst schränkt ein, wann die Transaktion, die diese Eingabe enthält, in einen Block aufgenommen werden kann.

> ► *Dieser Opcode ist ein Ersatz für `OP_NOP`. Er wurde auf `OP_NOP3` gesetzt. Er wird oft mit seinem Akronym "CSV" bezeichnet. Beachten Sie, dass `OP_CSV` nicht mit dem Feld `nSequence` einer Transaktion verwechselt werden sollte. Ersteres verwendet letzteres, aber ihre Natur und ihre Aktionen sind unterschiedlich.*