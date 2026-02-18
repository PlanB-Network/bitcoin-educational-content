---
term: OP_EQUALVERIFY (0X88)

definition: Kết hợp OP_EQUAL và OP_VERIFY, làm cho giao dịch không hợp lệ nếu các giá trị khác nhau.
---
Combines the functions of `OP_EQUAL` and `OP_VERIFY`. It first checks the equality of the top two values on the stack, then requires that the result is non-zero, otherwise, the transaction is invalid. `OP_EQUALVERIFY` is notably used in address verification scripts.