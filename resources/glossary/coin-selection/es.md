---
term: SELECCIÓN DE MONEDAS
---

El proceso mediante el cual un software de monedero Bitcoin elige qué UTXOs utilizar como entradas para satisfacer las salidas de una transacción. El método de selección de monedas es importante porque tiene consecuencias en el costo de una transacción y la privacidad del usuario. A menudo, se busca minimizar el número de entradas utilizadas, con el fin de reducir el tamaño de la transacción y las comisiones asociadas, mientras se intenta preservar la privacidad evitando combinar monedas de diferentes fuentes (CIOH). Existen varios métodos para la selección de monedas, como el *Knapsack Solver* o el *Branch-and-Bound*. Cuando la selección de monedas se realiza manualmente por el usuario, se le denomina “*Control de Monedas*”.

> ► *En inglés, se le denomina "Coin Selection".*