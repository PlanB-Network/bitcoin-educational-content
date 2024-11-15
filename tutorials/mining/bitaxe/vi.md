---
name: Cài Đặt BitAxe
Description: Hướng dẫn cách cài đặt BitAxe?
---

### Giới thiệu

BitAxe là một dự án mã nguồn mở được tạo ra bởi Skot và [có sẵn trên GitHub](https://github.com/skot/bitaxe) cho phép thực hiện thí nghiệm đào coin với chi phí hiệu quả.

Nó đã đảo ngược kỹ thuật của Antminer S19 nổi tiếng của Bitmain, nhà lãnh đạo thị trường trong ASICs, những máy chuyên dụng cho việc đào bitcoin. Bây giờ, việc sử dụng những chip mạnh mẽ này trong các dự án mã nguồn mở mới đã trở nên khả thi. Khác với Nerdminer, BitAxe có đủ sức mạnh tính toán để kết nối với một mining pool, điều này sẽ cho phép bạn kiếm được một số satoshis đều đặn. Ngược lại, Nerdminer chỉ có thể kết nối với cái gọi là solopool, hoạt động giống như một vé số: bạn có cơ hội nhỏ để giành được phần thưởng toàn bộ khối.

Có nhiều phiên bản của BitAxe, với các chip và hiệu suất khác nhau:

| Dòng Bitaxe              | ASIC Chip | Sử Dụng Trên                | Tốc Độ Hash Dự Kiến        | Lý Tưởng Cho                                                                                                |
| ------------------------ | --------- | --------------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Bitaxe Max (Dòng 100)    | 1 x BM1397| Antminer Series 17          | 400 GH/s (lên đến 450 GH/s) | Người mới bắt đầu đào Bitcoin, cung cấp tốc độ hash ổn định với mức tiêu thụ điện năng vừa phải.           |
| Bitaxe Ultra (Dòng 200)  | 1 x BM1366| Antminer S19 XP và S19k Pro | 500 GH/s (lên đến 550 GH/s) | Những người đào mỏ nghiêm túc muốn cân bằng hiệu quả và tốc độ hash cao hơn.                                |
| Bitaxe Hex (Dòng 300)    | 6 x BM1366| Antminer S19k Pro và S19 XP | 3.0 TH/s (lên đến 3.3 TH/s) | Những người đào mỏ tìm kiếm khả năng mở rộng và hiệu suất cao mà không hy sinh hiệu quả.                   |
| Bitaxe Supra (Dòng 400)  | 1 x BM1368| Antminer S21                | 600 GH/s (lên đến 700 GH/s) | Những người đam mê nghiêm túc tìm kiếm tốc độ hash và hiệu quả cao nhất.                                   |

Trong hướng dẫn này, chúng ta sẽ sử dụng BitAxe Ultra 204 được trang bị chip BM1366, dùng cho Antminer S19XP. Máy này đã được lắp ráp và flash sẵn bởi nhà bán lẻ.

### [Danh sách các nhà bán lẻ có sẵn trên trang này](https://bitaxe.org/legit.html)

![signup](assets/2.webp)

Thông thường, nguồn cung cấp điện được bán kèm theo. Nếu không, bạn sẽ cần mua một nguồn cung cấp điện với cáp jack 5V và ít nhất 4A.

![signup](assets/1.webp)

### Cấu hình
Khi bạn cắm BitAxe vào lần đầu tiên, nó sẽ cố gắng kết nối với mạng Wi-Fi mặc định. Sau năm lần thử, nó sẽ hiển thị tên của mạng Wi-Fi của chính nó để bạn có thể kết nối và cấu hình.
Để làm điều này, bạn có thể sử dụng bất kỳ máy tính hoặc điện thoại thông minh nào. Vào cài đặt Wi-Fi của bạn, tìm kiếm các mạng mới, và bạn sẽ thấy một Wi-Fi có tên là Bitaxe_XXXX. Ở đây, nó là `Bitaxe_A859`. Kết nối với mạng Wi-Fi này, và một cửa sổ sẽ tự động mở ra.

![signup](assets/3.webp)

Trong cửa sổ này, nhấp vào ba thanh ngang nhỏ ở góc trên bên trái, sau đó chọn `Settings`.

![signup](assets/4.webp)

Bạn sẽ cần nhập thông tin mạng Wi-Fi của mình một cách thủ công, vì không có hệ thống phát hiện tự động.
![signup](assets/5.webp)
Do đó, hãy chỉ định SSID của Wi-Fi, tức là tên của mạng của bạn, mật khẩu, cũng như thông tin về mining pool mà bạn đã chọn. Hãy cẩn thận, ở đây URL của pool không được trình bày theo cùng một cách. Ví dụ, đối với Braiins, URL pool được cung cấp là: `stratum+tcp://eu.stratum.braiins.com:3333`.

![signup](assets/6.webp)

Như bạn có thể thấy trên màn hình, bạn cần loại bỏ phần `stratum+tcp://` và `:3333`, chỉ để lại `eu.stratum.braiins.com`. Sau đó, trong trường `Port`, nhập 4 chữ số cuối cùng của URL do pool cung cấp, nhưng không có `:`. Ở đây, do đó là `3333`.

Trong hướng dẫn này, chúng tôi đang sử dụng mining pool Braiins, nhưng bạn có thể tự do chọn một pool khác. Bạn có thể tìm các hướng dẫn của chúng tôi về mining pool [trên trang web của PlanB Network](https://planb.network/en/tutorials/mining).

Tiếp theo, trong `User`, nhập mã định danh của bạn và sau đó là `Password`, thường thì đó là `"x"` hoặc `"Anything123"`.

Cài đặt `Core Voltage` nên để mặc định là `1200`, và đối với `Frequency`, cũng để giá trị mặc định ban đầu. Sau này sẽ có thể điều chỉnh cài đặt này để có được nhiều sức mạnh tính toán hơn. Tuy nhiên, điều quan trọng là phải đảm bảo nhiệt độ của chip không vượt quá 65-70°C, vì BitAxe không có hệ thống giảm hiệu suất trong trường hợp quá nhiệt. Nếu nhiệt độ vượt quá 65°C quá nhiều, nó có thể làm hỏng BitAxe của bạn.

![signup](assets/7.webp)

Sau khi bạn đã nhập chính xác tất cả các cài đặt, nhấn nút `Save` ở phía dưới, sau đó khởi động lại BitAxe của bạn đơn giản bằng cách rút phích cắm và cắm lại.
Nếu bạn đã nhập thông tin của mình một cách chính xác, thiết bị sẽ nhanh chóng kết nối với Wi-Fi của bạn, sau đó đến mining pool, và bắt đầu hiển thị một số thông tin trên màn hình nhỏ của nó. Có thể sẽ mất vài phút để nó xuất hiện trên bảng điều khiển của mining pool.
### Bảng Điều Khiển và Màn Hình

Ba màn hình khác nhau sẽ lướt qua. Trên trang thứ ba, bạn sẽ thấy thông tin `IP`, đó là địa chỉ IP cho phép bạn kết nối với bảng điều khiển. Ở đây, địa chỉ là `192.168.1.19`.

![signup](assets/8.webp) ![signup](assets/9.webp) ![signup](assets/10.webp)

Để truy cập bảng điều khiển, chỉ cần nhập địa chỉ này vào trình duyệt internet của bạn.

Trên bảng điều khiển, bạn sẽ tìm thấy tất cả thông tin được hiển thị trên màn hình nhỏ, mà chúng tôi sẽ giờ đây xem xét chi tiết.

![signup](assets/11.webp)

| Màn Hình BitAxe | Bảng Điều Khiển                             | Mô Tả                                                                                                                                                                                                                     |
| --------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gh              | Hashrate                                    | Sức mạnh tính toán hiện tại, được biểu thị bằng GigaHash/s                                                                                                                                                                |
| W/THs           | Hiệu Suất                                   | Đây là hiệu suất của BitAxe của bạn được biểu thị bằng W/THs. Đó là tỷ lệ giữa công suất điện tiêu thụ và sức mạnh tính toán sản xuất.                                                                                    |
| A/R             | Shares                                      | Số lượng `Shares` được BitAxe của bạn gửi đến pool, đại diện cho lượng công việc được cung cấp.                                                                                                                          |
| UT              | Thời Gian Hoạt Động                         | Thời gian kể từ khi BitAxe của bạn hoạt động không gián đoạn (có sẵn trong menu bên trái dưới `Logs`).                                                                                                                   |
| BD            | Độ Khó Tốt Nhất                             | Độ khó tối đa đạt được kể từ lần khởi động lại cuối cùng. Để so sánh, độ khó mạng hiện tại khoảng 85T.                                                                                                                      |
| FAN           | Quạt trong hộp `Nhiệt`                     | Tốc độ quay của quạt, được biểu thị bằng số vòng quay mỗi phút.                                                                                                                                                           |
| Temp          | Nhiệt độ ASIC trong hộp `Nhiệt`            | Nhiệt độ chip, không nên vượt quá 65°C.                                                                                                                                                                                   |
| Pwr           | Công Suất                                  | Công suất tiêu thụ tính bằng watt. Tuy nhiên, thông tin này không tính đến màn hình, quạt hoặc nguồn cung cấp điện. Ví dụ, khi nó hiển thị 11.7W, tổng mức tiêu thụ thực tế là 15.8W.                                   |
| mV mA         | Điện Áp Đầu Vào Dòng Điện Đầu Vào          | Điện áp và dòng điện tiêu thụ bởi máy. Công suất tính bằng watt bằng với điện áp nhân với dòng điện.                                                                                                                      |
| FH            | Bộ Nhớ Trống (menu bên trái -> `Nhật Ký`)   | Bộ nhớ khả dụng.                                                                                                                                                                                                          |
| vCore         | Điện Áp ASIC (trong hộp Hiệu Suất)         | Điện áp đo được trên chip ASIC.                                                                                                                                                                                           |
| IP            | NA                                          | Địa chỉ IP.                                                                                                                                                                                                               |
| V2.1.0        | Phiên Bản (menu bên trái -> `Nhật Ký`)      | Phiên bản firmware.                                                                                                                                                                                                       |

Bạn có thể thay đổi cài đặt Wi-Fi hoặc pool bất cứ lúc nào mà không gặp vấn đề gì.  
Tùy thuộc vào hệ thống thông gió và nhiệt độ của phòng bạn, bạn có thể cần phải tăng hoặc có thể phải giảm hiệu suất sao cho nhiệt độ không vượt quá 65°C. Nếu bạn tăng hiệu suất, bạn sẽ kiếm được nhiều satoshis hơn, nhưng BitAxe của bạn cũng sẽ tiêu thụ nhiều điện hơn!