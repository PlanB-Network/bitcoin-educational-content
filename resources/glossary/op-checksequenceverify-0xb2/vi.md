---
term: OP_CHECKSEQUENCEVERIFY (0XB2)
---

Làm cho giao dịch trở nên không hợp lệ nếu quan sát thấy bất kỳ đặc điểm nào sau đây:
* Ngăn xếp (stack) trống;
* Giá trị ở đầu ngăn xếp nhỏ hơn `0`;
* Cờ vô hiệu hóa cho giá trị ở đầu ngăn xếp không được định nghĩa và; Phiên bản giao dịch nhỏ hơn `2` hoặc; Cờ vô hiệu hóa cho trường `nSequence` của đầu vào được thiết lập hoặc; Loại thời gian khóa không giống nhau giữa trường `nSequence` và giá trị ở đầu ngăn xếp (thời gian thực hoặc số khối) hoặc; Giá trị ở đầu ngăn xếp lớn hơn giá trị của trường `nSequence` của đầu vào.

Nếu một hoặc nhiều đặc điểm này được quan sát, script chứa `OP_CHECKSEQUENCEVERIFY` không thể được thỏa mãn. Nếu tất cả các điều kiện hợp lệ, thì `OP_CHECKSEQUENCEVERIFY` hoạt động như một `OP_NOP`, nghĩa là nó không thực hiện bất kỳ hành động nào trên script. Nó như thể nó biến mất. `OP_CHECKSEQUENCEVERIFY` do đó áp đặt một ràng buộc thời gian tương đối đối với việc chi tiêu UTXO được bảo vệ bằng script chứa nó. Nó có thể làm điều này dưới dạng thời gian thực hoặc dưới dạng số khối. Để làm điều này, nó hạn chế các giá trị có thể có cho trường `nSequence` của đầu vào chi tiêu nó, và chính trường `nSequence` này hạn chế khi nào giao dịch bao gồm đầu vào này có thể được bao gồm trong một khối.

> ► *Mã lệnh này thay thế cho `OP_NOP`. Nó được đặt trên `OP_NOP3`. Nó thường được gọi bằng từ viết tắt "CSV". Lưu ý, `OP_CSV` không nên bị nhầm lẫn với trường `nSequence` của một giao dịch. Cái trước sử dụng cái sau, nhưng bản chất và hành động của chúng là khác nhau.*