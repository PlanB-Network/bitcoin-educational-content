---
term: SIGHASH_NONE (0X02)
---

Loại cờ SigHash được sử dụng trong chữ ký giao dịch Bitcoin để chỉ ra rằng chữ ký áp dụng cho tất cả các đầu vào của giao dịch, nhưng không áp dụng cho bất kỳ đầu ra nào. Việc sử dụng `SIGHASH_NONE` có nghĩa là người ký cam kết chỉ với các đầu vào, cho phép các đầu ra vẫn chưa được xác định hoặc có thể được sửa đổi sau khi ký. Loại chữ ký này hữu ích trong các trường hợp mà người ký muốn ủy quyền cho các bên khác quyết định cách phân phối bitcoin trong giao dịch.