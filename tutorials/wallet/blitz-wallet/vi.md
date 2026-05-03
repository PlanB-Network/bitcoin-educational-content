---
name: Blitz Wallet
description: Ví Bitcoin đơn giản nhất.
---

![cover](assets/cover.webp)

Trải nghiệm người dùng là một trong những yếu tố quyết định khi chọn ví Bitcoin. Trong hướng dẫn này, chúng tôi giới thiệu Blitz Wallet, một ví đặt sự đơn giản làm trọng tâm trong cách tiếp cận: nhờ tích hợp giao thức **Spark**, Blitz mang đến cho bạn một trong những ví Bitcoin đơn giản và toàn diện nhất trên thị trường, với các khoản thanh toán tức thì và không cần quản lý kỹ thuật.

## Blitz Wallet là gì?

Blitz Wallet là một ví Bitcoin **self-custodial** và **open source**, tập trung vào quyền tự chủ của bạn cùng trải nghiệm người dùng mượt mà và trực quan.

[Blitz Wallet](https://blitz-wallet.com/) là ứng dụng di động có sẵn trên Android (Play Store) và iOS (App Store).

Không giống các ví Lightning truyền thống yêu cầu quản lý các kênh thanh toán và thanh khoản đầu vào, Blitz Wallet dựa trên **giao thức Spark** để loại bỏ những phức tạp kỹ thuật này. Kết quả: thanh toán tức thì ngay từ satoshi đầu tiên nhận được, không cần bất kỳ cấu hình nào trước đó. Mục tiêu của Blitz là làm cho thanh toán bằng bitcoin đơn giản như một ứng dụng thanh toán thông thường, mà không bao giờ ảnh hưởng đến quyền self-custody đối với tiền của bạn.

Blitz Wallet cũng hỗ trợ **địa chỉ dễ đọc** theo định dạng `nguoidung@tendomain.com` (qua LNURL), cho phép gửi bitcoin dễ dàng như gửi email, mà không cần phải xử lý các invoice dài hoặc QR code cho mỗi giao dịch.

## Tìm hiểu giao thức Spark

Trước khi đi vào thực hành, sẽ rất hữu ích nếu hiểu công nghệ vận hành Blitz Wallet bên trong: **giao thức Spark**.

### Spark là gì?

Spark là một giao thức lớp phủ open source được xây dựng trên Bitcoin, phát triển bởi đội ngũ Lightspark. Nó cho phép thực hiện các giao dịch tức thì với chi phí thấp, đồng thời bảo toàn quyền self-custody đối với bitcoin của bạn.

Không giống Lightning Network dựa trên **các kênh thanh toán** giữa hai bên, Spark sử dụng một công nghệ gọi là **statechain** (chuỗi trạng thái). Nguyên tắc cơ bản như sau: thay vì di chuyển bitcoin trên blockchain cho mỗi giao dịch, Spark chuyển **quyền chi tiêu** từ người dùng này sang người dùng khác, mà không có chuyển động on-chain.

### Nó hoạt động như thế nào?

Để hiểu Spark một cách trực quan, hãy tưởng tượng rằng chi tiêu bitcoin trên Spark đòi hỏi phải hoàn thành một câu đố gồm hai mảnh:
- Một mảnh được giữ bởi người dùng (ví dụ, Alice).
- Mảnh còn lại được giữ bởi một nhóm các nhà vận hành gọi là **Spark Entity (SE)**.

Chỉ sự kết hợp của hai mảnh tương ứng mới cho phép chi tiêu bitcoin.

Khi Alice muốn gửi bitcoin cho Bob, đây là những gì xảy ra: một câu đố mới được tạo ra cùng nhau giữa Bob và SE. Câu đố giữ nguyên hình dạng, nhưng các mảnh cấu thành nó thay đổi. Bây giờ, mảnh của Bob tương ứng với mảnh của SE. Mảnh cũ của Alice trở nên không sử dụng được, vì SE đã hủy mảnh tương ứng của nó. Quyền sở hữu bitcoin đã chuyển tay, **mà không có bất kỳ giao dịch nào trên blockchain**.

Bob sau đó có thể lặp lại cùng một quy trình để gửi bitcoin này cho Carol, và cứ tiếp tục như vậy. Mỗi lần chuyển hoạt động bằng cách thay thế các mảnh câu đố, chứ không phải bằng chuyển động tiền on-chain.

### Tại sao nó an toàn?

Một câu hỏi chính đáng được đặt ra: điều gì xảy ra nếu SE không thực sự hủy mảnh cũ của mình?

Spark Entity không phải là một thực thể duy nhất: nó là một nhóm các nhà vận hành độc lập. Mảnh của SE không bao giờ được giữ bởi một nhà vận hành duy nhất. Việc thay thế câu đố đòi hỏi sự hợp tác của nhiều nhà vận hành. Chỉ cần **một nhà vận hành duy nhất trung thực** trong một lần chuyển là đủ để ngăn chặn việc kích hoạt lại một câu đố cũ. Không một nhà vận hành đơn lẻ nào có thể bí mật giữ lại một câu đố cũ đang hoạt động hoặc tái tạo nó sau này.

Ngoài ra, Spark tích hợp một cơ chế rút tiền đơn phương: bạn luôn có thể lấy lại bitcoin on-chain mà không cần sự hợp tác của SE. Cơ chế dự phòng này là một phần không thể tách rời trong kiến trúc của Spark, và đảm bảo rằng bạn không bao giờ phụ thuộc vào mạng lưới để truy cập tiền của mình.

### Spark vs Lightning Network

Spark và Lightning không cạnh tranh nhau: chúng **bổ sung cho nhau**. Blitz Wallet tích hợp cả hai, cho phép bạn tận hưởng ưu điểm của từng giao thức.

|                               | **Spark**                       | **Lightning Network**      |
| ----------------------------- | ------------------------------- | -------------------------- |
| **Công nghệ**                 | Statechains (chuỗi trạng thái) | Kênh thanh toán            |
| **Quản lý kênh**              | Không yêu cầu                  | Yêu cầu                   |
| **Thanh khoản đầu vào**       | Không yêu cầu                  | Yêu cầu                   |
| **Giao dịch tức thì**         | Có                              | Có                         |
| **Self-custody**              | Có                              | Có                         |
| **Tương thích Lightning**     | Có (qua atomic swaps)          | Nguyên bản                 |

Lightning Network vẫn là một giao thức tuyệt vời cho thanh toán tức thì, nhưng nó áp đặt các ràng buộc kỹ thuật (quản lý kênh, thanh khoản đầu vào, node trực tuyến...) có thể gây khó khăn cho người mới. Spark loại bỏ những ràng buộc này trong khi vẫn tương thích với Lightning.

## Cài đặt và cấu hình

Trong hướng dẫn này, chúng tôi sử dụng phiên bản Android của Blitz Wallet, nhưng tất cả các quy trình được trình bày dưới đây cũng áp dụng được trên iOS.

![installation](assets/fr/01.webp)

Vì Blitz Wallet là ví self-custody, bạn có thể chọn **tạo ví mới** hoặc **nhập cụm từ khôi phục** (12 hoặc 24 từ) từ ví hiện có.

Ở đây, chúng tôi sẽ tạo một ví mới. Dưới đây là các khuyến nghị của chúng tôi về việc sao lưu cụm từ khôi phục:

https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

❗ **QUAN TRỌNG**: 12 hoặc 24 từ khôi phục này là **chìa khóa duy nhất để truy cập bitcoin của bạn**. Blitz là ví self-custodial: cả Blitz và Spark đều không có quyền truy cập vào cụm từ khôi phục hay tiền của bạn. Nếu bạn mất những từ này, bạn sẽ mất vĩnh viễn quyền truy cập vào bitcoin của mình. Đừng chia sẻ chúng với bất kỳ ai: bất cứ ai sở hữu chúng đều có thể chi tiêu bitcoin của bạn.

Sau đó tạo một **mã PIN** để bảo mật quyền truy cập vào ví của bạn.

![setup-wallet](assets/fr/02.webp)

## Bắt đầu với Blitz

Thực hiện giao dịch với Blitz trực quan hơn so với hầu hết các ví Bitcoin khác. Giao diện tối giản và tập trung vào ba hành động chính: gửi, quét và nhận.

### Nhận bitcoin

Để nhận bitcoin vào ví Blitz của bạn, nhấn vào biểu tượng **"Mũi tên xuống"** (↓), nhập số lượng satoshi bạn muốn nhận, thêm mô tả tùy chọn, sau đó ví sẽ tạo một hóa đơn (invoice) mà bạn có thể chia sẻ với người gửi.

⚠️ **LƯU Ý**: Satoshi (hay "sat") là đơn vị nhỏ nhất của bitcoin: **1 bitcoin = 100 000 000 satoshi**.

Một trong những đặc điểm của Blitz Wallet là hỗ trợ nhiều mạng lưới và giao thức trong hệ sinh thái Bitcoin:

- **Lightning Network**: Một trong những lớp phủ của Bitcoin cho phép thực hiện các khoản thanh toán nhỏ tức thì với phí rất thấp. Lý tưởng cho các khoản chi nhỏ hàng ngày.

- **Bitcoin (on-chain)**: Blockchain chính của giao thức Bitcoin, phù hợp cho các giao dịch có giá trị lớn hơn khi bảo mật tối đa và tính chung cuộc là ưu tiên.

- **Liquid Network**: Một sidechain (chuỗi song song) của Bitcoin được phát triển bởi Blockstream, cho phép các giao dịch nhanh chóng và bảo mật sử dụng Liquid Bitcoin (L-BTC).

https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

Theo mặc định, Blitz tạo một hóa đơn Lightning, nhưng bạn có thể chọn mạng lưới mà bạn muốn nhận satoshi bằng cách nhấn nút **"Choose format"** (Chọn định dạng).

![receive-sats](assets/fr/03.webp)

### Tạo danh bạ

Blitz Wallet đơn giản hóa việc gửi bitcoin định kỳ nhờ hệ thống danh bạ.

Trong menu **Contacts**, bạn có thể lưu tên người dùng Blitz hoặc địa chỉ Lightning (LNURL) mà bạn thường xuyên tương tác.

Nhờ đó, bạn có thể gửi satoshi đến các địa chỉ này chỉ trong vài cú nhấp, mà không cần quét QR code hoặc nhập thủ công địa chỉ mỗi lần.

### Gửi bitcoin

Ngoài các phương thức gửi bitcoin thông thường (quét QR code, nhập thủ công địa chỉ), Blitz cung cấp nhiều tùy chọn tiện lợi:

- **Từ ảnh** (*From Image*): Nhập QR code từ thư viện ảnh của bạn.
- **Từ bộ nhớ tạm** (*From Clipboard*): Dán địa chỉ hoặc hóa đơn đã sao chép trước đó.
- **Nhập thủ công** (*Manual Input*): Nhập trực tiếp địa chỉ Bitcoin, hóa đơn Lightning hoặc địa chỉ dễ đọc (ví dụ `nguoidung@walletofsatoshi.com`).
- **Từ danh bạ**: Chọn người nhận đã lưu trước để gửi chỉ trong vài cú nhấp.

Trong menu **Wallet**, nhấn nút **"Mũi tên lên"** (↑), chọn phương thức gửi, nhập số tiền cần gửi, thêm mô tả và xác nhận giao dịch.

Số tiền tối thiểu để thực hiện gửi hiện tại là **1 000 satoshi**.

![send-bitcoin](assets/fr/05.webp)

## Cửa hàng Blitz

Ngoài các hoạt động chuyển bitcoin, Blitz Wallet tích hợp một cửa hàng nơi bạn có thể chi tiêu bitcoin để mua các dịch vụ số trực tiếp từ ứng dụng.

Từ menu chính, nhấn vào tab **Store** để truy cập cửa hàng. Bạn cũng sẽ tìm thấy quyền truy cập vào nền tảng **Bitrefill** cho phép mua thẻ quà tặng từ hàng nghìn cửa hàng trên toàn thế giới, trực tiếp bằng bitcoin.

- **Trí tuệ nhân tạo**: Truy cập các mô hình AI sinh tạo mới nhất (Claude 3.5 Sonnet, GPT-4o, GPT-4o-mini, Gemini Flash 1.5) và thanh toán tín dụng trực tiếp bằng satoshi. Nhiều gói khả dụng theo nhu cầu của bạn (Casual, Pro, Power).

![ia-credits](assets/fr/06.webp)

- **SMS ẩn danh**: Gửi và nhận SMS ở mọi nơi trên thế giới mà không tiết lộ số điện thoại cá nhân của bạn. Dịch vụ được tính phí bằng satoshi cho mỗi tin nhắn gửi đi.

![sms-credit](assets/fr/07.webp)

- **VPN WireGuard**: Bảo vệ quyền riêng tư trực tuyến của bạn bằng cách đăng ký gói VPN WireGuard (hàng tuần, hàng tháng hoặc hàng quý), thanh toán bằng bitcoin trực tiếp từ cửa hàng Blitz. Bạn chỉ cần tải ứng dụng client WireGuard trên thiết bị của mình để sử dụng.

![wireguard](assets/fr/08.webp)

https://planb.academy/tutorials/exchange/centralized/bitrefill-8c588412-1bfc-465b-9bca-e647a647fbc1

## Blitz Wallet hậu trường: tìm hiểu sâu hơn

Đằng sau sự đơn giản trong sử dụng của Blitz Wallet là một kiến trúc kỹ thuật được thiết kế tốt, kết hợp nhiều lớp của hệ sinh thái Bitcoin.

### Phân bổ số dư của bạn

Blitz Wallet quản lý số dư của bạn một cách minh bạch bằng cách phân bổ tiền giữa các giao thức khác nhau tùy theo nhu cầu. Khi số dư của bạn dưới 500 000 satoshi, Blitz sử dụng **Liquid Network** và các hoán đổi nguyên tử (*atomic swaps*) để cung cấp trải nghiệm mượt mà và cho phép giao dịch trên Lightning Network ngay cả với số tiền nhỏ.

Cách tiếp cận này đảm bảo việc sử dụng đơn giản cho người dùng mới, mà không cần phải hiểu các cơ chế bên dưới. Bạn có thể xem phân bổ số dư giữa các lớp khác nhau trong menu **Cài đặt > Balance Info**.

![balance](assets/fr/09.webp)

### Chế độ Lightning (tùy chọn)

Theo mặc định, Blitz Wallet sử dụng Liquid Network và giao thức Spark để cung cấp trải nghiệm mượt mà mà không cần cấu hình kỹ thuật. Tuy nhiên, Blitz cho phép bạn kích hoạt **chế độ Lightning** sẽ tự động mở kênh thanh toán khi bạn đạt số dư **500 000 satoshi** (0,005 BTC).

Để kích hoạt chế độ Lightning, vào **Cài đặt**, sau đó trong phần **Cài đặt Kỹ thuật**, nhấn vào tùy chọn **Node Info**.

![enable-lightning](assets/fr/10.webp)

Nhờ giao thức Spark, việc kích hoạt này là **tùy chọn**: Spark đã cho phép thực hiện các khoản thanh toán tương thích Lightning mà không cần mở kênh hay quản lý thanh khoản đầu vào. Chế độ Lightning nguyên bản vẫn hữu ích cho người dùng nâng cao muốn có node Lightning riêng tích hợp trong ứng dụng.

### Điểm bán hàng (PoS)

Blitz Wallet tích hợp tính năng **điểm bán hàng** cho phép các thương nhân chấp nhận thanh toán bằng bitcoin trực tiếp từ ứng dụng.

Trong menu **Cài đặt > Point-of-sale**, bạn có thể cấu hình:

- Mã định danh duy nhất của cửa hàng
- Đồng tiền pháp định địa phương để hiển thị giá
- Hướng dẫn cho nhân viên của bạn
- Tùy chọn tiền tip cho khách hàng

Khách hàng chỉ cần quét QR code được tạo để thực hiện thanh toán bằng bitcoin một cách tức thì.

![pos](assets/fr/11.webp)

https://planb.academy/tutorials/wallet/mobile/speed-wallet-8715e454-1720-4a7f-8c1d-3da02cf67312

Tài liệu tham khảo được sử dụng để viết hướng dẫn này:
- Blog của [Breez](https://breez.technology/) Technology: [*Spark Explained Like You're Five*](https://blog.breez.technology/spark-explained-like-youre-five-8d554aad18d0).
