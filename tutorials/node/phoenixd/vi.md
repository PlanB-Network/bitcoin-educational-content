---
name: Phoenixd
description: Triển khai nút Lightning tối giản của riêng bạn với Phoenixd
---

![cover](assets/cover.webp)



Tự chủ tài chính cũng đồng nghĩa với việc kiểm soát cơ sở hạ tầng Lightning của bạn. Đối với các nhà phát triển và công ty muốn tích hợp Bitcoin Lightning vào ứng dụng của mình, **Phoenixd** là giải pháp lý tưởng: một node Lightning tối giản, chuyên biệt với khả năng quản lý thanh khoản tự động.



Phoenixd là máy chủ Lightning do ACINQ phát triển, được thiết kế chuyên biệt để gửi và nhận thanh toán Lightning thông qua API HTTP. Không giống như các giải pháp triển khai đầy đủ tính năng như LND hoặc Core Lightning, Phoenixd trừu tượng hóa mọi sự phức tạp của việc quản lý kênh trong khi vẫn đảm bảo tính tự bảo vệ tiền của bạn.



Trong hướng dẫn này, chúng ta sẽ xem cách cài đặt, cấu hình và sử dụng Phoenixd để phát triển các ứng dụng Lightning với cơ sở hạ tầng tự lưu trữ và API dễ sử dụng.



## Phoenixd là gì?



Phoenixd là một node Lightning tối giản, chuyên biệt do ACINQ phát triển. Đây là giải pháp được thiết kế dành cho các nhà phát triển và doanh nghiệp muốn tích hợp Lightning vào ứng dụng của họ mà không cần phải quản lý phức tạp như Full node.



### Nguyên lý hoạt động



**Phoenixd là một nút Lightning tối thiểu sử dụng ACINQ làm LSP (Nhà cung cấp dịch vụ Lightning) để tự động thanh khoản. Khi bạn nhận được thanh toán Lightning, nó sẽ tự động mở các kênh với các nút ACINQ để phân bổ dung lượng đầu vào cần thiết. Tính thanh khoản "ngay lập tức" này diễn ra tức thời, nhưng được tính phí chính xác **1% + phí Mining** trên số tiền nhận được.



**Quản lý tự động:** Hệ thống quản lý ba Elements chính:




- Kênh Lightning**: Tự động mở, đóng và quản lý khi cần
- Thanh khoản đến/đi**: Tự động cung cấp thông qua việc ghép nối và mở kênh
- Tín dụng phí**: Các khoản thanh toán nhỏ không đủ để biện minh cho một kênh được lưu trữ như một khoản dự phòng cho các khoản phí trong tương lai



### Lợi ích của Phoenixd



**Bạn kiểm soát khóa riêng (seed 12 từ) và tiền của mình. Phoenixd tạo Wallet cục bộ mà không cần chia sẻ khóa.



**Cơ sở hạ tầng cá nhân:** Phoenixd chạy trên máy chủ của bạn, cho phép bạn truy cập nhật ký chi tiết, cấu hình và kiểm soát API. Bạn không còn phụ thuộc vào dịch vụ của bên thứ ba để truy cập vào tiền của mình nữa.



**API tích hợp:** Phoenixd có API HTTP để tích hợp với các dịch vụ khác, hỗ trợ LNURL gốc và phát triển ứng dụng tùy chỉnh.



**Dễ dàng tích hợp:** Nhờ REST API đơn giản, Phoenixd có thể được tích hợp vào bất kỳ ứng dụng hoặc dịch vụ nào yêu cầu thanh toán Lightning.



**Lưu ý quan trọng:** Tính thanh khoản tự động vẫn đến từ ACINQ với tư cách là Nhà cung cấp dịch vụ Lightning (LSP). Phoenixd sử dụng cơ chế tương tự như Phoenix Mobile để quản lý kênh tự động.



## Cài đặt Phoenixd



### Điều kiện tiên quyết



Phoenixd yêu cầu môi trường Linux (khuyến nghị Ubuntu/Debian) và một số kỹ năng dòng lệnh cơ bản. Để có hiệu suất tối ưu, bạn cần:





- Máy chủ Linux**: VPS hoặc máy cục bộ có kết nối ổn định
- OpenJDK 21**: Môi trường chạy Java
- Kết nối Internet ổn định**: Để đồng bộ hóa với Lightning Network
- Tên miền** (tùy chọn): Để truy cập HTTPS an toàn vào API



### Tải xuống và cài đặt



**1. Tải xuống Phoenixd**



Truy cập trang [Bản phát hành GitHub] (https://github.com/ACINQ/phoenixd/releases) và tải xuống phiên bản mới nhất cho kiến trúc của bạn:



```bash
# For Linux x86_64
# Replace with the latest release
wget https://github.com/ACINQ/phoenixd/releases/download/v0.6.1/phoenixd-0.6.1-linux-x64.zip
unzip -j phoenixd-0.6.1-linux-x64.zip
chmod +x phoenixd phoenix-cli
```



**2. Khởi động lần đầu



Khởi động Phoenixd để khởi tạo:



```bash
./phoenixd
```



Khi khởi chạy lần đầu, bạn sẽ được yêu cầu xác nhận hai bước quan trọng bằng cách nhập "Tôi hiểu":



**Tin nhắn 1 - Sao lưu:**


```
This software is self-custodial, you have full control and responsibility over your funds.
Your 12-words seed is located in /home/<user>/.phoenix, make sure to do a backup or you risk losing your funds.
Do not share the same seed with other phoenix instances (mobile or server), it will cause issues and channel force closes.
```



**Lưu lại 12 từ này** - đây là cách duy nhất đảm bảo bạn sẽ phục hồi.



**Tin nhắn 2 - Thanh khoản tự động:**


```
Continuous liquidity
Liquidity management is fully automated.
When receiving a Lightning payment that doesn't fit in your existing channel:
- If the payment amount is large enough to cover mining fees and service fees for automated liquidity,
then your channel will be created or enlarged right away.
- If the payment is too small, then the full amount is added to your fee credit,
and will be used later to pay for future fees. The fee credit is non-refundable.
```



Nhập `Tôi hiểu` cho mỗi xác nhận.



![Premier démarrage](assets/fr/01.webp)



*Phoenixd khởi động lần đầu tiên: xác nhận sao lưu và thanh khoản tự động*



**3. Cấu hình trong quá trình sử dụng** (chỉ có tiếng Pháp)



Để hoạt động liên tục, hãy tạo systemd:



```bash
sudo nano /etc/systemd/system/phoenixd.service
```



```ini
[Unit]
Description=Phoenixd - Minimalist Lightning node
After=network.target

[Service]
User=your_user
WorkingDirectory=/home/your_user
ExecStart=/home/your_user/phoenixd
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```



```bash
sudo systemctl daemon-reload
sudo systemctl enable phoenixd
sudo systemctl start phoenixd
```



![Service systemd](assets/fr/02.webp)



*Dịch vụ Phoenixd đang hoạt động thông qua systemd và `auto-liquidity` tại 2m sat*



## Cấu hình và bảo mật



### Tệp cấu hình



Phoenixd tự động tạo `~/.phoenix/phoenix.conf` với các tham số cần thiết:



```conf
# Network (mainnet by default)
chain=mainnet

# Size of automatic channels and requested liquidity amount (in satoshis)
auto-liquidity=2000000

# API configuration
http-bind-address=127.0.0.1
http-bind-port=9740
http-password=auto_generated_password
http-password-limited-access=limited_password
```



**Các thông số chính:**




- `auto-liquidity`: Kích thước của các kênh tự động mở (mặc định: 2M Sats)
- http-password`: Mật khẩu quản trị cho API (tạo Invoice VÀ gửi thanh toán)
- http-password-limited-access`: Mật khẩu bị hạn chế (chỉ dành cho việc tạo Invoice)



### Truy cập an toàn với HTTPS



Theo mặc định, API Phoenixd chỉ có thể truy cập qua HTTP cục bộ (`http://127.0.0.1:9740`). Để sử dụng nút của bạn từ bên ngoài (ứng dụng di động, máy chủ khác, tích hợp web), bạn cần cấu hình quyền truy cập HTTPS an toàn.



**Nguyên tắc proxy ngược:**


```
Internet → nginx (port 443 HTTPS) → Phoenixd (port 9740 HTTP local)
```



**Nginx** hoạt động như một **proxy ngược**: nó lắng nghe các yêu cầu HTTPS từ Internet trên cổng 443, chuyển hướng chúng đến Phoenixd cục bộ (cổng 9740), sau đó gửi phản hồi được mã hóa trở lại máy khách.



**Chứng chỉ SSL/TLS** là một tệp kỹ thuật số:




- Chứng minh danh tính máy chủ của bạn** (ngăn chặn các cuộc tấn công trung gian)
- Cho phép mã hóa HTTPS**: tất cả dữ liệu, bao gồm cả mật khẩu API của bạn, đều được mã hóa trong quá trình truyền tải
- Được phát hành miễn phí** bởi Let's Encrypt thông qua công cụ certbot



Cấu hình này cho phép bạn:




- Truy cập an toàn vào API từ Internet**
- Mã hóa mật khẩu API** của bạn trong quá trình truyền tải (để tránh việc chúng được truyền dưới dạng văn bản thuần túy)
- Tích hợp Phoenixd** vào các ứng dụng bên ngoài yêu cầu HTTPS
- Tuân thủ các tiêu chuẩn bảo mật** cho API tài chính



Cấu hình proxy ngược HTTPS này với nginx:



**1. Cấu hình Nginx**



```bash
sudo apt install nginx certbot python3-certbot-nginx
sudo nano /etc/nginx/sites-available/phoenixd.conf
```



```nginx
server {
listen 80;
server_name phoenixd.your-domain.com;

location / {
proxy_pass http://127.0.0.1:9740;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header Host $host;
}
}
```



```bash
sudo ln -s /etc/nginx/sites-available/phoenixd.conf /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```



**2. Chứng chỉ SSL**



```bash
sudo certbot --nginx -d phoenixd.your-domain.com
```



### Kiểm tra chức năng



Kiểm tra xem Phoenixd có hoạt động bình thường không:



```bash
./phoenix-cli getinfo
./phoenix-cli getbalance
```



Các lệnh này sẽ trả về thông tin JSON về trạng thái và số dư của nút (ban đầu là trống).



![Commandes CLI](assets/fr/03.webp)



*Lệnh Getinfo và getbalance để kiểm tra trạng thái nút*



## Sử dụng API



### Bài kiểm tra tiếp nhận đầu tiên



**1. Tạo ra tia sét** Invoice



Sử dụng API để tạo Invoice đầu tiên của bạn:



```bash
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='First test' \
-d amountSat=100000
```



### Hiểu về cơ chế thanh khoản tự động



**Nguyên tắc cơ bản:** Khi bạn nhận được khoản thanh toán Lightning, Phoenixd đôi khi phải mở một kênh mới để có thể nhận được. Việc mở kênh này sẽ mất một khoản phí, khoản phí này **sẽ được tự động khấu trừ** vào số tiền nhận được.



**Ví dụ cụ thể với 100.000 Sats:**



![Premier test de réception](assets/fr/04.webp)



*Kiểm tra chấp nhận đầu tiên: Sats đã nhận 100 nghìn, số dư cuối cùng của Sats là 75.561 sau khi trừ chi phí thanh khoản*



```bash
# Payment received: 100,000 sats
# Channel created: 2,115,000 sats total capacity
# Liquidity fee: 24,439 sats
# Final balance: 75,561 sats
```



**Tính phí:**




- Phí dịch vụ**: 1% dung lượng kênh (2.115.000 Sats) = 21.150 Sats
- Phí Mining**: ~3.289 Sats (cho giao dịch On-Chain)
- Tổng cộng**: 24.439 Sats được khấu trừ tự động



**Xác minh bằng lệnh CLI:**


```bash
# View details of all channels
./phoenix-cli listchannels

# Important output:
# "toLocal": 75561000 (your balance in milli-sats)
# "toRemote": 2039439000 (ACINQ's balance)
# Total channel: 2,115,000 sats
```



![Nouveau solde après paiement](assets/fr/05.webp)



*Số dư cuối cùng sau khi thanh toán: Còn lại 257 Sats sau khi giao hàng Lightning*



**Tín dụng phí cho các khoản thanh toán nhỏ:** Nếu bạn nhận được các khoản thanh toán quá nhỏ để mở kênh (< khoảng 25k Sats), chúng sẽ được lưu trữ trong một "tín dụng phí" không hoàn lại. Tín dụng này sẽ được sử dụng để thanh toán phí kênh trong tương lai khi bạn nhận được một số tiền đủ lớn.



**2. Theo dõi kênh mở**



Xem nhật ký Phoenixd:



```bash
journalctl -u phoenixd -f
```



Bạn sẽ thấy kênh mở và phí thanh khoản được tự động khấu trừ. Phí thay đổi tùy theo điều kiện Mempool Bitcoin, nhưng luôn bao gồm 1% phí dịch vụ cộng với phí Mining hiện hành.



**3. Kiểm tra kênh**



```bash
./phoenix-cli listchannels
```



Lệnh này hiển thị các kênh đang hoạt động của bạn cùng với trạng thái và số dư của chúng.



### Hoàn thành các hoạt động API



Phoenixd cung cấp REST API trên cổng 9740 cho phép:



**Các thao tác cơ bản:**


```bash
# Create an invoice
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='Test payment' \
-d amountSat=100000

# Send a payment (routing fee 0.4%)
curl -X POST http://localhost:9740/payinvoice \
-u :your_password \
-d invoice='lnbc...'

# Check balance
curl http://localhost:9740/getbalance \
-u :your_password

# Send on-chain funds (in case of channel closure)
./phoenix-cli sendtoaddress \
--address bc1q... \
--amountSat 50000 \
--feerateSatByte 12
```



**Quan trọng về chi phí:**




- Biên lai**: 1% + phí Mining cho thanh khoản tự động
- Vận chuyển**: Phí định tuyến 0,4% cho Lightning Network



**Webhooks:** Webhooks cho phép Phoenixd **tự động thông báo** cho ứng dụng của bạn khi có sự kiện xảy ra (đã nhận thanh toán, Invoice đã thanh toán, kênh đã mở, v.v.). Thay vì liên tục yêu cầu Phoenixd cập nhật, ứng dụng của bạn sẽ nhận được thông báo HTTP ngay lập tức.



**Cửa hàng trực tuyến của bạn sẽ tự động nhận được thông báo khi khách hàng thanh toán đơn hàng, cho phép xác thực giao dịch ngay lập tức.



Cấu hình trong `phoenix.conf`:


```conf
webhook-url=https://your-app.com/webhook-phoenixd
webhook-secret=votre_secret_de_verification
```



## Ứng dụng nâng cao



### Tích hợp LNURL



Phoenixd hỗ trợ giao thức LNURL để tích hợp nâng cao:



**LNURL-Pay:** Thanh toán cho các dịch vụ tương thích với LNURL


```bash
curl -X POST http://localhost:9740/lnurlpay \
-u :your_password \
-d lnurl=LNURL1DP68GURN8GHJ7MRWW4EXCTN... \
-d amountSat=100
```



**LNURL-Withdraw :** Lấy tiền từ các dịch vụ LNURL


```bash
curl -X POST http://localhost:9740/lnurlwithdraw \
-u :your_password \
-d lnurl=lightning:LNURL1DP68GURN8GHJ7MRW...
```



**LNURL-Auth:** Xác thực qua Lightning để truy cập các dịch vụ


```bash
curl -X POST http://localhost:9740/lnurlauth \
-u :your_password \
-d lnurl=lnurl1dp68gurn8ghj7um5v93kket...
```



### Tích hợp với LNbits



LNbits có thể sử dụng Phoenixd làm nguồn tài trợ theo [tài liệu chính thức](https://docs.lnbits.org/guide/wallets.html):



**Cấu hình LNbits:**


```bash
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://localhost:9740/
PHOENIXD_API_PASSWORD=your_password_phoenixd
```



Sự tích hợp này cho phép bạn tạo các tài khoản phụ LNbits được hỗ trợ bởi nút Phoenixd của bạn, cung cấp Interface dựa trên web để quản lý nhiều ví Lightning.



### Ứng dụng tùy chỉnh



Nhờ có REST API toàn diện, bạn có thể phát triển:



**Thương mại điện tử:** Tích hợp trực tiếp thanh toán Lightning vào cửa hàng của bạn


**Dịch vụ quyên góp:** Hệ thống quyên góp có hóa đơn và webhook tự động


**Bot mạng xã hội:** Bot Telegram/Discord có chức năng tiền boa


**Paywall Lightning:** Nội dung cao cấp có sẵn với mức phí Lightning



## An toàn và thực hành tốt nhất



### Bảo vệ quyền truy cập



**Mật khẩu API:** Mật khẩu được tạo tự động là chìa khóa để truy cập kho bạc Lightning của bạn. Tuyệt đối không chia sẻ chúng và hãy thay đổi nếu nghi ngờ.



**Tường lửa:** Không bao giờ để cổng 9740 mở trực tiếp ra Internet. Luôn sử dụng nginx với HTTPS.



**Xác thực nâng cao:** Hãy cân nhắc sử dụng VPN hoặc Tailscale để hạn chế quyền truy cập vào máy chủ của bạn chỉ dành cho các thiết bị được ủy quyền.



### Sao lưu thiết yếu



**Phục hồi seed:** Lưu 12 từ của bạn ở nơi an toàn, ngoài máy chủ. Đây là đảm bảo duy nhất cho việc phục hồi của bạn.



*~/.phoenix directory:** Sao lưu thư mục này thường xuyên (sau khi Phoenixd đã tắt) để bảo toàn trạng thái kênh và tăng tốc độ khôi phục.



**Mã khôi phục dịch vụ:** Ngoài ra, hãy giữ mã sao lưu cho tất cả các dịch vụ mà bạn kích hoạt 2FA bằng Phoenix của mình.



### Giám sát và bảo trì



**Nhật ký giám sát:**


```bash
journalctl -u phoenixd -f  # Real-time logs
./phoenix-cli getinfo      # Node status
```



**Cập nhật:** Theo dõi [Bản phát hành GitHub](https://github.com/ACINQ/phoenixd/releases) để biết phiên bản mới. Việc cập nhật rất đơn giản, chỉ cần thay thế tệp nhị phân và khởi động lại dịch vụ.



## So sánh với các lựa chọn thay thế



### Phoenixd so với Phoenix tiêu chuẩn



**Phoenix tiêu chuẩn (di động) :**




- ✅ Cài đặt ngay lập tức, không cần cấu hình
- ✅ Interface di động trực quan
- ✅ Tự động lưu giống như Phoenixd
- ❌ Không có API dành cho nhà phát triển
- ❌ Không có quyền truy cập vào nhật ký chi tiết



**Phoenixd (máy chủ) :**




- ✅ API HTTP để tích hợp
- ✅ Truy cập đầy đủ vào nhật ký
- ✅ Cơ sở hạ tầng cá nhân
- ❌ Yêu cầu kỹ năng kỹ thuật
- ❌ Cần bảo trì máy chủ



**Cả hai đều sử dụng ACINQ làm LSP để thanh khoản tự động.



### Phoenixd so với LND/Core Lightning



**LND/Core Lightning :**




- ✅ Kiểm soát toàn diện, giao thức Lightning đầy đủ
- ✅ Cộng đồng lớn, hệ sinh thái trưởng thành
- ❌ Quản lý thanh khoản thủ công phức tạp
- ❌ Đường cong học tập lớn



**Phoenixd :**




- ✅ Quản lý thanh khoản tự động (giống như Phoenix mobile)
- ✅ API dành cho nhà phát triển
- ✅ Cấu hình đơn giản
- ❌ Sử dụng ACINQ làm LSP (không có định tuyến độc lập)
- ❌ Ít linh hoạt hơn các nút hoàn chỉnh



## Giải quyết các vấn đề thường gặp



### Các vấn đề truy cập API



Lỗi **Xác thực không thành công:**


1. Kiểm tra mật khẩu trong tệp `~/.phoenix/phoenix.conf`


2. Kiểm tra định dạng xác thực `-u:password`


3. Đảm bảo Phoenixd đang chạy (`./phoenix-CLI getinfo`)



**Hết thời gian kết nối:**




- Kiểm tra xem Phoenixd có đang lắng nghe trên cổng chính xác (9740) không
- Kiểm tra quyền truy cập cục bộ trước khi cấu hình HTTPS
- Kiểm tra nhật ký: `journalctl -u phoenixd -f`



### Vấn đề thanh khoản



**Thanh toán không đến :**


1. Kiểm tra xem số lượng có vượt quá ngưỡng tối thiểu không (~30k Sats)


2. Tham khảo nhật ký để xác định lỗi kênh


3. Khởi động lại Phoenixd nếu cần thiết



**Số dư trong "tín dụng chi phí":**


Các khoản thanh toán nhỏ được lưu trữ như một khoản dự phòng. Nhận số tiền lớn hơn để kích hoạt việc mở kênh và giải ngân số tiền này.



## Phần kết luận



Phoenixd là sự kết hợp hoàn hảo giữa tính dễ sử dụng và khả năng quản lý kỹ thuật tối ưu cho các nhà phát triển. Nó cung cấp một API Lightning đơn giản nhưng mạnh mẽ với khả năng quản lý thanh khoản tự động, loại bỏ sự phức tạp của các nút Lightning truyền thống.



Giải pháp này đặc biệt phù hợp với các nhà phát triển và công ty muốn:




- Tích hợp Bitcoin Lightning vào ứng dụng của bạn
- Tránh sự phức tạp của việc quản lý kênh Lightning
- Tận dụng cơ sở hạ tầng tự lưu trữ
- Một API đơn giản và đáng tin cậy



Với Phoenixd, bạn có thể xây dựng cơ sở hạ tầng Lightning riêng với REST API hiện đại và quản lý tự động các khía cạnh kỹ thuật. Đây là giải pháp lý tưởng để dân chủ hóa việc tích hợp Lightning vào các dự án của bạn.



## Tài nguyên hữu ích



### Tài liệu chính thức




- GitHub Phoenixd** : [github.com/ACINQ/phoenixd](https://github.com/ACINQ/phoenixd) - Mã nguồn và bản phát hành
- Trang web Phoenix Server**: [phoenix.acinq.co/server](https://phoenix.acinq.co/server) - Tài liệu đầy đủ
- Câu hỏi thường gặp về Phoenixd**: [phoenix.acinq.co/server/faq](https://phoenix.acinq.co/server/faq) - Câu hỏi thường gặp



### Hỗ trợ cộng đồng




- GitHub Issues**: [github.com/ACINQ/phoenixd/issues](https://github.com/ACINQ/phoenixd/issues) - Hỗ trợ kỹ thuật
- Twitter ACINQ** : [@ACINQ_co](https://twitter.com/ACINQ_co) - Tin tức và thông báo