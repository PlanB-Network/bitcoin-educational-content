---
term: HTLC
---

Viết tắt của "*Hashed Timelock Contract*". Đây là cơ chế Smart contract chủ yếu được sử dụng trên Lightning. Đôi khi cũng được tìm thấy trong các giao dịch hoán đổi nguyên tử. Về cơ bản, HTLC khiến việc chuyển tiền có điều kiện là phải tiết lộ bí mật và cũng bao gồm điều kiện về thời gian để bảo vệ tiền của người gửi trong trường hợp giao dịch không thành công.


Trên Lightning, HTLC cho phép bạn gửi bitcoin đến một nút mà bạn không có kênh trực tiếp, bằng cách chuyển qua nhiều kênh, không cần phải tin tưởng trong suốt quá trình. Thanh toán giữa mỗi nút có điều kiện là phải cung cấp một hình ảnh trước (bí mật, khi được băm, tương ứng với một giá trị đã thỏa thuận). Nếu người nhận cuối cùng cung cấp hình ảnh trước này, nó có thể yêu cầu tiền và nhất thiết cho phép mỗi nút trung gian yêu cầu tiền theo tầng.


Ví dụ, nếu Alice muốn gửi 1 BTC cho David nhưng không có kênh trực tiếp với anh ấy, cô ấy phải thông qua Bob và Carol, những người có kênh thanh toán với nhau. Giao dịch diễn ra như sau:




- David tặng Alice một Invoice Lightning. Nó chứa Hash $h$ của một $s$ bí mật (hình ảnh trước) mà chỉ David biết. Vì vậy, chúng ta có: $h = \text{Hash}(s)$ ;
- Alice tạo ra HTLC với Bob, người đề nghị gửi cho cô ấy 1 BTC với điều kiện Bob cung cấp cho cô ấy một $s$ bí mật (hình ảnh trước) tương ứng với Hash $h$;
- Bob tạo ra HTLC với Carol, người đề nghị gửi cho anh ta 1 BTC với điều kiện cô ấy cũng cung cấp cùng một bí mật $s$;
- Carol tạo ra HTLC với David, người sẽ trả thêm 1 BTC nếu anh ta tiết lộ hình ảnh trước $s$;
- David tiết lộ $s$ (mà chỉ mình anh ấy biết) cho Carol để nhận 1 BTC. Carol bây giờ có thể sử dụng $s$ để lấy BTC từ Bob. Và Bob, người bây giờ biết $s$, làm tương tự với Alice.


Cuối cùng, Alice đã gửi 1 BTC cho David thông qua Bob và Carol (một hành động trung lập đối với Carol), mà không cần ai phải tin tưởng lẫn nhau, vì mọi thứ đều được bảo mật theo tầng theo các điều kiện của HTLC.


HTLC do đó cho phép cái gọi là trao đổi "nguyên tử": hoặc là việc chuyển giao hoàn toàn thành công, hoặc là thất bại, và tiền được trả lại. Điều này đảm bảo tính bảo mật của các giao dịch, ngay cả giữa nhiều bên tham gia mà không cần sự tin tưởng.