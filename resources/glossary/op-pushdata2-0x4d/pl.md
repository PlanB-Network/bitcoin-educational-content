---
term: OP_PUSHDATA2 (0X4D)
definition: Opcode kładący do 65 KB danych na stosie.
---

Umożliwia wepchnięcie dużej ilości danych na stos. Po nim następują dwa bajty (little-endian), które określają długość danych do wypchnięcia (do około 65 KB). Służy do wstawiania większych danych do skryptów.