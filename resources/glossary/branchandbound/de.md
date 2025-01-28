---
term: BRANCH-AND-BOUND

---
Methode, die seit Version 0.17 für die Auswahl von Inputs in der Bitcoin Core Wallet verwendet wird und von Murch erfunden wurde. Branch-and-Bound (BnB) ist eine Suche nach einer Menge von UTXOs, die genau der Menge der in einer Transaktion zu erfüllenden Ausgaben entspricht, um Wechselgeld und die damit verbundenen Gebühren zu minimieren. Ziel ist es, ein Verschwendungskriterium zu reduzieren, das sowohl die unmittelbaren Kosten als auch die für die Änderung zu erwartenden künftigen Kosten berücksichtigt. Diese Methode ist im Vergleich zu früheren Heuristiken wie dem *Knapsack Solver* genauer, was die Gebühren angeht. Die *Branch-and-Bound* ist inspiriert von der gleichnamigen Problemlösungsmethode, die 1960 von Ailsa Land und Alison Harcourt erfunden wurde.

> diese Methode wird in Anlehnung an ihren Erfinder manchmal auch "Murch's Algorithm" genannt