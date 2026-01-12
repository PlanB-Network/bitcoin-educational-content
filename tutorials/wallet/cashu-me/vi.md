---
name: Cashu.me
description: Hướng dẫn sử dụng Cashu.me
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=LIPw1c74LBU)


*Đây là video hướng dẫn từ BTC Sessions, video hướng dẫn bạn cách thiết lập và sử dụng Cashu.me Bitcoin Wallet, giúp bạn truy cập vào các giao dịch Bitcoin đơn giản, rẻ và riêng tư - mà không cần đến cửa hàng ứng dụng!*


Trong hướng dẫn này, chúng ta sẽ khám phá Cashu.me, một Wallet dựa trên trình duyệt cho phép thanh toán Bitcoin riêng tư bằng Chaumian ecash. Trước khi đi sâu vào chi tiết, hãy cùng tìm hiểu sơ lược về ecash và cách thức hoạt động của nó.


## Giới thiệu về ecash


Hãy tưởng tượng bạn có tiền mặt kỹ thuật số hoạt động chính xác như tiền giấy trong túi - riêng tư, tức thì và có thể sử dụng ngang hàng mà không cần trung gian. Đó chính là những gì ecash mang lại: một phương thức thanh toán kỹ thuật số mang lại sự riêng tư của tiền mặt vật lý cho thế giới số. Không giống như onchain-Bitcoin, vốn ghi lại mọi giao dịch trên Ledger công khai mà bất kỳ ai cũng có thể nhìn thấy, ecash tạo ra các token riêng tư đại diện cho giá trị Bitcoin thực tế, đồng thời bảo mật thói quen chi tiêu của bạn.


Hãy nghĩ về ecash như những công cụ mang tính kỹ thuật số được lưu trữ trên thiết bị của bạn - nếu bạn giữ chúng, bạn sở hữu chúng, giống như tiền mặt vật lý. Các token này được phát hành bởi các dịch vụ đáng tin cậy gọi là `Mints`, nắm giữ dự trữ Bitcoin cơ bản. Khi sử dụng ecash, bạn không phát tán giao dịch của mình ra toàn bộ mạng lưới. Thay vào đó, bạn trao đổi token riêng tư trực tiếp với người khác, tạo ra trải nghiệm thanh toán giống như trao tiền mặt cho ai đó hơn là thực hiện thanh toán kỹ thuật số truyền thống.


Cashu là một giao thức ecash Chaumian mã nguồn mở, miễn phí được xây dựng cho Bitcoin. Công nghệ này được xây dựng dựa trên nghiên cứu mật mã tiên phong của David Chaum vào những năm 1980, sử dụng `chữ ký ẩn` để đảm bảo quyền riêng tư. Khi bạn nhận được token ecash, xưởng đúc tiền sẽ ký chúng mà không biết chúng sẽ được chi tiêu vào đâu tiếp theo - một tính năng quan trọng giúp ngăn chặn việc theo dõi giao dịch. Quan trọng là, ecash không thay thế Bitcoin; nó bổ sung cho Bitcoin bằng cách giải quyết một số vấn đề quan trọng đi kèm với các yêu cầu về kiến trúc của Bitcoin. Nó cung cấp quyền riêng tư mà tiền mặt vật lý mang lại (điều mà Ledger minh bạch của Bitcoin không có) và cho phép các giao dịch vi mô tức thì mà không có phí Blockchain hoặc chậm trễ xác nhận.


Ecash tích hợp liền mạch với Lightning Network. Bạn sử dụng Lightning để gửi Bitcoin vào máy đúc tiền (chuyển đổi giá trị Bitcoin của bạn thành token ecash) và rút tiền sau đó (chuyển đổi token trở lại số dư Lightning có thể chi tiêu). Cùng nhau, chúng tạo nên một sự kết hợp mạnh mẽ: Bitcoin cung cấp giải pháp thanh toán an toàn Layer, Lightning cho phép giao dịch nhanh chóng và khả năng tương tác mạng, và ecash bổ sung tính năng bảo mật Layer, giúp thanh toán kỹ thuật số trở nên thực sự riêng tư.


## Cashu.me


Cashu.me là một `Ứng dụng Web Tiến bộ (PWA)` triển khai giao thức Cashu - một triển khai cụ thể của Chaumian ecash được thiết kế cho Bitcoin. Là một PWA, nó hoạt động trực tiếp trên trình duyệt của bạn mà không cần cài đặt từ các cửa hàng ứng dụng, mặc dù bạn có thể `cài đặt` nó vào thiết bị của mình để truy cập dễ dàng hơn. Phương pháp tiếp cận dựa trên web này đảm bảo khả năng tương thích rộng rãi trên các hệ điều hành, đồng thời duy trì bảo mật thông qua các giao thức mã hóa thay vì các hạn chế của nền tảng.


## 🎉 Các tính năng chính


Hãy cùng tìm hiểu sâu hơn về các tính năng và khám phá những gì Cashu.me mang lại:



- Chaumian ecash trên Lightning**: Sử dụng chữ ký ẩn danh để các đơn vị đúc tiền không thể theo dõi số dư của người dùng hoặc lịch sử giao dịch
- Tự quản lý mã thông báo**: Bạn kiểm soát mã thông báo ecash cục bộ bằng cụm từ seed của mình
- Sao lưu cụm từ seed**: Cụm từ phục hồi 12 từ để phục hồi Wallet
- Độc lập với xưởng đúc tiền**: Hoạt động với nhiều xưởng đúc tiền độc lập—bạn không bị giới hạn bởi một nhà cung cấp
- Giao dịch tức thì, miễn phí**: Trong cùng một máy đúc, thanh toán được hoàn tất trong vài giây mà không mất phí
- Kiến trúc bảo vệ quyền riêng tư**: Mint không thể biết ai giao dịch với ai
- Ecash ngoại tuyến**: Gửi/nhận mã thông báo thông qua giao thức truyền cục bộ, như NFC, mã QR, Bluetooth, v.v. mà không cần kết nối internet
- Khám phá các xưởng đúc tiền điện tử ecash thông qua Nostr**: Tìm và xác minh các xưởng đúc tiền đáng tin cậy thông qua giao thức Nostr
- Đổi tiền điện tử giữa các xưởng đúc tiền**: Tất cả các xưởng đúc tiền đều sử dụng Lightning, nghĩa là bạn có thể chuyển giá trị giữa các xưởng đúc tiền.
- Điều khiển Wallet từ xa bằng Nostr Wallet Connect (NWC)**: Kết nối với các ứng dụng khác như Nostr Client và bắt đầu điều khiển qua NWC


Sự đánh đổi quan trọng nhất là `niềm tin`: trong khi bạn kiểm soát chính các token, bạn phải tin tưởng các xưởng đúc tiền sẽ lưu giữ lượng dự trữ Bitcoin cơ bản. Như tài liệu của Cashu đã nêu:


> ...sở đúc tiền đang vận hành cơ sở hạ tầng Lightning và quản lý satoshi cho người dùng ecash của sở đúc tiền. Người dùng phải tin tưởng sở đúc tiền để Redeem ecash của họ khi họ muốn chuyển sang Lightning.

— Tài liệu Cashu, [Câu hỏi chung về an toàn và quyền riêng tư](https://docs.cashu.space/faq#general-safety-and-privacy-questions)


Điều này khiến ecash trở thành giải pháp lưu ký cho chính Bitcoin, mặc dù bạn vẫn giữ toàn quyền kiểm soát các mã thông báo.


## 1️⃣ Thiết lập ban đầu


① Bắt đầu bằng cách truy cập [Wallet.cashu.me](https://Wallet.cashu.me) trên trình duyệt của bạn. Vì Cashu.me là một `PWA`, bạn không cần tải xuống từ cửa hàng ứng dụng, chỉ cần mở trang web trực tiếp trong trình duyệt. Để truy cập dễ dàng hơn, bạn có thể tùy chọn cài đặt nó vào màn hình chính của thiết bị.


② Để cài đặt PWA, hãy nhấn vào nút menu ⋮ trên trình duyệt và chọn `Thêm vào Màn hình Chính`. Sau khi cài đặt, hãy đóng tab trình duyệt và khởi chạy Cashu.me từ màn hình chính của thiết bị. Trên màn hình chào mừng, nhấn `Tiếp theo` để tiếp tục.


③ Bảo mật là yếu tố quan trọng hàng đầu. Hãy lưu trữ cụm từ seed của bạn một cách an toàn trong trình quản lý mật khẩu, hoặc tốt hơn nữa, hãy viết nó ra giấy. Cụm từ khôi phục 12 từ này là cách duy nhất để bạn lấy lại tiền nếu mất quyền truy cập vào thiết bị. Nhấn vào biểu tượng 👁️ để hiển thị cụm từ seed của bạn, cẩn thận viết lại tất cả 12 từ theo thứ tự, sau đó đánh dấu vào ô `Tôi đã viết nó ra`. Nhấn `Tiếp theo` để tiếp tục, và đánh dấu vào ô để xác nhận bạn chấp nhận các `điều khoản` trên màn hình tiếp theo.


![image](assets/en/01.webp)


Sau khi hoàn tất thiết lập, bạn cần kết nối với một `Mint`. Nhấn vào `THÊM MINT`, sau đó là `KHÁM PHÁ MINT` để xem các loại bạc hà được cộng đồng Nostr đề xuất. Để xác minh thêm, bạn có thể xem xếp hạng bạc hà tại [bitcoinmints.com](bitcoinmints.com).


Tiếp theo, chạm vào `Nhấp để duyệt các loại bạc hà` để xem danh sách đầy đủ. Chọn một loại bạc hà bằng cách sao chép URL của nó, dán vào trường URL và đặt cho nó một cái tên dễ nhận biết. Trong ví dụ này, chúng tôi sẽ sử dụng:


URL: `https://mint.minibits.cash/Bitcoin`

Tên: `Minibits`


![image](assets/en/02.webp)


Nhấn `THÊM MINT` để hoàn tất quy trình. Trên màn hình xác nhận, hãy xác minh rằng bạn tin tưởng người vận hành máy đúc tiền này, sau đó nhấn `THÊM MINT` một lần nữa. Máy đúc tiền Minibits sẽ xuất hiện trên Màn hình chính của bạn. Sau khi thiết lập Wallet, bạn cần nạp tiền vào máy trước khi thực hiện giao dịch.


![image](assets/en/03.webp)


## 2️⃣ Tài trợ cho Wallet của bạn


Cashu.me cung cấp hai phương thức riêng biệt để nạp tiền vào ví Wallet của bạn. Khi bạn nhấn vào `Nhận` trên Màn hình chính, bạn sẽ thấy các tùy chọn nhận tiền qua `ECASH` hoặc qua `LIGHTNING`. Hãy cùng khám phá cả hai tùy chọn.


![image](assets/en/04.webp)


### Tài trợ thông qua LIGHTNING


Lựa chọn đầu tiên là nạp tiền vào Wallet thông qua Lightning Invoice. `Chọn một xưởng đúc` nếu bạn đã thêm nhiều xưởng đúc khác nhau và xác định `số tiền (Sats)` bạn muốn nhận. Sau đó, nhấn `TẠO Invoice`. Lúc này, mã QR sẽ hiển thị, bạn có thể quét bằng một Lightning Wallet khác hoặc chỉ cần `Sao chép` Invoice và dán vào một Wallet khác để thanh toán và nạp tiền vào cashu.me Wallet của bạn.


![image](assets/en/05.webp)


### Nhận tiền điện tử


Phương pháp ecash cho phép bạn nhận token trực tiếp từ một ecash Wallet khác. Bắt đầu bằng cách chạm vào nút `Receive` và chọn tùy chọn `ECASH`. Bạn sẽ có thể `Paste` hoặc `Scan` hoặc sử dụng `NFC` để gửi Cashu token từ một Wallet khác. Nếu bạn chọn dán, hãy nhập chuỗi token mà bạn đã sao chép từ một Wallet khác, `Amount` và `Mint` sẽ tự động được hiển thị. Chạm vào `RECEIVE` để hoàn tất giao dịch và Sats sẽ xuất hiện trong Wallet của bạn. Lưu ý rằng số dư của bạn hiện được phân bổ trên nhiều xưởng đúc tiền. Ví dụ: bạn có thể có 1.000 Sats trong `Mint` Minibits của mình và thêm 1.000 Sats trong `Mint` Coinos. Sự tách biệt này giữa các xưởng đúc tiền khác nhau là một khía cạnh quan trọng trong kiến trúc của Cashu.


![image](assets/en/06.webp)


### Hoán đổi giữa các loại kẹo bạc hà


Nếu bạn không còn tin tưởng một xưởng đúc tiền cụ thể mà bạn đã thêm, cashu.me cung cấp tính năng `Swap` tiền từ xưởng đúc tiền này sang xưởng đúc tiền khác. Điều hướng đến tab xưởng đúc tiền và cuộn xuống cho đến khi bạn thấy `Multimint Swaps`. Chọn xưởng đúc tiền `FROM` và `TO` từ menu thả xuống và nhập số tiền bạn muốn chuyển. Nhấn `SWAP` để chuyển token giữa các xưởng đúc tiền. Thao tác này sẽ được thực hiện thông qua giao dịch Lightning, vì vậy bạn cần chừa chỗ cho các khoản phí Lightning tiềm ẩn. Trong ví dụ của tôi, 1 sat là đủ.


![image](assets/en/07.webp)


## 3️⃣ Gửi tiền


Để gửi Sats, Cashu.me cung cấp hai lựa chọn: gửi qua `ecash` hoặc qua `lightning`. Hãy cùng xem xét cả hai lựa chọn.


### Gửi qua Lightning


Để gửi qua Lightning, hãy làm theo các bước sau:


1. Chạm vào `GỬI` trên Màn hình chính và chọn `Lightning`

2. Ứng dụng sẽ nhắc bạn nhập `Lightning Invoice` hoặc `-Address`. Bạn có thể dán trực tiếp Invoice/Address hoặc sử dụng tùy chọn quét mã QR để chụp ảnh, sau đó xác nhận bằng `ENTER`.

3. Chọn Xưởng đúc tiền mà bạn muốn thanh toán bằng cách sử dụng trường thả xuống và nhấn `THANH TOÁN` để xác nhận. **Lưu ý**: cũng có tùy chọn sử dụng `Multinut` trong `Cài đặt` -> `Thử nghiệm` cho phép bạn thanh toán hóa đơn từ nhiều xưởng đúc tiền cùng một lúc.

4. Sau khi hoàn tất thành công, bạn sẽ thấy xác nhận thanh toán và số tiền được khấu trừ khỏi số dư của bạn.


![image](assets/en/08.webp)


### Gửi qua ecash


Gửi tiền điện tử cũng đơn giản tương tự.


1. Chạm vào `GỬI` và lần này chọn tùy chọn `ECASH`.

2. `Chọn một xưởng đúc tiền` và nhập `Số tiền` bạn muốn gửi vào Sats và nhấn `GỬI` để xác nhận

3. Thao tác này sẽ tạo ra một `Mã QR động` mà bạn có thể tùy chỉnh bằng cách điều chỉnh các thông số Tốc độ và Kích thước. Bất kỳ ai cũng có thể quét Mã QR này ngay lập tức đến Redeem hoặc Sats, hoặc bạn có thể nhấn SAO CHÉP để gửi chuỗi token cho người khác thông qua các kênh thay thế như Bluetooth, NFC hoặc tin nhắn tiêu chuẩn.

4. Tôi đang mở một Wallet khác. Dán từ bảng tạm và chọn `Nhận tiền điện tử` trong Wallet kia.


![image](assets/en/09.webp)


## 4️⃣ Các tính năng bổ sung


Ngoài chức năng gửi và nhận cốt lõi, Cashu.me còn cung cấp các tính năng bổ sung mạnh mẽ giúp nâng cao trải nghiệm Bitcoin của bạn trong hệ sinh thái Nostr.


### Kết nối Wallet của chúng tôi


Nostr Wallet Connect (`NWC`) thay đổi cách bạn tương tác với các ứng dụng Nostr bằng cách tạo ra một kết nối liền mạch giữa Wallet và các ứng dụng mạng xã hội. Giao thức này cho phép các ứng dụng như [Damus](https://damus.io/) hoặc [Primal](https://primal.net/home) yêu cầu thanh toán trực tiếp thông qua các rơle Nostr mà không yêu cầu bạn phải thoát khỏi ứng dụng.


Để thiết lập `NWC` trong Cashu.me:


1. Vào `Cài đặt` ở menu Hamburger góc trên bên trái

2. Cuộn đến phần `NOSTR Wallet CONNECT` và chạm vào nút `Enable`

3. Sau đó, bạn sẽ thiết lập một khoản trợ cấp để xác định số tiền tối đa mà các ứng dụng có thể chi tiêu từ Wallet của bạn.

4. Sau khi cấu hình xong, bạn có thể sao chép chuỗi kết nối và dán vào bất kỳ ứng dụng khách Nostr nào hỗ trợ `NWC`, cho phép chức năng chuyển hướng và chuyển tiếp tức thì.


![image](assets/en/10.webp)


### Lightning Address qua npub.cash


Cashu.me tích hợp với [npub.cash](https://npub.cash/) để cung cấp cho bạn Lightning Address hoạt động liền mạch với giao thức Nostr. Tại đây, bạn có thể đăng ký và xác nhận tên người dùng bằng cách cung cấp Nostr `nsec`, có giá 5.000 Sats và hỗ trợ dự án npub.cash, hoặc bạn có thể sử dụng bất kỳ khóa công khai Nostr nào (`npub`) mà không cần đăng ký.


Trước tiên, hãy vào `Cài đặt` và nhấn `Bật` Lightning Address với npub.cash. Thao tác này sẽ generate một npub.cash Address bằng chuỗi `npub` được lấy từ cụm từ Wallet seed của bạn theo mặc định.


Ngoài ra, hãy truy cập [trang web này](https://npub.cash/username) để yêu cầu tên người dùng tùy chỉnh bằng Nostr `nsec` của riêng bạn, giúp bạn có được Lightning Address được cá nhân hóa như username@npub.cash.


![image](assets/en/11.webp)


## 🎯 Kết luận


Cashu.me cung cấp các khoản thanh toán Bitcoin riêng tư, hoạt động như tiền mặt — tức thì và ngang hàng mà không tiết lộ lịch sử giao dịch của bạn. Cá nhân tôi đánh giá cao kiến trúc PWA của nó vì nó hoạt động không bị hạn chế bởi các hạn chế của cửa hàng ứng dụng. Bằng cách kết hợp tính bảo mật của Bitcoin, tốc độ của Lightning và quyền riêng tư của ecash, Wallet mang đến những ứng dụng có thể nâng cao việc áp dụng Bitcoin hàng ngày.


Mặc dù bạn có toàn quyền kiểm soát token ecash của mình thông qua việc tự lưu ký, hãy nhớ rằng các xưởng đúc tiền hoạt động như bên thứ ba đáng tin cậy nắm giữ dự trữ Bitcoin cơ bản. Khả năng sử dụng nhiều xưởng đúc tiền và hoán đổi giữa chúng mang lại sự linh hoạt mà vẫn đảm bảo quyền riêng tư.


Nhờ các tính năng như địa chỉ NWC và npub.cash, Cashu.me là lựa chọn hấp dẫn cho Wallet đối với những khách hàng mạng xã hội coi trọng quyền riêng tư và chủ quyền hơn các hạn chế về chính sách công nghệ lớn.


## 📚 Tài nguyên


[https://github.com/cashubtc/cashu.me](https://github.com/cashubtc/cashu.me)


[https://github.com/cashubtc](https://github.com/cashubtc)


[https://github.com/cashubtc/awesome-cashu](https://github.com/cashubtc/awesome-cashu)


[https://cashu.space/](https://cashu.space/)