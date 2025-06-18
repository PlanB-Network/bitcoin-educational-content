---
term: OP_PUSHDATA4 (0X4E)
---

Umożliwia wypychanie bardzo dużej ilości danych na stos. Po nim następują cztery bajty (little-endian), które wskazują długość danych do wypchnięcia (do około 4,3 GB). Ten kod operacyjny jest używany do wstawiania bardzo dużych danych do skryptów, chociaż jego użycie jest niezwykle rzadkie ze względu na praktyczne ograniczenia rozmiaru transakcji.