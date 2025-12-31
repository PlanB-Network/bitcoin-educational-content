---
name: Coin Wallet
description: Hướng dẫn về Coin, Wallet và các cách để tăng cường quyền riêng tư và bảo mật.
---

![cover](assets/cover.webp)


Hướng dẫn này đề cập đến [Coin Wallet](https://coin.space/) - một loại tiền điện tử tự quản lý wallet dành cho thiết bị di động, và cách tăng cường bảo mật và quyền riêng tư khi sử dụng ứng dụng wallet trên thiết bị di động.



## Về Coin Wallet


**Coin Wallet** là một hệ điều hành wallet mã nguồn mở, tự quản lý/không quản lý, được tạo ra bởi một nhóm những người đam mê Bitcoin vào năm 2015. Ban đầu nó là một ứng dụng web, sau đó là ứng dụng iOS vào năm 2017 và ứng dụng Android vào năm 2020 - có sẵn trên Google Play, Samsung Galaxy Store và Huawei AppGallery.


Ưu điểm chính:


- Kiến trúc phi giam giữ
- Mã nguồn hoàn toàn [mở](https://github.com/CoinSpace/CoinSpace/blob/master/LICENSE)
- Thiết kế đơn giản và gọn gàng
- Tập trung vào mục đích cốt lõi - lưu trữ tiền điện tử một cách an toàn, không có các tính năng không cần thiết.
- Hỗ trợ đa nền tảng: di động (iOS & Android), máy tính để bàn, web
- Hỗ trợ RBF (Thay thế bằng phí) - tăng tốc các giao dịch bị kẹt bất cứ lúc nào
- Xác thực hai yếu tố phần cứng (2FA) với [YubiKey](https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/) / khóa FIDO2
- Tích hợp hỗ trợ Tor – định tuyến toàn bộ lưu lượng truy cập qua mạng Tor để đảm bảo quyền riêng tư tối đa.



## 1️⃣ Lắp đặt Coin Wallet

Coin Wallet hiện có sẵn trên tất cả các nền tảng chính.



- [iOS App Store](https://apps.apple.com/app/coin-wallet-bitcoin-crypto/id980719434)



- [Android Google Play](https://play.google.com/store/apps/details?id=com.coinspace.app)



- [Android (Galaxy Store)](https://galaxystore.samsung.com/detail/com.coinspace.app)



- [Android (Huawei AppGallery)](https://appgallery.huawei.com/app/C112183767)



- [Android (Uptodown)](https://coin-wallet.en.uptodown.com/android)



- [Ứng dụng Android APK](https://coin.space/api/v3/download/android-apk/any)



- [Tất cả các liên kết phát hành](https://github.com/CoinSpace/CoinSpace/releases)


Ứng dụng này cũng có sẵn cho máy tính để bàn (Windows, Linux, macOS), dưới dạng ứng dụng web và thông qua Tor.


![image](assets/en/01.webp)


## 2️⃣ Tạo Wallet và thiết lập mã PIN


wallet được tạo ra bằng cách sử dụng passphrase – một chuỗi ngẫu nhiên gồm 12 từ được phân tách bởi dấu cách, được tạo ra từ [danh sách 2048 từ](https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts).

Coin và Wallet hỗ trợ các cụm mật khẩu gồm 12, 15, 18, 21 hoặc 24 từ được nhập từ các ví khác.


passphrase là dạng dễ đọc của khóa riêng tư chính. Nó phải được lưu trữ an toàn. Chỉ cần passphrase là đủ để truy cập hoặc khôi phục wallet. Nếu passphrase bị mất, wallet và tất cả tiền trong tài khoản sẽ bị mất vĩnh viễn. passphrase tuyệt đối không được chia sẻ. Coin và Wallet không lưu trữ khóa trên bất kỳ máy chủ hoặc cơ sở dữ liệu nào.


**Mã passphrase gồm 12 từ có an toàn không?**

Với 2048 từ khả thi cho mỗi vị trí, có 2048¹² ≈ 10³⁹ tổ hợp — cung cấp mức độ bảo mật ~128 bit, tương đương với khóa riêng Bitcoin. Mức độ này được coi là đủ an toàn.


![image](assets/en/02.webp)


Sau khi ghi lại và xác nhận mã passphrase, ứng dụng sẽ yêu cầu bạn thiết lập mã PIN 4 chữ số để truy cập hàng ngày. Để thuận tiện hơn, bạn có thể bật xác thực sinh trắc học (vân tay hoặc nhận diện khuôn mặt) thay vì sử dụng mã PIN.


![image](assets/en/03.webp)



Không có chức năng khôi phục tài khoản, khôi phục khóa, thiết lập lại passphrase và hoàn trả giao dịch. Bảo mật hoàn toàn là trách nhiệm của người dùng.


Để biết các phương pháp tốt nhất chi tiết về cách lưu cụm từ ghi nhớ:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 3️⃣ Mật khẩu + Mã PIN. Khi nào và cách thức sử dụng chúng


**Khi nào cần sử dụng passphrase?**

Chỉ trong những trường hợp hiếm hoi này:


- Thiết lập wallet trên thiết bị mới
- Cài đặt lại ứng dụng Coin Wallet
- Xóa dữ liệu ứng dụng/trình duyệt (Bộ nhớ cục bộ)
- Xóa khóa phần cứng khỏi tài khoản
- Nhập sai mã PIN ba lần (ứng dụng sẽ bị khóa vì lý do bảo mật)


Trong sử dụng hàng ngày, mã PIN 4 chữ số là đủ để mở khóa wallet.


**Mật khẩu + Mã PIN: Cách thức hoạt động**

passphrase là khóa riêng tư chính thực sự và hoạt động trên mọi thiết bị.

Vì việc gõ 12-24 từ mỗi lần sẽ bất tiện, Coin và Wallet sử dụng mã PIN 4 chữ số để truy cập nhanh chóng hàng ngày trên thiết bị hiện tại.

Mã PIN đơn giản không đủ an toàn để bảo vệ trực tiếp khóa chính, vì vậy nó không bao giờ được sử dụng để mã hóa. Thay vào đó:



- Mã PIN được gửi đến máy chủ và được đổi lấy một chuỗi mã hóa dài token.
- Thiết bị token này giải mã khóa chính được mã hóa, chỉ được lưu trữ trên thiết bị.


Nếu nhập mã PIN sai ba lần, máy chủ sẽ xóa vĩnh viễn token. Khóa được lưu trữ cục bộ sẽ không thể sử dụng được nữa, và cách duy nhất để khôi phục wallet là nhập lại passphrase ban đầu.

Thiết kế này mang lại cả sự tiện lợi và khả năng bảo vệ dự phòng mạnh mẽ.



## 4️⃣ Nhận Bitcoin - Các loại Address và quyền riêng tư


Coin Wallet hỗ trợ cả ba định dạng địa chỉ Bitcoin:



- SegWit gốc (Bech32)** – bắt đầu với **bc1q** – phí thấp nhất, được khuyến nghị
- SegWit lồng nhau (P2SH)** – bắt đầu bằng **3**
- Di sản (P2PKH)** – bắt đầu với **1**


![image](assets/en/04.webp)


**Tại sao địa chỉ lại thay đổi sau mỗi lần gửi tiền?**

Đây là hành động có chủ đích và nhằm bảo vệ quyền riêng tư. Mỗi khi nhận được tiền điện tử, Coin và Wallet tự động tạo ra một địa chỉ mới chưa được sử dụng. Nếu cùng một địa chỉ được sử dụng lại (ví dụ: cho lương tháng), bất kỳ ai cũng có thể dễ dàng tổng hợp tất cả các giao dịch đến trên trình khám phá blockchain và biết tổng thu nhập.


Các địa chỉ cũ vẫn có hiệu lực vĩnh viễn – bạn vẫn có thể nhận hàng tại đó – nhưng sử dụng một địa chỉ mới mỗi lần là cách tốt nhất để bảo vệ quyền riêng tư.


**Cách nhận Bitcoin:**

1. Mở đồng xu

2. Chạm vào **Nhận**

3. Chọn loại địa chỉ mong muốn (tốt nhất là **bc1q** – `Native SegWit`)

4. Hiển thị mã QR hoặc sao chép địa chỉ và gửi cho người thanh toán.


**Tùy chọn - Mecto (cho thanh toán trực tiếp):**

Trên cùng màn hình Nhận đó có một nút `Mecto`.

Khi bạn bật nó lên:


- Bạn sẽ được yêu cầu nhập **biệt danh** (ảnh đại diện).
- Vị trí hiện tại của bạn và địa chỉ nhận được sẽ tạm thời được chia sẻ với những người dùng Coin Wallet khác cũng đã bật Mecto.
- Họ có thể định vị bạn trên một bản đồ nhỏ và gửi tiền xu mà không cần gõ chữ hay quét mã.


Dữ liệu chỉ hiển thị cho những người dùng Mecto khác và sẽ tự động bị xóa sau 1 giờ (hoặc ngay lập tức khi bạn tắt thiết bị).

Mecto hoàn toàn là tùy chọn – hãy tắt nó đi nếu bạn muốn có sự riêng tư tối đa.


![image](assets/en/05.webp)


## 5️⃣ Gửi Bitcoin


Để gửi Bitcoin:


1. Mở ví → chạm vào **Gửi**

2. Dán địa chỉ hoặc quét mã QR.

3. Nhập số tiền (hoặc nhấn **Tối đa**)

4. Chọn tốc độ giao dịch:


| Speed   | Approx. confirmation time | Fee level     |
|---------|---------------------------|---------------|
| **Slow**    | ~120 minutes              | Lowest
| **Default** | ~60 minutes               | Medium
| **Fast**    | ~20 minutes               | Higher

5. Xác nhận bằng mã PIN 4 chữ số của bạn → giao dịch được thực hiện


### Cách tăng tốc giao dịch ₿itcoin đang chờ xử lý (RBF)


Nếu bạn chọn phí giao dịch chậm và giao dịch bị kẹt:


1. Vào tab **Lịch sử**

2. Chạm vào giao dịch đang chờ xử lý

3. Chạm vào **Tăng tốc** (Thay thế bằng phí)

4. Xác nhận → giao dịch sẽ được phát lại với mức phí cao hơn


Tính năng tăng tốc RBF hiện được hỗ trợ cho:

Bitcoin • Avalanche • Binance Smart Chain • Ethereum • Ethereum Classic • Polygon


Thông tin chi tiết hơn về Replace-by-fee (RBF): https://bitcoinops.org/en/topics/replace-by-fee/


## 6️⃣ Xuất khóa riêng tư


**Khi nào bạn thực sự cần khóa riêng tư?**

(99% người dùng không bao giờ làm vậy — chỉ cần mã passphrase gồm 12 từ là đủ)


| Situation                                      | Why you need the private key                     |
|------------------------------------------------|--------------------------------------------------|
| Sweeping an old paper wallet                   | To move funds to your current wallet             |
| Importing into a hardware signer (e.g. Coldcard) | For offline signing                              |
| Emergency recovery (lost seed but app still open) | To rescue coins before the app is gone           |
| Using tools that don’t accept seed phrases     | Some watch-only or signing utilities             |

### Cách xuất khóa riêng tư trên Coin Wallet


1. Mở **Bitcoin (BTC)**

2. Cuộn xuống cuối trang - nhấn **Xuất khóa riêng tư**

3. Ứng dụng hiển thị mọi địa chỉ kèm số dư + khóa riêng tư ở định dạng **WIF** (bắt đầu bằng 5, K hoặc L) và mã QR.


Chỉ những địa chỉ không rỗng mới được hiển thị.


**Ví dụ về khóa WIF**

`L2v1eK4i9j3k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k`


**Những việc cần làm tiếp theo (khuyến nghị)**


- Mở Electrum, Sparrow, BlueWallet hoặc bất kỳ thiết bị phần cứng wallet nào.
- Nhập/Quét khóa riêng tư
- Tất cả tiền sẽ được chuyển ngay lập tức đến một địa chỉ an toàn mới thuộc tài khoản seed hiện tại của bạn.


Tuyệt đối không lưu trữ khóa riêng tư dưới dạng văn bản thuần. Sau khi quét xong, bạn có thể xóa nó một cách an toàn.


Để có hướng dẫn đầy đủ về khóa riêng tư và đường dẫn tạo khóa: [Cách làm việc với khóa riêng tư: Hướng dẫn toàn diện](https://coin.space/how-to-work-with-private-keys-the-ultimate-guide/)



## 7️⃣ Chi tiết kỹ thuật – BIP39, BIP32 và các đường dẫn dẫn xuất


Coin và Wallet tuân thủ nghiêm ngặt các tiêu chuẩn Bitcoin chính thức được hầu hết các ví điện tử chuyên nghiệp sử dụng.


`BIP39` - cách passphrase trở thành khóa riêng tư chính


- Số từ mặc định: 12
- passphrase/mật khẩu tùy chọn: không có ("")
- Độ nhiễu loạn ban đầu: 128 bit (12 từ) → 256 bit (24 từ)
- Mã nguồn mở: https://github.com/paulmillr/scure-bip39
- Danh sách từ vựng: danh sách từ vựng tiếng Anh chuẩn gồm 2048 từ.
- Hỗ trợ nhập các cụm từ gồm 12, 15, 18, 21 và 24 từ bất kỳ thiết bị BIP39 wallet nào khác.


`BIP32 + BIP44/BIP49/BIP84` - tạo địa chỉ một cách xác định.

Từ một khóa chính duy nhất, wallet có thể truy cập hàng tỷ địa chỉ generate theo một thứ tự được xác định nghiêm ngặt. Đó là lý do tại sao cùng một 12 từ được nhập vào Electrum, Sparrow, Trezor, Ledger, BlueWallet, v.v. sẽ hiển thị chính xác cùng một địa chỉ và số dư.


**Các đường dẫn dẫn xuất được sử dụng trong Coin, Wallet cho Bitcoin**


| Address type              | Standard | Derivation path       | Starts with | Comment                              |
|---------------------------|----------|-----------------------|-------------|--------------------------------------|
| Native SegWit (Bech32)    | BIP84    | `m/84'/0'/0'`         | bc1q…       | Modern format, lowest fees           |
| Nested SegWit (P2SH)      | BIP49    | `m/49'/0'/0'`         | 3…          | Compatibility wrapper for old services |
| Legacy (P2PKH)            | BIP44    | `m/44'/0'/0'`         | 1…          | Oldest format, highest fees          |

Bên trong mỗi con đường:


- `/0` — chuỗi bên ngoài (địa chỉ bạn dùng để nhận thanh toán)
- `/1` — chuỗi nội bộ (thay đổi địa chỉ mà chính wallet sử dụng)


Vì Coin Wallet tuân thủ các tiêu chuẩn công khai này mà không có bất kỳ thay đổi nào, nên tiền của bạn vẫn có thể được thu hồi trong bất kỳ wallet tương thích nào khác ngay cả sau 10–20–30 năm.


## 8️⃣ Tăng cường tính ẩn danh với Tor


**Tại sao nên sử dụng Tor trong Coin Wallet**

Tor che giấu địa chỉ IP thực của bạn khỏi các nút Bitcoin, các điểm trao đổi và các bên quan sát.

Tất cả lưu lượng truy cập (số dư, giao dịch, hoán đổi) đều đi qua mạng Tor - không có kết nối trực tiếp, không rò rỉ địa chỉ IP.

Điều này được triển khai trực tiếp trong mã nguồn của ứng dụng (xem [.env configuration](https://github.com/CoinSpace/CoinSpace/blob/master/web/.env#L31)).


Coin Wallet có địa chỉ .onion ẩn và, kể từ phiên bản v6.6.3 (tháng 12 năm 2024), **đã tích hợp hỗ trợ Tor trực tiếp trong ứng dụng di động**.


### Cách bật Tor trên Android và iOS


1. **Cài đặt Orbot** - ứng dụng chính thức của Dự án Tor (miễn phí)


   - Android → [Google Play](https://play.google.com/store/apps/details?id=org.torproject.android) / [F-Droid](https://orbot.app/en/)
   - iPhone / iPad → [App Store](https://apps.apple.com/us/app/orbot/id1609461599)


2. **Mở Orbot → chạm vào Bắt đầu**

Chọn **Coin Wallet** từ danh sách để chỉ wallet sử dụng Tor (tùy chọn nhưng được khuyến nghị)

Chờ cho đến khi màn hình hiển thị **"Đã kết nối"** (10-30 giây)


3. **Mở Coin Wallet → Cài đặt → Mạng**

Bật **Sử dụng Tor**


4. **Kiểm tra trạng thái**

Một biểu tượng **hình củ hành Tor màu tím** xuất hiện trên thanh trên cùng → tất cả lưu lượng truy cập hiện được định tuyến qua Tor.


![image](assets/en/06.webp)


Vậy là xong - thiết bị di động Coin Wallet của bạn đã hoàn toàn ẩn danh.


Tận hưởng dịch vụ quản lý tiền điện tử riêng tư!


## 📝 Kết luận


[Coin Wallet](https://coin.space/) - một trong những người tiên phong thực sự của Bitcoin wallet với lịch sử phát triển 10 năm.

Nó được thiết kế đơn giản một cách có chủ ý và tập trung tuyệt đối vào nhiệm vụ cốt lõi của mình: lưu trữ tiền điện tử của bạn một cách an toàn.

Không có quảng cáo, không có nguồn cấp tin tức, không có đăng ký, không có tính năng mạng xã hội, không có gì gây xao nhãng - chỉ đơn giản là một chiếc wallet sạch sẽ, nhanh chóng, tự quản lý và làm đúng những gì nó cần làm.

Coin Wallet luôn đặt sự đơn giản và bảo mật lên hàng đầu, và sẽ luôn như vậy.


## 📖 Tài nguyên


https://coin.space/


https://support.coin.space/hc/en-us


https://en.bitcoin.it/wiki/Wallet


https://bitcoinops.org/


https://github.com/CoinSpace/CoinSpace/


https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/


https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts


https://github.com/paulmillr/scure-bip39