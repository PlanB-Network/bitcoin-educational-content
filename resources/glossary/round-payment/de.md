---
term: RUNDUMZAHLUNG

---
Eine interne Heuristik für die Kettenanalyse bei Bitcoin, die eine Hypothese über die Art der Ausgaben einer Transaktion auf der Grundlage von runden Beträgen ermöglicht. Im Allgemeinen gilt bei einem einfachen Zahlungsmuster (1 Eingang und 2 Ausgänge), dass wenn einer der Ausgänge einen runden Betrag ausgibt, er die Zahlung darstellt. Wenn ein Ausgang die Zahlung darstellt, steht der andere für das Wechselgeld. Daraus lässt sich ableiten, dass der Benutzer, der die Transaktion eingibt, wahrscheinlich noch im Besitz der Ausgabe ist, die als Wechselgeld identifiziert wurde.

Es ist anzumerken, dass diese Heuristik nicht immer anwendbar ist, da die meisten Zahlungen immer noch in Fiat-Währungseinheiten getätigt werden. Wenn ein Händler in Frankreich Bitcoin annimmt, zeigt er in der Regel keine stabilen Preise in Sats an. Vielmehr entscheiden sie sich für eine Umrechnung zwischen dem Preis in Euro und dem Betrag in Bitcoins, der über ihr POS-System (wie z. B. BTCPay Server) zu zahlen ist. Daher sollte es keine runde Zahl in der Transaktionsausgabe geben. Dennoch könnte ein Analyst versuchen, diese Umrechnung vorzunehmen, indem er den Wechselkurs berücksichtigt, der zum Zeitpunkt der Übertragung der Transaktion im Netzwerk gültig war. Wenn der Bitcoin eines Tages die bevorzugte Rechnungseinheit an unseren Börsen wird, könnte diese Heuristik für Analysen noch nützlicher werden.

![](../../dictionnaire/assets/11.webp)