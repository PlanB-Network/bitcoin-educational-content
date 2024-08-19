---
term: DANDELION
---

Ein Vorschlag, der darauf abzielt, die Privatsphäre des Transaktionsroutings im Bitcoin-Netzwerk zu verbessern, um der Deanonymisierung entgegenzuwirken. Im Standardbetrieb von Bitcoin werden Transaktionen sofort an mehrere Knoten übertragen. Dieses Phänomen kann es Beobachtern potenziell ermöglichen, Transaktionen, die normalerweise anonym sind, mit IP-Adressen zu verknüpfen. Das Ziel von BIP156 ist es, dieses Problem anzugehen. Dazu führt es eine zusätzliche Phase im Übertragungsprozess ein, um die Anonymität vor der öffentlichen Verbreitung zu bewahren. So verwendet Dandelion zunächst eine "Stem"-Phase (Stiel-Phase), in der die Transaktion über einen zufälligen Pfad von Knoten gesendet wird, bevor sie in der "Fluff"-Phase (Pusteblumen-Phase) an das gesamte Netzwerk übertragen wird. Die Begriffe Stem und Fluff beziehen sich auf das Verhalten der Transaktionsverbreitung durch das Netzwerk, das der Form eines Löwenzahns ähnelt. Diese Routing-Methode verschleiert die Spur zurück zum Quellknoten, was es schwierig macht, eine Transaktion durch das Netzwerk bis zu ihrem Ursprung zurückzuverfolgen.

![](../../dictionnaire/assets/36.png)