---
term: OP_ROLL (0X7A)

---
Moves an item from the stack to the top of the stack, based on the depth specified by the value at the top of the stack before the operation. For example, if the value at the top of the stack is `4`, `OP_ROLL` will select the fourth item from the top of the stack, and it will move this value to the top. `OP_ROLL` serves the same function as `OP_PICK`, except that it removes the item from its original position.