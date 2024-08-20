---
term: ASSUME UTXO
---

Một tham số cấu hình trong ứng dụng Bitcoin Core hàng đầu cho phép một nút vừa được khởi tạo (nhưng chưa trải qua IBD) hoãn việc xác minh các giao dịch và bộ UTXO cho đến một bản chụp nhất định. Khái niệm này dựa trên việc sử dụng một bộ UTXO (danh sách tất cả UTXO hiện có tại một thời điểm nhất định) được cung cấp bởi Core và được giả định là chính xác, cho phép nút được đồng bộ hóa rất nhanh chóng với chuỗi có nhiều công việc tích lũy nhất. Vì nút bỏ qua bước IBD dài, nó trở nên hoạt động nhanh chóng cho người dùng của mình. Assume UTXO chia quá trình đồng bộ hóa (IBD) thành hai phần:
* Đầu tiên, nút thực hiện Đồng bộ Hóa Đầu Tiên Theo Header (xác minh chỉ các header) và coi bộ UTXO do Core cung cấp là hợp lệ;
* Sau đó, khi đã hoạt động, nút sẽ xác minh toàn bộ lịch sử khối ở chế độ nền, cập nhật một bộ UTXO mới mà nó đã xác minh. Nếu bộ UTXO mới này không khớp với bộ do Core cung cấp, nó sẽ tạo ra một thông báo lỗi.

Do đó, Assume UTXO tăng tốc quá trình chuẩn bị một nút Bitcoin mới bằng cách hoãn quá trình xác minh giao dịch và bộ UTXO thông qua một bản chụp cập nhật được cung cấp trong Core.