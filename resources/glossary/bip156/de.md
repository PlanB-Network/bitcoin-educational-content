---
term: BIP156
---

Vorschlag, bekannt als Dandelion, der darauf abzielt, die Privatsphäre des Routings von Transaktionen im Bitcoin-Netzwerk zu verbessern, um der Deanonymisierung entgegenzuwirken. Im Standardbetrieb von Bitcoin werden Transaktionen sofort an mehrere Knoten übertragen. Wenn ein Beobachter jede Transaktion sehen kann, die von jedem Knoten im Netzwerk weitergeleitet wird, könnte er annehmen, dass der erste Knoten, der eine Transaktion sendet, auch der Ursprungsknoten dieser Transaktion ist und daher vom Betreiber des Knotens stammt. Dieses Phänomen könnte es Beobachtern potenziell ermöglichen, Transaktionen, die normalerweise anonym sind, mit IP-Adressen zu verknüpfen.

Das Ziel von BIP156 ist es, dieses Problem anzugehen. Um dies zu tun, führt es eine zusätzliche Phase in der Übertragung ein, um die Anonymität vor der öffentlichen Verbreitung zu bewahren. So verwendet Dandelion zunächst eine "Stem"-Phase, in der die Transaktion über einen zufälligen Pfad von Knoten gesendet wird, bevor sie in der "Fluff"-Phase an das gesamte Netzwerk übertragen wird. Stem und Fluff sind Referenzen auf das Verhalten der Ausbreitung der Transaktion durch das Netzwerk, ähnlich der Form eines Löwenzahns (*a dandelion* auf Englisch).

Diese Routing-Methode verschleiert den Weg zurück zum Quellknoten, was es schwierig macht, eine Transaktion durch das Netzwerk zurück zu ihrem Ursprung zu verfolgen. Dandelion verbessert somit die Privatsphäre, indem es die Fähigkeit der Gegner einschränkt, das Netzwerk zu deanonymisieren. Diese Methode ist noch effektiver, wenn die Transaktion während der "Stem"-Phase einen Knoten durchquert, der seine Netzwerkkommunikation verschlüsselt, wie z.B. mit Tor oder *P2P Transport V2*. BIP156 wurde noch nicht zu Bitcoin Core hinzugefügt.

![](../../dictionnaire/assets/36.png)