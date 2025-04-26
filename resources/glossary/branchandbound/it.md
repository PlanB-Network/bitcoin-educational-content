---
term: BRANCH-AND-BOUND

---
Metodo utilizzato per la selezione degli ingressi nel portafoglio Bitcoin Core dalla versione 0.17 e inventato da Murch. Branch-and-Bound (BnB) è una ricerca per trovare un insieme di UTXO che corrisponda all'esatta quantità di output da soddisfare in una transazione, al fine di minimizzare il cambio e le commissioni associate. Il suo obiettivo è ridurre un criterio di spreco che tenga conto sia del costo immediato che dei costi futuri previsti per il cambiamento. Questo metodo è più accurato in termini di costi rispetto a euristiche precedenti come il *Knapsack Solver*. Il *Branch-and-Bound* si ispira all'omonimo metodo di risoluzione dei problemi, inventato nel 1960 da Ailsa Land e Alison Harcourt.

> questo metodo viene talvolta chiamato anche "Algoritmo di Murch" in riferimento al suo inventore