---
term: DANDELION

---
Ein Vorschlag, der darauf abzielt, die Privatsphäre bei der Weiterleitung von Transaktionen im Bitcoin-Netzwerk zu verbessern, um einer Deanonymisierung entgegenzuwirken. Im Standardbetrieb von Bitcoin werden Transaktionen sofort an mehrere Knotenpunkte weitergeleitet. Dieses Phänomen kann es Beobachtern ermöglichen, Transaktionen, die normalerweise anonym sind, mit IP-Adressen zu verknüpfen. Das Ziel von BIP156 ist es, dieses Problem zu lösen. Zu diesem Zweck führt es eine zusätzliche Phase in den Übertragungsprozess ein, um die Anonymität vor der öffentlichen Verbreitung zu wahren. So verwendet Dandelion zunächst eine "Stem"-Phase, in der die Transaktion durch einen zufälligen Pfad von Knoten gesendet wird, bevor sie in der "Fluff"-Phase an das gesamte Netzwerk gesendet wird. Der Stamm und die Fluff-Phase beziehen sich auf das Verhalten bei der Ausbreitung der Transaktion durch das Netzwerk und ähneln der Form einer Pusteblume. Diese Routing-Methode verwischt die Spur, die zum Ursprungsknoten zurückführt, und erschwert die Rückverfolgung einer Transaktion durch das Netz bis zu ihrem Ursprung.

![](../../dictionnaire/assets/36.webp)