---
term: OP_TUCK (0X7D)

---
Copia o item no topo da pilha e insere-o entre o segundo e o terceiro itens da pilha. Por exemplo, se a pilha for:

```text
A
B
C
D
```

`OP_TUCK` irá duplicar o item de topo `A` e colocá-lo na terceira posição. A pilha resultante será:

```text
A
B
A
C
D
```