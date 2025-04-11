---
term: SELECCIÓN DE MONEDAS

---
El proceso por el cual el software de un monedero Bitcoin elige qué UTXOs utilizar como entradas para satisfacer las salidas de una transacción. El método de selección de monedas es importante porque tiene consecuencias sobre el coste de una transacción y la privacidad del usuario. A menudo se intenta minimizar el número de entradas utilizadas, con el fin de reducir el tamaño de la transacción y las tarifas asociadas, al tiempo que se intenta preservar la privacidad evitando fusionar monedas de diferentes fuentes (CIOH). Existen varios métodos para la selección de monedas, como el *Knapsack Solver* o el *Branch-and-Bound*. Cuando la selección de monedas la realiza manualmente el usuario, se denomina "*Coin Control*".

> ► *En inglés, se denomina "Coin Selection".*