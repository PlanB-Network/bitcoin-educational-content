---
term: OP_2DUP (0X6E)
---

Dupliziert die zwei obersten Elemente des Stapels und platziert sie dann oben auf dem Stapel. Zum Beispiel, wenn der Stapel ist:

```text
A
B
C
D
```

wird `OP_2DUP` folgendes produzieren:

```text
A
B
A
B
C
D
```