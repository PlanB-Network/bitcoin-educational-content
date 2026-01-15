---
name: Macadamia Wallet
description: Cashu mobile wallet cho thanh toán BTC ẩn danh và tức thì
---

![cover](assets/cover.webp)



Macadamia Wallet là một ví điện tử wallet dành cho thiết bị di động iOS, triển khai giao thức Cashu, một hệ thống tiền điện tử Chaumian cho phép thanh toán Bitcoin hoàn toàn ẩn danh. Nhờ chữ ký ẩn danh, không ai có thể liên kết khoản tiền gửi của bạn với chi tiêu, mang lại tính bảo mật tương tự như tiền mặt.



Trong hướng dẫn này, chúng ta sẽ xem cách cài đặt và cấu hình Macadamia, thực hiện các giao dịch Cashu đầu tiên của bạn (Đúc, Gửi, Nhận, Nấu chảy) và quản lý nhiều lần đúc để bảo vệ tiền của bạn.



## Macadamia Wallet là gì?



### Giao thức Cashu



Cashu sử dụng chữ ký ẩn do David Chaum phát minh: bạn gửi bitcoin vào máy chủ "mint", nơi phát hành các token tương đương bằng satoshi. Mint ký các token này mà không cần nhìn thấy nội dung của chúng, khiến việc liên kết token với người dùng trở nên bất khả thi. Các sàn giao dịch là off-chain, ngang hàng và hoàn toàn không minh bạch - ngay cả Mint cũng không thể theo dõi ai đang trả tiền cho ai.



Macadamia là một nền tảng iOS mã nguồn mở wallet được phát triển bằng Swift/SwiftUI. Nó hoạt động mà không cần tài khoản hoặc KYC, token của bạn được lưu trữ cục bộ và được bảo vệ bởi cụm từ seed. Mã nguồn có thể được kiểm tra trên GitHub và token có thể tương tác với các ví Cashu khác (Minibits, Cashu.me).



### Mô hình giám sát và thỏa hiệp



**Quan trọng**: Cashu hoạt động theo mô hình lưu ký. Token là lời hứa trả nợ (IOU) được bảo đảm bằng dự trữ Bitcoin của xưởng đúc tiền. Nếu xưởng đúc tiền biến mất, token của bạn sẽ mất giá trị. Đây là sự thỏa hiệp để đảm bảo tính bảo mật tối đa.



Sử dụng Macadamia như một wallet vật lý: chỉ với số lượng nhỏ. Chia nhỏ vốn thành nhiều đợt để giảm thiểu rủi ro.



## Các tính năng chính



Macadamia triển khai bốn hoạt động cơ bản của giao thức Cashu. **Mint** chuyển đổi satoshi của bạn thành token thông qua hóa đơn Lightning. **Send** cho phép bạn gửi token miễn phí qua mã QR hoặc liên kết, hoàn toàn off-chain. **Receive** cho phép bạn nhận token hoặc generate hóa đơn Lightning. **Melt** thanh toán hóa đơn Lightning bằng cách hủy token của bạn.



wallet hỗ trợ quản lý nhiều xưởng đúc tiền cùng lúc. Bạn có thể trao đổi token giữa các xưởng đúc tiền khác nhau thông qua Lightning.



## Nền tảng được hỗ trợ



Macadamia chỉ khả dụng trên iOS 17 trở lên cho iPhone và iPad. Ứng dụng Swift/SwiftUI gốc mang đến khả năng tích hợp tối ưu với hệ sinh thái Apple.



Giao thức Cashu đảm bảo khả năng tương tác giữa các ví. Bạn có thể khôi phục cụm từ seed của mình trong các ứng dụng khác như Minibits trên Android hoặc Nutstash trên máy tính để bàn.



Phiên bản hiện tại được phân phối qua TestFlight. Chỉ sử dụng một lượng nhỏ với phiên bản beta này.



## Cài đặt



Macadamia hiện có sẵn thông qua TestFlight, chương trình thử nghiệm beta của Apple. Sau đây là cách cài đặt:



### Cài đặt qua TestFlight



**Bước 1: Tải xuống TestFlight**



Nếu bạn chưa cài đặt ứng dụng TestFlight trên thiết bị, hãy tìm kiếm "TestFlight" trên App Store và cài đặt. TestFlight là ứng dụng chính thức của Apple để thử nghiệm phiên bản beta của các ứng dụng iOS.



**Bước 2: Tham gia chương trình beta Macadamia** (bằng tiếng Pháp)



Sau khi cài đặt TestFlight, hãy nhấp vào liên kết lời mời này từ iPhone hoặc iPad của bạn: [https://testflight.apple.com/join/RMU6PaRu](https://testflight.apple.com/join/RMU6PaRu)



Liên kết sẽ tự động mở TestFlight và đề nghị bạn cài đặt Macadamia Wallet. Nhấn "Chấp nhận" rồi "Cài đặt" để bắt đầu tải xuống. Ứng dụng nặng khoảng mười megabyte và chỉ mất vài giây để cài đặt.



![Installation TestFlight](assets/fr/01.webp)



### Thông tin quan trọng về phiên bản beta



Macadamia vẫn đang trong giai đoạn phát triển tích cực. Các phiên bản TestFlight được cập nhật thường xuyên và có thể giới thiệu các tính năng mới hoặc sửa lỗi. Tuy nhiên, như với bất kỳ phiên bản beta nào, lỗi vẫn có thể xảy ra. **Chúng tôi khuyến nghị bạn chỉ nên sử dụng một lượng nhỏ**, vì bạn có thể chấp nhận rằng lượng nhỏ này có thể bị mất trong trường hợp xảy ra sự cố kỹ thuật.



Macadamia không thu thập bất kỳ dữ liệu người dùng nào theo chính sách bảo mật được hiển thị. Vui lòng kiểm tra xem nhà phát triển có phải là Cypherbase UG hay không khi cài đặt.



## Cấu hình ban đầu



Khi khởi chạy lần đầu, Macadamia sẽ tạo ra một câu BIP-39 gồm 12 từ. Hãy viết chúng ra ở nơi an toàn - tuyệt đối không chụp màn hình. Những từ này cho phép bạn tạo lại wallet và sử dụng token của mình.



![Configuration initiale](assets/fr/02.webp)



Thực hiện theo bốn bước: chào mừng, chấp nhận điều khoản, lưu câu seed và xác nhận cuối cùng.



![Interface principale](assets/fr/03.webp)



Sau khi hoàn tất cấu hình, Macadamia sẽ hiển thị ba tab chính. **Wallet** hiển thị số dư và lịch sử giao dịch của bạn. **Mints** cho phép bạn quản lý máy chủ Cashu. **Settings** cho phép truy cập vào cài đặt và cụm từ seed của bạn.



![Ajout d'un mint](assets/fr/04.webp)



Bây giờ bạn cần cấu hình một xưởng đúc tiền, tức là một máy chủ Cashu sẽ phát hành token của bạn. Vào tab "Xưởng đúc tiền", nhấn "Thêm URL Xưởng đúc tiền mới" và nhập địa chỉ xưởng đúc tiền bạn đã chọn (ví dụ: mint.cubabitcoin.org). Truy cập bitcoinmints.com hoặc cashu.space để tìm các xưởng đúc tiền công khai uy tín. Chỉ xác thực các xưởng đúc tiền mà bạn đã kiểm tra uy tín, vì họ sẽ nắm giữ satoshi của bạn.



## Sử dụng hàng ngày



### Tạo mã thông báo mới (Mint)



Để nạp tiền điện tử vào máy Macadamia wallet, bạn cần thực hiện thao tác "Đúc" (để tạo token). Chạm vào "Nhận", sau đó chọn tùy chọn "Lightning". Nhập số tiền mong muốn (ví dụ: 1000 sats), chọn loại tiền cần đúc, sau đó generate nhập hóa đơn Lightning.



![Opération Mint](assets/fr/05.webp)



Thanh toán hóa đơn Lightning được tạo bằng wallet (Phoenix, Zeus, BlueWallet) thông thường của bạn.



![Confirmation Mint](assets/fr/06.webp)



Mã thông báo Cashu sẽ xuất hiện ngay trong số dư của bạn sau khi thanh toán.



### Gửi mã thông báo



Để gửi token Cashu cho người dùng khác, hãy chạm vào nút "Gửi" trên màn hình chính, sau đó chọn "Ecash". Nhập số tiền cần gửi (ví dụ: 50 sats) và thêm ghi chú mô tả nếu cần.



![Envoi Ecash](assets/fr/07.webp)



Chia sẻ mã QR hoặc văn bản được tạo qua iMessage, Signal hoặc Telegram. Người nhận sẽ nhận tiền ngay lập tức và miễn phí.



### Nhận mã thông báo



Để nhận token Cashu do người dùng khác gửi, hãy chạm vào "Nhận" rồi chọn "Ecash". Quét mã QR token hoặc dán liên kết token bạn đã nhận được.



![Réception Ecash](assets/fr/08.webp)



Chạm vào "Redeem" để nhận token.



### Thanh toán Lightning (Melt)



Để thanh toán hóa đơn Lightning bằng token Cashu, hãy chạm vào "Gửi" rồi chọn "Lightning". Dán hóa đơn BOLT11 bạn muốn thanh toán.



![Paiement Lightning](assets/fr/11.webp)



Xưởng đúc sẽ hủy token của bạn và thực hiện thanh toán Lightning. Vì vậy, bạn có thể thanh toán cho bất kỳ dịch vụ Lightning nào mà vẫn giữ được tính ẩn danh.



### Hoán đổi giữa các loại bạc hà



Khi bạn nhận được mã thông báo từ một xưởng đúc tiền mà bạn chưa cấu hình, Macadamia cung cấp cho bạn một số tùy chọn để quản lý các mã thông báo này.



![Swap inter-mints](assets/fr/09.webp)



Thêm xưởng đúc tiền mới hoặc hoán đổi token sang một xưởng đúc tiền hiện có. Việc hoán đổi này sử dụng Lightning làm cầu nối để chuyển tiền của bạn một cách ẩn danh.



### Quản lý đa tiền xu nâng cao



Macadamia cung cấp các công cụ tinh vi để quản lý nhiều cơ sở đúc tiền cùng lúc và phân bổ nguồn vốn một cách chiến lược.



![Gestion multi-mints](assets/fr/10.webp)



"Phân phối Quỹ" tự động phân phối số dư của bạn theo tỷ lệ phần trăm (ví dụ: 50/50). "Chuyển khoản" cho phép chuyển khoản thủ công giữa các đơn vị đúc tiền để phân tán rủi ro của bạn.



## Ưu điểm và hạn chế



**Điểm nổi bật**:





- Bảo mật tối đa**: Giao dịch không thể theo dõi, ngay cả bởi xưởng đúc tiền. Không có siêu dữ liệu blockchain, giao dịch ngang hàng không theo dõi.
- Nhanh chóng và miễn phí**: Chuyển khoản tức thời miễn phí trong thời gian ngắn, lý tưởng cho các khoản thanh toán nhỏ.
- Khả năng tương tác**: mã thông báo Cashu được chuẩn hóa để sử dụng với các ví tương thích khác (Minibits, Nutstash).
- Tính đơn giản**: Interface iOS gốc có thể được sử dụng bởi người mới bắt đầu nhưng vẫn có thể kiểm tra được (mã nguồn mở).



**Hạn chế** :





- Mô hình lưu ký**: cần có ủy thác đúc tiền. Nếu một xưởng đúc tiền biến mất, token của bạn sẽ mất giá trị.
- Chỉ dành cho iOS**: Không có phiên bản Android/máy tính. Khả năng tương tác của Cashu cho phép truy cập qua các ví khác, nhưng trải nghiệm tối ưu vẫn là iOS.
- Phụ thuộc vào Mint**: Mint ngoại tuyến = không thể thực hiện các giao dịch yêu cầu sự can thiệp của nó (Mint, Melt).
- Công nghệ mới nổi**: Phát triển tích cực, có thể có lỗi, tiêu chuẩn đang thay đổi.



## Thực hành tốt nhất





- Đa dạng hóa các loại bạc hà của bạn**: Phân bổ số tiền của bạn vào nhiều loại bạc hà có uy tín để giảm thiểu rủi ro.
- Giới hạn số tiền**: Sử dụng Macadamia như một wallet vật lý để thanh toán hàng ngày, không phải là két sắt.
- Bảo mật seed** của bạn: Giữ cụm từ 12 từ của bạn trên giấy ở nơi an toàn. Thỉnh thoảng hãy kiểm tra việc khôi phục.
- Kiểm tra máy đúc tiền**: Tham khảo cashu.space và các diễn đàn cộng đồng trước khi thêm máy đúc tiền. Chọn những máy đúc tiền có thời gian hoạt động tốt và uy tín vững chắc.
- VPN hoặc Tor**: Ẩn IP của bạn bằng VPN/Tor để tối đa hóa quyền riêng tư trên mạng.
- Tham gia cộng đồng**: Nhóm Telegram/Discord Cashu để cập nhật, đưa ra khuyến nghị về tiền xu và các phương pháp hay nhất.



## Phần kết luận



Macadamia Wallet mang các đặc tính của tiền mặt vật lý vào Bitcoin kỹ thuật số. Bằng cách kết hợp chữ ký mù Chaum và Lightning, nó mang đến một giải pháp tinh tế cho tính bảo mật giao dịch. Giao diện iOS gốc của nó cho phép công nghệ mã hóa tinh vi dễ tiếp cận trong khi vẫn duy trì mã nguồn mở và tương thích với hệ sinh thái Cashu.



Mô hình lưu ký đòi hỏi sự cảnh giác và các biện pháp bảo mật tốt. Nếu được sử dụng đúng cách, Macadamia sẽ trở thành một công cụ vô giá cho các khoản thanh toán hàng ngày đòi hỏi tính ẩn danh, bổ sung cho các ví tiền điện tử phi lưu ký để tiết kiệm.



## Tài nguyên



### Tài liệu chính thức




- Trang web chính thức: [macadamia.cash](https://macadamia.cash)
- Câu hỏi thường gặp về Macadamia: [macadamia.cash/faq](https://macadamia.cash/faq)
- Mã nguồn GitHub: [github.com/zeugmaster/macadamia](https://github.com/zeugmaster/macadamia)



### Tài liệu Cashu




- Tài liệu kỹ thuật: [docs.cashu.space](https://docs.cashu.space)
- Danh sách các xưởng đúc tiền công cộng: [bitcoinmints.com](https://bitcoinmints.com)
- Trang web chính thức của giao thức: [cashu.space](https://cashu.space)



### Cộng đồng




- Nhóm Telegram Cashu: [t.me/cashu_ecash](https://t.me/cashu_ecash)