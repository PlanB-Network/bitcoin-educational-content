---
term: SWEEP-TRANSAKTION

---
Muster oder Transaktionsmodell, das in der Kettenanalyse verwendet wird, um die Art der Transaktion zu bestimmen. Dieses Modell ist gekennzeichnet durch den Verbrauch eines einzigen UTXO als Input und die Produktion eines einzigen UTXO als Output. Die Interpretation dieses Modells ist, dass es sich um einen Selbsttransfer handelt. Der Nutzer hat seine Bitcoins auf sich selbst übertragen, auf eine andere Adresse, die er besitzt. Da sich an der Transaktion nichts ändert, ist es sehr unwahrscheinlich, dass wir es mit einer Zahlung zu tun haben. Bei einer Zahlung ist es nämlich fast unmöglich, dass der Zahler über einen UTXO verfügt, der genau dem vom Verkäufer geforderten Betrag entspricht, abgesehen von den Transaktionsgebühren. Im Allgemeinen ist der Zahler daher gezwungen, einen Wechselgeldbetrag auszugeben. Wir wissen dann, dass der beobachtete Nutzer wahrscheinlich noch im Besitz dieses UTXO ist. Wenn wir im Rahmen einer Kettenanalyse wissen, dass der in der Transaktion als Input verwendete UTXO Alice gehört, können wir davon ausgehen, dass auch der UTXO im Output ihr gehört.

![](../../dictionnaire/assets/6.webp)

> ► *Im Französischen könnte "sweep transaction" mit "transaction de balayage" übersetzt werden.*