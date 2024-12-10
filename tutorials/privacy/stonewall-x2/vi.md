---
name: Stonewall x2
description: Hiểu và sử dụng giao dịch Stonewall x2
---
![cover stonewall x2](assets/cover.webp)

***CẢNH BÁO:** Sau vụ bắt giữ các nhà sáng lập của Samourai Wallet và việc tịch thu máy chủ của họ vào ngày 24 tháng 4, giao dịch Stonewallx2 chỉ hoạt động bằng cách trao đổi PSBT giữa các bên liên quan một cách thủ công, miễn là cả hai người dùng đều kết nối với Dojo của riêng họ. Tuy nhiên, có khả năng những công cụ này có thể được khởi động lại trong những tuần tới. Trong thời gian chờ đợi, bạn vẫn có thể tham khảo bài viết này để hiểu về cách hoạt động lý thuyết của Stonewallx2 và học cách thực hiện chúng một cách thủ công.*

_Nếu bạn đang xem xét thực hiện Stonewallx2 một cách thủ công, quy trình rất giống với quy trình được mô tả trong hướng dẫn này. Sự khác biệt chính nằm ở việc chọn loại giao dịch Stonewallx2: thay vì chọn `Online`, hãy nhấp vào `Trực tiếp / Thủ công`. Sau đó, bạn sẽ cần trao đổi PSBT một cách thủ công để xây dựng giao dịch Stonewallx2. Nếu bạn và đối tác của mình ở gần nhau, bạn có thể quét mã QR lần lượt. Nếu bạn ở xa, các tệp JSON có thể được trao đổi qua một kênh liên lạc an toàn. Phần còn lại của hướng dẫn không thay đổi._

_Chúng tôi đang theo dõi sát sao các diễn biến của vụ việc này cũng như các phát triển liên quan đến các công cụ tương ứng. Hãy yên tâm rằng chúng tôi sẽ cập nhật hướng dẫn này khi có thông tin mới._

_Hướng dẫn này chỉ mang tính chất giáo dục và thông tin. Chúng tôi không ủng hộ hoặc khuyến khích việc sử dụng các công cụ này cho mục đích phạm tội. Mỗi người dùng có trách nhiệm tuân thủ các luật lệ trong phạm vi quyền hạn của họ._

---

> *Biến mỗi lần chi tiêu thành một coinjoin.*

## Giao dịch Stonewall x2 là gì?

Stonewall x2 là một dạng giao dịch Bitcoin cụ thể nhằm tăng cường quyền riêng tư cho người dùng trong quá trình chi tiêu, bằng cách hợp tác với một bên thứ ba không tham gia vào việc chi tiêu đó. Phương pháp này mô phỏng một mini-coinjoin giữa hai người tham gia, trong khi thực hiện thanh toán cho một bên thứ ba. Giao dịch Stonewall x2 có sẵn trên cả ứng dụng Samourai Wallet và phần mềm Sparrow Wallet. Cả hai đều tương thích với nhau.

Cách hoạt động của nó tương đối đơn giản: chúng ta sử dụng một UTXO mà chúng ta sở hữu để thực hiện thanh toán và tìm kiếm sự hỗ trợ của một bên thứ ba, người cũng đóng góp một UTXO của riêng họ. Giao dịch kết quả trong bốn đầu ra: hai trong số đó có số lượng bằng nhau, một dành cho địa chỉ nhận thanh toán, cái kia cho một địa chỉ thuộc về người hợp tác. Một UTXO thứ ba được trả về một địa chỉ khác của người hợp tác, cho phép họ thu hồi số tiền ban đầu (một hành động trung lập đối với họ, trừ phí khai thác), và một UTXO cuối cùng trả về một địa chỉ thuộc về chúng ta, đó là số tiền thối lại từ việc thanh toán.

Như vậy, ba vai trò khác nhau được định nghĩa trong giao dịch Stonewall x2:
- Người gửi, người thực hiện thanh toán thực tế;
- Người hợp tác, người cung cấp bitcoin để cải thiện tổng thể sự ẩn danh của giao dịch, trong khi hoàn toàn thu hồi lại số tiền của họ ở cuối (một hành động trung lập đối với họ, trừ phí khai thác);
- Người nhận, người có thể không biết về bản chất cụ thể của giao dịch và đơn giản là mong đợi một khoản thanh toán từ người gửi.

Hãy lấy một ví dụ để hiểu rõ hơn. Alice đang ở tiệm bánh mua baguette của mình, giá `4,000 sats`. Cô ấy muốn thanh toán bằng bitcoin trong khi duy trì một mức độ quyền riêng tư nhất định cho việc thanh toán của mình. Do đó, cô ấy nhờ cậy vào người bạn của mình là Bob, người sẽ hỗ trợ cô trong quá trình này.
![schema stonewall x2](assets/en/1.webp)
Phân tích giao dịch này, chúng ta có thể thấy rằng người bán bánh thực sự đã nhận được `4,000 sats` như là thanh toán cho chiếc bánh mì baguette. Alice đã sử dụng `10,000 sats` làm đầu vào và nhận được `6,000 sats` làm đầu ra, dẫn đến một số dư ròng là `-4,000 sats`, tương ứng với giá của chiếc bánh mì baguette. Đối với Bob, anh ta đã cung cấp `15,000 sats` làm đầu vào và nhận được hai đầu ra: một là `4,000 sats` và cái kia là `11,000 sats`, dẫn đến một số dư là `0`. Trong ví dụ này, tôi cố ý bỏ qua phí khai thác để dễ hiểu hơn. Trong thực tế, phí giao dịch được chia sẻ đều giữa người gửi thanh toán và người hợp tác.

## Sự khác biệt giữa Stonewall và Stonewall x2 là gì?

Một giao dịch StonewallX2 hoạt động giống hệt như một giao dịch Stonewall, ngoại trừ việc trước đó là cộng tác trong khi sau này thì không. Như chúng ta đã thấy, một giao dịch Stonewall x2 bao gồm sự tham gia của một bên thứ ba, người nằm ngoài việc thanh toán, và người này sẽ cung cấp bitcoin của họ để tăng cường quyền riêng tư cho giao dịch. Trong một giao dịch Stonewall điển hình, vai trò của người hợp tác được thực hiện bởi người gửi.

Hãy xem lại ví dụ của Alice tại tiệm bánh. Nếu cô ấy không thể tìm thấy ai đó như Bob để cùng tham gia chi tiêu, cô ấy có thể đã thực hiện một giao dịch Stonewall một mình. Do đó, hai UTXO đầu vào sẽ là của cô ấy, và cô ấy sẽ nhận được 3 tại đầu ra.
![giao dịch stonewall](assets/en/2.webp)

Từ quan điểm bên ngoài, mô hình giao dịch sẽ giữ nguyên.
![Stonewall hay Stonewall x2?](assets/en/5.webp)
Do đó, logic nên như sau khi sử dụng công cụ chi tiêu Samourai:
- Nếu người bán không hỗ trợ Payjoin Stowaway, một giao dịch cộng tác có thể được thực hiện với một người khác nằm ngoài việc thanh toán sử dụng Stonewall x2.
- Nếu không tìm được ai để thực hiện giao dịch Stonewall x2, một giao dịch Stonewall có thể được thực hiện một mình, mô phỏng hành vi của một giao dịch Stonewall x2.
- Cuối cùng, lựa chọn cuối cùng sẽ là thực hiện giao dịch với JoinBot, một máy chủ do Samourai duy trì, có thể, theo yêu cầu, đóng vai trò là người hợp tác trong một giao dịch Stonewall x2.

Nếu bạn muốn tìm một người hợp tác sẵn lòng hỗ trợ bạn trong một giao dịch Stonewall X2, bạn cũng có thể tham gia nhóm Telegram này (không chính thức) được duy trì bởi người dùng Samourai để kết nối người gửi và người hợp tác: [Make Every Spend a Coinjoin](https://t.me/EverySpendACoinjoin).

[**-> Tìm hiểu thêm về giao dịch Stonewall**](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)

## Mục đích của một giao dịch Stonewall x2 là gì?

Cấu trúc Stonewall x2 thêm một lượng lớn entropy vào giao dịch và làm rối loạn phân tích chuỗi. Từ bên ngoài, một giao dịch như vậy có thể được hiểu là một Coinjoin nhỏ giữa hai cá nhân. Nhưng thực tế, đó là một thanh toán. Phương pháp này tạo ra sự không chắc chắn trong phân tích chuỗi, và thậm chí dẫn đến những dấu hiệu sai lầm.

Hãy quay lại ví dụ về Alice, Bob, và người bán bánh. Giao dịch trên blockchain sẽ trông như thế này:
![stonewall x2 công khai](assets/en/3.webp)
Một người quan sát bên ngoài dựa vào các phương pháp phân tích chuỗi thông thường có thể nhầm lẫn kết luận rằng "Alice và Bob đã thực hiện một giao dịch coinjoin nhỏ, với mỗi người một UTXO làm đầu vào và mỗi người hai UTXO làm đầu ra."![misinterpretation stonewall x2](assets/en/4.webp)Cách giải thích này không chính xác bởi vì, như bạn biết, một UTXO đã được gửi đến Baker, Alice chỉ có một đầu ra thay đổi, và Bob có hai.
![transaction stonewall x2](assets/en/1.webp)
Ngay cả khi người quan sát bên ngoài quản lý để xác định mô hình của giao dịch Stonewall x2, họ sẽ không có tất cả thông tin. Họ sẽ không thể xác định được UTXO nào trong hai UTXO có cùng số lượng tương ứng với khoản thanh toán. Hơn nữa, họ sẽ không thể biết được là Alice hay Bob đã thực hiện khoản thanh toán. Cuối cùng, họ sẽ không thể xác định được liệu hai UTXO đầu vào có đến từ hai người khác nhau hay chúng thuộc về một người đã kết hợp chúng. Điểm cuối cùng này là do giao dịch Stonewall cổ điển, mà chúng ta đã thảo luận ở trên, tuân theo chính xác cùng một mô hình như giao dịch Stonewall x2. Từ bên ngoài và không có thông tin bổ sung về bối cảnh, không thể phân biệt được giao dịch Stonewall với giao dịch Stonewall x2. Tuy nhiên, cái trước không phải là giao dịch hợp tác, trong khi cái sau thì có. Điều này thêm vào nhiều nghi ngờ hơn về khoản chi này.
![Stonewall hay Stonewall x2 ?](assets/en/5.webp)

## Làm thế nào để thiết lập kết nối giữa Paynyms để có thể hợp tác qua Soroban?

Giống như các giao dịch hợp tác khác trên Samourai (*Cahoots*), việc thực hiện một Stonewall x2 bao gồm việc trao đổi các giao dịch được ký một phần giữa người gửi và người hợp tác. Việc trao đổi này có thể được thực hiện một cách thủ công, trong trường hợp bạn đang ở cùng với người hợp tác của mình, hoặc tự động thông qua giao thức truyền thông Soroban.

Nếu bạn chọn phương án thứ hai, bạn sẽ cần thiết lập một kết nối giữa Paynyms trước khi có thể thực hiện một Stonewall x2. Để làm điều này, Paynym của bạn phải "theo dõi" Paynym của người hợp tác, và ngược lại.

**Truy cập Paynym của người hợp tác:**

Để bắt đầu, cần phải lấy mã thanh toán của Paynym của người hợp tác. Trong ứng dụng Samourai Wallet, người hợp tác của bạn phải nhấn vào biểu tượng Paynym của họ (robot nhỏ) nằm ở góc trên bên trái của màn hình, sau đó nhấp vào biệt danh Paynym của họ, bắt đầu bằng `+...`. Ví dụ, của tôi là `+namelessmode0aF`.

![samourai paynym](assets/notext/6.webp)
Nếu người hợp tác của bạn đang sử dụng Sparrow Wallet, họ nên nhấp vào tab 'Tools', sau đó vào 'Show PayNym'.![paynym sparrow](assets/notext/7.webp)
**Theo dõi PayNym của người hợp tác từ Samourai Wallet:**

Nếu bạn đang sử dụng Samourai Wallet, khởi chạy ứng dụng và truy cập menu 'PayNyms' theo cách tương tự. Nếu đây là lần đầu tiên bạn sử dụng PayNym của mình, bạn sẽ cần lấy mã định danh của nó.

![request paynym samourai](assets/notext/8.webp)

Sau đó nhấp vào dấu '+' màu xanh ở góc dưới bên phải của màn hình.
![add collaborator paynym](assets/notext/9.webp)
Bạn có thể sau đó dán mã thanh toán của người hợp tác bằng cách chọn 'PASTE PAYMENT CODE', hoặc mở camera để quét mã QR của họ bằng cách nhấn 'SCAN QR CODE'.
![nhập mã định danh paynym](assets/notext/10.webp)
Nhấn vào nút 'THEO DÕI'.
![theo dõi paynym](assets/notext/11.webp)
Xác nhận bằng cách nhấn 'CÓ'.
![xác nhận theo dõi paynym](assets/notext/12.webp)
Sau đó, phần mềm sẽ cung cấp cho bạn nút 'KẾT NỐI'. Việc nhấn vào nút này không cần thiết cho hướng dẫn của chúng tôi. Bước này chỉ cần thiết nếu bạn dự định thực hiện thanh toán cho PayNym khác như một phần của BIP47, không liên quan đến hướng dẫn của chúng tôi.
![kết nối paynym](assets/notext/13.webp)
Một khi PayNym của bạn đang theo dõi PayNym của người cộng tác, lặp lại quy trình này theo hướng ngược lại để người cộng tác của bạn cũng có thể theo dõi bạn. Sau đó, bạn có thể thực hiện giao dịch Stonewall x2.

**Theo dõi PayNym của người cộng tác từ Sparrow Wallet:**

Nếu bạn đang sử dụng Sparrow Wallet, mở ví của bạn và truy cập menu 'Hiển thị PayNym'. Nếu bạn sử dụng PayNym lần đầu, bạn sẽ cần lấy mã định danh bằng cách nhấn vào 'Lấy PayNym'.
![yêu cầu paynym sparrow](assets/notext/14.webp)
Sau đó nhập mã định danh PayNym của người cộng tác (hoặc biệt danh của họ '+...' hoặc mã thanh toán của họ 'PM...') vào ô 'Tìm Liên Hệ', và nhấn vào nút 'Thêm Liên Hệ'.
![thêm liên hệ paynym](assets/notext/15.webp)
Sau đó, phần mềm sẽ cung cấp cho bạn nút 'Liên Kết Liên Hệ'. Việc nhấn vào nút này không cần thiết cho hướng dẫn của chúng tôi. Bước này chỉ cần thiết nếu bạn dự định thực hiện thanh toán cho PayNym được chỉ định như một phần của BIP47, không liên quan đến hướng dẫn của chúng tôi.

Một khi PayNym của bạn đang theo dõi PayNym của người cộng tác, lặp lại quy trình này theo hướng ngược lại để người cộng tác của bạn cũng có thể theo dõi bạn. Sau đó, bạn có thể thực hiện giao dịch Stonewall x2.
## Cách thực hiện giao dịch Stonewall x2 trên Samourai Wallet?

Nếu bạn đã hoàn thành các bước trước đó của việc kết nối Paynyms, bạn cuối cùng đã sẵn sàng để thực hiện giao dịch Stonewall x2! Để làm điều này, hãy theo dõi hướng dẫn video của chúng tôi trên Samourai Wallet:
![Hướng dẫn Stonewall x2 - Samourai Wallet](https://youtu.be/89oYE1Hw3Fk?si=QTqUZ6IypiR6PPMr)

## Cách thực hiện giao dịch Stonewall x2 trên Sparrow Wallet?

Nếu bạn đã hoàn thành các bước trước đó của việc kết nối Paynyms, bạn cuối cùng đã sẵn sàng để thực hiện giao dịch Stonewall x2! Để làm điều này, hãy theo dõi hướng dẫn video của chúng tôi trên Sparrow Wallet:
![Hướng dẫn Stonewall x2 - Sparrow Wallet](https://youtu.be/mO3Xpp34Hhk?si=bfYiTl0Gxjs9sNQq)

**Nguồn tài nguyên bên ngoài:**
- https://sparrowwallet.com/docs/spending-privately.html;
- https://docs.samourai.io/en/spend-tools#stonewallx2.