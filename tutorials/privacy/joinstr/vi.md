---
name: Joinstr
description: CoinJoins phi tập trung thông qua mạng lưới Nostr để bảo mật Bitcoin có chủ quyền
---

![cover](assets/cover.webp)



Tính minh bạch của blockchain Bitcoin cho phép theo dõi lịch sử giao dịch. CoinJoins phá vỡ các liên kết này bằng cách trộn nhiều giao dịch đồng thời, khôi phục mức độ bảo mật tương đương với tiền mặt.



Tuy nhiên, các giải pháp truyền thống dựa vào một bộ điều phối trung tâm như một điểm lỗi duy nhất. Wasabi và Samourai đã ngừng hoạt động vào năm 2024 do áp lực từ cơ quan quản lý.



**Joinstr** khắc phục điểm yếu này bằng cách sử dụng mạng lưới Nostr phi tập trung để điều phối. Ứng dụng nguồn mở này cho phép CoinJoins thực sự có chủ quyền, nơi không một cơ quan trung ương nào có thể kiểm duyệt, giám sát hoặc gián đoạn dịch vụ.



## Joinstr là gì?



Joinstr là một công cụ nguồn mở cách mạng hóa phương pháp CoinJoins bằng cách tận dụng giao thức Nostr làm cơ sở hạ tầng điều phối. Không giống như các giải pháp tập trung yêu cầu máy chủ chuyên dụng, Joinstr dựa vào mạng lưới phân tán các rơle Nostr để cho phép người tham gia phối hợp trực tiếp giữa các đồng nghiệp.



**Kiến trúc phi tập trung**: Mạng lưới Nostr thay thế bộ điều phối trung tâm. Người tham gia tạo hoặc tham gia "nhóm" bằng cách đăng thông báo được mã hóa qua các rơ le Nostr. Thông tin này (số lượng, người tham gia, địa chỉ) sẽ không được các rơ le hiểu được, đảm bảo rằng không một thực thể trung tâm nào có thể giám sát, kiểm duyệt hoặc lọc CoinJoin.



**Cơ chế SIGHASH_ALL|ANYONECANPAY**: Joinstr khai thác cờ chữ ký Bitcoin này, cho phép mỗi người tham gia chỉ ký dữ liệu đầu vào của mình trong khi xác thực tất cả dữ liệu đầu ra. Mỗi người dùng tạo PSBT cục bộ, sau đó phân phối qua Nostr. Mỗi người dùng tạo PSBT cục bộ, ký nó, sau đó phân phối qua Nostr. Bitcoin của bạn sẽ nằm dưới sự kiểm soát độc quyền của bạn cho đến khi chữ ký cuối cùng được ký.



**Triết lý**: Joinstr tuân theo tinh thần cypherpunk của Bitcoin, hướng tới ba mục tiêu: **chống kiểm duyệt** (không có cơ quan nào có thể ngăn chặn dịch vụ), **hoàn toàn không lưu giữ** (bạn giữ khóa riêng của mình) và **đối xử bình đẳng** (không có UTXO nào bị phân biệt đối xử).



### Các tính năng chính



**Các nhóm linh hoạt**: Không giống như mệnh giá cố định, bất kỳ người dùng nào cũng có thể tạo một nhóm với số tiền chính xác mong muốn và số lượng người tham gia mục tiêu, tối ưu hóa việc sử dụng UTXO mà không cần chia tách nhân tạo.



**Phí minh bạch**: Không có phí điều phối. Chỉ có phí giao dịch Bitcoin được chia đều cho những người tham gia (vài nghìn satoshi cho mỗi người).



**Tính tạm thời**: Không lưu giữ dữ liệu người dùng. Thông tin được truyền qua các tin nhắn Nostr tạm thời được mã hóa, bị lãng quên ngay sau khi giao dịch.



### Nền tảng có sẵn



Hướng dẫn này tập trung vào **ứng dụng Android**, giải pháp duy nhất hiện đang ổn định và được khuyến nghị. Plugin Electrum đã có nhưng gặp vấn đề về khả năng tương thích khiến nó không ổn định. Giao diện web đang được phát triển.



## Cấu hình lõi Bitcoin



Joinstr Android yêu cầu kết nối đến nút Bitcoin thông qua RPC. Trước tiên, bạn phải cấu hình Bitcoin Core trên máy tính để chấp nhận kết nối từ điện thoại.



**Lưu ý**: Để biết thêm chi tiết về cấu hình đầy đủ của Bitcoin Core, hãy xem hướng dẫn chuyên dụng của chúng tôi:



https://planb.academy/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.academy/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3


### Yêu cầu về mạng



#### Xác định địa chỉ IP cục bộ của bạn



Điện thoại Android của bạn phải có khả năng kết nối đến nút Bitcoin trên mạng cục bộ. Tìm địa chỉ IP của máy tính:



**Trên macOS**:



```bash
ifconfig | grep "inet " | grep -v "127.0.0.1" | awk '{print $2}' | head -n 1
```



Giải pháp thay thế đơn giản:



```bash
ipconfig getifaddr en0
# or for WiFi: ipconfig getifaddr en1
```



**Trên Linux**:



```bash
hostname -I | awk '{print $1}'
```



**Trên Windows**:



```cmd
ipconfig
```



Tìm địa chỉ IPv4 (định dạng `192.168.x.x` hoặc `10.0.x.x`)



### Cấu hình RPC



#### Chỉnh sửa bitcoin.conf



![LOCALISATION BITCOIN.CONF](assets/fr/01.webp)



Xác định vị trí tệp `bitcoin.conf` của bạn:




- Linux**: `~/.bitcoin/bitcoin.conf
- macOS**: `~/Thư viện/Hỗ trợ ứng dụng/Bitcoin/bitcoin.conf
- Windows**: `%APPDATA%\Bitcoin\bitcoin.conf`



![CONTENU BITCOIN.CONF](assets/fr/02.webp)



Mở tệp bằng trình soạn thảo văn bản yêu thích của bạn và thêm cấu hình này để kích hoạt máy chủ RPC.



**Cấu hình được đề xuất để bắt đầu (đánh dấu trang)**:



```conf
# Enable signet (test network)
signet=1
prune=550

# Enable the RPC server
server=1
rpcbind=0.0.0.0

# Allow connections from your local network
# Adjust according to your network (192.168.x.0/24 or 10.0.x.0/24)
rpcallowip=192.168.1.0/24

# RPC Credentials (CHANGE THESE VALUES!)
rpcuser=your_username
rpcpassword=your_strong_password

# Specific signet configuration
[signet]
rpcport=38332
```



Cấu hình **mainnet** (dùng cho sản xuất):



```conf
# RPC Server
server=1
rpcbind=0.0.0.0
rpcallowip=192.168.1.0/24

# RPC Credentials
rpcuser=your_username
rpcpassword=your_strong_password

# Mainnet Port
rpcport=8332
```



**Quan trọng** :




- Signet được khuyến nghị mạnh mẽ** cho các thử nghiệm đầu tiên của bạn: ứng dụng vẫn đang trong giai đoạn phát triển (beta) và có thể vẫn còn lỗi. Signet cho phép bạn thử nghiệm miễn phí mà không cần phải mạo hiểm tiền thật.
- Thay thế `192.168.1.0/24` bằng mạng con của bạn (ví dụ: nếu IP của bạn là `192.168.68.57`, hãy sử dụng `192.168.68.0/24`)



**Bảo mật**: Tạo mật khẩu mạnh:



```bash
openssl rand -base64 32
```



### Khởi tạo



#### Khởi động lại và kiểm tra



1. Tắt hoàn toàn Bitcoin Core


2. Khởi động lại để áp dụng cấu hình




![SYNCHRONISATION BITCOIN CORE](assets/fr/03.webp)



Khi Bitcoin Core khởi động lần đầu tiên, nó sẽ tải xuống và đồng bộ hóa chuỗi khối bookmark. Thao tác này nhanh hơn nhiều so với mainnet (chỉ mất vài phút). Vui lòng đợi cho đến khi quá trình đồng bộ hóa hoàn tất trước khi tiếp tục.



![CRÉATION DE WALLET](assets/fr/04.webp)



Sau khi đồng bộ hóa, hãy tạo một danh mục đầu tư mới bằng cách nhấp vào "Tạo wallet mới". Đặt tên rõ ràng cho danh mục này, chẳng hạn như `tuto_joinstr_signet`.



![WALLET CRÉÉ](assets/fr/05.webp)



wallet của bạn hiện đã được tạo và sẵn sàng để nhận bitcoin đã đánh dấu để thử nghiệm.



#### Nhận bitcoin được đánh dấu (thử nghiệm)



Để kiểm tra Joinstr trên bookmark, bạn cần bitcoin thử nghiệm miễn phí:



![SIGNET FAUCET](assets/fr/06.webp)



Sử dụng dấu trang công khai như:




- [signetfaucet.com](https://signetfaucet.com)
- [alt.signetfaucet.com](https://alt.signetfaucet.com)
- [bookmark257.bublina.eu.org](https://signet257.bublina.eu.org)



Trong Bitcoin Core, generate, hãy tạo một địa chỉ nhận mới (tab "Nhận"), sao chép và dán vào biểu mẫu vòi. Giải mã captcha nếu cần. Bạn sẽ nhận được bitcoin được đánh dấu miễn phí trong vài giây.



## Ứng dụng Android



### Cài đặt



![APPLICATION ANDROID](assets/fr/07.webp)



Truy cập [gitlab.com/invincible-privacy/joinstr-kmp/-/releases](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases) để tải xuống phiên bản APK mới nhất. Trên trình duyệt Android, hãy tải xuống tệp, sau đó mở tệp để bắt đầu cài đặt. Bạn sẽ cần cho phép cài đặt từ các nguồn không xác định trong cài đặt bảo mật của điện thoại nếu cần.



### Cấu hình ứng dụng



![PERMISSIONS VPN](assets/fr/08.webp)



Khi khởi chạy lần đầu, ứng dụng Joinstr sẽ yêu cầu cấp quyền kiểm soát VPN tích hợp. Hãy chấp nhận cả hai yêu cầu cấp quyền: Kiểm soát OpenVPN và Kết nối VPN. Các quyền này là bắt buộc để tích hợp VPN, giúp bảo vệ quyền riêng tư mạng của bạn.



![INTERFACE APPLICATION](assets/fr/09.webp)



Ứng dụng Joinstr được tổ chức thành ba tab chính:




- Trang chủ**: Màn hình chính
- Nhóm**: Tạo và quản lý nhóm CoinJoin
- Cài đặt**: Cấu hình ứng dụng



![CONFIGURATION SETTINGS](assets/fr/13.webp)



Cấu hình cài đặt trong tab "Cài đặt":



**1. Chuyển tiếp Nostr**: Địa chỉ chuyển tiếp Nostr để điều phối nhóm




- Ví dụ: `wss://relay.damus.io`
- Các rơ le được đề xuất khác: `wss://nos.lol`, `wss://relay.nostr.band`, `wss://nostr.fmt.wiz.biz`
- ⚠️ **Quan trọng**: Tất cả người tham gia phải sử dụng **cùng một kênh tiếp sức Nostr** để xem và tham gia cùng một nhóm. Nếu bạn sử dụng một kênh tiếp sức khác, bạn sẽ không thấy các nhóm được tạo trên các kênh tiếp sức khác.



**2. URL nút**: Địa chỉ IP của nút Bitcoin của bạn (không có cổng)




- Định dạng: `http://VOTRE_IP_LOCALE`
- Ví dụ: `http://192.168.68.57`



**3. Tên người dùng RPC**: Tên người dùng được cấu hình trong `rpcuser=` trên bitcoin.conf của bạn




- Ví dụ: `satoshi



**4. Mật khẩu RPC**: Mật khẩu được đặt trong `rpcpassword=` trên bitcoin.conf của bạn



**5. Cổng RPC**: Cổng RPC tùy thuộc vào mạng




- Mainnet** : `8332`
- Đánh dấu**: `38332`



**6. Wallet**: Chọn danh mục đầu tư cốt lõi Bitcoin chứa các UTXO cần trộn




- Ví dụ: `tuto_joinstr_signet`



**7. Cổng VPN**: Chọn máy chủ Riseup VPN




- Ví dụ: `(Paris) vpn07-par.riseup.net`
- Những nơi khác có sẵn: Amsterdam, Seattle, v.v.
- ⚠️ **Quan trọng**: Tất cả người tham gia trong cùng một nhóm phải sử dụng **Cổng VPN** để tham gia CoinJoin. Trong vòng trộn, tất cả người tham gia phải xuất hiện với cùng một địa chỉ IP đầu ra để tránh việc phân tích mạng nhầm lẫn người tham gia.



Ứng dụng Joinstr **tích hợp gốc** Riseup VPN, giúp đơn giản hóa việc phối hợp giữa những người tham gia.



**Quan trọng** :




- Đảm bảo điện thoại và máy tính của bạn nằm trên cùng một mạng WiFi cục bộ
- Kết nối VPN sẽ được kích hoạt tự động khi tham gia vào một nhóm
- Nhấp vào **"Lưu"** sau khi bạn đã thiết lập tất cả các thông số



## Sử dụng thực tế



### Tạo hoặc tham gia một nhóm



![CRÉATION POOL ANDROID](assets/fr/10.webp)



Bạn có hai lựa chọn để tham gia CoinJoin:



**Tùy chọn 1: Tạo một nhóm mới**



Nhấp vào "Tạo nhóm mới" trong tab "Nhóm". Nhập mệnh giá BTC (ví dụ: 0,002 BTC) và số lượng người tham gia mong muốn (tối thiểu 2, khuyến nghị 3-5 để ẩn danh hơn). Sau đó, ứng dụng sẽ chờ người dùng khác tham gia nhóm của bạn. Khi đạt đến số lượng yêu cầu, quá trình đăng ký đầu ra sẽ tự động bắt đầu, và bạn sẽ cần chọn UTXO để trộn và nhấp vào "Đăng ký".



**⏱️ Quan trọng**: Nhóm sẽ hết hạn sau **10 phút** không hoạt động. Nếu không đủ số lượng người tham gia yêu cầu, nhóm sẽ tự động đóng.



**Lựa chọn 2: Tham gia nhóm hiện có**



Trong tab "Xem các nhóm khác", hãy duyệt qua các nhóm khả dụng do người dùng khác tạo. Chọn một nhóm tương ứng với số tiền của bạn và tham gia. Đảm bảo bạn đã cấu hình cùng một rơle Nostr và Cổng VPN như những người tham gia khác (xem phần Cấu hình).



**Quy tắc lựa chọn UTXO**: UTXO của bạn phải cao hơn một chút so với mệnh giá của nhóm (từ +500 đến +5000 thặng dư sats).



**Ví dụ**: Đối với nhóm 0,002 BTC (200.000 sats), hãy sử dụng UTXO giữa 200.500 và 205.000 sats.



![PROCESSUS COINJOIN](assets/fr/11.webp)



Quá trình sau đó hoàn toàn tự động: sau khi dữ liệu đầu vào của bạn đã được đăng ký, ứng dụng sẽ chờ tất cả người tham gia đăng ký dữ liệu đầu vào của họ. Khi tất cả dữ liệu đầu vào đã được đăng ký, PSBT sẽ được tạo, tự động ký bằng khóa của bạn, sau đó kết hợp với chữ ký của những người tham gia khác. Cuối cùng, toàn bộ giao dịch được phát trên mạng Bitcoin. Bạn sẽ nhận được TXID (mã định danh giao dịch) sau khi quá trình phát hoàn tất. Không cần thao tác thủ công trên PSBT trên Android.



### Xác minh on-chain



![TRANSACTION MEMPOOL](assets/fr/12.webp)



Sau khi giao dịch được phát sóng, bạn sẽ nhận được TXID (mã định danh giao dịch). Xem mã này trên [mempool.space](https://mempool.space) hoặc trình duyệt yêu thích của bạn. Để kiểm tra trên dấu trang, hãy sử dụng [mempool.space/signet](https://mempool.space/signet).



Bạn có thể quan sát:





- N mục nhập**: Một mục nhập cho mỗi người tham gia (trong ví dụ của chúng tôi, 2 mục nhập)
- N đầu ra giống hệt nhau**: số tiền chính xác theo mệnh giá (ở đây, 2 đầu ra, mỗi đầu ra 0,00199800 BTC)
- Biểu đồ luồng**: mempool.space hiển thị trực quan sự kết hợp giữa đầu vào và đầu ra
- Tính năng**: Giao dịch có thể được xác định là SegWit, Taproot, RBF, v.v.



Vì tất cả các đầu ra chính đều có cùng số lượng, nên **không thể xác định được đầu ra nào thuộc về ai**. Đây là nguyên tắc cơ bản của CoinJoin: tính không thể phân biệt được của các đầu ra.



**Ví dụ về chữ ký giao dịch**: [404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c](https://mempool.space/signet/tx/404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c)



**Xin lưu ý**: Nếu UTXO của bạn lớn hơn mệnh giá của nhóm, bạn sẽ có đầu ra ngoại hối (thặng dư). Các UTXO giao dịch này vẫn có thể theo dõi được và phải được quản lý riêng biệt với các đầu ra ẩn danh của bạn. Không bao giờ kết hợp chúng với các đầu ra hỗn hợp của bạn.



## Gói chất lượng và ẩn danh CoinJoin



Hiệu suất của CoinJoin được đo bằng **anonset**: số lượng đầu ra có giá trị giống hệt nhau được tạo ra bởi giao dịch. Con số này càng cao, việc xác định đầu vào nào tương ứng với đầu ra nào càng khó khăn.



Joinstr hiện tạo ra các nhóm trung bình từ **2 đến 5 người tham gia**. Những con số này thấp hơn so với các điều phối viên tập trung truyền thống như Wasabi (50-100 người tham gia) hoặc Whirlpool (5-10 người tham gia), nhưng đó là cái giá phải trả của sự phi tập trung.



💡 **Để hiểu chi tiết về tập ẩn danh và cách tính của chúng**, hãy xem khóa học đầy đủ của chúng tôi: [Tập ẩn danh](https://planb.academy/fr/courses/65c138b0-4161-4958-bbe3-c12916bc959c/les-ensembles-danonymat-be1093dc-1a74-40e5-9545-2b97a7d7d431).



### Joinstr so với các CoinJoin khác




| Khía cạnh | Wasabi | Whirlpool/Ashigaru | JoinMarket | **Joinstr** |
|--------|--------|--------------------|------------|-------------|
| **Người tham gia trên mỗi hồ** | 50-100 | 5-10 | Biến đổi (P2P) | **2-5** |
| **Người phối hợp** | Tập trung (đóng 2024) | Tập trung (hoạt động) | P2P maker/taker | **Không (Nostr)** |
| **Khả năng chống lại kiểm duyệt** | Yếu | Trung bình | Rất cao | **Rất cao** |
| **Phí phối hợp** | Phần trăm | Phí vào cửa | Trả cho các nhà sáng tạo | **Không** |
| **Phân biệt UTXO** | Có (danh sách đen) | Không | Không | **Không** |

💡 **Các giải pháp CoinJoin đang hoạt động khác**:




- Ashigaru**: Triển khai mã nguồn mở giao thức Whirlpool với bộ điều phối tập trung nhưng có thể triển khai theo cách phi tập trung. Tiếp tục hoạt động sau khi Samourai Wallet bị chiếm giữ vào năm 2024.
- JoinMarket**: Giải pháp P2P phi tập trung không có điều phối viên trung tâm, dựa trên mô hình kinh doanh người tạo ra/người mua trong đó "người tạo ra" cung cấp thanh khoản và được "người mua" trả tiền.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add

**Sự đánh đổi cơ bản**: Joinstr và JoinMarket là hai giải pháp duy nhất không có bộ điều phối trung tâm. JoinMarket sử dụng mô hình kinh doanh P2P với các ưu đãi tài chính, trong khi Joinstr sử dụng Nostr để điều phối miễn phí. Joinstr hy sinh tính ẩn danh tức thời trên quy mô lớn để đổi lấy sự đơn giản (không quản lý người tạo/người nhận) và hoàn toàn không có phí điều phối.



**Khuyến nghị thực tế**: Để bù đắp cho các nhóm nhỏ, hãy chạy nhiều vòng CoinJoin liên tiếp với nhiều người tham gia khác nhau. Hãy giãn cách các vòng chơi và thay đổi rơle Nostr giữa mỗi vòng để tối đa hóa tính bảo mật của bạn.



Hãy thoải mái tham khảo khóa học đầy đủ của chúng tôi về quyền riêng tư bitcoin để biết thêm thông tin về chủ đề này:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Ưu điểm và hạn chế



### Điểm nổi bật



**Nâng cao quyền riêng tư**: Sự kết hợp giữa mã hóa truyền thông Nostr, VPN chia sẻ giữa những người tham gia và khuyến nghị sử dụng Tor tạo ra lớp bảo vệ nhiều lớp khó có thể vượt qua.



**Minh bạch, chi phí tối thiểu**: Không có chi phí điều phối, chỉ có chi phí mining được chia đều cho những người tham gia. Không có nhà điều hành nào thu phần trăm nào.



### Những hạn chế cần xem xét





- Tính thanh khoản thay đổi**: Các nhóm nhỏ hơn, có thể chờ những người tham gia tập hợp lại
- Dự án đang tiến hành**: Ứng dụng đang trong giai đoạn beta, có thể có lỗi. Hãy thử nghiệm trước với một lượng nhỏ trên bookmark.
- Sybil tấn công**: Khả năng một đối thủ điều khiển nhiều người tham gia nhóm



## Thực hành tốt nhất



**Cách ly UTXO**: Không bao giờ kết hợp UTXO đã trộn với UTXO chưa trộn. Hãy sử dụng một danh mục riêng cho các đầu ra ẩn danh của bạn.



**Cần thực hiện nhiều vòng**: Thực hiện tối thiểu 3 vòng liên tiếp với nhiều người tham gia khác nhau. Thay đổi số lượng và thời gian để tránh trùng lặp. Các vòng cách nhau vài giờ.



**Bảo vệ mạng**: Sử dụng Tor một cách có hệ thống bên cạnh VPN tích hợp. Tạo khóa Nostr tạm thời cho mỗi phiên làm việc quan trọng.



**Tiến triển thận trọng**: Bắt đầu đánh dấu trang với số lượng nhỏ.



## Phần kết luận



Joinstr đại diện cho một giải pháp bảo mật Bitcoin thực sự phi tập trung. Bằng cách sử dụng Nostr để điều phối, giải pháp này loại bỏ sự phụ thuộc vào các điều phối viên trung tâm, đồng thời bảo vệ quyền chủ quyền của người dùng.



**Dành cho người dùng coi trọng khả năng chống kiểm duyệt và sẵn sàng thực hiện nhiều vòng CoinJoin để bù đắp cho các nhóm nhỏ hơn.



Trong bối cảnh giám sát tài chính ngày càng tăng, các công cụ phi tập trung để bảo vệ quyền riêng tư đang trở nên cần thiết.



## Tài nguyên



### Tài liệu chính thức




- [Trang web chính thức của Joinstr](https://joinstr.xyz)
- [Tài liệu hướng dẫn sử dụng](https://docs.joinstr.xyz/users/using-joinstr)
- [Tài liệu kỹ thuật](https://docs.joinstr.xyz/overview/how-does-it-work)
- [Mã nguồn GitLab](https://gitlab.com/invincible-privacy/joinstr)
- [Ứng dụng Android](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases)



### Hướng dẫn




- [Hướng dẫn sử dụng plugin Electrum](https://uncensoredtech.substack.com/p/tutorial-electrum-plugin-for-joinstr) - Hướng dẫn đầy đủ từ Uncensored Tech



### Cộng đồng và hỗ trợ




- [Telegram Joinstr Group](https://t.me/joinstr) - Hỗ trợ cộng đồng và góc đánh dấu trang
- [Thảo luận kỹ thuật về DelvingBitcoin](https://delvingbitcoin.org/t/who-will-run-the-coinjoin-coordinators/934)



### Công cụ bổ sung




- [Đánh dấu Faucet](https://signetfaucet.com) - Dùng thử Bitcoin miễn phí
- [Alt Signet Faucet](https://alt.signetfaucet.com) - Lựa chọn thay thế cho Faucet
- [Mempool.space](https://mempool.space) - Block explorer với phân tích quyền riêng tư