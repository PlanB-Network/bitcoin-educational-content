---
term: P2PKH
---

P2PKH là viết tắt của *Pay to Public Key Hash* (Thanh toán cho Hash của Khóa Công khai). Đây là một mô hình script chuẩn được sử dụng để thiết lập các điều kiện chi tiêu trên một UTXO. Nó cho phép khóa bitcoin trên một hash của khóa công khai, tức là, trên một địa chỉ nhận. Script này được liên kết với tiêu chuẩn Legacy và đã được giới thiệu trong các phiên bản đầu tiên của Bitcoin bởi Satoshi Nakamoto.

Khác với P2PK, nơi mà khóa công khai được bao gồm một cách rõ ràng trong script, P2PKH sử dụng một dấu vân tay mật mã của khóa công khai. Script này bao gồm hash `RIPEMD160` của `SHA256` của khóa công khai và quy định rằng, để truy cập vào quỹ, người nhận phải cung cấp một khóa công khai phù hợp với hash này, cũng như một chữ ký số hợp lệ được tạo từ khóa riêng tư tương ứng. Địa chỉ P2PKH được mã hóa sử dụng định dạng `Base58Check`, giúp chúng có độ bền vững chống lại lỗi đánh máy thông qua việc sử dụng một checksum. Các địa chỉ này luôn bắt đầu với số `1`.