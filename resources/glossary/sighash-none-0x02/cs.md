---
term: SIGHASH_NONE (0X02)
---

Typ příznaku SigHash používaný v podpisech transakcí Bitcoinu, který indikuje, že podpis se vztahuje na všechny vstupy transakce, ale na žádný z jejích výstupů. Použití `SIGHASH_NONE` znamená, že podepisující se zavazuje pouze k vstupům, což umožňuje, aby výstupy zůstaly neurčené nebo modifikovatelné po podpisu. Tento typ podpisu je užitečný v případech, kdy podepisující chce oprávnit jiné strany rozhodnout o tom, jak budou bitcoiny v transakci rozděleny.