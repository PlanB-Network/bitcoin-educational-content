---
name: ThunderHub
description: Interface Lightning node quản lý web LND
---
![cover](assets/cover.webp)



## Giới thiệu



ThunderHub là **trình quản lý nguồn mở cho các nút Lightning (LND)**, cung cấp Interface trực quan có thể truy cập từ bất kỳ thiết bị hoặc trình duyệt nào.



**Đặc điểm chính:**




- **Giám sát**: Tổng quan về số dư, kênh, giao dịch, thống kê định tuyến
- **Quản lý**: Mở/đóng kênh, thanh toán đến/đi, cân bằng kênh
- **Tích hợp**: Hỗ trợ LNURL, hoán đổi qua Boltz, sao lưu Amboss
- **Interface responsive**: Tương thích với các thiết bị di động, máy tính bảng và máy tính để bàn có chủ đề tối/sáng



ThunderHub tích hợp dễ dàng với **Umbrel**, **Voltage**, **RaspiBlitz** và **MyNode**, giúp đơn giản hóa việc quản lý nút hàng ngày của bạn.



**ThunderHub đặc biệt phù hợp với các nhà điều hành đang tìm kiếm một Interface tiện dụng để quản lý các kênh của họ, kiểm soát thanh khoản (tái cân bằng), giám sát các giao dịch và tích hợp các dịch vụ của bên thứ ba như Amboss. Bảo mật được đảm bảo thông qua kết nối cục bộ hoặc Tor.**



Nếu bạn chưa có nút Lightning, chúng tôi khuyên bạn nên làm theo hướng dẫn LND Umbrel của chúng tôi:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Cài đặt



ThunderHub có thể được cài đặt theo nhiều cách khác nhau, tùy thuộc vào môi trường lưu trữ Lightning node của bạn. Cho dù bạn sử dụng giải pháp chìa khóa trao tay (Umbrel, Voltage, RaspiBlitz, MyNode, Start9, v.v.) hay cài đặt thủ công, ThunderHub thường có sẵn mà không cần nỗ lực lớn. Dưới đây, chúng tôi mô tả hai cách tiếp cận phổ biến: thông qua Umbrel App Store và thông qua cài đặt thủ công (áp dụng cho máy chủ hoặc bản phân phối tự lưu trữ).



### Cài đặt qua Umbrel



Umbrel tích hợp ThunderHub vào **App Store**, giúp việc cài đặt cực kỳ đơn giản. Không cần dòng lệnh hoặc cấu hình thủ công: mọi thứ đều được thực hiện thông qua Interface Umbrel. Chỉ cần làm theo các bước sau:





- **Mở bảng điều khiển Umbrel**: Kết nối với trang web Interface của nút Umbrel (ví dụ: `http://umbrel.local` trên mạng cục bộ của bạn hoặc thông qua `.onion` Address nếu bạn đang sử dụng Tor).
- Truy cập **App Store**: Trong menu chính của Umbrel, nhấp vào "App Store" (hoặc "App"). Tìm kiếm **ThunderHub** trong danh sách các ứng dụng khả dụng.



![Écran d'installation de ThunderHub via Umbrel](assets/fr/01.webp)





- **Cài đặt ThunderHub**: Nhấp vào ứng dụng ThunderHub, sau đó nhấp vào nút cài đặt. Xác nhận nếu cần. Umbrel sẽ tự động tải xuống và triển khai ThunderHub trên nút của bạn.





- **Khởi chạy ứng dụng**: Sau khi cài đặt hoàn tất (vài chục giây), ThunderHub sẽ xuất hiện trên trang chủ của bạn. Nhấp vào biểu tượng để mở. ThunderHub sẽ khởi chạy trong trình duyệt của bạn.



![Identifiants par défaut pour ThunderHub](assets/fr/02.webp)



**Quan trọng:** Khi ThunderHub được mở lần đầu tiên, nó sẽ tự động hiển thị **mật khẩu mặc định** cần thiết để đăng nhập. Tùy chọn "Không hiển thị lại" cho phép bạn ẩn màn hình hiển thị này cho các kết nối trong tương lai. **Chúng tôi khuyên bạn nên:**




- **Lưu mật khẩu này ngay lập tức** trong trình quản lý mật khẩu của bạn
- Sao chép nó để sử dụng ở bước tiếp theo
- Kiểm tra "Không hiển thị lại" sau khi mật khẩu đã được lưu



![Page de connexion de ThunderHub](assets/fr/03.webp)



Sau đó, bạn sẽ được đưa đến trang đăng nhập, tại đây bạn phải nhập mật khẩu đã sao chép ở bước trước để mở khóa Interface.



![Interface de connexion complète à ThunderHub](assets/fr/04.webp)



Umbrel sẽ đảm nhiệm việc cung cấp ThunderHub thông tin kết nối LND (chứng chỉ TLS, macaroon quản trị, v.v.) ở chế độ nền, do đó bạn không cần phải thực hiện bất kỳ cấu hình bổ sung nào. Chỉ với vài cú nhấp chuột, bạn sẽ có ThunderHub hoạt động trên nút Umbrel của mình.



### Cài đặt thủ công (tự lưu trữ, không bao gồm Umbrel)



Đối với người dùng bên ngoài Umbrel (ví dụ: trên máy chủ cá nhân, Raspberry Pi với RaspiBlitz hoặc cài đặt *độc lập*), cài đặt ThunderHub yêu cầu một vài bước bổ sung. Dưới đây chúng tôi mô tả cài đặt từ nguồn và cấu hình, theo [tài liệu ThunderHub chính thức](https://docs.thunderhub.io).



#### Cài đặt



**Điều kiện tiên quyết:** Đảm bảo hệ thống của bạn đáp ứng các yêu cầu tối thiểu theo [thiết lập tài liệu](https://docs.thunderhub.io/setup):




- **Node.js** phiên bản 18 trở lên
- **npm** đã cài đặt
- Truy cập vào các tệp xác thực LND:
  - Chứng chỉ LND TLS (`tls.cert`)
  - LND macaroon quản trị (`admin.macaroon`)
  - Dịch vụ gRPC LND Address (tên máy chủ: cổng) (mặc định `127.0.0.1:10009` cục bộ)



**1. Truy xuất mã ThunderHub:** Sao chép kho lưu trữ GitHub của dự án như được mô tả trong [tài liệu cài đặt](https://docs.thunderhub.io/installation):



```bash
git clone https://github.com/apotdevin/thunderhub.git
cd thunderhub
```



**2. cài đặt các phụ thuộc và xây dựng ứng dụng:**



```bash
npm install
npm run build
```



Các lệnh này cài đặt tất cả các mô-đun cần thiết và sau đó biên dịch ứng dụng (ThunderHub được viết bằng TypeScript/React).



**3. Cập nhật sau:** ThunderHub cung cấp một số phương pháp để cập nhật trong tương lai:



```bash
# Méthode rapide
npm run update

# Ou méthode manuelle
git pull
npm install
npm run build
```



#### Cấu hình (Cài đặt)



**1. Tệp cấu hình chính:** Tạo tệp `.env.local` ở gốc thư mục ThunderHub để tùy chỉnh cấu hình (điều này sẽ ngăn cài đặt của bạn bị ghi đè trong quá trình cập nhật). Các biến chính theo [tài liệu thiết lập](https://docs.thunderhub.io/setup):



```bash
# -----------
# Server Configs
# -----------
LOG_LEVEL='info' # 'error' | 'warn' | 'info' | 'http' | 'verbose' | 'debug' | 'silly'
PORT=3000
NODE_ENV=production

# -----------
# Interface Configs
# -----------
THEME='dark' # 'dark' | 'light' | 'night'
CURRENCY='sat' # 'sat' | 'btc' | 'fiat'

# -----------
# Privacy Configs
# -----------
FETCH_PRICES=true # Récupération des prix BTC/fiat depuis Blockchain.com
FETCH_FEES=true # Récupération des frais on-chain depuis Earn.com
DISABLE_LINKS=false # Liens vers 1ml.com et Blockchain.com
NO_VERSION_CHECK=false # Vérification de version depuis GitHub

# -----------
# TOR (optionnel)
# -----------
TOR_PROXY_SERVER='socks://127.0.0.1:9050' # Pour proxifier via TOR

# -----------
# Account Configs
# -----------
ACCOUNT_CONFIG_PATH='/chemin/vers/thubConfig.yaml' # Fichier de comptes
```



**2. Cấu hình tài khoản máy chủ:** Tạo tệp YAML được chỉ định trong `ACCOUNT_CONFIG_PATH`:



```yaml
masterPassword: 'votre_mot_de_passe_principal'
accounts:
- name: 'Mon Nœud LND'
serverUrl: '127.0.0.1:10009'
macaroonPath: '/home/user/.lnd/data/chain/bitcoin/mainnet/admin.macaroon'
certificatePath: '/home/user/.lnd/tls.cert'
password: 'mot_de_passe_compte_specifique'
# Optionnel : compte avec macaroon en hexadécimal
- name: 'Nœud Distant'
serverUrl: 'ip.distante:10009'
macaroon: '0201056c6e6402f8...' # Macaroon en HEX ou Base64
certificate: '0202045c7365...' # Certificat en HEX ou Base64
```



**3. Truy cập từ xa:** Để kết nối với một nút LND từ xa, hãy thêm vào `LND.conf`:



```bash
# Option 1 : accès par IP
tlsextraip=<ip-externe-accessible>
rpclisten=0.0.0.0:10009

# Option 2 : accès par domaine
tlsextradomain=<domaine-externe-accessible>
rpclisten=0.0.0.0:10009
```



**4. Bảo mật:** Khi khởi động lần đầu, ThunderHub **tự động** ẩn `masterPassword` và tất cả mật khẩu tài khoản trong tệp YAML để tránh lưu mật khẩu dưới dạng văn bản thuần túy trên máy chủ.



**5. Khởi động ThunderHub:**



```bash
npm start
```



Theo mặc định, máy chủ sẽ lắng nghe trên cổng 3000. Truy cập `http://localhost:3000` (hoặc `http://ip-serveur:3000` từ mạng cục bộ).



**6. Giải pháp thay thế Docker:** ThunderHub cung cấp hình ảnh Docker chính thức:



```bash
# Image standard
docker pull apotdevin/thunderhub:latest
docker run --rm -it -p 3000:3000/tcp apotdevin/thunderhub:latest

# Image avec base path /thub
docker pull apotdevin/thunderhub:base-v0.11.1
```



Trang đăng nhập ThunderHub xuất hiện. Chọn tài khoản đã cấu hình và nhập mật khẩu để truy cập bảng điều khiển.



**Cài đặt trên các bản phân phối khác:** Các bản phân phối nút đóng gói sẵn (RaspiBlitz, MyNode, Start9, v.v.) thường cung cấp hỗ trợ ThunderHub gốc thông qua giao diện quản trị tương ứng của chúng.



**Để biết thêm thông tin:** Tham khảo tài liệu chính thức đầy đủ:




- **Cài đặt:** [docs.thunderhub.io/installation](https://docs.thunderhub.io/installation)
- **Cấu hình:** [docs.thunderhub.io/setup](https://docs.thunderhub.io/setup)



Các tài nguyên này cung cấp chi tiết các tùy chọn nâng cao như tài khoản SSO, macaron được mã hóa, cấu hình TOR và nhiều hơn nữa.



Sau khi ThunderHub được cài đặt và truy cập, bạn đã sẵn sàng khai thác tất cả các tính năng của nó. Trong phần sau, chúng ta sẽ xem xét Interface ThunderHub và các tab khác nhau của nó để hướng dẫn bạn cách sử dụng.



## Bài thuyết trình Interface



Interface ThunderHub được cấu trúc xung quanh một menu chính (thường được hiển thị ở cột bên trái) bao gồm một số phần chính. Mỗi phần tương ứng với một khía cạnh quản lý nút Lightning của bạn. Chúng ta hãy xem xét từng phần một:





- **Trang chủ** - Tab Trang chủ với bảng điều khiển chung (tổng quan về nút của bạn và các hành động nhanh).
- **Bảng điều khiển** - Bảng điều khiển có thể tùy chỉnh với các tiện ích và số liệu nâng cao.
- **Peers** - Quản lý ngang hàng Lightning (kết nối với các nút khác).
- **Kênh** - Quản lý chi tiết các kênh Lightning.
- **Cân bằng lại** - Công cụ cân bằng kênh (thanh toán tuần hoàn).
- **Giao dịch** - Lịch sử thanh toán Lightning (giao dịch LN).
- **Chuyển tiếp** - Thống kê định tuyến (các khoản thanh toán được chuyển tiếp bởi nút của bạn).
- **Chain** - Danh mục đầu tư On-Chain của Node (On-Chain BTC: UTXO, giao dịch).
- **Amboss** - Tích hợp với Amboss (giám sát nút, sao lưu, v.v.).
- **Công cụ** - Các công cụ khác nhau (sao lưu, tin nhắn đã ký, macaron, báo cáo, v.v.).
- **Swap** - Chức năng hoán đổi On-Chain/Lightning thông qua Boltz.
- **Thống kê** - Thống kê nâng cao và số liệu hiệu suất của nút.



*(Lưu ý: Tùy thuộc vào phiên bản ThunderHub, một số phần có thể có tiêu đề hoặc tính năng bổ sung hơi khác nhau, nhưng các nguyên tắc chung vẫn giữ nguyên)*



### Trang chủ (Bảng điều khiển chung)



Tab **Trang chủ** của ThunderHub là trang chủ xuất hiện sau khi bạn đăng nhập. Tab này chứa **Bảng điều khiển chung**, cung cấp **tổng quan toàn cầu** về trạng thái của nút Lightning của bạn và gợi ý **các hành động nhanh** cho các hoạt động thường lệ. Sau đây là những gì bạn thường thấy:



![Tableau de bord principal de ThunderHub](assets/fr/05.webp)





- **Số dư và dung lượng:** Ở đầu trang, ThunderHub hiển thị số dư khả dụng của bạn. Tại đây, bạn thường sẽ thấy số dư On-Chain (Bitcoin On-Chain trong Wallet của nút, được biểu tượng hóa bằng Anchor ⚓) và số dư Lightning (dung lượng kênh của bạn, được biểu tượng hóa bằng Bolt ⚡). Điều này giúp bạn biết ngay số tiền bạn có trong On-Chain và Lightning. Nếu bạn có nhiều tài khoản hoặc kênh, hãy đảm bảo bạn đang ở đúng kênh (ví dụ: Mainnet so với Testnet).





- **Thống kê chính:** Bảng điều khiển có thể hiển thị một số số liệu chung cho nút của bạn - ví dụ: số kênh mở, số lượng đối tác được kết nối, phí định tuyến kiếm được (nếu có), v.v. Đây là bản tóm tắt về hoạt động và tình trạng gần đây của nút.





- **Hành động nhanh:** Bảng điều khiển có các nút để thực hiện nhanh các tác vụ phổ biến nhất mà không cần phải điều hướng qua menu. Các hành động nhanh này bao gồm:





- **Ghost**: Thiết lập Lightning Address tùy chỉnh thông qua Amboss.
- **Quyên góp**: Quyên góp qua Lightning.
- **Đăng nhập/Đi tới**: Kết nối với tài khoản Amboss của bạn (Kết nối nhanh) và truy cập trực tiếp vào Amboss.space để xem thông tin về nút của bạn.
- **Address**: Nhập mã Lightning Address để thực hiện thanh toán.
- **Mở**: Mở một kênh Lightning mới. Nhấp vào sẽ mở một biểu mẫu để nhập URI của nút từ xa để mở kênh, số tiền và nếu có thể, phí On-Chain tối đa sẽ được sử dụng.
- **Giải mã**: Giải mã Lightning Invoice hoặc LNURL để xem thông tin chi tiết trước khi thanh toán.
- **LNURL**: Xử lý LNURL để thanh toán hoặc rút tiền bằng Lightning.
- **Đăng nhập LnMarkets**: Đăng nhập vào LnMarkets để giao dịch.



Những thao tác nhanh này cho phép bạn thực hiện các thao tác thường xuyên nhất trực tiếp từ trang chủ mà không cần phải điều hướng qua nhiều tab khác nhau của Interface.



Tóm lại, bảng điều khiển ThunderHub cung cấp cho bạn **cái nhìn nhanh** về nút của bạn và cho phép bạn thực hiện các hoạt động thường xuyên nhất (gửi/nhận, mở kênh) chỉ bằng một cú nhấp chuột. Đây là điểm khởi đầu lý tưởng cho việc quản lý hàng ngày.



### Bảng điều khiển



Phần **Bảng điều khiển** tách biệt với tab Trang chủ và cung cấp bảng điều khiển tùy chỉnh nâng cao hơn. Phần này cho phép bạn tạo chế độ xem tùy chỉnh với các tiện ích cụ thể theo nhu cầu của bạn với tư cách là người vận hành nút.





- **Tiện ích có thể tùy chỉnh:** Không giống như Trang chủ có bố cục cố định, Bảng điều khiển cho phép bạn chọn chính xác Elements nào để hiển thị và cách sắp xếp chúng.



![Dashboard sans widgets activés](assets/fr/06.webp)



Nếu không có tiện ích nào được bật, bạn sẽ thấy thông báo "Không có tiện ích nào được bật!" cùng nút "Cài đặt" để truy cập các thông số tùy chỉnh.



![Paramètres des widgets du Dashboard](assets/fr/07.webp)



Trong phần cài đặt, bạn có thể chọn từ nhiều tiện ích được sắp xếp thành các danh mục: "Lightning - Thông tin", "Lightning - Bảng", "Lightning - Đồ thị", v.v. Mỗi tiện ích có thể được kích hoạt hoặc hủy kích hoạt riêng lẻ bằng các nút "Hiển thị/Ẩn".



![Bas de la page des paramètres](assets/fr/08.webp)



Ở cuối phần cài đặt, bạn sẽ thấy nút "Đến bảng điều khiển" để quay lại bảng điều khiển và nút "Đặt lại tiện ích" để đặt lại màn hình mặc định.



![Dashboard personnalisé avec widgets](assets/fr/09.webp)



Sau khi cấu hình, bảng điều khiển của bạn có thể hiển thị nhiều biểu đồ và số liệu khác nhau: Biểu đồ thanh toán Lightning, số lượng hóa đơn đã phát hành, số liệu thống kê chuyển tiếp, số dư chi tiết, v.v.





- **Số liệu nâng cao:** Truy cập số liệu thống kê chi tiết hơn về hiệu suất của nút của bạn, với biểu đồ và dữ liệu thời gian thực.





- **Tổng quan có thể cấu hình:** Tùy chỉnh màn hình để phù hợp với việc bạn là người dùng thông thường hay là nhà điều hành chuyên nghiệp quản lý nhiều kênh định tuyến.





- **Mô-đun Interface:** Thêm hoặc xóa các tiện ích theo yêu cầu: biểu đồ chuyển tiếp, số liệu thanh khoản, cảnh báo tình trạng nút, v.v.



Phần này đặc biệt hữu ích cho người dùng nâng cao muốn theo dõi các số liệu cụ thể hoặc có cái nhìn tổng quan hơn về kỹ thuật của nút Lightning. Phần này bổ sung cho phần Trang chủ bằng cách cung cấp tính linh hoạt và khả năng kiểm soát tốt hơn đối với cách hiển thị thông tin.



### Đồng nghiệp



Phần **Peers** liệt kê tất cả các nút Lightning hiện đang được kết nối với nút của bạn dưới dạng các nút ngang hàng. **Peer** là kết nối trực tiếp từ nút này đến nút khác trên Lightning Network. Nút của bạn có thể được kết nối với các nút ngang hàng ngay cả khi không có kênh mở (ví dụ: chỉ để Exchange trao đổi thông tin trên mạng) hoặc tất nhiên mọi kênh mở đều tự động ngụ ý một nút ngang hàng được kết nối.



![Vue de l'onglet Peers avec les pairs connectés](assets/fr/10.webp)



Trong tab Peers, bạn sẽ thấy:





- **Cột thông tin:** Interface hiển thị các thông tin chi tiết hữu ích như trạng thái đồng bộ hóa, loại kết nối (clearnet hoặc Tor), ping, satoshi đã nhận/đã gửi và khối lượng dữ liệu được trao đổi.
- Thêm một đối tác: ThunderHub cho phép bạn kết nối thủ công với một đối tác mới thông qua nút **"Thêm"** ở góc trên bên phải. Bạn sẽ cần nhập URI của nút (định dạng `<public_key>@<socket>`). Sau khi xác thực, ThunderHub sẽ gửi lệnh `lncli connect` tương ứng. Nếu nút trực tuyến và có thể truy cập, nút đó sẽ được thêm vào danh sách các đối tác của bạn.



### Kênh



Tab **Kênh** là trung tâm của quản lý kênh Lightning. Đây có lẽ là phần bạn sẽ tham khảo thường xuyên nhất. Tab này trình bày **tất cả các kênh Lightning** của bạn cùng với thông tin chi tiết của chúng và cho phép bạn thực hiện các hành động quản lý trên các kênh này.



![Vue d'ensemble des channels ouverts](assets/fr/11.webp)



Sau đây là những gì bạn sẽ tìm thấy trên trang Kênh:





- **Chế độ xem danh sách kênh:** Mỗi kênh mở (hoặc mở/đóng) đều được liệt kê, thường có bí danh của nút từ xa, tổng dung lượng kênh và một thanh màu minh họa sự phân bổ thanh khoản cục bộ so với từ xa. ThunderHub sử dụng mã màu (thường là màu xanh lam/Green) hoặc phần trăm để chỉ ra sự cân bằng kênh: ví dụ, màu xanh lam cho chia sẻ cục bộ của bạn, Green cho chia sẻ từ xa. Nếu một kênh được cân bằng hoàn hảo (50/50), thanh sẽ bằng một nửa của mỗi màu. Điều này cho phép bạn xác định ngay lập tức kênh nào không cân bằng (tất cả màu xanh lam = hầu như tất cả cục bộ





- **Cột thông tin:** Interface hiển thị các cột chi tiết bao gồm Trạng thái, Hành động khả dụng, Thông tin ngang hàng, ID kênh, Dung lượng, Hoạt động, Phí và Số dư với màn hình hiển thị thanh khoản đồ họa.





- **Cấu hình hiển thị:** Bánh răng ở góc trên bên phải cho phép bạn tùy chỉnh màn hình kênh theo sở thích của mình.





- **Trạng thái:** Bạn cũng sẽ thấy các chỉ báo trạng thái - ví dụ: `Hoạt động` (kênh mở và hoạt động), `Ngoại tuyến` (đối tác bị ngắt kết nối, do đó kênh tạm thời không sử dụng được), `Đang chờ` (đối với việc mở hoặc đóng chờ xác nhận On-Chain).





- Các hành động trên kênh: **Đối với mỗi kênh, ThunderHub cung cấp các nút hành động (thường ở dạng biểu tượng):**



![Actions de gestion des canaux - Modifier et Fermer](assets/fr/12.webp)





- **Phí chỉnh sửa:** Interface "Cập nhật Chính sách Kênh" cho phép bạn điều chỉnh tất cả các thông số kênh: Phí cơ bản, Tỷ lệ Phí (tính theo ppm), CLTV Delta, HTLC Tối đa và HTLC Tối thiểu. Điều này cho phép bạn điều chỉnh chính sách phí của mình riêng lẻ cho từng kênh, với mục đích thu hút (hoặc ngăn cản) lưu lượng định tuyến. *(Lưu ý: ThunderHub không phải là công cụ thay thế cho công cụ quản lý phí tự động, nhưng đối với việc điều chỉnh thủ công thì nó rất hiệu quả)*
- Đóng Kênh (**Đóng**): "Kênh Đóng" Interface cho bạn lựa chọn giữa **đóng hợp tác** (mặc định) hoặc **đóng bắt buộc** (*Đóng bắt buộc*) bằng cách xác định các khoản phí (trong Sats/vByte). **Quan trọng:** luôn ưu tiên đóng hợp tác khi có thể, để tránh sự chậm trễ thanh toán On-Chain và phí cao hơn. ThunderHub sẽ cho bạn biết liệu đối tác có trực tuyến (có thể hợp tác) hay không. Trong trường hợp đóng bắt buộc, hãy đảm bảo xác nhận vì điều này là không thể đảo ngược và sẽ kích hoạt giao dịch quét với khóa thời gian (thường là 144 khối hoặc ~1 ngày trên Bitcoin Mainnet).
- **Mở kênh mới:** Để mở kênh mới, hãy nhấp vào bánh răng ở góc trên bên phải của trang Kênh, sau đó chọn "Mở". Sau đó, bạn có thể khởi tạo kênh cho một đối tác mới hoặc hiện có. Ưu điểm của việc sử dụng trang này là bạn có danh sách các kênh hiện có trước mặt, có thể giúp bạn quyết định nơi mở kênh mới.



Tóm lại, phần Kênh cung cấp cho bạn **quyền kiểm soát chặt chẽ đối với từng kênh**. Đây là nơi bạn điều khiển phân bổ thanh khoản, quyết định kênh nào sẽ giữ hoặc đóng và thiết lập các tham số định tuyến cho từng kênh. ThunderHub cung cấp Interface rõ ràng cho các hoạt động quản lý nút quan trọng này.



### Cân bằng lại



Tab **Tái cân bằng** dành riêng cho **cân bằng kênh**. Cân bằng (hay *tái cân bằng*) bao gồm việc điều chỉnh lại việc phân bổ tiền giữa các kênh đi và đến của bạn, bằng cách thực hiện **thanh toán tuần hoàn** từ một trong các kênh của bạn sang một kênh khác của bạn, thông qua Lightning Network. Điều này cho phép bạn, mà không cần phải mang tiền mới vào, chuyển thanh khoản từ một kênh quá đầy sang một kênh quá trống, giúp các kênh của bạn hữu ích hơn (một kênh cân bằng có thể vừa gửi vừa nhận thanh toán).



![Interface de rebalance des canaux](assets/fr/13.webp)



ThunderHub hỗ trợ rất nhiều cho thao tác này, nếu không sẽ rất tẻ nhạt trên dòng lệnh. Sau đây là cách sử dụng phần Rebalance:





- **Chế độ xem kênh ban đầu:** Khi vào Rebalance, ThunderHub sẽ hiển thị danh sách các kênh của bạn, với chỉ báo cân bằng cho từng kênh (tương tự như chỉ báo trên trang Channels). Bạn có thể thấy ngay kênh nào mất cân bằng. ThunderHub có thể sắp xếp các kênh theo thứ tự tăng dần của cân bằng, do đó các kênh mất cân bằng nhất sẽ nổi bật ở đầu danh sách (0.0 nghĩa là hoàn toàn cục bộ hoặc từ xa).





- **Lựa chọn đối tác:** Interface giúp bạn dễ dàng lựa chọn đối tác đi và đến để cân bằng lại.





- **Cài đặt tham số:** Bạn có thể cài đặt:
  - **Phí tối đa** (tính theo Sats và ppm) mà bạn sẵn sàng trả
  - **Số tiền cần cân bằng lại** với tùy chọn "Cố định" hoặc "Mục tiêu"
- Các nút cần tránh khi định tuyến
- **Thời gian dùng thử tối đa** để tìm đường





- Chọn kênh **nguồn**: Đầu tiên, hãy chọn kênh **ra (nguồn)**, tức là kênh mà bạn có quá nhiều thanh khoản cục bộ để chuyển đi. Trên thực tế, đây là kênh mà tỷ lệ chia sẻ cục bộ của bạn cao (> 50%). Hãy tưởng tượng một kênh A có 1.000.000 Satss, trong đó 900.000 là cục bộ - một ứng cử viên tốt để gửi Satss đến nơi khác. Bằng cách nhấp vào kênh A này là "ra", ThunderHub sẽ đánh dấu kênh đó là nguồn.





- Chọn **kênh mục tiêu**: Tiếp theo, chọn kênh **đến (mục tiêu)** cần nhận thanh khoản. Thông thường, đây sẽ là kênh mà ngược lại - hầu hết các quỹ đều ở phía xa (ví dụ: chỉ có 100.000 Satss cục bộ trong số 1.000.000 Satss cục bộ). ThunderHub, sau khi kênh nguồn được chọn, sẽ sắp xếp các kênh khác theo thứ tự ngược lại (số dư giảm dần) để giúp xác định các kênh bổ sung nhất. Chọn kênh B có chỗ ở phía cục bộ. Sau đó, ThunderHub sẽ hiển thị rõ ràng hai kênh nào đã được chọn (nguồn A và mục tiêu B).





- Thiết lập số tiền phí và mức dung sai: **Một biểu mẫu cho phép bạn nhập:**





  - **Số lượng** cần cân bằng lại (trong Sats). Thông thường, chúng tôi chọn số lượng bằng với số lượng cân bằng cả hai kênh ở \~50/50. Ví dụ, ThunderHub có thể lấp đầy trước một nửa dung lượng dư thừa của kênh nguồn.
  - **Phí tối đa** mà bạn sẵn sàng trả cho hoạt động này (tùy chọn). Phí này được thể hiện bằng Sats (tổng chi phí định tuyến vòng tròn). Nếu bạn để trống, ThunderHub sẽ tìm kiếm đường dẫn bất kể chi phí, điều này thường không được khuyến khích (tốt hơn là nên đặt giới hạn, ví dụ: 10 Sats cho một lần cân bằng lại nhỏ hoặc ppm tối đa).





- **Tìm tuyến đường:** Nhấp vào nút để tìm tuyến đường. ThunderHub truy vấn LND để tính toán tuyến đường từ kênh nguồn của bạn qua mạng đến kênh đích của riêng bạn. Nếu tìm thấy tuyến đường khả thi đáp ứng tiêu chí phí của bạn, nó sẽ hiển thị tuyến đường đó cùng với thông tin chi tiết về các bước nhảy và chi phí phí. Ví dụ, nó có thể chỉ ra rằng nó đã tìm thấy một đường dẫn 3 bước nhảy với tổng cộng 2 Sats trong các khoản phí.





- **Bắt đầu cân bằng lại:** Nếu bạn hài lòng với lộ trình được đề xuất, hãy nhấp vào **Kênh cân bằng**. Sau đó, ThunderHub sẽ bắt đầu thanh toán tuần hoàn qua LND. Nếu thanh toán thành công, bạn sẽ thấy thông báo thành công và kênh A và B sẽ có số dư được sửa đổi theo thời gian thực. ThunderHub sẽ cập nhật chỉ báo số dư cho các kênh này (lý tưởng nhất là chúng sẽ xanh hơn trước, cho biết số dư tốt hơn).





- **Điều chỉnh và lặp lại:** Nếu không tìm thấy tuyến đường nào trong lần thử đầu tiên (hoặc nếu quá tốn kém), bạn có thể điều chỉnh các thông số:





  - Hãy thử một số tiền nhỏ hơn (đôi khi việc tái cân bằng một phần có thể diễn ra trong khi số tiền lớn lại không thành công).
  - Tăng dần mức phí tối đa, nhưng hãy cẩn thận đừng trả nhiều phí hơn mức đáng có.
  - Sử dụng nút **Lấy tuyến đường khác** nếu có, để thử tuyến đường thay thế.
  - Hãy thử một cặp kênh khác nếu mọi thứ thực sự trở nên khó khăn.



ThunderHub giúp quy trình trở nên **trực quan và trực quan**. Chỉ trong 4 bước (chọn kênh gửi đi, chọn kênh đến, số tiền, xác thực), bạn có thể thực hiện những gì trước đây cần các lệnh thủ công phức tạp. Công cụ này vô cùng hữu ích để duy trì một nút cân bằng, cải thiện hiệu suất định tuyến và trải nghiệm của bạn (dễ dàng gửi và nhận thanh toán trên tất cả các kênh của bạn).



Cuối cùng, lưu ý rằng việc cân bằng lại sẽ tiêu tốn chi phí định tuyến (trả cho các nút trung gian), do đó, đây là **khoản đầu tư** để làm cho nút của bạn linh hoạt hơn. Hãy sử dụng nó một cách khôn ngoan, ví dụ như để hỗ trợ một kênh cho một dịch vụ mà bạn thường sử dụng (thanh khoản đến) hoặc để cân bằng một kênh định tuyến lớn. ThunderHub cho phép bạn thực hiện việc này **một cách đơn giản và hiệu quả**.



### Giao dịch



Phần **Giao dịch** trong ThunderHub tương ứng với lịch sử giao dịch **Lightning** của nút của bạn, tức là các khoản thanh toán và hóa đơn đã thanh toán hoặc nhận được qua các kênh. Đây là một loại báo cáo tài khoản cho các hoạt động LN của bạn.



![Historique des transactions Lightning](assets/fr/14.webp)



Trong tab này bạn sẽ tìm thấy:





- **Biểu đồ Invoice:** Ở góc trên bên phải, có một biểu đồ hiển thị sự phát triển của các hóa đơn nhận được theo thời gian, cho phép bạn hình dung hoạt động của nút.





- Danh sách theo thứ tự thời gian của tất cả các giao dịch Lightning được thực hiện *từ* hoặc *đến* nút của bạn. Mỗi mục nhập có thể hiển thị:





  - Loại hoạt động: **đã gửi thanh toán** (thanh toán đi) hoặc **đã nhận thanh toán** (đến, thông qua Invoice đã thanh toán).
  - Số tiền tính theo Sats.
  - Ngày/giờ.
  - ID thanh toán (Hash hoặc RHash trước hình ảnh) hoặc bình luận (nếu bạn đã thêm ghi chú vào Invoice).
  - Trạng thái: **đã hoàn thành** hoặc có thể **đang tiến hành**/*thất bại* (ví dụ: thanh toán đang chờ giải quyết, nhưng nhìn chung LND xử lý việc này rất nhanh, do đó có ít giao dịch "đang chờ xử lý" ở đây so với giao dịch On-Chain).



Tóm lại, mục Giao dịch đóng vai trò là **Nhật ký hoạt động LN** của bạn. Mục này rất hữu ích để kiểm tra xem khoản thanh toán đã được thực hiện chưa, có bao nhiêu khoản phí hoặc theo dõi lịch sử giao dịch Lightning của bạn. Kết hợp với mục Chuyển tiếp (sẽ mô tả tiếp theo), bạn sẽ có cái nhìn toàn diện về số tiền đã đi qua nút của mình.



### Tiền đạo



Tab **Chuyển tiếp** dành riêng cho hoạt động **định tuyến** của nút của bạn, tức là các khoản thanh toán **chuyển tiếp** qua các kênh của bạn (khi bạn hoạt động như một nút trung gian trên Lightning Network). Nếu bạn vận hành nút của mình như một nút định tuyến, đây là phần quan trọng để theo dõi hiệu suất của bạn.



![Statistiques de routage Lightning](assets/fr/15.webp)



Trong Forwards, ThunderHub trình bày:





- **Bộ lọc và tùy chọn hiển thị:** Ở góc trên bên phải, bộ lọc cho phép bạn sắp xếp dữ liệu theo ngày/tuần/tháng/năm và chọn giữa hiển thị dạng đồ họa hoặc dạng bảng.





- **Thông báo hoạt động:** Nếu không có định tuyến nào được thực hiện trong khoảng thời gian đã chọn, Interface sẽ hiển thị "Không có chuyển tiếp nào cho khoảng thời gian này", như thể hiện trong ví dụ này.





- **Bảng các giao dịch chuyển tiếp gần đây**: mỗi mục tương ứng với một khoản thanh toán đã được **chuyển tiếp** qua nút của bạn. Đối với mỗi giao dịch chuyển tiếp, chúng ta thường thấy:





  - Timestamp,
  - số tiền được định tuyến (trong Sats),
  - **phí kiếm được** cho lần chuyển tiếp này (trong Sats, đây là sự khác biệt giữa số tiền bạn nhận được trên kênh đến và số tiền bạn gửi trên kênh đi),
  - các kênh đến và đi được sử dụng (thường được xác định bằng bí danh ngang hàng hoặc ID kênh).
  - trạng thái (thường là *hoàn thành*, hoặc thất bại nếu một chuyến đi tiếp theo bị lỗi trên đường đi).





- **Thống kê tổng hợp**: ThunderHub tính toán và hiển thị ở đầu trang tổng số và số liệu thống kê trong một khoảng thời gian nhất định (ví dụ: 24 giờ qua hoặc 7 ngày, v.v., đôi khi có thể cấu hình được).



Tóm lại, phần Forwards cung cấp **tổng quan theo thời gian thực về hoạt động định tuyến của nút Lightning**. Kết hợp với phần Channels và Rebalance, phần này tạo thành một gói hoàn chỉnh để tối ưu hóa nút của bạn: Channels/Rebalance cho thanh khoản, Forwards để quan sát kết quả (dòng chảy và lợi nhuận).



### Xích



Phần **Chuỗi** tương ứng với quản lý danh mục đầu tư Bitcoin On-Chain của nút LND của bạn. Interface này cho phép bạn xem và quản lý các quỹ Bitcoin, được sử dụng để mở kênh hoặc nhận tiền từ các kênh đóng.



![Gestion du portefeuille on-chain](assets/fr/16.webp)



Trong Chain, bạn sẽ tìm thấy:





- Số dư On-Chain: **Hiển thị tổng số dư BTC có trong Wallet LND.**





- **Danh sách UTXO:** Xem tất cả các đầu ra chưa sử dụng (UTXO) với số lượng, xác nhận, Address và định dạng cho mỗi đầu ra.





- **Lịch sử giao dịch:** Bảng chi tiết tất cả các giao dịch Bitcoin với loại (vào/ra), ngày, số tiền, phí, xác nhận, khối bao gồm, địa chỉ và txid.



### Đè bẹp



ThunderHub tích hợp với nền tảng **Amboss** (amboss.space), cung cấp thông tin chi tiết về các nút Lightning, thị trường thanh khoản và các tính năng hữu ích như sao lưu kênh được mã hóa và giám sát tính khả dụng.



![Intégration Amboss avec ses options](assets/fr/17.webp)



Trong ThunderHub, phần Amboss cho phép bạn **liên kết** nút của mình với tài khoản Amboss:





- **Ghost Address:** Thiết lập **Lightning Address** được cá nhân hóa cho nút của bạn, tạo điều kiện thuận lợi cho các khoản thanh toán đến.





- Sao lưu kênh tự động:** Tính năng chủ chốt cho sao lưu kênh được mã hóa** (tệp SCB) trên Amboss. Kích hoạt **Amboss Auto Backup = Có** trong cài đặt để tự động gửi các bản cập nhật sao lưu được mã hóa mỗi khi bạn thay đổi kênh. Trong trường hợp xảy ra lỗi, bạn sẽ có thể khôi phục tiền của mình nhờ bản sao lưu bên ngoài này.





- **Kiểm tra sức khỏe:** Kích hoạt **Kiểm tra sức khỏe Amboss = Có** để nút của bạn gửi ping thường xuyên đến Amboss. Bạn sẽ nhận được cảnh báo nếu nút của bạn có vẻ ngoại tuyến.





- **Các tính năng khác:** Tự động đẩy số dư, tích hợp **Magma/Hydro** (thị trường thanh khoản) và quyền truy cập vào số liệu thống kê hiệu suất chi tiết.



Tích hợp Amboss bổ sung **bảo mật Layer** thiết yếu với tính năng sao lưu bên ngoài tự động và giám sát tính khả dụng, có thể truy cập trực tiếp từ ThunderHub.



### Công cụ



Phần **Công cụ** nhóm các công cụ nâng cao khác nhau để quản lý nút của bạn. Sau đây là Elements chính:



![Interface des outils disponibles](assets/fr/18.webp)





- **Sao lưu:** Quản lý thủ công các bản sao lưu kênh của bạn (SCB). ThunderHub cho phép bạn **tải xuống tệp sao lưu đầy đủ** của các kênh của bạn (tùy chọn "Sao lưu tất cả các kênh -> Tải xuống"). Lưu tệp `channel-all.bak` này ở nơi an toàn - tệp này rất cần thiết để khôi phục tiền của bạn trong trường hợp xảy ra sự cố. Bạn cũng có thể **nhập** tệp sao lưu khi triển khai lại một nút.





- **Kế toán:** Công cụ xuất báo cáo tài chính bao gồm phí đã kiếm/đã trả và khối lượng được định tuyến trong một khoảng thời gian nhất định.
- **Tin nhắn đã ký:** **Ký hoặc xác minh tin nhắn** bằng nút của bạn để chứng minh Ownership của nút Lightning của bạn thông qua chữ ký mật mã.
- Macaroons (phần Bakery):** Quản lý macaroons LND** để tạo quyền truy cập tùy chỉnh. "Bakery" Interface cho phép bạn chọn chính xác từng quyền: "Thêm hoặc xóa Peers", "Tạo địa chỉ chuỗi", "Tạo hóa đơn", "Tạo Macaroons", "Derive Keys", "Get Access Keys", "Get Chain Transactions", "Get Invoices", "Get Wallet Info", "Get Payments", "Get Peers", "Pay Invoices", "Revoke Access IDs", "Send to Chain Addresses", "Sign bytes", "Sign Messages", "Stop daemon", "Verify bytes signature", "Verify messages", v.v. Mỗi quyền có thể được kích hoạt riêng lẻ bằng các nút "Yes/No" để tạo macaroon tùy chỉnh.
- **Thông tin hệ thống:** Hiển thị phiên bản Wallet và RPC được kích hoạt.



Tóm lại, phần Công cụ tập hợp các chức năng quản trị nâng cao - sao lưu, kế toán, bảo mật và quản lý quyền truy cập - trong một Interface thống nhất.



### Tráo đổi



Tab **Swap** của ThunderHub cho phép bạn hoán đổi Lightning satoshi sang Bitcoin On-Chain thông qua dịch vụ Boltz. Tính năng này hữu ích để "đổ" lượng thanh khoản Lightning dư thừa vào kênh mà không cần đóng kênh.



![Interface de swap via Boltz](assets/fr/19.webp)



Quá trình này rất đơn giản:





- **Số tiền**: Xác định số tiền cần trao đổi
- **Address**: Nhập tín hiệu Bitcoin Address
- **Thực hiện**: ThunderHub giao tiếp với Boltz để tự động xử lý Exchange



**Những lợi ích:**




- Dịch vụ không lưu ký (không lưu ký tiền mặt)
- Bảo tồn các kênh hiện có của bạn
- Interface tích hợp dễ sử dụng



Boltz tính một khoản hoa hồng nhỏ và bạn phải trả phí giao dịch Bitcoin tiêu chuẩn. ThunderHub hiển thị tất cả chi phí trước khi xác nhận.



### Thống kê



Phần **Thống kê** của ThunderHub cung cấp **thống kê nâng cao** về nút Lightning của bạn để phân tích hiệu suất và tối ưu hóa định tuyến.



![Statistiques du nœud via Amboss](assets/fr/20.webp)



Phần này rất cần thiết để tối ưu hóa chi phí, xác định các kênh thành công và lập kế hoạch mở rộng nút của bạn.



## Phần kết luận



**ThunderHub** đã khẳng định mình là công cụ thiết yếu để quản lý dễ dàng một nút Lightning **LND**. Interface hiện đại này cung cấp tất cả các chức năng thiết yếu: quản lý kênh, thanh toán, giám sát, với các tính năng tiên tiến như tự động cân bằng lại và tích hợp Amboss.



**Lợi ích chính:**




- Interface đẹp và trực quan
- Các công cụ mạnh mẽ (cân bằng lại, hoán đổi Boltz, sao lưu tự động)
- Tương thích với Umbrel, Voltage, RaspiBlitz và các bản phân phối khác



ThunderHub dân chủ hóa việc quản lý nút Lightning nâng cao, giúp bạn có thể truy cập những gì trước đây yêu cầu các lệnh kỹ thuật phức tạp. Cho dù bạn là người mới bắt đầu hay người vận hành có kinh nghiệm, ThunderHub cho phép bạn quản lý nút Lightning của mình một cách hiệu quả thông qua Interface hiện đại, toàn diện.



## Tài nguyên



**Liên kết chính thức:**




- **Trang web chính thức:** [thunderhub.io](https://thunderhub.io)
- **Tài liệu:** [docs.thunderhub.io](https://docs.thunderhub.io)
- **Mã nguồn GitHub:** [github.com/apotdevin/thunderhub](https://github.com/apotdevin/thunderhub)