---
name: Satochip
description: Cài đặt và sử dụng thẻ thông minh Satochip
---
![cover](assets/cover.webp)

Ví cứng là một thiết bị điện tử chuyên dụng để quản lý và bảo mật các khóa riêng của một ví Bitcoin. Khác với ví phần mềm (hoặc ví nóng) được cài đặt trên các máy tính chung thường xuyên kết nối với Internet, ví cứng cho phép cô lập vật lý các khóa riêng, giảm thiểu rủi ro bị hack và mất cắp.

Mục tiêu chính của một ví cứng là giảm thiểu các chức năng của thiết bị để giảm bề mặt tấn công. Một bề mặt tấn công nhỏ hơn cũng có nghĩa là ít véc-tơ tấn công tiềm năng hơn, tức là ít điểm yếu trong hệ thống mà kẻ tấn công có thể khai thác để truy cập vào bitcoin.

Việc sử dụng ví cứng để bảo mật bitcoin của bạn được khuyến nghị, đặc biệt nếu bạn sở hữu một lượng lớn, dù là về giá trị tuyệt đối hay là tỷ lệ so với tổng tài sản của bạn.

Ví cứng được sử dụng kết hợp với phần mềm quản lý ví trên máy tính hoặc điện thoại thông minh. Phần mềm này quản lý việc tạo giao dịch, nhưng chữ ký mã hóa cần thiết để xác nhận các giao dịch này chỉ được thực hiện trong ví cứng. Điều này có nghĩa là các khóa riêng không bao giờ được tiếp xúc với môi trường có thể bị tấn công.

Ví cứng cung cấp bảo vệ kép cho người dùng: một mặt, chúng bảo vệ bitcoin của bạn khỏi các cuộc tấn công từ xa bằng cách giữ các khóa riêng ngoại tuyến, và mặt khác, chúng thường cung cấp khả năng chống chịu vật lý tốt hơn đối với các nỗ lực nhằm trích xuất các khóa. Và chính trên 2 tiêu chí bảo mật này, người ta có thể đánh giá và xếp hạng các mô hình khác nhau có mặt trên thị trường.

Trong hướng dẫn này, tôi đề xuất khám phá một trong những giải pháp này: Satochip.

## Giới thiệu về Satochip

Satochip là một ví cứng dưới dạng thẻ với chip được chứng nhận *EAL6+*, đây là một tiêu chuẩn bảo mật rất cao (*NXP JCOP*). Nó được sản xuất bởi một công ty Bỉ.

![SATOCHIP](assets/notext/01.webp)

Thẻ thông minh này được bán với giá €25, rất phải chăng so với các ví cứng khác trên thị trường. Chip là một yếu tố bảo mật đảm bảo khả năng chống lại các cuộc tấn công vật lý rất tốt. Hơn nữa, mã nguồn của nó là mã nguồn mở (*AGPLv3*).
Tuy nhiên, do định dạng của nó, Satochip không cung cấp nhiều lựa chọn như các ví cứng khác. Rõ ràng là không có pin, không có camera, cũng không có đầu đọc thẻ micro SD, vì nó là một thẻ. Nhược điểm lớn nhất, theo ý kiến của tôi, là thiếu màn hình trên ví cứng, làm cho nó dễ bị tổn thương hơn đối với một số loại tấn công từ xa. Thực tế, điều này buộc người dùng phải ký mù và tin tưởng vào những gì họ thấy trên màn hình máy tính của mình.

Mặc dù có những hạn chế, Satochip vẫn thú vị vì giá cả phải chăng. Ví này có thể được sử dụng để tăng cường bảo mật cho một ví chi tiêu bổ sung cho một ví tiết kiệm được bảo vệ bởi một ví cứng có màn hình. Nó cũng là một giải pháp tốt cho những người sở hữu một lượng nhỏ bitcoin và không muốn đầu tư hàng trăm euro vào một thiết bị phức tạp hơn. Hơn nữa, việc sử dụng Satochips trong các cấu hình multisig, hoặc có thể trong các hệ thống ví với timelock trong tương lai, có thể mang lại những lợi ích thú vị.

Công ty Satochip cũng cung cấp 2 sản phẩm khác. Có Satodime, là một thẻ mang theo được thiết kế để lưu trữ bitcoin ngoại tuyến, nhưng không cho phép giao dịch. Đó là một loại ví giấy an toàn hơn nhiều, có thể được sử dụng, ví dụ, để làm quà. Cuối cùng, có Seedkeeper, là một trình quản lý cụm từ ghi nhớ. Nó có thể được sử dụng để lưu trữ an toàn hạt giống của chúng ta mà không cần ghi trực tiếp trên một tờ giấy.

## Làm thế nào để mua Satochip?
Satochip hiện đã có bán [trên trang web chính thức](https://satochip.io/product/satochip/). Để mua nó tại cửa hàng vật lý, bạn cũng có thể tìm thấy [danh sách các nhà bán lẻ được chứng nhận](https://satochip.io/resellers/) trên trang web của Satochip.
Để tương tác với phần mềm quản lý ví của bạn, Satochip cung cấp hai khả năng: thông qua giao tiếp NFC hoặc qua một đầu đọc thẻ thông minh. Đối với tùy chọn NFC, hãy đảm bảo máy của bạn tương thích với công nghệ này hoặc có một đầu đọc NFC bên ngoài. Satochip hoạt động ở tần số chuẩn 13.56 MHz. Nếu không, bạn cũng có thể mua một đầu đọc thẻ thông minh. Bạn có thể tìm mua một cái trên trang web của Satochip hoặc nơi khác.

![SATOCHIP](assets/notext/02.webp)

## Cách thiết lập Satochip với Sparrow?

Sau khi bạn nhận được Satochip của mình, bước đầu tiên là kiểm tra bao bì để đảm bảo nó chưa được mở. Bao bì của Satochip nên bao gồm một tem niêm phong. Nếu tem này bị mất hoặc hỏng, nó có thể chỉ ra rằng thẻ thông minh đã bị xâm phạm và có thể không phải là hàng chính hãng.
![SATOCHIP](assets/notext/03.webp)
Bạn sẽ tìm thấy Satochip bên trong.

![SATOCHIP](assets/notext/04.webp)

Để quản lý ví, trong hướng dẫn này, tôi đề xuất sử dụng Sparrow. Nếu bạn chưa có phần mềm, [truy cập trang web chính thức để tải xuống](https://sparrowwallet.com/download/). Bạn cũng có thể xem hướng dẫn của chúng tôi về Sparrow Wallet (sẽ có sớm).

![SATOCHIP](assets/notext/05.webp)

Chèn Satochip của bạn vào đầu đọc thẻ thông minh hoặc đặt nó lên đầu đọc NFC, và kết nối đầu đọc với máy tính mà Sparrow đang mở.

![SATOCHIP](assets/notext/06.webp)

Mở Sparrow Wallet và đảm bảo bạn đã kết nối đúng cách với một nút Bitcoin. Để làm điều này, kiểm tra dấu tích ở góc dưới bên phải: nó nên là màu vàng nếu bạn kết nối với một nút công cộng, xanh lá cho kết nối với Bitcoin Core, hoặc xanh dương cho Electrum.

![SATOCHIP](assets/notext/07.webp)

Trên Sparrow Wallet, nhấp vào tab "*File*".

![SATOCHIP](assets/notext/08.webp)

Sau đó vào menu "*New Wallet*".

![SATOCHIP](assets/notext/09.webp)

Chọn một tên cho ví của bạn và sau đó nhấp vào "*Create Wallet*".

![SATOCHIP](assets/notext/10.webp)

Nhấp vào nút "*Connected Hardware Wallet*".

![SATOCHIP](assets/notext/11.webp)

Nhấp vào nút "*Scan...*".

![SATOCHIP](assets/notext/12.webp)

Satochip của bạn sẽ xuất hiện. Nhấp vào "*Import Keystore*".

![SATOCHIP](assets/notext/13.webp)

Tiếp theo, bạn cần thiết lập một mã PIN để mở khóa Satochip của mình. Chọn một mật khẩu mạnh, từ 4 đến 16 ký tự. Lưu lại mật khẩu này.

Hãy nhớ, mật khẩu này không phải là một cụm từ bí mật. Điều này có nghĩa là ngay cả khi không có mật khẩu này, cụm từ ghi nhớ của bạn vẫn sẽ cho phép bạn nhập lại ví vào phần mềm nếu cần. Mật khẩu chỉ được sử dụng để bảo vệ quyền truy cập vào chính Satochip. Nó tương đương với mã PIN tìm thấy trên các ví cứng khác.

Sau khi nhập mật khẩu, nhấp lại vào nút "*Import Keystore*".

![SATOCHIP](assets/notext/14.webp)

Ghi lại mật khẩu một lần nữa, sau đó nhấp vào nút "*Initialize*".
![SATOCHIP](assets/notext/15.webp)
Bạn sẽ đến với cửa sổ để tạo cụm từ ghi nhớ của mình. Nhấn vào nút "*Generate New*".

![SATOCHIP](assets/notext/16.webp)
Hãy tạo một hoặc nhiều bản sao vật lý của cụm từ khôi phục của bạn bằng cách viết nó ra trên giấy hoặc vật liệu kim loại. Hãy nhớ, cụm từ này cung cấp quyền truy cập đầy đủ vào bitcoin của bạn mà không cần bất kỳ bảo vệ bổ sung nào. Do đó, nếu ai đó phát hiện ra nó, họ có thể lập tức ăn cắp bitcoin của bạn, ngay cả khi không có quyền truy cập vào Satochip hoặc mã PIN của bạn. Vì vậy, việc bảo vệ những bản sao này là rất quan trọng. Hơn nữa, cụm từ này cho phép bạn lấy lại quyền truy cập vào bitcoin của mình trong trường hợp mất, hỏng Satochip, hoặc nếu bạn quên mã PIN của mình.
![SATOCHIP](assets/notext/17.webp)

Ví Bitcoin của bạn đã được tạo thành công.

![SATOCHIP](assets/notext/18.webp)

Nhấn lại vào nút "*Import Keystore*".

![SATOCHIP](assets/notext/19.webp)

Ví của bạn bây giờ đã được tạo. Khóa riêng của bạn giờ đây được lưu trữ trên thẻ thông minh của Satochip. Nhấn vào nút "*Apply*" để tiếp tục.

![SATOCHIP](assets/notext/20.webp)

Được khuyến nghị thiết lập một mật khẩu bổ sung để bảo vệ thông tin công khai được quản lý bởi Sparrow Wallet, bổ sung cho mã PIN của Satochip của bạn. Mật khẩu này sẽ đảm bảo an ninh truy cập vào Sparrow Wallet, giúp bảo vệ khóa công khai, địa chỉ và lịch sử giao dịch của bạn khỏi bất kỳ truy cập trái phép nào.

![SATOCHIP](assets/notext/21.webp)

Nhập mật khẩu của bạn vào hai trường, sau đó nhấn vào nút "*Set Password*".

![SATOCHIP](assets/notext/22.webp)

Và đó là, Satochip của bạn bây giờ đã được cấu hình trên Sparrow Wallet.

![SATOCHIP](assets/notext/23.webp)

Bây giờ ví của bạn đã được tạo, bạn có thể ngắt kết nối Satochip của mình. Giữ nó ở một nơi an toàn!

## Làm thế nào để nhận bitcoin với Satochip?

Khi bạn đang trong ví của mình, nhấn vào tab "*Receive*".

![SATOCHIP](assets/notext/24.webp)

Sparrow Wallet tạo một địa chỉ cho ví của bạn. Thông thường, đối với các ví phần cứng khác, bạn được khuyến khích nhấn vào "*Display Address*" để xác minh địa chỉ trực tiếp trên màn hình của thiết bị. Thật không may, tùy chọn này không khả dụng với Satochip, nhưng hãy chắc chắn sử dụng nó cho các ví khác của bạn.

![SATOCHIP](assets/notext/25.webp)

Bạn có thể thêm một "*Label*" để mô tả nguồn của bitcoin sẽ được bảo vệ với địa chỉ này. Đây là một thực hành tốt giúp bạn quản lý UTXOs của mình tốt hơn.

![SATOCHIP](assets/notext/26.webp)

Để biết thêm thông tin về việc gắn nhãn, tôi cũng khuyên bạn nên xem hướng dẫn khác này:

https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Sau đó, bạn có thể sử dụng địa chỉ này để nhận bitcoin.

![SATOCHIP](assets/notext/27.webp)
## Làm thế nào để gửi Bitcoin với Satochip?
Bây giờ bạn đã nhận được sats đầu tiên của mình trong ví an toàn với Satochip, bạn cũng có thể tiêu chúng! Kết nối Satochip của bạn với máy tính, khởi chạy Sparrow Wallet, và sau đó đi đến tab "*Send*" để tạo một giao dịch mới.

![SATOCHIP](assets/notext/28.webp)
Nếu bạn muốn thực hiện kiểm soát tiền xu, tức là chọn cụ thể các UTXO để tiêu trong giao dịch, hãy chuyển đến tab "*UTXOs*". Chọn các UTXO bạn muốn chi tiêu, sau đó nhấn vào "*Gửi Đã Chọn*". Bạn sẽ được chuyển hướng đến màn hình giống như tab "*Gửi*", nhưng với các UTXO của bạn đã được chọn sẵn cho giao dịch.
![SATOCHIP](assets/notext/29.webp)

Nhập địa chỉ đích. Bạn cũng có thể nhập nhiều địa chỉ bằng cách nhấn vào nút "*+ Thêm*".

![SATOCHIP](assets/notext/30.webp)

Ghi chú một "*Nhãn*" để nhớ mục đích của khoản chi này.

![SATOCHIP](assets/notext/31.webp)

Chọn số tiền gửi đến địa chỉ này.

![SATOCHIP](assets/notext/32.webp)

Điều chỉnh mức phí giao dịch theo thị trường hiện tại.

![SATOCHIP](assets/notext/33.webp)

Đảm bảo tất cả các thông số của giao dịch của bạn đều chính xác, sau đó nhấn vào "*Tạo Giao Dịch*".

![SATOCHIP](assets/notext/34.webp)

Nếu mọi thứ đều đúng ý bạn, nhấn vào "*Hoàn Tất Giao Dịch để Ký*".

![SATOCHIP](assets/notext/35.webp)

Nhấn vào "*Ký*".

![SATOCHIP](assets/notext/36.webp)

Nhấn vào "*Ký*" một lần nữa bên cạnh Satochip của bạn.

![SATOCHIP](assets/notext/37.webp)

Nhập mã PIN của Satochip của bạn, sau đó nhấn vào "*Ký*" một lần nữa để ký giao dịch.

![SATOCHIP](assets/notext/38.webp)

Giao dịch của bạn giờ đã được ký. Nhấn vào "*Phát Sóng Giao Dịch*" để phát sóng nó lên mạng Bitcoin.

![SATOCHIP](assets/notext/39.webp)

Bạn có thể tìm thấy nó trong tab "*Giao Dịch*" của Sparrow Wallet.

![SATOCHIP](assets/notext/40.webp)

Xin chúc mừng, bạn giờ đã biết cách sử dụng Satochip! Nếu bạn thấy hướng dẫn này hữu ích, tôi sẽ rất trân trọng nếu bạn để lại một lượt thích phía dưới. Đừng ngần ngại chia sẻ bài viết này trên các mạng xã hội của bạn. Cảm ơn bạn rất nhiều!