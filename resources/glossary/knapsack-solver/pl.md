---
term: Knapsack solver
definition: Stara metoda wyboru monet w Bitcoin Core, zastąpiona przez Branch-and-Bound.
---

Stara metoda używana do wyboru monet w Bitcoin Core Wallet przed wersją 0.17. Knapsack Solver próbuje rozwiązać problem wyboru monet, iteracyjnie i losowo wybierając UTXO i sumując je według podzbiorów, w celu zminimalizowania opłat i wielkości transakcji. Metoda ta została zastąpiona przez *Branch-and-Bound*.