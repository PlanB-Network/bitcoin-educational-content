---
term: OUTPOINT
---

Ein einzigartiger Verweis auf einen unverbrauchten Transaktionsausgang (UTXO). Er besteht aus zwei Elementen:
* `txid`: der Identifikator der Transaktion, die den Ausgang erzeugt hat;
* `vout`: der Index des Ausgangs in der Transaktion.

Die Kombination dieser beiden Elemente identifiziert präzise einen UTXO. Zum Beispiel, wenn eine Transaktion eine `txid` von `abc...123` hat und der Ausgangsindex `0` ist, wird der Outpoint wie folgt notiert:

```text
abc...123:0
```

Der Outpoint wird in den Eingängen (`vin`) einer neuen Transaktion verwendet, um anzugeben, welcher UTXO verbraucht wird.

> ► *Der Begriff "Outpoint" wird oft synonym mit "UTXO" verwendet.*