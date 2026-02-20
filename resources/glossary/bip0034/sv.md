---
term: BIP0034
definition: Soft fork som kräver att blockhöjden inkluderas i coinbase-transaktionen, vilket garanterar att varje block är unikt.
---

Soft Fork tillämpades i mars 2013, med början från block 227.930, vilket introducerade version 2 för Bitcoin-block. Denna nya version kräver att varje block inkluderar höjden på det block som skapas i `scriptSig` för Coinbase Transaction. Denna ändring tjänar till att klargöra hur nätverket kommer överens om att ändra blockens struktur och konsensusreglerna. Dessutom förstärker den det unika i varje block och varje Coinbase Transaction.