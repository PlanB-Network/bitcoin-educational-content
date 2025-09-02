---
name: LNbit

description: Nền tảng kế toán thương mại
---

![presentation](assets/lnbits-intro.webp)

# Hệ thống kế toán


LNbits được tích hợp rất nhiều công cụ để kiểm soát và phân bổ dòng tiền vào và ra của bạn, kết nối cửa hàng trực tuyến hoặc thậm chí các thiết bị như Hardware Wallet hoặc máy ATM do bạn tự chế tạo. Các loại người dùng bao gồm:


- Những người sở hữu Wallet muốn sử dụng LNbits như Interface để quản lý quỹ cũng như các tính năng bổ sung của nó.
- Các thương gia hoặc nhà cung cấp dịch vụ trực tuyến và ngoại tuyến muốn chấp nhận thanh toán Bitcoin trên chuỗi và Lightning Network.
- Các nhà phát triển muốn xây dựng ứng dụng Lightning Network.
- Các nhà điều hành nút muốn tích hợp nút của họ với hệ thống LNbits cho mục đích kế toán.
- Mỗi loại đều có những nhu cầu khác nhau. Chúng tôi xây dựng LNbit theo mô-đun để mọi người dùng đều có thể sử dụng các tính năng của chúng tôi theo cách phù hợp nhất với mình.


# Quản lý Wallet


LNbits là một hệ thống kế toán mã nguồn mở và miễn phí - không phải là trình quản lý nút. Quản lý kênh là phạm vi của nút Lightning được kết nối với LNbits như một nguồn tài trợ như LND hoặc c-lightning. Người dùng Siêu cấp hoặc Người dùng Quản trị trong hệ thống LNbits chịu trách nhiệm quản lý khả năng truy cập và cấu hình chung của các tính năng kế toán và tiện ích mở rộng nội bộ.


LNbits hoạt động như một Interface giữa người dùng và nút Lightning, cung cấp một cách đơn giản, thân thiện với người dùng để quản lý và tương tác với mạng thanh toán.


Hãy nghĩ về LNbits như một "khung mô-đun wordpress" cho nút của bạn. Một nền tảng dễ quản lý, dựa trên các tiện ích mở rộng mà bạn có thể kết hợp cho nhiều trường hợp sử dụng.


Hãy coi LNbits như phần mềm quản lý tài chính ngân hàng của riêng bạn. Nút của bạn cung cấp các kênh thanh toán và LNbits mở rộng nút của bạn để có thể chạy nhiều hơn một Lightning Wallet mà nút của bạn đi kèm. Những ví này không nhất thiết phải thuộc về bạn. Giả sử bạn, với tư cách là người vận hành nút LN, đã có đủ thanh khoản kênh và tiền mặt và giờ bạn muốn cung cấp một số dịch vụ ngân hàng Bitcoin cho bạn bè, gia đình, cửa hàng của riêng bạn hoặc các thương gia thường xuyên khác.


Bạn sẽ cung cấp cho họ một cách đơn giản để mở một "tài khoản ngân hàng" trên nút của bạn mà không cần truy cập vào các ví khác trên nút của bạn và vào toàn bộ thanh khoản của nút, mà chỉ là một phần của họ. Nút của bạn (ngân hàng) chỉ đóng vai trò là nhà cung cấp dịch vụ vận chuyển cho các khoản thanh toán của họ (vào/ra).


LƯU Ý: tất cả tiền mà "khách hàng" của bạn gửi vào tài khoản ngân hàng LNbits trên nút của bạn sẽ được chuyển thẳng vào kênh LN của nút. Điều đó có nghĩa là BẠN thực sự là chủ sở hữu của số tiền đó. Bạn sẽ có trách nhiệm lớn đối với số tiền của họ. Đừng làm điều xấu và bỏ trốn với số tiền đó, đừng làm điều xấu và tính phí cao. Chúng tôi muốn làm khó những kẻ làm ngân hàng fiat, chứ không phải làm khó lẫn nhau (người dùng Bitcoin).


# Nền tảng demo


Bạn có thể tìm thấy bản demo tại [https://legend.lnbits.com](https://legend.lnbits.com). Bản demo hoạt động đầy đủ và có thể được sử dụng để tìm hiểu về Lightning Network, các tính năng của LNbits và LNURL nói chung. Mặc dù chúng tôi không thể ngăn cản bạn, nhưng chúng tôi muốn bạn không sử dụng nó cho thiết lập sản xuất của mình. Chúng tôi không chỉ thường xuyên làm việc trên các máy chủ để kiểm tra các tính năng mới mà còn khuyến khích bạn tự vận hành node và LNbits của mình một cách độc lập. Nếu bạn cảm thấy việc vận hành một node là quá nhiều vào lúc này, bạn có thể kết nối LNbits với một dịch vụ tài trợ lưu ký trên đám mây như Opennode, Luna hoặc Votage, hoặc với Lightning Tipbot trên Telegram, v.v.


# Tờ rơi LNbits


Bạn muốn chia sẻ một số thông tin cơ bản cho một thương gia hoặc một người bạn trong ngành xây dựng? Chúng tôi rất vui mừng được giới thiệu tờ rơi đầu tiên của chúng tôi dành cho mọi người. Kích thước tờ rơi được thiết kế theo chuẩn chung của thế giới, gồm 6 trang (gấp 2 lần), chiều rộng 3508 pixel và chiều cao 2480 pixel.


LNbits dành cho thương gia: [EN](/assets/lnbits-merchants-en.pdf) | [DE](/assets/lnbits-merchants-de.pdf) | [ES](/assets/lnbits-merchants-es.pdf) | [IT](/assets/lnbits-merchants-it.pdf) | [PL](/assets/lnbits-merchants-pl.pdf)


LNbits dành cho thợ xây dựng: [EN](/assets/lnbits-builders-en.pdf) | [DE](/assets/lnbits-builders-de.pdf) | [ES](/assets/lnbits-builders-es.pdf) | [IT](/assets/lnbits-builders-it.pdf) | [PL](/assets/lnbits-builders-pl.pdf)


# Một số điều cơ bản


LNbits hoạt động dựa trên giao thức LNURL, nghĩa là các yêu cầu có thể được thực hiện dưới hai hình thức: liên kết https:// clearnet (không cho phép chứng chỉ tự ký) hoặc liên kết http:// v2/v3 onion. Để cung cấp các dịch vụ LNbits như mã QR LNURLp/w hoặc Thẻ NFC, có thể sử dụng ngoài thực tế, bạn cần mở LNbits lên clearnet (https).


Trước khi cài đặt LNbits, hãy đảm bảo bạn đã đọc và hiểu các hướng dẫn chung sau đây về LNbits là gì và những khả năng mà nó mang lại cho bạn.



- [Hướng dẫn LND](https://docs.lightning.engineering/) | Cài đặt LND
- [Ví dụ cấu hình LND](https://github.com/lightningnetwork/LND/blob/master/sample-LND.conf) | Cài đặt LND
- [Hướng dẫn CLN](https://docs.corelightning.org/docs/installation) | Cài đặt CLN
- [LUDs](https://github.com/lnurl/luds) Đặc tả LNURL | [NIPs](https://github.com/nostr-protocol/nips) Đặc tả Nostr
- [Chạy Watchtower](https://docs.lightning.engineering/lightning-network-tools/LND/Watchtower) | Rất quan trọng!


Hướng dẫn chi tiết hơn về cách sử dụng LNbit trong các trường hợp sử dụng cụ thể tại đây:



- [Bắt đầu với LNbits](https://darthcoin.substack.com/p/getting-started-lnbits) | Hướng dẫn Substack
- [Những việc cần làm để đảm bảo an toàn cho bạn với LNbits](https://youtu.be/i5FQf96e6zg) | Video trên Youtube
- [Ngân hàng tư nhân trên Lightning Network](https://darthcoin.substack.com/p/Bitcoin-private-banks-over-lightning) | Hướng dẫn Substack
- [Quản lý ví lưu ký cho bạn bè và gia đình](https://darthcoin.substack.com/p/the-bank-of-lnbits) | Hướng dẫn Substack
- [LNbits cho nhà hàng/khách sạn nhỏ](https://darthcoin.substack.com/p/lnbits-for-small-merchants) | Hướng dẫn Substack
- [Sử dụng LNbits Streamer copilot](https://darthcoin.substack.com/p/lnbits-streamer-copilot) | Hướng dẫn Substack
- [Bắt đầu thị trường NOSTR của bạn với LNbits](https://darthcoin.substack.com/p/lnbits-nostr-market) | Hướng dẫn Substack
- [Sử dụng LNbits cho các dự án trường học hoặc sự kiện lễ hội](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools) Hướng dẫn Substack



# Cài đặt LNbits


## Hướng dẫn cài đặt cơ bản


LNbits có thể được cài đặt trên bất kỳ máy tính chạy hệ điều hành Linux nào. Nó không yêu cầu máy tính hoặc máy chủ mạnh, chỉ cần đủ bộ nhớ RAM và dung lượng ổ đĩa cho cơ sở dữ liệu. Nó có thể được chạy riêng biệt từ một nút BTC/LN (máy tính cục bộ hoặc VPS từ xa) hoặc cùng chạy trên một máy tính với nút đó hoặc đã được cài đặt trong một máy tính phần mềm nút bundle.


Bạn có thể chọn giữa các trình quản lý gói phổ biến nhất như poetry và nix. Theo mặc định, LNbits sẽ sử dụng SQLite làm cơ sở dữ liệu. Bạn cũng có thể sử dụng PostgreSQL, được khuyến nghị cho các ứng dụng có tải cao. [Đây là hướng dẫn cài đặt cơ bản bằng poetry hoặc nix](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md).


Đối với những người mới bắt đầu, bạn sẽ tìm thấy hướng dẫn từng bước chi tiết hơn để chạy LNbit trong các môi trường cụ thể:


- [LNbits trên clearnet](https://ereignishorizont.xyz/lnbits-server/en/) của Axel
- [LNbits trên VPS](https://github.com/TrezorHannes/vps-lnbits) của Hannes
- [LNbits trên cloudflare](https://www.nodeacademy.org/lnbits) của Leo


Bạn cũng có thể tìm thấy video về [Cài đặt Docker trên VPS với PostgreSQ, LightningTipBot làm nguồn tài trợ bằng cách sử dụng nginx](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/).


[Thêm các kịch bản cài đặt tại đây](https://darthcoin.substack.com/p/build-your-own-lnbits-app-server).


Đối với các nút phần mềm gói, vui lòng tham khảo tài liệu cụ thể của họ về LNbit: [Citadel](https://runcitadel.space) | [Umbrel](https://umbrel.com) | [MyNode](https://mynodebtc.com) | [RaspiBlitz](https://raspiblitz.org/) | [RaspiBolt](https://raspibolt.org)


## LNbits SaaS


Nếu bạn không quan tâm đến kỹ thuật và cũng không muốn tự mình lưu trữ nguồn tài trợ cũng như lnbits, thì có một phiên bản [LNbits SaaS] (https://saas.lnbits.com) (Phần mềm dưới dạng dịch vụ) bạn có thể sử dụng. Về cơ bản, nó giống như LNbits trên nền tảng đám mây, nhưng bạn có thể tự xác định nguồn tài trợ (ví dụ: Node, LNbits Wallet, LNtipbot, fakewallet, v.v.) và các biến môi trường - điều mà hầu hết các giải pháp đám mây khác không làm được.


[Đây là hướng dẫn chi tiết về cách sử dụng LNbits SaaS cho các trường hợp sử dụng cụ thể](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools).


## Nguồn tài trợ


LNbits không phải là phần mềm quản lý node mà là hệ thống kế toán tập trung vào LN dựa trên nguồn tài trợ LND hoặc CLN. Sau lần cài đặt đầu tiên, bạn có thể truy cập LNbits tại http://localhost:5000/.


Để sửa đổi nguồn tài trợ, hãy truy cập URL siêu người dùng của bạn và chọn nguồn tài trợ trong "Quản lý máy chủ" hoặc chỉnh sửa tệp .env bằng cách sửa đổi `LNBITS_BACKEND_WALLET_CLASS` thành nguồn bạn cần nếu bạn đặt `adminUI=TRUE` trong `.env`.


Bạn sẽ tìm thấy tệp .env trong thư mục lnbits/ hoặc lnbits/apps/data bằng cách mở rộng lệnh để liệt kê các tệp trong thư mục của bạn bằng `ls -a`.


Bạn cũng có thể cần cài đặt các gói bổ sung hoặc thực hiện các bước thiết lập bổ sung, chọn nguồn tài trợ mong muốn. Sau khi khởi động lại, thiết lập mới của bạn sẽ được kích hoạt.


Tôi có thể sử dụng nguồn tài trợ nào cho LNbits?


LNbits có thể hoạt động trên nhiều nguồn tài trợ của mạng lưới Lightning. Hiện tại, có hỗ trợ cho CoreLightning, LND, LNbits, LNPay, OpenNode, và nhiều nguồn khác sẽ được bổ sung thường xuyên.

Điều quan trọng là phải chọn một nguồn có tính thanh khoản tốt và được kết nối tốt với các đối tác. Nếu bạn sử dụng LNbits cho các dịch vụ công, thanh toán của người dùng sẽ được thực hiện thuận lợi theo cả hai hướng.


Có thể cấu hình Wallet (nguồn tài trợ) bằng cách sử dụng các biến môi trường LNbits sau trong tệp `.env` hoặc trong tài khoản siêu người dùng của bạn trong phần Quản lý máy chủ.

Nếu bạn muốn sử dụng phiên bản .env, bạn có thể tìm thấy các thông số tại đây:



### CoreLightning


- CLN
  - `LNBITS_BACKEND_WALLET_CLASS`: **CoreLightningWallet**
  - `CORELIGHTNING_RPC`: /file/path/lightning-RPC
- Tia lửa (c-tia chớp)
  - `LNBITS_BACKEND_WALLET_CLASS`: **Ví Spark**
  - `SPARK_URL`: http://10.147.17.230:9737/RPC
   - `SPARK_TOKEN`: khóa_truy_cập_bí_mật

### Lightning Network Daemon


- LND (PHẦN CÒN LẠI)
  - `LNBITS_BACKEND_WALLET_CLASS`: **Ví LndRest**
  - `LND_REST_ENDPOINT`: http://10.147.17.230:8080/
  - `LND_REST_CERT`: /file/path/tls.cert
  - `LND_REST_MACAROON`: /file/path/admin.macaroon hoặc Bech64/Hex
  - `LND_REST_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn
- LND (gRPC)
  - `LNBITS_BACKEND_WALLET_CLASS`: **Ví Lnd**
  - `LND_GRPC_ENDPOINT`: địa chỉ ip
  - `LND_GRPC_PORT`: cổng
  - `LND_GRPC_CERT`: /file/path/tls.cert
  - `LND_GRPC_MACAROON`: /file/path/admin.macaroon hoặc Bech64/Hex

Bạn cũng có thể sử dụng macaroon được mã hóa AES (thông tin thêm) bằng cách sử dụng


  - `LND_GRPC_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn

Để mã hóa macaroon của bạn, hãy chạy `./venv/bin/python lnbits/wallets/macaroon/macaroon.py`.


### LNbits (một trường hợp LNbits khác)



- Phiên bản LNbits được lưu trữ trên máy chủ đám mây hoặc máy chủ tại nhà của bạn
  - `LNBITS_BACKEND_WALLET_CLASS`: **Ví LNbit**
  - `LNBITS_ENDPOINT`: https://lnbits.mydomain.com
  - `LNBITS_KEY`: my-lnbits-AdminKey
- Máy chủ demo LNbits Legend (!! KHÔNG sử dụng máy chủ này cho mục đích sản xuất/thương mại, chỉ sử dụng để thử nghiệm !!)
  - `LNBITS_BACKEND_WALLET_CLASS`: **Ví LNbit**
  - `LNBITS_ENDPOINT`: https://legend.lnbits.com
  - `LNBITS_KEY`: chú thích-lnbits-AdminKey

### Lightning TipBot


Để kết nối [Lightning Tipbot](https://t.me/LightningTipBot) của bạn từ Telegram, bạn sẽ cần thiết lập tham số sau:


  - `LNBITS_BACKEND_WALLET_CLASS`: **Ví LnTips**
  - `LNBITS_ENDPOINT`: https://LN.tips
  - `LNBITS_KEY`: Để lấy Khóa, bạn sẽ cần chạy /api trong cuộc trò chuyện riêng với LightningTipbot trên Telegram một lần.


Ngoài ra, hãy xem hướng dẫn này để biết cách cài đặt [LNbits với LightningTipBot qua vps](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/)


### TRUNG TÂM IBEX


Đăng ký [tại đây](https://ibexpay.ibexmercado.com/onboard) sau đó nhận khóa/mã thông báo từ đó, điểm cuối là https://ibexpay-api.ibexmercado.com.

Để biết thêm thông tin, hãy xem [Tài liệu API IBEX](https://ibexpay-api.readme.io/reference/getting-started-with-your-api).


### LNPay

Để trình lắng nghe Invoice hoạt động, bạn cần có một URL có thể truy cập công khai trong LNbits của mình và phải thiết lập [webhook LNPay](https://dashboard.lnpay.co/webhook/) trỏ đến `<your LNbits host>/Wallet/webhook` với sự kiện "Wallet Receive" và không có khóa bí mật nào được cung cấp. Thiết lập `https://mylnbits/Wallet/webhook` sẽ là URL điểm cuối được thông báo về bất kỳ khoản thanh toán nào.


  - `LNBITS_BACKEND_WALLET_CLASS`: **Ví LNPay**
  - `LNPAY_API_ENDPOINT`: https://api.lnpay.co/v1/
  - `LNPAY_API_KEY`: sak_apiKey
  - `LNPAY_WALLET_KEY`: waka_apiKey


### OpenNode

Để Invoice hoạt động, bạn cần có một URL có thể truy cập công khai trong LNbits của mình. Cài đặt webhook là tùy chọn.


  - `LNBITS_BACKEND_WALLET_CLASS`: **Ví OpenNode**
  - `OPENNODE_API_ENDPOINT`: https://api.opennode.com/
  - `OPENNODE_KEY`: opennodeAdminApiKey


### Alby


Alby là tiện ích mở rộng trình duyệt có chức năng LN Wallet và tài khoản LNDHUB có thể được sử dụng làm nguồn tài trợ cho LNbits. [Chi tiết hơn tại đây](https://getalby.com/).


Để Invoice hoạt động, bạn phải có URL có thể truy cập công khai trong LNbits của mình. Không cần thiết lập webhook thủ công. Bạn có thể truy cập generate và Alby token tại đây: https://getalby.com/developer/access_tokens/new



- `LNBITS_BACKEND_WALLET_CLASS`: Ví Alby
- `ALBY_API_ENDPOINT`: https://api.getalby.com/
- `ALBY_ACCESS_TOKEN`: AlbyAccessToken


## Hướng dẫn bổ sung / khắc phục sự cố


Dưới đây là một số hướng dẫn bổ sung phòng trường hợp bạn cần. Nhấp vào mũi tên để mở rộng mô tả.


### Công tắc giết người 🚨


Gần đây, có rất nhiều lỗi nguy hiểm không chỉ trong toàn bộ không gian mà còn trong LNbits nên chúng tôi quyết định phải hành động. Giờ đây, bạn có thể chọn nhận cảnh báo và/hoặc thực hiện hành động trực tiếp khi lỗ hổng hoặc lỗi có thể dẫn đến mất tiền xảy ra lần nữa.


![killswitchn](assets/lnbits-killswitch.webp)


Nếu chuyển sang void-Wallet, tất cả các loại người dùng trên phiên bản này sẽ thấy một biểu ngữ màu vàng ở vị trí thông thường mà bạn sẽ thấy thông báo "LNbits đang ở giai đoạn Beta" bên cạnh khu vực chủ đề/ngôn ngữ ở bên phải - và đó là dấu hiệu rõ ràng nhất cho thấy có điều gì đó đã xảy ra. Hãy xem tab máy chủ mới của bạn được tô sáng trong Green ở phía bên trái cửa sổ.


Nó hoạt động như thế nào? Khi killswitch được bật, một kho lưu trữ GitHub bí mật chỉ dành cho nhóm cốt lõi LNbits sẽ được kiểm tra sau mỗi X phút (có thể chỉ định). Nếu một lỗi dễ bị tấn công được công bố trong kho lưu trữ này, nó sẽ đóng vai trò là tín hiệu kích hoạt killswitch trên tất cả các cài đặt đã đăng ký và chuyển đổi phiên bản lnbits của bạn sang sử dụng void Wallet. Nếu đám mây đã được dọn sạch và bạn đã cài đặt bản cập nhật bảo mật, bạn có thể đặt lại nguồn tài trợ thành node, Wallet hoặc bất kỳ node nào bạn đang sử dụng thông qua phần Quản lý Máy chủ. Wiki này có một phần về việc chuyển đổi nguồn tài trợ nếu bạn không biết phải cấu hình như thế nào.



### Sự khác biệt giữa quản trị viên và siêu người dùng


Giao diện Quản trị LNbits cho phép bạn thay đổi cài đặt LNbits thông qua giao diện người dùng LNbits. Mặc định, tính năng này bị tắt và khi bạn đặt biến môi trường `LNBITS_ADMIN_UI=true` trong tệp `.env` lần đầu tiên, các cài đặt sẽ được khởi tạo và sử dụng. Từ đó, các cài đặt tương ứng từ cơ sở dữ liệu sẽ được sử dụng thay vì cài đặt trong tệp .env.


### Người dùng siêu cấp


Với Giao diện Quản trị, chúng tôi đã giới thiệu siêu người dùng, người có quyền truy cập vào máy chủ, do đó có thể thay đổi các thiết lập có thể làm máy chủ bị sập hoặc không phản hồi thông qua giao diện người dùng và API, chẳng hạn như thay đổi nguồn tài trợ. Siêu người dùng chỉ được lưu trữ bên trong bảng thiết lập của cơ sở dữ liệu. Sau khi thiết lập được "đặt lại về mặc định" và khởi động lại, một siêu người dùng mới sẽ được tạo. Chúng tôi cũng đã thêm một trình trang trí cho các tuyến API để kiểm tra sự tồn tại của siêu người dùng. ID của siêu người dùng này không bao giờ được gửi qua API và giao diện người dùng, và chỉ nhận được một giá trị bool (có/không) cho dù bạn có phải là siêu người dùng hay không.


Chỉ người dùng siêu cấp mới được phép chuyển satoshi vào các ví khác nhau thông qua phần "Nạp tiền".


Bạn cũng có thể đăng siêu người dùng qua webhook lên một dịch vụ khác khi nó được tạo. Thông tin thêm tại đây https://github.com/lnbits/lnbits/blob/main/lnbits/settings.py `class SaaSSettings`


Ở giao diện người dùng, bạn cũng có thể thay đổi hình ảnh cửa hàng hiển thị trên trang "tạo Wallet" bằng cách mở phần Quản lý máy chủ và chọn Chủ đề -> Logo tùy chỉnh.


### Người dùng quản trị


Biến môi trường: `LNBITS_ADMIN_USERS`, danh sách ID người dùng được phân cách bằng dấu phẩy. Người dùng quản trị có thể thay đổi cài đặt trong giao diện quản trị - ngoại trừ cài đặt nguồn tài trợ, vì việc này sẽ yêu cầu khởi động lại máy chủ và có khả năng khiến máy chủ không thể truy cập được. Họ cũng có quyền truy cập vào tất cả các tiện ích mở rộng được dành riêng cho họ trong `LNBITS_ADMIN_EXTENSIONS`.


### Người dùng được phép


Biến môi trường: `LNBITS_ALLOWED_USERS`, danh sách ID người dùng được phân cách bằng dấu phẩy. Sau khi xác định những người dùng này, LNbits sẽ không còn được sử dụng bởi công chúng nữa. Chỉ những người dùng và quản trị viên đã xác định mới có thể truy cập giao diện người dùng LNbits.




#### Cập nhật LNbits

Để cập nhật phiên bản cục bộ LNbits thông thường, bạn chỉ cần sao chép và dán các lệnh CLI sau:


```
cd lnbits
## Stop LNbits with `ctrl + x`
git pull
## Keep your poetry install up to date, this can be done with
poetry self update
poetry install --only main
## or
git checkout main && git pull && poetry install
## Start LNbits with
poetry run lnbits
```


Nếu bạn chạy Raspiblitz hoặc MyNode, bạn có thể cần thêm một

```
sudo systemctl restart lnbits
```

cuối cùng, vì nó chạy LNbits như một dịch vụ.


Trên Umbrel/Citadel các lệnh sẽ là

```
cd ~/apps/lnbits
git pull upstream main
sudo ~/scripts/app start lnbits
```


#### Di chuyển từ SQLite sang PostgreSQL


Nếu bạn đã cài đặt và chạy LNbits trên cơ sở dữ liệu SQLite, chúng tôi thực sự khuyên bạn nên chuyển sang postgres nếu bạn định chạy LNbits ở quy mô lớn.


Có một tập lệnh đi kèm giúp bạn dễ dàng di chuyển. Bạn cần cài đặt Postgres và có mật khẩu cho người dùng (xem hướng dẫn cài đặt Postgres ở trên). Ngoài ra, phiên bản LNbits của bạn cần chạy một lần trên Postgres để triển khai cơ sở dữ liệu Schema trước khi quá trình di chuyển có thể hoạt động:


```
# STOP LNbits

# add the database connection string to .env 'nano .env' LNBITS_DATABASE_URL=
# postgres://<user>:<password>@<host>/<database> - alter line bellow with your user, password and db name
LNBITS_DATABASE_URL="postgres://postgres:postgres@localhost/lnbits"
# save and exit

# START LNbits
# STOP LNbits
poetry run python tools/conv.py
# or
make migration
```

Hy vọng bây giờ mọi thứ hoạt động và được di chuyển... Khởi chạy lại LNbits và kiểm tra xem mọi thứ có hoạt động bình thường không.



#### Sao lưu và khôi phục cơ sở dữ liệu


Vui lòng tham khảo [hướng dẫn rất chi tiết này về quy trình sao lưu và khôi phục](https://ereignishorizont.xyz/lnbits-server/en/#94_LNbits_-_Databases_Backup_Restore).



#### Việc cấp vốn cho LNbits Wallet từ nút của tôi không hiệu quả


Nếu bạn muốn gửi Sats từ cùng một nút là nguồn tài trợ cho LNbit của bạn, bạn sẽ cần chỉnh sửa tệp LND.conf.


Các tham số cần đưa vào là: `allow-circular-route=1`


Vui lòng thực hiện việc này trong phần Tùy chọn ứng dụng của LND.conf. Trên một số nút bundle, việc khởi động LND có thể bị lỗi.


LƯU Ý: Bạn nên sử dụng tiện ích mở rộng adminUI mới với tùy chọn "Nạp tiền" để thêm tiền vào tài khoản LNbits.


#### Lỗi 426

Tôi gặp lỗi: "lnurl cần được phân phối qua miền https hoặc tor có thể truy cập công khai. Yêu cầu nâng cấp 426"</summary>


Lỗi này thường xảy ra do LNbit của bạn phía sau đường hầm ngnix không chuyển tiếp LNURL Address chính xác. Hãy dừng LNbit và chỉnh sửa tệp .env bằng cách thêm dòng này:

`CHO_PHÉP_IPS_CHUYỂN_ĐẾN=*`


Ngoài ra, nếu bạn sử dụng thiết lập ngnix, hãy đảm bảo rằng bạn có các tiêu đề này trong cấu hình ngnix:


```
RequestHeader set "X-Forwarded-Proto" expr=%{REQUEST_SCHEME}
RequestHeader set "X-Forwarded-SSL" expr=%{HTTPS}
```


#### Lỗi mạng

Tôi gặp lỗi "lỗi https", lỗi mạng" hoặc các lỗi khác khi quét mã QR</summary>


Tin xấu là đây là lỗi định tuyến có thể có khá nhiều lý do. Trước tiên, hãy kiểm tra LNURL của QR bằng [Lightning Decoder](https://lightningdecoder.com/) nếu bạn thấy có gì bất thường. Hãy cùng thử một vài vấn đề có thể xảy ra nhất và giải pháp cho chúng.


LNbits chỉ chạy qua Tor, bạn không thể mở nó trên miền công cộng như lnbits.yourdomain.com



- Nếu bạn muốn thiết lập như vậy, hãy mở LNbits Wallet bằng URI .onion và tạo lại. Bằng cách này, mã QR được tạo để có thể truy cập thông qua URI .onion này, tức là chỉ thông qua tor. Không nên generate mã QR đó từ URI .local, vì nó sẽ không thể truy cập qua internet - chỉ có thể truy cập từ mạng LAN tại nhà của bạn.
- Mở ứng dụng LN Wallet mà bạn đã dùng để quét mã QR đó và lần này bằng Tor (xem phần cài đặt ứng dụng Wallet). Nếu ứng dụng không hỗ trợ Tor, bạn có thể sử dụng Orbot (Android). Xem phần cài đặt để biết hướng dẫn chi tiết về cách mở LNbit cho clearnet/https.



#### Ngăn chặn người khác tạo ví trên LNbit của tôi


Khi bạn chạy LNbit trên clearnet, về cơ bản, mọi người đều có thể generate và Wallet trên đó. Vì tiền của nút của bạn được liên kết với các ví này, bạn có thể muốn ngăn chặn điều đó. Có hai cách để thực hiện:


Cấu hình người dùng và tiện ích mở rộng được phép trong tệp `.env` ([xem ví dụ về env tại đây](https://github.com/lnbits/lnbits/blob/main/.env.example)). Thao tác này chỉ hoạt động nếu bạn sử dụng cài đặt `adminUI=FALSE` trong tệp .env, nếu không, bạn cần thực hiện điều đó trong phần Quản lý Máy chủ -> Người dùng -> Người dùng Được phép. Những người khác sẽ không được phép sau đó.




#### Tùy chỉnh khung thời gian hết hạn Invoice


Giờ đây, bạn có thể tạo hóa đơn generate với thời hạn sử dụng tùy chỉnh. Tương thích với các nền tảng sau: LndRestWallet, LndWallet, CoreLightningWallet, EclairWallet, LnbitsWallet, SparkWallet!


Bạn có thể đặt `LIGHTNING_INVOICE_EXPIRY` trong tệp .env hoặc sử dụng AdminUI để thay đổi giá trị mặc định cho tất cả hóa đơn. Ngoài ra còn có một trường mới trong điểm cuối /api/v1/payments nơi bạn có thể đặt thời hạn sử dụng trong dữ liệu JSON.




## Wallet-URL đã bị xóa


### Wallet trên máy chủ demo legend.lnbits


Luôn lưu một bản sao Wallet-URL, Export2phone-QR hoặc LNDhub vào ví của bạn ở nơi an toàn. LNbits KHÔNG THỂ giúp bạn khôi phục chúng khi bị mất.


### Wallet trên nguồn tài trợ/nút của riêng bạn

Luôn lưu một bản sao của Wallet-URL, Export2phone-QR hoặc LNDhub cho ví của bạn ở nơi an toàn. Bạn có thể tìm thấy tất cả người dùng LNbits và Wallet-ID trong tiện ích mở rộng quản lý người dùng LNbits hoặc trong cơ sở dữ liệu sqlite của mình. Để chỉnh sửa hoặc đọc cơ sở dữ liệu LNbits, hãy vào thư mục LNbits /data và tìm tệp có tên sqlite.db. Bạn có thể mở và chỉnh sửa tệp này bằng Excel hoặc bằng trình soạn thảo SQL chuyên dụng như [trình duyệt SQLite](https://sqlitebrowser.org/).


Ngoài ra, bạn có thể dump ví thông qua CLI và xem mọi Wallet trong cơ sở dữ liệu của mình.


```
cd ~/app-data/lnbits/data
sqlite3 database.sqlite3
.dump wallets
```


Đầu ra sẽ trông giống như thế này


```
INSERT INTO wallets VALUES('f8a43fc363ea428db5c53b3559935f1f','NAME OF WALLET','1280ff5910a9c485a782a2376f338b6c','33b95b099ce848e3b484124373f681e5','2cca208ae6d94d438227b9487ff216f9');
```

và bạn muốn đưa những giá trị này vào một url như thế này


```
https://your.lnbits.com/wallet?usr=1280ff5910a9c485a782a2376f338b6c&wal=f8a43fc363ea428db5c53b3559935f1f
```


Trong đó, bạn thay thế f8a43fc363ea428db5c53b3559935f1f bằng giá trị đứng trước tên (trong ví dụ của chúng ta là f8a43fc363ea428db5c53b3559935f1f) và 1280ff5910a9c485a782a2376f338b6c là tên người dùng của bạn và sẽ trở thành giá trị hiển thị sau tên. Để thoát khỏi sqlite3, hãy nhập


```
.quit
```

#### LNURL cho lightning-Address ngược lại


Hãy thử [encoder](https://lnurl-codec.netlify.app/) từ fiatjaf hoặc [trang này](https://lightningdecoder.com/). Để thanh toán hoặc kiểm tra LNURLp, bạn cũng có thể sử dụng [LNurlpay](https://wwww.lnurlpay.com/). Nó phải ghi là HTTPS, KHÔNG PHẢI HTTP.



#### Cấu hình bình luận mà mọi người sẽ thấy khi thanh toán cho mã QR LNURLp của tôi

Khi bạn tạo LNURL-p, theo mặc định, hộp bình luận sẽ không được điền. Điều này có nghĩa là bạn không được phép đính kèm bình luận vào các khoản thanh toán.


Để cho phép bình luận, hãy thêm số ký tự của ô, từ 1 đến 250. Sau khi nhập số, ô bình luận sẽ được hiển thị trong quá trình thanh toán. Bạn cũng có thể chỉnh sửa LNURL-p đã tạo và thêm số đó.


![lnbits comments](assets/lnbits-comments.webp)


#### Gửi BTC onchain vào LNbits

Có hai cách để chuyển Exchange Sats từ BTC trên chuỗi sang LN BTC (tương ứng với LNbit).


##### Thông qua dịch vụ trao đổi bên ngoài.


Những người dùng khác không có quyền truy cập vào LNb của bạn có thể sử dụng dịch vụ hoán đổi như [Boltz](https://boltz.Exchange/), [FixedFloat](https://fixedfloat.com/), [DiamondHands](https://swap.diamondhands.technology/) hoặc [ZigZag](https://zigzag.io/). Điều này hữu ích nếu bạn chỉ cung cấp hóa đơn LNURL/LN từ phiên bản LNbits của mình, nhưng người thanh toán chỉ có Sats trên chuỗi nên họ sẽ phải hoán đổi Sats đó trước. Quy trình rất đơn giản: người dùng gửi BTC trên chuỗi đến dịch vụ hoán đổi và cung cấp LNURL/LN Invoice từ LNbits làm đích đến của giao dịch hoán đổi.


##### Sử dụng tiện ích mở rộng Onchain và Boltz LNbits.


Xin lưu ý rằng đây là một Wallet riêng biệt, không phải là LN BTC được LNbits đại diện là "Wallet của bạn" dựa trên nguồn tài trợ LN của bạn. Wallet trên chuỗi này cũng có thể được sử dụng để hoán đổi LN BTC sang (ví dụ: ví phần cứng của bạn) bằng cách sử dụng tiện ích mở rộng LNbits Boltz hoặc Deezy. Nếu bạn điều hành một cửa hàng trực tuyến được liên kết với LNbits của mình để thanh toán LN, việc thường xuyên rút toàn bộ Sats từ LN vào chuỗi sẽ rất tiện lợi. Điều này giúp có thêm dung lượng trong các kênh LN của bạn để có thể nhận Sats mới.


Quy trình dành cho những người không có Bitcoin Hardware Wallet:



- Sử dụng Electrum hoặc Sparrow wallet để tạo Wallet mới trên chuỗi và lưu bản sao lưu seed ở nơi an toàn.
- Đi tới thông tin Wallet và sao chép xpub.
- Truy cập LNbits - tiện ích mở rộng Onchain và tạo Watch-only wallet mới bằng xpub đó.
- Truy cập LNbits - tiện ích mở rộng Tipjar và tạo một Tipjar mới. Ngoài tùy chọn LN Wallet, hãy chọn tùy chọn onchain.
- Tùy chọn - Truy cập LNbits - tiện ích mở rộng SatsPay và tạo một khoản phí mới cho BTC onchain. Bạn có thể chọn giữa onchain và LN hoặc cả hai. Sau đó, nó sẽ tạo một Invoice có thể được chia sẻ.
- Tùy chọn - Nếu bạn sử dụng LNbits được liên kết với trang Wordpress + Woocommerce, sau khi bạn tạo/liên kết Watch-only wallet với cửa hàng btc LN Wallet, khách hàng sẽ có cả hai tùy chọn thanh toán trên cùng một màn hình.


Khi bạn nhận được khoản thanh toán bằng LNbits, nhật ký giao dịch sẽ chỉ hiển thị loại giao dịch đã tiếp tục.


![lnbits payment details](assets/lnbits-payment-details.webp)


Trong phần tổng quan giao dịch, bạn sẽ thấy một mũi tên Green nhỏ cho số tiền đã nhận và một mũi tên màu đỏ cho số tiền đã gửi.


Nếu bạn nhấp vào các mũi tên đó, một cửa sổ bật lên sẽ hiển thị thông tin chi tiết về các tin nhắn đính kèm cũng như tên người gửi (nếu có).


Để cấu hình tên hiển thị trong phần thanh toán, hiện tại LNbits không thể thực hiện việc này - nhưng có thể nhận. Điều này chỉ khả thi nếu LN Wallet của người gửi hỗ trợ [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (nameDesc) như [OBW, Blixt, Alby, ZBD, BitBanana](https://github.com/lnurl/luds?tab=readme-ov-file#lnurl-documents).


Sau đó, bạn sẽ thấy một bí danh/bút danh trong phần chi tiết giao dịch LNbits của mình (nhấp vào mũi tên). Lưu ý rằng bạn có thể cung cấp bất kỳ tên nào ở đó và tên đó có thể không liên quan đến tên người gửi thực sự nếu bạn nhận được.


![lnbits namedesc](assets/lnbits-namedesc.webp)


Để nhập tài khoản LNbits của bạn vào ứng dụng Wallet, hãy mở LNbits bằng tài khoản / Wallet bạn muốn sử dụng, vào "Quản lý tiện ích mở rộng" và kích hoạt tiện ích mở rộng LNDHUB. Mở tiện ích mở rộng LNDHUB, chọn Wallet bạn muốn sử dụng và quét mã QR "admin" hoặc "chỉ Invoice", tùy thuộc vào mức độ bảo mật bạn muốn cho Wallet đó.


Bạn có thể sử dụng [Zeus](https://zeusln.app/) hoặc [Bluewallet](https://bluewallet.io/) làm ứng dụng Wallet cho tài khoản lndhub trong đó BW hỗ trợ nhiều hơn một Wallet như vậy.


Khi thực hiện việc này, chúng tôi khuyên bạn nên đặt URI mạng LN thành URI của nút bạn. Nếu phiên bản LNbits của bạn chỉ có Tor, bạn cũng phải sử dụng các ứng dụng này với Tor đã được kích hoạt. Trong trường hợp này, bạn cũng cần mở trang LNbits thông qua Tor .onion Address của mình.


Nếu bạn gặp lỗi "loại Hash không được hỗ trợ" khi sử dụng ypub trong tiện ích mở rộng On-Chain, hãy kiểm tra xem phiên bản LNbits của bạn có đang sử dụng python 3.10 hay không. Phiên bản này có thể bị ảnh hưởng bởi [sự cố này](https://stackoverflow.com/questions/72409563/unsupported-Hash-type-ripemd160-with-hashlib-in-python). Chỉnh sửa openssl.cnf như mô tả trong câu trả lời stackoverflow và khởi động lại LNbits của bạn.



## Gia công & Xây dựng với LNbits


LNbits có đủ loại [API mở](https://legend.lnbits.com/docs) và các công cụ để lập trình và kết nối với nhiều thiết bị khác nhau cho vô số trường hợp sử dụng.


Khi bạn mới bắt đầu xây dựng, hãy bắt đầu với [bài thuyết trình MakerBits](https://www.youtube.com/channel/UCZhKfzK6_KWZ-CFC2wXQVBw/videos) của Ben Arc về việc xây dựng các tiện ích dựa trên LNbit.


### QUAN TRỌNG:


- LNbits hoạt động dựa trên giao thức LNURL, trong đó các yêu cầu có thể được thực hiện dưới hai hình thức: dưới dạng liên kết https:// clearnet (không cho phép chứng chỉ tự ký) hoặc dưới dạng liên kết onion http:// v2/v3. Để cung cấp các dịch vụ LNbits như mã QR LNURLp/w hoặc Thẻ NFC, có thể sử dụng ngoài thực tế, bạn cần mở LNbits để clearnet (https).
- Chỉ sử dụng cáp dữ liệu để cấp nguồn cho esp32. Không phải tất cả cáp đều hỗ trợ truyền dữ liệu ngoài việc cấp nguồn cho esp. Bạn sẽ không phải là người đầu tiên gặp trường hợp cáp đi kèm với esp chỉ là cáp cấp nguồn.
- Đảm bảo không sử dụng USB-Hub khi kết nối với các thiết bị khác. Điều này có thể dẫn đến những hiệu ứng lạ cần được gỡ lỗi (ví dụ: không khởi động hoặc không dừng).
- Để thực hiện các dự án ESP trên MacOS, bạn sẽ cần Trình điều khiển Cầu nối UART. Nếu bạn gặp sự cố với trình điều khiển trên hệ thống Mac hoặc Linux, bạn có thể tìm thấy chúng tại đây hoặc nếu có màn hình TTGO, hãy tìm trình điều khiển này. Nếu bạn đang sử dụng Windows và gặp sự cố kết nối, hãy đảm bảo tải xuống phiên bản CŨ 11.1.0 vì phiên bản mới hơn không hoạt động! Bạn cũng có thể tìm thấy một thiết bị đầu cuối nối tiếp tại đây để kiểm tra kết nối của mình - đặt tốc độ baudrate 115200.
- Mặc dù sử dụng Platform.io thoải mái hơn nhiều (ví dụ: các phần phụ thuộc được cài đặt tự động) nhưng chúng tôi khuyên bạn nên sử dụng Arduino cho những người mới bắt đầu xây dựng.
- Màn hình TT-Go S3: Màu sắc của miếng dán bảo vệ màn hình cho bạn biết chính xác bộ điều khiển nào (ST7735_redtab, ST7735_blacktag, ST7735_greetab, greentab128, ..) đã được sử dụng để lắp ráp nó. Hãy giữ lại để có thể gỡ lỗi nếu bạn tự lập trình và màn hình không hiển thị đồ họa chính xác, ví dụ: màu sắc sai, hình ảnh bị phản chiếu hoặc điểm ảnh lạc ở các cạnh. Nếu bạn cần làm điều này, có một hướng dẫn chi tiết về cách điều chỉnh cho các màn hình khác nhau.
- Luôn sử dụng chữ thường lnurl239xx thay vì LNURLl239xx
- Thêm lightning:lnurl1234xyz sẽ tạo mã QR yêu cầu mở Wallet của người dùng cho Invoice này khi quét (ứng dụng lightning được cài đặt lần cuối trên iOS, cài đặt trong Android)
- Nếu bạn flash esp32 qua web thì nó chỉ hoạt động với các trình duyệt sau (TL:DR Chrome, Edge & Opera).
- Xin lưu ý tài liệu tham khảo PIN-OUT này cho esp
- Khi bạn sử dụng FOSSoftware hoặc FOSGuides, vui lòng luôn dẫn link tác giả. Ai cũng thích xem con mình lớn lên và điều đó cũng khởi đầu cho một chuỗi phát triển thú vị đáng xem :)


Hãy đến [Nhóm Telegram Makerbits](https://t.me/makerbits) nếu bạn cần trợ giúp về một dự án - chúng tôi sẽ hỗ trợ bạn!


![lnbits hackathlon](assets/lnbits-hackathlon.webp)


Sau đây là một số danh mục dự án bạn có thể xây dựng bằng LNbits:



- [Thiết bị ký Nostr](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#nostr-signing-device)
- [Máy Archade](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#arcade-machine)
- [Gerty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#gerty)
- [Đèn Zap của chúng tôi](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#zap-lamp)
- [BTC/LN ATM](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#atm)
- [LNPoS](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lnpos-terminal)
- [Lightning Piggy](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lightning-piggy)
- [Hardware Wallet](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#hardware-Wallet)
- [Công tắc Bitcoin](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Bitcoin-switch)
- [Máy bán hàng tự động](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#vending-machine)
- [Bolty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bolty)
- [Nerdminer](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Nerdminer)
- [Bitcoin Ticker](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Bitcoin-ticker)
- [BTClock](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#btclock)
- [Lora và Mạng lưới Mesh](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lora)



- [TRỢ GIÚP & TÀI NGUYÊN](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#resources)
- [Thêm ví dụ về các dự án "Được hỗ trợ bởi LNbits" tại đây](https://github.com/lnbits/lnbits/wiki/Powered-by-LNbits).
- [Các trường hợp sử dụng cho LNbit](https://github.com/lnbits/lnbits/wiki/Use-Cases-of-LNbits)