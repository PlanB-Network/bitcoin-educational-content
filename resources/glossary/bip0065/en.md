---
term: BIP0065
definition: Introduction of the OP_CHECKLOCKTIMEVERIFY opcode allowing bitcoins to be locked until a specific date or block height.
---

Introduced a new opcode named `OP_CHECKLOCKTIMEVERIFY` which allows a UTXO to be locked and remain unusable until a specified future time. 
The implementation of this BIP required a soft fork, which occurred on December 14, 2015. It also introduced block version 4.

