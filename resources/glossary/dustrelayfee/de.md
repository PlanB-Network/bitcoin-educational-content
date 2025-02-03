---
term: DUSTRELAYFEE

---
Eine Standardisierungsregel, die von Netzknoten verwendet wird, um zu bestimmen, was sie als "Staubgrenze" betrachten Dieser Parameter legt einen Gebührensatz in Sats pro virtuellem Kilobyte (sats/kvB) fest, der als Referenz für die Berechnung dient, ob der Wert eines UTXO geringer ist als die notwendigen Gebühren, um ihn in eine Transaktion aufzunehmen. Tatsächlich gilt ein UTXO als "Staub" auf Bitcoin, wenn es mehr an Gebühren erfordert, um übertragen zu werden, als der Wert, den es selbst darstellt. Die Berechnung dieser Grenze ist wie folgt:

```text
limit = (input size + output size) * fee rate
```

Da der erforderliche Gebührensatz für eine Transaktion, die in einen Bitcoin-Block aufgenommen werden soll, ständig variiert, erlaubt der Parameter `DustRelayFee` jedem Knoten, den Gebührensatz zu definieren, der in dieser Berechnung verwendet wird. Standardmäßig ist dieser Wert bei Bitcoin Core auf 3.000 sats/kvB eingestellt. Um zum Beispiel das Staublimit für einen P2PKH-Eingang und -Ausgang zu berechnen, die 148 bzw. 34 Bytes groß sind, würde die Berechnung folgendermaßen aussehen:

```text
limit (sats) = (148 + 34) * 3000 / 1000 = 546 sats
```

Das bedeutet, dass der betreffende Knoten keine Transaktionen weiterleitet, die einen P2PKH-gesicherten UTXO enthalten, dessen Wert weniger als 546 Sats beträgt.