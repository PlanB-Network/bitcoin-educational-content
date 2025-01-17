---
term: DUSTRELAYFEE

---
Regla de normalización utilizada por los nodos de la red para determinar lo que consideran el "límite de polvo" Este parámetro establece una tasa de comisión en sats por kilobyte virtual (sats/kvB) que sirve de referencia para calcular si el valor de un UTXO es inferior a las comisiones necesarias para incluirlo en una transacción. De hecho, un UTXO se considera "polvo" en Bitcoin si requiere más en tasas para ser transferido que el valor que representa en sí mismo. El cálculo de este límite es el siguiente:

```text
limit = (input size + output size) * fee rate
```

Como la tasa requerida para que una transacción sea incluida en un bloque Bitcoin varía constantemente, el parámetro `DustRelayFee` permite a cada nodo definir la tasa usada en este cálculo. Por defecto, en Bitcoin Core, este valor está fijado en 3.000 sats/kvB. Por ejemplo, para calcular el límite de polvo para una entrada y salida P2PKH, que miden 148 y 34 bytes respectivamente, el cálculo sería:

```text
limit (sats) = (148 + 34) * 3000 / 1000 = 546 sats
```

Esto significa que el nodo en cuestión no retransmitirá transacciones que incluyan un UTXO asegurado P2PKH cuyo valor sea inferior a 546 sats.