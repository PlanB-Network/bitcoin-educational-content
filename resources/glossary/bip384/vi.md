---
term: BIP384
---

Giới thiệu hàm `combo(KEY)` cho các mô tả. Hàm này mô tả một tập hợp các kịch bản đầu ra có thể có cho một khóa công khai nhất định. Do đó, nó bao gồm nhiều loại kịch bản cùng một lúc, bao gồm P2PK, P2PKH, P2WPKH và P2SH-P2WPKH. Nếu khóa được nén, tất cả 4 loại kịch bản sẽ được kiểm tra, và nếu không, chỉ có 2 loại kịch bản Legacy được kiểm tra. Mục tiêu là đơn giản hóa việc biểu diễn khóa trong các mô tả bằng cách cung cấp một phương pháp đơn lẻ để tạo ra các biến thể khác nhau của kịch bản đầu ra dựa trên cùng một khóa công khai. BIP384 đã được triển khai cùng với tất cả các BIP liên quan đến mô tả khác (trừ BIP386) trong phiên bản 0.17 của Bitcoin Core.