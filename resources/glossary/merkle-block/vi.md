---
term: MERKLE BLOCK
---

Một cấu trúc dữ liệu được sử dụng trong bối cảnh của BIP37 (*Transaction Bloom Filtering*) để cung cấp một bằng chứng gọn nhẹ về việc bao gồm các giao dịch cụ thể trong một khối. Nó đặc biệt được sử dụng cho ví SPV. Merkle Block chứa các tiêu đề khối, giao dịch đã lọc, và một cây Merkle một phần, cho phép các khách hàng nhẹ có thể nhanh chóng xác minh một giao dịch có thuộc về một khối mà không cần tải xuống tất cả các giao dịch.