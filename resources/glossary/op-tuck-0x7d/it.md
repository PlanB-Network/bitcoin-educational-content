---
term: OP_TUCK (0X7D)

---
Copia l'elemento in cima alla pila e lo inserisce tra il secondo e il terzo elemento della pila. Ad esempio, se la pila è:

```text
A
B
C
D
```

`OP_TUCK` duplicherà l'elemento superiore `A` e lo collocherà in terza posizione. La pila risultante sarà:

```text
A
B
A
C
D
```