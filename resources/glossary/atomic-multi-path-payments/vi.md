---
term: THANH TOÁN ĐA ĐƯỜNG NGUYÊN TỬ
---

Phiên bản cải tiến của MPP (*Thanh toán đa đường dẫn*) trong đó mỗi phần thanh toán có một bí mật riêng biệt, đảm bảo rằng giao dịch được giải quyết một cách nguyên tử, tức là toàn bộ hoặc không giải quyết gì cả.


MPP là các kỹ thuật thanh toán trên Lightning cho phép chia nhỏ giao dịch thành nhiều phần nhỏ hơn và định tuyến qua các tuyến khác nhau. Nói cách khác, mỗi phần thanh toán sẽ đi qua một đường dẫn nút khác nhau. Điều này tránh được các hạn chế về thanh khoản trên một kênh duy nhất trong tuyến. Trong MPP cơ bản, mỗi phần thanh toán chia sẻ cùng một bí mật và do đó cùng một Hash trong HTLC. Điều này có thể khiến giao dịch có thể truy xuất được nếu người quan sát có mặt trên nhiều tuyến, vì người đó có thể liên kết tất cả các bí mật giống hệt nhau này lại với nhau. Hơn nữa, vì bí mật là duy nhất cho tất cả các phần của khoản thanh toán, nên nó không phải là nguyên tử. Điều này có nghĩa là một số phần của khoản thanh toán có thể được thực hiện thành công, trong khi những phần khác có thể không thành công.


Trong AMP, các bí mật cục bộ duy nhất được sử dụng cho mỗi phân số. Sau khi nhận được tất cả các phân đoạn, chúng cho phép người nhận tái tạo bí mật chung ban đầu và yêu cầu thanh toán đầy đủ. Phương pháp này khiến việc thanh toán một phần trở nên bất khả thi, vì cần phải sở hữu tất cả các bí mật cục bộ để mở khóa toàn bộ thanh toán. Điều này đảm bảo rằng thanh toán hoàn toàn thành công hoặc hoàn toàn không thành công (tức là nguyên tử). AMP cũng cải thiện tính bảo mật, vì không còn bất kỳ liên kết nào có thể nhìn thấy giữa các tuyến đường khác nhau.


Một lợi thế của AMP là chúng hoạt động ngay cả khi chỉ có người nhận và người gửi triển khai phương pháp này. Các nút trung gian xử lý các khoản thanh toán này như các giao dịch thông thường bằng HTLC, không biết rằng họ đang xử lý một phần của một khoản thanh toán lớn hơn.