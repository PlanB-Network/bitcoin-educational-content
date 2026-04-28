---
term: Assume utxo

definition: Một tham số Bitcoin Core cho phép đồng bộ hóa nhanh của nút mới bằng cách sử dụng ảnh chụp của bộ UTXO được coi là hợp lệ, trước khi xác minh lịch sử trong nền.
---
Tham số cấu hình trong ứng dụng khách đa số Bitcoin Core cho phép một nút vừa được khởi tạo (nhưng chưa thực hiện IBD) trì hoãn việc xác minh các giao dịch và tập hợp UTXO trước một ảnh chụp nhanh (snapshot) nhất định. Khái niệm này dựa trên việc sử dụng một tập hợp UTXO (danh sách tất cả các UTXO hiện có tại một thời điểm nhất định) do Core cung cấp và được giả định là chính xác, cho phép nút được đồng bộ hóa rất nhanh trên chuỗi có khối lượng công việc tích lũy nhiều nhất. Vì nút bỏ qua bước IBD dài nên nó nhanh chóng hoạt động cho người dùng của mình.

Assume UTXO chia quá trình đồng bộ hóa (IBD) thành hai phần: Đầu tiên, nút thực hiện Header First Sync (chỉ xác minh các tiêu đề) và coi tập hợp UTXO do Core cung cấp là hợp lệ; Sau đó, khi đã hoạt động, nút sẽ xác minh toàn bộ lịch sử khối trong nền, cập nhật một tập hợp UTXO mới mà chính nó đã xác minh. Nếu tập hợp sau này không khớp với tập hợp UTXO do Core cung cấp, nó sẽ đưa ra thông báo lỗi.

Do đó, Assume UTXO cho phép tăng tốc việc chuẩn bị một nút Bitcoin mới bằng cách trì hoãn quá trình xác minh các giao giao dịch và tập hợp UTXO nhờ vào ảnh chụp nhanh (snapshot) cập nhật được cung cấp trong Core.





