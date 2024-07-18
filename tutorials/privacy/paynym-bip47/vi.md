---
name: BIP47 - PayNym

description: Cách PayNyms hoạt động
---
***CẢNH BÁO:** Sau vụ bắt giữ các nhà sáng lập của Samourai Wallet và việc tịch thu máy chủ của họ vào ngày 24 tháng 4, ứng dụng không còn có thể sử dụng bởi những người dùng không có Dojo riêng của họ. BIP47 vẫn có thể sử dụng trên Sparrow Wallet cho tất cả người dùng và **trên Samourai Wallet chỉ dành cho những người dùng có Dojo**.*

_Chúng tôi đang chú ý theo dõi sự phát triển của vụ việc này cũng như các công cụ liên quan. Hãy yên tâm rằng chúng tôi sẽ cập nhật hướng dẫn này khi có thông tin mới._

_Hướng dẫn này chỉ mang tính chất giáo dục và thông tin. Chúng tôi không ủng hộ hoặc khuyến khích việc sử dụng những công cụ này cho mục đích phạm tội. Mỗi người dùng có trách nhiệm tuân thủ luật pháp tại quốc gia của họ._

---

> "Nó quá to," tất cả mọi người đều nói, và con gà tây, người đã sinh ra với cựa và nghĩ mình là một hoàng đế, phồng lên như một con tàu với tất cả các buồm được căng ra, và tiến thẳng đến anh ta trong cơn thịnh nộ lớn, mắt đỏ như lửa. Chú vịt con tội nghiệp không biết nên đứng lại hay chạy trốn, và cảm thấy rất không hạnh phúc vì bị tất cả các con vịt trong sân khinh thường.

![BIP47, minh họa chú vịt xấu xí](assets/1.webp)

Một trong những vấn đề đáng kể nhất trên giao thức Bitcoin là việc tái sử dụng địa chỉ. Sự minh bạch và phân phối của mạng lưới khiến thực hành này nguy hiểm cho quyền riêng tư của người dùng. Để tránh những vấn đề liên quan đến điều này, người ta khuyến nghị sử dụng một địa chỉ nhận mới trống cho mỗi khoản thanh toán đến mới vào ví, điều này có thể khó thực hiện trong một số trường hợp.

Sự thỏa hiệp này đã tồn tại ngay từ Bản Trắng. Satoshi đã cảnh báo chúng ta về rủi ro này trong công trình của ông được công bố vào cuối năm 2008:

> "Như một bức tường lửa bổ sung, một cặp khóa mới nên được sử dụng cho mỗi giao dịch để giữ chúng không bị liên kết với một chủ sở hữu chung."

Có nhiều giải pháp có sẵn để nhận nhiều khoản thanh toán mà không cần tái sử dụng địa chỉ. Mỗi giải pháp đều có những thỏa hiệp và hạn chế của nó. Trong tất cả các giải pháp này, có [BIP47](https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki), một đề xuất được phát triển bởi Justus Ranvier và công bố vào năm 2015, cho phép tạo ra các mã thanh toán có thể tái sử dụng. Mục tiêu của nó là cho phép thực hiện nhiều giao dịch cho cùng một người mà không cần tái sử dụng địa chỉ.

Ban đầu, đề xuất này đã bị một phần của cộng đồng khinh thường, và nó không bao giờ được thêm vào Bitcoin Core. Tuy nhiên, một số phần mềm vẫn chọn triển khai nó một cách độc lập. Ví dụ, Samourai Wallet đã phát triển triển khai BIP47 của riêng mình: PayNym. Ngày nay, triển khai này có sẵn trên Samourai Wallet cho điện thoại thông minh, cũng như trên [Sparrow Wallet](https://sparrowwallet.com/) cho máy tính.

Theo thời gian, Samourai đã lập trình các tính năng mới trực tiếp liên quan đến PayNym. Bây giờ, có một hệ sinh thái toàn bộ các công cụ có sẵn để tối ưu hóa quyền riêng tư của người dùng dựa trên PayNym và BIP47.
Trong bài viết này, bạn sẽ khám phá nguyên tắc của BIP47 và PayNym, cơ chế của các giao thức này, và các ứng dụng thực tế phát sinh từ chúng. Tôi chỉ đề cập đến phiên bản đầu tiên của BIP47, hiện đang được sử dụng cho PayNym, nhưng các phiên bản 2, 3, và 4 hoạt động gần như cùng một cách.
Chỉ có một sự khác biệt lớn được tìm thấy trong giao dịch thông báo. Phiên bản 1 sử dụng một địa chỉ đơn giản với OP_RETURN cho thông báo, phiên bản 2 sử dụng một kịch bản multisig (bloom-multisig) với OP_RETURN, và phiên bản 3 và 4 đơn giản chỉ sử dụng một kịch bản multisig (cfilter-multisig). Các cơ chế được thảo luận trong bài viết này, bao gồm các phương pháp mật mã được nghiên cứu, do đó, áp dụng được cho cả bốn phiên bản. Đến nay, việc triển khai PayNym trên Samourai Wallet và Sparrow sử dụng phiên bản đầu tiên của BIP47.

## Tóm tắt:

1- Vấn đề tái sử dụng địa chỉ.

2- Nguyên tắc của BIP47 và PayNym.

3- Hướng dẫn: Sử dụng PayNym.

- Xây dựng một giao dịch BIP47 với Samourai Wallet.
- Xây dựng một giao dịch BIP47 với Sparrow Wallet.

4- Cách thức hoạt động của BIP47.

- Mã thanh toán có thể tái sử dụng.
- Phương pháp mật mã: Trao đổi khóa Diffie-Hellman được thiết lập trên đường cong elliptic (ECDH).
- Giao dịch thông báo.
- Xây dựng giao dịch thông báo.
- Nhận giao dịch thông báo.
- Giao dịch thanh toán BIP47.
- Nhận thanh toán BIP47 và suy ra khóa riêng.
- Hoàn trả thanh toán BIP47.

5- Các ứng dụng phái sinh của PayNym.

6- Ý kiến cá nhân của tôi về BIP47.

## Vấn đề tái sử dụng địa chỉ.

Một địa chỉ nhận được sử dụng để nhận bitcoin. Nó được tạo ra từ một khóa công khai bằng cách băm nó và áp dụng một định dạng cụ thể. Như vậy, nó cho phép tạo ra một điều kiện chi tiêu mới trên một đồng xu để thay đổi chủ sở hữu của nó.

> Để tìm hiểu thêm về việc tạo ra một địa chỉ nhận, tôi khuyên bạn đọc phần cuối của bài viết này: The Bitcoin Wallet - trích từ [ebook Bitcoin Démocratisé 2](https://www.pandul.fr/post/le-portefeuille-bitcoin-extrait-ebook-bitcoin-d%C3%A9mocratis%C3%A9-2#viewer-epio7).

Hơn nữa, bạn có thể đã nghe từ một người am hiểu về bitcoin rằng các địa chỉ nhận chỉ nên sử dụng một lần, và bạn nên tạo một địa chỉ mới cho mỗi khoản thanh toán đến mới vào ví của bạn. Được, nhưng tại sao?
Cơ bản, việc tái sử dụng địa chỉ không trực tiếp gây nguy hiểm cho quỹ của bạn. Việc sử dụng mật mã trên đường cong elliptic cho phép bạn chứng minh với mạng lưới rằng bạn đang sở hữu một khóa riêng mà không cần tiết lộ khóa đó. Do đó, bạn có thể khóa nhiều UTXOs (Unspent Transaction Outputs) khác nhau trên cùng một địa chỉ và chi tiêu chúng vào các thời điểm khác nhau. Nếu bạn không tiết lộ khóa riêng liên quan đến địa chỉ đó, không ai có thể truy cập vào quỹ của bạn. Vấn đề với việc tái sử dụng địa chỉ liên quan nhiều hơn đến quyền riêng tư.

Như đã đề cập trong phần giới thiệu, sự minh bạch và phân phối của mạng lưới Bitcoin có nghĩa là bất kỳ người dùng nào có quyền truy cập vào một nút có thể quan sát các giao dịch của hệ thống thanh toán. Kết quả là, họ có thể thấy các số dư khác nhau của các địa chỉ. Satoshi Nakamoto sau đó đã đề cập đến khả năng tạo ra các cặp khóa mới, và do đó, các địa chỉ mới, cho mỗi khoản thanh toán đến mới vào một ví. Mục tiêu sẽ là có một bức tường lửa bổ sung trong trường hợp có sự liên kết giữa danh tính của người dùng và một trong các cặp khóa của họ.

Ngày nay, với sự hiện diện của các công ty phân tích chuỗi và sự phát triển của KYC (Know Your Customer), việc sử dụng các địa chỉ trắng không còn là một bức tường lửa bổ sung, mà là một nghĩa vụ đối với bất kỳ ai quan tâm đến quyền riêng tư của mình dù chỉ một chút.

Việc theo đuổi quyền riêng tư không phải là một sự thoải mái hay một ảo tưởng của những người ủng hộ Bitcoin tối đa. Đó là một tham số cụ thể ảnh hưởng trực tiếp đến an ninh cá nhân và an ninh của quỹ của bạn. Để giúp bạn hiểu điều này, dưới đây là một ví dụ rất cụ thể:
- Bob mua Bitcoin thông qua phương pháp Dollar Cost Averaging (DCA), nghĩa là anh ấy mua một lượng nhỏ Bitcoin tại các khoảng thời gian đều đặn để trung bình giá nhập của mình. Bob hệ thống hóa việc gửi số tiền mua được vào cùng một địa chỉ nhận. Anh ấy mua 0.01 Bitcoin mỗi tuần và gửi nó vào địa chỉ này. Sau hai năm, Bob đã tích lũy được một Bitcoin đầy đủ trên địa chỉ này.
- Người bán bánh ở góc phố chấp nhận thanh toán bằng Bitcoin. Phấn khích vì có thể chi tiêu Bitcoin, Bob đi mua bánh mì baguette bằng satoshis. Để thanh toán, anh ấy sử dụng số tiền bị khóa với địa chỉ của mình. Bây giờ người bán bánh biết rằng anh ấy sở hữu một Bitcoin. Số lượng lớn này có thể thu hút sự ghen tị, và Bob có thể đối mặt với nguy cơ bị tấn công vật lý trong tương lai.

Việc tái sử dụng địa chỉ cho phép một người quan sát tạo ra một liên kết không thể chối cãi giữa các UTXO khác nhau của bạn và đôi khi giữa danh tính của bạn và toàn bộ ví của bạn.
Đó là lý do tại sao phần lớn phần mềm ví Bitcoin tự động tạo ra một địa chỉ nhận mới khi bạn nhấp vào nút "Nhận". Đối với người dùng thông thường, việc làm quen với việc sử dụng địa chỉ mới không phải là một sự bất tiện lớn. Tuy nhiên, đối với một doanh nghiệp trực tuyến, một sàn giao dịch, hoặc một chiến dịch quyên góp, ràng buộc này có thể nhanh chóng trở nên khó quản lý.
Có nhiều giải pháp cho các tổ chức này. Mỗi giải pháp đều có ưu và nhược điểm của nó, nhưng đến nay, và như chúng ta sẽ thấy sau, BIP47 thực sự nổi bật so với các giải pháp khác.

Vấn đề tái sử dụng địa chỉ trong Bitcoin không phải là không đáng kể. Như bạn có thể thấy trong biểu đồ dưới đây lấy từ trang web oxt.me, tỷ lệ tái sử dụng địa chỉ tổng thể của người dùng Bitcoin hiện tại là 52%:
Biểu đồ từ OXT.me cho thấy sự phát triển của tỷ lệ tái sử dụng địa chỉ tổng thể trên mạng lưới Bitcoin.

![image](assets/2.webp)

Credit: OXT

Phần lớn các trường hợp tái sử dụng này đến từ các sàn giao dịch, vì lý do hiệu quả và tiện lợi, tái sử dụng cùng một địa chỉ nhiều lần. Đến nay, BIP47 sẽ là giải pháp tốt nhất để ngăn chặn hiện tượng này giữa các sàn giao dịch. Điều này sẽ giúp giảm tỷ lệ tái sử dụng địa chỉ tổng thể mà không gây ra quá nhiều trở ngại cho các thực thể này.

Biện pháp toàn cầu này trên toàn bộ mạng lưới đặc biệt có liên quan trong trường hợp này. Thực sự, tái sử dụng địa chỉ không chỉ là vấn đề đối với người thực hiện hành vi này, mà còn đối với bất kỳ ai giao dịch với họ. Sự mất mát quyền riêng tư trên Bitcoin hoạt động như một virus, lan truyền từ người dùng này sang người dùng khác. Việc nghiên cứu một biện pháp toàn cầu trên tất cả các giao dịch mạng lưới cho phép chúng ta hiểu được quy mô của hiện tượng này.

## Nguyên tắc của BIP47 và PayNym.

BIP47 nhằm cung cấp một cách đơn giản để nhận nhiều khoản thanh toán mà không cần tái sử dụng địa chỉ. Hoạt động của nó dựa trên việc sử dụng một mã thanh toán có thể tái sử dụng.

Như vậy, nhiều người gửi có thể gửi nhiều khoản thanh toán cho một mã thanh toán có thể tái sử dụng duy nhất của người dùng khác, mà không cần người nhận phải cung cấp một địa chỉ trống mới cho mỗi giao dịch mới.

Người dùng có thể tự do chia sẻ mã thanh toán của mình (trên mạng xã hội, trên trang web của họ...) mà không có rủi ro mất quyền riêng tư, không giống như một địa chỉ nhận thông thường hoặc một khóa công khai.
Để thực hiện một giao dịch, cả hai người dùng đều phải có một ví Bitcoin với triển khai BIP47, như PayNym trên Samourai Wallet hoặc Sparrow Wallet. Sự kết hợp của mã thanh toán của hai người dùng sẽ thiết lập một kênh bí mật giữa họ. Để thiết lập kênh này một cách đúng đắn, người gửi phải thực hiện một giao dịch trên blockchain Bitcoin: giao dịch thông báo (tôi sẽ giải thích thêm về điều này sau).

Sự kết hợp của mã thanh toán của hai người dùng tạo ra các bí mật chung, chính chúng tạo ra một số lượng lớn địa chỉ nhận Bitcoin duy nhất (chính xác là 2^32). Như vậy, trong thực tế, việc thanh toán với BIP47 không được gửi đến mã thanh toán, mà đến các địa chỉ bình thường, được phái sinh từ mã thanh toán của các bên liên quan.
Mã thanh toán hoạt động như một bộ nhận dạng ảo, được tạo ra từ hạt giống ví (wallet seed). Trong cấu trúc phát sinh ví HD (HD wallet derivation structure), mã thanh toán được đặt ở độ sâu 3, tại cấp độ tài khoản ví.

![image](assets/3.webp)

Mục đích phát sinh của nó được ghi nhận là 47' (0x8000002F) theo BIP47. Ví dụ, một đường dẫn phát sinh cho mã thanh toán có thể tái sử dụng sẽ là:

> m/47'/0'/0'/

Để bạn có cái nhìn về mã thanh toán trông như thế nào, đây là mã của tôi:

> PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qDudE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5

Nó cũng có thể được mã hóa dưới dạng mã QR để thuận tiện cho việc giao tiếp:

![image](assets/4.webp)

Về PayNym Bots, những robot bạn thấy trên Twitter, chúng chỉ là biểu diễn hình ảnh của mã thanh toán của bạn, được tạo ra bởi Samourai Wallet. Chúng được tạo ra bằng cách sử dụng một hàm băm, làm cho chúng gần như là duy nhất. Đây là mã của tôi với bộ nhận dạng của nó:

> +throbbingpond8B1

![image](assets/5.webp)

Những Bots này không có bất kỳ tiện ích kỹ thuật thực sự nào. Thay vào đó, chúng giúp tạo điều kiện cho các tương tác giữa người dùng bằng cách tạo ra một danh tính hình ảnh ảo.

Đối với người dùng, quá trình thực hiện thanh toán BIP47 với triển khai PayNym cực kỳ đơn giản. Hãy tưởng tượng Alice muốn gửi thanh toán cho Bob:

1. Bob chia sẻ mã QR của mình hoặc trực tiếp mã thanh toán có thể tái sử dụng của mình. Anh ấy có thể đặt nó trên trang web của mình, trên các mạng xã hội công cộng khác nhau của mình, hoặc gửi nó cho Alice thông qua phương tiện giao tiếp khác.
2. Alice mở phần mềm Samourai hoặc Sparrow của mình và quét hoặc dán mã thanh toán của Bob.
3. Alice liên kết PayNym của mình với của Bob ("Follow" trong tiếng Anh). Thao tác này được thực hiện ngoại tuyến và hoàn toàn miễn phí.

4. Alice kết nối PayNym của mình với của Bob ("Connect" trong tiếng Anh). Thao tác này được thực hiện "trên chuỗi". Alice phải trả phí khai thác giao dịch cũng như một khoản phí cố định 15,000 sats cho dịch vụ trên Samourai. Phí dịch vụ được miễn trên Sparrow. Bước này là những gì chúng ta gọi là giao dịch thông báo.

5. Một khi giao dịch thông báo được xác nhận, Alice có thể tạo một giao dịch thanh toán BIP47 cho Bob. Ví của cô ấy sẽ tự động tạo ra một địa chỉ nhận mới trống, mà chỉ có Bob có khóa riêng.

Thực hiện giao dịch thông báo, tức là kết nối PayNym của mình, là một điều kiện tiên quyết bắt buộc để thực hiện thanh toán BIP47. Tuy nhiên, một khi điều này được thực hiện, người gửi có thể thực hiện nhiều thanh toán cho người nhận (chính xác là 2^32) mà không cần thực hiện một giao dịch thông báo mới.

Bạn có thể đã nhận thấy rằng có hai thao tác khác nhau để liên kết PayNyms với nhau: "follow" và "connect". Thao tác kết nối ("connect") tương ứng với giao dịch thông báo BIP47, chỉ đơn giản là một giao dịch Bitcoin với một số thông tin được truyền qua đầu ra OP_RETURN. Do đó, nó giúp thiết lập giao tiếp mã hóa giữa hai người dùng để tạo ra các bí mật chung cần thiết cho việc tạo ra các địa chỉ nhận mới trống.

Mặt khác, thao tác liên kết ("follow" hoặc "relier") cho phép liên kết trên Soroban, một giao thức giao tiếp mã hóa dựa trên Tor, được phát triển đặc biệt bởi các đội ngũ của Samourai.

Tóm lại:
- Liên kết hai PayNym ("theo dõi") hoàn toàn miễn phí. Điều này giúp thiết lập các kênh giao tiếp mã hóa ngoại tuyến, đặc biệt là khi sử dụng các công cụ giao dịch hợp tác của Samourai (Stowaway hoặc StonewallX2). Thao tác này đặc biệt dành cho PayNym và không được mô tả trong BIP47.
- Kết nối hai PayNym sẽ phát sinh chi phí. Điều này bao gồm việc thực hiện giao dịch thông báo để khởi tạo kết nối. Chi phí bao gồm bất kỳ phí dịch vụ nào, phí khai thác giao dịch, và 546 sats được gửi đến địa chỉ thông báo của người nhận để thông báo cho họ về việc mở đường hầm. Thao tác này liên quan đến BIP47. Một khi hoàn thành, người gửi có thể thực hiện nhiều giao dịch BIP47 với người nhận.

Để kết nối hai PayNyms, chúng phải đã được liên kết.

## Hướng dẫn: Sử dụng PayNym.

Bây giờ chúng ta đã hiểu lý thuyết, hãy cùng nhau tìm hiểu thực hành. Ý tưởng của các hướng dẫn dưới đây là liên kết PayNym của tôi trên ví Sparrow với PayNym của tôi trên ví Samourai. Hướng dẫn đầu tiên chỉ bạn cách thực hiện giao dịch sử dụng mã thanh toán có thể tái sử dụng từ Samourai sang Sparrow, và hướng dẫn thứ hai mô tả cùng một cơ chế từ Sparrow sang Samourai.

> Tôi thực hiện các hướng dẫn này trên Testnet. Đây không phải là bitcoin thật.

### Xây dựng giao dịch BIP47 với ví Samourai.

Để bắt đầu, bạn rõ ràng cần ứng dụng ví Samourai. Bạn có thể tải trực tiếp nó từ Google Play Store hoặc với tệp APK có sẵn trên trang web chính thức của Samourai.

Một khi ví được khởi tạo, nếu bạn chưa làm, yêu cầu PayNym của bạn bằng cách nhấp vào dấu cộng (+) ở góc dưới bên phải, sau đó chọn "PayNym".

Bước đầu tiên để thực hiện giao dịch BIP47 là lấy mã thanh toán có thể tái sử dụng từ người nhận của chúng ta. Sau đó, chúng ta sẽ có thể kết nối với họ và tiếp theo là liên kết:

![video](assets/6.mp4)

Một khi giao dịch thông báo được xác nhận, tôi có thể gửi nhiều khoản thanh toán cho người nhận của mình. Mỗi giao dịch sẽ tự động được thực hiện với một địa chỉ trống mới mà người nhận có chìa khóa. Người nhận không cần phải thực hiện bất kỳ hành động nào, mọi thứ đều được tính toán ở phía tôi.

Đây là cách thực hiện giao dịch BIP47 trên ví Samourai:

![video](assets/7.mp4)

### Xây dựng giao dịch BIP47 với ví Sparrow.

Giống như với Samourai, bạn rõ ràng cần phải có phần mềm Sparrow. Phần mềm này có sẵn trên máy tính của bạn. Bạn có thể tải nó từ [trang web chính thức](https://sparrowwallet.com/) của họ.

Hãy chắc chắn xác minh chữ ký của nhà phát triển và tính toàn vẹn của phần mềm đã tải trước khi cài đặt nó trên máy của bạn.

Tạo ví và yêu cầu PayNym của bạn bằng cách nhấp vào "Show PayNym" từ menu "Tool" trên thanh trên cùng:

![image](assets/8.webp)

Sau đó, bạn sẽ cần liên kết và kết nối PayNym của mình với PayNym của người nhận. Để làm điều này, nhập mã thanh toán có thể tái sử dụng của họ vào cửa sổ "Find Contact", theo dõi họ, và sau đó thực hiện giao dịch thông báo bằng cách nhấp vào "Link Contact":

![image](assets/9.webp)

Một khi giao dịch thông báo được xác nhận, bạn có thể gửi thanh toán đến mã thanh toán có thể tái sử dụng. Đây là cách làm:

![video](assets/10.mp4)

Bây giờ chúng ta đã có thể nghiên cứu khía cạnh thực hành của việc triển khai PayNym của BIP47, hãy xem tất cả các cơ chế này hoạt động như thế nào và những phương pháp mật mã nào được sử dụng.

## Cơ chế bên trong của BIP47.
Để nghiên cứu các cơ chế của BIP47, việc hiểu rõ cấu trúc của ví phân cấp xác định (HD wallet), cơ chế để tạo ra các cặp khóa con, cũng như các nguyên tắc của mật mã hình elip là rất quan trọng. May mắn thay, bạn có thể tìm thấy tất cả thông tin cần thiết để hiểu phần này trên blog của tôi:
- [Hiểu về các đường dẫn phái sinh của một ví Bitcoin](https://www.pandul.fr/post/comprendre-les-chemins-de-d%C3%A9rivation-d-un-portefeuille-bitcoin)

- [Ví Bitcoin - trích từ ebook Bitcoin Dân chủ hóa 2](https://www.pandul.fr/post/le-portefeuille-bitcoin-extrait-ebook-bitcoin-d%C3%A9mocratis%C3%A9-2)

### Mã thanh toán có thể tái sử dụng.

Như đã giải thích trong phần thứ hai của bài viết này, mã thanh toán có thể tái sử dụng nằm ở độ sâu ba của ví HD. Nó có thể so sánh với xpub, cả về vị trí và cấu trúc, cũng như vai trò của nó.

Dưới đây là các phần khác nhau tạo nên một mã thanh toán 80 byte:

- Byte 0: Phiên bản. Nếu sử dụng phiên bản đầu tiên của BIP47, byte này sẽ bằng 0x01.

- Byte 1: Trường bit. Không gian này được dành riêng để cung cấp các chỉ dẫn bổ sung trong trường hợp sử dụng cụ thể. Nếu chỉ sử dụng PayNym, byte này sẽ bằng 0x00.

- Byte 2: Tính chẵn lẻ của y. Byte này chỉ ra 0x02 hoặc 0x03 tùy thuộc vào tính chẵn lẻ (số chẵn hoặc số lẻ) của giá trị tọa độ y của khóa công khai của chúng ta. Để biết thêm thông tin về thực hành này, vui lòng đọc bước 1 của phần "phái sinh địa chỉ" của bài viết này.

- Từ byte 3 đến byte 34: Giá trị x. Các byte này chỉ ra tọa độ x của khóa công khai của chúng ta. Sự kết hợp của x và tính chẵn lẻ của y cho chúng ta khóa công khai nén của mình.

- Từ byte 35 đến byte 66: Mã chuỗi. Không gian này được dành riêng cho mã chuỗi liên kết với khóa công khai đã nêu trên.

- Từ byte 67 đến byte 79: Đệm. Không gian này được dành riêng cho các phát triển tương lai có thể có. Đối với phiên bản 1, chúng ta đơn giản điền nó bằng số không để đạt được 80 byte, là kích thước của dữ liệu cho một đầu ra OP_RETURN.

Dưới đây là biểu diễn thập lục phân của mã thanh toán có thể tái sử dụng của tôi, được trình bày trong phần trước, với các màu tương ứng với các byte đã trình bày ở trên:
Tiếp theo, bạn cũng cần thêm byte tiền tố "P" để nhanh chóng xác định rằng chúng ta đang xử lý một mã thanh toán. Byte này là 0x47.

> 0x47010002a0716529bae6b36c5c9aa518a52f9c828b46ad8d907747f0d09dcd4d9a39e97c3c5f37c470c390d842f364086362f6122f412e2b0c7e7fc6e32287e364a7a36a00000000000000000000000000

Cuối cùng, chúng ta tính toán mã kiểm tra của mã thanh toán này bằng cách sử dụng HASH256, nghĩa là băm kép với hàm SHA256. Chúng ta lấy bốn byte đầu tiên của bản tóm tắt này và nối chúng vào cuối (màu hồng).
Mã thanh toán đã sẵn sàng, giờ chúng ta chỉ cần chuyển đổi nó sang Base 58:

> PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qDudE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5

Như bạn có thể thấy, cấu trúc này rất giống với cấu trúc của một khóa công khai mở rộng loại "xpub".

Trong quá trình này để thu được mã thanh toán của chúng ta, chúng ta đã sử dụng một khóa công khai nén và một mã chuỗi. Hai yếu tố này là kết quả của một quá trình phái sinh xác định và phân cấp từ hạt giống ví, theo đường dẫn phái sinh sau: m/47'/0'/0'/
Cụ thể, để thu được khóa công khai và mã chuỗi của mã thanh toán có thể tái sử dụng, chúng ta sẽ tính toán khóa riêng tư chính từ hạt giống, sau đó phái sinh một cặp con với chỉ số 47 + 2^31 (phái sinh cứng). Sau đó, chúng ta phái sinh thêm hai cặp con với chỉ số 2^31 (phái sinh cứng).

> Nếu bạn muốn tìm hiểu thêm về việc phái sinh cặp khóa con trong một ví Bitcoin xác định phân cấp, tôi khuyên bạn nên tham gia CRYPTO301.

### Phương pháp mật mã: Trao đổi khóa Elliptic Curve Diffie-Hellman (ECDH).

Phương pháp mật mã được sử dụng ở trung tâm của BIP47 là ECDH (Elliptic-Curve Diffie-Hellman). Giao thức này là một biến thể của giao thức trao đổi khóa Diffie-Hellman cổ điển.

Diffie-Hellman, trong phiên bản đầu tiên của nó, là một giao thức thỏa thuận khóa được trình bày vào năm 1976 cho phép hai bên, mỗi bên có một cặp khóa công khai và khóa riêng, xác định một bí mật chung bằng cách trao đổi thông tin qua một kênh giao tiếp không an toàn.

![image](assets/11.webp)

Bí mật chung này (khóa màu đỏ) sau đó có thể được sử dụng cho các nhiệm vụ khác. Thông thường, bí mật chung này có thể được sử dụng để mã hóa và giải mã giao tiếp qua một mạng không an toàn:

![image](assets/12.webp)

Để thực hiện trao đổi này, Diffie-Hellman sử dụng số học mô-đun để tính toán bí mật chung. Dưới đây là một giải thích đơn giản về cách nó hoạt động:

- Alice và Bob đồng ý về một màu chung, trong trường hợp này là màu vàng. Màu này được biết đến bởi mọi người. Đó là thông tin công khai.

- Alice chọn một màu bí mật, trong trường hợp này là màu đỏ. Cô ấy trộn hai màu lại, kết quả là màu cam.

- Bob chọn một màu bí mật, trong trường hợp này là màu xanh ngọc. Anh ấy trộn hai màu lại, kết quả là màu xanh da trời.

- Alice và Bob có thể trao đổi các màu họ thu được: màu cam và màu xanh da trời. Sự trao đổi này có thể xảy ra qua một mạng không an toàn và có thể được quan sát bởi kẻ tấn công.

- Alice trộn màu xanh da trời nhận được từ Bob với màu bí mật của mình (màu đỏ). Cô ấy thu được màu nâu.

- Bob trộn màu cam nhận được từ Alice với màu bí mật của mình (màu xanh ngọc). Anh ấy cũng thu được màu nâu.

![image](assets/13.webp)
> z bằng A nâng lên lũy thừa b modulo p:
> z = A^b % p

- Như đã nhắc, A = g^a % p. Do đó:

  > z = A^b % p
  > z = (g^a)^b % p
  >
  > Theo quy tắc của phép lũy thừa:
  >
  > (x^n)^m = x^nm
  >
  > Do đó:
  >
  > z = g^ab % p

Màu nâu trong sự đơn giản hóa này đại diện cho bí mật chia sẻ giữa Alice và Bob. Cần phải tưởng tượng rằng, trong thực tế, không thể tách biệt màu cam và màu xanh da trời để lấy được màu bí mật của Alice hoặc Bob.

Bây giờ, chúng ta hãy nghiên cứu cách thức hoạt động thực tế của nó. Ngay từ cái nhìn đầu tiên, Diffie-Hellman có vẻ phức tạp để nắm bắt. Trên thực tế, nguyên tắc hoạt động gần như trẻ con. Trước khi chi tiết về cơ chế của nó, tôi sẽ nhanh chóng nhắc bạn về hai khái niệm toán học mà chúng ta sẽ cần (và ngẫu nhiên, cũng được sử dụng trong nhiều phương pháp mã hóa khác).

1. Một số nguyên tố là một số tự nhiên chỉ có hai ước số: 1 và chính nó. Ví dụ, số 7 là số nguyên tố vì nó chỉ có thể chia hết cho 1 và 7 (chính nó). Ngược lại, số 8 không phải là số nguyên tố vì nó có thể chia hết cho 1, 2, 4, và 8. Do đó, nó không chỉ có hai ước số, mà có bốn ước số toàn và dương.

2. "Modulo" (được ký hiệu là "mod" hoặc "%") là một phép toán toán học cho phép hai số nguyên trả về phần dư của phép chia Euclid của số thứ nhất cho số thứ hai. Ví dụ, 16 mod 5 bằng 1.

Sự trao đổi khóa Diffie-Hellman giữa Alice và Bob hoạt động như sau:

- Alice và Bob xác định hai số chung: p và g. p là một số nguyên tố. Số p càng lớn, Diffie-Hellman sẽ càng an toàn. g là căn nguyên thủy của p. Hai số này có thể được truyền đạt dưới dạng văn bản rõ ràng qua mạng không an toàn, chúng tương đương với màu vàng trong sự đơn giản hóa ở trên. Alice và Bob chỉ cần có chính xác cùng một giá trị cho p và g.

- Một khi các tham số đã được chọn, Alice và Bob mỗi người xác định một số ngẫu nhiên bí mật của riêng họ. Số ngẫu nhiên do Alice thu được được gọi là a (tương đương với màu đỏ) và số ngẫu nhiên do Bob thu được được gọi là b (tương đương với màu xanh ngọc). Hai số này phải được giữ bí mật.

- Thay vì trao đổi những số này a và b, mỗi bên sẽ tính toán A (viết hoa) và B (viết hoa) sao cho:

> A bằng g nâng lên lũy thừa a modulo p:
> A = g^a % p

> B bằng g nâng lên lũy thừa b modulo p:
> B = g^b % p

- Những số này A (tương đương với màu cam) và B (tương đương với màu xanh da trời) sẽ được trao đổi giữa hai bên. Việc trao đổi có thể được thực hiện dưới dạng văn bản rõ ràng qua mạng không an toàn.

- Alice, người bây giờ biết B, sẽ tính toán giá trị của z sao cho:

> z bằng B nâng lên lũy thừa a modulo p:
> z = B^a % p
z bằng A mũ b modulo p:
> z = A^b % p

Do đó:
> z = (g^a)^b % p
> z = g^ab % p
> z = g^ba % p

Nhờ vào tính phân phối của toán tử modulo, Alice và Bob tìm ra chính xác cùng một giá trị cho z. Con số này đại diện cho bí mật chung của họ, tương đương với màu nâu trong giải thích trước đó. Họ có thể sử dụng bí mật chung này để mã hóa giao tiếp giữa họ trên một mạng không an toàn.

![Sơ đồ Hoạt động Kỹ thuật Diffie-Hellman](assets/14.webp)

Một kẻ tấn công nắm giữ p, g, A, và B sẽ không thể tính toán được a, b, hoặc z. Thực hiện thao tác này đòi hỏi phải đảo ngược phép lũy thừa, điều này không thể thực hiện ngoại trừ việc thử tất cả các khả năng từng cái một vì chúng ta đang làm việc với một trường hữu hạn. Điều này tương đương với việc tính toán logarit rời rạc, là phép nghịch đảo của phép lũy thừa trong một nhóm hữu hạn tuần hoàn.

Do đó, miễn là chúng ta chọn các giá trị đủ lớn cho a, b, và p, Diffie-Hellman là an toàn. Thông thường, với các tham số 2,048 bit (một số có 600 chữ số trong hệ thập phân), việc thử tất cả các khả năng cho a và b sẽ không thực tế. Đến nay, với các số có kích thước này, thuật toán được coi là an toàn.

Đây chính xác là nơi mà nhược điểm chính của giao thức Diffie-Hellman nằm. Để đảm bảo an toàn, thuật toán phải sử dụng các số lớn. Kết quả là, thuật toán ECDH hiện được ưa chuộng hơn, đây là một biến thể của Diffie-Hellman sử dụng một đường cong đại số, cụ thể là một đường cong elliptic. Điều này cho phép chúng ta làm việc với các số nhỏ hơn nhiều trong khi vẫn duy trì an ninh tương đương, do đó giảm bớt tài nguyên tính toán và lưu trữ cần thiết.

Nguyên tắc chung của thuật toán vẫn giữ nguyên. Tuy nhiên, thay vì sử dụng một số ngẫu nhiên a và một số A được tính từ a bằng phép lũy thừa modulo, chúng ta sẽ sử dụng một cặp khóa được thiết lập trên một đường cong elliptic. Thay vì dựa vào tính phân phối của toán tử modulo, chúng ta sẽ sử dụng luật nhóm trên các đường cong elliptic, cụ thể là tính kết hợp của luật này.
Nếu bạn không biết cách hoạt động của khóa riêng và khóa công khai trên một đường cong elliptic, tôi sẽ giải thích cơ bản của phương pháp này trong sáu phần đầu của bài viết này.

Tóm lại, một khóa riêng là một số ngẫu nhiên từ 1 đến n-1 (nơi n là thứ tự của đường cong), và một khóa công khai là một điểm duy nhất trên đường cong được xác định bởi khóa riêng thông qua phép cộng điểm và nhân đôi từ điểm sinh, như sau:

> K = k·G

Nơi K là khóa công khai, k là khóa riêng, và G là điểm sinh.

Một trong những tính chất của cặp khóa này là rất dễ dàng để xác định K nếu bạn biết k và G, nhưng hiện nay không thể xác định k nếu bạn biết K và G. Đó là một hàm một chiều.

Nói cách khác, bạn có thể dễ dàng tính toán khóa công khai nếu bạn biết khóa riêng, nhưng không thể tính toán khóa riêng nếu bạn biết khóa công khai. Sự an toàn này một lần nữa dựa trên sự không thể tính toán được của logarit rời rạc.

Chúng ta sẽ sử dụng tính chất này để điều chỉnh thuật toán Diffie-Hellman của mình. Do đó, nguyên tắc hoạt động của ECDH như sau:

- Alice và Bob thỏa thuận về một đường cong elliptic an toàn về mặt mật mã và các tham số của nó. Thông tin này là công khai.
- Alice tạo ra một số ngẫu nhiên ka, đó sẽ là khóa riêng của cô ấy. Khóa riêng này phải được giữ bí mật. Cô ấy xác định khóa công khai Ka của mình bằng cách cộng và nhân đôi các điểm trên đường cong elliptic đã chọn.
> Ka = ka·G

- Bob cũng tạo ra một số ngẫu nhiên kb, đó sẽ là khóa riêng của anh ấy. Anh ấy tính toán khóa công khai Kb tương ứng.
> Kb = kb·G

- Alice và Bob trao đổi khóa công khai Ka và Kb của họ qua một mạng công cộng không an toàn.

- Alice tính toán một điểm (x, y) trên đường cong bằng cách áp dụng khóa riêng ka của mình vào khóa công khai Kb của Bob.
> (x, y) = ka·Kb

- Bob tính toán một điểm (x, y) trên đường cong bằng cách áp dụng khóa riêng kb của mình vào khóa công khai Ka của Alice.
> (x, y) = kb·Ka

- Alice và Bob thu được cùng một điểm trên đường cong elliptic. Bí mật chung sẽ là tọa độ x của điểm này.

Họ thu được cùng một bí mật chung bởi vì:
> (x, y) = ka·Kb = ka·kb·G = kb·ka·G = kb·Ka

Một kẻ tấn công tiềm năng quan sát mạng công cộng không an toàn chỉ có thể thu được khóa công khai của mỗi bên và các tham số đường cong đã chọn. Như đã giải thích trước đó, chỉ hai thông tin này không đủ để xác định khóa riêng, vì vậy kẻ tấn công không thể truy cập vào bí mật.

ECDH là một thuật toán cho phép trao đổi khóa. Nó thường được sử dụng cùng với các phương pháp mã hóa khác để định nghĩa một giao thức. Ví dụ, ECDH được sử dụng trong cốt lõi của TLS (Transport Layer Security), một giao thức mã hóa và xác thực được sử dụng cho tầng vận chuyển internet. TLS sử dụng ECDHE cho việc trao đổi khóa, một biến thể của ECDH nơi mà các khóa là tạm thời để cung cấp tính bảo mật liên tục. Ngoài ECDHE, TLS cũng sử dụng một thuật toán xác thực như ECDSA, một thuật toán mã hóa như AES, và một hàm băm như SHA256.

TLS định nghĩa "s" trong "https" và biểu tượng khóa nhỏ bạn thấy trên trình duyệt internet ở góc trên bên trái, đảm bảo giao tiếp được mã hóa. Vì vậy, bạn đang sử dụng ECDH khi đọc bài viết này, và có lẽ bạn sử dụng nó hàng ngày mà không nhận ra.

### Giao dịch thông báo.

Như chúng ta đã khám phá trong phần trước, ECDH là một biến thể của trao đổi Diffie-Hellman liên quan đến các cặp khóa được thiết lập trên một đường cong elliptic. May mắn thay, chúng ta có rất nhiều cặp khóa đáp ứng tiêu chuẩn này trong ví Bitcoin của chúng ta!

Ý tưởng là sử dụng các cặp khóa từ ví Bitcoin phân cấp xác định của cả hai bên để thiết lập bí mật chung và tạm thời giữa họ. Trong BIP47, ECDHE (Elliptic Curve Diffie-Hellman Ephemeral) được sử dụng thay thế.

ECDHE được sử dụng ban đầu trong BIP47 để truyền mã thanh toán của người gửi cho người nhận. Đây là giao dịch thông báo nổi tiếng. Để BIP47 được sử dụng, cả hai bên (người gửi thanh toán và người nhận thanh toán) cần phải biết mã thanh toán của nhau. Điều này cần thiết để suy ra các khóa công khai tạm thời và do đó là các địa chỉ nhận dành riêng.
Trước khi thực hiện giao dịch này, người gửi lô-gíc đã biết mã thanh toán của người nhận vì họ có thể đã lấy được nó thông qua các kênh ngoại tuyến, ví dụ như từ website hoặc mạng xã hội của họ. Tuy nhiên, người nhận có thể chưa chắc đã biết mã thanh toán của người gửi. Mã này cần được truyền đến họ, nếu không họ sẽ không thể tạo ra các khóa tạm thời và do đó sẽ không biết bitcoins của họ ở đâu và không thể mở khóa quỹ của mình. Việc truyền đạt này có thể được thực hiện thông qua một hệ thống giao tiếp ngoại tuyến khác, nhưng điều này sẽ gặp vấn đề nếu ví được khôi phục từ seed. Thực sự, như tôi đã đề cập, địa chỉ BIP47 không được tạo ra từ seed của người nhận (nếu không, sẽ tốt hơn là sử dụng một trong những xpubs của họ trực tiếp), mà là kết quả của một phép tính liên quan đến cả mã thanh toán của người nhận và mã thanh toán của người gửi. Do đó, nếu người nhận mất ví và cố gắng khôi phục nó từ seed của họ, họ sẽ cần phải có tất cả mã thanh toán của những người đã gửi bitcoins cho họ qua BIP47.

Việc sử dụng BIP47 mà không cần giao dịch thông báo sẽ có thể thực hiện được, nhưng mỗi người dùng sẽ cần phải sao lưu mã thanh toán của các đối tác của họ. Tình hình này sẽ không thể quản lý được cho đến khi tìm ra một cách đơn giản và bền vững để tạo, lưu trữ và cập nhật các bản sao lưu này. Do đó, giao dịch thông báo gần như là bắt buộc trong tình hình hiện tại.

Ngoài vai trò sao lưu mã thanh toán, như tên gọi của nó, giao dịch này còn có chức năng thông báo cho người nhận. Nó thông báo cho ứng dụng của họ biết rằng một đường hầm vừa được mở.

Trước khi giải thích chi tiết hơn về cách thức kỹ thuật của giao dịch thông báo, tôi muốn nói một chút về mô hình bảo mật. Thực sự, mô hình bảo mật của BIP47 biện minh cho một số biện pháp phòng ngừa được thực hiện khi xây dựng giao dịch ban đầu này.

Mã thanh toán bản thân nó không trực tiếp gây rủi ro cho quyền riêng tư. Khác với mô hình Bitcoin cổ điển, cho phép ngắt dòng thông tin giữa danh tính người dùng và các giao dịch, đặc biệt là bằng cách giữ ẩn danh các khóa công khai, mã thanh toán có thể được liên kết trực tiếp với một danh tính. Điều này không bắt buộc, nhưng liên kết này không nguy hiểm.

Thực sự, mã thanh toán không trực tiếp tạo ra các địa chỉ được sử dụng để nhận thanh toán BIP47. Thay vào đó, các địa chỉ được thu được bằng cách áp dụng ECDHE giữa các khóa con của mã thanh toán của cả hai bên.

Do đó, một mã thanh toán một mình không trực tiếp gây rủi ro cho quyền riêng tư vì chỉ có địa chỉ thông báo được tạo ra từ nó. Một số thông tin có thể được suy luận từ nó, nhưng bình thường người ta không thể biết bạn đang giao dịch với ai.

Vì vậy, việc duy trì sự tách biệt nghiêm ngặt giữa mã thanh toán của người dùng là cực kỳ quan trọng. Về mặt này, bước giao tiếp ban đầu của mã là một thời điểm quan trọng cho quyền riêng tư thanh toán, và vẫn là bắt buộc cho sự hoạt động đúng đắn của giao thức. Nếu một trong các mã thanh toán có thể được truy cập công khai (ví dụ, từ một website), mã thứ hai, tức là mã của người gửi, không nên được liên kết với mã đầu tiên.

Ví dụ, hãy tưởng tượng rằng tôi muốn thực hiện một khoản quyên góp bằng BIP47 cho một phong trào biểu tình hòa bình ở Canada:

- Tổ chức này đã công bố mã thanh toán của mình trực tiếp trên website hoặc các nền tảng mạng xã hội của họ.
- Mã này do đó được liên kết với phong trào.

- Tôi lấy được mã thanh toán này.

- Trước khi tôi có thể gửi cho họ một giao dịch, tôi phải đảm bảo rằng họ biết mã thanh toán cá nhân của tôi, cũng được liên kết với danh tính của tôi vì tôi sử dụng nó để nhận giao dịch từ mạng xã hội của mình.

Làm thế nào tôi có thể truyền đạt nó cho họ? Nếu tôi gửi nó cho họ bằng một phương tiện giao tiếp thông thường, thông tin có thể bị rò rỉ, và tôi có thể được xác định là một người ủng hộ các phong trào hòa bình.
Giao dịch thông báo chắc chắn không phải là giải pháp duy nhất để truyền đạt mã thanh toán của người gửi một cách bí mật, nhưng hiện tại nó hoàn thành vai trò này một cách hoàn hảo bằng cách áp dụng nhiều lớp bảo mật.

Trong sơ đồ dưới đây, các đường màu đỏ đại diện cho thời điểm khi dòng thông tin cần được ngắt kết nối, và các mũi tên màu đen đại diện cho các liên kết không thể chối cãi mà một quan sát viên bên ngoài có thể tạo ra:

![Mô hình bảo mật cho mã thanh toán tái sử dụng](assets/15.webp)

Trong thực tế, đối với mô hình bảo mật cổ điển của Bitcoin, thường khó để hoàn toàn ngắt kết nối dòng thông tin giữa cặp khóa và người dùng, đặc biệt là khi thực hiện giao dịch từ xa. Ví dụ, trong trường hợp của một chiến dịch quyên góp, người nhận sẽ được yêu cầu tiết lộ một địa chỉ hoặc khóa công khai trên trang web hoặc nền tảng truyền thông xã hội của họ. Việc sử dụng đúng BIP47, tức là, với giao dịch thông báo, giải quyết vấn đề này thông qua ECDHE và lớp mã hóa mà chúng ta sẽ nghiên cứu.

Rõ ràng, mô hình bảo mật cổ điển của Bitcoin vẫn được quan sát ở cấp độ của các khóa công khai tạm thời được tạo ra từ sự kết hợp của hai mã thanh toán. Hai mô hình là tương phụ thuộc. Tôi chỉ muốn nhấn mạnh ở đây rằng, không giống như việc sử dụng cổ điển một khóa công khai để nhận bitcoin, mã thanh toán có thể được liên kết với một danh tính vì thông tin "Bob đang thực hiện giao dịch với Alice" được ngắt kết nối tại một thời điểm khác. Mã thanh toán được sử dụng để tạo địa chỉ thanh toán, nhưng chỉ bằng cách quan sát blockchain, không thể liên kết một giao dịch thanh toán BIP47 với các mã thanh toán được sử dụng để thực hiện nó.

### Xây dựng giao dịch thông báo.

Bây giờ, hãy xem giao dịch thông báo này hoạt động như thế nào. Hãy tưởng tượng rằng Alice muốn gửi tiền cho Bob sử dụng BIP47. Trong ví dụ của tôi, Alice đóng vai trò là người gửi và Bob là người nhận. Bob đã công bố mã thanh toán của mình trên trang web của mình, vì vậy Alice đã biết mã thanh toán của Bob.

1. Alice tính toán một bí mật chung với ECDH:

- Cô ấy chọn một cặp khóa từ ví HD của mình nằm trên một nhánh khác so với mã thanh toán của mình. Lưu ý rằng cặp này không nên dễ dàng liên kết với địa chỉ thông báo của Alice hoặc danh tính của Alice (xem phần trước).
- Alice chọn khóa riêng từ cặp này. Chúng ta sẽ gọi nó là "a" (chữ thường).

> a

- Alice lấy khóa công khai liên kết với địa chỉ thông báo của Bob. Khóa này là con đầu tiên được tạo ra từ mã thanh toán của Bob (chỉ số 0). Chúng ta sẽ gọi khóa công khai này là "B" (chữ hoa). Khóa riêng liên kết với khóa công khai này được gọi là "b" (chữ thường). "B" được xác định bằng cách cộng và nhân đôi điểm trên đường cong elliptic từ "G" (điểm sinh) với "b" (khóa riêng).

> B = b·G

- Alice tính toán một điểm bí mật "S" (chữ hoa) trên đường cong elliptic bằng cách cộng và nhân đôi điểm, áp dụng khóa riêng "a" của mình vào khóa công khai "B" của Bob.

> S = a·B

- Alice tính toán yếu tố làm mờ "f" sẽ được sử dụng để mã hóa mã thanh toán của mình. Để làm điều này, cô ấy sẽ tạo ra một số ngẫu nhiên giả mạo bằng cách sử dụng hàm HMAC-SHA512. Là đầu vào thứ hai cho hàm này, cô ấy sử dụng một giá trị mà chỉ Bob mới có thể truy xuất: (x), là tọa độ x của điểm bí mật đã được tính toán trước đó. Đầu vào đầu tiên là (o), là UTXO được tiêu thụ như một đầu vào cho giao dịch này (outpoint).

> f = HMAC-SHA512(o, x)

2. Alice chuyển đổi mã thanh toán cá nhân của mình thành cơ số 2 (nhị phân).
3. Cô ấy sử dụng yếu tố làm mờ này như một chìa khóa để thực hiện mã hóa đối xứng trên phần tải của mã thanh toán của mình. Thuật toán mã hóa được sử dụng đơn giản là XOR. Thao tác thực hiện tương tự như mật mã Vernam, còn được biết đến là "mật mã một lần" (one-time pad):
- Alice đầu tiên chia yếu tố làm mờ của mình thành hai phần: 32 byte đầu tiên được gọi là "f1" và 32 byte cuối cùng được gọi là "f2". Vậy chúng ta có:

> f = f1 || f2

- Alice tính toán bản mã (x') của tọa độ x của khóa công khai (x) của mã thanh toán của mình, và riêng biệt tính toán bản mã (c') của mã chuỗi (c) của mình. "f1" và "f2" đóng vai trò như các khóa mã hóa, và thao tác XOR được sử dụng.

> x' = x XOR f1
>
> c' = c XOR f2

- Alice thay thế các giá trị thực của tọa độ abscissa của khóa công khai (x) và mã chuỗi (c) trong mã thanh toán của mình bằng các giá trị đã mã hóa (x') và (c').

Trước khi tiếp tục với mô tả kỹ thuật của giao dịch thông báo này, hãy dành một chút thời gian để thảo luận về thao tác XOR. XOR là một toán tử logic theo bit dựa trên đại số Boolean. Cho hai toán hạng bit, nó trả về 1 nếu các bit tương ứng khác nhau, và trả về 0 nếu các bit tương ứng bằng nhau. Dưới đây là bảng chân lý cho XOR dựa trên giá trị của các toán hạng D và E:

| D   | E   | D XOR E |
| --- | --- | ------- |
| 0   | 0   | 0       |
| 0   | 1   | 1       |
| 1   | 0   | 1       |
| 1   | 1   | 0       |

Ví dụ:

> 0110 XOR 1110 = 1000

Hoặc:

> 010011 XOR 110110 = 100101

Với ECDH, việc sử dụng XOR như một lớp mã hóa là đặc biệt phù hợp. Đầu tiên, nhờ vào toán tử này, mã hóa là đối xứng. Điều này cho phép người nhận giải mã mã thanh toán bằng cùng một khóa được sử dụng để mã hóa. Khóa mã hóa và giải mã được tính toán từ bí mật chung sử dụng ECDH.

Tính đối xứng này được kích hoạt bởi các tính chất giao hoán và kết hợp của toán tử XOR:

- Các tính chất khác:
  -> D ⊕ D = 0
  -> D ⊕ 0 = D

- Giao hoán:
  D ⊕ E = E ⊕ D

- Kết hợp:
  D ⊕ (E ⊕ Z) = (D ⊕ E) ⊕ Z = D ⊕ E ⊕ Z

- Đối xứng:
  Nếu: D ⊕ E = L
  Thì: D ⊕ L = D ⊕ (D ⊕ E) = D ⊕ D ⊕ E = 0 ⊕ E = E
  -> D ⊕ L = E
Tiếp theo, phương pháp mã hóa này rất giống với mã Vernam (One-Time Pad), là thuật toán mã hóa duy nhất được biết đến cho đến nay có độ an toàn tuyệt đối (hoặc tuyệt đối). Để mã Vernam có được đặc tính này, khóa mã hóa phải hoàn toàn ngẫu nhiên, có kích thước bằng với thông điệp, và chỉ được sử dụng một lần. Trong phương pháp mã hóa được sử dụng ở đây cho BIP47, khóa thực sự có kích thước bằng với thông điệp, yếu tố làm mờ chính xác bằng kích thước của sự kết hợp giữa tọa độ x của khóa công khai với mã chuỗi thanh toán. Khóa mã hóa này thực sự chỉ được sử dụng một lần. Tuy nhiên, khóa này không được tạo ra từ một nguồn ngẫu nhiên hoàn hảo vì nó là một HMAC. Nó khá giả ngẫu nhiên. Do đó, đây không phải là mã Vernam, nhưng phương pháp này tương tự.

Hãy quay lại với việc xây dựng giao dịch thông báo của chúng ta:

4. Hiện tại Alice có mã thanh toán của mình với một payload được mã hóa. Cô ấy sẽ xây dựng và phát sóng một giao dịch liên quan đến khóa công khai "A" của mình như đầu vào, một đầu ra đến địa chỉ thông báo của Bob, và một đầu ra OP_RETURN bao gồm mã thanh toán của cô ấy với payload được mã hóa. Giao dịch này là giao dịch thông báo.

OP_RETURN là một Opcode, là một script đánh dấu một đầu ra giao dịch Bitcoin như không hợp lệ. Ngày nay, nó được sử dụng để phát sóng hoặc neo thông tin trên blockchain Bitcoin. Nó có thể lưu trữ tới 80 byte dữ liệu được ghi lại trên chuỗi và do đó có thể nhìn thấy bởi tất cả người dùng khác.

Như chúng ta đã thấy trong phần trước, Diffie-Hellman được sử dụng để tạo ra một bí mật chung giữa hai người dùng giao tiếp qua mạng không an toàn, có thể được quan sát bởi kẻ tấn công. Trong BIP47, ECDH được sử dụng để giao tiếp trên mạng Bitcoin, bản chất là một mạng giao tiếp minh bạch được nhiều kẻ tấn công quan sát. Bí mật chung được tính toán thông qua trao đổi khóa Diffie-Hellman trên đường cong elliptic sau đó được sử dụng để mã hóa thông tin bí mật cần truyền đạt: mã thanh toán của người gửi (Alice).

Dưới đây là một sơ đồ được trích từ BIP47 mô tả những gì chúng ta vừa mô tả:

![Sơ đồ Alice gửi mã thanh toán được che giấu của mình đến địa chỉ thông báo của Bob](assets/16.webp)

Credit: Reusable Payment Codes for Hierarchical Deterministic Wallets, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Nếu chúng ta so sánh sơ đồ này với những gì tôi đã mô tả trước đó:

- "Wallet Priv-Key" phía Alice tương ứng với: a.

- "Child Pub-Key 0" phía Bob tương ứng với: B.
- "Notification Shared Secret" tương ứng với: f.
- "Masked Payment Code" tương ứng với mã thanh toán được mã hóa, tức là, với payload được mã hóa: x' và c'.

- "Notification Transaction" là giao dịch chứa OP_RETURN.

Hãy tóm tắt lại các bước chúng ta vừa trải qua để thực hiện một giao dịch thông báo:

- Alice lấy mã thanh toán và địa chỉ thông báo của Bob.

- Alice chọn một UTXO thuộc về mình trong ví HD của mình với cặp khóa tương ứng.

- Cô ấy tính toán một điểm bí mật trên đường cong elliptic sử dụng ECDH.

- Cô ấy sử dụng điểm bí mật này để tính toán một HMAC, đó là yếu tố làm mờ.

- Cô ấy sử dụng yếu tố làm mờ này để mã hóa payload của mã thanh toán cá nhân của mình.

- Cô ấy sử dụng một đầu ra giao dịch OP_RETURN để chuyển mã thanh toán được che giấu đến Bob.

Để hiểu rõ hơn về hoạt động của nó, đặc biệt là việc sử dụng OP_RETURN, hãy cùng nghiên cứu một giao dịch thông báo thực tế. Tôi đã thực hiện một giao dịch loại này trên Testnet, bạn có thể tìm thấy bằng cách nhấp vào đây:
Quan sát giao dịch này, chúng ta có thể thấy rằng nó chỉ có một đầu vào và 4 đầu ra:

- Đầu ra đầu tiên là OP_RETURN chứa mã thanh toán bị che của tôi.

- Đầu ra thứ hai là 546 sats chỉ đến địa chỉ thông báo của người nhận.

- Đầu ra thứ ba là 15,000 sats đại diện cho phí dịch vụ, vì tôi đã sử dụng Ví Samourai để tạo giao dịch này.

- Đầu ra thứ tư là hai triệu sats đại diện cho số tiền thừa, tức là sự chênh lệch còn lại từ đầu vào của tôi quay trở lại một địa chỉ khác thuộc về tôi.

Thú vị nhất để nghiên cứu rõ ràng là đầu ra số 0 sử dụng OP_RETURN. Hãy xem xét kỹ lưỡng nó chứa gì:

Chúng ta khám phá mã lệnh hex của đầu ra:

> 6a4c50010002b13b2911719409d704ecc69f74fa315a6cb20fdd6ee39bc9874667703d67b164927b0e88f89f3f8b963549eab2533b5d7ed481a3bea7e953b546b4e91b6f50d800000000000000000000000000

Trong mã lệnh này, chúng ta có thể phân tích ra một số phần:
Trong các opcode, chúng ta có thể nhận ra 0x6a đề cập đến OP_RETURN và 0x4c đề cập đến OP_PUSHDATA1. Byte tiếp theo sau opcode này chỉ ra kích thước của payload theo sau. Nó chỉ ra 0x50, tức là 80 byte.

Tiếp theo là mã thanh toán với payload được mã hóa.

Dưới đây là mã thanh toán của tôi được sử dụng trong giao dịch này:

> Trong base 58:
>
> PM8TJQCyt6ovbozreUCBrfKqmSVmTzJ5vjqse58LnBzKFFZTwny3KfCDdwTqAEYVasn11tTMPc2FJsFygFd3YzsHvwNXLEQNADgxeGnMK8Ugmin62TZU
>
> Trong base 16 (HEX):
> 4701000277507c9c17a89cfca2d3af554745d6c2db0e7f6b2721a3941a504933103cc42add94881210d6e752a9abc8a9fa0070e85184993c4f643f1121dd807dd556d1dc000000000000000000000000008604e4db

Nếu chúng ta so sánh mã thanh toán của tôi với OP_RETURN, chúng ta có thể thấy rằng HRP (màu nâu) và checksum (màu hồng) không được truyền đi. Điều này là bình thường, vì thông tin này dành cho con người.
Tiếp theo, chúng ta có thể nhận biết (màu xanh) phiên bản (0x01), trường bit (0x00), và tính chẵn lẻ của khóa công khai (0x02). Và, ở cuối mã thanh toán, các byte trống màu đen (0x00) cho phép thêm vào để đạt tổng cộng 80 byte. Tất cả metadata này được truyền đi không mã hóa (plaintext). Cuối cùng, chúng ta có thể thấy rằng tọa độ x của khóa công khai (màu xanh dương) và mã chuỗi (màu đỏ) đã được mã hóa. Điều này tạo thành phần dữ liệu (payload) của mã thanh toán.

### Nhận giao dịch thông báo.

Bây giờ Alice đã gửi giao dịch thông báo cho Bob, hãy xem anh ấy giải mã nó như thế nào.

Nhắc lại, Bob phải có khả năng truy cập vào mã thanh toán của Alice. Không có thông tin này, như chúng ta sẽ thấy trong phần tiếp theo, anh ấy sẽ không thể suy ra các cặp khóa được tạo bởi Alice, và do đó, anh ấy sẽ không thể truy cập vào bitcoin của mình nhận được với BIP47. Hiện tại, payload mã thanh toán của Alice được mã hóa. Hãy cùng xem Bob giải mã nó như thế nào.

1. Bob theo dõi các giao dịch tạo ra outputs với địa chỉ thông báo của mình.

2. Khi một giao dịch có output đến địa chỉ thông báo của mình, Bob phân tích nó để xem nó có chứa output OP_RETURN tuân thủ tiêu chuẩn BIP47 không.

3. Nếu byte đầu tiên của payload OP_RETURN là 0x01, Bob bắt đầu tìm kiếm một bí mật chia sẻ có thể có với ECDH:

- Bob chọn khóa công khai trong input của giao dịch. Đó là, khóa công khai của Alice được gọi là "A" với:

> A = a·G

- Bob chọn khóa riêng "b" liên kết với địa chỉ thông báo cá nhân của mình:

> b

- Bob tính điểm bí mật "S" (bí mật chia sẻ ECDH) trên đường cong elliptic bằng cách cộng và nhân đôi các điểm, áp dụng khóa riêng "b" của mình vào khóa công khai "A" của Alice:

> S = b·A

- Bob xác định yếu tố làm mờ "f" sẽ cho phép anh ấy giải mã payload mã thanh toán của Alice. Cũng như Alice đã tính trước đó, Bob sẽ tìm "f" bằng cách áp dụng HMAC-SHA512 vào (x) giá trị tọa độ x của điểm bí mật "S", và vào (o) UTXO được tiêu thụ như input trong giao dịch thông báo này:

> f = HMAC-SHA512(o, x)

4. Bob giải mã dữ liệu trong OP_RETURN của giao dịch thông báo như một mã thanh toán. Anh ấy đơn giản giải mã payload của mã thanh toán tiềm năng này sử dụng yếu tố làm mờ "f".

- Bob chia yếu tố làm mờ "f" thành hai phần: 32 byte đầu tiên của "f" sẽ là "f1" và 32 byte cuối cùng sẽ là "f2".
- Bob giải mã giá trị tọa độ x đã mã hóa (x') của khóa công khai mã thanh toán của Alice:

> x = x' XOR f1

- Bob giải mã giá trị mã chuỗi đã mã hóa (c') của mã thanh toán của Alice:

> c = c' XOR f2

5. Bob kiểm tra xem giá trị của khóa công khai mã thanh toán của Alice có thuộc nhóm secp256k1 không. Nếu có, anh ấy giải thích nó như một mã thanh toán hợp lệ. Nếu không, anh ấy bỏ qua giao dịch.

Bây giờ Bob biết mã thanh toán của Alice, cô ấy có thể gửi cho anh ấy tới 2^32 khoản thanh toán mà không bao giờ cần thực hiện giao dịch thông báo như thế này nữa.

Tại sao điều này lại hoạt động? Làm thế nào Bob có thể xác định cùng một yếu tố làm mờ như Alice và giải mã mã thanh toán của cô ấy? Hãy xem xét quy trình ECDH một cách chi tiết hơn dựa trên những gì chúng ta vừa mô tả.
Trước hết, chúng ta đang xử lý với mã hóa đối xứng. Điều này có nghĩa là khóa mã hóa và khóa giải mã có cùng một giá trị. Trong trường hợp này, khóa trong giao dịch thông báo là yếu tố làm mờ (f = f1 || f2). Alice và Bob cần phải có được cùng một giá trị cho f mà không truyền trực tiếp nó, vì một kẻ tấn công có thể chặn nó và giải mã thông tin bí mật.

Yếu tố làm mờ này được thu được bằng cách áp dụng HMAC-SHA512 lên hai giá trị: tọa độ x của một điểm bí mật và UTXO đã sử dụng trong đầu vào giao dịch. Do đó, Bob cần phải có hai thông tin này để giải mã mã thanh toán của Alice.

Đối với UTXO đầu vào, Bob có thể đơn giản lấy nó bằng cách quan sát giao dịch thông báo. Đối với điểm bí mật, Bob sẽ phải sử dụng ECDH.

Như đã thấy trong phần về Diffie-Hellman, bằng cách trao đổi các khóa công khai tương ứng và bí mật áp dụng khóa riêng của họ vào khóa công khai của người kia, Alice và Bob có thể tìm ra một điểm cụ thể và bí mật trên đường cong elliptic. Giao dịch thông báo dựa vào cơ chế này:

> Cặp khóa của Bob:
>
> B = b·G
>
> Cặp khóa của Alice:
>
> A = a·G
>
> Đối với một điểm bí mật S (x,y):
>
> S = a·B = a·b·G = b·a·G = b·A

![Sơ đồ tạo ra một bí mật chung với ECDHE](assets/19.webp)
Bây giờ Bob biết mã thanh toán của Alice, anh ấy sẽ có thể phát hiện các khoản thanh toán BIP47 của cô ấy và suy ra các khóa riêng để mở khóa các bitcoin nhận được.
![Bob giải mã giao dịch thông báo của Alice](assets/20.webp)

Tín dụng: Mã Thanh Toán Có Thể Sử Dụng Lại cho Ví Phân Cấp Xác Định, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Nếu chúng ta so sánh sơ đồ này với những gì tôi đã mô tả cho bạn trước đó:

- "Wallet Pub-Key" ở phía Alice tương ứng với: A.

- "Child Priv-Key 0" ở phía Bob tương ứng với: b.

- "Notification Shared Secret" tương ứng với: f.

- "Masked Payment Code" tương ứng với mã thanh toán được che của Alice, tức là, với payload được mã hóa: x' và c'.

- "Notification Transaction" là giao dịch chứa OP_RETURN.

Hãy tôi tóm tắt lại các bước mà chúng ta vừa xem cùng nhau để nhận và giải mã một giao dịch thông báo:

- Bob theo dõi các đầu ra giao dịch đến địa chỉ thông báo của mình.

- Khi anh ấy phát hiện một cái, anh ấy lấy thông tin chứa trong OP_RETURN.

- Bob chọn khóa công khai đầu vào và tính toán một điểm bí mật sử dụng ECDH.

- Anh ấy sử dụng điểm bí mật này để tính toán một HMAC, đó là yếu tố làm mờ.

- Anh ấy sử dụng yếu tố làm mờ này để giải mã payload mã thanh toán của Alice chứa trong OP_RETURN.

### Giao dịch thanh toán BIP47.

Bây giờ chúng ta hãy nghiên cứu quy trình thanh toán với BIP47. Để nhắc bạn về tình hình hiện tại:

- Alice biết mã thanh toán của Bob, mà cô ấy đơn giản lấy từ website của anh ấy.

- Bob biết mã thanh toán của Alice nhờ giao dịch thông báo.

- Alice sẽ thực hiện một khoản thanh toán ban đầu cho Bob. Cô ấy có thể thực hiện nhiều khoản thanh toán hơn theo cùng một cách.

Trước khi giải thích quy trình này cho bạn, tôi nghĩ là quan trọng phải nhắc bạn về các chỉ số mà chúng ta đang làm việc:

Chúng ta mô tả đường dẫn phái sinh của một mã thanh toán như sau: m/47'/0'/0'/.

Các độ sâu tiếp theo phân phối các chỉ số như sau:
- Cặp con đầu tiên bình thường (không cứng) được sử dụng để tạo ra địa chỉ thông báo mà chúng ta đã thảo luận trong phần trước: m/47'/0'/0'/0/.
- Các cặp khóa con bình thường được sử dụng trong ECDH để tạo ra địa chỉ nhận thanh toán BIP47, như chúng ta sẽ thấy trong phần này: m/47'/0'/0'/ từ 0 đến 2,147,483,647/.

- Các cặp khóa con cứng là mã thanh toán tạm thời: m/47'/0'/0'/ từ 0' đến 2,147,483,647'/.
  Mỗi khi Alice muốn gửi thanh toán cho Bob, cô ấy tạo ra một địa chỉ trống duy nhất mới, một lần nữa nhờ vào giao thức ECDH:
- Alice chọn khóa riêng đầu tiên được tạo ra từ mã thanh toán cá nhân có thể tái sử dụng của mình:

> a

- Alice chọn khóa công khai chưa sử dụng đầu tiên được tạo ra từ mã thanh toán của Bob. Khóa công khai này, chúng ta sẽ gọi là "B". Nó được liên kết với khóa riêng "b" mà chỉ Bob biết.

> B = b·G

- Alice tính toán một điểm bí mật "S" trên đường cong elliptic bằng cách cộng và nhân đôi các điểm, áp dụng khóa riêng "a" của mình vào khóa công khai "B" của Bob:

> S = a·B

- Từ điểm bí mật này, Alice sẽ tính toán bí mật chung "s" (chữ thường). Để làm điều này, cô ấy chọn tọa độ x của điểm bí mật "S" được gọi là "Sx", và cô ấy đưa giá trị này vào hàm băm SHA256.

> s = SHA256(Sx)

Đừng tin. Hãy kiểm chứng! Nếu bạn muốn hiểu các nguyên tắc cơ bản của một hàm băm, bạn sẽ tìm thấy những gì bạn cần trong bài viết này. Và nếu bạn không tin tưởng NIST (bạn đúng), và bạn muốn có thể hiểu chi tiết cách SHA256 hoạt động, tôi giải thích mọi thứ trong bài viết này bằng tiếng Pháp.

- Alice sử dụng bí mật chung "s" này để tính toán địa chỉ nhận thanh toán Bitcoin. Đầu tiên, cô ấy kiểm tra xem "s" có nằm trong thứ tự của đường cong secp256k1 hay không. Nếu không, cô ấy tăng chỉ số của khóa công khai của Bob để tạo ra một bí mật chung khác.

- Thứ hai, cô ấy tính toán một khóa công khai "K0" bằng cách cộng các điểm "B" và "s·G" trên đường cong elliptic. Nói cách khác, Alice cộng khóa công khai được tạo ra từ mã thanh toán của Bob "B" với một điểm khác được tính toán trên đường cong elliptic bằng cách cộng và nhân đôi các điểm với bí mật chung "s" từ điểm sinh của đường cong secp256k1 "G". Điểm mới này đại diện cho một khóa công khai, và chúng ta gọi nó là "K0":

> K0 = B + s·G

- Với khóa công khai "K0" này, Alice có thể tạo ra một địa chỉ nhận trống theo cách tiêu chuẩn (ví dụ, SegWit V0 trong Bech32).

Một khi Alice có địa chỉ nhận "K0" thuộc về Bob, cô ấy có thể xây dựng một giao dịch Bitcoin tiêu chuẩn bằng cách chọn một UTXO thuộc về mình trên một nhánh khác của ví HD của mình, và chi tiêu nó cho địa chỉ "K0" của Bob.

![Alice gửi bitcoins với BIP47 cho Bob](assets/21.webp)

Tín dụng: Mã Thanh Toán Có Thể Tái Sử Dụng cho Ví Phân Cấp Xác Định, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki
Nếu chúng ta so sánh sơ đồ này với những gì tôi đã mô tả cho bạn trước đó:

- "Child Priv-Key" ở phía Alice tương ứng với: a.
- "Child Pub-Key 0" ở phía Bob tương ứng với: B.
- "Payment Secret 0" tương ứng với: s.
- "Payment Pub-Key 0" tương ứng với: K0.
Hãy cùng tóm tắt các bước chúng ta vừa trải qua để thực hiện một giao dịch BIP47:

- Alice chọn khóa riêng con đầu tiên được sinh ra từ mã thanh toán cá nhân của cô ấy.
- Cô ấy tính toán một điểm bí mật trên đường cong elliptic sử dụng ECDH từ khóa công khai con chưa được sử dụng đầu tiên từ mã thanh toán của Bob.
- Cô ấy sử dụng điểm bí mật này để tính toán một bí mật chung với SHA256.
- Cô ấy sử dụng bí mật chung này để tính toán một điểm bí mật mới trên đường cong elliptic.
- Cô ấy cộng điểm bí mật mới này vào khóa công khai của Bob.
- Cô ấy nhận được một khóa công khai tạm thời mới mà chỉ Bob có khóa riêng tương ứng.
- Alice có thể gửi một giao dịch thông thường cho Bob với địa chỉ nhận tạm thời được sinh ra.

Nếu cô ấy muốn thực hiện một khoản thanh toán thứ hai, cô ấy sẽ lặp lại các bước trên, ngoại trừ việc cô ấy sẽ chọn khóa công khai con thứ hai từ mã thanh toán của Bob. Đó là, khóa tiếp theo chưa được sử dụng. Cô ấy sau đó sẽ có một địa chỉ nhận thứ hai thuộc về Bob, "K1".

![Alice sinh ra ba địa chỉ nhận BIP47 cho Bob](assets/22.webp)

Tín dụng: Reusable Payment Codes for Hierarchical Deterministic Wallets, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Cô ấy có thể tiếp tục như vậy và sinh ra tới 2^32 địa chỉ trống thuộc về Bob.

Từ góc độ bên ngoài, bằng cách quan sát blockchain Bitcoin, là lý thuyết không thể phân biệt một giao dịch BIP47 với một giao dịch thông thường. Dưới đây là một ví dụ về giao dịch BIP47 trên Testnet:

https://blockstream.info/testnet/tx/94b2e59510f2e1fa78411634c98a77bbb638e28fb2da00c9f359cd5fc8f87254

TXID:

> 94b2e59510f2e1fa78411634c98a77bbb638e28fb2da00c9f359cd5fc8f87254

Nó trông giống như một giao dịch thông thường với một đầu vào đã chi, một đầu ra thanh toán của 210,000 sats, và tiền thối.

![Giao dịch thanh toán Bitcoin với BIP47](assets/23.webp)

Tín dụng: https://blockstream.info/

### Nhận thanh toán BIP47 và sinh khóa riêng.

Alice vừa thực hiện khoản thanh toán đầu tiên của mình đến một địa chỉ BIP47 trống thuộc về Bob. Bây giờ chúng ta hãy xem Bob nhận thanh toán này như thế nào. Chúng ta cũng sẽ xem tại sao Alice không có quyền truy cập vào khóa riêng của địa chỉ mà cô ấy vừa tạo, và làm thế nào Bob lấy lại khóa này để chi tiêu bitcoin mà anh ấy vừa nhận được.

Ngay khi Bob nhận được giao dịch thông báo từ Alice, anh ấy sinh ra khóa công khai BIP47 "K0" ngay cả trước khi cô ấy gửi bất kỳ khoản thanh toán nào đến nó. Do đó, anh ấy quan sát bất kỳ khoản thanh toán nào đến địa chỉ liên quan. Thực tế, anh ấy ngay lập tức sinh ra một số địa chỉ mà anh ấy sẽ quan sát (K0, K1, K2, K3...). Dưới đây là cách anh ấy sinh ra khóa công khai "K0":

- Bob chọn khóa riêng con đầu tiên được sinh ra từ mã thanh toán của mình. Khóa riêng này được gọi là "b". Nó được liên kết với khóa công khai "B" mà Alice đã sử dụng trong bước trước:

> b

- Bob chọn khóa công khai con đầu tiên được sinh ra từ mã thanh toán của Alice. Khóa này được gọi là "A". Nó được liên kết với khóa riêng "a" mà Alice đã sử dụng trong các phép tính của mình, và chỉ có Alice biết. Bob có thể thực hiện quá trình này vì anh ấy biết mã thanh toán của Alice được truyền cho anh ấy với giao dịch thông báo.

> A = a·G
- Bob tính toán điểm bí mật "S" bằng cách cộng và nhân đôi các điểm trên đường cong elliptic, áp dụng khóa riêng "b" của mình vào khóa công khai "A" của Alice. Tại đây, chúng ta sử dụng ECDH, đảm bảo rằng điểm "S" này sẽ giống nhau đối với cả Bob và Alice.
> S = b·A

- Giống như Alice đã làm, Bob tách riêng tọa độ x của điểm "S" này. Chúng tôi đã đặt tên giá trị này là "Sx". Anh ấy đưa giá trị này qua hàm SHA256 để tìm ra bí mật chung "s" (chữ thường).

> s = SHA256(Sx)

- Cũng như Alice, Bob tính toán điểm "s·G" trên đường cong elliptic. Sau đó, anh ấy cộng điểm bí mật này với khóa công khai "B" của mình. Anh ấy sau đó nhận được một điểm mới trên đường cong elliptic mà anh ấy hiểu là một khóa công khai "K0":

> K0 = B + s·G

Một khi Bob có khóa công khai "K0" này, anh ấy có thể suy ra khóa riêng tương ứng để chi tiêu bitcoin của mình. Chỉ mình anh ấy mới có thể tạo ra con số này.

- Bob thêm khóa riêng con đã suy ra "b" từ mã thanh toán cá nhân của mình. Chỉ mình anh ấy mới có thể nhận được giá trị của "b". Sau đó, anh ấy cộng "b" với bí mật chung "s" để nhận được k0, khóa riêng của K0:

> k0 = b + s
> Nhờ vào luật nhóm của đường cong elliptic, Bob chính xác nhận được khóa riêng tương ứng với khóa công khai mà Alice sử dụng. Vì vậy, chúng ta có:
> K0 = k0·G

![Bob tạo địa chỉ nhận BIP47 của mình](assets/24.webp)

Tín dụng: Reusable Payment Codes for Hierarchical Deterministic Wallets, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Nếu chúng ta so sánh sơ đồ này với những gì tôi đã mô tả cho bạn trước đó:

- "Child Priv-Key 0" phía Bob tương ứng với: b.

- "Child Pub-Key 0" phía Alice tương ứng với: A.

- "Payment Secret 0" tương ứng với: s.

- "Payment Pub-Key 0" tương ứng với: K0.

- "Payment Priv-Key 0" tương ứng với: k0.

Hãy tôi tóm tắt lại các bước mà chúng ta vừa xem cùng nhau để nhận một khoản thanh toán BIP47 và tính toán khóa riêng tương ứng:

- Bob chọn khóa riêng con đầu tiên được suy ra từ mã thanh toán cá nhân của mình.

- Anh ấy tính toán một điểm bí mật trên đường cong elliptic sử dụng ECDH từ khóa công khai con đầu tiên được suy ra từ mã chuỗi của Alice.

- Anh ấy sử dụng điểm bí mật này để tính toán một bí mật chung với SHA256.

- Anh ấy sử dụng bí mật chung này để tính toán một điểm bí mật mới trên đường cong elliptic.

- Anh ấy cộng điểm bí mật mới này với khóa công khai cá nhân của mình.

- Anh ấy nhận được một khóa công khai tạm thời mới, mà Alice sẽ gửi khoản thanh toán đầu tiên của cô ấy.

- Bob tính toán khóa riêng tương ứng với khóa công khai tạm thời này bằng cách cộng khóa riêng con đã suy ra từ mã thanh toán của mình và bí mật chung.

Vì Alice không thể nhận được "b," khóa riêng của Bob, cô ấy không thể xác định k0, khóa riêng tương ứng với địa chỉ nhận BIP47 của Bob.

Một cách sơ đồ, chúng ta có thể biểu diễn việc tính toán bí mật chung "S" như sau:

![Tính toán bí mật chung với ECDHE](assets/25.webp)

Một khi bí mật chung được tìm thấy với ECDH, Alice và Bob tính toán khóa công khai thanh toán BIP47 "K0," và Bob cũng tính toán khóa riêng tương ứng "k0":
![Phát sinh địa chỉ nhận BIP47 từ khóa bí mật chung](assets/26.webp)
### Hoàn tiền cho giao dịch BIP47.

Vì Bob biết mã thanh toán tái sử dụng của Alice, anh ta đã có tất cả thông tin cần thiết để gửi lại tiền cho cô ấy. Anh ta sẽ không cần phải liên hệ với Alice để yêu cầu bất kỳ thông tin nào. Anh ta chỉ cần thông báo cho cô ấy bằng một giao dịch thông báo, đặc biệt là để cô ấy có thể khôi phục địa chỉ BIP47 của mình với seed, và sau đó anh ta cũng có thể gửi cho cô ấy tới 2^32 khoản thanh toán.
Bob có thể hoàn tiền cho Alice theo cùng một cách mà cô ấy đã gửi tiền cho anh ta. Vai trò được đảo ngược:

![Bob gửi hoàn tiền cho Alice với BIP47](assets/27.webp)

Tín dụng: Mã Thanh Toán Tái Sử Dụng cho Ví Phân Cấp Xác Định, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Bây giờ bạn đã biết tất cả những điều cần biết về giải pháp tuyệt vời mà BIP47 đại diện.

## Các ứng dụng phái sinh của PayNym.

Việc triển khai BIP47 trên Samourai Wallet đã dẫn đến việc tạo ra PayNyms, các định danh được tính toán từ mã thanh toán của người dùng. Ngày nay, tính hữu ích của chúng vượt xa việc sử dụng BIP47.

Nhóm Samourai đang dần phát triển một hệ sinh thái toàn diện của công cụ và dịch vụ dựa trên PayNym của người dùng. Trong số này, rõ ràng có tất cả các công cụ chi tiêu giúp tối ưu hóa quyền riêng tư của người dùng bằng cách thêm entropy vào một giao dịch, và do đó thêm khả năng chối bỏ hợp lý.

Việc kết hợp sử dụng Soroban, mạng lưới truyền thông mã hóa dựa trên Tor, và PayNyms đã tối ưu hóa đáng kể trải nghiệm người dùng khi xây dựng giao dịch hợp tác, đồng thời duy trì một mức độ bảo mật tốt. Do đó, việc thực hiện giao dịch Stowaway (PayJoin) và StonewallX2 trở nên dễ dàng mà không cần thực hiện thủ công nhiều giao dịch chưa ký cần thiết để thiết lập một giao dịch hợp tác như vậy.

Khác với việc sử dụng BIP47, vì những giao dịch hợp tác này không yêu cầu một giao dịch thông báo, chỉ cần liên kết các PayNyms để sử dụng những công cụ này. Không cần phải kết nối chúng.

Nếu bạn muốn tìm hiểu thêm về giao dịch hợp tác, và rộng lớn hơn về tất cả các công cụ chi tiêu của Samourai Wallet, bạn có thể đọc phần "Công Cụ Chi Tiêu" trong bài viết này. Bạn sẽ tìm thấy một giải thích kỹ thuật và hướng dẫn chi tiết cho mỗi công cụ.

Ngoài những giao dịch hợp tác này, gần đây đã được quan sát thấy rằng nhóm Samourai đang làm việc trên một giao thức xác thực liên kết với PayNym: Auth47. Công cụ này đã được triển khai và cho phép, ví dụ, xác thực với một PayNym trên một trang web chấp nhận phương thức này. Trong tương lai, tôi nghĩ rằng ngoài khả năng xác thực trên web này, Auth47 sẽ là một phần của một dự án lớn hơn xung quanh hệ sinh thái BIP47/PayNym/Samourai. Có thể giao thức này sẽ được sử dụng để tối ưu hóa trải nghiệm người dùng của Samourai Wallet, đặc biệt là trong việc sử dụng các công cụ chi tiêu. Chúng ta sẽ chờ xem...

## Ý kiến cá nhân của tôi về BIP47.

Rõ ràng, nhược điểm chính của BIP47 là giao dịch thông báo. Nó buộc người dùng phải chi trả phí cho việc khai thác của nó, điều này có thể gây khó chịu cho một số người. Tuy nhiên, lập luận về "spam" trên blockchain Bitcoin là hoàn toàn không thể chấp nhận được. Bất kỳ ai trả phí cho giao dịch của mình đều phải có thể ghi nó vào sổ cái, bất kể mục đích của nó là gì. Khẳng định ngược lại là ủng hộ kiểm duyệt.

Có thể trong tương lai, các giải pháp ít tốn kém hơn sẽ được tìm thấy để truyền đạt mã thanh toán của người gửi cho người nhận, và cho người nhận lưu trữ nó một cách an toàn. Nhưng hiện tại, giao dịch thông báo vẫn là giải pháp ít nhất sự thỏa hiệp.
Nhược điểm này trở nên không đáng kể khi xem xét tất cả lợi ích của BIP47. Trong tất cả các đề xuất hiện có để giải quyết vấn đề tái sử dụng địa chỉ, nó dường như là giải pháp tốt nhất đối với tôi.
Như đã giải thích trước đó, phần lớn việc tái sử dụng địa chỉ đến từ các sàn giao dịch. BIP47 là giải pháp duy nhất hợp lý thực sự giải quyết vấn đề này ngay từ gốc. Bất kỳ đề xuất nào nhằm giảm số lượng tái sử dụng địa chỉ đều nên tập trung vào khía cạnh này và điều chỉnh giải pháp cho nguồn gốc chính của vấn đề.

Về khả năng sử dụng, mặc dù cơ chế bên trong khá phức tạp, nhưng quy trình thanh toán BIP47 lại rất đơn giản. Do đó, mã thanh toán có thể tái sử dụng có thể dễ dàng được áp dụng, ngay cả bởi người dùng mới.

Về quyền riêng tư, BIP47 rất thú vị. Như tôi đã giải thích trong phần về giao dịch thông báo, mã thanh toán không tiết lộ bất kỳ thông tin nào về các địa chỉ tạm thời được tạo ra. Do đó, nó phá vỡ dòng thông tin giữa giao dịch Bitcoin và bộ nhận dạng của người nhận, không giống như việc sử dụng truyền thống một địa chỉ nhận.

Và quan trọng nhất, việc triển khai PayNym của BIP47 hoạt động! Nó đã có sẵn trên Samourai Wallet từ năm 2016 và trên Sparrow Wallet từ đầu năm nay. Đây không phải là một dự án khoa học, mà là một giải pháp đã được kiểm tra ngày hôm qua và hoàn toàn hoạt động ngày hôm nay.

Hy vọng rằng, trong tương lai, những mã thanh toán có thể tái sử dụng này sẽ được các nhà hoạt động trong hệ sinh thái áp dụng, triển khai trong phần mềm ví, và được người dùng Bitcoin sử dụng.

Bất kỳ giải pháp tích cực nào cho quyền riêng tư của người dùng đều phải được thảo luận, thúc đẩy và bảo vệ, để Bitcoin không trở thành sân chơi của các CA và công cụ giám sát của chính phủ.
Anh ấy nghĩ về việc mình đã bị bách hại và xúc phạm ở khắp mọi nơi, và bây giờ anh ấy nghe mọi người nói rằng mình là con chim đẹp nhất trong tất cả những con chim đẹp! Và ngay cả cây cơm cháy cũng cúi cành về phía anh, và mặt trời lan tỏa ánh sáng ấm áp và từ bi! Sau đó, bộ lông của anh phồng lên, cổ thon dài của anh duỗi thẳng, và anh hét lên bằng cả trái tim, "Làm sao tôi có thể mơ về hạnh phúc nhiều như vậy khi tôi chỉ là một chú vịt con xấu xí."

## Để tìm hiểu thêm:

- Hiểu và sử dụng CoinJoin trên Bitcoin.

- Hiểu về các đường dẫn phái sinh của một ví Bitcoin.

- Cài đặt và sử dụng nút Bitcoin RoninDojo của bạn.

### Nguồn tài liệu và lời cảm ơn bên ngoài:

Cảm ơn LaurentMT và Théo Pantamis vì đã giải thích cho tôi nhiều khái niệm, mà tôi đã sử dụng trong bài viết này. Tôi hy vọng đã truyền đạt chính xác chúng.

Cảm ơn Fanis Michalakis đã đọc và đưa ra lời khuyên chuyên môn.

- https://bitcoiner.guide/paynym/
- https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki
- https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman
- https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman_bas%C3%A9_sur_les_courbes_elliptiques
- https://security.stackexchange.com/questions/46802/what-is-the-difference-between-dhe-and-ecdh#:~:text=The%20difference%20between%20DHE%20and%20ECDH%20in%20two%20bullet%20points,a%20type%20of%20algebraic%20curve).
- https://commandlinefanatic.com/cgi-bin/showarticle.cgi?article=art060
- https://ee.stanford.edu/~hellman/publications/24.pdf
- https://www.researchgate.net/publication/317339928_A_study_on_diffie-hellman_key_exchange_protocols