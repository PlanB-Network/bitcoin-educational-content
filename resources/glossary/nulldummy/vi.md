---
term: NULLDUMMY
---

Quy tắc đồng thuận được giới thiệu với BIP147 trong bản nâng cấp mềm SegWit yêu cầu phần tử giả (dummy element) được sử dụng trong các opcode `OP_CHECKMULTISIG` và `OP_CHECKMULTISIGVERIFY` phải là một mảng byte trống (`OP_0`). Biện pháp này được thực hiện để loại bỏ một vector dễ bị biến đổi bằng cách cấm bất kỳ giá trị nào khác ngoài `OP_0` cho phần tử này.