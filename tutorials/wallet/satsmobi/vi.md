---
name: Sats.mobi

description: Một dịch vụ giám hộ có thể truy cập Telegram Wallet
---

![cover](assets/cover.webp)


_Hướng dẫn này được viết bởi_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)


## Sats.Mobi

SatsMobi là Wallet hoạt động trên Telegram, có tất cả các chức năng của Lightning Network (bảo vệ) Wallet, cùng với một loạt các tính năng rất thú vị. Nó bắt nguồn từ Fork của LightningTipBot hiện đã ngừng sản xuất, kế thừa tất cả các tính năng của nó trong khi bổ sung thêm nhiều tính năng hiện tại, do đó làm cho nó hiện đại hơn. Giống như LNTipBot, Sats.Mobi cũng áp dụng triết lý nguồn mở. Wallet có thể được cấu hình và quản lý độc lập bằng cách sao chép nó từ [kho lưu trữ] này (https://github.com/massmux/SatsMobiBot).


Nếu bạn muốn sử dụng đơn giản, khi bắt đầu trò chuyện trên Telegram, bạn sẽ thấy đó là bot.


## Cài đặt

Từ thanh tìm kiếm của Telegram, hãy tìm "satsmobi" và liên kết đến [bot](@SatsMobiBot) sẽ xuất hiện.


**Lưu ý**: Nếu bạn không chắc chắn về việc tìm kiếm qua Telegram, hãy truy cập bot một cách an toàn bằng [liên kết](https://t.me/SatsMobiBot) sau


![image](assets/it/01.webp)


Tất cả những gì bạn cần làm để bắt đầu là nhấn _START_


![image](assets/it/02.webp)


Để khám phá Wallet, bạn có thể chọn _Menu_ ở góc dưới bên trái.


![image](assets/it/03.webp)


Bây giờ hãy chọn _/help_ trong số các lệnh chính.


![image](assets/it/04.webp)


Sats.Mobi chào đón chúng ta bằng cách hiển thị một thông báo, liệt kê tất cả các chức năng chính. Khi khởi động, bot cũng tạo ra một LN Address, được liên kết với tên người dùng đã chọn trên Telegram (mặc định là duy nhất). Các lệnh để gửi và nhận Sats bằng Wallet này có thể nhìn thấy được, cũng như các chức năng khác mà chúng ta sẽ thấy sau. Thật thú vị khi xem qua menu _/advanced_


![image](assets/it/05.webp)


Có thể thấy Sats.Mobi cũng tạo ra một LN Address ẩn danh, để sử dụng cho mục đích giành quyền riêng tư. Bot hoạt động với các lệnh: chỉ cần nhấp vào từ tương ứng hoặc nhập dấu gạch chéo "/" vào thanh thông báo, theo sau là lệnh bạn muốn thực hiện. Ngay cả khi Wallet vừa mới được tạo, hãy chọn ví dụ _/transactions_


![image](assets/it/06.webp)


Lệnh này hiển thị danh sách các giao dịch mới nhất, trong trường hợp cụ thể này bằng không.


![image](assets/it/07.webp)


## Nhận Sats

Lệnh để tạo Invoice và nhận Sats là _/invoice_. Sats.Mobi hoạt động độc quyền trong Satoshi, đơn vị nhỏ nhất của Bitcoin; do đó, để tạo Invoice, cần phải viết số tiền trong Sats vào thanh tin nhắn rồi gửi vào phần trò chuyện với bot.

![image](assets/it/08.webp)


Trong ví dụ sau, lựa chọn được đưa ra là nhận số tiền là 210 Sats.


![cover](assets/it/09.webp)


Sau một vài phút chờ đợi Invoice được chuẩn bị, nó sẽ có dạng văn bản và mã QR. Khi thanh toán Invoice, Wallet sẽ hiển thị số dư. Nếu vì lý do nào đó mà tổng số tiền không được cập nhật, hãy viết _/balance_ và nhấn phím `enter`.


![image](assets/it/10.webp)


## Gửi Sats


Mặc dù Sats là một tài sản cực kỳ có giá trị mà chúng ta không nên dễ dàng từ bỏ, nhưng Sats.Mobi lại khiến phần này trở nên hấp dẫn, việc thực hiện một số thử nghiệm ngắn (tức là một vài giao dịch thử nghiệm) sẽ không thành vấn đề.


### Thanh toán Invoice


Cách đơn giản nhất để thanh toán Invoice là sao chép chuỗi tin nhắn `lnbc1xxxxx` và dán vào thanh tin nhắn sau khi nhập lệnh _/pay_. **Cú pháp đúng** yêu cầu phải để lại một khoảng trắng sau lệnh.


![image](assets/it/11.webp)


Wallet gửi tin nhắn yêu cầu xác nhận. Bằng cách nhấp vào _Pay_, Invoice được thanh toán.


![image](assets/it/12.webp)


Sats.Mobi có thể dựa vào một nút Lightning hiệu quả và được kết nối tốt, hiếm khi thanh toán thất bại vì nó luôn tìm được tuyến đường chính xác.


### Thanh toán thoải mái từ điện thoại di động


Duyệt trên Telegram, Sats.Mobi cũng khả dụng trên thiết bị di động. Chức năng thuận tiện nhất để thanh toán bằng thiết bị di động là quét mã QR, nhưng Wallet này không có chức năng này theo thiết kế, vì nó không phải là ứng dụng độc lập mà được chứa trong mạng xã hội. Do đó, Sats.Mobi được lập trình để tạo điều kiện thuận lợi cho trải nghiệm di động nhiều nhất có thể: nó thực sự có thể giải mã hình ảnh, giống như ảnh chụp mã QR của Invoice mà bạn muốn thanh toán.


Ví dụ, giả sử bạn muốn trả Invoice là 50 Sats.


![image](assets/it/20.webp)


Khi điều này được hiển thị, chúng tôi có thể chụp ảnh mã QR liên quan.


![image](assets/it/21.webp)


Sau đó, chúng tôi mở Telegram trên điện thoại di động và trong cuộc trò chuyện với Sats.Mobi, đính kèm ảnh vừa chụp mã QR


![cover](assets/it/22.webp)


Sau khi chọn, chúng tôi sẽ gửi nó tới bot:


![image](assets/it/23.webp)

Sats.Mobi giải mã ảnh và **ngay lập tức đưa ra yêu cầu thanh toán**, với mô tả chính xác. Trò chuyện yêu cầu xác nhận, để tiếp tục, bạn phải nhấn _/pay_

![image](assets/it/24.webp)


Vui lòng đợi một lát để quá trình thanh toán được xử lý.


![image](assets/it/25.webp)


Invoice có giá 50 đô la, Sats đã được thanh toán, một kết quả đạt được mà không cần sử dụng camera và chức năng quét tích hợp.


### Sats.Mobi trong Nhóm Telegram


![image](assets/it/27.webp)


Trong số những tính năng làm nên sự nổi tiếng của LNTipBot và Sats.Mobi mang đến cho Telegram, có một tính năng giúp trải nghiệm trở nên thú vị và tương tác hơn cho các thành viên trong nhóm.

Chủ sở hữu có thể mời bot tham gia trò chuyện nhóm và sau đó đề cử Sats.Mobi làm quản trị viên. Từ thời điểm đó, niềm vui bắt đầu, vì các thành viên có thể bắt đầu thưởng cho những người dùng khác vì sự đóng góp của họ cho nhóm.


- _/tip_ thêm tiền boa bằng cách trả lời tin nhắn;
- _/send_ gửi tiền với thông tin chỉ định LN Address hoặc tên người nhận là Telegram;
- _/faucet_ (trong menu _/advanced_) cho phép tạo một loạt mẹo mà các thành viên nhanh nhất trong nhóm có thể thu thập bằng cách nhấp vào _/collect_;
- _/tipjar_ (trong menu _/advanced_) tạo ra một loại phân phối khác có thể được gửi tới người dùng trong nhóm.


Mỗi lệnh này đều có cú pháp riêng, được giải thích trong menu lệnh chính.


Còn nếu chúng ta không phải là chủ sở hữu của một nhóm thì sao? Không vấn đề gì: chỉ cần yêu cầu người sáng lập mời Sats.Mobi, thêm nó làm quản trị viên của nhóm và bạn đã hoàn tất!


## Điểm bán hàng (POS)


Khi Sats.Mobi được khởi chạy lần đầu tiên, bot cũng tạo ra một tính năng khác cho người dùng: **POS**. "Thiết bị" được người dùng kích hoạt bằng lệnh _/pos_ hoặc bằng cách nhấp vào nút liên quan từ bảng điều khiển ở góc dưới bên phải. Trên thực tế, POS là một ứng dụng web, mở dưới dạng cửa sổ bật lên trên trò chuyện Telegram


![image](assets/it/14.webp)


Interface hiển thị tên người dùng Telegram cá nhân ở góc trên bên trái và được sử dụng đơn giản như mọi POS khác: bằng cách nhập số tiền trên bàn phím. Giả sử bây giờ chúng ta muốn thu 21 euro cent cho một dịch vụ. Biết rằng Sats.Mobi chỉ quản lý Sats, không dễ để thực hiện chuyển đổi trong đầu. Ngược lại, POS hiển thị euro là đơn vị tính toán, đồng thời hiển thị giá trị tương đương trong Satoshi.


![image](assets/it/15.webp)

Nhấp vào _/OK_ sẽ hiển thị Invoice có thể được hiển thị cho khách hàng thông qua mã QR hoặc có thể được gửi dưới dạng chuỗi thông qua tin nhắn tức thời để khách hàng có thể thanh toán.

![image](assets/it/16.webp)

![image](assets/it/17.webp)


Tất nhiên, POS cũng có sẵn trên điện thoại di động, truy cập theo cách tương tự như đã trình bày ở trên.


![image](assets/it/18.webp)


Nó cũng được hiển thị tốt trên màn hình điện thoại di động:


![image](assets/it/19.webp)


## Các tính năng bổ sung


Có những tính năng khác hoàn thiện dịch vụ của Sats.Mobi Wallet, như chúng ta đã thấy, mở rộng khái niệm về Wallet vượt ra ngoài các hoạt động nhận và gửi thanh toán:


- _/nostr_: để kết nối Wallet với người dùng Nostr của bạn để nhận zap;
- _/cashback_: hiển thị mã có thể được xuất trình cho người bán để được hoàn tiền khi mua hàng;
- _/buy_: bắt đầu một quy trình hướng dẫn trong bot, cho phép mua Sats bằng euro;
- _/activatecard_: để yêu cầu kích hoạt thẻ ghi nợ NFC, có thể nạp tiền qua Sats.Mobi Wallet và có thể kích hoạt thông báo;
- _/link_: tạo liên kết đến Zeus hoặc Blue Wallet của bạn, có thể được sử dụng làm điều khiển từ xa cho Wallet này.


## Phần kết luận

Sats.Mobi là một Wallet dễ chịu và thú vị khi sử dụng, mang lại những trải nghiệm đã có với LNTipBot khi sử dụng các chức năng tiên tiến hơn của LNBits. Tuy nhiên, điều quan trọng cần nhớ là **đây là dịch vụ lưu ký**. Do đó, nên sử dụng để giữ rất ít Sats, đây không phải là Wallet chính cho các quỹ Lightning Network của bạn. Ngoài ra còn có giới hạn dung lượng nội tại, bằng 500.000 Sats, một giới hạn được khuyên là không nên vượt quá.


Nếu bạn đang tìm kiếm ví Lightning Network không lưu ký, bạn chắc chắn nên xem xét các sản phẩm khác.


---
### Tài liệu


- [Github](https://github.com/massmux/SatsMobiBot)
- Danh sách phát [video](https://www.youtube.com/results?search_query=Sats.mobi) bản demo