---
term: CPFP (CHILD PAYS FOR PARENT)
---

Một cơ chế giao dịch nhằm mục đích tăng tốc độ xác nhận của một giao dịch Bitcoin, tương tự như những gì Replace-by-Fee (RBF) làm, nhưng từ phía người nhận. Khi một giao dịch với phí quá thấp so với thị trường bị kẹt trong mempool của các nút và không được xác nhận nhanh chóng, người nhận có thể thực hiện một giao dịch mới, sử dụng số bitcoin nhận được trong giao dịch bị chặn, mặc dù nó chưa được xác nhận. Giao dịch thứ hai này yêu cầu giao dịch đầu tiên phải được khai thác để được xác nhận. Do đó, các thợ mỏ buộc phải bao gồm cả hai giao dịch cùng một lúc. Giao dịch thứ hai sẽ phân bổ nhiều hơn về phí giao dịch so với giao dịch đầu tiên, theo cách mà phí trung bình khuyến khích thợ mỏ bao gồm cả hai giao dịch. Giao dịch con (giao dịch thứ hai) trả phí cho giao dịch cha bị kẹt (giao dịch đầu tiên). Đây là lý do tại sao nó được gọi là "CPFP."

Như vậy, CPFP cho phép người nhận nhận được tiền của họ nhanh hơn bất chấp phí ban đầu thấp do người gửi chịu, không giống như RBF (*Replace-By-Fee*), cho phép người gửi chủ động tăng tốc giao dịch của mình bằng cách tăng phí.