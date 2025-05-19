---
term: OP_IF (0X63)
---

Hutekeleza sehemu ifuatayo ya hati ikiwa thamani iliyo juu ya rafu si sifuri (kweli). Ikiwa thamani ni sifuri (sivyo), shughuli hizi kurukwa, zikisogezwa moja kwa moja hadi zile baada ya `OP_ELSE`, ikiwa iko. `OP_IF` huwezesha uzinduzi wa muundo wa udhibiti wa masharti ndani ya hati. Huamua mtiririko wa udhibiti katika hati kulingana na hali iliyotolewa wakati wa utekelezaji wa shughuli. `OP_IF` inatumika pamoja na `OP_ELSE` na `OP_ENDIF` kwa njia ifuatayo:


```text
<condition>
OP_IF
<operations if the condition is true>
OP_ELSE
<operations if the condition is false>
OP_ENDIF
```