---
term: BATTERY
---

In the context of the scripting language used to affix spending conditions to Bitcoin UTXOs, the stack is a LIFO (*Last In, First Out*) data structure used to store temporary elements during script execution. Each operation in the script manipulates these stacks, where elements can be added (*push*) or removed (*pop*). Scripts use stacks to evaluate expressions, store temporary variables and manage conditions.

When executing a Bitcoin script, 2 stacks can be used: the main stack and the alt (alternative) stack. The main stack is used for the majority of script operations. It is on this stack that script operations add, remove or manipulate data. The alternative stack, on the other hand, is used to temporarily store data during script execution. Specific opcodes, such as `OP_TOALTSTACK` and `OP_FROMALTSTACK`, allow you to transfer elements from the main stack to the alternate stack and vice versa.

For example, when a transaction is validated, signatures and public keys are pushed onto the main stack and processed by successive opcodes to verify that the signatures match the transaction keys and data.