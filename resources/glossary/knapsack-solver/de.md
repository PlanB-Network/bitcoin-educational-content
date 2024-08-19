---
term: KNAPSACK SOLVER
---

Eine alte Methode, die für die Auswahl von Münzen im Bitcoin Core Wallet vor Version 0.17 verwendet wurde. Der Knapsack Solver versucht, das Problem der Münzauswahl zu lösen, indem iterativ und zufällig UTXOs ausgewählt und in Teilmengen addiert werden, mit dem Ziel, die Gebühren und die Größe der Transaktion zu minimieren. Diese Methode wurde mittlerweile durch *Branch-and-Bound* ersetzt.