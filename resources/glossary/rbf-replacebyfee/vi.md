---
term: RBF (REPLACE-BY-FEE)
---

Một cơ chế giao dịch cho phép người gửi thay thế một giao dịch bằng giao dịch khác bằng cách trả phí cao hơn, nhằm mục đích tăng tốc độ xác nhận giao dịch. Nếu một giao dịch với mức phí quá thấp bị kẹt, người gửi có thể sử dụng *Replace-By-Fee* để tăng mức phí và ưu tiên giao dịch thay thế của họ trong mempool.

RBF có thể áp dụng miễn là giao dịch còn trong mempool; một khi đã vào block, giao dịch không thể được thay thế. Khi gửi ban đầu, giao dịch phải chỉ định khả năng được thay thế bằng cách điều chỉnh giá trị `nSequence` thành một số nhỏ hơn `0xfffffffe`. Điều này được biết đến như một cờ RBF. Cài đặt này báo hiệu khả năng cập nhật giao dịch sau khi nó đã được phát sóng, điều này sau đó cho phép thực hiện RBF. Tuy nhiên, đôi khi có thể thay thế một giao dịch mà không báo hiệu RBF. Các nút sử dụng tham số cấu hình `mempoolfullrbf=1` chấp nhận việc thay thế này ngay cả khi RBF không được báo hiệu ban đầu.

Khác với CPFP (*Child Pays For Parent*), nơi người nhận có thể hành động để tăng tốc giao dịch, RBF (*Replace-By-Fee*) cho phép người gửi chủ động tăng tốc giao dịch của mình bằng cách tăng phí.