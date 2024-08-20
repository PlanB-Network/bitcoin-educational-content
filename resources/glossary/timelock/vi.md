---
term: TIMELOCK
---

Một nguyên tắc cơ bản của hợp đồng thông minh cho phép thiết lập một điều kiện dựa trên thời gian phải được thỏa mãn để một giao dịch được thêm vào một khối. Có hai loại timelock trên Bitcoin:
* Timelock tuyệt đối, xác định một thời điểm cụ thể trước đó giao dịch không thể được bao gồm trong một khối;
* Timelock tương đối, thiết lập một khoảng thời gian chờ từ việc chấp nhận một giao dịch trước đó.
Timelock có thể được xác định hoặc là một ngày được biểu diễn trong thời gian Unix hoặc là một số khối. Cuối cùng, timelock có thể áp dụng cho một đầu ra giao dịch bằng cách sử dụng một mã lệnh cụ thể trong script khóa (`OP_CHECKLOCKTIMEVERIFY` hoặc `OP_CHECKSEQUENCEVERIFY`), hoặc áp dụng cho toàn bộ giao dịch bằng cách sử dụng các trường giao dịch cụ thể (`nLockTime` hoặc `nSequence`).