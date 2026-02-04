---
term: OP_VERIFY (0X69)
definition: Opcode requiring the top of the stack to be non-zero, otherwise the transaction is invalid.
---

Requires that the top stack value is non-zero (true). The transaction is invalid if this is not the case. `OP_VERIFY` is used to confirm script conditions.