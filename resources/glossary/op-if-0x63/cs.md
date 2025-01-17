---
term: OP_IF (0X63)

---
Provede následující část skriptu, pokud je hodnota na vrcholu zásobníku nenulová (true). Pokud je hodnota nulová (false), tyto operace se přeskočí a přejde se přímo k operacím za `OP_ELSE`, pokud je přítomen. `OP_IF` umožňuje spuštění podmíněné řídicí struktury v rámci skriptu. Určuje tok řízení ve skriptu na základě podmínky zadané v okamžiku provádění transakce. `OP_IF` se používá spolu s `OP_ELSE` a `OP_ENDIF` následujícím způsobem:

```text
<condition>
OP_IF
<operations if the condition is true>
OP_ELSE
<operations if the condition is false>
OP_ENDIF
```