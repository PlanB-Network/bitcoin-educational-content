---
term: TIMELOCK
---

Ein primitives Smart-Contract-Element, das es ermöglicht, eine zeitbasierte Bedingung festzulegen, die erfüllt sein muss, damit eine Transaktion einem Block hinzugefügt werden kann. Es gibt zwei Arten von Timelocks bei Bitcoin:
* Der absolute Timelock, der einen genauen Zeitpunkt angibt, vor dem die Transaktion nicht in einem Block enthalten sein kann;
* Der relative Timelock, der eine Verzögerung ab der Annahme einer vorherigen Transaktion festlegt.
Der Timelock kann entweder als Datum in Unix-Zeit ausgedrückt oder als Blocknummer definiert werden. Schließlich kann der Timelock auf einen Transaktionsausgang angewendet werden, indem ein spezifischer Opcode im Sperrskript verwendet wird (`OP_CHECKLOCKTIMEVERIFY` oder `OP_CHECKSEQUENCEVERIFY`), oder auf eine gesamte Transaktion, indem spezifische Transaktionsfelder verwendet werden (`nLockTime` oder `nSequence`).