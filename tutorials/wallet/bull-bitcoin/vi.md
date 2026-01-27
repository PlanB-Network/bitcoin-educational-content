---
name: Bull Bitcoin Wallet
description: Tìm hiểu cách sử dụng Wallet Bull Bitcoin
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=6b0xTB2sE8E)


*Video hướng dẫn này từ BTC Sessions sẽ hướng dẫn bạn từng bước thiết lập và sử dụng Bull Bitcoin Wallet!*


Hướng dẫn này sẽ hướng dẫn bạn qua quá trình cài đặt, cấu hình và sử dụng Bull Bitcoin Wallet. Bạn sẽ học cách gửi và nhận tiền trên các mạng Bitcoin, On-Chain, Liquid và Lightning, cũng như cách di chuyển Bitcoin giữa các mạng này. Các tính năng mở rộng của wallet biến nó thành một công cụ mạnh mẽ, đa năng để quản lý Bitcoin của bạn. Hãy bắt đầu nào.


## Giới thiệu


Bull Bitcoin Wallet, được phát triển bởi [Bull Bitcoin](https://www.bullbitcoin.com/), là một Bitcoin wallet **tự quản lý**, có nghĩa là bạn có toàn quyền kiểm soát khóa riêng tư và do đó là tiền của mình, mà không cần phụ thuộc vào bên thứ ba. Mã nguồn mở và dựa trên triết lý Cypherpunk, Wallet này kết hợp sự đơn giản, bảo mật và các tính năng nâng cao như hoán đổi mạng chéo và hỗ trợ PayJoin. Nó cho phép bạn quản lý bitcoin của mình trên ba mạng: **Bitcoin onchain**, **Liquid** và **Lightning**, mỗi mạng được thiết kế riêng cho các mục đích sử dụng cụ thể. Trên [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49), bạn có thể xem các chủ đề hiện tại và các phát triển sắp tới. Vì dự án là mã nguồn mở 100% và "được xây dựng công khai", bạn cũng có thể gửi đề xuất và bất kỳ lỗi nào bạn gặp phải. Mặc dù một số ví điện tử hiện nay hỗ trợ nhiều mạng khác nhau, Bull Bitcoin Wallet nổi bật nhờ tích hợp sâu các tính năng bảo mật trên tất cả các mạng, biến nó thành một công cụ mạnh mẽ để quản lý Bitcoin của bạn trên tất cả các mạng chính.


## 1️⃣ Điều kiện tiên quyết


Trước khi bắt đầu sử dụng **Bull Bitcoin Wallet**, hãy đảm bảo bạn có những vật dụng sau:



- Điện thoại thông minh tương thích**: Thiết bị **iOS** (iPhone hoặc iPad) hoặc **Android**
- Kết nối Internet
- Phương tiện sao lưu an toàn**: Viết cụm từ khôi phục của bạn (12 từ) ra giấy hoặc kim loại và cất giữ ở nơi an toàn.
- Kiến thức cơ bản**: Hiểu biết tối thiểu về các khái niệm Bitcoin (địa chỉ, giao dịch, phí) là hữu ích, mặc dù hướng dẫn này giải thích từng bước cho người mới bắt đầu.


## 2️⃣ Lắp đặt


Bạn có thể cài đặt ứng dụng thông qua:



- [Apple App Store](https://apps.apple.com/app/bull-bitcoin/id6743380972)[ ](https://apps.apple.com/us/app/bitchat-mesh/id6748219622)(dành cho thiết bị iOS)
- [Google Play Store](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&hl=en) (dành cho thiết bị Android)


Người dùng Android cũng có những lựa chọn thay thế khác:



- Tải xuống APK trực tiếp từ trang [GitHub Releases](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) hoặc
- Cài đặt thông qua [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqtxxmmd9e382mrvvf5hgcm0d9hzumt0vf5kcegnah0ap) tương thích với Nostr


Sau khi cài đặt ứng dụng, hãy làm theo hướng dẫn trên màn hình chào mừng để cấu hình tài khoản của bạn.


## 3️⃣ Cấu hình ban đầu


Khi mở ứng dụng, bạn sẽ được nhắc chọn các tùy chọn sau:



- `Tạo Wallet mới`
- `Khôi phục Wallet` và
- Tùy chọn nâng cao


Chúng ta hãy bắt đầu bằng cách nhấn vào "Tùy chọn nâng cao".


Tại đây, chúng ta có thể cấu hình các cài đặt nâng cao trước khi tạo hoặc khôi phục wallet:


1. Kích hoạt `Tor proxy` để định tuyến lưu lượng truy cập qua mạng Tor.

1. Ứng dụng [Orbot](https://orbot.app/en/) cần được cài đặt và chạy trước khi kích hoạt.

2. Tor Proxy chỉ áp dụng cho Bitcoin (không áp dụng cho Liquid) và có thể dẫn đến kết nối chậm hơn.

2. Thiết lập `Electrum Server tùy chỉnh`, hoặc

3. Điều chỉnh cài đặt của `Recover Bull`. Chúng ta sẽ tìm hiểu thêm về [Recover Bull](https://recoverbull.com/) sau.


Sau khi thực hiện tất cả các điều chỉnh tùy chọn, hãy nhấn `Xong`. Nếu bạn muốn sử dụng lại Wallet hiện có, hãy nhấp vào `Khôi phục Wallet` và điền 12 từ của cụm từ khôi phục của bạn.


Nếu không, hãy nhấp vào `Tạo Wallet mới`.


![image](assets/en/01.webp)


## 4️⃣ Màn hình chính


Trước khi đi sâu hơn, hãy cùng xem qua "Màn hình chính" để làm quen:



- Menu "Tổng quan giao dịch" và "Menu cài đặt" nằm ở phía trên cùng.
- Mục "Số dư khả dụng" có tùy chọn bảo mật có thể được "bật hoặc tắt".
- Truy cập `Bitcoin Bull Exchange` để `Mua, Bán hoặc Thanh toán` (tùy thuộc vào khu vực pháp lý và có thể yêu cầu xác minh danh tính khách hàng).
- Chuyển tiền giữa các ví
- `Secure Bitcoin` tương đương với Onchain Bitcoin Wallet
- Thanh toán tức thì qua Lightning- / Liquid Network *(Lưu ý: Bull Bitcoin Wallet cho phép thực hiện và nhận thanh toán qua Lightning. Tiền nhận được qua Lightning được lưu trữ trên mạng [*Liquid](https://liquid.net/) (trong Wallet Thanh toán tức thì) nhờ vào việc hoán đổi tự động qua sàn giao dịch [*Boltz](https://boltz.exchange/). Điều này cho phép bạn tương tác với Lightning mà không cần phải quản lý các kênh thanh khoản, đồng thời vẫn tự quản lý tài sản của mình.)*
- Gửi và nhận tiền


![image](assets/en/02.webp)


Trước tiên, hãy thực hiện một số cấu hình quan trọng và bắt đầu với mục `Sao lưu`.


## 5️⃣ Sao lưu


Để bắt đầu quá trình sao lưu, hãy nhấn vào biểu tượng bánh răng (⚙) ở góc trên bên phải ứng dụng và chọn `Sao lưu Wallet`. Bạn sẽ được cung cấp hai phương pháp để bảo mật wallet của mình: `Kho lưu trữ mã hóa` và `Sao lưu vật lý`. Chúng ta hãy cùng tìm hiểu từng phương pháp.


![image](assets/en/03.webp)


### Sao lưu vật lý


Nhấn vào `Sao lưu vật lý` để xem danh sách 12 từ đại diện cho cụm từ khôi phục hoặc cụm từ seed của bạn. Vui lòng xem xét những điều sau:



- Hãy ghi lại cụm từ khôi phục của bạn một cách cẩn thận nhất. Viết nó ra giấy hoặc kim loại và cất giữ ở nơi an toàn (két sắt, nơi không có kết nối internet). Cụm từ này là phương tiện duy nhất để bạn truy cập vào bitcoin của mình trong trường hợp mất thiết bị hoặc xóa ứng dụng.
- Điều quan trọng cần lưu ý là bất kỳ ai có cụm từ này đều có thể đánh cắp toàn bộ bitcoin của bạn. Tuyệt đối không lưu trữ nó dưới dạng kỹ thuật số:
- Không có ảnh chụp màn hình
- Không có bản sao lưu đám mây, email hoặc tin nhắn.
- Không được sao chép/dán (có nguy cơ lưu vào clipboard)


![image](assets/en/25.webp)


Màn hình tiếp theo sẽ yêu cầu bạn sắp xếp các từ theo đúng thứ tự để đảm bảo bạn đã nhận diện chính xác cụm từ seed. Bạn sẽ nhận được thông báo xác nhận khi bài kiểm tra hoàn tất và thành công.


! **Điểm này rất quan trọng**. Để được hỗ trợ thêm:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### Kho lưu trữ được mã hóa


Ngoài ra còn có tùy chọn sao lưu ẩn danh được mã hóa trên đám mây. Nhưng chẳng phải chúng ta đã đề cập ở đoạn trước rằng sao lưu đám mây tiềm ẩn rủi ro và nên tránh sao? Tuy nhiên, nhóm Bull Bitcoin đã phát triển một cách thông minh để làm cho quá trình này an toàn hơn. Đây là cách nó hoạt động:


`Recoverbull` là một giao thức sao lưu giúp đơn giản hóa việc bảo mật thiết bị Bitcoin hoặc wallet của bạn bằng cách chia bản sao lưu thành hai phần. Đầu tiên, tệp sao lưu wallet của bạn được mã hóa trên thiết bị bằng khóa mã hóa mạnh. Bạn có thể lưu tệp đã mã hóa này ở bất cứ đâu bạn muốn, chẳng hạn như Google Drive hoặc thiết bị của bạn. Thứ hai, khóa mã hóa cần thiết để mở khóa tệp được lưu trữ bởi Máy chủ Khóa Recoverbull. Để khôi phục wallet của bạn, bạn cần cả tệp sao lưu đã mã hóa và khóa, mà bạn truy cập bằng mã PIN hoặc mật khẩu của mình. Thiết kế này đảm bảo rằng chỉ riêng bản sao lưu đám mây của bạn là vô dụng và máy chủ khóa cũng vô dụng nếu không có tệp sao lưu cụ thể của bạn. Điều này giúp giữ an toàn cho tiền của bạn ngay cả khi một phần bị xâm phạm.


Hãy tưởng tượng nó giống như một két sắt. Tệp sao lưu được mã hóa là *chiếc hộp*, bạn có thể lưu trữ nó ở bất cứ đâu (như Google Drive). Mã PIN khôi phục của bạn là *chìa khóa*, được lưu trữ riêng biệt bởi Máy chủ Khóa Recoverbull. Kẻ trộm sẽ cần cả chiếc hộp cụ thể và chìa khóa cụ thể của bạn để mở nó. Thiết kế này đảm bảo rằng ngay cả khi ai đó có được tệp sao lưu của bạn, nó cũng vô dụng nếu không có chìa khóa từ máy chủ, và chìa khóa của máy chủ cũng vô dụng nếu không có tệp sao lưu duy nhất của bạn.


Tìm hiểu thêm về giao thức sao lưu wallet của `Recoverbull` [tại đây](https://recoverbull.com/).


Nhấn vào `Kho lưu trữ được mã hóa` rồi nhấn `Tiếp tục` để xác nhận sử dụng Máy chủ mặc định. Kết nối sẽ được định tuyến qua Mạng `Tor` để đảm bảo quyền riêng tư và tính ẩn danh.


**Hiểu rõ mã PIN của bạn**



- Mã PIN mở khóa ứng dụng: Mã PIN tùy chọn được thiết lập trong Cài đặt > Mã PIN bảo mật để khóa ứng dụng trên điện thoại của bạn.
- Mã PIN khôi phục: Mã PIN bắt buộc được tạo trong quá trình sao lưu "Kho lưu trữ mã hóa", được sử dụng để giải mã tệp sao lưu của bạn trong quá trình khôi phục.


Đây là hai mã PIN riêng biệt. Đừng quên mã PIN khôi phục của bạn, vì nó rất cần thiết để khôi phục wallet của bạn."


**Thiết lập mã PIN khôi phục:**



- Bạn cần tạo mã PIN hoặc mật khẩu để khôi phục quyền truy cập vào wallet của mình.
- Mã PIN/Mật khẩu phải có ít nhất 6 chữ số (ví dụ: tránh các dãy số đơn giản như 123456, vì chúng không được chấp nhận).
- Nếu không có mã PIN này, việc khôi phục wallet là không thể.


Tiếp theo, hãy chọn nhà cung cấp kho lưu trữ:



- `Google Drive` hoặc
- một `vị trí tùy chỉnh` (ví dụ: thiết bị của bạn)


![image](assets/en/04.webp)


Bây giờ, hãy lưu tệp sao lưu. Tiếp theo, nhấn vào "Kiểm tra khôi phục", chọn tệp sao lưu hoặc kho dữ liệu đã lưu của bạn, rồi nhấn vào "Giải mã kho dữ liệu". Nhập mã PIN hoặc mật khẩu của bạn. Nếu mọi thứ hoạt động bình thường, màn hình "Kiểm tra hoàn tất thành công" sẽ xuất hiện.


### Nhãn nhập/xuất khẩu


Giờ chúng ta đã tạo bản sao lưu, hãy cùng xem xét mục `Nhãn`. Bull Bitcoin và wallet tăng cường tính bảo mật và khả năng tổ chức bằng cách cho phép người dùng tạo nhãn tùy chỉnh cho địa chỉ nhận và giao dịch của họ. Những nhãn này giúp bạn phân loại tiền của mình, vì các giao dịch được gửi đến địa chỉ có nhãn sẽ kế thừa nhãn đó, và bạn cũng có thể gắn nhãn cho các giao dịch gửi đi để theo dõi tiền thừa. wallet hỗ trợ đầy đủ tiêu chuẩn [BIP-329](https://bip329.org/), có nghĩa là bạn có thể xuất tất cả các nhãn của mình ra một tệp và nhập chúng vào một wallet khác. Tính năng này đảm bảo bạn có thể sao lưu lịch sử giao dịch và phân loại một cách liền mạch, hoặc di chuyển chúng giữa các phiên bản wallet khác nhau mà không làm mất đi khả năng tổ chức cá nhân hóa của mình.


![image](assets/en/05.webp)


## 6️⃣ Cài đặt


Sau khi đã bảo mật bản sao lưu chính, hãy cùng khám phá các tính năng khác có sẵn trong phần cài đặt.


### A - Bảo mật quyền truy cập


Để bảo mật ứng dụng, hãy vào "Cài đặt" và chọn "Mã PIN bảo mật" để chọn Mã PIN. Tạo một mã PIN mạnh để khóa quyền truy cập vào wallet của bạn. Mặc dù bước này là tùy chọn, nhưng rất nên thực hiện để ngăn chặn truy cập trái phép nếu người khác sử dụng điện thoại của bạn.


![image](assets/en/06.webp)


### B - Kết nối với một nút cá nhân (tùy chọn)


Wallet BullBitcoin mặc định kết nối với các máy chủ Electrum: máy chủ đầu tiên do Bull Bitcoin quản lý và máy chủ thứ hai từ Blockstream, cả hai đều được cho là không lưu nhật ký, giảm thiểu rủi ro bị theo dõi.


Để tăng cường tính bảo mật, bạn có thể kết nối ứng dụng với nút Bitcoin của riêng mình thông qua máy chủ Electrum. Để thực hiện việc này, hãy nhấn vào `Cài đặt` > `Cài đặt Bitcoin` > `Cài đặt Electrum Server`, sau đó nhấn vào `+ Thêm máy chủ tùy chỉnh` để nhập địa chỉ và thông tin đăng nhập của máy chủ.


![image](assets/en/07.webp)


### C - Tiền tệ


Số dư khả dụng được hiển thị trên màn hình chính bằng cả `sats` và `USD`. Để thay đổi, hãy vào `Cài đặt` > `Tiền tệ`. Tại đó, bạn có thể chuyển đổi giữa `sats/BTC` và chọn `đơn vị tiền tệ mặc định` của mình.


![image](assets/en/08.webp)


### D - Cài đặt Bitcoin


Menu `Cài đặt Bitcoin` cung cấp quyền truy cập sâu vào các cấu hình và dữ liệu cốt lõi của wallet. Tại đây, bạn có thể kiểm tra các chi tiết cơ bản của ví `Bitcoin Bảo mật` và `Ví Thanh toán tức thì`, mang lại cho bạn sự minh bạch và quyền kiểm soát hoàn toàn. Các tính năng chính trong menu này bao gồm:



- Chi tiết Wallet:** Hãy truy cập vào Bitcoin Bảo mật hoặc wallet Thanh toán tức thì để xem thông tin cụ thể.
- Dấu vân tay Wallet:** Mã định danh duy nhất cho thiết bị wallet của bạn.
- Khóa công khai (Pubkey):** Khóa được sử dụng để xác thực địa chỉ nhận generate của bạn.
- Descriptor:** Bản tóm tắt kỹ thuật về cấu trúc của wallet.
- Đường dẫn dẫn xuất:** Đường dẫn cụ thể được sử dụng để chuyển đổi tất cả địa chỉ từ khóa riêng chính của bạn sang generate.
- Address View:** Truy cập danh sách các địa chỉ nhận thư chưa sử dụng và thay đổi địa chỉ (sắp ra mắt)


Ngoài ra, bạn còn có các lựa chọn sau:



- Cài đặt "Bật chuyển khoản tự động" để thiết lập số dư wallet tức thời tối đa, sau đó số dư này sẽ được tự động chuyển sang wallet Bitcoin an toàn.
- Nhập ví Generic thông qua cụm từ `Mnemonic` hoặc nhập `watch-only`.
- Kết nối ví phần cứng: các thiết bị hiện được hỗ trợ là ColdcardQ, SeedSigner, Specter, Krux, Blockstream Jade và Foundation Passport.


## 7️⃣ Bull Bitcoin Exchange


Trực tiếp từ wallet, bạn có thể truy cập vào [sàn giao dịch Bull Bitcoin](https://www.bullbitcoin.com/), cho phép bạn mua, bán và thanh toán Bitcoin mà không cần rời khỏi ứng dụng. Sự tích hợp này cung cấp một giải pháp thuận tiện để quản lý nhu cầu Bitcoin của bạn. Xin lưu ý rằng việc truy cập vào sàn giao dịch và các dịch vụ của nó có thể bị hạn chế tùy thuộc vào khu vực pháp lý của bạn, và việc hoàn tất xác minh Biết Khách hàng của Bạn (KYC) có thể được yêu cầu để tuân thủ các tiêu chuẩn quy định và sử dụng đầy đủ các tính năng của nền tảng.


Để bắt đầu, hãy nhấn vào `Exchange` ở góc dưới bên phải, sau đó nhấn `Đăng ký` hoặc `Đăng nhập` vào tài khoản của bạn.


Sàn giao dịch này cung cấp các [tính năng](https://www.bullbitcoin.com/) sau đây:



- Mua Bitcoin bằng hình thức tự quản lý từ tài khoản ngân hàng của bạn
- Không giam giữ
- Cá nhân hoặc tập đoàn
- Rút tiền tức thì
- Không có phí ẩn
- Lightning Network có sẵn
- Không giới hạn giao dịch
- Tùy chọn mua định kỳ


![image](assets/en/09.webp)


Để tìm hiểu thêm, vui lòng xem hướng dẫn này:


https://planb.academy/en/tutorials/exchange/centralized/bull-bitcoin-europe-0ccf713e-efcd-44ec-8205-211f49ac7d53

## 8️⃣ Nhận tiền


Việc nhận tiền với **Bull Bitcoin Wallet** rất đơn giản và linh hoạt, hỗ trợ ba mạng lưới riêng biệt được thiết kế cho các trường hợp sử dụng khác nhau:



- Mạng lưới `Bitcoin (onchain)` dành cho lưu trữ an toàn, dài hạn.
- Mạng lưới `Liquid` dành cho các giao dịch nhanh chóng và bảo mật hơn.
- Mạng lưới "Lightning" cho phép thanh toán tức thời với chi phí thấp.


Ứng dụng sẽ tự động tạo địa chỉ hoặc hóa đơn phù hợp dựa trên mạng di động bạn đã chọn. Dưới đây là hướng dẫn cách thực hiện cho từng mạng.


### Nhận tiền qua Onchain (mạng Bitcoin)


Để nhận tiền on-chain, bạn có thể chọn `Secure Bitcoin Wallet` từ màn hình chính và nhấn `Nhận`, hoặc nhấn vào nút `Nhận` chính rồi chọn `mạng Bitcoin`.


Bạn có hai chế độ chính để tạo địa chỉ nhận:


**Chế độ mặc định (URI với các tham số đầu vào bổ sung)**


Theo mặc định, wallet tạo ra một [URI BIP21](https://bips.dev/21/). Đây là định dạng tiêu chuẩn chứa nhiều thông tin hơn một địa chỉ đơn giản, bao gồm số tiền, ghi chú cá nhân và các tham số PayJoin để tăng cường quyền riêng tư. URI toàn diện này được mã hóa thành mã QR và có thể sao chép. Định dạng trông như sau: `bitcoin:<địa chỉ>?<tham số1>=<giá trị1>&<tham số2>=<giá trị2>`.



- Các tham số đầu vào bổ sung:**
    - Số lượng:** Vui lòng chỉ định số lượng yêu cầu bằng BTC, sats hoặc tiền tệ pháp định.
    - Tin nhắn:** Thêm lời nhắn cá nhân mà người gửi chỉ nhìn thấy.
    - PayJoin:** Hãy bật tùy chọn này để cải thiện quyền riêng tư bằng cách kết hợp thông tin đầu vào từ cả người gửi và người nhận trong giao dịch.


Ví dụ về URI:


```
bitcoin:bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54xxxxx?amount=0.0005&message=Tip+for+tutorial&pj=HTTPS%3A%2F%2FPAYJO.IN%2F78UH9WZUP8KKJ%23RK1Q2H30FASCU9WW09DQY2LK0K8P2DPRJ99V72CA78ACQAEL675QYTMQ+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1L0LYV6G
```


*Lưu ý quan trọng: Vui lòng không gửi bất kỳ khoản tiền nào đến các địa chỉ trong hướng dẫn này, tài khoản wallet sẽ bị xóa.*


![image](assets/en/10.webp)


**Chỉ tùy chọn sao chép hoặc quét Address được kích hoạt**


Khi tùy chọn `Chỉ sao chép hoặc quét Address` được bật, ứng dụng sẽ tạo ra một địa chỉ Bitcoin đơn giản ở định dạng SegWit (bech32).


Ví dụ:


```javascript
bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54x3g56
```


Ngay cả khi bạn nhập số tiền hoặc ghi chú, chúng cũng sẽ không được bao gồm trong mã QR hoặc địa chỉ đã sao chép.


![image](assets/en/11.webp)


### Nhận tín hiệu qua Liquid Network


Bạn có thể nhận thanh toán trên Liquid Network. Khi ở màn hình `Nhận`, bạn có hai tùy chọn tương tự để tạo yêu cầu thanh toán:


**1. Address đơn giản:** Sao chép địa chỉ `Liquid` tiêu chuẩn. Đây là mã định danh duy nhất cho wallet của bạn trên mạng Liquid và không bao gồm bất kỳ số tiền hoặc thông điệp cụ thể nào.


Ví dụ Address:


```javascript
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7xxxxxxx
```


**2. Yêu cầu thanh toán chi tiết (URI):** Để yêu cầu được cấu trúc rõ ràng hơn, bạn có thể chỉ định số tiền và ghi chú cá nhân. Thông tin này sẽ tự động được mã hóa thành một URI có thể chia sẻ và mã QR tương ứng.



- Số lượng:** Bạn có thể thiết lập số lượng bằng Bitcoin (BTC), Satoshi (Sats) hoặc một loại tiền tệ pháp định.
- Lưu ý: **Thêm lời nhắn cá nhân để xác định giao dịch.**


**Ví dụ về URI:**


```javascript
liquidnetwork:lq1qqdhgs7w537nun55a5sdy4gxkd08pclk3d7v4qz36sy4xp0cq6gvl52fcfv7kdgkgzmfycrud0zsygqgyjclycckpasxxxxxx?amount=0.00001&message=Test&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```


Để hoàn tất giao dịch, hãy cung cấp cho người gửi địa chỉ hoặc URL. Bạn có thể làm điều này bằng cách sao chép vào clipboard hoặc yêu cầu họ quét mã QR trực tiếp từ màn hình của bạn.


![image](assets/en/12.webp)


### Nhận qua Lightning



Bull Bitcoin Wallet cũng cho phép bạn gửi và nhận thanh toán thông qua Lightning Network. Một tính năng quan trọng là tiền nhận được qua Lightning sẽ tự động được hoán đổi và lưu trữ trên `Liquid Network` trong `Thanh toán tức thì Wallet` của bạn. Dịch vụ này được hỗ trợ bởi `Boltz`. Thiết kế này cho phép bạn tận hưởng tốc độ và chi phí thấp của Lightning mà không cần phải quản lý các kênh thanh khoản phức tạp, đồng thời vẫn duy trì quyền tự quản hoàn toàn đối với tiền của mình. Mặc dù phương pháp lai này mang tính tự quản và tránh được sự phức tạp trong việc quản lý các kênh, nhưng nó lại giới thiệu một dịch vụ của bên thứ ba (Boltz), một khoản phí hoán đổi nhỏ và sự phụ thuộc vào liên kết các chức năng của Liquid Network với tư cách là người giữ khóa, điều này khác với Lightning wallet truyền thống, không tự quản lý tiền của bạn. Bạn có thể tìm hiểu thêm về Liquid và mô hình quản trị của nó tại đây:


https://planb.academy/en/courses/e17ee350-41d4-49fa-b270-29e4d26d22f8/overview-of-liquid-architecture-and-governance-model-17650c4b-cd1f-4bc6-b490-708f92dc9306


- Giới hạn:**
    - Số tiền tối thiểu:** Cần có số tiền tối thiểu trên hóa đơn. Vui lòng kiểm tra ứng dụng để biết giới hạn hiện tại.
    - Phí:** Người nhận sẽ chịu một khoản phí chuyển đổi nhỏ. Phí này sẽ được trừ vào số tiền người gửi chuyển và có thể thay đổi.
- Những lợi ích:**
    - Tự quản lý:** Tiền của bạn luôn nằm dưới sự kiểm soát của bạn, được bảo mật trên mạng Liquid.
    - Tránh phí On-Chain cao:** Bằng cách sử dụng Lightning và lưu trữ trên Liquid, bạn sẽ tránh được phí on-chain liên quan đến việc mở kênh Lightning truyền thống. Bạn có thể chọn chuyển tiền sang kênh on-chain sau này, khi số tiền tích lũy đủ lớn để bù đắp chi phí.
    - Mẹo: Để thực hiện giao dịch tiết kiệm chi phí nhất giữa hai người dùng Bull Bitcoin, hãy sử dụng trực tiếp mạng Liquid để tránh hoàn toàn phí chuyển đổi Lightning.


Để nhận thanh toán, bạn phải sử dụng generate để tạo `hóa đơn Lightning`:


1. `Nhập số tiền`: Chỉ định số tiền bạn muốn nhận bằng Bitcoin (BTC), Satoshi (Sats) hoặc một loại tiền tệ pháp định.

2. `Thêm ghi chú` **(Tùy chọn):** Thêm một ghi chú. Ghi chú này sẽ được nhúng vào hóa đơn và hiển thị trong lịch sử giao dịch của bạn sau khi thanh toán hoàn tất, giúp bạn dễ dàng nhận biết hơn.

3. `Hiệu lực của Invoice`: Hóa đơn Lightning có thời hạn và hết hạn sau **12 giờ**. Nếu không được thanh toán trong khoảng thời gian này, hóa đơn sẽ trở nên không hợp lệ và bạn sẽ cần sử dụng generate để tạo hóa đơn mới.


Hãy cung cấp hóa đơn cho người gửi bằng cách sao chép vào clipboard hoặc cho phép họ quét mã QR hiển thị trên màn hình của bạn.


![image](assets/en/13.webp)


## 9️⃣ Chuyển tiền


Bạn có thể truy cập màn hình gửi trực tiếp từ trang chủ hoặc từ bất kỳ ví nào của mình. Bull Bitcoin Wallet đơn giản hóa quy trình bằng cách tự động phát hiện mạng đích—`Bitcoin`, `Liquid` hoặc `Lightning`—dựa trên địa chỉ hoặc hóa đơn bạn nhập, cho dù được dán hay quét qua mã QR.


### Truyền tín hiệu On-Chain qua mạng Bitcoin


Việc gửi tiền qua on-chain có nghĩa là giao dịch của bạn được ghi lại trực tiếp trên chuỗi khối Bitcoin. Phương pháp này phù hợp nhất cho các giao dịch chuyển tiền lớn hoặc các giao dịch không cần gấp. Để bắt đầu, bạn có thể nhấn vào nút "Gửi" ở góc dưới bên phải, sau đó quét hoặc nhập địa chỉ Bitcoin tiêu chuẩn.


Nếu địa chỉ bạn cung cấp không bao gồm số tiền cụ thể, bạn sẽ được yêu cầu điền thông tin chi tiết trên màn hình gửi. Bạn có thể chỉ định số tiền bằng đơn vị ưa thích của mình, chẳng hạn như BTC, satoshi hoặc tiền tệ pháp định tương đương. Bạn cũng có tùy chọn thêm ghi chú cá nhân, là một ghi chú riêng tư để bạn tham khảo và giúp xác định giao dịch sau này. Ghi chú này sẽ không được chia sẻ với người nhận.


Ngược lại, nếu yêu cầu thanh toán mà bạn quét hoặc dán đã chứa tất cả các chi tiết cần thiết, chẳng hạn như URI BIP21 với số tiền được xác định trước, thì wallet sẽ bỏ qua màn hình nhập dữ liệu và đưa bạn trực tiếp đến màn hình xác nhận để ủy quyền thanh toán.


![image](assets/en/14.webp)


Trước khi giao dịch của bạn được thực hiện, bạn sẽ được hiển thị màn hình xác nhận. Điều quan trọng là hãy dành chút thời gian để xem xét kỹ lưỡng mọi thông số, chú ý đến địa chỉ người nhận, số tiền gửi và phí mạng. Màn hình này cũng cung cấp các công cụ mạnh mẽ để tùy chỉnh giao dịch của bạn.


Bạn có thể kiểm soát phí theo hai cách chính. Cách thứ nhất là chọn tốc độ giao dịch mong muốn, chẳng hạn như thấp, trung bình hoặc cao, và wallet sẽ tự động tính toán mức phí phù hợp cho bạn. Cách thứ hai cho phép kiểm soát chính xác hơn bằng cách cho phép bạn đặt một mức phí cụ thể, hoặc là tổng số tuyệt đối tính bằng satoshi hoặc là tỷ lệ tương đối trên mỗi byte, từ đó sẽ cung cấp thời gian xác nhận ước tính.


Đối với người dùng nâng cao, wallet cung cấp một số cài đặt để tinh chỉnh giao dịch. Chức năng `Thay thế bằng phí` (RBF) được bật theo mặc định, đây là một tính năng hữu ích cho phép bạn tăng tốc giao dịch nếu nó bị kẹt trong mempool bằng cách phát lại nó với mức phí cao hơn. Bạn cũng có thể chọn thủ công `Đầu ra giao dịch chưa sử dụng` (UTXO) để chi tiêu. Đây là một công cụ mạnh mẽ cho việc hợp nhất UTXO, một chiến lược kết hợp nhiều đầu vào nhỏ thành một đầu vào lớn hơn. Mặc dù điều này có thể tốn nhiều phí hơn cho giao dịch hiện tại, nhưng nó có thể giảm đáng kể phí cho các giao dịch trong tương lai, đặc biệt nếu dự kiến phí mạng sẽ tăng.


![image](assets/en/15.webp)


PayJoin được tự động thực hiện khi bạn quét yêu cầu thanh toán của người nhận (URI BIP21) có chứa tham số `pj=`. Nếu bạn chỉ dán một địa chỉ thông thường mà không có tham số bổ sung, tính năng này sẽ không được kích hoạt. Phương pháp hợp tác này tăng cường quyền riêng tư bằng cách kết hợp thông tin đầu vào từ cả người gửi và người nhận, phá vỡ quy tắc suy luận về quyền sở hữu đầu vào chung và cho phép mở rộng quy mô tốt hơn cũng như tiết kiệm phí trong một số trường hợp.


### Gửi tới Liquid Network


Thiết bị `Liquid Network` được thiết kế cho các giao dịch nhanh chóng, bảo mật với phí tối thiểu. Khi bạn gửi tiền qua Liquid, tiền sẽ được rút từ `Thanh toán tức thì Wallet` của bạn. Quy trình rất đơn giản: bạn chỉ cần nhập hoặc quét `địa chỉ Liquid` của người nhận.


Nếu địa chỉ không ghi rõ số tiền, bạn sẽ được yêu cầu nhập số tiền trên màn hình gửi. Bạn có thể nhập số tiền bằng BTC, satoshi hoặc tiền pháp định. Một ưu điểm chính của Liquid là ngưỡng tối thiểu thấp. Giống như các giao dịch on-chain, bạn có thể thêm ghi chú cá nhân tùy chọn để lưu lại. Nếu yêu cầu thanh toán đã bao gồm số tiền, wallet sẽ chuyển thẳng đến màn hình xác nhận.


Trên màn hình xác nhận giao dịch Liquid, bạn sẽ xem lại các chi tiết. Phí giao dịch khá thấp và được tính dựa trên độ phức tạp của giao dịch. Thông thường, phí chỉ khoảng 0,1 satoshi/vB, tương đương khoảng 20-40 satoshi cho một giao dịch đơn giản (ví dụ: 26 satoshi tính đến ngày 21 tháng 12 năm 2025).


![image](assets/en/16.webp)


### Gửi đến Lightning Network


Bạn có thể quét mã Lightning Address (ví dụ: `runningbitcoin@rizful.com`), cho phép bạn thiết lập số tiền và ghi chú tùy chọn cho người nhận, hoặc quét hóa đơn với số tiền đã được xác định trước, điều này sẽ đưa bạn trực tiếp đến màn hình xác nhận.


*Lưu ý rằng có áp dụng mức phí và số tiền tối thiểu.*


Bull Bitcoin Wallet gửi các khoản thanh toán Lightning bằng cách rút tiền từ `Thanh toán tức thì Wallet` của bạn (trên Liquid) và hoán đổi chúng thông qua `Boltz`. Phương pháp kết hợp này hoàn toàn tự quản lý và tránh được các khoản phí cao của on-chain khi quản lý một kênh Lightning chuyên dụng, nhưng nó yêu cầu phải trả `phí hoán đổi`. Để có chi phí thấp nhất, hãy gửi trực tiếp đến địa chỉ Liquid của người nhận nếu họ cũng sử dụng Bull Bitcoin hoặc wallet.


## 🔟 Chuyển tiền giữa các ví của bạn


Bull Bitcoin cho phép bạn chuyển Bitcoin giữa wallet (Bitcoin bảo mật) và Wallet (Bitcoin thanh toán tức thì) trên Liquid Network hoặc đến một Wallet bên ngoài. Để thực hiện chuyển khoản, chỉ cần điều hướng đến mục "Chuyển khoản", chọn ví nguồn và ví đích, nhập số tiền bạn muốn chuyển và xác nhận giao dịch.


![image](assets/en/17.webp)


## 1️⃣1️⃣ Khôi phục Bull Bitcoin Wallet của bạn


Phần này giải thích cách khôi phục quyền truy cập vào số tiền trong Bull Bitcoin Wallet nếu bạn làm mất thiết bị, gỡ cài đặt ứng dụng hoặc đơn giản là cần chuyển sang thiết bị mới. Như đã giải thích, có hai phương pháp chính để khôi phục: sử dụng phương pháp `Recoverbull` độc đáo và sử dụng cụm từ `BIP39 seed` tiêu chuẩn.


### Phương pháp 1: Recoverbull


Tóm tắt: Bản sao lưu Wallet được mã hóa cục bộ. Tệp đã mã hóa có thể được lưu trữ trên bộ nhớ đám mây hoặc trên thiết bị khác. Khóa mã hóa được lưu trữ bởi Recoverbull Key Server. Cả hai được giữ riêng biệt và phải được kết hợp để khôi phục wallet.


Đầu tiên, tôi sẽ xóa Wallet cùng toàn bộ số tiền trên đó và cài đặt lại wallet. Chúng ta sẽ quay lại màn hình "Chào mừng". Lần này, hãy chọn tùy chọn "Khôi phục Wallet". Sau đó, điều hướng đến phương pháp "Kho mã hóa", xác nhận sử dụng "Máy chủ khóa mặc định" và chọn vị trí hoặc "Nhà cung cấp kho" nơi bạn đã lưu trữ tệp sao lưu.


![image](assets/en/18.webp)


Thông báo cho biết kho tiền đã được nhập thành công. Nhấn vào nút "Giải mã kho tiền" và nhập mã PIN. Màn hình tiếp theo sẽ hiển thị số dư và số lượng giao dịch đã được khôi phục.


![image](assets/en/19.webp)


### Phương pháp 2: Cụm từ hạt giống


Phương pháp này sử dụng cụm từ khôi phục chính của wallet, một danh sách 12 từ tiêu chuẩn đóng vai trò là bản sao lưu tối ưu cho tiền của bạn. Đây là cách phổ biến nhất để khôi phục Bitcoin hoặc wallet, vì nó không bị ràng buộc với bất kỳ dịch vụ hoặc máy chủ cụ thể nào. Chỉ cần bạn có cụm từ này, bạn có thể khôi phục wallet của mình trên bất kỳ thiết bị tương thích nào, ngay cả khi không có quyền truy cập vào Máy chủ Khóa Bull Bitcoin.


Từ màn hình Chào mừng, chọn `Khôi phục Wallet`. Lần này, hãy chọn phương pháp `Sao lưu vật lý`. Ứng dụng sẽ hiển thị một lưới các từ. Hãy cẩn thận chọn từng từ trong cụm từ seed gồm 12 từ của bạn theo đúng thứ tự. Hãy tỉ mỉ, vì một lỗi nhỏ cũng sẽ dẫn đến wallet không chính xác.


## 1️⃣2️⃣ Kết nối Hardware Wallet


Để đảm bảo an ninh tối đa, nhiều người dùng Bitcoin chọn lưu trữ tiền của họ trong "kho lưu trữ ngoại tuyến". Điều này có nghĩa là giữ "khóa riêng" điều khiển Bitcoin của bạn trên một thiết bị không bao giờ kết nối với internet. "wallet phần cứng" (hoặc thiết bị ký) là một thiết bị vật lý chuyên dụng được thiết kế cho mục đích này. Nó hoạt động như một kho lưu trữ kỹ thuật số cho các khóa của bạn, đảm bảo chúng không bao giờ bị lộ trước các mối đe dọa tiềm tàng từ máy tính hoặc điện thoại thông minh trực tuyến.


Bằng cách kết nối thiết bị wallet phần cứng với ứng dụng Bull Bitcoin, bạn sẽ có được những lợi ích tốt nhất của cả hai: tính bảo mật tuyệt đối của lưu trữ ngoại tuyến cho khóa riêng tư của bạn, kết hợp với các tính năng mạnh mẽ và giao diện thân thiện với người dùng của Bull Bitcoin để xem số dư và quản lý giao dịch. Trong chương cuối này, chúng tôi sẽ hướng dẫn bạn cách kết nối thiết bị wallet phần cứng, chẳng hạn như [Coldcard Q](https://coldcard.com/q), với Bull Bitcoin của bạn. Hướng dẫn này sẽ không đi sâu vào thiết lập Coldcard Q; bạn có thể tìm hiểu thêm tại đây:


https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

### Nhập khẩu một chiếc Wallet


![image](assets/en/26.webp)


Đầu tiên, từ menu chính trên Coldcard Q của bạn, chọn `Export Wallet`, sau đó chọn `Bull Wallet`. Coldcard của bạn sẽ tạo mã QR generate.


![image](assets/en/20.webp)


Mở Bull Bitcoin Wallet và điều hướng đến `Cài đặt` > `Cài đặt Bitcoin` > `Nhập wallet` và chọn `Coldcard Q` trên điện thoại của bạn rồi nhấn `Mở camera` để quét mã QR này và nhập khóa công khai của thiết bị phần cứng wallet.


![image](assets/en/21.webp)


### Nhận hàng bằng Coldcard Q


Để nhận Bitcoin bằng Coldcard Q đã kết nối, bạn không cần thiết phải kết nối thiết bị vật lý với điện thoại. Bull Bitcoin Wallet đã nhập sẵn các khóa công khai cần thiết, cho phép nó tự động gửi đến các địa chỉ generate.


1. Chạm vào thiết bị ký Coldcard Q đã nhập của bạn và chọn `Nhận`.

2. Ứng dụng sẽ tự động hiển thị địa chỉ Bitcoin mới từ wallet của thẻ Coldcard của bạn.

3. Sử dụng địa chỉ này để nhận tiền. Bitcoin sẽ được bảo mật trực tiếp với các khóa của phần cứng wallet, ngay cả khi thiết bị ngoại tuyến trong quá trình này.


![image](assets/en/22.webp)


### Gửi thư bằng Coldcard Q


Việc gửi Bitcoin cùng với Coldcard Q của bạn yêu cầu xác nhận vật lý để ủy quyền bất kỳ giao dịch nào. Mặc dù ứng dụng Bull Wallet được sử dụng để tạo giao dịch, nhưng chữ ký cuối cùng chỉ có thể được tạo trên chính thiết bị phần cứng wallet.


Để bắt đầu, hãy mở ứng dụng `Coldcard Q` wallet và nhấn vào `Gửi`. Sau đó, `mở camera` để quét mã QR của địa chỉ người nhận. Sau khi quét, nhập `số tiền` bạn muốn gửi và điều chỉnh `ưu tiên phí` nếu cần.


Để có thêm tùy chọn, bạn có thể xem trong Cài đặt Nâng cao. Tại đây, bạn sẽ tìm thấy tùy chọn `Thay thế bằng Phí` (RBF), được kích hoạt theo mặc định và cho phép bạn tăng tốc giao dịch bị kẹt sau này. Bạn cũng có tùy chọn `Coin Control`, cho phép bạn chọn thủ công các UTXO cụ thể mà bạn muốn chi tiêu.


Sau khi xem xét kỹ tất cả các chi tiết, hãy nhấn vào `Show PSBT` để chuẩn bị giao dịch.


![image](assets/en/23.webp)


Nhấn vào nút "Quét" trên thẻ Coldcard Q và sử dụng camera của thẻ để quét mã QR hiển thị trên điện thoại của bạn. Màn hình Coldcard sẽ hiển thị tất cả chi tiết giao dịch. Kiểm tra kỹ số tiền, địa chỉ người nhận và địa chỉ nhận tiền thừa. Nếu mọi thứ đều chính xác, nhấn nút "Xác nhận" trên Coldcard Q để ký giao dịch. Tiếp theo, mã QR của giao dịch đã ký sẽ xuất hiện trên màn hình.


![image](assets/en/24.webp)


Trên thiết bị Bull wallet, chạm vào `Tôi đã xong`, sau đó chạm vào nút `Máy ảnh` để quét mã QR của `giao dịch đã ký` từ thẻ Coldcard Q của bạn. Thiết bị Bull Wallet sẽ hiển thị màn hình tóm tắt giao dịch đã ký. Xem lại lần cuối, sau đó chạm vào `Phát sóng` giao dịch. Thao tác này hoàn tất quá trình bằng cách gửi giao dịch đến mạng Bitcoin, và tiền của bạn sẽ được chuyển đi.


## 🎯 Kết luận


Bạn đã hoàn thành hành trình khám phá Bull Bitcoin Wallet. Ứng dụng này cung cấp cho bạn các công cụ bảo mật và riêng tư mạnh mẽ ngay trong tầm tay, giúp việc sử dụng các tính năng nâng cao trở nên đơn giản. Nó giúp bạn bảo mật thông tin cá nhân với các tính năng như `PayJoin`, giúp ẩn các giao dịch của bạn trên blockchain, và `tích hợp Tor`, giúp che giấu hoạt động mạng của bạn khỏi những con mắt tò mò. Đối với những người muốn kiểm soát tối đa, bạn có thể kết nối với `nút Bitcoin cá nhân` của riêng mình để không còn phụ thuộc vào máy chủ của bên thứ ba, và sử dụng `wallet phần cứng` để giữ các khóa riêng tư của bạn hoàn toàn ngoại tuyến và an toàn. Với các tùy chọn sao lưu thông minh và hỗ trợ liền mạch cho Bitcoin, Liquid và Lightning, Bull Bitcoin Wallet là một lựa chọn mạnh mẽ, toàn diện dành cho bất kỳ ai nghiêm túc muốn giữ cho tiền của mình được bảo mật, riêng tư và hoàn toàn nằm dưới sự kiểm soát của chính mình.


## 📚 Tài liệu Bull Wallet


[Github](https://github.com/SatoshiPortal/bullbitcoin-mobile) | [Trang web](https://www.bullbitcoin.com/)| [Recoverbull](https://recoverbull.com/)