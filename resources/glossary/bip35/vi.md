---
term: BIP35
---

Đề xuất cho phép một nút Bitcoin mở thông tin về mempool của mình, tức là các giao dịch đang chờ xác nhận. Nhờ đó, các bên tham gia khác có thể nhận dữ liệu thời gian thực về các giao dịch chưa được xác nhận bằng cách gửi một thông điệp cụ thể đến một nút. Trước khi BIP35 được áp dụng, các nút chỉ có thể truy cập thông tin về các giao dịch đã được xác nhận. Sự cải tiến này mang lại cho ví SPV khả năng nhận thông tin về các giao dịch chưa được xác nhận, cho phép một thợ mỏ tránh bỏ lỡ các giao dịch có phí cao trong quá trình khởi động lại, và tạo điều kiện cho việc phân tích thông tin mempool bởi các dịch vụ bên ngoài.