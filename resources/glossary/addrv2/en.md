---
term: ADDRV2
---

An improvement introduced with BIP155 to the `addr` message on the Bitcoin network. The `addr` message was used to broadcast the addresses of nodes that accept incoming connections, but it was limited to 128-bit addresses. This size was adequate for IPv6, IPv4, and Tor V2 addresses, but too short for other protocols. The updated version `addrv2` is designed to support longer addresses, including 256-bit Tor v3 hidden services, as well as other network protocols such as I2P and potential future ones.