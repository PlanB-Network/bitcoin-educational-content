---
name: Tails

description: Cài đặt Tails trên một chiếc USB
---

![image](assets/cover.webp)

Một hệ điều hành di động và quên đi sau khi sử dụng, bảo vệ bạn khỏi sự giám sát và kiểm duyệt.

## Tại sao cần có một chiếc USB đã cài đặt Tails?

Tails (https://tails.net/) là cách dễ nhất để bạn luôn có một máy tính an toàn bên mình, không để lại bất kỳ dấu vết nào trên máy tính mà bạn sử dụng.

Để sử dụng Tails, tắt máy tính mà bạn có quyền truy cập (tại nhà của bố mẹ, nhà bạn bè, tại quán Internet...) và khởi động nó với chiếc USB Tails của bạn thay vì Windows, macOS, hoặc Linux.

Sau đó, bạn sẽ có một môi trường làm việc và giao tiếp độc lập với hệ điều hành thông thường và không bao giờ sử dụng ổ cứng.

Tails không bao giờ ghi vào ổ cứng và chỉ sử dụng RAM của máy tính để hoạt động. Bộ nhớ này được xóa hoàn toàn khi Tails được tắt, do đó loại bỏ mọi dấu vết có thể có.

## Một số trường hợp sử dụng cụ thể

Để cho bạn những ý tưởng cụ thể về lợi ích của việc luôn có một chiếc USB với Tails, dưới đây là một danh sách không đầy đủ được biên soạn bởi đội ngũ Agora256:

- Kết nối Internet và Tor một cách không bị kiểm duyệt và ẩn danh để duyệt web mà không để lại dấu vết;
- Mở một PDF từ một trang web đáng ngờ;
- Kiểm tra bản sao lưu khóa riêng tư Bitcoin của bạn với ví Electrum;
- Sử dụng bộ ứng dụng văn phòng (LibreOffice) và làm việc trên một máy tính không thuộc về bạn;
- Bắt đầu những bước đầu tiên trong môi trường Linux để học cách rời bỏ thế giới của Microsoft và Apple.

## Làm thế nào để tin tưởng Tails?

Luôn có một yếu tố tin tưởng khi sử dụng phần mềm, nhưng không cần phải mù quáng. Một công cụ như Tails phải cố gắng cung cấp cho người dùng của mình các phương tiện để đáng tin cậy. Đối với Tails, điều này có nghĩa là:

- Mã nguồn công khai: https://gitlab.tails.boum.org/;
- Một dự án dựa trên các dự án uy tín: Tor và Debian;
- Tải về có thể kiểm chứng và tái tạo;
- Được khuyến nghị bởi các cá nhân và tổ chức khác nhau.

## Hướng dẫn cài đặt và sử dụng

Mục đích của hướng dẫn cài đặt này là hướng dẫn bạn qua từng bước của quá trình cài đặt. Chúng tôi sẽ không mô tả các hành động cần thực hiện nhiều hơn so với hướng dẫn chính thức, nhưng chúng tôi sẽ chỉ cho bạn hướng đi đúng đắn trong khi cung cấp cho bạn mẹo và thủ thuật.

Vì lý do kinh nghiệm thực tế, những mẹo này sẽ tập trung vào các nền tảng macOS và Linux.
🛠️
Trước khi bắt đầu quy trình này, vui lòng đảm bảo bạn có một chiếc USB với tốc độ đọc tối thiểu 150 MB/s và dung lượng ít nhất 8 GB, lý tưởng là USB 3.0.

Yêu cầu:

- 1 chiếc USB, chỉ dành cho Tails, với dung lượng ít nhất 8 GB
- Một máy tính kết nối Internet với Linux, macOS, (hoặc Windows)
- Khoảng một giờ thời gian rảnh, tùy thuộc vào tốc độ kết nối Internet của bạn, bao gồm ½ giờ cho việc cài đặt (tải xuống tệp 1.3 GB)

## Bước 1: Tải xuống Tails từ máy tính của bạn

![image](assets/1.webp)

> 🔗 Mục chính thức của Tails: https://tails.net/install/linux/index.fr.html#download

Việc tải xuống tệp cài đặt với phần mở rộng .img có thể mất một thời gian tùy thuộc vào tốc độ tải xuống Internet của bạn, vì vậy hãy lên kế hoạch trước. Với một kết nối hiện đại và hiệu quả, việc này sẽ mất ít hơn 5 phút.

Lưu tệp vào một thư mục đã biết, chẳng hạn như Downloads, vì điều này sẽ cần thiết cho bước tiếp theo.

## Bước 2: Xác minh tải xuống của bạn

![image](assets/2.webp)
🔗 Mục chính thức của Tails: https://tails.net/install/linux/index.fr.html#verify
Xác minh việc tải xuống đảm bảo rằng nó được phát hành bởi các nhà phát triển Tails và không bị hỏng hoặc bị chặn trong quá trình tải xuống.

Có thể tự mình xác minh rằng tệp bạn vừa tải xuống là tệp mong đợi sử dụng PGP, nhưng nếu không có kiến thức nâng cao, việc xác minh này cung cấp cùng một mức độ bảo mật như việc xác minh JavaScript trên trang tải xuống, trong khi đó lại phức tạp và dễ mắc lỗi hơn nhiều.

Để xác minh tệp, hãy sử dụng nút "Chọn tải xuống của bạn..." được cung cấp trong mục chính thức!

## Bước 3: Cài đặt Tails trên USB của bạn

![hình ảnh](assets/3.webp)

> 🔗 Mục chính thức của Tails:
>
> - Linux: https://tails.net/install/linux/index.fr.html#install
> - macOS: https://tails.net/install/mac/index.fr.html#etcher và https://tails.net/install/mac/index.fr.html#install

Bước này của việc cài đặt Tails trên USB của bạn là khó khăn nhất trong toàn bộ hướng dẫn, đặc biệt nếu bạn chưa bao giờ thực hiện nó trước đây. Điểm quan trọng nhất là chọn đúng quy trình trong mục chính thức cho hệ điều hành của bạn: Linux hoặc macOS.

Một khi các công cụ đã được cài đặt và chuẩn bị theo khuyến nghị, tệp có phần mở rộng .img có thể được sao chép vào USB của bạn (xóa tất cả dữ liệu hiện có) để làm cho nó có thể "khởi động" độc lập.

Chúc may mắn! và hẹn gặp lại ở bước 4.

## Bước 4: Khởi động từ USB Tails của bạn

![hình ảnh](assets/4.webp)

> 🔗 Mục chính thức của Tails: https://tails.net/install/linux/index.en.html#restart
> Đã đến lúc khởi động một trong những máy tính của bạn sử dụng USB mới của bạn. Cắm nó vào một trong các cổng USB và khởi động lại!

> 💡 Hầu hết máy tính không tự động khởi động từ USB Tails, nhưng bạn có thể nhấn phím menu khởi động để hiển thị danh sách các thiết bị có thể khởi động từ.

Để xác định phím nào bạn nên nhấn để đảm bảo rằng bạn có menu khởi động cho phép bạn chọn USB thay vì ổ cứng thông thường của mình, dưới đây là danh sách không đầy đủ theo nhà sản xuất:

| Nhà sản xuất | Phím              |
| ------------ | ---------------- |
| Acer         | F12, F9, F2, Esc |
| Apple        | Option           |
| Asus         | Esc              |
| Clevo        | F7               |
| Dell         | F12              |
| Fujitsu      | F12, Esc         |
| HP           | F9               |
| Huawei       | F12              |
| Intel        | F10              |
| Lenovo       | F12              |
| MSI          | F11              |
| Samsung      | Esc, F12, F2     |
| Sony         | F11, Esc, F10    |
| Toshiba      | F12              |
| khác...      | F12, Esc         |

Một khi USB được chọn, bạn sẽ thấy màn hình khởi động mới này, đó là một dấu hiệu rất tốt, vì vậy hãy để máy tính tiếp tục khởi động...

![hình ảnh](assets/5.webp)

## Bước 5: Chào mừng đến với Tails!

![hình ảnh](assets/6.webp)

> 🔗 Mục chính thức của Tails: https://tails.net/install/linux/index.en.html#tails

Một hoặc hai phút sau bộ nạp khởi động và màn hình tải, Màn hình Chào mừng xuất hiện.

![hình ảnh](assets/7.webp)

Trong Màn hình Chào mừng, chọn ngôn ngữ và bố cục bàn phím của bạn trong mục Ngôn ngữ & Khu vực. Nhấn vào Bắt đầu Tails.

![hình ảnh](assets/8.webp)
Nếu máy tính của bạn không được kết nối trực tiếp với mạng, vui lòng tham khảo hướng dẫn chính thức của Tails để giúp bạn kết nối với mạng mà không cần Wi-Fi (mục "Test your Wi-Fi").
Khi đã kết nối với mạng địa phương, trình hướng dẫn Kết nối Tor xuất hiện để giúp bạn kết nối với mạng Tor.

![image](assets/9.webp)

Bạn có thể bắt đầu duyệt web ẩn danh, khám phá các tùy chọn và phần mềm được bao gồm trong Tails. Hãy thưởng thức, bạn có nhiều không gian để mắc lỗi, vì không có gì được sửa đổi trên USB... Lần khởi động tiếp theo của bạn sẽ quên hết tất cả những trải nghiệm của bạn!

## Trong một hướng dẫn tương lai...

Sau khi bạn đã thử nghiệm một chút với USB Tails của riêng mình, chúng tôi sẽ khám phá các chủ đề nâng cao hơn trong một bài viết khác, như:

> Cập nhật một khóa với phiên bản mới nhất của Tails; Cấu hình và sử dụng bộ nhớ lưu trữ cố định; Cài đặt phần mềm bổ sung.
> Cho đến lúc đó, như mọi khi, nếu bạn có bất kỳ câu hỏi nào, đừng ngần ngại chia sẻ với cộng đồng Agora256. Chúng ta cùng nhau học hỏi để ngày mai tốt hơn hôm nay!