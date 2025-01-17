---
term: OP_CHECKLOCKTIMEVERIFY (0XB1)

---
Macht die Transaktion ungültig, wenn nicht alle diese Bedingungen erfüllt sind:


- Der Stapel ist nicht leer;
- Der Wert an der Spitze des Stapels ist größer oder gleich `0`;
- Der Typ der Zeitsperre ist derselbe wie das Feld "nLockTime" und der Wert an der Spitze des Stapels (Echtzeit oder Blocknummer);
- Das Feld "nSequence" der Eingabe ist ungleich "0xffffffff";
- Der Wert an der Spitze des Stapels ist größer oder gleich dem Wert des Feldes "nLockTime" der Transaktion.

Wenn eine dieser Bedingungen nicht erfüllt ist, kann das Skript, das die `OP_CHECKLOCKTIMEVERIFY` enthält, nicht erfüllt werden. Wenn alle diese Bedingungen erfüllt sind, dann verhält sich `OP_CHECKLOCKTIMEVERIFY` wie ein `OP_NOP`, d.h. es führt keine Aktion an dem Skript aus. Es ist so, als ob es verschwindet. oP_CHECKLOCKTIMEVERIFY" erlegt somit eine zeitliche Beschränkung für die Ausgabe des UTXO auf, das mit dem Skript, das es enthält, gesichert ist. Es kann dies entweder in Form eines Unix-Zeitdatums oder einer Blocknummer tun. Zu diesem Zweck schränkt es die möglichen Werte für das Feld "nLockTime" der Transaktion ein, die es ausgibt, und dieses Feld "nLockTime" selbst schränkt ein, wann die Transaktion in einen Block aufgenommen werden kann.

> ► *Dieser Opcode ist ein Ersatz für `OP_NOP`. Er wurde auf `OP_NOP2` gesetzt. Er wird oft mit seinem Akronym "CLTV" bezeichnet. Beachten Sie, dass `OP_CLTV` nicht mit dem Feld `nLockTime` einer Transaktion verwechselt werden sollte. Ersteres verwendet letzteres, aber ihre Natur und ihre Aktionen sind unterschiedlich.*