---
term: OP_CHECKMULTISIGVERIFY (0XAF)

definition: Kết hợp OP_CHECKMULTISIG và OP_VERIFY, dừng tập lệnh nếu xác minh thất bại.
---
Combines an `OP_CHECKMULTISIG` and an `OP_VERIFY`. It takes multiple signatures and public keys to verify that `M` out of `N` signatures are valid, just as `OP_CHECKMULTISIG` does. Then, like `OP_VERIFY`, if the verification fails, the script immediately stops with an error. If the verification is successful, the script continues without pushing any value onto the stack. This opcode was removed in Tapscript.