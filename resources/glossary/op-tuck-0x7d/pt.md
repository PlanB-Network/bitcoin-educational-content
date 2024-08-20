---
term: OP_TUCK (0X7D)
---

Copia o item no topo da pilha e o insere entre o segundo e o terceiro itens da pilha. Por exemplo, se a pilha for:

```text
A
B
C
D
```

`OP_TUCK` duplicará o item do topo `A` e o colocará na terceira posição. A pilha resultante será:

```text
A
B
A
C
D
```