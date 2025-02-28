---
term: OP_NOP (0X61)

---
Hat keine Auswirkungen auf den Stapel oder den Zustand des Skripts. Es führt keine Bewegungen, Prüfungen oder Änderungen durch. Es tut einfach nichts, es sei denn, es wird über eine Soft Fork anders entschieden. Seit ihrer Änderung durch Satoshi Nakamoto im Jahr 2010 werden die `OP_NOP`-Befehle (`OP_NOP1` (`0XB0`) bis `OP_NOP10` (`0XB9`)) verwendet, um neue Opcodes in Form eines Soft Forks hinzuzufügen.

So wurden `OP_NOP2` (`0XB1`) und `OP_NOP3` (`0XB2`) bereits zur Implementierung von `OP_CHECKLOCKTIMEVERIFY` bzw. `OP_CHECKSEQUENCEVERIFY` verwendet. Sie werden in Kombination mit `OP_DROP` verwendet, um die zugehörigen zeitlichen Werte vom Stack zu entfernen und so die Ausführung des Skripts fortzusetzen, unabhängig davon, ob der Knoten aktuell ist oder nicht. Die `OP_NOP`-Befehle ermöglichen es daher, einen Unterbrechungspunkt in ein Skript einzufügen, um zusätzliche Bedingungen zu prüfen, die bereits vorhanden sind oder mit zukünftigen Soft Forks hinzugefügt werden können. Seit Tapscript ist die Verwendung von `OP_NOP` durch das effizientere `OP_SUCCESS` ersetzt worden.