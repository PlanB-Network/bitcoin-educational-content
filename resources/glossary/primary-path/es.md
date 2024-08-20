---
term: PRIMARY PATH
---

En un software de billetera que utiliza Miniscript, como Liana por ejemplo, el primary path se refiere al conjunto de llaves que permiten el gasto inmediato de fondos, sin ninguna condición basada en tiempo. Este camino siempre es accesible y se utiliza para la gestión diaria de bitcoins, sin requerir una espera (timelock) a diferencia de los caminos de recuperación. Tomemos el ejemplo de un script que incorpora 2 llaves distintas: la llave A, que autoriza el gasto inmediato de bitcoins, y la llave B, que permite gastarlos después de un retraso definido por un timelock de 52,560 bloques. En este ejemplo, la llave A proviene del primary path, mientras que la llave B proviene del recovery path.