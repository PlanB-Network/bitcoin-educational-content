---
name: Blixt

description: Ví Lightning Network Node Di Động
---

![presentation](assets/blixt_intro_en.webp)

## Một BTC/Lightning Node mạnh mẽ trong túi bạn, ở bất cứ đâu

Tôi muốn giới thiệu với bạn một Node và ví di động BTC/LN mới, thú vị và mạnh mẽ - Blixt. Tên gọi này có nguồn gốc từ tiếng Thụy Điển và có nghĩa là "tia chớp".
Nếu bạn chưa bao giờ sử dụng Bitcoin Lightning Network, trước khi bắt đầu, vui lòng đọc bài này về [giải thích đơn giản bằng cách so sánh tương tự về Lightning Network (LN)](https://darthcoin.substack.com/p/the-lightning-network-and-the-airport).

## CÁC KHÍA CẠNH QUAN TRỌNG:

### 1. Blixt là một node riêng tư, KHÔNG phải là một node định tuyến! Hãy nhớ điều này.

Điều đó có nghĩa, tất cả các kênh LN trong Blixt sẽ không được công bố trên bản đồ LN (các kênh riêng tư). Điều đó có nghĩa, NODE NÀY SẼ KHÔNG THỰC HIỆN ĐỊNH TUYẾN các khoản thanh toán của người khác qua node Blixt. [Đọc thêm về kênh riêng tư và kênh công khai tại đây](https://voltage.cloud/blog/lightning-network-faq/what-are-the-differences-between-public-and-private-channels/).

Node di động Blixt KHÔNG dành cho định tuyến, tôi nhắc lại. Nó chủ yếu được dùng để bạn có thể quản lý các kênh LN của mình và thực hiện các khoản thanh toán LN một cách riêng tư, bất cứ khi nào bạn cần.

  Node di động Blixt, CHỈ CẦN phải trực tuyến và đồng bộ ngay TRƯỚC khi bạn thực hiện giao dịch của mình. Đó là lý do tại sao bạn sẽ thấy một biểu tượng phia trên hiển thị trạng thái đồng bộ. Việc này chỉ mất vài khoảnh khắc, tùy thuộc vào thời gian bạn giữ nó ngoại tuyến và đồng bộ lại bản đồ LN (LN graph).

### 2. Blixt sử dụng LND (aezeed) làm ví backend, vì vậy đừng cố gắng nhập vào các loại ví bitcoin khác.

[Tại đây bạn có hướng dẫn về các loại ví](https://coldbit.com/what-types-of-mnemonic-seeds-are-used-in-bitcoin/). Vì vậy, nếu trước đây bạn đã có một LND Node, bạn có thể nhập hạt giống và file channels.backup vào Blixt, [như được chỉ ra trong hướng dẫn này](https://darthcoin.substack.com/p/umbrel-btcln-node-shtf-scenario).

### 3. Các liên kết quan trọng của Blixt (vui lòng đánh dấu chúng):

- [Kho lưu trữ Github của Blixt](https://github.com/hsjoberg/blixt-wallet) | [Phát hành trên Github](https://github.com/hsjoberg/blixt-wallet/releases) (tải trực tiếp tệp apk)
- [Trang các tính năng của Blixt](https://blixtwallet.github.io/features) - giải thích từng tính năng và chức năng của Blixt một cách chi tiết.
- [Trang FAQ của Blixt](https://blixtwallet.github.io/faq) - Danh sách câu hỏi thường gặp & trả lời và cách khắc phục sự cố của Blixt
- [Trang Hướng dẫn của Blixt](https://blixtwallet.github.io/guides) - demos, video hướng dẫn, hướng dẫn bổ sung và ứng dụng của Blixt vào thực tế
- [Tờ rơi giới thiệu trên một trang A4 có thể in](https://github.com/BlixtWallet/blixtwallet.github.io/tree/master/assets/flyer) -  các bước đầu tiên để sử dụng Blixt, bằng nhiều ngôn ngữ.
- Blixt cũng cung cấp một bản demo đầy đủ các chức năng ngay trên [trang web của mình](https://blixtwallet.com) hoặc trên một [phiên bản web chuyên dụng](https://blixt-wallet-git-master-hsjoberg.vercel.app/), để người dùng có thể trải nghiệm đầy đủ trước khi bắt đầu sử dụng Blixt trong thế giới thực.
- [Trang gây quỹ Geyser](https://geyser.fund/project/blixt) - quyên góp số lượng sat tùy thích để hỗ trợ dự án
- [Nhóm hỗ trợ Telegram](https://t.me/blixtwallet)
# Các tính năng chính có sẵn

## Neutrino Node

Blixt mặc định kết nối với máy chủ của Blixt để đồng bộ hóa các block và chỉ mục với Neutrino (chế độ SPV cho Simplified Payment Verification), nhưng người dùng cũng có thể kết nối với node của riêng họ. Thật ngạc nhiên khi thấy rằng việc đồng bộ hóa một node SPV mất ít hơn 5 phút để sẵn sàng sử dụng ví node đầy đủ (on-chain và LN), trong trường hợp của tôi thao tác trên Android 11.

## Node tự quản hoàn chỉnh

Người dùng có thể quản lý các kênh của mình với giao diện dễ sử dụng và với đẩy đủ thông tin hiển thị để có trải nghiệm tốt. Trong menu kéo ở góc trên bên trái, bạn có thể đi đến các kênh Lightning để bắt đầu mở kênh với các node khác, tùy ý bạn. Đừng quên kích hoạt Tor trong cài đặt. Nó tốt hơn cho quyền riêng tư và cũng vì là một node di động, nếu bạn thay đổi kết nối internet / IP clearnet thường xuyên, các đối tác của bạn có thể bị gián đoạn. Với URI node Tor, bạn sẽ luôn có cùng một định danh riêng tư bất kể vị trí / IP của bạn.

## Sao lưu/Phục hồi một LND Node

Một tính năng mạnh mẽ, dễ quản lý và hữu ích là khôi phục các LND Node đã chết, chỉ với danh sách 24 từ khóa và tệp channels.backup.

> [Đây là hướng dẫn về cách khôi phục các node Umbrel đã chết trong Blixt trong trường hợp SHTF.](https://darthcoin.substack.com/p/umbrel-btcln-node-shtf-scenario)

Người dùng cũng có tùy chọn lưu sao lưu kênh Blixt vào Google Drive và/hoặc bộ nhớ cục bộ trên thiết bị di động của riêng họ (để sau này chuyển nó đến một nơi an toàn, cách biệt với điện thoại của họ).

Quy trình khôi phục khá đơn giản: chèn danh sách 24 từ khóa, thêm tệp sao lưu (đã trước đó được sao chép vào bộ nhớ di động), và nhấp khôi phục. Sẽ mất một thời gian để đồng bộ và quét tất cả các khối cho các giao dịch trước đó của bạn. Các kênh sẽ được đóng tự động và tiền sẽ được trả về ví on-chain của bạn (xem menu kéo ở góc trên bên trái - on-chain).

> Nếu trước đó bạn đã mở các kênh với node cũ của mình qua Tor, trước tiên, bạn phải kích hoạt tùy chọn Tor (và khởi động lại ứng dụng) từ menu cài đặt. Như vậy, quy trình đóng sẽ không thất bại và/hoặc tùy chọn đóng ép buộc sẽ không được sử dụng.

Nhớ sao lưu các kênh LN của bạn sau khi mở và/hoặc đóng các kênh. Chỉ mất vài giây để đảm bảo an toàn. Sau đó, bạn có thể chuyển tệp sao lưu đến một nơi an toàn cách biệt với thiết bị di động của mình.
Để kiểm tra hạt giống của bạn trong một kịch bản khôi phục, trước khi thêm tiền, chỉ cần sử dụng cùng một danh sách 24 từ khóa (aezeed) trong BlueWallet. Nếu địa chỉ BTC được tạo ra giống nhau trong Blixt, bạn đã sẵn sàng. Sau đó, không cần sử dụng ví BlueWallet đó nữa, bạn có thể xóa ví đã được kiểm tra cho việc khôi phục.

## Tor được tích hợp

Một khi bạn đã kích hoạt nó, ứng dụng sẽ khởi động lại qua mạng Tor. Từ đây, bạn có thể thấy trong menu cài đặt ID node của mình với địa chỉ onion, để các node khác có thể mở kênh với node Blixt di động của bạn. Hoặc giả sử bạn có node của riêng mình tại nhà và bạn muốn có các kênh nhỏ với node di động Blixt của bạn. Một sự kết hợp hoàn hảo.

## Dunder LSP - Nhà cung cấp dịch vụ thanh khoản - Liquidity Service Provider

Một tính năng đơn giản và tuyệt vời cho phép người dùng mới có thể bắt đầu chấp nhận BTC trên Lightning Network ngay lập tức, mà không cần phải gửi tiền on-chain và sau đó mở các kênh LN.
Đây là tin tốt lành dành cho người mới, bởi vì họ có thể bắt đầu từ con số không, trực tiếp trên LN. Để làm điều này, chỉ cần tạo một hóa đơn LN từ màn hình chính trên nút "nhận", nhập số lượng, mô tả, v.v., và thanh toán từ một ví khác. Blixt sẽ mở một kênh lên đến 400k sat cho mỗi giao dịch nhận được. Bạn có thể mở nhiều kênh nếu cần thiết.
Một trường hợp thú vị và hữu ích như sau: giả sử số tiền bạn nhận đầu tiên là 200k sat. Blixt sẽ mở một kênh 400k sat với 200k (trừ phí mở kênh) ở phía bạn, nhưng vì bạn vẫn còn 200k "không gian trống" để bạn có thể nhận thêm. Vậy nên, giao dịch tiếp theo, giả sử là 100k, sẽ đến trực tiếp qua kênh này, không phát sinh thêm phí, và bạn vẫn còn 100k không gian để nhận thêm.

Nhưng nếu bạn chọn nhận, giả sử, 300k cho giao dịch thứ ba, nó sẽ tạo một kênh mới 400k khác và chuyển 300k này vào phía bạn.

Nếu có quá nhiều yêu cầu, node Blixt có thể điều chỉnh dung lượng kênh trong quá trình mở.

## Mở kênh tự động

Trong cài đặt, người dùng có thể kích hoạt tùy chọn này và có một dịch vụ tự động mở kênh với các node và tuyến (route) tốt nhất dựa trên số dư có sẵn trong ví on-chain của ứng dụng Blixt. Đây là tính năng có lợi cho người dùng mới, khi họ không chắc chắn nên mở kênh với node nào và/hoặc làm thế nào để mở một kênh LN. Nó giống như một hệ thống lái tự động cho LN.

> Nhớ rằng: tùy chọn này chỉ được sử dụng một lần, khi bạn tạo ví Blixt mới của mình, và được kích hoạt theo mặc định. Vì vậy, nếu người dùng mới quét mã QR on-chain trên màn hình chính và gửi những sat đầu tiên đến địa chỉ đó, Blixt sẽ tự động mở một kênh với số sat đó, với node công khai của Blixt.

## Dịch vụ thanh khoản nhận vào

Tính năng dành riêng cho các nhà bán hàng cần nhiều thanh khoản NHẬN VÀO hơn, dễ sử dụng. Để làm điều này, chỉ cần chọn một trong số các nhà cung cấp thanh khoản từ danh sách, thanh toán số tiền bạn muốn cho kênh, và cung cấp ID của node của bạn, và từ đó, một kênh sẽ được mở đến node Blixt của bạn.

## Danh sách liên lạc

Tính năng hữu ích nếu bạn muốn có một danh sách bền vững của người nhận mà bạn giao dịch trong phần lớn thời gian. Danh sách này có thể bao gồm LNURLs, địa chỉ Lightning, hoặc thông tin/ hóa đơn thanh toán tĩnh trong tương lai. Hiện tại, danh sách này không thể được lưu bên ngoài ứng dụng, nhưng đang có kế hoạch để có một tùy chọn xuất nó.

## LNURL và Địa chỉ Lightning

Hỗ trợ đầy đủ LNURL. Bạn có thể thanh toán đến LNURL, LN-auth, yêu cầu LN-chan với LNURL.
Bạn cũng có thể gửi đến bất kỳ địa chỉ LN nào và thêm nó vào danh sách liên lạc của mình.
Bắt đầu từ phiên bản 0.6.9, cũng có thể nhận vào địa chỉ LN của riêng bạn *@blixtwallet.com* qua tính năng [Blixt Lightning Box](https://github.com/hsjoberg/lightning-box).

## Keysend

Một tính năng mạnh mẽ mà ít ví di động có. Bạn có thể gửi/đẩy tiền trực tiếp qua một kênh hoặc chỉ đến một node khác, thêm một tin nhắn nếu cần. Giống như một cuộc trò chuyện bí mật qua LN. Tính năng này rất hữu ích để hiển thị tin nhắn trên bảng thông báo Amboss.space ([đây là hướng dẫn về bảng thông báo Amboss này](https://darthcoin.substack.com/p/amboss-billboard-amazing-tool)).

## Ký tin nhắn
Công cụ rất hữu ích để ký các tin nhắn bằng khóa riêng của Node Blixt của bạn, xác thực tin nhắn. Rất ít ví di động có tính năng này, gần như không có.

## Thanh toán đa kênh - Thanh toán đa đường dẫn (MPP)

Tính năng hữu ích cho thanh toán LN, cho phép bạn chia một thanh toán LN thành nhiều phần, qua nhiều kênh. Đây là cách tốt để cân bằng tính thanh khoản trên mạng và cải thiện quyền riêng tư.

## Trìnhduyệt Lightning

Một loạt các dịch vụ của bên thứ ba với LN, được gói gém sắp xếp trong một trình duyệt đơn giản, dễ tiếp cận và thân thiện với người dùng. Đây cũng là cách tốt để quảng bá các doanh nghiệp chấp nhận BTC trên LN. Đây là một tính năng sẽ được phát triển thêm trong tương lai. Hiện tại, nó không hoạt động phía sau Tor, vì vậy việc duyệt các ứng dụng này sẽ dùng clearnet.

## Trình duyệt nhật ký

Đây là công cụ mạnh mẽ để kiểm tra nhật ký LND (LND log) và trạng thái node của bạn nói chung. Có một tùy chọn để lưu file nhật ký. Rất hữu ích khi có những thông tin nhật ký này trong tay nếu bạn cần sự hỗ trợ của nhà phát triển để xác định một số vấn đề.

## Bảo mật

Bạn có thể thiết lập trong cài đặt ứng dụng, để tăng cường bảo mật cho ví/node của mình, có thể khởi động ứng dụng bằng mã PIN và/hoặc dấu vân tay.

## Ví On-chain

Tính năng này hơi ẩn, trong menu kéo ở góc trên bên trái. Vì nó không thường xuyên được sử dụng bởi người dùng LN, nó không hiển thị trên màn hình chính. Nhưng không sao, bạn có thể có nó trên một ví riêng biệt nơi bạn có thể quản lý địa chỉ và xem nhật ký giao dịch, bằng cách nhập hạt giống của bạn trên Sparrow chẳng hạn. Có thể trong tương lai, ví Blixt cũng sẽ bao gồm tính năng quản lý UTXO. Nhưng hiện tại, CHỈ sử dụng ví on-chain này để mở hoặc đóng các kênh trên LN.

## Tính năng đặc biệt

- Với phiên bản 0.6.9 đã giới thiệu "chế độ bền bỉ - persistent mode" cho phép người dùng chạy Blixt như một node LN luôn trực tuyến, giữ cho dịch vụ LND hoạt động và ví LN sẵn sàng nhận/gửi bất cứ lúc nào.
- Kênh Taproot đơn giản - cho phép mở kênh Taproot để tăng cường quyền riêng tư và các tính năng nâng cao
- Kênh không cần xác nhận với Blixt Dunder LSP
- Speedloader ("đồng bộ kênh LN") - Điều này có nghĩa là tất cả các kênh sẽ được đồng bộ nhanh chóng khi khởi động, để tìm đường đi tốt hơn. Mặc dù hơi khó chịu khi bạn phải xem màn hình đồng bộ ở đầu, nhưng điều này sẽ đảm bảo rằng ví biết về tất cả các kênh nên các giao dịch sẽ nhanh chóng và đáng tin cậy hơn.
- Đã dịch sang 25+ ngôn ngữ!

## "Trứng phục sinh - Easter Eggs"

Vâng, trong ứng dụng Blixt, có một số tính năng ẩn, những điều nhỏ nhặt làm cho ứng dụng trở nên quyến rũ, kích hoạt các hành động/phản ứng vui vẻ/thú vị.
Gợi ý: thử nhấp hai lần liên tục vào logo Blixt trong menu kéo 🙂 Tôi sẽ để bạn khám phá phần còn lại.

# Hướng dẫn từng bước để bắt đầu với Blixt

> Là người dùng LN mới, nếu bạn bắt đầu sử dụng Node LN Blixt, bạn sẽ cần phải biết Lightning Network là gì và cách hoạt động của nó, ít nhất ở cấp độ cơ bản. [Ở đây chúng tôi đã tổng hợp một danh sách nhỏ về các nguồn tài liệu về Lightning Network](https://blixtwallet.github.io/faq#what-is-ln). Vui lòng đọc chúng trước.”

Chạy một node LN đầy đủ trên một thiết bị di động không phải là một nhiệm vụ dễ dàng và có thể sẽ chiếm một khoản không gian bộ nhớ (tối thiểu 600MB). Chúng tôi khuyên bạn nên có một thiết bị di động tốt, được cập nhật và sử dụng ít nhất là hệ điều hành Android 11.

Khi bạn mở Blixt, màn hình “Chào mừng - Welcome” sẽ cung cấp cho bạn một số tùy chọn:

![Demo Blixt 01](assets/blixt_t01.webp)
Ở góc trên bên phải, bạn sẽ thấy 3 chấm kích hoạt một menu với:
- “enable Tor” - người dùng có thể bắt đầu với mạng Tor, đặc biệt nếu muốn khôi phục một node LND cũ đang chạy chỉ với các đối tác ngang hàng (peer) trên Tor.

- “Set Bitcoin Node” - nếu người dùng muốn kết nối trực tiếp với Node của mình, để đồng bộ các khối thông qua Neutrino, có thể thực hiện ngay từ màn hình chào mừng. Tùy chọn này cũng tốt trong trường hợp kết nối internet hoặc Tor của bạn không ổn định để kết nối với Node Bitcoin mặc định (node.blixtwallet.com).

## Bước đầu tiên - Tạo ví mới

Nếu bạn chọn “Tạo một ví mới - Create a new wallet”, bạn sẽ được chuyển thẳng đến màn hình chính của Blixt Wallet.

Đây là “bảng điều khiển” của bạn và cũng là “Ví LN Chính”, vì vậy hãy lưu ý, nó chỉ hiển thị số dư ví LN của bạn. Ví onchain được hiển thị riêng biệt (xem C).

![Demo Blixt 02](assets/blixt_t02.webp)

A - Biểu tượng chỉ báo đồng bộ khối Blixt. Đây là điều quan trọng nhất cho một node LN: phải được đồng bộ hóa với mạng. Nếu biểu tượng đó vẫn đang hoạt động, có nghĩa là node của bạn CHƯA SẴN SÀNG! Vì vậy hãy kiên nhẫn, đặc biệt là cho lần đồng bộ đầu tiên. Nó có thể mất khoảng 6-8 phút, tùy thuộc vào thiết bị và kết nối internet của bạn.

Bạn có thể nhấp vào đó và xem trạng thái của việc đồng bộ:

![Demo Blixt 03](assets/blixt_t03.webp)

Bạn cũng có thể nhấp vào nút “Xem nhật ký LND - Show LND Log” (A) nếu bạn muốn xem và đọc thêm chi tiết kỹ thuật của nhật ký LND, theo thời gian thực. Rất hữu ích cho việc gỡ lỗi và học hỏi thêm về cách LN hoạt động.

B - Tại đây bạn có thể truy cập tất cả các Cài đặt của Blixt, và có rất nhiều! Blixt cung cấp nhiều tính năng và tùy chọn phong phú để quản lý node LN của bạn như một chuyên gia. Tất cả các tùy chọn này được giải thích chi tiết trong [“Trang tính năng Blixt - Menu tùy chọn”](https://blixtwallet.github.io/features#blixt-options).

C - Tại đây bạn có menu “Ngăn kéo ma thuật - Magic Drawer”, cũng được giải thích chi tiết ở đây. Đây là “Ví Onchain” (B), Kênh Lightning (C), Liên hệ, Biểu tượng trạng thái kênh (A), Keysend (D).

![Demo Blixt 04](assets/blixt_t04.webp)

D - Là menu trợ giúp, với các liên kết đến trang FAQ / Hướng dẫn, liên hệ nhà phát triển, trang Github và nhóm hỗ trợ Telegram.

E - Chỉ địa chỉ BTC đầu tiên của bạn, nơi bạn có thể gửi số sat thử nghiệm đầu tiên của mình. ĐIỀU NÀY LÀ TÙY CHỌN! Nếu bạn gửi trực tiếp vào địa chỉ đó, bạn đang mở một kênh LN với Node của Blixt. Điều đó có nghĩa là bạn sẽ thấy số sat của mình, chuyển vào một giao dịch onchain khác (tx), để mở kênh LN đó. Bạn có thể kiểm tra điều đó trong ví onchain của Blixt (xem điểm C), bằng cách nhấp vào menu TX ở góc trên bên phải.

![Demo Blixt 05](assets/blixt_t05.webp)

Như bạn có thể thấy trong Nhật ký giao dịch onchain, các bước được chỉ ra rất chi tiết, chỉ ra nơi mà sat đang đi (gửi tiền, mở, đóng kênh)

> KHUYẾN NGHỊ: Sau khi thử nghiệm nhiều tình huống, chúng tôi đã đến kết luận rằng việc mở kênh ở khoảng giữa 1 và 5 triệu sat là hiệu quả hơn nhiều. Các kênh nhỏ hơn có xu hướng cạn kiệt nhanh chóng và phải trả một tỷ lệ phí cao hơn so với các kênh lớn hơn.
F - Chỉ ra số dư ví Lightning chính của bạn. Đây KHÔNG phải là tổng số dư ví Blixt của bạn, nó chỉ đại diện cho số sat bạn có trong các kênh Lightning, có sẵn để gửi. Như đã chỉ ra trước đó, ví onchain là riêng biệt. Hãy nhớ về khía cạnh này. Ví onchain được tách biệt vì một lý do quan trọng: nó chủ yếu được sử dụng để mở/đóng các kênh LN.

Vậy giờ bạn đã gửi một số sat vào địa chỉ onchain được hiển thị trên màn hình chính. Khi làm điều đó, bạn được khuyến nghị giữ ứng dụng Blixt của bạn trực tuyến và hoạt động một thời gian, cho đến khi giao dịch BTC được các thợ đào đưa vào khối đầu tiên.

Sau đó có thể mất đến 20-30 phút cho đến khi được xác nhận hoàn toàn và kênh được mở, bạn sẽ thấy nó trong Magic Drawer - Lightning Channels ở trạng thái kích hoạt. Cũng như dấu chấm màu nhỏ ở trên cùng của ngăn kéo, nếu là màu xanh lá cây sẽ chỉ ra rằng kênh LN của bạn đang trực tuyến và sẵn sàng để được sử dụng để gửi sat qua LN.

Địa chỉ và thông điệp chào mừng hiển thị sẽ biến mất. Không cần thiết phải mở một kênh tự động nữa. Bạn cũng có thể vô hiệu hóa tùy chọn trong menu Cài đặt.

Đã đến lúc chuyển sang, thử nghiệm các tính năng và tùy chọn khác để mở kênh LN.

Bây giờ, hãy mở một kênh khác với một node ngang hàng khác. Cộng đồng Blixt đã tổng hợp [một danh sách các node chất lượng để bắt đầu sử dụng với Blixt.](https://github.com/hsjoberg/blixt-wallet/issues/1033)

### Quy trình mở một kênh LN riêng tư bình thường trong node di động Blixt của bạn

Điều này rất đơn giản, chỉ cần thực hiện một số bước và một chút kiên nhẫn:
- Đi đến [danh sách Cộng đồng Blixt](https://github.com/hsjoberg/blixt-wallet/issues/1033) của các đối tác ngang hàng chất lượng
- Chọn một node và nhấp vào tiêu đề liên kết của nó, nó sẽ mở trang Amboss của nó
- Nhấp để hiển thị mã QR cho địa chỉ URI của node

![Demo Blixt 06](assets/blixt_t06.webp)

Bây giờ, mở Blixt và đi đến ngăn kéo trên cùng - Kênh Lightning (Lightning Channels) và nhấp vào nút “+”

![Demo Blixt 07](assets/blixt_t07.webp)

Bây giờ, nhấp vào (A) camera để quét mã QR từ trang Amboss và thông tin chi tiết của node sẽ được điền. Thêm số lượng sat cho kênh bạn muốn và sau đó chọn mức phí cho giao dịch. Bạn có thể để tự động (B) để nhanh được xác nhận hơn hoặc điều chỉnh nó bằng cách trượt nút. Bạn cũng có thể nhấn và giữ số và chỉnh sửa nó theo ý bạn.

Đừng đặt ít hơn 1 sat/vbyte! Thông thường tốt hơn là [tham khảo phí mempool](https://mempool.space/) trước khi mở một kênh và chọn một mức phí hợp lý.

Xong, bây giờ chỉ cần nhấp vào nút “Mở kênh - Open Channel” và chờ 3 xác nhận, thường mất 30 phút (1 khối khoảng mỗi 10 phút).

Một khi được xác nhận, bạn sẽ thấy kênh hoạt động trong phần “Kênh Lightning - Lightning Channels” của mình.

## Bước thứ hai - Nhận thêm thanh khoản đầu vào

Ok vậy giờ chúng ta đã có một kênh LN chỉ với thanh khoản ĐẦU RA. Điều đó có nghĩa là chúng ta chỉ có thể GỬI, chúng ta vẫn chưa thể NHẬN sat qua LN. Tại sao? Bạn đã đọc các hướng dẫn được chỉ ra ở đầu không? Không? Quay lại và đọc chúng. Rất quan trọng để hiểu cách hoạt động của các kênh LN.

![Demo Blixt 08](assets/blixt_t08.webp)
Như bạn có thể thấy trong ví dụ này, kênh mở với khoản tiền gửi đầu tiên, không có quá nhiều tính thanh khoản ĐẦU VÀO ("Có thể nhận") nhưng lại có rất nhiều tính thanh khoản ĐẦU RA ("Có thể gửi").
Vậy bạn có những lựa chọn nào, nếu bạn muốn nhận được nhiều sat hơn qua LN?
- Tiêu một số sat từ kênh hiện tại. Đúng vậy, LN là một mạng lưới thanh toán của Bitcoin, chủ yếu được sử dụng để bạn có thể chi tiêu số sat của mình nhanh chóng, rẻ hơn, kín đáo và dễ dàng. LN KHÔNG phải là nới để giữ sat, cho mục đích đó bạn có ví onchain.
- Chuyển đổi một số sat, trở lại ví onchain của bạn, sử dụng dịch vụ chuyển đổi tàu ngầm. Theo cách này, bạn không tiêu sat của mình, mà là chuyển chúng trở lại ví onchain của bạn. Tại đây bạn có thể xem chi tiết một số phương pháp, trong [Trang hướng dẫn Blixt](https://blixtwallet.github.io/guides).
- Mở một kênh ĐẦU VÀO từ bất kỳ nhà cung cấp dịch vụ LSP nào. Đây là một video demo về [cách sử dụng LNBig LSP để mở một kênh đầu vào](https://blixtwallet.github.io/assets/images/blixt-lnbig.mp4). Điều này có nghĩa, bạn sẽ trả một khoản phí nhỏ cho một kênh TRỐNG (về phía bạn) và bạn sẽ có thể nhận được nhiều sat hơn vào kênh đó. Nếu bạn là một người bán hàng nhận được nhiều hơn là chi tiêu, đây là một lựa chọn tốt. Cũng như nếu bạn đang mua sat qua LN, sử dụng Robosat hoặc bất kỳ sàn giao dịch LN nào khác.
- Mở một kênh Dunder, với node Blixt hoặc bất kỳ nhà cung cấp dịch vụ LSP Dunder nào khác. Một kênh Dunder là một cách đơn giản để nhận được một lượng thanh khoản ĐẦU VÀO, nhưng đồng thời bạn cũng gửi một số sat vào kênh đó. Điều này cũng tốt vì nó sẽ mở kênh với một [UTXO](https://en.bitcoin.it/wiki/UTXO) không phải từ ví Blixt của bạn. Điều này tăng thêm tính riêng tư.
Điều này cũng tốt vì, nếu bạn không có sat trong ví onchain để mở một kênh LN bình thường, nhưng bạn có chúng trong một ví LN khác, bạn có thể chỉ cần thanh toán từ ví khác đó qua LN cho việc mở và gửi tiền (về phía bạn) của kênh Dunder đó. [Xem thêm chi tiết về cách Dunder hoạt động và cách chạy máy chủ của riêng bạn tại đây.](https://github.com/hsjoberg/dunder-lsp)

![Demo Blixt 09](assets/blixt_t09.webp)

Dưới đây là các bước để kích hoạt việc mở một kênh Dunder:
- Vào Cài đặt, trong mục “Thử nghiệm - Experiments” kích hoạt ô cho “Kích hoạt Dunder LSP - Enable Dunder LSP”.
- Sau khi bạn làm điều đó, quay lại mục “Lightning Network” và bạn sẽ thấy xuất hiện tùy chọn “Thiết lập Máy chủ Dunder LSP - Set Dunder LSP Server”. Tại đây, mặc định được đặt là “https://dunder.blixtwallet.com” nhưng bạn có thể thay đổi nó bằng bất kỳ địa chỉ nhà cung cấp Dunder LSP nào khác. [Đây là danh sách cộng đồng Blixt](https://github.com/hsjoberg/blixt-wallet/issues/1033) với các node có thể cung cấp kênh LSP Dudner cho Blixt của bạn.
- Bây giờ bạn có thể quay lại màn hình chính và nhấn vào nút “Nhận - Receive”. Sau đó làm theo quy trình này được giải thích [trong hướng dẫn này](https://blixtwallet.github.io/guides#guide-lsp).

OK, vậy là sau khi kênh Dunder được xác nhận (sẽ mất vài phút) bạn sẽ kết thúc với việc có 2 kênh LN: một được mở ban đầu với autopilot (kênh A) và một với tính thanh khoản đầu vào nhiều hơn, được mở với Dunder (kênh B).
![Demo Blixt 10](assets/blixt_t10.webp)
Tốt, bây giờ bạn đã sẵn sàng để gửi và nhận đủ sat qua LN!

## Bước thứ ba - Quy trình khôi phục Node

Vậy bây giờ, chúng ta hãy thảo luận về cách khôi phục ví Blixt hoặc bất kỳ node LND bị hỏng nào khác. Đây là phần kỹ thuật hơn một chút, nhưng xin hãy chú ý. Nó không quá khó.

> NHẮC NHỞ: Trước đây, tôi đã viết một bài hướng dẫn chi tiết với nhiều lựa chọn [cách khôi phục một node LND bị hỏng](https://darthcoin.substack.com/p/umbrel-btcln-node-shtf-scenario), nơi tôi cũng đã đề cập đến phương pháp sử dụng Blixt để khôi phục nhanh, sử dụng hạt giống + tệp channel.backup từ node LND đã chết của bạn. Tôi cũng đã viết một hướng dẫn cách khôi phục node Blixt của bạn hoặc chuyển node Blixt sang một thiết bị khác, [tại đây](https://blixtwallet.github.io/faq#blixt-restore).

![Demo Blixt 11](assets/blixt_t11.webp)

Nhưng hãy diễn giải quy trình này bằng các bước đơn giản. Như bạn có thể thấy trong hình trên, có 2 việc bạn cần làm để khôi phục node Blixt/LND trước đó của bạn:
- Ô trên cùng (A) là nơi bạn phải điền tất cả 24 từ hạt giống (node cũ / đã chết)
- Phía dưới (B) là hai nút tùy chọn để chèn / tải lên tệp channel.backup, đã được lưu trước đó từ node Blixt/LND cũ của bạn. Nó có thể từ một tệp cục bộ (bạn đã tải nó vào thiết bị của mình trước đó) hoặc có thể từ một vị trí tách biệt trên Google Drive / iCloud. Blixt có tùy chọn này để lưu bản sao lưu kênh của bạn trực tiếp vào Google / iCloud Drive. Xem thêm chi tiết tại [Trang tính năng Blixt](https://blixtwallet.github.io/features#blixt-options).

Cần phải nói thêm, nếu trước đó bạn không có bất kỳ kênh LN nào đang mở, thì không cần phải tải lên bất kỳ tệp channel.backup nào. Chỉ cần nhập 24 từ hạt giống và nhấn nút khôi phục.

Đừng quên kích hoạt Tor, từ menu 3 chấm ở trên cùng, như chúng tôi đã giải thích trong chương "Bước đầu tiên" của hướng dẫn này. Đó là trường hợp khi bạn CHỈ có các đối tác ngang hàng Tor và không thể được liên hệ qua clearnet (domain/IP). Nếu không thì không cần thiết.

Một tính năng hữu ích khác là thiết lập một node Bitcoin cụ thể từ menu trên cùng. Theo mặc định, nó đồng bộ các block từ node.blixtwallet.com (chế độ neutrino) nhưng bạn có thể thiết lập bất kỳ node Bitcoin nào khác cung cấp đồng bộ neutrino.

Như vậy một khi bạn điền những tùy chọn đó, và nhấn nút khôi phục, Blixt sẽ bắt đầu đồng bộ các khối thông qua Neutrino như chúng ta đã giải thích trong chương "Bước đầu tiên" của hướng dẫn này. Vì vậy, hãy kiên nhẫn và theo dõi quá trình khôi phục trên màn hình chính, bằng cách nhấp vào biểu tượng đồng bộ.

![Demo Blixt 12](assets/blixt_t12.webp)

Như bạn có thể thấy trong ví dụ này, nó cho thấy các khối bitcoin đã được đồng bộ hóa 100% (A) và quá trình khôi phục đang diễn ra (B). Điều đó có nghĩa là các kênh LN mà bạn đã có trước đó, sẽ được đóng và các quỹ sẽ được khôi phục vào ví onchain Blixt của bạn.

Quá trình này sẽ tốn thời gian! Vì vậy, xin hãy kiên nhẫn và cố gắng giữ cho Blixt của bạn hoạt động và trực tuyến. Đồng bộ ban đầu có thể mất khoản 6-8 phút và đóng các kênh có thể mất khoảng 10-15 phút. Vì vậy, bạn nên sạc thiết bị đầy đủ.
Khi quá trình này được bắt đầu, bạn có thể kiểm tra trong Magic Drawer - Lightning Channels, trạng thái của từng kênh trước đó của bạn, cho thấy chúng đang ở trạng thái “đang chờ đóng”. Khi mỗi kênh được đóng, bạn có thể thấy giao dịch đóng trong ví onchain (xem Magic Drawer - Onchain), và mở menu nhật ký giao dịch.

![Demo Blixt 13](assets/blixt_t13.webp)

Cũng sẽ tốt nếu bạn kiểm tra và thêm vào, nếu chưa có, các đối tác trước đây bạn đã có trong node LN cũ của mình. Vì vậy, hãy vào menu Cài đặt, xuống “Lightning Network” và chọn tùy chọn “Show Lightning Peers”.

![Demo Blixt 14](assets/blixt_t14.webp)

Trong phần này, bạn sẽ thấy các đối tác bạn đang kết nối tại thời điểm đó và bạn có thể thêm, tốt hơn là thêm những người bạn đã có kênh trước đó. Chỉ cần vào trang Amboss, tìm kiếm tên bí danh của node đối tác hoặc nodeID và quét URI node của họ.

![Demo Blixt 15](assets/blixt_t15.webp)

Như bạn có thể thấy trong hình trên, có 3 phần:

A - đại diện cho địa chỉ URI node clearnet (domain/IP)

B - đại diện cho địa chỉ URI node Tor onion (.onion)

C - là mã QR để quét bằng camera Blixt hoặc nút sao chép.

Địa chỉ URI node này bạn phải thêm vào danh sách đối tác ngang hàng của mình. Vì vậy, hãy lưu ý rằng chỉ có tên bí danh của node hoặc nodeID là không đủ.

Bây giờ bạn có thể vào Magic Drawer (menu trên cùng bên trái) - Lightning Channels, và bạn có thể thấy ở độ cao khối "trưởng thành" mà tiền sẽ được trả lại vào địa chỉ onchain của bạn.

![Demo Blixt 16](assets/blixt_t16.webp)

Số khối 764272 là khi tiền sẽ có thể sử dụng trong địa chỉ bitcoin onchain của bạn. Và nó có thể mất đến 144 khối từ khối xác nhận đầu tiên cho đến khi được giải phóng. Vì vậy, hãy kiểm tra điều đó trong [mempool](https://mempool.space/).

Và đó là tất cả. Chỉ cần kiên nhẫn chờ đợi cho đến khi tất cả các kênh được đóng và tiền trở lại ví onchain của bạn.

## Bước thứ tư - Tùy chỉnh

Chương này nói về việc tùy chỉnh và hiểu rõ hơn về node Blixt của bạn. Tôi sẽ không mô tả tất cả các tính năng có sẵn, có quá nhiều và đã được giải thích trước đó trong [Trang tính năng Blixt](https://blixtwallet.github.io/features).

Nhưng tôi sẽ chỉ ra một số tính năng cần thiết để bạn tiếp tục sử dụng Blixt và có trải nghiệm tốt.

### A - Tên (NameDesc)

![Demo Blixt 17](assets/blixt_t17.webp)

[NameDesc](https://github.com/lightning/blips/blob/master/blip-0011.md) là một tiêu chuẩn để truyền đạt "tên người nhận" trong hóa đơn BOLT11.

Đây có thể là bất kỳ tên nào và có thể được thay đổi bất cứ lúc nào.

Tùy chọn này thực sự hữu ích trong nhiều trường hợp, khi bạn muốn gửi một tên cùng với mô tả hóa đơn, để người nhận có thể biết được ai đã gửi những sat đó. Đây là tùy chọn hoàn toàn và cũng có trên màn hình thanh toán, người dùng phải đánh dấu vào ô để báo hiệu rằng gửi tên bí danh.

Dưới đây là một ví dụ về cách hiển thị khi bạn sử dụng [chat.blixtwallet.com](https://chat.blixtwallet.com/)

![Demo Blixt 18](assets/blixt_t18.webp)

Đây là một ví dụ khác khi gửi đến một ứng dụng ví khác hỗ trợ NameDesc:

![Demo Blixt 19](assets/blixt_t19.webp)

### B - Sao lưu Kênh LN và cụm từ hạt giống

Đây là một tính năng rất quan trọng!
Sau khi mở hoặc đóng một kênh LN, bạn nên thực hiện sao lưu. Việc này có thể được thực hiện thủ công bằng cách lưu một tệp nhỏ vào thiết bị cục bộ (thường là thư mục tải xuống) hoặc sử dụng tài khoản Google Drive hoặc iCloud.
![Demo Blixt 20](assets/blixt_t20.webp)

Đi tới Cài đặt Blixt - mục Ví. Tại đây, bạn có các tùy chọn để lưu tất cả dữ liệu quan trọng cho ví Blixt của mình:
- “Hiển thị mnemonic - Show mnemonic” - sẽ hiển thị 24 từ khóa để bạn ghi chú lại
- “Xóa mnemonic khỏi thiết bị - Remove mnemonic from device” - đây là tùy chọn không bắt buộc và chỉ sử dụng nếu bạn thực sự muốn loại bỏ các từ khóa khỏi thiết bị của mình. Điều này sẽ KHÔNG xóa ví của bạn, chỉ xóa các từ khóa hạt giống. Nhưng hãy cẩn thận! Không có cách nào để khôi phục chúng nếu bạn không ghi chú lại trước.
- “Xuất sao lưu kênh - Export channel backup” - tùy chọn này sẽ lưu một tệp nhỏ vào thiết bị cục bộ của bạn, thường là vào thư mục “tải xuống”, từ đó bạn có thể lấy nó và di chuyển ra khỏi thiết bị của mình để bảo quản an toàn.
- “Xác minh sao lưu kênh - Verify channel backup” - đây là tùy chọn tốt nếu bạn sử dụng Google Drive hoặc iCloud để kiểm tra tính toàn vẹn của bản sao lưu thực hiện từ xa.
- “Sao lưu kênh trên Google Drive - Google drive channel backup” - sẽ sao lưu tệp sao lưu vào Google Drive cá nhân của bạn. Tệp được mã hóa và được lưu trữ trong một kho lưu trữ riêng biệt so với các tệp google thông thường của bạn. Vì vậy, không có lo ngại nào về việc tệp có thể được đọc bởi bất kỳ ai. Dù sao thì tệp đó cũng hoàn toàn vô dụng nếu không có các cụm từ hạt giống, vì vậy không ai có thể lấy tiền từ tệp đó cả.

Tôi sẽ đưa ra lời khuyên cho phần này như sau:
- Sử dụng một trình quản lý mật khẩu để lưu trữ an toàn cụm từ hạt giống và tệp sao lưu của bạn. [KeePass](https://keepass.info/) hoặc Bitwarden rất tốt cho việc này và có thể được sử dụng trên nhiều nền tảng và tự lưu trữ hoặc ngoại tuyến.
- THỰC HIỆN SAO LƯU MỖI KHI bạn mở hoặc đóng một kênh. Tệp đó được cập nhật với thông tin của các kênh. Không cần phải thực hiện sau mỗi giao dịch bạn đã thực hiện trên LN. Sao lưu kênh không lưu trữ thông tin đó, chỉ lưu trữ trạng thái của kênh.

![Demo Blixt 21](assets/blixt_t21.webp)

## Kết luận

OK, có nhiều tính năng tuyệt vời khác mà Blixt cung cấp, tôi sẽ để bạn khám phá từng cái một và tận hưởng hành trình đó.

Ứng dụng này thực sự bị đánh giá thấp, chủ yếu vì không được tài trợ bởi bất kỳ quỹ đầu tư mạo hiểm nào, được điều hành bởi cộng đồng, xây dựng với tình yêu và đam mê dành cho Bitcoin và Lightning Network.

Node LN di động này, Blixt, là một công cụ rất mạnh mẽ trong tay của nhiều người dùng, nếu họ biết cách sử dụng nó một cách hiệu quả. Chỉ cần tưởng tượng, bạn đang đi khắp thế giới với một node LN trong túi của mình và không ai biết điều đó.

Và chưa nói đến tất cả các tính năng phong phú khác đi kèm, mà rất ít hoặc không có ứng dụng ví nào khác có thể cung cấp.

Tôi hy vọng bạn thích sử dụng nó. Cá nhân tôi, tôi yêu thích nó và nó rất hữu ích đối với tôi (tôi xem ở đây một trường hợp sử dụng mà ví này là một công cụ tuyệt vời).

CHÚC MỪNG BITCOIN LIGHTNING!

Nguyện Mong ₿ITCOIN Ở Bên Bạn!

> LƯU Ý: Tôi không được trả tiền hoặc hỗ trợ bằng bất kỳ cách nào từ các nhà phát triển của ứng dụng này. Tôi viết hướng dẫn này vì tôi thấy rằng sự quan tâm đến ứng dụng ví này đang tăng lên và người dùng mới vẫn không hiểu cách bắt đầu với nó. Cũng để giúp Hampus (nhà phát triển chính) có tài liệu về việc sử dụng ví node này. Tôi không có bất kỳ lợi ích nào khác trong việc quảng bá ứng dụng LN này, ngoài việc thúc đẩy việc áp dụng Bitcoin và LN. Đây là cách duy nhất!
