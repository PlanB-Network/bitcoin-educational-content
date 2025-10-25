---
name: Ride The Lightning (RTL)
description: Sử dụng Ride The Lightning (RTL) để quản lý nút Lightning của bạn
---
![cover](assets/cover.webp)


## 1. Giới thiệu



**Ride The Lightning (RTL)** là ứng dụng web Interface hoàn chỉnh để quản lý một nút Lightning Network. Ứng dụng web tự lưu trữ này cung cấp một **cockpit** Lightning có thể truy cập từ trình duyệt của bạn. RTL hoạt động với tất cả các triển khai Lightning chính (LND, Core Lightning/CLN và Eclair) và cung cấp cho bạn quyền kiểm soát hoàn toàn đối với nút và kênh của mình. Mã nguồn mở (giấy phép MIT) và miễn phí, RTL được tích hợp theo mặc định trong nhiều giải pháp nút chìa khóa trao tay (RaspiBlitz, MyNode, Umbrel, v.v.).



**Nếu không có Interface đồ họa, các nút Lightning chỉ có thể được quản lý thông qua các lệnh CLI thân thiện với người dùng. RTL đơn giản hóa các hoạt động này bằng Interface tiện dụng. Sau đây là các ứng dụng chính:**





- **Xem kênh và nút của bạn** - Bảng điều khiển hiển thị số dư On-Chain, thanh khoản Lightning (cục bộ/từ xa), trạng thái đồng bộ hóa, bí danh nút và nhiều thông tin khác. Bạn có thể xem danh sách kênh, dung lượng, phân phối cục bộ/từ xa và trạng thái của mình. RTL cung cấp bảng điều khiển theo ngữ cảnh để phân tích hoạt động từ nhiều góc độ khác nhau.





- **Quản lý kênh Lightning** - Mở/đóng kênh chỉ bằng vài cú nhấp chuột. RTL cho phép bạn kết nối với một đối tác và mở kênh mà không cần lệnh. Bạn có thể điều chỉnh phí định tuyến, xem điểm số dư hoặc khởi tạo tái cân bằng vòng tròn để tái cân bằng tiền giữa các kênh.





- **Theo dõi và thực hiện thanh toán** - RTL quản lý các giao dịch Lightning: gửi thanh toán qua hóa đơn, hóa đơn generate để nhận, theo dõi các giao dịch (thanh toán, định tuyến) với lịch sử chi tiết. Interface cũng phân tích định tuyến để xem những khoản thanh toán nào đang đi qua nút của bạn.





- Quản lý và sao lưu **Wallet On-Chain** - Tab On-Chain cho phép bạn định địa chỉ generate và gửi giao dịch. RTL giúp lưu kênh dễ dàng bằng cách xuất tệp SCB cho LND, với bản cập nhật tự động cho mỗi lần sửa đổi kênh.



Tóm lại, RTL là **bảng điều khiển mạnh mẽ cho Lightning Network**, cung cấp Interface giáo dục để điều khiển nút của bạn hàng ngày. Hướng dẫn này sẽ hướng dẫn bạn cài đặt và sử dụng để quản lý kênh và thanh toán của mình.



## 2. Vận hành kỹ thuật RTL



![Schéma de l'architecture RTL : interface responsive compatible avec tous les appareils, frontend Angular, serveur Node (port 3000), connecté aux API REST de LND](assets/fr/01.webp)



Trước khi đi sâu vào vấn đề, bạn nên hiểu sơ qua về **cách RTL tương tác với nút Lightning của bạn** ở cấp độ kỹ thuật.



**Kiến trúc chung:** RTL là một ứng dụng web được xây dựng bằng Node.js (phần phụ trợ) và Angular (phần giao diện). Cụ thể, RTL chạy như một máy chủ web cục bộ nhỏ (mặc định là cổng 3000) để đối thoại với triển khai Lightning của bạn thông qua API của nó. Tùy thuộc vào loại:





- Với **LND**, RTL sử dụng REST API của LND (cổng 8080) để thực thi lệnh Lightning. Kết nối được bảo mật bằng TLS và yêu cầu tệp **admin macaroon** của LND để xác thực.





- Với **Core Lightning (CLN)**, RTL sử dụng REST API do *c-lightning-REST* cung cấp hoặc **truy cập rune** thông qua plugin `commando`. Các giải pháp như Umbrel tự động cấu hình Elements này.





- Với **Eclair**, RTL kết nối với Eclair REST API bằng mật khẩu xác thực đã cấu hình.



**Cấu hình và bảo mật:** RTL được cấu hình thông qua tệp JSON (`RTL-Config.json`) trong đó bạn xác định cổng web, mật khẩu truy cập và thông tin kết nối đến nút của mình. Web Interface được bảo vệ bằng thông tin đăng nhập/mật khẩu (`mật khẩu` mặc định có thể thay đổi) và hỗ trợ 2FA. Theo mặc định, RTL chạy dưới dạng HTTP cục bộ (`http://localhost:3000`), nhưng để truy cập từ xa, hãy luôn sử dụng kết nối an toàn (HTTPS qua proxy ngược, Tor hoặc VPN).



Tóm lại, RTL là một thành phần bổ sung kết nối với nút của bạn thông qua API an toàn, yêu cầu mã thông báo truy cập phù hợp và cung cấp bảo mật Layer riêng. Kiến trúc mô-đun này thậm chí cho phép bạn quản lý **nhiều nút Lightning bằng một phiên bản RTL duy nhất**.



## 3. Cài đặt RTL



Vì RTL được phân phối dưới dạng phần mềm mã nguồn mở nên có một số cách để cài đặt nó trên hệ thống của bạn. Trong phần này, chúng tôi sẽ đề cập đến hai cách tiếp cận chính: cài đặt thủ công và cài đặt thông qua Umbrel.



### Phương pháp thủ công



Cài đặt thủ công phù hợp nếu bạn muốn giữ quyền kiểm soát chi tiết hoặc nếu bạn đang tích hợp RTL vào cấu hình tùy chỉnh. Các bước dưới đây dành cho nút LND chạy Linux (ví dụ: Raspberry Pi hoặc VPS chạy Ubuntu/Debian), nhưng tương tự đối với CLN/Eclair.



**Điều kiện tiên quyết:** đảm bảo bạn có một nút Bitcoin **đã đồng bộ hóa** và một nút Lightning đang hoạt động (LND, CLN hoặc Eclair) trên máy. RTL không chứa một nút Lightning, nó kết nối với một nút hiện có. Bạn cũng cần cài đặt **Node.js** (khuyến nghị phiên bản 14 trở lên). Bạn có thể kiểm tra bằng `node -v` hoặc cài đặt Node từ trang web chính thức (https://nodejs.org/en/download/) hoặc trình quản lý gói của bạn.



Các giai đoạn cài đặt chính là:



**Tải xuống mã RTL**: Sao chép kho lưu trữ RTL GitHub chính thức trong thư mục bạn chọn. Ví dụ:



```bash
git clone https://github.com/Ride-The-Lightning/RTL.git
cd RTL
```



**Cài đặt các phụ thuộc**: RTL là một ứng dụng Node.js, vì vậy bạn cần cài đặt các mô-đun cần thiết của nó. Trong thư mục RTL, hãy chạy:



```bash
npm install --omit=dev --legacy-peer-deps
```



Lệnh này cài đặt các gói NPM cần thiết (bỏ qua các phụ thuộc phát triển). Tùy chọn `--legacy-peer-deps` được khuyến nghị để tránh xung đột phụ thuộc Node có thể xảy ra.



**RTL-Config**: Sau khi các phụ thuộc đã được thiết lập, hãy chuẩn bị tệp cấu hình. Sao chép/đổi tên tệp `Sample-RTL-Config.json` trong thư mục gốc của dự án thành `RTL-Config.json`. Mở tệp đó trong :





- **Mật khẩu UI**: chọn một mật khẩu an toàn và nhập vào `multiPass` (thay vì `"password"` mặc định).
- **Cổng**: mặc định là `3000`. Bạn có thể thay đổi nếu cổng này đã được sử dụng trên máy của bạn.
- **Node**: trong phần `nodes[0]`, điều chỉnh các tham số cho nút của bạn:
     - `lnNode`: tên mô tả cho nút của bạn (ví dụ: `"LND Node Maison"`).
     - lnImplementation`: `"LND"` (hoặc `"CLN"`/`"ECL"` tùy theo trường hợp).
     - Trong mục `xác thực`:
       - macaroonPath`: chỉ định đường dẫn đầy đủ đến thư mục chứa tệp macaroon admin của LND.
       - `configPath`: đường dẫn đến tệp cấu hình của nút (`LND.conf` cho LND).
     - Trong `cài đặt`:
       - `fiatConversion`: đặt thành `true` nếu bạn muốn chuyển đổi tiền tệ fiat.
       - `unannouncedChannels`: đặt thành `true` để xem các kênh chưa được công bố.
       - themeColor` và `themeMode`: Tùy chỉnh Interface.
       - channelBackupPath`: đường dẫn sao lưu kênh LND.
       - `lnServerUrl`: URL của nút Lightning của bạn (ví dụ: `https://127.0.0.1:8080`).



**Khởi động máy chủ RTL**: Trong thư mục RTL, chạy:



```bash
node rtl
```



Ứng dụng khởi động và có thể truy cập tại `http://localhost:3000`.



**(Tùy chọn) Chạy RTL dưới dạng dịch vụ**: Để khởi động tự động, hãy tạo systemd:



Để thực hiện điều này:




- Mở terminal trên máy của bạn.
- Tạo một tệp dịch vụ mới bằng lệnh sau (thay thế `nano` bằng trình soạn thảo yêu thích của bạn):


```bash
sudo nano /etc/systemd/system/RTL.service
```




- Sao chép và dán nội dung bên dưới vào tập tin này:



```ini
[Unit]
Description=Ride The Lightning web UI
Wants=lnd.service
After=lnd.service

[Service]
ExecStart=/usr/bin/node /chemin/vers/RTL/rtl
User=<votre_user>
Restart=always
TimeoutSec=120
RestartSec=30

[Install]
WantedBy=multi-user.target
```





- Thay thế `/path/to/RTL/rtl` bằng đường dẫn thực tế đến tệp `rtl` trên máy của bạn và `<your_user>` bằng tên người dùng Linux của bạn.
- Lưu và đóng tệp.
- Tải lại cấu hình systemd:


```bash
sudo systemctl daemon-reload
```




- Kích hoạt và khởi động dịch vụ RTL:


```bash
sudo systemctl enable RTL
sudo systemctl start RTL
```



RTL bây giờ sẽ tự động khởi động mỗi khi máy khởi động lại. Bạn có thể kiểm tra trạng thái của nó bằng:


```bash
sudo systemctl status RTL
```



### Cài đặt qua Umbrel



Nếu bạn sử dụng [Umbrel](https://getumbrel.com), việc cài đặt RTL sẽ đơn giản hơn nhiều:





- Truy cập Interface Umbrel (thường thông qua `http://umbrel.local`)
- Vào **App Store**
- Tìm kiếm "Ride The Lightning"



**Lưu ý quan trọng: có hai ứng dụng RTL riêng biệt trong Umbrel App Store:**




- **Ride The Lightning** (dành cho LND): để sử dụng với nút Lightning mặc định của Umbrel (LND).
- **Ride The Lightning (Core Lightning)**: chỉ sử dụng nếu bạn đã cài đặt ứng dụng *Core Lightning* trên Umbrel và muốn quản lý nút này bằng RTL.



*Mỗi phiên bản RTL được cấu hình sẵn để đối thoại với triển khai tương ứng (LND hoặc Core Lightning). Nếu bạn chưa thay đổi nút Lightning của mình, chỉ cần chọn phiên bản LND cổ điển*



![Fiche de l'application Ride The Lightning dans Umbrel : présentation de l'app avec captures d'écran et bouton violet "Install" en haut à droite](assets/fr/02.webp)





- Nhấp vào **Cài đặt**



![Fenêtre d'affichage du mot de passe par défaut après installation de RTL dans Umbrel, avec bouton "Open Ride The Lightning"](assets/fr/03.webp)



**Quan trọng:** Sau khi cài đặt, RTL sẽ hiển thị màn hình có mật khẩu mặc định. **Sao chép và lưu mật khẩu này** - bạn sẽ cần mật khẩu này để đăng nhập vào Interface RTL. Mật khẩu này sẽ được hiển thị mỗi khi RTL khởi động cho đến khi bạn chọn tùy chọn "Không hiển thị lại".



Umbrel tự động xử lý:




- Tải xuống và cấu hình RTL
- Cấu hình quyền truy cập vào nút Lightning
- Quản lý cập nhật
- Bảo mật quyền truy cập vào Interface



Sau khi cài đặt, ứng dụng sẽ xuất hiện trong menu *Ứng dụng* trên Umbrel. Nhấp vào **Ride The Lightning** để khởi chạy ứng dụng.



![Écran de connexion RTL via Umbrel : champ de mot de passe avec logo du cheval en haut à gauche, bouton "Login"](assets/fr/04.webp)



Trên màn hình đăng nhập, nhập mật khẩu bạn đã sao chép trước đó. Sau khi đăng nhập, Interface web RTL sẽ có thể truy cập trực tiếp từ bảng điều khiển Umbrel mà không cần cấu hình bổ sung!



## 4. Giới thiệu và sử dụng Interface RTL



Bây giờ RTL đã hoạt động, hãy cùng khám phá web Interface và các tính năng chính của nó. Chúng ta sẽ xem xét các phần khác nhau của ứng dụng để cung cấp cho bạn cái nhìn tổng quan đầy đủ.



### Bảng điều khiển chính



![Tableau de bord RTL : solde Lightning, solde on-chain, capacité de liquidité entrante/sortante et création de facture](assets/fr/05.webp)



Ngay khi bạn đăng nhập, bạn sẽ truy cập vào **bảng điều khiển chính**, nơi cung cấp cho bạn tổng quan về nút Lightning của bạn. Trang này tập trung thông tin cần thiết:




- Tổng số dư Lightning của bạn
- Cân On-Chain có sẵn
- Sự cố về thanh khoản của bạn (đến/đi)
- Truy cập nhanh để gửi và nhận Satss qua nút Lightning của bạn



### Quản lý quỹ On-Chain



![Onglet "On-chain" actif dans RTL : solde Bitcoin (en sats, BTC, USD), et liste des transactions avec type d'adresse Taproot](assets/fr/06.webp)



Tab **On-Chain** cho phép bạn quản lý bitcoin của mình trực tiếp trên chuỗi chính:




- Hiển thị số dư theo các đơn vị khác nhau (Sats, BTC, USD)
- Danh sách đầy đủ các giao dịch
- Thế hệ Address Taproot (P2TR), P2SH (NP2WKH) hoặc Bech32 (P2WKH)
- Quản lý UTXO, nhận và gửi bitcoin



### Lightning: trình bày chi tiết các menu phụ



Interface RTL có menu phụ dành riêng cho Lightning Network, tập hợp tất cả các chức năng cần thiết để quản lý nút của bạn. Sau đây là thông tin chi tiết về từng menu phụ, theo thứ tự của ảnh chụp màn hình:



#### 1. Đồng nghiệp/Kênh



![Vue de gestion des canaux Lightning (onglet "Peers/Channels" ouvert)](assets/fr/07.webp)



Menu phụ này cho phép bạn:




- Xem danh sách các đối tác được kết nối và các kênh Lightning đang mở hoặc đang chờ.
- Thêm một đối tác mới (kết nối với một nút Lightning khác).
- Mở, đóng hoặc quản lý các kênh hiện có.
- Xem thông tin chi tiết của từng kênh: năng lực, số dư cục bộ/từ xa, trạng thái, lịch sử giao dịch, điểm số dư, v.v.



#### 2. Giao dịch



![Historique des transactions Lightning (onglet "Transactions" > "Payments")](assets/fr/08.webp)



Trong menu phụ này, bạn có thể:




- Gửi thanh toán Lightning (qua Invoice).
- generate và quản lý hóa đơn để nhận thanh toán.
- Xem lịch sử đầy đủ các khoản thanh toán đã gửi và nhận, kèm theo thông tin chi tiết (số tiền, ngày, trạng thái, phí, số lần bỏ qua, v.v.).



#### 3. Định tuyến



Menu phụ này hiển thị:




- Thanh toán được định tuyến bởi nút của bạn cho những người dùng Lightning Network khác.
- Thống kê định tuyến: số lượng giao dịch chuyển tiếp, phí kiếm được, lỗi gặp phải.
- Lịch sử có thể xuất để phân tích nâng cao.



#### 4. Sự hoãn lại



Menu phụ này cung cấp:




- Báo cáo chi tiết về hoạt động của nút Lightning của bạn.
- Biểu đồ và bảng về kênh, thanh toán, phí, năng lực, v.v.
- Công cụ giúp bạn hiểu rõ hơn về hiệu suất của nút.



#### 5. Tra cứu biểu đồ



Menu phụ này cho phép bạn:




- Khám phá cấu trúc của Lightning Network.
- Tìm kiếm các nút hoặc kênh cụ thể.
- Thu thập thông tin về khả năng kết nối và dung lượng mạng tổng thể.



#### 6. Ký/Xác minh



Menu phụ này cung cấp:




- Khả năng ký tin nhắn bằng khóa của nút của bạn (bằng chứng của Ownership).
- Xác minh chữ ký để xác thực tin nhắn từ các nút khác.



#### 7. Sao lưu



Menu phụ này dành riêng cho việc sao lưu:




- Xuất tệp sao lưu kênh (SCB cho LND).
- Khôi phục cấu hình hoặc kênh nếu cần thiết.
- Mẹo bảo mật bản sao lưu của bạn.



#### 8. Nút/Mạng



![Vue d'ensemble du nœud Lightning (onglet "Node/Network")](assets/fr/09.webp)



Trong menu phụ này bạn sẽ tìm thấy:




- Tóm tắt đầy đủ về trạng thái của nút Lightning của bạn: bí danh, phiên bản, màu sắc, trạng thái đồng bộ hóa.
- Thống kê về kênh (hoạt động, chờ, đóng), tổng dung lượng, kết nối.
- Thông tin về Lightning Network toàn cầu và vị trí nút của bạn trong đó.



### Dịch vụ: Boltz Swaps



![Interface de gestion des swaps avec Boltz (onglet "Services" > "Boltz")](assets/fr/10.webp)



Boltz là dịch vụ Exchange thân thiện với quyền riêng tư, không lưu ký, chuyển đổi bitcoin giữa Lightning Network và Blockchain Bitcoin (On-Chain). Dịch vụ này cung cấp hai loại hoạt động: Hoán đổi tàu ngầm ngược (** Hoán đổi ra**) và Hoán đổi tàu ngầm (** Hoán đổi vào**).



#### Hoán đổi (Hoán đổi tàu ngầm ngược)



Swap Out chuyển đổi Satss có sẵn trên Lightning Network thành Bitcoin On-Chain. Cơ chế này hữu ích khi một nút hết dung lượng đầu vào hoặc khi bạn muốn khôi phục tiền từ On-Chain Address. Quy trình hoạt động như sau:




- Người dùng chọn số tiền cần trao đổi
- Nút gửi thanh toán Lightning đến Boltz
- Trong Exchange, Boltz chặn một lượng tương đương trong On-Chain bitcoin
- Sau khi giao dịch được xác nhận, người dùng có thể yêu cầu tiền bằng cách tiết lộ bí mật được sử dụng trong giao dịch hoán đổi



Quá trình này không mang tính lưu ký, Boltz không bao giờ giữ tiền của người dùng.


![Double capture des étapes de configuration d'un swap-out](assets/fr/11.webp)



#### Hoán đổi (Hoán đổi tàu ngầm)



Mặt khác, Swap In cho phép các quỹ On-Chain được tái cấp vào Lightning Network. Điều này đặc biệt hữu ích để khôi phục công suất đầu ra trên các kênh của bạn. Quy trình như sau:




- Người dùng gửi bitcoin đến một Address cụ thể do Boltz tạo ra
- Số tiền này chỉ có thể được Boltz giải ngân nếu anh ta trả Lightning Invoice do nút của người dùng tạo ra
- Sau khi Invoice được thanh toán, số tiền sẽ có sẵn trên kênh Lightning, giúp tăng công suất đầu ra của nút



![Configuration d'un swap-in](assets/fr/12.webp)



Hai cơ chế này cho phép quản lý tính thanh khoản của kênh Lightning một cách hiệu quả, đồng thời duy trì quyền tự chủ của người dùng đối với tiền của mình.



### Cấu hình và tùy chỉnh



![Écran de configuration du nœud (onglet "Node Config")](assets/fr/13.webp)



Tab **Cấu hình nút** cho phép bạn tùy chỉnh trải nghiệm của mình:




- Kích hoạt các kênh không báo trước
- Tùy chỉnh màn hình bán hàng
- Cấu hình Block explorer
- Điều chỉnh Interface



### Tài liệu và trợ giúp



![Section d'aide de RTL (onglet "Help")](assets/fr/14.webp)



Cuối cùng, phần **Trợ giúp** cung cấp tài liệu toàn diện về:




- Cấu hình ban đầu
- Quản lý kênh và ngang hàng
- Thanh toán và giao dịch
- Sao lưu và khôi phục
- Báo cáo và thống kê
- Chữ ký và xác minh
- Các tham số nút và ứng dụng



Interface toàn diện này cho phép bạn quản lý nút Lightning của mình một cách hiệu quả, từ các hoạt động cơ bản đến các tính năng nâng cao, tất cả đều có trong một Interface trực quan và được tổ chức tốt.



## 5. Các trường hợp sử dụng nâng cao và bảo mật



Trong phần này, đây là những điều bạn cần biết để tiến xa hơn với RTL và bảo mật nút Lightning của bạn:



### Giám sát và xử lý sự cố



Để giám sát nút của bạn, bạn có thể xuất dữ liệu RTL (nhật ký, CSV) và xem chúng trong các công cụ như Grafana. Trong trường hợp có vấn đề (thanh toán bị chặn, kênh không hoạt động), hãy tham khảo nhật ký LND/CLN và sử dụng các lệnh chẩn đoán (`lncli listchannels`, `lncli pendingchannels`, v.v.). RTL cũng cung cấp nhật ký Interface để giám sát các sự kiện định tuyến.



### Truy cập từ xa an toàn



Không bao giờ để lộ RTL trực tiếp trên Internet. Ưu tiên:




- **VPN** (ví dụ: Tailscale) để truy cập riêng tư, được mã hóa
- **Tor** để truy cập an toàn, ẩn danh
- **Proxy ngược HTTPS** (Nginx/Caddy) chỉ khi bạn biết cách cấu hình nó



https://planb.network/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Thực hành an toàn tốt





- **Bảo vệ quyền truy cập của bạn**: không bao giờ chia sẻ admin.macaroon hoặc mật khẩu RTL của bạn. Giới hạn quyền đối với các tệp nhạy cảm.
- **Sao lưu thường xuyên**: xuất tệp sao lưu kênh (SCB) sau mỗi lần sửa đổi và lưu trữ bên ngoài nút.
- **Cập nhật**: cập nhật RTL, node và Umbrel của bạn với các bản sửa lỗi bảo mật mới nhất.
- **Bảo mật**: ẩn danh nhật ký và ảnh chụp màn hình trước khi chia sẻ. Không bao giờ chia sẻ số dư hoặc danh sách ngang hàng của bạn một cách công khai.
- **Truy cập đơn**: RTL không phải là đa người dùng. Không chia sẻ quyền truy cập quản trị. Đối với quyền truy cập chỉ đọc, hãy sử dụng macaroon chuyên dụng nếu cần.



Bằng cách áp dụng những nguyên tắc này, bạn có thể hạn chế đáng kể rủi ro và giữ quyền kiểm soát đối với nút Lightning của mình.



## 7. Kết luận



**Ride The Lightning** là một công cụ thiết yếu để quản lý hiệu quả một node Bitcoin/Lightning, cho dù bạn là người mới bắt đầu hay người dùng nâng cao. Nó cung cấp một Interface rõ ràng để kiểm soát các kênh, thanh toán và tình trạng node của bạn, đồng thời giúp bạn hiểu sâu hơn về Lightning Network.



RTL nổi bật với khả năng tương thích với nhiều triển khai, các chức năng nâng cao (cân bằng lại, hoán đổi, báo cáo) và phương pháp sư phạm. Đối với các nhu cầu đơn giản, Interface Umbrel hoặc Wallet mobile sẽ đủ, nhưng RTL hoàn toàn hợp lý cho việc quản lý nút chủ động, tối ưu.



Để tìm hiểu thêm:




- Trang web chính thức của RTL: https://www.ridethelightning.info/
- GitHub RTL: https://github.com/Ride-The-Lightning/RTL
- **Reddit r/lightningnetwork**: [r/lightningnetwork](https://www.reddit.com/r/lightningnetwork) - Thảo luận kỹ thuật, thông báo dự án, phản hồi và tài nguyên giáo dục
- **Diễn đàn cộng đồng Umbrel**: [community.getumbrel.com](https://community.getumbrel.com) - Diễn đàn chính thức với mục Bitcoin/Lightning chuyên dụng, hướng dẫn và giải pháp cho các vấn đề thường gặp
- **Lightning Network Developers**: [github.com/lightning](https://github.com/lightning) - Kho lưu trữ GitHub chính thức để theo dõi quá trình phát triển và đóng góp mã nguồn
- **Stack Exchange Bitcoin**: [Bitcoin.stackexchange.com](https://Bitcoin.stackexchange.com) - Hỏi đáp kỹ thuật với các nhà phát triển và người dùng nâng cao



Tóm lại, RTL cung cấp cho bạn quyền kiểm soát hoàn toàn đối với nút Lightning của mình trong Interface hiện đại và đầy đủ tính năng.



**Nguồn:** Trang web chính thức của RTL; RTL GitHub; Umbrel App Store; Cộng đồng Umbrel; Tài nguyên của Plan B Network.



Để hiểu sâu hơn về cách thức hoạt động của Lightning Network, tôi cũng khuyên bạn nên tham gia khóa học miễn phí này:



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb