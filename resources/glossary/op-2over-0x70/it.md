---
termine: OP_2OVER (0X70)
---

Copia gli elementi che si trovano nella quarta e terza posizione dall'alto dello stack, poi li posiziona in cima allo stack. Ad esempio, se lo stack è:

```testo
A
B
C
D
```

`OP_2OVER` produrrà:

```testo
C
D
A
B
C
D
```