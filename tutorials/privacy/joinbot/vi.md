---
name: JoinBot
description: Hiểu và sử dụng JoinBot
---

![DALL·E – robot samurai trong rừng đỏ, 3D render](assets/cover.webp)

***CẢNH BÁO:** Sau vụ bắt giữ các nhà sáng lập của Samourai Wallet và việc tịch thu máy chủ vào ngày 24 tháng 4, **dịch vụ JoinBot không còn khả dụng**. Tính đến thời điểm hiện tại, không thể sử dụng công cụ này. Tuy nhiên, bạn vẫn có thể thực hiện Stonewall X2, nhưng bạn cần tìm một đối tác và trao đổi PSBT một cách thủ công. Dịch vụ này có thể được khởi động lại trong những tháng tới tùy thuộc vào tiến trình của vụ án.*

_Chúng tôi đang theo dõi sát sao các diễn biến của vụ án cũng như các công cụ liên quan. Hãy yên tâm rằng chúng tôi sẽ cập nhật hướng dẫn này khi có thông tin mới._

_Hướng dẫn này được cung cấp chỉ với mục đích giáo dục và thông tin. Chúng tôi không ủng hộ hoặc khuyến khích sử dụng các công cụ này cho mục đích phạm tội. Mỗi người dùng có trách nhiệm tuân thủ các luật lệ trong phạm vi quyền hạn của họ._

---

JoinBot là một công cụ mới được thêm vào bộ Samourai Wallet với bản cập nhật mới nhất 0.99.98f của phần mềm ví Bitcoin nổi tiếng. Nó cho phép bạn dễ dàng thực hiện một giao dịch hợp tác để tối ưu hóa quyền riêng tư của mình, mà không cần phải tìm một đối tác.

*Cảm ơn Fanis Michalakis tuyệt vời vì ý tưởng sử dụng DALL-E cho hình thu nhỏ!*

## Giao dịch hợp tác trên Bitcoin là gì?

Bitcoin dựa trên một sổ cái tài khoản phân tán và minh bạch. Bất kỳ ai cũng có thể truy vết các giao dịch của người dùng hệ thống tiền mặt điện tử này. Để đảm bảo một mức độ quyền riêng tư nhất định, người dùng Bitcoin có thể thực hiện giao dịch với cấu trúc cụ thể để thêm khả năng chối bỏ hợp lý trong việc giải thích của họ.

Ý tưởng không phải là che giấu thông tin trực tiếp, mà là làm rối thông tin giữa những người khác. Mục tiêu này được sử dụng trong Coinjoins, các giao dịch làm vỡ lịch sử của một đồng tiền trên Bitcoin và làm cho việc truy vết của nó trở nên phức tạp. Để đạt được kết quả này, cần phải tạo ra nhiều đầu vào và đầu ra với cùng một số lượng trong giao dịch.

Đầu vào là các đầu vào của một giao dịch Bitcoin, và đầu ra đại diện cho các đầu ra. Giao dịch tiêu thụ các đầu vào của mình để tạo ra các đầu ra mới bằng cách thay đổi điều kiện chi tiêu của một đồng tiền. Cơ chế này cho phép di chuyển bitcoin giữa các người dùng.
Tôi thảo luận chi tiết về điều này trong bài viết này: Cơ chế Giao dịch Bitcoin: UTXO, Đầu vào, và Đầu ra.

Một cách để làm mờ dấu vết trong một giao dịch Bitcoin là thực hiện một giao dịch hợp tác. Như tên gọi, nó liên quan đến sự thỏa thuận giữa nhiều người dùng, mỗi người trong số họ đặt một số tiền bitcoin như đầu vào trong cùng một giao dịch và nhận một số tiền như đầu ra.

Như đã đề cập trước đó, cấu trúc hợp tác giao dịch nổi tiếng nhất là Coinjoin. Ví dụ, trên giao thức Coinjoin Whirlpool, giao dịch liên quan đến 5 người tham gia như đầu vào và đầu ra, mỗi người với cùng một số lượng bitcoin.

![Sơ đồ của một giao dịch Coinjoin trên Whirlpool](assets/1.webp)

Một quan sát viên bên ngoài của giao dịch này sẽ không thể biết đầu ra nào thuộc về người dùng nào như đầu vào. Nếu chúng ta lấy ví dụ về người dùng #4 (màu tím), chúng ta có thể nhận ra UTXO đầu vào của họ, nhưng chúng ta sẽ không biết đầu ra nào thực sự là của họ. Thông tin ban đầu không được ẩn, mà là bị làm rối trong một nhóm.
Người dùng có thể chối bỏ việc sở hữu một UTXO nhất định như đầu ra. Hiện tượng này được gọi là "khả năng chối bỏ hợp lý", và nó cho phép bảo mật trong một giao dịch Bitcoin minh bạch.

Để tìm hiểu thêm về Coinjoin, tôi giải thích MỌI THỨ trong bài viết dài này: Hiểu và sử dụng CoinJoin trên Bitcoin.
Mặc dù rất hiệu quả trong việc ngăn chặn việc truy vết một UTXO, Coinjoin không phù hợp cho việc chi tiêu trực tiếp. Thực tế, cấu trúc của nó đòi hỏi phải sử dụng các đầu vào với một số lượng đã được xác định trước và các đầu ra có giá trị tương tự (trừ phí khai thác). Tuy nhiên, giao dịch chi tiêu trên Bitcoin là một thời điểm quan trọng đối với quyền riêng tư vì nó thường tạo ra một liên kết vật lý giữa người dùng và hoạt động trên chuỗi của họ. Do đó, việc sử dụng các công cụ bảo mật quyền riêng tư cho việc chi tiêu dường như là cần thiết. Có các cấu trúc giao dịch hợp tác khác được thiết kế đặc biệt cho các giao dịch thanh toán thực tế.
## Giao dịch StonewallX2

Trong số vô số công cụ chi tiêu được cung cấp trên Samourai Wallet, có giao dịch hợp tác StonewallX2. Đây là một mini Coinjoin giữa hai người dùng được thiết kế cho việc thanh toán. Từ bên ngoài, giao dịch này có thể dẫn đến nhiều giải thích khả dĩ. Do đó, nó cung cấp khả năng phủ nhận hợp lý và do đó, bảo mật cho người dùng.

Cài đặt giao dịch hợp tác StonewallX2 có sẵn trên Samourai Wallet và Sparrow Wallet. Công cụ này có thể tương tác giữa hai phần mềm.

Cơ chế của nó khá dễ hiểu. Dưới đây là cách nó hoạt động trên thực tế:

> - Một người dùng muốn thực hiện một khoản thanh toán bằng bitcoin (ví dụ, tại một cửa hàng).
> - Họ lấy địa chỉ nhận của người nhận thanh toán thực sự (cửa hàng).
> - Họ xây dựng một giao dịch cụ thể với nhiều đầu vào: ít nhất một thuộc về họ và một thuộc về một người hợp tác bên ngoài.
> - Giao dịch sẽ có 4 đầu ra, bao gồm 2 đầu ra có cùng số lượng: một đến địa chỉ của cửa hàng để thanh toán, một là tiền thối trả lại cho người dùng, một đầu ra có giá trị tương đương với khoản thanh toán chuyển đến người hợp tác, và một đầu ra khác cũng trả lại cho người hợp tác.

Ví dụ, dưới đây là một giao dịch StonewallX2 điển hình mà tôi đã thực hiện một khoản thanh toán 50,125 sats. Đầu vào đầu tiên 102,588 sats đến từ ví Samourai của tôi. Đầu vào thứ hai 104,255 sats đến từ ví của người hợp tác của tôi:

![Sơ đồ giao dịch StonewallX2](assets/2.webp)

Chúng ta có thể quan sát 4 đầu ra, bao gồm 2 đầu ra có cùng số lượng để gây nhầm lẫn:

> - 50,125 sats chuyển đến người nhận thanh toán thực sự của tôi.
> - 52,306 sats đại diện cho tiền thối của tôi và do đó trả lại một địa chỉ trong ví của tôi.
> - 50,125 sats trả lại cho người hợp tác của tôi.
> - 53,973 sats trả lại cho người hợp tác của tôi.
>   Cuối cùng, người hợp tác sẽ có lại số dư ban đầu của họ (trừ phí khai thác), và người dùng đã thanh toán cho cửa hàng. Điều này thêm một lượng lớn entropy vào giao dịch và phá vỡ các liên kết không thể chối cãi giữa người gửi và người nhận thanh toán.

Sức mạnh của giao dịch StonewallX2 là nó hoàn toàn đối phó với một trong những quy tắc thực nghiệm được các nhà phân tích chuỗi sử dụng: sở hữu chung của các đầu vào trong một giao dịch đa đầu vào. Nói cách khác, trong hầu hết các trường hợp, nếu chúng ta quan sát một giao dịch Bitcoin với nhiều đầu vào, chúng ta có thể giả định rằng tất cả các đầu vào này thuộc về cùng một người. Satoshi Nakamoto đã nhận diện vấn đề này đối với quyền riêng tư của người dùng trong Bản Thảo của mình:

> "Là một bức tường lửa bổ sung, một cặp khóa mới có thể được sử dụng cho mỗi giao dịch để giữ chúng không bị liên kết với một chủ sở hữu chung. Tuy nhiên, sự liên kết là không thể tránh khỏi với các giao dịch đa đầu vào, chúng nhất thiết tiết lộ rằng các đầu vào của họ được sở hữu bởi cùng một chủ sở hữu."

Đây là một trong nhiều quy tắc thực nghiệm được sử dụng trong phân tích chuỗi để xây dựng các cụm địa chỉ. Để tìm hiểu thêm về các phép suy luận này, tôi khuyên bạn đọc loạt bài viết gồm bốn phần của Samourai, giới thiệu về chủ đề một cách tuyệt vời.
Sức mạnh của giao dịch StonewallX2 nằm ở việc một quan sát viên bên ngoài sẽ nghĩ rằng các đầu vào khác nhau của giao dịch thuộc về một chủ sở hữu chung. Trên thực tế, đó là hai người dùng khác nhau đang hợp tác. Việc phân tích giao dịch do đó bị dẫn lạc và quyền riêng tư của người dùng được bảo vệ.

Từ bên ngoài, một giao dịch StonewallX2 không thể phân biệt được với một giao dịch Stonewall. Sự khác biệt duy nhất hiệu quả giữa chúng là Stonewall không phải là hợp tác. Nó chỉ sử dụng UTXOs của một người dùng duy nhất. Tuy nhiên, trong cấu trúc của chúng trên sổ cái tài khoản, Stonewall và StonewallX2 hoàn toàn giống nhau. Điều này cho phép có thêm nhiều cách giải thích khả dĩ về cấu trúc giao dịch này, vì một quan sát viên bên ngoài sẽ không thể biết liệu các đầu vào đến từ cùng một người hay từ hai người hợp tác.

Hơn nữa, lợi thế của StonewallX2 so với một PayJoin kiểu Stowaway là nó có thể được sử dụng trong bất kỳ tình huống nào. Người nhận thanh toán thực tế không đóng góp bất kỳ đầu vào nào vào giao dịch. Do đó, một StonewallX2 có thể được sử dụng để thanh toán tại bất kỳ nhà bán lẻ nào chấp nhận Bitcoin, ngay cả khi nhà bán lẻ không sử dụng Samourai hoặc Sparrow.

Mặt khác, nhược điểm chính của cấu trúc giao dịch này là nó đòi hỏi một người hợp tác sẵn lòng sử dụng bitcoin của họ để tham gia vào thanh toán của bạn. Nếu bạn có bạn bè bitcoin sẵn lòng giúp đỡ bạn trong bất kỳ tình huống nào, đây không phải là vấn đề. Tuy nhiên, nếu bạn không biết bất kỳ người dùng Ví Samourai nào, hoặc nếu không có ai sẵn lòng hợp tác, thì bạn sẽ gặp khó khăn.

Để giải quyết vấn đề này, nhóm Samourai gần đây đã thêm một tính năng mới vào ứng dụng của họ: JoinBot.

# JoinBot là gì?

Nguyên tắc của JoinBot rất đơn giản. Nếu bạn không thể tìm thấy ai để hợp tác cho một giao dịch StonewallX2, bạn có thể hợp tác với JoinBot. Trên thực tế, bạn sẽ thực sự thực hiện một giao dịch hợp tác trực tiếp với Ví Samourai.

Dịch vụ này rất tiện lợi, đặc biệt là cho người dùng mới, vì nó có sẵn 24/7. Nếu bạn cần thực hiện một khoản thanh toán khẩn cấp và muốn thực hiện một StonewallX2, bạn không cần phải liên hệ với một người bạn hoặc tìm kiếm một người hợp tác trực tuyến nữa. JoinBot sẽ hỗ trợ bạn.

Một lợi ích khác của JoinBot là UTXOs mà nó cung cấp làm đầu vào độc quyền từ Whirlpool sau khi trộn, điều này cải thiện quyền riêng tư của khoản thanh toán của bạn. Ngoài ra, vì JoinBot luôn trực tuyến, bạn nên hợp tác với UTXOs có Anonsets tiềm năng lớn.

Rõ ràng, JoinBot có một số điều chỉnh cần được lưu ý:

> Giống như với một StonewallX2 cổ điển, người hợp tác của bạn nhất thiết phải biết về UTXOs được sử dụng và điểm đến của chúng. Trong trường hợp của JoinBot, Samourai biết chi tiết của giao dịch này. Điều này không nhất thiết là điều xấu, nhưng nên được ghi nhớ.
> Để tránh spam, Samourai tính phí dịch vụ 3.5% trên số tiền của giao dịch thực tế, với giới hạn tối đa là 0.01 BTC. Ví dụ, nếu tôi gửi một khoản thanh toán thực sự là 100 kilosats với JoinBot, số tiền phí dịch vụ sẽ là 3,500 sats.
> Để sử dụng JoinBot, bạn phải có ít nhất hai UTXOs không liên quan và có sẵn trong ví của mình.
> Trong một StonewallX2 cổ điển, phí khai thác được chia đều giữa hai người hợp tác. Với JoinBot, bạn rõ ràng sẽ phải trả toàn bộ phí khai thác.
Để một giao dịch JoinBot được hoàn toàn giống như một giao dịch StonewallX2 hoặc Stonewall cổ điển, việc thanh toán phí dịch vụ được thực hiện trong một giao dịch hoàn toàn riêng biệt. Việc hoàn trả một nửa phí khai thác ban đầu mà Samourai đã trả sẽ được thực hiện trong giao dịch thứ hai này. Để tối ưu hóa quyền riêng tư của bạn đến cùng, việc thanh toán phí được thực hiện bằng cách sử dụng một giao dịch được cấu trúc theo Stowaway (PayJoin).

## Cách sử dụng JoinBot?

Để thực hiện một giao dịch JoinBot, bạn phải có Ví Samourai. Bạn có thể tải về tại đây, hoặc từ Google Playstore.

Khác với đa số công cụ được phát triển bởi Samourai, Sparrow Wallet chưa công bố việc triển khai JoinBot. Do đó, công cụ này chỉ có sẵn trên Samourai.

Khám phá từng bước cách thực hiện một giao dịch StonewallX2 với JoinBot trong video này:

![Cách sử dụng Joinbot](https://youtu.be/80MoMz2Ne5g)

Dưới đây là sơ đồ giao dịch mà chúng tôi vừa thực hiện trong video:

![Sơ đồ giao dịch StonewallX2 của tôi với JoinBot.](assets/3.webp)

Chúng ta có thể thấy 5 đầu vào:

> - 3 đầu vào của 100 kilosats đến từ Samourai (JoinBot).
> - 2 đầu vào đến từ ví cá nhân của tôi, lần lượt là 3,524 sats và 1.8 megasat.

Có 4 đầu ra của giao dịch như sau:

> - 1 đầu ra là 212,452 sats đến người nhận thanh toán thực sự của tôi.
> - Một đầu ra khác cùng số lượng đó quay trở lại địa chỉ Samourai.
> - 1 đầu ra thay đổi cũng quay trở lại Samourai với 87,302 sats. Điều này đại diện cho sự chênh lệch giữa tổng số đầu vào của họ (300,000 sats) và đầu ra làm mờ (212,452 sats) trừ đi phí khai thác.
> - 1 đầu ra thay đổi quay trở lại một địa chỉ khác trong ví của tôi. Nó đại diện cho sự chênh lệch giữa tổng số đầu vào của tôi và khoản thanh toán thực tế, trừ đi phí khai thác.

Như một lời nhắc nhở, phí khai thác không đại diện cho các đầu ra giao dịch. Chúng chỉ đại diện cho sự chênh lệch giữa tổng số đầu vào và tổng số đầu ra.

## Kết luận

JoinBot là một công cụ bổ sung mang lại nhiều lựa chọn và tự do hơn cho người dùng Samourai. Nó cho phép thực hiện một giao dịch StonewallX2 cộng tác trực tiếp với Samourai làm đối tác cộng tác. Loại giao dịch này giúp cải thiện quyền riêng tư cho người dùng.

Nếu bạn có thể thực hiện một giao dịch StonewallX2 cổ điển với một người bạn, tôi vẫn khuyên bạn nên sử dụng công cụ này. Tuy nhiên, nếu bạn gặp khó khăn và không thể tìm thấy bất kỳ đối tác cộng tác nào để thực hiện thanh toán, bạn biết rằng JoinBot sẽ luôn sẵn sàng 24/7 để cộng tác với bạn.

**Nguồn tài nguyên bên ngoài:**
- https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923
- https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin