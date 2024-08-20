---
term: BIP322
---

Đề xuất một tiêu chuẩn mới để thay thế BIP137 cho việc ký tin nhắn bằng khóa riêng Bitcoin và các địa chỉ liên quan, nhằm chứng minh quyền sở hữu của một địa chỉ. Những chữ ký này hữu ích cho các ứng dụng khác nhau như chứng minh quỹ, kiểm toán, và các ứng dụng khác yêu cầu xác thực địa chỉ qua khóa riêng của nó. So với BIP137, BIP322 mở rộng tiêu chuẩn ký tin nhắn ra ngoài các địa chỉ truyền thống, sử dụng một phương pháp dựa trên script. Nó cho phép phần mềm ví ký một tin nhắn cho bất kỳ script nào mà họ có thể mở khóa để chi tiêu bitcoin. Để làm điều này, phương pháp bao gồm việc ký một văn bản bằng cách tạo ra một chữ ký cho một giao dịch Bitcoin ảo. Đối với các địa chỉ P2PKH truyền thống, BIP322 vẫn tương thích với định dạng chữ ký truyền thống.