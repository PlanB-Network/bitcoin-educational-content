---
term: LỜI ĐỀ NGHỊ
---

Trong BOLT12, *offer* là mã QR tĩnh để thực hiện nhiều khoản thanh toán trên Lightning Network. Không giống như các hóa đơn thông thường, *offer* có thể được sử dụng lại. Chúng có thể được sử dụng để generate nhiều yêu cầu Invoice. Khi người dùng quét mã QR có chứa *offer*, nó sẽ gửi một thông báo yêu cầu một Invoice mới đến nút Lightning được liên kết. Nút phản hồi bằng một Invoice mà người trả tiền có thể sử dụng. Do đó, *offer* cung cấp một mã định danh duy nhất để nhận nhiều khoản thanh toán từ những người dùng khác nhau trên Lightning.