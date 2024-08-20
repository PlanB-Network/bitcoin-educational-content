---
term: BRANCH-AND-BOUND
---

Método utilizado para seleccionar entradas en la cartera de Bitcoin Core desde la versión 0.17 e inventado por Murch. Branch-and-Bound (BnB) es una búsqueda para encontrar un conjunto de UTXOs que coincida con la cantidad exacta de salidas a cumplir en una transacción, con el fin de minimizar el cambio y las comisiones asociadas. Su objetivo es reducir un criterio de desperdicio que tiene en cuenta tanto el costo inmediato como los costos futuros esperados por el cambio. Este método es más preciso en términos de comisiones en comparación con heurísticas anteriores como el *Knapsack Solver*. El *Branch-and-Bound* se inspira en el método de resolución de problemas del mismo nombre, inventado en 1960 por Ailsa Land y Alison Harcourt.

> ► *Este método también es a veces nombrado "Algoritmo de Murch" en referencia a su inventor.*