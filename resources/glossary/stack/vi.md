---
term: STACK

---
In the context of the scripting language used to apply spending conditions on Bitcoin UTXOs, the stack is a "LIFO" (*Last In, First Out*) data structure that serves to store temporary elements during the execution of a script. Each operation in the script manipulates these stacks, where elements can be added (*push*) or removed (*pop*). Scripts use stacks to evaluate expressions, store temporary variables, and manage conditions.

During the execution of a Bitcoin script, 2 stacks can be used: the main stack and the alt (alternative) stack. The main stack is used for the majority of a script's operations. It is on this stack that script operations add, remove, or manipulate data. The alternative stack, on the other hand, serves to temporarily store data during the script's execution. Specific opcodes, like `OP_TOALTSTACK` and `OP_FROMALTSTACK`, allow for the transfer of elements from the main stack to the alternative stack and vice versa.

For example, during the validation of a transaction, signatures and public keys are pushed onto the main stack and processed by successive opcodes to verify that the signatures match the keys and the transaction data.

> ► *In English, the translation of « pile » is « stack ». The English term is generally used even in French during technical discussions.*