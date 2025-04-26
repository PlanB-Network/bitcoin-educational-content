---
term: OP_2OVER (0X70)

---
Copia os dois elementos que estão na quarta e terceira posições a partir do topo da pilha e, em seguida, coloca-os no topo da pilha. Por exemplo, se a pilha for:

```text
A
B
C
D
```

o `OP_2OVER` produzirá:

```text
C
D
A
B
C
D
```