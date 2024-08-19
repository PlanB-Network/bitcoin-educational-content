---
termine: OP_TUCK (0X7D)
---

Copia l'elemento in cima allo stack e lo inserisce tra il secondo e il terzo elemento dello stack. Ad esempio, se lo stack è:

```testo
A
B
C
D
```

`OP_TUCK` duplicherà l'elemento in cima `A` e lo posizionerà nella terza posizione. Lo stack risultante sarà:

```testo
A
B
A
C
D
```