---
term: Knapsack solver

definition: Gammel myntutvelgelsesmetode i Bitcoin Core, erstattet av Branch-and-Bound.
---
En gammel metode som ble brukt for å velge mynter i Bitcoin Core-lommeboken før versjon 0.17. Knapsack Solver forsøker å løse myntvalgproblemet ved iterativt og tilfeldig å velge UTXO-er og legge dem sammen i undergrupper, med mål om å minimere avgiftene og størrelsen på transaksjonen. Denne metoden har siden blitt erstattet av *Branch-and-Bound*.