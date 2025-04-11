---
term: KNAPSACK-LÖSER

---
Eine alte Methode, die für die Auswahl von Münzen in der Bitcoin Core Wallet vor Version 0.17 verwendet wurde. Der Knapsack Solver versucht, das Münzauswahlproblem zu lösen, indem er iterativ und zufällig UTXOs auswählt und sie zu Teilmengen addiert, mit dem Ziel, die Gebühren und die Größe der Transaktion zu minimieren. Diese Methode ist inzwischen durch *Branch-and-Bound* ersetzt worden.