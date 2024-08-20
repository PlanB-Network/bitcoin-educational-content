---
term: DẤU VÂN TAY CHỦ
---

Dấu vân tay chủ là một dấu vân tay 4 byte (32-bit) của khóa riêng chủ trong một ví Phân Cấp Xác Định (HD). Nó được thu được bằng cách tính toán băm `SHA256` của khóa riêng chủ, tiếp theo là một băm `RIPEMD160`, quá trình này được gọi là `HASH160` trên Bitcoin. Dấu vân tay chủ được sử dụng để xác định một ví HD, độc lập với các con đường phái sinh, nhưng xem xét sự có mặt hoặc vắng mặt của một cụm từ bí mật. Đây là thông tin ngắn gọn cho phép tham chiếu đến nguồn gốc của một bộ khóa, mà không tiết lộ thông tin nhạy cảm về ví.