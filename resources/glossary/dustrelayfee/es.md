---
term: DUSTRELAYFEE
---

Una regla de estandarización utilizada por los nodos de la red para determinar lo que consideran el "límite de polvo" ("dust limit"). Este parámetro establece una tasa de comisión en sats por kilobyte virtual (sats/kvB) que sirve como referencia para calcular si el valor de un UTXO es menor que las comisiones necesarias para incluirlo en una transacción. De hecho, un UTXO se considera "polvo" en Bitcoin si requiere más en comisiones para ser transferido que el valor que representa. El cálculo de este límite es el siguiente:

```text
límite = (tamaño de entrada + tamaño de salida) * tasa de comisión
```

Como la tasa de comisión requerida para que una transacción sea incluida en un bloque de Bitcoin varía constantemente, el parámetro `DustRelayFee` permite a cada nodo definir la tasa de comisión utilizada en este cálculo. Por defecto, en Bitcoin Core, este valor está establecido en 3,000 sats/kvB. Por ejemplo, para calcular el límite de polvo para una entrada y salida P2PKH, que miden 148 y 34 bytes respectivamente, el cálculo sería:

```text
límite (sats) = (148 + 34) * 3000 / 1000 = 546 sats
```

Esto significa que el nodo en cuestión no retransmitirá transacciones que incluyan un UTXO asegurado por P2PKH cuyo valor sea menor a 546 sats.