---
term: BIP156

---
Vorschlag, bekannt als "Dandelion", der darauf abzielt, die Privatsphäre bei der Weiterleitung von Transaktionen im Bitcoin-Netzwerk zu verbessern, um einer Deanonymisierung entgegenzuwirken. Im Standardbetrieb von Bitcoin werden die Transaktionen sofort an mehrere Knoten weitergeleitet. Wenn ein Beobachter in der Lage ist, jede Transaktion zu sehen, die von jedem Knoten im Netzwerk weitergeleitet wird, könnte er annehmen, dass der erste Knoten, der eine Transaktion sendet, auch der Ursprungsknoten dieser Transaktion ist, und dass sie daher vom Betreiber dieses Knotens stammt. Dieses Phänomen könnte es Beobachtern ermöglichen, Transaktionen, die normalerweise anonym sind, mit IP-Adressen zu verknüpfen.

Das Ziel von BIP156 ist es, dieses Problem zu lösen. Zu diesem Zweck führt es eine zusätzliche Phase in die Übertragung ein, um die Anonymität vor der öffentlichen Verbreitung zu wahren. So verwendet Dandelion zunächst eine "Stem"-Phase, in der die Transaktion durch einen zufälligen Pfad von Knoten gesendet wird, bevor sie in der "Fluff"-Phase an das gesamte Netzwerk gesendet wird. Der "stem" und der "fluff" beziehen sich auf das Verhalten bei der Ausbreitung der Transaktion durch das Netzwerk und ähneln der Form einer Pusteblume (*a dandelion* auf Englisch).

Diese Routing-Methode verwischt die Spur, die zum Ursprungsknoten zurückführt, und erschwert so die Rückverfolgung einer Transaktion durch das Netz bis zu ihrem Ursprung. Dandelion verbessert somit die Privatsphäre, indem es die Möglichkeiten der Angreifer, das Netzwerk zu deanonymisieren, einschränkt. Diese Methode ist sogar noch effektiver, wenn die Transaktion während der "Stamm"-Phase einen Knoten durchquert, der seine Netzwerkkommunikation verschlüsselt, wie z. B. Tor oder *P2P Transport V2*. BIP156 ist noch nicht zu Bitcoin Core hinzugefügt worden.

![](../../dictionnaire/assets/36.webp)