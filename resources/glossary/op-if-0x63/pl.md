---
term: OP_IF (0X63)
---

Wykonuje następującą część skryptu, jeśli wartość na szczycie stosu jest niezerowa (true). Jeśli wartość wynosi zero (false), operacje te są pomijane, przechodząc bezpośrednio do tych po `OP_ELSE`, jeśli jest obecny. `OP_IF` umożliwia uruchomienie warunkowej struktury kontrolnej w skrypcie. Określa ona przepływ kontroli w skrypcie na podstawie warunku podanego w czasie wykonywania transakcji. `OP_IF` jest używane z `OP_ELSE` i `OP_ENDIF` w następujący sposób:


```text
<condition>
OP_IF
<operations if the condition is true>
OP_ELSE
<operations if the condition is false>
OP_ENDIF
```