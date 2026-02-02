---
term: Addr
definition: An old Bitcoin network message that allowed communicating IP addresses of nodes accepting connections. Replaced by addrv2 (BIP155) to support longer address formats.
---

Network message previously used in Bitcoin to broadcast the addresses of nodes that accept incoming connections. This original format, limited to 128 bits per address, was only suitable for IPv6, IPv4, and version 2 Tor addresses. With the emergence of new protocols like Tor V3 and the need for improved scalability for future network protocols, the `addr` format was replaced by `addrv2`, introduced in BIP155.