---
name: Breez điểm bán hàng

description: Hướng dẫn bắt đầu chấp nhận bitcoin sử dụng Breez POS
---

![cover](assets/cover.webp)

_Văn bản này đến từ trang web tài liệu của Breez: https://doc.breez.technology/How-to-Get-Started-with-Breez-POS.html_

## Breez POS là gì?

**Breez** là một ứng dụng Lightning không giữ tiền (non-custodial) đầy đủ dịch vụ. Hãy giải thích rõ hơn:

- **Lightning** là một mạng lưới thanh toán bitcoin giảm thời gian giao dịch từ vài phút xuống vài mili giây và phí giao dịch từ vài đô la xuống vài xu hoặc ít hơn. Lightning biến bitcoin từ vàng số thành tiền tệ số trong khi vẫn giữ nguyên tất cả lợi ích làm cho bitcoin trở nên tuyệt vời.
- **Không giữ tiền (Non-custodial)** có nghĩa là Breez không giữ tiền của người dùng. Nhiều ứng dụng Lightning giữ tiền của người dùng. Chúng thực chất là các ngân hàng bitcoin. Với một ứng dụng không giữ tiền như Breez, tất cả người dùng đều là ngân hàng của chính họ.
- **Đầy đủ dịch vụ** có nghĩa là Breez tự động và ngầm xử lý hầu hết các hoạt động kỹ thuật. Những việc như tạo kênh, tính thanh khoản đầu vào, và định tuyến được giữ kín. (Nhưng Breez cũng là mã nguồn mở, vì vậy những ai quan tâm đến việc kiểm tra công nghệ được chào đón!)

**Breez POS** là viết tắt của chế độ điểm bán hàng. Nói cách khác, Breez hoạt động như một máy tính tiền số cho các doanh nghiệp và thương nhân muốn chấp nhận thanh toán Lightning (bên cạnh chế độ "tiêu chuẩn" của nó, giống như phiên bản số của một ví da cho bitcoin, và một trình phát podcast thế hệ mới). Bây giờ, hãy xem cách thiết lập Breez như một máy tính tiền Lightning cho doanh nghiệp của bạn.

## Làm thế nào để bắt đầu với Breez?

1. Bước đầu tiên là tải xuống ứng dụng. Nó có sẵn cho Android và iOS (cài đặt TestFlight và nhấp vào liên kết từ thiết bị của bạn).
2. Breez có thể tự động sao lưu vào Google Drive, iCloud, hoặc bất kỳ máy chủ WebDav nào.
   > Lưu ý rằng mỗi thiết bị chạy node Lightning riêng của mình. Bạn có thể chạy chế độ POS trên nhiều thiết bị tùy thích, nhưng số dư sẽ được giữ riêng biệt.
3. Với ứng dụng mở, nhấp vào biểu tượng ở góc trên bên trái để tìm chế độ Điểm Bán Hàng.

## Thiết lập POS

1. Nhấp vào biểu tượng ở góc trên bên trái, và nhấp vào Điểm Bán Hàng > Cài Đặt POS.

### Mật khẩu Quản lý

Trong Cài Đặt POS, bạn có tùy chọn tạo một mật khẩu quản lý. Mật khẩu quản lý làm cho việc gửi thanh toán ra khỏi ứng dụng Breez không thể thực hiện mà không có sự ủy quyền. Nhân viên bán hàng chỉ có thể nhận thanh toán từ thiết bị. Lưu ý rằng nếu bạn sử dụng tùy chọn này, bạn cũng có thể muốn ngăn chặn truy cập vào sao lưu của Breez, vì vậy sử dụng một tài khoản WebDav bên ngoài (ví dụ, Nextcloud) được khuyến khích cho trường hợp sử dụng này.

### Danh Sách Mặt Hàng

Danh sách mặt hàng là một danh mục các mặt hàng bán và giá của chúng. Có hai cách để thêm mặt hàng vào danh sách:

- Để nhập từng mặt hàng một, nhấp vào Mặt Hàng gần đầu của giao diện POS chính, sau đó nhấp vào dấu "+" ở góc dưới bên phải. Tại đây bạn có thể nhập tên của một loại mặt hàng duy nhất, giá (hiển thị theo đơn vị tiền tệ tùy chọn của bạn), và SKU (một định danh nội bộ duy nhất cho loại mặt hàng đó; nó là tùy chọn).
- Để nhập nhiều mặt hàng cùng một lúc, nhấp vào biểu tượng máy tính ở góc trên bên trái, sau đó chọn Point of Sale > Preferences > POS Settings, tiếp theo nhấp vào ba chấm ở bên phải của Items List, và sau đó chọn Import from CSV. Điều này sẽ cho phép bạn nhập một tệp CSV mà bạn đã chuẩn bị trước đó chứa tên, giá và SKU của các mặt hàng.

### Hiển Thị Fiat

Breez chỉ gửi và nhận bitcoin, và đối với hầu hết các giao dịch trên Lightning, thường là với số lượng nhỏ, tổng số thường được hiển thị bằng Satoshis, còn được gọi là sats (1 BTC = 100,000,000 sats). Tuy nhiên, nhiều người bán hàng thấy rằng việc có thể thấy (và thông báo cho khách hàng) giá trị của giao dịch được hiển thị bằng tiền tệ fiat địa phương là thực tế.

Trong giao diện POS chính, tiền tệ đang được hiển thị có thể thấy ở phía bên phải (mặc định là SAT). Cũng có một danh sách thả xuống của các tiền tệ khác có sẵn để hiển thị. Để thêm hoặc loại bỏ các tiền tệ khỏi danh sách thả xuống này, nhấp vào Point of Sale > Preferences > Fiat Currencies. Sau đó chỉ cần đánh dấu vào các tiền tệ bạn muốn có trong menu thả xuống và bỏ đánh dấu những tiền tệ bạn muốn loại bỏ.

Giá trị được hiển thị là từ yadio, một nguồn tin cậy về dữ liệu tỷ giá hối đoái, và chúng được cập nhật gần như thời gian thực. Nhưng nhớ rằng: bất kể giá trị tiền tệ nào đang được hiển thị, việc thanh toán vẫn là bằng bitcoin.

### Thanh Toán Đơn Hàng

Để tạo đơn hàng, hoặc là thêm mặt hàng từ danh sách mặt hàng hoặc chỉ cần nhập một số tiền vào bàn phím. Sau đó nhấp vào Charge ở phía trên cùng của giao diện POS chính. Bạn sẽ thấy một mã QR mà khách hàng có thể quét bằng ứng dụng Lightning của họ, mà bạn có thể chia sẻ trực tiếp từ một ứng dụng khác trên thiết bị của mình, hoặc bạn có thể sao chép và dán nếu cần.

Khi quét mã đó hoặc nhấp vào hóa đơn được chia sẻ/dán, khách hàng sẽ thấy hóa đơn trong ứng dụng Lightning của họ và có tùy chọn thanh toán ngay lập tức và giải quyết giao dịch.

Một khi bạn thấy hoạt ảnh Payment approved! trong ứng dụng Breez trên thiết bị của người bán, bạn có thể nhấp vào biểu tượng máy in để tạo hóa đơn cho khách hàng. Để sử dụng máy in hóa đơn trên Android, hãy thử sử dụng trình điều khiển này. Lưu ý rằng bạn cũng có thể in các giao dịch trước đó qua màn hình Transactions.

### Báo Cáo Doanh Số

Để xem báo cáo hàng ngày/tuần/tháng về doanh số bán hàng của bạn (cho mục đích kế toán hoặc khác), nhấp vào biểu tượng ở góc trên bên trái, sau đó nhấp vào Transactions. Nhấp vào biểu tượng Report để hiển thị báo cáo và biểu tượng Calendar để thay đổi khoảng thời gian đã chọn.

### Xuất Giao Dịch

Để xem danh sách các khoản thanh toán đã nhận trong Breez, nhấp vào biểu tượng ở góc trên bên trái, sau đó nhấp vào Transactions. Nhấp vào ba chấm ở phía trên bên phải, sau đó chọn Export để xuất danh sách các khoản thanh toán đến dưới dạng tệp CSV. Để hạn chế danh sách trong một khoảng thời gian nhất định, nhấp vào biểu tượng lịch để thiết lập khoảng thời gian.

### In Hóa Đơn

Để in hóa đơn bán hàng, nhấp vào biểu tượng máy in ở phía trên bên phải của hộp thoại xác nhận thanh toán. Hoặc, nhấp vào biểu tượng ở góc trên bên trái, sau đó nhấp vào Transactions. Tìm giao dịch cần in, mở nó và nhấp vào biểu tượng máy in ở phía trên bên phải.

> Lưu ý: sử dụng trình điều khiển này để in trên máy in nhiệt di động 58mm/80mm Bluetooth/USB.

## Tôi muốn tìm hiểu thêm

- Để biết thêm thông tin về Lightning và Breez, hãy kiểm tra [blog](https://breez.technology/blog) của chúng tôi.
- Để biết thêm các mẹo kỹ thuật về cách tận dụng tối đa ứng dụng và thực hiện các thao tác phổ biến, hãy xem [tài liệu](https://breez.technology/documentation) của chúng tôi.
- Nếu bạn gặp khó khăn và không tìm thấy câu trả lời trong bất kỳ tài liệu hỗ trợ nào của chúng tôi, bạn có thể tìm chúng tôi trên [Telegram](https://t.me/breez_labs) hoặc gửi cho chúng tôi một [email](mailto:support@breez.technology).
- Nếu bạn muốn xem một số video minh họa về chế độ POS của Breez do người hâm mộ và người dùng của chúng tôi thực hiện, [đây](https://www.youtube.com/watch?v=xxxx) là một video ngắn tuyệt vời, và [đây](https://www.youtube.com/watch?v=xxxx) là một video dài hơn, chi tiết hơn.