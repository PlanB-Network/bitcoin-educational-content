---
term: SIGHASH_ALL/SIGHASH_ACP
---

Loại cờ SigHash (`0x81`) kết hợp với bộ chỉnh sửa `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`) được sử dụng trong chữ ký giao dịch Bitcoin. Sự kết hợp này chỉ định rằng chữ ký áp dụng cho tất cả các đầu ra và chỉ áp dụng cho một đầu vào cụ thể của giao dịch. `SIGHASH_ALL | SIGHASH_ANYONECANPAY` cho phép các bên tham gia khác thêm đầu vào bổ sung vào giao dịch sau khi đã ký ban đầu. Điều này đặc biệt hữu ích trong các tình huống hợp tác, như giao dịch gây quỹ cộng đồng, nơi các đóng góp viên khác nhau có thể thêm đầu vào của riêng họ trong khi vẫn bảo toàn tính toàn vẹn của các đầu ra đã được người ký ban đầu cam kết.