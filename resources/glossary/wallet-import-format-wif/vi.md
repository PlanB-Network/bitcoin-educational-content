---
term: WALLET IMPORT FORMAT (WIF)
---

Một phương pháp mã hóa khóa riêng Bitcoin theo cách mà nó có thể được nhập khẩu hoặc xuất khẩu dễ dàng hơn giữa các ví khác nhau. WIF dựa trên mã hóa `Base58Check`, bao gồm thông tin về phiên bản, sự nén của khóa công khai tương ứng, và một mã kiểm tra lỗi khi gõ. Một khóa riêng WIF bắt đầu với các ký tự `5` cho các khóa không nén, hoặc `K` và `L` cho các khóa nén, và chứa tất cả các ký tự cần thiết để tái tạo lại khóa riêng gốc. Định dạng WIF cung cấp một phương tiện tiêu chuẩn để chuyển một khóa riêng giữa các phần mềm ví khác nhau.