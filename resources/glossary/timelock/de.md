---
term: TIMELOCK

---
Ein Smart-Contract-Primitiv, das es ermöglicht, eine zeitbasierte Bedingung festzulegen, die erfüllt sein muss, damit eine Transaktion zu einem Block hinzugefügt werden kann. Es gibt zwei Arten von Timelocks auf Bitcoin:


- Die absolute Zeitsperre, die einen genauen Zeitpunkt angibt, vor dem die Transaktion nicht in einen Block aufgenommen werden kann;
- Die relative Zeitsperre, die eine Verzögerung bei der Annahme einer früheren Transaktion festlegt.

Die Zeitsperre kann entweder als Datum, ausgedrückt in Unix-Zeit, oder als Blocknummer definiert werden. Schließlich kann die Zeitsperre für eine Transaktionsausgabe gelten, indem ein bestimmter Opcode im Sperrskript verwendet wird (`OP_CHECKLOCKTIMEVERIFY` oder `OP_CHECKSEQUENCEVERIFY`), oder für eine gesamte Transaktion, indem bestimmte Transaktionsfelder verwendet werden (`nLockTime` oder `nSequence`).