---
term: OP_TUCK (0X7D)
---

Kopiert das Element an der Spitze des Stapels und fügt es zwischen das zweite und dritte Element des Stapels ein. Zum Beispiel, wenn der Stapel ist:

```text
A
B
C
D
```

wird `OP_TUCK` das oberste Element `A` duplizieren und es an die dritte Position setzen. Der resultierende Stapel wird sein:

```text
A
B
A
C
D
```