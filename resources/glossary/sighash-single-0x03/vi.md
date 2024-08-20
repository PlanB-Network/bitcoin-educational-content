---
term: SIGHASH_SINGLE (0X03)
---

Loại cờ SigHash được sử dụng trong chữ ký giao dịch Bitcoin để chỉ ra rằng chữ ký áp dụng cho tất cả các đầu vào của giao dịch và chỉ một đầu ra, tương ứng với chỉ mục của đầu vào được ký. Do đó, mỗi đầu vào được ký với `SIGHASH_SINGLE` được liên kết cụ thể với một đầu ra nhất định. Các đầu ra khác không được cam kết bởi chữ ký và do đó có thể được sửa đổi sau. Loại chữ ký này hữu ích trong các giao dịch phức tạp, nơi mà các bên tham gia muốn liên kết các đầu vào nhất định với các đầu ra cụ thể, trong khi vẫn giữ sự linh hoạt cho các đầu ra khác của giao dịch.