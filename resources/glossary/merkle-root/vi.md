---
term: MERKLE ROOT
---

Digest hoặc "top hash" của một cây Merkle, đại diện cho bản tóm tắt của tất cả thông tin có trong cây. Một cây Merkle là một cấu trúc tích lũy mật mã, đôi khi còn được gọi là "cây hash". Trong bối cảnh của Bitcoin, cây Merkle được sử dụng để tổ chức các giao dịch trong một khối và để tạo điều kiện thuận lợi cho việc xác minh nhanh chóng việc bao gồm một giao dịch cụ thể. Do đó, trong các khối Bitcoin, Merkle root được thu được bằng cách liên tục băm các giao dịch theo cặp cho đến khi chỉ còn lại một hash (Merkle root). Hash này sau đó được bao gồm trong tiêu đề của khối tương ứng. Cây hash này cũng được tìm thấy trong UTREEXO, một cấu trúc cho phép làm gọn bộ UTXO của các nút, và trong MAST Taproot.