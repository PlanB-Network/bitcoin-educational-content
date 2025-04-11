---
term: ADDR

---
Network message formerly used on Bitcoin to communicate the addresses of nodes that accept incoming connections. This old format, limited to 128 bits per address, was only suitable for IPv6, IPv4, and version 2 Tor addresses. With the arrival of new protocols such as Tor V3 and the need for better scalability for future network protocols, the `addr` format was superseded by `addrv2`, introduced in BIP155.