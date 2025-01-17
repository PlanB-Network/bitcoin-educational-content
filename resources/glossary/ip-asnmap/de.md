---
term: IP_ASN.MAP

---
Datei, die in Bitcoin Core verwendet wird, um die ASMAP zu speichern, die das Bucketing (d.h. die Gruppierung) von IP-Adressen verbessert, indem sie sich auf Autonomous System Numbers (ASN) stützt. Anstatt ausgehende Verbindungen nach IP-Netzwerk-Präfixen (/16) zu gruppieren, ermöglicht diese Datei die Diversifizierung von Verbindungen durch die Erstellung einer IP-Adressierungskarte zu ASNs, die eindeutige Bezeichner für jedes Netzwerk im Internet sind. Die Idee ist, die Sicherheit und die Topologie des Bitcoin-Netzwerks zu verbessern, indem Verbindungen diversifiziert werden, um sich gegen bestimmte Angriffe (insbesondere den Erebus-Angriff) zu schützen.