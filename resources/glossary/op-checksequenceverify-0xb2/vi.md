---
term: OP_CHECKSEQUENCEVERIFY (0XB2)

---
Renders the transaction invalid if any one of these characteristics is observed:


- The stack is empty;
- The value at the top of the stack is less than `0`;
- The disable flag for the value at the top of the stack is undefined and; The transaction version is less than `2` or; The disable flag for the `nSequence` field of the input is set or; The timelock type is not the same between the `nSequence` field and the value at the top of the stack (real time or number of blocks) or; The value at the top of the stack is greater than the value of the `nSequence` field of the input.

If one or more of these characteristics is observed, the script containing the `OP_CHECKSEQUENCEVERIFY` cannot be satisfied. If all conditions are valid, then `OP_CHECKSEQUENCEVERIFY` acts as an `OP_NOP`, meaning it does not perform any action on the script. It's as if it disappears. `OP_CHECKSEQUENCEVERIFY` thus imposes a relative time constraint on the spending of the UTXO secured with the script containing it. It can do this either in the form of real time or as a number of blocks. To do this, it restricts the possible values for the `nSequence` field of the input spending it, and this `nSequence` field itself restricts when the transaction that includes this input can be included in a block.

> ► *This opcode is a replacement for `OP_NOP`. It was placed on `OP_NOP3`. It is often referred to by its acronym "CSV". Note, `OP_CSV` should not be confused with the `nSequence` field of a transaction. The former uses the latter, but their natures and actions are different.*