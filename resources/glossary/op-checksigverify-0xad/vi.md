---
term: OP_CHECKSIGVERIFY (0XAD)

definition: Kết hợp OP_CHECKSIG và OP_VERIFY, dừng tập lệnh nếu chữ ký không hợp lệ.
---
Performs the same operation as `OP_CHECKSIG`, but if the signature verification fails, the script immediately halts with an error and the transaction is thus invalid. If the verification succeeds, the script continues without pushing a `1` (true) value onto the stack. In summary, `OP_CHECKSIGVERIFY` performs the operation `OP_CHECKSIG` followed by `OP_VERIFY`. This opcode was modified in Tapscript to verify Schnorr signatures.