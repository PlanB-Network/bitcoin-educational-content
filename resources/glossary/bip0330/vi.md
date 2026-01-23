---
term: BIP0330
definition: Erlay, tối ưu hóa việc lan truyền giao dịch giúp giảm mức sử dụng băng thông khoảng 40%.
---

Một đề xuất được gọi là "*Erlay*", nhằm mục đích tối ưu hóa việc truyền bá các giao dịch chưa được xác nhận trong mạng Bitcoin. Hiện tại, các giao dịch được phát đến tất cả các đối tác của một nút, dẫn đến tình trạng dư thừa và sử dụng quá mức băng thông. BIP330 đề xuất giới hạn việc phát này ở 8 đối tác theo mặc định, sau đó sử dụng cơ chế đối chiếu để chia sẻ hiệu quả các giao dịch bị thiếu. Erlay giảm mức tiêu thụ băng thông khoảng 40%. Nó cũng tránh được tình trạng tăng tuyến tính mức tiêu thụ băng thông theo số lượng đối tác được kết nối với nút.