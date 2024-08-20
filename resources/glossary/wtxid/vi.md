---
term: WTXID
---

Là một sự mở rộng của TXID truyền thống, bao gồm dữ liệu chứng thực được giới thiệu với SegWit. Trong khi TXID là một băm của dữ liệu giao dịch không bao gồm chứng thực, WTXID là `SHA256d` của toàn bộ dữ liệu giao dịch, bao gồm cả chứng thực. WTXIDs được lưu trữ trong một cây Merkle riêng biệt mà gốc của nó được đặt trong giao dịch coinbase. Sự tách biệt này cho phép loại bỏ tính biến đổi giao dịch của TXID.