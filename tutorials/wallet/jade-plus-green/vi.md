---
name: Jade Plus - Green
description: Dễ dàng cấu hình Jade Plus với Green
---
![cover](assets/cover.webp)


![video](https://youtu.be/rv_cN7F7-TM)


Jade Plus là phiên bản phần cứng wallet chỉ dành riêng cho Bitcoin, được thiết kế bởi Blockstream. Đây là phiên bản kế nhiệm của Jade cổ điển, với những cải tiến về phần mềm, nhiều tùy chọn hơn và thiết kế công thái học được cải tiến để sử dụng trực quan hơn. Phiên bản mới này sở hữu màn hình LCD 1,9 inch tuyệt đẹp, với dải màu rộng hơn so với phiên bản tiền nhiệm. Các nút bấm và điều hướng menu cũng đã được tối ưu hóa.


Jade Plus có thể được sử dụng theo nhiều cách: thông qua kết nối có dây USB-C, ở chế độ "*Air-Gap*" với thẻ nhớ micro SD (cần bộ chuyển đổi), qua Bluetooth hoặc thậm chí bằng cách trao đổi mã QR nhờ camera tích hợp. Phần cứng wallet này sử dụng pin.


Sản phẩm có giá khởi điểm từ 149,99 đô la cho phiên bản màu đen cơ bản, và giá có thể tăng lên đến 20 đô la cho các phiên bản "*Genesis Grey*" hoặc "*Lunar Silver*". Do đó, Jade Plus là một lựa chọn thú vị, với các chức năng tiên tiến tương đương với các thiết bị wallet cao cấp như Coldcard Q hoặc Passport V2, nhưng với mức giá khá thấp, gần với các mẫu tầm trung.


![JADE-PLUS-GREEN](assets/fr/01.webp)


Jade Plus tương thích với hầu hết phần mềm quản lý wallet. Dưới đây là tóm tắt về khả năng tương thích tại thời điểm viết bài này (tháng 1 năm 2025):


| Management Software  | Desktop | Mobile | USB | Bluetooth   | QR  | JadeLink |
| -------------------- | ------- | ------ | --- | ----------- | --- | -------- |
| Blockstream Green    | 🟢      | 🟢     | 🟢  | 🟢 (Mobile) | 🟢  | 🔴       |
| Liana                | 🟢      | 🔴     | 🟢  | 🔴          | 🔴  | 🔴       |
| Sparrow              | 🟢      | 🔴     | 🟢  | 🔴          | 🟢  | 🟢       |
| Nunchuk              | 🟢      | 🟢     | 🔴  | 🔴          | 🟢  | 🟢       |
| Specter              | 🟢      | 🔴     | 🔴  | 🔴          | 🟢  | 🟢       |
| BlueWallet           | 🟢      | 🟢     | 🔴  | 🔴          | 🟢  | 🟢       |
| Electrum             | 🟢      | 🔴     | 🟢  | 🔴          | 🔴  | 🔴       |
| Keeper               | 🔴      | 🟢     | 🔴  | 🔴          | 🟢  | 🔴       |

Trong hướng dẫn này, chúng ta sẽ thiết lập và sử dụng Jade Plus với ứng dụng di động Green Wallet của Blockstream thông qua kết nối Bluetooth. Thiết lập này lý tưởng cho người mới bắt đầu. Nếu bạn đang tìm kiếm cách tiếp cận nâng cao hơn, tôi khuyên bạn nên xem hướng dẫn này, nơi chúng tôi sử dụng Jade Plus với Sparrow Wallet ở chế độ mã QR:


https://planb.academy/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

## Mẫu an toàn Jade Plus


Jade Plus sử dụng mô hình bảo mật dựa trên "secure element ảo", được hiện thực hóa bởi một "oracle mù". Cụ thể, cơ chế này kết hợp mã PIN do người dùng chọn, một khóa bí mật được lưu trữ trên Jade và một khóa bí mật do oracle (máy chủ do Blockstream duy trì) nắm giữ để tạo ra khóa AES-256 được phân bổ cho hai thực thể. Trong quá trình khởi tạo, việc trao đổi ECDH bảo mật giao tiếp với oracle và mã hóa cụm từ khôi phục trên phần cứng wallet. Trên thực tế, khi bạn muốn truy cập seed để ký giao dịch, bạn cần quyền truy cập vào:




- Đối với chính thiết bị Jade Plus;
- Nhập mã PIN để mở khóa thiết bị;
- Và cả bí mật của lời tiên tri nữa.


Ưu điểm chính của phương pháp này là không có điểm lỗi duy nhất ở cấp độ phần cứng, vì nếu kẻ tấn công có thể truy cập vào Jade của bạn, việc trích xuất khóa đòi hỏi phải đồng thời xâm nhập cả Jade và oracle. Mô hình này cũng có nghĩa là Jade Plus hoàn toàn là mã nguồn mở, tránh được những hạn chế liên quan đến việc sử dụng các secure element vật lý thực sự, chẳng hạn như những Ledger.


Nhược điểm của hệ thống này là việc sử dụng Jade Plus phụ thuộc vào oracle do Blockstream duy trì. Nếu oracle này không thể truy cập được, bạn sẽ không thể sử dụng trực tiếp thiết bị phần cứng wallet với mã PIN nữa. Tuy nhiên, điều này không có nghĩa là bitcoin của bạn bị mất, vì chúng vẫn có thể được khôi phục bằng cụm từ khôi phục, mà bạn có thể nhập vào Jade Plus ở chế độ "không trạng thái". Để khắc phục sự phụ thuộc này, bạn cũng có thể cấu hình và quản lý máy chủ oracle của riêng mình.


## Mở hộp Jade Plus


Khi nhận được Jade Plus, hãy kiểm tra hộp và niêm phong xem còn nguyên vẹn không để đảm bảo gói hàng của bạn chưa bị mở.


![JADE-PLUS-GREEN](assets/fr/02.webp)


Trong hộp bạn sẽ tìm thấy:




- Le Jade Plus;
- Cáp USB-C;
- Thẻ để ghi lại cụm từ ghi nhớ của bạn dưới dạng từ hoặc dưới dạng "*CompactSeedQR*";
- Một số hướng dẫn sử dụng;
- Một sợi dây;
- Một số hình dán.


![JADE-PLUS-GREEN](assets/fr/03.webp)


Thiết bị có 4 nút điều hướng:




- Nút ở phía dưới bên phải dùng để bật Jade;
- Nút lớn ở phía trước thiết bị được dùng để chọn một mục;
- Hai nút nhỏ ở phía trên cho phép bạn di chuyển sang trái và phải;
- Bạn cũng có thể chọn một mục bằng cách nhấn đồng thời vào hai nút ở phía trên thiết bị.


![JADE-PLUS-GREEN](assets/fr/04.webp)


## Thiết lập Bitcoin wallet mới


Nhấp vào nút bắt đầu.


![JADE-PLUS-GREEN](assets/fr/05.webp)


Nhấp vào "*Thiết lập Jade*".


![JADE-PLUS-GREEN](assets/fr/06.webp)


Chọn "Bắt đầu thiết lập". Tùy chọn "*Thiết lập nâng cao*" cũng thực hiện thao tác tương tự, nhưng cho phép truy cập vào các cài đặt nâng cao.


![JADE-PLUS-GREEN](assets/fr/07.webp)


Sau đó nhấp vào "*Tạo Wallet mới*" để tạo seed mới.


![JADE-PLUS-GREEN](assets/fr/08.webp)


Nhấp vào nút "*Tiếp tục*" để hiển thị cụm từ khôi phục mới của bạn.


![JADE-PLUS-GREEN](assets/fr/09.webp)


Thiết bị Jade Plus của bạn hiển thị cụm từ ghi nhớ 12 từ. **Cụm từ ghi nhớ này cho phép bạn truy cập đầy đủ và không hạn chế vào tất cả bitcoin của mình. Bất kỳ ai sở hữu cụm từ này đều có thể đánh cắp tiền của bạn, ngay cả khi không có quyền truy cập vật lý vào Jade Plus của bạn. Cụm từ 12 từ này sẽ khôi phục quyền truy cập vào bitcoin của bạn trong trường hợp Jade bị mất, bị đánh cắp hoặc bị hỏng. Do đó, điều rất quan trọng là phải lưu giữ nó cẩn thận và cất giữ ở một nơi an toàn.**


Bạn có thể viết nó lên tấm bìa cứng được cung cấp trong hộp, hoặc để an toàn hơn, tôi khuyên bạn nên khắc nó lên đế bằng thép không gỉ để bảo vệ khỏi hỏa hoạn, lũ lụt hoặc sụp đổ.


![JADE-PLUS-GREEN](assets/fr/10.webp)


Để biết thêm thông tin về cách lưu và quản lý cụm từ ghi nhớ đúng cách, tôi đặc biệt khuyên bạn nên tham khảo hướng dẫn khác này, nhất là nếu bạn là người mới bắt đầu:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Rõ ràng là bạn tuyệt đối không được chia sẻ những từ ngữ này trên Internet, như tôi đã làm trong hướng dẫn này. Mẫu wallet này sẽ chỉ được sử dụng trên Testnet và sẽ bị xóa khi kết thúc hướng dẫn.**


Nhấp vào mũi tên ở bên phải màn hình để hiển thị các từ sau.


![JADE-PLUS-GREEN](assets/fr/11.webp)


Sau khi lưu cụm từ, Jade Plus sẽ yêu cầu bạn xác nhận. Chọn từ đúng theo thứ tự bằng các nút ở phía trên thiết bị, rồi nhấn nút ở giữa để chuyển sang từ tiếp theo.


![JADE-PLUS-GREEN](assets/fr/12.webp)


## Kết nối Jade Plus với Green Wallet


Trong hướng dẫn này, chúng ta sẽ sử dụng ứng dụng Green Wallet để quản lý wallet được lưu trữ trên Jade Plus. Phương pháp này đặc biệt phù hợp cho người mới bắt đầu. Nếu bạn muốn quản lý Bitcoin wallet chi tiết hơn, bạn cũng có thể sử dụng Sparrow Wallet, mà chúng ta sẽ đề cập trong một hướng dẫn riêng:


https://planb.academy/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262

Để biết hướng dẫn về cách cài đặt và thiết lập ứng dụng Blockstream Green, vui lòng xem phần đầu tiên của hướng dẫn khác này:


https://planb.academy/tutorials/wallet/mobile/blockstream-app-onchain-e84edaa9-fb65-48c1-a357-8a5f27996143

Sau khi mở ứng dụng Blockstream Green, hãy nhấp vào nút "*Cấu hình wallet mới*".


![JADE-PLUS-GREEN](assets/fr/13.webp)


Chọn "*Trên Hardware Wallet*".


![JADE-PLUS-GREEN](assets/fr/14.webp)


Kích hoạt Bluetooth trên điện thoại thông minh của bạn, sau đó nhấn vào nút "Kết nối Jade của bạn".


![JADE-PLUS-GREEN](assets/fr/15.webp)


Cấp quyền cho ứng dụng Green truy cập các kết nối Bluetooth.


![JADE-PLUS-GREEN](assets/fr/16.webp)


Ứng dụng đang tìm kiếm thiết bị Jade Plus của bạn.


![JADE-PLUS-GREEN](assets/fr/17.webp)


Trên Jade Plus, hãy nhấp vào menu "*Bluetooth*".


![JADE-PLUS-GREEN](assets/fr/18.webp)


Chọn thiết bị của bạn trên ứng dụng Green.


![JADE-PLUS-GREEN](assets/fr/19.webp)


Hãy xác nhận mã ghép nối trên thiết bị Jade Plus của bạn.


![JADE-PLUS-GREEN](assets/fr/20.webp)


Green cung cấp cho bạn một bài kiểm tra để đảm bảo rằng Jade của bạn là hàng chính hãng. Nhấp vào nút để thực hiện.


![JADE-PLUS-GREEN](assets/fr/21.webp)


Xác nhận trên Jade.


![JADE-PLUS-GREEN](assets/fr/22.webp)


Green xác nhận rằng thiết bị của bạn là hàng chính hãng.


![JADE-PLUS-GREEN](assets/fr/23.webp)


## Thiết lập mã PIN


Nhấp vào nút "*Tiếp tục*" để chọn mã PIN cho Jade của bạn.


![JADE-PLUS-GREEN](assets/fr/24.webp)


Mã PIN mở khóa Jade của bạn. Do đó, nó là một biện pháp bảo vệ chống lại việc truy cập vật lý trái phép. Mã PIN này không liên quan đến việc tạo ra các khóa mã hóa của wallet. Vì vậy, ngay cả khi không có mã PIN này, việc sở hữu cụm từ ghi nhớ 12 từ sẽ cho phép bạn lấy lại quyền truy cập vào bitcoin của mình. Chúng tôi khuyên bạn nên chọn một mã PIN càng ngẫu nhiên càng tốt. Và hãy chắc chắn lưu mã này ở một nơi riêng biệt với nơi bạn lưu trữ Jade (ví dụ: trong trình quản lý mật khẩu).


Chọn mã PIN 6 chữ số trên thiết bị Jade của bạn bằng cách sử dụng các nút bên phải và bên trái để cuộn qua các chữ số, và nút ở giữa để xác nhận việc nhập một chữ số.


![JADE-PLUS-GREEN](assets/fr/25.webp)


Hãy xác nhận mã PIN của bạn lần thứ hai.


![JADE-PLUS-GREEN](assets/fr/26.webp)


Giao dịch Bitcoin wallet của bạn đã được tạo.


![JADE-PLUS-GREEN](assets/fr/27.webp)


## Tạo tài khoản Bitcoin


Bạn cần tạo tài khoản trong wallet. Nhấp vào nút "*Tạo tài khoản*".


![JADE-PLUS-GREEN](assets/fr/28.webp)


Chọn "*Tiêu chuẩn*" nếu bạn muốn tạo một khẩu wallet cổ điển với một chữ ký duy nhất.


![JADE-PLUS-GREEN](assets/fr/29.webp)


Để biết thêm thông tin về tùy chọn "*2FA*", bạn có thể tham khảo hướng dẫn khác này:


https://planb.academy/tutorials/wallet/mobile/blockstream-green-2fa-37397d5c-5c27-44ad-a27a-c9ceac8c9df9

Tài khoản của bạn đã được tạo.


![JADE-PLUS-GREEN](assets/fr/30.webp)


Nếu bạn muốn cá nhân hóa chiếc Green wallet của mình, hãy nhấp vào ba dấu chấm nhỏ ở góc trên bên phải.


![JADE-PLUS-GREEN](assets/fr/31.webp)


Tùy chọn "*Đổi tên*" cho phép bạn tùy chỉnh tên của wallet, điều này đặc biệt hữu ích nếu bạn quản lý nhiều wallet trên cùng một ứng dụng. Menu "*Đơn vị*" cho phép bạn thay đổi đơn vị cơ bản của wallet. Ví dụ, bạn có thể chọn hiển thị nó bằng satoshi thay vì bitcoin. Cuối cùng, menu "*Thông số*" cung cấp cho bạn quyền truy cập vào các tùy chọn khác. Ví dụ, tại đây bạn sẽ tìm thấy khóa công khai mở rộng và mô tả của nó, hữu ích nếu bạn đang có kế hoạch thiết lập một wallet chỉ để xem từ Jade của mình.


![JADE-PLUS-GREEN](assets/fr/32.webp)


Để kết nối lại với Jade sau khi tắt thiết bị, hãy nhấn nút bật/tắt ở phía dưới thiết bị. Trên ứng dụng Green, chọn thiết bị của bạn từ trang chủ:


![JADE-PLUS-GREEN](assets/fr/33.webp)


Sau đó, nhập mã PIN trên thiết bị Jade của bạn, và bạn sẽ được kết nối lại.


![JADE-PLUS-GREEN](assets/fr/34.webp)


Thiết bị Jade của bạn được mở khóa thông qua "secure element ảo" của Blockstream (xem phần đầu tiên của hướng dẫn này). Việc này yêu cầu kết nối Bluetooth với ứng dụng Green. Nếu bạn gặp khó khăn với kết nối Bluetooth trong quá trình mở khóa, hãy thử ngắt kết nối và kết nối lại hai thiết bị. Nếu sự cố vẫn tiếp diễn, bạn vẫn có thể mở khóa Jade bằng cách chọn tùy chọn "*Quét mã QR*" và làm theo hướng dẫn có sẵn [trên trang web của Blockstream](https://jadefw.blockstream.com/pinqr/index.html).


Trước khi nhận được những đồng bitcoin đầu tiên trên wallet, **tôi khuyên bạn nên thực hiện kiểm tra khôi phục trống**. Hãy ghi lại một số thông tin tham khảo, chẳng hạn như địa chỉ xpub hoặc địa chỉ nhận tiền đầu tiên của bạn, sau đó xóa wallet trên ứng dụng Green và trên Jade Plus khi thiết bị vẫn đang trống (`Tùy chọn -> Thiết bị -> Khôi phục cài đặt gốc`). Sau đó, hãy thử khôi phục wallet bằng cách sử dụng bản sao lưu giấy của cụm từ ghi nhớ. Kiểm tra xem thông tin cookie được tạo ra sau khi khôi phục có khớp với thông tin bạn đã ghi lại ban đầu hay không. Nếu khớp, bạn có thể yên tâm rằng bản sao lưu giấy của bạn đáng tin cậy. Để tìm hiểu thêm về cách thực hiện kiểm tra khôi phục, vui lòng tham khảo hướng dẫn khác này:


https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Nhận bitcoin


Giờ đây, sau khi đã thiết lập xong Bitcoin và wallet, bạn đã sẵn sàng nhận chiếc sats đầu tiên! Chỉ cần nhấp vào nút "*Nhận*" trên ứng dụng Green.


![JADE-PLUS-GREEN](assets/fr/35.webp)


Green hiển thị địa chỉ nhận tín hiệu, nhưng trước khi sử dụng, điều cần thiết là phải kiểm tra trên Jade để xác nhận rằng nó thực sự thuộc về wallet của chúng ta. Để làm điều này, hãy nhấp vào nút "*Xác minh trên thiết bị*".


![JADE-PLUS-GREEN](assets/fr/36.webp)


Kiểm tra trên Jade xem địa chỉ có giống với trên Green hay không, sau đó nhấp vào nút để xác nhận.


![JADE-PLUS-GREEN](assets/fr/37.webp)


Giờ đây bạn có thể chia sẻ địa chỉ với người trả tiền để nhận bitcoin vào wallet của mình. Khi giao dịch được phát sóng trên mạng, nó sẽ xuất hiện trong wallet của bạn. Hãy đợi cho đến khi bạn nhận được đủ xác nhận để coi giao dịch là hoàn tất.


![JADE-PLUS-GREEN](assets/fr/38.webp)


## Gửi bitcoin


Với Bitcoin trong wallet, giờ đây bạn cũng có thể gửi Bitcoin. Nhấp vào "*Gửi*".


![JADE-PLUS-GREEN](assets/fr/39.webp)


Ở trang tiếp theo, hãy nhập địa chỉ người nhận. Bạn có thể nhập thủ công hoặc quét mã QR.


![JADE-PLUS-GREEN](assets/fr/40.webp)


Chọn số tiền thanh toán.


![JADE-PLUS-GREEN](assets/fr/41.webp)


Ở cuối màn hình, bạn có thể chọn mức phí cho giao dịch này. Bạn có thể chọn theo khuyến nghị của ứng dụng hoặc tùy chỉnh mức phí của mình. Mức phí càng cao so với các giao dịch đang chờ xử lý khác, giao dịch của bạn sẽ được xử lý càng nhanh. Để biết thông tin về thị trường phí, vui lòng truy cập [Mempool.space](https://mempool.space/) trong mục "*Phí giao dịch*".


![JADE-PLUS-GREEN](assets/fr/42.webp)


Nhấp vào "*Tiếp theo*" để truy cập màn hình tóm tắt giao dịch. Kiểm tra xem địa chỉ, số tiền và phí có chính xác không.


![JADE-PLUS-GREEN](assets/fr/43.webp)


Nếu mọi việc suôn sẻ, hãy trượt nút màu xanh lá cây ở cuối màn hình sang bên phải để ký và phát sóng giao dịch trên mạng Bitcoin.


![JADE-PLUS-GREEN](assets/fr/44.webp)


Bạn được yêu cầu xác nhận giao dịch trên thiết bị Jade.


![JADE-PLUS-GREEN](assets/fr/45.webp)


Hãy chắc chắn rằng địa chỉ người nhận là chính xác. Nhấp vào dấu tích để xác nhận.


![JADE-PLUS-GREEN](assets/fr/46.webp)


Kiểm tra lại số tiền thanh toán xem có chính xác không, sau đó xác nhận.


![JADE-PLUS-GREEN](assets/fr/47.webp)


Giao dịch của bạn đã được ký và phát sóng từ Green.


![JADE-PLUS-GREEN](assets/fr/48.webp)


Chúc mừng, giờ bạn đã biết cách thiết lập và sử dụng Jade Plus với ứng dụng di động Blockstream Green thông qua kết nối Bluetooth. Nếu bạn thấy hướng dẫn này hữu ích, tôi rất biết ơn nếu bạn để lại một biểu tượng ngón tay cái màu xanh lá cây bên dưới. Hãy thoải mái chia sẻ bài viết này trên mạng xã hội của bạn. Cảm ơn vì đã chia sẻ!


Để hiểu rõ hơn, tôi khuyên bạn nên tham khảo hướng dẫn này về Jade Plus, trong đó chúng ta sẽ cấu hình nó với phần mềm Sparrow Wallet ở chế độ QR. Bạn cũng sẽ học cách sử dụng các cài đặt nâng cao của phần cứng wallet:


https://planb.academy/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262