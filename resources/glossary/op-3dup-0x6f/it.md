---
termine: OP_3DUP (0X6F)
---

Duplica i primi tre elementi dello stack, poi li posiziona in cima allo stack. Ad esempio, se lo stack è:

```testo
A
B
C
D
```

`OP_3DUP` produrrà:

```testo
A
B
C
A
B
C
D
```