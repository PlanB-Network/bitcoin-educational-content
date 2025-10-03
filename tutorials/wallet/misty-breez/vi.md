---
name: Misty Breez
description: Lightning Wallet không có bát.
---

![misty-breez-cover](assets/cover.webp)



Misty Breez là Wallet tự giữ Lightning do Breez phát triển dựa trên Bộ phát triển phần mềm của họ và mạng **Liquid** do BlockStream phát triển.


Nó đi kèm với một cách tiếp cận hoàn toàn mới để vận hành mà không cần nút Lightning: một **BÍ QUYẾT THAY ĐỔI CUỘC CHƠI** tiềm năng trong việc chuyển giao liên mạng Bitcoin.


Trong hướng dẫn này, chúng tôi sẽ mô tả cách danh mục đầu tư này hoạt động và cung cấp cho bạn cái nhìn tổng quan đầy đủ.



## Misty Breez hoạt động như thế nào?



Misty Breez là một triển khai không có nút Lightning làm backend. Nó được phát triển trên cơ sở Breez SDK và Liquid.



Liquid là Layer song song với mạng Bitcoin, mang lại những cải tiến đáng kể về tốc độ và chi phí giao dịch. Layer này cho phép Misty Breez không cần nút Lightning và thay vào đó sử dụng các dịch vụ Exchange của bên thứ ba như **Boltz** để đảm bảo khả năng tương tác giữa Liquid Network và Lightning Network. Đừng vội, chúng ta sẽ quay lại vấn đề này.



Bây giờ, chúng ta hãy bắt đầu cuộc phiêu lưu với Misty Breez Wallet.



## Bắt đầu với Misty Breez



Ứng dụng di động Misty Breez có sẵn trên các nền tảng tải xuống chính thức như Google Play Store (trên Android) và Apple Store (trên iOS). Bạn cũng có thể được chuyển hướng đến đúng ứng dụng từ trang web chính thức [Misty Breez] (https://breez.technology/misty/).



⚠️ Hãy đảm bảo bạn không nhầm lẫn Misty Breez với Breez Wallet.



⚠️ **QUAN TRỌNG**: Để đảm bảo an toàn cho bitcoin của bạn, điều cần thiết là phải tải xuống ứng dụng từ các nền tảng chính thức để đảm bảo tính xác thực của ứng dụng.



![download-misty-breez](assets/fr/01.webp)



Trong hướng dẫn này, chúng ta sẽ bắt đầu từ thiết bị Android. Tuy nhiên, mỗi bước và tính năng cụ thể được nêu chi tiết trong phần này đều áp dụng cho iOS.



Sau khi cài đặt, Misty Breez cung cấp cho bạn tùy chọn tạo Wallet mới hoặc khôi phục Lightning Wallet cũ mà bạn có từ khóa khôi phục.


Trong hướng dẫn này, chúng ta sẽ chọn tạo một danh mục đầu tư mới.



⚠️Misty Breez hiện đang trong giai đoạn phát triển, vì vậy chúng tôi khuyên bạn nên bắt đầu với số lượng hợp lý.



![create-wallet](assets/fr/02.webp)


### Lưu các từ khôi phục của bạn:


Một trong những điều đầu tiên bạn nên làm khi tạo danh mục đầu tư mới là sao lưu 12 từ khôi phục của mình.


Sau đây là một số mẹo về cách sao lưu cụm từ dự phòng của bạn.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Để sao lưu cụm từ của bạn, hãy chọn menu **Tùy chọn > Bảo mật**, sau đó chọn tùy chọn **Kiểm tra cụm từ sao lưu**.



![backup](assets/fr/03.webp)


Để tăng cường bảo mật, bạn cũng có thể **tạo mã PIN** để xác thực quyền truy cập vào Wallet của mình.




Tìm loại tiền tệ địa phương của bạn trong số nhiều loại tiền tệ được Misty Breez chấp nhận. Cấu hình loại tiền tệ của bạn từ menu **Tùy chọn > Tiền tệ Fiat**, sau đó chọn loại tiền tệ hoặc các loại tiền tệ bạn yêu cầu.



![devises](assets/fr/04.webp)



### Thực hiện giao dịch đầu tiên của bạn


Nếu bạn đã quen thuộc với danh mục đầu tư Breez, bạn sẽ không hề cảm thấy khó chịu với Interface trực quan của Misty Breez.



Trên menu **Số dư** của Interface, hãy nhấp vào tùy chọn **Nhận** để tạo hóa đơn nhận bitcoin của bạn trên Wallet.



⚠️ Misty Breez sẽ yêu cầu bạn kích hoạt thông báo cho ứng dụng trong phần cài đặt của điện thoại để được cấp quyền sở hữu Lightning Address.



Với Misty Breez, bạn có thể:




- Nhận bitcoin trên Lightning Network từ **100 satoshi** lên đến **25.000.000 satoshi**.
- Nhận bitcoin trên mạng chính Bitcoin từ **25.000 satoshi**.



![transactions](assets/fr/05.webp)



Đây chính là nơi phép thuật của Misty Breez bắt đầu.


Không giống như Breez Wallet, cung cấp cho bạn một nút Lightning và yêu cầu bạn tự chi trả chi phí mở và đóng kênh thanh toán, Misty Breez không yêu cầu bạn phải làm gì cả. Như đã đề cập trước đó, Misty Breez thậm chí không hoạt động trên cơ sở một nút Lightning.



Chúng ta hãy cùng xem xét kỹ hơn hậu trường.



Trên thực tế, bạn sở hữu danh mục đầu tư Liquid liên quan đến danh mục đầu tư Misty Breez của bạn. Về mặt logic, bạn sẽ xử lý L-BTC (Liquid Bitcoin) với tỷ giá cố định liên quan đến các dịch vụ chuyển đổi satoshi ngầm của bên thứ ba cho phép bạn tương tác với Lightning Network.



Khi bạn nhận được khoản thanh toán trên Misty Breez Wallet của mình, người gửi sẽ gửi cho bạn satoshi, số satoshi này sẽ được chuyển qua dịch vụ chuyển đổi như Boltz (hiện đang được Misty Breez sử dụng) để chuyển đổi satoshi được gửi thành L-BTC, số L-BTC này sẽ được nhận trên Misty Breez Wallet của bạn (liên kết với Liquid Wallet).


Sau đây là sơ đồ đơn giản về quy trình diễn ra đằng sau hậu trường.



![lnswap-in](assets/fr/06.webp)



Nhấp vào Interface trong menu **Số dư**, nhấp vào tùy chọn **Gửi** để thanh toán Lightning Invoice.


Cắm Lightning Invoice, Lightning Address của người nhận hoặc chỉ cần quét mã QR trên Invoice để thực hiện thanh toán.



![send-bitcoins](assets/fr/07.webp)



Về cơ bản, bạn kích hoạt Liquid Wallet được liên kết với Misty Breez Wallet của bạn để chuyển đổi lượng L-BTC tương đương thành satoshi thông qua Boltz, sau đó chuyển những satoshi này đến Lightning Wallet của người nhận (có trên Lightning Network).



![send-bitcoin-bts](assets/fr/08.webp)



Tính năng này của cơ sở hạ tầng Misty Breez cho phép người dùng thực hiện giao dịch ngay cả khi Misty Breez ngoại tuyến.



Đối với những người có nhiều kinh nghiệm hơn, cũng có một menu **Tùy chọn > Nhà phát triển** cung cấp cho bạn thêm thông tin chi tiết về:




- Phiên bản của Bộ phát triển phần mềm Breez.
- Khóa công khai của Misty Breez Wallet của bạn.
- Người vay, mã định danh duy nhất được lấy từ khóa công khai chính.
- Số dư danh mục đầu tư của bạn.
- Mẹo Liquid để gửi số lượng nhỏ L-BTC.
- Đầu Bitcoin dùng để gửi một lượng nhỏ Bitcoin.



Bạn cũng có thể thực hiện một số hành động nhất định, chẳng hạn như đồng bộ hóa với Liquid Network, sao lưu khóa, chia sẻ nhật ký hoạt động và chọn quét lại Liquid Network.



![dev-mode](assets/fr/09.webp)


Xin chúc mừng! Bây giờ bạn đã hiểu rõ về danh mục Misty Breez và đóng góp của nó vào các giao dịch liên mạng Bitcoin. Nếu bạn thấy hướng dẫn này hữu ích, vui lòng cho chúng tôi một ngón tay cái Green. Chúng tôi rất vui khi được nghe từ bạn.



Để tìm hiểu sâu hơn, tôi cũng khuyên bạn nên khám phá hướng dẫn của chúng tôi về Aqua Wallet, hoạt động theo cách tương tự như Misty Breez:



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125