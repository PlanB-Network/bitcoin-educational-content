---
term: OP_CHECKHASHVERIFY (CHV)
---

Một opcode mới được đề xuất vào năm 2012 trong BIP17 bởi Luke Dashjr, có chức năng tương tự như `OP_EVAL` hoặc P2SH. Opcode này được thiết kế để băm phần cuối của `scriptSig`, so sánh kết quả với phần trên cùng của stack, và làm cho giao dịch trở nên không hợp lệ nếu hai bản băm không khớp nhau. Opcode này chưa bao giờ được triển khai.