---
name: BitcoinVoucherBot P2P
description: Hướng dẫn mua và bán Bitcoin P2P bằng BitcoinVoucherBot
---

![image](assets/cover.webp)



Chúng ta vẫn còn nghe về BitcoinVoucherBot, một bot Telegram được tạo ra để mua Bitcoin mà không cần [KYC](https://planb.academy/resources/glossary/kyc-know-your-customer) thông qua chuyển khoản ngân hàng SEPA. Thật không may, kể từ tháng 11 năm 2025, BitcoinVoucherBot ở dạng tập trung không còn khả dụng như một dịch vụ không yêu cầu KYC nữa.



Trong hướng dẫn này, chúng ta sẽ xem xét cách thức hoạt động của tính năng mới cho phép người dùng mua và bán Bitcoin trực tiếp trên thị trường P2P (giao dịch ngang hàng) mới, do đó không cần xác minh danh tính (KYC). Để đối phó với những hạn chế mới ngày càng đe dọa tự do kỹ thuật số và quyền riêng tư, các nhà phát triển đã tạo ra tiện ích mở rộng này, cho phép người dùng mua và bán Bitcoin với mức độ ẩn danh cao thông qua P2P (giao dịch ngang hàng). Hãy cùng nhau xem phương thức trao đổi mới này hoạt động như thế nào.



Để sử dụng dịch vụ này, bạn sẽ phải thực hiện chuyển khoản qua Lightning Network. Vì vậy, hãy đảm bảo bạn có wallet hỗ trợ giao thức này và cho phép bạn sử dụng "LNURL" hoặc "Lightning Address" để nhận và gửi tiền.



Trong số các ví được hỗ trợ, chúng ta có thể tìm thấy:





- [Sats.Mobi](https://planb.academy/tutorials/wallet/mobile/satsmobi-ea04e1cd-609a-4ea8-9c61-f9de1fe3a1fb) (Bot Telegram) (Custodial)
- [Wallet của Satoshi](https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7) (Lưu trữ có chuyển đổi sang không lưu trữ)
- [Breez](https://planb.academy/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06) (Không giam giữ)



Hoặc bất kỳ wallet nào có "Lightning Address" và tạo ra hóa đơn Bolt11. Ví generate tạo ra hóa đơn Bolt12 hiện không được hỗ trợ. Để biết thêm thông tin, hãy xem định nghĩa của [Bolt](https://planb.academy/resources/glossary/bolt).



Trong hướng dẫn này, vì tính dễ sử dụng ngay lập tức của nó, chúng ta sẽ sử dụng Wallet of Satoshi.



**Lưu ý**: Wallet of Satoshi, mặc dù phổ biến với người mới bắt đầu, là loại lưu ký có quyền kiểm soát hạn chế đối với tiền; chỉ nên sử dụng tạm thời, chuyển ngay lập tức sang loại không lưu ký để có quyền tự chủ hoàn toàn. Tính đến tháng 10 năm 2025, nó bao gồm chế độ tự lưu ký ổn định trên toàn thế giới trên iOS/Android (cập nhật ứng dụng), với khóa riêng tư tự chủ, chuyển đổi giữa các chế độ, địa chỉ Lightning tùy chỉnh và sao lưu 12 từ seed. Tuy nhiên, nó vẫn chỉ là giải pháp tạm thời cho đến khi hợp nhất, nên ưu tiên sử dụng wallet không lưu ký đã ổn định để quản lý lâu dài.



Tuyệt vời! Giờ chúng ta có thể bắt đầu hành trình của mình, hướng dẫn bạn từng bước tạo tài khoản, quản lý các giao dịch mua bán và sử dụng khu vực dành riêng cho bạn.



## Wallet và Tuyển sinh



Trước tiên, nếu bạn chưa cài đặt ứng dụng này trên điện thoại thông minh của mình, hãy tải xuống Wallet of Satoshi.





- [Google Play](https://play.google.com/store/apps/details?id=com.livingroomofsatoshi.wallet&pli=1)
- [App Store](https://apps.apple.com/au/app/wallet-of-satoshi/id1438599608)



![image](assets/it/01.webp)



Nếu bạn chưa từng sử dụng Wallet of Satoshi và muốn hiểu cách hoạt động của nó, tôi khuyên bạn nên làm theo hướng dẫn này để có thể kích hoạt đúng cách và sao lưu dữ liệu một cách an toàn.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Giờ wallet của bạn đã sẵn sàng, bạn có thể bắt đầu gửi một lượng nhỏ sats. Hãy nhớ rằng, để hoàn tất việc đăng ký nền tảng P2P (Giao dịch ngang hàng), bạn sẽ cần gửi 1000 sats như một biện pháp kiểm soát: điều này nhằm tạo ra rào cản chống lại bất kỳ cuộc tấn công lừa đảo nào, ngăn chặn bất kỳ ai đăng ký mà không có bộ lọc thư rác.



![image](assets/it/02.webp)



Giờ đây, chúng ta có thể mở nền tảng P2P (mạng ngang hàng) để tiến hành đăng ký. Bạn có thể đăng nhập từ máy tính để bàn hoặc trình duyệt trên điện thoại thông minh, thông qua Telegram BitcoinVoucherBot hoặc qua các liên kết .onion để đảm bảo mức độ riêng tư cao hơn.



Nếu bạn chọn sử dụng liên kết Tor .onion, tôi cũng khuyên dùng "Tor Browser". Nếu bạn chưa biết về nó, bạn có thể tìm hiểu thêm tại liên kết này:



https://planb.academy/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

Bây giờ hãy chọn cách bạn muốn truy cập nền tảng.





- [BitcoinVoucherBot](https://t.me/BitcoinVoucherBot?start=55360009) (Telegram)
- [Máy tính để bàn / Trình duyệt trên điện thoại thông minh](https://p2p.bitcoinvoucher.bot/?ref=55360009)
- [Tor .Onion](http://umembxtpokml6fkogemcfnpyt3qqvyw6u3hnvwinevo3gvoe6j7vfyad.onion/?ref=55360009)



Bạn sẽ được chuyển hướng đến trang chính.



Nhấn vào "Bắt đầu" để bắt đầu ngay lập tức.



![image](assets/it/03.webp)



Trên màn hình tiếp theo, bạn phải chọn một mật khẩu và nhập nó (ô A), sau đó nhập lại (ô B). Tôi khuyên bạn nên lưu mật khẩu này ngay lập tức vào một phương tiện sao lưu, có thể là trên một thiết bị kỹ thuật số an toàn như "Bitwarden":



https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

Hoặc lưu mật khẩu của bạn vào một phương tiện giấy (**cảnh báo**: đây không phải là giải pháp tốt, nhưng có thể chấp nhận được nếu chỉ dùng tạm thời).



Hãy đánh dấu vào ô xác nhận nơi bạn xác nhận rằng bạn không phải là robot (ô C). Xin lưu ý: Không bật mã hóa RSA trừ khi bạn hiểu chính xác nó là gì và cách hoạt động của nó. Bạn không cần làm gì ở bước này. Nhấp vào "Tạo Avatar" ("Tạo Avatar") (ô D).



![image](assets/it/04.webp)



Giờ bạn cần phải trả 1000 sats để hoàn tất quá trình đăng ký.



1. Bắt đầu từ trên xuống, trước tiên hãy xem "ID Avatar" được tạo ngẫu nhiên và cực kỳ quan trọng của bạn. Hãy lưu lại cẩn thận, giống như tôi đã khuyên bạn nên làm với mật khẩu.


2. Sau đó, bạn phải nhập "Lightning Address" vào ô bên dưới. Điều này sẽ cho phép bạn nhận thanh toán nếu bạn mua Bitcoin, hoặc nhận hoàn tiền. Nếu bạn đang sử dụng Wallet hoặc Satoshi, bạn có thể sao chép Address của mình bằng cách nhấp vào "nhận".


3. Tích vào ô xác nhận nơi bạn khẳng định rằng mình không phải là robot.


4. Thanh toán 1000 sats để truy cập vào khu vực hạn chế của bạn. Nếu bạn không thể đóng khung nó, hãy nhấp chuột (trên máy tính) hoặc chạm vào nó bằng ngón tay (trên trình duyệt/điện thoại thông minh Telegram) để sao chép địa chỉ cần dán vào Wallet of Satoshi và hoàn tất thanh toán hóa đơn.



![image](assets/it/05.webp)



Đây là LNURL Address của bạn.



![image](assets/it/06.webp)



Chúc mừng!!! Bạn đã tạo Avatar vĩnh viễn và có thể xem tóm tắt tại đây. Một lần nữa, tôi khuyên bạn nên lưu lại Avatar và mật khẩu cẩn thận, như tôi đã đề nghị trước đó.



Nhấp vào `Tôi đã lưu thông tin đăng nhập của mình, tiếp tục` (dịch là: "Tôi đã lưu thông tin đăng nhập của mình, tiếp tục")



![image](assets/it/07.webp)



Bạn hiện đang ở trung tâm của nền tảng, nơi bạn có thể xem tất cả các giao dịch khớp lệnh cùng với thông tin chi tiết của chúng. Để dễ hình dung hơn, bên dưới là hình ảnh hiển thị trên trang web từ máy tính để bàn.





- "Loại" ("Type") xác định xem đó là giao dịch "Bán" ("sell") hay giao dịch "mua"
- "Số lượng" ("Amount"): cho biết người dùng đang bán bao nhiêu sats nếu trận đấu thuộc loại "Bán", hoặc người dùng sẵn sàng mua bao nhiêu Bitcoin nếu trận đấu thuộc loại "Mua".
- "Giá BTC có ký quỹ" ("Giá BTC có ký quỹ"): hiển thị giá đã tính đến khoản ký quỹ được áp dụng trên giá trị được đánh dấu.
- "Tỷ lệ chênh lệch giá" ("Margin") là phần trăm được áp dụng cho giá thị trường. Với dấu trừ (-), bạn được giảm giá so với giá thị trường, với dấu cộng (+), giá sẽ cao hơn so với giá thị trường.
- "Phương thức" ("Method") cho biết người dùng muốn được thanh toán bằng phương thức motodo nào.
- "Người tạo" là hình đại diện duy nhất mà người dùng sử dụng trên nền tảng này.
- "Rep" (Uy tín): Mức độ uy tín của người dùng dao động từ -5 (không đáng tin cậy) đến +5 (cực kỳ đáng tin cậy).
- "Trạng thái" ("Status"): cho biết trạng thái của trận đấu. Trong ảnh chụp màn hình ví dụ, tất cả các trận đấu đều hiển thị là "Mở" ("Open").
- "Thời gian hết hạn" ("Expiration"): hiển thị thời gian còn lại trước khi trận đấu kết thúc và bị hủy nếu không có ai chọn.



![image](assets/it/08.webp)



Ở góc trên bên phải, hãy nhấp vào ảnh đại diện của bạn để truy cập hồ sơ cá nhân.



![image](assets/it/09.webp)



Tại đây, bạn có thể thấy tên Avatar, ID người dùng, ngày tạo và điểm uy tín của mình, những yếu tố này sẽ phản ánh tích cực hoặc tiêu cực đến hành vi của bạn trong các cuộc đàm phán.



![image](assets/it/10.webp)



Trong phần Cài đặt, bạn có thể xem "Lightning Address" đã nhập trong quá trình đăng ký và thay đổi nếu cần. Bạn cũng có tùy chọn tạo Khóa công khai, như đã đề cập, chỉ nên thiết lập nếu bạn có đủ kỹ năng cần thiết. Khóa này được sử dụng để mã hóa các tin nhắn bạn sẽ trao đổi với đối tác trực tiếp từ máy tính của mình.



Tính năng Thông báo của Telegram rất được khuyến khích sử dụng. Khi kích hoạt tính năng này, một mã QR sẽ hiện ra để bạn quét bằng ứng dụng Telegram: bằng cách này, bạn sẽ nhận được thông báo theo thời gian thực về tất cả các hành động liên quan đến các trận đấu của mình, trực tiếp trong khung chat của bot trên Telegram.



![image](assets/it/11.webp)



Cuối cùng, bạn sẽ thấy phần giới thiệu, hiển thị thu nhập được tạo ra bởi những người dùng mà bạn đã mời. Từ đây, bạn có thể sử dụng nút để chia sẻ liên kết hoặc mã QR của mình và, ở phía dưới một chút, xem danh sách các kết quả phù hợp để theo dõi uy tín của bạn cùng với điểm số tương ứng.



![image](assets/it/12.webp)



## Tạo đơn đặt hàng để mua Bitcoin



Vào Marketplace: từ thanh điều hướng chính, nhấp vào biểu tượng giỏ hàng "Marketplace" ("Marketplace") để mở sổ đặt hàng. Sau đó, bắt đầu một đơn hàng mới: nhấn nút "New Order" ("New Order") để bắt đầu quá trình.



![image](assets/it/13.webp)





- Chi tiết đơn hàng:
- Chọn tùy chọn "Mua Bitcoin" ("Mua Bitcoin").
- Nhập số lượng sats bạn muốn.
- Xác định biên độ giá (trong khoảng từ -20% đến +20% so với giá thị trường).
- Hãy chọn phương thức thanh toán (SEPA tức thì, v.v.).
- Chỉ định loại tiền tệ ưu tiên.
- Xác nhận đơn hàng: nhấp vào "Tạo đơn hàng" ("Xác nhận đơn hàng") để chuyển sang bước nộp đơn.



![image](assets/it/14.webp)



Cần đặt cọc: Khách hàng cần đặt cọc 10% tổng số tiền cộng thêm phí dịch vụ để kích hoạt đơn hàng.




- Thanh toán tiền đặt cọc: khi đơn hàng được tạo, hệ thống sẽ tự động tạo hóa đơn Lightning. Tiền đặt cọc chỉ là tạm thời và sẽ được hoàn trả khi đơn hàng hoàn tất.
- Các tính năng chính:
- Tiền đặt cọc: 10% giá trị đơn hàng.
- Phí dịch vụ: chi phí sử dụng nền tảng.
- Thời hạn: Bạn có 5 phút để thực hiện thanh toán, nếu không giao dịch sẽ bị hủy bỏ.



![image](assets/it/15.webp)



Sau khi thanh toán thành công, lệnh sẽ xuất hiện trong sổ lệnh và hiển thị cho tất cả người dùng, những người có thể chọn và chấp nhận lệnh. Để tạo lệnh bán, tất cả những gì bạn cần làm là nhấp vào "Bán Bitcoin", nhập số lượng satoshi bạn muốn bán, đặt mức ký quỹ, chọn phương thức thanh toán và loại tiền tệ, sau đó tiến hành đặt cọc 10% làm tiền đặt cọc bảo đảm. Sau khi hoàn tất, lệnh của bạn sẽ hiển thị trong danh sách.



![image](assets/it/16.webp)



## Cách chấp nhận đơn đặt hàng



1. Người bán có thể xem danh sách tất cả các đơn hàng hiện có trong sổ.


2. Kiểm tra chi tiết: mỗi đơn hàng đều hiển thị các thông tin như sau:




  - Số lượng Bitcoin,
  - Lợi nhuận trên giá bán,
  - Phương thức thanh toán,
  - Uy tín người dùng.



![image](assets/it/17.webp)



3. Nhấp vào đơn hàng để mở toàn bộ bảng tính với đầy đủ thông tin.


4. Nhấn vào "Bán Bitcoin" ("Bán Bitcoin") để chấp nhận đề nghị.



![image](assets/it/18.webp)



## Người bán yêu cầu đặt cọc.



Khi đơn hàng được chấp nhận, hệ thống sẽ tạo hóa đơn thanh toán. Tiền đặt cọc bao gồm:



- Tổng số tiền của đơn hàng,



- Ủy ban dịch vụ.



Việc thanh toán tiền đặt cọc phải được thực hiện trong thời hạn quy định, nếu không giao dịch sẽ không được xác nhận.



![image](assets/it/19.webp)



## Hướng dẫn gửi thanh toán



Sau khi khoản tiền gửi được thực hiện, giao dịch sẽ hiển thị trên bảng điều khiển cá nhân của người bán, người bán phải cung cấp thông tin chi tiết cho người mua để hoàn tất thanh toán bằng tiền tệ thông thường.



1. Người bán hiển thị giao dịch đang hoạt động trên bảng điều khiển của họ.


2. Nhấp vào "Gửi hướng dẫn thanh toán".


3. Nhập đầy đủ thông tin cần thiết cho việc thanh toán bằng tiền pháp định (IBAN, người nhận, địa chỉ, lý do thanh toán, v.v.).


4. Nhấp vào "Gửi tin nhắn" để truyền dữ liệu cho người mua.



![image](assets/it/20.webp)



## Quy trình thanh toán



Người mua sẽ nhận được một tin nhắn trong khung chat của nền tảng, chứa đầy đủ thông tin cần thiết để thực hiện thanh toán bằng tiền tệ pháp định:




- Thông tin ngân hàng: Số IBAN kèm tên và địa chỉ chủ tài khoản của người bán.
- Số tiền chính xác: số tiền pháp định chính xác cần chuyển.
- Nguyên nhân/mô tả: văn bản cần được đưa vào giao dịch.
- Thời hạn: hạn chót để hoàn tất thanh toán.



Việc chuyển tiền diễn ra bên ngoài hệ thống P2P và phải được thực hiện thông qua tổ chức ngân hàng của người nhận.



⚠️ **Lưu ý quan trọng:** Việc xác nhận trên nền tảng chỉ nên được thực hiện sau khi bạn đã hoàn tất việc chuyển khoản hoặc thanh toán bằng tiền tệ thông qua ngân hàng của mình.



![image](assets/it/21.webp)



## Xác nhận thanh toán bằng tiền pháp định



Bước này rất quan trọng đối với người mua và chỉ nên được thực hiện sau khi đã xác minh rằng khoản thanh toán đã thực sự được gửi đi.



1. Nhận dữ liệu: người mua đã nhận được hướng dẫn thanh toán từ người bán.


2. Thực hiện thanh toán: việc chuyển tiền được thực hiện từ tài khoản ngân hàng của người nhận.


3. Xác minh: kiểm tra xem thao tác đã được xử lý chính xác hay chưa.


4. Xác nhận trên nền tảng: nhấp vào "Xác nhận thanh toán tiền pháp định" ("Confirm fiat payment") trên trang giao dịch.


Nút "Xác nhận thanh toán bằng tiền pháp định" xuất hiện trong phần giao dịch và chỉ nên được sử dụng sau khi đã xác minh rằng khoản thanh toán đã được gửi thành công.



![image](assets/it/22.webp)



Bước cuối cùng trong quy trình là người bán xác nhận đã nhận được khoản thanh toán bằng tiền pháp định, sau đó satss sẽ được chuyển cho người mua.



![image](assets/it/23.webp)



## Phần kết luận



Với hy vọng rằng hướng dẫn này sẽ giúp bạn sử dụng một phương pháp mới để giao dịch Bitcoin hoặc thậm chí chỉ để mua chúng, dù là để lưu trữ giá trị cho riêng mình hay để bắt đầu hiện thực hóa các khoản thanh toán hàng ngày. Tuy nhiên, đây vẫn là một cánh cửa cần khám phá để đối phó với những gì sắp xảy ra trong thế giới kỹ thuật số của chúng ta.



Vòng vây do các thế lực kiểm soát chúng ta giăng ra đang siết chặt, dẫn đến việc hình thành một Internet ngày càng bị kiểm soát. Bằng cách mua P2P, bạn sẽ giữ kín hoàn toàn các giao dịch mua bán của mình, không để lại dấu vết và không phải chịu bất kỳ hậu quả nào từ bên thứ ba.