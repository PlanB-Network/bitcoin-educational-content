---
name: StashPay
description: Bitcoin Wallet tối giản dành cho mọi người
---

![cover](assets/cover.webp)



Trải nghiệm người dùng là yếu tố then chốt trong việc áp dụng các giải pháp Bitcoin trên toàn cầu. Việc cung cấp trải nghiệm mượt mà, đơn giản và không bị cản trở về mặt kỹ thuật là ưu tiên hàng đầu của nhiều ví điện tử và nền tảng Exchange. Về mặt này, StashPay nổi bật với phương pháp tối giản, đồng thời thể hiện sức mạnh của Lightning Network.



Trong hướng dẫn này, chúng ta sẽ xem xét danh mục đầu tư này để tìm hiểu cách thức hoạt động và lý tưởng cho các doanh nghiệp nhỏ hoặc người kinh doanh đơn lẻ.



## Bắt đầu với StashPay



StashPay là một ví Wallet tự quản lý Lightning, được biết đến chủ yếu nhờ trải nghiệm người dùng tối giản, lấy người dùng làm trung tâm. Với Wallet này, bạn không cần bất kỳ kiến thức kỹ thuật nào để nhận và gửi những satoshi đầu tiên.



StashPay là một dự án mã nguồn mở được phát triển trên React Native và nhằm mục đích giải quyết vấn đề phí giao dịch cao ngay cả với các giao dịch trên chuỗi chính của giao thức Bitcoin. Ứng dụng có sẵn dưới dạng ứng dụng di động trên nền tảng Android và iOS thông qua các liên kết tải xuống có trên [trang web](https://stashpay.me/).



![introduce](assets/fr/01.webp)



Điều quan trọng là phải tải ứng dụng Android từ trang web vì ứng dụng này không có sẵn trên Cửa hàng Google Play.


Khi quá trình tải xuống hoàn tất, vui lòng cấp các quyền cần thiết để bạn có thể cài đặt ứng dụng trên điện thoại Android của mình.



Sau khi cài đặt ứng dụng, StashPay sẽ tạo một Bitcoin Wallet ban đầu cho bạn ngay lần đầu tiên bạn mở ứng dụng. Trước bất kỳ giao dịch nào, chúng tôi khuyên bạn nên sao lưu Wallet này. Dưới đây là tất cả các hướng dẫn của chúng tôi để đảm bảo cụm từ khôi phục của bạn được sao lưu đúng cách.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Truy cập cài đặt StashPay bằng cách nhấp vào biểu tượng "Cài đặt", sau đó nhấp vào tùy chọn **Tạo bản sao lưu**. Sau đó, cho phép hiển thị cụm từ khôi phục. Không sao chép cụm từ khôi phục vào bộ nhớ tạm của điện thoại, vì chúng có thể bị các ứng dụng gian lận khác cài đặt trên thiết bị di động của bạn truy cập.



![backup](assets/fr/02.webp)



Bạn cũng có thể khôi phục Bitcoin Wallet mà bạn đang sử dụng bằng cách nhấp vào tùy chọn **Khôi phục Wallet** và chèn 12 hoặc 24 từ khôi phục của bạn.



### Nhận satoshi đầu tiên của bạn trên StashPay



Trên màn hình chính, nhấp vào nút **Nhận** và đặt số tiền lớn hơn số tiền được chỉ định bằng màu đỏ. Trong trường hợp của chúng tôi, chúng tôi không thể nhận ít hơn 0,11 USD với StashPay Wallet.



![receive](assets/fr/03.webp)



Sau khi xác định số tiền, bạn có thể nhấp vào nút **Tạo Invoice**, sau đó quét hoặc sao chép Invoice để gửi đến người gửi satoshi của bạn.



![receive_sats](assets/fr/04.webp)



Bạn có thể xem lịch sử giao dịch của mình bằng cách nhấp vào biểu tượng "đồng hồ" trên trang chủ.



![network_fee](assets/fr/05.webp)



Bạn sẽ nhận thấy rằng để nhận satoshi, bạn sẽ phải trả phí mạng. Phí này sẽ được khấu trừ vào số satoshi bạn sắp nhận. Lý do là vì StashPay là Wallet dựa trên Bộ công cụ Phát triển Breez. Để nhận satoshi với việc triển khai Bộ công cụ không cần nút Lightning, Breez sẽ tính phí khách hàng (trong trường hợp của chúng tôi là StashPay) `0,25% + 40 satoshi`. Tìm hiểu thêm trong hướng dẫn Misty Breez của chúng tôi.



https://planb.network/tutorials/wallet/mobile/misty-breez-738ced2a-0764-4d7f-a150-ec0ce84a9d25

### Gửi bitcoin với StashPay



Việc gửi Bitcoin với StashPay khá trực quan nhờ giao thức Interface tối giản. Trên màn hình chính, nhấp vào nút **Gửi**. Quét mã QR hoặc dán giao thức Address mà bạn muốn gửi satoshi. StashPay sẽ tự động phát hiện chuỗi giao thức Bitcoin mà bạn muốn gửi Bitcoin.



![send](assets/fr/06.webp)



Vì StashPay là Wallet dựa trên Bộ công cụ Phát triển Breez, nên nó được hưởng lợi từ một lợi thế thú vị: gửi bitcoin trên chuỗi chính với chi phí thấp. Breez sử dụng dịch vụ Boltz để thực hiện giao dịch giữa các chuỗi khác nhau của giao thức Bitcoin, cho phép khách hàng triển khai Bộ công cụ Phát triển được hưởng lợi trực tiếp từ dịch vụ này trong ứng dụng của họ.



https://planb.network/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

Tuy nhiên, Breez SDK áp đặt số tiền tối thiểu mà bạn có thể gửi bitcoin đến Address trên chuỗi chính.



![onchain](assets/fr/07.webp)



Bạn cũng có thể gửi bitcoin bằng Lightning Address của người nhận. Hãy xem lại thông tin giao dịch, sau đó xác nhận bằng cách nhấp vào nút **Gửi**.



![confirm](assets/fr/08.webp)



## Nhiều cấu hình hơn



Trong cài đặt StashPay, bạn có thể điều chỉnh cấu hình để cá nhân hóa việc sử dụng Wallet của mình.



StashPay cho phép bạn chuyển đổi Exchange satoshi dựa trên đơn vị tiền tệ địa phương bạn chọn. Nhấp vào tùy chọn **Tiền tệ**, sau đó tìm kiếm loại tiền tệ của bạn trong danh sách +113 loại tiền tệ do StashPay cung cấp.



![currencies](assets/fr/09.webp)



Trong menu **Tùy chọn nhận**, bạn sẽ tìm thấy tất cả các cài đặt để nhận bitcoin với StashPay. Ví dụ: bằng cách chọn **Chọn Lightning hoặc Onchain**, hãy cho phép Wallet của bạn nhận bitcoin từ chuỗi chính.



![receive-onchain](assets/fr/10.webp)



Tùy chọn **Quét địa chỉ OnChain** cho phép bạn làm mới số dư Wallet của mình bằng cách kiểm tra tất cả UTXO (bitcoin mà bạn chưa chi tiêu) được liên kết với nhiều địa chỉ khác nhau của bạn.



![rescan](assets/fr/11.webp)



Menu **Xuất nhật ký** liệt kê tất cả các hoạt động của cơ sở hạ tầng Breez và Boltz liên quan đến các giao dịch và trao đổi nguyên tử giữa các chuỗi giao thức Bitcoin khác nhau.



![export](assets/fr/12.webp)



Bạn vừa làm quen với Bitcoin Wallet tối giản của StashPay. Nếu bạn thấy hướng dẫn này hữu ích, chúng tôi khuyên bạn nên xem hướng dẫn của chúng tôi về cách bắt đầu sử dụng Bitcoin và kiếm những đồng bitcoin đầu tiên.



https://planb.network/courses/obtenir-ses-premiers-bitcoins-f3e3843d-1a1d-450c-96d6-d7232158b81f