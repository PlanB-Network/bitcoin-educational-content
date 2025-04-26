---
term: OP_CHECKLOCKTIMEVERIFY (0XB1)

---
Makes the transaction invalid unless all these conditions are met:


- The stack is not empty;
- The value at the top of the stack is greater than or equal to `0`;
- The type of timelock is the same between the `nLockTime` field and the value at the top of the stack (real time or block number);
- The `nSequence` field of the input is not equal to `0xffffffff`;
- The value at the top of the stack is greater than or equal to the value of the `nLockTime` field of the transaction.

If any one of these conditions is not met, the script containing the `OP_CHECKLOCKTIMEVERIFY` cannot be satisfied. If all these conditions are valid, then `OP_CHECKLOCKTIMEVERIFY` acts as an `OP_NOP`, meaning it does not perform any action on the script. It's as if it disappears. `OP_CHECKLOCKTIMEVERIFY` thus imposes a time constraint on the spending of the UTXO secured with the script containing it. It can do this either in the form of a Unix time date or as a block number. To do this, it restricts the possible values for the `nLockTime` field of the transaction spending it, and this `nLockTime` field itself restricts when the transaction can be included in a block.

> ► *This opcode is a replacement for `OP_NOP`. It was placed on `OP_NOP2`. It is often referred to by its acronym "CLTV". Note, `OP_CLTV` should not be confused with the `nLockTime` field of a transaction. The former uses the latter, but their natures and actions are different.*