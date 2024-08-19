---
term: OP_3DUP (0X6F)
---

Dupliziert die obersten drei Elemente des Stapels und platziert sie dann oben auf dem Stapel. Zum Beispiel, wenn der Stapel ist:

```text
A
B
C
D
```

wird `OP_3DUP` folgendes produzieren:

```text
A
B
C
A
B
C
D
```