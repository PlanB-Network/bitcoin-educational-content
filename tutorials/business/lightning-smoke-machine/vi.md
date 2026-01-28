---
name: Lightning Smoke Machine
description: Kích hoạt máy tạo khói bằng thanh toán Lightning thông qua ESP32.
---

![cover-lightning-smoke-machine](assets/cover.webp)



## Giới thiệu



Biến máy tạo khói cổ điển thành thiết bị có thể thanh toán bằng Bitcoin thông qua Lightning Network. Mỗi lần thanh toán sẽ tự động kích hoạt một luồng khói!





- Trình độ: Trung cấp
- Thời gian dự kiến: 2-3 giờ
- Các trường hợp sử dụng: Sự kiện Bitcoin, biểu diễn nghệ thuật, trình diễn Lightning, hiệu ứng sân khấu tự động.



## Điều kiện tiên quyết



### Kiến thức





 - Điện tử cơ bản (dây dẫn, rơle)
 - Hàn (hoặc sử dụng đầu nối Dupont)
 - Cấu hình mạng (WiFi, WebSocket)



### Cần có tài khoản





- Máy chủ BTCPay: Phiên bản hoạt động (tự lưu trữ hoặc được lưu trữ)
- Blink Wallet: Tài khoản + quyền truy cập API



### Truy cập





- Quyền quản trị viên truy cập máy chủ BTCPay
- Kết nối WiFi cho ESP32



## Vật liệu cần thiết



### Phần cứng - Linh kiện điện tử





- 1 Vi điều khiển - ESP32-WROOM-32


*ESP32-WROOM-32 là một vi điều khiển WiFi/Bluetooth nhỏ gọn, giá thành thấp dùng để kết nối các thiết bị điện tử với Internet và điều khiển chúng từ xa.*



![ESP32](assets/fr/1.webp)





- 1 Mô-đun rơle - 5V có bộ ghép quang


*Rơle giống như một công tắc mà ESP32 có thể điều khiển để bật hoặc tắt máy tạo khói.*



![relay](assets/fr/2.webp)





- ~10 dây cáp Dupont - Đầu đực/đầu đực và đầu đực/đầu cái



![dupont-cables](assets/fr/3.webp)





- 1. Nguồn cấp điện cho ESP32 - USB 5V hoặc pin Li-Po.



![battery](assets/fr/4.webp)





- 1 cáp micro-USB - dùng để kết nối ESP32 với nguồn điện.



![micro-usb-cables](assets/fr/5.webp)





- 1 máy tạo khói 220V kèm điều khiển từ xa bằng pin 12V



![remote-and-smoke-machine](assets/fr/6.webp)





- 1 chai dung dịch tương thích với máy tạo khói của bạn



### Phần cứng - Dụng cụ





- Mỏ hàn + thiếc (nếu hàn)
- Tua vít
- Đồng hồ vạn năng (khuyến nghị)



### Phần mềm





- Phần mềm BitcoinSwitch: **[https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)**
- Trình duyệt web tương thích với WebSerial (Chrome/Edge/Brave)
- Máy chủ BTCPay đã được cấu hình. Để biết thêm thông tin về cách tạo một phiên bản máy chủ BTCPay, hãy truy cập hướng dẫn này: https://planb.academy/fr/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc



## Kiến trúc hệ thống



![architecture-lightning-smoke-machine](assets/fr/7.webp)



---


**⚠️** **CẢNH BÁO AN TOÀN - ĐỌC TRƯỚC KHI TIẾP TỤC** **⚠️**



Dự án này liên quan đến một máy tạo khói được kết nối với nguồn điện lưới **220V**. Vận hành không đúng cách có thể dẫn đến **điện giật gây tử vong** hoặc **hỏa hoạn**.



**Những quy tắc không thể thương lượng:**



1. **LUÔN LUÔN ngắt máy tạo khói khỏi nguồn điện** trước khi mở điều khiển từ xa hoặc can thiệp vào hệ thống dây điện.


2. **Tháo pin khỏi điều khiển từ xa** trước khi cầm nắm (nguy cơ đoản mạch và hư hỏng các linh kiện)


3. **Hãy kiểm tra kỹ tất cả các kết nối đã được cách ly** trước khi kết nối lại bất cứ thứ gì.


4. **Tuyệt đối không được kết nối lại nguồn điện 220V** cho đến khi hộp điều khiển từ xa đã được đóng kín và cố định chắc chắn.



Nếu bạn không thoải mái với cách xử lý này, hãy đi cùng người nào đó có kinh nghiệm.



---

## PHẦN 1: Lắp ráp phần cứng



### Bước 1: Chuẩn bị điều khiển từ xa



Mục tiêu: Kết nối rơle với nút BẬT/TẮT trên điều khiển từ xa.


1. Mở điều khiển từ xa




    - Xác định nút BẬT/TẮT
    - Tháo ốc vít trên vỏ để mở điều khiển từ xa.


2. Xác định vị trí các kết nối




 - Xác định vị trí các cực dương (+) và cực âm (-) của thiết bị.
 - Kiểm tra tính liên tục của mạch bằng đồng hồ vạn năng (tùy chọn)



![smoke-machine-remote](assets/fr/8.webp)



3. Đấu dây nút bấm (hàn hoặc dùng đầu nối)




    - Hàn một sợi dây màu đen vào cực âm (-) của nút bấm.
    - Hàn một dây cáp màu đỏ vào cực dương (+) chung.



![smoke-machine-remote](assets/fr/9.webp)



### Bước 2: Kết nối với mô-đun rơle



**Nhắc nhở: Thuật ngữ chuyển tiếp




| **Cực**         | **Mô tả**           | **Chức năng**                        |
| -------------------- | ------------------------- | ----------------------------------- |
| NO (Bình thường Mở)   | Mạch mở theo mặc định | Đóng khi rơle được kích hoạt |
| NC (Bình thường Đóng) | Mạch đóng theo mặc định  | Mở khi rơle được kích hoạt  |
| COM (Chung)         | Cực trung tâm          | Chuyển đổi giữa NO và NC              |

**Sơ đồ đấu dây từ bộ điều khiển từ xa đến mô-đun rơle:**




- Dây màu đen từ nút BẬT/TẮT **→** thường mở (Normally Open)
- Dây màu đỏ (chung) **→** COM (Chung)



**Lý luận:**


Khi ESP32 kích hoạt rơle, nó sẽ kết nối chân COM và NO, điều này hoàn toàn giống như việc nhấn nút trên điều khiển từ xa.


Khi ESP32 ngắt rơle, chân COM và NO sẽ tách rời, điều này tương đương với việc nhả nút bấm.



![remote-relay](assets/fr/10.webp)



### Bước 3: Kết nối ESP32 với mô-đun rơle



**Sơ đồ đấu dây:**




| **ESP32** | **→** | **Mô-đun Rơle** |
| --------- | ----- | ----------------- |
| V5 (5V)   | **→** | VCC               |
| GND       | **→** | GND               |
| GPIO 21   | **→** | IN (Đầu vào)        |

**Xác minh:**




- VCC và GND được kết nối đúng cực.
- Chân GPIO 21 được sử dụng cho tín hiệu điều khiển.
- Không có hiện tượng đoản mạch rõ ràng



![relay-esp32](assets/fr/11.webp)



**Phần cứng Checkpoint**


Trước khi chuyển sang sử dụng phần mềm, hãy kiểm tra:




- Điều khiển từ xa được đấu dây đúng cách
- Mô-đun rơle được kết nối với ESP32
- Không có dây trần nào chạm vào các linh kiện khác.
- Điện áp 220V luôn bị ngắt kết nối



![relay-esp32](assets/fr/12.webp)





---


## PHẦN 2: Cấu hình phần mềm



Chúng ta sẽ sử dụng *Blink* làm ví dụ, nhưng *BTCPay Server* cũng cung cấp *Strike, Breez và Boltz* nếu bạn muốn lựa chọn khác.



### Bước 1: Cài đặt Plugin *BitcoinSwitch* + *Blink*



1 - Truy cập vào máy chủ *BTCPay Server* của bạn bằng tài khoản quản trị viên.



2 - Tạo tin nhắn đầu tiên của bạn



3 - Ở phía bên trái của *BTCPay Server*, cuộn xuống dưới cùng và chọn *"Quản lý Plugin"*.



![btcpay-plugins](assets/fr/13.webp)



4 - Chúng ta sẽ cài đặt các plugin *BitcoinSwitch* cũng như *Blink*.



![btcpay-plugins](assets/fr/14.webp)



5 - Cuộn xuống danh sách các plugin và nhấp vào *"Cài đặt"*: *BitcoinSwitch và Blink* (hoặc wallet nếu bạn muốn)



![btcpay-plugins](assets/fr/15.webp)



6 - Sau khi quá trình cài đặt hoàn tất, hãy khởi động lại *BTCPay Server* và đợi 1 phút để máy chủ khởi động lại.



![btcpay-plugins](assets/fr/16.webp)



7 - Khi bạn quay lại mục *"Quản lý plugin"*, hãy kiểm tra xem cả hai plugin đã được cài đặt chưa.



![btcpay-plugins](assets/fr/17.webp)



### Bước 2: Phần phụ trợ: Cấu hình *BTCPay Server + Blink*



**1 - Tạo wallet *Blink***




- Hãy truy cập https://www.blink.sv
- Hãy tạo tài khoản của bạn. Vui lòng tham khảo hướng dẫn:



[https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd)



**2 - Tạo khóa API *Blink***




- Truy cập giao diện API: **[https://www.blink.sv/en/api](https://www.blink.sv/en/api)** và đăng nhập bằng cùng tài khoản bạn đã sử dụng để tạo wallet *Blink*



![blink-api](assets/fr/18.webp)





   - Sau khi kết nối, hãy chuyển đến tab *API Keys*



![blink-api](assets/fr/19.webp)





   - Nhấp vào biểu tượng (*) + ** ở góc trên bên phải để truy cập cấu hình khóa API của bạn.



![blink-api](assets/fr/20.webp)





   - Đặt tên cho khóa API của bạn và giữ nguyên các cài đặt mặc định. Sau đó, ở bước thứ ba, hãy ghi lại khóa API của bạn - bạn chỉ nhìn thấy nó một lần: `blink_mZ5KxxxxxxxxxxxxxNbmX`



![blink-api](assets/fr/21.webp)





   - Sau khi tạo xong, nó sẽ xuất hiện trong danh sách Khóa API đang hoạt động của bạn.



![blink-api](assets/fr/22.webp)



**3 - Kết nối *Blink* với *Máy chủ BTCPay***




- Mở *Máy chủ BTCPay* của bạn
- Điều hướng đến: *Wallet* **→** *Lightning*



![btcpay-server](assets/fr/23.webp)





- Nhấp vào *Sử dụng nút tùy chỉnh*
- Dán chuỗi kết nối sau:



```
type=blink;server=https://api.blink.sv/graphql;api-key=blink_mZ5KxxxxxxxxNbmX;wallet-id=0a3fc465-082xxxxxxxxxx-2545595d856f
```



**⚠️** **Quan trọng** :




- Không được sửa đổi phần đầu tiên: `type=blink;server=https://api.blink.sv/graphql`;
- Chỉ thay thế:
    - api-key= *bằng khóa API Blink của bạn*
    - wallet-id= *bằng ID wallet Blink của bạn*
- Sau đó nhấp vào *Kiểm tra kết nối*, rồi *Lưu*.



![btcpay-server](assets/fr/24.webp)





 - Kiểm tra xem kết nối đã được thiết lập chưa (trạng thái màu xanh lá cây).



![btcpay-server](assets/fr/25.webp)



**4 - Tạo hệ thống bán hàng (POS)**




- Trong BTCPay Server, hãy vào tab *Plugins* và nhấp vào *Point of sale*.



![btcpay-server](assets/fr/26.webp)





- Đặt tên cho hệ thống POS của bạn và nhấp vào *Tạo*.



![btcpay-server](assets/fr/27.webp)





- Cấu hình POS:
    - Chọn kiểu hiển thị tại điểm bán hàng = *In ấn*
    - Đơn vị tiền tệ = *SATS*
    - Nhấp vào *LƯU*



![btcpay-server](assets/fr/28.webp)





- Cấu hình sản phẩm:
    - Xóa tất cả sản phẩm mặc định
    - Sau đó nhấp vào *thêm mục*.



![btcpay-server](assets/fr/29.webp)



![btcpay-server](assets/fr/30.webp)





- Cấu hình sản phẩm:
    - Tiêu đề: *Máy tạo khói*
    - Giá: *10 sats*
    - Công tắc GPIO Bitcoin: 21
    - Thời gian chuyển mạch Bitcoin (tính bằng mili giây): 5000
    - Nhấp vào *Đóng* rồi *Lưu* để lưu sản phẩm mới.



![btcpay-server](assets/fr/31.webp)



### Bước 3: Nạp firmware: Nạp firmware cho ESP32



**1 - Truy cập trang web Flash




- Truy cập vào: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)



![bitcoinswitch-lnbits](assets/fr/32.webp)



**2 - Flash firmware của BitcoinSwitch**




- Kết nối ESP32 với máy tính của bạn bằng cáp USB/Micro-USB.
- Sau đó nhấp vào *Kết nối với thiết bị*.
- Một cửa sổ sẽ hiện ra, chọn cổng USB trên ESP32 của bạn, sau đó nhấp vào *Kết nối*.



![bitcoinswitch-lnbits](assets/fr/33.webp)





- Sau khi kết nối ESP32, chúng ta sẽ nạp firmware BitcoinSwitch. Trong phần *T-Display*, hãy nhấp vào *Upload Firmware* để tải phiên bản mới nhất (hiện tại: *bitcoinSwitch T-Display v1.0.1*).



![bitcoinswitch-lnbits](assets/fr/34.webp)





- Chờ quá trình tải lên hoàn tất, khi nhật ký hiển thị *"Đang rời đi..."*


![bitcoinswitch-lnbits](assets/fr/35.webp)





- Rút phích cắm ESP32



**3 - Kiểm tra cài đặt firmware BitcoinSwitch




- Tải lại trang: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- Kết nối lại ESP32 với máy tính của bạn bằng cáp USB/Micro-USB.
- Sau đó nhấp vào *Kết nối với thiết bị*
- Chọn cổng USB trên ESP32 của bạn, sau đó nhấp vào *Kết nối* như đã mô tả ở trên.
- Sau khi kết nối, hãy nhấn nút **RESET** trên ESP32.
- Hãy kiểm tra nhật ký để đảm bảo các dòng cuối cùng hiển thị như sau:



```
Welcome to BitcoinSwitch! (v1.0.1)
Config file does not exist.
Entering config mode. until we receive /config-done.
```



(Đây là điều bình thường, có nghĩa là chưa có cấu hình nào được thiết lập, nhưng phần mềm đã được cài đặt)



![bitcoinswitch-lnbits](assets/fr/36.webp)



**4 - Tạo URL WebSocket LN**



Định dạng cuối cùng dự kiến:



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```



Các bước tạo ra sản phẩm:




- Mở máy chủ BTCPay của bạn, sau đó truy cập vào máy POS mà chúng ta đã tạo ở bước sau.
- Sau đó nhấp vào "Xem" để mở phần mềm POS của bạn trong trình duyệt.



![btcpay-server-https](assets/fr/37.webp)





- Sao chép URL của trang, ví dụ:



![btcpay-server-https](assets/fr/38.webp)



Hãy cùng phân tích URL này:



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```





- `XXXXv` → tên miền của máy chủ BTCPay Server của bạn
- `46XXXXXXXXXXXXXXXXXXXXwFB` → mã định danh duy nhất của máy POS của bạn
- `/pos` → biểu thị điểm bán hàng



Biến đổi nó:




- Thay thế `https://` bằng `wss://`
- Thêm `/bitcoinswitch` vào cuối



Kết quả:



```
wss://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos/bitcoinswitch
```



Hãy giữ lại URL này để cấu hình trong tương lai, vì nó sẽ cho phép ESP32 của bạn giao tiếp theo thời gian thực với máy chủ BTCPay. Giao thức WebSocket (`wss://`) thiết lập kết nối liên tục giữa hai bên: ngay sau khi thanh toán Lightning được xác nhận trên máy POS của bạn, BTCPay sẽ ngay lập tức gửi thông tin đến ESP32, từ đó có thể kích hoạt máy tạo khói của bạn.



**5 - Cấu hình WiFi và WebSocket




- Quay lại trang: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/) với ESP32 đã được kết nối.
- Vào *Cấu hình thiết bị* → *Cài đặt Wifi*



Thông báo :




- SSID WiFi: tên mạng WiFi của bạn
- Mật khẩu WiFi: mật khẩu WiFi của bạn



![bitcoinswitch-lnbits](assets/fr/39.webp)





- Trong phần *URL thiết bị LNbits*, hãy dán URL WebSocket đã tạo ở bước trước.
- Nhấp vào *Tải lên cấu hình*



![bitcoinswitch-lnbits](assets/fr/40.webp)





- Hãy đợi quá trình tải lên hoàn tất; nhật ký sẽ hiển thị các thông số bạn vừa nhập (SSID, mật khẩu và URL WebSocket).



![bitcoinswitch-lnbits](assets/fr/41.webp)





- Hãy đợi trong khi ESP32 thiết lập kết nối WebSocket. Bạn sẽ thấy:



```
WiFi connection established!

[WebSocket] Connected to url: ...
```



![bitcoinswitch-lnbits](assets/fr/42.webp)





- Giờ bạn có thể ngắt kết nối ESP32.



---
## Phần mềm Checkpoint



Trước khi làm bài kiểm tra cuối cùng, hãy kiểm tra:





- Blink được kết nối với BTCPay
- PoS được tạo với ít nhất 1 mặt hàng
- ESP32 đã được nạp firmware BitcoinSwitch.
- WiFi đã được cấu hình trên ESP32
- URL WebSocket chính xác
- Nhật ký ESP32 không lỗi



---

## Kiểm thử và gỡ lỗi



### Hoàn thành bài kiểm tra cuối kỳ



1. Cắm máy tạo khói (220V) vào ổ điện và bật máy lên.


2. Cấp nguồn cho ESP32 (pin hoặc USB)


3. Mở BTCPay PoS trong trình duyệt của bạn.


4. Quét mục "máy tạo khói"


5. Thanh toán bằng wallet Lightning (Blink hoặc các loại wallet khác)


6. Quan sát:




 - Rơ le kêu tách (có tiếng kêu và đèn LED của rơ le sáng lên)
 - Máy tạo khói đã được kích hoạt
 - Khói bốc lên!



### Các vấn đề và giải pháp về sự công bằng




| **Vấn đề**                        | **Nguyên nhân có thể**              | **Giải pháp**                                                                                 |
| ----------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------- |
| ESP32 không kết nối            | Thiếu trình điều khiển USB             | Cài đặt [CH340 drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers) |
| Rơle không nhấp chuột                | Dây GPIO sai            | Kiểm tra GPIO 21 → IN                                                                        |
| Máy tạo khói không phản ứng         | Điều khiển từ xa được nối sai         | Kiểm tra NO/NC/COM                                                                           |
| Hết thời gian chờ WebSocket                   | URL không chính xác                  | Kiểm tra wss:// và /bitcoinswitch                                                            |
| WiFi không kết nối             | SSID/Mật khẩu sai            | Flash lại cấu hình WiFi                                                                    |
| Nhận thanh toán nhưng không có gì xảy ra | ESP32 không được kết nối với WebSocket | Kiểm tra nhật ký RESET                                                                      |

## Tài nguyên



### Các liên kết hữu ích





- Phần mềm BitcoinSwitch: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- Tài liệu hướng dẫn sử dụng BTCPay Server: [https://docs.btcpayserver.org/](https://docs.btcpayserver.org/)
- Blink API : [https://dev.blink.sv/](https://dev.blink.sv/)
- Sơ đồ chân ESP32: [https://randomnerdtutorials.com/esp32-pinout-reference-gpios/](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/)



### Cộng đồng & Hỗ trợ





- Máy chủ BTCPay** : [chat.btcpayserver.org](https://chat.btcpayserver.org/) - Mattermost chính thức
- Máy chủ BTCPay Telegram** : [t.me/btcpayserver](https://t.me/btcpayserver)
- LNbits** : [t.me/lnbits](https://t.me/lnbits) - Cộng đồng Telegram chính thức, hoạt động tích cực
- BitcoinSwitch (lỗi phần mềm)**: [github.com/lnbits/bitcoinswitch/issues](https://github.com/lnbits/bitcoinswitch/issues)



### Mã nguồn





- Mã nguồn firmware của BitcoinSwitch: [https://github.com/lnbits/bitcoinswitch](https://github.com/lnbits/bitcoinswitch)



---

**⚡** Tích trữ sats, tạo khói, vui vẻ và luôn khiêm tốn! **⚡**