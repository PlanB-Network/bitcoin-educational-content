---
term: OP_IF (0X63)

---
Führt den folgenden Teil des Skripts aus, wenn der Wert an der Spitze des Stapels ungleich Null ist (true). Ist der Wert Null (false), werden diese Operationen übersprungen und es wird direkt zu den Operationen nach `OP_ELSE` übergegangen, falls dieses vorhanden ist. `OP_IF` ermöglicht den Start einer bedingten Kontrollstruktur innerhalb eines Skripts. Es bestimmt den Kontrollfluss in einem Skript auf der Grundlage einer Bedingung, die zum Zeitpunkt der Ausführung der Transaktion gegeben ist. `OP_IF` wird in Verbindung mit `OP_ELSE` und `OP_ENDIF` wie folgt verwendet:

```text
<condition>
OP_IF
<operations if the condition is true>
OP_ELSE
<operations if the condition is false>
OP_ENDIF
```