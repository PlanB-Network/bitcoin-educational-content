---
term: BIP12
---

Đề xuất bởi Gavin Andresen nhằm tăng cường tính linh hoạt và bảo mật cho các kịch bản giao dịch Bitcoin. BIP này đề xuất triển khai một mã lệnh kịch bản mới, được gọi là `OP_EVAL`, cho phép đánh giá một kịch bản chứa trong dữ liệu của `scriptSig` trong quá trình xác thực giao dịch. Sửa đổi chính của BIP12 là cho phép bao gồm một kịch bản bên trong kịch bản khác. Kỹ thuật này cho phép tạo ra các điều kiện phức tạp hơn có thể được xác minh tại thời điểm chi tiêu, mà không cần phải tiết lộ chúng cho người dùng gửi bitcoin đến địa chỉ sử dụng. BIP12 sau đó đã được thay thế bằng các đề xuất an toàn hơn, đáng chú ý là BIP16 (P2SH), cung cấp một phương pháp khác để đạt được cùng một mục tiêu như `OP_EVAL`.