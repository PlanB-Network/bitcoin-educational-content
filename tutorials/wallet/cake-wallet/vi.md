---
name: Bánh Wallet
description: Hướng dẫn về Cake Wallet và Thanh toán im lặng
---

![cover](assets/cover.webp)


Hướng dẫn này khám phá [**Cake Wallet**](https://cakewallet.com/): một wallet đa tiền tệ, mã nguồn mở, không lưu ký, tập trung vào quyền riêng tư, có sẵn cho Android, iOS, macOS, Linux và Windows. Chúng ta sẽ tìm hiểu sâu hơn về các tính năng riêng tư dành riêng cho Bitcoin, hướng dẫn gửi/nhận Bitcoin thông qua **Thanh toán Im lặng** (một giao thức riêng tư được cải tiến của on-chain) và sẽ xem xét việc triển khai PayJoin v2 cho các giao dịch bất đồng bộ.


## 🎉 Các tính năng chính



- [**Thanh toán Im lặng (BIP-352)**](https://bips.dev/352/) cải thiện [mã thanh toán BIP 47](https://silentpayments.xyz/docs/comparing-proposals/bip47/) trước đây, còn được gọi là "PayNyms" với các địa chỉ ẩn có thể tái sử dụng. Khi người gửi sử dụng địa chỉ Thanh toán Im lặng của bạn, wallet của họ sẽ tạo ra một địa chỉ dùng một lần duy nhất bằng cách sử dụng các khóa khác nhau, sau đó được kết hợp thành một địa chỉ Taproot dùng một lần duy nhất. Hồ sơ blockchain hiển thị các giao dịch không liên quan, ngăn chặn việc liên kết các khoản thanh toán đến. Thanh toán Im lặng mang lại một loạt lợi ích, bao gồm:
    - Địa chỉ có thể tái sử dụng: Không cần generate một địa chỉ mới cho mỗi giao dịch, mang lại trải nghiệm người dùng tốt hơn và tăng cường quyền riêng tư
    - Không tăng chi phí: Thanh toán im lặng không làm tăng quy mô hoặc chi phí của giao dịch.
    - Nâng cao tính ẩn danh: Người quan sát bên ngoài không thể liên kết các giao dịch với địa chỉ Thanh toán im lặng.
    - Không cần tương tác giữa người gửi và người nhận: Giao dịch có thể được thực hiện mà không cần bất kỳ sự giao tiếp nào giữa các bên.
    - Địa chỉ duy nhất cho mỗi khoản thanh toán: Loại bỏ nguy cơ sử dụng lại địa chỉ một cách vô tình.
    - Không cần máy chủ: Có thể thực hiện thanh toán im lặng mà không cần máy chủ chuyên dụng.
- PayJoin v2** giảm thiểu việc phân tích đồ thị giao dịch bằng cách hợp nhất dữ liệu đầu vào của bên gửi và bên nhận thành một giao dịch duy nhất. Cake Wallet triển khai hai cải tiến quan trọng:
    - Giao dịch không đồng bộ**: Người gửi và người nhận không cần phải trực tuyến cùng lúc để hoàn tất giao dịch riêng tư.
    - Giao tiếp không cần máy chủ**: Không bên nào cần phải chạy máy chủ Payjoin, loại bỏ rào cản kỹ thuật lớn.
- Coin Control** cho phép chọn UTXO thủ công trong quá trình giao dịch. Điều này ngăn ngừa việc liên kết địa chỉ ngẫu nhiên khi sử dụng nhiều UTXO có nguồn gốc khác nhau.
- Hỗ trợ TOR**, cho phép người dùng định tuyến lưu lượng mạng của họ thông qua mạng Tor
- RBF** (Replace-By.Fee) cho phép bạn điều chỉnh phí sau khi gửi giao dịch.


## 1️⃣ Thiết lập Wallet của bạn


Cake Wallet hỗ trợ nhiều nền tảng. Bạn có thể chọn giữa `Android`, `iOS / macOS`, `Linux` và `Windows`. Để bắt đầu, hãy truy cập https://docs.cakewallet.com/get-started/ và chọn hệ điều hành của bạn.


![image](assets/en/01.webp)


Sau khi cài đặt, hãy đặt `PIN` (4 hoặc 6 chữ số). Sau đó, bạn sẽ thấy:


1. `Tạo Wallet mới` (dành cho người dùng mới)

2. `Khôi phục Wallet` (cho ví hiện có)


![image](assets/en/02.webp)


Trên màn hình tiếp theo, bạn có thể chọn từ nhiều loại tiền điện tử. Chọn `Bitcoin`, nhấn `Tiếp theo` và nhập `tên Wallet` để xác định wallet. Bằng cách nhấn vào `Cài đặt Nâng cao`, một loạt `Cài đặt Quyền riêng tư` sẽ xuất hiện. Thực hiện các thay đổi sau:



- Fiat API:** chọn `Chỉ Tor` (định tuyến yêu cầu giá thông qua Tor)
- Hoán đổi:** chọn `Chỉ Tor` (ẩn danh lưu lượng trao đổi)


Kiểu BIP-39 seed được tạo theo mặc định, với tùy chọn chuyển sang kiểu Electrum seed. Các Đường Dẫn Xuất Phát như sau:



- Electrum: `m/0'`
- BIP-39: `m/84'/0'/0`


Nếu bạn muốn thêm một lớp bảo mật bổ sung, bạn có thể thiết lập `passphrase`. Mục đích chính của passphrase là cung cấp khả năng bảo vệ bổ sung chống lại các cuộc tấn công vật lý. Ngay cả khi kẻ tấn công tìm thấy cụm từ seed, chúng cũng không thể truy cập wallet của bạn nếu không có passphrase chính xác. Nói cách khác, cụm từ seed riêng lẻ đại diện cho một wallet, trong khi cụm từ seed cộng với passphrase tạo ra một wallet hoàn toàn khác, không liên quan gì đến bản gốc. Tính năng này cũng cho phép `ví bí mật` được bảo vệ bởi passphrase và cung cấp cho bạn khả năng phủ nhận hợp lý. Trong tình huống bị ép buộc, bạn có thể tiết lộ cụm từ seed trong khi vẫn giữ an toàn cho các tài sản lớn hơn trong wallet được bảo vệ bởi passphrase.


Nếu bạn đã chạy node riêng, hãy bật `Thêm Node Tùy chỉnh Mới` và cung cấp `Node Address` để xác thực giao dịch và khối trong cơ sở hạ tầng của bạn. Sau khi hoàn tất, hãy nhấn `Tiếp tục` và `Tiếp theo` để tạo wallet.


![image](assets/en/03.webp)


Ở màn hình tiếp theo, bạn sẽ thấy một thông báo miễn trừ trách nhiệm:


```
On the next page you will see a series of words. This is your unique and private seed and it is the ONLY way to recover your wallet in case of lass or malfunction. It is YOUR responsibility to write it down and store it in a safe place outside of the Cake Wallet app.
```


![image](assets/en/04.webp)


Để tìm hiểu cách thực hành tốt nhất để lưu cụm từ ghi nhớ của bạn, vui lòng tham khảo hướng dẫn này:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Nhấn vào `Tôi hiểu. Cho tôi xem seed của tôi` và lưu những từ này vào một nơi an toàn! Sau đó, nhấn `Xác minh seed` và sau khi xác minh, hãy nhấn `Mở Wallet`.


## 2️⃣ Cài đặt


Trước khi đi sâu hơn, chúng ta hãy xem qua `Màn hình chính` và `Cài đặt`.


Trên Màn hình chính, chúng ta có thể thấy các mục khác nhau được hiển thị:



- `Menu Hamburger` đưa chúng ta đến `cài đặt`
- Số dư khả dụng
- Thẻ Thanh toán Im lặng để Bắt đầu quét các giao dịch được gửi đến địa chỉ Thanh toán Im lặng của bạn
- Thẻ Payjoin sẽ `Kích hoạt` Payjoin như một tính năng bảo vệ quyền riêng tư và tiết kiệm phí
- ở phía dưới là các phím tắt đến `Tổng quan về Wallet`, `Nhận`, `Hoán đổi` giữa Bitcoin và các loại tiền tệ khác, `Gửi` và `Mua`


![image](assets/en/11.webp)


Nhấn vào biểu tượng `Menu Hamburger` để mở menu cài đặt. Hãy cùng xem qua các tùy chọn.


![image](assets/en/05.webp)


### A - Kết nối & đồng bộ hóa 🔗


Tại đây, chúng ta có thể kết nối lại wallet, quản lý các nút và kết nối với nút của riêng mình (khuyến nghị). `Quét Thanh toán Im lặng` cho phép chúng ta tùy chỉnh quét bằng cách chỉ định `Quét từ chiều cao khối` hoặc `Quét từ ngày`.


![image](assets/en/06.webp)


Là tính năng `Alpha`, cũng có tùy chọn `Kích hoạt Tor tích hợp` để định tuyến lưu lượng truy cập qua mạng Tor.


### B - Cài đặt Thanh toán im lặng 🔈


Chúng ta có thể bật thẻ Thanh toán Im lặng trên màn hình chính để hiển thị tính năng này. Việc bật `Luôn quét` cho phép wallet liên tục theo dõi blockchain để phát hiện các khoản Thanh toán Im lặng đến. Chúng ta có thể chỉ định các thông số quét để tùy chỉnh quy trình quét theo nhu cầu của mình như đã mô tả ở trên.


![image](assets/en/07.webp)


### C - Bảo mật & sao lưu 🗝️


Để bảo mật wallet, chúng ta có thể tạo bản sao lưu bằng cách làm theo hướng dẫn trong ứng dụng. Điều này sẽ đảm bảo chúng ta có một bản sao an toàn cho khóa riêng tư, cho phép chúng ta khôi phục wallet nếu bị mất hoặc bị đánh cắp. Ngoài ra, chúng ta có thể xem cụm từ seed và khóa riêng tư, thay đổi mã PIN, bật xác thực sinh trắc học, Ký/Xác minh và thiết lập 2FA để tăng cường bảo vệ.


![image](assets/en/08.webp)


**Lưu ý**: Kể từ tháng 9 năm 2025, xác thực sinh trắc học vân tay trên các thiết bị Android phải hoạt động với ít nhất một triển khai sinh trắc học Lớp 2. Để biết thêm chi tiết, hãy xem [tại đây](https://source.android.com/docs/security/features/biometric/measure#biometric-classes). Tuy nhiên, yêu cầu này có thể thay đổi trong tương lai.


### D - Cài đặt quyền riêng tư 🔒


Chúng ta cũng có thể tăng cường bảo mật cho wallet bằng cách sử dụng Tor để mã hóa kết nối internet và bảo vệ quyền riêng tư khi truy cập các nguồn bên ngoài. Ngoài ra, chúng ta có thể ngăn ảnh chụp màn hình để giữ bí mật thông tin wallet, bật tính năng tự động tạo địa chỉ mới cho mỗi giao dịch và vô hiệu hóa các hành động mua/bán để ngăn chặn các giao dịch trái phép. Ngoài ra, chúng ta có thể `Bật PayJoin`, một tính năng bảo mật khác mà chúng ta sẽ xem xét sau.


![image](assets/en/09.webp)


### E - Các thiết lập khác 🔧


Các cài đặt khác cho phép chúng tôi quản lý mức ưu tiên phí và đặt mức phí mặc định cho các giao dịch. Điều này cho phép chúng tôi kiểm soát phí giao dịch liên quan đến Thanh toán Im lặng, có tính đến mức sử dụng mạng hiện tại.


![image](assets/en/10.webp)


## 3️⃣ Nhận ₿itcoin bằng Thanh toán im lặng


Có một số tùy chọn và loại địa chỉ khả dụng để nhận Bitcoin. `Segwit (P2WPKH)` *(bắt đầu bằng bc1q....)* là tùy chọn mặc định. Trong ví dụ này, hãy chọn `Silent Payments`.


Để nhận Thanh toán Im lặng, trước tiên hãy chạm vào biểu tượng `Nhận` trên Cake Wallet. Tiếp theo, nhập số tiền bạn mong muốn nhận. Để chỉ định loại địa chỉ, hãy chạm lại vào `Nhận` ở đầu màn hình, sau đó chọn `Thanh toán Im lặng` từ các tùy chọn.


Trên màn hình chính, mã QR Thanh toán Im lặng và địa chỉ của bạn sẽ được hiển thị. Đúng như dự đoán, địa chỉ khá dài:


`sp1qq0ryu780uwragyk06prxn29830a9csnl3wvr4as6fwh73rzn28zzcqmc6ve36vadllfztaa403ty9et0rlzup7kt55qh486gxzrde6y27c8s6x5p` .


![image](assets/en/12.webp)


Bây giờ, hãy sử dụng wallet tương thích với BIP-352 (chẳng hạn như Blue Wallet) để quét mã QR này và gửi thanh toán. Bạn sẽ thấy wallet lấy một địa chỉ đích duy nhất từ địa chỉ im lặng của bạn.


![image](assets/en/13.webp)


## 4️⃣ Gửi ₿itcoin bằng Thanh toán im lặng


Vì Blue Wallet chỉ có thể `Gửi` Thanh toán Im lặng, chúng tôi sẽ sử dụng một wallet tương thích với BIP 352 khác làm bên nhận. Quy trình này giống hệt với giao dịch Bitcoin thông thường.



- Chạm vào `Gửi` trên Màn hình chính
- hoặc dán địa chỉ `sp1qq...` có thể sử dụng lại hoặc quét mã QR trực tiếp trong ứng dụng.
- Chọn số tiền bạn muốn chi tiêu từ số dư khả dụng của mình
- Chạm vào `Gửi` ở cuối màn hình để xác nhận giao dịch


Sau khi chúng ta nhập địa chỉ `sp1qq...`, wallet sẽ tự động lấy địa chỉ `bc1p...` tương ứng của Taproot (P2TR) ở chế độ nền, địa chỉ này sẽ được sử dụng cho Thanh toán im lặng.


Chúng tôi có thể tùy chọn viết ghi chú nội bộ cho mọi giao dịch, điều chỉnh cài đặt phí hoặc chọn UTXO nhất định cho giao dịch bằng tính năng `Coin Control`.


![image](assets/en/14.webp)


`Vuốt` sang phải để xác nhận giao dịch.


Sau khi bạn đã gửi giao dịch, bạn sẽ được hỏi xem bạn có muốn thêm địa chỉ liên hệ này vào sổ địa chỉ của mình hay không.


![image](assets/en/15.webp)


## 5️⃣ PayJoin


Hãy cùng xem lại PayJoin là gì [về](https://docs.cakewallet.com/cryptos/bitcoin/#payjoin):


_Payjoin v2 là một tính năng bảo vệ quyền riêng tư và tiết kiệm phí trong Bitcoin, cho phép người gửi và người nhận giao dịch cùng nhau tạo ra một giao dịch duy nhất. Giao dịch này nhận dữ liệu đầu vào từ cả người gửi và người nhận, phá vỡ các kỹ thuật giám sát phổ biến nhất đối với Bitcoin và cho phép mở rộng quy mô tốt hơn cũng như tiết kiệm phí trong một số trường hợp._


Để tìm hiểu thêm về PayJoin, bạn cũng có thể tham khảo hướng dẫn sau.


https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

Để sử dụng PayJoin, cả hai bên đều cần có máy wallet tương thích với PayJoin, và người nhận cần có ít nhất một đồng xu hoặc đầu ra trong máy wallet của họ. Để bắt đầu, vui lòng làm theo các bước sau:


1. Chạm vào `Menu Hamburger` và chạm vào nút `Quyền riêng tư`

2. Bật/tắt tùy chọn `Sử dụng Payjoin`

3. Chạm vào `Nhận` trên Màn hình chính và bạn sẽ thấy Mã QR PayJoin và nút sao chép (khi chọn Segwit)


![image](assets/en/16.webp)


## 6️⃣ Các tính năng khác


Có một số tính năng khác như `Hoán đổi` đa tiền tệ, tùy chọn `Mua và Bán` với nhiều kết nối nhà cung cấp khác nhau và các chương trình dành riêng cho Cake như `Cake Pay`, cho phép bạn mua thẻ trả trước hoặc thẻ quà tặng.


![image](assets/en/17.webp)


## 🎯 Kết luận


Đây là bài đánh giá của chúng tôi về Cake Wallet, sản phẩm mang lại sự riêng tư thiết thực như Bitcoin nhờ các tính năng như Thanh toán im lặng (BIP-352) và Payjoin v2.


Thanh toán Im lặng thay thế các địa chỉ dùng một lần bằng các địa chỉ ẩn có thể tái sử dụng để ngăn chặn việc liên kết on-chain với các giao dịch đến. Mặc dù các vấn đề đồng bộ hóa của các phiên bản trước đã được cải thiện đáng kể, nhưng vẫn cần một số yêu cầu tính toán cao hơn để quét và phát hiện Thanh toán Im lặng, đòi hỏi nhiều tài nguyên và băng thông hơn.


Payjoin v2 phá vỡ quy trình phân tích chuỗi bằng cách hợp nhất dữ liệu đầu vào của người gửi và người nhận thành một giao dịch duy nhất mà không mất thêm phí hay điều phối tập trung. Điều này phá vỡ quy tắc "quyền sở hữu đầu vào" thông thường, một lợi thế đáng kể vì nó cho phép bạn không thể giả định rằng tất cả dữ liệu đầu vào đều thuộc về người gửi.


Đối với những người dùng ưu tiên tính ẩn danh tài chính, Cake Wallet là một lựa chọn khả thi. Nó tích hợp các giao thức bảo mật trực tiếp vào chức năng cốt lõi, giúp dễ dàng truy cập mà không gặp bất kỳ sự phức tạp kỹ thuật nào. Khi hoạt động giám sát trên các blockchain công khai ngày càng tăng, các công cụ như thế này giúp duy trì quyền riêng tư trong giao dịch ở những nơi quan trọng nhất. Việc triển khai rộng rãi các tiêu chuẩn này trong bối cảnh wallet sẽ là một bước tiến đáng hoan nghênh.


## 📚 Tài nguyên


https://cakewallet.com


https://docs.cakewallet.com/


https://github.com/cake-tech/cake_wallet


https://blog.cakewallet.com/


[https://silentpayments.xyz/](https://silentpayments.xyz/)


[ttps://bips.dev/352/](https://bips.dev/352/)


https://payjoin.org/