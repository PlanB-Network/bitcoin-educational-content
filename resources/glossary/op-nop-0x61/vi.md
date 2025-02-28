---
term: OP_NOP (0X61)

---
Produces no effect on the stack or the script's state. It performs no movement, checks, or modifications. It simply does nothing unless decided otherwise via a soft fork. Indeed, since their modification by Satoshi Nakamoto in 2010, the `OP_NOP` commands (`OP_NOP1` (`0XB0`) to `OP_NOP10` (`0XB9`)) are used to add new opcodes in the form of a soft fork.

Thus, `OP_NOP2` (`0XB1`) and `OP_NOP3` (`0XB2`) have already been used to implement `OP_CHECKLOCKTIMEVERIFY` and `OP_CHECKSEQUENCEVERIFY`, respectively. They are used in combination with `OP_DROP` to remove the associated temporal values from the stack, thereby allowing the script's execution to continue, whether the node is up-to-date or not. The `OP_NOP` commands, therefore, allow the insertion of an interruption point in a script to check for additional conditions that already exist or may be added with future soft forks. Since Tapscript, the use of `OP_NOP` has been replaced by the more efficient `OP_SUCCESS`.