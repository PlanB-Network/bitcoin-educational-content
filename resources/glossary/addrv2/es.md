---
term: ADDRV2

---
Evolución propuesta con BIP155 del mensaje `addr` en la red Bitcoin. El mensaje `addr` se utilizaba para difundir direcciones de nodos que aceptan conexiones entrantes, pero estaba limitado a direcciones de 128 bits. Este tamaño era adecuado para direcciones IPv6, IPv4, y Tor V2, pero insuficiente para otros protocolos. La versión actualizada `addrv2` está diseñada para soportar direcciones más largas, incluyendo servicios ocultos Tor v3 de 256 bits, así como otros protocolos de red como I2P o futuros protocolos.