---
name: Amboss
description: Khám phá và phân tích Lightning Network
---

![cover](assets/cover.webp)



Lightning Network là phiên bản Layer của giao thức Bitcoin, được phát triển chủ yếu để thúc đẩy việc áp dụng thanh toán Bitcoin hàng ngày bằng cách tăng tốc độ xử lý của mỗi giao dịch. Dựa trên nguyên tắc phi tập trung, Lightning Network bao gồm các nút (máy tính chạy triển khai Lightning) giao tiếp ngang hàng, chuyển tiếp dữ liệu (thanh toán và xác minh thanh toán) cho nhau.



https://planb.network/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Cũng như trên chuỗi chính, việc cho phép người dùng biết thông tin và trạng thái của mạng lưới là điều cần thiết để tạo điều kiện thuận lợi cho việc kết nối giữa các nút và giảm thiểu vấn đề thanh khoản thường phát sinh trong mạng lưới. Trên thực tế, trên Lightning Network, chúng tôi khuyến nghị các khoản thanh toán nhỏ với số tiền tương đối nhỏ hơn so với các giao dịch trên chuỗi chính Bitcoin.



Điều quan trọng cần lưu ý là không phải tất cả các nút Lightning đều có sẵn trên nền tảng Amboss.



Giống như [Mempool Space](https://Mempool.space), cung cấp thông tin hữu ích về chuỗi chính của giao thức Bitcoin, kể từ năm 2022, [Amboss](https://amboss.space) cung cấp thông tin về:





- Các nút trên Lightning Network
- Các kênh thanh toán và khả năng thanh toán của chúng
- Sự tiến hóa của Lightning Network theo thời gian
- Thống kê về chi phí chuyển tiếp đến các nút thanh toán của bạn.



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

Trong hướng dẫn này, chúng tôi sẽ đưa bạn tham quan nền tảng này, đây là tài nguyên thiết yếu cho người dùng Lightning Network, những người muốn kết nối nút của mình để mở rộng mạng, v.v.




## Tìm cặp



Một trong những mục tiêu của nền tảng Amboss là cho phép các nút khác nhau trong mạng kết nối và trao đổi thông tin với nhau. Trên trang chủ của nền tảng, bạn có thể trực tiếp tìm kiếm tên của một nút mà bạn đã biết hoặc tìm các nút từ các danh mục Lightning phổ biến nhất mà bạn đang sử dụng.



![home](assets/fr/01.webp)



![wallet](assets/fr/02.webp)



https://planb.network/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f

Trên trang chủ, bạn cũng sẽ tìm thấy các nút được phân loại theo:




- Tiến hóa dung lượng: số lượng Bitcoin được liên kết với khóa công khai của nút và tổng số có sẵn trên tất cả các kênh của nút đó.
- Sự phát triển của kênh: số lượng kết nối mới tới các nút khác trong mạng.
- Mức độ phổ biến của nút: tần suất sử dụng nút.



![nodes](assets/fr/03.webp)



Do đó, việc lựa chọn đúng nút để kết nối phụ thuộc vào việc kiểm tra các tiêu chí sau:





- Đảm bảo rằng nút có đủ số lượng bitcoin; sức chứa của nút càng lớn thì số lượng bitcoin bạn có thể thanh toán càng lớn.





- Đảm bảo rằng nút có nhiều kết nối và kênh mở với các nút khác trong mạng.





- Đảm bảo nút này đang hoạt động và vẫn được các nút khác trong mạng đánh giá cao bằng cách kiểm tra số kênh mới; nút này mở càng nhiều kênh mới thì càng được các nút khác trong mạng đánh giá cao.



Khi đã tìm thấy đúng nút, hãy nhấp vào tên nút đó để được chuyển hướng đến trang thông tin nút.



Trên Interface này, bằng cách kiểm tra Timestamp của kênh mới tạo, bạn sẽ biết được hoạt động của nút này. Bạn cũng sẽ tìm thấy thông tin về dung lượng của các kênh của nút này: thông tin này rất quan trọng nếu bạn muốn chủ động sử dụng nút này để thực hiện thanh toán.




![node_info](assets/fr/04.webp)



Ở phần bên trái, bạn sẽ tìm thấy thêm thông tin chi tiết về vị trí của nút này. Ví dụ: bạn có thể xem:




- Khóa công khai: mã định danh ngay bên dưới tên nút.
- Vị trí địa lý của nút này.




![channels](assets/fr/05.webp)



Interface này cho bạn biết kết nối Address cho nút này: nó có dạng `pubkey@ip:port`. Trong ví dụ của chúng ta, chúng ta muốn kết nối đến nút có:




- khóa công khai `pubkey` là: `035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226`
- iP Address: `170.75.163.209`
- Cổng: `9735`



![geoinfo](assets/fr/06.webp)



Trong phần **Kênh**, bạn sẽ thấy danh sách các kênh đang mở và kết nối của nút với các nút khác trong mạng. Trên Interface này, một số thông tin quan trọng cần được xem xét để xác nhận nút này có đáp ứng nhu cầu của chúng ta hoặc có đáng tin cậy hay không:





- Tỷ lệ đầu vào**: Số tiền mà nút sẽ tính phí cho bạn cho mỗi triệu Satoshi mà nó nhận được, tùy thuộc vào kênh được chọn.
- Tỷ lệ (phần triệu)**: biểu thị số Satoshi trên một triệu đơn vị mà nút sẽ tính phí khi bạn quyết định thanh toán qua một trong các kênh của nó. Giả sử bạn quyết định thanh toán `10_000 Sats` qua một kênh có tỷ lệ ppm là `500 Sats`, bạn sẽ phải trả cho nút `10_000 * 500 / 1_000_000` satoshi, tương đương với `5 Sats`.
- [HTLC](https://planb.network/resources/glossary/htlc) tối đa**: Số lượng tối đa mà nút này cho phép bạn chuyển qua một trong các kênh này.



Bằng cách tham khảo bảng trong Interface này, bạn cũng có thể tìm thấy tất cả thông tin này trên nút mà nó khớp với.



![channels_info](assets/fr/07.webp)



Trong phần **Bản đồ kênh**, bạn có thể xem phân phối và dung lượng của các kênh khác nhau trên nút này. Bạn có thể thay đổi tiêu chí phân phối được hiển thị bằng cách chọn một trong các tùy chọn trong danh sách thả xuống bên phải.



![cha_maps](assets/fr/08.webp)



Phần **Kênh đóng** nhóm tất cả các kênh trước đây của nút theo loại đóng:




- Đóng chung**: thể hiện sự đồng ý của cả hai bên, những bên sử dụng khóa riêng của mình để ký giao dịch đánh dấu việc đóng kênh và phân phối số dư trong đó
- **Đóng cửa bắt buộc**: là việc đóng đột ngột, đơn phương một phần của kênh. Kiểu đóng cửa này không được khuyến khích, vì Lightning Network là một giao thức dựa trên hình phạt: khi bạn cố gắng gian lận số dư của một kênh, bạn có nguy cơ mất toàn bộ số dư khả dụng trong kênh đó.



![closed](assets/fr/09.webp)



Nhận thông tin về phí chuyển khoản để định tuyến thanh toán của bạn thông qua kênh trên nút bạn sử dụng



![fees](assets/fr/10.webp)



## Thông tin mạng



Amboss không chỉ tập trung vào thông tin thành viên mạng mà còn vào trạng thái của chính mạng đó.



Trong phần **Thống kê**, bên dưới menu "Mô phỏng" bên trái, bạn sẽ thấy biểu đồ hiển thị xác suất thanh toán thành công theo số tiền thanh toán.



Trên thực tế, bạn sẽ nhận thấy đường cong đang giảm dần vì khi số tiền thanh toán của bạn tăng lên, khả năng khoản thanh toán đó được xử lý thành công sẽ thấp hơn. Điều này phản ánh vấn đề thanh khoản thực sự trên Lightning Network. Ví dụ: khoản thanh toán `10_000` satoshi của bạn có `79%` khả năng được thực hiện. Mặt khác, với khoản thanh toán `3_000_000` satoshi, bạn có ít hơn `13%` khả năng thành công.



![network](assets/fr/11.webp)



Menu **Thống kê mạng** cho phép bạn hiển thị số liệu thống kê theo đồ họa cho:




- Kênh thanh toán
- Các nút
- Dung tích
- Phí
- Sự phát triển của kênh.



![network_stat](assets/fr/12.webp)



Trong menu **Thống kê thị trường**, tùy chọn **Chi tiết lệnh** cho phép bạn xem nhu cầu thanh khoản trên Lightning Network. Biểu đồ này cũng có thể hiển thị kênh nào có nhu cầu cao nhất và/hoặc kênh nào có dung lượng giao dịch đáng kể.



![markets](assets/fr/13.webp)




## Công cụ



Amboss cung cấp một số công cụ giúp bạn tối ưu hóa tìm kiếm và hành động của mình.



### Bộ giải mã Lightning Network



Công cụ này chủ yếu có chức năng cung cấp cho bạn thông tin chi tiết về cấu trúc của Lightning Invoice, Lightning Address hoặc Lightning URL.



Trên trang chủ, trong phần **Công cụ**, hãy gửi Lightning Address của bạn chẳng hạn.



![decoder](assets/fr/14.webp)



Từ bộ giải mã này, bạn có thể thu được thông tin như sau:




- khóa công khai của nút được liên kết với Lightning Address của bạn;
- Thời hạn sử dụng của Invoice so với Address của bạn;
- Số tiền tối thiểu và tối đa bạn có thể gửi;
- Nút Nostr được liên kết với Address của bạn, nếu Nostr được bật trên nút này.



![decode](assets/fr/15.webp)



### Magma IA



Khám phá công cụ mới nhất do Amboss giới thiệu để quản lý hiệu quả các kết nối của bạn với các nút Lightning Network. Magma AI sử dụng trí tuệ nhân tạo chuyên dụng để tập trung vào một vấn đề quan trọng: lựa chọn đúng các nút để kết nối.



![magma](assets/fr/16.webp)



### Máy tính Satoshi



Tìm hiểu giá hiện tại của Bitcoin theo đơn vị tiền tệ địa phương của bạn (EUR / USD). Trên trang chủ, hãy sử dụng công cụ tính satoshi để tìm giá thị trường hiện tại.



![calculator](assets/fr/17.webp)




Bạn đã khám phá đầy đủ các tính năng và công cụ phân tích của nền tảng. Vui lòng xem bài viết của chúng tôi về trình khám phá Bitcoin **Mempool.space** bên dưới.



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f