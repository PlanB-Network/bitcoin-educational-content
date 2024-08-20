---
term: OP_CHECKLOCKTIMEVERIFY (0XB1)
---

Làm cho giao dịch không hợp lệ trừ khi tất cả các điều kiện sau được thỏa mãn:
* Ngăn xếp không trống;
* Giá trị ở đỉnh ngăn xếp lớn hơn hoặc bằng `0`;
* Loại thời gian khóa giữa trường `nLockTime` và giá trị ở đỉnh ngăn xếp phải giống nhau (thời gian thực hoặc số khối);
* Trường `nSequence` của đầu vào không bằng `0xffffffff`;
* Giá trị ở đỉnh ngăn xếp lớn hơn hoặc bằng giá trị của trường `nLockTime` của giao dịch.

Nếu bất kỳ điều kiện nào trong số này không được thỏa mãn, script chứa `OP_CHECKLOCKTIMEVERIFY` không thể được thực hiện. Nếu tất cả các điều kiện này đều hợp lệ, thì `OP_CHECKLOCKTIMEVERIFY` hoạt động như một `OP_NOP`, có nghĩa là nó không thực hiện bất kỳ hành động nào trên script. Nó như thể nó biến mất. `OP_CHECKLOCKTIMEVERIFY` do đó áp đặt một ràng buộc thời gian đối với việc chi tiêu UTXO được bảo vệ bằng script chứa nó. Nó có thể làm điều này dưới dạng một ngày thời gian Unix hoặc như một số khối. Để làm điều này, nó hạn chế các giá trị có thể có cho trường `nLockTime` của giao dịch chi tiêu nó, và chính trường `nLockTime` này hạn chế thời điểm giao dịch có thể được bao gồm trong một khối.

> ► *Mã lệnh này thay thế cho `OP_NOP`. Nó được đặt trên `OP_NOP2`. Nó thường được gọi bằng từ viết tắt "CLTV". Lưu ý, `OP_CLTV` không nên bị nhầm lẫn với trường `nLockTime` của một giao dịch. Cái trước sử dụng cái sau, nhưng bản chất và hành động của chúng là khác nhau.*