---
term: BIP143
---

Giới thiệu một cách mới để băm giao dịch cho việc xác minh chữ ký trong các script sau SegWit. Mục tiêu là giảm thiểu các hoạt động lặp lại trong quá trình xác minh và bao gồm giá trị của UTXOs trong input vào chữ ký. Điều này giải quyết hai vấn đề lớn với thuật toán băm giao dịch ban đầu:
* Sự tăng cấp bậc hai của việc băm dữ liệu với số lượng chữ ký;
* Sự thiếu vắng việc bao gồm giá trị input trong chữ ký, điều này tạo ra rủi ro cho ví cứng, đặc biệt là liên quan đến việc biết phí giao dịch phát sinh.
Kể từ khi cập nhật SegWit, được giải thích trong BIP141, giới thiệu một dạng giao dịch mới mà script của nó sẽ không được các node cũ xác minh, BIP143 tận dụng cơ hội này để giải quyết vấn đề này mà không yêu cầu một hard fork. Do đó, BIP143 là một phần của soft fork SegWit.