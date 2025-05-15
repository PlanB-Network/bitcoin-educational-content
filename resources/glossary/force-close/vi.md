---
term: BUỘC ĐÓNG
---

Cơ chế đóng kênh Lightning không hợp tác. Khi hai người dùng mở một kênh bằng Multisig 2/2, mỗi người có thể đơn phương đóng kênh bằng cách phát Commitment Transaction cuối cùng đã được ký, để khôi phục bitcoin trên chuỗi của họ. Điều này được gọi là "buộc đóng".


Phương pháp này thường được sử dụng nếu một trong những người tham gia không còn phản hồi nữa hoặc nếu việc đóng kênh hợp tác là không thể. Nếu có thể tránh được việc đóng bắt buộc, thì tốt nhất là như vậy, vì mất nhiều thời gian hơn để khôi phục tiền trên chuỗi và có thể tốn kém hơn nhiều về mặt phí.


Trong một lần đóng bắt buộc, một trong hai người dùng phát Commitment Transaction, phản ánh trạng thái đã biết cuối cùng của kênh Lightning. Sau đó, có một khoảng thời gian khóa trước khi bitcoin có thể được lấy lại trên chuỗi, cho bên kia thời gian để xác minh rằng giao dịch tương ứng với trạng thái kênh mới nhất. Nếu người dùng cố gắng gian lận bằng cách xuất bản Commitment Transaction lỗi thời, bên kia có thể sử dụng bí mật thu hồi để trừng phạt kẻ gian lận và khôi phục tất cả tiền trong kênh.