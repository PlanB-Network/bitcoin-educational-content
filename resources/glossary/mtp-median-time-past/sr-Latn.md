---
term: MTP (MEDIJANA PROŠLOG VREMENA)
---

Ovaj koncept se koristi u Bitcoin protokolu za određivanje margine na konsenzusu mreže Timestamp. MTP je definisan kao medijana vremenskih oznaka poslednjih 11 iskopanih blokova. Korišćenje ovog indikatora pomaže da se izbegnu neslaganja među čvorovima oko tačnog vremena u slučaju neslaganja. MTP je prvobitno korišćen za verifikaciju validnosti vremenskih oznaka blokova u odnosu na prošlost. Od BIP113, takođe se koristi kao referenca za mrežno vreme za verifikaciju validnosti transakcija sa vremenskim zaključavanjem (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence`, i `OP_CHECKSEQUENCEVERIFY`).