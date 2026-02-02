---
term: OP_CHECKHASHVERIFY (CHV)
definition: Opcode proposed in 2012 for functionalities similar to P2SH, never implemented.
---

A new opcode proposed in 2012 in BIP17 by Luke Dashjr that would offer the same functionalities as `OP_EVAL` or P2SH. It was intended to hash the end of the `scriptSig`, compare the result with the top of the stack, and render the transaction invalid if the two hashes did not match. This opcode was never implemented.