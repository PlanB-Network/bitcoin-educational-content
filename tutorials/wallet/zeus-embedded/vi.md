---
name: Zeus Embedded
description: Cách sử dụng Lightning Zeus Embedded Wallet
---
![cover-zeus-embedded](assets/cover.webp)



ZEUS ban đầu là một ứng dụng di động để quản lý từ xa các nút sét, cho phép bạn kiểm soát nút của mình được cài đặt trên máy chủ từ xa


Nhưng ứng dụng này cũng có tính năng "Nút nhúng".



**Đây là khía cạnh của ứng dụng mà chúng ta sẽ khám phá trong hướng dẫn này.** Điều này cho phép bất kỳ ai cũng có nút sét riêng trên thiết bị di động, mà không cần máy chủ chuyên dụng, giống như cách ACINQ cung cấp Wallet Lightning Phoenix đáng kinh ngạc của mình.



https://planb.network/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

*Xin nhắc lại, Lightning là một mạng lưới hoạt động song song với Bitcoin, cho phép trao đổi bitcoin mà không cần phải thực hiện các giao dịch On-Chain một cách có hệ thống. Kết quả là các giao dịch gần như ngay lập tức, không cần phải đợi 10 phút để một khối được xác thực. Điều này đặc biệt hữu ích khi thanh toán cho một thương gia trong thế giới thực. Hơn nữa, Lightning cung cấp mức độ **bảo mật** đáng chú ý mà mạng lưới Bitcoin không có*.



**Zeus "Integrated"** hướng đến những người dùng Bitcoin muốn tối đa hóa quyền riêng tư và quyền tự chủ của mình.


Tóm lại, nó **có khả năng** là chiếc Wallet di động trong mơ của những người theo chủ nghĩa cypherpunk. Mặc dù nó vẫn còn trong giai đoạn trứng nước (phiên bản alpha) và có một vài lỗi, nhưng các tính năng của nó thì vô số, và không nghi ngờ gì nữa, nó sẽ làm hài lòng những người gan dạ nhất trong số chúng ta, những người muốn có khả năng kiểm soát và tùy chọn tối đa.



Mặt khác, tôi không nghĩ rằng hiện tại nó phù hợp với những người mới bắt đầu không quen với Bitcoin và chỉ muốn có một cách đơn giản để gửi/nhận satoshi. Mặc dù điều này có thể thay đổi trong tương lai, vì tính năng lưu ký thông qua giao thức Cashu (chaumian Ecash) đang được triển khai cho người mới bắt đầu...



## Cài đặt ứng dụng



Truy cập [trang web của dự án](https://zeusln.com/) để tải xuống ứng dụng cho hệ điều hành điện thoại thông minh của bạn:



![image](assets/fr/01.webp)



![image](assets/fr/02.webp)



## Tạo danh mục đầu tư



Sau khi ứng dụng khởi động, hãy nhấp vào nút "Khởi động nhanh" để bắt đầu tạo Wallet.



![image](assets/fr/03.webp)





Sau đó, một loạt màn hình khởi tạo sẽ xuất hiện. Đợi một lúc, sau đó đợi thêm vài phút nữa cho đến khi nút được đồng bộ hóa 100% qua Neutrino.



Việc này có thể mất vài phút. Đối với thông tin, neutrino là cách để ví di động truy cập thông tin Blockchain Bitcoin mà không cần phải chạy Full node.



![image](assets/fr/04.webp)





Sau vài phút, bạn đã sẵn sàng.



![image](assets/fr/05.webp)




## Thiết lập ứng dụng



Sẵn sàng, nhưng chưa hẳn, vì không cần phải nói rằng một người dùng Zeus xứng đáng với cái tên này sẽ điều khiển Wallet của mình một cách đẳng cấp và phong cách. Vì vậy, chúng ta sẽ phải thay đổi hình đại diện của anh ta.



Nhấp vào ảnh đại diện của bạn ở góc trên bên phải màn hình:



![image](assets/fr/06.webp)





Nhấp vào bánh răng, sau đó nhấp vào dấu cộng "+":



![image](assets/fr/07.webp)





Chọn bức ảnh đẹp nhất của Zeus để đại diện cho Wallet này và nhấp vào "CHỌN ẢNH" ở cuối màn hình, sau đó quay lại bằng cách nhấp vào mũi tên ở góc trên bên phải.



![image](assets/fr/08.webp)





Cuối cùng, đặt biệt danh cho Wallet của bạn và nhấp vào "LƯU CẤU HÌNH Wallet" để thay đổi có hiệu lực. Cuối cùng, nhấp vào mũi tên quay lại ở góc trên bên trái để trở về màn hình chính.



![image](assets/fr/09.webp)





Lần này chúng ta thực sự có thể bắt đầu.



![image](assets/fr/10.webp)



### Sinh trắc học



Để bảo vệ quyền truy cập vào Wallet, bạn có thể thêm mã PIN/mật khẩu và kích hoạt sinh trắc học.



Để thực hiện việc này, hãy vào menu chính của Wallet bằng cách nhấp vào dấu gạch ngang ở góc trên bên trái.



![image](assets/fr/11.webp)





Chọn "Cài đặt", sau đó chọn "Bảo mật" và cuối cùng là "Đặt/Đổi mã PIN".



![image](assets/fr/12.webp)





Tạo mã PIN, xác nhận và kích hoạt sinh trắc học bằng cách nhấn nút "Sinh trắc học" tương ứng. Quay lại menu chính bằng cách sử dụng mũi tên ở trên cùng bên trái.



![image](assets/fr/13.webp)




### Lưu cụm từ Mnemonic



Khi bạn quay lại menu chính, hãy nhấp vào "Sao lưu Wallet", sau đó đọc văn bản cảnh báo thông báo cho bạn rằng việc mất 24 từ mà bạn sắp nhận được cũng giống như mất quyền truy cập vào tiền của bạn và bất kỳ ai có những từ này ngoài bạn đều có thể truy cập vào tiền của bạn. Không bao giờ đưa chúng cho bất kỳ ai.



Chọn "TÔI HIỂU" ở cuối màn hình. Sau đó nhấp vào từng từ trong số 24 từ để hiển thị chúng và ghi chú cẩn thận.



Bạn có thể viết nó trên giấy, hoặc có lẽ, để tăng thêm tính bảo mật, hãy khắc nó trên thép không gỉ để bảo vệ nó khỏi hỏa hoạn, lũ lụt hoặc sụp đổ. Lựa chọn phương tiện cho Mnemonic của bạn sẽ phụ thuộc vào chiến lược bảo mật của bạn, nhưng nếu bạn đang sử dụng Zeus như một danh mục chi tiêu có số lượng vừa phải, thì giấy sẽ là đủ.



Để biết thêm thông tin về cách lưu và quản lý cụm từ Mnemonic đúng cách, tôi thực sự khuyên bạn nên làm theo hướng dẫn khác này, đặc biệt nếu bạn là người mới bắt đầu:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![image](assets/fr/14.webp)



Khi hoàn tất, hãy nhấp vào "TÔI ĐÃ SAO LƯU 24 TỪ" ở cuối màn hình và chúng ta sẽ trở lại màn hình chính, sẵn sàng nhận những bitcoin đầu tiên.




## Tùy chọn 1 - Nhận bitcoin On-Chain và mở kênh Lightning



**Zeus Embedded** chủ yếu được thiết kế như một nút sét nhúng, nhưng nó cũng có thể được sử dụng như Wallet On-Chain.



Để nhận bitcoin On-Chain, hãy nhấp vào nút "On-Chain" rồi nhấp vào "Nhận".


Cuối cùng, quét mã QR hoặc sao chép Bitcoin Address để gửi tiền.



![image](assets/fr/15.webp)





Sau khi tiền đã được xác nhận và ghi có vào Wallet của bạn, bạn có thể sử dụng chúng để mở **Kênh Lightning**. Kênh Lightning của bạn là cổng vào Lightning Network, cho phép bạn Exchange bitcoin theo cách bảo mật và nhanh chóng hơn nhiều.





- Để thực hiện, hãy nhấp vào "DI CHUYỂN QUỸ On-Chain ĐẾN LIGHTNING"



Trên màn hình tiếp theo, bạn được yêu cầu mở một kênh hợp tác với **"Olympus by Zeus"**, LSP (Nhà cung cấp dịch vụ Lightning) được Wallet ưa chuộng.


Trong hướng dẫn này, chúng ta sẽ chọn tùy chọn này vì mục đích đơn giản, nhưng hoàn toàn có thể mở kênh với bất kỳ nút nào trên mạng.


Thậm chí có thể mở nhiều kênh trong một giao dịch duy nhất bằng cách chọn "MỞ KÊNH BỔ SUNG". *Nhưng chúng ta sẽ xem xét điều này trong phiên bản "nâng cao" của hướng dẫn* **Zeus Embedded**.





- Sau đó chọn số tiền bạn muốn dành cho kênh này. Trong trường hợp của chúng tôi, tất cả các quỹ On-Chain của chúng tôi sẽ được sử dụng, vì vậy chúng tôi kích hoạt nút "Sử dụng tất cả các quỹ có thể".





- Cuối cùng, chọn nút "MỞ KÊNH" ở cuối màn hình.



![image](assets/fr/16.webp)





Trong vòng vài giây, kênh được thiết lập và chúng tôi đã sẵn sàng thực hiện giao dịch Lightning đầu tiên. Trên màn hình chính, chúng tôi có thể thấy một chiếc đồng hồ nhỏ bên cạnh số dư Wallet của mình. Điều này là do chúng tôi vẫn cần phải đợi 3 xác nhận On-Chain trước khi kênh thực sự hoạt động.



![image](assets/fr/17.webp)





Sau 3 lần xác nhận, chúng tôi nhận thấy số dư của mình hiện đã được ghi có vào thẻ Lightning.



![image](assets/fr/18.webp)



Một điểm chi tiết nhỏ: khi chúng ta nhấp vào menu ở cuối màn hình để xem trạng thái kênh Lightning, chúng ta thấy rằng một phần nhỏ số dư của chúng ta không khả dụng để chi tiêu: chúng ta chỉ có thể chi tiêu 208253 satoshi thay vì 210370 satoshi mà chúng ta thực sự có. Điều này là bình thường vì nó dành riêng cho giao thức Lightning.



Cuối cùng, cần lưu ý rằng đối tác Olympus của chúng tôi có quyền đóng kênh theo quyết định riêng của mình, ví dụ như nếu kênh không được sử dụng. Để đảm bảo kênh của chúng tôi được duy trì, chúng tôi sẽ phải trả cho LSP (Nhà cung cấp dịch vụ Lightning), như chúng ta sẽ thấy trong đoạn tiếp theo, thông qua cách mở kênh thứ 2.





## Gửi bitcoin qua Lightning



Bây giờ kênh của chúng ta đã hoạt động, hãy xem cách chúng ta có thể sử dụng nó để trả tiền sét Invoice (Invoice).



Để thực hiện việc này, hãy nhấp vào nút "Lightning", sau đó nhấp vào "Gửi".



![image](assets/fr/19.webp)





Trên màn hình tiếp theo, sao chép Invoice của bạn vào trường chuyên dụng hoặc quét bằng cách nhấp vào biểu tượng ở góc trên bên phải. Cuối cùng, trượt nút "Trượt để thanh toán" sang phải để thanh toán.



![image](assets/fr/20.webp)






Đợi vài giây và Invoice sẽ được thanh toán và số satoshi của bạn sẽ di chuyển với tốc độ ánh sáng.



![image](assets/fr/21.webp)





Zeus sau đó cho phép bạn thêm ghi chú để ghi giá trị thanh toán của bạn hoặc xem lộ trình mà satoshi của bạn đã đi trước khi đến đích (và các khoản phí do tất cả các nút trung gian tính). Đây là loại chức năng mà chúng tôi yêu thích ở Wallet.



![image](assets/fr/22.webp)



Lưu ý rằng không giống như Wallet như [Phoenix]([Plan ₿ Network - Phoenix](https://planb.network/fr/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf)), với Zeus, tuyến đường được tính toán cục bộ và không được chuyển giao cho bên thứ ba (ACINQ trong trường hợp của Phoenix). Vì vậy, bạn là người duy nhất biết người nhận thanh toán. Chúng tôi mất một chút hiệu quả (thanh toán mất nhiều thời gian hơn một chút để hoàn tất, nhưng chúng tôi đạt được rất nhiều về mặt quyền riêng tư).





Bằng cách nhấp vào mũi tên nhỏ ở cuối màn hình chính, bạn cũng có thể xem lịch sử thanh toán của chúng tôi. Ở đây chúng ta thấy trong Green là 212.121 Sats nhận được cho On-Chain, sau đó là màu đỏ tương ứng là 211.756 Sats được sử dụng để mở kênh của chúng tôi, sau đó là 121.212 satoshi được sử dụng để thanh toán cho Invoice lightning của chúng tôi.



![image](assets/fr/23.webp)





## Tùy chọn 2 - Nhận bitcoin trực tiếp trên Lightning



Thay vì mở kênh theo cách thủ công như chúng ta vừa thấy, bạn có thể nhận tiền trực tiếp qua Lightning, ngay cả khi không có kênh nào tồn tại trước đó, bằng cách sử dụng Olympus, Zeus LSP.




- Để thực hiện việc này, hãy nhấp vào nút "Lightning" trên màn hình chính, sau đó nhấp vào "Receive".
- Sau đó chọn số tiền bạn muốn nhận trong ô "Số tiền" và chọn nút "TẠO Invoice" ở cuối màn hình.



![image](assets/fr/24.webp)





Màn hình tiếp theo hiển thị Invoice phải trả để nhận satoshi. Chúng tôi được thông báo rằng LSP sẽ giữ lại 10.000 Sats nếu thanh toán bằng Lightning. Chúng ta sẽ xem sau cách tính phí mở kênh này.



Trả Invoice hoặc nhờ người khác trả, kênh sẽ tự động được mở nhưng sẽ trừ 10.000 Sats theo thỏa thuận.



![image](assets/fr/25.webp)





Bây giờ chúng ta đang ở đầu 2 kênh Lightning, trạng thái của chúng có thể được kiểm tra bằng cách nhấp vào nút được chỉ định bằng mũi tên màu trắng ở cuối màn hình chính.



Chúng ta có thể thấy rằng, không giống như kênh được mở từ thang đo On-Chain, kênh được mở trực tiếp qua tia sét không hiển thị cảnh báo nào.


Vì bạn đã trả tiền để thiết lập kênh này, Nhà cung cấp dịch vụ Lightning (LSP) cam kết duy trì kênh trong 3 tháng và cung cấp cho bạn "thanh khoản đến". Ở kênh dưới cùng, bạn có thể thấy khả năng tiếp nhận là 96383 satoshi. Do đó, LSP đã ràng buộc vốn để cho phép bạn nhận thanh toán trực tiếp sau khi mở kênh.



Vì vậy, số tiền phí 10.000 Satoshi được trả bao gồm: chi phí mở kênh đào (giao dịch Bitcoin On-Chain, bảo đảm duy trì kênh đào trong 3 tháng và khóa vốn).



![image](assets/fr/26.webp)





Xin chúc mừng, giờ bạn đã sẵn sàng sử dụng Zeus Embedded, hệ thống chiếu sáng di động Wallet có các tính năng tiên tiến nhất trên thị trường.





Để tìm hiểu thêm về hoạt động kỹ thuật của Lightning Network, bạn có thể tìm thấy khóa đào tạo Plan ₿ Network miễn phí tuyệt vời của Fanis Michalakis:



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb