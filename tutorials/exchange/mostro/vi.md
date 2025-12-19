---
name: Mostro
description: Nền tảng trao đổi Bitcoin P2P không cần KYC thông qua Lightning và Nostr
---

![cover](assets/cover.webp)



Làm thế nào để mua hoặc bán Bitcoin mà không ảnh hưởng đến chủ quyền tài chính của bạn? Các nền tảng tập trung áp dụng các quy trình KYC xâm phạm, làm lộ dữ liệu cá nhân của bạn, cùng với khả năng bị đóng băng tài khoản tùy ý hoặc bị nhà nước giám sát.



**Mostro P2P** cung cấp một giải pháp thay thế phi tập trung kết hợp Lightning Network, giao thức Nostr và hóa đơn lưu trữ. Cải tiến chính của nó: một hệ thống ký quỹ tự động, cho phép bạn kiểm soát bitcoin của mình trong suốt quá trình giao dịch, loại bỏ nguy cơ bị đánh cắp, sàn giao dịch phá sản hoặc bị tịch thu tùy tiện.



## Mostro P2P là gì?



Mostro P2P là giao thức trao đổi Bitcoin nguồn mở được tạo ra bởi **grunch**, nhà phát triển bot Telegram phổ biến **lnp2pbot** ra mắt năm 2021. Mặc dù lnp2pbot đã kích hoạt các sàn giao dịch P2P không cần KYC thông qua Lightning, nhưng nó lại có một lỗ hổng bảo mật lớn: **Telegram là điểm lỗi tập trung** dễ bị chính phủ kiểm duyệt.



Mostro đại diện cho sự **tiến hóa phi tập trung** của khái niệm này: bằng cách thay thế Telegram bằng giao thức **Nostr** (một mạng lưới các rơle phân tán không thể kiểm duyệt), Mostro loại bỏ rủi ro hệ thống này. Giao thức này kết hợp Lightning Network cho các giao dịch tức thời, Nostr cho giao tiếp chống kiểm duyệt và **giữ hóa đơn** để tạo ra một dịch vụ ký quỹ tự động thực sự không cần lưu ký.



### Kiến trúc kỹ thuật



Mostro hoạt động thông qua ba thành phần:




- Daemon Mostrod**: điều phối các trao đổi giữa người dùng và Lightning Network
- Nút Lightning**: tạo hóa đơn giữ (ký quỹ mật mã ~24 giờ)
- Khách hàng Mostro**: giao diện người dùng (CLI, Di động, Web)



Các lệnh được công bố trên Nostr dưới dạng sự kiện công khai (loại 38383), trong khi các giao dịch riêng tư được truyền qua tin nhắn được mã hóa đầu cuối (NIP-59, NIP-44). Mỗi phiên bản Mostro tự xác định mức phí riêng (thường từ 0,3% đến 1%) và giới hạn giao dịch (dao động từ vài nghìn đến vài trăm nghìn sats, tùy thuộc vào phiên bản).



### Lợi thế quyết định



**Chống kiểm duyệt**: Không chính phủ nào có thể đóng cửa Mostro chừng nào các trạm chuyển tiếp Nostr còn tồn tại ở đâu đó trên thế giới. Không giống như lnp2pbot dễ bị tấn công qua Telegram, Mostro cho phép các sàn giao dịch **chống kiểm duyệt**.



**Ký quỹ không lưu ký**: Hóa đơn Lightning Hold sẽ khóa Bitcoin của bạn mà không chuyển chúng vĩnh viễn. Tiền của bạn vẫn nằm trong tầm kiểm soát của bạn và sẽ tự động được hoàn trả trong trường hợp có sự cố (khoảng 24 giờ).



**Bảo mật theo thiết kế**: Có hai chế độ phù hợp với nhu cầu của bạn. Chế độ Uy tín** liên kết uy tín của bạn với khóa Nostr để xây dựng niềm tin lâu dài. Chế độ Riêng tư Hoàn toàn** ưu tiên tính ẩn danh tuyệt đối với khóa tạm thời dùng một lần.



## Các tính năng chính



**Giao tiếp phi tập trung**: Tất cả các lệnh đều được công bố trên Nostr thông qua các sự kiện được ký mã hóa. Các cuộc đàm phán riêng tư được truyền qua tin nhắn được mã hóa đầu cuối, đảm bảo tính bảo mật tuyệt đối.



**Hệ thống uy tín**: Xếp hạng 5 sao với tính toán lặp lại được lưu trữ vĩnh viễn trên Nostr. Cho phép bạn dần dần xây dựng uy tín là một nhà giao dịch đáng tin cậy.



**Trọng tài phi tập trung**: Trong trường hợp có tranh chấp, một trọng tài viên công bằng sẽ xem xét bằng chứng và đưa ra quyết định dựa trên các tiêu chí minh bạch. Mỗi tranh chấp sẽ tạo ra một mã token duy nhất để truy xuất nguồn gốc.



**Linh hoạt thanh toán**: Hỗ trợ nhiều loại tiền tệ fiat thông qua dịch vụ tỷ giá hối đoái yadio.io. Chấp nhận chuyển khoản SEPA, PayPal, Revolut, tiền mặt và bất kỳ phương thức nào được thỏa thuận giữa các bên.



## Khách hàng Mostro có sẵn



Mostro cung cấp hai khách hàng hoạt động chính cho sàn giao dịch P2P của bạn.



### Mostro CLI - Máy khách dòng lệnh



**Mostro CLI** là máy khách hoàn thiện và đa chức năng nhất. Được viết bằng Rust, nó cung cấp đầy đủ các tính năng của Mostro thông qua giao diện dòng lệnh. Tương thích với macOS, Linux và Windows.



**Điều khiển chính**:




- `listorders`: Hiển thị tất cả các đơn hàng có sẵn
- `neworder`: Tạo lệnh mua hoặc bán mới
- `takesell` / `takebuy`: Nhận lệnh mua hoặc bán
- `fiatsent`: Xác nhận gửi thanh toán bằng tiền pháp định
- `release`: Giải phóng tài khoản ký quỹ và hoàn tất giao dịch
- `getdm`: Xem tin nhắn trực tiếp
- `rate`: Đánh giá đối tác của bạn sau khi trao đổi



Lý tưởng cho người dùng kỹ thuật, tự động hóa và môi trường yêu cầu độ an toàn tối đa.



### Mostro Mobile - Ứng dụng điện thoại thông minh



**Ứng dụng di động** phiên bản alpha cho phép giao dịch P2P trực tiếp từ điện thoại thông minh của bạn. Giao diện Interface trực quan với điều hướng theo tab, xem lệnh, bộ lọc nâng cao và tính năng trò chuyện tích hợp để giao tiếp với đối tác của bạn.



Có sẵn cho **Android** (thông qua APK trên GitHub), đây là lựa chọn tối ưu cho người dùng ưa thích sự đơn giản và giao dịch di động thường xuyên.



### Mostro-web - Interface web (đang phát triển)



Ứng dụng web JavaScript nâng cao Interface đang được phát triển tích cực. Được thiết kế để mang đến trải nghiệm người dùng toàn diện với các chức năng giao dịch và quản lý danh mục đầu tư mở rộng. Truy cập qua trình duyệt mà không cần cài đặt.



## Cài đặt và cấu hình



Hướng dẫn này sẽ hướng dẫn bạn cài đặt và sử dụng hai ứng dụng Mostro chính: CLI và ứng dụng di động.



### Điều kiện tiên quyết cần thiết



Trước khi bắt đầu, bạn sẽ cần:





- Một Lightning Network** wallet đang hoạt động có đủ tính thanh khoản (hoặc tương thích với Lightning)
 - Đề xuất: Phoenix, Breez, Wallet của Satoshi...
 - Tối thiểu 1000 satoshi thanh khoản để kiểm tra



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf



- Khóa riêng tư Nostr** (định dạng `nsec1...`)
 - Tạo khóa giao dịch chuyên dụng trên [nostrkeygen.com](https://nostrkeygen.com/)
 - Quan trọng**: Không bao giờ sử dụng khóa Nostr cá nhân chính của bạn
 - Giữ khóa riêng của bạn ở nơi an toàn (trình quản lý mật khẩu)





- Tùy chọn nhưng được khuyến nghị**: Kết nối VPN hoặc Tor để che giấu địa chỉ IP của bạn



https://planb.academy/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8

### Lắp đặt Mostro CLI



#### Trên macOS



**Bước 1: Kiểm tra Rust**



Kiểm tra xem Rust đã được cài đặt chưa (yêu cầu phiên bản 1.64 trở lên):



```bash
rustc --version
```



Nếu Rust không được cài đặt:



```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```



**Bước 2: Sao chép kho lưu trữ**



```bash
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
```



![Vérification Rust et clonage](assets/fr/01.webp)



**Bước 3: Cấu hình**



Sao chép và chỉnh sửa:



```bash
cp .env-sample .env
```



Mở `.env` và cấu hình cài đặt của bạn:



```bash
# Public key of the Mostro instance (choose an instance)
# Main mainnet instance (recommended):
MOSTRO_PUBKEY='npub1ykvsmrmw2hk7jgxgy64zr8tfkx4nnjhq9eyfxdlg3caha3ph0skq6jr3z0'
# Alternative/test instance:
# MOSTRO_PUBKEY='npub19m9laul6k463czdacwx5ta4ap43nlf3lr0p99mqugnz8mdz7wtvskkm5wg'

# Your Nostr private key dedicated to trading
NSEC_PRIVKEY='nsec1votre_cle...'

# List of Nostr relays (use the same ones as the mobile app for synchronization)
RELAYS='wss://nos.lol,wss://relay.damus.io,wss://nostr-pub.wellorder.net,wss://nostr.mutinywallet.com,wss://relay.nostr.band'

POW='0'
```



**Quan trọng đối với việc đồng bộ hóa CLI/Di động**: Để truy cập cùng một đơn hàng trên CLI và ứng dụng di động, bạn phải sử dụng **cùng một Mostro Pubkey** và **cùng một rơle Nostr** trên cả hai máy khách. Kiểm tra các cài đặt này trong phần Cài đặt trên ứng dụng di động.



![Configuration .env](assets/fr/02.webp)



**Bước 4: Cài đặt**



Biên dịch và cài đặt CLI:



```bash
cargo install --path .
```



Quá trình biên dịch mất khoảng 1-2 phút. Tệp thực thi `mostro-cli` sẽ được cài đặt trong `~/.cargo/bin/`.



![Installation du CLI](assets/fr/03.webp)



**Bước 5: Kiểm tra**



Kiểm tra xem mọi thứ có hoạt động không:



```bash
mostro-cli --help
```



Bạn sẽ thấy danh sách đơn hàng đầy đủ.



![Vérification avec --help](assets/fr/04.webp)



#### Trên Linux (Ubuntu/Debian)



Cài đặt giống hệt macOS, bổ sung thêm:



```bash
sudo apt update
sudo apt install -y cmake build-essential pkg-config
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



Sau đó làm theo bước 3 và 4 trong phần macOS.



#### Trên Windows



Đầu tiên hãy cài đặt Rust qua [rustup.rs](https://rustup.rs/), sau đó sử dụng PowerShell:



```powershell
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



Cấu hình giống hệt nhau: sao chép `.env-sample` vào `.env` và điền vào các tham số của bạn.



### Cài đặt Mostro Mobile



#### Trên Android



**Bước 1**: Truy cập [Trang phát hành GitHub](https://github.com/MostroP2P/mobile/releases) và tải xuống tệp **app-release.apk** (khoảng 65 MB).



![Page GitHub Releases](assets/fr/10.webp)



**Bước 2: Sau khi tải xuống, hãy mở tệp APK từ thư mục đã tải xuống. Android sẽ yêu cầu bạn cấp quyền cài đặt từ nguồn này.



![Téléchargement et installation APK](assets/fr/11.webp)



**Bước 3**: Làm theo màn hình hướng dẫn để biết các chức năng:




- Giao dịch Bitcoin tự do - không cần KYC**: Giao dịch không cần xác minh danh tính nhờ Nostr
- Quyền riêng tư theo mặc định**: Chọn giữa chế độ Uy tín và chế độ Riêng tư hoàn toàn
- Bảo mật ở mọi bước**: Bảo vệ bằng hóa đơn giữ lại không lưu ký



![Écrans d'accueil Mostro](assets/fr/12.webp)



**Bước 4**: Tiếp tục hướng dẫn để khám phá:




- Trò chuyện được mã hóa hoàn toàn**: Giao tiếp được mã hóa đầu cuối
- Nhận một lời đề nghị**: Duyệt sổ lệnh và chọn một lời đề nghị
- Không tìm thấy những gì bạn cần?**: Tạo đơn hàng tùy chỉnh của riêng bạn



![Suite onboarding](assets/fr/13.webp)



**Bước 5: Sau khi hoàn tất quá trình đăng nhập, ứng dụng sẽ tự động tạo một cặp khóa Nostr. Vào menu (☰) rồi chọn **Tài khoản** để lưu **Từ khóa bí mật** (cụm từ khôi phục). Trên màn hình này, bạn cũng có thể thay đổi chế độ riêng tư đã đề cập trước đó.



![Menu et sauvegarde des clés](assets/fr/15.webp)



**Quan trọng**: Viết cụm từ khôi phục của bạn ở nơi an toàn (trình quản lý mật khẩu, két đựng giấy).



### Cấu hình bảo mật ban đầu



Bất kể bạn sử dụng nền tảng nào:





- Khóa chuyên dụng**: Sử dụng danh tính Nostr riêng để giao dịch
- Số tiền nhỏ**: Bắt đầu với số tiền dưới 10.000 sats để bắt đầu
- Nhiều rơle**: Cấu hình 3-5 rơle ở nhiều vị trí địa lý khác nhau
- Bảo vệ mạng**: Kích hoạt VPN hoặc Tor để ẩn địa chỉ IP của bạn
- Wallet secure**: Kích hoạt chức năng khóa tự động cho wallet Lightning của bạn



## Sử dụng với CLI



Phần này trình bày cách mua bitcoin thông qua Mostro CLI sau một trường hợp sử dụng thực tế.



### Bước 1: Liệt kê các đơn hàng có sẵn



Lệnh `listorders` hiển thị tất cả các đơn hàng đang hoạt động:



```bash
mostro-cli listorders
```



Bạn sẽ thấy bảng thông tin chi tiết về từng lệnh: ID, loại (mua/bán), số tiền, loại tiền tệ, phương thức thanh toán.



![Liste des ordres disponibles](assets/fr/05.webp)



Trong ví dụ này, lệnh bán 5 EUR thông qua Revolut có thể nhìn thấy được (ID: `305a59d0-dbee-4880-9b9a-44a60486ba4a`).



### Bước 2: Tiếp nhận đơn hàng



Để mua những bitcoin này, hãy thực hiện lệnh với `takesell`:



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



Mostro sẽ yêu cầu bạn cung cấp **Hóa đơn Lightning** để nhận BTC. Số tiền chính xác tính bằng satoshi được ghi rõ (ở đây: 4715 sats).



![Prise d'ordre de vente](assets/fr/06.webp)



### Bước 3: Cung cấp hóa đơn Lightning của bạn



Tạo hóa đơn Lightning từ wallet (Phoenix, Breez, v.v.) của bạn với số tiền chính xác, sau đó gửi:



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a --invoice lnbc47150n1p...
```



Hệ thống xác nhận việc giao hàng và yêu cầu bạn đợi người bán thanh toán hóa đơn giữ hàng trước khi kích hoạt ký quỹ.



![Envoi de la Lightning invoice](assets/fr/07.webp)



### Bước 4: Liên hệ với người bán



Sau khi ký quỹ được kích hoạt, hãy sử dụng `dmtouser` để yêu cầu thông tin thanh toán từ người bán:



```bash
mostro-cli dmtouser --pubkey 7100aed1b44819555b34f90a6ca8dbb7263526e0c580f5ee35fe20d7b0644ae4 \
--orderid 305a59d0-dbee-4880-9b9a-44a60486ba4a \
--message "Hey what's your revtag ?"
```



![Communication avec le vendeur](assets/fr/08.webp)



### Bước 5: Lấy lại câu trả lời



Kiểm tra tin nhắn trực tiếp để xem phản hồi của người bán:



```bash
mostro-cli getdm
```



Người bán cung cấp cho bạn ID thanh toán của anh ấy (ở đây là Revtag của anh ấy: `@satoshi`).



![Réception de la réponse](assets/fr/09.webp)



### Bước 6: Thực hiện thanh toán bằng tiền pháp định



Gửi thanh toán qua phương thức đã thỏa thuận (trong ví dụ này là Revolut) đến thông tin liên hệ được cung cấp. **Lưu giữ tất cả các chứng từ hỗ trợ** (ảnh chụp màn hình, mã giao dịch).



### Bước 7: Xác nhận thanh toán



Sau khi thanh toán xong, hãy thông báo cho Mostro:



```bash
mostro-cli fiatsent -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



### Bước 8: Nhận bitcoin



Ngay khi người bán xác nhận đã nhận được tiền pháp định và giải phóng tài khoản ký quỹ bằng lệnh `giải phóng`, bạn sẽ ngay lập tức nhận được bitcoin trên hóa đơn Lightning mà bạn đã cung cấp.



### Bước 9: Đánh giá



Đánh giá người bán để đóng góp vào danh tiếng phi tập trung:



```bash
mostro-cli rate -o 305a59d0-dbee-4880-9b9a-44a60486ba4a -r 5
```



### Các lệnh hữu ích



**Hủy đơn hàng** (trước khi đơn hàng được nhận):


```bash
mostro-cli cancel -o <order-id>
```



**Tạo đơn đặt hàng mới**:


```bash
mostro-cli neworder -k sell -c eur -f 20 -m "Revolut" -p 2
```



**Mở tranh chấp** :


```bash
mostro-cli dispute -o <order-id>
```



## Sử dụng với ứng dụng di động



Phần này trình bày việc bán bitcoin thông qua Mostro Mobile bằng cách thực hiện một trường hợp sử dụng thực tế.



### Interface chính



Ứng dụng có 3 tab chính:





- Sổ lệnh**: Duyệt các lệnh mua (MUA BTC) và bán (BÁN BTC) có sẵn
- Giao dịch của tôi**: Xem các lệnh đang hoạt động và lịch sử của bạn
- Trò chuyện**: Giao tiếp với đối tác của bạn bằng các con số



![Interface principale](assets/fr/14.webp)



### Cấu hình được đề xuất



Trước khi giao dịch, hãy thiết lập một số cài đặt thông qua menu (☰) > **Cài đặt**:





- Lightning Address** (tùy chọn): Để nhận thanh toán trực tiếp
- Rơ le**: Thêm một số rơ le Nostr để tăng khả năng phục hồi (ví dụ: `wss://nos.lol`, `wss://relay.damus.io`)
- Mostro Pubkey**: Kiểm tra khóa công khai của phiên bản Mostro bạn đang sử dụng



![Paramètres de l'application](assets/fr/16.webp)



**Quan trọng đối với việc đồng bộ hóa CLI/Di động**: Nếu bạn đang sử dụng cả CLI và ứng dụng di động, hãy cấu hình **chính xác cùng một rơ-le Nostr và Mostro Pubkey** trên cả hai máy khách. Nếu không có cấu hình giống hệt nhau, bạn sẽ không thấy cùng một lệnh khả dụng trên cả hai giao diện. Các rơ-le và Mostro Pubkey hiển thị trong Cài đặt (ảnh chụp màn hình ở trên) phải khớp với các rơ-le và Mostro Pubkey trong tệp `.env' của CLI.



### Bước 1: Tạo lệnh bán



Nhấn nút **"+"** màu xanh lá cây ở góc dưới bên phải, sau đó chọn **BÁN** (nút màu đỏ).



![Boutons de création d'ordre](assets/fr/17.webp)



Điền vào mẫu tạo:



1. **Tiền tệ**: Chọn loại tiền tệ bạn muốn nhận (EUR, USD, v.v.)


2. **Số tiền**: Nhập số tiền bằng tiền pháp định (ví dụ: 1 đến 3 EUR)


3. **Phương thức thanh toán**: Chọn phương thức (ví dụ: "Revolut")


4. **Loại giá**: Chọn "Giá thị trường"


5. **Cao cấp**: Điều chỉnh cao cấp (thanh trượt từ -10% đến +10%, khuyến nghị: 0% để bán nhanh)



Nhấn **Gửi** để đăng đơn hàng của bạn.



### Bước 2: Xác nhận xuất bản



Đơn hàng của bạn hiện đã được xuất bản! Đơn hàng sẽ có hiệu lực trong vòng 24 giờ. Bạn có thể hủy đơn hàng bất cứ lúc nào trước khi người mua nhận hàng bằng cách thực hiện lệnh `cancel`.



![Ordre publié](assets/fr/18.webp)



Lệnh sẽ xuất hiện trong tab **Giao dịch của tôi** với trạng thái "Đang chờ xử lý" và huy hiệu "Do bạn tạo".



### Bước 3: Người mua nhận đơn hàng của bạn



Khi người mua chấp nhận đơn hàng của bạn, bạn sẽ nhận được thông báo. Xem chi tiết trong mục **Giao dịch của tôi**.



![Ordre pris par un acheteur](assets/fr/19.webp)



**Hướng dẫn quan trọng**: Bây giờ bạn phải **thanh toán hóa đơn giữ** được hiển thị để khóa bitcoin của bạn (ở đây là 4674 sats với giá 1-5 EUR) trong tài khoản ký quỹ. Bạn có **tối đa 15 phút**, nếu không giao dịch sẽ bị hủy.



Sao chép hóa đơn giữ hàng và thanh toán từ máy wallet Lightning (Phoenix, Breez, v.v.) của bạn.



### Bước 4: Giao tiếp với người mua



Sau khi ký quỹ được kích hoạt, hãy nhấn **LIÊN HỆ** để mở cuộc trò chuyện được mã hóa với người mua.



Người mua (ở đây là "anonymous-gloriaZhao") sẽ liên hệ với bạn để yêu cầu thông tin thanh toán. Vui lòng trả lời kèm theo thông tin của bạn (Revtag, IBAN, v.v.).



![Chat avec l'acheteur](assets/fr/20.webp)



### Bước 5: Nhận thanh toán bằng tiền pháp định



Chờ cho đến khi bạn nhận được khoản thanh toán bằng tiền pháp định vào tài khoản Revolut của mình (hoặc phương thức đã thỏa thuận khác). **Kiểm tra cẩn thận**:




- Số tiền chính xác
- Người gửi
- Tài liệu tham khảo nếu được yêu cầu



Người mua sẽ thông báo cho bạn qua trò chuyện rằng họ đã gửi thanh toán. Mostro cũng sẽ hiển thị thông báo xác nhận rằng tiền pháp định đã được gửi cho bạn.



![Confirmation d'envoi du paiement](assets/fr/20.webp)



### Bước 6: Giải phóng tài khoản ký quỹ



Sau khi bạn đã **xác nhận biên lai** khoản thanh toán bằng tiền pháp định vào tài khoản của mình, hãy nhấn nút **GIẢI PHÓNG** màu xanh lá cây và xác nhận gửi tiền cho người mua.



![Libération de l'escrow](assets/fr/20.webp)



Bitcoin sẽ được chuyển ngay cho người mua thông qua hóa đơn Lightning của họ.



### Bước 7: Đánh giá sự cân nhắc



Sau khi phát hành, hãy nhấn **ĐÁNH GIÁ** để đánh giá người mua. Chọn từ 1 đến 5 sao (ở đây là 5/5) và nhấn **Gửi đánh giá**.



![Évaluation de la contrepartie](assets/fr/21.webp)



Cuộc trao đổi đã kết thúc!



### Mua bitcoin bằng ứng dụng di động



Quá trình mua bitcoin cũng tương tự nhưng ngược lại:



1. Duyệt qua tab **Sổ lệnh** > **MUA BTC** để xem lệnh bán


2. Nhấp vào đơn hàng thú vị để xem chi tiết


3. Nhấn **Nhận đơn hàng**


4. Cung cấp hóa đơn Lightning của bạn (được tạo từ wallet của bạn)


5. Chờ người bán kích hoạt ký quỹ


6. Liên hệ với người bán qua **LIÊN HỆ** để biết thông tin thanh toán


7. Gửi thanh toán bằng tiền pháp định (giữ lại bằng chứng)


8. Người bán giải phóng tiền ký quỹ sau khi xác minh


9. Nhận bitcoin ngay lập tức trên hóa đơn Lightning của bạn


10. Đánh giá người bán (1-5 sao)



### Quản lý vấn đề



**Hủy lệnh**: Trong **Giao dịch của tôi**, hãy nhấn lệnh của bạn rồi nhấn nút **HỦY** (chỉ khả dụng trước khi lệnh được thực hiện).



**Mở tranh chấp**: Nếu có bất đồng, hãy nhấn **TRANH CHẤP** trong chi tiết đơn hàng. Đính kèm tất cả bằng chứng (ảnh chụp màn hình trò chuyện, thông tin giao dịch ngân hàng).



## Ưu điểm và hạn chế



### Những lợi ích



**Chủ quyền tài chính**: Bitcoin của bạn sẽ không bao giờ rời khỏi quyền kiểm soát trực tiếp của bạn nhờ cơ chế giữ hóa đơn, loại bỏ nguy cơ sàn giao dịch phá sản hoặc vi phạm bản quyền.



**Chống kiểm duyệt**: Không cơ quan nào có thể đóng cửa mạng lưới hoặc kiểm duyệt đơn hàng của bạn. Hệ thống sẽ hoạt động miễn là các rơle Nostr còn hoạt động.



**Ẩn danh mặc định**: Chỉ có khóa Nostr ẩn danh mới xác định được bạn, không cần KYC hoặc dữ liệu cá nhân. Truyền thông được mã hóa đầu cuối.



**Tính linh hoạt trong thanh toán**: Có thể sử dụng bất kỳ phương thức thanh toán nào được cả hai bên chấp nhận (chuyển khoản, ứng dụng di động, tiền mặt, đổi hàng).



### Hạn chế



**Phát triển ban đầu**: Cần có giao diện cơ bản và đường cong học tập kỹ thuật.



**Tính thanh khoản hạn chế**: Số lượng lệnh hạn chế, đặc biệt đối với số lượng lớn hoặc các loại tiền tệ hiếm.



**Yêu cầu kỹ thuật**: Cần có hiểu biết cơ bản về Lightning và Nostr.



**Trách nhiệm cá nhân**: Không có sự hỗ trợ tập trung trong trường hợp có vấn đề, cần phải thận trọng.



## Phần kết luận



Mostro P2P là một giải pháp thay thế đầy hứa hẹn cho các sàn giao dịch tập trung, kết hợp Lightning Network, Nostr và ký quỹ tự động để tạo nên một giao dịch phi tập trung thực sự. Mặc dù mới được phát triển ban đầu và còn hạn chế về tính thanh khoản, nền tảng này đã cung cấp khả năng tự chủ tài chính, khả năng chống kiểm duyệt và tính ẩn danh khi vỡ nợ.



Đối với những người dùng Bitcoin ưa chuộng tính tự chủ và bảo mật, Mostro là một lựa chọn khả thi đáng để khám phá. Kiến trúc phi tập trung của nó đảm bảo sự phát triển cộng đồng thay vì thương mại, mở đường cho một tương lai của các sàn giao dịch Bitcoin thực sự miễn phí.



## Tài nguyên



### Tài liệu chính thức




- [Trang web chính thức của Mostro](https://mostro.network)
- [Tài liệu kỹ thuật](https://mostro.network/docs-english/index.html)
- [Quỹ Mostro](https://mostro.foundation)



### Mã nguồn và phát triển




- [Kho lưu trữ GitHub chính](https://github.com/MostroP2P/mostro)
- [Trình duyệt web](https://github.com/MostroP2P/mostro-web)
- [Khách hàng CLI](https://github.com/MostroP2P/mostro-cli)



### Cộng đồng




- [Giao thức Nostr](https://nostr.com)
- [Hướng dẫn Lightning Network](https://lightning.network)