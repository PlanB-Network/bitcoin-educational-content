---
term: ENTROPIE (ANALYSE)

---
Im spezifischen Kontext der Kettenanalyse ist Entropie auch der Name eines Indikators, der von der Shannon-Entropie abgeleitet ist und von LaurentMT erfunden wurde. Dieser Indikator ermöglicht es, den Mangel an Wissen zu messen, den Analysten über die genaue Konfiguration einer Bitcoin-Transaktion haben. Mit anderen Worten: Je höher die Entropie einer Transaktion ist, desto schwieriger ist es für Analysten, die Bewegungen von Bitcoins zwischen Ein- und Ausgängen zu identifizieren.

In der Praxis gibt die Entropie Aufschluss darüber, ob eine Transaktion aus der Sicht eines externen Beobachters mehrere mögliche Interpretationen aufweist, die allein auf der Menge der Ein- und Ausgaben beruhen, ohne andere externe oder interne Muster und Heuristiken zu berücksichtigen. Eine hohe Entropie ist dann gleichbedeutend mit einer besseren Vertraulichkeit der Transaktion.

Die Entropie ist definiert als der binäre Logarithmus der Anzahl der möglichen Kombinationen. Hier ist die verwendete Formel, wobei $E$ die Entropie der Transaktion und $C$ die Anzahl der möglichen Interpretationen darstellt:

$$
E = \log_2(C)
$$

Unter Berücksichtigung der Werte der an der Transaktion beteiligten UTXOs stellt die Anzahl der Interpretationen $C$ die Anzahl der Möglichkeiten dar, auf die Inputs mit Outputs verbunden werden können. Mit anderen Worten, sie bestimmt die Anzahl der Interpretationen, die eine Transaktion aus der Sicht eines externen Beobachters, der sie analysiert, hervorrufen kann.