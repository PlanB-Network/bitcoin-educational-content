---
name: Ashigaru - Whirlpool Coinjoin
description: Làm thế nào để thực hiện coinjoin trên ứng dụng Ashigaru?
---

![cover](assets/cover.webp)



"*một chiếc Bitcoin wallet dành cho đường phố*"



Trong hướng dẫn này, bạn sẽ tìm hiểu coinjoin là gì và cách tạo coinjoin bằng ứng dụng Ashigaru Terminal và triển khai Whirlpool, một giao thức coinjoin được kế thừa từ Samourai Wallet.



## Cách thức hoạt động của khớp nối Whirlpool



Trong hướng dẫn này, tôi sẽ không nhắc lại khái niệm coinjoin, tính hữu ích của nó hay lý thuyết vận hành của Whirlpool, vì những chủ đề này đã được giải thích chi tiết trong Phần 5 của khóa đào tạo BTC 204 trên Plan ₿ Academy. Nếu bạn chưa nắm vững cách vận hành của Whirlpool hoặc nguyên lý của coinjoin, tôi thực sự khuyên bạn nên tham khảo phần 5 này trước khi tiếp tục:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Tuy nhiên, sau đây là một số thông tin và số liệu nhanh có thể hữu ích.



Danh mục đầu tư tương thích với Whirlpool sử dụng 4 tài khoản riêng biệt để đáp ứng nhu cầu của quy trình coinjoin:




- Tài khoản **Gửi tiền**, được xác định bằng chỉ mục `0'`;
- Tài khoản **Bad Bank** (hoặc *doxxic exchange*), được xác định bằng chỉ mục `2.147.483.644'`;
- Tài khoản **Premix**, được xác định bằng chỉ mục `2 147 483 645'`;
- Tài khoản **Postmix** được xác định bằng chỉ mục `2 147 483 646'`.



Vào tháng 11 năm 2025, trên Ashigaru, có hai mệnh giá tiền cược (danh sách này có thể sẽ thay đổi trong những tháng tới: vì vậy hãy nhớ kiểm tra giá trị khi bạn đọc):




- 0,25 BTC`, với phí tham gia là `0,0125 BTC`;
- 0,025 BTC, với phí tham gia là 0,00125 BTC.



Mỗi chu kỳ trộn có thể bao gồm từ 5 đến 10 UTXO ở đầu vào và đầu ra.



![Image](assets/fr/01.webp)



## Yêu cầu phần mềm



Để thực hiện coinjoin bằng Whirlpool, bạn sẽ cần ba chương trình riêng biệt:





- Ashigaru Terminal**, cho phép bạn quản lý coinjoin trực tiếp từ máy tính;



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add



- Ashigaru Wallet**, ứng dụng trên điện thoại thông minh mà bạn có thể sử dụng để chi tiêu bitcoin của mình trong *postmix* từ bất kỳ đâu;



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f



- Dojo**, một triển khai nút Bitcoin đảm bảo cho bạn kết nối an toàn với mạng, không phụ thuộc vào máy chủ của bên thứ ba.



https://planb.academy/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Cài đặt từng công cụ này bằng cách làm theo hướng dẫn tương ứng, sau đó bạn có thể bắt đầu tạo coinjoin đầu tiên.



## Nhận bitcoin



Sau khi tạo danh mục đầu tư, bạn sẽ bắt đầu với một tài khoản duy nhất, được xác định bằng chỉ số `0'`. Đây là tài khoản `Nạp tiền`. Bạn sẽ gửi bitcoin đến tài khoản này để tham gia coinjoin. Bạn có thể nhận chúng thông qua ứng dụng Ashigaru (xem phần 5 của hướng dẫn chuyên sâu) hoặc qua Ashigaru Terminal (cũng được trình bày chi tiết trong phần 5 của hướng dẫn chuyên sâu).



Khi tài khoản tiền gửi của bạn có ít nhất số tiền cần thiết để tham gia vào nhóm nhỏ nhất (cộng với phí dịch vụ và số tiền tối thiểu cần thiết để trang trải chi phí mining), bạn sẽ sẵn sàng thực hiện giao dịch coinjoin đầu tiên.



![Image](assets/fr/02.webp)



## Thực hiện Tx0



Sau khi tiền đã về tài khoản tiền gửi của bạn và giao dịch đã được xác nhận, bạn có thể bắt đầu quá trình coinjoin. Để thực hiện việc này, trên Ashigaru Terminal, hãy mở menu `Ví`, sau đó chọn wallet của bạn. Nếu wallet của bạn bị khóa, phần mềm sẽ yêu cầu bạn nhập mật khẩu và passphrase.



![Image](assets/fr/03.webp)



Sau đó chọn tài khoản `Gửi tiền`.



![Image](assets/fr/04.webp)



Vào menu `UTXOs`.



![Image](assets/fr/05.webp)



Tại đây, bạn sẽ thấy danh sách tất cả các UTXO trong tài khoản tiền gửi của mình. Chọn những UTXO bạn muốn gửi trong các chu kỳ coinjoin.



Để bảo mật hơn và tránh *Phương pháp tiếp cận Ownership đầu vào chung (CIOH)*, khuyến nghị chỉ sử dụng một UTXO cho mỗi đầu vào trong Whirlpool (có thể tìm thấy lời giải thích chi tiết về nguyên tắc này trong BTC 204).



Nhấn phím `ENTER` trên bàn phím để chọn UTXO: dấu hoa thị `(*)` sẽ xuất hiện bên cạnh để cho biết rằng phím này đã được chọn.



![Image](assets/fr/06.webp)



Sau đó nhấp vào nút `Trộn mục đã chọn`.



![Image](assets/fr/07.webp)



Nếu bạn có UTXO đủ lớn để tham gia vào một trong hai nhóm có sẵn, bạn có thể chọn nhóm đích bằng cách sử dụng các mũi tên. Trên trang này, bạn sẽ thấy chi tiết về Tx0 của mình:




- số lượng UTXO sẽ vào nhóm;
- các loại phí khác nhau được áp dụng (phí dịch vụ và phí mining);
- lượng *thay đổi doxxic*.



Kiểm tra thông tin cẩn thận, sau đó nhấp vào `Phát sóng` để phát Tx0.



![Image](assets/fr/08.webp)



Sau đó, Ashigaru sẽ hiển thị TXID của Tx0 của bạn, xác nhận rằng giao dịch đã được phát trên mạng.



![Image](assets/fr/09.webp)



## Tạo coinjoin



Sau khi Tx0 được phát đi, hãy quay lại trang chủ tài khoản tiền gửi của bạn, sau đó nhấp vào `Tài khoản` và chọn tài khoản `Premix`.



![Image](assets/fr/10.webp)



Trong menu `UTXOs`, bạn sẽ thấy các phần đã được cân bằng khác nhau, sẵn sàng để bước vào chu kỳ coinjoin. Ngay khi Tx0 được xác nhận, Ashigaru Terminal sẽ tự động bắt đầu chu kỳ trộn đầu tiên.



![Image](assets/fr/11.webp)



Sau khi Tx0 được xác nhận, giao dịch coinjoin đầu tiên sẽ được Ashigaru Terminal tạo và tự động phát sóng. Bằng cách vào `Tài khoản > Postmix > UTXOs`, bạn có thể xem các UTXO đã được cân bằng, đang chờ xác nhận chu kỳ đầu tiên.



![Image](assets/fr/12.webp)



Bây giờ bạn có thể để Ashigaru Terminal chạy ở chế độ nền: nó sẽ tiếp tục tự động trộn và phối lại các bản nhạc của bạn.



## Hoàn thiện coinjoin



Giờ đây, bạn có thể để tiền xu của mình tự động trộn lại. Mô hình Whirlpool đồng nghĩa với việc không có thêm bất kỳ khoản phí nào cho việc trộn lại: không phí dịch vụ, không phí mining. Vì vậy, việc để tiền xu của bạn tham gia vào nhiều chu kỳ trộn hơn chỉ có thể mang lại lợi ích cho tính bảo mật của bạn.



Để hiểu rõ hơn về cơ chế này và số chu kỳ cần chờ, tôi khuyên bạn nên đọc bài viết này:



https://planb.academy/tutorials/privacy/on-chain/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

Để xem số bản phối lại của từng tác phẩm, hãy mở menu `UTXOs` trong tài khoản `Postmix`.



![Image](assets/fr/13.webp)



Để sử dụng các đồng tiền hỗn hợp của bạn, hãy truy cập ứng dụng Ashigaru, ứng dụng này sử dụng cùng mã wallet với phần mềm Ashigaru Terminal của bạn. Mã wallet hiển thị khi mở ứng dụng tương ứng với tài khoản `Deposit` của bạn. Để truy cập tài khoản `Postmix`, nơi chứa các UTXO hỗn hợp của bạn, hãy nhấp vào biểu tượng Whirlpool ở góc trên bên phải.



![Image](assets/fr/14.webp)



Trong tài khoản này, bạn sẽ thấy tất cả số xu của mình hiện đang được trộn lẫn. Để chi tiêu, hãy nhấn biểu tượng `+` ở góc dưới bên phải màn hình, sau đó chọn `Gửi`.



![Image](assets/fr/15.webp)



Điền thông tin chi tiết về giao dịch của bạn: địa chỉ người nhận, số tiền cần gửi và nếu muốn, hãy chọn cấu trúc giao dịch cụ thể để tăng cường tính bảo mật hơn nữa (xem hướng dẫn tương ứng).



![Image](assets/fr/16.webp)



Kiểm tra kỹ thông tin giao dịch, sau đó kéo mũi tên ở cuối màn hình để xác nhận việc giao hàng.



![Image](assets/fr/17.webp)



Giao dịch của bạn đã được ký và phát trên mạng Bitcoin.



![Image](assets/fr/18.webp)



## Chi tiêu Doxxic Thay đổi



Lưu ý: Mô hình Whirlpool dựa trên việc cân bằng các quân cờ của bạn tại Tx0, trước khi chúng được đưa vào nhóm. Chính cơ chế này đã phá vỡ việc theo dõi UTXO. Theo tôi, đây là mô hình coinjoin hiệu quả nhất, nhưng nó có một nhược điểm: nó tạo ra một *thay đổi* không thông qua quá trình coinjoin.



Thay đổi này tương ứng với một UTXO được tạo cho mỗi Tx0. Nó được phân lập trong một tài khoản cụ thể có tên là `Doxxic Change` hoặc `Bad Bank`, tùy thuộc vào phần mềm, để tránh sử dụng với các UTXO khác của bạn. Điều này rất quan trọng, vì các UTXO này chưa được trộn lẫn: các liên kết truy xuất nguồn gốc của chúng vẫn còn nguyên vẹn, và chúng có thể làm ảnh hưởng đến tính bảo mật của bạn bằng cách thiết lập kết nối giữa bạn và hoạt động coinjoin của bạn. Vì vậy, hãy xử lý chúng một cách cẩn thận và **không bao giờ sử dụng chúng với các UTXO khác**, dù đã được trộn lẫn hay chưa. Việc kết hợp một UTXO độc hại với một UTXO hỗn hợp sẽ xóa sạch mọi lợi ích về quyền riêng tư mà bạn đã đạt được từ việc coinjoin.



Hiện tại, Ashigaru không cung cấp quyền truy cập trực tiếp vào tài khoản `Doxxic Change` này (ít nhất là tôi chưa tìm thấy). Tính năng này có thể sẽ được bổ sung trong bản cập nhật sắp tới. Trong thời gian chờ đợi, cách duy nhất để lấy lại số tiền này là nhập seed của bạn vào Sparrow Wallet. Wallet thường sẽ tự động phát hiện đây là wallet được sử dụng với Whirlpool và cấp cho bạn quyền truy cập vào cả bốn tài khoản, bao gồm cả tài khoản `Doxxic Change`. Sau đó, bạn có thể sử dụng các UTXO này như bitcoin thông thường từ Sparrow.



Sau đây là một số chiến lược khả thi để quản lý UTXO ngoại hối của bạn từ coinjoins mà không ảnh hưởng đến quyền riêng tư của bạn:





- Trộn chúng vào các nhóm nhỏ hơn:** Nếu UTXO độc hại của bạn đủ lớn để tham gia vào một nhóm nhỏ hơn, đây thường là lựa chọn tốt nhất. Tuy nhiên, hãy cẩn thận, đừng bao giờ gộp nhiều UTXO độc hại để thực hiện việc này, vì điều này sẽ tạo ra một liên kết giữa các mục nhập khác nhau của bạn trong Whirlpool.





- Đánh dấu chúng là không thể chi tiêu:** Một cách tiếp cận thận trọng khác là giữ chúng nguyên trạng trong tài khoản riêng và không động đến. Điều này sẽ ngăn bạn vô tình chi tiêu chúng. Nếu giá trị Bitcoin tăng, các nhóm mới phù hợp với quy mô của chúng có thể được mở ra.





- Quyên góp:** Bạn có thể chọn chuyển đổi các UTXO độc hại này thành khoản quyên góp cho các nhà phát triển Bitcoin, các dự án nguồn mở hoặc các hiệp hội chấp nhận BTC. Điều này cho phép bạn xử lý chúng một cách hữu ích đồng thời hỗ trợ hệ sinh thái.





- Mua thẻ quà tặng trả trước hoặc thẻ Visa:** Các nền tảng như [Bitrefill](https://www.bitrefill.com/) cho phép bạn đổi bitcoin lấy thẻ quà tặng hoặc thẻ Visa nạp lại có thể sử dụng tại các cửa hàng. Đây có thể là một cách đơn giản và kín đáo để tiêu UTXO độc hại của bạn.





- Đổi chúng lấy Monero:** Samourai Wallet từng cung cấp dịch vụ hoán đổi nguyên tử BTC/XMR hiện đã ngừng hoạt động. Nếu có dịch vụ tương tự (cá nhân tôi không biết dịch vụ nào), thì đó là một giải pháp tuyệt vời để cô lập các UTXO này, chuyển đổi chúng thành Monero, rồi cuối cùng gửi chúng trở lại Bitcoin. Tuy nhiên, phương pháp này tốn kém và phụ thuộc vào tính thanh khoản.





- Chuyển chúng sang Lightning Network:** Việc chuyển các UTXO này sang Lightning Network để được hưởng mức phí giao dịch thấp hơn là một lựa chọn tiềm năng. Tuy nhiên, phương pháp này có thể tiết lộ một số thông tin nhất định tùy thuộc vào cách bạn sử dụng Lightning, do đó cần thận trọng khi sử dụng.



## Làm sao tôi có thể biết được chất lượng chu kỳ coinjoin của chúng tôi?



Để một coinjoin thực sự hiệu quả, nó phải thể hiện mức độ đồng nhất cao giữa lượng đầu vào và đầu ra. Sự đồng nhất này làm tăng số lượng các cách diễn giải có thể có đối với người quan sát bên ngoài, từ đó làm tăng tính không chắc chắn về giao dịch. Để đo lường mức độ không chắc chắn này, chúng tôi sử dụng khái niệm entropy được áp dụng cho giao dịch. Mô hình Whirlpool được công nhận là một trong những mô hình hiệu quả nhất về mặt này, vì nó đảm bảo tính đồng nhất tuyệt vời giữa những người tham gia. Để tìm hiểu sâu hơn về nguyên tắc này, tôi khuyên bạn nên tham khảo chương cuối của Phần 5 trong khóa đào tạo BTC 204.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Hiệu suất của một số chu kỳ coinjoin được đo bằng kích thước của các tập hợp chứa đồng xu. Các tập hợp này định nghĩa cái được gọi là *anonsets*. Có hai loại: loại thứ nhất đo lường tính bảo mật khi đối mặt với phân tích hồi cứu (từ hiện tại về quá khứ), và loại thứ hai đo lường khả năng chống lại phân tích triển vọng (từ quá khứ về hiện tại). Để biết giải thích đầy đủ về hai chỉ số này, vui lòng đọc hướng dẫn sau (hoặc, một lần nữa, khóa đào tạo BTC 204):



https://planb.academy/tutorials/privacy/on-chain/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

## Làm thế nào để quản lý postmix?



Sau khi chạy một số chu kỳ coinjoin, chiến lược tốt nhất là giữ UTXO của bạn trong tài khoản `Postmix`, để chúng trộn lại vô thời hạn cho đến khi bạn thực sự cần chi tiêu chúng.



Một số người dùng thích chuyển số bitcoin hỗn hợp của họ sang wallet được bảo mật bằng phần cứng wallet. Tùy chọn này khả thi, nhưng đòi hỏi một mức độ nghiêm ngặt nhất định để đảm bảo tính bảo mật có được từ coinjoin không bị xâm phạm.



Việc hợp nhất UTXO là lỗi thường gặp nhất. Điều quan trọng là không bao giờ kết hợp các UTXO đã trộn lẫn với các UTXO chưa trộn lẫn trong cùng một giao dịch, nếu không bạn có nguy cơ kích hoạt *Phương pháp Đầu vào Chung Ownership (CIOH)*. Điều này ngụ ý việc quản lý chặt chẽ các UTXO của bạn, đặc biệt là thông qua việc gắn nhãn rõ ràng và chính xác. Nhìn chung, việc hợp nhất UTXO là một hành vi không tốt, thường dẫn đến mất tính bảo mật nếu quản lý kém.



https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Bạn cũng nên thận trọng khi hợp nhất các UTXO hỗn hợp. Có thể cân nhắc hợp nhất hạn chế nếu các UTXO có nhiều ẩn danh đáng kể, nhưng điều này chắc chắn sẽ làm giảm mức độ bảo mật của bạn. Tránh hợp nhất hàng loạt hoặc gấp rút, được thực hiện trước khi có đủ số lượng bản phối lại, vì chúng có thể thiết lập các liên kết suy luận giữa các bản phối lại trước và sau của bạn. Trong trường hợp nghi ngờ, tốt nhất không nên hợp nhất các UTXO hậu phối lại và chuyển từng cái một sang phần cứng wallet, tạo ra một địa chỉ nhận mới trống mỗi lần. Đừng quên gắn nhãn cho mỗi UTXO đã chuyển.



Chúng tôi đặc biệt khuyên bạn không nên chuyển UTXO postmix của mình sang danh mục đầu tư bằng các tập lệnh thiểu số. Ví dụ: nếu bạn tham gia Whirlpool từ danh mục đầu tư multi-sig trong `P2WSH`, sẽ có rất ít người chia sẻ loại tập lệnh này. Bằng cách gửi UTXO postmix của bạn đến cùng loại tập lệnh này, bạn sẽ giảm đáng kể tính ẩn danh của mình. Ngoài loại tập lệnh, các dấu vân tay wallet cụ thể khác có thể làm ảnh hưởng đến tính bảo mật của bạn, vì vậy tốt nhất nên sử dụng chúng từ ứng dụng Ashigaru.



Cuối cùng, như với tất cả các giao dịch Bitcoin, đừng bao giờ sử dụng lại địa chỉ nhận. Mỗi khoản thanh toán phải được gửi đến một địa chỉ mới, duy nhất và trống.



Phương pháp đơn giản và an toàn nhất là để các UTXO đã trộn của bạn nằm trong tài khoản `Postmix`, để chúng tự trộn lại và chỉ sử dụng chúng khi cần từ Ashigaru.



Ví Ashigaru và Sparrow tích hợp các biện pháp bảo vệ bổ sung chống lại các lỗi phổ biến nhất liên quan đến phân tích blockchain, giúp bạn bảo vệ tính bảo mật của các giao dịch.