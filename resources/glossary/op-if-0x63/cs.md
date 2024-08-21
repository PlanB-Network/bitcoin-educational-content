---
term: OP_IF (0X63)
---

Spouští následující část skriptu, pokud je hodnota na vrcholu zásobníku nenulová (pravda). Pokud je hodnota nula (nepravda), tyto operace jsou přeskočeny a pokračuje se přímo k operacím po `OP_ELSE`, pokud je přítomen. `OP_IF` umožňuje spuštění podmíněné kontrolní struktury v rámci skriptu. Určuje tok řízení ve skriptu na základě podmínky poskytnuté v době vykonání transakce. `OP_IF` se používá společně s `OP_ELSE` a `OP_ENDIF` následujícím způsobem:

```text
<podmínka>
OP_IF
<operace, pokud je podmínka pravdivá>
OP_ELSE
<operace, pokud je podmínka nepravdivá>
OP_ENDIF
```