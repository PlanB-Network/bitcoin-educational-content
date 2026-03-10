---
name: Aqua
description: Bitcoin, Lightning và Liquid trong một wallet duy nhất
---
![cover](assets/cover.webp)


Aqua là một ứng dụng di động giúp dễ dàng tạo ra một wallet hoạt động mạnh mẽ cho Bitcoin và Liquid, đồng thời cung cấp khả năng sử dụng Lightning mà không cần quản lý node phức tạp nhờ tính năng hoán đổi tích hợp. Ứng dụng này cũng cho phép quản lý stablecoin USDT trên nhiều mạng khác nhau.


Được phát triển bởi công ty JAN3 dưới sự chỉ đạo của Samson Mow, ứng dụng Aqua ban đầu được thiết kế dành riêng cho nhu cầu của người dùng ở Mỹ Latinh, mặc dù nó phù hợp với bất kỳ người dùng nào trên toàn thế giới. Ứng dụng này đặc biệt hữu ích cho người mới bắt đầu và những người sử dụng Bitcoin hàng ngày để thanh toán.


Trong hướng dẫn này, chúng ta sẽ tìm hiểu cách sử dụng nhiều tính năng của Aqua. Nhưng trước khi làm điều đó, hãy dành chút thời gian để hiểu sidechain trên Bitcoin là gì và Liquid hoạt động như thế nào, để chúng ta có thể nắm bắt đầy đủ giá trị của Aqua.


![AQUA](assets/fr/01.webp)


## Sidechain là gì?


Giao thức Bitcoin có những hạn chế kỹ thuật được thiết kế có chủ đích nhằm duy trì tính phi tập trung của mạng lưới và đảm bảo an ninh được phân bổ cho tất cả người dùng. Tuy nhiên, những hạn chế này đôi khi có thể gây khó chịu cho người dùng, đặc biệt là trong thời gian tắc nghẽn do khối lượng giao dịch đồng thời lớn. Cuộc tranh luận về khả năng mở rộng của Bitcoin đã chia rẽ cộng đồng từ lâu, đặc biệt là trong Cuộc chiến kích thước khối (Blocksize War). Kể từ sự kiện này, cộng đồng Bitcoin đã thừa nhận rộng rãi rằng khả năng mở rộng phải được đảm bảo bằng các giải pháp off-chain, trên các hệ thống lớp thứ hai. Các giải pháp này bao gồm các chuỗi phụ (sidechain), vốn vẫn còn tương đối ít được biết đến và ít được sử dụng so với các hệ thống khác như Lightning Network.


Sidechain là một blockchain độc lập hoạt động song song với Bitcoin chính. Nó sử dụng bitcoin làm đơn vị tính toán, nhờ vào cơ chế gọi là "*neo hai chiều*". Hệ thống này cho phép khóa bitcoin trên chuỗi chính để tái tạo giá trị của chúng trên sidechain, nơi chúng lưu hành dưới dạng token được hỗ trợ bởi bitcoin gốc. Các token này thường giữ nguyên giá trị tương đương với bitcoin bị khóa trên chuỗi chính, và quá trình này có thể đảo ngược để thu hồi tiền trên Bitcoin.


Mục tiêu của các sidechain là cung cấp các chức năng bổ sung hoặc cải tiến kỹ thuật, chẳng hạn như giao dịch nhanh hơn, phí thấp hơn hoặc hỗ trợ hợp đồng thông minh. Những cải tiến này không phải lúc nào cũng có thể được triển khai trực tiếp trên Bitcoin hoặc blockchain mà không làm ảnh hưởng đến tính phi tập trung hoặc bảo mật của nó. Do đó, Sidechain cho phép thử nghiệm và khám phá các giải pháp mới trong khi vẫn bảo toàn tính toàn vẹn của Bitcoin. Tuy nhiên, các giao thức này thường đòi hỏi sự thỏa hiệp, đặc biệt là về tính phi tập trung và bảo mật, tùy thuộc vào mô hình quản trị và cơ chế đồng thuận được lựa chọn.


## Liquid là gì?


Liquid là một lớp phủ chuỗi phụ liên kết cho Bitcoin, được phát triển bởi Blockstream để cải thiện tốc độ giao dịch, quyền riêng tư và chức năng. Nó sử dụng cơ chế neo song phương được thiết lập trên một liên minh để khóa bitcoin trên chuỗi chính và tạo ra bitcoin Liquid (L-BTC) để đổi lại, các token lưu hành trên Liquid trong khi vẫn được hỗ trợ bởi bitcoin gốc.


![AQUA](assets/fr/02.webp)


Mạng lưới Liquid dựa trên một liên minh các bên tham gia, bao gồm các thực thể được công nhận từ hệ sinh thái Bitcoin, những người xác thực các khối và quản lý việc neo giá song phương. Ngoài L-BTC, Liquid cũng cho phép phát hành các tài sản kỹ thuật số khác, chẳng hạn như stablecoin USDT và các loại tiền điện tử khác.


![AQUA](assets/fr/03.webp)


## Cài đặt ứng dụng Aqua


Bước đầu tiên, tất nhiên, là tải xuống ứng dụng Aqua. Hãy vào cửa hàng ứng dụng của bạn:



- [Dành cho Android](https://play.google.com/store/apps/details?id=io.aquawallet.android);
- [Dành cho Apple](https://apps.apple.com/us/app/aqua-wallet/id6468594241).

![AQUA](assets/fr/04.webp)


Đối với người dùng Android, bạn cũng có tùy chọn cài đặt ứng dụng thông qua tệp `.apk` [có sẵn trên GitHub của họ](https://github.com/AquaWallet/aqua-wallet/releases).


![AQUA](assets/fr/05.webp)


Khởi động ứng dụng, sau đó tích vào ô "*Tôi đã đọc và đồng ý với Điều khoản dịch vụ & Chính sách bảo mật*".


![AQUA](assets/fr/06.webp)


## Tạo wallet của bạn trên Aqua


Nhấp vào nút "*Tạo Wallet*".


![AQUA](assets/fr/07.webp)


Và thế là xong, chiếc wallet của bạn đã được tạo ra!


![AQUA](assets/fr/08.webp)


Nhưng trước hết, vì đây là wallet tự quản lý, điều bắt buộc là phải sao lưu cụm từ ghi nhớ của bạn vào một bản sao vật lý. **Cụm từ ghi nhớ này cho phép bạn truy cập đầy đủ và không hạn chế vào tất cả bitcoin của mình**. Bất kỳ ai sở hữu cụm từ ghi nhớ này đều có thể đánh cắp tiền của bạn, ngay cả khi không có quyền truy cập vật lý vào điện thoại của bạn.


Nó cho phép bạn khôi phục quyền truy cập vào bitcoin của mình trong trường hợp bị mất, bị đánh cắp hoặc bị hỏng điện thoại. Do đó, điều rất quan trọng là phải lưu trữ cẩn thận trên một phương tiện vật lý (không phải kỹ thuật số) và cất giữ ở một nơi an toàn. Bạn có thể viết nó ra giấy, hoặc để tăng cường bảo mật, nếu đây là một thiết bị wallet lớn, tôi khuyên bạn nên khắc nó lên một vật liệu bằng thép không gỉ để bảo vệ nó khỏi nguy cơ hỏa hoạn, lũ lụt hoặc sụp đổ (đối với một thiết bị wallet được thiết kế để bảo vệ một lượng bitcoin nhỏ, một bản sao lưu bằng giấy đơn giản có lẽ là đủ).


Để thực hiện việc này, hãy nhấp vào menu Cài đặt.


![AQUA](assets/fr/09.webp)


Sau đó nhấp vào "*Xem cụm từ gốc*". Sao lưu cụm từ 12 từ này vào một bản sao vật lý.


![AQUA](assets/fr/10.webp)


Trong cùng menu cài đặt đó, bạn cũng có thể thay đổi ngôn ngữ ứng dụng và đơn vị tiền tệ được sử dụng.


![AQUA](assets/fr/11.webp)


Trước khi nhận được những đồng bitcoin đầu tiên vào wallet, **tôi khuyên bạn nên thực hiện kiểm tra khôi phục trống**. Hãy ghi lại một số thông tin tham khảo, chẳng hạn như địa chỉ xpub hoặc địa chỉ nhận tiền đầu tiên, sau đó xóa wallet trên ứng dụng Aqua khi nó vẫn còn trống. Sau đó, thử khôi phục wallet trên Aqua bằng cách sử dụng bản sao lưu giấy của bạn. Kiểm tra xem thông tin cookie được tạo ra sau khi khôi phục có khớp với thông tin bạn đã ghi lại ban đầu hay không. Nếu khớp, bạn có thể yên tâm rằng bản sao lưu giấy của bạn đáng tin cậy. Để tìm hiểu thêm về cách thực hiện kiểm tra khôi phục, vui lòng tham khảo hướng dẫn khác này:


https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

Bạn không thể thấy nó trên màn hình của tôi vì tôi đang sử dụng trình giả lập, nhưng trong phần cài đặt, bạn sẽ tìm thấy tùy chọn khóa ứng dụng bằng hệ thống xác thực sinh trắc học. Tôi đặc biệt khuyên bạn nên bật tính năng bảo mật này vì nếu không, bất kỳ ai có quyền truy cập vào điện thoại đã mở khóa của bạn đều có thể đánh cắp bitcoin của bạn. Bạn có thể sử dụng Face ID trên iOS hoặc dấu vân tay trên Android. Nếu các phương pháp này không thành công trong quá trình xác thực, bạn vẫn có thể truy cập ứng dụng bằng mã PIN của điện thoại.


## Nhận bitcoin trên Aqua


Giờ đây, wallet của bạn đã được thiết lập xong, bạn đã sẵn sàng nhận sats đầu tiên! Chỉ cần nhấp vào nút "*Nhận*" trong menu "*Wallet*".


![AQUA](assets/fr/12.webp)


Bạn có thể chọn nhận bitcoin trên chuỗi khối, trên Liquid hoặc thông qua Lightning.


![AQUA](assets/fr/13.webp)


Đối với các giao dịch trên chuỗi, Aqua sẽ tạo ra một địa chỉ nhận cụ thể, nơi bạn có thể nhận sats của mình.


![AQUA](assets/fr/14.webp)


Tương tự, khi chọn Liquid, Aqua sẽ cung cấp cho bạn địa chỉ Liquid.


![AQUA](assets/fr/15.webp)


Nếu bạn muốn nhận tiền qua Lightning, trước tiên bạn cần chỉ định số tiền mong muốn.


![AQUA](assets/fr/16.webp)


Sau đó nhấp vào "*Tạo Invoice*".


![AQUA](assets/fr/17.webp)


Aqua sẽ tạo hóa đơn để nhận tiền từ Lightning wallet. Xin lưu ý rằng, không giống như các tùy chọn onchain và Liquid, tiền nhận được qua Lightning sẽ tự động được chuyển đổi thành L-BTC trên Liquid bằng công cụ Boltz, vì Aqua không phải là một node Lightning. Quá trình này cho phép bạn nhận và gửi tiền qua Lightning, nhưng không cần lưu trữ bitcoin của bạn trên Lightning.


![AQUA](assets/fr/18.webp)


Cá nhân tôi sẽ bắt đầu bằng cách gửi bitcoin qua Lightning đến Aqua. Sau khi giao dịch hoàn tất và hóa đơn được cung cấp, chúng ta sẽ nhận được xác nhận.


![AQUA](assets/fr/19.webp)


Để theo dõi tiến trình trao đổi, hãy quay lại trang chủ wallet của bạn và nhấp vào tài khoản "*L2 Bitcoin*", tài khoản này sẽ liệt kê các giao dịch Lightning (thông qua trao đổi) và Liquid.


![AQUA](assets/fr/20.webp)


Tại đây bạn có thể xem giao dịch và số dư L-BTC của mình.


![AQUA](assets/fr/21.webp)


## Bitcoin đổi chỗ với Aqua


Giờ đây, khi bạn đã có tài sản trong Aqua hoặc wallet, bạn có thể trực tiếp trao đổi chúng từ ứng dụng, để chuyển sang Bitcoin hoặc blockchain chính, hoặc sang Liquid. Bạn cũng có thể chuyển đổi bitcoin của mình thành stablecoin USDT (hoặc các loại khác). Để làm điều đó, hãy vào menu "*Marketplace*".


![AQUA](assets/fr/22.webp)


Nhấp vào "*Trao đổi*".


![AQUA](assets/fr/23.webp)


Trong ô "*Chuyển từ*", hãy chọn tài sản bạn muốn giao dịch. Hiện tại, tôi chỉ sở hữu L-BTC, vì vậy tôi chọn tài sản đó.


![AQUA](assets/fr/24.webp)


Trong ô "*Chuyển đến*", hãy chọn tài sản đích cho giao dịch hoán đổi của bạn. Về phần mình, tôi đã chọn USDT trên mạng Liquid.


![AQUA](assets/fr/25.webp)


Nhập số tiền bạn muốn chuyển đổi.


![AQUA](assets/fr/26.webp)


Xác nhận bằng cách nhấp vào "*Tiếp tục*".


![AQUA](assets/fr/27.webp)


Hãy đảm bảo bạn hài lòng với các thiết lập hoán đổi, sau đó xác nhận bằng cách kéo nút "*Hoán đổi*" ở cuối màn hình.


![AQUA](assets/fr/28.webp)


Giao dịch đổi trả của bạn đã được xác nhận.


![AQUA](assets/fr/29.webp)


Nhìn lại wallet của chúng ta, ta có thể thấy hiện tại chúng ta đã có USDT trên Liquid.


![AQUA](assets/fr/30.webp)


## Gửi bitcoin bằng Aqua


Giờ bạn đã có bitcoin trong Aqua hoặc wallet, bạn có thể gửi chúng đi. Nhấp vào nút "*Gửi*".


![AQUA](assets/fr/31.webp)


Hãy chọn loại tài sản bạn muốn gửi hoặc chọn mạng lưới để thực hiện giao dịch. Về phần mình, tôi sẽ gửi bitcoin qua Lightning Network.


![AQUA](assets/fr/32.webp)


Tiếp theo, nhập thông tin cần thiết để gửi thanh toán: đối với bitcoin onchain hoặc Liquid, bạn cần nhập địa chỉ nhận; đối với Lightning, cần có hóa đơn. Bạn có thể dán thông tin này trực tiếp vào ô được cung cấp, hoặc sử dụng biểu tượng mã QR để mở camera và quét địa chỉ hoặc hóa đơn. Sau đó nhấp vào "*Tiếp tục*".


![AQUA](assets/fr/33.webp)


Nếu tất cả thông tin đều chính xác, hãy nhấp vào "*Tiếp tục*" một lần nữa.


![AQUA](assets/fr/34.webp)


Aqua sau đó sẽ hiển thị cho bạn bản tóm tắt giao dịch. Hãy đảm bảo tất cả thông tin đều chính xác, bao gồm địa chỉ người nhận, phí và số tiền. Để xác nhận giao dịch, hãy trượt nút "*Trượt để gửi*" ở cuối màn hình.


![AQUA](assets/fr/35.webp)


Sau đó bạn sẽ nhận được xác nhận về việc vận chuyển.


![AQUA](assets/fr/36.webp)


Vậy là giờ bạn đã biết cách sử dụng ứng dụng Aqua để nhận và chi tiêu tiền trên Bitcoin, Lightning và Liquid, tất cả chỉ từ một giao diện duy nhất.


Nếu bạn thấy hướng dẫn này hữu ích, tôi rất biết ơn nếu bạn để lại một biểu tượng ngón tay cái màu xanh lá cây bên dưới. Hãy thoải mái chia sẻ bài viết này trên mạng xã hội của bạn. Cảm ơn rất nhiều!


Tôi cũng khuyên bạn nên xem hướng dẫn chi tiết khác về ứng dụng di động Blockstream Green, đây cũng là một giải pháp thú vị khác để thiết lập Liquid wallet của bạn:


https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a