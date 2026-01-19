---
name: BIP47 - PayNym
description: Sử dụng mã thanh toán có thể tái sử dụng trên Ashigaru
---
![cover](assets/cover.webp)



Sai lầm về quyền riêng tư tồi tệ nhất bạn có thể mắc phải trên Bitcoin là sử dụng lại địa chỉ. Mỗi khi cùng một địa chỉ nhận được nhiều khoản thanh toán, các giao dịch này sẽ được liên kết với nhau, cung cấp cho thế giới một bản đồ về các giao dịch của bạn. Do đó, chúng tôi đặc biệt khuyến nghị bạn luôn sử dụng generate một địa chỉ duy nhất cho mỗi biên lai. Tuy nhiên, đối với một số ứng dụng Bitcoin, đây không phải là vấn đề đơn giản.



BIP47, được Justus Ranvier đề xuất vào năm 2015, cung cấp một giải pháp tinh tế cho vấn đề này. Nó giới thiệu khái niệm về **mã thanh toán có thể tái sử dụng**: một mã định danh duy nhất cho phép nhận số lượng thanh toán bitcoin trên chuỗi gần như không giới hạn mà không cần sử dụng lại địa chỉ. Nhờ cơ chế mã hóa dựa trên trao đổi ECDH (*Diffie-Hellman trên đường cong elliptic*), mỗi khoản thanh toán cho cùng một mã sẽ tạo ra một địa chỉ trống, cụ thể cho mối quan hệ giữa người gửi và người nhận.



![Image](assets/fr/01.webp)



Nguyên tắc BIP47 này được triển khai cụ thể bởi **PayNym**, hệ thống ban đầu được phát triển bởi Samourai Wallet và hiện được Ashigaru tiếp quản. Trong hướng dẫn này, chúng ta sẽ xem xét cách kích hoạt PayNym, trao đổi mã thanh toán với đối tác và thực hiện giao dịch mà không cần sử dụng lại địa chỉ.



Tôi sẽ không đi sâu vào hoạt động chi tiết của BIP47 ở đây. Nếu bạn muốn tìm hiểu sâu hơn về chủ đề này, vui lòng tham khảo chương 6.6 của khóa đào tạo BTC 204 của tôi.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Điều kiện tiên quyết



Để làm theo hướng dẫn này, tất cả những gì bạn cần là wallet trên ứng dụng Ashigaru. Nếu bạn chưa biết cách tải xuống, xác minh, cài đặt ứng dụng hoặc tạo wallet, tôi khuyên bạn nên tham khảo hướng dẫn này trước:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

## Yêu cầu PayNym



Bước đầu tiên là yêu cầu PayNym của bạn. Thao tác này chỉ cần thực hiện một lần cho mỗi wallet. Nó sẽ liên kết mã thanh toán BIP47 của bạn được lấy từ seed (`PM...`) với một mã định danh duy nhất dành riêng cho việc triển khai PayNym. Mã định danh ngắn gọn và dễ đọc này sau đó có thể được gửi đến các đối tác liên lạc của bạn để tạo điều kiện thuận lợi cho việc trao đổi mà không cần phải chia sẻ mã BIP47 dài dòng và đầy đủ.



Để thực hiện, hãy nhấp vào hình ảnh PayNym của bạn ở góc trên bên trái của giao diện, sau đó nhấp vào mã thanh toán `PM...`.



![Image](assets/fr/02.webp)



Sau đó nhấp vào ba dấu chấm nhỏ ở góc trên bên phải và chọn `Yêu cầu PayNym`.



![Image](assets/fr/03.webp)



Xác nhận bằng cách nhấp vào nút `NHẬN PAYNYM`.



![Image](assets/fr/04.webp)



Làm mới trang: ID PayNym của bạn hiện được hiển thị bên dưới ảnh, ngay phía trên mã thanh toán BIP47.



![Image](assets/fr/05.webp)



PayNym của bạn hiện đã hoạt động và sẵn sàng để sử dụng cho các giao dịch BIP47 đầu tiên.



## Kết nối với một liên hệ



Có hai loại kết nối giữa PayNym: **follow** và **connect**. Thao tác `follow` hoàn toàn miễn phí. Nó thiết lập một liên kết giữa hai PayNym thông qua Soroban, một giao thức truyền thông được mã hóa dựa trên Tor do nhóm Samourai phát triển và Ashigaru áp dụng. Liên kết này cho phép hai người dùng theo dõi nhau trao đổi thông tin riêng tư, đặc biệt là để phối hợp các giao dịch hợp tác như Stowaway hoặc StonewallX2, mà chúng ta sẽ xem xét trong một hướng dẫn khác. Bước này dành riêng cho PayNym và không phải là một phần của giao thức BIP47.



![Image](assets/fr/06.webp)



Mặt khác, thao tác kết nối (`connect`) yêu cầu giao dịch on-chain. Giao dịch này bao gồm việc thực hiện một giao dịch thông báo như được định nghĩa trong BIP47. Giao dịch Bitcoin này chứa siêu dữ liệu trong đầu ra `OP_RETURN`, thiết lập một kênh giao tiếp được mã hóa giữa người trả tiền và người nhận. Từ kênh này, người trả tiền sẽ có thể generate các địa chỉ nhận duy nhất cho mỗi khoản thanh toán, và người nhận sẽ được thông báo về các khoản thanh toán này, đồng thời có thể generate các khóa riêng được liên kết với các địa chỉ này để chi tiêu số tiền này sau.



Giao dịch thông báo này có chi phí: phí mining và 546 sats được gửi đến địa chỉ thông báo của người nhận để báo hiệu kết nối. Sau khi kết nối được thiết lập, gần như vô số khoản thanh toán có thể được thực hiện thông qua BIP47.



Nói tóm lại:




- "follow": miễn phí, thiết lập giao tiếp được mã hóa thông qua Soroban, hữu ích cho các công cụ cộng tác của Ashigaru;
- `Kết nối`: có thể tính phí, thực hiện giao dịch thông báo BIP47 để kích hoạt kênh giữa người trả tiền và người nhận.



Để tương tác với PayNym, trước tiên bạn phải *theo dõi* PayNym. Đây là bước đầu tiên trước khi thiết lập kết nối BIP47. Giả sử bạn muốn gửi thanh toán định kỳ đến PayNym `+instinctiveoffer10`.



Truy cập trang PayNym của bạn trên Ashigaru, sau đó nhấp vào nút `+` ở góc dưới bên phải của giao diện.



![Image](assets/fr/07.webp)



Sau đó, bạn có thể dán mã thanh toán đầy đủ của người nhận hoặc quét mã QR của họ.



![Image](assets/fr/08.webp)



Nếu bạn chỉ có ID PayNym của anh ấy, hãy truy cập [Paynym.rs](https://paynym.rs/) để tìm mã QR liên kết với mã thanh toán của anh ấy.



![Image](assets/fr/09.webp)



Sau khi quét mã QR, hãy nhấp vào nút `THEO DÕI` để theo dõi PayNym.



![Image](assets/fr/10.webp)



Thao tác `FOLLOW` đủ cho các giao dịch hợp tác (*cahoots*). Tuy nhiên, để gửi thanh toán BIP47, bạn cần thiết lập kết nối: nhấp vào `CONNECT` để thực hiện giao dịch thông báo.



![Image](assets/fr/11.webp)



Giao dịch thông báo sau đó sẽ được phát trên mạng. Hãy đợi cho đến khi có ít nhất một xác nhận trước khi thực hiện khoản thanh toán đầu tiên.



![Image](assets/fr/12.webp)



## Thực hiện thanh toán BIP47



Bây giờ bạn đã kết nối với người nhận và có thể gửi thanh toán đến một địa chỉ duy nhất, được tạo tự động bằng giao thức BIP47, mà không cần trao đổi trước với người nhận.



Từ trang chính PayNym, hãy nhấp vào địa chỉ liên hệ mà bạn muốn gửi thanh toán.



![Image](assets/fr/13.webp)



Ở góc trên bên phải của giao diện, nhấp vào biểu tượng mũi tên.



![Image](assets/fr/14.webp)



Nhập số tiền cần gửi. Bạn không cần nhập địa chỉ nhận: địa chỉ sẽ tự động được lấy bằng giao thức BIP47.



![Image](assets/fr/15.webp)



Kiểm tra cẩn thận các chi tiết giao dịch, bao gồm cả phí, sau đó kéo mũi tên màu xanh lá cây ở cuối màn hình để ký và phát giao dịch.



![Image](assets/fr/16.webp)



Giao dịch đã được gửi.



![Image](assets/fr/17.webp)



Trong ví dụ này, khoản thanh toán đã được thực hiện vào một ví PayNym khác của tôi. Do đó, tôi có thể thấy rằng khoản thanh toán đã đến ví Ashigaru wallet khác của tôi mà không cần bất kỳ địa chỉ nào được trao đổi thủ công: chỉ sử dụng mã định danh PayNym.



![Image](assets/fr/18.webp)



Giờ đây, bạn đã biết cách sử dụng mã thanh toán BIP47 tái sử dụng nhờ việc triển khai PayNym trên ứng dụng Ashigaru. Bạn có thể chia sẻ mã thanh toán này với bất kỳ ai muốn gửi tiền cho bạn (đặc biệt là các khoản thanh toán định kỳ). Bạn cũng có thể đăng ID PayNym của mình lên trang web hoặc mạng xã hội để nhận quyên góp.



Để hiểu sâu hơn về giao thức này, hiểu chi tiết về cách thức hoạt động và ý nghĩa của nó đối với tính bảo mật, tôi thực sự khuyên bạn nên tham gia khóa học BTC 204 của tôi:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c