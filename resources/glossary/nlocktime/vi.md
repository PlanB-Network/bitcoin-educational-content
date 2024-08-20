---
term: NLOCKTIME
---

Một trường nhúng trong các giao dịch đặt ra một điều kiện dựa trên thời gian trước khi giao dịch không thể được thêm vào một khối hợp lệ. Tham số này cho phép chỉ định một thời gian cụ thể (dấu thời gian Unix) hoặc một số lượng khối cụ thể như một điều kiện để giao dịch được coi là hợp lệ. Do đó, đây là một khóa thời gian tuyệt đối (không tương đối). `nLockTime` ảnh hưởng đến toàn bộ giao dịch và hiệu quả cho phép xác minh thời gian, trong khi opcode `OP_CHECKLOCKTIMEVERIFY` chỉ cho phép so sánh giá trị hàng đầu của ngăn xếp với giá trị `nLockTime`.