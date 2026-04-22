---
name: RGB Lightning Node
description: Tôi có thể khởi chạy một node Lightning tương thích với RGB bằng RLN như thế nào?
---
![cover](assets/cover.webp)


Trong hướng dẫn từng bước này, bạn sẽ học cách thiết lập một node Lightning RGB trên môi trường Regtest. Chúng ta sẽ xem cách tạo RGB token và phân phối chúng trong các kênh.


## Dự án RLN


Nhóm RGB của Bitfinex đã làm việc từ năm 2022 để làm phong phú thêm hệ sinh thái RGB bằng cách phát triển một bộ công nghệ hoàn chỉnh. Thay vì hướng đến một sản phẩm thương mại duy nhất, nỗ lực của họ tập trung vào việc cung cấp các khối phần mềm mã nguồn mở, đóng góp vào các đặc tả giao thức RGB và tạo ra các tài liệu tham khảo triển khai.


Một trong những đóng góp đáng chú ý của Bitfinex cho hệ sinh thái RGB là thư viện [*RGBlib*](https://github.com/RGB-Tools/rgb-lib), được viết bằng Rust và có thể truy cập thông qua các liên kết trong Kotlin và Python, giúp đơn giản hóa đáng kể việc phát triển các ứng dụng RGB bằng cách đóng gói các cơ chế xác thực và tương tác phức tạp.


Nhóm Bitfinex cũng đã thiết kế một phiên bản di động của RGB, gọi là "[*Iris Wallet*](https://iriswallet.com/)", có sẵn trên Android. wallet này tích hợp việc sử dụng máy chủ proxy RGB để dễ dàng quản lý việc trao đổi dữ liệu off-chain (*lô hàng*) cho *Client-side Validation* trên RGB.


Bitfinex cũng đã phát triển dự án `rgb-lightning-node` (RLN). Đây là một Rust daemon dựa trên fork của `rust-lightning` (LDK), được sửa đổi để tính đến sự tồn tại của các tài sản RGB trong một kênh. Khi một kênh được mở, sự hiện diện của RGB token có thể được chỉ định, và mỗi khi trạng thái kênh được cập nhật, một chuyển đổi trạng thái được tạo ra phản ánh sự phân bố của token trong đầu ra Lightning. Điều này cho phép:




- Ví dụ, hãy mở các kênh Lightning bằng USDT;
- Định tuyến các thiết bị token này qua mạng, với điều kiện các đường dẫn định tuyến có đủ tính thanh khoản;
- Khai thác logic khóa thời gian và trừng phạt của Lightning mà không cần sửa đổi: chỉ cần neo quá trình chuyển đổi RGB vào một đầu ra bổ sung của commitment transaction.


Mã RLN vẫn đang trong giai đoạn alpha: chúng tôi khuyên bạn chỉ nên sử dụng nó trong **regtest** hoặc trên **testnet**.


## Lời nhắc nhở về giao thức RGB


RGB là một giao thức chạy trên nền tảng Bitcoin và mô phỏng chức năng hợp đồng thông minh và quản lý tài sản kỹ thuật số, mà không làm quá tải blockchain mà nó dựa trên. Không giống như các hợp đồng thông minh on-chain thông thường (như trên Ethereum chẳng hạn), RGB dựa vào hệ thống "*xác thực phía máy khách*": phần lớn dữ liệu và lịch sử trạng thái được trao đổi và lưu trữ độc quyền bởi những người tham gia, trong khi Bitcoin blockchain chỉ lưu trữ các cam kết mật mã nhỏ (thông qua các cơ chế như *Tapret* hoặc *Opret*). Do đó, trong giao thức RGB, Bitcoin blockchain chỉ đóng vai trò là máy chủ đóng dấu thời gian và hệ thống bảo vệ double-spending.


Hợp đồng RGB được cấu trúc giống như một cỗ máy trạng thái tiến hóa. Nó bắt đầu với một Genesis xác định trạng thái ban đầu (ví dụ: mô tả nguồn cung, mã giao dịch hoặc siêu dữ liệu khác) theo một Schema được định kiểu và biên dịch nghiêm ngặt. Sau đó, các State Transition và, nếu cần, State Extension được áp dụng để sửa đổi hoặc mở rộng trạng thái này. Mỗi thao tác, dù là chuyển giao tài sản có thể hoán đổi (RGB20) hay tạo ra tài sản độc nhất (RGB21), đều liên quan đến *Seal sử dụng một lần*. Chúng liên kết các Bitcoin và UTXO với các trạng thái off-chain và ngăn chặn việc chi tiêu kép, đồng thời đảm bảo tính bảo mật và khả năng mở rộng.


Để tìm hiểu thêm về cách thức hoạt động của giao thức RGB, tôi khuyên bạn nên tham gia khóa đào tạo toàn diện này:


https://planb.academy/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

## Cài đặt nút Lightning tương thích RGB


Để biên dịch và cài đặt tệp nhị phân `rgb-lightning-node`, chúng ta bắt đầu bằng cách sao chép kho lưu trữ và các mô-đun con của nó, sau đó chạy lệnh:


```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```


![RLN](assets/fr/01.webp)




- Tùy chọn `--recurse-submodules` cũng sao chép các thiết bị con cần thiết (bao gồm cả phiên bản đã sửa đổi của `rust-lightning`);
- Tùy chọn `--shallow-submodules` giới hạn độ sâu của bản sao để tăng tốc độ tải xuống, đồng thời vẫn cung cấp quyền truy cập vào các commit thiết yếu.


Từ thư mục gốc của dự án, chạy lệnh sau để biên dịch và cài đặt tệp nhị phân:


```bash
cargo install --locked --debug --path .
```


![RLN](assets/fr/02.webp)




- `--locked` đảm bảo rằng phiên bản của các phần phụ thuộc được tôn trọng;
- Tùy chọn `--debug` không bắt buộc, nhưng có thể giúp bạn tập trung hơn (bạn có thể sử dụng `--release` nếu muốn);
- `--path .` cho lệnh `cargo install` biết cần cài đặt từ thư mục hiện tại.


Sau khi thực thi lệnh này, một tệp thực thi `rgb-lightning-node` sẽ có sẵn trong thư mục `$CARGO_HOME/bin/` của bạn. Hãy đảm bảo đường dẫn này nằm trong biến môi trường `$PATH` để bạn có thể chạy lệnh từ bất kỳ thư mục nào.


## Điều kiện tiên quyết


Để hoạt động, `rgb-lightning-node` daemon cần có sự hiện diện và cấu hình của các thành phần sau:




- Một nút **`bitcoind`**


Mỗi phiên bản RLN sẽ cần giao tiếp với `bitcoind` để phát sóng và giám sát các giao dịch on-chain của nó. Thông tin xác thực (tên đăng nhập/mật khẩu) và URL (máy chủ/cổng) cần được cung cấp cho daemon.




- Một **thiết bị lập chỉ mục** (Electrum hoặc Esplora)


daemon phải có khả năng liệt kê và khám phá các giao dịch on-chain, đặc biệt là tìm UTXO nơi tài sản đã được neo giữ. Bạn cần chỉ định URL của máy chủ Electrum hoặc Esplora của mình.




- Một mô hình thay thế cho **RGB**


Máy chủ proxy là một thành phần (tùy chọn, nhưng rất được khuyến nghị) để đơn giản hóa việc trao đổi các *lô hàng* RGB giữa các thiết bị Lightning. Một lần nữa, cần phải chỉ định URL.


ID và URL được nhập khi daemon được *mở khóa* thông qua API.


## Khởi chạy Regtest


Để sử dụng đơn giản, có một công cụ `regtest.sh` script tự động khởi chạy, thông qua Docker, một tập hợp các dịch vụ: `bitcoind`, `electrs` (trình lập chỉ mục), `rgb-proxy-server`.


![RLN](assets/fr/03.webp)


Điều này cho phép bạn khởi chạy một môi trường cục bộ, biệt lập và được cấu hình sẵn. Nó tạo và hủy các container và thư mục dữ liệu mỗi khi khởi động lại. Chúng ta sẽ bắt đầu bằng cách khởi động :


```bash
./regtest.sh start
```


Chiếc script này sẽ:




- Tạo thư mục `docker/` để lưu trữ;
- Chạy `bitcoind` trong regtest, cũng như trình lập chỉ mục `electrs` và `rgb-proxy-server`;
- Hãy đợi cho đến khi mọi thứ đã sẵn sàng để sử dụng.


![RLN](assets/fr/04.webp)


Tiếp theo, chúng ta sẽ khởi chạy một số node RLN. Trong các cửa sổ dòng lệnh riêng biệt, hãy chạy lệnh sau, ví dụ (để khởi chạy 3 node RLN):


```bash
# 1st shell
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network regtest
# 2nd shell
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network regtest
# 3rd shell
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network regtest
```


![RLN](assets/fr/05.webp)




- Tham số `--network regtest` cho biết việc sử dụng cấu hình regtest;
- `--daemon-listening-port` chỉ ra cổng REST nào mà nút Lightning sẽ lắng nghe các cuộc gọi API (JSON);
- `--ldk-peer-listening-port` chỉ định cổng Lightning p2p nào cần lắng nghe;
- `dataldk0/`, `dataldk1/` là đường dẫn đến các thư mục lưu trữ (mỗi nút lưu trữ thông tin của nó một cách riêng biệt).


Giờ đây, bạn có thể thực thi các lệnh trên các nút RLN của mình từ trình duyệt, nhờ vào API. Đặc biệt, đây là nơi bạn có thể *mở khóa* các daemon. Chỉ cần mở trình duyệt trên cùng máy tính với các nút của bạn và nhập URL:


```url
https://rgb-tools.github.io/rgb-lightning-node/
```


Để một nút mở kênh, trước tiên nó phải có bitcoin tại địa chỉ được tạo bằng lệnh sau (ví dụ: đối với nút số 1):


```bash
curl -X POST http://localhost:3001/address
```


Câu trả lời sẽ cung cấp cho bạn một địa chỉ.


![RLN](assets/fr/06.webp)


Trên máy chủ kiểm thử `bitcoind`, chúng ta sẽ khai thác một vài bitcoin. Chạy lệnh:


```bash
./regtest.sh mine 101
```


![RLN](assets/fr/07.webp)


Hãy chuyển tiền đến địa chỉ nút được tạo ở trên:


```bash
./regtest.sh sendtoaddress <address> <amount>
```


![RLN](assets/fr/08.webp)


Sau đó, khai thác một khối để xác nhận giao dịch:


```bash
./regtest.sh mine 1
```


![RLN](assets/fr/09.webp)


## Khởi chạy Testnet (không dùng Docker)


Nếu bạn muốn kiểm tra một kịch bản thực tế hơn, bạn có thể khởi chạy các nút RLN trên Testnet thay vì trong Regtest, trỏ đến các dịch vụ công cộng hoặc các dịch vụ mà bạn kiểm soát:


```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```


Theo mặc định, nếu không tìm thấy cấu hình nào, daemon sẽ cố gắng sử dụng:




- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- `bitcoind_rpc_port`: `18332`
- `indexer_url`: `ssl://electrum.iriswallet.com:50013`
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-rpc`


Đăng nhập bằng tài khoản:




- `bitcoind_rpc_username`: `user`
- `bitcoind_rpc_username`: `password`


Bạn cũng có thể tùy chỉnh các thành phần này thông qua lệnh `init`/`unlock` API.


## Phát hành RGB token


Để phát hành token, chúng ta sẽ bắt đầu bằng cách tạo ra các UTXO "có thể tô màu":


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"up_to": false,
"num": 4,
"size": 2000000,
"fee_rate": 4.2,
"skip_sync": false
}' \
http://localhost:3001/createutxos
```


![RLN](assets/fr/10.webp)


Tất nhiên, bạn có thể điều chỉnh thứ tự. Để xác nhận giao dịch, chúng tôi khai thác một:


```bash
./regtest.sh mine 1
```


Giờ chúng ta có thể tạo một tài sản RGB. Lệnh sẽ phụ thuộc vào loại tài sản bạn muốn tạo và các tham số của nó. Ở đây tôi đang tạo một tài sản NIA (*Tài sản không bơm hơi*) token có tên "Plan ₿ Academy" với nguồn cung là 1000 đơn vị. Tham số `precision` cho phép bạn xác định khả năng chia nhỏ của các đơn vị.


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amounts": [
1000
],
"ticker": "Plan ₿ Academy",
"name": "Plan ₿ Academy",
"precision": 0
}' \
http://localhost:3001/issueassetnia
```


![RLN](assets/fr/11.webp)


Phản hồi bao gồm ID của tài sản mới được tạo. Hãy nhớ ghi lại mã định danh này. Trong trường hợp của tôi, đó là:


```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```


![RLN](assets/fr/12.webp)


Sau đó, bạn có thể chuyển nó qua on-chain hoặc phân bổ nó vào một kênh Lightning. Đó chính xác là những gì chúng ta sẽ làm trong phần tiếp theo.


## Mở kênh và chuyển giao tài sản RGB


Trước tiên, bạn phải kết nối nút của mình với một nút ngang hàng trên mạng Lightning bằng lệnh `/connectpeer`. Trong ví dụ của tôi, tôi điều khiển cả hai nút. Vì vậy, tôi sẽ lấy khóa công khai của nút Lightning thứ hai bằng lệnh này:


```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```


Lệnh này trả về khóa công khai của nút số 2 của tôi:


```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```


![RLN](assets/fr/13.webp)


Tiếp theo, chúng ta sẽ mở kênh bằng cách chỉ định tài sản liên quan (`Plan ₿ Academy`). Lệnh `/openchannel` cho phép bạn xác định kích thước của kênh theo satoshi và chọn bao gồm cả tài sản RGB. Điều này phụ thuộc vào những gì bạn muốn tạo, nhưng trong trường hợp của tôi, lệnh là:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"peer_pubkey_and_opt_addr": "031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94@localhost:9736",
"capacity_sat": 1000000,
"push_msat": 10000000,
"asset_amount": 500,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"public": true,
"with_anchors": true,
"fee_base_msat": 1000,
"fee_proportional_millionths": 0,
"temporary_channel_id": "a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5"
}' \
http://localhost:3001/openchannel
```


Tìm hiểu thêm tại đây:




- `peer_pubkey_and_opt_addr`: Mã định danh của thiết bị mà chúng ta muốn kết nối (khóa công khai mà chúng ta đã tìm thấy trước đó);
- `capacity_sat`: Tổng dung lượng kênh tính bằng satoshis;
- `push_msat`: Số lượng millisatoshi được chuyển ban đầu cho bên kia khi kênh được mở (ở đây tôi chuyển ngay 10.000 sats để anh ấy có thể thực hiện chuyển khoản RGB sau đó);
- `asset_amount`: Số lượng tài sản RGB sẽ được cam kết cho kênh;
- `asset_id`: Mã định danh duy nhất của thiết bị RGB đang tham gia kênh;
- `public`: Cho biết liệu kênh có nên được công khai để định tuyến trên mạng hay không.


![RLN](assets/fr/14.webp)


Để xác nhận giao dịch, 6 khối được khai thác:


```bash
./regtest.sh mine 6
```


![RLN](assets/fr/15.webp)


Kênh Lightning hiện đã được mở và cũng chứa 500 gói `Plan ₿ Academy` token ở phía nút số 1. Nếu nút số 2 muốn nhận `Plan ₿ Academy` token, nó phải tạo hóa đơn. Sau đây là cách thực hiện:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amt_msat": 3000000,
"expiry_sec": 420,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"asset_amount": 100
}' \
http://localhost:3002/lninvoice
```


Với :




- `amt_msat`: Lượng Invoice tính bằng millisatoshi (tối thiểu 3000 sats);
- `expiry_sec` : Thời gian hết hạn của Invoice tính bằng giây ;
- `asset_id`: Mã định danh của tài sản RGB liên kết với hóa đơn;
- `asset_amount`: Số lượng tài sản RGB cần chuyển giao kèm theo hóa đơn này.


Đáp lại, bạn sẽ nhận được hóa đơn RGB:


```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```


![RLN](assets/fr/16.webp)


Chúng tôi sẽ thanh toán hóa đơn này từ nút đầu tiên, nơi nắm giữ số tiền mặt cần thiết cùng với Plan ₿ Academy và token:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```


![RLN](assets/fr/17.webp)


Giao dịch thanh toán đã được thực hiện. Bạn có thể xác minh điều này bằng cách chạy lệnh:


```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```


![RLN](assets/fr/18.webp)


Dưới đây là cách triển khai một nút Lightning được sửa đổi để mang theo các tài sản RGB. Bản trình diễn này dựa trên:




- Môi trường regtest (thông qua `./regtest.sh`) hoặc testnet;
- Một nút Lightning (`rgb-lightning-node`) dựa trên `bitcoind`, một bộ lập chỉ mục và một `rgb-proxy-server`;
- Một loạt các thiết bị JSON REST API dùng để mở/đóng kênh, phát hành token, chuyển giao tài sản qua Lightning, v.v.


Nhờ vào quy trình này:




- Các giao dịch tham gia chớp nhoáng bao gồm một đầu ra bổ sung (OP_RETURN hoặc Taproot) với việc neo giữ quá trình chuyển đổi RGB;
- Việc chuyển tiền được thực hiện hoàn toàn giống như các khoản thanh toán Lightning truyền thống, nhưng có thêm RGB token;
- Nhiều nút RLN có thể được liên kết để định tuyến và thử nghiệm thanh toán giữa nhiều nút, miễn là có đủ thanh khoản cả về bitcoin và tài sản RGB trên đường dẫn.


Nếu bạn thấy hướng dẫn này hữu ích, tôi sẽ rất biết ơn nếu bạn nhấn nút thích bên dưới. Vui lòng chia sẻ bài viết này trên mạng xã hội của bạn. Cảm ơn rất nhiều!


Tôi cũng khuyên bạn nên xem hướng dẫn khác này, trong đó tôi giải thích cách sử dụng công cụ RGB CLI do hiệp hội LNP/BP phát triển để tạo hợp đồng RGB:


https://planb.academy/tutorials/node/others/rgb-cli-1f8a28d4-fa99-4261-9d80-48275b496fd4