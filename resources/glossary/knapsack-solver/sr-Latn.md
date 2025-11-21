---
term: KNAPSACK SOLVER
---

Stara metoda korišćena za odabir novčića u Bitcoin Core Wallet pre verzije 0.17. Knapsack Solver pokušava da reši problem odabira novčića iterativnim i nasumičnim izborom UTXO-a, i njihovim sabiranjem po podskupovima, sa ciljem minimiziranja naknada i veličine transakcije. Ova metoda je od tada zamenjena metodom *Branch-and-Bound*.