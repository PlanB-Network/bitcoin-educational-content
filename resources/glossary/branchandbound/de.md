---
term: BRANCH-AND-BOUND
---

Methode, die seit Version 0.17 für die Auswahl von Eingaben im Bitcoin Core Wallet verwendet wird und von Murch erfunden wurde. Branch-and-Bound (BnB) ist eine Suche, um eine Menge von UTXOs zu finden, die genau der Menge der in einer Transaktion zu erfüllenden Ausgaben entspricht, um Wechselgeld und damit verbundene Gebühren zu minimieren. Ihr Ziel ist es, ein Verschwendungskriterium zu reduzieren, das sowohl die sofortigen Kosten als auch die erwarteten zukünftigen Kosten für das Wechselgeld berücksichtigt. Diese Methode ist in Bezug auf die Gebühren genauer im Vergleich zu früheren Heuristiken wie dem *Knapsack Solver*. Der *Branch-and-Bound* ist inspiriert von der gleichnamigen Problemlösungsmethode, die 1960 von Ailsa Land und Alison Harcourt erfunden wurde.

> ► *Diese Methode wird manchmal auch "Murch's Algorithmus" in Bezug auf ihren Erfinder genannt.*