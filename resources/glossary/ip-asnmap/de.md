---
term: IP_ASN.MAP
---

Datei, die in Bitcoin Core verwendet wird, um die ASMAP zu speichern, welche die Gruppierung (d.h. Bucketing) von IP-Adressen durch die Verwendung von Autonomen Systemnummern (ASN) verbessert. Anstatt ausgehende Verbindungen nach IP-Netzwerkpräfixen (/16) zu gruppieren, ermöglicht diese Datei eine Diversifizierung der Verbindungen, indem eine IP-Adressierungskarte zu ASNs erstellt wird, die eindeutige Kennungen für jedes Netzwerk im Internet sind. Die Idee ist, die Sicherheit und Topologie des Bitcoin-Netzwerks zu verbessern, indem Verbindungen diversifiziert werden, um gegen bestimmte Angriffe (insbesondere den Erebus-Angriff) zu schützen.