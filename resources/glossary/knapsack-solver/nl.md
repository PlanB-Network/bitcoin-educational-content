---
term: Knapsack solver
definition: Oude methode voor muntselectie in Bitcoin Core, vervangen door Branch-and-Bound.
---

Een oude methode die werd gebruikt voor het selecteren van munten in de Bitcoin core Wallet vóór versie 0.17. De Knapsack Solver probeert het Coin selectieprobleem op te lossen door iteratief en willekeurig UTXO's te kiezen en deze op te tellen per subset, met als doel de kosten en de grootte van de transactie te minimaliseren. Deze methode is sindsdien vervangen door *Branch-and-Bound*.