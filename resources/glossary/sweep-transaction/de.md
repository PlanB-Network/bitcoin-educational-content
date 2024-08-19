---
term: SWEEP TRANSACTION
---

Muster oder Transaktionsmodell, das in der Kettenanalyse verwendet wird, um die Natur der Transaktion zu bestimmen. Dieses Modell zeichnet sich durch den Verbrauch eines einzelnen UTXO als Eingabe und die Erzeugung eines einzelnen UTXO als Ausgabe aus. Die Interpretation dieses Modells ist, dass wir in Anwesenheit einer Selbstübertragung sind. Der Benutzer hat seine Bitcoins an sich selbst, an eine andere Adresse, die er besitzt, übertragen. Da es bei der Transaktion keine Änderung gibt, ist es sehr unwahrscheinlich, dass wir es mit einer Zahlung zu tun haben. Tatsächlich ist es fast unmöglich, dass der Zahler ein UTXO besitzt, das genau dem vom Verkäufer geforderten Betrag entspricht, zusätzlich zu den Transaktionsgebühren. In der Regel ist der Zahler daher gezwungen, ein Änderungsausgang zu produzieren. Wir wissen dann, dass der beobachtete Benutzer wahrscheinlich immer noch im Besitz dieses UTXO ist. Im Kontext einer Kettenanalyse, wenn wir wissen, dass das UTXO, das als Eingabe in der Transaktion verwendet wird, Alice gehört, können wir annehmen, dass das UTXO in der Ausgabe ihr ebenfalls gehört.

![](../../dictionnaire/assets/6.png)

> ► *Auf Französisch könnte "sweep transaction" als "transaction de balayage" übersetzt werden.*