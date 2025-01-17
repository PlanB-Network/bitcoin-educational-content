---
name: Seed Signer

description: Thiết lập Seed signer của bạn
---

![cover](assets/cover.webp)

## Vật liệu:

1. Raspberry Pi Zero (phiên bản 1.3)

Raspberry Pi Zero

Để có một giải pháp hoàn toàn không kết nối (air-gapped), hãy chắc chắn sử dụng phiên bản 1.3 không có khả năng WiFi hoặc Bluetooth, nhưng bất kỳ mô hình Raspberry Pi 2/3/4 hoặc Zero nào cũng sẽ hoạt động.

Lưu ý: Raspberry Pi thường không đi kèm với các chân gắn sẵn; bạn cần phải hàn chân vào, hoặc có thể sử dụng cái gọi là “GPIO Hammer”.
GPIO Hammer

Nếu kỹ năng hàn của bạn không thực sự tốt, hoặc bạn chưa sở hữu một cây hàn, thì bạn có thể sử dụng “GPIO Hammer” như một phương án thay thế cho việc hàn.

2. Mũ LCD WaveShare 1,3 inch với màn hình 240×240 pixel

WaveShare LCD Hat

Waveshare 1.3″ 240×240 pxl LCD

Lưu ý: Chọn màn hình Waveshare cẩn thận; hãy chắc chắn mua mô hình có độ phân giải 240×240 pixel.
thêm thông tin

3. Mô-đun camera tương thích với Pi Zero

Raspberry Pi Camera

Aokin / AuviPal 5MP 1080p với cảm biến OV5647 Video Camera Module; các thương hiệu khác với mô-đun cảm biến OV5647 cũng nên hoạt động, nhưng có thể không tương thích với vỏ Orange Pill.

Lưu ý: Bạn sẽ cần có một cáp ribbon camera cụ thể tương thích với Raspberry Pi Zero.

4. Thẻ MicroSD với ít nhất 4 GB dung lượng

nguồn tài nguyên rộng lớn: https://seedsigner.com/explainers/

## Phần mềm:

Cài đặt Phần mềm

1. Tải xuống tệp “seedsigner_x_x_x.img.zip” mới nhất
   phiên bản mới nhất

2. Giải nén tệp “seedsigner_x_x_x.img.zip”

3. Sử dụng Balena Etcher hoặc công cụ tương tự để ghi tệp hình ảnh .img đã giải nén vào thẻ microsd
   BALENA ETCHER

4. Cài đặt thẻ microsd vào SeedSigner.
   Khóa công khai GPG của SeedSigner
   seedsigner_pubkey.gpg

## Hướng dẫn video

_hướng dẫn được lấy từ Southerbitcoiner, tạo bởi Cole_

### Một loạt các hướng dẫn video về SeedSigner: một thiết bị Ví Phần cứng/Máy ký mã nguồn mở, DIY

![image](assets/1.webp)

SeedSigner là một Thiết bị Ký Bitcoin mà bạn có thể tự xây dựng từ đầu. Nghe có vẻ khó, nhưng loạt 4 phần này sẽ giúp bạn :) Tôi đề xuất bạn xem phần 1 và 2, sau đó quyết định liệu bạn muốn sử dụng máy tính để bàn (xem phần 3) hay thiết bị di động (xem phần 4).

Mọi thứ bạn cần biết sẽ ở dưới đây. Các liên kết hữu ích khác bao gồm trang web của SeedSigner, Github của họ, Keybase của họ, phiên bản mới nhất, và yêu cầu về phần cứng.

### Phần 1: Cách xây dựng một SeedSigner:

Trong video này, tôi sẽ hướng dẫn bạn cách tải xuống và xác minh phần mềm SeedSigner, những bộ phận cần thiết, và cách lắp ráp SeedSigner của bạn.

![video](https://youtu.be/mGmNKYOXtxY)

### Phần 2: Kiểm tra SeedSigner của bạn
Trước khi tôi sử dụng SeedSigner của mình, tôi đã thực hiện một số bài kiểm tra để đảm bảo rằng nó không thực hiện bất kỳ hành động độc hại nào. Tôi nghĩ mình sẽ chia sẻ bước này nữa. Dưới đây là cách để xác minh SeedSigner xuất ví đúng (xpub), cách xác minh toán học của lần lắc xúc xắc của SeedSigner, và cách xác minh hạt giống con bip-85 của SeedSigner.
![video](https://youtu.be/34W1IyTyXZE)

### Phần 3: Cách sử dụng SeedSigner với Sparrow Wallet (desktop)

SeedSigner có khả năng tạo hạt giống và ký xác nhận các giao dịch bitcoin. Nhưng bằng chính nó, nó không có khả năng tạo giao dịch. Bạn cần sử dụng một "điều phối viên" ví với SeedSigner của mình. Đây là cách sử dụng Sparrow Wallet với SeedSigner của bạn:

![video](https://youtu.be/IQb8dh-VTOg)

Phần 4: Cách sử dụng SeedSigner với Blue Wallet (di động)

SeedSigner có khả năng tạo hạt giống và ký xác nhận các giao dịch bitcoin. Nhưng bằng chính nó, nó không có khả năng tạo giao dịch. Bạn cần sử dụng một "điều phối viên" ví với SeedSigner của mình. Đây là cách sử dụng Blue Wallet với SeedSigner của bạn:

![video](https://youtu.be/x0Ee35Ct0r4)

Đó là tất cả các hướng dẫn về SeedSigner, cho đến bây giờ! Hãy cho tôi biết nếu bạn nghĩ tôi đang thiếu điều gì. Đây là những gì tôi đã liệt kê cho các video tiềm năng:

> Đánh giá tổng quan về SeedSigner. Liệu đó có phải là lựa chọn tốt cho một thiết bị ký? Ưu/nhược điểm?

> Cách sử dụng Bip-85 với SeedSigner
> Làm thế nào để trở thành chú Jim với SeedSigner

Bạn thấy những thông tin này hữu ích? Hãy xem xét gửi một khoản tiền tip để giúp tài trợ cho các video tương lai:
https://www.southernbitcoiner.com/donate/