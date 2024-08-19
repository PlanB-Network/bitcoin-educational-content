---
term: OP_NOP (0X61)
---

Hat keine Auswirkung auf den Stapel oder den Zustand des Skripts. Es führt keine Bewegungen, Überprüfungen oder Modifikationen durch. Es tut einfach nichts, es sei denn, es wird anders durch einen Soft Fork entschieden. Tatsächlich werden seit ihrer Modifikation durch Satoshi Nakamoto im Jahr 2010 die `OP_NOP` Befehle (`OP_NOP1` (`0XB0`) bis `OP_NOP10` (`0XB9`)) verwendet, um neue Opcodes in Form eines Soft Forks hinzuzufügen.

So wurden `OP_NOP2` (`0XB1`) und `OP_NOP3` (`0XB2`) bereits verwendet, um `OP_CHECKLOCKTIMEVERIFY` und `OP_CHECKSEQUENCEVERIFY` zu implementieren. Sie werden in Kombination mit `OP_DROP` verwendet, um die zugehörigen zeitlichen Werte vom Stapel zu entfernen, wodurch die Ausführung des Skripts fortgesetzt werden kann, unabhängig davon, ob der Knoten auf dem neuesten Stand ist oder nicht. Die `OP_NOP` Befehle ermöglichen daher das Einfügen eines Unterbrechungspunktes in ein Skript, um nach zusätzlichen Bedingungen zu prüfen, die bereits existieren oder mit zukünftigen Soft Forks hinzugefügt werden können. Seit Tapscript wurde die Verwendung von `OP_NOP` durch das effizientere `OP_SUCCESS` ersetzt.