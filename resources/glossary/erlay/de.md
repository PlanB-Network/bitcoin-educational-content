---
term: ERLAY
---

Vorgeschlagenes Netzprotokoll zur Verbesserung der Effizienz der Weiterleitung von unbestätigten Transaktionen zwischen Bitcoin-Knoten.


Derzeit wird jede Transaktion über ein System verbreitet, bei dem jeder Knoten die Transaktion, die ihm bekannt ist, an alle seine Peers sendet. Das Problem ist, dass dies zu einer Menge Redundanz und Bandbreitennutzung für Duplikate führt. Viele Transaktionsübertragungen sind unnötig, da der Empfänger bereits über diese Transaktionen Bescheid weiß, und jeder Knoten muss nur einmal über jede Transaktion informiert werden. Erlay schlägt vor, die Anzahl der Peers, an die ein Knoten direkt Transaktionen sendet, die ihm bekannt sind, standardmäßig auf 8 zu begrenzen und dann einen auf der minisketch-Bibliothek basierenden Abstimmungsprozess zu verwenden, um fehlende Transaktionen effizienter zu teilen.


Erlay würde den Bandbreitenverbrauch um etwa 40 % senken, wodurch der Full node-Betrieb für Nutzer mit begrenzten Internetverbindungen zugänglicher würde und somit eine bessere Dezentralisierung des Netzes gefördert würde. Dieses Protokoll würde auch einen nahezu konstanten Bandbreitenverbrauch beibehalten, wenn die Anzahl der Verbindungen steigt. Dies bedeutet, dass es für die Betreiber von Knoten viel einfacher wäre, eine sehr große Anzahl von Verbindungen von ihren Kollegen zu akzeptieren, was die Sicherheit des Bitcoin-Netzes erhöhen würde, da das Risiko einer absichtlichen oder versehentlichen Partitionierung verringert würde. Außerdem würde Erlay es schwieriger machen, den Ursprungsknoten einer Transaktion zu bestimmen, was die Vertraulichkeit für Nutzer von Knoten, die nicht mit Tor arbeiten, erhöht.


Erlay wird in BIP330 vorgeschlagen.