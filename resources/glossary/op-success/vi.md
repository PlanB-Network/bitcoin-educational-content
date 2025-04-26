---
term: OP_SUCCESS

---
The `OP_SUCCESS` represent a series of opcodes that were disabled in the past and are now reserved for future use in Tapscript. Their ultimate goal is to facilitate updates and extensions of the script language, by allowing the introduction of new functionalities via soft forks. When one of these opcodes is encountered in a script, it indicates an automatic success of that part of the script, regardless of the data or conditions present. This means that the script continues its execution without failure, independent of the previous operations.

Thus, when a new opcode is added on an `OP_SUCCESS`, it necessarily represents the addition of a more restrictive rule than the previous one. Updated nodes can then verify the compliance with this rule, and nodes not updated will not refuse the associated transactions and the blocks that include them, because the `OP_SUCCESS` validates that part of the script. Therefore, there is no hard fork.

In comparison, the `OP_NOP` (*No Operation*) also serve as placeholders in the script, but they have no effect on the execution of the script. When an `OP_NOP` is encountered, the script simply continues without altering the state of the stack or the progression of the script. The key difference, therefore, is in their impact on execution: `OP_SUCCESS` guarantees a successful passage through that portion of the script, while `OP_NOP` is neutral, and does not affect either the stack or the flow of the script. These opcodes are designated by `OP_SUCCESSN` where `N` is a number used to differentiate the `OP_SUCCESS`.