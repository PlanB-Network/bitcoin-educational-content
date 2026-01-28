---
term: OP_2SWAP (0X72)

definition: Opcode che scambia i primi due elementi dello stack con i due successivi.
---
Scambia i due elementi in cima alla pila con i due elementi immediatamente sotto. Ad esempio, se la pila è:

```text
A
B
C
D
```

`OP_2SWAP` produrrà:

```text
C
D
A
B
```