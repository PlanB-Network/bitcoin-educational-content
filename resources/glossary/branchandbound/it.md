---
termine: BRANCH-AND-BOUND
---

Metodo utilizzato per la selezione degli input nel portafoglio Bitcoin Core dalla versione 0.17 e inventato da Murch. Branch-and-Bound (BnB) è una ricerca per trovare un insieme di UTXO che corrisponde esattamente all'importo degli output da soddisfare in una transazione, al fine di minimizzare il resto e le commissioni associate. Il suo obiettivo è ridurre un criterio di spreco che prende in considerazione sia il costo immediato sia i costi futuri previsti per il resto. Questo metodo è più accurato in termini di commissioni rispetto a euristiche precedenti come il *Knapsack Solver*. Il *Branch-and-Bound* si ispira al metodo di risoluzione dei problemi omonimo, inventato nel 1960 da Ailsa Land e Alison Harcourt.

> ► *Questo metodo è talvolta chiamato anche "Algoritmo di Murch" in riferimento al suo inventore.*