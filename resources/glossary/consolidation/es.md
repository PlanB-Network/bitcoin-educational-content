---
term: CONSOLIDACIÓN

---
Una transacción específica en la que varios UTXO pequeños se fusionan en una entrada para formar un único UTXO más grande como salida. Esta operación es una transacción realizada al propio monedero. El objetivo de la consolidación es aprovechar los periodos en los que las comisiones en la red Bitcoin son bajas para fusionar varios UTXOs pequeños en uno mayor en valor. De este modo, se anticipa a los gastos obligatorios en caso de aumento de las tasas, lo que permite ahorrar en las tasas de transacción futuras.

De hecho, las transacciones con muchos insumos son más pesadas y, en consecuencia, más caras. Más allá del ahorro que se puede conseguir en las tasas de transacción, la consolidación es también una forma de planificación a largo plazo. Si su monedero contiene UTXOs muy pequeños, éstos pueden volverse inutilizables si la red Bitcoin entra en un periodo prolongado de altas comisiones. Por ejemplo, si necesita gastar un UTXO de 10.000 sats pero las tasas mínimas de minería ascienden a 15.000 sats, el gasto superaría el valor del propio UTXO. Estos pequeños UTXOs se convierten entonces en económicamente irracionales de usar y permanecen inutilizables mientras las tasas no disminuyan. A estos UTXOs se les conoce comúnmente como "polvo" Al consolidar regularmente sus UTXO pequeños, se reduce este riesgo asociado al aumento de las comisiones.

Sin embargo, es importante señalar que las transacciones de consolidación son reconocibles durante un análisis de cadena. Una transacción de este tipo indica una heurística de propiedad de entrada común (CIOH), lo que significa que las entradas de la transacción de consolidación son propiedad de una única entidad. Esto puede tener implicaciones en términos de privacidad para el usuario.

![](../../dictionnaire/assets/7.webp)