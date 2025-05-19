---
term: PATHFINDING
---

Verfahren, mit dem ein Knoten den optimalen Pfad für die Weiterleitung einer Zahlung durch das Lightning-Channel-Netz ermittelt. Die Pfadfindung erfolgt durch den Knoten des Zahlers, der die am besten geeigneten Zwischenknoten auswählen muss, um den Empfänger zu erreichen. Diese Auswahl basiert auf einer Reihe von Kriterien, wie z. B. Gebühren, Kanalkapazität und Timelocks.


Pfadfindungsalgorithmen erstellen aus den Gossip-Daten einen Graphen der Netztopologie und bewerten die verschiedenen möglichen Routen zwischen dem Zahler- und dem Empfängerknoten. Diese Routen werden nach verschiedenen Kriterien von der besten zur schlechtesten eingestuft. Der Knoten testet dann diese Routen, bis es ihm gelingt, die Zahlung auf einer dieser Routen vorzunehmen.