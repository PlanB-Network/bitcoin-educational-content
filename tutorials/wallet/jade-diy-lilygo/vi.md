---
name: Ngọc bích tự làm
description: Biến một bo mạch phát triển giá 15 đô la thành phần cứng Bitcoin wallet có đầy đủ chức năng
---

![cover](assets/cover.webp)


## Bitcoin Hardware Wallet - Xây dựng cho người mới bắt đầu


**Đối tượng:** Những người xây dựng tò mò nhưng có ít hoặc không có kinh nghiệm thực tế.


**Thời lượng:** 2 giờ (có thể linh hoạt)


**Kết quả:** Khi kết thúc khóa học, học sinh sẽ:



- Nhận biết mô hình bảo mật của ví phần cứng tự làm so với các thiết bị thương mại.
- Lắp ráp thiết bị ký tên dựa trên vi điều khiển.
- Flash chương trình cơ sở mã nguồn mở và xác minh tổng kiểm tra bản dựng.
- Ký và phát giao dịch mainnet bằng thiết bị mới của họ.


---

## Tóm tắt


Hội thảo kéo dài 2 giờ này hướng dẫn người mới bắt đầu cách xây dựng phần cứng Bitcoin wallet hoạt động bằng cách nạp firmware Jade mã nguồn mở vào bo mạch LilyGO T-Display giá 15 đô la. Học viên sẽ biến đổi phần cứng phát triển chung thành thiết bị ký số tương đương với ví thương mại giá 150 đô la, đồng thời học các kiến thức cơ bản về bảo mật thông qua trải nghiệm thực tế thay vì chỉ lý thuyết suông.


### Triết lý


Việc tự chế tạo thiết bị ký số không chỉ là tiết kiệm tiền mà còn là hiểu rõ công nghệ bảo vệ thiết bị Bitcoin của bạn. Hội thảo này đề cao "bảo mật thông qua hiểu biết" thay vì niềm tin hộp đen. Bằng cách tìm nguồn cung ứng linh kiện, cài đặt firmware mã nguồn mở và tự tạo ra entropy, sinh viên giảm thiểu rủi ro chuỗi cung ứng đồng thời học cách đánh giá các yêu cầu bảo mật một cách nghiêm túc. Mục tiêu là sự tự chủ có hiểu biết: sinh viên cần hiểu rõ cả sức mạnh và hạn chế của thiết bị tự chế so với các giải pháp thương mại đã được kiểm chứng.


---

## Khái niệm cơ bản (15 phút)


### Quyền tự chủ là gì và tại sao nó lại quan trọng?


Bitcoin được tạo ra để loại bỏ nhu cầu về các bên thứ ba đáng tin cậy, chẳng hạn như ngân hàng và tập đoàn, khỏi hệ thống tiền tệ của chúng ta. Thay vì sử dụng lòng tin, Bitcoin sử dụng toán học, vật lý và mật mã để cho phép bất kỳ ai có quyền sở hữu và kiểm soát tiền của mình mà không cần sự cho phép của bất kỳ ai.


Cách thức hoạt động này là bitcoin tồn tại trên một sổ cái kỹ thuật số toàn cầu gọi là blockchain hay còn gọi là chuỗi thời gian bitcoin, đây là một sổ cái công khai và minh bạch do máy tính quản lý, thay vì một sổ cái tập trung như tài khoản ngân hàng.


Điều quan trọng cần hiểu là để chuyển bitcoin từ nơi này sang nơi khác, bạn phải ký giao dịch đó bằng cái gọi là khóa riêng tư. Hãy tưởng tượng việc này giống như mở khóa két bằng mật khẩu và chuyển bitcoin sang két của người khác. Bitcoin trao cho bạn quyền tự giữ chìa khóa két đó, thay vì phải nhờ ngân hàng chuyển tiền hộ.


Quyền lực càng lớn thì trách nhiệm càng lớn, mất chìa khóa là tiền của bạn sẽ mất mãi mãi. Theo cách này, bạn có thể hình dung chìa khóa két sắt chính là tiền. Mặc dù chìa khóa không phải là Bitcoin, nhưng chúng là cơ chế để bạn di chuyển tiền của mình và do đó, việc bảo vệ chúng là vô cùng quan trọng. Đây là lý do tại sao chúng tôi nói "không phải chìa khóa, không phải tiền của bạn".


Thuật ngữ tự lưu ký nghe có vẻ khó hiểu, nhưng nó chỉ có nghĩa là bạn tự nắm giữ khóa riêng và kiểm soát Bitcoin của mình. Nếu bạn không nắm giữ khóa đó, bạn đang ủy thác cho người khác nắm giữ nó thay bạn. Nếu Bitcoin của bạn nằm trong một quỹ ETF hoặc trên một sàn giao dịch (Mt. Gox, FTX, Coinbase, Binance, v.v.), bạn không sở hữu Bitcoin, mà bạn sở hữu quyền sở hữu Bitcoin. Điều này tiềm ẩn đủ loại rủi ro, chẳng hạn như sàn giao dịch bị tấn công và mất Bitcoin của bạn, hoặc các công ty cho vay tiền của bạn và chỉ cung cấp cho bạn một phần nhỏ dự trữ. Ngoài ra, các bên thứ ba đáng tin cậy sẽ có toàn quyền kiểm soát tiền của bạn và có thể hạn chế hoặc đóng băng việc rút tiền.


![image](assets/fr/01.webp)


Với quyền tự quản, bạn loại bỏ niềm tin khỏi phương trình. Không ai có thể đóng băng tiền của bạn hoặc từ chối giao dịch, bạn có thể gửi tiền xuyên biên giới, cho bất kỳ ai, bất cứ lúc nào, và bạn không cần tài khoản ngân hàng, giấy tờ tùy thân hay sự chấp thuận của bất kỳ ai. Không ai có thể ngăn cản, kiểm duyệt hay đánh cắp của bạn, mở khóa toàn bộ sức mạnh của Bitcoin như một loại tiền tự do. Đây là lý do tại sao chúng tôi nói, với Bitcoin, bạn có thể là ngân hàng của chính mình.


Bitcoin được tạo ra để giải quyết vấn đề thao túng niềm tin và tiền bạc, một lựa chọn thoát khỏi hệ thống hiện tại, nhưng lối thoát chỉ hiệu quả nếu bạn nắm giữ chìa khóa. Đây là lý do tại sao quyền tự quản lại quan trọng đến vậy.


### Wallet là gì?


Thuật ngữ wallet có phần không chính xác và do đó có thể gây nhầm lẫn. Đúng là Bitcoin wallet, giống như wallet vật lý, cũng lưu trữ giá trị. Nhưng điểm khác biệt chính là ví Bitcoin không thực sự lưu trữ bất kỳ Bitcoin nào.


Bitcoin chỉ tồn tại dưới dạng một mục nhập sổ cái trên blockchain công khai, hoặc trong các kho lưu trữ ẩn dụ trên không gian mạng. Hãy nhớ rằng để chuyển Bitcoin, bạn phải sử dụng khóa của mình để mở khóa kho lưu trữ và chuyển tiền đến nơi khác, khóa riêng tư là thứ được sử dụng để chi tiêu Bitcoin. Khi bạn thực hiện giao dịch bằng wallet, thực chất bạn chỉ sử dụng khóa của mình để ký giao dịch. Đây là cách bạn chứng minh rằng bạn sở hữu số tiền đó và có quyền chi tiêu số tiền đó.


Ví Bitcoin thực chất chỉ lưu trữ khóa riêng của bạn, do đó sẽ chính xác hơn nếu gọi chúng là móc khóa.


### Ví Hot so với Cold


Hot wallet là một ứng dụng phần mềm trên điện thoại hoặc máy tính. Nó được kết nối với internet, do đó dễ sử dụng và ký giao dịch nhanh hơn, nhưng điều này cũng đồng nghĩa với việc nó dễ bị tin tặc, phần mềm độc hại và lừa đảo hơn. Nó được gọi là "hot" vì được kết nối với internet, được cắm điện và bật nguồn. Ví dụ như wallet trên điện thoại hoặc wallet trên trình duyệt.


Mặt khác, wallet lạnh, hay wallet phần cứng, là một thiết bị tạo và lưu trữ khóa ngoại tuyến. Điều này loại bỏ khả năng bị hack tiền của bạn và an toàn hơn nhiều cho việc tiết kiệm dài hạn, tuy nhiên, đây là thiết bị cần thiết để ký mọi giao dịch và có thể kém tiện lợi hơn.


### Mô hình đe dọa Hardware Wallet


Ví phần cứng ra đời để giải quyết một vấn đề cơ bản: làm thế nào để ký các giao dịch Bitcoin mà không để lộ khóa riêng tư của bạn cho một máy tính được kết nối internet, vốn có thể bị phần mềm độc hại hoặc kẻ tấn công từ xa xâm phạm? Mô hình mối đe dọa cốt lõi giả định rằng máy tính xách tay hoặc điện thoại thông thường của bạn có khả năng bị tấn công. Ví phần cứng wallet tạo ra một môi trường biệt lập, nơi khóa riêng tư không bao giờ rời khỏi thiết bị, và việc ký giao dịch diễn ra trong secure element hoặc bộ vi điều khiển, chỉ truyền chữ ký trở lại máy chủ, chứ không phải chính khóa. Ngay cả khi máy tính của bạn bị xâm nhập hoàn toàn, kẻ tấn công cũng không thể đánh cắp Bitcoin của bạn nếu không có quyền truy cập vật lý vào thiết bị và mã PIN của bạn.


Tuy nhiên, ví phần cứng cũng tiềm ẩn những mối đe dọa riêng. Bạn phải tin tưởng rằng nhà sản xuất không cài đặt cửa hậu, chuỗi cung ứng chưa bị can thiệp, và việc tạo số ngẫu nhiên thực sự là ngẫu nhiên. Kẻ tấn công vật lý có thể trích xuất khóa thông qua các cuộc tấn công kênh phụ hoặc thao túng chip, và người có quyền truy cập tạm thời có thể sửa đổi thiết bị của bạn. Tự xây dựng phần cứng wallet giúp bạn hiểu rõ những đánh đổi này—bạn sẽ đưa ra quyết định về các yếu tố bảo mật so với bộ vi điều khiển đa năng, cách xác minh giao dịch trên màn hình và cách bảo vệ chống lại cả các mối đe dọa từ xa và vật lý. Mục tiêu không phải là bảo mật hoàn hảo, mà là hiểu rõ bạn đang bảo vệ khỏi những mối đe dọa nào và những mối đe dọa nào còn tồn tại.


### Các khái niệm chính



- Cụm từ Entropy và seed:** wallet của bạn chỉ an toàn khi tính ngẫu nhiên của nó được sinh ra. Chúng tôi sẽ kết hợp bộ tạo số ngẫu nhiên của thiết bị với các thủ thuật thân thiện với con người như tung xúc xắc, chuyển đổi entropy đó thành một [cụm từ BIP39] gồm 12 hoặc 24 từ (https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki), và rời khỏi phòng với một bản sao lưu bằng văn bản hoặc kim loại mà bạn tin tưởng.
- Vệ sinh cụm từ gốc:** Hãy coi seed như chìa khóa vạn năng cho khoản tiết kiệm của bạn. Đừng bao giờ nhập các từ vào điện thoại hoặc máy tính—keylogger, ảnh chụp màn hình và sao lưu đám mây có thể làm rò rỉ thông tin mãi mãi. Hãy giữ cụm từ ngoại tuyến, lưu trữ ở nơi chỉ bạn mới có thể truy cập và luyện đọc lại thành tiếng trước khi rời đi.
- Phần tử bảo mật + vi điều khiển:** Hãy coi secure element như một két an toàn và vi điều khiển như bộ não. secure element bảo vệ khóa riêng tư với khả năng chống giả mạo, trong khi vi điều khiển xử lý màn hình, nút bấm và logic phần mềm. Lưu ý rằng các ví phần cứng chúng ta đang xây dựng hiện nay không có secure element. Điều này không có nghĩa là nó không an toàn, chỉ là nó có ít hơn một cấp độ bảo vệ.
- Tin tưởng firmware:** Firmware là hệ điều hành ẩn của wallet. Luôn tải xuống từ các bản phát hành được gắn thẻ, kiểm tra mã băm đã công bố và hiểu rằng các bản dựng có thể tái tạo cho phép nhiều người biên dịch cùng một mã và tạo ra cùng một tệp nhị phân. Nếu tổng kiểm tra không khớp, bạn không được ký.


---

## Chúng ta đang xây dựng cái gì?


Chúng tôi đang sử dụng phần cứng chung, LilyGo T-Display, và cài đặt firmware Jade SDK trên đó. [Jade Plus](https://blockstream.com/jade/jade-plus/) là một wallet mã nguồn mở, thường có giá 150 đô la:


![image](assets/fr/02.webp)


Hôm nay, chúng ta sẽ cài phần mềm của họ vào phần cứng có giá 15 đô la.


### Nên mua gì


![image](assets/fr/03.webp)



- LilyGO T-Display (16MB kèm shell, model K164)** — [Đặt hàng trực tiếp từ LilyGO](https://lilygo.cc/products/t-display?srsltid=AfmBOornob5U3FzZifuSwBBOdeXKcdPDqkYEnAVYKBLdzl0BPyNglGBR) với giá khoảng 15 đô la. Bo mạch ESP32 này cung cấp màn hình, nút bấm và giao diện USB tương tự như Jade Plus của Blockstream. ESP32 tích hợp cũng bao gồm các kết nối Wi-Fi và Bluetooth; chúng tôi sẽ cung cấp firmware để vô hiệu hóa các kết nối này, nhưng chúng sẽ định hình mô hình mối đe dọa của bạn vì mã độc có thể bật lại chúng.
- Cáp USB-C** — Mang theo cáp có khả năng truyền dữ liệu để bạn có thể flash chương trình cơ sở và cấp nguồn cho bo mạch trực tiếp từ máy tính xách tay (hoàn toàn phù hợp để sử dụng trong lớp học).


### Tại sao bạn nên tự chế tạo Hardware Wallet?



- Tiết kiệm khoảng 135 đô la so với việc mua thiết bị thương mại.
- Tạo sự thoải mái với chức năng cài đặt phần mềm, các thành phần bảo mật và vệ sinh wallet.
- Mở thêm các thiết bị ký tên để phân bổ số tiền tiết kiệm vào nhiều ví.
- Giảm thiểu rủi ro trong chuỗi cung ứng bằng cách tự tìm nguồn cung ứng và lắp ráp mọi linh kiện.
- Hãy ghi nhớ câu thần chú của Lopp: chủ quyền và sự tiện lợi luôn trái ngược nhau.


## Thiết lập vật lý


### Chuẩn bị trường hợp của bạn


Bạn có hai lựa chọn để bảo vệ bo mạch LilyGO T-Display của mình: vỏ in 3D hoặc vỏ LilyGO chính hãng. Vỏ in có thể được tìm thấy và in từ [mẫu này](https://www.printables.com/model/119144-lilygo-ttgo-t-display-enclosure). Vỏ này nhẹ và có thể tùy chỉnh cho thiết bị của bạn.


![image](assets/fr/04.webp)


Ngoài ra, bạn có thể sử dụng ốp lưng LilyGO chính hãng, có kiểu dáng và lớp hoàn thiện hơi khác một chút, mang lại khả năng bảo vệ chắc chắn hơn và vẻ ngoài bóng bẩy hơn.


![image](assets/fr/05.webp)


Lưu ý rằng vỏ hộp in và vỏ hộp chính thức có đôi chút khác biệt về thiết kế và lắp ráp. Dù bạn chọn loại nào, hãy đảm bảo bo mạch được lắp đúng vị trí bên trong vỏ hộp để tránh bị lỏng kết nối hoặc hư hỏng.


### Kiểm tra Hội đồng quản trị


Trước khi tiếp tục, hãy kiểm tra kỹ bo mạch LilyGO T-Display xem có bất kỳ khuyết tật hoặc mảnh vụn nào không. Kiểm tra xem màn hình, các nút bấm và cổng USB-C có sạch sẽ, không có bụi hoặc vết hàn bắn ra không. Cẩn thận khi cầm bo mạch và tuân thủ quy định an toàn về phóng tĩnh điện (ESD) bằng cách nối đất hoặc sử dụng vòng đeo tay chống tĩnh điện (ESD) để tránh làm hỏng các linh kiện nhạy cảm.


### Kết nối với máy tính xách tay của bạn


Sử dụng cáp USB-C có khả năng truyền dữ liệu, kết nối bo mạch LilyGO với máy tính xách tay của bạn. Kết nối này sẽ cung cấp nguồn điện và cho phép bạn flash firmware.


Khi khởi động, bạn sẽ thấy màn hình sau:


![image](assets/fr/06.webp)



Khi bật nguồn, LilyGO sẽ hiển thị màn hình thử nghiệm màu, chuyển đổi qua các màu đơn sắc. Điều này xác nhận màn hình và bo mạch hoạt động bình thường trước khi flash firmware.


Sau khi quá trình kiểm tra màu hoàn tất, màn hình sẽ chuyển sang trạng thái mặc định, cho biết bo mạch đã sẵn sàng cho các bước tiếp theo trong quy trình xây dựng.


![image](assets/fr/07.webp)


## Cách dễ dàng hay cách Hard


Có hai cách chính để flash firmware phần cứng wallet của bạn: cách dễ và cách khó. Cách dễ sử dụng các công cụ được cấu hình sẵn hoặc trình flash dựa trên web, tự động tải firmware vào thiết bị của bạn với thao tác tối thiểu. Phương pháp này lý tưởng cho người mới bắt đầu muốn nhanh chóng hoặc muốn tránh sự phức tạp của việc gỡ lỗi và tương tác dòng lệnh. Nó đơn giản hóa quy trình và giúp bạn khởi động và chạy nhanh hơn, giúp những người mới làm quen với phát triển nhúng hoặc ví phần cứng dễ dàng tiếp cận.


Mặt khác, phương pháp khó khăn hơn là sử dụng thủ công các công cụ dòng lệnh để flash firmware. Phương pháp này yêu cầu xác minh chữ ký và tổng kiểm tra firmware để đảm bảo tính xác thực và toàn vẹn, giúp bạn hiểu sâu hơn về quy trình flash và cách firmware tương tác với phần cứng. Mặc dù đòi hỏi nhiều công sức và sự quen thuộc hơn với các lệnh đầu cuối, nhưng nó mang lại khả năng kiểm soát, tính minh bạch và sự tin tưởng cao hơn vào bảo mật thiết bị của bạn.


Mỗi phương pháp đều có những đánh đổi riêng: cách dễ dàng đòi hỏi sự tin tưởng và hiểu biết nhất định để đổi lấy tốc độ và sự tiện lợi, trong khi cách khó đòi hỏi nhiều thời gian và kỹ năng chuyên môn hơn nhưng bù lại bạn sẽ có được sự linh hoạt và nắm bắt công nghệ nền tảng tốt hơn. Giảng viên nên khuyến khích học viên lựa chọn con đường phù hợp nhất với mức độ thoải mái và sự tò mò của mình, từ đó nuôi dưỡng sự tự tin và khả năng khám phá.


## Cách dễ dàng


Cách dễ nhất để flash ESP32



- Truy cập trang Github chính thức của Blockstream: [https://github.com/Blockstream/jadediyflasher](https://github.com/Blockstream/jadediyflasher)


![image](assets/fr/08.webp)



- Bạn có thể tải xuống tệp nguồn và chạy trang web cục bộ, nhưng GitHub đã lưu trữ tệp này tại [https://blockstream.github.io/jadediyflasher/](https://blockstream.github.io/jadediyflasher/). GitHub cung cấp HTML, CSS, JavaScript, v.v. trực tiếp cho trình duyệt của bạn để bạn có thể flash thiết bị mà không cần cài đặt công cụ dành cho nhà phát triển.


![image](assets/fr/09.webp)



- Mở menu thả xuống (có thể mặc định là `M5Stack Core2`) và chọn bo mạch phát triển của bạn — đối với lớp này, hãy chọn `LILYGO T-Display`.


![image](assets/fr/10.webp)



- Khi bạn nhấp vào Flash, thông báo này sẽ xuất hiện. Để biết thiết bị nào là LILYGO, hãy rút phích cắm của Lilygo và cắm lại. Cổng COM mà Lilygo đang kết nối sẽ hiện ra và biến mất. Nhấp vào cổng COM mà Jade đang kết nối.


![image](assets/fr/11.webp)



- Đó là thanh tiến trình sẽ xuất hiện và khi hoàn tất, bạn đã sẵn sàng để thiết lập.


## Thiết lập Jade Wallet


Sau khi flash firmware thành công, LilyGO T-Display của bạn giờ đây đã là một thiết bị Jade wallet hoàn chỉnh. Phần này sẽ hướng dẫn bạn quy trình thiết lập ban đầu, từ việc tạo cụm từ seed đến kết nối thiết bị với phần mềm wallet như Sparrow hoặc ứng dụng di động Blockstream Green.


### Khởi động ban đầu và thiết lập thiết bị



- Bật thiết bị:** Khi LilyGO vẫn được kết nối với máy tính xách tay qua cổng USB-C, firmware Jade sẽ tự động khởi động. Bạn sẽ thấy logo Jade xuất hiện trên màn hình.



- Vào chế độ thiết lập:** Thiết bị sẽ hiển thị menu ban đầu. Sử dụng hai nút vật lý trên bảng để điều hướng:
 - Nút bên trái:** Di chuyển lên/lùi
 - Nút bên phải:** Di chuyển xuống/tiến lên
 - Cả hai nút cùng lúc:** Chọn/xác nhận



- Chọn "Thiết lập":** Điều hướng đến tùy chọn Thiết lập và nhấn cả hai nút để xác nhận. Thiết bị sẽ hướng dẫn bạn thực hiện quy trình cấu hình ban đầu.


### Tạo Wallet của bạn



- Chọn "Bắt đầu thiết lập":** Thiết bị sẽ nhắc bạn bắt đầu quá trình tạo wallet. Xác nhận lựa chọn của bạn.



- Chọn "Tạo Wallet mới":** Bạn sẽ thấy hai tùy chọn:
 - Tạo Wallet mới:** Tạo cụm từ seed mới (chọn cụm từ này cho hội thảo)
 - Khôi phục Wallet:** Khôi phục wallet hiện có từ cụm từ seed (dành cho người dùng nâng cao)



- Chọn "Tạo Wallet mới" và xác nhận.



- Tạo entropy:** Thiết bị sẽ sử dụng bộ tạo số ngẫu nhiên để tạo entropy mật mã. Quá trình này mất vài giây vì thiết bị sẽ thu thập dữ liệu ngẫu nhiên từ nhiều nguồn.


### Ghi lại cụm từ hạt giống của bạn



- Viết lại cụm từ seed của bạn:** Thiết bị sẽ hiển thị cụm từ BIP39 seed gồm 12 từ, từng từ một. Đây là bước quan trọng nhất trong toàn bộ quy trình.


**Các biện pháp bảo mật quan trọng:**


- Viết rõ ràng từng từ trên giấy (sử dụng thẻ cụm từ seed được cung cấp nếu có)
- Kiểm tra lại từng từ khi bạn viết nó
- Không bao giờ chụp ảnh cụm từ seed bằng điện thoại của bạn
- Không bao giờ nhập các từ vào bất kỳ máy tính hoặc điện thoại nào
- Giữ cụm từ seed của bạn ở chế độ riêng tư—không chia sẻ màn hình hoặc cho người khác xem



- Xác minh cụm từ seed của bạn:** Sau khi ghi lại đủ 12 từ, thiết bị sẽ yêu cầu bạn xác nhận một số từ trong cụm từ để đảm bảo bạn đã ghi lại chính xác. Sử dụng các nút để chọn từ đúng cho mỗi lời nhắc.


**Mẹo hay:** Trước khi chuyển sang phần tiếp theo, hãy luyện đọc lại cụm từ seed của bạn thành tiếng (nhỏ nhẹ để người khác không nghe thấy). Điều này giúp phát hiện bất kỳ lỗi viết tay hoặc sự mơ hồ nào.


### Phương pháp kết nối



- Chọn loại kết nối:** Phần mềm Jade hỗ trợ hai phương thức kết nối:
 - USB:** Kết nối có dây qua cáp USB-C (khuyến nghị cho hội thảo này)
 - Bluetooth:** Kết nối không dây với các thiết bị di động



- Hãy chọn **USB** ngay bây giờ vì đây là tùy chọn đơn giản nhất cho phần mềm wallet trên máy tính để bàn và không tạo ra các vectơ tấn công không dây.



- Đặt tên thiết bị:** Jade sẽ hiển thị một mã định danh duy nhất, chẳng hạn như "Connect Jade A7D924". Mã định danh này giúp bạn phân biệt giữa nhiều ví phần cứng nếu bạn tạo nhiều hơn một ví. Hãy ghi lại mã định danh này nếu cần.


### Kết nối với phần mềm Wallet


Giờ đây, bạn có hai lựa chọn chính để kết nối với phần cứng wallet mới tạo: ứng dụng di động Blockstream Green (dùng khi di chuyển) hoặc Sparrow Wallet (dùng cho máy tính để bàn với các tính năng nâng cao hơn). Trong buổi hội thảo này, chúng ta sẽ tập trung vào Sparrow Wallet, vì nó cung cấp khả năng hiển thị tốt hơn các chi tiết kỹ thuật của giao dịch Bitcoin.


#### Tùy chọn 1: Ứng dụng di động Blockstream Green (Khởi động nhanh)


Nếu bạn muốn kiểm tra thiết bị của mình nhanh chóng bằng thiết bị di động:



- Tải xuống ứng dụng **Blockstream Green** từ App Store (iOS) hoặc Google Play (Android)
- Mở ứng dụng và chọn "Kết nối Hardware Wallet"
- Chọn "Jade" từ danh sách các thiết bị được hỗ trợ
- Cắm Jade vào điện thoại bằng cáp USB-C sang USB-C (hoặc bộ chuyển đổi USB-C sang Lightning cho iPhone 15 trở lên)
- Làm theo lời nhắc trên màn hình để kết nối và tạo wallet đầu tiên của bạn


**Lưu ý về Liquid:** Ứng dụng Blockstream Green hỗ trợ cả Bitcoin và Liquid (một sidechain Bitcoin). Nếu bạn đang sử dụng các tính năng của Liquid, bạn có thể được nhắc "Xuất khóa che giấu chính"—điều này cho phép ứng dụng xem số tiền giao dịch trên mạng Liquid, vốn là thông tin bảo mật. Trong buổi hội thảo này, bạn có thể bỏ qua các tính năng của Liquid và tập trung vào các giao dịch Bitcoin tiêu chuẩn.


#### Lựa chọn 2: Sparrow Wallet (Khuyến nghị cho Xưởng)


Sparrow Wallet là ứng dụng máy tính để bàn mạnh mẽ giúp bạn kiểm soát chi tiết các giao dịch Bitcoin và kết nối liền mạch với phần cứng Jade wallet của bạn.


**Cài đặt:**



- Tải xuống Sparrow Wallet từ trang web chính thức: [sparrowwallet.com](https://sparrowwallet.com)
- Xác minh chữ ký tải xuống (xem tài liệu Sparrow để biết chi tiết)
- Cài đặt và khởi chạy ứng dụng


**Kết nối Jade của bạn với Sparrow:**



- Trong Sparrow, hãy vào **Tệp → Wallet mới**
- Đặt tên cho wallet của bạn (ví dụ: "My Jade Wallet")
- Nhấp vào **Hardware Wallet đã kết nối**
- Sparrow sẽ tự động phát hiện thiết bị Jade được cắm vào của bạn
- Nếu được nhắc, hãy xác nhận kết nối trên màn hình Jade bằng cách nhấn cả hai nút
- Chọn loại tập lệnh mong muốn của bạn:
 - Native Segwit (P2WPKH):** Được khuyến nghị cho người mới bắt đầu—phí thấp nhất, khả năng tương thích rộng nhất với các ví hiện đại
 - Segwit lồng nhau (P2SH-P2WPKH):** Để tương thích với các dịch vụ cũ hơn
 - Taproot (P2TR):** Tiên tiến nhất, cung cấp quyền riêng tư tốt nhất và mức phí thấp nhất, nhưng yêu cầu hỗ trợ wallet tiên tiến
- Nhấp vào **Nhập kho khóa** để hoàn tất kết nối


**Cấu hình kết nối máy chủ của Sparrow:**


Trước khi bạn có thể xem số dư hoặc giao dịch phát sóng, Sparrow cần kết nối với một nút Bitcoin để lấy dữ liệu blockchain. Bạn có một số lựa chọn, mỗi lựa chọn đều có những đánh đổi khác nhau giữa sự tiện lợi, quyền riêng tư và sự tin cậy:



- Electrum Server công cộng (Dễ nhất, ít riêng tư nhất):** Kết nối với máy chủ công cộng do bên thứ ba vận hành. Thiết lập nhanh chóng, nhưng máy chủ có thể thấy địa chỉ wallet của bạn và có khả năng liên kết chúng với địa chỉ IP của bạn. Thích hợp để thử nghiệm trên mạng thử nghiệm.
 - Trong Sparrow, hãy vào **Công cụ → Tùy chọn → Máy chủ**
 - Chọn **Máy chủ công cộng** và chọn một máy chủ từ danh sách
 - Nhấp vào **Kiểm tra kết nối** để xác minh



- Nút Bitcoin Core hoặc Knots (Riêng tư nhất, hoạt động hiệu quả nhất):** Chạy nút Bitcoin đầy đủ của riêng bạn. Đây là tiêu chuẩn vàng cho quyền riêng tư và xác minh, vì bạn tự xác thực mọi giao dịch và không tin tưởng máy chủ của bất kỳ ai khác. Tuy nhiên, bạn cần tải xuống toàn bộ blockchain (~600GB) và đồng bộ hóa nút của mình.
 - Cài đặt và đồng bộ Bitcoin Core hoặc Knots
 - Trong Sparrow, hãy vào **Công cụ → Tùy chọn → Máy chủ**
 - Chọn **Bitcoin Core hoặc Knots** và nhập thông tin kết nối của nút của bạn



- Riêng tư Electrum Server (Cân bằng tốt):** Lưu trữ máy chủ Electrum của riêng bạn (như Fulcrum hoặc Electrs) được kết nối với nút Bitcoin Core hoặc Knots của bạn. Cung cấp quyền riêng tư hoàn toàn mà không cần chạy Sparrow trên cùng máy với nút của bạn.
 - Thiết lập máy chủ Electrum trỏ đến nút Bitcoin Core hoặc Knots của bạn
 - Trong Sparrow, hãy vào **Công cụ → Tùy chọn → Máy chủ**
 - Chọn **Private Electrum** và nhập URL máy chủ của bạn


Đối với hội thảo này, việc sử dụng **Public Electrum Server** là hoàn toàn phù hợp cho các giao dịch trên mạng thử nghiệm. Trong môi trường sản xuất với nguồn vốn thực tế, bạn nên cân nhắc việc chạy node riêng hoặc sử dụng máy chủ riêng đáng tin cậy để đảm bảo quyền riêng tư tối đa.


#### Tùy chọn 3: Ứng dụng máy tính để bàn Blockstream Green (Khởi động nhanh)


Blockstream Green là phần mềm để hoàn tất việc thiết lập JadeDIY và phải có phiên bản dành cho máy tính để bàn



- Tải ứng dụng Blockstream chính thức — đây là liên kết đến ứng dụng từ trang web của họ. Khi bạn truy cập vào đó, hãy nhấp vào [Tải xuống ngay](https://blockstream.com/app/).


![image](assets/fr/12.webp)



- Tùy thuộc vào nơi lưu trữ tệp tải xuống, nhiều khả năng tệp sẽ nằm trong thư mục Tải xuống. Hãy kiểm tra thư mục đó và nhấp đúp vào tệp thực thi để cài đặt phần mềm.


![image](assets/fr/13.webp)



- Bạn có thể phải cấp quyền quản trị để chạy trình cài đặt. Sau đó, một cửa sổ sẽ bật lên trông giống như hình ảnh sau — nhấp vào **Tiếp theo**.


![image](assets/fr/14.webp)



- Chọn nơi bạn muốn lưu trữ ứng dụng đã cài đặt (nơi có các chương trình khác hoặc nơi dễ tìm), sau đó nhấp vào **Tiếp theo**.


![image](assets/fr/15.webp)



- Trình cài đặt sẽ yêu cầu nhập tên phím tắt. Nhập tên hoặc giữ nguyên tên mặc định, sau đó nhấp vào **Tiếp theo**.


![image](assets/fr/16.webp)



- Nếu bạn muốn có lối tắt trên màn hình, hãy đánh dấu vào ô; nếu không, hãy nhấp vào **Tiếp theo**.


![image](assets/fr/17.webp)



- Cuối cùng, nhấp vào **Cài đặt** và đợi vài phút để quá trình cài đặt hoàn tất.


![image](assets/fr/18.webp)



- Thanh tiến trình sẽ đầy đến hết.


![image](assets/fr/19.webp)



- Khi hoàn tất, một trang mới sẽ xuất hiện — nhấp vào **Hoàn tất**.


![image](assets/fr/20.webp)



- Tìm ứng dụng Blockstream mới cài đặt của bạn (ví dụ hiển thị trong menu Bắt đầu của Windows 11).


![image](assets/fr/21.webp)



- Khi tìm thấy, hãy nhấp để khởi chạy — màn hình chào mừng sẽ xuất hiện.


### Xác minh thiết lập của bạn


Sau khi kết nối với Sparrow (hoặc ứng dụng wallet khác):



- Kiểm tra địa chỉ của bạn:** Sparrow sẽ hiển thị địa chỉ nhận được lấy từ cụm từ seed của bạn. Bạn có thể xác minh địa chỉ trên thiết bị Jade bằng cách vào tab "Nhận" trong Sparrow và nhấp vào "Hiển thị Address"—địa chỉ sẽ hiển thị trên cả màn hình máy tính và màn hình Jade.



- Tạo địa chỉ nhận:** Nhấp vào tab **Nhận** trong Sparrow và sao chép địa chỉ nhận Bitcoin đầu tiên của bạn.



- Sẵn sàng cho giao dịch:** Phần cứng wallet của bạn hiện đã được cấu hình đầy đủ và sẵn sàng để tiếp nhận và ký các giao dịch Bitcoin. Hãy chuyển sang phần tiếp theo để thực hành ký giao dịch testnet.



---

### Danh sách kiểm tra thiết lập nhanh



- Phần mềm Jade khởi động thành công
- wallet mới được tạo bằng cụm từ seed gồm 12 từ
- Cụm từ hạt giống được viết rõ ràng và đã được xác minh
- Đã chọn chế độ kết nối USB
- Phần mềm Wallet (Sparrow) đã được cài đặt và kết nối
- Kết nối máy chủ đã được cấu hình (Electrum công khai cho mainnet)
- Địa chỉ nhận đầu tiên được tạo và xác minh trên thiết bị



---

**Giấy phép MIT**


**Bản quyền (c) 2025 Mạng lưới Bitcoin NYC**


Theo đây, bất kỳ cá nhân nào có được bản sao của phần mềm này và các tệp tài liệu liên quan ("Phần mềm") đều được cấp quyền sử dụng Phần mềm này mà không bị hạn chế, bao gồm nhưng không giới hạn ở quyền sử dụng, sao chép, sửa đổi, hợp nhất, xuất bản, phân phối, cấp phép phụ và/hoặc bán các bản sao của Phần mềm, và cho phép những người được cung cấp Phần mềm làm như vậy, tuân theo các điều kiện sau:


Thông báo bản quyền ở trên và thông báo cấp phép này phải được đưa vào tất cả các bản sao hoặc phần quan trọng của Phần mềm.


PHẦN MỀM ĐƯỢC CUNG CẤP "NGUYÊN TRẠNG", KHÔNG CÓ BẤT KỲ BẢO HÀNH NÀO, DÙ RÕ RÀNG HAY NGỤ Ý, BAO GỒM NHƯNG KHÔNG GIỚI HẠN Ở CÁC BẢO HÀNH VỀ KHẢ NĂNG THƯƠNG MẠI, TÍNH PHÙ HỢP CHO MỘT MỤC ĐÍCH CỤ THỂ VÀ KHÔNG VI PHẠM. TRONG MỌI TRƯỜNG HỢP, TÁC GIẢ HOẶC NGƯỜI CÓ BẢN QUYỀN SẼ KHÔNG CHỊU TRÁCH NHIỆM ĐỐI VỚI BẤT KỲ KHIẾU NẠI, THIỆT HẠI HOẶC TRÁCH NHIỆM PHÁP LÝ NÀO KHÁC, DÙ LÀ TRONG HÀNH ĐỘNG HỢP ĐỒNG, HÀNH VI PHẠM PHÁP LÝ HOẶC CÁC TRƯỜNG HỢP KHÁC, PHÁT SINH TỪ, DO HOẶC LIÊN QUAN ĐẾN PHẦN MỀM HOẶC VIỆC SỬ DỤNG HOẶC CÁC GIAO DỊCH KHÁC TRONG PHẦN MỀM.


---