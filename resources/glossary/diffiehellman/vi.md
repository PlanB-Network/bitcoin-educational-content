---
term: DIFFIE-HELLMAN
---

Phương pháp mật mã cho phép hai bên tạo ra một bí mật chung qua một kênh giao tiếp không an toàn. Bí mật này sau đó có thể được sử dụng để mã hóa giao tiếp giữa hai bên. Diffie-Hellman sử dụng số học mô-đun sao cho, ngay cả khi một kẻ tấn công có thể quan sát các giao dịch, họ không thể suy luận ra bí mật chung mà không giải quyết được một bài toán toán học khó: logarit rời rạc. Trong Bitcoin, một biến thể của DH được gọi là ECDH sử dụng một đường cong elliptic đôi khi được sử dụng, đặc biệt là cho các giao thức địa chỉ tĩnh như Silent Payments hoặc BIP47.