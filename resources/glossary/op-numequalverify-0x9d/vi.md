---
term: OP_NUMEQUALVERIFY (0X9D)

---
Combines the operations `OP_NUMEQUAL` and `OP_VERIFY`. It numerically compares the two topmost elements on the stack. If the values are equal, `OP_NUMEQUALVERIFY` removes the true result from the stack and continues the script's execution. If the values are not equal, the result is false, and the script immediately fails.