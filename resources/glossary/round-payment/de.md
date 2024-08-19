---
term: ROUND PAYMENT
---

Eine interne Heuristik für die Kettenanalyse bei Bitcoin, die eine Hypothese über die Natur der Ausgänge einer Transaktion auf Basis von runden Beträgen zulässt. Allgemein gilt, wenn man mit einem einfachen Zahlungsmuster konfrontiert wird (1 Eingang und 2 Ausgänge), dass, wenn einer der Ausgänge einen runden Betrag ausgibt, dieser den Zahlungsbetrag darstellt. Durch Eliminierung, wenn ein Ausgang die Zahlung repräsentiert, stellt der andere das Wechselgeld dar. Es kann daher interpretiert werden, dass es wahrscheinlich ist, dass der Benutzer, der die Transaktion eingibt, den als Wechselgeld identifizierten Ausgang noch besitzt.

Es sollte beachtet werden, dass diese Heuristik nicht immer anwendbar ist, da die Mehrheit der Zahlungen immer noch in Fiat-Währungseinheiten getätigt wird. Tatsächlich, wenn ein Händler in Frankreich Bitcoin akzeptiert, zeigen sie in der Regel keine stabilen Preise in Sats an. Sie würden eher eine Umrechnung zwischen dem Preis in Euro und dem in Bitcoins zu zahlenden Betrag über ihr POS (wie BTCPay Server, zum Beispiel) bevorzugen. Daher sollte in dem Transaktionsausgang keine runde Zahl sein. Dennoch könnte ein Analyst versuchen, diese Umrechnung vorzunehmen, indem er den zum Zeitpunkt der Übertragung der Transaktion im Netzwerk geltenden Wechselkurs berücksichtigt. Wenn eines Tages Bitcoin zur bevorzugten Recheneinheit in unseren Austauschprozessen wird, könnte diese Heuristik noch nützlicher für Analysen werden.

![](../../dictionnaire/assets/11.png)