---
term: OP_IF (0X63)
---

Izvršava sledeći deo skripta ako je vrednost na vrhu steka različita od nule (tačno). Ako je vrednost nula (netačno), ove operacije se preskaču, prelazeći direktno na one posle `OP_ELSE`, ako je prisutan. `OP_IF` omogućava pokretanje uslovne kontrolne strukture unutar skripta. Određuje tok kontrole u skriptu na osnovu uslova koji je dat u trenutku izvršenja transakcije. `OP_IF` se koristi sa `OP_ELSE` i `OP_ENDIF` na sledeći način:


```text
<condition>
OP_IF
<operations if the condition is true>
OP_ELSE
<operations if the condition is false>
OP_ENDIF
```