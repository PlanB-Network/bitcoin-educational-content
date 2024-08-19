---
term: NLOCKTIME
---

Ein eingebettetes Feld in Transaktionen, das eine zeitbasierte Bedingung festlegt, bevor die Transaktion einem gültigen Block hinzugefügt werden kann. Dieser Parameter ermöglicht es, eine genaue Zeit (Unix-Zeitstempel) oder eine spezifische Anzahl von Blöcken als Bedingung dafür anzugeben, dass die Transaktion als gültig betrachtet wird. Somit handelt es sich um eine absolute Zeitverriegelung (nicht relativ). Das `nLockTime` betrifft die gesamte Transaktion und ermöglicht effektiv eine Zeitüberprüfung, während der Opcode `OP_CHECKLOCKTIMEVERIFY` nur den Vergleich des obersten Werts des Stacks mit dem `nLockTime`-Wert zulässt.