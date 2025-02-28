---
name: Bitcoin Core Node (linux)
description: Tự chạy node của bạn với Bitcoin Core
---

![cover](assets/cover.webp)

# Tự chạy node của bạn với Bitcoin Core

Giới thiệu về Bitcoin và khái niệm về node, bổ sung bằng hướng dẫn cài đặt toàn diện trên Linux.

Một trong những đề xuất thú vị nhất của Bitcoin là khả năng tự chạy chương trình, và do đó tham gia ở cấp độ chi tiết trong mạng lưới và việc xác minh sổ cái giao dịch công cộng.

Bitcoin, một dự án mã nguồn mở, đã được phân phối công khai và miễn phí từ năm 2009. Gần 15 năm sau khi ra đời, Bitcoin giờ đây là một mạng tiền tệ số mạnh mẽ và không thể ngăn cản, hưởng lợi từ một hiệu ứng mạng tự nhiên mạnh mẽ. Vì những nỗ lực và tầm nhìn của mình, Satoshi Nakamoto xứng đáng nhận được lòng biết ơn của chúng ta. Nhân tiện, chúng tôi lưu trữ bản whitepaper của Bitcoin tại đây trên Agora 256 (lưu ý: cũng trên trường đại học).

## Trở thành ngân hàng của chính bạn

Việc tự chạy node của mình đã trở nên thiết yếu đối với những người tuân theo nguyên tắc của Bitcoin. Không cần phải xin phép ai, bạn có thể tải xuống blockchain từ đầu và do đó xác minh tất cả các giao dịch từ A đến Z theo giao thức Bitcoin.

Chương trình cũng bao gồm ví của riêng nó. Như vậy, chúng ta có quyền kiểm soát các giao dịch mà chúng ta gửi đến phần còn lại của mạng, không qua bất kỳ trung gian hay bên thứ ba nào. Bạn là ngân hàng của chính mình.

Phần còn lại của bài viết này do đó là hướng dẫn cài đặt Bitcoin Core — phiên bản phần mềm Bitcoin được sử dụng rộng rãi nhất — cụ thể trên các bản phân phối Linux tương thích với Debian như Ubuntu và Pop!_OS. Hãy theo dõi hướng dẫn này để tiến gần hơn đến chủ quyền cá nhân của bạn.

## Hướng dẫn Cài đặt Bitcoin Core cho Debian/Ubuntu

> Yêu cầu trước
>
> - Tối thiểu 6GB dung lượng lưu trữ (node đã cắt tỉa) — 1TB dung lượng lưu trữ (node đầy đủ)
> - Dành ít nhất 24 giờ để hoàn thành Việc Tải xuống Khối Ban đầu (IBD). Hoạt động này là bắt buộc ngay cả đối với node đã cắt tỉa.
> - Dành ~600GB băng thông cho IBD, ngay cả đối với node đã cắt tỉa.

> 💡 Các lệnh sau đây được định nghĩa trước cho phiên bản Bitcoin Core 24.1.

## Tải xuống và Xác minh Tệp

1. Tải xuống bitcoin-24.1-x86_64-linux-gnu.tar.gz, cũng như các tệp SHA256SUMS và SHA256SUMS.asc. (https://bitcoincore.org/bin/bitcoin-core-24.1/bitcoin-24.1-x86_64-linux-gnu.tar.gz)

2. Mở một terminal trong thư mục nơi các tệp đã tải xuống được đặt. Ví dụ, cd ~/Downloads/.
3. Xác minh rằng checksum của tệp phiên bản được liệt kê trong tệp checksum sử dụng lệnh sha256sum --ignore-missing --check SHA256SUMS.
4. Đầu ra của lệnh này nên bao gồm tên của tệp phiên bản đã tải xuống theo sau là "OK". Ví dụ: bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: OK.

5. Cài đặt git sử dụng lệnh sudo install git. Sau đó, clone kho lưu trữ chứa các khóa PGP của người ký Bitcoin Core sử dụng lệnh git clone https://github.com/bitcoin-core/guix.sigs.
6. Nhập các khóa PGP của tất cả người ký sử dụng lệnh gpg --import guix.sigs/builder-keys/\*
7. Xác minh rằng tệp checksum được ký với các khóa PGP của người ký sử dụng lệnh gpg --verify SHA256SUMS.asc.
Mỗi chữ ký sẽ trả về một dòng bắt đầu với: gpg: Good signature và một dòng khác kết thúc với Primary key fingerprint: 133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320 (ví dụ về dấu vân tay PGP của Pieter Wuille).
> 💡 Không cần thiết tất cả các khóa ký phải trả về "OK". Thực tế, chỉ cần một khóa là đủ. Việc xác định ngưỡng xác thực PGP là tùy thuộc vào người dùng.

> Bạn có thể bỏ qua các thông báo WARNING: This key is not certified with a trusted signature!

> Không có chỉ dẫn nào cho thấy chữ ký thuộc về chủ sở hữu.

## Cài đặt giao diện đồ họa Bitcoin Core

1. Trong terminal, vẫn ở trong thư mục chứa file phiên bản Bitcoin Core, sử dụng lệnh tar xzf bitcoin-24.1-x86_64-linux-gnu.tar.gz để giải nén các file trong lưu trữ.

2. Cài đặt các file vừa giải nén bằng lệnh sudo install -m 0755 -o root -g root -t /usr/local/bin bitcoin-24.1/bin//\*

3. Cài đặt các phụ thuộc cần thiết bằng lệnh sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev

4. Khởi động bitcoin-qt (giao diện đồ họa Bitcoin Core) bằng lệnh bitcoin-qt.

5. Để chọn một node cắt tỉa, kiểm tra Limit blockchain storage và cấu hình giới hạn dữ liệu được lưu trữ:

![welcome](assets/1.webp)

## Kết luận Phần 1: Hướng dẫn Cài đặt

Một khi Bitcoin Core đã được cài đặt, khuyến nghị giữ nó chạy càng nhiều càng tốt để đóng góp vào mạng lưới Bitcoin bằng cách xác minh giao dịch và truyền các khối mới cho các peer khác.

Tuy nhiên, việc chạy và đồng bộ hóa node của bạn một cách gián đoạn, ngay cả chỉ để xác thực các giao dịch nhận và gửi, vẫn là một thực hành tốt.

![Creation wallet](assets/2.webp)

# Cấu hình Tor cho một Node Bitcoin Core

> 💡 Hướng dẫn này được thiết kế cho Bitcoin Core 24.0.1 trên các bản phân phối Linux tương thích với Ubuntu/Debian.

## Cài đặt và cấu hình Tor cho Bitcoin Core

Đầu tiên, chúng ta cần cài đặt dịch vụ Tor (The Onion Router), một mạng được sử dụng cho giao tiếp ẩn danh, sẽ cho phép chúng ta ẩn danh các tương tác của mình với mạng lưới Bitcoin. Để được giới thiệu về các công cụ bảo vệ quyền riêng tư trực tuyến, bao gồm Tor, hãy tham khảo bài viết của chúng tôi về chủ đề này.

Để cài đặt Tor, mở một terminal và nhập sudo apt -y install tor. Sau khi cài đặt hoàn tất, dịch vụ sẽ thường được tự động khởi chạy ở chế độ nền. Kiểm tra xem nó có đang chạy đúng cách không với lệnh sudo systemctl status tor. Phản hồi nên hiển thị Active: active (exited). Nhấn Ctrl+C để thoát chức năng này.

> Trong mọi trường hợp, bạn có thể sử dụng các lệnh sau trong terminal để bắt đầu, dừng hoặc khởi động lại Tor:

```
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```

Tiếp theo, hãy khởi động giao diện đồ họa Bitcoin Core với lệnh bitcoin-qt. Sau đó, kích hoạt tính năng tự động của phần mềm để định tuyến các kết nối của chúng tôi qua một proxy Tor: Settings > Network, và từ đó chúng ta có thể kiểm tra Connect through SOCKS5 proxy (default proxy) cũng như Use a separate SOCKS5 proxy to reach peers via Tor onion services.

![option](assets/3.webp)

Bitcoin Core tự động phát hiện nếu Tor đã được cài đặt và, nếu có, sẽ mặc định tạo kết nối ra bên ngoài với các node khác cũng sử dụng Tor, ngoài ra còn có kết nối với các node sử dụng mạng IPv4/IPv6 (clearnet).
💡 Để thay đổi ngôn ngữ hiển thị sang tiếng Pháp, hãy vào tab Hiển thị trong Cài đặt.
## Cấu hình Tor Nâng cao (tùy chọn)

Có thể cấu hình Bitcoin Core để chỉ sử dụng mạng Tor để kết nối với các peer, như vậy tối ưu hóa sự ẩn danh của chúng ta qua node của mình. Vì không có chức năng tích hợp sẵn cho điều này trong giao diện đồ họa, chúng ta sẽ cần phải tạo thủ công một tệp cấu hình. Đi tới Cài đặt, sau đó là Tùy chọn.

![option 2](assets/4.webp)

Tại đây, nhấp vào Mở tệp cấu hình. Một khi đã ở trong tệp văn bản bitcoin.conf, chỉ cần thêm một dòng onlynet=onion và lưu tệp. Bạn cần khởi động lại Bitcoin Core để lệnh này có hiệu lực.
Chúng ta sau đó sẽ cấu hình dịch vụ Tor để Bitcoin Core có thể nhận kết nối đến qua proxy, cho phép các node khác trên mạng sử dụng node của chúng ta để tải dữ liệu blockchain mà không làm ảnh hưởng đến an ninh của máy tính của chúng ta.

Trong terminal, nhập sudo nano /etc/tor/torrc để truy cập vào tệp cấu hình dịch vụ Tor. Trong tệp này, tìm dòng #ControlPort 9051 và xóa # để kích hoạt nó. Bây giờ thêm hai dòng mới vào tệp: HiddenServiceDir /var/lib/tor/bitcoin-service/ và HiddenServicePort 8333 127.0.0.1:8334. Để thoát khỏi tệp và lưu nó, nhấn Ctrl+X > Y > Enter. Quay lại terminal, khởi động lại Tor bằng cách nhập lệnh sudo systemctl restart tor.

Với cấu hình này, Bitcoin Core sẽ có thể thiết lập kết nối đến và đi với các node khác trên mạng chỉ qua mạng Tor (Onion). Để xác nhận điều này, nhấp vào tab Window, sau đó là Peers.

![Nodes Window](assets/5.webp)

## Tài Nguyên Bổ Sung

Cuối cùng, việc chỉ sử dụng mạng Tor (onlynet=onion) có thể khiến bạn dễ bị tấn công Sybil. Đó là lý do tại sao một số người khuyến nghị duy trì một cấu hình đa mạng để giảm thiểu loại rủi ro này. Hơn nữa, tất cả các kết nối IPv4/IPv6 sẽ được định tuyến qua proxy Tor một khi nó được cấu hình, như đã chỉ ra trước đó.

Thay thế, để chỉ ở lại trên mạng Tor và giảm thiểu rủi ro của một cuộc tấn công Sybil, bạn có thể thêm địa chỉ của một node đáng tin cậy khác vào tệp bitcoin.conf của mình bằng cách thêm dòng addnode=trusted_address.onion. Bạn có thể thêm dòng này nhiều lần nếu muốn kết nối với nhiều node đáng tin cậy.

Để xem nhật ký của node Bitcoin của bạn liên quan đặc biệt đến tương tác của nó với Tor, thêm debug=tor vào tệp bitcoin.conf của bạn. Bây giờ bạn sẽ có thông tin Tor liên quan trong nhật ký gỡ lỗi của mình, mà bạn có thể xem trong cửa sổ Thông tin với nút Tệp Gỡ lỗi. Cũng có thể xem những nhật ký này trực tiếp trong terminal với lệnh bitcoind -debug=tor.

> 💡 Một số liên kết thú vị:
>
> - Trang Wiki giải thích về Tor và mối quan hệ của nó với Bitcoin
> - Trình tạo tệp cấu hình Bitcoin Core của Jameson Lopp
> - Hướng dẫn cấu hình Tor của Jon Atack

Như mọi khi, nếu bạn có bất kỳ câu hỏi nào, đừng ngần ngại chia sẻ chúng với cộng đồng Agora256. Chúng ta học cùng nhau để ngày mai tốt hơn hôm nay!