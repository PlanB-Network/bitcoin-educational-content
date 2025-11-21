---
term: LIBSECP256K1
---

Thư viện C hiệu suất cao, bảo mật cao dành cho chữ ký số và các nguyên hàm mật mã khác trên đường cong elip `secp256k1`. Vì đường cong này chưa bao giờ được sử dụng rộng rãi bên ngoài Bitcoin (không giống như đường cong `secp256r1` thường được ưa chuộng), nên thư viện này hướng đến mục tiêu trở thành tài liệu tham khảo toàn diện nhất cho mục đích sử dụng của nó. Việc phát triển libsecp256k1 chủ yếu hướng đến nhu cầu của Bitcoin và các tính năng dành cho các ứng dụng khác có thể ít được kiểm tra hoặc xác minh hơn. Việc sử dụng hợp lý thư viện này đòi hỏi sự chú ý cẩn thận để đảm bảo rằng nó phù hợp với các mục đích cụ thể của các ứng dụng khác ngoài Bitcoin.


Thư viện libsecp256k1 cung cấp nhiều tính năng, bao gồm:




- Chữ ký và xác minh ECDSA-secp256k1 và tạo khóa mật mã;
- Các phép toán cộng và nhân trên khóa bí mật và khóa công khai;
- Tuần tự hóa và phân tích khóa bí mật, khóa công khai và chữ ký;
- Ký và tạo khóa công khai theo thời gian thực với quyền truy cập bộ nhớ liên tục;
- Và nhiều nguyên lý mật mã khác.