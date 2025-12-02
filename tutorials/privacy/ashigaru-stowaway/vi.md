---
name: Ashigaru - Người đi lậu
description: Làm thế nào để thực hiện giao dịch Payjoin trên Ashigaru?
---
![cover](assets/cover.webp)



> *Buộc những kẻ theo dõi blockchain phải suy nghĩ lại mọi thứ họ nghĩ mình biết.*

Payjoin là một cấu trúc giao dịch Bitcoin được thiết kế để tăng cường tính bảo mật của người dùng bằng cách hợp tác trực tiếp với người nhận thanh toán. Có nhiều giải pháp triển khai giúp việc triển khai dễ dàng hơn và tự động hóa quy trình. Nổi tiếng nhất trong số đó chắc chắn là Stowaway, ban đầu được phát triển bởi nhóm Samurai Wallet và hiện được tích hợp vào fork Ashigaru.



## Stowaway hoạt động như thế nào?



Như đã đề cập trước đó, Ashigaru tích hợp công cụ PayJoin có tên là `Stowaway`. Công cụ này có sẵn trong ứng dụng Ashigaru trên Android. Để Payjoin được thực hiện, người nhận (đồng thời cũng là cộng tác viên) phải sử dụng phần mềm tương thích với Stowaway, tức là hiện tại chỉ có Ashigaru.



Stowaway dựa trên một loại giao dịch mà Samurai gọi là "Cahoots". Cahoot là một giao dịch hợp tác giữa nhiều người dùng, bao gồm việc trao đổi thông tin bên ngoài blockchain Bitcoin. Ashigaru hiện cung cấp hai công cụ Cahoots: Stowaway (Payjoins) và StonewallX2.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b

Giao dịch Cahoots yêu cầu trao đổi các giao dịch đã được ký một phần giữa người dùng. Quá trình này có thể mất nhiều thời gian và công sức, đặc biệt là khi thực hiện từ xa. Tuy nhiên, vẫn có thể thực hiện thủ công nếu các cộng tác viên ở cùng một địa điểm. Cụ thể, việc này bao gồm việc quét năm mã QR liên tiếp, được trao đổi giữa hai bên tham gia.



Ở khoảng cách xa, phương pháp này trở nên quá phức tạp. Để khắc phục điều này, Samourai đã phát triển một giao thức truyền thông được mã hóa dựa trên Tor có tên là "*Soroban*". Nhờ Soroban, các giao dịch cần thiết cho Payjoin được tự động hóa và diễn ra ở chế độ nền.



Các giao tiếp được mã hóa này yêu cầu kết nối và xác thực giữa những người tham gia Cahoot. Đây là lý do tại sao Soroban dựa vào Paynym của người dùng. Nếu bạn chưa quen với cách thức hoạt động của Paynym, hãy xem hướng dẫn chuyên sâu này để tìm hiểu thêm:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

Tóm lại, Paynym là một mã định danh duy nhất được liên kết với wallet của bạn, cho phép bạn kích hoạt nhiều chức năng khác nhau, bao gồm cả các giao dịch được mã hóa. Nó có dạng một mã định danh kèm theo hình minh họa. Ví dụ, đây là mã định danh tôi sử dụng trên Testnet:



![Image](assets/fr/01.webp)



**Tóm lại:**





- "payjoin" = Cấu trúc giao dịch hợp tác cụ thể;





- `Stowaway` = Triển khai Payjoin có sẵn trên Ashigaru;





- `Cahoots` = Tên do Samourai đặt cho tất cả các loại giao dịch hợp tác của họ, đặc biệt là Payjoin `Stowaway`, được tiếp quản ngày hôm nay trên Ashigaru;





- soroban = Giao thức truyền thông được mã hóa được thiết lập trên Tor cho phép cộng tác với những người dùng khác trong giao dịch `Cahoots`;





- "paynym" = Mã định danh wallet duy nhất được sử dụng để thiết lập liên lạc với người dùng khác trên "Soroban" nhằm thực hiện giao dịch "Chahoots".



Để hiểu sâu hơn về cách thức hoạt động của Payjoin và tính hữu ích của chúng trong quyền riêng tư trên chuỗi, tôi xin giới thiệu hướng dẫn khác này:



https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

## Làm thế nào để thiết lập kết nối giữa Paynyms?



Để bắt đầu, tất nhiên bạn sẽ cần cài đặt Ashigaru và tạo:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Để thực hiện giao dịch Cahoots từ xa, bao gồm cả PayJoin (*Người đi lậu*) qua Ashigaru, trước tiên bạn phải "theo dõi" người dùng mà bạn muốn cộng tác, sử dụng Paynym của họ. Trong trường hợp người đi lậu, điều này có nghĩa là theo dõi người mà bạn muốn gửi bitcoin. Nếu bạn chưa biết cách theo dõi một Paynym khác, bạn sẽ tìm thấy quy trình chi tiết trong hướng dẫn này:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## Làm thế nào để tôi có thể tham gia Payjoin trên Ashigaru?



Để thực hiện giao dịch Stowaway, hãy nhấp vào hình ảnh Paynym của bạn ở góc trên bên trái màn hình, sau đó mở menu `Cộng tác`. Người tham gia giao dịch với bạn cũng phải làm như vậy, trừ khi bạn trao đổi mã QR trực tiếp.



![Image](assets/fr/02.webp)



Bạn có hai lựa chọn: chọn `Initiate` nếu bạn là người gửi thanh toán hoặc `Participate` nếu bạn là người nhận thanh toán của giao dịch thanh toán này.



![Image](assets/fr/03.webp)



Nếu bạn là người nhận, quy trình rất đơn giản. Để cộng tác từ xa qua mạng Soroban, hãy nhấp vào `Tham gia`, chọn tài khoản bạn muốn sử dụng, sau đó nhấn `LISTEN FOR CAHOOTS REQUESTS` để chờ yêu cầu từ người trả tiền.



![Image](assets/fr/04.webp)



Mặt khác, để cộng tác trực tiếp thông qua quét mã QR, hãy vào trang chủ của wallet, nhấn vào biểu tượng mã QR ở đầu màn hình, sau đó quét mã QR do người thanh toán cung cấp khi thực hiện giao dịch.



![Image](assets/fr/05.webp)



Nếu bạn là người thanh toán, tức là người khởi tạo giao dịch, hãy vào menu `Cộng tác`, sau đó chọn `Khởi tạo`.



![Image](assets/fr/06.webp)



Đối với loại giao dịch, vì chúng ta muốn thực hiện giao dịch Payjoin Stowaway, hãy chọn tùy chọn này.



![Image](assets/fr/07.webp)



Sau đó, bạn có thể chọn giữa hình thức cộng tác trực tuyến (*Cahoots* thông qua *Soroban*) hoặc cộng tác trực tiếp bằng cách trao đổi mã QR.



![Image](assets/fr/08.webp)



### Thông đồng trực tuyến



Nếu bạn chọn tùy chọn `Trực tuyến`, hãy chọn người nhận từ Paynyms mà bạn đang theo dõi.



![Image](assets/fr/09.webp)



Nhấp vào `Thiết lập giao dịch`, sau đó chọn tài khoản mà bạn muốn thực hiện chi tiêu.



![Image](assets/fr/10.webp)



Ở trang tiếp theo, hãy nhập thông tin chi tiết giao dịch: số tiền cần gửi cho người nhận và mức phí. Không cần nhập địa chỉ nhận, vì người nhận sẽ tự chuyển địa chỉ này trong quá trình trao đổi PSBT.



Sau đó nhấp vào `Xem lại thiết lập giao dịch`.



![Image](assets/fr/11.webp)



Kiểm tra thông tin cẩn thận, đảm bảo cộng tác viên của bạn đang lắng nghe yêu cầu *Cahoots*, sau đó nhấp vào nút `BEGIN TRANSACTION` màu xanh lá cây để bắt đầu trao đổi PSBT qua Soroban.



![Image](assets/fr/12.webp)



Chờ cho đến khi cả hai bên tham gia đều ký giao dịch, sau đó phát sóng giao dịch đó trên mạng Bitcoin.



![Image](assets/fr/13.webp)



### Thảo luận trực tiếp



Nếu bạn muốn thực hiện giao dịch trực tiếp, hãy chọn loại giao dịch `STONEWALL X2`, sau đó chọn tùy chọn `Trực tiếp/Thủ công`.



![Image](assets/fr/14.webp)



Nhấp vào `Thiết lập giao dịch`, sau đó chọn tài khoản mà bạn muốn thực hiện chi tiêu.



![Image](assets/fr/15.webp)



Ở trang tiếp theo, hãy nhập thông tin chi tiết giao dịch: số tiền cần gửi cho người nhận và mức phí. Không cần nhập địa chỉ nhận, vì người nhận sẽ tự chuyển địa chỉ này trong quá trình trao đổi PSBT.



Sau đó nhấp vào `Xem lại thiết lập giao dịch`.



![Image](assets/fr/16.webp)



Kiểm tra thông tin chi tiết, sau đó nhấn nút `BEGIN TRANSACTION` màu xanh lá cây để bắt đầu trao đổi PSBT thông qua quét mã QR.



![Image](assets/fr/17.webp)



Việc trao đổi được thực hiện bằng cách luân phiên quét mã QR với cộng tác viên: nhấp vào `HIỂN THỊ MÃ QR` để hiển thị mã QR của bạn cho cộng tác viên, người này sẽ quét mã. Sau đó, họ sẽ nhấp vào `HIỂN THỊ MÃ QR` để hiển thị mã QR của họ, và bạn sẽ quét mã bằng `LAUNCH QR Scanner`. Lặp lại quy trình này cho đến khi hoàn tất cả năm bước trao đổi.



![Image](assets/fr/18.webp)



Sau khi hoàn tất mọi giao dịch, hãy kiểm tra thông tin chi tiết về giao dịch, sau đó phát hành giao dịch bằng cách kéo mũi tên màu xanh lá cây ở cuối màn hình.



![Image](assets/fr/19.webp)



[Giao dịch đã được công bố](https://mempool.space/testnet4/tx/82efd3700bba87b0f172e9cc045e441b38622c95a60df9f39a21f63eb4590a96). Cấu trúc của giao dịch như sau:



![Image](assets/fr/20.webp)



*Nguồn: [mempool.space](https://mempool.space/)*



Nếu chúng ta phân tích giao dịch này, chúng ta thấy UTXO của tôi là `164.211 sats` ở phía đầu vào, cũng như UTXO là `190.002 sats` thuộc về người nhận thực tế của khoản thanh toán. Ở phía đầu ra, tôi nhận được một khoản trao đổi UTXO là `63.995 sats`, trong khi người nhận nhận được UTXO là `290.002 sats`. So sánh đầu vào và đầu ra, chúng ta có thể thấy rằng người nhận thực sự đã kiếm được `100.000 sats`, tương ứng với số tiền thanh toán thực tế của tôi, và tôi đã mất `100.000 sats`, mà tôi đã cộng thêm chi phí mining.



Rõ ràng là tôi có thể mô tả cấu trúc này vì tôi đã tự mình xây dựng giao dịch. Nhưng đối với người quan sát bên ngoài, nhìn chung không thể xác định được UTXO nào thuộc về bên tham gia nào, dù là đầu vào hay đầu ra.



Để hiểu sâu hơn về quản lý quyền riêng tư trên chuỗi khối trên Bitcoin, tôi khuyên bạn nên tham gia khóa đào tạo BTC 204 của tôi trên Plan ₿ Academy:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c