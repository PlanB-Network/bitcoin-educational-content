---
term: KNAPSACK SOLVER
---

Stará metoda používaná pro výběr mincí v peněžence Bitcoin Core před verzí 0.17. Knapsack Solver se pokouší vyřešit problém výběru mincí iterativním a náhodným výběrem UTXO a jejich sčítáním do podmnožin s cílem minimalizovat poplatky a velikost transakce. Tato metoda byla od té doby nahrazena metodou *Branch-and-Bound*.