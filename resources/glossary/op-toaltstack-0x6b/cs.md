---
term: OP_TOALTSTACK (0X6B)

definition: Opcode přesouvající vrchol hlavního zásobníku do alternativního zásobníku.
---
Vezme vrchol hlavního zásobníku (*main stack*) a přesune jej do alternativního zásobníku (*alt stack*). Tento opkód se používá k dočasnému uložení dat stranou pro pozdější použití ve skriptu. Přesunutá položka je tak z hlavního zásobníku odstraněna. poté se použije `OP_FROMALTSTACK` k jejímu vrácení na vrchol hlavního zásobníku.