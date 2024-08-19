---
termine: OP_2DUP (0X6E)
---

Duplica i due elementi in cima allo stack, poi li posiziona sopra lo stack. Ad esempio, se lo stack è:

```testo
A
B
C
D
```

`OP_2DUP` produrrà:

```testo
A
B
A
B
C
D
```