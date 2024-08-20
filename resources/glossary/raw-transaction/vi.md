---
term: GIAO DỊCH THÔ
---

Một giao dịch Bitcoin được xây dựng và ký kết, tồn tại dưới dạng nhị phân. Giao dịch thô (*raw TX*) là biểu diễn cuối cùng của một giao dịch, ngay trước khi nó được phát sóng trên mạng. Giao dịch này chứa tất cả thông tin cần thiết cho việc bao gồm nó trong một khối:
* Phiên bản;
* Cờ;
* Các đầu vào;
* Các đầu ra;
* Thời gian khóa;
* Chứng nhân.

Những gì được gọi là "*giao dịch thô*" đại diện cho dữ liệu thô được truyền qua hàm băm SHA256 hai lần để tạo ra TXID của giao dịch. Những dữ liệu này sau đó được sử dụng trong cây Merkle của khối để tích hợp giao dịch vào blockchain.

> ► *Khái niệm này cũng đôi khi được gọi là "Giao Dịch Đã Mã Hóa". Trong tiếng Pháp, các thuật ngữ này có thể lần lượt được dịch là "transaction brute" và "transaction sérialisée".*