---
term: SPV NODE (LIGHT NODE)
---

Một nút SPV (*Simple Payment Verification*), đôi khi được gọi là "nút nhẹ," là một khách hàng nhẹ của một nút Bitcoin cho phép người dùng xác thực giao dịch mà không cần phải lưu trữ toàn bộ blockchain. Thay vào đó, một nút SPV chỉ lưu trữ các tiêu đề khối và lấy thông tin về các giao dịch cụ thể bằng cách truy vấn các nút đầy đủ khi cần thiết. Nguyên tắc xác thực này được làm cho khả thi bởi cấu trúc của các giao dịch trong các khối Bitcoin, được tổ chức trong một bộ tích lũy mật mã (Merkle Tree).

Cách tiếp cận này có lợi cho các thiết bị có nguồn lực hạn chế, như điện thoại di động. Tuy nhiên, các nút SPV phụ thuộc vào các nút đầy đủ cho sự khả dụng của thông tin, điều này ngụ ý một mức độ tin cậy bổ sung và do đó, ít an toàn hơn so với các nút đầy đủ. Các nút SPV không thể xác thực giao dịch một cách tự chủ, nhưng chúng có thể xác minh nếu một giao dịch được bao gồm trong một khối bằng cách tham khảo các bằng chứng Merkle.