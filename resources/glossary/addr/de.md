---
term: ADDR

---
Netzwerknachricht, die früher bei Bitcoin verwendet wurde, um die Adressen von Knoten zu kommunizieren, die eingehende Verbindungen akzeptieren. Dieses alte Format, das auf 128 Bit pro Adresse begrenzt war, war nur für IPv6, IPv4 und Tor-Adressen der Version 2 geeignet. Mit dem Aufkommen neuer Protokolle wie Tor V3 und der Notwendigkeit einer besseren Skalierbarkeit für zukünftige Netzwerkprotokolle wurde das `addr`-Format durch `addrv2` ersetzt, das in BIP155 eingeführt wurde.