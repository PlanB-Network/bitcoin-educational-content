---
term: LOCK (.LOCK)
---

Fil som används i Bitcoin Core för att låsa datakatalogen. Den skapas när bitcoind eller Bitcoin-qt startar för att förhindra att flera instanser av programvaran får åtkomst till samma datakatalog samtidigt. Målet är att förhindra konflikter och datakorruption. Om programvaran oväntat stannar kan .lock-filen finnas kvar och måste raderas manuellt innan Bitcoin Core startas om.