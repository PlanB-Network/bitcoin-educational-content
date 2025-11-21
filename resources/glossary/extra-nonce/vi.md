---
term: THÊM-Nonce
---

Trường được sử dụng trong `scriptSig` của Coinbase Transaction trong khối, cho phép kiểm tra nhiều khả năng hơn để có Hash thấp hơn mục tiêu độ khó, ngoài Nonce cổ điển, nằm trực tiếp trong tiêu đề của mỗi khối.


Việc sửa đổi extra-Nonce trong Coinbase Transaction sẽ thay đổi định danh của giao dịch này và do đó thay đổi Merkle Root của tất cả các giao dịch trong khối, điều này cũng sửa đổi tiêu đề khối. Điều này cho phép Miner tiếp tục tìm kiếm băm khi phạm vi của Nonce cổ điển đã cạn kiệt, mà không thay đổi cấu trúc của khối ứng viên của nó.


Trong nhóm Mining, Nonce bổ sung thường được chia thành hai phần: một phần do nhóm tạo ra để xác định từng chopper và phần còn lại do chopper sửa đổi để tìm kiếm một phần hợp lệ. Điều này cho phép các chopper khác nhau trong nhóm làm việc đồng thời trên cùng một khối ứng viên với toàn bộ phạm vi nonce, mà không cần phải sao chép cùng một công việc ở cấp độ nhóm.