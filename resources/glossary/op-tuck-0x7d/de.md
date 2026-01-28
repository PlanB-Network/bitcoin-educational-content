---
term: OP_TUCK (0X7D)

definition: Opcode, der das oberste Stack-Element kopiert und an die dritte Position einfügt.
---
Kopiert das Element an der Spitze des Stapels und fügt es zwischen dem zweiten und dritten Element des Stapels ein. Zum Beispiel, wenn der Stapel ist:

```text
A
B
C
D
```

mit "OP_TUCK" wird das oberste Element "A" dupliziert und an die dritte Position gesetzt. Der resultierende Stapel wird sein:

```text
A
B
A
C
D
```