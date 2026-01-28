---
term: OP_CHECKHASHVERIFY (CHV)

definition: Mã vận hành được đề xuất vào năm 2012 cho các chức năng tương tự như P2SH, chưa bao giờ được triển khai.
---
A new opcode proposed in 2012 in BIP17 by Luke Dashjr that would offer the same functionalities as `OP_EVAL` or P2SH. It was intended to hash the end of the `scriptSig`, compare the result with the top of the stack, and render the transaction invalid if the two hashes did not match. This opcode was never implemented.