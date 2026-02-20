---
term: BIP0112
definition: Introduction of the OP_CHECKSEQUENCEVERIFY (CSV) opcode allowing relative timelocks to be created in scripts.
---

Introduces the opcode `OP_CHECKSEQUENCEVERIFY` (CSV) in the Bitcoin Script language. This opcode allows the creation of transactions that are only valid after a relative delay from a previous transaction, defined either by the number of blocks or by elapsed time. `OP_CHECKSEQUENCEVERIFY` compares the value at the top of the stack with the `nSequence` value  of the input. 
If it is greater and all other conditions are met, the script is valid. Effectively, `OP_CHECKSEQUENCEVERIFY` restricts the values allowed for the input's `nSequence` field, which in turn restricts when the transaction containing that input can be confirmed in a block. BIP112 was introduced via a soft fork on July 4, 2016, alongside BIP68 and BIP113, activated for the first time using the BIP9 method.

