---
term: Addrv2

definition: Ein neues Netzwerk-Nachrichtenformat (BIP155) zum Verbreiten von Adressen von Bitcoin-Knoten. Unterstützt längere Adressen wie Tor v3 oder I2P.
---
Vorgeschlagene Entwicklung mit BIP155 der "addr"-Nachricht im Bitcoin-Netzwerk. Die "addr"-Nachricht wurde verwendet, um Knotenadressen zu verbreiten, die eingehende Verbindungen akzeptieren, aber sie war auf 128-Bit-Adressen beschränkt. Diese Größe war ausreichend für IPv6-, IPv4- und Tor-V2-Adressen, aber nicht ausreichend für andere Protokolle. Die aktualisierte Version `addrv2` wurde entwickelt, um längere Adressen zu unterstützen, einschließlich 256-bit Tor v3 versteckte Dienste, sowie andere Netzwerkprotokolle wie I2P oder zukünftige Protokolle.