---
term: BIP380
---

Đề xuất cải tiến giới thiệu một ngôn ngữ chuẩn để mô tả các bộ sưu tập của script đầu ra của ví HD Bitcoin. Ngôn ngữ này được gọi là "Mô Tả Script Đầu Ra" (Output Script Descriptors). Mục tiêu là chuẩn hóa cách thể hiện và quản lý script đầu ra, nhằm tạo điều kiện thuận lợi cho việc sao lưu, xuất khẩu, và nhập khẩu ví. Ngoài dữ liệu riêng tư như cụm từ khôi phục, các mô tả cung cấp tất cả thông tin cần thiết để truy xuất các cặp khóa được sử dụng trong ví HD. BIP380 mô tả hoạt động chung của các mô tả, trong khi BIP381, BIP382, BIP383, BIP384, BIP385, và BIP386 chỉ rõ các biểu thức được sử dụng. BIP380 được triển khai cùng với tất cả các BIP liên quan đến mô tả khác (trừ BIP386) trong phiên bản 0.17 của Bitcoin Core.