---
term: ADDR
---

Netzwerknachricht, die früher bei Bitcoin verwendet wurde, um die Adressen von Knoten zu kommunizieren, die eingehende Verbindungen akzeptieren. Dieses alte Format, begrenzt auf 128 Bits pro Adresse, war nur geeignet für IPv6, IPv4 und Version 2 Tor-Adressen. Mit der Ankunft neuer Protokolle wie Tor V3 und dem Bedarf an besserer Skalierbarkeit für zukünftige Netzwerkprotokolle wurde das `addr` Format durch `addrv2` ersetzt, eingeführt in BIP155.