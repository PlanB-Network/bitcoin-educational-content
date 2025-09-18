---
name: Minibits Wallet
description: Hướng dẫn sử dụng Minibits Wallet
---

![cover](assets/cover.webp)


Trong hướng dẫn này, tôi sẽ hướng dẫn bạn thiết lập Minibits Wallet để sử dụng ecash. Một công nghệ thanh toán mạnh mẽ, tập trung vào quyền riêng tư, hoạt động song song với Bitcoin. Minibits là ecash và Lightning Wallet cho phép chuyển tiền tức thì, tiết kiệm và riêng tư, lý tưởng cho các giao dịch hàng ngày cần sự riêng tư.


Trước khi tìm hiểu sâu hơn về Minibits, hãy cùng tìm hiểu rõ ecash là gì và không phải là gì. Nhiều người nhầm lẫn ecash với công nghệ Bitcoin hoặc Blockchain, nhưng về cơ bản chúng là những khái niệm khác nhau.


Ecash KHÔNG PHẢI là Bitcoin. Nó không thay thế Bitcoin và Wallet tự quản lý của bạn mà chỉ bổ sung cho nó. Ecash KHÔNG PHẢI là Blockchain và KHÔNG tồn tại trên bất kỳ Ledger công khai nào. Điều thú vị là, ecash KHÔNG phải là một công nghệ mới—nó thực sự đã có từ trước khi có mạng lưới toàn cầu, với các khái niệm được phát triển vào những năm 1980 và 1990.


Ecash LÀ GÌ: cực kỳ riêng tư (giao dịch không để lại lịch sử truy vết), ngang hàng (chuyển khoản trực tiếp không qua trung gian) và hoạt động như một công cụ mang thông tin kỹ thuật số (nếu bạn sở hữu nó, bạn sẽ kiểm soát nó). Một lợi thế quan trọng là Ecash CÓ THỂ được sử dụng ngoại tuyến—người gửi hoặc người nhận có thể ngắt kết nối internet trong khi giao dịch. Ecash CÓ THỂ được tạo ra bởi một bên duy nhất hoặc bởi một liên minh các tổ chức đáng tin cậy, và nó LÀ một công nghệ bổ sung hoàn hảo cho Bitcoin, xử lý các giao dịch nhỏ, thường xuyên trong khi Bitcoin đóng vai trò là đơn vị thanh toán Layer.


Xin lưu ý rằng thiết lập Minibits này là một `giải pháp lưu ký`, nghĩa là bạn tin tưởng đơn vị vận hành Mint sẽ quản lý tiền của mình. Điều này tiềm ẩn những rủi ro cụ thể mà bạn cần hiểu rõ trước khi tiến hành.


Dự án hiển thị thông báo từ chối trách nhiệm quan trọng này:


- Wallet này chỉ nên được sử dụng cho mục đích nghiên cứu.
- Wallet là phiên bản beta với chức năng chưa hoàn thiện và có cả lỗi đã biết và chưa biết.
- Không sử dụng với số lượng lớn tiền điện tử.
- Tiền điện tử được lưu trữ trong Wallet được phát hành bởi xưởng đúc tiền
- bạn tin tưởng xưởng đúc tiền sẽ hỗ trợ nó bằng Bitcoin cho đến khi bạn chuyển số tiền nắm giữ của mình sang một Bitcoin Lightning Wallet khác.
- Giao thức Cashu mà Wallet triển khai vẫn chưa được đánh giá hoặc thử nghiệm rộng rãi.


Hãy coi Minibit như một chiếc Wallet thông thường, không phải là một tài khoản tiết kiệm và không bao giờ lưu trữ giá trị đáng kể ở đây.


## 1️⃣ Thiết lập Wallet của bạn


Để bắt đầu, hãy truy cập [Trang web Minibits](https://www.minibits.cash/), tại đó bạn sẽ tìm thấy các tùy chọn tải xuống cho tất cả các nền tảng chính. Người dùng iOS có thể tải xuống từ [App Store](https://testflight.apple.com/join/defJQgTD), trong khi người dùng iOS EU có thêm tùy chọn cài đặt từ [Freedom Store](https://freedomstore.io/). Người dùng Android có thể tải ứng dụng từ [Google Play Store](https://play.google.com/store/apps/details?id=com.minibits_wallet) hoặc tải xuống tệp APK trực tiếp từ trang [GitHub Releases](https://github.com/minibits-cash/minibits_wallet/releases).


Khi cài đặt Minibits, bạn sẽ thấy màn hình giới thiệu giải thích các khái niệm cơ bản—bạn có thể đọc qua hoặc bỏ qua nếu đã quen thuộc với công nghệ này. Sau khi hoàn tất các bước ban đầu này, bạn sẽ được nhắc chọn giữa:


- `Đã hiểu, hãy đưa tôi đến Wallet` dành cho người dùng mới hoặc
- `Khôi phục Wallet đã mất` nếu bạn đang khôi phục từ bản sao lưu.


![image](assets/en/01.webp)

Sau khi hoàn tất thiết lập ban đầu, bạn sẽ đến Màn hình chính, nơi có một số Elements quan trọng cần lưu ý. ① Biểu tượng hồ sơ ở góc trên cùng sẽ đưa bạn đến trang hồ sơ của mình, nơi bạn có thể truy cập Minibits Wallet Address và chọn tùy chọn `nhận hàng loạt`. ② Ở giữa màn hình, bạn sẽ thấy các loại Mint bạn có thể sử dụng, với Minibits mint được chọn theo mặc định. ③ Hàng hành động bên dưới cung cấp các tùy chọn để gửi thanh toán ecash hoặc lightning, quét mã QR và nhận thanh toán. ④ Cuối cùng, thanh điều hướng phía dưới chứa các phím tắt đến Màn hình chính, Lịch sử giao dịch, Danh bạ và Cài đặt.


![image](assets/en/02.webp)


## 2️⃣ Quản lý bạc hà


Theo mặc định, Minibits Mint được bật khi bạn khởi động ứng dụng. Tuy nhiên, một trong những điểm mạnh của ecash là khả năng sử dụng nhiều Mint để tăng cường tính phân quyền và bảo mật. Để thêm Mint khác, hãy vào `Cài đặt`, sau đó chọn `Quản lý Mint`, và cuối cùng nhấn `Thêm Mint`.


[Bitcoinmints.com](Bitcoinmints.com) cung cấp danh sách đầy đủ các xưởng đúc tiền hiện có kèm theo đánh giá của người dùng để giúp bạn lựa chọn những lựa chọn uy tín. Sử dụng nhiều xưởng đúc tiền sẽ giúp giảm thiểu rủi ro. Nếu một xưởng đúc tiền gặp sự cố, tiền của bạn tại các xưởng đúc tiền khác vẫn có thể được truy cập.


![image](assets/en/04.webp)


## 3️⃣ Tạo bản sao lưu


Sao lưu được cho là bước quan trọng nhất trong toàn bộ quá trình thiết lập. Để truy cập các tùy chọn Sao lưu, hãy điều hướng đến `Cài đặt`-> `Sao lưu`. Tại đây, bạn sẽ tìm thấy hai tùy chọn thiết yếu:

1. `Cụm từ seed của bạn` bao gồm `12 từ` cho phép bạn khôi phục số dư ecash trong trường hợp mất thiết bị. Cụm từ seed này là chìa khóa chính cho tất cả ecash trên tất cả các máy đúc tiền bạn đã thêm. Hãy viết cụm từ này ra giấy hoặc kim loại và lưu trữ an toàn ở nhiều nơi. Tuyệt đối không lưu trữ cụm từ seed của bạn dưới dạng kỹ thuật số, nơi có thể bị xâm phạm. Hãy xem [hướng dẫn] này (https://planb.network/en/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270) để biết các biện pháp tốt nhất nhằm bảo vệ Wallet của bạn.

2. `Wallet backup` chứa một chuỗi sao lưu dài.


**Lưu ý**: Bạn vẫn cần cụm từ seed khi sử dụng bản sao lưu này để khôi phục Wallet.


![image](assets/en/05.webp)


## 4️⃣ Tạo Minibits Wallet Address


Tiếp theo, hãy điều hướng đến `Contacts` ở cuối trang và tùy chỉnh `Minibits Wallet Address` chuyên dụng của bạn bằng cách nhấn `Change` -> `Change Wallet Address`. Nhập Address bạn muốn và kiểm tra tình trạng còn hàng.


![image](assets/en/07.webp)


Sau khi thiết lập Address, bạn sẽ được nhắc đóng góp một khoản `Donation` nhỏ để hỗ trợ dự án. Mặc dù đây là tùy chọn, tôi thực sự khuyên bạn nên cân nhắc nếu dự định sử dụng dịch vụ thường xuyên. Các dự án nguồn mở như Minibits dựa vào sự hỗ trợ của cộng đồng để tiếp tục phát triển và bảo trì. Ngay cả một khoản đóng góp nhỏ cũng giúp đảm bảo tính bền vững của dự án.


![image](assets/en/08.webp)


## 5️⃣ Thiết lập Nostr


Nếu bạn muốn tặng tiền boa cho những người bạn theo dõi trên Nostr, bạn có thể `Thêm khóa npub` bằng cách chọn `Danh bạ` rồi chọn `Công khai`. Thao tác này sẽ kết nối Minibits Wallet của bạn với mạng xã hội Nostr, cho phép tặng tiền boa liền mạch.


Bạn cũng có thể chọn `Sử dụng hồ sơ của riêng bạn` bằng cách vào `Cài đặt`, sau đó chọn `Quyền riêng tư` để nhập Nostr Address và khóa của riêng bạn. Tuy nhiên, lưu ý rằng việc này sẽ ngăn Wallet của bạn giao tiếp với máy chủ minibits.cash Nostr và LNURL Address, điều này sẽ vô hiệu hóa các tính năng Lightning Address để nhận zap và thanh toán.


![image](assets/en/09.webp)


## 6️⃣ Nhận tiền


Để nhận tiền ban đầu, bạn cần nạp tiền vào Wallet thông qua ví Lightning Invoice. Quy trình này rất đơn giản: chạm vào `Nạp tiền`, nhập `Số tiền` bạn muốn thêm, tùy chọn thêm `Ghi chú`, rồi chạm vào `Tạo Invoice`. Sau đó, bạn cần thanh toán Invoice này bằng một ví Lightning Wallet khác, thao tác này sẽ chuyển đổi các khoản thanh toán Bitcoin Lightning thành token ecash trong ví Minibits Wallet của bạn.


![image](assets/en/10.webp)


## 7️⃣ Gửi tiền


Bây giờ bạn đã nạp tiền vào tài khoản Wallet, bạn có thể gửi tiền theo hai cách khác nhau.


### Gửi tiền điện tử


Tùy chọn đầu tiên là gửi tiền điện tử trực tiếp. Nhấn vào `Gửi`, sau đó chọn `Gửi tiền điện tử`, nhập `Số tiền` và nhấn `Tạo token`. Thao tác này sẽ tạo mã QR generate mà bạn có thể chia sẻ với người nhận hoặc yêu cầu họ quét trực tiếp bằng thiết bị của họ. Người nhận sẽ thấy mã thông báo xuất hiện trong Wallet của họ gần như ngay lập tức, không mất phí Blockchain hay thời gian xác nhận.


![image](assets/en/11.webp)


### Thanh toán bằng Lightning


Lựa chọn thứ hai là thanh toán qua Lightning. Nhấn vào `Gửi`, sau đó chọn `Thanh toán bằng Lightning`. Bạn có thể chọn từ danh bạ Nostr (nếu bạn đã kết nối npub), hoặc nhập/dán mã thanh toán Lightning Address, Invoice hoặc LNURL bằng tùy chọn `Dán` hoặc `Quét`. Sau khi `Xác nhận` người nhận, bạn sẽ được nhắc nhập `Số tiền cần thanh toán`, (tùy chọn) thêm ghi chú, rồi nhấn `Xác nhận`, sau đó nhấn `Thanh toán ngay` để hoàn tất giao dịch Lightning.


![image](assets/en/12.webp)


## 8️⃣ Tạo kết nối NWC


Một tính năng mạnh mẽ khác của Minibits là khả năng tạo kết nối `Nostr Wallet Connect (NWC)`, cho phép các ứng dụng khác yêu cầu thanh toán từ Wallet của bạn mà không cần tiết lộ khóa riêng của bạn.


Để thiết lập, hãy vào `Cài đặt`, sau đó chọn `Nostr Wallet Connect` và nhấn `Thêm kết nối`. Đặt tên cho kết nối của bạn sao cho dễ hiểu để nhận dạng cả ứng dụng và tài khoản người dùng được liên kết. Đặt giới hạn tối đa hàng ngày hợp lý để kiểm soát số tiền có thể chi tiêu qua kết nối này, sau đó nhấn `Lưu` để hoàn tất thiết lập.


Tính năng này đặc biệt hữu ích cho các dịch vụ như Nostr Clients, nơi bạn muốn bật tính năng boa tiền tự động mà không cần phải phê duyệt thủ công từng giao dịch.


![image](assets/en/12.webp)


## 🎯 Kết luận


Minibits cung cấp một điểm khởi đầu dễ dàng vào thế giới tiền điện tử, cung cấp các khoản thanh toán tập trung vào quyền riêng tư, bổ sung cho khoản nắm giữ Bitcoin của bạn. Hãy nhớ luôn duy trì các bản sao lưu phù hợp, cân nhắc sử dụng nhiều máy đào coin để dự phòng và chỉ lưu trữ số lượng phù hợp trong giải pháp lưu trữ này.


Để biết thêm tài nguyên, hãy xem kho lưu trữ Minibits GitHub, trang web chính thức và kênh Telegram của họ, nơi cộng đồng tích cực thảo luận về các phát triển và khắc phục sự cố


- [Github](https://github.com/minibits-cash/minibits_wallet)
- [Trang web](https://www.minibits.cash/)
- [Telegram](https://t.me/MinibitsWallet)


Hệ sinh thái ecash vẫn đang phát triển, nhưng các công cụ như Minibits đang giúp công nghệ bảo mật mạnh mẽ này ngày càng dễ tiếp cận hơn với người dùng hàng ngày.