---
term: SENDERO PRIMARIO

---
En un software de monedero que utiliza Miniscript, como Liana por ejemplo, la ruta primaria se refiere al conjunto de claves que permiten el gasto inmediato de fondos, sin condiciones temporales. Esta ruta está siempre accesible y se utiliza para la gestión diaria de bitcoins, sin requerir una espera (timelock) a diferencia de las rutas de recuperación. Tomemos el ejemplo de un script que incorpora 2 claves distintas: la clave A, que autoriza el gasto inmediato de bitcoins, y la clave B, que permite gastarlos tras un retraso definido por un timelock de 52.560 bloques. En este ejemplo, la clave A procede de la ruta primaria, mientras que la clave B procede de la ruta de recuperación.