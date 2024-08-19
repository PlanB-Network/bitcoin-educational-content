---
term: OP_2OVER (0X70)
---

Kopiert die zwei Elemente, die sich an der vierten und dritten Position von oben auf dem Stapel befinden, und platziert sie dann oben auf dem Stapel. Zum Beispiel, wenn der Stapel ist:

```text
A
B
C
D
```

wird `OP_2OVER` folgendes Ergebnis produzieren:

```text
C
D
A
B
C
D
```