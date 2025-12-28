---
name: SMS4Sats
description: Nhận và gửi tin nhắn SMS ẩn danh bằng cách thanh toán bằng Bitcoin Lightning
---

![cover](assets/cover.webp)



Xác minh qua SMS đã trở thành điều bắt buộc đối với nhiều dịch vụ trực tuyến. Cho dù là để tạo tài khoản trên một nền tảng, xác thực đăng ký hay xác nhận danh tính, các trang web hầu như đều yêu cầu số điện thoại. Thực tiễn phổ biến này đặt ra một vấn đề lớn cho bất kỳ ai muốn bảo vệ quyền riêng tư của mình: số điện thoại cá nhân của bạn trở thành một mã định danh vĩnh viễn, liên kết các hoạt động kỹ thuật số khác nhau của bạn với danh tính thực và mở ra cánh cửa cho các lời mời chào thương mại không mong muốn.



**SMS4Sats** giải quyết vấn đề này bằng cách cung cấp các số điện thoại tạm thời để nhận và gửi tin nhắn SMS. Dịch vụ này nổi bật với mô hình không cần đăng ký và thanh toán độc quyền bằng Bitcoin thông qua Lightning Network. Chỉ với một vài satoshi, bạn sẽ nhận được một số điện thoại dùng một lần cho phép bạn xác thực đăng ký mà không cần tiết lộ số điện thoại cá nhân của mình.



Hướng dẫn này sẽ giới thiệu cho bạn ba tính năng của SMS4Sats: nhận tin nhắn SMS xác nhận, gửi tin nhắn SMS ẩn danh và thuê số điện thoại tạm thời trong vài giờ.



## SMS4Sats là gì?



SMS4Sats là một dịch vụ trực tuyến có thể truy cập tại [sms4sats.com](https://sms4sats.com), cho phép quản lý tin nhắn SMS ẩn danh thông qua thanh toán bằng Bitcoin Lightning. Dịch vụ này cung cấp ba chức năng riêng biệt: nhận mã xác minh dùng một lần, gửi tin nhắn SMS đến bất kỳ số nào và thuê số điện thoại tạm thời trong vài giờ.



### Triết lý và mô hình hoạt động



Dự án được thiết kế để đảm bảo tính bảo mật tối đa và chủ quyền tài chính. Bằng cách không yêu cầu tạo tài khoản và chỉ chấp nhận thanh toán Bitcoin Lightning, SMS4Sats loại bỏ hoàn toàn nhu cầu cung cấp dữ liệu cá nhân. Không cần địa chỉ email, không cần thẻ tín dụng, không cần thông tin cá nhân nào. Chỉ cần thanh toán Lightning là đủ để truy cập dịch vụ.



Dịch vụ này hỗ trợ hơn 400 trang web và ứng dụng tại khoảng 120 quốc gia, đáp ứng hầu hết các nhu cầu xác minh thông thường. Phạm vi phủ sóng địa lý rộng lớn này cho phép xác thực đăng ký trên nhiều nền tảng khác nhau, từ mạng xã hội đến các dịch vụ nhắn tin.



### Mô hình thanh toán có điều kiện



SMS4Sats sử dụng hóa đơn Lightning có điều kiện (hóa đơn hodl) cho chức năng nhận tin nhắn SMS. Cơ chế này đảm bảo rằng bạn chỉ bị tính phí nếu tin nhắn SMS thực sự được nhận. Nếu không có tin nhắn nào đến trong thời gian quy định (tối đa 20 phút), khoản thanh toán sẽ tự động bị hủy và số satoshi sẽ được hoàn trả vào wallet của bạn. Sự đảm bảo này không áp dụng cho các tính năng gửi và thuê, vốn không được hoàn lại.



## Ba tính năng của SMS4Sats



Giao diện SMS4Sats được tổ chức xung quanh ba tab tương ứng với ba chức năng khác nhau: **NHẬN** để nhận mã xác minh, **GỬI** để gửi tin nhắn SMS ẩn danh và **THUÊ** để thuê số điện thoại tạm thời.



### Nhận tin nhắn SMS



Tính năng chính cho phép bạn nhận một số điện thoại tạm thời để lấy mã xác minh duy nhất. Sau khi nhận và sử dụng mã, số điện thoại đó sẽ bị vô hiệu hóa vĩnh viễn.



### Gửi tin nhắn SMS



Tính năng này cho phép bạn gửi tin nhắn SMS đến bất kỳ số điện thoại nào mà không tiết lộ danh tính của mình. Người nhận sẽ nhận được tin nhắn từ một số điện thoại ẩn danh.



### Thuê một tiết mục



Đối với người dùng cần nhận nhiều tin nhắn SMS trên cùng một số điện thoại, SMS4Sats cung cấp tùy chọn thuê bao tạm thời. Tùy chọn này cho phép bạn nhận và gửi nhiều tin nhắn trong thời gian thuê.



**Lưu ý về giá cả**: Giá hiển thị trong hướng dẫn này chỉ mang tính chất tham khảo. Giá thực tế có thể thay đổi tùy thuộc vào quốc gia của số điện thoại, dịch vụ mục tiêu và nhu cầu hiện tại. Ví dụ, một tin nhắn SMS đến Telegram Pháp có thể có giá từ 1.500 đến 5.000 satoshi, tùy thuộc vào điều kiện. Luôn kiểm tra số tiền chính xác trên hóa đơn Lightning trước khi thanh toán.



## Nhận tin nhắn SMS xác nhận



Chúng ta hãy cùng xem chi tiết cách sử dụng SMS4Sats để nhận mã xác minh, minh họa bằng việc tạo tài khoản Telegram.



### Bước 1: Chọn quốc gia và dịch vụ



Truy cập [sms4sats.com](https://sms4sats.com) và giữ nguyên ở tab **NHẬN**. Chọn quốc gia của số điện thoại bạn muốn nhận từ menu thả xuống. Nếu dịch vụ mục tiêu của gói cước của bạn được liệt kê, hãy chọn dịch vụ đó để tối ưu hóa khả năng nhận cuộc gọi.



![Sélection du pays France et du service Telegram sur SMS4Sats](assets/fr/01.webp)



Trong ví dụ này, chúng ta chọn Pháp là quốc gia và Telegram là dịch vụ mục tiêu. Nhấp vào **TIẾP THEO** để chuyển sang bước tiếp theo.



### Bước 2: Thanh toán hóa đơn Lightning



Hóa đơn Lightning được hiển thị dưới dạng mã QR. Số tiền sẽ khác nhau tùy thuộc vào quốc gia và dịch vụ đã chọn. Quét mã QR bằng thiết bị Lightning wallet của bạn hoặc sao chép hóa đơn để thanh toán thủ công.



![QR code de paiement Lightning avec garantie de remboursement](assets/fr/02.webp)



Xin lưu ý thông báo quan trọng: "Không có mã SMS = Không thanh toán". Nếu bạn không nhận được tin nhắn SMS, giao dịch thanh toán của bạn sẽ tự động bị hủy và hoàn tiền trong vòng tối đa 20 phút.



### Bước 3: Lấy số điện thoại tạm thời



Sau khi thanh toán được xác nhận, số điện thoại tạm thời sẽ được hiển thị ngay lập tức. Bộ đếm thời gian sẽ hiển thị thời gian còn lại để nhận tin nhắn SMS.



![Numéro temporaire révélé avec timer d'attente](assets/fr/03.webp)



Sao chép số này (ở đây là +33 7 74 70 09 66) để sử dụng trên dịch vụ bạn muốn đăng ký.



### Bước 4: Sử dụng số điện thoại trên dịch vụ mục tiêu



Nhập số tạm thời vào ứng dụng hoặc trang web nơi bạn tạo tài khoản. Trong ví dụ Telegram của chúng tôi, hãy nhập số, xác nhận và chờ mã xác minh.



![Processus d'inscription Telegram avec le numéro temporaire SMS4Sats](assets/fr/04.webp)



Quy trình này hoàn toàn giống với đăng ký thông thường: bạn nhập số điện thoại, Telegram sẽ gửi mã xác minh qua SMS, sau đó bạn hoàn tất việc tạo tài khoản.



### Bước 5: Lấy mã xác minh



Quay lại giao diện SMS4Sats. Ngay khi nhận được tin nhắn SMS, mã kích hoạt sẽ tự động hiển thị. Nhấp vào **SAO CHÉP MÃ** để sao chép mã dễ dàng.



![Code de vérification reçu sur SMS4Sats](assets/fr/05.webp)



Nhập mã này vào dịch vụ mục tiêu để hoàn tất đăng ký. Số điện thoại tạm thời sau đó sẽ bị vô hiệu hóa vĩnh viễn.



## Gửi tin nhắn SMS ẩn danh



SMS4Sats cũng cho phép bạn gửi tin nhắn SMS đến bất kỳ số nào mà không cần tiết lộ danh tính của mình.



### Bước 1: Viết tin nhắn



Nhấp vào tab **GỬI**. Nhập số điện thoại người nhận kèm mã vùng quốc tế và viết tin nhắn của bạn (tối đa 1600 ký tự).



![Interface d'envoi de SMS avec numéro destinataire et message](assets/fr/06.webp)



Nhấp vào **TIẾP THEO** để tiến hành thanh toán.



### Bước 2: Thanh toán và gửi



Thanh toán hóa đơn Lightning được hiển thị. Sau khi thanh toán được xác nhận, tin nhắn SMS sẽ được gửi ngay lập tức đến người nhận.



![Confirmation d'envoi du SMS avec code de confirmation](assets/fr/07.webp)



Mã xác nhận sẽ được hiển thị để xác nhận rằng tin nhắn đã được gửi. Người nhận sẽ nhận được tin nhắn SMS từ một số điện thoại ẩn danh.



## Thuê số điện thoại tạm thời



Đối với các trường hợp cần gửi nhiều tin nhắn SMS trên cùng một số điện thoại, tính năng THUÊ cho phép bạn thuê số điện thoại đó trong vài giờ.



### Cấu hình cho thuê



Nhấp vào tab **THUÊ**. Chọn quốc gia và thời gian thuê.



![Interface de location de numéro avec avertissement de non-remboursement](assets/fr/08.webp)



**Những điểm quan trọng cần lưu ý:**




- Giá cả thay đổi tùy thuộc vào quốc gia và thời gian lưu trú.
- Phí thuê không được hoàn lại**, không giống như tin nhắn SMS dùng một lần.
- Các số thuê bao thường không hoạt động với Telegram.
- Tùy chọn này phù hợp để đăng ký nhiều dịch vụ liên tiếp.



Sau khi bạn nhấp vào **TIẾP THEO** và thanh toán hóa đơn Lightning, bạn sẽ nhận được một số điện thoại mà bạn có thể sử dụng trong suốt thời gian thuê để nhận và gửi tin nhắn SMS.



## Ưu điểm và hạn chế



### Điểm nổi bật



**Không yêu cầu dữ liệu cá nhân**: Mô hình không cần đăng ký đảm bảo rằng không có thông tin cá nhân nào được thu thập.



**Ba chức năng bổ sung**: Nhận, gửi và cho thuê đáp ứng hầu hết các nhu cầu.



**Chỉ thanh toán bằng Bitcoin**: Lightning Network cho phép giao dịch tức thời và ẩn danh.



**Hoàn tiền tự động**: Khi nhận được tin nhắn SMS, hệ thống hóa đơn hodl đảm bảo rằng bạn chỉ phải thanh toán nếu tin nhắn SMS được gửi đến.



### Các ràng buộc cần xem xét



**Mức độ bảo mật tương đối của kênh SMS**: Mã SMS không phải là phương pháp xác thực mạnh mẽ và không nên được sử dụng cho các tài khoản nhạy cảm.



**Khả năng tương thích biến đổi**: Nhiều trang web phát hiện và chặn số điện thoại ảo. Có thể cần thử nhiều lần.



**Số định danh không thể tái sử dụng**: Sau khi sử dụng một lần, số định danh sẽ được tái chế và không thể thu hồi lại.



**Dịch vụ cho thuê không hoàn tiền**: Khác với tin nhắn SMS dùng một lần, dịch vụ cho thuê không kèm theo đảm bảo hoàn tiền.



## Thực tiễn tốt nhất



### Hãy sử dụng Tor để bảo mật thông tin cá nhân tốt hơn.



SMS4Sats có thể truy cập được thông qua [Tor](sms4sat6y7lkq4vscloomatwyj33cfeddukkvujo2hkdqtmyi465spid.onion). Cấu hình này sẽ che giấu địa chỉ IP của bạn khi truy cập dịch vụ.



### Tránh các tài khoản quan trọng



Tuyệt đối không sử dụng số điện thoại dùng một lần cho các tài khoản quan trọng (ngân hàng, email chính). Nếu các nền tảng này yêu cầu bạn xác thực lại số điện thoại sau này, bạn sẽ mất quyền truy cập vào tài khoản.



### Tách biệt danh tính kỹ thuật số của bạn



Đối với các tài khoản giả danh, hãy kết hợp số điện thoại tạm thời với một địa chỉ email dùng một lần và một trình duyệt riêng biệt, không liên quan đến trình duyệt bạn thường dùng.



### Hãy chọn một giải pháp xác thực hai yếu tố (2FA) mạnh mẽ.



Sau khi tài khoản của bạn được tạo, hãy kích hoạt các giải pháp xác thực mạnh mẽ hơn: ứng dụng TOTP (Aegis, Ente Auth) hoặc khóa bảo mật vật lý FIDO2.



## Phần kết luận



SMS4Sats là giải pháp hoàn chỉnh cho việc quản lý tin nhắn SMS bảo mật. Cho dù bạn muốn nhận mã xác minh, gửi tin nhắn ẩn danh hay thuê số điện thoại tạm thời, dịch vụ này đáp ứng nhiều nhu cầu bảo mật khác nhau, nhờ vào phương thức thanh toán bằng Bitcoin Lightning.



Tuy nhiên, cần lưu ý những hạn chế của dịch vụ này: nó không đảm bảo tính ẩn danh tuyệt đối và không phù hợp với các tài khoản nhạy cảm hoặc tài khoản sử dụng lâu dài. Nếu sử dụng một cách khôn ngoan và hiểu rõ những hạn chế của nó, SMS4Sats là một công cụ thiết thực giúp bạn lấy lại quyền kiểm soát các cuộc liên lạc điện thoại của mình.



## Tài nguyên





- [Trang web chính thức của SMS4Sats](https://sms4sats.com)
- [Câu hỏi thường gặp về dịch vụ](https://sms4sats.com/faq)
- [Địa chỉ Tor](http://sms4sat6y7lkq4vscloomatwyj33cfeddukkvujo2hkdqtmyi465spid.onion)