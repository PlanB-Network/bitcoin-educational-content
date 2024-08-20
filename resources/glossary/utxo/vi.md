---
term: UTXO
---

Viết tắt của *Unspent Transaction Output*. UTXO là một đầu ra của giao dịch chưa được tiêu, nghĩa là nó chưa được sử dụng làm đầu vào cho một giao dịch mới. UTXO đại diện cho phần bitcoin mà người dùng sở hữu và hiện đang có sẵn để tiêu. Mỗi UTXO được liên kết với một script đầu ra cụ thể (`scriptPubKey`), định nghĩa các điều kiện cần thiết để tiêu bitcoin. Giao dịch trong Bitcoin tiêu thụ những UTXO này như là đầu vào và tạo ra UTXO mới như là đầu ra. Mô hình UTXO là cơ bản đối với Bitcoin, vì nó cho phép dễ dàng xác minh rằng các giao dịch không cố gắng tiêu bitcoin không tồn tại hoặc đã được tiêu.