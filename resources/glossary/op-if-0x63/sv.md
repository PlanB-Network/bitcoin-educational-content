---
term: OP_IF (0X63)
definition: Opcode som kör en del av scriptet om villkoret överst på stacken är sant.
---

Exekverar följande del av skriptet om värdet högst upp i stacken är ett annat än noll (true). Om värdet är noll (false) hoppas dessa operationer över och flyttas direkt till dem efter `OP_ELSE`, om den finns. `OP_IF` gör det möjligt att starta en villkorlig kontrollstruktur i ett skript. Den bestämmer kontrollflödet i ett skript baserat på ett villkor som anges vid tidpunkten för transaktionens exekvering. `OP_IF` används tillsammans med `OP_ELSE` och `OP_ENDIF` på följande sätt:


```text
<condition>
OP_IF
<operations if the condition is true>
OP_ELSE
<operations if the condition is false>
OP_ENDIF
```