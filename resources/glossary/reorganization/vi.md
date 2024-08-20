---
term: TÁI TỔ CHỨC
---

Đề cập đến hiện tượng blockchain trải qua sự thay đổi cấu trúc do sự tồn tại của các khối cạnh tranh ở cùng một độ cao. Điều này xảy ra khi một phần của blockchain được thay thế bằng một chuỗi khác có lượng công việc tích lũy lớn hơn.

Những tái tổ chức này là một phần của chức năng tự nhiên của Bitcoin, nơi các thợ mỏ khác nhau có thể tìm thấy các khối mới gần như đồng thời, do đó chia mạng Bitcoin thành hai. Trong những trường hợp như vậy, mạng có thể tạm thời chia thành các chuỗi cạnh tranh. Cuối cùng, khi một trong những chuỗi này tích lũy được nhiều công việc hơn, các chuỗi khác sẽ bị các nút bỏ qua, và các khối của chúng trở thành những gì được gọi là "khối lỗi thời" hoặc "khối mồ côi". Quá trình thay thế một chuỗi bằng chuỗi khác được gọi là tái tổ chức.

![](../../dictionnaire/assets/9.png)

Tái tổ chức có thể có nhiều hậu quả. Đầu tiên, nếu một người dùng có một giao dịch được xác nhận trong một khối mà sau đó bị bỏ qua, nhưng giao dịch này không xuất hiện trong chuỗi cuối cùng hợp lệ, thì giao dịch của họ trở nên chưa được xác nhận một lần nữa. Đó là lý do tại sao luôn được khuyến cáo chờ đợi ít nhất 6 xác nhận để coi một giao dịch thực sự không thể thay đổi. Sau 6 khối, khả năng tái tổ chức xảy ra rất thấp đến mức có thể coi là gần như không xảy ra.

Hơn nữa, ở cấp độ hệ thống toàn cầu, tái tổ chức có nghĩa là lãng phí sức mạnh tính toán của các thợ mỏ. Thực sự, khi một sự chia rẽ xảy ra, một số thợ mỏ sẽ ở trên chuỗi `A`, và những người khác trên chuỗi `B`. Nếu chuỗi `B` cuối cùng bị bỏ qua trong một tái tổ chức, thì tất cả sức mạnh tính toán được triển khai bởi các thợ mỏ trên chuỗi này, theo định nghĩa, là lãng phí. Nếu có quá nhiều tái tổ chức trên mạng Bitcoin, an ninh tổng thể của nó do đó được giảm bớt. Đây là một phần lý do tại sao việc tăng kích thước khối hoặc giảm khoảng thời gian giữa mỗi khối (10 phút) có thể nguy hiểm.

> ► *Một số người yêu thích Bitcoin thích sử dụng "khối mồ côi" để chỉ một khối hết hạn. Ngoài ra, trong ngôn ngữ thông thường, "reorg" được sử dụng để chỉ "tái tổ chức". Thuật ngữ "tái tổ chức" là một từ vay mượn từ tiếng Anh. Để chính xác hơn, người ta có thể nói về "đồng bộ hóa lại".*