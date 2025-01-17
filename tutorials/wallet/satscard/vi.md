---
name: Satscard
description: Cài đặt và sử dụng Satscard với Nunchuk
---
![cover](assets/cover.webp)

Bitcoin là một hệ thống tiền mặt điện tử cho phép chúng ta thực hiện các giao dịch ngang hàng. Tuy nhiên, để tin tưởng rằng một giao dịch không thể thay đổi, cần phải chờ đợi một số lần xác nhận (thường là 6), để tránh bất kỳ nỗ lực nào của người gửi trong việc chi tiêu gấp đôi. Sự chậm trễ trong việc xác nhận này đôi khi có thể gây bất tiện, đặc biệt là khi muốn có sự kết thúc ngay lập tức tương tự như tiền mặt vật lý. Khác với việc sở hữu một tờ tiền được chuyển giao ngay lập tức, các giao dịch Bitcoin liên quan đến thời gian chờ đợi trước khi được coi là không thể đảo ngược một cách chắc chắn.

Đây là nơi mà Satscard xuất hiện. Nó cung cấp một phương pháp để cho phép truyền đạt bitcoins một cách vật lý và tức thì, mà không cần thực hiện giao dịch trên chuỗi. Satscard hoạt động như một thẻ mang, cho phép chuyển giao quyền sở hữu bitcoin một cách an toàn, do đó mang lại trải nghiệm gần gũi hơn với tiền mặt truyền thống. Trong hướng dẫn này, tôi sẽ giới thiệu cho bạn giải pháp này.

## Satscard là gì?

Satscard của Coinkite là người kế nhiệm của Opendime. Đây là một thẻ NFC cho phép truyền đạt bitcoins một cách vật lý, tương tự như một tờ tiền hoặc đồng xu. Khác với một ví cứng truyền thống, Satscard là một thẻ mang, có nghĩa là việc sở hữu vật lý của thẻ tương đương với quyền sở hữu bitcoins được bảo vệ bởi các khóa lưu trữ trên đó. Giá của nó dao động từ $6.99 đến $17.99 tùy thuộc vào thiết kế được chọn.

![SATSCARD](assets/notext/01.webp)

Chip Satscard được trang bị 10 khe, cho phép nó lưu trữ bitcoins lên đến 10 lần trên 10 địa chỉ khác nhau. Mỗi khe hoạt động độc lập và lý thuyết chỉ nên được sử dụng một lần để khóa bitcoins vào đó. Để chi tiêu bitcoins, chỉ cần mở khóa khe với một ứng dụng tương thích, như Nunchuk, bằng cách nhập mã xác minh 6 chữ số ghi ở mặt sau của Satscard.

Thẻ đảm bảo rằng khóa riêng bảo vệ bitcoins trên blockchain không thể được giữ lại bởi chủ sở hữu trước khi họ vật lý rời bỏ thẻ. Người nhận cũng có thể xác minh tính hợp lệ của một khe và số lượng lưu trữ trong đó tại thời điểm giao dịch.

Hệ thống này đặc biệt hữu ích cho việc mua hàng hóa vật lý bằng bitcoins, hoặc tặng bitcoins như một món quà.

## Làm thế nào để mua một Satscard?

Satscard có sẵn để mua [trên trang web chính thức của Coinkite](https://store.coinkite.com/store/category/satscard). Để mua nó tại một cửa hàng vật lý, bạn cũng có thể tìm [danh sách các nhà bán lẻ được chứng nhận](https://coinkite.com/resellers) trên trang web.
Bạn cũng sẽ cần một điện thoại tương thích với giao tiếp NFC, hoặc một thiết bị USB để đọc thẻ NFC ở tần số chuẩn 13.56 MHz.
## Làm thế nào để tải một khe trên Satscard?

Sau khi bạn nhận được Satscard của mình, bước đầu tiên là kiểm tra bao bì để đảm bảo nó chưa được mở. Nếu bao bì bị hỏng, điều này có thể chỉ ra rằng thẻ đã bị xâm phạm và có thể không phải là hàng chính hãng.

Để quản lý Satscard, chúng ta sẽ sử dụng ứng dụng di động **Nunchuk Wallet**. Đảm bảo điện thoại thông minh của bạn tương thích với NFC, sau đó tải xuống Nunchuk từ [Google Play Store](https://play.google.com/store/apps/details?id=io.nunchuk.android), [App Store](https://apps.apple.com/us/app/nunchuk-bitcoin-wallet/id1563190073), hoặc trực tiếp qua tệp [`.apk`](https://github.com/nunchuk-io/nunchuk-android/releases).
Lý thuyết, bạn có thể trực tiếp gửi bitcoin đến địa chỉ được chỉ định ở mặt sau của Satscard của bạn mà không cần sử dụng Nunchuk. Tuy nhiên, tôi khuyên bạn không nên làm điều này, vì chúng tôi sẽ trước tiên xác minh rằng địa chỉ của khe đầu tiên thực sự được tạo ra từ một khóa riêng được lưu trữ trong Satscard và nó không phải là một địa chỉ giả mạo.

Nếu bạn sử dụng Nunchuk lần đầu, ứng dụng sẽ đề nghị bạn tạo một tài khoản. Đối với mục đích của hướng dẫn này, không cần thiết phải tạo một tài khoản. Vì vậy, chọn "*Tiếp tục như khách*" để tiếp tục mà không cần tài khoản.

Sau đó, nhấp vào "*Ví không hỗ trợ*".

Tiếp theo, nhấp vào nút "*Tôi sẽ tự khám phá*".

Một khi đã ở màn hình chính của Nunchuk, nhấp vào biểu tượng "*NFC*" ở đầu màn hình.

Giữ Satscard của bạn vào mặt sau của điện thoại để quét nó.

Nunchuk hiển thị địa chỉ nhận tương ứng với khe đầu tiên của Satscard của bạn. Bình thường, địa chỉ này nên giống hệt với địa chỉ được viết thủ công ở mặt sau của thẻ của bạn. Sao chép địa chỉ này và sử dụng nó để chuyển bitcoin mà bạn muốn khóa với khe này.

## Làm thế nào để kiểm tra bitcoin trên một khe?

Một khi giao dịch được xác nhận, bạn có thể kiểm tra số dư liên kết với một khe của Satscard của bạn bằng cách quét nó với Nunchuk. Như vậy, trong một giao dịch, người nhận bitcoin có thể ngay lập tức xác minh, qua ứng dụng Nunchuk của họ, rằng thẻ thực sự chứa bitcoin nợ họ.

Nếu bên kia không có ứng dụng Nunchuk, họ vẫn có thể xác minh tính hợp lệ của Satscard. Chỉ cần kích hoạt NFC trên điện thoại thông minh của họ và đặt Satscard ở mặt sau của thiết bị. Điều này sẽ tự động mở trang web Satscard trong trình duyệt, nơi người ta có thể kiểm tra tính hợp lệ của thẻ cũng như số lượng bitcoin liên kết với nó.

## Làm thế nào để rút bitcoin từ một khe?

Bây giờ, sau khi khe đầu tiên của Satscard đã được nạp với một lượng nhất định bitcoin, bạn có thể trao thẻ cho người nhận thanh toán.

Nếu bạn là người nhận, bạn cần cài đặt Nunchuk. Một khi đã ở trong ứng dụng, nhấp vào biểu tượng "*NFC*" ở đầu màn hình.

Đặt Satscard của bạn ở mặt sau của điện thoại.

Nunchuk sẽ tiết lộ số tiền được bảo đảm trên địa chỉ.

Để mở khóa khóa riêng và chuyển bitcoin đến một địa chỉ bạn sở hữu, nhấp vào nút "*Mở khóa và quét số dư*".

Tùy chọn "*Quét vào ví*" cho phép bạn trực tiếp gửi bitcoin đến một ví đã có trong ứng dụng Nunchuk của bạn. Để chuyển quỹ đến một địa chỉ nhận khác, chọn "*Rút đến một địa chỉ*".
Nhập địa chỉ nhận mà bạn muốn gửi bitcoin được bảo mật bởi Satscard. Hãy chắc chắn rằng địa chỉ nhập là chính xác (đây là lần duy nhất bạn có thể kiểm tra nó), sau đó nhấn vào nút "*Tạo giao dịch*".

Nhập mã PIN của Satscard của bạn. Mã 6 chữ số này được ghi ở mặt sau của thẻ vật lý.

Giữ Satscard ở mặt sau của điện thoại thông minh của bạn trong khi ký giao dịch với khóa riêng được lưu trữ trên thẻ NFC.

Giao dịch của bạn bây giờ đã được ký và phát sóng trên mạng Bitcoin, nghĩa là khe cắm được sử dụng trên Satscard của bạn bây giờ đã trống.

## Làm thế nào để tái sử dụng Satscard?

Khác với các giải pháp sử dụng một lần như Opendime, Satscard được trang bị một chip chứa 10 khe cắm độc lập, cho phép thực hiện tới 10 thao tác với một thẻ duy nhất. Khe cắm đầu tiên, được cài đặt sẵn tại nhà máy bởi Coinkite, tương ứng với địa chỉ nhận được viết ở mặt sau của Satscard của bạn.

Để kích hoạt 9 khe cắm còn lại, bạn sẽ cần tạo cặp khóa và địa chỉ thông qua ứng dụng Nunchuk. Trên trang chủ của ứng dụng, nhấn vào biểu tượng "*NFC*" ở đầu màn hình.

Đặt Satscard của bạn ở mặt sau của điện thoại.

Nunchuk chỉ ra rằng không có khe cắm nào được kích hoạt trên thẻ, điều này là bình thường vì khe đầu tiên đã được sử dụng và khe thứ hai chưa được tạo. Để xem các khe đã sử dụng trước đó, nhấn vào "*Xem các khe chưa được niêm phong*". Việc tái sử dụng các khe này không được khuyến khích, vì điều này sẽ dẫn đến việc tái sử dụng địa chỉ gây hại cho quyền riêng tư trên chuỗi của bạn. Do đó, chúng ta sẽ thiết lập một khe mới bằng cách nhấn vào nút "*Có*".

Bây giờ bạn sẽ cần chọn cách bạn tạo mã chuỗi chính của mình.

Các khe trên Satscard tuân theo tiêu chuẩn BIP32, nghĩa là việc phát sinh các khóa mật mã bảo vệ bitcoin không dựa vào cụm từ ghi nhớ như trong ví BIP39, mà trực tiếp dựa vào một khóa riêng chính và một mã chuỗi chính. Hai yếu tố này được sử dụng làm đầu vào trong hàm HMAC-SHA512 để tạo ra một cặp khóa con. Mỗi khe có khóa chính của riêng mình và mã chuỗi chính của riêng mình. Chỉ có một cấp độ phát sinh cho mỗi khe.

Cặp khóa cho khe đầu tiên được Coinkite tạo sẵn. Đó là lý do bạn có quyền truy cập trực tiếp vào nó qua Nunchuk, và tại sao địa chỉ nhận được viết ở mặt sau của thẻ NFC. Tuy nhiên, đối với các khe khác, bạn chịu trách nhiệm tạo các khóa.

Khóa riêng chính cho mỗi khe được tạo trực tiếp bởi Satscard, và mã chuỗi chính phải được cung cấp từ bên ngoài. Đối với mã chuỗi của khe mới của bạn, bạn có hai lựa chọn: để Nunchuk tạo tự động bằng cách chọn "*Tự động*", hoặc tự tạo bằng cách chọn "*Nâng cao*" và nhập vào không gian dành riêng. Để mã chuỗi có hiệu quả, nó cần phải ngẫu nhiên càng nhiều càng tốt.
Nhập mã PIN 6 chữ số được ghi ở mặt sau của Satscard.
![SATSCARD](assets/notext/26.webp)

Đặt Satscard của bạn ở mặt sau điện thoại.

![SATSCARD](assets/notext/27.webp)

Một khe mới đã được cấu hình thành công. Bây giờ bạn có thể thấy địa chỉ nhận để nạp bitcoin vào. Để tiếp tục với việc nạp, hãy làm theo hướng dẫn trong phần "*Cách nạp một khe trên Satscard?*" của hướng dẫn này.
Bạn có thể lặp lại quá trình này lên đến 10 lần trên mỗi Satscard.

Xin chúc mừng, bạn giờ đã nắm bắt cách sử dụng Satscard! Nếu bạn thấy hướng dẫn này hữu ích, tôi sẽ rất biết ơn nếu bạn có thể để lại một lượt thích ở phía dưới. Đừng ngần ngại chia sẻ bài viết này trên các mạng xã hội của bạn. Cảm ơn bạn rất nhiều!