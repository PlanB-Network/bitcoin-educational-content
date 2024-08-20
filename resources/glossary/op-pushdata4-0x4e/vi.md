---
term: OP_PUSHDATA4 (0X4E)
---

Cho phép đẩy một lượng lớn dữ liệu vào stack. Nó được theo sau bởi bốn byte (little-endian) chỉ ra độ dài của dữ liệu cần đẩy (lên đến khoảng 4.3 GB). Mã lệnh này được sử dụng để chèn dữ liệu lớn vào script, mặc dù việc sử dụng nó cực kỳ hiếm gặp do những hạn chế thực tế về kích thước giao dịch.