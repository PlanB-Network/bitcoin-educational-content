---
term: DỮ LIỆU VẬT
---

Timestamping, hay "Timestamp" trong tiếng Anh, là một cơ chế liên kết một mốc thời gian chính xác với một sự kiện, dữ liệu hoặc thông điệp. Trong bối cảnh chung của hệ thống máy tính, timestamping được sử dụng để xác định thứ tự thời gian của các hoạt động và để xác minh tính toàn vẹn của dữ liệu theo thời gian.


Trong trường hợp cụ thể của Bitcoin, dấu thời gian được sử dụng để thiết lập niên đại của các giao dịch và khối. Mỗi khối trong Blockchain chứa một Timestamp cho biết thời gian gần đúng khi khối đó được tạo ra. Satoshi Nakamoto thậm chí còn nói về "máy chủ Timestamp" trong Sách trắng của mình để mô tả những gì chúng ta gọi là "Blockchain" ngày nay. Vai trò của dấu thời gian trên Bitcoin là xác định niên đại của các giao dịch, do đó, không cần sự can thiệp của một cơ quan trung ương, có thể xác định được giao dịch nào đến trước. Cơ chế này cho phép mỗi người dùng xác minh sự không tồn tại của một giao dịch trong quá khứ và do đó ngăn chặn người dùng có ý đồ xấu thực hiện chi tiêu gấp đôi. Cơ chế này được Satoshi Nakamoto biện minh trong Sách trắng của mình bằng câu nói nổi tiếng: "*Tiêu chuẩn này dựa trên thời gian Unix, biểu thị tổng số giây đã trôi qua kể từ ngày 1 tháng 1 năm 1970.


> ► *Dấu thời gian khối tương đối linh hoạt trên Bitcoin, vì để Timestamp được coi là hợp lệ, thì nó chỉ cần lớn hơn thời gian trung bình của 11 khối trước nó (MTP) và nhỏ hơn thời gian trung bình do các nút trả về (thời gian điều chỉnh theo mạng) cộng với 2 giờ.*