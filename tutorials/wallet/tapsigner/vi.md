---
name: Tapsigner
description: Cài đặt và sử dụng Tapsigner với Nunchuk
---
![cover](assets/cover.webp)

Một ví cứng (hardware wallet) là một thiết bị điện tử được thiết kế riêng để quản lý và bảo mật khóa riêng của ví Bitcoin. Khác với ví phần mềm (hoặc ví nóng) được cài đặt trên các máy tính chung thường xuyên kết nối với Internet, ví cứng cho phép cô lập vật lý khóa riêng, giảm thiểu rủi ro bị hack và mất cắp.

Mục tiêu chính của một ví cứng là giảm thiểu chức năng của thiết bị để giảm bề mặt tấn công. Một bề mặt tấn công nhỏ hơn cũng có nghĩa là ít véc-tơ tấn công tiềm năng hơn, tức là ít điểm yếu trong hệ thống mà kẻ tấn công có thể khai thác để truy cập vào bitcoin.

Việc sử dụng ví cứng để bảo mật bitcoin của bạn được khuyến nghị, đặc biệt nếu bạn sở hữu một lượng lớn, dù là về giá trị tuyệt đối hay là tỷ lệ so với tổng tài sản của bạn.

Ví cứng được sử dụng kết hợp với phần mềm quản lý ví trên máy tính hoặc điện thoại thông minh. Phần mềm này quản lý việc tạo giao dịch, nhưng chữ ký mã hóa cần thiết để xác nhận các giao dịch này chỉ được thực hiện trong ví cứng. Điều này có nghĩa là khóa riêng không bao giờ được tiếp xúc với môi trường có thể bị tấn công.

Ví cứng cung cấp hai lớp bảo vệ cho người dùng: một mặt, chúng bảo vệ bitcoin của bạn khỏi các cuộc tấn công từ xa bằng cách giữ khóa riêng ngoại tuyến, và mặt khác, chúng thường cung cấp khả năng chống chịu vật lý tốt hơn đối với các nỗ lực nhằm trích xuất khóa. Và chính trên 2 tiêu chí bảo mật này, người ta có thể đánh giá và xếp hạng các mô hình khác nhau có mặt trên thị trường.

Trong hướng dẫn này, tôi đề xuất khám phá một trong những giải pháp này: Tapsigner của Coinkite.

## Giới thiệu về Tapsigner

Tapsigner là một ví cứng được thiết kế dưới dạng thẻ NFC bởi công ty Coinkite, cũng nổi tiếng với việc sản xuất Coldcards.

![TAPSIGNER NUNCHUK](assets/notext/01.webp)

Tapsigner cho phép lưu trữ một cặp bao gồm một khóa riêng chính và một mã chuỗi theo BIP32, để phái sinh một cây khóa mã hóa. Những khóa này có thể được sử dụng để ký giao dịch bằng cách đặt Tapsigner gần một điện thoại hoặc đầu đọc thẻ NFC.
Thẻ NFC này được bán với giá $19.99, rất phải chăng so với các ví cứng khác có mặt trên thị trường. Tuy nhiên, do định dạng của nó, Tapsigner không cung cấp nhiều lựa chọn như các thiết bị khác. Rõ ràng là không có pin, không có camera, cũng không có đầu đọc thẻ micro SD, vì nó là một thẻ. Theo ý kiến của tôi, nhược điểm lớn nhất là thiếu màn hình trên ví cứng, làm cho nó dễ bị tổn thương trước một số loại tấn công từ xa. Thực tế, điều này buộc người dùng phải ký mù và tin tưởng vào những gì họ thấy trên màn hình máy tính của mình.

Mặc dù có những hạn chế, Tapsigner có thể thú vị vì giá cả phải chăng của nó. Ví này có thể được sử dụng để tăng cường bảo mật cho một ví chi tiêu bổ sung cho một ví tiết kiệm được bảo vệ bởi một ví cứng có màn hình. Nó cũng đại diện cho một giải pháp tốt cho những người sở hữu một lượng nhỏ bitcoin và không muốn đầu tư hàng trăm euro vào một thiết bị phức tạp hơn. Hơn nữa, việc sử dụng Tapsigner trong các cấu hình multisig, hoặc có thể trong các hệ thống ví với timelock trong tương lai, có thể mang lại những lợi ích thú vị.

## Làm thế nào để mua một Tapsigner?

Tapsigner có sẵn để mua [trên trang web chính thức của Coinkite](https://store.coinkite.com/store/category/tapsigner). Để mua nó tại cửa hàng vật lý, bạn cũng có thể tìm [danh sách các nhà bán lẻ được chứng nhận](https://coinkite.com/resellers) trên trang web.
Bạn cũng cần một điện thoại tương thích với giao tiếp NFC, hoặc một thiết bị USB để đọc thẻ NFC ở tần số chuẩn 13.56 MHz.
## Làm thế nào để khởi tạo một Tapsigner với Nunchuk?

Khi bạn nhận được Tapsigner của mình, bước đầu tiên là kiểm tra bao bì để đảm bảo rằng nó chưa được mở. Nếu gói hàng bị hỏng, điều này có thể chỉ ra rằng thẻ đã bị xâm phạm và có thể không phải là hàng chính hãng. CoinKite sẽ giao Tapsigner của bạn với một hộp chặn sóng radio. Hãy chắc chắn rằng nó có mặt trong gói hàng của bạn.

![TAPSIGNER NUNCHUK](assets/notext/02.webp)

Để quản lý ví, chúng ta sẽ sử dụng ứng dụng di động **Nunchuk Wallet**. Đảm bảo điện thoại thông minh của bạn tương thích NFC, sau đó tải xuống Nunchuk từ [Google Play Store](https://play.google.com/store/apps/details?id=io.nunchuk.android), [App Store](https://apps.apple.com/us/app/nunchuk-bitcoin-wallet/id1563190073) hoặc trực tiếp qua tệp [`.apk`](https://github.com/nunchuk-io/nunchuk-android/releases) của nó.

![TAPSIGNER NUNCHUK](assets/notext/03.webp)
Nếu bạn sử dụng Nunchuk lần đầu, ứng dụng sẽ yêu cầu bạn tạo một tài khoản. Đối với mục đích của hướng dẫn này, không cần thiết phải tạo một tài khoản. Vì vậy, chọn "*Tiếp tục như khách*" để tiếp tục mà không cần tài khoản.
![TAPSIGNER NUNCHUK](assets/notext/04.webp)

Sau đó nhấn vào "*Ví không hỗ trợ*".

![TAPSIGNER NUNCHUK](assets/notext/05.webp)

Tiếp theo, nhấn vào nút "*Tôi sẽ khám phá một mình*".

![TAPSIGNER NUNCHUK](assets/notext/06.webp)

Khi đã vào Nunchuk, nhấn vào nút "*+*" bên cạnh tab "*Keys*".

![TAPSIGNER NUNCHUK](assets/notext/07.webp)

Chọn "*Thêm khóa NFC*".

![TAPSIGNER NUNCHUK](assets/notext/08.webp)

Sau đó nhấn vào "*Thêm TAPSIGNER*".

![TAPSIGNER NUNCHUK](assets/notext/09.webp)

Nhấn vào "*Tiếp tục*" và sau đó đặt thẻ NFC Tapsigner của bạn gần điện thoại thông minh.

![TAPSIGNER NUNCHUK](assets/notext/10.webp)

Nếu Tapsigner của bạn là mới, Nunchuk sẽ đề nghị khởi tạo nó. Nhấn vào "*Có*".

![TAPSIGNER NUNCHUK](assets/notext/11.webp)

Bây giờ bạn sẽ cần chọn cách tạo mã chuỗi chính của mình.

Tapsigner sử dụng tiêu chuẩn BIP32. Điều này có nghĩa là việc phái sinh các khóa mật mã bảo vệ bitcoin của bạn không dựa vào cụm từ ghi nhớ như ví BIP39, mà trực tiếp dựa vào khóa riêng chính và mã chuỗi chính. Hai yếu tố này được truyền qua hàm HMAC để phái sinh một cách có hệ thống và phân cấp phần còn lại của ví của bạn.

Khóa riêng chính được tạo trực tiếp bởi TRNG (*True Random Number Generator*) tích hợp trong Tapsigner của bạn. Mã chuỗi chính, mặt khác, phải được cung cấp từ bên ngoài. Tại bước này, bạn có một lựa chọn: để Nunchuk tự động tạo ra bằng cách nhấn vào "*Tự động*", hoặc tự tạo ra bằng cách chọn "*Nâng cao*" và nhập vào trường được cung cấp.

![TAPSIGNER NUNCHUK](assets/notext/12.webp)
Tiếp theo, bạn cần chọn một mã PIN. Trong khu vực "*Starting PIN*", nhập mã PIN được ghi ở mặt sau của Tapsigner của bạn.
![TAPSIGNER NUNCHUK](assets/notext/13.webp)

Chọn một mã PIN để bảo vệ quyền truy cập vật lý vào Tapsigner của bạn. Mã PIN này không đóng vai trò nào trong quá trình khôi phục ví. Chức năng duy nhất của nó là để mở khóa Tapsigner của bạn để ký các giao dịch. Hãy chắc chắn lưu mã PIN này để tránh quên mất. Nhấn vào "*Continue*" để tiếp tục.

![TAPSIGNER NUNCHUK](assets/notext/14.webp)
Đặt thẻ Tapsigner của bạn ở mặt sau của điện thoại ngay bây giờ để khởi tạo nó.
![TAPSIGNER NUNCHUK](assets/notext/15.webp)

Nunchuk sau đó sẽ tạo ra tệp khôi phục cho ví của bạn, cho phép bạn lấy lại quyền truy cập vào bitcoin của mình trong trường hợp bạn mất thẻ NFC. Tệp này được mã hóa bằng mã sao lưu được viết ở mặt sau của Tapsigner của bạn. Để khôi phục bitcoin của bạn, bạn sẽ cần tệp này cũng như mã để giải mã nó. Do đó, việc tạo một bản sao giấy của mã này là quan trọng, bởi vì nếu bạn mất thẻ NFC, quyền truy cập vào mã này cũng sẽ bị mất, vì hiện tại nó chỉ được viết trên thẻ. Hãy chắc chắn tạo nhiều bản sao lưu của tệp khôi phục đã mã hóa của bạn.

![TAPSIGNER NUNCHUK](assets/notext/16.webp)

Chọn một tên cho ví của bạn.

![TAPSIGNER NUNCHUK](assets/notext/17.webp)

Nền tảng của ví bạn giờ đây đã được thiết lập. Để xác minh tính xác thực của Tapsigner của bạn, bất cứ lúc nào, bạn có thể nhấn vào nút "*Run health check*".

![TAPSIGNER NUNCHUK](assets/notext/18.webp)

Nhập mã PIN của bạn.

![TAPSIGNER NUNCHUK](assets/notext/19.webp)

Sau đó đặt thẻ của bạn ở mặt sau của điện thoại.

![TAPSIGNER NUNCHUK](assets/notext/20.webp)

## Làm thế nào để tạo một ví trên Tapsigner?

Quay lại trang chủ của Nunchuk, bạn có thể thấy Tapsigner của bạn được đăng ký trong các thiết bị ký có sẵn.

![TAPSIGNER NUNCHUK](assets/notext/21.webp)

Bây giờ bạn sẽ cần tạo các khóa cho ví Bitcoin của mình. Để làm điều này, nhấn vào nút "*+*" bên phải của tab "*Wallets*".

![TAPSIGNER NUNCHUK](assets/notext/22.webp)

Nhấn vào "*Create new wallet*".

![TAPSIGNER NUNCHUK](assets/notext/23.webp)

Sau đó chọn tùy chọn "*Create a new wallet using existing keys*".

![TAPSIGNER NUNCHUK](assets/notext/24.webp)

Chọn một tên cho ví của bạn và sau đó nhấn vào "*Continue*".

![TAPSIGNER NUNCHUK](assets/notext/25.webp)

Chọn Tapsigner của bạn là thiết bị ký cho bộ khóa mới này, sau đó nhấn vào "*Continue*".

![TAPSIGNER NUNCHUK](assets/notext/26.webp)

Nếu mọi thứ đều đúng như bạn mong đợi, xác nhận việc tạo.

![TAPSIGNER NUNCHUK](assets/notext/27.webp)
Sau đó, bạn có thể lưu tệp cấu hình của ví tiền của mình. Tệp này chỉ chứa các khóa công khai của bạn, điều này có nghĩa là ngay cả khi ai đó truy cập vào nó, họ cũng không thể ăn cắp bitcoin của bạn. Tuy nhiên, họ có thể theo dõi tất cả các giao dịch của bạn. Do đó, tệp này chỉ đặt ra rủi ro cho quyền riêng tư của bạn. Trong một số trường hợp, nó có thể rất quan trọng để khôi phục ví của bạn.

Và đó là, ví của bạn đã được tạo thành công!

Khi bạn không sử dụng Tapsigner, hãy nhớ cất giữ nó trong hộp được Coinkite cung cấp, hộp này chặn sóng vô tuyến để bảo vệ chống lại việc đọc không được phép.

## Làm thế nào để nhận bitcoin trên Tapsigner?

Để nhận bitcoin, nhấp vào ví của bạn.

Sau đó sử dụng địa chỉ được tạo để nhận bitcoin. Nếu bạn đã từng nhận bitcoin vào ví này, bạn sẽ cần nhấp vào nút "*Nhận*" để tạo một địa chỉ nhận mới trống.

Một khi giao dịch của người gửi được phát sóng, bạn sẽ thấy nó xuất hiện trên ví của mình.

Nhấp vào "*Xem tiền xu*".

Chọn UTXO mới của bạn.

Nhấp vào nút "*+*" bên cạnh "*Tags*" để thêm nhãn cho UTXO của bạn. Đây là một thực hành tốt, vì nó giúp bạn nhớ nguồn gốc của tiền xu và tối ưu hóa quyền riêng tư của bạn cho việc chi tiêu trong tương lai.

Chọn một nhãn hiện có hoặc tạo một nhãn mới, sau đó nhấp vào "*Lưu*". Bạn cũng có tùy chọn tạo "*bộ sưu tập*" để tổ chức tiền xu của mình một cách có cấu trúc hơn.

## Làm thế nào để gửi bitcoin với Tapsigner?

Bây giờ bạn đã có bitcoin trong ví, bạn cũng có thể gửi chúng. Để làm điều này, nhấp vào ví bạn chọn.

Nhấp vào nút "*Gửi*".

Chọn số lượng để gửi, sau đó nhấp vào "*Tiếp tục*".

Thêm một "*ghi chú*" cho giao dịch tương lai của bạn để nhớ mục đích của nó.

Tiếp theo, nhập địa chỉ của người nhận vào trường được chỉ định.

Bạn cũng có thể quét một địa chỉ được mã hóa bằng mã QR bằng cách nhấp vào biểu tượng nằm ở góc trên bên phải của màn hình.

Nhấp vào nút "*Tạo Giao Dịch*".

Xác minh chi tiết của giao dịch của bạn, sau đó nhấp vào nút "*Ký*" bên cạnh Tapsigner của bạn.

Nhập mã PIN của bạn để mở khóa.

Sau đó đặt Tapsigner vào mặt sau của điện thoại thông minh của bạn.
![TAPSIGNER NUNCHUK](assets/notext/46.webp)
Giao dịch của bạn đã được ký. Kiểm tra một lần nữa để đảm bảo mọi thứ đều chính xác, sau đó nhấp vào "*Broadcast Transaction*" để phát sóng nó trên mạng Bitcoin.

![TAPSIGNER NUNCHUK](assets/notext/47.webp)

Giao dịch của bạn đang chờ xác nhận.

![TAPSIGNER NUNCHUK](assets/notext/48.webp)

## Làm thế nào để khôi phục ví trong trường hợp mất Tapsigner?

Nếu bạn đã mất Tapsigner của mình, bạn có thể khôi phục ví của mình bằng cách sử dụng mã ghi trên mặt sau của thẻ. Do đó, việc lưu mã này riêng biệt khỏi Tapsigner là quan trọng, bởi vì nếu thẻ bị mất, quyền truy cập vào mã này cũng sẽ bị mất. Bạn cũng sẽ cần bản sao lưu được mã hóa của ví.

Để khôi phục, chúng ta sẽ sử dụng ứng dụng Nunchuk, nhưng hãy nhớ rằng điều này có nghĩa là tạm thời bảo vệ số tiền của bạn trong một ví nóng. Nếu Tapsigner của bạn đang bảo vệ một số tiền lớn, hãy xem xét việc theo dõi cùng một quy trình khôi phục với một Coldcard mới thay thế.

Mở ứng dụng Nunchuk và nhấp vào nút "*+*" bên cạnh tab "*Keys*".

![TAPSIGNER NUNCHUK](assets/notext/49.webp)

Chọn "*Add NFC key*".

![TAPSIGNER NUNCHUK](assets/notext/50.webp)

Chọn tùy chọn "*Recover TAPSIGNER key from backup*".

![TAPSIGNER NUNCHUK](assets/notext/51.webp)

Sau đó, bạn sẽ được chuyển hướng đến trình quản lý tệp của thiết bị. Tìm và chọn tệp sao lưu được mã hóa của ví của bạn. Thông thường, tên của tệp này bắt đầu với `backup...`.

![TAPSIGNER NUNCHUK](assets/notext/52.webp)

Nhập mật khẩu giải mã tệp sao lưu. Mật khẩu này tương ứng với mật khẩu ban đầu được ghi trên mặt sau của Tapsigner của bạn.

![TAPSIGNER NUNCHUK](assets/notext/53.webp)
Sau đó chọn một tên cho ví khôi phục của bạn.
![TAPSIGNER NUNCHUK](assets/notext/54.webp)

Bây giờ bạn đã lấy lại quyền truy cập vào bitcoin của mình. Ví của bạn giờ đây được quản lý như một ví nóng hiển thị trong tab "*Keys*" của ứng dụng Nunchuk. Tiếp theo, bạn cần tạo một bộ khóa mật mã mới trong phần "*Wallets*" bằng cách kết hợp khóa này với nó. Để làm điều này, bạn có thể theo dõi lại các bước trong phần "*How to create a wallet on a Tapsigner?*" của hướng dẫn này.

![TAPSIGNER NUNCHUK](assets/notext/55.webp)

Nếu bạn đã mất Tapsigner của mình, tôi khuyên bạn nên ngay lập tức chuyển bitcoin của mình sang một ví khác bạn sở hữu, lý tưởng nhất là được bảo vệ bởi một ví cứng. Thực sự, Tapsigner bạn đã mất có thể rơi vào tay sai. Do đó, việc rút hết tiền từ ví bạn vừa khôi phục và ngừng sử dụng nó là rất quan trọng.

Xin chúc mừng, bạn giờ đã nắm bắt được cách sử dụng Tapsigner! Nếu bạn thấy hướng dẫn này hữu ích, tôi sẽ rất biết ơn nếu bạn có thể để lại một lượt thích phía dưới. Đừng ngần ngại chia sẻ bài viết này trên các mạng xã hội của bạn. Cảm ơn bạn rất nhiều!