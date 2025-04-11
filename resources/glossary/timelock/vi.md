---
term: TIMELOCK

---
A smart contract primitive that allows setting a time-based condition that must be met for a transaction to be added to a block. There are two types of timelocks on Bitcoin:


- The absolute timelock, which specifies an exact moment before which the transaction cannot be included in a block;
- The relative timelock, which sets a delay from the acceptance of a previous transaction.

The timelock can be defined either as a date expressed in Unix time or as a block number. Finally, the timelock can apply to a transaction output by using a specific opcode in the locking script (`OP_CHECKLOCKTIMEVERIFY` or `OP_CHECKSEQUENCEVERIFY`), or to an entire transaction by using specific transaction fields (`nLockTime` or `nSequence`).