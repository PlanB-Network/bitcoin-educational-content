---
term: BIFURCACIÓN

---
Método utilizado para seleccionar entradas en el monedero Bitcoin Core desde la versión 0.17 e inventado por Murch. Branch-and-Bound (BnB) es una búsqueda para encontrar un conjunto de UTXOs que coincida con la cantidad exacta de salidas a cumplir en una transacción, con el fin de minimizar el cambio y las tasas asociadas. Su objetivo es reducir un criterio de desperdicio que tenga en cuenta tanto el coste inmediato como los costes futuros previstos para el cambio. Este método es más preciso en términos de tasas en comparación con heurísticas anteriores como el *Knapsack Solver*. El *Branch-and-Bound* se inspira en el método de resolución de problemas del mismo nombre, inventado en 1960 por Ailsa Land y Alison Harcourt.

> ► *Este método también se denomina a veces "Algoritmo de Murch" en referencia a su inventor.*