---
name: BitBanana
description: Trình quản lý di động cho nút Lightning của bạn
---

![cover](assets/cover.webp)



Trong hướng dẫn này, bạn sẽ học cách cài đặt và cấu hình BitBanana trên Android để điều khiển nút Lightning từ điện thoại thông minh. Chúng ta sẽ tìm hiểu cách kết nối ứng dụng với cơ sở hạ tầng hiện có của bạn (Umbrel, RaspiBlitz, myNode hoặc bất kỳ nút Lightning LND/Core nào), thực hiện thanh toán Lightning, quản lý kênh từ xa, xem doanh thu định tuyến và sao lưu cấu hình. Bạn cũng sẽ tìm hiểu về các biện pháp bảo mật tốt nhất để bảo vệ quyền truy cập vào nút của mình và so sánh nó với Zeus, một giải pháp thay thế phổ biến.



## Giới thiệu BitBanana



BitBanana là một ứng dụng di động Android mã nguồn mở, biến điện thoại thông minh của bạn thành một bảng điều khiển hoàn chỉnh để điều khiển từ xa nút Lightning. Không giống như ví Lightning, vốn tích hợp một nút cục bộ trên điện thoại, BitBanana áp dụng triết lý điều khiển từ xa 100%: ứng dụng không chứa satoshi và chỉ kết nối với cơ sở hạ tầng hiện có của bạn.



Được phát triển bởi Michael Wünsch theo giấy phép MIT, ứng dụng đảm bảo tính minh bạch tuyệt đối với việc không thu thập dữ liệu cá nhân và các bản dựng có thể tái tạo được đã được xác minh. BitBanana hỗ trợ LND và Core Lightning thông qua các URI tiêu chuẩn (`lndconnect://` và `clngrpc://`), giúp đơn giản hóa đáng kể việc cấu hình ban đầu. Ứng dụng cũng nhận dạng LndHub và Nostr Wallet Connect cho người dùng không có node cá nhân, mặc dù các chế độ này hoạt động độc lập với chức năng hạn chế.



Giao diện cung cấp quyền truy cập đầy đủ vào tất cả các chức năng quan trọng của nút: gửi và nhận thanh toán (BOLT11, Lightning Address, LNURL, BOLT12, Keysend), quản lý kênh Lightning (mở, đóng, điều chỉnh phí, cân bằng lại), kiểm soát tiền điện tử nâng cao và quản lý tháp canh. BitBanana cũng triển khai nhiều lớp bảo mật mạnh mẽ: khóa sinh trắc học, chế độ ẩn danh, mã PIN khẩn cấp và hỗ trợ Tor gốc để ẩn danh kết nối.



## Nền tảng được hỗ trợ và cài đặt



### Cài đặt



BitBanana chỉ khả dụng cho Android 8.0 trở lên. Ứng dụng này không có trên iOS và chưa có phiên bản nào được lên kế hoạch. Hạn chế này được giải thích bởi lịch sử của dự án: BitBanana là phiên bản kế thừa trực tiếp của Zap Android, ban đầu được phát triển bởi Michael Wünsch, người đã quyết định tiếp tục công việc của mình dưới thương hiệu riêng. Zap là một nhóm các ứng dụng riêng biệt (Zap Android, Zap iOS, Zap Desktop) được phát triển bởi nhiều cộng tác viên khác nhau với các cơ sở mã riêng biệt. BitBanana chỉ tập trung vào nhánh Android.



Ngoài ra, hệ sinh thái iOS còn đặt ra những hạn chế đáng kể về mặt quy định và kỹ thuật đối với các ứng dụng Lightning không lưu ký. Năm 2023, Apple đã từ chối bản cập nhật Zeus vì "vi phạm giấy phép", và năm 2024, Phoenix Wallet đã rời khỏi App Store Hoa Kỳ do những bất ổn về quy định liên quan đến các nhà cung cấp dịch vụ Lightning. Những trở ngại này giải thích tại sao nhiều nhà phát triển Lightning ưa chuộng Android, nền tảng cung cấp chính sách cởi mở hơn cho các ứng dụng không lưu ký.



Có ba phương pháp cài đặt dành cho Android: Cửa hàng Google Play (hơn 5000 lượt cài đặt, cập nhật tự động), F-Droid (bản dựng có thể tái tạo, xác minh mã nguồn) hoặc APK thủ công từ GitHub.



![BitBanana](assets/fr/01.webp)



Trang web chính thức của bitbanana.app (bên trái) tự hào tuyên bố "100% tự quản lý và KHÔNG thu thập dữ liệu". Màn hình trung tâm hiển thị ba tùy chọn tải xuống: F-Droid (khuyến nghị), Google Play và APK. Màn hình bên phải hiển thị quyền thông báo cho các cảnh báo thanh toán.



Ứng dụng yêu cầu các quyền: mạng (kết nối nút), camera (mã QR), NFC (LNURL), dịch vụ nền (thông báo), sinh trắc học (bảo mật) và WireGuard VPN. Không theo dõi, không thu thập dữ liệu. Bật khóa mật khẩu hoặc sinh trắc học để bảo mật quyền truy cập.



## Cấu hình ban đầu



### Kết nối với nút LND



Để kết nối BitBanana với nút LND của bạn (Umbrel, RaspiBlitz, myNode), hãy lấy URI `lndconnect` hoặc mã QR chứa địa chỉ, chứng chỉ TLS và macaroon xác thực.



Trong hướng dẫn này, chúng tôi sử dụng nút LND thông qua ô. Để biết thêm chi tiết, vui lòng xem hướng dẫn chuyên sâu của chúng tôi:



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16


![BitBanana](assets/fr/03.webp)



Trên ứng dụng Lightning Node, hãy truy cập menu ở góc trên bên phải và chọn "Kết nối wallet".



![BitBanana](assets/fr/04.webp)



Chọn **gRPC (Tor)** để kết nối qua Tor (khuyến nghị). Mã QR và thông tin chi tiết (Host .onion, Port 10009, Macaroon) sẽ được hiển thị.



![BitBanana](assets/fr/02.webp)



Trong BitBanana, nhấn "CONNECT NODE", quét mã QR hoặc dán URI. Cho phép truy cập camera, sau đó kiểm tra địa chỉ .onion được hiển thị trước khi xác nhận.



Kết nối **Core Lightning**



Nếu bạn sử dụng Core Lightning (CLN) thay vì LND, quy trình vẫn giống hệt nhau, với URI `clngrpc://` chứa các chứng chỉ TLS chung. Core Lightning hỗ trợ BOLT12 (ưu đãi), cho phép sử dụng lại hóa đơn và thanh toán định kỳ, vốn không khả dụng trên LND.



**Kết nối không có nút cá nhân (LNbits/được lưu trữ)**



Nếu bạn không có nút Lightning, BitBanana có thể kết nối với các dịch vụ lưu trữ thông qua LndHub (giao thức được BlueWallet và LNbits sử dụng) hoặc Nostr Wallet Connect (NWC). Xin lưu ý: các chế độ này hoạt động ở chế độ lưu ký (dịch vụ lưu trữ tiền của bạn) với chức năng hạn chế. Bạn sẽ không thể quản lý kênh hoặc cấu hình phí định tuyến, và chỉ có thể gửi và nhận thanh toán Lightning.



Để biết thêm chi tiết về LNbits hoặc Nostr Wallet Connect, vui lòng tham khảo các hướng dẫn khác nhau của chúng tôi:



https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Sử dụng hàng ngày



### Interface chính



Màn hình chính hiển thị số dư Lightning của bạn, với menu ở góc trên bên trái cung cấp quyền truy cập vào các mục sau: Kênh, Định tuyến, Ký/Xác minh, Nút, Danh bạ, Cài đặt, Sao lưu. Biểu tượng đồng hồ (góc trên bên phải) mở lịch sử giao dịch. Các nút "Gửi" và "Nhận" ở phía dưới cho phép bạn gửi và nhận satoshi.



![BitBanana](assets/fr/05.webp)



### Thanh toán Lightning và on-chain



![BitBanana](assets/fr/10.webp)



**Gửi thanh toán:** Nhấn nút "Gửi" từ màn hình chính. Màn hình thanh toán (bên trái) cho phép bạn dán địa chỉ hoặc dữ liệu thanh toán vào trường "Address hoặc dữ liệu thanh toán", với máy quét QR ở góc trên bên phải để quét mã. Bạn cũng có thể chọn một liên hệ đã lưu trong phần Danh bạ để tránh phải quét mỗi lần.



BitBanana nhận dạng thông minh tất cả các định dạng thanh toán: hóa đơn Lightning cổ điển (chuỗi ký tự bắt đầu bằng `lnbc`), Lightning Address (định dạng email như `utilisateur@domaine.com`), mã LNURL-pay cho thanh toán động, LNURL-withdraw để rút tiền, và thậm chí cả thanh toán Keysend trực tiếp vào khóa công khai Lightning mà không cần hóa đơn trước đó. Ứng dụng tự động thực hiện các giải pháp LNURL cần thiết ở chế độ nền.



Sau khi hóa đơn được tải lên, BitBanana sẽ hiển thị đầy đủ thông tin chi tiết: số tiền chính xác, phí định tuyến ước tính, mô tả thanh toán (nếu người nhận cung cấp) và ngày hết hạn hóa đơn. Sau khi xác nhận, khoản thanh toán sẽ được chuyển qua kênh Lightning của bạn. Sau đó, bạn có thể xem lộ trình đã đi và các khoản phí thực tế đã thanh toán trong chi tiết giao dịch.



**Nhận thanh toán:** Nhấn nút "Nhận". Một nút chọn (màn hình bên phải) cho phép bạn chọn giữa Lightning (thanh toán tức thì qua kênh của bạn) và On-Chain. Đối với biên lai Lightning, hãy nhập số tiền mong muốn (tính bằng satoshi) (hoặc giữ nguyên số 0 để tạo hóa đơn không có số tiền cố định để người thanh toán điền), và thêm mô tả tùy chọn để hiển thị trên hóa đơn. BitBanana sẽ ngay lập tức tạo hóa đơn Lightning kèm mã QR để quét. Bạn cũng có thể sao chép hóa đơn dưới dạng văn bản và gửi qua email. Ngay khi nhận được thanh toán, một thông báo đẩy sẽ thông báo cho bạn và giao dịch sẽ xuất hiện ngay trong lịch sử với đầy đủ thông tin chi tiết.



### Kênh và định tuyến



![BitBanana](assets/fr/06.webp)



Mục "Kênh" hiển thị khả năng gửi/nhận của bạn và liệt kê các kênh với hình đại diện riêng. Mỗi kênh hiển thị mức phân bổ thanh khoản giữa số dư cục bộ và từ xa. Chạm vào một kênh để biết chi tiết và hành động đầy đủ (đóng, thay đổi phí định tuyến). Ba dấu chấm ở góc trên bên phải cho phép truy cập tùy chọn "Cân bằng lại" để cân bằng lại thanh khoản của kênh. Nút "+" sẽ mở một kênh mới.



Phần Định tuyến (màn hình trung tâm) hiển thị doanh thu chuyển tiếp theo kỳ (1 ngày, 1 tuần, 1 tháng, 3 tháng, 6 tháng, 1 năm) với lịch sử chuyển tiếp chi tiết để tối ưu hóa chiến lược của bạn.



Ký/Xác minh (màn hình bên phải) cho phép bạn ký/xác minh tin nhắn bằng mật mã để chứng minh quyền kiểm soát nút.



### Nhiều nút và tham số



![BitBanana](assets/fr/07.webp)



**Quản lý Node**: liệt kê các node của bạn, với các nút để thêm thủ công, quét QR hoặc chuyển đổi giữa các node. Đặc biệt, bạn có thể thiết lập các loại kết nối khác nhau đến cùng một node: LAN, VPN hoặc Tor.



**Quản lý danh bạ**: lưu trữ danh bạ Lightning của bạn để thanh toán nhanh chóng.



**Cài đặt**: tùy chỉnh tiền tệ, ngôn ngữ, ảnh đại diện. Phần Bảo mật & Quyền riêng tư: Khóa ứng dụng (mã PIN/sinh trắc học), Ẩn số dư (chế độ ẩn), Tor (ẩn danh IP). Cấu hình oracle giá, trình khám phá khối, trình ước tính phí tùy chỉnh.



## Ưu điểm và hạn chế



**Điểm nổi bật:**




- Khả năng di chuyển toàn diện: điều khiển nút Lightning của bạn từ bất cứ đâu
- Chức năng đầy đủ: thanh toán (LNURL, Lightning Address, BOLT 12), quản lý kênh, kiểm soát tiền xu, tháp canh, nhiều nút
- Bảo mật: Mã PIN/sinh trắc học, chế độ ẩn, Mã PIN khẩn cấp, Tor gốc, chặn ảnh chụp màn hình
- Miễn phí, mã nguồn mở (MIT), không hoa hồng, không thu thập dữ liệu



**Hạn chế:**




- Yêu cầu một nút Lightning đang hoạt động (hoặc LNbit ở chế độ giám sát)
- Không có phiên bản iOS nào được lên kế hoạch
- Việc bảo mật quyền truy cập vào điện thoại là rất quan trọng (macaroon admin = toàn quyền truy cập vào nút)



## Thực hành tốt nhất



**Sự an toàn:**




- Kích hoạt khóa mã PIN/sinh trắc học (ngăn chặn truy cập trái phép vào nút)
- Thiết lập mã PIN khẩn cấp (xóa dữ liệu nhạy cảm trong trường hợp bị ép buộc)
- Không bao giờ chia sẻ URI đăng nhập hoặc macaroon của bạn
- Chế độ tàng hình trong môi trường thù địch



**Đăng nhập:**




- Mạng VPN (Tailscale, ZeroTier): sự cân bằng tốt nhất giữa tốc độ và bảo mật
- Tor: bảo mật tối đa, độ trễ cao hơn
- Clearnet: tránh trừ khi cần thiết (phơi bày IP, mở cổng)



### Sao lưu và phục hồi



Cuối cùng, có menu "Sao lưu", cho phép bạn lưu cấu hình để di chuyển hoặc cài đặt lại điện thoại.



![BitBanana](assets/fr/08.webp)



**Quan trọng:** Bản sao lưu KHÔNG chứa seed hoặc bản sao lưu kênh (sẽ được thực hiện trên nút). Bản sao lưu bao gồm: cấu hình nút (địa chỉ, chứng chỉ, macaroon), nhãn, danh bạ, tham số. Nút Khôi phục cho phép bạn nhập bản sao lưu hiện có. Cần xác nhận trước khi lưu.



![BitBanana](assets/fr/09.webp)



Nhập mật khẩu mã hóa (màn hình bên phải). Hệ thống sẽ mở trình chọn tệp (màn hình bên trái) để lưu `BitBananaBackup_2025-XX-XX.dat`. Xác nhận "Đã tạo bản sao lưu".



**Bảo mật:** Lưu trữ bản sao lưu được mã hóa (đám mây cá nhân, USB, NAS). Không bao giờ chia sẻ tệp hoặc mật khẩu. Kiểm tra khôi phục thường xuyên. Bản sao lưu khôi phục kết nối, không phải dữ liệu.



## BitBanana và Zeus: Sự khác biệt là gì?



Nếu bạn đang tìm hiểu các ứng dụng di động để quản lý một nút Lightning, bạn có thể sẽ bắt gặp Zeus, một lựa chọn thay thế phổ biến cho BitBanana. Khác với BitBanana, vốn chỉ tập trung vào việc điều khiển từ xa một nút hiện có, Zeus có cách tiếp cận toàn diện hơn, cung cấp hai chế độ hoạt động: một nút Lightning được nhúng trực tiếp vào ứng dụng (chế độ nhúng với LND tích hợp) và kết nối từ xa với một nút bên ngoài, giống như BitBanana.



Chức năng kép này khiến Zeus đặc biệt hấp dẫn đối với người mới bắt đầu muốn thử nghiệm Lightning mà không cần bất kỳ cơ sở hạ tầng nào trước đó. Chế độ nhúng cho phép khởi động ngay lập tức với một nút di động hoàn chỉnh, trong khi người dùng nâng cao có thể chuyển sang kết nối từ xa sau khi nút cá nhân của họ được cấu hình. Zeus cũng hỗ trợ LND và Core Lightning cho kết nối từ xa, chẳng hạn như BitBanana.



Một lợi thế lớn khác của Zeus là khả năng tương thích đa nền tảng (iOS và Android), trong khi BitBanana vẫn chỉ hoạt động trên Android. Zeus cũng tích hợp cơ sở hạ tầng LSP của Olympus để tạo điều kiện thuận lợi cho việc nhận thanh toán Lightning qua các kênh tức thời, hệ thống Điểm bán hàng (Point of Sale) dành cho các nhà bán lẻ và chức năng hoán đổi tích hợp để quản lý thanh khoản.



Tuy nhiên, BitBanana vẫn giữ được những điểm mạnh đặc trưng: giao diện đơn giản, hợp lý hơn, trải nghiệm người dùng (UX) tốt hơn nhờ tập trung hoàn toàn vào điều khiển từ xa, và phương pháp tiếp cận giáo dục với các giải thích theo ngữ cảnh. Zeus cung cấp nhiều chức năng hơn, nhưng giao diện phức tạp hơn. Ứng dụng này vẫn đặc biệt phù hợp với người dùng muốn điều khiển một node hoàn toàn từ xa, không cần chức năng giám sát.



Để tìm hiểu thêm về Zeus, hãy xem các hướng dẫn sau:



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-advanced-3e89603c-501d-439c-8691-d4a0d0de459b

## Phần kết luận



BitBanana biến điện thoại thông minh Android của bạn thành một bảng điều khiển Lightning hoàn chỉnh, mang đến khả năng di động chưa từng có cho các nhà điều hành node. Ứng dụng bao gồm tất cả các chức năng: thanh toán (mọi định dạng), quản lý kênh, kiểm soát coin, tháp canh, đa node, với bảo mật nâng cao (mã PIN/sinh trắc học, Tor, mã PIN khẩn cấp).



BitBanana hoàn toàn độc lập, không thu thập dữ liệu và không xâm phạm tính bảo mật cũng như quyền kiểm soát tiền của bạn. Mã nguồn mở (MIT) đảm bảo tính minh bạch.



## Tài nguyên



### Tài liệu chính thức




- [Trang web BitBanana](https://bitbanana.app)
- [Tài liệu đầy đủ](https://docs.bitbanana.app)
- [Mã nguồn GitHub](https://github.com/michaelWuensch/BitBanana)



### Cài đặt




- [Cửa hàng Google Play](https://play.google.com/store/apps/details?id=app.michaelwuensch.bitbanana)
- [F-Cold](https://f-droid.org/packages/app.michaelwuensch.bitbanana)