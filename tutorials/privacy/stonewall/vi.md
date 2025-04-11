---
name: Stonewall
description: Hiểu và sử dụng giao dịch Stonewall
---
![cover stonewall](assets/cover.webp)

***CẢNH BÁO:** Sau vụ bắt giữ các nhà sáng lập của Samourai Wallet và việc tịch thu máy chủ của họ vào ngày 24 tháng 4, việc sử dụng ứng dụng Samourai Wallet hiện đòi hỏi phải kết nối với Dojo của riêng bạn để hoạt động đúng cách. Ngoài ra, giao dịch Stonewall không bị ảnh hưởng gì cả và vẫn có thể thực hiện mà không gặp bất kỳ vấn đề nào. Thực tế, các loại giao dịch này được thực hiện một cách tự động, không cần sự hợp tác bên ngoài hoặc kết nối qua Soroban.*

_Chúng tôi đang ch closely theo dõi các diễn biến của vụ việc này cũng như các phát triển liên quan đến các công cụ liên quan. Hãy yên tâm rằng chúng tôi sẽ cập nhật hướng dẫn này khi có thông tin mới._

_Hướng dẫn này được cung cấp chỉ cho mục đích giáo dục và thông tin. Chúng tôi không ủng hộ hoặc khuyến khích việc sử dụng các công cụ này cho mục đích phạm tội. Mỗi người dùng có trách nhiệm tuân thủ các luật pháp trong phạm vi quyền hạn của họ._

---

> *"Phá vỡ các giả định của phân tích blockchain với sự nghi ngờ có thể chứng minh được về mặt toán học giữa người gửi và người nhận trong giao dịch của bạn."*

## Giao dịch Stonewall là gì?
Stonewall là một dạng giao dịch Bitcoin cụ thể nhằm tăng cường quyền riêng tư cho người dùng trong quá trình giao dịch bằng cách mô phỏng một coinjoin giữa hai bên, mặc dù thực tế không phải là một. Trên thực tế, giao dịch này không phải là cộng tác. Một người dùng có thể tự mình xây dựng nó, chỉ sử dụng UTXOs của họ làm đầu vào. Do đó, bạn có thể tạo một giao dịch Stonewall cho bất kỳ dịp nào mà không cần phải phối hợp với người dùng khác.

Cách thức hoạt động của một giao dịch Stonewall như sau: làm đầu vào, người gửi sử dụng 2 UTXOs thuộc về họ. Làm đầu ra, giao dịch tạo ra 4 đầu ra, bao gồm 2 đầu ra có cùng một lượng chính xác. 2 đầu ra còn lại sẽ là tiền thối. Trong số 2 đầu ra có cùng số lượng, chỉ có một thực sự đi đến người nhận thanh toán.

Chỉ có 2 vai trò trong một giao dịch Stonewall:
- Người gửi, người thực hiện thanh toán thực sự;
- Người nhận, người có thể không biết về bản chất cụ thể của giao dịch và đơn giản là mong đợi một khoản thanh toán từ người gửi.

Hãy lấy một ví dụ để hiểu cấu trúc giao dịch này. Alice đang ở tiệm bánh để mua bánh mì baguette của mình, có giá `4,000 sats`. Cô ấy muốn thanh toán bằng bitcoin trong khi duy trì một mức độ quyền riêng tư nhất định trong thanh toán của mình. Do đó, cô ấy quyết định tạo một giao dịch Stonewall cho việc thanh toán.
![transaction stonewall bakery](assets/en/1.webp)
Phân tích giao dịch này, chúng ta có thể thấy rằng người bán bánh thực sự đã nhận được `4,000 sats` làm thanh toán cho chiếc bánh mì baguette. Alice đã sử dụng 2 UTXOs làm đầu vào: một của `10,000 sats` và một của `15,000 sats`. Làm đầu ra, cô ấy nhận được 3 UTXOs: một của `4,000 sats`, một của `6,000 sats`, và một của `11,000 sats`. Alice có một số dư ròng là `-4,000 sats` trong giao dịch này, tương ứng với giá của chiếc bánh mì baguette.

Trong ví dụ này, tôi cố ý bỏ qua phí khai thác để dễ hiểu hơn. Trên thực tế, phí giao dịch được người gửi thanh toán hoàn toàn.

## Sự khác biệt giữa Stonewall và Stonewall x2 là gì?
Giao dịch Stonewall hoạt động giống như giao dịch StonewallX2, với sự khác biệt duy nhất là giao dịch sau đòi hỏi sự hợp tác, không giống như giao dịch Stonewall cổ điển, do đó có tên gọi "x2". Thực sự, giao dịch Stonewall có thể được thực hiện mà không cần sự hợp tác bên ngoài: người gửi có thể thực hiện nó mà không cần sự giúp đỡ của người khác. Tuy nhiên, đối với một giao dịch Stonewall x2, một người tham gia bổ sung, được gọi là "người hợp tác", tham gia vào quá trình. Người hợp tác đóng góp bitcoin của họ như một đầu vào, cùng với những người của người gửi, và nhận toàn bộ số tiền như đầu ra (trừ phí khai thác).

Hãy xem lại ví dụ của chúng ta với Alice tại tiệm bánh. Nếu cô ấy muốn thực hiện một giao dịch Stonewall x2, Alice sẽ phải hợp tác với Bob (một bên thứ ba) khi tạo giao dịch. Họ mỗi người sẽ cung cấp một UTXO đầu vào. Sau đó, Bob sẽ nhận được toàn bộ số tiền của mình như đầu ra. Người bán bánh sẽ nhận được tiền thanh toán cho chiếc bánh mì của mình giống như trong giao dịch Stonewall, trong khi Alice sẽ nhận lại số dư ban đầu của mình, trừ chi phí của chiếc bánh mì.
![giao dịch stonewall x2](assets/en/2.webp)

Từ góc độ bên ngoài, mô hình của giao dịch sẽ giữ nguyên hoàn toàn.
![Stonewall hay Stonewall x2 ?](assets/en/3.webp)

Tóm lại, giao dịch Stonewall và Stonewall x2 chia sẻ một cấu trúc giống nhau. Sự khác biệt giữa hai loại nằm ở bản chất hợp tác của chúng. Giao dịch Stonewall được phát triển một cách độc lập, không cần sự hợp tác. Ngược lại, giao dịch Stonewall x2 dựa vào sự hợp tác giữa hai cá nhân để thực hiện.

[**-> Tìm hiểu thêm về giao dịch Stonewall x2**](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)

## Mục đích của giao dịch Stonewall là gì?
Cấu trúc Stonewall thêm một lượng lớn entropy vào giao dịch và làm mờ phân tích chuỗi. Từ góc độ bên ngoài, một giao dịch như vậy có thể được hiểu là một coinjoin nhỏ giữa hai người. Nhưng thực tế, giống như giao dịch Stonewall x2, đó là một khoản thanh toán. Phương pháp này do đó tạo ra sự không chắc chắn trong phân tích chuỗi, và thậm chí có thể dẫn đến những dấu hiệu sai lầm.

Hãy xem lại ví dụ của Alice tại tiệm bánh. Giao dịch trên blockchain sẽ xuất hiện như sau:
![Stonewall hay Stonewall x2 ?](assets/en/4.webp)
Một người quan sát bên ngoài dựa vào các phép suy luận phân tích chuỗi thông thường có thể nhầm lẫn kết luận rằng "*hai người đã thực hiện một coinjoin nhỏ, với mỗi người một UTXO làm đầu vào và hai UTXO làm đầu ra*".
![Stonewall hay Stonewall x2 ?](assets/en/5.webp)
Giải thích này không chính xác bởi vì, như bạn biết, một UTXO đã được gửi đến người bán bánh, 2 UTXO trong đầu vào đến từ Alice, và cô ấy nhận được 3 đầu ra thay đổi.

![giao dịch stonewall người bán bánh](assets/en/1.webp)
Dù một quan sát viên bên ngoài có thể xác định được mô hình của giao dịch Stonewall, họ sẽ không có đủ thông tin. Họ không thể xác định được UTXO nào trong hai UTXO có cùng số lượng tương ứng với khoản thanh toán. Hơn nữa, họ không thể xác định liệu hai UTXO trong đầu vào đến từ hai người khác nhau hay chúng thuộc về một người đã kết hợp chúng. Điểm cuối cùng này là do giao dịch Stonewall x2, mà chúng ta đã nói ở trên, tuân theo chính xác mô hình giống như giao dịch Stonewall. Từ bên ngoài và không có thông tin bổ sung về bối cảnh, không thể phân biệt được giao dịch Stonewall với giao dịch Stonewall x2. Tuy nhiên, giao dịch đầu tiên không phải là giao dịch hợp tác, trong khi giao dịch sau là. Điều này càng làm tăng thêm sự nghi ngờ về khoản chi này. ![Stonewall hay Stonewall x2?](assets/en/3.webp)
## Làm thế nào để thực hiện giao dịch Stonewall trên Samourai Wallet?
Khác với giao dịch Stowaway hoặc Stonewall x2 (cahoots), giao dịch Stonewall không yêu cầu sử dụng Paynyms. Nó có thể được thực hiện trực tiếp, không cần bất kỳ bước chuẩn bị nào. Để làm điều này, hãy theo dõi hướng dẫn video của chúng tôi trên Samourai Wallet:
![Hướng dẫn Stonewall - Samourai Wallet](https://youtu.be/mlRtZvWGuk0?si=e_lSKJLvybWUna1j)

## Làm thế nào để thực hiện giao dịch Stonewall trên Sparrow Wallet?
Khác với giao dịch Stowaway hoặc Stonewall x2 (cahoots), giao dịch Stonewall không yêu cầu sử dụng Paynyms. Nó có thể được thực hiện trực tiếp, không cần bất kỳ bước chuẩn bị nào. Để làm điều này, hãy theo dõi hướng dẫn video của chúng tôi trên Sparrow Wallet:
![Hướng dẫn Stonewall - Sparrow Wallet](https://youtu.be/su89ljkV_OI?si=1jNaSJGvECUYe6Or)

**Nguồn Tài Nguyên Bên Ngoài:**
- https://docs.samourai.io/en/spend-tools#stonewall.