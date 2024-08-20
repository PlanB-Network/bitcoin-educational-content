---
term: ELTOO
---

ELTOO là một giao thức chung cho các lớp thứ hai của Bitcoin, định nghĩa cách để quản lý chung quyền sở hữu của một UTXO. Eltoo được thiết kế bởi Christian Decker, Rusty Russell và Olaoluwa Osuntokun, nhằm giải quyết các vấn đề liên quan đến cơ chế thương lượng của trạng thái kênh Lightning, tức là giữa việc mở và đóng. Kiến trúc Eltoo đơn giản hóa quá trình thương lượng bằng cách giới thiệu một hệ thống quản lý trạng thái tuyến tính, thay thế phương pháp tiếp cận dựa trên hình phạt đã được thiết lập bằng một phương pháp cập nhật linh hoạt và ít phạt hơn. Giao thức này yêu cầu sử dụng một loại SigHash mới cho phép bỏ qua tất cả các đầu vào trong chữ ký của một giao dịch. SigHash này ban đầu được gọi là `SIGHASH_NOINPUT`, sau đó là `SIGHASH_ANYPREVOUT` (*Bất Kỳ Đầu Ra Trước Đó*). Việc triển khai nó được lên kế hoạch trong BIP118.

> ► *Eltoo đôi khi còn được gọi là "LN-Symmetry".*