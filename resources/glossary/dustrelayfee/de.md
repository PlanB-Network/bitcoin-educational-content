---
term: DUSTRELAYFEE
---

Eine Standardisierungsregel, die von Netzwerkknoten verwendet wird, um zu bestimmen, was sie als "Staubgrenze" betrachten. Dieser Parameter legt eine Gebührenrate in Sats pro virtuellem Kilobyte (sats/kvB) fest, die als Referenz dient, um zu berechnen, ob der Wert eines UTXO geringer ist als die notwendigen Gebühren, um ihn in eine Transaktion einzubeziehen. Tatsächlich wird ein UTXO bei Bitcoin als "Staub" betrachtet, wenn die Übertragungsgebühren höher sind als der Wert, den es selbst darstellt. Die Berechnung dieser Grenze erfolgt wie folgt:

```text
limit = (Eingabegröße + Ausgabegröße) * Gebührenrate
```

Da die erforderliche Gebührenrate für die Aufnahme einer Transaktion in einen Bitcoin-Block ständig variiert, ermöglicht der `DustRelayFee`-Parameter jedem Knoten, die Gebührenrate zu definieren, die in dieser Berechnung verwendet wird. Standardmäßig ist dieser Wert bei Bitcoin Core auf 3.000 sats/kvB festgelegt. Zum Beispiel, um die Staubgrenze für eine P2PKH-Eingabe und -Ausgabe zu berechnen, die jeweils 148 und 34 Bytes messen, wäre die Berechnung:

```text
limit (sats) = (148 + 34) * 3000 / 1000 = 546 sats
```

Das bedeutet, dass der betreffende Knoten Transaktionen, die ein durch P2PKH gesichertes UTXO enthalten, dessen Wert weniger als 546 sats beträgt, nicht weiterleiten wird.