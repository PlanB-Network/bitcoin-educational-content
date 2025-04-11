---
term: OP_EQUALVERIFY (0X88)

---
Combines the functions of `OP_EQUAL` and `OP_VERIFY`. It first checks the equality of the top two values on the stack, then requires that the result is non-zero, otherwise, the transaction is invalid. `OP_EQUALVERIFY` is notably used in address verification scripts.