---
term: OP_VERIFY (0X69)

definition: Opcode yêu cầu đỉnh của ngăn xếp phải khác không, nếu không giao dịch sẽ không hợp lệ.
---
Requires that the top stack value is non-zero (true). The transaction is invalid if this is not the case. `OP_VERIFY` is used to confirm script conditions.