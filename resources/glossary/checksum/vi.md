---
term: CHECKSUM
---

Checksum là một giá trị được tính toán từ một tập dữ liệu, được sử dụng để xác minh tính toàn vẹn và hợp lệ của dữ liệu đó trong quá trình truyền tải hoặc lưu trữ. Các thuật toán checksum được thiết kế để phát hiện lỗi ngẫu nhiên hoặc sự thay đổi không mong muốn của dữ liệu, như lỗi truyền tải hoặc hỏng file. Có nhiều loại thuật toán checksum khác nhau, như kiểm tra chẵn lẻ, checksum mô-đun, hàm băm mật mã, hoặc mã BCH (*Bose, Ray-Chaudhuri, và Hocquenghem*).

Trong Bitcoin, checksum được sử dụng ở cấp độ ứng dụng để đảm bảo tính toàn vẹn của địa chỉ nhận. Một checksum được tính toán từ phần dữ liệu chính của địa chỉ người dùng, sau đó được thêm vào địa chỉ này để phát hiện lỗi có thể xảy ra trong quá trình nhập. Checksum cũng có mặt trong cụm từ khôi phục (mnemonic).

> ► *Bản dịch tiếng Anh của "somme de contrôle" là "checksum". Thuật ngữ "checksum" thường được chấp nhận sử dụng trực tiếp trong tiếng Pháp.*