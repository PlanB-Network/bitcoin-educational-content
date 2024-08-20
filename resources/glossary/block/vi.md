---
term: BLOCK
---

Cấu trúc dữ liệu trong hệ thống Bitcoin. Một khối chứa một tập hợp các giao dịch hợp lệ và siêu dữ liệu được chứa trong tiêu đề của nó. Mỗi khối được liên kết với khối tiếp theo thông qua băm của tiêu đề nó, từ đó hình thành nên blockchain. Blockchain hoạt động như một máy chủ đánh dấu thời gian cho phép mọi người dùng biết tất cả các giao dịch trong quá khứ, nhằm mục đích xác minh sự không tồn tại của một giao dịch và ngăn chặn việc chi tiêu gấp đôi. Các giao dịch được tổ chức trong một cây Merkle. Bộ tích lũy mã hóa này cho phép tạo ra một bản tóm tắt của tất cả các giao dịch trong một khối, được gọi là "gốc Merkle." Tiêu đề của một khối chứa 6 yếu tố:
* Phiên bản của khối;
* Dấu ấn của khối trước đó;
* Gốc của cây Merkle của các giao dịch;
* Dấu thời gian của khối;
* Mục tiêu khó khăn;
* Số nonce.

Để một khối được coi là hợp lệ, nó phải có một tiêu đề mà, một khi được băm với `SHA256d`, tạo ra một bản tóm tắt nhỏ hơn hoặc bằng với mục tiêu khó khăn.