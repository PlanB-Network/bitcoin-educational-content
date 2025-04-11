---
term: OP_WITHIN (0XA5)

---
Checks if the top element on the stack is within the range defined by the second and third top elements. In other words, `OP_WITHIN` checks if the top element is greater than or equal to the second and less than the third. If this condition is true, it pushes `1` (true) onto the stack, otherwise, it pushes `0` (false).