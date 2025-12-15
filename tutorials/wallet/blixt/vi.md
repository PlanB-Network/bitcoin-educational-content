---
name: Blixt Wallet
description: Làm thế nào để bắt đầu sử dụng nút LN mạnh mẽ trên thiết bị di động của bạn?
---
![cover](assets/cover.webp)


Hướng dẫn này dành cho tất cả người dùng mới muốn bắt đầu sử dụng Bitcoin Lightning Network (LN) theo cách MIỄN PHÍ MÃ NGUỒN MỞ, HOÀN TOÀN KHÔNG CÓ BẢO VỆ.


Sử dụng [Blixt Wallet](https://blixtwallet.com/), một nút LN đầy đủ trên thiết bị di động của bạn, bất kể bạn ở đâu.


Nếu bạn chưa từng sử dụng Bitcoin Lightning Network, trước khi bắt đầu, [vui lòng đọc phần giải thích đơn giản về phép loại suy Lightning Network (LN)](https://darth-coin.github.io/beginner/LN-airport-analogy-en.html).


## CÁC ĐIỀU QUAN TRỌNG:



- Blixt là một nút riêng tư, KHÔNG phải là một nút định tuyến! Hãy ghi nhớ điều đó: Điều đó có nghĩa là, tất cả các kênh LN trong Blixt sẽ không được thông báo đến biểu đồ LN (còn gọi là kênh riêng tư). Điều đó có nghĩa là, NÚT NÀY SẼ KHÔNG ĐỊNH TUYẾN các khoản thanh toán khác thông qua nút Blixt. Nút Blixt này KHÔNG dùng để định tuyến, tôi nhắc lại. Chủ yếu là để có thể quản lý các kênh LN của riêng bạn và thực hiện các khoản thanh toán LN của bạn một cách riêng tư, bất cứ khi nào bạn cần. Nút Blixt này cần phải trực tuyến và được đồng bộ hóa CHỈ TRƯỚC KHI bạn thực hiện giao dịch của mình. Đó là lý do tại sao bạn sẽ thấy một biểu tượng ở trên cùng cho biết trạng thái đồng bộ hóa. Chỉ mất vài phút, tùy thuộc vào thời gian bạn giữ nó ngoại tuyến.



- Blixt đang sử dụng LND (aezeed) làm backend Wallet, vì vậy đừng cố gắng nhập các loại ví Bitcoin khác vào đó. [Tại đây, bạn đã giải thích các loại hạt giống Wallet Mnemonic](https://coldbit.com/what-types-of-Mnemonic-seeds-are-used-in-Bitcoin/). Và đây là [danh sách mở rộng hơn về tất cả các loại ví](https://walletsrecovery.org/). Vì vậy, nếu trước đây bạn đã có một nút LND, bạn có thể nhập seed và backup.channels vào Blixt, [như được giải thích trong hướng dẫn này](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html).



- Ở cuối hướng dẫn này, bạn sẽ tìm thấy một phần đặc biệt với ["mẹo và thủ thuật"](https://darth-coin.github.io/wallets/getting-started-blixt-Wallet-en.html#tips)



- Blixt các liên kết quan trọng - xem chúng ở cuối hướng dẫn này, vui lòng đánh dấu chúng.


---

## Blixt - Tiếp xúc đầu tiên


Vậy thì… Mẹ của Darth quyết định bắt đầu sử dụng LN với Blixt. Quyết định Hard, nhưng khôn ngoan. Blixt chỉ dành cho những người thông minh và những người thực sự muốn tìm hiểu thêm, sử dụng sâu LN.


![blixt](assets/en/01.webp)


Darth cảnh báo mẹ mình:


"*Mẹ ơi, nếu mẹ bắt đầu sử dụng Blixt LN Node, trước tiên mẹ cần biết Lightning Network là gì và nó hoạt động như thế nào, ít nhất là ở mức cơ bản. [Ở đây, con đã tổng hợp một danh sách đơn giản các tài nguyên về Lightning Network](https://blixtwallet.github.io/faq#what-is-LN). Mẹ hãy đọc chúng trước nhé.*"


Mẹ của Darth đã đọc các tài nguyên và thực hiện bước đầu tiên: cài đặt Blixt trên thiết bị Android hoàn toàn mới của bà. Blixt cũng khả dụng cho iOS và macOS (máy tính để bàn). Nhưng những ứng dụng đó không dành cho mẹ của Darth… Tuy nhiên, nên sử dụng phiên bản Android mới hơn, ít nhất là 9 hoặc 10 để có khả năng tương thích và trải nghiệm tốt hơn. Chạy một nút LN đầy đủ trên thiết bị di động không phải là một nhiệm vụ dễ dàng và có thể chiếm một số dung lượng (tối thiểu 600MB) và bộ nhớ.


Sau khi bạn mở Blixt, màn hình “Chào mừng” sẽ cung cấp cho bạn một số tùy chọn:


![blixt](assets/en/02.webp)


Ở góc trên bên phải, bạn sẽ thấy 3 dấu chấm kích hoạt menu với:



- “bật Tor” - người dùng có thể bắt đầu với mạng Tor, đặc biệt nếu muốn khôi phục một nút LND cũ đang chạy với các đối tác chỉ có Tor.
- “Set Bitcoin node” - nếu người dùng muốn kết nối trực tiếp đến node của mình, để đồng bộ các khối thông qua Neutrino, có thể thực hiện ngay từ màn hình chào mừng. Tùy chọn này cũng tốt trong trường hợp kết nối internet hoặc Tor của bạn không ổn định để kết nối đến node Bitcoin mặc định (node.blixtwallet.com).
- Sẽ sớm thêm ngôn ngữ vào đó, vì vậy người dùng có thể bắt đầu ngay với ngôn ngữ mà họ thấy thoải mái. Nếu bạn muốn đóng góp cho dự án nguồn mở này bằng bản dịch sang các ngôn ngữ khác, [vui lòng tham gia tại đây](https://explore.transifex.com/blixt-Wallet/blixt-Wallet/).


### TÙY CHỌN A - Tạo Wallet mới


Nếu bạn chọn “tạo Wallet mới”, bạn sẽ được chuyển hướng thẳng đến màn hình chính của Blixt Wallet.


Đây là “buồng lái” của bạn và cũng là “Main LN Wallet”, vì vậy hãy lưu ý, nó sẽ chỉ hiển thị cho bạn số dư của LN Wallet của bạn. Wallet trên chuỗi được hiển thị riêng (xem C).


![blixt](assets/en/03.webp)


A - Biểu tượng chỉ báo đồng bộ hóa khối Blixt. Đây là điều quan trọng nhất đối với một nút LN: được đồng bộ hóa với mạng. Nếu biểu tượng đó vẫn còn hoạt động, nghĩa là nút của bạn CHƯA SẴN SÀNG! Vì vậy, hãy kiên nhẫn, đặc biệt là đối với lần đồng bộ hóa ban đầu đầu tiên. Có thể mất tới 6-8 phút, tùy thuộc vào thiết bị và kết nối internet của bạn.


Bạn có thể nhấp vào đó và xem trạng thái đồng bộ hóa:


![blixt](assets/en/04.webp)


Bạn cũng có thể nhấp vào nút “Show LND Log” (A) nếu bạn muốn xem và đọc thêm thông tin chi tiết kỹ thuật của nhật ký LND theo thời gian thực. Rất hữu ích để gỡ lỗi và tìm hiểu thêm về cách LN hoạt động.


B - Tại đây, bạn có thể truy cập tất cả các Cài đặt Blixt và rất nhiều! Blixt cung cấp nhiều tính năng và tùy chọn phong phú để quản lý nút LN của bạn như một chuyên gia. Tất cả các tùy chọn đó đều được giải thích chi tiết trong “[Trang tính năng Blixt](https://blixtwallet.github.io/features#blixt-options) - Menu Tùy chọn”.


C - Tại đây bạn có menu “Magic Drawer”, [cũng được giải thích chi tiết tại đây](https://blixtwallet.github.io/features#blixt-drawer). Đây là “Onchain Wallet” (B), Lightning Channels (C), Contacts, biểu tượng trạng thái Channels (A), Keysend (D).


![blixt](assets/en/05.webp)


D - Là menu trợ giúp, có liên kết đến trang Câu hỏi thường gặp/Hướng dẫn, liên hệ với nhà phát triển, trang Github và nhóm hỗ trợ Telegram.


E - Chỉ ra BTC Address đầu tiên của bạn, nơi bạn có thể gửi Sats thử nghiệm đầu tiên của mình. ĐIỀU NÀY LÀ TÙY CHỌN! Nếu bạn gửi thẳng vào Address đó, sẽ mở một kênh LN hướng đến Blixt Node. Điều đó có nghĩa là bạn sẽ thấy Sats đã gửi của mình, đi vào một giao dịch onchain (tx) khác, để mở kênh LN đó. Bạn có thể kiểm tra điều đó trong Blixt onchain Wallet (xem điểm C), nhấp vào menu TX trên cùng bên phải.


![blixt](assets/en/06.webp)


Như bạn có thể thấy trong Nhật ký giao dịch Onchain, các bước rất chi tiết chỉ ra nơi Sats sẽ đến (gửi tiền, mở, đóng kênh).


SỰ GIỚI THIỆU:


Sau khi thử nghiệm một số tình huống, chúng tôi đi đến kết luận rằng mở các kênh giữa 1 và 5 M Sats hiệu quả hơn nhiều. Các kênh nhỏ hơn có xu hướng cạn kiệt nhanh chóng và phải trả mức phí cao hơn so với các kênh lớn hơn.


F - Chỉ ra số dư Lightning Wallet chính của bạn. Đây KHÔNG phải là số dư Blixt Wallet tổng thể của bạn, nó chỉ đại diện cho Sats bạn có trong Lightning Channels, có thể gửi. Như đã chỉ ra trước đó, Onchain Wallet là riêng biệt. Hãy ghi nhớ khía cạnh này. Onchain Wallet là riêng biệt vì một lý do quan trọng: nó chủ yếu được sử dụng để mở/đóng các kênh LN.


Được rồi, vậy thì giờ Darth’s Mom đã gửi một số Sats vào Address trên chuỗi được hiển thị trên màn hình chính. Khi bạn làm như vậy, bạn nên giữ ứng dụng Blixt của mình trực tuyến và hoạt động trong một thời gian, cho đến khi giao dịch BTC được thợ đào đưa vào khối đầu tiên.


Sau đó có thể mất đến 20-30 phút cho đến khi được xác nhận đầy đủ và kênh mở và bạn sẽ thấy nó trong Magic Drawer - Lightning Channels là đang hoạt động. Ngoài ra, chấm màu nhỏ ở trên cùng của ngăn kéo, nếu là Green sẽ chỉ ra rằng kênh LN của bạn đang trực tuyến và sẵn sàng để sử dụng để gửi Sats qua LN.


Address và tin nhắn chào mừng hiển thị sẽ biến mất. Bây giờ không cần phải mở kênh tự động nữa. Bạn cũng có thể hủy kích hoạt tùy chọn trong menu Cài đặt.


Đã đến lúc tiếp tục, thử nghiệm các tính năng và tùy chọn khác để mở kênh LN.


Bây giờ, hãy mở một kênh khác với một node ngang hàng khác. Cộng đồng Blixt đã cùng nhau đưa ra [danh sách các node tốt để bắt đầu sử dụng với Blixt](https://github.com/hsjoberg/blixt-Wallet/issues/1033).


**Quy trình mở kênh LN trong Blixt**


Điều này rất đơn giản, chỉ cần thực hiện vài bước và một chút kiên nhẫn:



- Đã đến danh sách đồng nghiệp của [Cộng đồng Blixt](https://github.com/hsjoberg/blixt-Wallet/issues/1033)
- Chọn một nút và nhấp vào liên kết tiêu đề tên của nó, nó sẽ mở trang Amboss của nó
- Nhấp để hiển thị mã QR cho nút URI Address


![blixt](assets/en/07.webp)


Mở Blixt và đi đến ngăn kéo trên cùng - Kênh Lightning và nhấp vào nút “+”


![blixt](assets/en/08.webp)


Bây giờ, hãy nhấp vào camera (A) để quét mã QR từ trang Amboss và các chi tiết về nút sẽ được điền vào. Thêm số tiền Sats cho kênh bạn muốn và sau đó chọn mức phí cho giao dịch. Bạn có thể để tự động (B) để xác nhận nhanh hơn hoặc điều chỉnh thủ công bằng cách trượt nút. Bạn cũng có thể nhấn và giữ số và chỉnh sửa theo ý muốn.


Không đặt ít hơn 1 sat/vbyte! Thường thì tốt hơn là nên tham khảo [phí Mempool](https://Mempool.space/) trước khi mở kênh và chọn mức phí thuận tiện.


Xong, bây giờ chỉ cần nhấp vào nút “mở kênh” và đợi 3 lần xác nhận, thường mất 30 phút (khoảng 1 khối mỗi 10 phút).


Sau khi xác nhận, bạn sẽ thấy kênh đang hoạt động trong phần “Kênh Lightning”.


---

## Blixt - Liên lạc lần thứ hai


Được rồi, bây giờ chúng ta có kênh LN chỉ có thanh khoản OUTBOURGE. Điều đó có nghĩa là chúng ta chỉ có thể GỬI, chúng ta vẫn không thể NHẬN Sats qua LN.


![blixt](assets/en/09.webp)


Tại sao? Bạn đã đọc hướng dẫn được chỉ ra ở phần đầu chưa? Chưa? Hãy quay lại và đọc chúng. Điều rất quan trọng là phải hiểu cách kênh LN hoạt động.


![blixt](assets/en/10.webp)


Như bạn có thể thấy trong ví dụ này, kênh mở với khoản tiền gửi đầu tiên không có quá nhiều thanh khoản ĐẾN (“Có thể nhận”) nhưng có rất nhiều thanh khoản ĐI (“Có thể gửi”).


Vậy bạn có những lựa chọn nào nếu muốn nhận được nhiều Sats hơn LN?



- Chi tiêu một số Sats từ kênh hiện có. Đúng vậy, LN là mạng lưới thanh toán của Bitcoin, chủ yếu được sử dụng để chi tiêu Sats của bạn nhanh hơn, rẻ hơn, riêng tư và dễ dàng hơn. LN KHÔNG phải là cách hodling, vì vậy bạn có Wallet trên chuỗi.



- Hoán đổi một số Sats, trở lại Wallet trên chuỗi của bạn, bằng cách sử dụng dịch vụ hoán đổi ngầm. Theo cách này, bạn không chi tiêu Sats của mình mà trả lại cho Wallet trên chuỗi của riêng bạn. Tại đây, bạn có thể xem chi tiết một số phương pháp, trong [Trang hướng dẫn Blixt](https://blixtwallet.github.io/guides).



- Mở một kênh INBOUND từ bất kỳ nhà cung cấp LSP nào. Đây là video demo về cách sử dụng LSP LNBig để mở một kênh inbound. Điều đó có nghĩa là bạn sẽ trả một khoản phí nhỏ cho một kênh EMPTY (về phía bạn) và bạn sẽ có thể nhận được nhiều Sats hơn vào kênh đó. Nếu bạn là một thương gia nhận được nhiều hơn số tiền chi tiêu, thì đó là một lựa chọn tốt. Ngoài ra, nếu bạn đang mua Sats thay vì LN, sử dụng Robosats hoặc bất kỳ LN Exchange nào khác.



- Mở một kênh Dunder, với nút Blixt hoặc bất kỳ nhà cung cấp Dunder LSP nào khác. Kênh Dunder là một cách đơn giản để có được một số thanh khoản ĐẾN, nhưng đồng thời bạn gửi một số Sats vào kênh đó. Cũng tốt vì nó sẽ mở kênh bằng một [UTXO](https://en.Bitcoin.it/wiki/UTXO) không phải từ Blixt Wallet của bạn. Điều đó thêm một số quyền riêng tư. Cũng tốt vì, nếu bạn không có Sats vào Wallet trên chuỗi, để mở một kênh LN bình thường, nhưng bạn có chúng vào một LN Wallet khác, bạn chỉ có thể trả từ Wallet khác đó thông qua LN để mở và gửi tiền (về phía bạn) của kênh Dunder đó. [Thông tin chi tiết hơn về cách Dunder hoạt động và cách chạy máy chủ của riêng bạn tại đây](https://github.com/hsjoberg/dunder-lsp).


![blixt](assets/en/11.webp)


Sau đây là các bước để kích hoạt mở kênh Dunder:



- Vào Cài đặt, trong phần “Thử nghiệm”, kích hoạt hộp “Bật Dunder LSP”.
- Sau khi thực hiện xong, hãy quay lại phần “Lightning Network” và bạn sẽ thấy tùy chọn “Đặt máy chủ LSP Dunder” xuất hiện. Theo mặc định, tùy chọn này được đặt là “https://dunder.blixtwallet.com” nhưng bạn có thể thay đổi tùy chọn này bằng bất kỳ nhà cung cấp LSP Dunder nào khác Address. [Đây là danh sách cộng đồng Blixt](https://github.com/hsjoberg/blixt-Wallet/issues/1033) với các nút có thể cung cấp kênh LSP Dudner cho Blixt của bạn.
- Bây giờ bạn có thể vào màn hình chính và nhấp vào nút “Nhận”. Sau đó làm theo quy trình này [được giải thích trong hướng dẫn này](https://blixtwallet.github.io/guides#guide-lsp).


Được rồi, sau khi kênh Dunder được xác nhận (sẽ mất vài phút), bạn sẽ có 2 kênh LN: một kênh được mở ban đầu bằng chế độ lái tự động (kênh A) và một kênh có nhiều thanh khoản hơn, được mở bằng Dunder (kênh B).


![blixt](assets/en/12.webp)


Tốt, bây giờ bạn đã có thể gửi và nhận đủ Sats so với LN!


CHÚC MỪNG Bitcoin LIGHTNING!


---

## Blixt - Liên lạc lần thứ ba


Hãy nhớ rằng, trong chương một “Liên hệ đầu tiên” có 2 tùy chọn trên màn hình Chào mừng:


- [Tùy chọn A](https://darth-coin.github.io/wallets/getting-started-blixt-Wallet-en.html#option-a) - Tạo Wallet mới
- Tùy chọn B - Khôi phục Wallet


Bây giờ chúng ta hãy thảo luận về cách khôi phục Blixt Wallet hoặc bất kỳ nút nào khác bị sập LND. Điều này hơi kỹ thuật hơn một chút, nhưng hãy chú ý. Không phải là Hard sao.


### TÙY CHỌN B - Khôi phục Wallet


Trước đây, tôi đã viết một hướng dẫn chuyên sâu về [cách khôi phục nút Umbrel bị sập](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html), trong đó tôi cũng đề cập đến phương pháp sử dụng Blixt làm quy trình khôi phục nhanh, bằng cách sử dụng tệp seed + channel.backup từ Umbrel.


Tôi cũng đã viết hướng dẫn về cách khôi phục nút Blixt hoặc di chuyển Blixt của bạn sang thiết bị khác, [tại đây](https://blixtwallet.github.io/faq#blixt-restore).


![blixt](assets/en/13.webp)


Nhưng chúng ta hãy giải thích quy trình này theo các bước đơn giản. Như bạn có thể thấy trong hình ảnh trên, có 2 điều bạn nên làm để khôi phục nút Blixt/LND trước đó của mình:



- hộp trên cùng là nơi bạn phải điền tất cả 24 từ từ seed của bạn (nút cũ / chết)
- bên dưới là hai tùy chọn nút để chèn/tải lên tệp channel.backup, đã lưu trước đó từ nút Blixt/LND cũ của bạn. Tệp này có thể là tệp cục bộ (bạn đã tải tệp này lên thiết bị trước đó) hoặc có thể là tệp từ xa Google Drive/iCloud. Blixt có tùy chọn này để lưu bản sao lưu kênh của bạn trực tiếp vào Google Drive/iCloud Drive. Xem thêm chi tiết trong [Trang tính năng của Blixt](https://blixtwallet.github.io/features#blixt-options).


Tuy nhiên, nếu trước đây bạn không có bất kỳ kênh LN mở nào, thì không cần phải tải lên bất kỳ tệp channels.backup nào. Chỉ cần chèn 24 từ seed và nhấn nút khôi phục.


Đừng quên kích hoạt Tor, từ menu 3 chấm trên cùng, như chúng tôi đã giải thích trong phần Tùy chọn A. Đó là trường hợp khi bạn CHỈ có Tor ngang hàng và không thể liên lạc qua clearnet (tên miền/IP). Nếu không thì không cần thiết.


Một tính năng hữu ích khác là thiết lập một nút Bitcoin cụ thể từ menu trên cùng đó. Theo mặc định, nó đồng bộ các khối từ node.blixtwallet.com (chế độ neutrino) nhưng bạn có thể thiết lập bất kỳ nút Bitcoin nào khác cung cấp đồng bộ neutrino.


Vì vậy, sau khi bạn điền các tùy chọn đó và nhấn nút khôi phục, Blixt sẽ bắt đầu đồng bộ các khối thông qua Neutrino như chúng tôi đã giải thích trong chương First Contact. Vì vậy, hãy kiên nhẫn và theo dõi quá trình khôi phục trên màn hình chính bằng cách nhấp vào biểu tượng đồng bộ.


![blixt](assets/en/14.webp)


Như bạn có thể thấy trong ví dụ này, nó cho thấy các khối Bitcoin được đồng bộ hóa 100% (A) và quá trình khôi phục đang diễn ra (B). Điều đó có nghĩa là các kênh LN mà bạn đã có trước đó sẽ bị đóng và tiền được khôi phục vào Blixt onchain Wallet của bạn.


Quá trình này mất thời gian! Vì vậy, hãy kiên nhẫn và cố gắng giữ Blixt của bạn hoạt động và trực tuyến. Đồng bộ ban đầu có thể mất tới 6-8 phút và đóng kênh có thể mất tới 10-15 phút. Vì vậy, tốt hơn là bạn nên sạc thiết bị thật kỹ.


Sau khi quá trình này bắt đầu, bạn có thể kiểm tra trong Magic Drawer - Lightning Channels, trạng thái của từng kênh trước đó của bạn, hiển thị trạng thái "đang chờ đóng". Sau khi từng kênh đóng, bạn có thể thấy giao dịch đóng trong onchain Wallet (xem Magic Drawer - Onchain) và mở nhật ký menu tx.


![blixt](assets/en/15.webp)


Cũng sẽ tốt nếu kiểm tra và thêm nếu không có ở đó, các đồng nghiệp trước đây của bạn đã có trong nút LN cũ của bạn. Vì vậy, hãy vào menu Cài đặt, xuống “Lightning Network” và nhập vào tùy chọn “Hiển thị Lightning Peers”.


![blixt](assets/en/16.webp)


Bên trong phần này, bạn sẽ thấy các đối tác mà bạn đã kết nối vào thời điểm đó và bạn có thể thêm nhiều hơn, tốt hơn là thêm những đối tác mà bạn đã có kênh trước đó. Chỉ cần vào [Trang Amboss](https://amboss.space/), tìm kiếm các bí danh nút đối tác hoặc nodeID của bạn và quét URI nút của họ.


![blixt](assets/en/17.webp)


Như bạn có thể thấy trong hình ảnh trên, có 3 khía cạnh:


A - biểu thị nút clearnet Address URI (tên miền/IP)


B - biểu thị nút Tor onion Address URI (.onion)


C - là mã QR để quét bằng camera Blixt hoặc nút sao chép.


Bạn phải thêm URI Address của nút này vào danh sách các nút ngang hàng của bạn. Vì vậy, hãy lưu ý rằng chỉ tên bí danh nút hoặc nodeID là không đủ.


Bây giờ bạn có thể vào Magic Drawer (menu trên cùng bên trái) - Lightning Channels và bạn có thể xem số tiền sẽ được trả lại vào Address trên chuỗi của bạn ở độ cao khối đáo hạn nào.


![blixt](assets/en/18.webp)


Khối số 764272 là thời điểm tiền có thể sử dụng được trong Bitcoin onchain Address của bạn. Và có thể mất tới 144 khối từ khối xác nhận đầu tiên cho đến khi được giải phóng. [Vì vậy, hãy kiểm tra điều đó trong Mempool](https://Mempool.space/).


Và thế là xong. Chỉ cần kiên nhẫn chờ cho đến khi tất cả các kênh được đóng lại và tiền sẽ được chuyển trở lại Wallet trên chuỗi của bạn.


👉 **Phương pháp khôi phục bí mật:**


Có một phương pháp khác để khôi phục nút Blixt LND của bạn mà không cần đóng kênh. Nhưng phương pháp này bị ẩn khỏi người dùng noob thông thường, vì phương pháp này CHỈ dành cho những người biết họ đang làm gì.


Trong trường hợp bạn cần di chuyển nút Blixt hiện tại (đang hoạt động) sang một thiết bị mới khác mà không đóng các kênh LN hiện có, bạn sẽ phải thực hiện các bước sau:



- Chúng tôi cho rằng bạn đã lưu Blixt Wallet seed (24 từ aezeed)
- Trên thiết bị cũ, hãy vào "Cài đặt" - phần gỡ lỗi - "Thu gọn cơ sở dữ liệu LND". Bước này là tùy chọn nhưng được khuyến nghị nếu bạn muốn tệp channel.db có kích thước nhỏ hơn. Thường thì khá lớn, tùy thuộc vào hoạt động của nút. Thao tác này sẽ khởi động lại Blixt và thu gọn kích thước tệp db.
- Sau khi khởi động lại, hãy vào "Cài đặt" và đổi tên bí danh thường dùng của bạn thành "Hampus". Thao tác này sẽ kích hoạt các tùy chọn ẩn, chỉ dành cho người dùng nâng cao.
- Đi xuống phần "Debug" và bạn sẽ thấy tùy chọn mới "Export channel.db file". CẢNH BÁO! Sau khi bạn thực hiện thao tác xuất này, nút Blixt LN hiện tại sẽ bị vô hiệu hóa trên thiết bị cũ này và sẽ xuất toàn bộ cơ sở dữ liệu nút (channel.db) sẵn sàng để nhập vào thiết bị mới.
- Tệp db này sẽ được lưu vào một thư mục được chỉ định trên thiết bị cũ của bạn (Tài liệu hoặc Tải xuống) và từ đó bạn sẽ phải di chuyển tệp đó theo nguyên trạng sang thiết bị mới của mình. Ví dụ, bạn có thể sử dụng [ứng dụng FOSS LocalSend](https://github.com/localsend/localsend) để chuyển tệp trực tiếp giữa các thiết bị.
- Vào lúc này, chiếc Blixt cũ của bạn PHẢI tắt hẳn. ĐỪNG MỞ LẠI!
- Sau khi bạn chuyển tệp channel.db sang thiết bị mới, hãy bắt đầu cài đặt Blixt mới và chọn "Khôi phục Wallet" ở màn hình đầu tiên.
- Trên nút có ghi "Chọn tệp SCB", nhấn và giữ (KHÔNG phải nhấp chuột đơn giản!) và sau đó bạn sẽ thấy tùy chọn để chọn tệp channel.db nơi bạn lưu tệp cục bộ trong thiết bị mới. Nếu bạn chỉ cần nhấn nút đó, theo mặc định, tệp SCB sẽ được sử dụng (với các kênh đóng), không hoạt động đối với các kênh trực tiếp sao lưu đầy đủ.
- Nhập 24 từ seed rồi nhấp vào "Khôi phục"
- Bạn sẽ thấy Blixt sẽ bắt đầu đồng bộ hóa với Neutrino. Bạn cũng có thể xem nhật ký đồng bộ hóa.
- LƯU Ý! Cố gắng giữ Blixt luôn mở trong giai đoạn này! Không để nó ở chế độ ngủ hoặc đóng màn hình ứng dụng. Điều đó có thể làm gián đoạn quá trình đồng bộ ban đầu và bạn phải thực hiện lại. Hãy kiên nhẫn chờ đợi, không mất quá vài phút.
- Sau khi quá trình đồng bộ khối ban đầu hoàn tất, nó sẽ nhanh chóng quét các địa chỉ Wallet trước đó của bạn và sau đó các kênh của bạn sẽ trực tuyến trở lại, hoạt động bình thường.
- Thật không may là lịch sử thanh toán và danh bạ trước đó vẫn chưa thể khôi phục được. Nhưng dù sao thì điều đó cũng không quá quan trọng.


Và XONG! Bây giờ bạn đã khôi phục hoàn toàn nút Blixt LN. Nó cũng có thể hoạt động với các bản sao lưu LND khác (Umbrel, Raspiblitz, v.v.) nếu bạn đã lưu đúng tệp channel.db trước đó. Vì vậy, Blixt có thể lưu bất kỳ nút LND chết nào.


---

## Blixt - Liên lạc lần thứ tư


Chương này nói về tùy chỉnh và hiểu rõ hơn về Blixt Node. Tôi sẽ không mô tả tất cả các tính năng có sẵn, vì có quá nhiều và đã được giải thích trong [Trang tính năng Blixt](https://blixtwallet.github.io/features).


Nhưng tôi sẽ chỉ ra một số điều cần thiết để bạn có thể tiếp tục sử dụng Blixt và có được trải nghiệm tuyệt vời.


### A - Tên (NameDesc)


![blixt](assets/en/19.webp)


[NamDesc](https://github.com/lightning/blips/blob/master/blip-0011.md) là tiêu chuẩn để truyền đạt "tên người nhận" trong hóa đơn BOLT11.


Đây có thể là bất kỳ tên nào và có thể thay đổi bất cứ lúc nào.


Tùy chọn này thực sự hữu ích trong nhiều trường hợp, khi bạn muốn gửi tên cùng với mô tả Invoice, để người nhận có thể biết được ai đã nhận được Sats. Tùy chọn này hoàn toàn tùy chọn và trên màn hình thanh toán, người dùng phải tích vào ô cho biết muốn gửi tên bí danh.


Sau đây là ví dụ về cách hiển thị khi bạn sử dụng [chat.blixtwallet.com](https://chat.blixtwallet.com/)


![blixt](assets/en/20.webp)


Đây là một ví dụ khác về việc gửi đến ứng dụng Wallet khác hỗ trợ NameDesc:


![blixt](assets/en/21.webp)


### B - Hộp sét


Bắt đầu với phiên bản v0.6.9-420 mới [mới được công bố](https://github.com/hsjoberg/blixt-Wallet/releases/tag/v0.6.9-420), Blixt đã giới thiệu một tính năng mạnh mẽ mới cho Lightning Address trong Blixt.


Tính năng mới này là tùy chọn, không được BẬT theo mặc định!


Hiện tại, LN Box mặc định được chạy bởi máy chủ Blixt và cung cấp LN Address @blixtwallet.com. Nhưng BẤT KỲ AI có nút công khai LND đều có thể chạy máy chủ Lightning Box và cung cấp LN Address cho tên miền riêng của mình, tự lưu giữ.


Hiện tại, máy chủ Blixt chỉ chuyển tiếp các khoản thanh toán được gửi đến địa chỉ LN @blixtwallet.com đến người dùng Blixt đã đặt LN Address của họ. Người dùng phải đặt nút Blixt Wallet của họ ở "chế độ liên tục" để nhận các khoản thanh toán này đến địa chỉ LN @blixtwallet.com của họ.


Xem video demo về cách thiết lập LN Address của bạn trong Blixt trong ghi chú phát hành.


LN Address này được triển khai vào ứng dụng Blixt Wallet, giống như một cuộc trò chuyện qua LN, tức thời và thú vị, đồng thời hỗ trợ [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (thêm tên bí danh vào thanh toán). Bạn có thể thêm vào danh sách liên lạc tất cả các địa chỉ LN thông thường mà bạn thường xuyên sử dụng và có sẵn để trò chuyện. Bây giờ Blixt có thể được coi là một ứng dụng trò chuyện LN đầy đủ 😂😂.


Một tính năng hữu ích khác là hỗ trợ đầy đủ cho LUD-18 (cũng được [Stacker.News](https://stacker.news/r/DarthCoin) và những người khác hỗ trợ).


![blixt](assets/en/22.webp)


Như bạn có thể thấy trong ảnh chụp màn hình ở trên, khi gửi từ tài khoản Stacker News, nó hiển thị đẹp logo + LN Address + tin nhắn. Cách tương tự cũng áp dụng khi gửi từ Blixt, bạn có thể đính kèm Blixt LN Address hoặc chỉ cần thêm tên bí danh (đã đặt trước trong cài đặt Blixt) hoặc thậm chí cả hai.


Tùy chọn này từ LUD-18 cũng có thể hữu ích cho các dịch vụ đăng ký, nơi người dùng có thể gửi một bí danh cụ thể (KHÔNG phải là bí danh nút của bạn hoặc tên thật của bạn!) và dựa trên đó, bạn có thể được đăng ký hoặc nhận lại một tin nhắn cụ thể hoặc bất kỳ thứ gì khác. Việc đính kèm tên bí danh ([LUD-18](https://github.com/lnurl/luds/blob/luds/18.md))+ bình luận ([LUD-12](https://github.com/lnurl/luds/blob/luds/12.md)) vào thanh toán LN có thể có nhiều trường hợp sử dụng!


Sau đây là mã cho [Lightning Box](https://github.com/hsjoberg/lightning-box) nếu bạn chạy nó cho chính mình, cho gia đình và bạn bè, trên chính nút của bạn.


Tại đây, bạn cũng có thể chạy [máy chủ LSP Dunder](https://github.com/hsjoberg/dunder-lsp) cho các nút di động Blixt và cung cấp tính thanh khoản cho người dùng Blixt nếu bạn có nút LN công khai tốt (chỉ hoạt động với LND).


### C - Kênh LN dự phòng và từ seed


Đây là một tính năng rất quan trọng!


Sau khi mở hoặc đóng kênh LN, bạn nên sao lưu. Có thể thực hiện sao lưu thủ công một tệp nhỏ trên thiết bị cục bộ (thường là thư mục tải xuống) hoặc sử dụng tài khoản Google Drive hoặc iCloud.


![blixt](assets/en/23.webp)


Vào mục Blixt Settings - Wallet. Ở đó bạn có các tùy chọn để lưu tất cả dữ liệu quan trọng cho Blixt Wallet của bạn:



- “Show Mnemonic” - sẽ hiển thị 24 từ seed để ghi lại
- “Xóa Mnemonic khỏi thiết bị” - tùy chọn này là tùy chọn và chỉ sử dụng nếu bạn thực sự muốn xóa các từ seed khỏi thiết bị của mình. Thao tác này KHÔNG xóa Wallet của bạn, chỉ xóa seed. Nhưng hãy lưu ý! Không có cách nào để khôi phục chúng nếu bạn không ghi chúng ra trước.
- “Xuất bản sao lưu kênh” - tùy chọn này sẽ lưu một tệp nhỏ trên thiết bị cục bộ của bạn, thường là vào thư mục “tải xuống”, nơi bạn có thể lấy và di chuyển tệp đó ra bên ngoài thiết bị để giữ an toàn.
- “Xác minh kênh sao lưu” - đây là tùy chọn tốt nếu bạn sử dụng Google Drive hoặc iCloud để kiểm tra tính toàn vẹn của bản sao lưu được thực hiện từ xa.
- “Google Drive Channel Backup” - sẽ lưu tệp sao lưu vào Google Drive cá nhân của bạn. Tệp được mã hóa và được lưu trữ trong một kho lưu trữ riêng biệt so với các tệp Google thông thường của bạn. Vì vậy, không có mối lo ngại nào có thể bị bất kỳ ai đọc được. Dù sao thì tệp đó hoàn toàn vô dụng nếu không có các từ seed, vì vậy không ai có thể lấy tiền của bạn từ tệp đó.


Tôi xin đề xuất phần này như sau:



- sử dụng trình quản lý mật khẩu để lưu trữ an toàn seed và tệp sao lưu của bạn. KeePass hoặc Bitwarden rất tốt cho việc đó và có thể sử dụng trên nhiều nền tảng và tự lưu trữ hoặc ngoại tuyến.
- SAO LƯU MỖI LẦN bạn mở hoặc đóng kênh. Tệp đó được cập nhật thông tin kênh. Không cần phải làm điều đó sau mỗi giao dịch bạn thực hiện trên LN. Sao lưu kênh không lưu trữ thông tin đó, chỉ lưu trữ trạng thái của kênh.


![blixt](assets/en/24.webp)


---

## Blixt - Mẹo và thủ thuật


### TRƯỜNG HỢP 1 - VẤN ĐỀ ĐỒNG BỘ


"_Blixt của tôi không đồng bộ hóa... Blixt của tôi không hiển thị số dư... Blixt của tôi không mở được kênh... Tôi đã thử khôi phục nó trên một thiết bị khác... v.v._"


Tất cả những vấn đề này bắt đầu vì THIẾT BỊ CỦA BẠN KHÔNG ĐỒNG BỘ ĐÚNG CÁCH. Vui lòng hiểu khía cạnh quan trọng này: Blixt là một nút LND di động, sử dụng Neutrino để đồng bộ hóa / đọc các khối.



- Sau đây là lời giải thích ít mang tính kỹ thuật hơn từ [Tạp chí Bitcoin](https://bitcoinmagazine.com/technical/why-Bitcoin-wallets-need-block-filters)
- Sau đây là thêm các tài nguyên kỹ thuật từ [Bitcoin Optech](https://bitcoinops.org/en/topics/compact-block-filters/)
- Sau đây là cách bạn có thể kích hoạt Neutrino trên nút home của riêng bạn và phục vụ các bộ lọc khối cho nút di động của bạn, từ [Docs Lightning Engineering](https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core)


NHẮC NHỞ: Sử dụng Neutrino qua clearnet hoàn toàn an toàn, IP hoặc xpub của bạn không bị rò rỉ. Bạn chỉ đang đọc các khối từ một nút từ xa bằng neutrino. Chỉ vậy thôi. Mọi thứ còn lại được thực hiện trên thiết bị cục bộ của bạn.


Vì vậy, KHÔNG CẦN sử dụng nó với Tor. Tor sẽ làm tăng độ trễ rất lớn trong quá trình đồng bộ hóa của bạn và sẽ khiến Blixt của bạn rất không ổn định. Nếu bạn thực sự muốn sử dụng qua Tor, hãy chắc chắn về những gì bạn đang làm và có kết nối tốt và kiên nhẫn. Tương tự như khi sử dụng VPN. Hãy cẩn thận với độ trễ mà VPN đó cung cấp cho bạn.


Bạn có thể kiểm tra độ trễ của máy chủ neutrino bằng cách ping nó từ máy tính hoặc điện thoại di động.


![blixt](assets/en/25.webp)


Đây là lệnh ping thông thường tới máy chủ neutrino europe.blixtwallet.com, điều này cho thấy kết nối rất tốt với thời gian phản hồi trung bình là 50ms và TTL là 51. Thời gian phản hồi có thể thay đổi nhưng không quá nhiều. TTL phải ổn định.


Nếu các giá trị này cao hơn 100-150ms thì quá trình đồng bộ hóa của bạn sẽ chậm lại hoặc thậm chí tệ hơn, nó có thể khiến các kênh bị đóng bởi các đối tác! Đừng bỏ qua khía cạnh này.


Nếu không đồng bộ đúng cách, bạn cũng không thể thấy được sự cân bằng chính xác hoặc các kênh LN của bạn sẽ không trực tuyến và hoạt động. Cho dù bạn có bao nhiêu giga ultra terra mbps tốc độ tải xuống, ĐIỀU ĐÓ KHÔNG QUAN TRỌNG. Điều quan trọng là phản hồi thời gian và TTL (thời gian sống).


Đây giống như trường hợp chung của người dùng LATAM. Tôi không biết chuyện gì xảy ra ở đó nhưng các bạn có kết nối tệ với ping hơn 200ms có thể làm gián đoạn bất kỳ quá trình đồng bộ nào.


Vậy giải pháp cho những người dùng tuyệt vọng này là gì?



- ngừng sử dụng Blixt với Tor. Hoàn toàn vô dụng
- bạn có thể sử dụng VPN nhưng hãy chọn một cách khôn ngoan và theo dõi ping mọi lúc. Sử dụng VPN gần với vị trí địa lý của bạn hơn. Khoảng cách có nghĩa là thời gian phản hồi ms nhiều hơn, hãy nhớ nhé.
- hãy lựa chọn một cách khôn ngoan các máy chủ neutrino ngang hàng của bạn, sau đây là danh sách các máy chủ neutrino công cộng nổi tiếng:


```txt
For US region
btcd1.lnolymp.us | btcd2.lnolymp.us
btcd-mainnet.lightning.computer
swest.blixtwallet.com (Seattle)
node.eldamar.icu
noad.sathoarder.com
bb1.breez.technology | bb2.breez.technology
neutrino.shock.network
For EU region
europe.blixtwallet.com (Germany)
For Asia region
sg.lnolymp.us
asia.blixtwallet.com
```


Một cách khác là chọn một nút từ danh sách các nút thông báo "bộ lọc nhỏ gọn" (BIP157 / neutrino) - [Bộ lọc Neutrino của Bitnodes Page](https://bitnodes.io/nodes/?q=NODE_COMPACT_FILTERS). Chọn nút gần với vị trí địa lý của bạn hơn.


Một cách khác (cách tốt nhất) là kết nối với một nút cộng đồng cục bộ, do một người bạn hoặc nhóm mà bạn biết điều hành và đang cung cấp kết nối neutrino. [Sau đây là hướng dẫn cách thực hiện.](https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core) Nút của họ sẽ không bị ảnh hưởng theo bất kỳ cách nào, họ chỉ cần một kết nối ổn định và công khai.


Cần có nhiều máy chủ neutrino hơn trong khu vực LATAM để đồng bộ hóa nhanh hơn và tốt hơn. Vì vậy, hãy tự tổ chức, với cộng đồng Bitcoin địa phương của bạn và quyết định xem ai và ở đâu đang chạy Bitcoin Core + Neutrino cho mục đích sử dụng của riêng bạn. Chỉ cần một IP công khai là đủ. Nếu bạn không có quyền truy cập vào IP công khai, bạn có thể sử dụng IP VPS và tạo đường hầm wireguard đến nút home của mình. Theo cách đó, bạn sẽ chuyển hướng tất cả lưu lượng truy cập đến IP VPS cục bộ của mình mà không tiết lộ bất kỳ thông tin riêng tư nào về nút home của bạn.


### TRƯỜNG HỢP 2 - KHÔNG BAO GIỜ HOÀN THÀNH ĐỒNG BỘ


"_Blixt của tôi có kết nối tốt với máy chủ neutrino nhưng bị kẹt khi đồng bộ hóa._"


#### Máy chủ thời gian


Đôi khi mọi người sử dụng nhiều thiết bị cũ hoặc không kết nối đúng với máy chủ thời gian. Neutrino đang đồng bộ hóa bình thường cho đến khi đạt đến các khối thực tế không tương ứng với thời gian địa phương thực tế. Bạn sẽ thấy trong nhật ký Blixt LND lỗi nói rằng "dấu thời gian khối còn lâu mới đến" hoặc một cái gì đó liên quan đến "tiêu đề không vượt qua kiểm tra tính hợp lệ".


Sửa lỗi nhanh: đặt đúng thời gian và ngày tháng cho thiết bị của bạn và khởi động lại Blixt.


#### Không gian trên thiết bị thấp


Đôi khi sử dụng thiết bị cũ, có dung lượng thấp, nó có thể đạt đến ngưỡng giới hạn và bị kẹt. Thật vậy, đối với những người sử dụng nút LND di động này, các tệp neutrino sẽ lớn hơn và tệp channel.db cũng vậy.


Sửa lỗi nhanh: Vào mục Tùy chọn Blixt - Gỡ lỗi - Chọn "dừng LND và xóa các tệp neutrino". Nó sẽ khởi động lại ứng dụng và bắt đầu đồng bộ mới. Đôi khi, bản sửa lỗi nhanh này cũng có thể sửa dữ liệu bị hỏng. Hãy nhớ rằng sẽ mất một khoảng thời gian, từ 1 đến 3 phút để đồng bộ lại hoàn toàn. Nó KHÔNG xóa các quỹ hoặc kênh hiện có, nhưng đúng vậy, sau khi đồng bộ lại, nó có thể kích hoạt quét lại các địa chỉ Bitcoin của bạn và điều đó có thể mất nhiều thời gian hơn.


Bước tiếp theo là kiểm tra xem còn bao nhiêu dữ liệu đang chiếm dụng. Bạn có thể xem thông tin này trong Android App info - data. Nếu vẫn lớn hơn 400-500MB, bạn có thể nén các tệp LND. Vì vậy, hãy vào Blixt Options - Debug section - Chọn "Compact DB LND". Khởi động lại ứng dụng Blixt nếu không tự động thực hiện. Quá trình nén diễn ra khi khởi động và chỉ diễn ra một lần. Bây giờ bạn sẽ thấy dữ liệu Blixt ít bị chiếm dụng hơn.


#### Chế độ liên tục


Đôi khi mọi người không mở Blixt trong thời gian dài, vì vậy đồng bộ hóa đã quá cũ. Nhưng họ mong đợi được đồng bộ hóa ngay lập tức khi họ mở nó.


Xin hãy kiên nhẫn và nhìn vào bánh xe quay trên cùng. Tùy chọn, bạn có thể vào Options - See Node Info và xem liệu có đồng bộ với chain và đồng bộ với biểu đồ được đánh dấu là "true" hay không. Nếu không có "true" đó, bạn không thể sử dụng Blixt đúng cách, bạn không thể xem số dư chính xác, bạn không thể xem kênh LN trực tuyến, bạn không thể thanh toán.


Sửa lỗi nhanh: Có một tùy chọn mạnh mẽ để "duy trì" nút Blixt của bạn. Vào Options - Experiments - Chọn "Activate Persistent Mode". Tùy chọn này sẽ khởi động lại Blixt của bạn và sẽ đặt dịch vụ LND ở chế độ liên tục, tức là luôn hoạt động và giữ cho đồng bộ trực tuyến, ngay cả khi bạn chuyển sang ứng dụng khác hoặc chỉ cần đóng Blixt (không phải đóng bắt buộc hoặc tắt tác vụ). Bạn có thể giữ nguyên như vậy cả ngày nếu bạn có kết nối ổn định và cần sử dụng Blixt nhiều lần. Nó sẽ không tiêu tốn quá nhiều pin.


### TRƯỜNG HỢP 3 - TÔI MUỐN DI CHUYỂN SANG THIẾT BỊ KHÁC


Được rồi, về tình huống này, tôi đã viết hướng dẫn chi tiết trên trang [Câu hỏi thường gặp](https://blixtwallet.github.io/faq#blixt-restore): với 2 tùy chọn, nhanh (hợp tác đóng các kênh trước khi di chuyển) và chậm (buộc đóng các kênh vì thiết bị cũ đã chết).


Nhưng tôi muốn nhắc lại ở đây một số khía cạnh quan trọng và thêm một thủ tục "bí mật" mới.


LỜI NHẮC NHỞ:



- Luôn sao lưu trạng thái kênh (SCB) của bạn SAU mỗi lần bạn mở hoặc đóng kênh. Chỉ mất vài giây để thực hiện.
- Không giữ lại các tệp SCB cũ, để không bị nhầm lẫn và khôi phục chúng. Hoàn toàn vô dụng và có thể kích hoạt quy trình phạt nếu bạn thấy chúng. Luôn sử dụng phiên bản mới nhất của tệp SCB nếu bạn tiến hành khôi phục.
- Lưu tệp SCB (là văn bản được mã hóa có phần mở rộng .bin) ra khỏi thiết bị của bạn, ở nơi an toàn. Bạn có thể sử dụng [LocalSend](https://github.com/localsend/localsend) để di chuyển tệp này vào PC hoặc thiết bị khác.
- Lưu seed của Blixt Wallet ở nơi an toàn, ví dụ như trình quản lý mật khẩu ngoại tuyến/USB được mã hóa.


Phương pháp bí mật: Cách di chuyển nút Blixt mà không đóng các kênh hiện có. Đối với điều này, bạn sẽ cần đọc kỹ phần trước "Liên hệ thứ ba" trong hướng dẫn này về "Khôi phục Wallet".


Quy trình này KHÔNG DÀNH CHO NGƯỜI MỚI BẮT ĐẦU, nó chỉ dành cho người dùng nâng cao! Đó là lý do tại sao nó không được công khai rộng rãi và tôi khuyên bạn chỉ nên thực hiện với sự hỗ trợ từ các nhà phát triển Blixt hoặc bộ phận hỗ trợ của tôi. Vui lòng không bỏ qua lời khuyên này.


### TRƯỜNG HỢP 4 - SỬ DỤNG PERFECTS NÀO ĐỂ MỞ KÊNH?


Như tôi đã viết trong [Trang hướng dẫn Blixt](https://blixtwallet.github.io/guides) có nhiều cách để mở kênh bằng nút LND di động này. Nhưng có một số khía cạnh quan trọng mà tôi muốn nhắc bạn ở đây:



- mở với các nút LSP nổi tiếng và với các đối tác được cộng đồng bảo lãnh. [Xem danh sách tại đây](https://github.com/hsjoberg/blixt-Wallet/issues/1033)
- không mở bằng các nút Tor ngẫu nhiên. Những nút đó vô giá trị và bạn sẽ chỉ gặp vấn đề là không thể thanh toán. Cho dù bạn của bạn "người chạy nút" giỏi đến đâu với một nút Tor tệ hại trong rừng rậm, nó sẽ không bao giờ cung cấp cho bạn các tuyến đường tốt nhất cho một nút riêng tư di động. Bạn không mở kênh với ai đó vì đó là bạn của bạn. Đây không phải là Facebook! Bạn mở kênh vì: các tuyến đường tốt, phí nhỏ, khả dụng.
- không cần phải mở một đống kênh nhỏ, 2-3 hoặc tối đa là 4, nhưng phải có một lượng Sats tốt. Không mở các kênh nhỏ, chúng hoàn toàn vô dụng. Nhỏ hơn 200k cho một thiết bị di động không có nhiều tác dụng.
- hãy ghi nhớ các LSP cung cấp các kênh đến và các kênh JIT (đúng lúc). Chúng rất hữu ích vì bạn không cần sử dụng bất kỳ UTXO nào, bạn có thể thanh toán kênh mở bằng số tiền bạn đã có trong các ví LN khác, xếp chồng và chuẩn bị chúng để mở một kênh lớn hơn. Bạn nên sử dụng các kênh JIT này theo hướng có lợi cho mình. [Tôi đã giải thích trong hướng dẫn này](https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html) nhiều tùy chọn hơn cho các đối tác đối với các nút riêng tư như Blixt. Ngoài ra, [trong hướng dẫn này được đăng trên SN](https://stacker.news/items/679242/r/DarthCoin), tôi đã giải thích cách quản lý tính thanh khoản của các nút di động riêng tư.


---

## Phần kết luận


Vâng, Blixt còn nhiều tính năng tuyệt vời khác nữa, tôi sẽ cho bạn khám phá từng tính năng một và tận hưởng nhé.


Ứng dụng này thực sự bị đánh giá thấp, chủ yếu là vì không được hỗ trợ bởi bất kỳ nguồn tài trợ VC nào, do cộng đồng thúc đẩy, được xây dựng bằng tình yêu và niềm đam mê dành cho Bitcoin và Lightning Network.


Nút LN di động này, Blixt là một công cụ rất mạnh mẽ trong tay nhiều người dùng, nếu họ biết cách sử dụng tốt. Hãy tưởng tượng, bạn đang đi khắp thế giới với một nút LN trong túi của mình và không ai biết điều đó.


Và chưa kể đến những tính năng phong phú khác đi kèm mà rất ít hoặc không có ứng dụng Wallet nào có thể cung cấp.


Trong khi đó, đây là tất cả các liên kết về Bitcoin Lightning Node tuyệt vời này:



- [Trang web chính thức của Blixt](https://blixtwallet.com/)
- [Trang Blixt Github](https://github.com/hsjoberg/blixt-Wallet/)
- [Trang tính năng của Blixt](https://blixtwallet.github.io/features) - giải thích từng tính năng và chức năng.
- [Trang câu hỏi thường gặp của Blixt](https://blixtwallet.github.io/faq) - Danh sách câu hỏi và trả lời cũng như cách khắc phục sự cố của Blixt
- [Trang hướng dẫn Blixt](https://blixtwallet.github.io/guides) - bản demo, hướng dẫn bằng video, hướng dẫn bổ sung và các trường hợp sử dụng cho Blixt
- Tải xuống: [Android Play Store](https://play.google.com/store/apps/details?id=com.blixtwallet) |  [iOS](https://testflight.apple.com/join/EXvGhRzS) |  [Tải xuống trực tiếp APK](https://github.com/hsjoberg/blixt-Wallet/releases)
- [Nhóm Telegram để được hỗ trợ trực tiếp](https://t.me/blixtwallet)
- [Twitter](https://twitter.com/BlixtWallet)
- [Trang gây quỹ cộng đồng Geyser](https://geyser.fund/project/blixt) - hãy quyên góp Sats tùy thích để hỗ trợ dự án
- [LNURL Chat Blixt](https://chat.blixtwallet.com/) - trò chuyện ẩn danh LN
- [Bài thuyết trình của Blixt - video quảng cáo](https://lightning.video/06fdf68f99e246a6ec6ba1470677b9e632faaad4aa0ca9773c38714b682a4ac1)
- [Lịch Blixt Girls](https://lightning.video/eeb744202ad3f14c18bf6d719970ebd9c53f0f13b79c94d299c6be623fba64b6) - video quảng cáo (bạn có thể kiểm tra lần đầu sử dụng LN)
- [Tờ rơi A4 có thể in với các bước đầu tiên sử dụng Blixt, bằng nhiều ngôn ngữ khác nhau](https://github.com/BlixtWallet/blixtwallet.github.io/tree/master/assets/flyer).
- [Blixt cũng cung cấp bản demo đầy đủ chức năng](https://blixt-Wallet-git-master-hsjoberg.vercel.app/) ngay trên trang web của mình hoặc trên phiên bản web chuyên dụng để có trải nghiệm thử nghiệm đầy đủ trước khi bắt đầu sử dụng trong thế giới thực.


---
**TUYÊN BỐ MIỄN TRỪ TRÁCH NHIỆM:**


*Tôi không được trả tiền hoặc hỗ trợ theo bất kỳ cách nào bởi các nhà phát triển ứng dụng này. Tôi viết hướng dẫn này vì tôi thấy rằng sự quan tâm đến ứng dụng Wallet này đang tăng lên và người dùng mới vẫn chưa hiểu cách bắt đầu với nó. Ngoài ra, để giúp Hampus (nhà phát triển chính) với tài liệu hướng dẫn về cách sử dụng nút Wallet này.*


*Tôi không có bất kỳ mối quan tâm nào khác trong việc quảng bá ứng dụng LN này, ngoài việc thúc đẩy việc áp dụng Bitcoin và LN. Đây là cách duy nhất!*


---