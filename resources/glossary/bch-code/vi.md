---
term: MÃ BCH
---

Một lớp mã sửa lỗi được sử dụng để phát hiện và sửa lỗi trong chuỗi dữ liệu. Nói cách khác, mã sửa lỗi BCH được sử dụng để tìm và sửa lỗi ngẫu nhiên trong thông tin được truyền đi, để đảm bảo thông tin đến đích nguyên vẹn. Từ viết tắt "BCH" là chữ cái đầu của tên những người phát minh ra các mã này: Bose, Ray-Chaudhuri và Hocquenghem.


Công cụ này được sử dụng trong nhiều lĩnh vực điện toán, bao gồm SSD, DVD và mã QR. Ví dụ, nhờ các mã sửa lỗi này, ngay cả khi mã QR bị che một phần, vẫn có thể truy xuất thông tin mà nó mã hóa.


Là một phần của Bitcoin, mã BCH được sử dụng cho tổng kiểm tra trong các định dạng Bech32 và Bech32m (sau SegWit) Address. Chúng đại diện cho sự thỏa hiệp tốt hơn giữa kích thước tổng kiểm tra và khả năng phát hiện lỗi so với các hàm Hash đơn giản trước đây được sử dụng trên các địa chỉ Legacy. Trong bối cảnh của Bitcoin, mã BCH chỉ được sử dụng để phát hiện lỗi, không phải để sửa lỗi. Do đó, phần mềm danh mục đầu tư Bitcoin sẽ xác định và báo cáo cho người dùng bất kỳ lỗi nào trong Address đang nhận, nhưng sẽ không tự động thay đổi Address không chính xác. Lựa chọn này được thúc đẩy bởi thực tế là việc tích hợp sửa lỗi chắc chắn sẽ ảnh hưởng đến khả năng phát hiện lỗi của thuật toán.