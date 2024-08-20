---
term: STONEWALL
---

Một dạng cụ thể của giao dịch Bitcoin nhằm tăng cường quyền riêng tư cho người dùng trong quá trình chi tiêu bằng cách mô phỏng một coinjoin giữa hai người, mặc dù thực tế không phải là như vậy. Đúng vậy, giao dịch này không phải là cộng tác. Người dùng có thể tự mình xây dựng nó, chỉ liên quan đến UTXOs của chính họ làm đầu vào. Do đó, bạn có thể tạo một giao dịch Stonewall cho bất kỳ dịp nào, mà không cần phải đồng bộ với người dùng khác.

Cách hoạt động của giao dịch Stonewall như sau: tại đầu vào của giao dịch, người gửi sử dụng 2 UTXOs thuộc về họ. Giao dịch sau đó tạo ra 4 đầu ra, trong đó 2 đầu ra sẽ có cùng một lượng chính xác. 2 đầu ra còn lại sẽ là tiền thối. Trong số 2 đầu ra có cùng một lượng, chỉ có một đầu ra thực sự đi đến người nhận thanh toán.

Do đó, chỉ có 2 vai trò trong một giao dịch Stonewall:
* Người gửi, người thực hiện thanh toán thực sự;
* Người nhận, người có thể không biết về bản chất cụ thể của giao dịch và đơn giản chỉ chờ đợi một khoản thanh toán từ người gửi.

![](../../dictionnaire/assets/33.png)
Giao dịch Stonewall có sẵn trên cả ứng dụng Samourai Wallet và phần mềm Sparrow Wallet.

Cấu trúc Stonewall thêm rất nhiều entropy vào giao dịch và làm mờ dấu vết cho phân tích chuỗi. Từ bên ngoài, một giao dịch như vậy có thể được giải thích là một coinjoin nhỏ giữa hai người. Nhưng thực tế, giống như giao dịch Stonewall x2, đó là một khoản thanh toán. Phương pháp này do đó tạo ra sự không chắc chắn trong phân tích chuỗi, hoặc thậm chí dẫn đến những dấu vết sai lầm. Ngay cả khi một quan sát viên bên ngoài quản lý để xác định mô hình của giao dịch Stonewall, họ sẽ không có tất cả thông tin. Họ sẽ không thể xác định được UTXOs nào trong hai UTXOs có cùng số lượng tương ứng với thanh toán. Hơn nữa, họ sẽ không thể xác định liệu hai UTXOs tại đầu vào đến từ hai người khác nhau hay chúng thuộc về một người đã kết hợp chúng. Điểm cuối cùng này là do giao dịch Stonewall x2 tuân theo chính xác cùng một mô hình như giao dịch Stonewall. Từ bên ngoài và không có thông tin bối cảnh bổ sung, không thể phân biệt giao dịch Stonewall với giao dịch Stonewall x2. Tuy nhiên, cái trước không phải là giao dịch cộng tác, trong khi cái sau là. Điều này thêm vào còn nhiều nghi ngờ hơn về khoản chi tiêu này.