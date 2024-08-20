---
término: ADDR
---

Mensaje de red utilizado anteriormente en Bitcoin para comunicar las direcciones de nodos que aceptan conexiones entrantes. Este formato antiguo, limitado a 128 bits por dirección, solo era adecuado para direcciones IPv6, IPv4 y Tor versión 2. Con la llegada de nuevos protocolos como Tor V3 y la necesidad de una mejor escalabilidad para futuros protocolos de red, el formato `addr` fue superado por `addrv2`, introducido en BIP155.