---
term: CHỮ KÝ MÙ
---

Chữ ký mù của Chaum là một dạng chữ ký số mà người phát hành chữ ký không biết nội dung của thông điệp mà họ đang ký. Tuy nhiên, chữ ký sau đó có thể được xác minh với thông điệp gốc. Kỹ thuật này được phát triển bởi nhà mật mã học David Chaum vào năm 1983.

Xem xét ví dụ về một công ty muốn xác thực một tài liệu mật, như một hợp đồng, mà không tiết lộ nội dung của nó. Công ty áp dụng một quá trình che giấu mà biến đổi tài liệu gốc một cách có thể đảo ngược bằng mật mã. Tài liệu đã được sửa đổi này được gửi đến một cơ quan chứng nhận áp dụng một chữ ký mù mà không biết nội dung cơ bản. Sau khi nhận được tài liệu đã ký được che giấu, công ty gỡ bỏ lớp che giấu chữ ký. Kết quả là một tài liệu gốc được xác thực bởi chữ ký của cơ quan chứng nhận, mà cơ quan đó không bao giờ thấy nội dung gốc.

Như vậy, chữ ký mù của Chaum cho phép xác thực tính xác thực của một tài liệu mà không cần biết nội dung của nó, đảm bảo cả tính bảo mật của dữ liệu người dùng và tính toàn vẹn của tài liệu đã ký.

Trong Bitcoin, giao thức này được sử dụng trong các hệ thống của các ngân hàng Chaumian như một lớp phủ (Cashu, Fedimint, v.v.), nhưng đặc biệt là trong các giao thức coinjoin Chaumian, để đảm bảo rằng điều phối viên không thể liên kết một đầu vào với một đầu ra.