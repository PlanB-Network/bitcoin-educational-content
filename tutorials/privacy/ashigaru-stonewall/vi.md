---
name: Ashigaru - Stonewall
description: Hiểu và sử dụng giao dịch Stonewall trên Ashigaru
---
![cover stonewall](assets/cover.webp)



> *Phá vỡ các giả định của phân tích blockchain bằng sự nghi ngờ có thể chứng minh bằng toán học giữa người gửi và người nhận giao dịch của bạn.*

## Giao dịch Stonewall là gì?



Stonewall là một hình thức giao dịch Bitcoin đặc biệt được thiết kế để tăng cường tính bảo mật của người dùng khi chi tiêu bằng cách mô phỏng một giao dịch coinjoin giữa hai người, mà không thực sự là một. Trên thực tế, giao dịch này không mang tính cộng tác. Người dùng có thể tự xây dựng giao dịch này, chỉ sử dụng UTXO mà họ sở hữu làm đầu vào. Vì vậy, bạn có thể tạo giao dịch Stonewall cho bất kỳ dịp nào mà không cần phải đồng bộ hóa với người dùng khác.



Giao dịch Stonewall hoạt động như sau: đầu vào của giao dịch là 2 UTXO thuộc về bên phát hành. Về đầu ra, giao dịch tạo ra 4 đầu ra, trong đó 2 đầu ra có cùng số tiền. 2 đầu ra còn lại sẽ là ngoại tệ. Trong số 2 đầu ra có cùng số tiền, chỉ có một đầu ra thực sự được chuyển đến người thụ hưởng.



Vì vậy, chỉ có 2 vai trò trong giao dịch Stonewall:




- Người phát hành, người thực hiện thanh toán thực tế;
- Người nhận có thể không biết bản chất cụ thể của giao dịch và chỉ mong đợi người gửi thanh toán.



Hãy lấy một ví dụ để hiểu cấu trúc giao dịch này. Alice đến tiệm bánh để mua bánh mì baguette của cô ấy, với giá 4.000 sats. Cô ấy muốn thanh toán bằng bitcoin, đồng thời vẫn giữ bí mật về khoản thanh toán của mình. Vì vậy, cô ấy quyết định xây dựng một giao dịch Stonewall cho khoản thanh toán này.



![image](assets/fr/01.webp)



Qua phân tích giao dịch này, chúng ta có thể thấy rằng người thợ làm bánh thực sự đã nhận được 4.000 sats để thanh toán cho chiếc bánh mì baguette. Alice đã sử dụng 2 UTXO làm đầu vào: một là 10.000 sats và một là 15.000 sats. Về đầu ra, nó đã thu hồi được 3 UTXO: một là 4.000 sats, một là 6.000 sats và một là 11.000 sats. Do đó, Alice có số dư ròng là 4.000 sats trong giao dịch này, tương ứng với giá của chiếc bánh mì baguette.



Trong ví dụ này, tôi cố tình bỏ qua phí mining để dễ hiểu hơn. Trên thực tế, chi phí giao dịch hoàn toàn do bên phát hành chịu.



## Sự khác biệt giữa Stonewall và Stonewall x2 là gì?



Giao dịch Stonewall hoạt động giống hệt giao dịch StonewallX2, ngoại trừ việc giao dịch StonewallX2 yêu cầu sự hợp tác, không giống như giao dịch Stonewall cổ điển, do đó có tên là "x2". Điều này là do giao dịch Stonewall được thực hiện mà không cần sự hợp tác bên ngoài: người gửi có thể thực hiện giao dịch mà không cần sự trợ giúp của người khác. Ngược lại, đối với giao dịch Stonewall x2, một người tham gia bổ sung, được gọi là "người cộng tác", sẽ tham gia vào quy trình. Người này đóng góp bitcoin của mình vào giao dịch, cùng với bitcoin của người gửi, và nhận toàn bộ số tiền sau khi giao dịch kết thúc (modulo chi phí mining).



Quay lại ví dụ với Alice tại tiệm bánh. Nếu muốn thực hiện giao dịch Stonewall x2, Alice sẽ phải hợp tác với Bob (bên thứ ba) khi thiết lập giao dịch. Mỗi bên sẽ mang theo một UTXO. Sau đó, Bob sẽ nhận lại toàn bộ số tiền đóng góp. Người thợ làm bánh sẽ nhận được khoản thanh toán cho chiếc bánh mì baguette của mình theo cách tương tự như trong giao dịch Stonewall, trong khi Alice sẽ lấy lại được số dư ban đầu, trừ đi giá trị của chiếc bánh mì baguette.



![image](assets/fr/02.webp)



Theo quan điểm của người ngoài cuộc, giao dịch vẫn sẽ diễn ra như cũ.



![image](assets/fr/03.webp)



Tóm lại, giao dịch Stonewall và Stonewall x2 có cấu trúc giống hệt nhau. Sự khác biệt giữa hai giao dịch này nằm ở bản chất hợp tác hoặc không hợp tác. Giao dịch Stonewall được phát triển riêng lẻ, không cần sự hợp tác. Mặt khác, giao dịch Stonewall x2 dựa trên sự hợp tác giữa hai cá nhân để thiết lập.



[**-> Tìm hiểu thêm về giao dịch Stonewall x2**](https://planb.academy/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)



## Mục đích của giao dịch Stonewall là gì?



Cấu trúc Stonewall bổ sung một lượng entropy khổng lồ vào giao dịch, làm mờ ranh giới của phân tích chuỗi. Nhìn từ bên ngoài, một giao dịch như vậy có thể được hiểu là một giao dịch nhỏ giữa hai người. Nhưng trên thực tế, giống như giao dịch Stonewall x2, nó là một khoản thanh toán. Do đó, phương pháp này tạo ra sự không chắc chắn trong phân tích chuỗi, hoặc thậm chí dẫn đến những kết quả sai lệch.



Hãy lấy ví dụ về Alice tại tiệm bánh. Giao dịch trên blockchain sẽ như thế này:



![image](assets/fr/04.webp)



Một người quan sát bên ngoài dựa vào phương pháp phân tích chuỗi thông thường có thể kết luận sai rằng "**hai người đã thực hiện một lệnh ghép nhỏ, với một UTXO làm đầu vào và hai UTXO làm đầu ra cho mỗi người**".



![image](assets/fr/05.webp)



Giải thích này không chính xác, vì như bạn đã biết, một UTXO đã được gửi đến thợ làm bánh, 2 UTXO đến từ Alice và cô ấy đã thu hồi được 3 đầu ra tỷ giá hối đoái.



![image](assets/fr/01.webp)



Ngay cả khi người quan sát bên ngoài có thể xác định được người tạo ra giao dịch Stonewall, anh ta cũng không có đầy đủ thông tin. Anh ta sẽ không thể xác định được UTXO nào trong hai UTXO có cùng số tiền tương ứng với khoản thanh toán. Ngoài ra, anh ta cũng không thể xác định liệu hai UTXO được nhập có phải từ hai người khác nhau hay thuộc về một người duy nhất đã hợp nhất chúng. Điểm cuối cùng này là do thực tế là các giao dịch Stonewall x2, được đề cập ở trên, tuân theo cùng một mô hình như các giao dịch Stonewall. Nhìn từ bên ngoài và không có thông tin ngữ cảnh bổ sung, không thể phân biệt được sự khác biệt giữa giao dịch Stonewall và giao dịch Stonewall x2. Giao dịch Stonewall không phải là giao dịch hợp tác, trong khi giao dịch Stonewall x2 thì có. Điều này càng làm tăng thêm nghi ngờ về chi phí.



![image](assets/fr/03.webp)



## Làm thế nào để thực hiện giao dịch Stonewall trên Ashigaru?



Ban đầu được phát triển bởi nhóm Samourai Wallet, các giao dịch Stonewall đã được tiếp quản bởi ứng dụng Ashigaru, một phiên bản fork của wallet gốc được tạo ra sau khi các nhà phát triển Samourai bị bắt. Bạn sẽ cần cài đặt Ashigaru và tạo một wallet:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Không giống như giao dịch Stowaway hoặc Stonewall x2 (*cahoots*), giao dịch Stonewall không yêu cầu sử dụng Paynyms. Chúng có thể được thực hiện trực tiếp, không cần chuẩn bị trước hoặc hợp tác với người dùng khác.



Trên thực tế, bạn không thực sự cần hướng dẫn để thực hiện giao dịch Stonewall, vì Ashigaru sẽ tự động tạo giao dịch này mỗi khi bạn chi tiêu, ngay khi wallet của bạn chứa đủ UTXO.



Nhấp vào nút `+` ở góc dưới bên phải màn hình, sau đó chọn `Gửi`.



![Image](assets/fr/06.webp)



Chọn tài khoản mà bạn muốn thực hiện chi tiêu.



![Image](assets/fr/07.webp)



Sau đó nhập thông tin giao dịch: địa chỉ người nhận và số tiền cần gửi, rồi nhấn mũi tên để xác nhận.



![Image](assets/fr/08.webp)



Tại đây, tất nhiên bạn có thể điều chỉnh phí giao dịch mặc định theo điều kiện thị trường. Tuy nhiên, yếu tố thú vị nhất trên trang này là loại giao dịch. Bạn sẽ thấy Ashigaru đã tự động chọn `STONEWALL`. Nhấp vào nút `PREVIEW` để tìm hiểu thêm.



![Image](assets/fr/09.webp)



Bạn có thể thấy rằng giao dịch này thực sự thuộc loại Stonewall: nó bao gồm 2 đầu vào có cùng số tiền, 2 đầu ra có cùng số tiền, cũng như đầu ra trao đổi và, trong trường hợp của tôi, một đầu vào bổ sung để đáp ứng tổng số tiền thanh toán.



![Image](assets/fr/10.webp)



Nếu bạn không muốn thực hiện giao dịch Stonewall mà muốn thanh toán theo cách thông thường, hãy nhấp vào biểu tượng bút chì ở góc trên bên phải màn hình, sau đó chọn `Simple` thay vì `STONEWALL`.



![Image](assets/fr/11.webp)



Sau khi đã kiểm tra mọi thông tin chi tiết, hãy kéo mũi tên màu xanh lá cây ở cuối màn hình để ký và hoàn tất giao dịch.



![Image](assets/fr/12.webp)



Bây giờ bạn đã biết cách thực hiện giao dịch Stonewall, và quan trọng hơn là cách thức hoạt động của nó. Nếu bạn muốn tìm hiểu thêm, hãy xem hướng dẫn của tôi về Ashigaru Terminal, trong đó giải thích cách thực hiện coinjoin qua Whirlpool.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add