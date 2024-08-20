---
term: KNAPSACK SOLVER
---

Un método antiguo utilizado para seleccionar monedas en la cartera de Bitcoin Core antes de la versión 0.17. El Knapsack Solver intenta resolver el problema de selección de monedas eligiendo de manera iterativa y aleatoria UTXOs, y sumándolos por subconjuntos, con el objetivo de minimizar las comisiones y el tamaño de la transacción. Este método ha sido reemplazado desde entonces por *Branch-and-Bound*.