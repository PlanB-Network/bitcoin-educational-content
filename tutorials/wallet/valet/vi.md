---
name: Valet Bitcoin
description: Valet mang nút Lightning không lưu trữ vào túi của bạn
---

![cover_valet](assets/cover.webp)



## Giới thiệu


Valet là một hệ thống Bitcoin và Lightning wallet nhẹ, tự quản lý, cung cấp quy trình đăng ký dễ dàng và thuận tiện cho người mới bắt đầu. Nó được thiết kế đặc biệt để phục vụ các cộng đồng Bitcoin và nền kinh tế tuần hoàn, đặc biệt là ở các vùng sâu vùng xa.


Đây là fork của **Simple Bitcoin Wallet (SBW)**, với tính năng kênh Lightning được lưu trữ nâng cao có tên gọi **Fiat Channels**, được thiết kế để cho phép bất kỳ ai chấp nhận thanh toán Lightning mà không gặp rủi ro biến động giá.


Hiện tại, Valet chỉ khả dụng cho các thiết bị Android và có thể được tải xuống và cài đặt từ một số cửa hàng ứng dụng mã nguồn mở. Tuy nhiên, Valet **không** được lưu trữ trên **Google Play Store** do các vấn đề về quyền riêng tư của nhà phát triển và xác minh danh tính (KYC).



## Tải xuống và cài đặt Valet


Bạn có thể tải xuống Valet dưới dạng tệp APK từ trang GitHub của Standard Sats. [Standard Sats](https://standardsats.github.io/) là công ty đã phát triển Valet.


👉 Để tải xuống Valet, hãy truy cập trang GitHub của Standard Sats (https://github.com/standardsats/valet/releases) và tìm bản phát hành **mới nhất** (thường là bản nằm ở trên cùng).


👉 Vào mục **Tài sản** và nhấp vào tệp chỉ có đuôi **.apk**. Quá trình tải xuống sẽ bắt đầu tự động.


![Standard_Sats_GitHub_page_view](assets/en/001.webp)


👉 Sau khi quá trình tải xuống hoàn tất, hãy vào **Trình quản lý tập tin** trên thiết bị của bạn > **Tải xuống** và chọn tập tin apk Valet.


![Select_valet_apk](assets/en/002.webp)


👉 Cài đặt ứng dụng, và chỉ trong vài giây, ứng dụng sẽ sẵn sàng và xuất hiện trên màn hình chính của bạn.


![valet_icon_on_homescreen](assets/en/003.webp)


Ngoài ra, bạn cũng có thể tải xuống Valet từ cửa hàng ứng dụng **F-Droid**. Nếu bạn chưa có ứng dụng F-Droid trên thiết bị của mình, bạn có thể tải xuống và cài đặt ứng dụng [tại đây](https://f-droid.org/en/).


👉 Trên màn hình chính, mở F-Droid và tìm kiếm **Valet**. Chọn tùy chọn đầu tiên có biểu tượng **màu tím và trắng** trong hai tùy chọn sẽ xuất hiện, rồi nhấn **Tải xuống**.


![F-Droid_icon_on_homescreen](assets/en/004.webp)


![search_and_download_Valet](assets/en/005.webp)


👉 Sau khi tải xuống, hãy nhấp vào **Cài đặt** và làm theo hướng dẫn trên màn hình. Khi quá trình cài đặt hoàn tất, bạn có thể khởi chạy Valet từ F-Droid bằng cách nhấp vào **Mở**, hoặc khởi chạy ứng dụng từ màn hình chính của thiết bị.



## Tạo Bitcoin Wallet


Bạn có thể thiết lập Bitcoin wallet trên Valet chỉ với hai bước đơn giản.


👉 Khởi chạy Valet từ màn hình chính của thiết bị hoặc từ ứng dụng F-Droid. Màn hình thiết lập wallet sẽ hiện ra với hai tùy chọn: **Tạo Wallet mới** và **Khôi phục Wallet hiện có**.


👉 Chọn **Tạo Wallet mới**, và ngay lập tức, một wallet mới sẽ được tạo, và bạn sẽ được chuyển hướng đến trang chủ.


![set_up_a\_new_wallet](assets/en/006.webp)



## Sao lưu cụm từ hạt giống của bạn


👉 Trên trang chủ wallet, hãy nhấp vào **thẻ Green** có dòng chữ **"Chạm để lưu cụm từ khôi phục wallet trong trường hợp bạn bị mất hoặc thay thế thiết bị".**


![seed_phrase_green_card](assets/en/007.webp)


👉 Một bộ gồm 12 từ tiếng Anh sẽ được hiển thị. Hãy viết chúng ra giấy, theo thứ tự từ 1 đến 12, và giữ chúng cẩn thận.


![the_seed_phrase](assets/en/008.webp)


### Lưu ý ⚠️:


Hãy chú ý đến các yếu tố sau:


- Như bạn đã biết, Valet là một wallet tự quản lý, vì vậy cụm từ seed của bạn là cách duy nhất để khôi phục Wallet.
- Nếu bạn làm mất cụm từ seed, bạn sẽ **không bao giờ** có thể truy cập vào wallet.
- Nếu ai đó có được cụm từ seed của bạn, họ có thể đánh cắp vĩnh viễn tất cả các cụm từ Bitcoin của bạn.


Vì vậy, bạn cần viết ra cụm từ seed gồm 12 từ và cất giữ ở nơi an toàn. Bạn tuyệt đối không được chụp ảnh màn hình, lưu bản nháp trong email hoặc lưu trên bất kỳ thiết bị điện tử nào đã từng kết nối với internet.


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

## Nhận và gửi Bitcoin trên Valet


Valet là một wallet tự quản lý với cả khả năng on-chain và Lightning Bitcoin. Điều này có nghĩa là bạn có thể nhận và gửi Bitcoin từ Valet thông qua **trên chuỗi** hoặc thông qua **Lightning Network**.


Tuy nhiên, để có thể nhận hoặc gửi Bitcoin thông qua Lightning, bạn cần thiết lập kênh Lightning bằng cách sử dụng on-chain và Bitcoin của mình làm Liquidity. Hoặc bạn có thể mua một số thanh khoản kênh Lightning từ các nhà cung cấp.



## Tạo Bitcoin Address trên chuỗi


Để nhận được Bitcoin đến on-chain, bạn cần tạo địa chỉ Bitcoin.


👉 Trên trang chủ wallet, bạn sẽ thấy một thẻ **màu cam** và một thẻ **màu tím**, được dán nhãn tương ứng là **Bitcoin** và **Lightning**.


👉 Nhấp vào thẻ màu cam có nhãn **Bitcoin**. Bạn sẽ được chuyển hướng đến màn hình hiển thị địa chỉ Bitcoin.


![click_on_Bitcoin_card](assets/en/009.webp)


👉 Bạn có thể **sao chép** địa chỉ và gửi cho người đang gửi Bitcoin cho bạn, hoặc nhấp vào nút **chia sẻ** để gửi mã QR cho người đó qua mạng xã hội hoặc các kênh liên lạc khác.


👉 Bạn cũng có thể nhấp vào nút **Chỉnh sửa** để thiết lập số lượng Bitcoin cần gửi đến địa chỉ đó.


**Lưu ý:** Giống như hóa đơn, tính năng chỉnh sửa rất hữu ích trong trường hợp bạn muốn nhận một số lượng Bitcoin cụ thể tại một địa chỉ; tuy nhiên, điều này không có nghĩa là địa chỉ đó không thể nhận số lượng nhiều hơn hoặc ít hơn.


👉Nhấp vào **Thêm địa chỉ mới** để tạo địa chỉ ngẫu nhiên mới.


![generating_a\_bitcoin_add](assets/en/010.webp)


👉 Bạn cũng có thể tạo địa chỉ on-chain Bitcoin bằng cách nhấp vào nút **Nhận** ở cuối trang chủ wallet của bạn. Sau đó chọn **Nhận vào địa chỉ bitcoin** và tiếp tục với quy trình tương tự như trên.


![click_receieve_button](assets/en/011.webp)


![receive_to_bitcoin_address](assets/en/012.webp)



## Gửi Bitcoin qua On-chain


Việc gửi Bitcoin từ Valet wallet thông qua on-chain là một nhiệm vụ đơn giản.


👉 Ở cuối trang chủ wallet, hãy nhấp vào nút **Gửi**, nhập địa chỉ Bitcoin, hoặc nhấp vào **Quét** để quét mã QR địa chỉ, sau đó nhấp vào **OK**.


![click_send_button](assets/en/013.webp)


![enter_bitcoin_add](assets/en/014.webp)


👉 Nhập số tiền Bitcoin bạn muốn gửi. Bạn có thể nhập thủ công số tiền theo Sats hoặc theo đơn vị tiền tệ Fiat, hoặc bạn có thể nhấp vào **Tối đa** để sử dụng toàn bộ số dư on-chain của mình.


👉 Bạn cũng có thể điều chỉnh phí giao dịch bằng cách nhấp vào ô màu xanh nhỏ có nhãn **phí** rồi kéo chấm trắng sang phải hoặc trái để tăng hoặc giảm phí. Nhấp vào **Ok** để gửi giao dịch.


![enter_amount_and_fee_rate](assets/en/015.webp)



## Thiết lập kênh Lightning Network


Như đã đề cập ở trên, Valet là một thiết bị tự quản lý Bitcoin và Lightning wallet; do đó, để có thể gửi và nhận Bitcoin thông qua mạng Lightning, trước tiên bạn phải thiết lập một kênh Lightning theo các bước sau:


👉 Trên màn hình chính, hãy nhấp vào **thẻ màu tím** có nhãn **Lightning**. Bạn sẽ được chuyển đến một trang với các tùy chọn sau:



- Quét mã QR nút
- Mua hàng tại LNBIG.COM
- Mua hàng tại BITREFILL.COM
- Yêu cầu đồng bộ lại đồ thị LN.


Khi bạn chọn **Mua từ lnbig.com** hoặc **Mua từ bitrefill.com**, bạn sẽ được chuyển hướng đến trang web của các công ty này, nơi bạn có thể mua thanh khoản đầu vào với nhiều dung lượng khác nhau. Tạm thời bỏ qua tùy chọn cuối cùng **Yêu cầu đồng bộ lại biểu đồ LN**.


Vì vậy, lựa chọn tối ưu của chúng ta ở đây là **Quét mã QR của Node**. Tại thời điểm này, bạn phải đã quyết định và có được **mã QR** của node mà bạn muốn mở kênh. Bạn có thể mở kênh đến bất kỳ node công cộng nào bạn chọn. Hãy xem [1ML](https://1ml.com/) hoặc [Amboss](https://amboss.space/), chọn bất kỳ node công cộng nào bạn muốn và quét mã QR tương ứng của node bạn đã chọn.


![channel_opening_options](assets/en/016.webp)


👉 Bạn sẽ tự động được chuyển hướng đến trang tiếp theo, nơi bạn cần nạp tiền cho kênh của mình. Một lần nữa, việc sử dụng mạng Lightning tự quản lý yêu cầu bạn sử dụng Bitcoin để nạp tiền cho kênh. Điều này có nghĩa là bạn phải có Bitcoin trong on-chain hoặc wallet để nạp tiền cho kênh Lightning. Vui lòng tham khảo bài viết này của [Hacken](https://hacken.io/discover/lightning-network/) để tìm hiểu thêm về mạng Lightning.


![fund_channel](assets/en/017.webp)


👉 Nhập **số lượng** Bitcoin bạn muốn dùng để tài trợ cho kênh, hoặc nhấp vào **Tối đa** để sử dụng toàn bộ số dư on-chain/Bitcoin của bạn. Bạn có thể điều chỉnh **phí**, hoặc giữ nguyên mức phí mặc định, rồi nhấp vào **OK**.


**Lưu ý:** Số tiền bạn nạp vào kênh sẽ là dung lượng của kênh mới (tức là tổng khối lượng Sats có thể được giao dịch đến và đi từ kênh đó)


Điều quan trọng nữa là bạn cần sử dụng số tiền cấp vốn trên **100.000 Sats** khi mở kênh. Điều này là do nhiều node Lightning yêu cầu dung lượng tối thiểu 100.000 Sats để mở kênh kết nối với chúng. Vì vậy, để tránh thử và sai, hãy sử dụng số tiền cao hơn phạm vi đó.


![enter_funding_amount](assets/en/018.webp)


![funding_approval](assets/en/019.webp)


👉 Tại thời điểm này, khi bạn kiểm tra trang chủ wallet, bạn sẽ thấy số tiền đã được chuyển từ thẻ **Bitcoin** sang thẻ **Lightning**. Trong lịch sử giao dịch, bạn sẽ thấy giao dịch nạp tiền đang được xử lý.


![channel_funding_processing](assets/en/020.webp)


👉 Nếu bạn nhấp vào thẻ Lightning, bạn sẽ thấy thông tin cho thấy kênh Lightning của bạn đang được mở. Bạn cũng sẽ thấy **giao dịch nạp tiền vào kênh** trong danh sách giao dịch của mình. Hãy đợi cho đến khi giao dịch nạp tiền được xác nhận trên blockchain, và kênh Lightning của bạn sẽ sẵn sàng.


![channel_opening](assets/en/021.webp)


👉 Ngay sau khi giao dịch nạp tiền được xác nhận, hãy nhấp vào **thẻ Lightning** trên trang chủ của bạn, và bạn sẽ thấy thông tin về kênh Lightning của mình như sau:



- TẬP HỢP CÁC SỐ NGẪU NHIÊN ĐƯỢC PHÂN CÁCH BỞI DẤU CHẤM:** Đây là địa chỉ IP của các nút. (IPV4 và IPV6, tương ứng)
- DUNG LƯỢNG:** Đây là tổng dung lượng Sats có thể được gửi và nhận qua kênh này
- SỐ LƯỢNG CÓ THỂ GỬI:** Đây là số lượng Sats bạn có thể gửi đi tại thời điểm này. Bạn sẽ thấy rằng con số này gần như tương đương với **Dung lượng**. Điều này là do bạn chưa gửi bất kỳ khoản thanh toán nào qua kênh này.
- SỐ LƯỢNG CÓ THỂ NHẬN:** Đây là số lượng Sats bạn có thể nhận được trên kênh này hiện tại. (Số lượng này sẽ rất ít hoặc không có vào thời điểm này vì để có thể nhận được, trước tiên bạn phải gửi đi một số Sats để tạo ra tín hiệu Liquid đến)
- **CÓ THỂ HOÀN TRẢ:** Số tiền này được hiển thị và hoàn trả vào địa chỉ on-chain của bạn khi bạn đóng kênh. Số tiền này cũng được gọi là **số dư cục bộ của kênh**. Lưu ý rằng số tiền này thấp hơn một chút so với dung lượng kênh, vì khi đóng kênh, bạn phải trả phí để công bố giao dịch đóng kênh trên blockchain, giống như khi bạn nạp tiền vào kênh. Vì vậy, hệ thống đã trừ đi số tiền tối thiểu ước tính mà bạn sẽ phải trả.)
- GIÁ TRỊ TRONG QUÁ TRÌNH CHUYỂN TIỀN:** Khi ai đó gửi sats đến kênh của bạn, hoặc khi bạn cố gắng gửi sats cho ai đó, và vì bất kỳ lý do gì mà giao dịch bị trì hoãn, điều này thường được hiển thị trong trường này.


![channel_info](assets/en/022.webp)


## Gửi Sats qua kênh của bạn


Việc truyền tín hiệu Sats qua Lightning Network là một nhiệm vụ khá đơn giản.


👉 Ở cuối trang chủ, hãy nhấp vào **Gửi** và **dán** hóa đơn Lightning (bạn phải sao chép nó) vào ô được cung cấp, hoặc nhấp vào **Quét** để quét mã QR của hóa đơn Lightning.


![click_send_or_scan](assets/en/023.webp)


Hầu hết các hóa đơn Lightning đều có số tiền cần thanh toán được nhập sẵn. Nhưng trong một số trường hợp, đó có thể là hóa đơn chưa thanh toán mà bạn phải tự điền số tiền.


👉 Nhập số tiền bằng **Đô la** hoặc **Sats**, hoặc nhấp vào **Tối đa** để sử dụng toàn bộ số dư trên kênh Lightning của bạn, sau đó nhấp vào **OK**. Ngay khi tìm thấy đường dẫn phù hợp, khoản thanh toán của bạn sẽ được gửi và hoàn tất trong vài giây. Hãy theo dõi trang chủ để xem khoản thanh toán đã hoàn tất hay chưa. Nó sẽ hiển thị dấu tích màu xanh lá cây khi hoàn tất.


![enter_the_amount](assets/en/024.webp)


## Đang nhận tín hiệu Sats qua kênh của bạn


Việc nhận thanh toán trên kênh Lightning của bạn phụ thuộc phần lớn vào việc bạn có nhận được Liquidity hay không. Sau khi mở kênh, bạn sẽ không thể nhận thanh toán cho đến khi bạn gửi ít nhất một lượng Sats nhất định để **tạo thanh khoản đầu vào** ở đầu bên kia của kết nối kênh. Để xác nhận xem bạn có thể nhận Sats hay không và số lượng Sats bạn có thể nhận, hãy kiểm tra trường **Có thể nhận** trong thông tin kênh của bạn. Điều này sẽ cho bạn biết bạn nhận được bao nhiêu Sats tại mỗi thời điểm.


Giả sử bạn đã gửi một lượng Sats từ kênh của mình, hiện tại bạn đã có nguồn thanh khoản đến và có thể nhận thêm Sats.


Để nhận tin nhắn trên kênh Lightning, bạn cần tạo hóa đơn. Không giống như Bitcoin và on-chain sử dụng địa chỉ, mạng Lightning sử dụng hóa đơn. Có hai cách để tạo hóa đơn trên Valet.


#### LỰA CHỌN 1


👉 Ở cuối trang chủ, nhấp vào **Nhận**, chọn **Nhận vào hóa đơn Lightning**. Điền số tiền cần nhận trong hóa đơn và nhấp vào **Ok**. Sao chép hóa đơn hoặc chia sẻ mã QR với người trả tiền.


![receive_to_channel](assets/en/025.webp)


![fill_invoice_amount](assets/en/026.webp)


![copy_invoice_or_share_QR](assets/en/027.webp)


#### LỰA CHỌN 2


👉 Nhấp vào biểu tượng tia sét màu tím trên trang chủ wallet của bạn. Chạm vào bất kỳ đâu trên kênh của bạn, và một danh sách các tùy chọn sẽ hiện ra. Chọn **Nhận vào kênh** và nhập số tiền bạn đang nhận (bằng Sats hoặc đô la). Bạn cũng sẽ thấy số lượng Sats bạn có thể nhận (dung lượng nhận) khi bạn điền hóa đơn. Nhấp vào **OK** và sao chép hóa đơn hoặc chia sẻ mã QR với người trả tiền.


![receive_to_channel](assets/en/028.webp)


**Lưu ý:** Tùy chọn đầu tiên là tùy chọn chung, có nghĩa là nếu bạn có nhiều hơn một kênh đang hoạt động và bạn sử dụng tùy chọn đầu tiên, hệ thống sẽ tự động chọn một trong các kênh của bạn để thu tín hiệu Sats.


Vì vậy, trong trường hợp này, phương án thứ hai là lựa chọn tốt nhất nếu bạn muốn thu sóng Sats trên một kênh cụ thể.


### Giải thích các tùy chọn cửa sổ bật lên kênh của bạn


Khi bạn nhấn vào kênh của mình, các trường tùy chọn sau sẽ được hiển thị:


![channel_pop_ups](assets/en/029.webp)


**CHIA SẺ THÔNG TIN KÊNH LIGHTNING:** Tính năng này cho phép bạn chia sẻ thông tin chi tiết kênh của mình, chẳng hạn như ID của người dùng từ xa, ID kênh cục bộ, giao dịch cấp vốn, ngày tạo, v.v.


**ĐÓNG KÊNH VỚI VÍ:** Bạn có thể đóng kênh Lightning của mình bất cứ khi nào bạn muốn. Để đóng kênh, hệ thống sẽ kiểm tra số dư Bitcoin bạn có ở phía bên kia kênh (hãy nhớ trường **"Có thể gửi"**, còn được gọi là số dư cục bộ của bạn), và gửi lại cho bạn. Trong Valet, bạn có thể chọn nơi bạn muốn gửi Bitcoin đó khi kênh bị đóng. Vì vậy, **Đóng kênh với wallet** là một trong hai lựa chọn của bạn.


👉 Nhấp vào tùy chọn này và chọn **Bitcoin**. Quá trình đóng kênh sẽ bắt đầu và số dư kênh Bitcoin của bạn sẽ được chuyển lại địa chỉ on-chain của wallet.


![close_channel_to_wallet](assets/en/030.webp)


**ĐÓNG KÊNH ADDRESS:** Đây là tùy chọn thứ hai để đóng kênh. Khi chọn tùy chọn này, bạn sẽ được yêu cầu nhập địa chỉ wallet mà số dư Bitcoin trên kênh của bạn sẽ được chuyển đến. Xin lưu ý rằng trong tùy chọn này, bạn chỉ có thể quét mã QR của địa chỉ Bitcoin mà bạn muốn đóng kênh. Hiện tại, không có tùy chọn dán địa chỉ thủ công.


👉 Nhấp vào tùy chọn này, quét địa chỉ Bitcoin và nhấp **Ok**. Quá trình đóng kênh sẽ bắt đầu và số dư Lightning Bitcoin của bạn sẽ được gửi đến địa chỉ bạn đã quét.


![scan_address_and_Ok](assets/en/031.webp)


**NHẬN THANH TOÁN QUA KÊNH:** Chức năng này tương tự như tạo hóa đơn, nhưng trong một số trường hợp, bạn có thể có nhiều hơn một kênh, bao gồm cả các kênh Fiat (một loại kênh Lightning đặc biệt có thể tìm thấy trong Valet wallet). Vì vậy, nếu bạn đang mở nhiều kênh, tùy chọn này đảm bảo bạn có thể nhận thanh toán vào một kênh cụ thể.


**NẠP TIỀN TỪ CÁC KÊNH KHÁC:** Tùy chọn này cho phép bạn nạp tiền cho một kênh từ các kênh hiện có khác. Ví dụ, nếu bạn có 2 kênh Lightning khác nhau (A và B), và số dư Bitcoin trên kênh A đã cạn kiệt, với tùy chọn này, bạn có thể dễ dàng và tự động nạp thêm tiền vào kênh A từ kênh B.


**NHẬN TRỰC TIẾP KHÔNG RIÊNG TƯ:** Đây cũng là một tùy chọn để tạo hóa đơn nhận thanh toán, nhưng khi bạn sử dụng tùy chọn này, người gửi sẽ thanh toán trực tiếp cho bạn. Điều này có nghĩa là khoản thanh toán không đi qua nhiều nút khác nhau trước khi đến tay bạn, như một khoản thanh toán Lightning thông thường. Vì vậy, về cơ bản, người gửi biết họ đã thanh toán cho bạn, biết ID kênh của bạn, v.v. Tùy chọn này thường được sử dụng khi bạn nhận thanh toán từ một nguồn đáng tin cậy và không cần duy trì tính riêng tư của mình.


## Hosted và Fiat Channels


Giống như nhiều mẫu Bitcoin wallet khác, Valet là một chiếc Bitcoin và Lightning wallet đơn giản, gọn nhẹ. Nhưng nó có một tính năng độc đáo của Lightning giúp phân biệt nó với hầu hết các mẫu Bitcoin wallet khác. Tính năng đó được gọi là **Hosted and Fiat Channels**.


Kênh Fiat là một loại triển khai Lightning cho phép dễ dàng tham gia và sử dụng mạng Lightning. Đây là giải pháp lưu ký cho phép ẩn danh hoàn toàn, giống như kênh Lightning thông thường. Công nghệ kênh Fiat cũng cho phép tạo ra các sản phẩm phái sinh Bitcoin trên mạng Lightning. Ví dụ, với kênh Fiat, người bán có thể chấp nhận thanh toán Bitcoin có giá trị ổn định mà không cần lo lắng về sự biến động của Bitcoin.


Việc triển khai hiện tại của các kênh Fiat trên Valet cho phép tạo ra các loại tiền tệ Fiat tổng hợp ổn định được hỗ trợ bởi Sats. Nó sử dụng mối quan hệ Máy chủ-Máy khách, trong đó Máy chủ là bất kỳ nút Lightning nào cung cấp dịch vụ này, và máy khách là người dùng Valet. Đây là một giải pháp lưu ký vì tất cả các Sats đều nằm ở phía Máy chủ; tuy nhiên, việc tạo hóa đơn, định tuyến Tor và tạo ảnh trước vẫn diễn ra ở phía máy khách như trong một kênh Lightning thông thường.


Việc mở kênh Fiat có quy trình tương tự như mở kênh Lightning. Sự khác biệt đáng kể duy nhất là trong trường hợp này, khách hàng (người dùng Valet) không cần phải cam kết bất kỳ khoản thanh khoản on-chain nào để tạo dung lượng kênh. Máy chủ sẽ thiết lập dung lượng kênh và định tuyến tất cả các khoản thanh toán cho khách hàng.


👉 Để mở kênh Fiat, hãy nhấp vào **thẻ Lightning** màu tím trên trang chủ wallet của bạn. Chọn **Quét mã QR nút** (Tại bước này, bạn phải xác định được Máy chủ mà bạn muốn mở kênh và đã lấy được mã QR của nút đó. Ví dụ về một nút Máy chủ mà bạn có thể mở kênh Fiat là nút SATM của Standard Sats.)


**Lưu ý:** Điều quan trọng cần lưu ý là bất kỳ ai cũng có thể trở thành Host. Tất cả những gì bạn cần là chạy một node Lightning với **plugin kênh Fiat** và một **dịch vụ phòng ngừa rủi ro**. Kênh Fiat là một dự án mã nguồn mở của *Standard Sats*. Tìm hiểu thêm về nó [tại đây](https://github.com/standardsats/fiat-channels-rfc) và [tại đây](https://standardsats.github.io/).


Mã QR của nút SATM bên dưới:


![SATM_node_QR](assets/en/032.webp)


👉 Sau khi quét mã QR của node, hãy nhấp vào **Yêu cầu kênh tiền pháp định USD** hoặc **Yêu cầu kênh tiền pháp định EUR** (Đây là đơn vị tiền pháp định mà số dư tiền pháp định của bạn sẽ được hiển thị). Hiện tại, hãy chọn USD và nhấp vào **OK**. Kênh sẽ được mở tự động và bạn có thể bắt đầu nhận Sats ngay lập tức. Thấy chưa, thật đơn giản!!!


![choose_fiat_denomination](assets/en/033.webp)


![channel_confirmation_prompt](assets/en/034.webp)


👉 Vào trang chủ của wallet, bạn sẽ thấy một thẻ **màu xanh lá nhạt** có nhãn **USD**, đó là **kênh tiền pháp định** của bạn.


![fiat_channel_card](assets/en/035.webp)


**Lưu ý:** Khi bạn nhận Sats trên kênh Fiat, giá trị Fiat của Sats bạn nhận được sẽ được khóa lại dưới dạng số dư ổn định, trong khi khối lượng Sats sẽ biến động theo giá Bitcoin. Giải pháp này được thiết kế chủ yếu dành cho các thương gia muốn chấp nhận Sats làm phương thức thanh toán nhưng không muốn đối mặt với những thách thức về biến động giá của Bitcoin. Điều này giúp họ duy trì giá trị ổn định mọi lúc, đồng thời vẫn có thể giao dịch trên mạng Lightning, tận hưởng phạm vi toàn cầu và khả năng thanh toán nhanh chóng của Bitcoin như một phương tiện trao đổi trên Lightning Network.


Khi kênh Fiat của bạn được tạo, bạn sẽ thấy các trường Giá trị sau và ý nghĩa của từng trường:


![fiat_channel_info](assets/en/036.webp)



- TẬP HỢP CÁC SỐ NGẪU NHIÊN ĐƯỢC PHÂN CÁCH BỞI DẤU CHẤM:** Đây là địa chỉ IP của các nút. (IPV4 và IPV6, tương ứng)
- GIÁ THUÊ MÁY CHỦ:** Đây là giá thị trường Bitcoin mà Nhà cung cấp dịch vụ đang chào bán cho bạn. Giá này thường sẽ hơi khác so với giá thị trường phổ biến, vì Nhà cung cấp dịch vụ có thể cộng thêm một khoản phí nhỏ. Việc quyết định mức giá này hoàn toàn phụ thuộc vào Nhà cung cấp dịch vụ; do đó, mức giá này cũng sẽ khác nhau giữa các Nhà cung cấp dịch vụ.
- **Số dư tiền pháp định:** Đây là giá trị tiền pháp định ổn định được cố định của mỗi sat bạn nhận được trên kênh này. Hãy nhớ rằng, như đã giải thích trước đó, bất cứ khi nào bạn nhận được Sats trên kênh tiền pháp định của mình, giá trị tiền pháp định của Sats tại thời điểm nhận sẽ ngay lập tức được cố định dưới dạng giá trị tiền pháp định ổn định tổng hợp trong trường này. Giá trị **Số dư tiền pháp định** của bạn không biến động theo giá thị trường của Bitcoin. Bất cứ khi nào bạn muốn thực hiện thanh toán từ kênh này, bạn chỉ có thể gửi số tiền tương đương Sats của số dư tiền pháp định này. Vì vậy, hãy coi đây như một loại tiền pháp định kỹ thuật số được hỗ trợ bởi Sats.
- **DUNG LƯỢNG:** Đây là tổng dung lượng Sats có thể được gửi và nhận qua kênh này. (Thông số này cũng do Máy chủ thiết lập. Và không giống như kênh Lightning thông thường, dung lượng này có thể được Máy chủ điều chỉnh tùy theo trường hợp.)
- **KHẢ NĂNG GỬI:** Đây là khối lượng Sats bạn có thể gửi đi tại mỗi thời điểm dựa trên số dư tiền pháp định của bạn. Điều này hoàn toàn khác với những gì bạn thấy trong kênh Lightning thông thường, vì giá trị này biến động theo giá Bitcoin. Do đó, những gì bạn thấy ở đây là giá trị Sats tương ứng với số dư tiền pháp định của bạn tại bất kỳ thời điểm nào dựa trên **Tỷ giá máy chủ**.
- SỐ LƯỢNG CÓ THỂ NHẬN:** Đây là số lượng Sats mà bạn có thể nhận được trên kênh này hiện tại. Sau khi bạn tạo kênh, giá trị này sẽ bằng với dung lượng của kênh.
- GIÁ TRỊ ĐANG TRUYỀN TẢI:** Khi ai đó gửi sats đến kênh của bạn, hoặc khi bạn cố gắng gửi sats cho ai đó, và vì bất kỳ lý do gì, giao dịch bị trì hoãn, điều này thường được hiển thị trong trường này.


Dưới đây là những điều quan trọng cần lưu ý về các kênh phân phối của Fiat:



- Không giống như kênh Lightning thông thường, khi bạn mở kênh fiat, bạn có thể bắt đầu nhận Sats ngay lập tức, nhưng không thể gửi. Bạn chỉ có thể gửi Sats khi đã nhận được Sats.
- Trong mọi trường hợp, tài sản được gửi đi và nhận lại đều là Sats. *Số dư tiền pháp định* chỉ là một giấy nợ giả định thể hiện giá trị Bitcoin nhận được tại bất kỳ thời điểm nào. Vì vậy, nó không phải là một token được tạo ra hay một loại tiền điện tử mới.
- Kênh giao dịch bằng tiền pháp định chủ yếu hữu ích cho các thương nhân/doanh nghiệp còn e ngại việc chấp nhận thanh toán bằng Bitcoin do lo ngại về sự biến động của đồng tiền này. Nó cũng có thể hữu ích cho các công ty muốn trả lương cho nhân viên bằng Bitcoin mà không phải chịu hậu quả của sự biến động giá Bitcoin, điều có thể khiến vốn lương của họ trở nên không ổn định. Ngoài ra, nó cũng có thể hữu ích cho các cá nhân sống ở khu vực có tỷ lệ sử dụng Bitcoin cao nhưng có chi phí sinh hoạt cố định.
- Xin lưu ý rằng không có trường nào được gắn nhãn là **HOÀN TIỀN**. Điều này là do, về mặt kỹ thuật, bạn không thể đóng kênh Fiat. Bạn chỉ có thể ngừng sử dụng kênh Fiat bằng cách chuyển toàn bộ số dư của kênh đó sang kênh Lightning thông thường của mình.


### Giải thích các tùy chọn cửa sổ bật lên của Fiat Channel


Khi bạn chạm vào kênh Fiat Lightning của mình, các trường sau sẽ được hiển thị:


![fiat_channel_pop_up](assets/en/037.webp)


**CHIA SẺ THÔNG TIN KÊNH ĐƯỢC LƯU TRỮ:** Điều này cho phép bạn chia sẻ thông tin kênh Fiat của mình, chẳng hạn như ID của thiết bị đầu cuối từ xa, ID kênh cục bộ, ngày tạo, v.v.


**XUẤT TRẠNG THÁI KÊNH:** Chức năng này cho phép bạn xuất trạng thái của một kênh tại bất kỳ thời điểm nào. Điều này thường hữu ích trong việc khắc phục lỗi kênh, và người chủ trì có thể yêu cầu bạn chia sẻ thông tin này nếu cần thiết.


**XẢ DƯ KÊNH:** Như đã đề cập trước đó, về mặt kỹ thuật, bạn không thể đóng kênh Fiat, nhưng bạn có thể xả dư của kênh đó vào kênh Lightning thông thường hiện có của mình. Thao tác này sẽ tự động chuyển lượng dư tương đương với số dư kênh Fiat sang kênh Lightning thông thường của bạn.


**NHẬN TIỀN VÀO KÊNH:** Chức năng này tương tự như tạo hóa đơn, nhưng trong một số trường hợp, người dùng có thể có nhiều hơn một kênh Fiat với các Host khác nhau, bao gồm cả các kênh Lightning thông thường. Vì vậy, nếu người dùng đang mở nhiều kênh, tùy chọn này đảm bảo họ có thể nhận thanh toán vào một kênh cụ thể.


**NẠP TỪ CÁC KÊNH KHÁC:** Tùy chọn này cho phép người dùng nạp một kênh từ các kênh hiện có khác. Vì vậy, với tùy chọn này, bạn có thể nạp kênh Fiat của mình từ một kênh thông thường hoặc từ các kênh Fiat khác mà bạn có, giống như cách bạn xả hết nước.


**NHẬN TRỰC TIẾP KHÔNG QUA MẠNG RIÊNG TƯ:** Đây cũng là một tùy chọn để tạo hóa đơn nhận thanh toán, nhưng khi bạn sử dụng tùy chọn này, người gửi sẽ thanh toán trực tiếp cho bạn. Điều này có nghĩa là khoản thanh toán không đi qua nhiều khâu trung gian trước khi đến tay bạn. Vì vậy, về cơ bản, người gửi biết họ đã thanh toán cho bạn, biết ID kênh của bạn, v.v. Tùy chọn này thường được sử dụng khi bạn nhận thanh toán từ một nguồn đáng tin cậy và không cần phải bảo mật thông tin cá nhân.


## Cài đặt Valet:


Cũng giống như mọi ứng dụng khác, Valet có các cài đặt ứng dụng mà bạn có thể điều chỉnh theo sở thích của mình. Bạn có thể truy cập trang cài đặt từ màn hình chính.


👉 Trên màn hình chính, hãy nhấp vào biểu tượng **Bánh răng** nằm ở góc trên bên phải màn hình để truy cập cài đặt. Dưới đây là các thành phần trong phần cài đặt.


![settings_icon](assets/en/038.webp)


**CHỨC NĂNG SAO LƯU KÊNH CỤC BỘ ĐÃ ĐƯỢC KÍCH HOẠT:** Nếu chức năng này **bị vô hiệu hóa**, bạn nên kích hoạt nó vì đây là cách duy nhất để bạn có thể khôi phục các kênh Lightning thông thường nếu bạn gỡ cài đặt và cài đặt lại Valet. Chúng tôi sẽ giải thích điều này sau. Vì vậy, hãy nhấp vào đây và cấp cho Valet quyền truy cập vào **bộ nhớ phương tiện** của bạn vì đó là nơi lưu trữ tệp sao lưu.


![app_permissions](assets/en/039.webp)


![enable_media_access](assets/en/040.webp)


**NƠI LƯU TRỮ BẢN SAO LƯU CỤC BỘ:** Nếu bạn đã cấp quyền cho Valet truy cập vào bộ nhớ của mình, trường này sẽ tự động được thiết lập để lưu trữ bản sao lưu cục bộ trong thư mục **Tải xuống** của bạn. Nhưng bạn có thể thay đổi bằng cách nhấp vào đây và chọn bất kỳ thư mục nào bạn muốn.


**QUẢN LÝ VÍ CHAIN** Phần này hơi phức tạp một chút, và bạn không cần phải bận tâm về nó trừ khi bạn đủ kinh nghiệm. Cài đặt mặc định ở đây là hoàn toàn ổn.


**THÊM VÍ PHẦN CỨNG:** Bạn cũng không cần bận tâm về điều này, trừ khi bạn có ví phần cứng wallet muốn kết nối và theo dõi. Với thiết lập này, bạn có thể quét và kết nối ví phần cứng wallet của mình, chẳng hạn như Trezor hoặc Cold Card, và theo dõi hoạt động của nó. Đây là tính năng chỉ xem, nghĩa là bạn không thể thực hiện giao dịch trên ví phần cứng wallet từ đây. Bạn chỉ có thể quan sát và theo dõi hoạt động, số dư, v.v. của wallet.


**THIẾT LẬP NÚT ELECTRUM TÙY CHỈNH:** Đây cũng là vấn đề kỹ thuật, và trừ khi bạn đủ am hiểu, bạn không nên bận tâm đến điều này. Cài đặt mặc định là đủ tốt.


**ĐƠN VỊ BITCOIN:** Đây là cách bạn muốn hiển thị số dư Bitcoin của mình. Tùy chọn đầu tiên hiển thị số dư của bạn theo đơn vị Satoshi, ví dụ: 1.000.000 Sats, trong khi tùy chọn thứ hai hiển thị theo đơn vị BTC với số thập phân là 0,01 BTC


**SỬ DỤNG XÁC THỰC BẰNG MÃ PIN** Nếu bạn chọn ô này, bạn sẽ phải thiết lập mã PIN hoặc dấu vân tay để nhập khi đăng nhập vào wallet và xác thực giao dịch.


**SỬ DỤNG KẾT NỐI TOR:** Nếu bạn chọn ô này, các giao dịch của bạn sẽ được định tuyến qua mạng Tor. Điều này tăng thêm một lớp bảo mật nhưng có thể dẫn đến tốc độ xử lý thanh toán chậm hơn, đặc biệt là đối với các khoản thanh toán Lightning.


**XEM CỤM TỪ KHÔI PHỤC BIP39:** Đây là nơi bạn có thể truy cập cụm từ seed gồm 12 từ để sao lưu. Vì vậy, nếu bạn chưa ghi lại trước đó, hoặc bạn không tìm thấy nơi bạn đã ghi lại, miễn là bạn vẫn có quyền truy cập vào Wallet, bạn có thể sao chép nó từ đây.


**THỐNG KÊ SỬ DỤNG:** Phần này hiển thị tóm tắt tất cả các giao dịch và hoạt động của bạn kể từ khi tạo wallet


![usage_stats](assets/en/041.webp)


## Phục hồi Wallet


Valet là một ứng dụng wallet không lưu trữ dữ liệu, vì vậy nếu bạn làm mất thiết bị hoặc gỡ cài đặt ứng dụng wallet, bạn sẽ cần thực hiện khôi phục wallet để lấy lại các kênh Bitcoin và Lightning của mình. Ở đầu hướng dẫn này, chúng tôi đã đề cập đến tầm quan trọng của việc ghi lại **cụm từ 12 từ seed** vì đó là chìa khóa để khôi phục wallet của bạn. Không có đại diện chăm sóc khách hàng nào có thể giúp bạn truy cập lại vào wallet.


Để khôi phục Valet wallet, cần hai công cụ quan trọng, tùy thuộc vào việc bạn có kênh Lightning đang hoạt động hay không. Đối với người dùng không có kênh Lightning thông thường đang hoạt động, tất cả những gì họ cần là **cụm từ seed gồm 12 từ**, bằng cách làm theo các bước đơn giản dưới đây:


👉 Cài đặt ứng dụng Valet mới và khởi chạy ứng dụng.


👉 Chọn **Khôi phục Wallet hiện có**


![restore_existing_wallet](assets/en/042.webp)


👉 Chọn **Chỉ cụm từ khôi phục**.


![select_recovery_phrase](assets/en/043.webp)


👉 Nhập cụm từ khôi phục 12 từ của bạn và nhấn **OK**.


![input_12_words](assets/en/044.webp)


wallet của bạn sẽ được khôi phục. Trong trường hợp này, chỉ số dư on-chain và Bitcoin của bạn sẽ được khôi phục.


Tuy nhiên, nếu bạn đang sử dụng kênh Lightning thông thường và khôi phục wallet chỉ bằng cụm từ khôi phục, kênh Lightning của bạn sẽ bị buộc đóng và mọi số dư Bitcoin bạn có trên đó sẽ tự động được chuyển sang số dư on-chain của bạn.


Cách khác để khôi phục Valet wallet của bạn, đặc biệt nếu bạn đã mở một kênh Lightning thông thường trước khi gỡ cài đặt Valet, là **sử dụng tệp sao lưu cục bộ đã lưu trên thiết bị của bạn, cùng với cụm từ 12 từ seed**. Nếu bạn sử dụng hai thứ này, trạng thái kênh Lightning của bạn sẽ được khôi phục, do đó kênh Lightning của bạn sẽ không bị buộc đóng.


Dưới đây là các bước:


👉 Cài đặt ứng dụng Valet mới và khởi chạy ứng dụng.


👉 Chọn **Khôi phục Wallet hiện có**.


👉 Chọn **Cụm từ Sao lưu + Khôi phục**.


![select_backup_and_recovery_seed](assets/en/045.webp)


👉 Chọn tệp sao lưu từ trình quản lý tệp của điện thoại. (Theo mặc định, tệp này luôn được lưu trong thư mục **Tải xuống**.)


![local_backup_file_in_download_folder](assets/en/046.webp)


Sau khi chọn đúng tệp sao lưu, một thông báo xác nhận rằng **"Tệp sao lưu đã có"** sẽ hiển thị, và sau đó hệ thống sẽ yêu cầu bạn nhập cụm từ seed gồm 12 từ.


![enter_12_words](assets/en/047.webp)


👉 Nhập cụm từ khôi phục 12 từ của bạn và nhấn **OK**. Bạn sẽ được chuyển đến trang chủ wallet.


👉 Chờ quá trình đồng bộ mạng Bitcoin (**SYNC**) và đồng bộ nút Lightning (**LN Sync**) hoàn tất, sau đó wallet của bạn sẽ được khôi phục hoàn toàn, bao gồm cả các kênh Lightning.


![LN_sync](assets/en/048.webp)


## Phần kết luận


Valet là một giải pháp wallet đầy thú vị, với các tính năng phù hợp cho việc hướng dẫn người dùng mới. Nó cũng có kênh Fiat, một công nghệ không quá mới mẻ, đảm bảo sự tích hợp các doanh nghiệp vận hành bằng tiền pháp định trên tiêu chuẩn Bitcoin.


Tải Valet ngay hôm nay và dùng thử nhé!!! 🧡