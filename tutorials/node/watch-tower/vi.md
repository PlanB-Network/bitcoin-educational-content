---
name: Lightning Watchtower
description: Hiểu và sử dụng Watchtower trên nút Lightning của bạn
---
![cover](assets/cover.webp)



## Tháp canh hoạt động như thế nào?



Là một phần thiết yếu của hệ sinh thái Lightning Network, _Watchtower_ cung cấp mức độ bảo vệ bổ sung cho các kênh Lightning của người dùng. Vai trò chính của chúng là giám sát trạng thái kênh và can thiệp nếu một bên kênh cố gắng lừa đảo bên kia.



Làm thế nào Watchtower có thể xác định một kênh đã bị xâm phạm? Nó nhận được từ khách hàng (một trong các bên tham gia kênh) thông tin cần thiết để xác định và xử lý chính xác bất kỳ vi phạm nào. Thông tin này bao gồm chi tiết về giao dịch gần đây nhất, trạng thái hiện tại của kênh và Elements cần thiết để tạo giao dịch phạt. Trước khi truyền dữ liệu này đến Watchtower, khách hàng có thể mã hóa dữ liệu để bảo mật. Vì vậy, ngay cả khi Watchtower nhận được dữ liệu, nó sẽ không thể giải mã cho đến khi vi phạm thực sự xảy ra. Cơ chế mã hóa này bảo vệ quyền riêng tư của khách hàng và ngăn Watchtower truy cập trái phép vào thông tin nhạy cảm.



Trong hướng dẫn này, chúng ta sẽ xem xét 3 cách sử dụng **Watchtower**:




- đầu tiên, phương pháp thô cổ điển thông qua LND,
- sau đó một cách tiếp cận khác với Mắt Satoshi,
- và cuối cùng là cấu hình đơn giản hóa của Watchtower trên nút Lightning của bạn được lưu trữ bằng Umbrel.



## 1 - Cấu hình Watchtower hoặc máy khách thông qua LND



*Hướng dẫn này được trích từ [tài liệu chính thức của LND](https://github.com/lightningnetwork/LND/blob/master/docs/Watchtower.md). Một số thay đổi có thể đã được thực hiện đối với phiên bản gốc



Kể từ phiên bản v0.7.0, `LND` hỗ trợ việc thực thi Watchtower vị tha riêng tư như một hệ thống con tích hợp đầy đủ của `LND`. Tháp canh cung cấp tuyến phòng thủ thứ hai chống lại các tình huống vi phạm cố ý hoặc vô tình khi nút khách hàng ngoại tuyến hoặc không thể phản hồi tại thời điểm vi phạm, mang lại mức độ bảo mật cao hơn cho quỹ kênh.



Không giống như _tháp canh thưởng_, vốn yêu cầu một phần quỹ của kênh để đổi lấy dịch vụ của mình, _tháp canh vị tha_ sẽ hoàn trả toàn bộ quỹ của nạn nhân (trừ phí On-Chain) mà không tính hoa hồng. Tháp canh thưởng sẽ được kích hoạt trong phiên bản sau; chúng vẫn đang trong giai đoạn thử nghiệm và cải tiến.



Ngoài ra, `LND` giờ đây có thể được cấu hình để hoạt động như một _máy khách tháp canh_, lưu trữ các giao dịch khắc phục vi phạm được mã hóa (còn gọi là "giao dịch công lý") từ các tháp canh khác. Watchtower lưu trữ các khối dữ liệu được mã hóa có kích thước cố định và chỉ có thể giải mã và công bố giao dịch công lý sau khi bên vi phạm đã phát đi trạng thái Commitment đã bị thu hồi. Giao tiếp giữa khách hàng ↔ Watchtower được mã hóa và xác thực bằng cặp khóa tạm thời, điều này hạn chế khả năng theo dõi khách hàng của Watchtower thông qua thông tin xác thực dài hạn.



Xin lưu ý rằng chúng tôi đã quyết định triển khai trong phiên bản này một bộ tính năng giới hạn vốn đã cung cấp khả năng bảo mật đáng kể cho người dùng `LND`. Nhiều tính năng khác liên quan đến Watchtower đã gần hoàn thiện hoặc đang trong giai đoạn phát triển; chúng tôi sẽ tiếp tục cung cấp chúng khi chúng tôi kiểm tra và ngay khi chúng được xác định là an toàn.



lưu ý: hiện tại, các tháp canh chỉ lưu đầu ra `to_local` và `to_remote` của các cam kết đã thu hồi; việc lưu đầu ra HTLC sẽ được triển khai trong phiên bản tương lai, vì giao thức có thể được mở rộng để bao gồm dữ liệu chữ ký bổ sung trong các blob được mã hóa._



### Cấu hình Watchtower



Để thiết lập Watchtower, người dùng dòng lệnh cần biên dịch máy chủ phụ `watchtowerrpc` tùy chọn, cho phép tương tác với Watchtower thông qua gRPC hoặc `lncli`. Các tệp nhị phân đã xuất bản mặc định bao gồm máy chủ phụ `watchtowerrpc`.



Cấu hình tối thiểu để kích hoạt Watchtower là `Watchtower.active=1`.



Bạn có thể lấy thông tin cấu hình Watchtower của mình bằng `lncli tower info`:



```shell
$  lncli tower info
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"listeners": [
"[::]:9911"
],
"uris": [
],
}
```



Bộ tùy chọn cấu hình Watchtower đầy đủ có sẵn thông qua `LND -h`:



```shell
$  lnd -h
...
watchtower:
--watchtower.active                                     If the watchtower should be active or not
--watchtower.towerdir=                                  Directory of the watchtower.db (default: $HOME/.lnd/data/watchtower)
--watchtower.listen=                                    Add interfaces/ports to listen for peer connections
--watchtower.externalip=                                Add interfaces/ports where the watchtower can accept peer connections
--watchtower.readtimeout=                               Duration the watchtower server will wait for messages to be received before hanging up on client connections
--watchtower.writetimeout=                              Duration the watchtower server will wait for messages to be written before hanging up on client connections
...
```



#### Giao diện nghe



Theo mặc định, Watchtower lắng nghe trên `:9911`, tương ứng với cổng `9911` trên tất cả các giao diện khả dụng. Người dùng có thể tự định nghĩa giao diện lắng nghe của mình thông qua tùy chọn `--Watchtower.listen=`. Bạn có thể kiểm tra cấu hình của mình trong trường `"listeners"` của `lncli tower info`. Nếu bạn gặp sự cố khi kết nối với Watchtower, hãy đảm bảo rằng `<port>` đang mở hoặc proxy của bạn được cấu hình chính xác cho Interface đang hoạt động.



#### Địa chỉ IP bên ngoài



Người dùng cũng có thể chỉ định IP bên ngoài Watchtower Address(es) bằng `Watchtower.externalip=`, lệnh này sẽ hiển thị toàn bộ URI (pubkey@host:port) của Watchtower thông qua RPC hoặc `lncli tower info`:



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911"
]
```



URI Watchtower có thể được truyền đạt tới khách hàng để kết nối và sử dụng bằng lệnh sau:



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



Nếu khách hàng Watchtower cần truy cập từ xa, hãy đảm bảo:




- Mở cổng 9911 (hoặc cổng được xác định thông qua `Watchtower.listen`).
- Sử dụng proxy để chuyển hướng lưu lượng từ cổng mở đến Address đang lắng nghe Watchtower.



#### Dịch vụ ẩn Tor



Watchwers hỗ trợ các dịch vụ ẩn Tor và có thể tự động generate khi khởi động với các tùy chọn sau:



```shell
$  lnd --tor.active --tor.v3 --watchtower.active
```



.onion Address sau đó xuất hiện trong trường `"uris"` trong truy vấn `lncli tower info`:



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@bn2kxggzjysvsd5o3uqe4h7655u7v2ydhxzy7ea2fx26duaixlwuguad.onion:9911"
]
```



Lưu ý: Khóa công khai Watchtower khác với khóa công khai của nút `LND`. Hiện tại, nó hoạt động như một "danh sách trắng Soft", vì khách hàng cần biết khóa công khai của Watchtower để sử dụng làm bản sao lưu, trong khi chờ các cơ chế danh sách trắng tiên tiến hơn. Chúng tôi khuyến nghị KHÔNG tiết lộ khóa công khai này, trừ khi bạn sẵn sàng để lộ Watchtower của mình cho toàn bộ Internet.



#### Thư mục cơ sở dữ liệu Watchtower



Cơ sở dữ liệu Watchtower có thể được di chuyển bằng tùy chọn `Watchtower.towerdir=`. Lưu ý rằng hậu tố `/Bitcoin/Mainnet/Watchtower.db` sẽ được thêm vào đường dẫn đã chọn để phân tách cơ sở dữ liệu theo chuỗi. Do đó, việc thiết lập `Watchtower.towerdir=/path/to/towerdir` sẽ tạo ra một cơ sở dữ liệu tại `/path/to/towerdir/Bitcoin/Mainnet/Watchtower.db`.



Ví dụ, trên Linux, cơ sở dữ liệu mặc định của Watchtower nằm tại:


`/home/$USER/.LND/dữ liệu/Watchtower/Bitcoin/Mainnet/Watchtower.db`



### Cấu hình máy khách Watchtower



Để cấu hình máy khách Watchtower, bạn cần hai mục:





- Kích hoạt máy khách Watchtower bằng tùy chọn `--wtclient.active`.



```shell
$  lnd --wtclient.active
```





- URI của Watchtower đang hoạt động.



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



Bạn có thể cấu hình nhiều tháp canh theo cách này.



#### Mức phí cho các giao dịch pháp lý



Người dùng có thể tùy chọn đặt mức phí cho các giao dịch tư pháp thông qua tùy chọn `wtclient.sweep-fee-rate`, chấp nhận giá trị theo sat/byte. Giá trị mặc định là 10 sat/byte, nhưng có thể đặt mức phí cao hơn để đạt được mức ưu tiên cao hơn trong thời gian phí cao điểm. Việc thay đổi `sweep-fee-rate` áp dụng cho tất cả các bản cập nhật mới sau khi daemon khởi động lại.



#### Giám sát



Với lệnh `lncli wtclient`, người dùng hiện có thể tương tác trực tiếp với máy khách Watchtower để lấy hoặc sửa đổi thông tin về tất cả các tháp canh đã đăng ký.



Ví dụ, với `lncli wtclient tower`, bạn có thể tìm ra số lượng phiên hiện đang được thương lượng với Watchtower được thêm vào ở trên và xác định xem phiên đó có được sử dụng để sao lưu hay không nhờ vào trường `active_session_candidate`.



```shell
$  lncli wtclient tower 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": []
}
```



Để có thông tin về phiên Watchtower, hãy sử dụng tùy chọn `--include_sessions`.



```shell
$  lncli wtclient tower --include_sessions 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": [
{
"num_backups": 0,
"num_pending_backups": 0,
"max_backups": 1024,
"sweep_sat_per_vbyte": 10
}
]
}
```



Tất cả các tùy chọn cấu hình máy khách Watchtower đều có sẵn thông qua `lncli wtclient -h`:



```shell
$  lncli wtclient -h
NAME:
lncli wtclient - Interact with the watchtower client.

USAGE:
lncli wtclient command [command options] [arguments...]

COMMANDS:
add     Register a watchtower to use for future sessions/backups.
remove  Remove a watchtower to prevent its use for future sessions/backups.
towers  Display information about all registered watchtowers.
tower   Display information about a specific registered watchtower.
stats   Display the session stats of the watchtower client.
policy  Display the active watchtower client policy configuration.

OPTIONS:
--help, -h  show help
```




## 2 - Tự lắp đặt Eye of Satoshi



*Bài hướng dẫn này được trích một phần từ bài viết trên [Blog Mùa hè Bitcoin](https://blog.summerofbitcoin.org/). Phiên bản gốc đã được chỉnh sửa*



Eye of Satoshi ([Rust-TEOS](https://github.com/talaia-labs/Rust-teos)) là một Watchtower Lightning không lưu trữ, tuân thủ [Bolt 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org). Nó bao gồm hai thành phần chính:





- teos**: bao gồm Interface (CLI) dòng lệnh và các tính năng máy chủ thiết yếu của Watchtower. Hai tệp nhị phân - **teosd** và **teos-CLI** - được tạo ra khi _crate_ này được biên dịch.





- teos-common**: bao gồm chức năng chia sẻ ở phía máy chủ và phía máy khách (hữu ích khi tạo máy khách).



Để chạy Watchtower đúng cách, bạn cần chạy **bitcoind** trước khi khởi chạy Watchtower bằng lệnh **teosd**. Trước khi chạy hai lệnh này, bạn cần cấu hình tệp **Bitcoin.conf**. Sau đây là cách thực hiện:





- Cài đặt Bitcoin core từ nguồn hoặc tải xuống. Sau khi tải xuống, hãy đặt tệp **Bitcoin.conf** vào thư mục người dùng Bitcoin core. Xem liên kết này để biết thêm thông tin về vị trí đặt tệp, vì điều này phụ thuộc vào hệ điều hành được sử dụng.





- Sau khi xác định được vị trí, hãy thêm các tùy chọn sau:



```shell
# RPC
server=1
rpcuser=<your-user>
rpcpassword=<your-password>

# chaîne
regtest=1
```





- máy chủ**: dành cho các yêu cầu RPC





- rpcuser** và **rpcpassword**: xác thực máy khách RPC với máy chủ





- regtest**: không bắt buộc, nhưng hữu ích nếu bạn đang lập kế hoạch phát triển.



Giá trị cho **rpcuser** và **rpcpassword** do bạn tự chọn. Chúng phải được viết không có dấu ngoặc kép. Ví dụ:



```shell
rpcuser=aniketh
rpcpassword=strongpassword
```



Bây giờ, nếu bạn chạy **bitcoind**, nút sẽ bắt đầu.





- Đối với phần Watchtower, trước tiên bạn phải cài đặt **teos** từ nguồn. Làm theo hướng dẫn trong liên kết này.





- Sau khi cài đặt thành công **teos** trên hệ thống và chạy thử nghiệm, bạn có thể chuyển sang bước cuối cùng: thiết lập tệp **teos.toml** trong thư mục người dùng teos. Tệp này nên được đặt trong thư mục có tên **.teos** (lưu ý dấu chấm) trong thư mục home của bạn. Ví dụ: **/home//.teos** trên Linux. Sau khi tìm thấy vị trí, hãy tạo tệp **teos.toml** và thiết lập các tùy chọn sau phù hợp với các thay đổi đã thực hiện trên **bitcoind**:



```shell
# bitcoind
btc_network = "regtest"
btc_rpc_user = <your-user>
btc_rpc_password = <your-password>
```



Lưu ý rằng ở đây, tên người dùng và mật khẩu phải được viết **trong dấu ngoặc kép**. Sử dụng ví dụ trước:



```shell
btc_rpc_user = "aniketh"
btc_rpc_password = "strongpassword"
```



Sau khi hoàn tất các bước này, bạn đã sẵn sàng khởi chạy Watchtower. Vì chúng ta đang chạy trên **regtest**, nên có khả năng không có khối nào được khai thác trên mạng thử nghiệm Bitcoin khi Watchtower kết nối lần đầu (nếu có, chắc chắn có vấn đề). Watchtower xây dựng bộ nhớ đệm nội bộ cho 100 khối cuối cùng của **bitcoind**; vì vậy, khi khởi chạy lần đầu, bạn có thể gặp lỗi sau:



```shell
ERROR [teosd] Not enough blocks to start the tower (required: 100). Mine at least 100 more
```



Vì chúng ta đang sử dụng **regtest**, chúng ta có thể chặn Miner bằng cách phát lệnh RPC, mà không cần phải chờ độ trễ trung bình 10 phút như trên các mạng khác (chẳng hạn như Mainnet hoặc Testnet). Xem phần trợ giúp **bitcoin-cli** để biết chi tiết về cách chặn Miner.



![Image](assets/fr/01.webp)



Vậy là xong: bạn đã chạy thành công Watchtower. Xin chúc mừng. 🎉




## 3 - Cấu hình Watchtower trên Umbrel



Trên Umbrel, việc kết nối với Watchtower để bảo vệ nút Lightning của bạn cực kỳ đơn giản, vì mọi thứ đều được thực hiện thông qua giao diện đồ họa Interface. Sau khi kết nối từ xa với nút, hãy mở ứng dụng "**Lightning Node**".



![Image](assets/fr/02.webp)



Nhấp vào ba dấu chấm nhỏ ở góc trên bên phải của Interface, sau đó chọn "**Cài đặt nâng cao**".



![Image](assets/fr/03.webp)



Trong menu "**Watchtower**", có hai tùy chọn:





- Dịch vụ Watchtower**: Tùy chọn này cho phép bạn vận hành Watchtower, tức là một dịch vụ giám sát kênh của các nút khác để phát hiện bất kỳ hành vi gian lận nào. Trong trường hợp bị vi phạm, Watchtower của bạn sẽ xuất bản một giao dịch trên Blockchain, cho phép người dùng khôi phục số tiền bị khóa. Sau khi được kích hoạt, URI của Watchtower sẽ xuất hiện và có thể được truyền đến các nút khác để họ có thể thêm nó vào máy khách Watchtower của mình;





- Máy khách Watchtower**: tùy chọn này cho phép bạn kết nối với các tháp canh bên ngoài để bảo vệ kênh của mình. Sau khi được kích hoạt, bạn có thể thêm các dịch vụ Watchtower mà nút của bạn sẽ truyền thông tin cần thiết về các kênh của nó. Các tháp canh này sau đó sẽ theo dõi trạng thái của chúng và can thiệp trong trường hợp có hành vi gian lận.



Tất nhiên, ưu tiên hàng đầu của bạn là kích hoạt *Watchtower Client* để bảo vệ nút của bạn, nhưng tôi cũng khuyên bạn nên kích hoạt *Watchtower Service* để góp phần bảo mật cho những người dùng khác.



![Image](assets/fr/04.webp)



Sau đó nhấp vào nút "**Lưu và Khởi động lại Node**" của Green. LND của bạn sẽ khởi động lại.



Trong cùng menu, bạn cũng sẽ tìm thấy URI của dịch vụ Watchtower nếu đã kích hoạt. Bạn cũng có thể thêm URI của Watchtower bên ngoài để bảo vệ kênh của mình. Nhấp vào "**THÊM**" để xác nhận.



![Image](assets/fr/05.webp)



Có một số Tháp Canh có sẵn trực tuyến. Ví dụ, [LN+ và Voltage cung cấp Watchtower](https://lightningnetwork.plus/Watchtower) mà bạn có thể kết nối:



```
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



![Image](assets/fr/06.webp)



Một lựa chọn khác là Exchange URI Watchtower của bạn với những người dùng bitcoin khác để mỗi bên bảo vệ nút của bên kia.



Tôi cũng khuyên bạn nên thiết lập một số Tháp canh để giảm thiểu rủi ro trong trường hợp một trong số chúng không hoạt động.



Cuối cùng, bạn có thể điều chỉnh tham số "**Mức Phí Quét Khách Hàng Watchtower**". Tham số này xác định mức phí tối đa bạn sẵn sàng trả cho một giao dịch phạt phát sóng Watchtower được đưa vào một khối. Hãy đảm bảo bạn đặt một giá trị đủ cao, phù hợp với số tiền bị khóa trong các kênh của bạn.