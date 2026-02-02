---
term: BIP0031
definition: Introduction of the pong message in response to ping to verify connectivity between nodes in the Bitcoin network.
---

A proposal aimed at improving Bitcoin node's network management mechanisms. Before BIP31, Bitcoin nodes had no direct way to determine whether their peers were still connected, responsive, and not overloaded. BIP31 introduced the use of a `pong` message, in response to a `ping` message, enabling active connectivity checks between nodes.