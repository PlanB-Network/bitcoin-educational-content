---
name: Nakamochi
description: Chạy Node dễ dàng - Cách thiết lập và sử dụng node Nakamochi Bitcoin và Lightning.
---
Việc chạy full node Bitcoin và Lightning của riêng bạn không còn là một nhiệm vụ phức tạp chỉ dành cho các chuyên gia kỹ thuật nữa. Theo truyền thống, việc thiết lập và quản lý các node đòi hỏi kiến thức chuyên sâu về mật mã, mạng và phát triển phần mềm. Nakamochi thay đổi điều đó bằng cách làm cho các node có thể truy cập được với mọi người, bất kể trình độ kỹ thuật.

Với Nakamochi, bất kỳ ai cũng có thể thiết lập và vận hành một nút từ nhà, cho phép bảo mật hoàn toàn và độc lập về tài chính. Việc vận hành một nút đầy đủ không chỉ bảo mật các giao dịch của riêng bạn mà còn góp phần vào sức mạnh của mạng Bitcoin. Một mạng Bitcoin phi tập trung và bền bỉ dựa vào sự phân bổ rộng rãi các nút để đảm bảo tính bảo mật và độc lập của nó.

### Mục lục


- Nakamochi là gì và nó hoạt động như thế nào?
- Thiết lập Nakamochi
- Về Mạng lưới Lightning
- Mở kênh và thực hiện giao dịch trong Lightning Network

## Nakamochi là gì và nó hoạt động như thế nào?

Nakamochi là một full node chỉ dành cho Bitcoin hỗ trợ cả mạng lưới Bitcoin và Lightning. Nó bao gồm một ví Bitcoin và Lightning tích hợp, cho phép người dùng chạy một node Bitcoin an toàn, tự chủ trong khi vẫn được hưởng lợi từ tốc độ và chi phí giao dịch thấp của Lightning Network.

Nút Nakamochi của bạn được quản lý thông qua ứng dụng di động, [BitBanana (Android)](https://bitbanana.app) và [Zeus (iOS)](https://bitbanana.app), cho phép bạn điều khiển nút một cách thuận tiện từ bất kỳ đâu. Các ứng dụng này hoạt động như một bộ điều khiển từ xa cho nút của bạn, cho phép bạn thanh toán trực tiếp bằng Bitcoin hoặc Lightning, quản lý giao dịch, mở hoặc đóng kênh, kiểm tra số dư và theo dõi hiệu suất của nút, tất cả đều dễ dàng.

## Thiết lập Nakamochi chỉ mất 5 phút

### Bước 1: Cắm vào và bắt đầu

1. Kết nối Nakamochi với nguồn điện và Wi-Fi.

2. Nhấp vào **"Thiết lập ví mới"** và lưu trữ cụm từ khôi phục gồm 24 từ của bạn một cách an toàn.

3. Sử dụng ứng dụng quản lý nút (Zeus hoặc BitBanana) để kết nối với Nakamochi của bạn:

4. Mở ứng dụng và quét mã QR hiển thị trên Nakamochi của bạn.

5. Để tăng cường bảo mật, hãy đặt mã PIN trên thiết bị của bạn.

![image](assets/en/01.webp)

_Kết nối với nguồn điện và viết ra cụm từ hạt giống gồm 24 từ của bạn_

![image](assets/en/02.webp)

_Chờ cho đến khi Blockchain bắt kịp_

![image](assets/en/03.webp)

_Thiết lập ví mới trong Lightning Tab_

![image](assets/en/04.webp)

_Quét mã QR bằng ứng dụng Node Management_

![image](asset/en/05.webp)

_Để an toàn hơn, hãy đặt mã PIN_

**Lưu ý:** _Cho phép nút Nakamochi của bạn đồng bộ với blockchain. Quá trình này có thể mất một thời gian tùy thuộc vào kết nối internet của bạn._

## Về Mạng lưới Lightning

Bitcoin Lightning Network cách mạng hóa các giao dịch Bitcoin bằng cách làm cho chúng nhanh hơn, rẻ hơn và hiệu quả hơn. Nó hoàn hảo cho việc sử dụng hàng ngày, cho phép thanh toán gần như ngay lập tức với mức phí tối thiểu, lý tưởng cho các giao dịch nhỏ như mua cà phê hoặc xử lý các giao dịch mua nhỏ thường xuyên.

Bằng cách hoạt động ngoài chuỗi, Lightning được thiết kế để mở rộng quy mô, hỗ trợ hàng nghìn giao dịch mỗi giây mà không làm quá tải chuỗi khối Bitcoin chính. Điều này khiến nó trở thành một nhân tố chính trong quá trình phát triển của Bitcoin thành một hệ thống thanh toán toàn cầu thực tế.

Quyền riêng tư là một lợi thế khác, vì các giao dịch trên Lightning được định tuyến qua các kênh thanh toán riêng tư thay vì được ghi lại trực tiếp trên blockchain. Điều này đảm bảo một cách kín đáo hơn để giao dịch trong khi vẫn duy trì tính bảo mật mạnh mẽ của Bitcoin.

#### Giải thích về các kênh thanh toán

Lightning Network hoạt động thông qua các kênh thanh toán, là các kết nối giữa hai bên cho phép nhiều giao dịch mà không cần tương tác trực tiếp với blockchain. Khi một kênh mở, số dư giữa hai bên được cập nhật trên giải pháp Lightning lớp thứ hai này cho mọi giao dịch, đảm bảo thanh toán nhanh chóng, chi phí thấp. Chỉ có việc mở và đóng kênh được ghi lại trên chuỗi, giảm tình trạng tắc nghẽn trên blockchain Bitcoin. Thiết kế này đảm bảo khả năng mở rộng và quyền riêng tư, vì các giao dịch riêng lẻ vẫn không được ghi lại trên sổ cái công khai.

**Ví dụ:** Alice và Bob mở một kênh bằng cách cam kết Bitcoin vào đó. Alice gửi Bitcoin cho Bob và số dư ngoài chuỗi của họ được cập nhật ngay lập tức mà không cần hồ sơ trên chuỗi. Nếu sau đó Alice trả tiền cho Charlie và Alice không có kênh trực tiếp nào cho Charlie, khoản thanh toán có thể được định tuyến qua kênh của Bob để đến Charlie. Định tuyến qua các nút trung gian đảm bảo thanh toán ngay cả khi không có kết nối trực tiếp, giúp mạng lưới có hiệu quả cao.

## Mở kênh và thực hiện giao dịch trong Lightning Network

Sau khi Nakamochi của bạn được thiết lập và kết nối với ứng dụng quản lý nút, bạn có thể bắt đầu sử dụng Lightning Network bằng cách mở kênh và thực hiện giao dịch.

### Mở kênh trên Zeus (iOS):

1. Vào tab **“Kênh”** (menu phía dưới).

2. Nhấp vào **“+”** để mở kênh mới.

3. Quét hoặc nhập khóa công khai của nút mà bạn muốn kết nối.

4. Nhập số tiền bị khóa (chọn cùng với bạn bè hoặc sử dụng số tiền cố định tối thiểu cho các nút nổi tiếng).

5. Nhấp vào **“Mở kênh”**.

![image](asset/en/06.webp)

_Ảnh chụp màn hình ZEUS_

Để biết thêm thông tin: [Kênh | Tài liệu Zeus](https://docs.zeusln.app/)

### Mở kênh trên BitBanana (Android):

1. Mở menu hamburger (bên trái).

2. Vào mục **“Kênh”**.

3. Nhấp vào **“+”** để thêm/mở kênh mới.

4. Quét hoặc dán khóa công khai.

5. Nhập số tiền bị khóa (chọn cùng với bạn bè hoặc sử dụng số tiền cố định tối thiểu cho các nút nổi tiếng).

![image](asset/en/07.webp)

_Ảnh chụp màn hình Bitbanana_

Để biết thêm thông tin: [BitBanana](https://bitbanana.com)

Khi kênh của bạn mở, các khoản thanh toán có thể được định tuyến qua kênh đó đến những người tham gia khác trong mạng. Số dư được điều chỉnh ngoài chuỗi, đảm bảo giao dịch gần như ngay lập tức và chỉ phải trả phí tối thiểu.

Nếu bạn không còn cần kênh nữa, bạn có thể đóng kênh đó. Hành động này sẽ giải quyết số dư cuối cùng giữa bạn và đối tác của bạn và ghi lại trên chuỗi. Lý tưởng nhất là cả hai bên đều đồng ý và trực tuyến để "đóng hợp tác" (phí nhanh hơn và ít hơn so với "đóng bắt buộc" với đối tác không phản hồi/ngoại tuyến).

Nhìn chung, chúng tôi khuyên bạn nên để các kênh mở để giảm chi phí và tăng độ tin cậy cũng như hiệu quả của mạng. Bằng cách giữ các kênh mở, bạn giảm thiểu phí giao dịch trên chuỗi, tránh thời gian chết để kết nối lại kênh và duy trì khả năng định tuyến ổn định để xử lý thanh toán liền mạch. Cách tiếp cận này thúc đẩy mạng lưới mạnh mẽ và linh hoạt đồng thời nâng cao trải nghiệm người dùng tổng thể và giảm chi phí hoạt động.

### Liên kết hữu ích


- [Giới thiệu về Nakamochi](https://nakamochi.io/)
- [Đăng ký nhận Bản tin của Nakamochi](https://90c7addc.sibforms.com/serve/MUIFAHG7H5YBPpm-kZ8G6TuS-nmL4uaq85rlpBfI__S79tZ5jheIJfF3kJYudycgs_6_RUdDBkt8Sd7OyNL_JDTTJvOb36ifF6vcQoabBXKp4cbefzh1DYqnok_jItexICcQL13ucd2aS581ngqy7jr0Q1H3HhxV3z2eWKE5-Z-YMasj-MMotQeDvdorMCSi0XgCWDqs8rEMQC7E)