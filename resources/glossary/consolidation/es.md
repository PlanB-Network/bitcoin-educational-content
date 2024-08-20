---
term: CONSOLIDACIÓN
---

Una transacción específica en la que múltiples UTXOs pequeños se fusionan en una entrada para formar un único UTXO más grande como salida. Esta operación es una transacción realizada hacia la propia cartera del usuario. El objetivo de la consolidación es aprovechar los períodos cuando las comisiones en la red de Bitcoin son bajas para fusionar varios UTXOs pequeños en uno más grande en valor. Así, anticipa gastos obligatorios en caso de aumentos de comisiones, permitiendo ahorrar en futuras comisiones de transacción.

De hecho, las transacciones con muchas entradas son más pesadas y, por consiguiente, más caras. Más allá del ahorro alcanzable en comisiones de transacción, la consolidación es también una forma de planificación a largo plazo. Si tu cartera contiene UTXOs muy pequeños, estos pueden volverse inutilizables si la red de Bitcoin entra en un período prolongado de comisiones altas. Por ejemplo, si necesitas gastar un UTXO de 10,000 sats pero las comisiones mínimas de minería ascienden a 15,000 sats, el gasto superaría el valor del propio UTXO. Estos pequeños UTXOs se vuelven entonces económicamente irracionales de usar y permanecen inutilizables mientras las comisiones no disminuyan. A estos UTXOs comúnmente se les refiere como "polvo". Al consolidar regularmente tus pequeños UTXOs, reduces este riesgo asociado con los aumentos de comisiones.

Sin embargo, es importante notar que las transacciones de consolidación son reconocibles durante un análisis de cadena. Tal transacción indica una Heurística de Propiedad de Entrada Común (CIOH, por sus siglas en inglés), lo que significa que las entradas de la transacción de consolidación son propiedad de una única entidad. Esto puede tener implicaciones en términos de privacidad para el usuario.

![](../../dictionnaire/assets/7.png)