---
term: OP_RETURN (0X6A)
definition: Opcode making an output unspendable, often used to record arbitrary data.
---

Indicates an invalid script, making the output that contains it provably unspendable. Network nodes can thus remove this output from their UTXO set. `OP_RETURN` is often used to record arbitrary data in the blockchain.