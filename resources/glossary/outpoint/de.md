---
term: OUTPOINT

---
Eine eindeutige Referenz auf eine nicht verbrauchte Transaktionsausgabe (UTXO). Sie besteht aus zwei Elementen:


- txid": die Kennung der Transaktion, die die Ausgabe erzeugt hat;
- vout": der Index der Ausgabe in der Transaktion.

Durch die Kombination dieser beiden Elemente wird ein UTXO genau identifiziert. Wenn zum Beispiel eine Transaktion ein "txid" von "abc...123" hat und der Ausgangsindex "0" ist, wird der Ausgangspunkt wie folgt vermerkt:

```text
abc...123:0
```

Der Outpoint wird in den Inputs (`vin`) einer neuen Transaktion verwendet, um anzugeben, welcher UTXO ausgegeben wird.

> ► *Der Begriff "Outpoint" wird oft synonym mit "UTXO "* verwendet