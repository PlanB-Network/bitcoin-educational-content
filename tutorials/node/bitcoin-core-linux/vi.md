---
name: Bitcoin Core (Linux)
description: Chạy nút của riêng bạn với Bitcoin core trên Linux
---

![cover](assets/cover.webp)


## Chạy nút của riêng bạn với Bitcoin core


Giới thiệu về Bitcoin và khái niệm về nút, kèm theo hướng dẫn cài đặt toàn diện trên Linux.


Một trong những khía cạnh thú vị nhất của Bitcoin là khả năng tự chạy chương trình và do đó có thể tham gia ở cấp độ chi tiết trong mạng lưới và xác minh giao dịch công khai Ledger.


Bitcoin, là một dự án mã nguồn mở, đã được cung cấp miễn phí và phân phối công khai từ năm 2009. Gần 17 năm sau khi ra đời, Bitcoin hiện là một mạng lưới tiền tệ kỹ thuật số mạnh mẽ và không thể ngăn cản, được hưởng lợi từ hiệu ứng mạng lưới hữu cơ mạnh mẽ. Với những nỗ lực và tầm nhìn của họ, Satoshi Nakamoto xứng đáng được chúng ta ghi nhận. Nhân tiện, chúng tôi đăng tải sách trắng Bitcoin tại đây trên Agora 256 (lưu ý: cũng trên trường đại học).


### Trở thành ngân hàng của chính bạn


Việc vận hành node riêng đã trở nên thiết yếu đối với những người tuân thủ nguyên tắc Bitcoin. Không cần xin phép bất kỳ ai, bạn có thể tải xuống Blockchain ngay từ đầu và xác minh tất cả các giao dịch từ A đến Z theo giao thức Bitcoin.


Chương trình cũng bao gồm Wallet riêng. Nhờ đó, chúng tôi kiểm soát được các giao dịch gửi đến phần còn lại của mạng lưới mà không cần bất kỳ trung gian hay bên thứ ba nào. Bạn chính là ngân hàng của mình.


Phần còn lại của bài viết này là hướng dẫn cài đặt Bitcoin core — phiên bản phần mềm Bitcoin được sử dụng rộng rãi nhất — đặc biệt trên các bản phân phối Linux tương thích với Debian như Ubuntu và Pop!OS. Hãy làm theo hướng dẫn này để tiến gần hơn đến chủ quyền cá nhân của bạn.


## Hướng dẫn cài đặt Bitcoin core cho Debian/Ubuntu


**Điều kiện tiên quyết**


- Dung lượng lưu trữ dữ liệu tối thiểu 6GB (nút pruned) — Dung lượng lưu trữ dữ liệu 1TB (Full node)
- Dự kiến quá trình *Tải xuống Khối Ban đầu* (IBD) sẽ mất ít nhất 24 giờ. Thao tác này là bắt buộc ngay cả đối với nút pruned.
- Cho phép ~600GB băng thông cho IBD, ngay cả đối với một nút pruned.


**Lưu ý: 💡** các lệnh sau được xác định trước cho Bitcoin core phiên bản 24.1.


### Tải xuống và xác minh tệp



- [Tải xuống](https://bitcoincore.org/en/download/) `Bitcoin-24.1-x86_64-linux-gnu.tar.gz`, cũng như các tệp `SHA256SUMS` và `SHA256SUMS.asc` (rõ ràng là bạn cần tải xuống phiên bản phần mềm mới nhất).



- Mở terminal trong thư mục chứa các tệp đã tải xuống. Ví dụ: `cd ~/Downloads/`.



- Xác minh rằng tổng kiểm tra của tệp phiên bản được liệt kê trong tệp tổng kiểm tra bằng lệnh `sha256sum --ignore-missing --check SHA256SUMS`.



- Đầu ra của lệnh này phải bao gồm tên tệp phiên bản đã tải xuống, theo sau là `OK`. Ví dụ: `Bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: OK`.



- Cài đặt git bằng lệnh `sudo apt install git`. Sau đó, sao chép kho lưu trữ chứa khóa PGP của người ký Bitcoin core bằng lệnh `git clone https://github.com/Bitcoin-core/guix.sigs`.



- Nhập khóa PGP của tất cả người ký bằng lệnh `gpg --import guix.sigs/builder-keys/*`



- Xác minh rằng tệp tổng kiểm tra được ký bằng khóa PGP của người ký bằng lệnh `gpg --verify SHA256SUMS.asc`.



Mỗi chữ ký hợp lệ sẽ hiển thị một dòng bắt đầu bằng: `gpg: Good signature` và một dòng khác kết thúc bằng: `Dấu vân tay khóa chính: 133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320` (ví dụ về dấu vân tay khóa PGP của Pieter Wuille).


**Lưu ý💡:** không nhất thiết tất cả khóa chữ ký đều phải trả về "OK". Thực tế, có thể chỉ cần một khóa. Người dùng tự xác định ngưỡng xác thực của mình để xác minh PGP.


Bạn có thể bỏ qua các cảnh báo:



- `Khóa này không được chứng nhận bằng chữ ký đáng tin cậy!`



- `Không có dấu hiệu nào cho thấy chữ ký đó thuộc về chủ sở hữu.`


### Cài đặt đồ họa Bitcoin core Interface



- Trong terminal, vẫn trong thư mục chứa tệp phiên bản Bitcoin core, hãy sử dụng lệnh `tar xzf Bitcoin-24.1-x86_64-linux-gnu.tar.gz` để giải nén các tệp có trong kho lưu trữ.



- Cài đặt các tệp đã giải nén trước đó bằng lệnh `sudo install -m 0755 -o root -g root -t /usr/local/bin Bitcoin-24.1/bin/*`



- Cài đặt các phụ thuộc cần thiết bằng lệnh `sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev`



- Khởi động _bitcoin-qt_ (Bitcoin core đồ họa Interface) bằng lệnh `Bitcoin-qt`.



- Để chọn một nút pruned, hãy kiểm tra _Giới hạn lưu trữ Blockchain_ và cấu hình giới hạn dữ liệu sẽ được lưu trữ:


![welcome](assets/fr/02.webp)


### Kết luận Phần 1: Hướng dẫn cài đặt


Sau khi Bitcoin core được cài đặt, bạn nên duy trì hoạt động của nó càng lâu càng tốt để đóng góp cho mạng Bitcoin bằng cách xác minh các giao dịch và truyền các khối mới cho các đối tác khác.


Tuy nhiên, việc chạy và đồng bộ hóa nút của bạn theo từng đợt, ngay cả khi chỉ để xác thực các giao dịch đã nhận và đã gửi, vẫn là một biện pháp tốt.


![Creation wallet](assets/fr/03.webp)


## Cấu hình Tor cho nút Bitcoin core


**Lưu ý💡:** hướng dẫn này được thiết kế cho Bitcoin core 24.0.1 trên các bản phân phối Linux tương thích với Ubuntu/Debian.


### Cài đặt và cấu hình Tor cho Bitcoin core


Trước tiên, chúng ta cần cài đặt dịch vụ Tor (The Onion Router), một mạng lưới được sử dụng cho giao tiếp ẩn danh, cho phép chúng ta ẩn danh các tương tác với mạng Bitcoin. Để biết thêm thông tin về các công cụ bảo vệ quyền riêng tư trực tuyến, bao gồm Tor, vui lòng tham khảo bài viết của chúng tôi về chủ đề này.


Để cài đặt Tor, hãy mở terminal và nhập lệnh `sudo apt -y install tor`. Sau khi cài đặt hoàn tất, dịch vụ thường sẽ tự động chạy nền. Kiểm tra xem dịch vụ có đang chạy đúng cách không bằng lệnh `sudo systemctl status tor`. Phản hồi sẽ hiển thị `Active: active (exited)`. Nhấn `Ctrl+C` để thoát khỏi chức năng này.


**Mẹo:** trong mọi trường hợp, bạn có thể sử dụng các lệnh sau trong terminal để khởi động, dừng hoặc khởi động lại Tor:


```shell
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```


Tiếp theo, hãy khởi chạy Bitcoin core (Interface) đồ họa bằng lệnh `Bitcoin-qt`. Sau đó, bật tính năng tự động định tuyến kết nối của phần mềm thông qua proxy Tor: _Cài đặt > Mạng_, và từ đó chọn _Kết nối qua proxy SOCKS5 (proxy mặc định)_ cũng như _Sử dụng proxy SOCKS5 riêng để kết nối với các máy ngang hàng thông qua dịch vụ Tor onion_.


![option](assets/fr/04.webp)


Bitcoin core tự động phát hiện xem Tor có được cài đặt hay không và nếu có, theo mặc định sẽ tạo các kết nối đi đến các nút khác cũng sử dụng Tor, ngoài các kết nối đến các nút sử dụng mạng IPv4/IPv6 (clearnet).


**Lưu ý💡:** để thay đổi ngôn ngữ hiển thị sang tiếng Pháp, hãy vào tab Hiển thị trong Cài đặt.


### Cấu hình Tor nâng cao (tùy chọn)


Có thể cấu hình Bitcoin core để chỉ sử dụng mạng Tor để kết nối với các máy ngang hàng, do đó tối ưu hóa tính ẩn danh của chúng ta thông qua nút. Vì Interface đồ họa không có chức năng tích hợp cho việc này, chúng ta sẽ cần tạo thủ công một tệp cấu hình. Vào Cài đặt, sau đó chọn Tùy chọn.


![option 2](assets/fr/05.webp)


Tại đây, nhấp vào _Mở tệp cấu hình_. Khi đã vào tệp văn bản `Bitcoin.conf`, chỉ cần thêm dòng `onlynet=onion` và lưu tệp. Bạn cần khởi động lại Bitcoin core để lệnh này có hiệu lực.


Sau đó, chúng tôi sẽ cấu hình dịch vụ Tor để Bitcoin core có thể nhận các kết nối đến thông qua proxy, cho phép các nút khác trên mạng sử dụng nút của chúng tôi để tải xuống dữ liệu Blockchain mà không làm ảnh hưởng đến tính bảo mật của máy.


Trong terminal, nhập `sudo nano /etc/tor/torrc` để truy cập tệp cấu hình dịch vụ Tor. Trong tệp này, hãy tìm dòng `#ControlPort 9051` và xóa dấu `#` để bật nó. Bây giờ, hãy thêm hai dòng mới vào tệp:


```
HiddenServiceDir /var/lib/tor/bitcoin-service/
HiddenServicePort 8333 127.0.0.1:8334
```


Để thoát khỏi tệp khi đang lưu, hãy nhấn `Ctrl+X > Y > Enter`. Quay lại terminal, khởi động lại Tor bằng cách nhập lệnh `sudo systemctl restart tor`.


Với cấu hình này, Bitcoin core sẽ chỉ có thể thiết lập kết nối đến và đi với các nút khác trên mạng thông qua mạng Tor (Onion). Để xác nhận, hãy nhấp vào tab _Window_, sau đó nhấp vào _Peers_.


![Nodes Window](assets/fr/06.webp)


### Tài nguyên bổ sung


Cuối cùng, việc chỉ sử dụng mạng Tor (`onlynet=onion`) có thể khiến bạn dễ bị tấn công bởi Sybil Attack. Đó là lý do tại sao một số người khuyên nên duy trì cấu hình đa mạng để giảm thiểu loại rủi ro này. Hơn nữa, tất cả các kết nối IPv4/IPv6 sẽ được định tuyến qua proxy Tor sau khi được cấu hình, như đã đề cập trước đó.


Ngoài ra, để duy trì kết nối hoàn toàn trên mạng Tor và giảm thiểu rủi ro gặp lỗi Sybil Attack, bạn có thể thêm Address của một nút tin cậy khác vào tệp `Bitcoin.conf` bằng cách thêm dòng `addnode=trusted_address.onion`. Bạn có thể thêm dòng này nhiều lần nếu muốn kết nối với nhiều nút tin cậy.


Để xem nhật ký của nút Bitcoin liên quan cụ thể đến tương tác của nó với Tor, hãy thêm `debug=tor` vào tệp `Bitcoin.conf`. Bây giờ bạn sẽ có thông tin Tor liên quan trong nhật ký gỡ lỗi, có thể xem trong cửa sổ _Thông tin_ bằng nút _Tệp Gỡ lỗi_. Bạn cũng có thể xem các nhật ký này trực tiếp trong terminal bằng lệnh `bitcoind -debug=tor`.


**Mẹo💡:** đây là một số liên kết thú vị:


- [Trang Wiki giải thích về Tor và mối quan hệ của nó với Bitcoin](https://en.Bitcoin.it/wiki/Tor)
- [Trình tạo tệp cấu hình Bitcoin core của Jameson Lopp](https://jlopp.github.io/Bitcoin-core-config-generator/)
- [Hướng dẫn cấu hình Tor của Jon Atack](https://github.com/Bitcoin/Bitcoin/blob/master/doc/tor.md)


Như thường lệ, nếu bạn có bất kỳ thắc mắc nào, hãy thoải mái chia sẻ với cộng đồng Agora256. Chúng ta cùng nhau học hỏi để ngày mai tốt hơn hôm nay!