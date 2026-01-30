---
term: BIP0385
definition: addr() and raw() functions for describing output scripts by address or in hexadecimal in descriptors.
---

Introduces the descriptor functions `addr(ADDR)` and `raw(HEX)`. The `addr(ADDR)` function allows describing an output script using a receiving address, while the `raw(HEX)` function enables specifying an output script using a raw hexadecimal representation of that script. BIP385 was implemented along with all other descriptor-related BIPs (except BIP386) in version 0.17 of Bitcoin Core.

