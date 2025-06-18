---
term: LNURL
---

Giao thức truyền thông chỉ định một tập hợp các tính năng được thiết kế để đơn giản hóa tương tác giữa các nút Lightning và máy khách, cũng như các ứng dụng của bên thứ ba. Giao thức này dựa trên HTTP và cho phép tạo liên kết cho nhiều hoạt động khác nhau, chẳng hạn như yêu cầu thanh toán, yêu cầu rút tiền hoặc các chức năng khác giúp nâng cao trải nghiệm của người dùng. Mỗi LNURL là một URL được mã hóa trong bech32 với tiền tố `lnurl`, khi được quét, sẽ kích hoạt một loạt các hành động tự động trên Lightning Wallet.


Ví dụ, LNURL-withdraw (LUD-03) cho phép bạn rút tiền từ một dịch vụ bằng cách quét mã QR, mà không cần phải nhập generate vào Invoice theo cách thủ công. Hoặc LNURL-auth (LUD-04) cho phép bạn kết nối với các dịch vụ trực tuyến bằng khóa riêng trên Lightning Wallet thay vì mật khẩu.