---
term: BIP0022
definition: JSON-RPC getblocktemplate standard allowing mining software to communicate with full nodes to construct blocks.
---

BIP proposed in 2012 by Luke Dashjr that introduces a standardized JSON-RPC method for external mining interfaces, called "getblocktemplate". As mining difficulty increased, the use of specialized external software for performing proof-of-work computations became more common.
BIP22 proposed a common communication standard for sharing block templates between full nodes and mining software. Unlike previous approaches that sent only the block header, this method sends the entire block structure, giving miners the ability to customize it before performing proof-of-work.