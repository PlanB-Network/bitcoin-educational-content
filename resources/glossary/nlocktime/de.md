---
term: NLOCKTIME

---
Ein in Transaktionen eingebettetes Feld, das eine zeitbasierte Bedingung festlegt, vor der die Transaktion nicht zu einem gültigen Block hinzugefügt werden kann. Mit diesem Parameter kann eine genaue Zeit (Unix-Zeitstempel) oder eine bestimmte Anzahl von Blöcken als Bedingung dafür angegeben werden, dass die Transaktion als gültig gilt. Es handelt sich also um ein absolutes Timelock (nicht relativ). Die `nLockTime` wirkt sich auf die gesamte Transaktion aus und ermöglicht effektiv eine Zeitüberprüfung, während der Opcode `OP_CHECKLOCKTIMEVERIFY` nur den Vergleich des obersten Wertes auf dem Stack mit dem `nLockTime`-Wert ermöglicht.