---
name: Sparrow Wallet - Stonewall
description: Hiểu và sử dụng giao dịch Stonewall trên Sparrow
---

![cover](assets/cover.webp)




> *Phá vỡ các giả định của phân tích blockchain bằng sự nghi ngờ có thể chứng minh bằng toán học giữa người gửi và người nhận giao dịch của bạn.*

## Giao dịch Stonewall là gì?



Stonewall là một hình thức giao dịch Bitcoin đặc biệt được thiết kế để tăng cường tính bảo mật của người dùng khi chi tiêu bằng cách mô phỏng một giao dịch coinjoin giữa hai người, mà không thực sự là một. Trên thực tế, giao dịch này không mang tính cộng tác. Người dùng có thể tự xây dựng giao dịch, chỉ sử dụng UTXO thuộc sở hữu của mình làm đầu vào. Vì vậy, bạn có thể tạo giao dịch Stonewall cho bất kỳ dịp nào mà không cần phải đồng bộ hóa với người dùng khác.



Giao dịch Stonewall hoạt động như sau: đầu vào của giao dịch là 2 UTXO thuộc về bên phát hành. Về đầu ra, giao dịch tạo ra 4 đầu ra, trong đó 2 đầu ra có cùng số tiền. 2 đầu ra còn lại sẽ là ngoại tệ. Trong số 2 đầu ra có cùng số tiền, chỉ có một đầu ra thực sự được chuyển đến người thụ hưởng.



Vì vậy, chỉ có 2 vai trò trong giao dịch Stonewall:




- Người phát hành, người thực hiện thanh toán thực tế;
- Người nhận có thể không biết bản chất cụ thể của giao dịch và chỉ mong đợi người gửi thanh toán.



Hãy lấy một ví dụ để hiểu cấu trúc giao dịch này. Alice đến tiệm bánh để mua một ổ bánh mì baguette trị giá 4.000 sats. Cô ấy muốn thanh toán bằng bitcoin, đồng thời vẫn giữ bí mật về khoản thanh toán của mình. Vì vậy, cô ấy quyết định xây dựng một giao dịch Stonewall cho khoản thanh toán này.



![image](assets/fr/01.webp)



Phân tích giao dịch này, chúng ta có thể thấy rằng người thợ làm bánh thực sự đã nhận được `4.000 sats` tiền thanh toán cho bánh mì baguette. Alice đã sử dụng 2 UTXO làm đầu vào: một là `10.000 sats` và một là `15.000 sats`. Về đầu ra, nó đã thu hồi được 3 UTXO: một là `4.000 sats`, một là `6.000 sats` và một là `11.000 sats`. Do đó, Alice có số dư ròng là `- 4.000 sats` trong giao dịch này, tương ứng với giá của bánh mì baguette.



Trong ví dụ này, tôi cố tình bỏ qua phí mining để dễ hiểu hơn. Trên thực tế, chi phí giao dịch hoàn toàn do bên phát hành chịu.



## Sự khác biệt giữa Stonewall và Stonewall x2 là gì?



Giao dịch Stonewall hoạt động giống hệt giao dịch StonewallX2, ngoại trừ việc giao dịch StonewallX2 yêu cầu sự hợp tác, không giống như giao dịch Stonewall cổ điển, do đó có tên là "x2". Điều này là do giao dịch Stonewall được thực hiện mà không cần sự hợp tác bên ngoài: người gửi có thể thực hiện giao dịch mà không cần sự trợ giúp của người khác. Ngược lại, đối với giao dịch Stonewall x2, một người tham gia bổ sung, được gọi là "người cộng tác", sẽ tham gia vào quy trình. Người này đóng góp bitcoin của mình vào giao dịch, cùng với số bitcoin của người gửi, và nhận toàn bộ số tiền sau khi giao dịch kết thúc (trừ chi phí mining).



Quay lại ví dụ với Alice tại tiệm bánh. Nếu muốn thực hiện giao dịch Stonewall x2, Alice sẽ phải hợp tác với Bob (bên thứ ba) khi thiết lập giao dịch. Mỗi bên sẽ mang theo một UTXO. Sau đó, Bob sẽ nhận được toàn bộ số tiền đóng góp của mình khi thoát khỏi giao dịch. Người thợ làm bánh sẽ nhận được thanh toán cho ổ bánh mì baguette của mình theo cách tương tự như trong giao dịch Stonewall, trong khi Alice sẽ lấy lại được số dư ban đầu, trừ đi giá trị ổ bánh mì baguette.



![image](assets/fr/02.webp)



Theo quan điểm của người ngoài cuộc, giao dịch vẫn sẽ diễn ra như cũ.



![image](assets/fr/03.webp)



Tóm lại, giao dịch Stonewall và Stonewall x2 có cấu trúc giống hệt nhau. Sự khác biệt giữa hai giao dịch này nằm ở bản chất hợp tác hoặc không hợp tác. Giao dịch Stonewall được phát triển riêng lẻ, không cần sự hợp tác. Mặt khác, giao dịch Stonewall x2 dựa trên sự hợp tác giữa hai cá nhân để thiết lập.



[**-> Tìm hiểu thêm về giao dịch Stonewall x2**](https://planb.academy/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)



## Mục đích của giao dịch Stonewall là gì?



Cấu trúc Stonewall bổ sung một lượng entropy khổng lồ vào giao dịch, làm mờ ranh giới của phân tích chuỗi. Nhìn từ bên ngoài, một giao dịch như vậy có thể được hiểu là một giao dịch nhỏ giữa hai người. Nhưng trên thực tế, giống như giao dịch Stonewall x2, nó là một khoản thanh toán. Do đó, phương pháp này tạo ra sự không chắc chắn trong phân tích chuỗi, hoặc thậm chí dẫn đến những kết quả sai lệch.



Hãy lấy ví dụ về Alice tại tiệm bánh. Giao dịch trên blockchain sẽ như thế này:



![image](assets/fr/04.webp)



Một người quan sát bên ngoài dựa vào phương pháp phân tích chuỗi thông thường có thể kết luận sai rằng "*hai người đã thực hiện một lệnh ghép nhỏ, với một UTXO làm đầu vào và hai UTXO làm đầu ra cho mỗi người*".



![image](assets/fr/05.webp)



Giải thích này không chính xác, vì như bạn đã biết, một UTXO đã được gửi đến baker, 2 UTXO đến từ Alice và cô ấy đã khôi phục được 3 đầu ra trao đổi.



![image](assets/fr/01.webp)



Ngay cả khi người quan sát bên ngoài có thể xác định được người tạo ra giao dịch Stonewall, anh ta cũng sẽ không có đầy đủ thông tin. Anh ta sẽ không thể xác định được UTXO nào trong hai UTXO có cùng số tiền tương ứng với khoản thanh toán. Ngoài ra, anh ta sẽ không thể xác định liệu hai mục UTXO đến từ hai người khác nhau hay chúng thuộc về một người duy nhất đã hợp nhất chúng. Điểm cuối cùng này là do thực tế là các giao dịch Stonewall x2, được đề cập ở trên, tuân theo cùng một mô hình chính xác như các giao dịch Stonewall. Nhìn từ bên ngoài và không có thông tin ngữ cảnh bổ sung, không thể phân biệt được sự khác biệt giữa giao dịch Stonewall và giao dịch Stonewall x2. Giao dịch Stonewall không phải là giao dịch hợp tác, trong khi giao dịch Stonewall x2 thì có. Điều này càng làm tăng thêm nghi ngờ về chi phí.



![image](assets/fr/03.webp)



## Làm thế nào để thực hiện giao dịch Stonewall trên Sparrow?



Ban đầu được phát triển bởi nhóm Samurai Wallet, các giao dịch Stonewall đã được tiếp quản bởi ứng dụng Ashigaru, một fork trong danh mục đầu tư ban đầu được tạo ra sau khi các nhà phát triển Samurai bị bắt, và cũng trên Sparrow Wallet.



Bạn sẽ cần cài đặt Sparrow và tạo:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Không giống như giao dịch Stowaway hoặc Stonewall x2 (*cahoots*), giao dịch Stonewall không yêu cầu sử dụng Paynyms. Chúng có thể được thực hiện trực tiếp, không cần chuẩn bị đặc biệt hay hợp tác với người dùng khác.



Để thực hiện giao dịch Stonewall trên Sparrow, quy trình rất đơn giản: bắt đầu bằng cách tạo giao dịch như bình thường, thông qua menu `Gửi` hoặc từ menu `UTXOs` nếu bạn muốn thực hiện *Điều khiển Coin*.



![Image](assets/fr/06.webp)



Sau đó nhập thông tin chi tiết về giao dịch: địa chỉ người nhận, nhãn, số tiền cần gửi và số tiền hoặc mức phí, tùy thuộc vào điều kiện thị trường.



![Image](assets/fr/07.webp)



Trước khi xác nhận, đây là nơi bạn có thể chọn cấu trúc Stonewall. Ở cuối giao diện, hãy thay thế `Hiệu quả` bằng `Quyền riêng tư`. Nếu tùy chọn này không xuất hiện, điều đó có nghĩa là danh mục đầu tư của bạn không có đủ số lượng UTXO để xây dựng loại giao dịch này.



![Image](assets/fr/08.webp)



Sau khi chọn tùy chọn `Riêng tư`, bạn sẽ nhận thấy cấu trúc của giao dịch đã được thay đổi hoàn toàn: giao dịch này trở thành giao dịch Stonewall, sử dụng một số UTXO của bạn làm đầu vào và tạo ra hai đầu ra có số tiền giống hệt nhau, một trong số đó tương ứng với khoản thanh toán thực tế là `100.000 sats`, ngoài các đầu ra trao đổi.



![Image](assets/fr/09.webp)



Nếu mọi thứ đều chính xác, hãy nhấp vào `Tạo giao dịch`.



Sau đó, bạn có thể kiểm tra lại thông tin giao dịch lần cuối và nhấp vào `Hoàn tất giao dịch để ký`.



![Image](assets/fr/10.webp)



Sau đó, hãy ký giao dịch theo phương pháp cụ thể cho danh mục đầu tư của bạn và nhấp vào `Phát giao dịch` để phát trên mạng Bitcoin, chờ xác nhận.



![Image](assets/fr/11.webp)



Giờ đây, bạn đã biết cách giao dịch Stonewall hoạt động trên Sparrow Wallet và cách tạo một giao dịch như vậy. Để nâng cao kỹ năng sử dụng các công cụ được thiết kế để tăng cường bảo mật onchain, tôi mời bạn tham gia khóa đào tạo BTC 204 của tôi trên Plan ₿ Academy:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c