---
name: Payjoin - Ví Samourai
description: Cách thực hiện giao dịch Payjoin trên Ví Samourai?
---
![samourai payjoin cover](assets/cover.webp)

***CHÚ Ý:** Sau khi các nhà sáng lập của Samourai Wallet bị bắt và máy chủ của họ bị tịch thu vào ngày 24 tháng 4, các Payjoins Stowaway trên Samourai Wallet chỉ hoạt động bằng cách trao đổi thủ công PSBT giữa các bên liên quan, với điều kiện cả hai người dùng đều kết nối với Dojo của riêng mình. Đối với Sparrow, các Payjoins qua BIP78 vẫn hoạt động. Tuy nhiên, có thể các công cụ này sẽ được khởi động lại trong những tuần tới. Trong khi chờ đợi, bạn có thể đọc bài viết này để hiểu cách hoạt động lý thuyết của Stowaway.*

_Nếu bạn dự định thực hiện Stowaway một cách thủ công, quy trình là rất giống với những gì được mô tả trong hướng dẫn này. Sự khác biệt chính nằm ở việc chọn loại giao dịch Stowaway: thay vì chọn `Online`, hãy nhấp vào `Trực tiếp / Thủ công`. Sau đó, bạn sẽ cần trao đổi PSBTs một cách thủ công để xây dựng giao dịch Stowaway. Nếu bạn ở gần người hợp tác, bạn có thể quét các mã QR liên tiếp. Nếu bạn ở xa, các tệp JSON có thể được trao đổi qua một kênh giao tiếp an toàn. Phần còn lại của hướng dẫn không thay đổi._

_Chúng tôi đang theo dõi sát sao các diễn biến của vụ việc này cũng như các phát triển liên quan đến các công cụ tương ứng. Hãy yên tâm rằng chúng tôi sẽ cập nhật hướng dẫn này khi có thông tin mới._

_Hướng dẫn này chỉ mang tính chất giáo dục và thông tin. Chúng tôi không ủng hộ hoặc khuyến khích việc sử dụng những công cụ này cho mục đích phạm tội. Mỗi người dùng có trách nhiệm tuân thủ các luật lệ trong phạm vi quyền hạn của họ._

---

> *"Buộc những kẻ gián điệp blockchain phải xem xét lại mọi thứ họ nghĩ rằng họ biết."*

Payjoin là một cấu trúc giao dịch Bitcoin đặc biệt giúp tăng cường quyền riêng tư cho người dùng trong quá trình chi tiêu bằng cách hợp tác với người nhận thanh toán. Có một số triển khai giúp thiết lập và tự động hóa PayJoin. Trong số các triển khai này, phổ biến nhất là Stowaway, được phát triển bởi các đội ngũ tại Ví Samourai. Hướng dẫn này giải thích cách thực hiện giao dịch Payjoin Stowaway sử dụng ứng dụng Ví Samourai.

## Stowaway hoạt động như thế nào?

Như đã đề cập trước đó, Ví Samourai cung cấp một công cụ PayJoin gọi là "Stowaway." Nó có thể truy cập thông qua phần mềm Sparrow Wallet trên PC hoặc ứng dụng Ví Samourai trên Android. Để thực hiện Payjoin, người nhận, người cũng đóng vai trò là người hợp tác, phải sử dụng phần mềm tương thích với Stowaway, cụ thể là Sparrow hoặc Samourai. Hai phần mềm này có khả năng tương tác, cho phép thực hiện giao dịch Stowaway giữa ví Sparrow và ví Samourai, và ngược lại.

Stowaway dựa trên một loại giao dịch mà Samourai gọi là "Cahoots." Một Cahoot cơ bản là một giao dịch hợp tác giữa nhiều người dùng, yêu cầu trao đổi thông tin ngoại tuyến. Đến nay, Samourai cung cấp hai công cụ Cahoots: Stowaway (Payjoins) và StonewallX2 (mà chúng tôi sẽ khám phá trong một bài viết tương lai).

Giao dịch Cahoots bao gồm việc trao đổi các giao dịch đã ký một phần giữa người dùng. Quá trình này có thể kéo dài và phức tạp, đặc biệt là khi thực hiện từ xa. Tuy nhiên, nó vẫn có thể được thực hiện một cách thủ công với người dùng khác, điều này có thể thuận tiện nếu các bên hợp tác ở gần nhau về mặt vật lý. Trên thực tế, điều này bao gồm việc trao đổi thủ công năm mã QR để được quét liên tiếp.

Khi thực hiện từ xa, quá trình này trở nên quá phức tạp. Để giải quyết vấn đề này, Samourai đã phát triển một giao thức giao tiếp mã hóa dựa trên Tor, gọi là "Soroban." Với Soroban, các trao đổi cần thiết cho một Payjoin được tự động hóa phía sau một giao diện thân thiện với người dùng. Đây là phương pháp thứ hai mà chúng tôi sẽ nghiên cứu trong bài viết này.
Những giao dịch được mã hóa này đòi hỏi việc thiết lập một kết nối và xác thực giữa các thành viên tham gia Cahoots. Do đó, giao tiếp Soroban dựa trên Paynyms của người dùng. Nếu bạn chưa quen với Paynyms, tôi mời bạn tham khảo bài viết này để biết thêm chi tiết: [BIP47 - PAYNYM](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093)

 Để nói một cách đơn giản, Paynym là một định danh duy nhất liên kết với ví của bạn, cho phép nhiều chức năng khác nhau, bao gồm cả tin nhắn được mã hóa. Paynym được trình bày dưới dạng một định danh và một hình minh họa đại diện cho một robot. Dưới đây là ví dụ về Paynym của tôi trên Testnet: ![paynym samourai wallet](assets/en/1.webp)

**Tóm tắt:**
- _Payjoin_ = Cấu trúc cụ thể của các giao dịch hợp tác;
- _Stowaway_ = Triển khai Payjoin có sẵn trên Samourai và Sparrow Wallet;
- _Cahoots_ = Tên gọi do Samourai đặt cho tất cả các loại giao dịch hợp tác của họ, bao gồm Payjoin Stowaway;
- _Soroban_ = Giao thức giao tiếp được mã hóa thiết lập trên Tor, cho phép hợp tác với người dùng khác trong bối cảnh giao dịch Cahoots;
- _Paynym_ = Định danh duy nhất của một ví cho phép giao tiếp với người dùng khác trên Soroban, nhằm thực hiện giao dịch Cahoots.

[**-> Tìm hiểu thêm về giao dịch Payjoin và công dụng của chúng**](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f)

## Làm thế nào để thiết lập kết nối giữa các Paynyms?

Để thực hiện một giao dịch Cahoots từ xa, cụ thể là PayJoin (Stowaway) qua Samourai, bạn cần phải "Theo dõi" người dùng mà bạn dự định hợp tác, sử dụng Paynym của họ. Trong trường hợp của Stowaway, điều này có nghĩa là theo dõi người mà bạn muốn gửi bitcoins.

**Dưới đây là quy trình để thiết lập kết nối này:**

Đầu tiên, bạn cần lấy mã thanh toán của Paynym của người nhận cho Payjoin. Trong ứng dụng Samourai Wallet, người nhận phải chạm vào biểu tượng Paynym của họ (robot nhỏ) nằm ở góc trên bên trái của màn hình, sau đó nhấp vào biệt danh Paynym của họ, bắt đầu với `+...`. Ví dụ, của tôi là `+namelessmode0aF`. Nếu người hợp tác của bạn sử dụng Sparrow Wallet, tôi mời bạn tham khảo hướng dẫn chuyên dụng của chúng tôi bằng cách nhấp vào đây.

![connexion paynym samourai](assets/notext/2.webp)

Người hợp tác của bạn sau đó sẽ được chuyển hướng đến trang Paynym của họ. Từ đó, họ có thể chia sẻ thông tin đăng nhập Paynym của mình với bạn hoặc chia sẻ mã QR của họ để bạn quét. Để làm điều này, họ phải nhấp vào biểu tượng "chia sẻ" nhỏ nằm ở góc trên bên phải màn hình của họ.
![partager paynym samourai](assets/en/1.webp)

Ở phía bạn, khởi chạy ứng dụng Samourai Wallet của mình và truy cập menu "PayNyms" theo cách tương tự. Nếu đây là lần đầu tiên bạn sử dụng Paynym của mình, bạn sẽ cần lấy định danh.

![demander un paynym](assets/notext/3.webp)

Sau đó nhấp vào nút màu xanh "+" ở góc dưới bên phải của màn hình.
![ajouter paynym collaborateur](assets/notext/4.webp)
Bạn có thể sau đó dán mã thanh toán của người hợp tác bằng cách chọn `COLLER LE CODE PAIEMENT`, hoặc mở camera để quét mã QR của họ bằng cách nhấn `SCANNEZ LE CODE QR`.![paste paynym identifier](assets/notext/5.webp)

Nhấp vào nút `SUIVRE`.
![theo dõi paynym](assets/notext/6.webp)Xác nhận bằng cách nhấp vào `YES`.
![xác nhận theo dõi paynym](assets/notext/7.webp)
Sau đó, phần mềm sẽ cung cấp cho bạn nút `SE CONNECTER`. Không cần thiết phải nhấp vào nút này cho hướng dẫn của chúng tôi. Bước này chỉ cần thiết nếu bạn dự định thực hiện thanh toán cho Paynym khác như một phần của BIP47, điều này không liên quan đến hướng dẫn của chúng tôi.
![kết nối paynym](assets/notext/8.webp)
Một khi Paynym của người nhận đã được Paynym của bạn theo dõi, lặp lại thao tác này theo hướng ngược lại để người nhận cũng theo dõi bạn. Sau đó, bạn có thể thực hiện một giao dịch Payjoin.

## Làm thế nào để thực hiện một giao dịch Payjoin trên Samourai Wallet?

Nếu bạn đã hoàn thành những bước sơ bộ này, bạn cuối cùng cũng sẵn sàng để thực hiện giao dịch Payjoin! Để làm điều này, hãy theo dõi hướng dẫn video của chúng tôi:

![Hướng dẫn Video Payjoin - Samourai Wallet](https://youtu.be/FXW6XZim0ww?si=EXalYwK1t9DT48aE)

**Nguồn tài nguyên bên ngoài:**
- https://docs.samourai.io/en/spend-tools#stowaway.