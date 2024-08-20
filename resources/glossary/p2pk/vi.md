---
term: P2PK
---

P2PK viết tắt của *Pay to Public Key* (Thanh toán cho Khóa Công khai). Đây là một mô hình script chuẩn được sử dụng trên Bitcoin để thiết lập các điều kiện chi tiêu cho một UTXO. Nó cho phép khóa bitcoin trực tiếp vào một khóa công khai, thay vì một địa chỉ.
Về mặt kỹ thuật, script P2PK chứa một khóa công khai và một hướng dẫn yêu cầu chữ ký số tương ứng để mở khóa các khoản tiền. Khi chủ sở hữu muốn chi tiêu bitcoin, họ phải cung cấp một chữ ký được tạo ra với khóa riêng tư tương ứng. Chữ ký này được xác minh sử dụng ECDSA (*Elliptic Curve Digital Signature Algorithm* - Thuật toán Chữ ký Số Đường Cong Elliptic). P2PK thường được sử dụng trong các phiên bản đầu của Bitcoin, đáng chú ý là bởi Satoshi Nakamoto. Hiện nay, nó gần như không còn được sử dụng nữa.