---
term: SIGHASH_ALL

definition: SigHash Flag označující, že podpis pokrývá všechny vstupy a výstupy transakce.
---
Typ příznaku SigHash Příznak používaný v podpisech bitcoinových transakcí, který označuje, že se podpis vztahuje na všechny součásti transakce. Použitím `SIGHASH_ALL` se podpis vztahuje na všechny vstupy a výstupy. To znamená, že vstupy ani výstupy nelze po podpisu měnit, aniž by byl podpis zneplatněn. Tento typ příznaku SigHash je v bitcoinových transakcích nejběžnější, protože zajišťuje úplnou konečnost a integritu transakce.