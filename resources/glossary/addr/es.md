---
term: ADDR

---
Mensaje de red utilizado antiguamente en Bitcoin para comunicar las direcciones de los nodos que aceptan conexiones entrantes. Este antiguo formato, limitado a 128 bits por dirección, sólo era adecuado para direcciones IPv6, IPv4 y la versión 2 de Tor. Con la llegada de nuevos protocolos como Tor V3 y la necesidad de una mejor escalabilidad para futuros protocolos de red, el formato `addr` fue reemplazado por `addrv2`, introducido en BIP155.