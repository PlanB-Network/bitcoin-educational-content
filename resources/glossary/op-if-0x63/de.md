---
term: OP_IF (0X63)
---

Führt den folgenden Teil des Skripts aus, wenn der Wert an der Spitze des Stapels nicht Null (wahr) ist. Wenn der Wert Null (falsch) ist, werden diese Operationen übersprungen und direkt zu den Operationen nach `OP_ELSE` übergegangen, falls dieses vorhanden ist. `OP_IF` ermöglicht das Starten einer bedingten Kontrollstruktur innerhalb eines Skripts. Es bestimmt den Kontrollfluss in einem Skript basierend auf einer Bedingung, die zum Zeitpunkt der Ausführung der Transaktion bereitgestellt wird. `OP_IF` wird zusammen mit `OP_ELSE` und `OP_ENDIF` auf folgende Weise verwendet:

```text
<Bedingung>
OP_IF
<Operationen, wenn die Bedingung wahr ist>
OP_ELSE
<Operationen, wenn die Bedingung falsch ist>
OP_ENDIF
```