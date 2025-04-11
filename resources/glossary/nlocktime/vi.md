---
term: NLOCKTIME

---
An embedded field in transactions that sets a time-based condition before which the transaction cannot be added to a valid block. This parameter allows specifying an exact time (Unix timestamp) or a specific number of blocks as a condition for the transaction to be considered valid. Thus, it is an absolute timelock (not relative). The `nLockTime` affects the entire transaction and effectively enables time verification, whereas the opcode `OP_CHECKLOCKTIMEVERIFY` only allows comparing the top value of the stack with the `nLockTime` value.