---
term: ADDRV2
---

Vorgeschlagene Weiterentwicklung mit BIP155 der `addr`-Nachricht im Bitcoin-Netzwerk. Die `addr`-Nachricht wurde verwendet, um Knotenadressen zu übertragen, die eingehende Verbindungen akzeptieren, war jedoch auf 128-Bit-Adressen beschränkt. Diese Größe war ausreichend für IPv6, IPv4 und Tor V2 Adressen, jedoch unzureichend für andere Protokolle. Die aktualisierte Version `addrv2` ist darauf ausgelegt, längere Adressen zu unterstützen, einschließlich 256-Bit Tor v3 versteckte Dienste, sowie andere Netzwerkprotokolle wie I2P oder zukünftige Protokolle.