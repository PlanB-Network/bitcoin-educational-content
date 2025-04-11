---
name: Payjoin - Sparrow Wallet
description: Làm thế nào để thực hiện giao dịch Payjoin trên Sparrow Wallet?
---

![hình ảnh hướng dẫn về sparrow payjoin](assets/cover.webp)

_**CHÚ Ý:** Sau khi những người sáng lập Samourai Wallet bị bắt và máy chủ của họ bị tịch thu vào ngày 24 tháng 4, Payjoins Stowaway trên Samourai Wallet hiện chỉ hoạt động bằng cách trao đổi PSBT thủ công giữa các bên liên quan, với điều kiện cả hai người dùng đều kết nối với Dojo của riêng mình. Đối với Sparrow, Payjoins qua BIP78 vẫn hoạt động. Tuy nhiên, các công cụ này có thể sẽ được khởi động lại trong vài tuần tới. Trong thời gian chờ đợi, bạn luôn có thể đọc bài viết này để hiểu cách thức hoạt động lý thuyết của payjoins._

_Chúng tôi đang chú ý theo dõi sự phát triển của vụ việc này cũng như các công cụ liên quan. Hãy yên tâm rằng chúng tôi sẽ cập nhật hướng dẫn này khi có thông tin mới._

_Hướng dẫn này chỉ mang tính chất giáo dục và thông tin. Chúng tôi không ủng hộ hoặc khuyến khích việc sử dụng những công cụ này cho mục đích phạm tội. Mỗi người dùng có trách nhiệm tuân thủ luật pháp tại quốc gia của họ._

---

> *"Buộc những kẻ gián điệp blockchain phải xem xét lại mọi thứ họ nghĩ rằng họ biết."*

Payjoin là một cấu trúc giao dịch Bitcoin đặc biệt giúp tăng cường quyền riêng tư cho người dùng khi chi tiêu bằng cách hợp tác với người nhận thanh toán. Có một số triển khai giúp thiết lập và tự động hóa PayJoin. Trong số các triển khai này, phổ biến nhất là Stowaway do nhóm Samourai Wallet phát triển. Hướng dẫn này nhằm hướng dẫn bạn qua quá trình thực hiện giao dịch Stowaway Payjoin sử dụng phần mềm Sparrow Wallet.

## Stowaway hoạt động như thế nào?

Như đã đề cập trước đó, Samourai Wallet cung cấp một công cụ PayJoin gọi là "Stowaway." Nó có thể truy cập thông qua phần mềm Sparrow Wallet trên PC hoặc ứng dụng Samourai Wallet trên Android. Để thực hiện Payjoin, người nhận, người cũng đóng vai trò là người hợp tác, phải sử dụng phần mềm tương thích với Stowaway, cụ thể là Sparrow hoặc Samourai Wallet. Hai phần mềm này tương thích với nhau, cho phép thực hiện giao dịch Stowaway giữa ví Sparrow và ví Samourai, và ngược lại.

Stowaway dựa trên một loại giao dịch mà Samourai gọi là "Cahoots." Cahoot cơ bản là một giao dịch hợp tác giữa nhiều người dùng yêu cầu trao đổi thông tin ngoại tuyến. Hiện tại, Samourai cung cấp hai công cụ Cahoots: Stowaway (Payjoins) và StonewallX2 (mà chúng tôi sẽ khám phá trong một bài viết tương lai).

Giao dịch Cahoots liên quan đến việc trao đổi các giao dịch đã ký một phần giữa người dùng. Quá trình này có thể dài và phức tạp, đặc biệt là khi thực hiện từ xa. Tuy nhiên, nó vẫn có thể được thực hiện thủ công với người dùng khác, điều này có thể thuận tiện nếu các bên hợp tác ở gần nhau về mặt vật lý. Trên thực tế, điều này liên quan đến việc trao đổi thủ công năm mã QR để quét lần lượt.

Khi thực hiện từ xa, quá trình này trở nên quá phức tạp. Để giải quyết vấn đề này, Samourai đã phát triển một giao thức truyền thông mã hóa dựa trên Tor, gọi là "Soroban." Với Soroban, các trao đổi cần thiết cho Payjoin được tự động hóa thông qua một giao diện thân thiện với người dùng. Đây là phương pháp thứ hai mà chúng tôi sẽ khám phá trong bài viết này.

Những trao đổi mã hóa này yêu cầu thiết lập kết nối và xác thực giữa các bên tham gia Cahoots. Giao tiếp Soroban dựa trên Paynyms của người dùng. Nếu bạn chưa quen với Paynyms, tôi mời bạn tham khảo bài viết này để biết thêm chi tiết: [BIP47 - PAYNYM](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093)
Để nói một cách đơn giản, Paynym là một định danh duy nhất liên kết với ví của bạn cho phép thực hiện nhiều chức năng, bao gồm cả việc nhắn tin được mã hóa. Paynym được thể hiện dưới dạng một định danh và một hình minh họa đại diện cho một robot. Dưới đây là ví dụ về Paynym của tôi trên Testnet: ![Paynym Sparrow](assets/en/1.webp)
**Tóm tắt:**
- *Payjoin* = Cấu trúc cụ thể của giao dịch hợp tác;
- *Stowaway* = Triển khai Payjoin có sẵn trên Samourai và Sparrow Wallet;
- *Cahoots* = Tên gọi của Samourai cho tất cả các loại giao dịch hợp tác của họ, bao gồm Payjoin Stowaway;
- *Soroban* = Giao thức truyền thông được mã hóa thiết lập trên Tor, cho phép hợp tác với người dùng khác trong bối cảnh của một giao dịch Cahoots.
- *Paynym* = Định danh duy nhất của một ví cho phép giao tiếp với người dùng khác trên Soroban, nhằm thực hiện một giao dịch Cahoots.

[**-> Tìm hiểu thêm về giao dịch Payjoin và công dụng của chúng**](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f)

## Làm thế nào để thiết lập kết nối giữa các Paynyms?

Để thực hiện một giao dịch Cahoots từ xa, cụ thể là PayJoin (Stowaway) qua Samourai hoặc Sparrow, cần phải "Theo dõi" người dùng mà bạn dự định hợp tác, sử dụng Paynym của họ. Trong trường hợp của Stowaway, điều này có nghĩa là theo dõi người bạn muốn gửi bitcoin cho.

**Dưới đây là quy trình để thiết lập kết nối này:**

Đầu tiên, bạn cần lấy định danh Paynym của người nhận. Điều này có thể được thực hiện bằng cách sử dụng biệt danh hoặc mã thanh toán của họ. Để làm điều này, từ ví Sparrow của người nhận, chọn tab `Tools`, sau đó nhấp vào `Show PayNym`.
![Show Paynym](assets/notext/2.webp)
![Paynym Sparrow](assets/en/1.webp)
Về phía bạn, mở ví Sparrow của mình và truy cập cùng một menu `Show PayNym`. Nếu bạn đang sử dụng Paynym của mình lần đầu, bạn sẽ cần lấy một định danh bằng cách nhấp vào `Retrieve PayNym`.
![Retrieve paynym](assets/notext/3.webp)
Tiếp theo, nhập định danh Paynym của đối tác hợp tác của bạn (hoặc biệt danh `+...` hoặc mã thanh toán `PM...`) vào ô `Find Contact`, sau đó nhấp vào nút `Add Contact`.
![add contact](assets/notext/4.webp)
Phần mềm sau đó sẽ cung cấp cho bạn một nút `Link Contact`. Không cần thiết phải nhấp vào nút này cho hướng dẫn của chúng tôi. Bước này chỉ cần thiết nếu bạn dự định thực hiện thanh toán cho Paynym được chỉ định trong bối cảnh của BIP47, không liên quan đến hướng dẫn của chúng tôi.

Một khi Paynym của người nhận được Paynym của bạn theo dõi, lặp lại thao tác này theo hướng ngược lại để người nhận của bạn cũng theo dõi bạn. Bạn có thể sau đó thực hiện một Payjoin.

## Làm thế nào để thực hiện một Payjoin trên Sparrow Wallet?
Nếu bạn đã hoàn thành những bước sơ bộ này, bạn cuối cùng cũng sẵn sàng để thực hiện giao dịch Payjoin! Để làm điều này, hãy theo dõi hướng dẫn video của chúng tôi:
![Payjoin Tutorial - Sparrow Wallet](https://youtu.be/ZQxKod3e0Mg)

**Nguồn tài nguyên bên ngoài:**
- https://docs.samourai.io/en/spend-tools#stowaway ;
- https://sparrowwallet.com/docs/spending-privately.html.