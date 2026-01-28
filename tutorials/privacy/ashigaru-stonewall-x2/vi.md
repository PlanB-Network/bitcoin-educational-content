---
name: Ashigaru - Stonewall x2
description: Hiểu và sử dụng giao dịch Stonewall x2 trên Ashigaru
---
![cover stonewall x2](assets/cover.webp)



> *Hãy biến mỗi lần chi tiêu thành một lần tham gia

## Giao dịch Stonewall x2 là gì?



Stonewall x2 là một hình thức giao dịch Bitcoin đặc biệt được thiết kế để tăng cường tính bảo mật của người dùng khi chi tiêu, bằng cách hợp tác với một bên thứ ba không liên quan đến chi tiêu. Phương pháp này mô phỏng một giao dịch mini-coinjoin giữa hai bên tham gia, trong khi thực hiện thanh toán cho bên thứ ba. Giao dịch Stonewall x2 có sẵn trên ứng dụng Ashigaru, một fork của Samourai Wallet (đội ngũ đứng sau việc tạo ra loại giao dịch này).



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Cách thức hoạt động tương đối đơn giản: bạn sử dụng một thẻ UTXO do bạn sở hữu để thực hiện thanh toán và nhờ sự hỗ trợ của một bên thứ ba, bên này cũng đóng góp bằng một thẻ UTXO của riêng họ. Giao dịch kết thúc với bốn đầu ra: hai đầu ra có số tiền bằng nhau, một đầu ra đến địa chỉ của người nhận tiền, đầu ra còn lại đến địa chỉ của bên cộng tác. Một thẻ UTXO thứ ba được trả về một địa chỉ khác của bên cộng tác, cho phép bên cộng tác thu hồi số tiền ban đầu (một hành động trung lập đối với bên cộng tác, modulo chi phí của thẻ mining), và một thẻ UTXO cuối cùng được trả về một địa chỉ của chúng tôi, tạo thành giao dịch thanh toán.



Do đó, ba vai trò khác nhau được xác định trong các giao dịch Stonewall x2:




- Người phát hành, người thực hiện thanh toán thực tế;
- Người cộng tác, người cung cấp bitcoin để cải thiện tính ẩn danh của giao dịch, đồng thời thu hồi toàn bộ tiền của mình vào cuối giao dịch (một hành động trung lập đối với anh ta, modulo chi phí mining);
- Người nhận có thể không biết bản chất cụ thể của giao dịch và chỉ mong đợi người gửi thanh toán.



Hãy lấy một ví dụ. Alice đến tiệm bánh để mua một ổ bánh mì baguette, giá 4.000 sats. Cô ấy muốn thanh toán bằng bitcoin, đồng thời giữ bí mật về khoản thanh toán của mình. Vì vậy, cô ấy nhờ đến sự giúp đỡ của bạn mình là Bob.



![image](assets/fr/01.webp)



Phân tích giao dịch này, chúng ta có thể thấy rằng người thợ làm bánh thực sự đã nhận được 4.000 sats tiền thanh toán cho chiếc bánh mì baguette. Alice đã sử dụng 10.000 sats tiền đầu vào và thu về 6.000 sats tiền đầu ra, tạo ra số dư ròng là 4.000 sats, tương ứng với giá của chiếc bánh mì baguette. Đối với Bob, nó đã cung cấp 15.000 sats tiền đầu vào và nhận được hai đầu ra: một là 4.000 sats và một là 11.000 sats, tạo ra số dư là 0.



Trong ví dụ này, tôi cố tình bỏ qua phí mining để dễ hiểu hơn. Trên thực tế, phí giao dịch được chia đều giữa bên phát hành thanh toán và bên cộng tác.



## Sự khác biệt giữa Stonewall và Stonewall x2 là gì?



Giao dịch StonewallX2 hoạt động hoàn toàn giống với giao dịch Stonewall, ngoại trừ việc giao dịch StonewallX2 mang tính cộng tác, trong khi giao dịch StonewallX2 thì không. Như chúng ta đã thấy, giao dịch StonewallX2 liên quan đến sự tham gia của một bên thứ ba, bên ngoài giao dịch và sẽ cung cấp bitcoin của mình để tăng cường tính bảo mật của giao dịch. Trong một giao dịch Stonewall cổ điển, vai trò cộng tác viên được đảm nhận bởi người gửi.



Quay lại ví dụ về Alice ở tiệm bánh. Nếu cô ấy không tìm được ai đó như Bob để cùng đi mua sắm, cô ấy đã có thể tự mình thực hiện một cú Stonewall. Bằng cách đó, hai UTXO trên đường vào sẽ là của cô ấy, và cô ấy sẽ nhặt được 3 UTXO trên đường ra.



![image](assets/fr/02.webp)




Theo quan điểm của người ngoài cuộc, giao dịch vẫn sẽ như vậy.



![image](assets/fr/05.webp)



Do đó, logic phải như sau khi bạn muốn sử dụng công cụ chi tiêu Ashigaru:




- Nếu nhà cung cấp không hỗ trợ Payjoin Stowaway, bạn có thể thực hiện giao dịch hợp tác với người khác bên ngoài đơn vị thanh toán nhờ Stonewall x2;
- Nếu bạn không tìm được ai thực hiện giao dịch Stonewall x2, bạn có thể thực hiện giao dịch chỉ có Stonewall, giao dịch này sẽ mô phỏng hành vi của giao dịch Stonewall x2.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-033daa45-d42c-40e1-9511-cea89751c3d4

## Mục đích của giao dịch Stonewall x2 là gì?



Cấu trúc Stonewall x2 làm tăng một lượng entropy khổng lồ vào giao dịch, gây nhiễu loạn cho việc phân tích chuỗi. Nhìn từ bên ngoài, một giao dịch như vậy có thể được hiểu là một giao dịch Coinjoin nhỏ giữa hai người. Nhưng thực tế, đó là một khoản thanh toán. Do đó, phương pháp này tạo ra sự không chắc chắn trong phân tích chuỗi, hoặc thậm chí dẫn đến sai sót.



Hãy lấy ví dụ về Alice, Bob và Boulanger. Giao dịch trên blockchain sẽ như thế này:



![image](assets/fr/03.webp)



Một người quan sát bên ngoài dựa vào phương pháp phân tích chuỗi chung có thể kết luận sai rằng "*Alice và Bob đã thực hiện một liên kết nhỏ, với một UTXO vào và hai UTXO ra mỗi bên*".



![image](assets/fr/04.webp)



Cách giải thích này không chính xác vì, như bạn đã biết, một UTXO được gửi đến Boulanger, Alice chỉ có một đầu ra trao đổi và Bob có hai đầu ra.



![image](assets/fr/01.webp)



Ngay cả khi người quan sát bên ngoài có thể xác định được paterne của giao dịch Stonewall x2, anh ta cũng sẽ không có đầy đủ thông tin. Anh ta sẽ không thể xác định được UTXO nào trong hai UTXO có cùng số tiền tương ứng với khoản thanh toán. Anh ta cũng không thể xác định được Alice hay Bob đã thực hiện thanh toán. Cuối cùng, anh ta sẽ không thể xác định được liệu hai UTXO đã nhập có phải từ hai người khác nhau hay chúng thuộc về một người duy nhất đã hợp nhất chúng. Điểm cuối cùng này là do thực tế là các giao dịch Stonewall cổ điển, được thảo luận ở trên, tuân theo chính xác paterne giống như các giao dịch Stonewall x2. Nhìn từ bên ngoài và không có thông tin ngữ cảnh bổ sung, không thể phân biệt giao dịch Stonewall với giao dịch Stonewall x2. Các giao dịch trước không phải là giao dịch cộng tác, trong khi các giao dịch sau thì có. Điều này càng làm tăng thêm nghi ngờ về chi phí.



![image](assets/fr/05.webp)




## Làm thế nào để thiết lập kết nối giữa Paynyms?



Giống như các giao dịch cộng tác khác trên Ashigaru (*Cahoots*), Stonewall x2 bao gồm việc trao đổi các giao dịch đã được ký một phần giữa người gửi và người cộng tác. Việc trao đổi này có thể được thực hiện thủ công nếu bạn có mặt trực tiếp với người cộng tác, hoặc tự động sử dụng giao thức giao tiếp Soroban.



Nếu bạn chọn tùy chọn thứ hai, bạn sẽ cần thiết lập kết nối giữa các Paynym trước khi có thể thực hiện Stonewall x2. Để làm điều này, Paynym của bạn phải "*theo dõi*" Paynym của cộng tác viên, và ngược lại. Để tìm hiểu cách thực hiện, bạn có thể làm theo phần đầu của hướng dẫn khác này:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## Làm thế nào để thực hiện giao dịch Stonewall x2 trên Ashigaru?



Để thực hiện giao dịch Stonewall x2, hãy nhấp vào hình ảnh Paynym của bạn ở góc trên bên trái màn hình, sau đó mở menu `Cộng tác`. Người tham gia giao dịch với bạn cũng phải làm như vậy, trừ khi bạn trao đổi mã QR trực tiếp.



![Image](assets/fr/06.webp)



Bạn có hai lựa chọn: chọn `Khởi tạo` nếu bạn là người gửi thanh toán hoặc `Tham gia` nếu bạn là người cộng tác trong giao dịch nhưng không phải là người trả tiền hoặc người nhận thực tế.



![Image](assets/fr/07.webp)



Nếu bạn là cộng tác viên, quy trình rất đơn giản. Để cộng tác từ xa qua mạng Soroban, hãy nhấp vào `Tham gia`, chọn tài khoản bạn muốn sử dụng, sau đó nhấn `LISTEN FOR CAHOOTS REQUESTS` để chờ yêu cầu từ người trả tiền.



![Image](assets/fr/08.webp)



Mặt khác, để cộng tác trực tiếp thông qua quét mã QR, hãy vào trang chủ của wallet, nhấn vào biểu tượng mã QR ở đầu màn hình, sau đó quét mã QR do người thanh toán cung cấp khi thực hiện giao dịch.



![Image](assets/fr/09.webp)



Nếu bạn là người thanh toán, tức là người khởi tạo giao dịch, hãy vào menu `Cộng tác`, sau đó chọn `Khởi tạo`.



![Image](assets/fr/10.webp)



Đối với loại giao dịch, vì chúng ta muốn thực hiện Stonewall x2, hãy chọn tùy chọn này.



![Image](assets/fr/11.webp)



Sau đó, bạn có thể chọn giữa hình thức cộng tác trực tuyến (*Cahoots* thông qua *Soroban*) hoặc cộng tác trực tiếp bằng cách trao đổi mã QR.



![Image](assets/fr/12.webp)



### Thông đồng trực tuyến



Nếu bạn chọn tùy chọn `Trực tuyến`, hãy chọn cộng tác viên của bạn từ Paynym mà bạn đang theo dõi.



![Image](assets/fr/13.webp)



Nhấp vào `Thiết lập giao dịch`, sau đó chọn tài khoản mà bạn muốn thực hiện chi tiêu.



![Image](assets/fr/14.webp)



Ở trang tiếp theo, hãy nhập thông tin chi tiết giao dịch: địa chỉ người nhận thực tế, số tiền cần gửi và mức phí. Sau đó, nhấp vào `Xem lại thiết lập giao dịch`.



![Image](assets/fr/15.webp)



Kiểm tra thông tin cẩn thận, đảm bảo cộng tác viên của bạn đang lắng nghe yêu cầu *Cahoots*, sau đó nhấp vào nút `BEGIN TRANSACTION` màu xanh lá cây để bắt đầu trao đổi PSBT qua Soroban.



![Image](assets/fr/16.webp)



Chờ cho đến khi cả hai bên tham gia đều ký giao dịch, sau đó phát sóng giao dịch đó trên mạng Bitcoin.



![Image](assets/fr/17.webp)



### Thảo luận trực tiếp



Nếu bạn muốn thực hiện giao dịch trực tiếp, hãy chọn loại giao dịch `STONEWALL X2`, sau đó chọn tùy chọn `Trực tiếp/Thủ công`.



![Image](assets/fr/18.webp)



Nhấp vào `Thiết lập giao dịch`, sau đó chọn tài khoản mà bạn muốn thực hiện chi tiêu.



![Image](assets/fr/19.webp)



Ở trang tiếp theo, hãy nhập thông tin chi tiết giao dịch: địa chỉ người nhận thực tế, số tiền cần gửi và mức phí. Sau đó, nhấp vào `Xem lại thiết lập giao dịch`.



![Image](assets/fr/20.webp)



Kiểm tra thông tin chi tiết, sau đó nhấn nút `BEGIN TRANSACTION` màu xanh lá cây để bắt đầu trao đổi PSBT thông qua quét mã QR.



![Image](assets/fr/21.webp)



Việc trao đổi được thực hiện bằng cách luân phiên quét mã QR với cộng tác viên: nhấp vào `HIỂN THỊ MÃ QR` để hiển thị mã QR của bạn cho cộng tác viên, người này sẽ quét mã. Sau đó, họ sẽ nhấp vào `HIỂN THỊ MÃ QR` để hiển thị mã QR của họ, và bạn sẽ quét mã bằng `LAUNCH QR Scanner`. Lặp lại quy trình này cho đến khi hoàn tất cả năm bước trao đổi.



![Image](assets/fr/22.webp)



Sau khi hoàn tất mọi giao dịch, hãy kiểm tra thông tin chi tiết về giao dịch, sau đó phát hành giao dịch bằng cách kéo mũi tên màu xanh lá cây ở cuối màn hình.



![Image](assets/fr/23.webp)



[Giao dịch đã được công bố](https://mempool.space/testnet4/tx/9082f3d989728aacd290535a1ac374ab8c04a241a1d798b378db626dabea7a24). Cấu trúc của giao dịch như sau:



![Image](assets/fr/24.webp)



*Nguồn: [mempool.space](https://mempool.space/)*



Chúng ta có thể quan sát hai đầu vào từ danh mục đầu tư của tôi, tương ứng là `91.869 sats` và `64.823 sats`, trong khi hai đầu vào còn lại đến từ wallet của cộng tác viên của tôi. Về phía đầu ra, một UTXO là `100.000 sats` được gửi đến người thụ hưởng thực tế và hai UTXO là `100.000 sats` và `159.578 sats` trả về danh mục đầu tư của cộng tác viên của tôi. Đối với anh ta, hoạt động này là trung lập, vì anh ta thu hồi toàn bộ số tiền mà anh ta đã đầu tư vào đầu vào (không bao gồm chi phí mining mà anh ta đã đóng góp). Cuối cùng, tôi nhận được một UTXO trao đổi là `56.270 sats`, tương ứng với sự chênh lệch giữa tổng số đầu vào của tôi và khoản thanh toán `100.000 sats` được gửi cho người nhận.



Rõ ràng là tôi có thể mô tả cấu trúc này vì tôi đã tự mình xây dựng giao dịch. Nhưng đối với người quan sát bên ngoài, nhìn chung không thể xác định được UTXO nào thuộc về bên tham gia nào, dù là đầu vào hay đầu ra.



Để hiểu sâu hơn về quản lý quyền riêng tư trên chuỗi khối trên Bitcoin, tôi khuyên bạn nên tham gia khóa đào tạo BTC 204 của tôi trên Plan ₿ Academy:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c