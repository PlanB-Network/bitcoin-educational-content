---
name: Nerdminer
description: Bắt đầu đào bitcoin với cơ hội chiến thắng gần như bằng 0
---

![cover](assets/cover.webp)

> Thiết lập NerdMiner_v2 của bạn

Trong hướng dẫn này, chúng tôi sẽ hướng dẫn bạn qua các bước cần thiết để thiết lập một NerdMiner_v2, đó là một thiết bị phần cứng (một ESP-32 S3) dành riêng cho việc đào bitcoin.
Rõ ràng, sức mạnh tính toán của một thiết bị như vậy không thể cạnh tranh với các ASIC của những người đào mỏ nghiệp dư hoặc chuyên nghiệp. Tuy nhiên, NerdMiner là một công cụ giáo dục hoàn hảo để làm cho việc đào bitcoin trở nên cụ thể. Và ai biết được, với (rất nhiều) may mắn, bạn có thể tìm thấy một khối và phần thưởng đi kèm với nó. Đối với những người tò mò, chúng ta sẽ xem trong phần [Ước lượng xác suất chiến thắng](#estimation-de-la-probabilite-de-gain). Về mặt tiêu thụ năng lượng, một NerdMiner tiêu thụ 0.5W; để so sánh, một bóng đèn LED tiêu thụ trung bình nhiều hơn 20 lần.

Trước khi đi qua các bước khác nhau, hãy liệt kê thiết bị cần thiết để thực hiện:

- một [Lilygo T-display S3](https://lilygo.cc/products/t-display-s3)
- một [nguồn cấp USB-C](https://amzn.eu/d/gIOot90)
- một vỏ 3D: nếu bạn có máy in 3D, bạn có thể tải xuống [file 3D](https://www.printables.com/model/501547-nerdminer-v2-click-case-w-buttons) nếu không bạn có thể mua một cái trên [cửa hàng trực tuyến Silexperience](https://silexperience.company.site/NerdMiner_V2-p544379757).
- một PC với trình duyệt Chrome đã cài đặt
- một kết nối internet
- một địa chỉ bitcoin

Bạn cũng có thể mua một bộ kit NerdMiner đã lắp ráp sẵn từ một số nhà bán lẻ như:

- [DécouvreBitcoin](https://shop.decouvrebitcoin.com/products/nerd-miner?_pos=1&_psq=nerd&_ss=e&_v=1.0)
- [BitMaker](https://bitronics.store/shop/)

Đầu tiên, chúng ta sẽ xem cách flash phần mềm vào ESP-32 S3, sau đó chúng ta sẽ xem cách khởi động lại nó để thay đổi mạng wifi. Các bước này dành cho người dùng Windows, nếu bạn đang sử dụng hệ điều hành Linux, vui lòng thực hiện [các bước sơ bộ](#etapes-preliminaires-pour-utilisateurs-linux) để cho phép hệ thống nhận diện ESP-32 S3.

# Cài đặt phần mềm NerdMiner_v2

Việc cài đặt phần mềm được đơn giản hóa đáng kể nhờ sử dụng webflasher.

## Bước 1: Chuẩn bị webflasher

Đầu tiên, bạn cần truy cập vào [trình flash NM2 trực tuyến](https://bitmaker-hub.github.io/diyflasher/).

Sau đó chọn firmware tương ứng với ESP-32 của bạn. Hầu hết thời gian đó là mặc định: T-Display S3. Sau đó nhấp vào "Flash".

> ⚠️ Quan trọng là bạn sử dụng trình duyệt Chrome - vì nó cho phép, theo mặc định, sử dụng flash và truy cập vào các cổng USB của bạn.

![](assets/webflasher.webp)

## Bước 2: Kết nối ESP-32

Một khi webflasher được khởi chạy, một cửa sổ pop-up sẽ mở ra hiển thị các cổng USB được trình duyệt nhận diện.
Sau đó, bạn có thể kết nối ESP-32 của mình, và một cổng mới sẽ được hiển thị (trong trường hợp này, đó là cổng ttyACM0). Bạn phải chọn nó và nhấn vào "kết nối".
![](assets/flasher-port-serial.webp)

Phần mềm sau đó sẽ được tải xuống ESP32 của bạn trong vài giây.

![](assets/NM2-sucessfully-installed.webp)

## Bước 3: Cấu hình NerdMiner

Việc cấu hình NerdMiner của bạn sẽ được thực hiện qua smartphone hoặc máy tính.
Bật WiFi và kết nối với mạng NerdMinerAP địa phương. Nếu bạn sử dụng smartphone, cổng cấu hình sẽ tự động mở. Nếu không, hãy nhập địa chỉ 192.168.4.1 vào trình duyệt.
Sau đó chọn "Cấu hình WiFi".

Bây giờ bạn có thể cấu hình NerdMiner của mình.
Đầu tiên, bắt đầu bằng cách kết nối với mạng WiFi của bạn bằng cách chọn tên mạng của bạn và nhập mật khẩu tương ứng.

Sau đó, bạn có thể chọn hồ bơi khai thác mà bạn muốn tham gia. Thực sự, trong ngành công nghiệp khai thác bitcoin, việc gộp công suất tính toán để tăng cơ hội tìm thấy một khối đổi lại việc chia sẻ phần thưởng tương ứng với hashrate cung cấp là điều phổ biến.
Đối với NerdMiners, bạn có thể chọn kết nối với một trong những hồ sau:

| Pool URL          | Port  | URL                        | Status                                   |
| ----------------- | ----- | -------------------------- | ---------------------------------------- |
| public-pool.io    | 21496 | https://web.public-pool.io | Hồ solo và mã nguồn mở mặc định |
| pool.nerdminer.io | 3333  | https://nerdminer.io       | Được duy trì bởi CHMEX                      |
| pool.vkbit.com    | 3333  | https://vkbit.com/         | Được duy trì bởi djerfy                     |

Sau khi bạn đã chọn hồ của mình, bạn cần nhập địa chỉ bitcoin của mình để nhận phần thưởng trong trường hợp (nếu có) một khối được tìm thấy.

Ngoài ra, chọn múi giờ của bạn để NerdMiner có thể hiển thị thời gian chính xác.
Bây giờ bạn có thể nhấn vào "lưu".

![](assets/wifi-configuration.webp)

Xin chúc mừng, bạn giờ đây là một phần của mạng lưới khai thác Bitcoin!

## Hoạt động của NerdMiner

Phần mềm NerdMinerv2 có 3 màn hình khác nhau, mà bạn có thể truy cập bằng cách nhấn vào nút trên cùng bên phải màn hình của bạn:

- Màn hình chính cung cấp quyền truy cập vào thống kê của NerdMiner của bạn.
- Màn hình thứ hai cung cấp quyền truy cập vào thời gian, hashrate của bạn, giá của bitcoin, và chiều cao của khối.
- Màn hình thứ ba cung cấp quyền truy cập vào thống kê về mạng lưới khai thác bitcoin toàn cầu.
  ![](assets/NM2-screens.webp)

Nếu bạn muốn khởi động lại NerdMiner của mình, ví dụ để thay đổi mạng WiFi, bạn cần nhấn giữ nút trên cùng trong 5 giây.

Nhấn nút dưới cùng một lần sẽ tắt NerdMiner của bạn. Nhấn đôi sẽ xoay hướng màn hình.

### Các bước chuẩn bị cho người dùng Linux

Dưới đây là các bước để Chrome nhận diện cổng serial trên Linux.

1. Xác định cổng liên quan:

- Kết nối ESP-32 của bạn với máy tính.
- Mở một terminal.
- Nhập lệnh sau để liệt kê tất cả các cổng:
  - `dmesg | grep tty`
  - hoặc `ls /dev/tty*`
- Để chắc chắn về cổng, bạn có thể tiến hành loại bỏ bằng cách lặp lại lệnh mà không kết nối ESP-32.

2. Thay đổi quyền của cổng liên quan:
- Theo mặc định, việc truy cập vào các cổng serial có thể yêu cầu quyền root, vì vậy chúng ta sẽ làm cho chúng có sẵn bằng cách thêm người dùng của bạn vào nhóm `dialout`.  - `sudo usermod -a -G dialout TÊN_NGƯỜI_DÙNG_CỦA_BẠN`, thay thế `TÊN_NGƯỜI_DÙNG_CỦA_BẠN` bằng tên người dùng của bạn.
  - sau đó đăng xuất và đăng nhập lại với tư cách người dùng này, hoặc khởi động lại hệ thống để đảm bảo rằng các thay đổi nhóm có hiệu lực.

Bây giờ ESP-32 của bạn đã được hệ thống nhận diện, bạn có thể quay lại [bước đầu tiên](#etape-1-preparation-du-webflasher) để cài đặt phần mềm.

## Kết luận

Và đó là tất cả! NerdMiner_v2 của bạn giờ đã được cấu hình và sẵn sàng sử dụng.

Chúc bạn đào coin vui vẻ và may mắn luôn mỉm cười với bạn!

### Ước lượng khả năng chiến thắng

Hãy thử vui với việc ước lượng khả năng chiến thắng một phần thưởng khối. Ước lượng này sẽ khá sơ bộ và chỉ nhằm mục đích xác định cỡ lớn của khả năng.
Hồ bơi mà NerdMiner có thể kết nối chỉ là "hồ bơi đào coin một mình" nghĩa là hồ bơi không chia sẻ hashrate của tất cả các máy đào kết nối mà chỉ đơn giản là hành động như một điều phối viên.
Bây giờ giả sử rằng NerdMiner của chúng ta có hashrate khoảng 45kH/s.

Biết rằng tổng hashrate khoảng 450 EH/s (hoặc 4.5 x 10^20 hashes mỗi giây), chúng ta có thể coi khả năng tìm thấy khối tiếp theo là 1 trong 100 triệu tỷ, điều này rất rất rất khó xảy ra. Vì vậy, ngoài việc là một công cụ giáo dục và đối tượng của sự tò mò, một NerdMiner cũng có thể được coi như một vé số trong đào bitcoin với chi phí điện năng biên lề 0.5 W--mặc dù như chúng ta vừa thấy khả năng chiến thắng cực kỳ thấp. Tuy nhiên, tại sao không thử vận may của bạn?

### Thông Tin Bổ Sung

Dưới đây là một số liên kết nếu bạn muốn tìm hiểu thêm về chủ đề:

- [Trang dự án NerdMiner_v2](http://github.com/BitMaker-hub/NerdMiner_v2)
- [Tài liệu đầy đủ về NerdMiners](https://docs.bitwater.ch/nerd-miner-v2/)