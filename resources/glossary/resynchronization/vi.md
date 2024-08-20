---
term: RESYNCHRONIZATION
---

Đề cập đến hiện tượng mà blockchain trải qua sự thay đổi cấu trúc của nó do sự tồn tại của các khối cạnh tranh ở cùng một độ cao. Điều này xảy ra khi một phần của blockchain được thay thế bằng một chuỗi khác có lượng công việc tích lũy lớn hơn.

Những quá trình đồng bộ hóa lại này là một phần của chức năng tự nhiên của Bitcoin, nơi mà các thợ mỏ khác nhau có thể tìm thấy các khối mới gần như đồng thời, từ đó chia mạng Bitcoin thành hai. Trong những trường hợp như vậy, mạng lưới có thể tạm thời chia thành các chuỗi cạnh tranh. Cuối cùng, khi một trong những chuỗi này tích lũy được nhiều công việc hơn, các chuỗi khác được các nút bỏ qua, và các khối của chúng trở thành những gì được gọi là "khối lỗi thời" hoặc "khối mồ côi". Quá trình thay thế một chuỗi bằng chuỗi khác này là đồng bộ hóa lại.

![](../../dictionnaire/assets/9.png)

Đồng bộ hóa lại có thể có nhiều hậu quả. Đầu tiên, nếu một người dùng có một giao dịch được xác nhận trong một khối mà sau đó được bỏ qua, nhưng giao dịch này không được tìm thấy trong chuỗi cuối cùng hợp lệ, thì giao dịch của họ trở nên chưa được xác nhận một lần nữa. Đó là lý do tại sao luôn được khuyến cáo chờ đợi ít nhất 6 xác nhận để coi một giao dịch thực sự không thể thay đổi. Sau 6 khối, việc đồng bộ hóa lại trở nên ít có khả năng đến mức có thể coi là gần như không xảy ra.

Hơn nữa, ở cấp độ hệ thống toàn cầu, đồng bộ hóa lại có nghĩa là sự lãng phí sức mạnh tính toán của các thợ mỏ. Thực sự, khi một sự chia rẽ xảy ra, một số thợ mỏ sẽ ở trên chuỗi `A`, và những người khác trên chuỗi `B`. Nếu chuỗi `B` cuối cùng bị bỏ qua trong một quá trình đồng bộ hóa lại, thì toàn bộ sức mạnh tính toán được triển khai bởi các thợ mỏ trên chuỗi này, theo định nghĩa, là lãng phí. Nếu có quá nhiều quá trình đồng bộ hóa lại trên mạng Bitcoin, an ninh tổng thể của mạng do đó được giảm bớt. Đây là một phần lý do tại sao việc tăng kích thước khối hoặc giảm khoảng thời gian giữa mỗi khối (10 phút) có thể là nguy hiểm.

> ► *Một số người yêu thích Bitcoin thích sử dụng "khối mồ côi" để chỉ một khối đã hết hạn. Ngoài ra, mặc dù đó là một Anglicism, trong ngôn ngữ thông thường, một "tổ chức lại" hoặc "reorg" thường được ưa chuộng hơn là "đồng bộ hóa lại".*