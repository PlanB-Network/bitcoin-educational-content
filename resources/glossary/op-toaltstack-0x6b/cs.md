---
term: OP_TOALTSTACK (0X6B)
---

Přenáší vrchol hlavního zásobníku (*main stack*) na alternativní zásobník (*alt stack*). Tento operační kód se používá k dočasnému uložení dat stranou pro pozdější použití ve skriptu. Přesunutá položka je tak odstraněna z hlavního zásobníku. `OP_FROMALTSTACK` pak bude použit k jejímu vrácení zpět na vrchol hlavního zásobníku.