---
name: Ngọc bích - Electrum
description: Cách sử dụng Jade hoặc Jade Plus với Electrum (máy tính để bàn)
---

![cover](assets/cover.webp)



_Hướng dẫn này được trích từ [bài học Hội thảo Bitcoin](https://officinebitcoin.it/lezioni/jadeele/index.html)_



Hướng dẫn này được thực hiện bằng Jade Classic, nhưng các thao tác cũng có thể áp dụng cho những người dùng Jade Plus.



Sau khi khởi tạo Jade, bạn có thể bắt đầu sử dụng nó và - để làm như vậy - hãy chọn màn hình wallet.



Jade là một thiết bị có thể sử dụng với nhiều ứng dụng wallet hoặc các ứng dụng đi kèm như Blockstream chỉ định trên trang web của mình.



Trong hướng dẫn này, bạn sẽ thấy các bước sử dụng Electrum Wallet thông qua kết nối cáp USB.



## Chuyển giao khóa công khai



Hãy bật Jade đã được khởi tạo của bạn lên. Ngay khi bạn bật nó lên, nó sẽ trông như thế này:




![img](assets/en/32.webp)



Nếu bạn chọn _Mở khóa Jade_, bạn sẽ thấy menu nơi bạn phải chọn cách kết nối thiết bị của mình với ứng dụng đồng hành.



Với Electrum, bạn chỉ có thể kết nối Jade qua USB, vì vậy hãy chọn phương pháp này.



Khởi chạy Electrum, tùy chọn mở mặc định sẽ mở wallet được sử dụng gần đây nhất.



Nếu đây là lần đầu tiên bạn kết nối Jade với Electrum, hãy chọn _Tạo ví mới_ rồi chọn _Hoàn tất_.



![img](assets/en/34.webp)



Tên là wallet.



![img](assets/en/35.webp)



Chọn tiêu chuẩn Wallet.



![img](assets/en/36.webp)



Khi chọn kho khóa, điều cần thiết là phải chọn _Sử dụng thiết bị phần cứng_.



![img](assets/en/37.webp)



Electrum bắt đầu quét thiết bị phần cứng.



![img](assets/en/38.webp)



Khi kết nối USB với máy tính (đã được kết nối với Jade ở cổng USB C), phần cứng wallet sẽ hiển thị ở chế độ khóa. Jade sẽ mở khóa bằng cách nhập mã PIN sáu chữ số đã thiết lập trong quá trình thiết lập.




![img](assets/en/39.webp)



Thiết bị phần cứng đã mở khóa, Electrum phát hiện Jade. Tiếp tục bằng cách nhấp vào _Tiếp theo_.



![img](assets/en/40.webp)



Tại thời điểm này, Electrum yêu cầu bạn thiết lập tập lệnh chính sách: chọn _Native Segwit_.



![img](assets/en/41.webp)



Giai đoạn chuyển giao khóa công khai từ wallet từ Jade sang màn hình Electrum bắt đầu.



Khi quá trình xuất khóa công khai hoàn tất, quá trình sẽ kết thúc.



Chỉ xem khi đã sẵn sàng và Electrum sẽ cảnh báo khi hoàn tất bằng màn hình sau.



![img](assets/en/42.webp)



wallet thực sự đã được tạo và bạn có thể bắt đầu khám phá nó: bạn có thể thấy _địa chỉ_, _thông tin ví_, và quan trọng nhất là bạn có thể thấy ở góc dưới bên phải dấu hiệu cho biết đó là thiết bị của Blockstream. Dấu chấm màu xanh lá cây bên cạnh logo Blockstream cho biết thiết bị đã được bật và kết nối đúng cách với mạng cục bộ.



![img](assets/en/43.webp)



## Giao dịch nhận và chi tiêu



Từ menu _Nhận_ của Electrum, generate, hãy nhập `scriptPubKey` (địa chỉ) để nhận tiền. Luôn bắt đầu với số tiền nhỏ và thực hiện kiểm tra nhận + chi.



![img](assets/en/44.webp)



Sau khi nhận được satss, bạn có thể kiểm tra thời gian nhận satss trong menu _Lịch sử_.



![img](assets/en/45.webp)



![img](assets/en/46.webp)



Sau khi giao dịch được xác nhận, bạn có thể sử dụng UTXO này và hoàn tất bài kiểm tra.



Chi phí liên quan đến việc sử dụng Jade để ký.



Vào menu _Send_ của Electrum, dán scriptPubKey và kiểm tra kỹ.



![img](assets/en/47.webp)



Khi hoàn tất, nhấn _Thanh toán_.



Cửa sổ giao dịch sẽ mở ra, trong đó bạn cần thiết lập đúng phí giao dịch. Sau khi hoàn tất mọi thiết lập, hãy nhấp vào _Xem trước_ ở góc dưới bên phải.



![img](assets/en/48.webp)



Cửa sổ giao dịch hiển thị một số chi tiết quan trọng, trước hết là trạng thái: `Chưa ký`.



Ở giai đoạn này, bạn cũng có thể thấy lệnh _Sign_, bạn phải nhấp vào lệnh này để ký tên bằng Jade.



![img](assets/en/49.webp)



Bây giờ bắt đầu giai đoạn giao tiếp giữa màn hình wallet và thiết bị phần cứng, trong đó Electrum sẽ cảnh báo bạn làm theo hướng dẫn trên thiết bị phần cứng, được bật và sẵn sàng để ký.



![img](assets/en/50.webp)



**Trước tiên, bạn nên xác minh những gì bạn đang ký: tất cả các thông số của giao dịch bạn vừa thiết lập cũng xuất hiện trên Jade** và bạn có thể xác minh tất cả.



![img](assets/en/51.webp)



Để tiếp tục, hãy đảm bảo bạn luôn đặt con trỏ vào mũi tên `→` dẫn đến các bước tiếp theo và không bao giờ đặt con trỏ vào `X` trừ khi bạn muốn kết thúc thao tác mà không hoàn tất nó.



Phần xác minh kết thúc bằng màn hình hiển thị phí. Lúc này, việc xác nhận tương đương với việc bạn ký tên.



![img](assets/en/52.webp)



Trong một khoảnh khắc ngắn, Jade xử lý thao tác, khi hoàn tất, nó sẽ trở về menu trang chủ.



![img](assets/en/53.webp)



Trong khi trên Electrum, bạn có thể thấy trạng thái của giao dịch đã thay đổi từ `Chưa ký` thành `Đã ký` và bây giờ bạn có thể truyền bá giao dịch đó bằng cách nhấp vào _Phát sóng_.



![img](assets/en/54.webp)



Sau khi được thử nghiệm, wallet có thể được sử dụng để chứa UTXO nhằm mục đích lưu trữ an toàn.



![img](assets/en/55.webp)



Hướng dẫn này là một ví dụ về cách sử dụng Jade của bạn, được kết nối qua USB, với đồng hồ wallet. Electrum là một ví dụ điển hình, nhưng bạn có thể thích phần mềm wallet khác. Jade xuất khóa công khai sang nhiều ví khác: hãy tìm các chức năng tương tự mà bạn đã đọc trong hướng dẫn này, để được hướng dẫn và tìm cách sử dụng nó trên ứng dụng đồng hành yêu thích của bạn.