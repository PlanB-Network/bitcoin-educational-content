---
name: Điều phối viên Coinjoin - WabiSabi
description: Hướng dẫn thiết lập và vận hành bộ điều phối coinjoin theo giao thức WabiSabi (được sử dụng trong Wasabi Wallet 2.0)
---

![cover](assets/cover.webp)


---

## Giới thiệu 👋


Trong hướng dẫn chuyên sâu này, chúng tôi sẽ giúp bạn thiết lập một máy chủ điều phối coinjoin, về cơ bản là một máy chủ kết nối những người muốn tiết kiệm phí giao dịch hoặc tăng cường quyền riêng tư trên chuỗi trong các giao dịch hợp tác. Vì hiện không còn máy chủ điều phối do công ty cung cấp được tích hợp sẵn trong Wasabi Wallet, người dùng phải tự tìm và chọn máy chủ điều phối ưa thích của mình. Chỉ có một vài máy chủ điều phối xuất hiện với mức phí điều phối 0%, vì vậy các nhà phát triển của Wasabi Wallet đã nỗ lực hết sức để giúp việc bắt đầu vận hành máy chủ điều phối cộng đồng của riêng bạn trở nên dễ dàng nhất có thể (trên phần cứng nhỏ như Raspberry Pi5!). Các máy chủ điều phối hiện đang hoạt động với mức phí điều phối 0% có thể được tìm thấy trên [LiquiSabi](https://liquisabi.com) và quan trọng hơn là trên [nostr](https://github.com/Kukks/WasabiNostr).


## Yêu cầu 🫴



- VPS (máy chủ ảo) hoặc máy tính/máy chủ vật lý (máy chủ tự lưu trữ)
- Nút lõi Bitcoin đã được cắt tỉa/đầy đủ (đã thử nghiệm với phiên bản v29.0)


Không bắt buộc:


- (Tên miền phụ) Chuyển tiếp lưu lượng truy cập đến nút (ví dụ: coinjoin.[tên miền của bạn].io)


Bạn nên có một chút kinh nghiệm sử dụng dòng lệnh và bash, vì không phải tất cả các bước đều có thể tự động hóa.


Về phần cứng, nên trang bị một hệ thống có cấu hình như sau:


- 4 lõi
- RAM 16 GB
- Ổ cứng SSD hoặc NVMe 2 TB (cho node đầy đủ) / Ổ cứng SSD 128 GB (cho node pruned)


Những yêu cầu đó có thể được đáp ứng bởi một chiếc Raspberry Pi 5 với giá chỉ 120 đô la, chưa bao gồm ổ lưu trữ có giá khoảng 100 đô la cho một chiếc NVMe 2TB.


Các VPS giá rẻ thường chỉ có 1 lõi xử lý và 4GB RAM, theo kinh nghiệm của tôi thì dung lượng này quá ít để đồng bộ và xác minh toàn bộ cổng blockchain của Bitcoin ở độ cao khối 911817.


Về dung lượng lưu trữ, một node đầy đủ sẽ cần tối thiểu 2TB ổ cứng, tốt nhất là loại SSD hoặc NVMe. Khi tinh chỉnh blockchain, ổ cứng có dung lượng nhỏ hơn nhiều cũng được chấp nhận (ví dụ: SSD 128GB).


Nếu bạn dự định chạy một bộ điều phối cho các yêu cầu coinjoin lớn (300+ đầu vào), bạn nên chọn một hệ thống có lõi xử lý nhanh hơn/mới hơn với hiệu năng cao hơn cho tất cả các xác minh chữ ký.


## Lắp đặt 🛠️


Trên máy chủ này, chúng ta muốn tải xuống và cài đặt phiên bản Wasabi Wallet mới nhất, bao gồm cả phần phụ trợ và bộ điều phối dưới dạng các tệp thực thi độc lập bên cạnh wallet.


Tìm phiên bản mới nhất: [Wasabi Wallet](https://github.com/WalletWasabi/WalletWasabi/releases) và xác minh chữ ký PGP của bản phát hành bằng các khóa: [PGP.txt](https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt)


Chi tiết triển khai khác nhau tùy thuộc vào phần cứng (kiến trúc CPU) và lựa chọn hệ điều hành. Dưới đây là các chi tiết khác nhau dành cho Raspberry Pi (ARM-64) với RaspiBlitz dựa trên Debian làm điểm khởi đầu. Chuyển đến phần triển khai hệ điều hành Ubuntu (X86-64) sử dụng Nix.


Bạn có thể tìm hướng dẫn cài đặt tại đây: [Wasabi Docs](https://docs.wasabiwallet.io/using-wasabi/InstallPackage.html)


### Triển khai RaspiBlitz/Debian


Đối với các node RaspiBlitz (đã thử nghiệm với phiên bản v1.11), có thể sử dụng bản dựng triển khai script được xây dựng từ mã nguồn: [home.admin/config.scripts/bonus.wasabi.sh](https://github.com/kravens/raspiblitz/blob/dev/home.admin/config.scripts/bonus.wasabi.sh)



### Dễ dàng triển khai


Đối với việc triển khai tối thiểu, bạn chỉ cần giải nén các tệp thực thi dành cho nền tảng của mình vào một thư mục.

Ví dụ mã lệnh dòng lệnh cho Debian/Ubuntu:


```
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb.asc
wget https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt
gpg --import PGP.txt
gpg --verify Wasabi-2.7.2.deb.asc Wasabi-2.7.2.deb
```


Điều này sẽ tạo ra thông báo chữ ký hợp lệ sau:


```
gpg: Signature made Mon Nov 17 01:33:09 2025 CET
gpg:                using RSA key 6FB3872B5D42292F59920797856348328949861E
gpg: Good signature from "zkSNACKs <zksnacks@gmail.com>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 6FB3 872B 5D42 292F 5992  0797 8563 4832 8949 861E
```


Sau đó, bạn có thể tiến hành cài đặt gói đã tải xuống:


```
sudo apt install ./Wasabi-2.7.2.deb
```



## Cấu hình 🧾


Trước khi chạy trình điều phối, bạn cần chỉnh sửa tệp Config.json với các thông tin sau:


- Thông tin xác thực Bitcoin RPC
- Các thông số làm tròn được ưu tiên
- Khóa công khai mở rộng của điều phối viên (tạo SegWit wallet mới để nhận bụi đã thu thập)

**Cảnh báo**: Taproot wallet sẽ dẫn đến UTXO không thể sử dụng được! Hãy sử dụng Native Segwit wallet ở đây.


- Các loại địa chỉ đầu vào và đầu ra được cho phép
- Cấu hình thông báo để phát hành qua nostr (tên, mô tả, Uri, các thông tin đầu vào tối thiểu, bộ chuyển tiếp nostr, khóa riêng tư nostr)


Bạn có thể chạy trình điều phối chỉ có thể truy cập được thông qua địa chỉ .onion, hoặc sử dụng tên miền clearnet tùy chỉnh của mình.


Tìm hoặc tạo tệp cấu hình tại đường dẫn này:


`~/.walletwasabi/coordinator/Config.json`


Chỉnh sửa nó bằng lệnh:


```
sudo nano ~/.walletwasabi/coordinator/Config.json
```


Xem ví dụ về tệp Config.json này:


```
{
"Network": "Main",
"MainNetBitcoinRpcUri": "http://localhost:8332",
"TestNetBitcoinRpcUri": "http://localhost:48332",
"RegTestBitcoinRpcUri": "http://localhost:18443",
"BitcoinRpcConnectionString": "your_bitcoin_rpcuser:your_bitcoin_rpcpassword",
"ConfirmationTarget": 21,
"DoSSeverity": "0.02",
"DoSMinTimeForFailedToVerify": "1d 21h 0m 0s",
"DoSMinTimeForCheating": "1d 0h 0m 0s",
"DoSPenaltyFactorForDisruptingConfirmation": 0.2,
"DoSPenaltyFactorForDisruptingSignalReadyToSign": 1.0,
"DoSPenaltyFactorForDisruptingSigning": 1.0,
"DoSPenaltyFactorForDisruptingByDoubleSpending": 3.0,
"DoSMinTimeInPrison": "0d 0h 20m 0s",
"MinRegistrableAmount": "0.000021",
"MaxRegistrableAmount": "1000.00",
"AllowNotedInputRegistration": true,
"StandardInputRegistrationTimeout": "0d 0h 21m 0s",
"BlameInputRegistrationTimeout": "0d 0h 3m 0s",
"ConnectionConfirmationTimeout": "0d 0h 1m 0s",
"OutputRegistrationTimeout": "0d 0h 1m 0s",
"TransactionSigningTimeout": "0d 0h 1m 0s",
"FailFastOutputRegistrationTimeout": "0d 0h 3m 0s",
"FailFastTransactionSigningTimeout": "0d 0h 1m 0s",
"RoundExpiryTimeout": "0d 0h 5m 0s",
"MaxInputCountByRound": 100,
"MinInputCountByRoundMultiplier": 0.21,
"MinInputCountByBlameRoundMultiplier": 0.21,
"RoundDestroyerThreshold": 375,
"CoordinatorExtPubKey": "xpub_fill_in_your_new_wallet_here",
"CoordinatorExtPubKeyCurrentDepth": 0,
"MaxSuggestedAmountBase": "100.00",
"RoundParallelization": 1,
"CoordinatorIdentifier": "CoinJoinCoordinatorIdentifier",
"AllowP2wpkhInputs": true,
"AllowP2trInputs": true,
"AllowP2wpkhOutputs": true,
"AllowP2trOutputs": true,
"AllowP2pkhOutputs": true,
"AllowP2shOutputs": true,
"AllowP2wshOutputs": true,
"DelayTransactionSigning": false,
"AnnouncerConfig": {
"CoordinatorName": "Your Coordinator Name",
"IsEnabled": true,
"CoordinatorDescription": "Privacy is a human right!",
"CoordinatorUri": "https://coinjoin.yourdomain/",
"AbsoluteMinInputCount": 21,
"ReadMoreUri": "https://coinjoin.yourdomain/",
"RelayUris": [
"wss://relay.primal.net"
],
"Key": "nsec_your_coordinator_nostr_privatekey"
},
"PublishAsOnionService": true,
"OnionServicePrivateKey": your_onion_service_private_key
}
```

### Cấu hình Tor 🧅


Để điền thông tin vào OnionServicePrivateKey, có thể bạn cần tạo khóa này trước.


Wasabi Wallet sẽ tạo khóa riêng cho bạn nếu bạn chạy nó lần đầu tiên với thiết lập ```"PublishAsOnionService": true,``` trong tệp Config.json.


Chạy trình điều phối một lần bằng lệnh:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Để xem địa chỉ dịch vụ ẩn Onion của bạn, hãy kiểm tra nhật ký điều phối viên bằng lệnh sau:


```
cat ~/.walletwasabi/coordinator/Logs.txt | grep .onion
```


và bạn sẽ thấy một cái gì đó tương tự như:


```
2026-01-09 21:21:21.210 [14] INFO       TorProcessManagerService.StartAsync (50)        Coordinator server listening on http://acoo3vgmo4rawaeujh6wckurymm2fp4ojauoag6zwov3pryyopis47qd.onion
```


URL dài có đuôi .onion là địa chỉ dịch vụ ẩn hoặc CoordinatorUri của bạn.


Hoặc kiểm tra lại tệp cấu hình điều phối viên của bạn bằng lệnh:


```
cat ~/.walletwasabi/coordinator/Config.json | grep CoordinatorUri
```


Thông tin này sẽ tự động được điền vào ngay bây giờ.


## Chạy bộ ⚡


Sau khi thiết lập tất cả các thông số cấu hình, bạn có thể chạy dịch vụ điều phối và bắt đầu thông báo vòng đầu tiên của mình 🕶️


Chỉ cần khởi động trình điều phối bằng lệnh:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Bạn có thể theo dõi vòng hiện tại và số lượng UTXO/coin đã đăng ký bằng cách kiểm tra (trong trình duyệt Tor đối với .onion):


```
http://coinjoin.yourdomain/wabisabi/human-monitor/
```


![detected](assets/en/01.webp)


### Tùy chọn: gỡ lỗi máy chủ điều phối


Bạn có thể theo dõi bất kỳ sự cố hoặc lỗi nào trong tệp nhật ký tại ```~/.walletwasabi/backend/Logs.txt```


Các sự cố thường gặp bao gồm sự cố kết nối RPC, cần phải kích hoạt chức năng này trong ```~/.bitcoin/bitcoin.conf``` với lệnh:


```
[main] # or [test] for testnet
rpcbind=127.0.0.1
rpcuser=your_bitcoin_rpcuser
rpcpassword=your_bitcoin_rpcpassword
```


### Tùy chọn: Chạy máy chủ phụ trợ


Cùng với điều phối viên, bạn cũng có thể cung cấp máy chủ phụ trợ cho người dùng không có nút Bitcoin riêng để kết nối nhằm ước tính phí và lọc khối.


Khởi động dịch vụ này bằng lệnh:


```
wbackend
```


## Mời người dùng Wasabi tham gia nhóm điều phối của bạn 🫂


Để người dùng khác tìm thấy dịch vụ của bạn, bạn có thể dựa vào công cụ thông báo nostr, hoặc chia sẻ liên kết đặc biệt với tên miền của bạn (mạng thông thường) hoặc dịch vụ ẩn (liên kết .onion) và làm tròn các tham số như sau:


```
name=Your%20Coordinator%20Name&network=main&coordinatorUri=https://coinjoin.yourdomain&coordinationFeeRate=0&readMore=https://coinjoin.yourdomain/&absoluteMinInputCount=21
```


Khi người dùng sao chép liên kết ma thuật và mở Wasabi Wallet của họ, phần mềm sẽ tự động hiển thị hộp thoại điều phối viên với tên miền và các tham số của bạn.


![detected](assets/en/02.webp)


💚🍣 Chúc mừng vì đã phi tập trung hóa quyền riêng tư của Bitcoin 🕶️


Hãy nhớ rằng bạn đã được đào tạo [wasabika](https://docs.wasabiwallet.io/FAQ/FAQ-Contribution.html#you-can-become-a-wasabika), Wasabi Wallet chỉ dành cho mục đích phòng thủ 🛡️