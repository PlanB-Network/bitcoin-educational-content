---
term: DERIVATION
---

Đề cập đến quá trình tạo ra các cặp khóa con từ một cặp khóa cha (khóa riêng và khóa công khai) và một mã chuỗi trong ví xác định và phân cấp (HD). Quá trình này cho phép phân chia các nhánh và tổ chức ví vào các cấp độ khác nhau với nhiều cặp khóa con, tất cả đều có thể được khôi phục chỉ bằng cách biết thông tin khôi phục cơ bản (cụm từ ghi nhớ và bất kỳ cụm từ mật khẩu tiềm năng nào). Để tạo ra một khóa con, hàm `HMAC-SHA512` được sử dụng với mã chuỗi cha và sự kết hợp của khóa cha và một chỉ mục 32-bit. Có hai loại phái sinh:
* Phái sinh bình thường, sử dụng khóa công khai cha làm cơ sở của hàm `HMAC-SHA512`;
* Phái sinh cứng, sử dụng khóa riêng cha làm cơ sở của hàm `HMAC-SHA512`;

Kết quả của HMAC-SHA512 được chia thành hai phần: 256 bit đầu tiên trở thành khóa con (riêng hoặc công khai sau khi xử lý qua ECDSA), và 256 bit còn lại trở thành mã chuỗi con.