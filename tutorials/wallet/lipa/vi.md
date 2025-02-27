---
name: Môi
description: Thiết lập và sử dụng ví di động Lipa Lightning
---
![cover](assets/cover.webp)

Ví Bitcoin Lightning là ứng dụng di động cho phép giao dịch tức thời, chi phí thấp trên mạng lưới Lightning của Bitcoin. Không giống như giao dịch trên blockchain chính (trên chuỗi), thanh toán Lightning gần như tức thời và chỉ yêu cầu mức phí tối thiểu, khiến chúng đặc biệt phù hợp với các khoản thanh toán nhỏ, hàng ngày.

Ví Lightning, giống như tất cả các ví di động, được coi là ví "nóng" vì chúng được kết nối với Internet. Do đó, chúng chủ yếu dùng để quản lý số tiền nhỏ cho chi tiêu hàng ngày của bạn. Đối với số tiền lớn hơn, tốt hơn là sử dụng các giải pháp lưu trữ an toàn hơn như ví phần cứng.

Nếu bạn muốn tìm hiểu thêm về mạng Lightning và hiểu cách thức hoạt động về mặt kỹ thuật của nó, tôi khuyên bạn nên tham gia khóa học này:

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
Trong hướng dẫn này, chúng ta sẽ xem xét **Lipa**, một ví Lightning đơn giản và hiệu quả được phát triển tại Thụy Sĩ.

## Giới thiệu Lipa

Lipa là ví Lightning không lưu ký, nổi bật với tính đơn giản khi sử dụng và giao diện gọn gàng. Được phát triển bởi một nhóm Thụy Sĩ, nó nhấn mạnh tính bảo mật và dễ sử dụng cho người mới bắt đầu.

Các tính năng chính bao gồm:


- Giao diện người dùng trực quan
- Quản lý kênh Lightning tự động
- Hỗ trợ giao thức LNURL
- Khả năng mua bitcoin trực tiếp trong ứng dụng

## Cài đặt và cấu hình Lipa

Bước đầu tiên là tải xuống ứng dụng Lipa. Hiện tại, ứng dụng này chỉ khả dụng trên iOS:


- [Dành cho Apple](https://apps.apple.com/app/lipa-bitcoin-lightning/id1602180066)

Phiên bản Android hiện đang được phát triển và sẽ sớm ra mắt.

![Installation de Lipa](assets/fr/01.webp)

Sau khi khởi chạy ứng dụng, bạn sẽ đến màn hình chính với hai tùy chọn:


- Tạo danh mục đầu tư mới
- Khôi phục danh mục đầu tư hiện có từ bản sao lưu

Sau khi bạn đã chọn tùy chọn của mình, ứng dụng sẽ nhắc bạn bật thông báo. Bước này rất quan trọng vì thông báo là cần thiết cho:


- Nhận thông báo khi nhận được thanh toán, ngay cả khi ứng dụng đã đóng
- Được thông báo về các bước liên quan đến việc mua bitcoin thông qua giải pháp tích hợp của họ

Sau đó, ứng dụng sẽ trình bày các chức năng chính thông qua một loạt màn hình giới thiệu:


- Biên lai thanh toán liền mạch**: Người dùng có thể nhận thanh toán bằng Bitcoin ngay cả khi ứng dụng đã đóng, đảm bảo độ tin cậy và tiện lợi.
- Địa chỉ Lightning không lưu ký**: Lipa hiện hỗ trợ các địa chỉ Lightning không lưu ký, tăng cường quyền riêng tư và bảo mật bằng cách trao cho người dùng quyền kiểm soát hoàn toàn đối với bitcoin của họ.
- Kiểm soát dữ liệu phân tích**: Với tính minh bạch và bảo mật tối quan trọng, người dùng có thể xem các loại dữ liệu được thu thập và chọn tùy chọn chia sẻ của họ.
- Gửi qua số điện thoại**: Không cần địa chỉ phức tạp - chỉ cần chọn một số liên lạc, nhập số tiền và gửi bitcoin trực tiếp đến số điện thoại của họ.

Ứng dụng này cũng được cải tiến liên tục về tính ổn định, bảo mật và độ tin cậy để đảm bảo trải nghiệm tối ưu cho người dùng.

## Điều hướng ứng dụng

Giao diện của Lipa được tổ chức xung quanh 4 tab chính có thể truy cập thông qua thanh điều hướng ở cuối màn hình:

![Navigation principale](assets/fr/02.webp)


- Trang chủ**: Hiển thị số dư hiện tại và lịch sử giao dịch của bạn
- Máy quét**: Cho phép bạn quét mã QR để thanh toán
- Bản đồ**: Hiển thị bản đồ tương tác của các doanh nghiệp chấp nhận Bitcoin trong khu vực của bạn
- Cài đặt**: Truy cập vào cài đặt ứng dụng, sao lưu và tùy chọn

Có thể truy cập menu bổ sung bằng cách kéo xuống màn hình chính:

![Menu supplémentaire](assets/fr/03.webp)

Cử chỉ này cho thấy các chức năng bổ sung như:


- Mua bitcoin
- Tiền gửi bitcoin trên chuỗi
- Tạo hóa đơn Lightning để nhận bitcoin
- Thanh toán hóa đơn sét

## Lưu danh mục đầu tư của bạn

Để sao lưu ví của bạn, hãy vào tab "Cài đặt" và chọn "Cụm từ khôi phục". Lipa sử dụng một cụm từ khôi phục mà bạn cần phải viết cẩn thận trên một phương tiện vật lý (giấy, kim loại). Cụm từ này là cách duy nhất để khôi phục tiền của bạn nếu điện thoại của bạn bị mất hoặc bị đánh cắp. Để xác thực bản sao lưu của bạn, ứng dụng sẽ yêu cầu bạn xác nhận 3 từ ngẫu nhiên trong cụm từ của bạn.

![Backup](assets/fr/04.webp)

Để biết thêm thông tin về cách sao lưu và quản lý cụm từ khôi phục đúng cách, tôi thực sự khuyên bạn nên làm theo hướng dẫn khác này, đặc biệt nếu bạn là người mới bắt đầu:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270
## Nhận bitcoin

Để nhận bitcoin, bạn có hai lựa chọn. Để truy cập các tùy chọn này, hãy quay lại màn hình chính và kéo màn hình xuống. Sau đó, bạn có thể:


- Chọn "Chuyển BTC" để nhận bitcoin trên chuỗi. Sau đó chỉ cần quét mã QR bằng ví khác của bạn và hoàn tất giao dịch.
- Chọn "Yêu cầu" để nhận qua mạng Lightning và nhập số tiền bạn muốn nhận.

Trong cả hai trường hợp, bạn sẽ phải trả một khoản phí tương đương 0,4% số tiền hoặc khoảng 2.500 sats nếu ứng dụng phải mở một kênh thanh toán mới (điều này chắc chắn sẽ xảy ra đối với lần thanh toán đầu tiên).

![Recevoir des bitcoins on chain](assets/fr/05.webp)

![Recevoir des bitcoins lightning](assets/fr/06.webp)

## Gửi bitcoin

Để gửi bitcoin, hãy vào màn hình chính, kéo xuống màn hình và chọn "Thanh toán". Sau đó chỉ cần thực hiện một trong hai cách sau:


- nhập địa chỉ LNURL sét
- quét mã QR dạng tia sét để thực hiện thanh toán.

Bạn cũng có thể vào tab thứ hai ở cuối màn hình để quét mã QR trực tiếp.

![Envoi de bitcoins](assets/fr/07.webp)

## Mua bitcoin

Lipa cung cấp khả năng mua bitcoin trực tiếp trong ứng dụng với mức phí là 1,5%. Để mua, hãy vào màn hình chính và kéo xuống để hiển thị menu. Sau đó chọn "Mua BTC". Ba màn hình giới thiệu sẽ hướng dẫn bạn qua quy trình mua.

![Menu d'achat](assets/fr/08.webp)

Sau đó chỉ cần nhập thông tin chi tiết về ngân hàng của tài khoản bạn sẽ sử dụng để mua hàng. Chọn loại tiền tệ và nhập địa chỉ email của bạn.

Sau màn hình tải, bạn sẽ tìm thấy số tham chiếu được bao gồm trong giao dịch chuyển tiền mà bạn sắp thực hiện, cũng như thông tin chi tiết về ngân hàng để trao đổi.

![Sélection du montant](assets/fr/09.webp)

Tất cả những gì bạn phải làm là sử dụng ngân hàng của mình để chuyển số tiền mong muốn, thiết lập giao dịch bằng cách chỉ định RIB đã lấy trước đó và chỉ định tham chiếu tại thời điểm giao dịch để Lipa có thể liên kết chuyển khoản ngân hàng này với ví Lipa của bạn.

![Confirmation d'achat](assets/fr/10.webp)

## Ưu điểm và nhược điểm

### Những lợi ích


- Giao diện trực quan
- Phí dịch vụ chính xác
- Không giam giữ
- Giải pháp mua bitcoin tích hợp
- Tích hợp BTCmap
- Hỗ trợ NFC

### Nhược điểm


- Không thể gửi bitcoin trên chuỗi
- Thanh toán dài hơn một chút so với mức trung bình

Lipa là lựa chọn tuyệt vời để bắt đầu với Lightning Network, đặc biệt phù hợp với người dùng đang tìm kiếm giải pháp đơn giản cho các khoản thanh toán hàng ngày. Tính dễ sử dụng và giao diện gọn gàng khiến nó trở thành ví lý tưởng cho người mới bắt đầu, đồng thời cung cấp các tính năng thiết yếu để sử dụng Lightning hàng ngày.

## Tài nguyên


- [Trang web chính thức của Lipa](https://lipa.swiss/)
- [Hỗ trợ Lipa](https://getlipa.atlassian.net/servicedesk/customer/portal/1)