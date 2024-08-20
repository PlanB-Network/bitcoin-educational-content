---
term: BIP156
---

Đề xuất, được biết đến với tên Dandelion, nhằm mục đích cải thiện sự riêng tư của việc định tuyến giao dịch trong mạng Bitcoin để chống lại việc bỏ mặt nạ danh tính. Trong hoạt động tiêu chuẩn của Bitcoin, các giao dịch được phát sóng ngay lập tức đến nhiều nút. Nếu một quan sát viên có thể thấy mỗi giao dịch được mỗi nút trên mạng chuyển tiếp, họ có thể giả định rằng nút đầu tiên gửi giao dịch cũng là nút gốc của giao dịch đó, và do đó nó đến từ người vận hành nút. Hiện tượng này có thể cho phép quan sát viên liên kết các giao dịch, thường là ẩn danh, với địa chỉ IP.

Mục tiêu của BIP156 là giải quyết vấn đề này. Để làm điều này, nó giới thiệu một giai đoạn bổ sung trong quá trình phát sóng để bảo tồn sự ẩn danh trước khi phát sóng công khai. Do đó, Dandelion đầu tiên sử dụng một giai đoạn "stem" nơi giao dịch được gửi qua một đường dẫn ngẫu nhiên của các nút, trước khi được phát sóng đến toàn bộ mạng trong giai đoạn "fluff". Stem và fluff là những tham chiếu đến hành vi của sự lan truyền giao dịch qua mạng, giống hình dạng của một bông hoa bồ công anh (*dandelion* trong tiếng Anh).

Phương pháp định tuyến này làm mờ dấu vết dẫn trở lại nút gốc, khiến việc truy tìm một giao dịch qua mạng trở lại nguồn gốc của nó trở nên khó khăn. Dandelion do đó cải thiện sự riêng tư bằng cách hạn chế khả năng của kẻ thù để bỏ mặt nạ danh tính mạng. Phương pháp này càng hiệu quả hơn khi giao dịch trong giai đoạn "stem" qua một nút mà mã hóa giao tiếp mạng của nó, như với Tor hoặc *P2P Transport V2*. BIP156 chưa được thêm vào Bitcoin Core.

![](../../dictionnaire/assets/36.png)